# coding: utf-8
"""
 Copyright 2024 Huawei Technologies Co.,Ltd.

 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache LICENSE, Version 2.0 (the
 "LICENSE"); you may not use this file except in compliance
 with the LICENSE.  You may obtain a copy of the LICENSE at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the LICENSE is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the LICENSE for the
 specific language governing permissions and limitations
 under the LICENSE.
"""


class SdkExchange(object):
    def __init__(self):
        self._api_reference = None

    @property
    def api_reference(self):
        return self._api_reference

    @api_reference.setter
    def api_reference(self, value):
        self._api_reference = value


class SdkExchangeCache:
    _CACHE = {}

    @classmethod
    def put(cls, exchange):
        # type: (SdkExchange) -> str
        hash_code = str(hash(exchange))
        cls._CACHE[hash_code] = exchange
        return hash_code

    @classmethod
    def get(cls, hash_code):
        return cls._CACHE.get(hash_code)

    @classmethod
    def remove(cls, hash_code):
        if hash_code in cls._CACHE:
            del cls._CACHE[hash_code]
