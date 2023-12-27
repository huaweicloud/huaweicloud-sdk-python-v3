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

from huaweicloudsdkobs.v1.obs_signer import OBSSigner
from huaweicloudsdkcore.auth.credentials import Credentials
import datetime

_AUTHORIZATION_HEADER = 'Authorization'


class ObsCredentials(Credentials):
    def __init__(self, ak, sk, securityToken=None):
        self.ak = ak
        self.sk = sk
        self.security_token = securityToken

    def get_update_path_params(self):
        return {}

    def process_auth_params(self, http_client, region_id):
        return self

    def process_auth_request(self, request, http_client):
        if request.host.split('.')[0] == 'obs':
            bucketName = None
        else:
            bucketName = request.host.split('.')[0]
        objectKey = request.resource_path.split('/')[1]
        pathArgs = request.query_params
        gmt_format = '%a %b %d %Y %H:%M:%S GMT'
        request.header_params['Date'] = datetime.datetime.utcnow().strftime(gmt_format)
        ret = OBSSigner.doAuth(self, request.method, bucketName, objectKey, pathArgs, request.header_params)

        request.header_params[_AUTHORIZATION_HEADER] = ret[_AUTHORIZATION_HEADER]

        OBSSigner.process_request_uri(request)
        return http_client.executor.submit(lambda: request)


