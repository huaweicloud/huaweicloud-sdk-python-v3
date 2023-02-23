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
import decimal
import importlib
import logging
import re
import sys
import threading
import warnings
from collections import OrderedDict
from logging.handlers import RotatingFileHandler

import simplejson as json
import six
from huaweicloudsdkcore.exceptions.exceptions import HostUnreachableException
from requests_toolbelt import MultipartEncoder
from six.moves.urllib.parse import quote, urlparse

from huaweicloudsdkcore.auth.credentials import BasicCredentials, DerivedCredentials
from huaweicloudsdkcore.auth.provider import CredentialProviderChain
from huaweicloudsdkcore.http.formdata import FormFile
from huaweicloudsdkcore.http.http_client import HttpClient
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkcore.http.http_handler import HttpHandler
from huaweicloudsdkcore.http.primitive_types import native_types_mapping
from huaweicloudsdkcore.http.primitive_types import primitive_types
from huaweicloudsdkcore.sdk_request import SdkRequest
from huaweicloudsdkcore.sdk_response import FutureSdkResponse
from huaweicloudsdkcore.sdk_stream_response import SdkStreamResponse
from huaweicloudsdkcore.utils import http_utils, core_utils
from huaweicloudsdkcore.utils.xml_utils import XmlTransfer


class ClientBuilder(object):
    _HTTP_SCHEME = "http"
    _HTTPS_SCHEME = "https"

    def __init__(self, client_type, credential_type=BasicCredentials.__name__):
        self._client_type = client_type
        self._credential_type = credential_type.split(',')
        self._derived_auth_service_name = None
        self._config = None
        self._credentials = None
        self._region = None
        self._endpoints = []

        self._http_handler = None
        self._file_logger_handler = None
        self._stream_logger_handler = None

    def with_http_config(self, config):
        """
        :param config: Config for ClientBuilder
        :type config: :class:`huaweicloudsdkcore.http.http_config.HttpConfig`
        """
        self._config = config
        return self

    def with_credentials(self, credentials):
        """
        :param credentials: Credential for ClientBuilder
        :type credentials: :class:`huaweicloudsdkcore.auth.credentials.Credentials`
        """
        self._credentials = credentials
        return self

    def with_region(self, region):
        """
        :param region: Region for ClientBuilder
        :type region: :class:`huaweicloudsdkcore.region.region.Region`
        """
        self._region = region
        return self

    def with_endpoint(self, endpoint):
        """
        :param endpoint: Endpoint for ClientBuilder
        :type endpoint: str
        """
        warnings.warn("As of 3.1.27, because of the support of the multi-endpoint feature, use with_endpoints instead",
                      DeprecationWarning)
        return self.with_endpoints([endpoint])

    def with_endpoints(self, endpoints):
        self._endpoints = endpoints
        return self

    def with_http_handler(self, http_handler):
        """
        :param http_handler: HttpHandler for ClientBuilder
        :type http_handler: :class:`huaweicloudsdkcore.http.http_handler.HttpHandler`
        """
        self._http_handler = http_handler
        return self

    def with_file_log(self, path, log_level=logging.INFO, max_bytes=10485760, backup_count=5, format_string=None):
        self._file_logger_handler = {
            "path": path,
            "log_level": log_level,
            "max_bytes": max_bytes,
            "backup_count": backup_count,
            "format_string": format_string
        }
        return self

    def with_stream_log(self, stream=sys.stdout, log_level=logging.INFO, format_string=None):
        self._stream_logger_handler = {
            "stream": stream,
            "log_level": log_level,
            "format_string": format_string
        }
        return self

    def _with_derived_auth_service_name(self, derived_auth_service_name):
        self._derived_auth_service_name = derived_auth_service_name
        return self

    def build(self):
        if self._config is None:
            self._config = HttpConfig.get_default_config()

        client = self._client_type() \
            .with_credentials(self._credentials) \
            .with_config(self._config) \
            .with_http_handler(self._http_handler)

        client.init_http_client()

        if not self._credentials:
            provider = CredentialProviderChain.get_default_credential_provider_chain(self._credential_type[0])
            self._credentials = provider.get_credentials()

        if not self._credentials:
            raise ValueError("credential can not be None, %s credential objects are required"
                             % ",".join(self._credential_type))
        if self._credentials.__class__.__name__ not in self._credential_type:
            raise TypeError("credential type error, supported credential type is %s" % ",".join(self._credential_type))

        if self._region is not None:
            self._endpoints += self._region.endpoints
            self._credentials = self._credentials.process_auth_params(client.get_http_client(), self._region.id)

            if isinstance(self._credentials, DerivedCredentials):
                self._credentials._process_derived_auth_params(self._derived_auth_service_name, self._region.id)

        if not self._endpoints:
            raise ValueError("Could not find any endpoints, at least one endpoint is required")
        self._endpoints = [endpoint if endpoint.startswith(self._HTTP_SCHEME) else self._HTTPS_SCHEME + "://" + endpoint
                           for endpoint in self._endpoints]

        client.with_endpoints(self._endpoints).with_credentials(self._credentials)

        if self._file_logger_handler is not None:
            client.add_file_logger(**self._file_logger_handler)
        if self._stream_logger_handler is not None:
            client.add_stream_logger(**self._stream_logger_handler)

        return client


class Client(object):
    _CONTENT_TYPE = "Content-Type"
    _APPLICATION_JSON = "application/json"
    _APPLICATION_XML = "application/xml"
    _APPLICATION_OCTET_STREAM = "application/octet-stream"
    _MULTIPART_FORM_DATA = "multipart/form-data"
    _XML_NAME = "xml_name"
    _AUTHORIZATION = "Authorization"
    _HEADERS = "headers"

    def __init__(self):
        self.preset_headers = {}

        self._agent = {"User-Agent": "huaweicloud-usdk-python/3.0"}
        self._logger = self._init_logger()

        self._credentials = None
        self._config = None
        self._endpoint_index = 0
        self._endpoints = []
        self._mutex = threading.Lock()

        self._http_client = None
        self._http_handler = None

        self.model_package = None
        try:
            exception_handler_model_name = "%s.exception_handler" % self.__module__[:self.__module__.rindex('.')]
            self.exception_handler_model = importlib.import_module(exception_handler_model_name)
        except ImportError:
            self.exception_handler_model = None

    @classmethod
    def _init_logger(cls):
        logger_name = 'HuaweiCloud-SDK-%s' % cls.__name__
        logger = logging.getLogger(logger_name)
        logger.propagate = False
        return logger

    def with_config(self, config):
        """
        :param config: Config for Client
        :type config: :class:`huaweicloudsdkcore.http.http_config.HttpConfig`
        """
        self._config = config
        return self

    def with_credentials(self, credentials):
        """
        :param credentials: Credential for Client
        :type credentials: :class:`huaweicloudsdkcore.auth.credentials.Credentials`
        """
        self._credentials = credentials
        return self

    def with_endpoints(self, endpoints):
        """
        :param endpoints: Endpoint for Client
        :type endpoints: str
        """
        self._endpoints += endpoints
        return self

    def with_http_handler(self, http_handler):
        """
        :param http_handler: HttpHandler for Client
        :type http_handler: :class:`huaweicloudsdkcore.http.http_handler.HttpHandler`
        """
        self._http_handler = http_handler if http_handler is not None else HttpHandler()
        return self

    def init_http_client(self):
        exception_handler = None \
            if self.exception_handler_model is None else getattr(self.exception_handler_model, "handle_exception")
        self._http_client = HttpClient(self._config, self._http_handler, exception_handler, self._logger)

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

    def get_agent(self):
        return self._agent

    def get_credentials(self):
        return self._credentials

    def get_http_client(self):
        return self._http_client

    def _parse_header_params(self, collection_formats, header_params):
        header_params = self.post_process_params(header_params) or {}
        header_params.update(self.preset_headers)
        if header_params:
            header_params = http_utils.sanitize_for_serialization(header_params)
            header_params = dict(http_utils.parameters_to_tuples(header_params, collection_formats))
            header_params = {k: str(v) for k, v in header_params.items()}
        header_params.update(self._agent)
        return header_params

    def _parse_path_params(self, collection_formats, path_params, resource_path, update_path_params):
        path_params = self.post_process_params(path_params) or {}
        if path_params:
            path_params = http_utils.sanitize_for_serialization(path_params)
            path_params = http_utils.parameters_to_tuples(path_params, collection_formats)
            for k, v in path_params:
                resource_path = resource_path.replace('{%s}' % k, quote(str(v), safe=''))
        if update_path_params:
            update_path_params = http_utils.sanitize_for_serialization(update_path_params)
            update_path_params = http_utils.parameters_to_tuples(update_path_params, collection_formats)
            for k, v in update_path_params:
                resource_path = resource_path.replace('{%s}' % k, quote(str(v), safe=''))
        return resource_path

    def _parse_query_params(self, collection_formats, query_params):
        query_params = self.post_process_params(query_params) or []
        if query_params:
            query_params = http_utils.sanitize_for_serialization(query_params)
            query_params = http_utils.parameters_to_tuples(query_params, collection_formats)
        return query_params

    def _parse_post_params(self, collection_formats, post_params):
        post_params = self.post_process_params(post_params) if post_params else {}
        if post_params:
            post_params = http_utils.sanitize_for_serialization(post_params)
            post_params = http_utils.parameters_to_tuples(post_params, collection_formats)
        return post_params

    @classmethod
    def _parse_xml_body(cls, body):
        root_name = getattr(body, cls._XML_NAME) if hasattr(body, cls._XML_NAME) else body.__class__.__name__
        _dict = {root_name: http_utils.sanitize_for_serialization(body)}
        return XmlTransfer().to_string(_dict)

    @classmethod
    def _parse_body(cls, body, post_params):
        if body:
            if six.PY3:
                from typing import Mapping
                if all([hasattr(body, '__iter__'), not isinstance(body, (str, bytes, list, tuple, Mapping))]):
                    return body
            else:
                if all([hasattr(body, '__iter__'), not isinstance(body, (str, bytes, list, tuple, dict))]):
                    return body
            body = http_utils.sanitize_for_serialization(body)
            body = json.dumps(body, use_decimal=True)
        elif len(post_params) != 0:
            body = post_params
        else:
            body = ""
        return body

    @classmethod
    def _parse_formdata_body(cls, body):
        if not body:
            body = {}
        body = http_utils.sanitize_for_serialization(body)

        fields = OrderedDict()
        files = []
        for key, value in body.items():
            if isinstance(value, FormFile):
                files.append((key, value))
            else:
                fields[key] = str(value)
        for file_tuple in files:
            fields[file_tuple[0]] = file_tuple[1].convert_to_file_tuple()

        multipart = MultipartEncoder(fields=fields)
        return multipart

    def _is_stream(self, response_type):
        if type(response_type) == str and hasattr(self.model_package, response_type):
            klass = getattr(self.model_package, response_type)
            if issubclass(klass, SdkStreamResponse):
                return True
        return False

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
        return None

    def _url_parse(self, cname):
        parse_result = urlparse(self._endpoints[self._endpoint_index])
        if cname:
            endpoint = "%s://%s.%s" % (parse_result.scheme, cname, parse_result.netloc)
            parse_result = urlparse(endpoint)
        return parse_result

    def do_http_request(self, method, resource_path, path_params=None, query_params=None, header_params=None,
                        body=None, post_params=None, cname=None, response_type=None, response_headers=None,
                        collection_formats=None, request_type=None, async_request=False):

        if async_request:
            future_request = self.build_future_request(method, resource_path, path_params, query_params, header_params,
                                                       body, post_params, cname, response_type, collection_formats)
            future_response = self._http_client.executor.submit(self._do_http_request_async, future_request,
                                                                response_type, response_headers)
            return FutureSdkResponse(future_response, self._logger)

        while True:
            try:
                request = self.build_future_request(method, resource_path, path_params, query_params, header_params,
                                                    body, post_params, cname, response_type,
                                                    collection_formats).result()
                response = self._do_http_request_sync(request)
                break
            except HostUnreachableException as e:
                with self._mutex:
                    if self._endpoint_index < len(self._endpoints) - 1:
                        self._endpoint_index += 1
                    else:
                        self._endpoint_index = 0
                        raise e

        return self.sync_response_handler(response, response_type, response_headers)

    def build_future_request(self, method, resource_path, path_params, query_params, header_params,
                             request_body, post_params, cname, response_type, collection_formats):
        url_parse_result = self._url_parse(cname)
        schema = url_parse_result.scheme
        host = url_parse_result.netloc

        header_params = self._parse_header_params(collection_formats, header_params)
        resource_path = self._parse_path_params(collection_formats, path_params, resource_path,
                                                self._credentials.get_update_path_params())
        query_params = self._parse_query_params(collection_formats, query_params)
        post_params = self._parse_post_params(collection_formats, post_params)

        content_type = header_params.setdefault(self._CONTENT_TYPE, self._APPLICATION_JSON)
        if content_type == self._MULTIPART_FORM_DATA:
            body = self._parse_formdata_body(request_body)
            header_params[self._CONTENT_TYPE] = body.content_type
        elif content_type == self._APPLICATION_XML:
            body = self._parse_xml_body(request_body)
        elif content_type == self._APPLICATION_OCTET_STREAM:
            body = request_body
        else:
            body = self._parse_body(request_body, post_params)

        stream = self._is_stream(response_type)
        sdk_request = SdkRequest(method=method, schema=schema, host=host, resource_path=resource_path,
                                 query_params=query_params, header_params=header_params, body=body, stream=stream)
        if self._AUTHORIZATION not in header_params:
            return self._credentials.process_auth_request(sdk_request, self._http_client)
        else:
            return self._http_client.executor.submit(lambda: sdk_request)

    def _do_http_request_sync(self, request):
        response = self._http_client.do_request_sync(request)
        return response

    def _do_http_request_async(self, future_request, response_type, response_headers):
        request = future_request.result()
        future_response = self._http_client.do_request_async(
            request=request, hooks=[self.async_response_hook_factory(response_type, response_headers)]
        )
        return future_response

    def sync_response_handler(self, response, response_type, response_headers):
        return_data = self.deserialize(response, response_type)
        self.set_response_status_code(return_data, response)
        if response_headers is not None and len(response_headers) > 0:
            self.set_response_headers(return_data, response, response_headers)

        if not issubclass(return_data.__class__, SdkStreamResponse):
            return_data.raw_content = response.content

        return return_data

    def async_response_hook_factory(self, response_type, response_headers):
        def response_hook(resp, *args, **kwargs):
            resp.data = self.sync_response_handler(resp, response_type, response_headers)

        return response_hook

    @classmethod
    def set_response_status_code(cls, return_data, response):
        setattr(return_data, "status_code", response.status_code)

    @classmethod
    def set_response_headers(cls, return_data, response, response_headers):
        if not hasattr(return_data, "attribute_map"):
            return

        for attr in return_data.attribute_map:
            if getattr(return_data, attr) is not None:
                continue
            key_in_response_headers = return_data.attribute_map[attr]
            if key_in_response_headers in response_headers and key_in_response_headers in response.headers:
                setattr(return_data, attr, response.headers[key_in_response_headers])

    def deserialize(self, response, response_type):
        if type(response_type) == str and hasattr(self.model_package, response_type):
            klass = getattr(self.model_package, response_type)
            if issubclass(klass, SdkStreamResponse):
                return klass(response)

        try:
            if hasattr(response, self._HEADERS) and response.headers.get(self._CONTENT_TYPE) == self._APPLICATION_XML:
                data = XmlTransfer().to_dict(response.content, ignore_root=True)
            else:
                data = json.loads(six.ensure_str(response.text), parse_float=decimal.Decimal)
        except ValueError:
            data = response.text
        return self._deserialize(data, response_type)

    def _deserialize(self, data, klass):
        if data is None:
            return None

        if type(klass) == str:
            if klass.startswith('list['):
                if not isinstance(data, list):
                    data = [data]
                sub_kls = re.match(r'list\[(.*)\]', klass).group(1)
                return [self._deserialize(sub_data, sub_kls)
                        for sub_data in data]

            if klass.startswith('dict('):
                sub_kls = re.match(r'dict\(([^,]*), (.*)\)', klass).group(2)
                return {k: self._deserialize(v, sub_kls)
                        for k, v in six.iteritems(data)}

            if klass in native_types_mapping:
                klass = native_types_mapping[klass]
            elif klass == FormFile.TYPE:
                return FormFile(open(data, "rb"))
            else:
                klass = getattr(self.model_package, klass)

        if klass in primitive_types:
            return self._deserialize_primitive(data, klass)
        elif klass == decimal.Decimal:
            return data
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
            return parse(string if string.endswith("Z") else string + "Z").date()
        except ImportError:
            return string
        except ValueError:
            return string

    @classmethod
    def _deserialize_data_time(cls, string):
        try:
            from dateutil.parser import parse
            return parse(string if string.endswith("Z") else string + "Z")
        except ImportError:
            return string
        except ValueError:
            return string

    def _deserialize_model(self, data, klass):
        if not klass.openapi_types and not hasattr(klass, 'get_real_child_model'):
            if type(data) == int and hasattr(klass, "_%s" % data):
                return getattr(klass, "_%s" % data)
            if type(data) == str and hasattr(klass, re.sub(r'\W+', '_', data).upper()):
                return getattr(klass, re.sub(r'\W+', '_', data).upper())
            if type(data) == bool and hasattr(klass, str(data).upper()):
                return getattr(klass, str(data).upper())
            if type(data) == float and hasattr(klass, ("_%s" % data).replace('.', '_')):
                return getattr(klass, ("_%s" % data).replace('.', '_'))
            return klass()

        kwargs = {}
        if klass.openapi_types is not None:
            for attr, attr_type in six.iteritems(klass.openapi_types):
                if data is not None and isinstance(data, (list, dict)):
                    if klass.attribute_map[attr] == "body":
                        kwargs[attr] = self._deserialize(data, attr_type)
                    if klass.attribute_map[attr] in data:
                        value = data[klass.attribute_map[attr]]
                        kwargs[attr] = self._deserialize(value, attr_type)

        instance = klass(**kwargs)

        if hasattr(instance, 'get_real_child_model'):
            klass_name = instance.get_real_child_model(data)
            if klass_name:
                instance = self._deserialize(data, klass_name)
        return instance
