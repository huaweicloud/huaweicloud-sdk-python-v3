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

import pytest

from huaweicloudsdkcore.auth.credentials import BasicCredentials, GlobalCredentials
from huaweicloudsdkcore.exceptions.exceptions import ApiValueError


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


def test_basic_credentials_without_project_id():
    credentials = BasicCredentials().with_idp_id("idp_id").with_id_token_file("file")
    try:
        credentials.process_auth_params(None, None)
    except ApiValueError as e:
        assert "project_id is required when using idp_id & id_token_file" == str(e)


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


def test_global_credentials_without_domain_id():
    credentials = GlobalCredentials().with_idp_id("idp_id").with_id_token_file("file")
    try:
        credentials.process_auth_params(None, None)
    except ApiValueError as e:
        assert "domain_id is required when using idp_id & id_token_file" == str(e)


if __name__ == '__main__':
    pytest.main()
