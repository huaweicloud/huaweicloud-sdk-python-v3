# coding= utf-8
"""
 Copyright 2023 Huawei Technologies Co.,Ltd.

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

try:
    from enum import Enum

    _ENUM_CLS = Enum
except ImportError:
    _ENUM_CLS = object


class SigningAlgorithm(_ENUM_CLS):
    HMAC_SHA256 = 1
    HMAC_SM3 = 2
    ECDSA_P256_SHA256 = 3
    SM2_SM3 = 4

    @classmethod
    def get_default(cls):
        return cls.HMAC_SHA256
