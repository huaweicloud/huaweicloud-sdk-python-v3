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

from huaweicloudsdkcore.client import Client
from tests.model.vpc import Vpc


class CustomIter:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current < len(self.data):
            result = self.data[self.current]
            self.current += 1
            return result

        raise StopIteration


def test_parse_body():
    client = Client()
    parse_body = getattr(client, "_parse_body")
    assert parse_body(None) is None
    assert parse_body("") == ""
    assert parse_body("text") == "text"
    assert parse_body({}) == "{}"
    assert parse_body([]) == "[]"

    custom = CustomIter([1, 2, 3])
    assert parse_body(custom) == custom

    vpc = Vpc(id='id', name='name', cidr='cidr', description='description', routes='routes', status='status')
    assert parse_body(vpc) == ('{"id": "id", "name": "name", "cidr": "cidr", "description": "description", "routes": '
                               '"routes", "status": "status"}')
    assert parse_body([vpc]) == ('[{"id": "id", "name": "name", "cidr": "cidr", "description": "description", '
                                 '"routes": "routes", "status": "status"}]')
    assert parse_body({"vpc": vpc}) == ('{"vpc": {"id": "id", "name": "name", "cidr": "cidr", "description": '
                                        '"description", "routes": "routes", "status": "status"}}')
