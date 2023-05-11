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
import json

import requests
import requests_mock

MOCK_ENDPOINT = "https://service.test.com"
MOCK_ENDPOINT_WITHOUT_SCHEME = "service.test.com"

mock_session = requests.Session()
mock_adapter = requests_mock.Adapter()


def mock_keystone_list_projects(name):
    url = MOCK_ENDPOINT + "?name=" + name
    mock_adapter.register_uri("GET", url, text=mock_keystone_list_projects_response(), status_code=200)
    mock_session.mount("https://", mock_adapter)

    return mock_session.get(url)


def mock_keystone_list_projects_response():
    content = {
        "projects": [{
            "id": "123456789"
        }]
    }
    return json.dumps(content)
