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
import logging
import os
import time
from unittest.mock import patch

import pytest
from huaweicloudsdkcore.exceptions.exceptions import ConnectionException

from huaweicloudsdkkvs.v1 import KvsClient, CheckHealthResponse, KvsAsyncClient
from huaweicloudsdkkvs.v1.config.kvs_sdk_config_manager import KvsSdkConfigManager
from huaweicloudsdkkvs.v1.kvs_client_heartbeat_keeper import KvsClientHeartbeatKeeper
from huaweicloudsdkkvs.v1.util.thread_safe_utils import ThreadSafeDict


@pytest.fixture
def logger():
    logger_name = 'KVS-multichannel-async-SDK'
    logger = logging.getLogger(logger_name)
    logger.propagate = False
    yield logger


def test_heartbeat_keeper_all_success(logger):
    response = CheckHealthResponse()
    kvs_client_map = ThreadSafeDict()
    old_kvs_client_maps = ThreadSafeDict()
    config_manager = KvsSdkConfigManager(os.path.dirname(__file__) + "/config/test-kvs-sdk.config", False,
                                         kvs_client_map, old_kvs_client_maps)
    with patch.object(KvsClient, 'check_health', return_value=response):
        heartbeat_keeper = KvsClientHeartbeatKeeper(kvs_client_map, config_manager.kvs_sdk_config.heartbeat_interval,
                                                    config_manager.kvs_sdk_config.heartbeat_thread_pool_size, logger)

        time.sleep(config_manager.kvs_sdk_config.heartbeat_interval * 2 / 1000.0)
        assert kvs_client_map.size() == 3
        assert not kvs_client_map.get(1).is_async_client
        for index in kvs_client_map.keys():
            assert kvs_client_map.get(index).is_usable


def test_heartbeat_keeper_async_all_success(logger):
    response = CheckHealthResponse()
    kvs_async_client_map = ThreadSafeDict()
    old_kvs_client_maps = ThreadSafeDict()
    config_manager = KvsSdkConfigManager(os.path.dirname(__file__) + "/config/test-kvs-sdk.config", True,
                                         kvs_async_client_map, old_kvs_client_maps)
    with patch.object(KvsAsyncClient, 'check_health_async', return_value=response):
        heartbeat_keeper = KvsClientHeartbeatKeeper(kvs_async_client_map,
                                                    config_manager.kvs_sdk_config.heartbeat_interval,
                                                    config_manager.kvs_sdk_config.heartbeat_thread_pool_size, logger)

    time.sleep(config_manager.kvs_sdk_config.heartbeat_interval * 2 / 1000.0)
    assert kvs_async_client_map.size() == 3
    assert kvs_async_client_map.get(1).is_async_client
    for index in kvs_async_client_map.keys():
        assert kvs_async_client_map.get(index).is_usable


def test_heartbeat_keeper_all_failed(logger):
    kvs_client_map = ThreadSafeDict()
    old_kvs_client_maps = ThreadSafeDict()
    config_manager = KvsSdkConfigManager(os.path.dirname(__file__) + "/config/test-kvs-sdk.config", False,
                                         kvs_client_map, old_kvs_client_maps)
    with patch.object(KvsClient, 'check_health', side_effect=ConnectionException("Mocked error")):
        heartbeat_keeper = KvsClientHeartbeatKeeper(kvs_client_map,
                                                    config_manager.kvs_sdk_config.heartbeat_interval,
                                                    config_manager.kvs_sdk_config.heartbeat_thread_pool_size,
                                                    logger)

        count = 0
        while count < 60:
            if not kvs_client_map.get(1).is_usable and not kvs_client_map.get(2).is_usable and not kvs_client_map.get(
                    3).is_usable:
                break
            count += 1
            time.sleep(1)
        assert kvs_client_map.size() == 3
        assert not kvs_client_map.get(1).is_async_client
        for index in kvs_client_map.keys():
            assert not kvs_client_map.get(index).is_usable


def test_heartbeat_keeper_async_all_failed(logger):
    response = CheckHealthResponse()
    kvs_async_client_map = ThreadSafeDict()
    old_kvs_client_maps = ThreadSafeDict()
    config_manager = KvsSdkConfigManager(os.path.dirname(__file__) + "/config/test-kvs-sdk.config", True,
                                         kvs_async_client_map, old_kvs_client_maps)
    with patch.object(KvsAsyncClient, 'check_health_async', side_effect=ConnectionException("Mocked error")):
        heartbeat_keeper = KvsClientHeartbeatKeeper(kvs_async_client_map,
                                                    config_manager.kvs_sdk_config.heartbeat_interval,
                                                    config_manager.kvs_sdk_config.heartbeat_thread_pool_size,
                                                    logger)
        count = 0
        while count < 60:
            if not kvs_async_client_map.get(1).is_usable and not kvs_async_client_map.get(
                    2).is_usable and not kvs_async_client_map.get(3).is_usable:
                break
            count += 1
            time.sleep(1)
        assert kvs_async_client_map.size() == 3
        assert kvs_async_client_map.get(1).is_async_client
        for index in kvs_async_client_map.keys():
            assert not kvs_async_client_map.get(index).is_usable
