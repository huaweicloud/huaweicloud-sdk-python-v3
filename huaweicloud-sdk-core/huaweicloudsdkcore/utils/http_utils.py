# coding: utf-8
"""
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

import six

from huaweicloudsdkcore.http.primitive_types import primitive_types


def sanitize_for_serialization(obj):
    if obj is None:
        return None

    elif isinstance(obj, primitive_types):
        return obj

    elif isinstance(obj, list):
        return [sanitize_for_serialization(sub_obj) for sub_obj in obj]

    elif isinstance(obj, tuple):
        return tuple(sanitize_for_serialization(sub_obj) for sub_obj in obj)

    elif isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()

    elif isinstance(obj, dict):
        obj_dict = obj

    else:
        obj_dict = {obj.attribute_map[attr]: getattr(obj, attr) for attr, _ in six.iteritems(obj.openapi_types)
                    if getattr(obj, attr) is not None}

    return {key: sanitize_for_serialization(val)
            for key, val in six.iteritems(obj_dict)}


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
            new_params.append((k, v))
    return new_params


def select_header_accept(accepts):
    if not accepts:
        return
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
