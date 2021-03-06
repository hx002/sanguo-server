# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '2/20/14'

from _base import Logger

import traceback
import json
from core.mongoscheme import MongoPurchaseRecord
from core.purchase import PurchaseAction, YuekaLockTimeOut
from core.attachment import make_standard_drop_from_template
from core.mail import Mail

from preset.settings import MAIL_YUEKA_CONTENT_TEMPLATE, MAIL_YUEKA_TITLE

def send_yueka_reward(char_id, sycee, remained_days):
    standard_drop = make_standard_drop_from_template()
    standard_drop['sycee'] = sycee

    content = MAIL_YUEKA_CONTENT_TEMPLATE.format(sycee, remained_days)

    Mail(char_id).add(MAIL_YUEKA_TITLE, content, attachment=json.dumps(standard_drop), only_one=True)


def set_yueka():
    records = MongoPurchaseRecord.objects.all()
    logger = Logger('set_yueka.log')
    logger.write("start")

    for record in records:
        if record.yueka_remained_days > 0:
            # 发送奖励，并且days-1
            send_yueka_reward(record.id, record.yueka_sycee, record.yueka_remained_days-1)

            pa = PurchaseAction(record.id)
            try:
                pa.set_yueka_remained_days(-1)
            except YuekaLockTimeOut:
                logger.write(traceback.format_exc())

    logger.write("finish")
    logger.close()

if __name__ == '__main__':
    set_yueka()
