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
import os.path

import pytest
import responses

from huaweicloudsdkcore.auth.credentials import BasicCredentials, GlobalCredentials
from huaweicloudsdkcore.auth.internal import IamHelper
from huaweicloudsdkcore.exceptions.exception_handler import DefaultExceptionHandler
from huaweicloudsdkcore.exceptions.exceptions import ApiValueError
from huaweicloudsdkcore.http.http_client import HttpClient
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkcore.http.http_handler import HttpHandler
from tests.util.response_registry import OrderedRegistry


def test_basic_credentials():
    credentials = BasicCredentials().with_idp_id("idp_id").with_id_token_file("file").with_project_id("project_id")
    credentials.process_auth_params(None, None)


def test_basic_credentials_without_idp_id():
    credentials = BasicCredentials().with_id_token_file("file")
    try:
        credentials.process_auth_params(None, None)
    except ApiValueError as e:
        assert "idp_id is required when using idp_id & id_token_file" == str(e)


def test_basic_credentials_without_id_token_file():
    credentials = BasicCredentials().with_idp_id("idp_id")
    try:
        credentials.process_auth_params(None, None)
    except ApiValueError as e:
        assert "id_token_file is required when using idp_id & id_token_file" == str(e)


def test_global_credentials():
    credentials = GlobalCredentials().with_idp_id("idp_id").with_id_token_file("file").with_domain_id("domain_id")
    credentials.process_auth_params(None, None)


def test_global_credentials_without_idp_id():
    credentials = GlobalCredentials().with_id_token_file("file")
    try:
        credentials.process_auth_params(None, None)
    except ApiValueError as e:
        assert "idp_id is required when using idp_id & id_token_file" == str(e)


def test_global_credentials_without_id_token_file():
    credentials = GlobalCredentials().with_idp_id("idp_id")
    try:
        credentials.process_auth_params(None, None)
    except ApiValueError as e:
        assert "id_token_file is required when using idp_id & id_token_file" == str(e)


@responses.activate(registry=OrderedRegistry)
def test_federal_credentials():
    responses.add(
        method=responses.POST,
        url=IamHelper.get_iam_endpoint() + "/v3.0/OS-AUTH/id-token/tokens",
        adding_headers={
            "Content-Type": "application/json",
            "X-IAM-Trace-Id": "trace-id",
            "X-Subject-Token": "auth-token"
        },
        body="{\"token\":{\"expires_at\":\"2018-03-13T03:00:01.168000Z\",\"methods\":[\"mapped\"]}}",
        status=200,
        match=[responses.matchers.header_matcher({"X-Idp-Id": "idp_id"})]
    )
    responses.add(
        method=responses.POST,
        url=IamHelper.get_iam_endpoint() + "/v3.0/OS-CREDENTIAL/securitytokens",
        adding_headers={
            "Content-Type": "application/json",
            "X-IAM-Trace-Id": "trace-id"
        },
        body="{\"credential\":{\"access\":\"ak\"," +
             "\"expires_at\":\"2020-01-08T03:50:07.574000Z\"," +
             "\"secret\":\"sk\"," +
             "\"securitytoken\":\"sec-token\"}}",
        status=200,
        match=[responses.matchers.json_params_matcher(
            {"auth": {"identity": {"methods": ["token"], "token": {"id": "auth-token", "duration_seconds": 21600}}}})]
    )

    file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data", "test_token.txt")
    cred = BasicCredentials().with_idp_id("idp_id").with_id_token_file(file)
    http_client = HttpClient(HttpConfig.get_default_config(), HttpHandler(), DefaultExceptionHandler(),
                             logging.getLogger("test_federal"))
    assert getattr(cred, "_need_update_federal_auth_token")()
    getattr(cred, "_update_auth_token_by_id_token")(http_client)

    assert cred.ak == "ak"
    assert cred.sk == "sk"
    assert cred.security_token == "sec-token"


if __name__ == '__main__':
    pytest.main()
