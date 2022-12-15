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
        """添加云服务器组成员

        将云服务器加入云服务器组。添加成功后，如果该云服务器组是反亲和性策略的，则该云服务器与云服务器组中的其他成员尽量分散地创建在不同主机上。如果该云服务器时故障域类型的，则该云服务器会拥有故障域属性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddServerGroupMember
        :type request: :class:`huaweicloudsdkecs.v2.AddServerGroupMemberRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.AddServerGroupMemberResponse`
        """
        return self.add_server_group_member_with_http_info(request)

    def add_server_group_member_with_http_info(self, request):
        all_params = ['server_group_id', 'add_server_group_member_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='AddServerGroupMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_server_virtual_ip_async(self, request):
        """云服务器网卡配置虚拟IP地址

        虚拟IP地址用于为网卡提供第二个IP地址，同时支持与多个弹性云服务器的网卡绑定，从而实现多个弹性云服务器之间的高可用性。
        
        该接口用于给云服务器网卡配置虚拟IP地址：
        
        - 当指定的IP地址是一个不存在的虚拟IP地址时，系统会创建该虚拟IP，并绑定至对应网卡。
        
        - 当指定的IP地址是一个已经创建好的私有IP时，系统会将指定的网卡和虚拟IP绑定。如果该IP的device_owner为空，则仅支持VPC内二三层通信；如果该IP的device_owner为neutron:VIP_PORT，则支持VPC内二三层通信、VPC之间对等连接访问，以及弹性公网IP、VPN、云专线等Internet接入。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateServerVirtualIp
        :type request: :class:`huaweicloudsdkecs.v2.AssociateServerVirtualIpRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.AssociateServerVirtualIpResponse`
        """
        return self.associate_server_virtual_ip_with_http_info(request)

    def associate_server_virtual_ip_with_http_info(self, request):
        all_params = ['nic_id', 'associate_server_virtual_ip_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'nic_id' in local_var_params:
            path_params['nic_id'] = local_var_params['nic_id']

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
            resource_path='/v1/{project_id}/cloudservers/nics/{nic_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociateServerVirtualIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def attach_server_volume_async(self, request):
        """弹性云服务器挂载磁盘

        把磁盘挂载到弹性云服务器上。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AttachServerVolume
        :type request: :class:`huaweicloudsdkecs.v2.AttachServerVolumeRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.AttachServerVolumeResponse`
        """
        return self.attach_server_volume_with_http_info(request)

    def attach_server_volume_with_http_info(self, request):
        all_params = ['server_id', 'attach_server_volume_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='AttachServerVolumeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_add_server_nics_async(self, request):
        """批量添加云服务器网卡

        给云服务器添加一张或多张网卡。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAddServerNics
        :type request: :class:`huaweicloudsdkecs.v2.BatchAddServerNicsRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.BatchAddServerNicsResponse`
        """
        return self.batch_add_server_nics_with_http_info(request)

    def batch_add_server_nics_with_http_info(self, request):
        all_params = ['server_id', 'batch_add_server_nics_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='BatchAddServerNicsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_attach_sharable_volumes_async(self, request):
        """批量挂载指定共享盘

        将指定的共享磁盘一次性挂载到多个弹性云服务器，实现批量挂载。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAttachSharableVolumes
        :type request: :class:`huaweicloudsdkecs.v2.BatchAttachSharableVolumesRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.BatchAttachSharableVolumesResponse`
        """
        return self.batch_attach_sharable_volumes_with_http_info(request)

    def batch_attach_sharable_volumes_with_http_info(self, request):
        all_params = ['volume_id', 'batch_attach_sharable_volumes_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

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
            resource_path='/v1/{project_id}/batchaction/attachvolumes/{volume_id}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchAttachSharableVolumesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_create_server_tags_async(self, request):
        """批量添加云服务器标签

        - 为指定云服务器批量添加标签。
        
        - 标签管理服务TMS使用该接口批量管理云服务器的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateServerTags
        :type request: :class:`huaweicloudsdkecs.v2.BatchCreateServerTagsRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.BatchCreateServerTagsResponse`
        """
        return self.batch_create_server_tags_with_http_info(request)

    def batch_create_server_tags_with_http_info(self, request):
        all_params = ['server_id', 'batch_create_server_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='BatchCreateServerTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_server_nics_async(self, request):
        """批量删除云服务器网卡

        卸载并删除云服务器中的一张或多张网卡。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteServerNics
        :type request: :class:`huaweicloudsdkecs.v2.BatchDeleteServerNicsRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.BatchDeleteServerNicsResponse`
        """
        return self.batch_delete_server_nics_with_http_info(request)

    def batch_delete_server_nics_with_http_info(self, request):
        all_params = ['server_id', 'batch_delete_server_nics_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='BatchDeleteServerNicsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_server_tags_async(self, request):
        """批量删除云服务器标签

        - 为指定云服务器批量删除标签。
        
        - 标签管理服务TMS使用该接口批量管理云服务器的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteServerTags
        :type request: :class:`huaweicloudsdkecs.v2.BatchDeleteServerTagsRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.BatchDeleteServerTagsResponse`
        """
        return self.batch_delete_server_tags_with_http_info(request)

    def batch_delete_server_tags_with_http_info(self, request):
        all_params = ['server_id', 'batch_delete_server_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='BatchDeleteServerTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_reboot_servers_async(self, request):
        """批量重启云服务器

        根据给定的云服务器ID列表，批量重启云服务器，一次最多可以重启1000台。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchRebootServers
        :type request: :class:`huaweicloudsdkecs.v2.BatchRebootServersRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.BatchRebootServersResponse`
        """
        return self.batch_reboot_servers_with_http_info(request)

    def batch_reboot_servers_with_http_info(self, request):
        all_params = ['batch_reboot_servers_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='BatchRebootServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_reset_servers_password_async(self, request):
        """批量重置弹性云服务器密码

        批量重置弹性云服务器管理帐号（root用户或Administrator用户）的密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchResetServersPassword
        :type request: :class:`huaweicloudsdkecs.v2.BatchResetServersPasswordRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.BatchResetServersPasswordResponse`
        """
        return self.batch_reset_servers_password_with_http_info(request)

    def batch_reset_servers_password_with_http_info(self, request):
        all_params = ['batch_reset_servers_password_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v1/{project_id}/cloudservers/os-reset-passwords',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchResetServersPasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_start_servers_async(self, request):
        """批量启动云服务器

        根据给定的云服务器ID列表，批量启动云服务器，一次最多可以启动1000台。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchStartServers
        :type request: :class:`huaweicloudsdkecs.v2.BatchStartServersRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.BatchStartServersResponse`
        """
        return self.batch_start_servers_with_http_info(request)

    def batch_start_servers_with_http_info(self, request):
        all_params = ['batch_start_servers_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='BatchStartServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_stop_servers_async(self, request):
        """批量关闭云服务器

        根据给定的云服务器ID列表，批量关闭云服务器，一次最多可以关闭1000台。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchStopServers
        :type request: :class:`huaweicloudsdkecs.v2.BatchStopServersRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.BatchStopServersResponse`
        """
        return self.batch_stop_servers_with_http_info(request)

    def batch_stop_servers_with_http_info(self, request):
        all_params = ['batch_stop_servers_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='BatchStopServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_update_servers_name_async(self, request):
        """批量修改弹性云服务器

        批量修改弹性云服务器信息。
        当前仅支持批量修改云服务器名称，一次最多可以修改1000台。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchUpdateServersName
        :type request: :class:`huaweicloudsdkecs.v2.BatchUpdateServersNameRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.BatchUpdateServersNameResponse`
        """
        return self.batch_update_servers_name_with_http_info(request)

    def batch_update_servers_name_with_http_info(self, request):
        all_params = ['batch_update_servers_name_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v1/{project_id}/cloudservers/server-name',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchUpdateServersNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_server_os_with_cloud_init_async(self, request):
        """切换弹性云服务器操作系统(安装Cloud init)

        切换弹性云服务器操作系统。支持弹性云服务器数据盘不变的情况下，使用新镜像重装系统盘。
        
        调用该接口后，系统将卸载系统盘，然后使用新镜像重新创建系统盘，并挂载至弹性云服务器，实现切换操作系统功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeServerOsWithCloudInit
        :type request: :class:`huaweicloudsdkecs.v2.ChangeServerOsWithCloudInitRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ChangeServerOsWithCloudInitResponse`
        """
        return self.change_server_os_with_cloud_init_with_http_info(request)

    def change_server_os_with_cloud_init_with_http_info(self, request):
        all_params = ['server_id', 'change_server_os_with_cloud_init_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ChangeServerOsWithCloudInitResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_server_os_without_cloud_init_async(self, request):
        """切换弹性云服务器操作系统(未安装Cloud init)

        切换弹性云服务器操作系统。
        
        该接口支持未安装Cloud-init或Cloudbase-init的镜像使用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeServerOsWithoutCloudInit
        :type request: :class:`huaweicloudsdkecs.v2.ChangeServerOsWithoutCloudInitRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ChangeServerOsWithoutCloudInitResponse`
        """
        return self.change_server_os_without_cloud_init_with_http_info(request)

    def change_server_os_without_cloud_init_with_http_info(self, request):
        all_params = ['server_id', 'change_server_os_without_cloud_init_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/changeos',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeServerOsWithoutCloudInitResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_post_paid_servers_async(self, request):
        """创建云服务器(按需)

        创建一台或多台[按需付费](https://support.huaweicloud.com/productdesc-ecs/ecs_01_0065.html)方式的云服务器。
        
        弹性云服务器的登录鉴权方式包括两种：密钥对、密码。为安全起见，推荐使用密钥对方式。
        
        - 密钥对
        密钥对指使用密钥对作为弹性云服务器的鉴权方式。
        接口调用方法：使用key_name字段，指定弹性云服务器登录时使用的密钥文件。
        
        - 密码
        密码指使用设置初始密码方式作为弹性云服务器的鉴权方式，此时，您可以通过用户名密码方式登录弹性云服务器，Linux操作系统时为root用户的初始密码，Windows操作系统时为Administrator用户的初始密码。
        
        接口调用方法：使用adminPass字段，指定管理员帐号的初始登录密码。对于镜像已安装Cloud-init的Linux云服务器，如果需要使用密文密码，可以使用user_data字段进行密码注入。
        
        &gt; 对于安装Cloud-init镜像的Linux云服务器云主机，若指定user_data字段，则adminPass字段无效。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePostPaidServers
        :type request: :class:`huaweicloudsdkecs.v2.CreatePostPaidServersRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.CreatePostPaidServersResponse`
        """
        return self.create_post_paid_servers_with_http_info(request)

    def create_post_paid_servers_with_http_info(self, request):
        all_params = ['create_post_paid_servers_request_body', 'x_client_token']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_client_token' in local_var_params:
            header_params['X-Client-Token'] = local_var_params['x_client_token']

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
            cname=cname,
            response_type='CreatePostPaidServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_server_group_async(self, request):
        """创建云服务器组

        创建弹性云服务器组。
        
        与原生的创建云服务器组接口不同之处在于该接口支持企业项目细粒度权限的校验。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateServerGroup
        :type request: :class:`huaweicloudsdkecs.v2.CreateServerGroupRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.CreateServerGroupResponse`
        """
        return self.create_server_group_with_http_info(request)

    def create_server_group_with_http_info(self, request):
        all_params = ['create_server_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='CreateServerGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_servers_async(self, request):
        """创建云服务器

        创建一台或多台云服务器。
        
        指该接口兼容《弹性云服务器接口参考》创建云服务器v1的功能，同时合入新功能，支持创建[包年/包月](https://support.huaweicloud.com/productdesc-ecs/ecs_01_0065.html)的弹性云服务器。
        
        弹性云服务器的登录鉴权方式包括两种：密钥对、密码。为安全起见，推荐使用密钥对方式。
        
        - 密钥对
        
        指使用密钥对作为弹性云服务器的鉴权方式。
        
        接口调用方法：使用key_name字段，指定弹性云服务器登录时使用的密钥文件。
        
        - 密码
        
        指使用设置初始密码方式作为弹性云服务器的鉴权方式，此时，您可以通过用户名密码方式登录弹性云服务器，Linux操作系统时为root用户的初始密码，Windows操作系统时为Administrator用户的初始密码。
        
        接口调用方法：使用adminPass字段，指定管理员帐号的初始登录密码。对于镜像已安装Cloud-init的Linux云服务器，如果需要使用密文密码，可以使用user_data字段进行密码注入。
        
        &gt; 对于安装Cloud-init镜像的Linux云服务器云主机，若指定user_data字段，则adminPass字段无效。
        
        购买操作示例：
        - [使用API购买ECS过程中常见问题及处理方法](https://support.huaweicloud.com/api-ecs/ecs_04_0007.html)
        - [获取Token并检验Token的有效期 ](https://support.huaweicloud.com/api-ecs/ecs_04_0008.html)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateServers
        :type request: :class:`huaweicloudsdkecs.v2.CreateServersRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.CreateServersResponse`
        """
        return self.create_servers_with_http_info(request)

    def create_servers_with_http_info(self, request):
        all_params = ['create_servers_request_body', 'x_client_token']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_client_token' in local_var_params:
            header_params['X-Client-Token'] = local_var_params['x_client_token']

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
            cname=cname,
            response_type='CreateServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_server_group_async(self, request):
        """删除云服务器组

        删除云服务器组。
        
        与原生的删除云服务器组接口不同之处在于该接口支持企业项目细粒度权限的校验。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteServerGroup
        :type request: :class:`huaweicloudsdkecs.v2.DeleteServerGroupRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.DeleteServerGroupResponse`
        """
        return self.delete_server_group_with_http_info(request)

    def delete_server_group_with_http_info(self, request):
        all_params = ['server_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='DeleteServerGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_server_group_member_async(self, request):
        """删除云服务器组成员

        将弹性云服务器移出云服务器组。移出后，该云服务器与云服务器组中的成员不再遵从反亲和策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteServerGroupMember
        :type request: :class:`huaweicloudsdkecs.v2.DeleteServerGroupMemberRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.DeleteServerGroupMemberResponse`
        """
        return self.delete_server_group_member_with_http_info(request)

    def delete_server_group_member_with_http_info(self, request):
        all_params = ['server_group_id', 'delete_server_group_member_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='DeleteServerGroupMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_server_metadata_async(self, request):
        """删除云服务器指定元数据

        删除云服务器指定元数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteServerMetadata
        :type request: :class:`huaweicloudsdkecs.v2.DeleteServerMetadataRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.DeleteServerMetadataResponse`
        """
        return self.delete_server_metadata_with_http_info(request)

    def delete_server_metadata_with_http_info(self, request):
        all_params = ['key', 'server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='DeleteServerMetadataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_server_password_async(self, request):
        """云服务器清除密码(企业项目)

        清除Windows云服务器初始安装时系统生成的密码记录。清除密码后，不影响云服务器密码登录功能，但不能再使用获取密码功能来查询该云服务器密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteServerPassword
        :type request: :class:`huaweicloudsdkecs.v2.DeleteServerPasswordRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.DeleteServerPasswordResponse`
        """
        return self.delete_server_password_with_http_info(request)

    def delete_server_password_with_http_info(self, request):
        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/os-server-password',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteServerPasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_servers_async(self, request):
        """删除云服务器

        根据指定的云服务器ID列表，删除云服务器。
        
        系统支持删除单台云服务器和批量删除多台云服务器操作，批量删除云服务器时，一次最多可以删除1000台。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteServers
        :type request: :class:`huaweicloudsdkecs.v2.DeleteServersRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.DeleteServersResponse`
        """
        return self.delete_servers_with_http_info(request)

    def delete_servers_with_http_info(self, request):
        all_params = ['delete_servers_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='DeleteServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def detach_server_volume_async(self, request):
        """弹性云服务器卸载磁盘

        从弹性云服务器中卸载磁盘。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetachServerVolume
        :type request: :class:`huaweicloudsdkecs.v2.DetachServerVolumeRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.DetachServerVolumeResponse`
        """
        return self.detach_server_volume_with_http_info(request)

    def detach_server_volume_with_http_info(self, request):
        all_params = ['server_id', 'volume_id', 'delete_flag']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='DetachServerVolumeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disassociate_server_virtual_ip_async(self, request):
        """云服务器网卡解绑虚拟IP地址

        虚拟IP地址用于为网卡提供第二个IP地址，同时支持与多个弹性云服务器的网卡绑定，从而实现多个弹性云服务器之间的高可用性。
        
        该接口用于解绑定弹性云服务器网卡的虚拟IP地址。解绑后，网卡不会被删除。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateServerVirtualIp
        :type request: :class:`huaweicloudsdkecs.v2.DisassociateServerVirtualIpRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.DisassociateServerVirtualIpResponse`
        """
        return self.disassociate_server_virtual_ip_with_http_info(request)

    def disassociate_server_virtual_ip_with_http_info(self, request):
        all_params = ['nic_id', 'disassociate_server_virtual_ip_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'nic_id' in local_var_params:
            path_params['nic_id'] = local_var_params['nic_id']

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
            resource_path='/v1/{project_id}/cloudservers/nics/{nic_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisassociateServerVirtualIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_flavors_async(self, request):
        """查询规格详情和规格扩展信息列表

        查询云服务器规格详情信息和规格扩展信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFlavors
        :type request: :class:`huaweicloudsdkecs.v2.ListFlavorsRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ListFlavorsResponse`
        """
        return self.list_flavors_with_http_info(request)

    def list_flavors_with_http_info(self, request):
        all_params = ['availability_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListFlavorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_resize_flavors_async(self, request):
        """查询云服务器规格变更支持列表

        变更规格时，部分规格的云服务器之间不能互相变更。您可以通过本接口，通过指定弹性云服务器规格，查询该规格可以变更的规格列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResizeFlavors
        :type request: :class:`huaweicloudsdkecs.v2.ListResizeFlavorsRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ListResizeFlavorsResponse`
        """
        return self.list_resize_flavors_with_http_info(request)

    def list_resize_flavors_with_http_info(self, request):
        all_params = ['instance_uuid', 'limit', 'marker', 'sort_dir', 'sort_key', 'source_flavor_id', 'source_flavor_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListResizeFlavorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_server_block_devices_async(self, request):
        """查询弹性云服务器磁盘信息

        查询弹性云服务器挂载的磁盘信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServerBlockDevices
        :type request: :class:`huaweicloudsdkecs.v2.ListServerBlockDevicesRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ListServerBlockDevicesResponse`
        """
        return self.list_server_block_devices_with_http_info(request)

    def list_server_block_devices_with_http_info(self, request):
        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListServerBlockDevicesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_server_groups_async(self, request):
        """查询云服务器组列表

        查询弹性云服务器组。
        
        与原生的创建云服务器组接口不同之处在于该接口支持企业项目细粒度权限的校验。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServerGroups
        :type request: :class:`huaweicloudsdkecs.v2.ListServerGroupsRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ListServerGroupsResponse`
        """
        return self.list_server_groups_with_http_info(request)

    def list_server_groups_with_http_info(self, request):
        all_params = ['limit', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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
            resource_path='/v1/{project_id}/cloudservers/os-server-groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListServerGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_server_interfaces_async(self, request):
        """查询云服务器网卡信息

        查询云服务器网卡信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServerInterfaces
        :type request: :class:`huaweicloudsdkecs.v2.ListServerInterfacesRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ListServerInterfacesResponse`
        """
        return self.list_server_interfaces_with_http_info(request)

    def list_server_interfaces_with_http_info(self, request):
        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListServerInterfacesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_server_tags_async(self, request):
        """查询项目标签

        项目（Project）用于将OpenStack的资源（计算资源、存储资源和网络资源）进行分组和隔离。项目可以是一个部门或者一个项目组。一个帐户中可以创建多个项目。
        
        该接口用于查询用户在指定项目所使用的全部标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServerTags
        :type request: :class:`huaweicloudsdkecs.v2.ListServerTagsRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ListServerTagsResponse`
        """
        return self.list_server_tags_with_http_info(request)

    def list_server_tags_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v1/{project_id}/cloudservers/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListServerTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_servers_by_tag_async(self, request):
        """按标签查询云服务器列表

        使用标签过滤弹性云服务器，并返回云服务器使用的所有标签和资源列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServersByTag
        :type request: :class:`huaweicloudsdkecs.v2.ListServersByTagRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ListServersByTagResponse`
        """
        return self.list_servers_by_tag_with_http_info(request)

    def list_servers_by_tag_with_http_info(self, request):
        all_params = ['list_servers_by_tag_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v1/{project_id}/cloudservers/resource_instances/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListServersByTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_servers_details_async(self, request):
        """查询云服务器详情列表

        根据用户请求条件从数据库筛选、查询所有的弹性云服务器，并关联相关表获取到弹性云服务器的详细信息。
        
        该接口支持查询弹性云服务器计费方式，以及是否被冻结。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServersDetails
        :type request: :class:`huaweicloudsdkecs.v2.ListServersDetailsRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ListServersDetailsResponse`
        """
        return self.list_servers_details_with_http_info(request)

    def list_servers_details_with_http_info(self, request):
        all_params = ['enterprise_project_id', 'flavor', 'ip', 'limit', 'name', 'not_tags', 'offset', 'reservation_id', 'status', 'tags', 'ip_eq', 'server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
        if 'ip_eq' in local_var_params:
            query_params.append(('ip_eq', local_var_params['ip_eq']))
        if 'server_id' in local_var_params:
            query_params.append(('server_id', local_var_params['server_id']))

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
            cname=cname,
            response_type='ListServersDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def migrate_server_async(self, request):
        """冷迁移云服务器

        - 将部署在专属主机上的弹性云服务器迁移至其他专属主机。
        - 将部署在专属主机上的弹性云服务器迁移至公共资源池，即不再部署在专属主机上。
        - 将公共资源池的弹性云服务器迁移至专属主机上，成为专属主机上部署的弹性云服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for MigrateServer
        :type request: :class:`huaweicloudsdkecs.v2.MigrateServerRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.MigrateServerResponse`
        """
        return self.migrate_server_with_http_info(request)

    def migrate_server_with_http_info(self, request):
        all_params = ['server_id', 'migrate_server_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/migrate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='MigrateServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def nova_associate_security_group_async(self, request):
        """添加安全组

        为弹性云服务器添加一个安全组。
        
        添加多个安全组时，建议最多为弹性云服务器添加5个安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NovaAssociateSecurityGroup
        :type request: :class:`huaweicloudsdkecs.v2.NovaAssociateSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.NovaAssociateSecurityGroupResponse`
        """
        return self.nova_associate_security_group_with_http_info(request)

    def nova_associate_security_group_with_http_info(self, request):
        all_params = ['server_id', 'nova_associate_security_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='NovaAssociateSecurityGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def nova_create_keypair_async(self, request):
        """创建和导入SSH密钥

        创建SSH密钥，或把公钥导入系统，生成密钥对。
        
        创建SSH密钥成功后，请把响应数据中的私钥内容保存到本地文件，用户使用该私钥登录云服务器云主机。为保证云服务器云主机器安全，私钥数据只能读取一次，请妥善保管。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NovaCreateKeypair
        :type request: :class:`huaweicloudsdkecs.v2.NovaCreateKeypairRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.NovaCreateKeypairResponse`
        """
        return self.nova_create_keypair_with_http_info(request)

    def nova_create_keypair_with_http_info(self, request):
        all_params = ['nova_create_keypair_request_body', 'open_stack_api_version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='NovaCreateKeypairResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def nova_create_servers_async(self, request):
        """创建云服务器

        创建一台弹性云服务器。
        
        弹性云服务器创建完成后，如需开启自动恢复功能，可以调用配置云服务器自动恢复的接口，具体使用请参见管理云服务器自动恢复动作。
        
        该接口在云服务器创建失败后不支持自动回滚。若需要自动回滚能力，可以调用POST /v1/{project_id}/cloudservers接口，具体使用请参见创建云服务器（按需）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NovaCreateServers
        :type request: :class:`huaweicloudsdkecs.v2.NovaCreateServersRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.NovaCreateServersResponse`
        """
        return self.nova_create_servers_with_http_info(request)

    def nova_create_servers_with_http_info(self, request):
        all_params = ['nova_create_servers_request_body', 'open_stack_api_version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='NovaCreateServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def nova_delete_keypair_async(self, request):
        """删除SSH密钥

        根据SSH密钥的名称，删除指定SSH密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NovaDeleteKeypair
        :type request: :class:`huaweicloudsdkecs.v2.NovaDeleteKeypairRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.NovaDeleteKeypairResponse`
        """
        return self.nova_delete_keypair_with_http_info(request)

    def nova_delete_keypair_with_http_info(self, request):
        all_params = ['keypair_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='NovaDeleteKeypairResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def nova_delete_server_async(self, request):
        """删除云服务器

        删除一台云服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NovaDeleteServer
        :type request: :class:`huaweicloudsdkecs.v2.NovaDeleteServerRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.NovaDeleteServerResponse`
        """
        return self.nova_delete_server_with_http_info(request)

    def nova_delete_server_with_http_info(self, request):
        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='NovaDeleteServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def nova_disassociate_security_group_async(self, request):
        """移除安全组

        移除弹性云服务器中的安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NovaDisassociateSecurityGroup
        :type request: :class:`huaweicloudsdkecs.v2.NovaDisassociateSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.NovaDisassociateSecurityGroupResponse`
        """
        return self.nova_disassociate_security_group_with_http_info(request)

    def nova_disassociate_security_group_with_http_info(self, request):
        all_params = ['server_id', 'nova_disassociate_security_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='NovaDisassociateSecurityGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def nova_list_availability_zones_async(self, request):
        """查询可用区列表

        查询可用域列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NovaListAvailabilityZones
        :type request: :class:`huaweicloudsdkecs.v2.NovaListAvailabilityZonesRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.NovaListAvailabilityZonesResponse`
        """
        return self.nova_list_availability_zones_with_http_info(request)

    def nova_list_availability_zones_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='NovaListAvailabilityZonesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def nova_list_keypairs_async(self, request):
        """查询SSH密钥列表

        查询SSH密钥信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NovaListKeypairs
        :type request: :class:`huaweicloudsdkecs.v2.NovaListKeypairsRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.NovaListKeypairsResponse`
        """
        return self.nova_list_keypairs_with_http_info(request)

    def nova_list_keypairs_with_http_info(self, request):
        all_params = ['limit', 'marker', 'open_stack_api_version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='NovaListKeypairsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def nova_list_server_security_groups_async(self, request):
        """查询指定云服务器安全组列表

        查询指定弹性云服务器的安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NovaListServerSecurityGroups
        :type request: :class:`huaweicloudsdkecs.v2.NovaListServerSecurityGroupsRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.NovaListServerSecurityGroupsResponse`
        """
        return self.nova_list_server_security_groups_with_http_info(request)

    def nova_list_server_security_groups_with_http_info(self, request):
        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='NovaListServerSecurityGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def nova_list_servers_details_async(self, request):
        """查询云服务器详情列表

        查询云服务器详情信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NovaListServersDetails
        :type request: :class:`huaweicloudsdkecs.v2.NovaListServersDetailsRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.NovaListServersDetailsResponse`
        """
        return self.nova_list_servers_details_with_http_info(request)

    def nova_list_servers_details_with_http_info(self, request):
        all_params = ['changes_since', 'flavor', 'image', 'ip', 'limit', 'marker', 'name', 'not_tags', 'reservation_id', 'sort_key', 'status', 'tags', 'open_stack_api_version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='NovaListServersDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def nova_show_keypair_async(self, request):
        """查询SSH密钥详情

        根据SSH密钥名称查询指定SSH密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NovaShowKeypair
        :type request: :class:`huaweicloudsdkecs.v2.NovaShowKeypairRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.NovaShowKeypairResponse`
        """
        return self.nova_show_keypair_with_http_info(request)

    def nova_show_keypair_with_http_info(self, request):
        all_params = ['keypair_name', 'open_stack_api_version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='NovaShowKeypairResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def nova_show_server_async(self, request):
        """查询云服务器详情

        根据云服务器ID，查询云服务器的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NovaShowServer
        :type request: :class:`huaweicloudsdkecs.v2.NovaShowServerRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.NovaShowServerResponse`
        """
        return self.nova_show_server_with_http_info(request)

    def nova_show_server_with_http_info(self, request):
        all_params = ['server_id', 'open_stack_api_version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='NovaShowServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def register_server_auto_recovery_async(self, request):
        """管理云服务器自动恢复动作

        配置、删除云服务器自动恢复动作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RegisterServerAutoRecovery
        :type request: :class:`huaweicloudsdkecs.v2.RegisterServerAutoRecoveryRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.RegisterServerAutoRecoveryResponse`
        """
        return self.register_server_auto_recovery_with_http_info(request)

    def register_server_auto_recovery_with_http_info(self, request):
        all_params = ['server_id', 'register_server_auto_recovery_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/autorecovery',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RegisterServerAutoRecoveryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def register_server_monitor_async(self, request):
        """注册云服务器监控

        将云服务器添加到监控表中。
        
        注册到监控表中的云服务会被ceilometer周期性采集监控数据，包括平台的版本、cpu信息、内存、网卡、磁盘、硬件平台等信息，这些数据上报给云监控。例如SAP云服务器内部的插件会周期性从云监控中查询监控数据，以报表形式呈现给SAP。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RegisterServerMonitor
        :type request: :class:`huaweicloudsdkecs.v2.RegisterServerMonitorRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.RegisterServerMonitorResponse`
        """
        return self.register_server_monitor_with_http_info(request)

    def register_server_monitor_with_http_info(self, request):
        all_params = ['server_id', 'register_server_monitor_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v1.0/servers/{server_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RegisterServerMonitorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reinstall_server_with_cloud_init_async(self, request):
        """重装弹性云服务器操作系统(安装Cloud-init)

        重装弹性云服务器的操作系统。支持弹性云服务器数据盘不变的情况下，使用原镜像重装系统盘。
        
        调用该接口后，系统将卸载系统盘，然后使用原镜像重新创建系统盘，并挂载至弹性云服务器，实现重装操作系统功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ReinstallServerWithCloudInit
        :type request: :class:`huaweicloudsdkecs.v2.ReinstallServerWithCloudInitRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ReinstallServerWithCloudInitResponse`
        """
        return self.reinstall_server_with_cloud_init_with_http_info(request)

    def reinstall_server_with_cloud_init_with_http_info(self, request):
        all_params = ['server_id', 'reinstall_server_with_cloud_init_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ReinstallServerWithCloudInitResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reinstall_server_without_cloud_init_async(self, request):
        """重装弹性云服务器操作系统(未安装Cloud init)

        重装弹性云服务器的操作系统。
        
        该接口支持未安装Cloud-init或Cloudbase-init的镜像。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ReinstallServerWithoutCloudInit
        :type request: :class:`huaweicloudsdkecs.v2.ReinstallServerWithoutCloudInitRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ReinstallServerWithoutCloudInitResponse`
        """
        return self.reinstall_server_without_cloud_init_with_http_info(request)

    def reinstall_server_without_cloud_init_with_http_info(self, request):
        all_params = ['server_id', 'reinstall_server_without_cloud_init_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/reinstallos',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ReinstallServerWithoutCloudInitResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reset_server_password_async(self, request):
        """一键重置弹性云服务器密码(企业项目)

        重置弹性云服务器管理帐号（root用户或Administrator用户）的密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetServerPassword
        :type request: :class:`huaweicloudsdkecs.v2.ResetServerPasswordRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ResetServerPasswordResponse`
        """
        return self.reset_server_password_with_http_info(request)

    def reset_server_password_with_http_info(self, request):
        all_params = ['server_id', 'reset_server_password_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ResetServerPasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def resize_post_paid_server_async(self, request):
        """变更云服务器规格(按需)

        当您创建的弹性云服务器规格无法满足业务需要时，可以变更云服务器规格，升级vCPU、内存。具体接口的使用，请参见本节内容。
        
        变更规格时，部分规格的云服务器之间不能互相变更。
        
        您可以通过接口“/v1/{project_id}/cloudservers/resize_flavors?{instance_uuid,source_flavor_id,source_flavor_name}”查询支持列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResizePostPaidServer
        :type request: :class:`huaweicloudsdkecs.v2.ResizePostPaidServerRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ResizePostPaidServerResponse`
        """
        return self.resize_post_paid_server_with_http_info(request)

    def resize_post_paid_server_with_http_info(self, request):
        all_params = ['server_id', 'resize_post_paid_server_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ResizePostPaidServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def resize_server_async(self, request):
        """变更云服务器规格

        变更云服务器规格。
        
        v1.1版本：指该接口兼容v1接口的功能，同时合入新功能，支持变更包年/包月弹性云服务器的规格。
        
        注意事项：
        
        - 该接口可以使用合作伙伴自身的AK/SK或者token调用，也可以用合作伙伴子客户的AK/SK或者token来调用。
        - 如果使用AK/SK认证方式，示例代码中region请参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)中“弹性云服务 ECS”下“区域”的内容，，serviceName（英文服务名称缩写）请指定为ECS。
        - Endpoint请参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)中“弹性云服务 ECS”下“终端节点（Endpoint）”的内容。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResizeServer
        :type request: :class:`huaweicloudsdkecs.v2.ResizeServerRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ResizeServerResponse`
        """
        return self.resize_server_with_http_info(request)

    def resize_server_with_http_info(self, request):
        all_params = ['server_id', 'resize_server_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ResizeServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_reset_password_flag_async(self, request):
        """查询是否支持一键重置密码

        查询弹性云服务器是否支持一键重置密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResetPasswordFlag
        :type request: :class:`huaweicloudsdkecs.v2.ShowResetPasswordFlagRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ShowResetPasswordFlagResponse`
        """
        return self.show_reset_password_flag_with_http_info(request)

    def show_reset_password_flag_with_http_info(self, request):
        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowResetPasswordFlagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_server_async(self, request):
        """查询云服务器详情

        查询弹性云服务器的详细信息。
        
        该接口支持查询弹性云服务器的计费方式，以及是否被冻结。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServer
        :type request: :class:`huaweicloudsdkecs.v2.ShowServerRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ShowServerResponse`
        """
        return self.show_server_with_http_info(request)

    def show_server_with_http_info(self, request):
        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_server_auto_recovery_async(self, request):
        """查询云服务器是否配置了自动恢复动作

        查询云服务器是否配置了自动恢复动作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServerAutoRecovery
        :type request: :class:`huaweicloudsdkecs.v2.ShowServerAutoRecoveryRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ShowServerAutoRecoveryResponse`
        """
        return self.show_server_auto_recovery_with_http_info(request)

    def show_server_auto_recovery_with_http_info(self, request):
        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/autorecovery',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowServerAutoRecoveryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_server_block_device_async(self, request):
        """查询弹性云服务器单个磁盘信息

        查询弹性云服务器挂载的单个磁盘信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServerBlockDevice
        :type request: :class:`huaweicloudsdkecs.v2.ShowServerBlockDeviceRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ShowServerBlockDeviceResponse`
        """
        return self.show_server_block_device_with_http_info(request)

    def show_server_block_device_with_http_info(self, request):
        all_params = ['server_id', 'volume_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/block_device/{volume_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowServerBlockDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_server_group_async(self, request):
        """查询云服务器组详情

        查询弹性云服务器组详情。
        
        与原生的创建云服务器组接口不同之处在于该接口支持企业项目细粒度权限的校验。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServerGroup
        :type request: :class:`huaweicloudsdkecs.v2.ShowServerGroupRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ShowServerGroupResponse`
        """
        return self.show_server_group_with_http_info(request)

    def show_server_group_with_http_info(self, request):
        all_params = ['server_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowServerGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_server_limits_async(self, request):
        """查询租户配额

        查询租户配额信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServerLimits
        :type request: :class:`huaweicloudsdkecs.v2.ShowServerLimitsRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ShowServerLimitsResponse`
        """
        return self.show_server_limits_with_http_info(request)

    def show_server_limits_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowServerLimitsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_server_password_async(self, request):
        """云服务器获取密码(企业项目)

        当通过支持Cloudbase-init功能的镜像创建Windows云服务器时，获取云服务器初始安装时系统生成的管理员帐户（Administrator帐户或Cloudbase-init设置的帐户）随机密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServerPassword
        :type request: :class:`huaweicloudsdkecs.v2.ShowServerPasswordRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ShowServerPasswordResponse`
        """
        return self.show_server_password_with_http_info(request)

    def show_server_password_with_http_info(self, request):
        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/os-server-password',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowServerPasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_server_remote_console_async(self, request):
        """获取VNC远程登录地址

        获取弹性云服务器VNC远程登录地址。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServerRemoteConsole
        :type request: :class:`huaweicloudsdkecs.v2.ShowServerRemoteConsoleRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ShowServerRemoteConsoleResponse`
        """
        return self.show_server_remote_console_with_http_info(request)

    def show_server_remote_console_with_http_info(self, request):
        all_params = ['server_id', 'show_server_remote_console_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowServerRemoteConsoleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_server_tags_async(self, request):
        """查询云服务器标签

        - 查询指定云服务器的标签信息。
        
        - 标签管理服务TMS使用该接口查询指定云服务器的全部标签数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServerTags
        :type request: :class:`huaweicloudsdkecs.v2.ShowServerTagsRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ShowServerTagsResponse`
        """
        return self.show_server_tags_with_http_info(request)

    def show_server_tags_with_http_info(self, request):
        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowServerTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_server_async(self, request):
        """修改云服务器

        修改云服务器信息，目前支持修改云服务器名称及描述和hostname。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateServer
        :type request: :class:`huaweicloudsdkecs.v2.UpdateServerRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.UpdateServerResponse`
        """
        return self.update_server_with_http_info(request)

    def update_server_with_http_info(self, request):
        all_params = ['server_id', 'update_server_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='UpdateServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_server_auto_terminate_time_async(self, request):
        """修改云服务器销毁时间

        修改按需服务器，设置定时销毁时间。如果设置的销毁时间为空，表示取消销毁时间。
        
        该接口支持企业项目细粒度权限的校验，具体细粒度请参见 ecs:cloudServers:put。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateServerAutoTerminateTime
        :type request: :class:`huaweicloudsdkecs.v2.UpdateServerAutoTerminateTimeRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.UpdateServerAutoTerminateTimeResponse`
        """
        return self.update_server_auto_terminate_time_with_http_info(request)

    def update_server_auto_terminate_time_with_http_info(self, request):
        all_params = ['server_id', 'update_server_auto_terminate_time_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='UpdateServerAutoTerminateTimeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_server_block_device_async(self, request):
        """修改云服务器挂载的单个磁盘信息

        修改云服务器云主机挂载的单个磁盘信息。&#39;当前仅支持修改delete_on_termination字段。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateServerBlockDevice
        :type request: :class:`huaweicloudsdkecs.v2.UpdateServerBlockDeviceRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.UpdateServerBlockDeviceResponse`
        """
        return self.update_server_block_device_with_http_info(request)

    def update_server_block_device_with_http_info(self, request):
        all_params = ['server_id', 'volume_id', 'update_server_block_device_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/block_device/{volume_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateServerBlockDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_server_metadata_async(self, request):
        """更新云服务器元数据

        更新云服务器元数据。
        
        - 如果元数据中没有待更新字段，则自动添加该字段。
        
        - 如果元数据中已存在待更新字段，则直接更新字段值。
        
        - 如果元数据中的字段不再请求参数中，则保持不变
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateServerMetadata
        :type request: :class:`huaweicloudsdkecs.v2.UpdateServerMetadataRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.UpdateServerMetadataResponse`
        """
        return self.update_server_metadata_with_http_info(request)

    def update_server_metadata_with_http_info(self, request):
        all_params = ['server_id', 'update_server_metadata_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='UpdateServerMetadataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job_async(self, request):
        """查询任务的执行状态

        查询Job的执行状态。
        
        对于创建云服务器、删除云服务器、云服务器批量操作和网卡操作等异步API，命令下发后，会返回job_id，通过job_id可以查询任务的执行状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJob
        :type request: :class:`huaweicloudsdkecs.v2.ShowJobRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ShowJobResponse`
        """
        return self.show_job_with_http_info(request)

    def show_job_with_http_info(self, request):
        all_params = ['job_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, cname=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param cname: Used for obs endpoint.
        :param auth_settings: Auth Settings names for the request.
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
            cname=cname,
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type,
	    async_request=True)
