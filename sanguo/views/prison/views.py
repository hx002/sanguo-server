# -*- coding: utf-8 -*-
import logging

from django.http import HttpResponse
from mongoengine import DoesNotExist

import protomsg
from callbacks import timers
from core.exception import SanguoViewException, InvalidOperate
from core.hero import save_hero
from core.mongoscheme import MongoPrison
from core.signals import prisoner_changed_signal, prisoner_del_signal
from protomsg import Prisoner as PrisonerProtoMsg
from timer.tasks import cancel_job, sched
from utils import pack_msg, timezone

from core.prison import Prison
from core.notify import prison_notify

logger = logging.getLogger('sanguo')


def open_slot(request):
    req = request._proto
    char_id = request._char_id

    p = Prison(char_id)
    p.open_slot()

    prison_notify(char_id, prison=p)

    response = protomsg.OpenTrainSlotResponse()
    response.ret = 0
    data = pack_msg(response)
    return HttpResponse(data, content_type='text/plain')


def train(request):
    req = request._proto
    char_id = request._char_id

    try:
        prison = MongoPrison.objects.get(id=char_id)
    except DoesNotExist:
        logger.warning("Train. Char {0} has NO prison".format(char_id))
        raise InvalidOperate("TrainResponse")

    prisoners = prison.prisoners
    if str(req.hero) not in prisoners:
        logger.warning("Train. Char {0} wanna train a NONE exist prisoner".format(char_id))
        raise InvalidOperate("TrainResponse")

    this_prisoner = prisoners[str(req.hero)]
    if this_prisoner.status != PrisonerProtoMsg.NOT:
        logger.warning("Train. Char {0} wanna train a prisoner who can NOT train. {1}".format(
            char_id, this_prisoner.status
        ))
        raise SanguoViewException(801, "TrainResponse")

    in_train_amount = 0
    for p in prisoners.values():
        if p.status == PrisonerProtoMsg.IN or p.status == PrisonerProtoMsg.FINISH:
            in_train_amount += 1

    # FIXME
    if in_train_amount >= 3:
        logger.warning("Train. Char {0} train amount full, Cannot train".format(char_id))
        raise SanguoViewException(802, "TrainResponse")



    # 如果以前处于NOT状态，那么还有一个NOT转变为OUT的job
    # 先将其取消
    # FIXME , countdown
    cancel_job(this_prisoner.jobid)
    job = sched.apply_async(
        (timers.prisoner_job, char_id, req.hero, PrisonerProtoMsg.IN),
        countdown=10
    )

    this_prisoner.status = PrisonerProtoMsg.IN
    this_prisoner.jobid = job.id

    prison.save()

    prisoner_changed_signal.send(
        sender=None,
        char_id=char_id,
        mongo_prisoner_obj=this_prisoner
    )

    logger.debug("Train. Char {0} start a training. {1}".format(
        char_id, req.hero
    ))

    response = protomsg.TrainResponse()
    response.ret = 0
    data = pack_msg(response)
    return HttpResponse(data, content_type='text/plain')


def get(request):
    req = request._proto
    char_id = request._char_id

    try:
        prison = MongoPrison.objects.get(id=char_id)
    except DoesNotExist:
        raise InvalidOperate("TrainResponse")

    prisoners = prison.prisoners
    if str(req.hero) not in prisoners:
        raise InvalidOperate("TrainResponse")

    this_prisoner = prisoners[str(req.hero)]
    if this_prisoner.status == PrisonerProtoMsg.IN:
        raise SanguoViewException(803, "TrainResponse")

    if this_prisoner.status == PrisonerProtoMsg.NOT:
        # 直接招降
        pass
    elif this_prisoner.status == PrisonerProtoMsg.IN:
        # 加速
        pass
    elif this_prisoner.status == PrisonerProtoMsg.OUT:
        # 直接招降
        pass
    else:
        # 已经完成
        pass

    # FIXME 扣除元宝
    # FIXME 检查武将包裹是否满了

    save_hero(char_id, this_prisoner.oid)
    cancel_job(this_prisoner.jobid)

    del prison.prisoners[str(req.hero)]
    prison.save()

    prisoner_del_signal.send(
        sender=None,
        char_id=char_id,
        prisoner_id=req.hero
    )

    response = protomsg.GetPrisonerResponse()
    response.ret = 0
    data = pack_msg(response)
    return HttpResponse(data, content_type='text/plain')