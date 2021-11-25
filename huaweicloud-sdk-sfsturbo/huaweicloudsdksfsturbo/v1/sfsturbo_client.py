# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

import six

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class SFSTurboClient(Client):
    """
    :param configuration: .Configuration object for this client
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

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
        super(SFSTurboClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdksfsturbo.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "SFSTurboClient":
            raise TypeError("client type error, support client type is SFSTurboClient")

        return ClientBuilder(clazz)

    def batch_add_shared_tags(self, request):
        """批量添加共享标签

        指定共享批量添加标签。  一个共享上最多有10个标签。 一个共享上的多个标签的key不允许重复。 此接口为幂等接口：如果要添加的key在共享上已存在，则覆盖更新标签。

        :param BatchAddSharedTagsRequest request
        :return: BatchAddSharedTagsResponse
        """
        return self.batch_add_shared_tags_with_http_info(request)

    def batch_add_shared_tags_with_http_info(self, request):
        """批量添加共享标签

        指定共享批量添加标签。  一个共享上最多有10个标签。 一个共享上的多个标签的key不允许重复。 此接口为幂等接口：如果要添加的key在共享上已存在，则覆盖更新标签。

        :param BatchAddSharedTagsRequest request
        :return: BatchAddSharedTagsResponse
        """

        all_params = ['share_id', 'add_shareed_tags']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/sfs-turbo/{share_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchAddSharedTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def change_security_group(self, request):
        """修改文件系统绑定的安全组

        修改SFS Turbo文件系统绑定的安全组。修改安全组为异步任务，可以通过“查询单个文件系统”返回的子状态字段“sub_status”来判断是否修改安全组状态，子状态为“232”即为修改安全组成功。

        :param ChangeSecurityGroupRequest request
        :return: ChangeSecurityGroupResponse
        """
        return self.change_security_group_with_http_info(request)

    def change_security_group_with_http_info(self, request):
        """修改文件系统绑定的安全组

        修改SFS Turbo文件系统绑定的安全组。修改安全组为异步任务，可以通过“查询单个文件系统”返回的子状态字段“sub_status”来判断是否修改安全组状态，子状态为“232”即为修改安全组成功。

        :param ChangeSecurityGroupRequest request
        :return: ChangeSecurityGroupResponse
        """

        all_params = ['share_id', 'change_security_group']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/sfs-turbo/shares/{share_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ChangeSecurityGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_share(self, request):
        """创建文件系统

        创建文件系统。

        :param CreateShareRequest request
        :return: CreateShareResponse
        """
        return self.create_share_with_http_info(request)

    def create_share_with_http_info(self, request):
        """创建文件系统

        创建文件系统。

        :param CreateShareRequest request
        :return: CreateShareResponse
        """

        all_params = ['share']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/sfs-turbo/shares',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateShareResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_shared_tag(self, request):
        """创建共享标签

        指定共享添加一个标签。 一个共享上最多有10个标签。 一个共享上的多个标签的key不允许重复。 此接口为幂等接口：如果要添加的key在共享上已存在，则覆盖更新标签。

        :param CreateSharedTagRequest request
        :return: CreateSharedTagResponse
        """
        return self.create_shared_tag_with_http_info(request)

    def create_shared_tag_with_http_info(self, request):
        """创建共享标签

        指定共享添加一个标签。 一个共享上最多有10个标签。 一个共享上的多个标签的key不允许重复。 此接口为幂等接口：如果要添加的key在共享上已存在，则覆盖更新标签。

        :param CreateSharedTagRequest request
        :return: CreateSharedTagResponse
        """

        all_params = ['share_id', 'tag']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/sfs-turbo/{share_id}/tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateSharedTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_share(self, request):
        """删除文件系统

        删除文件系统。

        :param DeleteShareRequest request
        :return: DeleteShareResponse
        """
        return self.delete_share_with_http_info(request)

    def delete_share_with_http_info(self, request):
        """删除文件系统

        删除文件系统。

        :param DeleteShareRequest request
        :return: DeleteShareResponse
        """

        all_params = ['share_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

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
            resource_path='/v1/{project_id}/sfs-turbo/shares/{share_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteShareResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_shared_tag(self, request):
        """删除共享标签

        指定共享删除一个标签。当共享中不存在指定要删除的key时，接口调用将会返回404错误。

        :param DeleteSharedTagRequest request
        :return: DeleteSharedTagResponse
        """
        return self.delete_shared_tag_with_http_info(request)

    def delete_shared_tag_with_http_info(self, request):
        """删除共享标签

        指定共享删除一个标签。当共享中不存在指定要删除的key时，接口调用将会返回404错误。

        :param DeleteSharedTagRequest request
        :return: DeleteSharedTagResponse
        """

        all_params = ['share_id', 'key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']

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
            resource_path='/v1/{project_id}/sfs-turbo/{share_id}/tags/{key}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteSharedTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def expand_share(self, request):
        """扩容文件系统

        扩容文件系统。

        :param ExpandShareRequest request
        :return: ExpandShareResponse
        """
        return self.expand_share_with_http_info(request)

    def expand_share_with_http_info(self, request):
        """扩容文件系统

        扩容文件系统。

        :param ExpandShareRequest request
        :return: ExpandShareResponse
        """

        all_params = ['share_id', 'extend']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/sfs-turbo/shares/{share_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ExpandShareResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_shared_tags(self, request):
        """查询租户所有共享的标签

        查询租户所有共享的标签集合。

        :param ListSharedTagsRequest request
        :return: ListSharedTagsResponse
        """
        return self.list_shared_tags_with_http_info(request)

    def list_shared_tags_with_http_info(self, request):
        """查询租户所有共享的标签

        查询租户所有共享的标签集合。

        :param ListSharedTagsRequest request
        :return: ListSharedTagsResponse
        """

        all_params = []
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
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/sfs-turbo/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSharedTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_shares(self, request):
        """获取文件系统列表

        获取文件系统列表

        :param ListSharesRequest request
        :return: ListSharesResponse
        """
        return self.list_shares_with_http_info(request)

    def list_shares_with_http_info(self, request):
        """获取文件系统列表

        获取文件系统列表

        :param ListSharesRequest request
        :return: ListSharesResponse
        """

        all_params = ['limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v1/{project_id}/sfs-turbo/shares/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSharesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_share(self, request):
        """查询文件系统详细信息

        查询SFS Turbo文件系统详细信息。

        :param ShowShareRequest request
        :return: ShowShareResponse
        """
        return self.show_share_with_http_info(request)

    def show_share_with_http_info(self, request):
        """查询文件系统详细信息

        查询SFS Turbo文件系统详细信息。

        :param ShowShareRequest request
        :return: ShowShareResponse
        """

        all_params = ['share_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

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
            resource_path='/v1/{project_id}/sfs-turbo/shares/{share_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowShareResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_shared_tags(self, request):
        """查询共享标签

        查询指定共享的所有标签信息。

        :param ShowSharedTagsRequest request
        :return: ShowSharedTagsResponse
        """
        return self.show_shared_tags_with_http_info(request)

    def show_shared_tags_with_http_info(self, request):
        """查询共享标签

        查询指定共享的所有标签信息。

        :param ShowSharedTagsRequest request
        :return: ShowSharedTagsResponse
        """

        all_params = ['share_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

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
            resource_path='/v1/{project_id}/sfs-turbo/{share_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowSharedTagsResponse',
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
