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
from unittest.mock import patch

from huaweicloudsdkkvs.v1 import CheckHealthResponse, CreateTableRequest, CreateTableResponse, \
    DescribeTableResponse, ListStoreResponse, DescribeTableRequest, ListStoreRequest, ListTableResponse, \
    ListTableRequest, BatchWriteKvResponse, BatchWriteKvRequest, DeleteKvResponse, DeleteKvRequest, GetKvResponse, \
    GetKvRequest, PutKvResponse, PutKvRequest, ScanKvResponse, ScanKvRequest, ScanSkeyKvResponse, ScanSkeyKvRequest, \
    UpdateKvResponse, UpdateKvRequest, KvsAsyncClient
from huaweicloudsdkkvs.v1.multichannel_kvs_async_client import MultichannelKvsAsyncClient


def test_all_async_api():
    with patch.object(KvsAsyncClient, 'check_health_async', return_value=CheckHealthResponse()):
        multichannel_async_client = MultichannelKvsAsyncClient(
            os.path.dirname(__file__) + "/config/test-kvs-sdk.config")
        mocked_response = CreateTableResponse()
        with patch.object(KvsAsyncClient, 'create_table_async', return_value=mocked_response):
            response = multichannel_async_client.create_table_async(CreateTableRequest())
            assert response == mocked_response

        mocked_response = DescribeTableResponse()
        with patch.object(KvsAsyncClient, 'describe_table_async', return_value=mocked_response):
            response = multichannel_async_client.describe_table_async(DescribeTableRequest())
            assert response == mocked_response

        mocked_response = ListStoreResponse()
        with patch.object(KvsAsyncClient, 'list_store_async', return_value=mocked_response):
            response = multichannel_async_client.list_store_async(ListStoreRequest())
            assert response == mocked_response

        mocked_response = ListTableResponse()
        with patch.object(KvsAsyncClient, 'list_table_async', return_value=mocked_response):
            response = multichannel_async_client.list_table_async(ListTableRequest())
            assert response == mocked_response

        mocked_response = BatchWriteKvResponse()
        with patch.object(KvsAsyncClient, 'batch_write_kv_async', return_value=mocked_response):
            response = multichannel_async_client.batch_write_kv_async(BatchWriteKvRequest())
            assert response == mocked_response

        mocked_response = DeleteKvResponse()
        with patch.object(KvsAsyncClient, 'delete_kv_async', return_value=mocked_response):
            response = multichannel_async_client.delete_kv_async(DeleteKvRequest())
            assert response == mocked_response

        mocked_response = GetKvResponse()
        with patch.object(KvsAsyncClient, 'get_kv_async', return_value=mocked_response):
            response = multichannel_async_client.get_kv_async(GetKvRequest())
            assert response == mocked_response

        mocked_response = PutKvResponse()
        with patch.object(KvsAsyncClient, 'put_kv_async', return_value=mocked_response):
            response = multichannel_async_client.put_kv_async(PutKvRequest())
            assert response == mocked_response

        mocked_response = ScanKvResponse()
        with patch.object(KvsAsyncClient, 'scan_kv_async', return_value=mocked_response):
            response = multichannel_async_client.scan_kv_async(ScanKvRequest())
            assert response == mocked_response

        mocked_response = ScanSkeyKvResponse()
        with patch.object(KvsAsyncClient, 'scan_skey_kv_async', return_value=mocked_response):
            response = multichannel_async_client.scan_skey_kv_async(ScanSkeyKvRequest())
            assert response == mocked_response

        mocked_response = UpdateKvResponse()
        with patch.object(KvsAsyncClient, 'update_kv_async', return_value=mocked_response):
            response = multichannel_async_client.update_kv_async(UpdateKvRequest())
            assert response == mocked_response
