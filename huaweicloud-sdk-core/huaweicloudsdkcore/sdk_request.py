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


class SdkRequest(object):
    def __init__(self, method='GET', schema=None, host=None, resource_path=None, uri=None, query_params=None,
                 header_params=None, body=None, stream=False, signing_algorithm=None):
        self.method = method
        self.schema = schema
        self.host = host
        self.resource_path = resource_path
        self.uri = uri
        self.query_params = query_params
        self.header_params = header_params
        self.body = body
        self.stream = stream
        self.signing_algorithm = signing_algorithm
