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
import pytest

from huaweicloudsdkcore.utils.string_utils import replace_invalid_character, mask


def test_replace_invalid_character():
    assert replace_invalid_character("abc123#") == "abc123#"
    assert replace_invalid_character("") == ""
    assert replace_invalid_character("hello" + "\t" + "world") == "hello_world"
    assert replace_invalid_character("hello123" + "\t" + "world " + "\x07\x7f" + "中") == "hello123_world____"


@pytest.mark.parametrize("text, ratio, mask_char, expected", [
    ("abcdefghijklmnopqrstuvwxyz123456", 0.7, '*', "abcde**********************23456"),
    ("123456", 0.8, '*', "1****6"),
    ("12345", 0.8, '*', "****5"),
    ("12345", 1, '*', "*****"),
    ("12345", 1.5, '*', "*****"),
    ("12345", 0, '*', "12345"),
    ("12345", -1, '*', "12345")
])
def test_mask(text, ratio, mask_char, expected):
    assert mask(text, ratio, mask_char) == expected


if __name__ == '__main__':
    pytest.main()
