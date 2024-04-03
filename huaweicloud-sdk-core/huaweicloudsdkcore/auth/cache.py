# coding: utf-8
"""
 Copyright 2021 Huawei Technologies Co.,Ltd.

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


class AuthCache:

    _cache_dict = {}

    @classmethod
    def get_auth(cls, ak_with_name):
        return cls._cache_dict.get(ak_with_name) if ak_with_name else None

    @classmethod
    def put_auth(cls, ak_with_name, _id):
        cls._cache_dict[ak_with_name] = _id
