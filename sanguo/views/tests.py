"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase, TransactionTestCase

from protomsg import (
        RESPONSE_NOTIFY_TYPE,
        PVERequest,
        PVEResponse,
        )
from apps.character.models import Character
from core.character import char_initialize
from utils import crypto
from utils import app_test_helper as tests


def teardown():
    from core.drives import redis_client, mongodb_client, mongodb_client_db
    redis_client.flushdb()
    mongodb_client.drop_database(mongodb_client_db)


class BattleTest(TransactionTestCase):
    def setUp(self):
        char = Character.objects.create(account_id=1, server_id=1)
        char_initialize(char.id)

    def test_pve(self):
        req = PVERequest()
        req.session = crypto.encrypt('1:1:1')
        req.stage_id = 1

        data = tests.pack_data(req)
        res = tests.make_request('/pve/', data)
        msgs = tests.unpack_data(res)

        for id_of_msg, len_of_msg, msg in msgs:
            if id_of_msg == RESPONSE_NOTIFY_TYPE["PVEResponse"]:
                data = PVEResponse()
                data.ParseFromString(msg)
                self.assertEqual(data.stage_id, 1)
