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

from huaweicloudsdkkvs.v1.config.kvs_sdk_config import KvsSdkConfig
from huaweicloudsdkkvs.v1.managed_kvs_client import ManagedKvsClient


def test_managed_kvs_client_init():
    kvs_sdk_config = KvsSdkConfig(os.path.dirname(__file__) + "/config/test-kvs-sdk.config", False)
    managed_kvs_client = ManagedKvsClient(kvs_sdk_config.load_endpoint_list()[0], kvs_sdk_config)

    assert managed_kvs_client.client is not None
    assert not managed_kvs_client.is_async_client
    assert managed_kvs_client.is_usable
    assert managed_kvs_client.endpoint.name == "endpoint1"
    assert managed_kvs_client.endpoint.weight == 1


def test_managed_kvs_async_client_init():
    kvs_sdk_config = KvsSdkConfig(os.path.dirname(__file__) + "/config/test-kvs-sdk.config", True)
    managed_kvs_client = ManagedKvsClient(kvs_sdk_config.load_endpoint_list()[0], kvs_sdk_config)

    assert managed_kvs_client.client is not None
    assert managed_kvs_client.is_async_client
    assert managed_kvs_client.is_usable
    assert managed_kvs_client.endpoint.name == "endpoint1"
    assert managed_kvs_client.endpoint.weight == 1
