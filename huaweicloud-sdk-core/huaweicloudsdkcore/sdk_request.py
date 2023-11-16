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
from huaweicloudsdkcore.signer.algorithm import SigningAlgorithm


class SdkRequest(object):
    def __init__(self, method='GET', schema=None, host=None, resource_path=None, uri=None, query_params=None,
                 header_params=None, body=None, stream=False, signing_algorithm=SigningAlgorithm.get_default()):
        self._method = method
        self._schema = schema
        self._host = host
        self._resource_path = resource_path
        self._uri = uri
        self._query_params = query_params
        self._header_params = header_params
        self._body = body
        self._stream = stream
        self._signing_algorithm = signing_algorithm

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, method):
        self._method = method

    @property
    def schema(self):
        return self._schema

    @schema.setter
    def schema(self, schema):
        self._schema = schema

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, host):
        self._host = host

    @property
    def resource_path(self):
        return self._resource_path

    @resource_path.setter
    def resource_path(self, resource_path):
        self._resource_path = resource_path

    @property
    def uri(self):
        return self._uri

    @uri.setter
    def uri(self, uri):
        self._uri = uri

    @property
    def query_params(self):
        return self._query_params

    @query_params.setter
    def query_params(self, query_params):
        self._query_params = query_params

    @property
    def header_params(self):
        return self._header_params

    @header_params.setter
    def header_params(self, header_params):
        self._header_params = header_params

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, body):
        self._body = body

    @property
    def stream(self):
        return self._stream

    @stream.setter
    def stream(self, stream):
        self._stream = stream

    @property
    def signing_algorithm(self):
        return self._signing_algorithm

    @signing_algorithm.setter
    def signing_algorithm(self, signing_algorithm):
        self._signing_algorithm = signing_algorithm

    @property
    def url(self):
        return "%s://%s%s" % (self.schema, self.host, self.uri)
