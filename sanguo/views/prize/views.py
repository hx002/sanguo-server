from django.http import HttpResponse
from core.mongoscheme import Hang

from core.exception import SanguoViewException
from core.notify import hang_notify
from core.stage import get_stage_hang_drop, save_drop

from mongoengine import DoesNotExist

import protomsg

from utils import pack_msg


def prize_get(request):
    req = request._proto
    char_id = request._char_id

    prize_id = req.prize_id

    # XXX only support 1 now
    prize_id = 1

    try:
        hang = Hang.objects.get(id=char_id)
    except DoesNotExist:
        hang = None

    if hang is None or not hang.finished:
        raise SanguoViewException(703, "PrizeResponse")

    exp, gold, equips, gems = get_stage_hang_drop(hang.stage_id, hang.actual_hours)
    save_drop(char_id, exp, gold, equips, gems)

    hang.delete()

    hang_notify(char_id)

    response = protomsg.PrizeResponse()
    response.ret = 0
    response.prize_id = 1
    response.drop.gold = gold
    response.drop.exp = exp
    response.drop.equips.extend([i for i, _, _ in equips])
    response.drop.gems.extend([i for i, _ in gems])

    data = pack_msg(response)
    return HttpResponse(data, content_type='text/plain')