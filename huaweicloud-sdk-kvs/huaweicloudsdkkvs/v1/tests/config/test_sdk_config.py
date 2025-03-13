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

import pytest
from huaweicloudsdkcore.auth.credentials import BasicCredentials

from huaweicloudsdkkvs.v1.config.kvs_sdk_config import KvsSdkConfig


@pytest.fixture
def config():
    config = KvsSdkConfig(os.path.dirname(__file__) + "/test-kvs-sdk.config", False)
    yield config


def test_get_multichannel_sdk_config(config):
    assert config.heartbeat_interval == 1000
    assert config.heartbeat_thread_pool_size == 5
    assert config.reload_interval == 1
    assert config.api_retry_count == 3
    assert config.endpoint_name_list == ["endpoint1", "endpoint2", "endpoint3"]
    assert config.endpoint_weight_list == ["1", "3", "2"]


def test_get_verification_config(config):
    credentials = BasicCredentials(config.ak, config.sk, config.project_id).with_security_token(config.sts_token)

    assert credentials.ak == "testAk"
    assert credentials.sk == "testSk"
    assert credentials.security_token == "testStsToken"
    assert credentials.project_id == "testProjectId"
    assert config.ignore_ssl_verification
    assert config.ca_certificate_path == "ca.crt"


def test_get_union_sdk_config(config):
    assert config.region_id == "test_region_id"
    assert config.connection_timeout == 1000
    assert config.proxy_protocol == "http"
    assert config.proxy_host == "testHost"
    assert config.proxy_port == 80
    assert config.proxy_user == "testUser"
    assert config.proxy_password == "testPassword"
    assert config.file_log_path == "testLogFile"
    assert config.file_log_level == "INFO"
