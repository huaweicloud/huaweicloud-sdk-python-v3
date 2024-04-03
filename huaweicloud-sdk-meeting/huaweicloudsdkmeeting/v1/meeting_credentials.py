# coding: utf-8
"""
 Copyright 2020 Huawei Technologies Co.,Ltd.

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

import base64
import datetime
import json
import time

import six
import uuid
from hashlib import sha256
import hmac

from huaweicloudsdkcore.auth.credentials import Credentials
from huaweicloudsdkcore.exceptions.exceptions import SdkException, ApiValueError
from huaweicloudsdkcore.sdk_request import SdkRequest
from huaweicloudsdkcore.signer.signer import Signer
from enum import Enum


class MeetingCredentials(Credentials):
    def __init__(self, user_name=None, user_password=None):
        super(MeetingCredentials, self).__init__()
        self._token = None
        self._last_token_date = None
        self._auth_type_enum = None
        self._tenant_scene_enum = None
        self._app_id = None
        self._app_key = None
        self._corp_id = None
        self._user_id = None
        self._dept_code = None
        self._client_type = None

        if user_name is not None:
            self._user_name = user_name

        if user_password is not None:
            self._user_password = user_password

    def with_auth_type_enum(self, auth_type_enum):
        self._auth_type_enum = auth_type_enum
        return self

    def with_tenant_scene_enum(self, tenant_scene_enum):
        self._tenant_scene_enum = tenant_scene_enum
        return self

    def with_app_id(self, app_id):
        self._app_id = app_id
        return self

    def with_app_key(self, app_key):
        self._app_key = app_key
        return self

    def with_corp_id(self, corp_id):
        self._corp_id = corp_id
        return self

    def with_user_id(self, user_id):
        self._user_id = user_id
        return self

    def with_dept_code(self, dept_code):
        self._dept_code = dept_code
        return self

    def with_client_type(self, client_type):
        self._client_type = client_type
        return self

    def _sign_hmac256(self, expire_time, nonce):
        if self._user_id is None:
            self._user_id = ""
        if self._tenant_scene_enum == TenantSceneEnum.MULTI_TENANT:
            if self._corp_id is None:
                self._corp_id = ""
            data_param = (self._app_id, self._corp_id, self._user_id, str(expire_time), nonce)
        else:
            data_param = (self._app_id, self._user_id, str(expire_time), nonce)

        data = ':'.join(data_param)
        return hmac.new(self._app_key.encode('utf-8'), data.encode('utf-8'), digestmod=sha256).hexdigest().upper()

    def get_update_path_params(self):
        pass

    def process_auth_request(self, request, http_client, executor=None):
        executor = http_client.executor if executor is None else executor
        return executor.submit(self.process_request, request, http_client)

    def process_request(self, request, http_client):
        now_time = datetime.datetime.now()

        if self._token is None or self._last_token_date is None or (
                now_time - self._last_token_date).days * 24 * 3600 + (
                now_time - self._last_token_date).seconds > 12 * 60 * 60:
            if self._auth_type_enum is None or self._auth_type_enum == AuthTypeEnum.ACCOUNT:
                authorization = "Basic " + six.ensure_str(
                    base64.b64encode((self._user_name + ':' + self._user_password).encode('utf-8')))

                body = {'account': self._user_name, 'clientType': 72}
                sdk_request = SdkRequest('POST', 'https', request.host, [], '/v1/usg/acs/auth/account', [],
                                         {'Authorization': authorization, 'Content-Type': 'application/json'},
                                         json.dumps(body), [])
            else:
                nonce = str(uuid.uuid4())
                # 签名信息有效期（10分钟）
                expire_time = int(time.time()) + 60 * 10
                authorization = "HMAC-SHA256 signature=" + self._sign_hmac256(expire_time, nonce)
                body = {"appId": self._app_id, "userId": self._user_id, "corpId": self._corp_id,
                        "expireTime": expire_time, "nonce": nonce, "clientType": 72, "deptCode": self._dept_code}
                sdk_request = SdkRequest('POST', 'https', request.host, [], '/v2/usg/acs/auth/appauth', [],
                                         {'Authorization': authorization, 'Content-Type': 'application/json'},
                                         json.dumps(body), [])

            response = http_client.do_request_sync(sdk_request)
            content = json.loads(response.content.decode())
            self._token = content['accessToken']
            self._last_token_date = datetime.datetime.now()
            request.header_params["X-Access-Token"] = self._token
            canonical_query_string = Signer.process_canonical_query_string(request)
            request.uri = request.resource_path + "?" + canonical_query_string \
                if canonical_query_string != "" else request.resource_path
            return request
        else:
            request.header_params["X-Access-Token"] = self._token
            canonical_query_string = Signer.process_canonical_query_string(request)
            request.uri = request.resource_path + "?" + canonical_query_string \
                if canonical_query_string != "" else request.resource_path
            return request


class AuthTypeEnum(Enum):
    # 账号密码鉴权方式
    ACCOUNT = 0

    # APPID鉴权方式
    APP_ID = 1


class TenantSceneEnum(Enum):
    # 单租户场景
    SINGLE_TENANT = 0

    # 多租户场景
    MULTI_TENANT = 1
