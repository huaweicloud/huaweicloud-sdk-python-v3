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

from bson import MinKey, MaxKey, Regex, Code, ObjectId, Timestamp, Decimal128

BSON_TYPES = (MinKey, MaxKey, Regex, Code, ObjectId, Timestamp, Decimal128)

BSON_TYPES_MAPPING = {
    'dict': dict,
    'bytes': bytes,
    'MinKey': MinKey,
    'MaxKey': MaxKey,
    'Regex': Regex,
    'Code': Code,
    'ObjectId': ObjectId,
}
