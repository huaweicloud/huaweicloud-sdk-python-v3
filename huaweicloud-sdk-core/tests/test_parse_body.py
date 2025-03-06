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
import bson
import pytest
from bson import MaxKey, MinKey, Regex, ObjectId, Code
from huaweicloudsdkcore.client import Client
from tests.model.kvs import BsonBody
from tests.model.kvs import GetKvRequest
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


@pytest.fixture
def mocked_client():
    client = Client()
    yield client
    client.close()


def test_parse_body(mocked_client):
    parse_body = getattr(mocked_client, "_parse_body")
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


def test_parse_kvs_body(mocked_client):
    parse_bson_body = getattr(mocked_client, "_parse_bson_body")
    bson_dict = {
        "table_name": "test-table",
        "primary_key": {
            "name": "tom",
            "age": 10
        }
    }
    kvs = GetKvRequest(table_name="test-table", primary_key={"name": "tom", "age": 10})
    assert parse_bson_body(kvs) == bson.encode(bson_dict)


def test_parse_bson_type(mocked_client):
    parse_bson_body = getattr(mocked_client, "_parse_bson_body")
    assert parse_bson_body(None) is None
    assert parse_bson_body({}) == bson.encode({})
    dict_data = {
        "user": "jack",
        "age": 10
    }
    binary_data = b'\x00\x01\x02\x03\x04'
    regex_pattern = "^[A-Za-z0-9]*$"
    js_code = "function add(x, y) { return x + y; }"
    object_id = ObjectId("67adbe37399015c5d4661a5b")
    bson_dict = {
        "doc_field": dict_data,
        "binary_field": binary_data,
        "min_key_field": MinKey(),
        "max_key_field": MaxKey(),
        "regex_field": Regex(regex_pattern),
        "object_id_field": object_id,
        "js_code_field": Code(js_code)
    }
    body = BsonBody(doc_field=dict_data, binary_field=binary_data, min_key_field=MinKey(), max_key_field=MaxKey(),
                    object_id_field=object_id, regex_field=Regex(regex_pattern), js_code_field=Code(js_code))
    assert parse_bson_body(body) == bson.encode(bson_dict)


if __name__ == "__main__":
    pytest.main()
