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

import datetime
import decimal

import six

from huaweicloudsdkcore.http.formdata import FormFile
from huaweicloudsdkcore.http.primitive_types import PRIMITIVE_TYPES


def sanitize_for_serialization(obj):
    if obj is None:
        return None

    elif isinstance(obj, PRIMITIVE_TYPES):
        return obj

    elif isinstance(obj, decimal.Decimal):
        return obj

    elif isinstance(obj, list):
        return [sanitize_for_serialization(sub_obj) for sub_obj in obj]

    elif isinstance(obj, tuple):
        return tuple(sanitize_for_serialization(sub_obj) for sub_obj in obj)

    elif isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()

    elif isinstance(obj, FormFile):
        return obj

    elif isinstance(obj, dict):
        obj_dict = obj

    else:
        obj_dict = {obj.attribute_map[attr]: getattr(obj, attr) for attr, _ in six.iteritems(obj.openapi_types)
                    if getattr(obj, attr) is not None}

    return {key: sanitize_for_serialization(val)
            for key, val in six.iteritems(obj_dict)}


def dict_params_to_tuple(k, v):
    tuple_list = []
    if isinstance(v, list):
        if len(v) == 0:
            tuple_list.append((k, []))
        else:
            for value in v:
                list_value_to_tuple(tuple_list, k, value)
    elif isinstance(v, dict):
        for key, value in v.items():
            temp = dict_params_to_tuple(k + '[' + str(key) + ']', value)
            if isinstance(temp, list):
                for i in temp:
                    tuple_list.append(i)
            else:
                tuple_list.append(temp)
    else:
        tuple_list.append((k, v))
    return tuple_list


def list_value_to_tuple(tuple_list, key, value):
    if isinstance(value, dict):
        for kk, vv in value.items():
            tuple_list.append(dict_params_to_tuple(key + '[' + str(kk) + ']', vv))
    elif isinstance(value, list):
        if len(value) == 0:
            tuple_list.append((key, []))
        else:
            for i in value:
                tuple_list.append((key, value[i]))
    else:
        tuple_list.append((key, value))


def parameters_to_tuples(params, collection_formats):
    new_params = []
    if collection_formats is None:
        collection_formats = {}
    for k, v in six.iteritems(params) if isinstance(params, dict) else params:
        if k in collection_formats:
            collection_format = collection_formats[k]
            if collection_format == 'multi':
                new_params.extend((k, value) for value in v)
            else:
                new_params.append(
                    (k, ','.join(str(value) for value in v)))
        else:
            if isinstance(v, dict):
                value_tuples = parameters_to_tuples(v, collection_formats)
                for value_tuple in value_tuples:
                    new_params.append((k, "%s=%s" % (value_tuple[0], value_tuple[1])))
            else:
                new_params.append((k, v))
    return new_params


def select_header_accept(accepts):
    if not accepts:
        return ''
    accepts = [x.lower() for x in accepts]
    if 'application/json' in accepts:
        return 'application/json'
    else:
        return ', '.join(accepts)


def select_header_content_type(content_types):
    if not content_types:
        return 'application/json'
    content_types = [x.lower() for x in content_types]
    if 'application/json' in content_types or '*/*' in content_types:
        return 'application/json'
    else:
        return content_types[0]
