# coding: utf-8
"""
 Copyright 2023 Huawei Technologies Co.,Ltd.

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

from huaweicloudsdkobs.v1.obs_signer import OBSSigner
from huaweicloudsdkcore.auth.credentials import Credentials
import datetime
import hashlib
import base64

_AUTHORIZATION_HEADER = 'Authorization'
_CONTENT_MD5_HEADER = 'Content-MD5'


class ObsCredentials(Credentials):
    def __init__(self, ak, sk, securityToken=None):
        self.ak = ak
        self.sk = sk
        self.security_token = securityToken

    def get_update_path_params(self):
        return {}

    def process_auth_params(self, http_client, region_id):
        return self

    def get_encoded_md5(self, byte_val):
        hash_object = hashlib.md5(byte_val)
        base64_hash = base64.b64encode(hash_object.digest())
        return base64_hash

    def process_auth_request(self, request, http_client):
        if request.host.split('.')[0] == 'obs':
            bucketName = None
        else:
            bucketName = request.host.split('.')[0]
        objectKey = request.resource_path.split('/')[1]
        pathArgs = request.query_params
        gmt_format = '%a %b %d %Y %H:%M:%S GMT'
        request.header_params['Date'] = datetime.datetime.utcnow().strftime(gmt_format)
        if request.body and _CONTENT_MD5_HEADER not in request.header_params and isinstance(request.body, str):
            md5 = self.get_encoded_md5(request.body.encode('UTF-8')).decode('UTF-8')
            request.header_params[_CONTENT_MD5_HEADER] = md5
        ret = OBSSigner.doAuth(self, request.method, bucketName, objectKey, pathArgs, request.header_params)

        request.header_params[_AUTHORIZATION_HEADER] = ret[_AUTHORIZATION_HEADER]

        OBSSigner.process_request_uri(request)
        return http_client.executor.submit(lambda: request)


