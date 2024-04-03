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

from huaweicloudsdkcore.signer.signer import Signer


class IamCredentials:

    _X_AUTH_TOKEN = "X-Auth-Token"

    def __init__(self, auth_token=None):
        self.auth_token = auth_token

    def with_x_auth_token(self, auth_token):
        self.auth_token = auth_token
        return self

    def get_update_path_params(self):
        return {}

    def process_auth_params(self, http_client, region_id):
        return self

    def process_auth_request(self, request, http_client):
        if self.auth_token and self._X_AUTH_TOKEN not in request.header_params:
            request.header_params[self._X_AUTH_TOKEN] = self.auth_token

        Signer.process_request_uri(request)
        return http_client.executor.submit(lambda: request)
