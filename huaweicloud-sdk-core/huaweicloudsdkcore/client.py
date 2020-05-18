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
import importlib
import json
import os
import re

import six
from six.moves.urllib.parse import quote, urlparse

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.http.http_client import HttpClient
from huaweicloudsdkcore.http.primitive_types import native_types_mapping
from huaweicloudsdkcore.http.primitive_types import primitive_types
from huaweicloudsdkcore.sdk_request import SdkRequest
from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils import http_utils


class ClientBuilder:
    def __init__(self, clazz):
        self.__clazz = clazz
        self.__config = None
        self.__credentials = None
        self.__endpoint = None

    def with_config(self, config):
        self.__config = config
        return self

    def with_credentials(self, credentials):
        self.__credentials = credentials
        return self

    def with_endpoint(self, endpoint):
        self.__endpoint = endpoint
        return self

    def build(self):
        client = self.__clazz()

        if self.__credentials is None:
            self.__credentials = self.get_credential_from_environment_variables()

        client.set_config(self.__config)
        client.set_credentials(self.__credentials)
        client.set_endpoint(self.__endpoint)
        return client

    def get_credential_from_environment_variables(self):
        ak = os.environ.get("HUAWEICLOUD_SDK_AK")
        sk = os.environ.get("HUAWEICLOUD_SDK_SK")
        project_id = os.environ.get("HUAWEICLOUD_SDK_PROJECT_ID")
        domain_id = os.environ.get("HUAWEICLOUD_SDK_DOMAIN_ID")

        return BasicCredentials(ak, sk, project_id, domain_id)


class Client:

    @staticmethod
    def new_builder(clazz):
        return ClientBuilder(clazz)

    def __init__(self):
        self.__http_config = None
        self.__credentials = None
        self.__config = None
        self.__endpoint = None
        self.__agent = {"User-Agent": "huaweicloud-sdk-pythons/3.0"}
        self.preset_headers = {}
        self.model_package = None
        try:
            exception_handler_model_name = "%s.exception_handler" % self.__module__[:self.__module__.rindex('.')]
            self.exception_handler_model = importlib.import_module(exception_handler_model_name)
        except ModuleNotFoundError:
            self.exception_handler_model = None

    def set_config(self, config):
        self.__config = config

    def set_credentials(self, credentials):
        self.__credentials = credentials

    def set_endpoint(self, endpoint):
        self.__endpoint = endpoint

    def get_config(self):
        return self.__http_config

    def get_credentials(self):
        return self.__credentials

    def get_endpoint(self):
        return self.__endpoint

    def do_http_request(self, method, resource_path, path_params=None,
                        query_params=None, header_params=None, body=None, post_params=None,
                        response_type=None, collection_formats=None):
        url_parse_result = urlparse(self.__endpoint)
        schema = url_parse_result.scheme
        host = url_parse_result.netloc

        header_params = header_params or {}
        header_params.update(self.preset_headers)
        if header_params:
            header_params = http_utils.sanitize_for_serialization(header_params)
            header_params = dict(http_utils.parameters_to_tuples(header_params, collection_formats))
        header_params.update(self.__agent)

        path_params = self.postProcessParams(path_params) or {}
        if "project_id" not in path_params:
            path_params.update({"project_id": self.get_credentials().project_id})
        if path_params:
            path_params = http_utils.sanitize_for_serialization(path_params)
            path_params = http_utils.parameters_to_tuples(path_params, collection_formats)
            for k, v in path_params:
                resource_path = resource_path.replace('{%s}' % k, quote(str(v), safe=''))

        query_params = self.postProcessParams(query_params) or []
        if query_params:
            query_params = http_utils.sanitize_for_serialization(query_params)
            query_params = http_utils.parameters_to_tuples(query_params, collection_formats)

        post_params = self.postProcessParams(post_params) if post_params else []
        if post_params:
            post_params = http_utils.sanitize_for_serialization(post_params)
            post_params = http_utils.parameters_to_tuples(post_params, collection_formats)

        if body:
            body = http_utils.sanitize_for_serialization(body)
            body = json.dumps(body)
        else:
            body = ""

        sdk_request = SdkRequest(method, schema, host, resource_path, path_params,
                                 query_params, header_params, body, post_params)
        response = self.__do_http_request(sdk_request)

        return_data = response
        if self.__config.preload_content:
            if response_type:
                return_data = self.deserialize(return_data, response_type)
            else:
                return_data = None

        if self.__config.return_http_data_only:
            return return_data
        else:
            return SdkResponse(response.status_code, response.headers, return_data)

    def postProcessParams(self, params):
        if type(params) == dict:
            for key in list(params.keys()):
                if params[key] is None:
                    del [params[key]]
            return params
        elif type(params) == list:
            list_filter = filter(lambda x: type(x) == tuple and len(x) == 2 and x[1] is not None, params)
            return [i for i in list_filter]

    def __do_http_request(self, sdk_request):
        request = self.__credentials.sign_request(sdk_request)
        client = HttpClient(request)
        client.set_config(self.__config)
        if self.exception_handler_model is not None:
            client.set_service_spec_exception_handler(getattr(self.exception_handler_model, "handle_exception"))
        response = client.do_request()
        return response

    def deserialize(self, response, response_type):
        try:
            data = json.loads(response.text)
        except ValueError:
            data = response.text
        return self.__deserialize(data, response_type)

    def __deserialize(self, data, klass):
        if data is None:
            return None

        if type(klass) == str:
            if klass.startswith('list['):
                sub_kls = re.match(r'list\[(.*)\]', klass).group(1)
                return [self.__deserialize(sub_data, sub_kls)
                        for sub_data in data]

            if klass.startswith('dict('):
                sub_kls = re.match(r'dict\(([^,]*), (.*)\)', klass).group(2)
                return {k: self.__deserialize(v, sub_kls)
                        for k, v in six.iteritems(data)}

            if klass in native_types_mapping:
                klass = native_types_mapping[klass]
            else:
                klass = getattr(self.model_package, klass)

        if klass in primitive_types:
            return self.__deserialize_primitive(data, klass)
        elif klass == object:
            return self.__deserialize_object(data)
        elif klass == datetime.date:
            return self.__deserialize_date(data)
        elif klass == datetime.datetime:
            return self.__deserialize_datatime(data)
        else:
            return self.__deserialize_model(data, klass)

    def __deserialize_primitive(self, data, klass):
        try:
            return klass(data)
        except UnicodeEncodeError:
            return six.text_type(data)
        except TypeError:
            return data

    def __deserialize_object(self, value):
        return value

    def __deserialize_date(self, string):
        try:
            from dateutil.parser import parse
            return parse(string).date()
        except ImportError:
            return string
        except ValueError:
            return string

    def __deserialize_datatime(self, string):
        try:
            from dateutil.parser import parse
            return parse(string)
        except ImportError:
            return string
        except ValueError:
            return string

    def __deserialize_model(self, data, klass):
        if not klass.openapi_types and not hasattr(klass, 'get_real_child_model'):
            return data

        kwargs = {}
        if klass.openapi_types is not None:
            for attr, attr_type in six.iteritems(klass.openapi_types):
                if (data is not None and
                        klass.attribute_map[attr] in data and
                        isinstance(data, (list, dict))):
                    value = data[klass.attribute_map[attr]]
                    kwargs[attr] = self.__deserialize(value, attr_type)

        instance = klass(**kwargs)

        if hasattr(instance, 'get_real_child_model'):
            klass_name = instance.get_real_child_model(data)
            if klass_name:
                instance = self.__deserialize(data, klass_name)
        return instance
