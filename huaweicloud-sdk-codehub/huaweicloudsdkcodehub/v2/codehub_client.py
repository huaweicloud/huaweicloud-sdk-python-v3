#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: JeffreyDin
@license: 
@contact: dingjianfeng15@gmail.com
@software: 
@file: codehub_client.py
@ide: PyCharm
@time: 2021/5/18 18:47
@desc：
"""
from __future__ import absolute_import

import datetime
import re
import importlib

import six

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class CodeHubClient(Client):
    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def __init__(self):
        super(CodeHubClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcodehub.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "CodeHubClient":
            raise TypeError("client type error, support client type is CodeHubClient")

        return ClientBuilder(clazz)

    def create_repository(self, request):
        """创建仓库

        :param request: CreateRepositoryRequest
        :return: CreateRepositoryResponse
        """
        return self.create_repository_with_http_info(request)

    def create_repository_with_http_info(self, request):
        """创建仓库

        :param request: CreateRepositoryRequest
        :return: CreateRepositoryResponse
        """

        all_params = ['create_repository_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/repositories',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateRepositoryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def get_all_repository_by_projectid(self, request):
        """查询项目下的所有仓库

        :param request: GetAllRepositoryByProjectId2Request
        :return: GetAllRepositoryByProjectId2Response
        """
        return self.get_all_repository_by_projectid_with_http_info(request)

    def get_all_repository_by_projectid_with_http_info(self, request):
        """查询项目下的所有仓库

        :param request: GetAllRepositoryByProjectId2Request
        :return: GetAllRepositoryByProjectId2Response
        """
        all_params = ['project_uuid', 'page_index', 'page_size', 'search']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_uuid' in local_var_params:
            path_params['project_uuid'] = local_var_params['project_uuid']
        if 'page_index' in local_var_params:
            path_params['page_index'] = local_var_params['page_index']
        if 'page_size' in local_var_params:
            path_params['page_size'] = local_var_params['page_size']
        if 'search' in local_var_params:
            path_params['search'] = local_var_params['search']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/projects/{project_uuid}/repositories',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='GetAllRepositoryByProjectId2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response_type: Response data type.
        :param response_headers: Header should be added to response data.
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param request_type: Request data type.
        :return:
            Return the response directly.
        """
        return self.do_http_request(
            method=method,
            resource_path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
            post_params=post_params,
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type)
