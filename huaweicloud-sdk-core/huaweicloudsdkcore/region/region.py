# coding: utf-8
"""
 Copyright 2022 Huawei Technologies Co.,Ltd.

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
    def __init__(self, *args, **kwargs):
        """
        There are two ways to initialize the region object.

        In the first way, only one region and one endpoint can be specified.
        region1 = Region(id="region-id", endpoint="region-endpoint")

        In the second way, one region and multiple endpoints can be specified.
        region2 = Region("region-id", "endpoint1", "endpoint2")

        It is not recommended to mix the two initialization ways.
        If two initialization ways are mixed, the first way has priority over the second.
        """
        self._id = None
        self._endpoints = None

        if len(args) > 1:
            self._id = args[0]
            self._endpoints = list(args[1:])

        if kwargs:
            if "id" in kwargs:
                self._id = kwargs.get("id")
            if "endpoint" in kwargs:
                self._endpoints = [kwargs.get("endpoint")]

        if not self._id:
            raise ValueError("id is required")
        if not self.endpoints:
            raise ValueError("at lease one endpoint is required")

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
