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
import os
import time
from configparser import ConfigParser

import pytest

from huaweicloudsdkkvs.v1.config.kvs_sdk_config_manager import KvsSdkConfigManager
from huaweicloudsdkkvs.v1.util.thread_safe_utils import ThreadSafeDict


@pytest.fixture
def kvs_client_map():
    kvs_client_map = ThreadSafeDict()
    old_kvs_client_maps = ThreadSafeDict()
    config_manager = KvsSdkConfigManager(os.path.dirname(__file__) + "/test-kvs-sdk.config", False, kvs_client_map,
                                         old_kvs_client_maps)
    yield kvs_client_map


@pytest.fixture
def config():
    config = ConfigParser()
    config.read(os.path.dirname(__file__) + "/test-kvs-sdk.config", 'utf-8')
    yield config
    config['verification_config']['ak'] = "testAk"
    config['verification_config']['sk'] = "testSk"
    config['verification_config']['sts_token'] = "testStsToken"
    config['multichannel_sdk_config']['endpoint_names'] = "endpoint1,endpoint2,endpoint3"
    config['multichannel_sdk_config']['endpoint_weights'] = "1,3,2"
    with open(os.path.dirname(__file__) + "/test-kvs-sdk.config", 'w') as configfile:
        config.write(configfile)


def test_reload_endpoint_insert(kvs_client_map, config):
    new_endpoint_names = "endpoint1,endpoint2,endpoint3,endpoint4"
    new_endpoint_weights = "1,3,2,1"
    config['multichannel_sdk_config']['endpoint_names'] = new_endpoint_names
    config['multichannel_sdk_config']['endpoint_weights'] = new_endpoint_weights
    with open(os.path.dirname(__file__) + "/test-kvs-sdk.config", 'w') as configfile:
        config.write(configfile)
    count = 0
    while count < 60:
        if kvs_client_map.size() == 4:
            break
        count += 1
        time.sleep(1)
    assert kvs_client_map.size() == 4


def test_reload_endpoint_remove(kvs_client_map, config):
    new_endpoint_names = "endpoint1,endpoint2"
    new_endpoint_weights = "1,3"
    config['multichannel_sdk_config']['endpoint_names'] = new_endpoint_names
    config['multichannel_sdk_config']['endpoint_weights'] = new_endpoint_weights
    with open(os.path.dirname(__file__) + "/test-kvs-sdk.config", 'w') as configfile:
        config.write(configfile)
    count = 0
    while count < 60:
        if kvs_client_map.size() == 3:
            break
        count += 1
        time.sleep(1)
    assert kvs_client_map.size() == 3


def test_reload_aksk_and_endpoint_insert(kvs_client_map, config):
    new_ak = "testAk2"
    new_sk = "testSk2"
    new_sts_token = "testStsToken2"
    new_endpoint_names = "endpoint1,endpoint2,endpoint3,endpoint4"
    new_endpoint_weights = "1,3,2,1"
    config['verification_config']['ak'] = new_ak
    config['verification_config']['sk'] = new_sk
    config['verification_config']['sts_token'] = new_sts_token
    config['multichannel_sdk_config']['endpoint_names'] = new_endpoint_names
    config['multichannel_sdk_config']['endpoint_weights'] = new_endpoint_weights
    with open(os.path.dirname(__file__) + "/test-kvs-sdk.config", 'w') as configfile:
        config.write(configfile)
    count = 0
    while count < 60:
        if kvs_client_map.size() == 4:
            break
        count += 1
        time.sleep(1)
    assert kvs_client_map.size() == 4
    assert kvs_client_map.get(1).credential.ak == new_ak
    assert kvs_client_map.get(1).credential.sk == new_sk
    assert kvs_client_map.get(1).credential.sts_token == new_sts_token
