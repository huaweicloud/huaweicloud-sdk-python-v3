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

import pytest
from huaweicloudsdkcore.http.http_config import HttpConfig

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.client import Client
from huaweicloudsdkcore.sdk_stream_response import SdkStreamResponse
from tests.data.file_response_mocker import mocked_file_response, mocked_file


def process_stream(stream):
    line_size = 0
    for line in stream.iter_lines(decode_unicode=True):
        if line:
            line_size += 1
    assert line_size == 2


def test_upload_download(mocker):
    client = Client()\
        .with_credentials(BasicCredentials("ak", "sk", "project_id"))\
        .with_endpoint("mock://test.com")\
        .with_config(HttpConfig.get_default_config())
    client.init_http_client()

    mocker.patch.object(client, '_is_stream', return_value=True)
    mocker.patch.object(client, '_do_http_request_sync', return_value=mocked_file_response())
    mocker.patch.object(client, 'deserialize', return_value=SdkStreamResponse(mocked_file_response()))

    response = client.do_http_request(method="POST", resource_path="/",
                                      header_params={"Content-Type": "application/octet-stream"}, body=mocked_file(),
                                      response_type="SdkStreamResponse")

    response.consume_download_stream(process_stream)


if __name__ == "__main__":
    pytest.main()
