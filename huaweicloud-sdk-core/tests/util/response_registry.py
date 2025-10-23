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

try:
    from responses.registries import OrderedRegistry
except ImportError:
    from responses.registries import FirstMatchRegistry


    class OrderedRegistry(FirstMatchRegistry):
        """
        responses-0.17.0(earlier than python3.8) does not have OrderedRegistry
        """

        def find(self, request):
            if not self.registered:
                return None, ["registered responses is empty"]

            response = self.registered.pop(0)
            matches, reason = response.matches(request)
            if matches:
                return response, []

            self.reset()
            self.add(response)
            return None, [f"no responses matched, reason: {reason}"]
