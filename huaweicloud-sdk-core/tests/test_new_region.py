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

import pytest
from huaweicloudsdkcore.region.region import Region


def test_new_region1():
    region = Region(id="id", endpoint="endpoint1")
    assert region.id == "id"
    assert region.endpoints == ["endpoint1"]


def test_new_region2():
    region = Region("id", "endpoint1", "endpoint2")
    assert region.id == "id"
    assert region.endpoints == ["endpoint1", "endpoint2"]


def test_new_region3():
    region = Region("id", "endpoint1", "endpoint2", id="specified_id", endpoint="specified_endpoint")
    assert region.id == "specified_id"
    assert region.endpoints == ["specified_endpoint"]


if __name__ == '__main__':
    pytest.main()
