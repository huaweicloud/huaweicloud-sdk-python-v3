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
from unittest.mock import patch

import pytest
from huaweicloudsdkcore.exceptions.exceptions import ConnectionException

from huaweicloudsdkkvs.v1 import KvsClient, CheckHealthResponse, CreateTableRequest, CreateTableResponse, \
    DescribeTableResponse, ListStoreResponse, DescribeTableRequest, ListStoreRequest, ListTableResponse, \
    ListTableRequest, BatchWriteKvResponse, BatchWriteKvRequest, DeleteKvResponse, DeleteKvRequest, GetKvResponse, \
    GetKvRequest, PutKvResponse, PutKvRequest, ScanKvResponse, ScanKvRequest, ScanSkeyKvResponse, ScanSkeyKvRequest, \
    UpdateKvResponse, UpdateKvRequest
from huaweicloudsdkkvs.v1.multichannel_kvs_client import MultichannelKvsClient


@pytest.fixture
def config():
    config = ConfigParser()
    config.read(os.path.dirname(__file__) + "/config/test-kvs-sdk.config", 'utf-8')
    yield config
    config['verification_config']['ak'] = "testAk"
    config['verification_config']['sk'] = "testSk"
    config['verification_config']['sts_token'] = "testStsToken"
    config['multichannel_sdk_config']['endpoint_names'] = "endpoint1,endpoint2,endpoint3"
    config['multichannel_sdk_config']['endpoint_weights'] = "1,3,2"
    with open(os.path.dirname(__file__) + "/config/test-kvs-sdk.config", 'w') as configfile:
        config.write(configfile)


def test_old_client_map_clean(config):
    response = CheckHealthResponse()
    with patch.object(KvsClient, 'check_health', return_value=response):
        multichannel_client = MultichannelKvsClient(os.path.dirname(__file__) + "/config/test-kvs-sdk.config")
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
        with open(os.path.dirname(__file__) + "/config/test-kvs-sdk.config", 'w') as configfile:
            config.write(configfile)

        count = 0
        while count < 60:
            time.sleep(1)
            print("old_kvs_client_maps size : " + str(multichannel_client.old_kvs_client_maps.size()))
            if multichannel_client.old_kvs_client_maps.size() == 0:
                break
            count += 1

        assert multichannel_client.old_kvs_client_maps.size() == 0


endpoint_invoke_counts = [0, 0, 0]


def mock_create_table(self, request):
    global endpoint_invoke_counts
    if "endpoint1" in self._endpoints[0]:
        endpoint_invoke_counts[0] += 1
    elif "endpoint2" in self._endpoints[0]:
        endpoint_invoke_counts[1] += 1
    elif "endpoint3" in self._endpoints[0]:
        endpoint_invoke_counts[2] += 1
    return CreateTableResponse()


def test_three_client_create_table_success(config):
    global endpoint_invoke_counts
    response = CheckHealthResponse()
    with patch.object(KvsClient, 'check_health', return_value=response):
        multichannel_client = MultichannelKvsClient(os.path.dirname(__file__) + "/config/test-kvs-sdk.config")
        with patch.object(KvsClient, 'create_table', new=mock_create_table):
            count = 0
            while count < 7:
                request = CreateTableRequest()
                multichannel_client.create_table(request)
                count += 1

    assert endpoint_invoke_counts[0] == 2
    assert endpoint_invoke_counts[1] == 3
    assert endpoint_invoke_counts[2] == 2
    endpoint_invoke_counts = [0, 0, 0]


def test_three_client_create_table_with_1_unusable(config):
    global endpoint_invoke_counts
    response = CheckHealthResponse()

    def mock_heath_check_with_1_unusable(self, request):
        if "endpoint1" in self._endpoints[0]:
            raise ConnectionException("Mocked error")
        return CreateTableResponse()

    with patch.object(KvsClient, 'check_health', new=mock_heath_check_with_1_unusable):
        multichannel_client = MultichannelKvsClient(os.path.dirname(__file__) + "/config/test-kvs-sdk.config")
        time.sleep(int(config['multichannel_sdk_config']['config_reload_interval']) * 2)
        with patch.object(KvsClient, 'create_table', new=mock_create_table):
            count = 0
            while count < 7:
                request = CreateTableRequest()
                multichannel_client.create_table(request)
                count += 1

    assert endpoint_invoke_counts[0] == 0
    assert endpoint_invoke_counts[1] == 5
    assert endpoint_invoke_counts[2] == 2
    endpoint_invoke_counts = [0, 0, 0]


def test_all_api(config):
    with patch.object(KvsClient, 'check_health', return_value=CheckHealthResponse()):
        multichannel_client = MultichannelKvsClient(os.path.dirname(__file__) + "/config/test-kvs-sdk.config")
        mocked_response = CreateTableResponse()
        with patch.object(KvsClient, 'create_table', return_value=mocked_response):
            response = multichannel_client.create_table(CreateTableRequest())
            assert response == mocked_response

        mocked_response = DescribeTableResponse()
        with patch.object(KvsClient, 'describe_table', return_value=mocked_response):
            response = multichannel_client.describe_table(DescribeTableRequest())
            assert response == mocked_response

        mocked_response = ListStoreResponse()
        with patch.object(KvsClient, 'list_store', return_value=mocked_response):
            response = multichannel_client.list_store(ListStoreRequest())
            assert response == mocked_response

        mocked_response = ListTableResponse()
        with patch.object(KvsClient, 'list_table', return_value=mocked_response):
            response = multichannel_client.list_table(ListTableRequest())
            assert response == mocked_response

        mocked_response = BatchWriteKvResponse()
        with patch.object(KvsClient, 'batch_write_kv', return_value=mocked_response):
            response = multichannel_client.batch_write_kv(BatchWriteKvRequest())
            assert response == mocked_response

        mocked_response = DeleteKvResponse()
        with patch.object(KvsClient, 'delete_kv', return_value=mocked_response):
            response = multichannel_client.delete_kv(DeleteKvRequest())
            assert response == mocked_response

        mocked_response = GetKvResponse()
        with patch.object(KvsClient, 'get_kv', return_value=mocked_response):
            response = multichannel_client.get_kv(GetKvRequest())
            assert response == mocked_response

        mocked_response = PutKvResponse()
        with patch.object(KvsClient, 'put_kv', return_value=mocked_response):
            response = multichannel_client.put_kv(PutKvRequest())
            assert response == mocked_response

        mocked_response = ScanKvResponse()
        with patch.object(KvsClient, 'scan_kv', return_value=mocked_response):
            response = multichannel_client.scan_kv(ScanKvRequest())
            assert response == mocked_response

        mocked_response = ScanSkeyKvResponse()
        with patch.object(KvsClient, 'scan_skey_kv', return_value=mocked_response):
            response = multichannel_client.scan_skey_kv(ScanSkeyKvRequest())
            assert response == mocked_response

        mocked_response = UpdateKvResponse()
        with patch.object(KvsClient, 'update_kv', return_value=mocked_response):
            response = multichannel_client.update_kv(UpdateKvRequest())
            assert response == mocked_response
