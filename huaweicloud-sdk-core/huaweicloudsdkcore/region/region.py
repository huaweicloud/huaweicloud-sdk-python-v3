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

import warnings


class Region(object):
    def __init__(self, _id, *endpoints):
        self._id = _id
        self._endpoints = list(endpoints)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, _id):
        self._id = _id

    @property
    def endpoint(self):
        warnings.warn("As of 3.1.27, because of the support of the multi-endpoint feature, use endpoints instead",
                      DeprecationWarning)
        return self.endpoints[0] if self.endpoints else None

    @endpoint.setter
    def endpoint(self, endpoint):
        warnings.warn("As of 3.1.27, because of the support of the multi-endpoint feature, use endpoints instead",
                      DeprecationWarning)
        self.endpoints = [endpoint]

    @property
    def endpoints(self):
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        self._endpoints = endpoints

    def with_endpoint_override(self, endpoint):
        warnings.warn("As of 3.1.27, because of the support of the multi-endpoint feature,"
                      "use with_endpoints_override instead", DeprecationWarning)
        return self.with_endpoints_override([endpoint])

    def with_endpoints_override(self, endpoints):
        self.endpoints = endpoints
        return self
