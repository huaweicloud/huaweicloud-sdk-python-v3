# coding: utf-8
"""
 Copyright 2024 Huawei Technologies Co.,Ltd.

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

from huaweicloudsdkcore.auth.credentials import Credentials
from huaweicloudsdkcore.exceptions.exceptions import SdkException


class SMSApiCredentials(Credentials):

    def process_auth_params(self, http_client, region_id):
        return self

    def process_auth_request(self, request, http_client, executor=None):
        return http_client.executor.submit(self.sign_request, request)

    def sign_request(self, request):
        signer_cls = self._SIGNER_CASE.get(request.signing_algorithm)
        if not signer_cls:
            raise SdkException("unsupported signing algorithm: " + str(request.signing_algorithm))
        return signer_cls(self).sign(request)
