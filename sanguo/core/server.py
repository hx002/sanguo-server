# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-6-16'

from django.conf import settings
from libs.functional import get_ipv4_address

class _Server(object):
    __slots__ = ['id', 'name', 'host', 'port', 'port_https', 'active']
    def __init__(self):
        self.id = settings.SERVER_ID
        self.name = settings.SERVER_NAME
        self.host = get_ipv4_address(interface=settings.SERVER_INTERFACE)
        self.port = settings.LISTEN_PORT_HTTP
        self.port_https = settings.LISTEN_PORT_HTTPS
        self.active = True

server = _Server()
