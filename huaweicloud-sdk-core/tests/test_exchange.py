# coding: utf-8
"""
 Copyright 2025 Huawei Technologies Co.,Ltd.

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

from huaweicloudsdkcore.exchange.api_reference import ApiReference
from huaweicloudsdkcore.exchange.exchange import SdkExchange, SdkExchangeCache


def test_sdk_exchange():
    ref = ApiReference()
    ref.uri = "uri"
    ref.name = "name"
    ref.method = "method"

    assert ref.uri == "uri"
    assert ref.name == "name"
    assert ref.method == "method"

    exchange = SdkExchange()
    exchange.api_reference = ref

    assert exchange.api_reference == ref

    _id = SdkExchangeCache.put(exchange)

    assert SdkExchangeCache.get("test") is None
    assert SdkExchangeCache.get(_id) is exchange

    SdkExchangeCache.remove(_id)
    assert SdkExchangeCache.get(_id) is None
