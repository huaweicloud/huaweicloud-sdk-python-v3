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


class EcsAsyncClient(Client):
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
        super(EcsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkecs.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "EcsClient":
            raise TypeError("client type error, support client type is EcsClient")

        return ClientBuilder(clazz)

    def add_server_group_member_async(self, request):
        """云服务器组添加成员

        将云服务器加入云服务器组。添加成功后，如果该云服务器组是反亲和性策略的，则该云服务器与云服务器组中的其他成员尽量分散地创建在不同主机上。如果该云服务器时故障域类型的，则该云服务器会拥有故障域属性。

        :param AddServerGroupMemberRequest request
        :return: AddServerGroupMemberResponse
        """
        return self.add_server_group_member_with_http_info(request)

    def add_server_group_member_with_http_info(self, request):
        """云服务器组添加成员

        将云服务器加入云服务器组。添加成功后，如果该云服务器组是反亲和性策略的，则该云服务器与云服务器组中的其他成员尽量分散地创建在不同主机上。如果该云服务器时故障域类型的，则该云服务器会拥有故障域属性。

        :param AddServerGroupMemberRequest request
        :return: AddServerGroupMemberResponse
        """

        all_params = ['server_group_id', 'add_server_group_member_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_group_id' in local_var_params:
            path_params['server_group_id'] = local_var_params['server_group_id']

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
            resource_path='/v1/{project_id}/cloudservers/os-server-groups/{server_group_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddServerGroupMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def attach_server_volume_async(self, request):
        """弹性云服务器挂载磁盘

        把磁盘挂载到弹性云服务器上。

        :param AttachServerVolumeRequest request
        :return: AttachServerVolumeResponse
        """
        return self.attach_server_volume_with_http_info(request)

    def attach_server_volume_with_http_info(self, request):
        """弹性云服务器挂载磁盘

        把磁盘挂载到弹性云服务器上。

        :param AttachServerVolumeRequest request
        :return: AttachServerVolumeResponse
        """

        all_params = ['server_id', 'attach_server_volume_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/attachvolume',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AttachServerVolumeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_add_server_nics_async(self, request):
        """批量添加云服务器网卡

        给云服务器添加一张或多张网卡。

        :param BatchAddServerNicsRequest request
        :return: BatchAddServerNicsResponse
        """
        return self.batch_add_server_nics_with_http_info(request)

    def batch_add_server_nics_with_http_info(self, request):
        """批量添加云服务器网卡

        给云服务器添加一张或多张网卡。

        :param BatchAddServerNicsRequest request
        :return: BatchAddServerNicsResponse
        """

        all_params = ['server_id', 'batch_add_server_nics_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/nics',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchAddServerNicsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_create_server_tags_async(self, request):
        """批量添加云服务器标签

        - 为指定云服务器批量添加标签。  - 标签管理服务TMS使用该接口批量管理云服务器的标签。

        :param BatchCreateServerTagsRequest request
        :return: BatchCreateServerTagsResponse
        """
        return self.batch_create_server_tags_with_http_info(request)

    def batch_create_server_tags_with_http_info(self, request):
        """批量添加云服务器标签

        - 为指定云服务器批量添加标签。  - 标签管理服务TMS使用该接口批量管理云服务器的标签。

        :param BatchCreateServerTagsRequest request
        :return: BatchCreateServerTagsResponse
        """

        all_params = ['server_id', 'batch_create_server_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchCreateServerTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_delete_server_nics_async(self, request):
        """批量删除云服务器网卡

        卸载并删除云服务器中的一张或多张网卡。

        :param BatchDeleteServerNicsRequest request
        :return: BatchDeleteServerNicsResponse
        """
        return self.batch_delete_server_nics_with_http_info(request)

    def batch_delete_server_nics_with_http_info(self, request):
        """批量删除云服务器网卡

        卸载并删除云服务器中的一张或多张网卡。

        :param BatchDeleteServerNicsRequest request
        :return: BatchDeleteServerNicsResponse
        """

        all_params = ['server_id', 'batch_delete_server_nics_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/nics/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteServerNicsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_delete_server_tags_async(self, request):
        """批量删除云服务器标签

        - 为指定云服务器批量删除标签。  - 标签管理服务TMS使用该接口批量管理云服务器的标签。

        :param BatchDeleteServerTagsRequest request
        :return: BatchDeleteServerTagsResponse
        """
        return self.batch_delete_server_tags_with_http_info(request)

    def batch_delete_server_tags_with_http_info(self, request):
        """批量删除云服务器标签

        - 为指定云服务器批量删除标签。  - 标签管理服务TMS使用该接口批量管理云服务器的标签。

        :param BatchDeleteServerTagsRequest request
        :return: BatchDeleteServerTagsResponse
        """

        all_params = ['server_id', 'batch_delete_server_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteServerTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_reboot_servers_async(self, request):
        """批量重启云服务器

        根据给定的云服务器ID列表，批量重启云服务器，一次最多可以重启1000台。

        :param BatchRebootServersRequest request
        :return: BatchRebootServersResponse
        """
        return self.batch_reboot_servers_with_http_info(request)

    def batch_reboot_servers_with_http_info(self, request):
        """批量重启云服务器

        根据给定的云服务器ID列表，批量重启云服务器，一次最多可以重启1000台。

        :param BatchRebootServersRequest request
        :return: BatchRebootServersResponse
        """

        all_params = ['batch_reboot_servers_request_body']
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
            resource_path='/v1/{project_id}/cloudservers/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchRebootServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_start_servers_async(self, request):
        """批量启动云服务器

        根据给定的云服务器ID列表，批量启动云服务器，一次最多可以启动1000台。

        :param BatchStartServersRequest request
        :return: BatchStartServersResponse
        """
        return self.batch_start_servers_with_http_info(request)

    def batch_start_servers_with_http_info(self, request):
        """批量启动云服务器

        根据给定的云服务器ID列表，批量启动云服务器，一次最多可以启动1000台。

        :param BatchStartServersRequest request
        :return: BatchStartServersResponse
        """

        all_params = ['batch_start_servers_request_body']
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
            resource_path='/v1/{project_id}/cloudservers/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchStartServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_stop_servers_async(self, request):
        """批量关闭云服务器

        根据给定的云服务器ID列表，批量关闭云服务器，一次最多可以关闭1000台。

        :param BatchStopServersRequest request
        :return: BatchStopServersResponse
        """
        return self.batch_stop_servers_with_http_info(request)

    def batch_stop_servers_with_http_info(self, request):
        """批量关闭云服务器

        根据给定的云服务器ID列表，批量关闭云服务器，一次最多可以关闭1000台。

        :param BatchStopServersRequest request
        :return: BatchStopServersResponse
        """

        all_params = ['batch_stop_servers_request_body']
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
            resource_path='/v1/{project_id}/cloudservers/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchStopServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def change_server_os_with_cloud_init_async(self, request):
        """切换弹性云服务器操作系统(安装Cloud init)

        切换弹性云服务器操作系统。支持弹性云服务器数据盘不变的情况下，使用新镜像重装系统盘。  调用该接口后，系统将卸载系统盘，然后使用新镜像重新创建系统盘，并挂载至弹性云服务器，实现切换操作系统功能。

        :param ChangeServerOsWithCloudInitRequest request
        :return: ChangeServerOsWithCloudInitResponse
        """
        return self.change_server_os_with_cloud_init_with_http_info(request)

    def change_server_os_with_cloud_init_with_http_info(self, request):
        """切换弹性云服务器操作系统(安装Cloud init)

        切换弹性云服务器操作系统。支持弹性云服务器数据盘不变的情况下，使用新镜像重装系统盘。  调用该接口后，系统将卸载系统盘，然后使用新镜像重新创建系统盘，并挂载至弹性云服务器，实现切换操作系统功能。

        :param ChangeServerOsWithCloudInitRequest request
        :return: ChangeServerOsWithCloudInitResponse
        """

        all_params = ['server_id', 'change_server_os_with_cloud_init_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v2/{project_id}/cloudservers/{server_id}/changeos',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ChangeServerOsWithCloudInitResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_post_paid_servers_async(self, request):
        """创建云服务器(按需)

        创建一台或多台按需付费方式的云服务器。  弹性云服务器的登录鉴权方式包括两种：密钥对、密码。为安全起见，推荐使用密钥对方式。  - 密钥对 密钥对指使用密钥对作为弹性云服务器的鉴权方式。 接口调用方法：使用key_name字段，指定弹性云服务器登录时使用的密钥文件。  - 密码 密码指使用设置初始密码方式作为弹性云服务器的鉴权方式，此时，您可以通过用户名密码方式登录弹性云服务器，Linux操作系统时为root用户的初始密码，Windows操作系统时为Administrator用户的初始密码。  接口调用方法：使用adminPass字段，指定管理员帐号的初始登录密码。对于镜像已安装Cloud-init的Linux云服务器，如果需要使用密文密码，可以使用user_data字段进行密码注入。  > 对于安装Cloud-init镜像的Linux云服务器云主机，若指定user_data字段，则adminPass字段无效。

        :param CreatePostPaidServersRequest request
        :return: CreatePostPaidServersResponse
        """
        return self.create_post_paid_servers_with_http_info(request)

    def create_post_paid_servers_with_http_info(self, request):
        """创建云服务器(按需)

        创建一台或多台按需付费方式的云服务器。  弹性云服务器的登录鉴权方式包括两种：密钥对、密码。为安全起见，推荐使用密钥对方式。  - 密钥对 密钥对指使用密钥对作为弹性云服务器的鉴权方式。 接口调用方法：使用key_name字段，指定弹性云服务器登录时使用的密钥文件。  - 密码 密码指使用设置初始密码方式作为弹性云服务器的鉴权方式，此时，您可以通过用户名密码方式登录弹性云服务器，Linux操作系统时为root用户的初始密码，Windows操作系统时为Administrator用户的初始密码。  接口调用方法：使用adminPass字段，指定管理员帐号的初始登录密码。对于镜像已安装Cloud-init的Linux云服务器，如果需要使用密文密码，可以使用user_data字段进行密码注入。  > 对于安装Cloud-init镜像的Linux云服务器云主机，若指定user_data字段，则adminPass字段无效。

        :param CreatePostPaidServersRequest request
        :return: CreatePostPaidServersResponse
        """

        all_params = ['create_post_paid_servers_request_body']
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
            resource_path='/v1/{project_id}/cloudservers',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreatePostPaidServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_server_group_async(self, request):
        """创建云服务器组

        创建弹性云服务器组。  与原生的创建云服务器组接口不同之处在于该接口支持企业项目细粒度权限的校验。

        :param CreateServerGroupRequest request
        :return: CreateServerGroupResponse
        """
        return self.create_server_group_with_http_info(request)

    def create_server_group_with_http_info(self, request):
        """创建云服务器组

        创建弹性云服务器组。  与原生的创建云服务器组接口不同之处在于该接口支持企业项目细粒度权限的校验。

        :param CreateServerGroupRequest request
        :return: CreateServerGroupResponse
        """

        all_params = ['create_server_group_request_body']
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
            resource_path='/v1/{project_id}/cloudservers/os-server-groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateServerGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_servers_async(self, request):
        """创建云服务器

        创建一台或多台云服务器。  指该接口兼容《弹性云服务器接口参考》创建云服务器v1的功能，同时合入新功能，支持创建包年/包月的弹性云服务器。  弹性云服务器的登录鉴权方式包括两种：密钥对、密码。为安全起见，推荐使用密钥对方式。  - 密钥对  指使用密钥对作为弹性云服务器的鉴权方式。  接口调用方法：使用key_name字段，指定弹性云服务器登录时使用的密钥文件。  - 密码  指使用设置初始密码方式作为弹性云服务器的鉴权方式，此时，您可以通过用户名密码方式登录弹性云服务器，Linux操作系统时为root用户的初始密码，Windows操作系统时为Administrator用户的初始密码。  接口调用方法：使用adminPass字段，指定管理员帐号的初始登录密码。对于镜像已安装Cloud-init的Linux云服务器，如果需要使用密文密码，可以使用user_data字段进行密码注入。  > 对于安装Cloud-init镜像的Linux云服务器云主机，若指定user_data字段，则adminPass字段无效。

        :param CreateServersRequest request
        :return: CreateServersResponse
        """
        return self.create_servers_with_http_info(request)

    def create_servers_with_http_info(self, request):
        """创建云服务器

        创建一台或多台云服务器。  指该接口兼容《弹性云服务器接口参考》创建云服务器v1的功能，同时合入新功能，支持创建包年/包月的弹性云服务器。  弹性云服务器的登录鉴权方式包括两种：密钥对、密码。为安全起见，推荐使用密钥对方式。  - 密钥对  指使用密钥对作为弹性云服务器的鉴权方式。  接口调用方法：使用key_name字段，指定弹性云服务器登录时使用的密钥文件。  - 密码  指使用设置初始密码方式作为弹性云服务器的鉴权方式，此时，您可以通过用户名密码方式登录弹性云服务器，Linux操作系统时为root用户的初始密码，Windows操作系统时为Administrator用户的初始密码。  接口调用方法：使用adminPass字段，指定管理员帐号的初始登录密码。对于镜像已安装Cloud-init的Linux云服务器，如果需要使用密文密码，可以使用user_data字段进行密码注入。  > 对于安装Cloud-init镜像的Linux云服务器云主机，若指定user_data字段，则adminPass字段无效。

        :param CreateServersRequest request
        :return: CreateServersResponse
        """

        all_params = ['create_servers_request_body']
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
            resource_path='/v1.1/{project_id}/cloudservers',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_server_group_async(self, request):
        """删除云服务器组

        删除云服务器组。  与原生的删除云服务器组接口不同之处在于该接口支持企业项目细粒度权限的校验。

        :param DeleteServerGroupRequest request
        :return: DeleteServerGroupResponse
        """
        return self.delete_server_group_with_http_info(request)

    def delete_server_group_with_http_info(self, request):
        """删除云服务器组

        删除云服务器组。  与原生的删除云服务器组接口不同之处在于该接口支持企业项目细粒度权限的校验。

        :param DeleteServerGroupRequest request
        :return: DeleteServerGroupResponse
        """

        all_params = ['server_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_group_id' in local_var_params:
            path_params['server_group_id'] = local_var_params['server_group_id']

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
            resource_path='/v1/{project_id}/cloudservers/os-server-groups/{server_group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteServerGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_server_group_member_async(self, request):
        """云服务器组删除成员

        将弹性云服务器移出云服务器组。移出后，该云服务器与云服务器组中的成员不再遵从反亲和策略。

        :param DeleteServerGroupMemberRequest request
        :return: DeleteServerGroupMemberResponse
        """
        return self.delete_server_group_member_with_http_info(request)

    def delete_server_group_member_with_http_info(self, request):
        """云服务器组删除成员

        将弹性云服务器移出云服务器组。移出后，该云服务器与云服务器组中的成员不再遵从反亲和策略。

        :param DeleteServerGroupMemberRequest request
        :return: DeleteServerGroupMemberResponse
        """

        all_params = ['server_group_id', 'delete_server_group_member_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_group_id' in local_var_params:
            path_params['server_group_id'] = local_var_params['server_group_id']

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
            resource_path='/v1/{project_id}/cloudservers/os-server-groups/{server_group_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteServerGroupMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_server_metadata_async(self, request):
        """删除云服务器指定元数据

        删除云服务器指定元数据。

        :param DeleteServerMetadataRequest request
        :return: DeleteServerMetadataResponse
        """
        return self.delete_server_metadata_with_http_info(request)

    def delete_server_metadata_with_http_info(self, request):
        """删除云服务器指定元数据

        删除云服务器指定元数据。

        :param DeleteServerMetadataRequest request
        :return: DeleteServerMetadataResponse
        """

        all_params = ['key', 'server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/metadata/{key}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteServerMetadataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_servers_async(self, request):
        """删除云服务器

        根据指定的云服务器ID列表，删除云服务器。  系统支持删除单台云服务器和批量删除多台云服务器操作，批量删除云服务器时，一次最多可以删除1000台。

        :param DeleteServersRequest request
        :return: DeleteServersResponse
        """
        return self.delete_servers_with_http_info(request)

    def delete_servers_with_http_info(self, request):
        """删除云服务器

        根据指定的云服务器ID列表，删除云服务器。  系统支持删除单台云服务器和批量删除多台云服务器操作，批量删除云服务器时，一次最多可以删除1000台。

        :param DeleteServersRequest request
        :return: DeleteServersResponse
        """

        all_params = ['delete_servers_request_body']
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
            resource_path='/v1/{project_id}/cloudservers/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def detach_server_volume_async(self, request):
        """弹性云服务器卸载磁盘

        从弹性云服务器中卸载磁盘。

        :param DetachServerVolumeRequest request
        :return: DetachServerVolumeResponse
        """
        return self.detach_server_volume_with_http_info(request)

    def detach_server_volume_with_http_info(self, request):
        """弹性云服务器卸载磁盘

        从弹性云服务器中卸载磁盘。

        :param DetachServerVolumeRequest request
        :return: DetachServerVolumeResponse
        """

        all_params = ['server_id', 'volume_id', 'delete_flag']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

        query_params = []
        if 'delete_flag' in local_var_params:
            query_params.append(('delete_flag', local_var_params['delete_flag']))

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/detachvolume/{volume_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DetachServerVolumeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_flavors_async(self, request):
        """查询规格详情和规格扩展信息列表

        查询云服务器规格详情信息和规格扩展信息列表。

        :param ListFlavorsRequest request
        :return: ListFlavorsResponse
        """
        return self.list_flavors_with_http_info(request)

    def list_flavors_with_http_info(self, request):
        """查询规格详情和规格扩展信息列表

        查询云服务器规格详情信息和规格扩展信息列表。

        :param ListFlavorsRequest request
        :return: ListFlavorsResponse
        """

        all_params = ['availability_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'availability_zone' in local_var_params:
            query_params.append(('availability_zone', local_var_params['availability_zone']))

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
            resource_path='/v1/{project_id}/cloudservers/flavors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListFlavorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_resize_flavors_async(self, request):
        """查询云服务器规格变更支持列表

        变更规格时，部分规格的云服务器之间不能互相变更。您可以通过本接口，通过指定弹性云服务器规格，查询该规格可以变更的规格列表。

        :param ListResizeFlavorsRequest request
        :return: ListResizeFlavorsResponse
        """
        return self.list_resize_flavors_with_http_info(request)

    def list_resize_flavors_with_http_info(self, request):
        """查询云服务器规格变更支持列表

        变更规格时，部分规格的云服务器之间不能互相变更。您可以通过本接口，通过指定弹性云服务器规格，查询该规格可以变更的规格列表。

        :param ListResizeFlavorsRequest request
        :return: ListResizeFlavorsResponse
        """

        all_params = ['instance_uuid', 'limit', 'marker', 'sort_dir', 'sort_key', 'source_flavor_id', 'source_flavor_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_uuid' in local_var_params:
            query_params.append(('instance_uuid', local_var_params['instance_uuid']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'source_flavor_id' in local_var_params:
            query_params.append(('source_flavor_id', local_var_params['source_flavor_id']))
        if 'source_flavor_name' in local_var_params:
            query_params.append(('source_flavor_name', local_var_params['source_flavor_name']))

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
            resource_path='/v1/{project_id}/cloudservers/resize_flavors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListResizeFlavorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_server_block_devices_async(self, request):
        """查询弹性云服务器磁盘信息

        查询弹性云服务器挂载的磁盘信息。

        :param ListServerBlockDevicesRequest request
        :return: ListServerBlockDevicesResponse
        """
        return self.list_server_block_devices_with_http_info(request)

    def list_server_block_devices_with_http_info(self, request):
        """查询弹性云服务器磁盘信息

        查询弹性云服务器挂载的磁盘信息。

        :param ListServerBlockDevicesRequest request
        :return: ListServerBlockDevicesResponse
        """

        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/block_device',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListServerBlockDevicesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_server_interfaces_async(self, request):
        """查询云服务器网卡信息

        查询云服务器网卡信息。

        :param ListServerInterfacesRequest request
        :return: ListServerInterfacesResponse
        """
        return self.list_server_interfaces_with_http_info(request)

    def list_server_interfaces_with_http_info(self, request):
        """查询云服务器网卡信息

        查询云服务器网卡信息。

        :param ListServerInterfacesRequest request
        :return: ListServerInterfacesResponse
        """

        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/os-interface',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListServerInterfacesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_servers_details_async(self, request):
        """查询云服务器详情列表

        根据用户请求条件从数据库筛选、查询所有的弹性云服务器，并关联相关表获取到弹性云服务器的详细信息。  该接口支持查询弹性云服务器计费方式，以及是否被冻结。

        :param ListServersDetailsRequest request
        :return: ListServersDetailsResponse
        """
        return self.list_servers_details_with_http_info(request)

    def list_servers_details_with_http_info(self, request):
        """查询云服务器详情列表

        根据用户请求条件从数据库筛选、查询所有的弹性云服务器，并关联相关表获取到弹性云服务器的详细信息。  该接口支持查询弹性云服务器计费方式，以及是否被冻结。

        :param ListServersDetailsRequest request
        :return: ListServersDetailsResponse
        """

        all_params = ['enterprise_project_id', 'flavor', 'ip', 'limit', 'name', 'not_tags', 'offset', 'reservation_id', 'status', 'tags']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'flavor' in local_var_params:
            query_params.append(('flavor', local_var_params['flavor']))
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'not_tags' in local_var_params:
            query_params.append(('not-tags', local_var_params['not_tags']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'reservation_id' in local_var_params:
            query_params.append(('reservation_id', local_var_params['reservation_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))

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
            resource_path='/v1/{project_id}/cloudservers/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListServersDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def nova_associate_security_group_async(self, request):
        """添加安全组

        为弹性云服务器添加一个安全组。  添加多个安全组时，建议最多为弹性云服务器添加5个安全组。

        :param NovaAssociateSecurityGroupRequest request
        :return: NovaAssociateSecurityGroupResponse
        """
        return self.nova_associate_security_group_with_http_info(request)

    def nova_associate_security_group_with_http_info(self, request):
        """添加安全组

        为弹性云服务器添加一个安全组。  添加多个安全组时，建议最多为弹性云服务器添加5个安全组。

        :param NovaAssociateSecurityGroupRequest request
        :return: NovaAssociateSecurityGroupResponse
        """

        all_params = ['server_id', 'nova_associate_security_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v2.1/{project_id}/servers/{server_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaAssociateSecurityGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def nova_create_keypair_async(self, request):
        """创建和导入SSH密钥

        创建SSH密钥，或把公钥导入系统，生成密钥对。  创建SSH密钥成功后，请把响应数据中的私钥内容保存到本地文件，用户使用该私钥登录云服务器云主机。为保证云服务器云主机器安全，私钥数据只能读取一次，请妥善保管。

        :param NovaCreateKeypairRequest request
        :return: NovaCreateKeypairResponse
        """
        return self.nova_create_keypair_with_http_info(request)

    def nova_create_keypair_with_http_info(self, request):
        """创建和导入SSH密钥

        创建SSH密钥，或把公钥导入系统，生成密钥对。  创建SSH密钥成功后，请把响应数据中的私钥内容保存到本地文件，用户使用该私钥登录云服务器云主机。为保证云服务器云主机器安全，私钥数据只能读取一次，请妥善保管。

        :param NovaCreateKeypairRequest request
        :return: NovaCreateKeypairResponse
        """

        all_params = ['nova_create_keypair_request_body', 'open_stack_api_version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'open_stack_api_version' in local_var_params:
            header_params['OpenStack-API-Version'] = local_var_params['open_stack_api_version']

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
            resource_path='/v2.1/{project_id}/os-keypairs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaCreateKeypairResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def nova_create_servers_async(self, request):
        """创建云服务器

        创建一台弹性云服务器。  弹性云服务器创建完成后，如需开启自动恢复功能，可以调用配置云服务器自动恢复的接口，具体使用请参见管理云服务器自动恢复动作。  该接口在云服务器创建失败后不支持自动回滚。若需要自动回滚能力，可以调用POST /v1/{project_id}/cloudservers接口，具体使用请参见创建云服务器（按需）。

        :param NovaCreateServersRequest request
        :return: NovaCreateServersResponse
        """
        return self.nova_create_servers_with_http_info(request)

    def nova_create_servers_with_http_info(self, request):
        """创建云服务器

        创建一台弹性云服务器。  弹性云服务器创建完成后，如需开启自动恢复功能，可以调用配置云服务器自动恢复的接口，具体使用请参见管理云服务器自动恢复动作。  该接口在云服务器创建失败后不支持自动回滚。若需要自动回滚能力，可以调用POST /v1/{project_id}/cloudservers接口，具体使用请参见创建云服务器（按需）。

        :param NovaCreateServersRequest request
        :return: NovaCreateServersResponse
        """

        all_params = ['nova_create_servers_request_body', 'open_stack_api_version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'open_stack_api_version' in local_var_params:
            header_params['OpenStack-API-Version'] = local_var_params['open_stack_api_version']

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
            resource_path='/v2.1/{project_id}/servers',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaCreateServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def nova_delete_keypair_async(self, request):
        """删除SSH密钥

        根据SSH密钥的名称，删除指定SSH密钥。

        :param NovaDeleteKeypairRequest request
        :return: NovaDeleteKeypairResponse
        """
        return self.nova_delete_keypair_with_http_info(request)

    def nova_delete_keypair_with_http_info(self, request):
        """删除SSH密钥

        根据SSH密钥的名称，删除指定SSH密钥。

        :param NovaDeleteKeypairRequest request
        :return: NovaDeleteKeypairResponse
        """

        all_params = ['keypair_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'keypair_name' in local_var_params:
            path_params['keypair_name'] = local_var_params['keypair_name']

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
            resource_path='/v2.1/{project_id}/os-keypairs/{keypair_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaDeleteKeypairResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def nova_delete_server_async(self, request):
        """删除云服务器

        删除一台云服务器。

        :param NovaDeleteServerRequest request
        :return: NovaDeleteServerResponse
        """
        return self.nova_delete_server_with_http_info(request)

    def nova_delete_server_with_http_info(self, request):
        """删除云服务器

        删除一台云服务器。

        :param NovaDeleteServerRequest request
        :return: NovaDeleteServerResponse
        """

        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v2.1/{project_id}/servers/{server_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaDeleteServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def nova_disassociate_security_group_async(self, request):
        """移除安全组

        移除弹性云服务器中的安全组。

        :param NovaDisassociateSecurityGroupRequest request
        :return: NovaDisassociateSecurityGroupResponse
        """
        return self.nova_disassociate_security_group_with_http_info(request)

    def nova_disassociate_security_group_with_http_info(self, request):
        """移除安全组

        移除弹性云服务器中的安全组。

        :param NovaDisassociateSecurityGroupRequest request
        :return: NovaDisassociateSecurityGroupResponse
        """

        all_params = ['server_id', 'nova_disassociate_security_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v2.1/{project_id}/servers/{server_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaDisassociateSecurityGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def nova_list_availability_zones_async(self, request):
        """查询可用区列表

        查询可用域列表。

        :param NovaListAvailabilityZonesRequest request
        :return: NovaListAvailabilityZonesResponse
        """
        return self.nova_list_availability_zones_with_http_info(request)

    def nova_list_availability_zones_with_http_info(self, request):
        """查询可用区列表

        查询可用域列表。

        :param NovaListAvailabilityZonesRequest request
        :return: NovaListAvailabilityZonesResponse
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
            resource_path='/v2.1/{project_id}/os-availability-zone',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaListAvailabilityZonesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def nova_list_keypairs_async(self, request):
        """查询SSH密钥列表

        查询SSH密钥信息列表。

        :param NovaListKeypairsRequest request
        :return: NovaListKeypairsResponse
        """
        return self.nova_list_keypairs_with_http_info(request)

    def nova_list_keypairs_with_http_info(self, request):
        """查询SSH密钥列表

        查询SSH密钥信息列表。

        :param NovaListKeypairsRequest request
        :return: NovaListKeypairsResponse
        """

        all_params = ['limit', 'marker', 'open_stack_api_version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}
        if 'open_stack_api_version' in local_var_params:
            header_params['OpenStack-API-Version'] = local_var_params['open_stack_api_version']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.1/{project_id}/os-keypairs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaListKeypairsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def nova_list_server_security_groups_async(self, request):
        """查询指定云服务器安全组列表

        查询指定弹性云服务器的安全组。

        :param NovaListServerSecurityGroupsRequest request
        :return: NovaListServerSecurityGroupsResponse
        """
        return self.nova_list_server_security_groups_with_http_info(request)

    def nova_list_server_security_groups_with_http_info(self, request):
        """查询指定云服务器安全组列表

        查询指定弹性云服务器的安全组。

        :param NovaListServerSecurityGroupsRequest request
        :return: NovaListServerSecurityGroupsResponse
        """

        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v2.1/{project_id}/servers/{server_id}/os-security-groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaListServerSecurityGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def nova_list_servers_details_async(self, request):
        """查询云服务器详情列表

        查询云服务器详情信息列表。

        :param NovaListServersDetailsRequest request
        :return: NovaListServersDetailsResponse
        """
        return self.nova_list_servers_details_with_http_info(request)

    def nova_list_servers_details_with_http_info(self, request):
        """查询云服务器详情列表

        查询云服务器详情信息列表。

        :param NovaListServersDetailsRequest request
        :return: NovaListServersDetailsResponse
        """

        all_params = ['changes_since', 'flavor', 'image', 'ip', 'limit', 'marker', 'name', 'not_tags', 'reservation_id', 'sort_key', 'status', 'tags', 'open_stack_api_version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'changes_since' in local_var_params:
            query_params.append(('changes-since', local_var_params['changes_since']))
        if 'flavor' in local_var_params:
            query_params.append(('flavor', local_var_params['flavor']))
        if 'image' in local_var_params:
            query_params.append(('image', local_var_params['image']))
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'not_tags' in local_var_params:
            query_params.append(('not-tags', local_var_params['not_tags']))
        if 'reservation_id' in local_var_params:
            query_params.append(('reservation_id', local_var_params['reservation_id']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))

        header_params = {}
        if 'open_stack_api_version' in local_var_params:
            header_params['OpenStack-API-Version'] = local_var_params['open_stack_api_version']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.1/{project_id}/servers/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaListServersDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def nova_show_keypair_async(self, request):
        """查询SSH密钥详情

        根据SSH密钥名称查询指定SSH密钥。

        :param NovaShowKeypairRequest request
        :return: NovaShowKeypairResponse
        """
        return self.nova_show_keypair_with_http_info(request)

    def nova_show_keypair_with_http_info(self, request):
        """查询SSH密钥详情

        根据SSH密钥名称查询指定SSH密钥。

        :param NovaShowKeypairRequest request
        :return: NovaShowKeypairResponse
        """

        all_params = ['keypair_name', 'open_stack_api_version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'keypair_name' in local_var_params:
            path_params['keypair_name'] = local_var_params['keypair_name']

        query_params = []

        header_params = {}
        if 'open_stack_api_version' in local_var_params:
            header_params['OpenStack-API-Version'] = local_var_params['open_stack_api_version']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.1/{project_id}/os-keypairs/{keypair_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaShowKeypairResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def nova_show_server_async(self, request):
        """查询云服务器详情

        根据云服务器ID，查询云服务器的详细信息。

        :param NovaShowServerRequest request
        :return: NovaShowServerResponse
        """
        return self.nova_show_server_with_http_info(request)

    def nova_show_server_with_http_info(self, request):
        """查询云服务器详情

        根据云服务器ID，查询云服务器的详细信息。

        :param NovaShowServerRequest request
        :return: NovaShowServerResponse
        """

        all_params = ['server_id', 'open_stack_api_version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}
        if 'open_stack_api_version' in local_var_params:
            header_params['OpenStack-API-Version'] = local_var_params['open_stack_api_version']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.1/{project_id}/servers/{server_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaShowServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def reinstall_server_with_cloud_init_async(self, request):
        """重装弹性云服务器操作系统(安装Cloud-init)

        重装弹性云服务器的操作系统。支持弹性云服务器数据盘不变的情况下，使用原镜像重装系统盘。  调用该接口后，系统将卸载系统盘，然后使用原镜像重新创建系统盘，并挂载至弹性云服务器，实现重装操作系统功能。

        :param ReinstallServerWithCloudInitRequest request
        :return: ReinstallServerWithCloudInitResponse
        """
        return self.reinstall_server_with_cloud_init_with_http_info(request)

    def reinstall_server_with_cloud_init_with_http_info(self, request):
        """重装弹性云服务器操作系统(安装Cloud-init)

        重装弹性云服务器的操作系统。支持弹性云服务器数据盘不变的情况下，使用原镜像重装系统盘。  调用该接口后，系统将卸载系统盘，然后使用原镜像重新创建系统盘，并挂载至弹性云服务器，实现重装操作系统功能。

        :param ReinstallServerWithCloudInitRequest request
        :return: ReinstallServerWithCloudInitResponse
        """

        all_params = ['server_id', 'reinstall_server_with_cloud_init_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v2/{project_id}/cloudservers/{server_id}/reinstallos',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ReinstallServerWithCloudInitResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def reset_server_password_async(self, request):
        """一键重置弹性云服务器密码(企业项目)

        重置弹性云服务器管理帐号（root用户或Administrator用户）的密码。

        :param ResetServerPasswordRequest request
        :return: ResetServerPasswordResponse
        """
        return self.reset_server_password_with_http_info(request)

    def reset_server_password_with_http_info(self, request):
        """一键重置弹性云服务器密码(企业项目)

        重置弹性云服务器管理帐号（root用户或Administrator用户）的密码。

        :param ResetServerPasswordRequest request
        :return: ResetServerPasswordResponse
        """

        all_params = ['server_id', 'reset_server_password_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/os-reset-password',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ResetServerPasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def resize_post_paid_server_async(self, request):
        """变更云服务器规格(按需)

        当您创建的弹性云服务器规格无法满足业务需要时，可以变更云服务器规格，升级vCPU、内存。具体接口的使用，请参见本节内容。  变更规格时，部分规格的云服务器之间不能互相变更。  您可以通过接口“/v1/{project_id}/cloudservers/resize_flavors?{instance_uuid,source_flavor_id,source_flavor_name}”查询支持列表。

        :param ResizePostPaidServerRequest request
        :return: ResizePostPaidServerResponse
        """
        return self.resize_post_paid_server_with_http_info(request)

    def resize_post_paid_server_with_http_info(self, request):
        """变更云服务器规格(按需)

        当您创建的弹性云服务器规格无法满足业务需要时，可以变更云服务器规格，升级vCPU、内存。具体接口的使用，请参见本节内容。  变更规格时，部分规格的云服务器之间不能互相变更。  您可以通过接口“/v1/{project_id}/cloudservers/resize_flavors?{instance_uuid,source_flavor_id,source_flavor_name}”查询支持列表。

        :param ResizePostPaidServerRequest request
        :return: ResizePostPaidServerResponse
        """

        all_params = ['server_id', 'resize_post_paid_server_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/resize',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ResizePostPaidServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def resize_server_async(self, request):
        """变更云服务器规格

        变更云服务器规格。  v1.1版本：指该接口兼容v1接口的功能，同时合入新功能，支持变更包年/包月弹性云服务器的规格。  注意事项：  - 该接口可以使用合作伙伴自身的AK/SK或者token调用，也可以用合作伙伴子客户的AK/SK或者token来调用。 - 如果使用AK/SK认证方式，示例代码中region请参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)中“弹性云服务 ECS”下“区域”的内容，，serviceName（英文服务名称缩写）请指定为ECS。 - Endpoint请参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)中“弹性云服务 ECS”下“终端节点（Endpoint）”的内容。

        :param ResizeServerRequest request
        :return: ResizeServerResponse
        """
        return self.resize_server_with_http_info(request)

    def resize_server_with_http_info(self, request):
        """变更云服务器规格

        变更云服务器规格。  v1.1版本：指该接口兼容v1接口的功能，同时合入新功能，支持变更包年/包月弹性云服务器的规格。  注意事项：  - 该接口可以使用合作伙伴自身的AK/SK或者token调用，也可以用合作伙伴子客户的AK/SK或者token来调用。 - 如果使用AK/SK认证方式，示例代码中region请参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)中“弹性云服务 ECS”下“区域”的内容，，serviceName（英文服务名称缩写）请指定为ECS。 - Endpoint请参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)中“弹性云服务 ECS”下“终端节点（Endpoint）”的内容。

        :param ResizeServerRequest request
        :return: ResizeServerResponse
        """

        all_params = ['server_id', 'resize_server_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1.1/{project_id}/cloudservers/{server_id}/resize',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ResizeServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_reset_password_flag_async(self, request):
        """查询是否支持一键重置密码

        查询弹性云服务器是否支持一键重置密码。

        :param ShowResetPasswordFlagRequest request
        :return: ShowResetPasswordFlagResponse
        """
        return self.show_reset_password_flag_with_http_info(request)

    def show_reset_password_flag_with_http_info(self, request):
        """查询是否支持一键重置密码

        查询弹性云服务器是否支持一键重置密码。

        :param ShowResetPasswordFlagRequest request
        :return: ShowResetPasswordFlagResponse
        """

        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/os-resetpwd-flag',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowResetPasswordFlagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_server_async(self, request):
        """查询云服务器详情

        查询弹性云服务器的详细信息。  该接口支持查询弹性云服务器的计费方式，以及是否被冻结。

        :param ShowServerRequest request
        :return: ShowServerResponse
        """
        return self.show_server_with_http_info(request)

    def show_server_with_http_info(self, request):
        """查询云服务器详情

        查询弹性云服务器的详细信息。  该接口支持查询弹性云服务器的计费方式，以及是否被冻结。

        :param ShowServerRequest request
        :return: ShowServerResponse
        """

        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_server_limits_async(self, request):
        """查询租户配额

        查询租户配额信息。

        :param ShowServerLimitsRequest request
        :return: ShowServerLimitsResponse
        """
        return self.show_server_limits_with_http_info(request)

    def show_server_limits_with_http_info(self, request):
        """查询租户配额

        查询租户配额信息。

        :param ShowServerLimitsRequest request
        :return: ShowServerLimitsResponse
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
            resource_path='/v1/{project_id}/cloudservers/limits',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowServerLimitsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_server_remote_console_async(self, request):
        """获取VNC远程登录地址

        获取弹性云服务器VNC远程登录地址。

        :param ShowServerRemoteConsoleRequest request
        :return: ShowServerRemoteConsoleResponse
        """
        return self.show_server_remote_console_with_http_info(request)

    def show_server_remote_console_with_http_info(self, request):
        """获取VNC远程登录地址

        获取弹性云服务器VNC远程登录地址。

        :param ShowServerRemoteConsoleRequest request
        :return: ShowServerRemoteConsoleResponse
        """

        all_params = ['server_id', 'show_server_remote_console_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/remote_console',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowServerRemoteConsoleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_server_tags_async(self, request):
        """查询云服务器标签

        - 查询指定云服务器的标签信息。  - 标签管理服务TMS使用该接口查询指定云服务器的全部标签数据。

        :param ShowServerTagsRequest request
        :return: ShowServerTagsResponse
        """
        return self.show_server_tags_with_http_info(request)

    def show_server_tags_with_http_info(self, request):
        """查询云服务器标签

        - 查询指定云服务器的标签信息。  - 标签管理服务TMS使用该接口查询指定云服务器的全部标签数据。

        :param ShowServerTagsRequest request
        :return: ShowServerTagsResponse
        """

        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowServerTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_auto_terminate_time_server_async(self, request):
        """修改云服务器云主机销毁时间

        修改按需服务器，设置定时销毁时间。如果设置的销毁时间为空，表示取消销毁时间。  该接口支持企业项目细粒度权限的校验，具体细粒度请参见 ecs:cloudServers:put。

        :param UpdateAutoTerminateTimeServerRequest request
        :return: UpdateAutoTerminateTimeServerResponse
        """
        return self.update_auto_terminate_time_server_with_http_info(request)

    def update_auto_terminate_time_server_with_http_info(self, request):
        """修改云服务器云主机销毁时间

        修改按需服务器，设置定时销毁时间。如果设置的销毁时间为空，表示取消销毁时间。  该接口支持企业项目细粒度权限的校验，具体细粒度请参见 ecs:cloudServers:put。

        :param UpdateAutoTerminateTimeServerRequest request
        :return: UpdateAutoTerminateTimeServerResponse
        """

        all_params = ['server_id', 'update_auto_terminate_time_server_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/actions/update-auto-terminate-time',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateAutoTerminateTimeServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_server_async(self, request):
        """修改云服务器

        修改云服务器信息，目前支持修改云服务器名称及描述和hostname。

        :param UpdateServerRequest request
        :return: UpdateServerResponse
        """
        return self.update_server_with_http_info(request)

    def update_server_with_http_info(self, request):
        """修改云服务器

        修改云服务器信息，目前支持修改云服务器名称及描述和hostname。

        :param UpdateServerRequest request
        :return: UpdateServerResponse
        """

        all_params = ['server_id', 'update_server_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_server_metadata_async(self, request):
        """更新云服务器元数据

        更新云服务器元数据。  - 如果元数据中没有待更新字段，则自动添加该字段。  - 如果元数据中已存在待更新字段，则直接更新字段值。  - 如果元数据中的字段不再请求参数中，则保持不变

        :param UpdateServerMetadataRequest request
        :return: UpdateServerMetadataResponse
        """
        return self.update_server_metadata_with_http_info(request)

    def update_server_metadata_with_http_info(self, request):
        """更新云服务器元数据

        更新云服务器元数据。  - 如果元数据中没有待更新字段，则自动添加该字段。  - 如果元数据中已存在待更新字段，则直接更新字段值。  - 如果元数据中的字段不再请求参数中，则保持不变

        :param UpdateServerMetadataRequest request
        :return: UpdateServerMetadataResponse
        """

        all_params = ['server_id', 'update_server_metadata_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/metadata',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateServerMetadataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_job_async(self, request):
        """查询任务的执行状态

        查询Job的执行状态。  对于创建云服务器、删除云服务器、云服务器批量操作和网卡操作等异步API，命令下发后，会返回job_id，通过job_id可以查询任务的执行状态。

        :param ShowJobRequest request
        :return: ShowJobResponse
        """
        return self.show_job_with_http_info(request)

    def show_job_with_http_info(self, request):
        """查询任务的执行状态

        查询Job的执行状态。  对于创建云服务器、删除云服务器、云服务器批量操作和网卡操作等异步API，命令下发后，会返回job_id，通过job_id可以查询任务的执行状态。

        :param ShowJobRequest request
        :return: ShowJobResponse
        """

        all_params = ['job_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1/{project_id}/jobs/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowJobResponse',
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
        :param header_params: Header parameters to be
            placed in the request header.
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
            request_type=request_type,
	    async_request=True)
