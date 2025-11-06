# coding: utf-8
"""
 Copyright 2025 Huawei Technologies Co.,Ltd.

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
import os
from xml.etree import ElementTree

import pytest

from huaweicloudsdkcore.client import Client
from huaweicloudsdkcore.utils.xml_utils import XmlTransfer
from tests.model.obs import model


def equals(ele1, ele2):
    if ele1.tag != ele2.tag:
        return False
    if ele1.text != ele2.text:
        return False
    if ele1.attrib != ele2.attrib:
        return False

    childs1 = list(ele1)
    childs2 = list(ele2)
    if len(childs1) != len(childs2):
        return False

    for child1, child2 in zip(childs1, childs2):
        equals(child1, child2)

    return True


def mock_list_buckets_response():
    resp = model.ListBucketsResponse()
    resp.owner = model.Owner(id="id")
    bucket = [model.Bucket(name="bucketName", creation_date="date", location="region")]
    resp.buckets = model.Buckets(bucket=bucket)
    return resp


def mock_list_buckets_response1():
    resp = model.ListBucketsResponse()
    resp.owner = model.Owner(id="id")
    bucket = [
        model.Bucket(name="bucketName", creation_date="date", location="region"),
        model.Bucket(name="bucketName1", creation_date="date1", location="region1")
    ]
    resp.buckets = model.Buckets(bucket=bucket)
    return resp


class Response(object):
    def __init__(self):
        self.content = None
        self.headers = None


class TestXmlTransfer:
    DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
    ENCODING = "UTF-8"
    XML_FILES = []
    JSON_FILES = []

    @classmethod
    def setup_class(cls):
        xml_dir = os.path.join(cls.DATA_DIR, "xmls")
        xml_files = os.listdir(xml_dir)
        for file in xml_files:
            xml_file = os.path.join(xml_dir, file)
            cls.XML_FILES.append(xml_file)

            json_file = xml_file.replace("xmls", "dicts", 1).replace(".xml", ".json", 1)
            cls.JSON_FILES.append(json_file)

    @classmethod
    def gen_str_xmls(cls):
        for file in cls.XML_FILES:
            with open(file, "r", encoding=cls.ENCODING) as f:
                lines = map(lambda s: s.strip(), f.readlines())
            yield "".join(lines)

    @classmethod
    def gen_dicts(cls):
        for file in cls.JSON_FILES:
            with open(file, "r", encoding=cls.ENCODING) as f:
                _dict = json.load(f)
            yield _dict

    def test_xml_transfer(self):
        transfer = XmlTransfer()
        for xml_str, _dict in zip(self.gen_str_xmls(), self.gen_dicts()):
            # test xml to dict
            assert transfer.to_dict(xml_str) == _dict

            # test dict to xml
            actual_xml = transfer.to_string(_dict)
            actual_ele = ElementTree.fromstring(actual_xml)
            expected_ele = ElementTree.fromstring(xml_str)
            assert equals(expected_ele, actual_ele)

    def test_xml_to_response(self):
        client = Client()
        client.model_package = model

        resp = Response()
        resp.headers = {"Content-Type": "application/xml"}

        with open(os.path.join(self.DATA_DIR, "xmls", "ListAllMyBucketsResult.xml"), "rb") as f:
            resp.content = f.read()

        resp_model = client.deserialize(resp, "ListBucketsResponse", None)
        assert mock_list_buckets_response() == resp_model

        with open(os.path.join(self.DATA_DIR, "xmls", "ListAllMyBucketsResult1.xml"), "rb") as f:
            resp.content = f.read()

        resp_model1 = client.deserialize(resp, "ListBucketsResponse", None)
        assert mock_list_buckets_response1() == resp_model1
        client.close()


if __name__ == '__main__':
    pytest.main()
