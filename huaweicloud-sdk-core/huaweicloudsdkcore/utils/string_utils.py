# coding: utf-8
"""
 Copyright 2020 Huawei Technologies Co.,Ltd.

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


def camel_to_underline(camel_format):
    underline_format = ''
    if isinstance(camel_format, str):
        for _s_ in camel_format:
            underline_format += _s_ if _s_.islower() or _s_.isdigit() else '_' + _s_.lower()
    return underline_format.strip('_')


def underline_to_camel(underline_format):
    camel_format = ''
    if isinstance(underline_format, str):
        for _s_ in underline_format.split('_'):
            camel_format += _s_.capitalize()
    return camel_format
