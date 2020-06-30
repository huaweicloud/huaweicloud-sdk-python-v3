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
from concurrent.futures.thread import ThreadPoolExecutor

from huaweicloudsdkcore.exceptions.exceptions import ApiValueError
from huaweicloudsdkcore.signer import signer


class Credentials:
    def get_update_path_params(self):
        pass

    def process_auth_request(self, request, http_client):
        pass


class BasicCredentials(Credentials):
    def __init__(self, ak, sk, project_id, domain_id=None):
        if ak is None or ak == "":
            raise ApiValueError("AK can not be null.")

        if sk is None or sk == "":
            raise ApiValueError("SK can not be null.")

        self.ak = ak
        self.sk = sk
        self.project_id = project_id
        self.domain_id = domain_id

    def get_update_path_params(self):
        path_params = {}
        if self.project_id is not None:
            path_params["project_id"] = self.project_id
        if self.domain_id is not None:
            path_params["domain_id"] = self.domain_id
        return path_params

    def process_auth_request(self, request, http_client):
        executor = ThreadPoolExecutor(max_workers=8)
        future = executor.submit(self.sign_request, request)
        return future

    def sign_request(self, request):
        if self.project_id is not None:
            request.header_params["X-Project-Id"] = self.project_id
        if self.domain_id is not None:
            request.header_params["X-Domain-Id"] = self.domain_id
        return signer.Signer(self).sign(request)
