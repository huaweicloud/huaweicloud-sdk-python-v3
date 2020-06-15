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
import logging
import os
import re
import sys
from logging.handlers import RotatingFileHandler

import six
from six.moves.urllib.parse import quote, urlparse

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions.exceptions import ApiValueError
from huaweicloudsdkcore.http.http_client import HttpClient
from huaweicloudsdkcore.http.primitive_types import native_types_mapping
from huaweicloudsdkcore.http.primitive_types import primitive_types
from huaweicloudsdkcore.sdk_request import SdkRequest
from huaweicloudsdkcore.sdk_response import SdkResponse, FutureSdkResponse
from huaweicloudsdkcore.utils import http_utils, core_utils


class ClientBuilder:
    def __init__(self, clazz):
        self.__clazz = clazz
        self.__config = None
        self.__credentials = None
        self.__endpoint = None
        self.__file_logger_handler = None
        self.__stream_logger_handler = None
        self.__enable_http_log = False

    def with_config(self, config):
        self.__config = config
        return self

    def with_http_config(self, config):
        self.__config = config
        return self

    def with_credentials(self, credentials):
        self.__credentials = credentials
        return self

    def with_endpoint(self, endpoint):
        self.__endpoint = endpoint
        return self

    def with_enable_http_log(self, enable_http_log: bool):
        self.__enable_http_log = enable_http_log
        return self

    def with_file_log(self, path, log_level=logging.INFO, max_bytes=10485760, backup_count=5, format_string=None):
        self.__file_logger_handler = {
            "path": path,
            "log_level": log_level,
            "max_bytes": max_bytes,
            "backup_count": backup_count,
            "format_string": format_string
        }
        return self

    def with_stream_log(self, stream=sys.stdout, log_level=logging.INFO, format_string=None):
        self.__stream_logger_handler = {
            "stream": stream,
            "log_level": log_level,
            "format_string": format_string
        }
        return self

    def build(self):
        if self.__credentials is None:
            self.__credentials = self.get_credential_from_environment_variables()

        client = self.__clazz()
        client.set_endpoint(self.__endpoint)
        client.set_credentials(self.__credentials)
        client.set_config(self.__config)

        if self.__file_logger_handler is not None:
            client.add_file_logger(**self.__file_logger_handler)
        if self.__stream_logger_handler is not None:
            client.add_stream_logger(**self.__stream_logger_handler)
        client.enable_http_log(self.__enable_http_log)

        client.init_http_client()
        return client

    @classmethod
    def get_credential_from_environment_variables(cls):
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
        self._agent = {"User-Agent": "huaweicloud-sdk-pythons/3.0"}
        self._logger = self._init_logger()
        self._enable_http_log = False

        self._credentials = None
        self._config = None
        self._endpoint = None
        self._http_client = None

        self.preset_headers = {}
        self.model_package = None
        try:
            exception_handler_model_name = "%s.exception_handler" % self.__module__[:self.__module__.rindex('.')]
            self.exception_handler_model = importlib.import_module(exception_handler_model_name)
        except ModuleNotFoundError:
            self.exception_handler_model = None

    def _init_logger(self):
        logger_name = 'huaweicloud-sdk-{}'.format(str(id(self)))
        logger = logging.getLogger(logger_name)
        logger.propagate = False
        return logger

    def set_config(self, config):
        self._config = config

    def set_credentials(self, credentials):
        self._credentials = credentials

    def set_endpoint(self, endpoint):
        self._endpoint = endpoint

    def enable_http_log(self, enable_http_log):
        self._enable_http_log = enable_http_log

    def init_http_client(self):
        http_client = HttpClient(self._logger, self._enable_http_log)
        http_client.set_config(self._config)
        if self.exception_handler_model is not None:
            http_client.set_service_spec_exception_handler(getattr(self.exception_handler_model, "handle_exception"))
        self._http_client = http_client

    def add_stream_logger(self, stream, log_level, format_string):
        self._logger.setLevel(log_level)
        stream_handler = logging.StreamHandler(stream)
        stream_handler.setLevel(log_level)
        formatter = logging.Formatter(format_string if format_string is not None else core_utils.LOG_FORMAT)
        stream_handler.setFormatter(formatter)
        if stream_handler not in self._logger.handlers:
            self._logger.addHandler(stream_handler)

    def add_file_logger(self, path, log_level, max_bytes, backup_count, format_string):
        self._logger.setLevel(log_level)
        file_handler = RotatingFileHandler(path, maxBytes=max_bytes, backupCount=backup_count)
        file_handler.setLevel(log_level)
        formatter = logging.Formatter(format_string if format_string is not None else core_utils.LOG_FORMAT)
        file_handler.setFormatter(formatter)
        if file_handler not in self._logger.handlers:
            self._logger.addHandler(file_handler)

    def _parse_header_params(self, collection_formats, header_params):
        header_params = header_params or {}
        header_params.update(self.preset_headers)
        if header_params:
            header_params = http_utils.sanitize_for_serialization(header_params)
            header_params = dict(http_utils.parameters_to_tuples(header_params, collection_formats))
        header_params.update(self._agent)
        return header_params

    def _parse_path_params(self, collection_formats, path_params, resource_path, update_path_params):
        path_params = self.post_process_params(path_params) or {}
        if update_path_params is not None:
            path_params.update(update_path_params)
        if path_params:
            path_params = http_utils.sanitize_for_serialization(path_params)
            path_params = http_utils.parameters_to_tuples(path_params, collection_formats)
            for k, v in path_params:
                resource_path = resource_path.replace('{%s}' % k, quote(str(v), safe=''))
        return resource_path

    def _parse_query_params(self, collection_formats, query_params):
        query_params = self.post_process_params(query_params) or []
        if query_params:
            query_params = http_utils.sanitize_for_serialization(query_params)
            query_params = http_utils.parameters_to_tuples(query_params, collection_formats)
        return query_params

    def _parse_post_params(self, collection_formats, post_params):
        post_params = self.post_process_params(post_params) if post_params else []
        if post_params:
            post_params = http_utils.sanitize_for_serialization(post_params)
            post_params = http_utils.parameters_to_tuples(post_params, collection_formats)
        return post_params

    def _parse_body(self, body):
        if body:
            body = http_utils.sanitize_for_serialization(body)
            body = json.dumps(body)
        else:
            body = ""
        return body

    @classmethod
    def post_process_params(cls, params):
        if type(params) == dict:
            for key in list(params.keys()):
                if params[key] is None:
                    del [params[key]]
            return params
        elif type(params) == list:
            list_filter = filter(lambda x: type(x) == tuple and len(x) == 2 and x[1] is not None, params)
            return [i for i in list_filter]

    def do_http_request(self, method, resource_path, path_params=None, query_params=None, header_params=None, body=None,
                        post_params=None, response_type=None, collection_formats=None, request_type=None,
                        async_request=False):
        url_parse_result = urlparse(self._endpoint)
        schema = url_parse_result.scheme
        host = url_parse_result.netloc

        header_params = self._parse_header_params(collection_formats, header_params)
        resource_path = self._parse_path_params(collection_formats, path_params, resource_path,
                                                self._credentials.get_update_path_params())
        query_params = self._parse_query_params(collection_formats, query_params)
        post_params = self._parse_post_params(collection_formats, post_params)
        body = self._parse_body(body)
        sdk_request = SdkRequest(method, schema, host, resource_path, query_params, header_params, body, post_params)
        request = self._credentials.process_auth_request(sdk_request)

        request_sensitive_list = self._get_sensitive_list(request_type)
        response_sensitive_list = self._get_sensitive_list(response_type)

        if async_request:
            future_response = self._do_http_request_async(request, response_type, request_sensitive_list,
                                                          response_sensitive_list)
            return FutureSdkResponse(future_response, self._logger)
        else:
            response = self._do_http_request_sync(request, request_sensitive_list, response_sensitive_list)
            return self.sync_response_handler(response, response_type)

    def _get_sensitive_list(self, clazz):
        if clazz is None:
            return []

        response_sensitive_list = []
        if clazz in native_types_mapping:
            return response_sensitive_list

        klass = getattr(self.model_package, clazz)
        for attr, attr_type in six.iteritems(klass.openapi_types):
            if attr_type in native_types_mapping and attr in klass.sensitive_list:
                response_sensitive_list.append(attr)
            elif attr_type.startswith('list['):
                sub_attr_type = re.match(r'list\[(.*)\]', attr_type).group(1)
                response_sensitive_list.extend(
                    [attr + ".[*]." + i for i in self._get_sensitive_list(sub_attr_type)])
            elif attr_type.startswith('dict('):
                sub_attr_type = re.match(r'dict\(([^,]*), (.*)\)', attr_type).group(2)
                response_sensitive_list.extend(
                    [attr + ".*." + i for i in self._get_sensitive_list(sub_attr_type)])
            else:
                response_sensitive_list.extend(
                    [attr + "." + i for i in self._get_sensitive_list(attr_type)])
        return response_sensitive_list

    def _do_http_request_sync(self, request, request_sensitive_list, response_sensitive_list):
        response = self._http_client.do_request_sync(request, request_sensitive_list, response_sensitive_list)
        return response

    def _do_http_request_async(self, request, response_type, request_sensitive_list, response_sensitive_list):
        future = self._http_client.do_request_async(request,
                                                    [self.async_response_hook_factory(response_type=response_type)],
                                                    request_sensitive_list,
                                                    response_sensitive_list)
        return future

    def sync_response_handler(self, response, response_type):
        return_data = response
        if self._config.preload_content:
            if response_type:
                return_data = self.deserialize(response, response_type)
            else:
                return_data = None

        if self._config.return_http_data_only:
            return return_data
        else:
            return SdkResponse(response.status_code, response.headers, return_data)

    def async_response_hook_factory(self, response_type):
        def response_hook(resp, *args, **kwargs):
            resp.data = resp.text
            if self._config.preload_content:
                if response_type:
                    resp.data = self.deserialize(resp, response_type)
                else:
                    resp.data = None

        return response_hook

    def deserialize(self, response, response_type):
        try:
            data = json.loads(response.text)
        except ValueError:
            data = response.text
        return self._deserialize(data, response_type)

    def _deserialize(self, data, klass):
        if data is None:
            return None

        if type(klass) == str:
            if klass.startswith('list['):
                sub_kls = re.match(r'list\[(.*)\]', klass).group(1)
                return [self._deserialize(sub_data, sub_kls)
                        for sub_data in data]

            if klass.startswith('dict('):
                sub_kls = re.match(r'dict\(([^,]*), (.*)\)', klass).group(2)
                return {k: self._deserialize(v, sub_kls)
                        for k, v in six.iteritems(data)}

            if klass in native_types_mapping:
                klass = native_types_mapping[klass]
            else:
                klass = getattr(self.model_package, klass)

        if klass in primitive_types:
            return self._deserialize_primitive(data, klass)
        elif klass == object:
            return self._deserialize_object(data)
        elif klass == datetime.date:
            return self._deserialize_date(data)
        elif klass == datetime.datetime:
            return self._deserialize_data_time(data)
        else:
            return self._deserialize_model(data, klass)

    @classmethod
    def _deserialize_primitive(cls, data, klass):
        try:
            return klass(data)
        except UnicodeEncodeError:
            return six.text_type(data)
        except TypeError:
            return data

    @classmethod
    def _deserialize_object(cls, value):
        return value

    @classmethod
    def _deserialize_date(cls, string):
        try:
            from dateutil.parser import parse
            return parse(string).date()
        except ImportError:
            return string
        except ValueError:
            return string

    @classmethod
    def _deserialize_data_time(cls, string):
        try:
            from dateutil.parser import parse
            return parse(string)
        except ImportError:
            return string
        except ValueError:
            return string

    def _deserialize_model(self, data, klass):
        if not klass.openapi_types and not hasattr(klass, 'get_real_child_model'):
            return data

        kwargs = {}
        if klass.openapi_types is not None:
            for attr, attr_type in six.iteritems(klass.openapi_types):
                if (data is not None and
                        klass.attribute_map[attr] in data and
                        isinstance(data, (list, dict))):
                    value = data[klass.attribute_map[attr]]
                    kwargs[attr] = self._deserialize(value, attr_type)

        instance = klass(**kwargs)

        if hasattr(instance, 'get_real_child_model'):
            klass_name = instance.get_real_child_model(data)
            if klass_name:
                instance = self._deserialize(data, klass_name)
        return instance
