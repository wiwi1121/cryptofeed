'''
Copyright (C) 2017-2021  Bryant Moscon - bmoscon@gmail.com

Please see the LICENSE file for the terms and conditions
associated with this software.
'''
import logging

from cryptofeed.connection import RestEndpoint, WebsocketEndpoint, Routes
from cryptofeed.defines import BINANCE_US
from cryptofeed.exchanges.binance import Binance
from cryptofeed.exchanges.mixins.binance_rest import BinanceUSRestMixin


LOG = logging.getLogger('feedhandler')


class BinanceUS(Binance, BinanceUSRestMixin):
    id = BINANCE_US
    websocket_endpoints = [WebsocketEndpoint('wss://stream.binance.us:9443')]
    rest_endpoints = [RestEndpoint('https://api.binance.us', routes=Routes('/api/v3/exchangeInfo'))]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # overwrite values previously set by the super class Binance
        self.rest_endpoint = 'https://api.binance.us/api/v3'
        self.address = self._address()
