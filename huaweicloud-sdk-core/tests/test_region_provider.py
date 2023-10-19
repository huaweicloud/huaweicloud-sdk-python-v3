# coding= utf-8
"""
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache LICENSE, Version 2.0 (the
 "LICENSE"); you may not use this file except in compliance
 with the LICENSE.  You may obtain a copy of the LICENSE at

     http=//www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the LICENSE is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the LICENSE for the
 specific language governing permissions and limitations
 under the LICENSE.
"""

import os

import pytest

from huaweicloudsdkcore.region.cache import EnvRegionCache, ProfileRegionCache
from huaweicloudsdkcore.region.provider import EnvRegionProvider, ProfileRegionProvider, RegionProviderChain


@pytest.fixture(scope="module")
def set_region_file_env():
    path = os.path.abspath("data/regions.yaml")
    os.environ["HUAWEICLOUD_SDK_REGIONS_FILE"] = path

    yield

    os.unsetenv("HUAWEICLOUD_SDK_REGIONS_FILE")


def test_env_region_provider():
    # test singleton
    assert EnvRegionCache() is EnvRegionCache()
    # test not found
    provider = EnvRegionProvider("Service1")
    assert provider.get_region("not-exist-1") is None
    # test found
    env_name = "HUAWEICLOUD_SDK_REGION_SERVICE1_REGION_ID_1"
    os.environ[env_name] = "https://service1.region-id-1.com"
    actual_region = provider.get_region("region-id-1")
    assert actual_region
    assert "region-id-1" == actual_region.id
    assert ["https://service1.region-id-1.com"] == actual_region.endpoints


def test_env_region_provider2():
    provider = EnvRegionProvider("Service2")
    env_name = "HUAWEICLOUD_SDK_REGION_SERVICE2_REGION_ID_2"
    os.environ[env_name] = "https://service2.region-id-2.com,https://service3.region-id-3.com"
    actual_region = provider.get_region("region-id-2")
    assert actual_region
    assert "region-id-2" == actual_region.id
    assert ["https://service2.region-id-2.com", "https://service3.region-id-3.com"] == actual_region.endpoints


def test_profile_region_provider(set_region_file_env):
    # test singleton
    assert ProfileRegionCache() is ProfileRegionCache()
    provider = ProfileRegionProvider("Service1")
    # test found
    actual_region = provider.get_region("region-id-1")
    assert actual_region
    assert "region-id-1" == actual_region.id
    assert ["https://service1.region-id-1.com"] == actual_region.endpoints
    # test not found
    region = provider.get_region("not-exist-1")
    assert region is None


def test_profile_region_provider2(set_region_file_env):
    provider = ProfileRegionProvider("Service2")
    actual_region = provider.get_region("region-id-2")
    assert actual_region
    assert "region-id-2" == actual_region.id
    assert ["https://service2.region-id-2.com", "https://service2.region-id-2.cn"] == actual_region.endpoints


def test_region_provider_chain(set_region_file_env):
    chain = RegionProviderChain.get_default_region_provider_chain("Service1")
    # test not found
    assert chain.get_region("not-exist-1") is None
    # test found
    actual_region = chain.get_region("region-id-1")
    assert actual_region
    assert "region-id-1" == actual_region.id
    assert ["https://service1.region-id-1.com"] == actual_region.endpoints


if __name__ == '__main__':
    pytest.main()
