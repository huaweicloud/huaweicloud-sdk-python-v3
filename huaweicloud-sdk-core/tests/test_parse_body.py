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
from bson import MaxKey, MinKey, Regex, ObjectId, Code, Decimal128, Timestamp
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.http.formdata import FormFile
from huaweicloudsdkcore.http.multipart import MultipartEncoder

from huaweicloudsdkcore.client import Client
from tests.model.kvs import BsonBody
from tests.model.kvs import GetKvRequest
from tests.model.vpc import Vpc
import datetime
import os
import tempfile
from io import BytesIO


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
            "age": 10,
            "birthday": datetime.datetime(2025, 3, 14)
        }
    }
    kvs = GetKvRequest(table_name="test-table", primary_key={"name": "tom", "age": 10, "birthday": datetime.datetime(2025, 3, 14)})
    assert parse_bson_body(kvs) == bson.encode(bson_dict)


def test_parse_bson_type(mocked_client):
    parse_bson_body = getattr(mocked_client, "_parse_bson_body")
    assert parse_bson_body(None) is None
    assert parse_bson_body({}) == bson.encode({})
    dict_data = {
        "user": "jack",
        "age": 10,
        "birthday": datetime.datetime(2025, 3, 14)
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
        "js_code_field": Code(js_code),
        "string_field": "Hello, BSON!",  # 字符串
        "int32_field": 123456,  # 32 位整数
        "int64_field": 9876543210123,  # 64 位整数
        "double_field": 3.1415926535,  # 浮点数
        "decimal128_field": Decimal128("1234567890.123456789"),  # 高精度 Decimal128
        "boolean_field": True,  # 布尔值
        "array_field": [1, 2, 3, "abc"],  # 数组
        "timestamp_field": Timestamp(12345, 6789)
    }

    body = BsonBody(
        doc_field=dict_data,
        binary_field=binary_data,
        min_key_field=MinKey(),
        max_key_field=MaxKey(),
        regex_field=Regex(regex_pattern),
        object_id_field=object_id,
        js_code_field=Code(js_code),
        string_field="Hello, BSON!",
        int32_field=123456,
        int64_field=9876543210123,
        double_field=3.1415926535,
        decimal128_field=Decimal128("1234567890.123456789"),
        boolean_field=True,
        null_field=None,
        array_field=[1, 2, 3, "abc"],
        timestamp_field=Timestamp(12345, 6789)
    )
    assert http_utils.sanitize_for_bson_serialization(body) == bson_dict
    assert parse_bson_body(body) == bson.encode(bson_dict)


def test_parse_form_data_body(mocked_client):
    parse_form_data_body = getattr(mocked_client, "_parse_form_data_body")

    body = parse_form_data_body(None)
    assert body is not None
    assert "multipart/form-data" in body.content_type

    body = parse_form_data_body({"name": "test", "value": "123"})
    assert body is not None
    assert "multipart/form-data" in body.content_type
    content = body.read()
    assert b'name="name"' in content
    assert b'test' in content
    assert b'name="value"' in content
    assert b'123' in content

    with tempfile.NamedTemporaryFile(mode="wb", delete=False, suffix=".txt") as f:
        f.write(b"file content")
        tmp_path = f.name
    try:
        with open(tmp_path, "rb") as f:
            form_file = FormFile(f, content_type="text/plain")
            body = parse_form_data_body({"file": form_file})
            assert body is not None
            assert "multipart/form-data" in body.content_type
            content = body.read()
            assert b'filename=' in content
            assert b'file content' in content
    finally:
        os.unlink(tmp_path)


def test_multipart_encoder_plain_fields():
    from collections import OrderedDict
    fields = OrderedDict([("name", "test"), ("type", "demo")])
    encoder = MultipartEncoder(fields=fields)
    assert "multipart/form-data" in encoder.content_type
    assert "boundary=" in encoder.content_type
    content = encoder.read()
    assert b'name="name"' in content
    assert b'test' in content
    assert b'name="type"' in content
    assert b'demo' in content


def test_multipart_encoder_with_file():
    from collections import OrderedDict
    file_obj = BytesIO(b"hello world")
    fields = OrderedDict([("name", "test"), ("file", ("test.txt", file_obj, "text/plain"))])
    encoder = MultipartEncoder(fields=fields)
    assert "multipart/form-data" in encoder.content_type
    content = encoder.read()
    assert b'filename="test.txt"' in content
    assert b"hello world" in content
    assert b'name="name"' in content


def test_multipart_encoder_len():
    from collections import OrderedDict
    fields = OrderedDict([("key", "value")])
    encoder = MultipartEncoder(fields=fields)
    assert encoder.len > 0


if __name__ == "__main__":
    pytest.main()
