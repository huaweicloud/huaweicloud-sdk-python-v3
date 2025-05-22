# coding: utf-8
"""
 Copyright 2025 Huawei Technologies Co.,Ltd.

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
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkcore.signer.algorithm import SigningAlgorithm


def test_http_config():
    http_config = HttpConfig()
    http_config.proxy_protocol = "https"
    http_config.proxy_host = "proxy.com"
    http_config.proxy_port = 12345
    http_config.proxy_user = "user"
    http_config.proxy_password = "pass"
    http_config.ignore_ssl_verification = True
    http_config.allow_redirects = True
    http_config.ssl_ca_cert = "ssl_ca_cert"
    http_config.cert_file = "cert_file"
    http_config.key_file = "key_file"
    http_config.timeout = (10, 10)
    http_config.retry_times = 3
    http_config.pool_connections = 1
    http_config.pool_maxsize = 1
    http_config.signing_algorithm = SigningAlgorithm.HMAC_SHA256

    assert http_config.proxy_protocol == "https"
    assert http_config.proxy_host == "proxy.com"
    assert http_config.proxy_port == 12345
    assert http_config.proxy_user == "user"
    assert http_config.proxy_password == "pass"
    assert http_config.ignore_ssl_verification is True
    assert http_config.allow_redirects is True
    assert http_config.ssl_ca_cert == "ssl_ca_cert"
    assert http_config.cert_file == "cert_file"
    assert http_config.key_file == "key_file"
    assert http_config.timeout == (10, 10)
    assert http_config.retry_times == 3
    assert http_config.pool_connections == 1
    assert http_config.pool_maxsize == 1
    assert http_config.signing_algorithm == SigningAlgorithm.HMAC_SHA256
    assert http_config.get_proxy() == {'https': 'https://user:pass@proxy.com:12345'}