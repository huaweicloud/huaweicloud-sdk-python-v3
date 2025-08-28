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

from huaweicloudsdkcore.utils.string_utils import replace_invalid_character


def test_replace_invalid_character():
    assert replace_invalid_character("abc123#") == "abc123#"
    assert replace_invalid_character("") == ""
    assert replace_invalid_character("hello" + "\t" + "world") == "hello_world"
    assert replace_invalid_character("hello123" + "\t" + "world " + "\x07\x7f" + "中") == "hello123_world____"