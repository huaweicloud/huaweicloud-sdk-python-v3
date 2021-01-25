# coding: utf-8
"""
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
import types

from huaweicloudsdkcore.region.region import Region
from tests.data.project_response_mocker import MOCK_ENDPOINT


class ServiceRegion:
    def __init__(self):
        pass

    CN_NORTH_7 = Region(id="cn-north-7", endpoint=MOCK_ENDPOINT)

    static_fields = types.MappingProxyType({
        "cn-north-7": CN_NORTH_7,
    })

    @staticmethod
    def value_of(region_id, static_fields=static_fields):
        if region_id is None or len(region_id) == 0:
            raise KeyError("Unexpected empty parameter: regionId.")
        if not static_fields.get(region_id):
            raise KeyError("Unexpected regionId: " + region_id)
        return static_fields.get(region_id)
