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

import logging
import os
from logging import StreamHandler
from logging.handlers import RotatingFileHandler

import pytest

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.http.http_client import HttpClient
from huaweicloudsdkcore.http.http_config import HttpConfig

ak = "my ak"
sk = "my sk"
endpoint = "my endpoint"
project_id = "my project_id"
logger_name = 'HuaweiCloud-SDK-Client'
config = HttpConfig.get_default_config()
config.ignore_ssl_verification = True
credentials = BasicCredentials(ak, sk, project_id)


def test_build_client_by_client_builder():
    client = ClientBuilder(Client) \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_endpoint(endpoint) \
        .build()

    assert isinstance(client, Client)
    assert client.get_agent() == {"User-Agent": "huaweicloud-usdk-python/3.0"}
    assert client.get_credentials().ak == "my ak"
    assert client.get_credentials().sk == "my sk"

    assert isinstance(client.get_http_client(), HttpClient)
    assert client.get_http_client()._timeout == (3, 10)
    assert client.get_http_client()._verify is False


def test_default_sdk_logger():
    ClientBuilder(Client) \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_endpoint(endpoint) \
        .build()

    logger = logging.getLogger(logger_name)
    assert logger.propagate is False
    assert len(logger.handlers) == 0


def test_add_rotating_file_handler_to_sdk_logger():
    ClientBuilder(Client) \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_file_log(path="tests.log", log_level=logging.DEBUG, max_bytes=1024, backup_count=1) \
        .with_endpoint(endpoint) \
        .build()

    logger = logging.getLogger(logger_name)
    assert len(logger.handlers) == 1
    assert isinstance(logger.handlers[0], RotatingFileHandler)
    assert logger.handlers[0].baseFilename.endswith("tests.log")
    assert logger.handlers[0].maxBytes == 1024
    assert logger.handlers[0].backupCount == 1

    logger.removeHandler(logger.handlers[0])
    os.remove("tests.log")


def test_add_stream_handler_to_sdk_logger():
    ClientBuilder(Client) \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_endpoint(endpoint) \
        .with_stream_log(log_level=logging.DEBUG) \
        .build()

    logger = logging.getLogger(logger_name)
    assert len(logger.handlers) == 1
    assert isinstance(logger.handlers[0], StreamHandler)

    logger.removeHandler(logger.handlers[0])


if __name__ == "__main__":
    pytest.main()
