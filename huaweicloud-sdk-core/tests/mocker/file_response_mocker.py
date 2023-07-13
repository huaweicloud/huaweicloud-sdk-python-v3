# coding= utf-8
"""
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache LICENSE, Version 2.0 (the
 "LICENSE"); you may not use this file except in compliance
 with the LICENSE.  You may obtain a copy of the LICENSE at

     http=//www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the LICENSE is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the LICENSE for the
 specific language governing permissions and limitations
 under the LICENSE.
"""
import os

import requests
import requests_mock

mock_session = requests.Session()
mock_adapter = requests_mock.Adapter()


def mocked_file():
    return open(os.path.join(os.path.dirname(__file__), "../data/test.txt"), 'rb')


def mocked_file_response():
    mock_adapter.register_uri('GET', 'mock://file', content=mocked_file().read(), status_code=200)
    mock_session.mount('mock://', mock_adapter)
    return mock_session.get('mock://file')
