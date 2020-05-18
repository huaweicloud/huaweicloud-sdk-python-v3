# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

# python 2 and python 3 compatibility library
import six

from huaweicloudsdkcore.client import Client
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils


class EcsClient(Client):
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
        super(EcsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkecs.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}



    def associate_server_virtual_ip(self, request):
        """云服务器网卡配置虚拟IP地址

        虚拟IP地址用于为网卡提供第二个IP地址，同时支持与多个弹性云服务器的网卡绑定，从而实现多个弹性云服务器之间的高可用性。  该接口用于给云服务器网卡配置虚拟IP地址：  - 当指定的IP地址是一个不存在的虚拟IP地址时，系统会创建该虚拟IP，并绑定至对应网卡。  - 当指定的IP地址是一个已经创建好的私有IP时，系统会将指定的网卡和虚拟IP绑定。如果该IP的device_owner为空，则仅支持VPC内二三层通信；如果该IP的device_owner为neutron:VIP_PORT，则支持VPC内二三层通信、VPC之间对等连接访问，以及弹性公网IP、VPN、云专线等Internet接入。

        :param AssociateServerVirtualIpRequest request
        :return: AssociateServerVirtualIpResponse
        """
        return self.associate_server_virtual_ip_with_http_info(request)

    def associate_server_virtual_ip_with_http_info(self, request):
        """云服务器网卡配置虚拟IP地址

        虚拟IP地址用于为网卡提供第二个IP地址，同时支持与多个弹性云服务器的网卡绑定，从而实现多个弹性云服务器之间的高可用性。  该接口用于给云服务器网卡配置虚拟IP地址：  - 当指定的IP地址是一个不存在的虚拟IP地址时，系统会创建该虚拟IP，并绑定至对应网卡。  - 当指定的IP地址是一个已经创建好的私有IP时，系统会将指定的网卡和虚拟IP绑定。如果该IP的device_owner为空，则仅支持VPC内二三层通信；如果该IP的device_owner为neutron:VIP_PORT，则支持VPC内二三层通信、VPC之间对等连接访问，以及弹性公网IP、VPN、云专线等Internet接入。

        :param AssociateServerVirtualIpRequest request
        :return: tuple(AssociateServerVirtualIpResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['nic_id', 'associate_server_virtual_ip_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'nic_id' in local_var_params:
            path_params['nic_id'] = local_var_params['nic_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/nics/{nic_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='AssociateServerVirtualIpResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def attach_server_volume(self, request):
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
        :return: tuple(AttachServerVolumeResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id', 'attach_server_volume_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/{server_id}/attachvolume', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='AttachServerVolumeResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def batch_add_server_nics(self, request):
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
        :return: tuple(BatchAddServerNicsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id', 'batch_add_server_nics_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/{server_id}/nics', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchAddServerNicsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def batch_attach_sharable_volumes(self, request):
        """批量挂载指定共享盘

        将指定的共享磁盘一次性挂载到多个弹性云服务器，实现批量挂载。

        :param BatchAttachSharableVolumesRequest request
        :return: BatchAttachSharableVolumesResponse
        """
        return self.batch_attach_sharable_volumes_with_http_info(request)

    def batch_attach_sharable_volumes_with_http_info(self, request):
        """批量挂载指定共享盘

        将指定的共享磁盘一次性挂载到多个弹性云服务器，实现批量挂载。

        :param BatchAttachSharableVolumesRequest request
        :return: tuple(BatchAttachSharableVolumesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['volume_id', 'batch_attach_sharable_volumes_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/batchaction/attachvolumes/{volume_id}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchAttachSharableVolumesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def batch_create_server_tags(self, request):
        """批量添加云服务器标签

        - 为指定云服务器批量添加标签。  - 标签管理服务TMS使用该接口批量管理云服务器的标签。

        :param BatchCreateServerTagsRequest request
        :return: None
        """
        return self.batch_create_server_tags_with_http_info(request)

    def batch_create_server_tags_with_http_info(self, request):
        """批量添加云服务器标签

        - 为指定云服务器批量添加标签。  - 标签管理服务TMS使用该接口批量管理云服务器的标签。

        :param BatchCreateServerTagsRequest request
        :return: None
        """

        all_params = ['server_id', 'batch_create_server_tags_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/{server_id}/tags/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def batch_delete_server_nics(self, request):
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
        :return: tuple(BatchDeleteServerNicsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id', 'batch_delete_server_nics_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/{server_id}/nics/delete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteServerNicsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def batch_delete_server_tags(self, request):
        """批量删除云服务器标签

        - 为指定云服务器批量删除标签。  - 标签管理服务TMS使用该接口批量管理云服务器的标签。

        :param BatchDeleteServerTagsRequest request
        :return: None
        """
        return self.batch_delete_server_tags_with_http_info(request)

    def batch_delete_server_tags_with_http_info(self, request):
        """批量删除云服务器标签

        - 为指定云服务器批量删除标签。  - 标签管理服务TMS使用该接口批量管理云服务器的标签。

        :param BatchDeleteServerTagsRequest request
        :return: None
        """

        all_params = ['server_id', 'batch_delete_server_tags_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/{server_id}/tags/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def batch_reboot_servers(self, request):
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
        :return: tuple(BatchRebootServersResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['batch_reboot_servers_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchRebootServersResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def batch_reset_servers_password(self, request):
        """批量重置弹性云服务器密码

        批量重置弹性云服务器管理帐号（root用户或Administrator用户）的密码。

        :param BatchResetServersPasswordRequest request
        :return: BatchResetServersPasswordResponse
        """
        return self.batch_reset_servers_password_with_http_info(request)

    def batch_reset_servers_password_with_http_info(self, request):
        """批量重置弹性云服务器密码

        批量重置弹性云服务器管理帐号（root用户或Administrator用户）的密码。

        :param BatchResetServersPasswordRequest request
        :return: tuple(BatchResetServersPasswordResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['batch_reset_servers_password_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/os-reset-passwords', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchResetServersPasswordResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def batch_start_servers(self, request):
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
        :return: tuple(BatchStartServersResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['batch_start_servers_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchStartServersResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def batch_stop_servers(self, request):
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
        :return: tuple(BatchStopServersResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['batch_stop_servers_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchStopServersResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def batch_update_servers_name(self, request):
        """批量修改弹性云服务器

        批量修改弹性云服务器信息。 当前仅支持批量修改云服务器名称，一次最多可以修改1000台。

        :param BatchUpdateServersNameRequest request
        :return: BatchUpdateServersNameResponse
        """
        return self.batch_update_servers_name_with_http_info(request)

    def batch_update_servers_name_with_http_info(self, request):
        """批量修改弹性云服务器

        批量修改弹性云服务器信息。 当前仅支持批量修改云服务器名称，一次最多可以修改1000台。

        :param BatchUpdateServersNameRequest request
        :return: tuple(BatchUpdateServersNameResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['batch_update_servers_name_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/server-name', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchUpdateServersNameResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def change_server_os_with_cloud_init(self, request):
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
        :return: tuple(ChangeServerOsWithCloudInitResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id', 'change_server_os_with_cloud_init_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/cloudservers/{server_id}/changeos', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ChangeServerOsWithCloudInitResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def change_server_os_without_cloud_init(self, request):
        """切换弹性云服务器操作系统(未安装Cloud init)

        切换弹性云服务器操作系统。  该接口支持未安装Cloud-init或Cloudbase-init的镜像使用。

        :param ChangeServerOsWithoutCloudInitRequest request
        :return: ChangeServerOsWithoutCloudInitResponse
        """
        return self.change_server_os_without_cloud_init_with_http_info(request)

    def change_server_os_without_cloud_init_with_http_info(self, request):
        """切换弹性云服务器操作系统(未安装Cloud init)

        切换弹性云服务器操作系统。  该接口支持未安装Cloud-init或Cloudbase-init的镜像使用。

        :param ChangeServerOsWithoutCloudInitRequest request
        :return: tuple(ChangeServerOsWithoutCloudInitResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id', 'change_server_os_without_cloud_init_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/{server_id}/changeos', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ChangeServerOsWithoutCloudInitResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def create_post_paid_servers(self, request):
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
        :return: tuple(CreatePostPaidServersResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['create_post_paid_servers_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreatePostPaidServersResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def create_server_group(self, request):
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
        :return: tuple(CreateServerGroupResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['create_server_group_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/os-server-groups', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateServerGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def create_servers(self, request):
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
        :return: tuple(CreateServersResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['create_servers_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1.1/{project_id}/cloudservers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateServersResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def delete_server_group(self, request):
        """删除云服务器组

        删除云服务器组。  与原生的删除云服务器组接口不同之处在于该接口支持企业项目细粒度权限的校验。

        :param DeleteServerGroupRequest request
        :return: None
        """
        return self.delete_server_group_with_http_info(request)

    def delete_server_group_with_http_info(self, request):
        """删除云服务器组

        删除云服务器组。  与原生的删除云服务器组接口不同之处在于该接口支持企业项目细粒度权限的校验。

        :param DeleteServerGroupRequest request
        :return: None
        """

        all_params = ['server_group_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/os-server-groups/{server_group_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def delete_server_metadata(self, request):
        """删除云服务器指定元数据

        删除云服务器指定元数据。

        :param DeleteServerMetadataRequest request
        :return: None
        """
        return self.delete_server_metadata_with_http_info(request)

    def delete_server_metadata_with_http_info(self, request):
        """删除云服务器指定元数据

        删除云服务器指定元数据。

        :param DeleteServerMetadataRequest request
        :return: None
        """

        all_params = ['server_id', 'key']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/{server_id}/metadata/{key}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def delete_servers(self, request):
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
        :return: tuple(DeleteServersResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['delete_servers_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/delete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteServersResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def delete_windows_server_password(self, request):
        """Windows云服务器清除密码(企业项目)

        清除Windows云服务器初始安装时系统生成的密码记录。清除密码后，不影响云服务器密码登录功能，但不能再使用获取密码功能来查询该云服务器密码。

        :param DeleteWindowsServerPasswordRequest request
        :return: None
        """
        return self.delete_windows_server_password_with_http_info(request)

    def delete_windows_server_password_with_http_info(self, request):
        """Windows云服务器清除密码(企业项目)

        清除Windows云服务器初始安装时系统生成的密码记录。清除密码后，不影响云服务器密码登录功能，但不能再使用获取密码功能来查询该云服务器密码。

        :param DeleteWindowsServerPasswordRequest request
        :return: None
        """

        all_params = ['server_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/{server_id}/os-server-password', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def detach_server_volume(self, request):
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
        :return: tuple(DetachServerVolumeResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id', 'volume_id', 'delete_flag']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/{server_id}/detachvolume/{volume_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='DetachServerVolumeResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def disassociate_server_virtual_ip(self, request):
        """云服务器网卡解绑虚拟IP地址

        虚拟IP地址用于为网卡提供第二个IP地址，同时支持与多个弹性云服务器的网卡绑定，从而实现多个弹性云服务器之间的高可用性。  该接口用于解绑定弹性云服务器网卡的虚拟IP地址。解绑后，网卡不会被删除。

        :param DisassociateServerVirtualIpRequest request
        :return: DisassociateServerVirtualIpResponse
        """
        return self.disassociate_server_virtual_ip_with_http_info(request)

    def disassociate_server_virtual_ip_with_http_info(self, request):
        """云服务器网卡解绑虚拟IP地址

        虚拟IP地址用于为网卡提供第二个IP地址，同时支持与多个弹性云服务器的网卡绑定，从而实现多个弹性云服务器之间的高可用性。  该接口用于解绑定弹性云服务器网卡的虚拟IP地址。解绑后，网卡不会被删除。

        :param DisassociateServerVirtualIpRequest request
        :return: tuple(DisassociateServerVirtualIpResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['nic_id', 'disassociate_server_virtual_ip_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'nic_id' in local_var_params:
            path_params['nic_id'] = local_var_params['nic_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/nics/{nic_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='DisassociateServerVirtualIpResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def list_flavors(self, request):
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
        :return: tuple(ListFlavorsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['availability_zone']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/flavors', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListFlavorsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def list_resize_flavors(self, request):
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
        :return: tuple(ListResizeFlavorsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['instance_uuid', 'source_flavor_id', 'source_flavor_name', 'sort_key', 'sort_dir', 'marker']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_uuid' in local_var_params:
            query_params.append(('instance_uuid', local_var_params['instance_uuid']))
        if 'source_flavor_id' in local_var_params:
            query_params.append(('source_flavor_id', local_var_params['source_flavor_id']))
        if 'source_flavor_name' in local_var_params:
            query_params.append(('source_flavor_name', local_var_params['source_flavor_name']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/resize_flavors', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListResizeFlavorsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def list_server_block_devices(self, request):
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
        :return: tuple(ListServerBlockDevicesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/{server_id}/block_device', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListServerBlockDevicesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def list_server_interfaces(self, request):
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
        :return: tuple(ListServerInterfacesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/{server_id}/os-interface', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListServerInterfacesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def list_server_tags(self, request):
        """查询项目标签

        项目（Project）用于将OpenStack的资源（计算资源、存储资源和网络资源）进行分组和隔离。项目可以是一个部门或者一个项目组。一个帐户中可以创建多个项目。  该接口用于查询用户在指定项目所使用的全部标签。

        :param ListServerTagsRequest request
        :return: object
        """
        return self.list_server_tags_with_http_info(request)

    def list_server_tags_with_http_info(self, request):
        """查询项目标签

        项目（Project）用于将OpenStack的资源（计算资源、存储资源和网络资源）进行分组和隔离。项目可以是一个部门或者一个项目组。一个帐户中可以创建多个项目。  该接口用于查询用户在指定项目所使用的全部标签。

        :param ListServerTagsRequest request
        :return: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/tags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='object',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def list_server_volume_attachments(self, request):
        """查询弹性云服务器挂载磁盘信息

        查询弹性云服务器挂载的磁盘信息。

        :param ListServerVolumeAttachmentsRequest request
        :return: ListServerVolumeAttachmentsResponse
        """
        return self.list_server_volume_attachments_with_http_info(request)

    def list_server_volume_attachments_with_http_info(self, request):
        """查询弹性云服务器挂载磁盘信息

        查询弹性云服务器挂载的磁盘信息。

        :param ListServerVolumeAttachmentsRequest request
        :return: tuple(ListServerVolumeAttachmentsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/{server_id}/os-volume_attachments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListServerVolumeAttachmentsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def list_servers_details(self, request):
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
        :return: tuple(ListServersDetailsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['offset', 'flavor', 'name', 'status', 'not_tags', 'reservation_id', 'enterprise_project_id', 'tags', 'ip']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'flavor' in local_var_params:
            query_params.append(('flavor', local_var_params['flavor']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'not_tags' in local_var_params:
            query_params.append(('not-tags', local_var_params['not_tags']))
        if 'reservation_id' in local_var_params:
            query_params.append(('reservation_id', local_var_params['reservation_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/detail', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListServersDetailsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def migrate_server(self, request):
        """冷迁移云服务器

        - 将部署在专属主机上的弹性云服务器迁移至其他专属主机。 - 将部署在专属主机上的弹性云服务器迁移至公共资源池，即不再部署在专属主机上。 - 将公共资源池的弹性云服务器迁移至专属主机上，成为专属主机上部署的弹性云服务器。

        :param MigrateServerRequest request
        :return: MigrateServerResponse
        """
        return self.migrate_server_with_http_info(request)

    def migrate_server_with_http_info(self, request):
        """冷迁移云服务器

        - 将部署在专属主机上的弹性云服务器迁移至其他专属主机。 - 将部署在专属主机上的弹性云服务器迁移至公共资源池，即不再部署在专属主机上。 - 将公共资源池的弹性云服务器迁移至专属主机上，成为专属主机上部署的弹性云服务器。

        :param MigrateServerRequest request
        :return: tuple(MigrateServerResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id', 'migrate_server_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/{server_id}/migrate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='MigrateServerResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_associate_security_group(self, request):
        """添加安全组

        为弹性云服务器添加一个安全组。  添加多个安全组时，建议最多为弹性云服务器添加5个安全组。

        :param NovaAssociateSecurityGroupRequest request
        :return: None
        """
        return self.nova_associate_security_group_with_http_info(request)

    def nova_associate_security_group_with_http_info(self, request):
        """添加安全组

        为弹性云服务器添加一个安全组。  添加多个安全组时，建议最多为弹性云服务器添加5个安全组。

        :param NovaAssociateSecurityGroupRequest request
        :return: None
        """

        all_params = ['server_id', 'nova_associate_security_group_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_attach_interface(self, request):
        """添加云服务器网卡

        给云服务器添加一张网卡。

        :param NovaAttachInterfaceRequest request
        :return: NovaAttachInterfaceResponse
        """
        return self.nova_attach_interface_with_http_info(request)

    def nova_attach_interface_with_http_info(self, request):
        """添加云服务器网卡

        给云服务器添加一张网卡。

        :param NovaAttachInterfaceRequest request
        :return: tuple(NovaAttachInterfaceResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id', 'nova_attach_interface_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/os-interface', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaAttachInterfaceResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_attach_volume(self, request):
        """弹性云服务器挂载磁盘

        弹性云服务器挂载磁盘。

        :param NovaAttachVolumeRequest request
        :return: NovaAttachVolumeResponse
        """
        return self.nova_attach_volume_with_http_info(request)

    def nova_attach_volume_with_http_info(self, request):
        """弹性云服务器挂载磁盘

        弹性云服务器挂载磁盘。

        :param NovaAttachVolumeRequest request
        :return: tuple(NovaAttachVolumeResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id', 'nova_attach_volume_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/os-volume_attachments', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaAttachVolumeResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_confirm_resize_server(self, request):
        """确认变更云服务器规格

        确认单台云服务器规格调整。

        :param NovaConfirmResizeServerRequest request
        :return: None
        """
        return self.nova_confirm_resize_server_with_http_info(request)

    def nova_confirm_resize_server_with_http_info(self, request):
        """确认变更云服务器规格

        确认单台云服务器规格调整。

        :param NovaConfirmResizeServerRequest request
        :return: None
        """

        all_params = ['server_id', 'nova_confirm_resize_server_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_create_keypair(self, request):
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
        :return: tuple(NovaCreateKeypairResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['nova_create_keypair_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-keypairs', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaCreateKeypairResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_create_security_group(self, request):
        """创建安全组(废弃,不推荐使用)

        创建安全组

        :param NovaCreateSecurityGroupRequest request
        :return: NovaCreateSecurityGroupResponse
        """
        return self.nova_create_security_group_with_http_info(request)

    def nova_create_security_group_with_http_info(self, request):
        """创建安全组(废弃,不推荐使用)

        创建安全组

        :param NovaCreateSecurityGroupRequest request
        :return: tuple(NovaCreateSecurityGroupResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['nova_create_security_group_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-security-groups', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaCreateSecurityGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_create_security_group_rule(self, request):
        """创建安全组规则(废弃,不推荐使用)

        创建安全组规则

        :param NovaCreateSecurityGroupRuleRequest request
        :return: NovaCreateSecurityGroupRuleResponse
        """
        return self.nova_create_security_group_rule_with_http_info(request)

    def nova_create_security_group_rule_with_http_info(self, request):
        """创建安全组规则(废弃,不推荐使用)

        创建安全组规则

        :param NovaCreateSecurityGroupRuleRequest request
        :return: tuple(NovaCreateSecurityGroupRuleResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['nova_create_security_group_rule_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-security-group-rules', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaCreateSecurityGroupRuleResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_create_server_group(self, request):
        """创建云服务器组

        创建弹性云服务器组。

        :param NovaCreateServerGroupRequest request
        :return: NovaCreateServerGroupResponse
        """
        return self.nova_create_server_group_with_http_info(request)

    def nova_create_server_group_with_http_info(self, request):
        """创建云服务器组

        创建弹性云服务器组。

        :param NovaCreateServerGroupRequest request
        :return: tuple(NovaCreateServerGroupResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['nova_create_server_group_request_body', 'open_stack_api_version']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-server-groups', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaCreateServerGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_create_server_metadata(self, request):
        """设置云服务器元数据

        设置弹性云服务器的元数据信息。  将删除目前弹性云服务器的所有元数据信息，并更新为请求参数中的值。

        :param NovaCreateServerMetadataRequest request
        :return: NovaCreateServerMetadataResponse
        """
        return self.nova_create_server_metadata_with_http_info(request)

    def nova_create_server_metadata_with_http_info(self, request):
        """设置云服务器元数据

        设置弹性云服务器的元数据信息。  将删除目前弹性云服务器的所有元数据信息，并更新为请求参数中的值。

        :param NovaCreateServerMetadataRequest request
        :return: tuple(NovaCreateServerMetadataResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id', 'nova_create_server_metadata_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/metadata', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaCreateServerMetadataResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_create_servers(self, request):
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
        :return: tuple(NovaCreateServersResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['nova_create_servers_request_body', 'open_stack_api_version']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaCreateServersResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_create_snapshot(self, request):
        """创建快照（废弃, 不推荐使用）

        创建卷快照。

        :param NovaCreateSnapshotRequest request
        :return: NovaCreateSnapshotResponse
        """
        return self.nova_create_snapshot_with_http_info(request)

    def nova_create_snapshot_with_http_info(self, request):
        """创建快照（废弃, 不推荐使用）

        创建卷快照。

        :param NovaCreateSnapshotRequest request
        :return: tuple(NovaCreateSnapshotResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['nova_create_snapshot_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-snapshots', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaCreateSnapshotResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_create_snapshot_server(self, request):
        """云服务器创建镜像

        用弹性云服务器创建一个镜像，后续可以使用该镜像创建弹性云服务器。  对于弹性云服务器创建的镜像，会以快照的形式放在存储节点。  > 说明： >  > 该接口为社区原生接口，不适用公有云平台上创建镜像。 >  > - 如需创建系统盘镜像或数据盘镜像，请使用IMS接口：POST /v2/cloudimages/action，使用指导请参见《[镜像服务API参考](https://support.huaweicloud.com/api-ims/zh-cn_topic_0121588329.html)》的“制作镜像”章节。 > - 如需创建整机镜像，请使用IMS接口：POST /v1/cloudimages/wholeimages/action，使用指导请参见《[镜像服务API参考](https://support.huaweicloud.com/api-ims/zh-cn_topic_0121588329.html)》的“制作整机镜像”章节。

        :param NovaCreateSnapshotServerRequest request
        :return: NovaCreateSnapshotServerResponse
        """
        return self.nova_create_snapshot_server_with_http_info(request)

    def nova_create_snapshot_server_with_http_info(self, request):
        """云服务器创建镜像

        用弹性云服务器创建一个镜像，后续可以使用该镜像创建弹性云服务器。  对于弹性云服务器创建的镜像，会以快照的形式放在存储节点。  > 说明： >  > 该接口为社区原生接口，不适用公有云平台上创建镜像。 >  > - 如需创建系统盘镜像或数据盘镜像，请使用IMS接口：POST /v2/cloudimages/action，使用指导请参见《[镜像服务API参考](https://support.huaweicloud.com/api-ims/zh-cn_topic_0121588329.html)》的“制作镜像”章节。 > - 如需创建整机镜像，请使用IMS接口：POST /v1/cloudimages/wholeimages/action，使用指导请参见《[镜像服务API参考](https://support.huaweicloud.com/api-ims/zh-cn_topic_0121588329.html)》的“制作整机镜像”章节。

        :param NovaCreateSnapshotServerRequest request
        :return: tuple(NovaCreateSnapshotServerResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id', 'nova_create_snapshot_server_request_body', 'open_stack_api_version']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaCreateSnapshotServerResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_create_volume(self, request):
        """创建磁盘(废弃,不推荐使用)

        本接口提供创建磁盘的功能。

        :param NovaCreateVolumeRequest request
        :return: NovaCreateVolumeResponse
        """
        return self.nova_create_volume_with_http_info(request)

    def nova_create_volume_with_http_info(self, request):
        """创建磁盘(废弃,不推荐使用)

        本接口提供创建磁盘的功能。

        :param NovaCreateVolumeRequest request
        :return: tuple(NovaCreateVolumeResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['nova_create_volume_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-volumes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaCreateVolumeResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_delete_image(self, request):
        """删除镜像(废弃,不推荐使用)

        删除指定的镜像。镜像删除后，不能恢复。

        :param NovaDeleteImageRequest request
        :return: None
        """
        return self.nova_delete_image_with_http_info(request)

    def nova_delete_image_with_http_info(self, request):
        """删除镜像(废弃,不推荐使用)

        删除指定的镜像。镜像删除后，不能恢复。

        :param NovaDeleteImageRequest request
        :return: None
        """

        all_params = ['image_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/images/{image_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_delete_keypair(self, request):
        """删除SSH密钥

        根据SSH密钥的名称，删除指定SSH密钥。

        :param NovaDeleteKeypairRequest request
        :return: None
        """
        return self.nova_delete_keypair_with_http_info(request)

    def nova_delete_keypair_with_http_info(self, request):
        """删除SSH密钥

        根据SSH密钥的名称，删除指定SSH密钥。

        :param NovaDeleteKeypairRequest request
        :return: None
        """

        all_params = ['keypair_name']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-keypairs/{keypair_name}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_delete_security_group(self, request):
        """删除安全组(废弃,不推荐使用)

        删除安全组。

        :param NovaDeleteSecurityGroupRequest request
        :return: None
        """
        return self.nova_delete_security_group_with_http_info(request)

    def nova_delete_security_group_with_http_info(self, request):
        """删除安全组(废弃,不推荐使用)

        删除安全组。

        :param NovaDeleteSecurityGroupRequest request
        :return: None
        """

        all_params = ['security_group_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'security_group_id' in local_var_params:
            path_params['security_group_id'] = local_var_params['security_group_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-security-groups/{security_group_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_delete_security_group_rule(self, request):
        """删除安全组规则(废弃,不推荐使用)

        删除安全组规则

        :param NovaDeleteSecurityGroupRuleRequest request
        :return: None
        """
        return self.nova_delete_security_group_rule_with_http_info(request)

    def nova_delete_security_group_rule_with_http_info(self, request):
        """删除安全组规则(废弃,不推荐使用)

        删除安全组规则

        :param NovaDeleteSecurityGroupRuleRequest request
        :return: None
        """

        all_params = ['security_group_rule_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'security_group_rule_id' in local_var_params:
            path_params['security_group_rule_id'] = local_var_params['security_group_rule_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-security-group-rules/{security_group_rule_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_delete_server(self, request):
        """删除云服务器

        删除一台云服务器。

        :param NovaDeleteServerRequest request
        :return: None
        """
        return self.nova_delete_server_with_http_info(request)

    def nova_delete_server_with_http_info(self, request):
        """删除云服务器

        删除一台云服务器。

        :param NovaDeleteServerRequest request
        :return: None
        """

        all_params = ['server_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_delete_server_group(self, request):
        """删除云服务器组

        删除云服务器组。

        :param NovaDeleteServerGroupRequest request
        :return: None
        """
        return self.nova_delete_server_group_with_http_info(request)

    def nova_delete_server_group_with_http_info(self, request):
        """删除云服务器组

        删除云服务器组。

        :param NovaDeleteServerGroupRequest request
        :return: None
        """

        all_params = ['server_group_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-server-groups/{server_group_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_delete_server_metadata_item(self, request):
        """删除云服务器指定元数据

        删除云服务器指定元数据。

        :param NovaDeleteServerMetadataItemRequest request
        :return: None
        """
        return self.nova_delete_server_metadata_item_with_http_info(request)

    def nova_delete_server_metadata_item_with_http_info(self, request):
        """删除云服务器指定元数据

        删除云服务器指定元数据。

        :param NovaDeleteServerMetadataItemRequest request
        :return: None
        """

        all_params = ['key', 'server_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/metadata/{key}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_delete_server_password(self, request):
        """Windows云服务器清除密码

        清除Windows云服务器初始安装时系统生成的密码记录。清除密码后，不影响云服务器密码登录功能，但不能再使用获取密码功能来查询该云服务器密码。

        :param NovaDeleteServerPasswordRequest request
        :return: None
        """
        return self.nova_delete_server_password_with_http_info(request)

    def nova_delete_server_password_with_http_info(self, request):
        """Windows云服务器清除密码

        清除Windows云服务器初始安装时系统生成的密码记录。清除密码后，不影响云服务器密码登录功能，但不能再使用获取密码功能来查询该云服务器密码。

        :param NovaDeleteServerPasswordRequest request
        :return: None
        """

        all_params = ['server_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/os-server-password', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_delete_server_tag(self, request):
        """删除指定云服务器的标签

        删除弹性云服务器指定标签。  需在客户端通过以下HTTP header指定微版本号：X-OpenStack-Nova-API-Version: 2.26。

        :param NovaDeleteServerTagRequest request
        :return: None
        """
        return self.nova_delete_server_tag_with_http_info(request)

    def nova_delete_server_tag_with_http_info(self, request):
        """删除指定云服务器的标签

        删除弹性云服务器指定标签。  需在客户端通过以下HTTP header指定微版本号：X-OpenStack-Nova-API-Version: 2.26。

        :param NovaDeleteServerTagRequest request
        :return: None
        """

        all_params = ['server_id', 'tag', 'open_stack_api_version']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']
        if 'tag' in local_var_params:
            path_params['tag'] = local_var_params['tag']

        query_params = []

        header_params = {}
        if 'open_stack_api_version' in local_var_params:
            header_params['OpenStack-API-Version'] = local_var_params['open_stack_api_version']

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/tags/{tag}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_delete_server_tags(self, request):
        """删除云服务器标签

        删除云服务器所有tag。  需在客户端通过以下HTTP header指定微版本号：X-OpenStack-Nova-API-Version: 2.26。

        :param NovaDeleteServerTagsRequest request
        :return: None
        """
        return self.nova_delete_server_tags_with_http_info(request)

    def nova_delete_server_tags_with_http_info(self, request):
        """删除云服务器标签

        删除云服务器所有tag。  需在客户端通过以下HTTP header指定微版本号：X-OpenStack-Nova-API-Version: 2.26。

        :param NovaDeleteServerTagsRequest request
        :return: None
        """

        all_params = ['server_id', 'open_stack_api_version']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/tags', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_delete_snapshot(self, request):
        """删除快照（废弃, 不推荐使用）

        删除卷快照。

        :param NovaDeleteSnapshotRequest request
        :return: None
        """
        return self.nova_delete_snapshot_with_http_info(request)

    def nova_delete_snapshot_with_http_info(self, request):
        """删除快照（废弃, 不推荐使用）

        删除卷快照。

        :param NovaDeleteSnapshotRequest request
        :return: None
        """

        all_params = ['snapshot_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'snapshot_id' in local_var_params:
            path_params['snapshot_id'] = local_var_params['snapshot_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-snapshots/{snapshot_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_delete_volume(self, request):
        """删除磁盘(废弃,不推荐使用)

        本接口提供删除指定磁盘的功能。

        :param NovaDeleteVolumeRequest request
        :return: None
        """
        return self.nova_delete_volume_with_http_info(request)

    def nova_delete_volume_with_http_info(self, request):
        """删除磁盘(废弃,不推荐使用)

        本接口提供删除指定磁盘的功能。

        :param NovaDeleteVolumeRequest request
        :return: None
        """

        all_params = ['volume_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-volumes/{volume_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_detach_interface(self, request):
        """删除云服务器网卡

        根据指定的Port ID，从云服务器中卸载网卡。

        :param NovaDetachInterfaceRequest request
        :return: None
        """
        return self.nova_detach_interface_with_http_info(request)

    def nova_detach_interface_with_http_info(self, request):
        """删除云服务器网卡

        根据指定的Port ID，从云服务器中卸载网卡。

        :param NovaDetachInterfaceRequest request
        :return: None
        """

        all_params = ['id', 'server_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/os-interface/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_detach_volume(self, request):
        """卸载云服务器磁盘

        弹性云服务器卸载磁盘。

        :param NovaDetachVolumeRequest request
        :return: None
        """
        return self.nova_detach_volume_with_http_info(request)

    def nova_detach_volume_with_http_info(self, request):
        """卸载云服务器磁盘

        弹性云服务器卸载磁盘。

        :param NovaDetachVolumeRequest request
        :return: None
        """

        all_params = ['server_id', 'volume_id', 'delete_flag']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/os-volume_attachments/{volume_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_disassociate_security_group(self, request):
        """移除安全组

        移除弹性云服务器中的安全组。

        :param NovaDisassociateSecurityGroupRequest request
        :return: None
        """
        return self.nova_disassociate_security_group_with_http_info(request)

    def nova_disassociate_security_group_with_http_info(self, request):
        """移除安全组

        移除弹性云服务器中的安全组。

        :param NovaDisassociateSecurityGroupRequest request
        :return: None
        """

        all_params = ['server_id', 'nova_disassociate_security_group_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_list_availability_zones(self, request):
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
        :return: tuple(NovaListAvailabilityZonesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-availability-zone', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaListAvailabilityZonesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_list_flavors(self, request):
        """查询云服务器规格列表

        查询系统中可用的弹性云服务器规格列表。

        :param NovaListFlavorsRequest request
        :return: NovaListFlavorsResponse
        """
        return self.nova_list_flavors_with_http_info(request)

    def nova_list_flavors_with_http_info(self, request):
        """查询云服务器规格列表

        查询系统中可用的弹性云服务器规格列表。

        :param NovaListFlavorsRequest request
        :return: tuple(NovaListFlavorsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['min_disk', 'min_ram', 'sort_dir', 'sort_key']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'min_disk' in local_var_params:
            query_params.append(('minDisk', local_var_params['min_disk']))
        if 'min_ram' in local_var_params:
            query_params.append(('minRam', local_var_params['min_ram']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/flavors', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaListFlavorsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_list_flavors_details(self, request):
        """查询云服务器规格详情列表

        查询云服务器规格信息列表。

        :param NovaListFlavorsDetailsRequest request
        :return: NovaListFlavorsDetailsResponse
        """
        return self.nova_list_flavors_details_with_http_info(request)

    def nova_list_flavors_details_with_http_info(self, request):
        """查询云服务器规格详情列表

        查询云服务器规格信息列表。

        :param NovaListFlavorsDetailsRequest request
        :return: tuple(NovaListFlavorsDetailsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['min_disk', 'min_ram', 'sort_dir', 'sort_key', 'open_stack_api_version']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'min_disk' in local_var_params:
            query_params.append(('minDisk', local_var_params['min_disk']))
        if 'min_ram' in local_var_params:
            query_params.append(('minRam', local_var_params['min_ram']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))

        header_params = {}
        if 'open_stack_api_version' in local_var_params:
            header_params['OpenStack-API-Version'] = local_var_params['open_stack_api_version']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/flavors/detail', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaListFlavorsDetailsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_list_images(self, request):
        """查询镜像列表(废弃,不推荐使用)

        查询所有镜像的列表信息。

        :param NovaListImagesRequest request
        :return: NovaListImagesResponse
        """
        return self.nova_list_images_with_http_info(request)

    def nova_list_images_with_http_info(self, request):
        """查询镜像列表(废弃,不推荐使用)

        查询所有镜像的列表信息。

        :param NovaListImagesRequest request
        :return: tuple(NovaListImagesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['changes_since', 'min_disk', 'min_ram', 'name', 'status', 'limit', 'marker']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'changes_since' in local_var_params:
            query_params.append(('changes-since', local_var_params['changes_since']))
        if 'min_disk' in local_var_params:
            query_params.append(('minDisk', local_var_params['min_disk']))
        if 'min_ram' in local_var_params:
            query_params.append(('minRam', local_var_params['min_ram']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/images', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaListImagesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_list_images_details(self, request):
        """查询镜像列表详情(废弃,不推荐使用)

        查询详细的镜像信息列表。

        :param NovaListImagesDetailsRequest request
        :return: NovaListImagesDetailsResponse
        """
        return self.nova_list_images_details_with_http_info(request)

    def nova_list_images_details_with_http_info(self, request):
        """查询镜像列表详情(废弃,不推荐使用)

        查询详细的镜像信息列表。

        :param NovaListImagesDetailsRequest request
        :return: tuple(NovaListImagesDetailsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['min_disk', 'name', 'status', 'limit', 'marker']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'min_disk' in local_var_params:
            query_params.append(('minDisk', local_var_params['min_disk']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/images/detail', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaListImagesDetailsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_list_keypairs(self, request):
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
        :return: tuple(NovaListKeypairsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['marker']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-keypairs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaListKeypairsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_list_networks(self, request):
        """查询网络列表

        查询网络列表。

        :param NovaListNetworksRequest request
        :return: NovaListNetworksResponse
        """
        return self.nova_list_networks_with_http_info(request)

    def nova_list_networks_with_http_info(self, request):
        """查询网络列表

        查询网络列表。

        :param NovaListNetworksRequest request
        :return: tuple(NovaListNetworksResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['open_stack_api_version']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-networks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaListNetworksResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_list_security_groups(self, request):
        """查询安全组列表(废弃,不推荐使用)

        查询安全组列表

        :param NovaListSecurityGroupsRequest request
        :return: NovaListSecurityGroupsResponse
        """
        return self.nova_list_security_groups_with_http_info(request)

    def nova_list_security_groups_with_http_info(self, request):
        """查询安全组列表(废弃,不推荐使用)

        查询安全组列表

        :param NovaListSecurityGroupsRequest request
        :return: tuple(NovaListSecurityGroupsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-security-groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaListSecurityGroupsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_list_server_actions(self, request):
        """查询云服务器操作行为列表

        查询弹性云服务器的所有历史操作，显示操作行为列表。

        :param NovaListServerActionsRequest request
        :return: NovaListServerActionsResponse
        """
        return self.nova_list_server_actions_with_http_info(request)

    def nova_list_server_actions_with_http_info(self, request):
        """查询云服务器操作行为列表

        查询弹性云服务器的所有历史操作，显示操作行为列表。

        :param NovaListServerActionsRequest request
        :return: tuple(NovaListServerActionsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/os-instance-actions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaListServerActionsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_list_server_groups(self, request):
        """查询云服务器组列表

        查询云服务器组列表。

        :param NovaListServerGroupsRequest request
        :return: NovaListServerGroupsResponse
        """
        return self.nova_list_server_groups_with_http_info(request)

    def nova_list_server_groups_with_http_info(self, request):
        """查询云服务器组列表

        查询云服务器组列表。

        :param NovaListServerGroupsRequest request
        :return: tuple(NovaListServerGroupsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['all_projects', 'limit', 'marker', 'open_stack_api_version']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'all_projects' in local_var_params:
            query_params.append(('all_projects', local_var_params['all_projects']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}
        if 'open_stack_api_version' in local_var_params:
            header_params['OpenStack-API-Version'] = local_var_params['open_stack_api_version']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-server-groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaListServerGroupsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_list_server_i_ps(self, request):
        """查询指定弹性云服务器的网络列表

        查询指定弹性云服务器的网络列表。

        :param NovaListServerIPsRequest request
        :return: NovaListServerIPsResponse
        """
        return self.nova_list_server_i_ps_with_http_info(request)

    def nova_list_server_i_ps_with_http_info(self, request):
        """查询指定弹性云服务器的网络列表

        查询指定弹性云服务器的网络列表。

        :param NovaListServerIPsRequest request
        :return: tuple(NovaListServerIPsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/ips', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaListServerIPsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_list_server_interfaces(self, request):
        """查询云服务器网卡信息

        查询云服务器网卡信息。

        :param NovaListServerInterfacesRequest request
        :return: NovaListServerInterfacesResponse
        """
        return self.nova_list_server_interfaces_with_http_info(request)

    def nova_list_server_interfaces_with_http_info(self, request):
        """查询云服务器网卡信息

        查询云服务器网卡信息。

        :param NovaListServerInterfacesRequest request
        :return: tuple(NovaListServerInterfacesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/os-interface', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaListServerInterfacesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_list_server_security_groups(self, request):
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
        :return: tuple(NovaListServerSecurityGroupsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/os-security-groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaListServerSecurityGroupsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_list_server_tags(self, request):
        """查询云服务器标签

        查看弹性云服务器的所有Tag。  需在客户端通过以下HTTP header指定微版本号：X-OpenStack-Nova-API-Version: 2.26。

        :param NovaListServerTagsRequest request
        :return: NovaListServerTagsResponse
        """
        return self.nova_list_server_tags_with_http_info(request)

    def nova_list_server_tags_with_http_info(self, request):
        """查询云服务器标签

        查看弹性云服务器的所有Tag。  需在客户端通过以下HTTP header指定微版本号：X-OpenStack-Nova-API-Version: 2.26。

        :param NovaListServerTagsRequest request
        :return: tuple(NovaListServerTagsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id', 'open_stack_api_version']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/tags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaListServerTagsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_list_server_volumes(self, request):
        """查询弹性云服务器器挂载磁盘信息

        查询弹性云服务器挂载的磁盘信息。

        :param NovaListServerVolumesRequest request
        :return: NovaListServerVolumesResponse
        """
        return self.nova_list_server_volumes_with_http_info(request)

    def nova_list_server_volumes_with_http_info(self, request):
        """查询弹性云服务器器挂载磁盘信息

        查询弹性云服务器挂载的磁盘信息。

        :param NovaListServerVolumesRequest request
        :return: tuple(NovaListServerVolumesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/os-volume_attachments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaListServerVolumesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_list_servers(self, request):
        """查询云服务器列表

        查询云服务器信息列表。

        :param NovaListServersRequest request
        :return: NovaListServersResponse
        """
        return self.nova_list_servers_with_http_info(request)

    def nova_list_servers_with_http_info(self, request):
        """查询云服务器列表

        查询云服务器信息列表。

        :param NovaListServersRequest request
        :return: tuple(NovaListServersResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['open_stack_api_version', 'changes_since', 'ip', 'image', 'flavor', 'name', 'status', 'limit', 'marker', 'reservation_id', 'sort_key']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'changes_since' in local_var_params:
            query_params.append(('changes-since', local_var_params['changes_since']))
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))
        if 'image' in local_var_params:
            query_params.append(('image', local_var_params['image']))
        if 'flavor' in local_var_params:
            query_params.append(('flavor', local_var_params['flavor']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'reservation_id' in local_var_params:
            query_params.append(('reservation_id', local_var_params['reservation_id']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))

        header_params = {}
        if 'open_stack_api_version' in local_var_params:
            header_params['OpenStack-API-Version'] = local_var_params['open_stack_api_version']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaListServersResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_list_servers_details(self, request):
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
        :return: tuple(NovaListServersDetailsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['open_stack_api_version', 'ip', 'image', 'flavor', 'name', 'status', 'limit', 'marker', 'tags', 'not_tags', 'reservation_id', 'sort_key']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))
        if 'image' in local_var_params:
            query_params.append(('image', local_var_params['image']))
        if 'flavor' in local_var_params:
            query_params.append(('flavor', local_var_params['flavor']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'not_tags' in local_var_params:
            query_params.append(('not-tags', local_var_params['not_tags']))
        if 'reservation_id' in local_var_params:
            query_params.append(('reservation_id', local_var_params['reservation_id']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))

        header_params = {}
        if 'open_stack_api_version' in local_var_params:
            header_params['OpenStack-API-Version'] = local_var_params['open_stack_api_version']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/detail', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaListServersDetailsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_list_volumes(self, request):
        """查询磁盘列表(废弃,不推荐使用)

        本接口提供查询磁盘概要信息的功能。

        :param NovaListVolumesRequest request
        :return: NovaListVolumesResponse
        """
        return self.nova_list_volumes_with_http_info(request)

    def nova_list_volumes_with_http_info(self, request):
        """查询磁盘列表(废弃,不推荐使用)

        本接口提供查询磁盘概要信息的功能。

        :param NovaListVolumesRequest request
        :return: tuple(NovaListVolumesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-volumes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaListVolumesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_list_volumes_details(self, request):
        """查询磁盘列表详情(废弃,不推荐使用)

        本接口提供查询卷详细信息的功能。

        :param NovaListVolumesDetailsRequest request
        :return: NovaListVolumesDetailsResponse
        """
        return self.nova_list_volumes_details_with_http_info(request)

    def nova_list_volumes_details_with_http_info(self, request):
        """查询磁盘列表详情(废弃,不推荐使用)

        本接口提供查询卷详细信息的功能。

        :param NovaListVolumesDetailsRequest request
        :return: tuple(NovaListVolumesDetailsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-volumes/detail', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaListVolumesDetailsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_lock_server(self, request):
        """锁定云服务器

        锁定弹性云服务器。  租户可以锁定自己的弹性云服务器，不能锁定其他租户的云服务器。弹性云服务器被锁定后，租户将不能再对云服务器执行管理操作。

        :param NovaLockServerRequest request
        :return: None
        """
        return self.nova_lock_server_with_http_info(request)

    def nova_lock_server_with_http_info(self, request):
        """锁定云服务器

        锁定弹性云服务器。  租户可以锁定自己的弹性云服务器，不能锁定其他租户的云服务器。弹性云服务器被锁定后，租户将不能再对云服务器执行管理操作。

        :param NovaLockServerRequest request
        :return: None
        """

        all_params = ['server_id', 'nova_lock_server_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_reboot_server(self, request):
        """重启云服务器

        重启单台云服务器。

        :param NovaRebootServerRequest request
        :return: None
        """
        return self.nova_reboot_server_with_http_info(request)

    def nova_reboot_server_with_http_info(self, request):
        """重启云服务器

        重启单台云服务器。

        :param NovaRebootServerRequest request
        :return: None
        """

        all_params = ['server_id', 'nova_reboot_server_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_resize_server(self, request):
        """变更云服务器规格

        变更单台云服务器规格。  对于运行中的弹性云服务器，系统会自动关机，并将弹性云服务器中的数据拷贝到目标节点（目标节点可与源节点相同）后重新启动弹性云服务器。  底层资源不足时，该接口会自动回滚。  该接口不单独使用，需要轮询判断虚拟机状态，当虚拟机同时满足\"status\"为\"VERIFY_RESIZE\"、\"OS-EXT-STS:task_state\"为\"\"、\"OS-EXT-STS:vm_state\"为\"RESIZED\"时，配合“确认变更云服务器规格（POST /v2/{project_id}/servers/{server_id}/action）”或“回退变更云服务器规格（POST /v2/{project_id}/servers/{server_id}/action）”两个接口一起使用。

        :param NovaResizeServerRequest request
        :return: None
        """
        return self.nova_resize_server_with_http_info(request)

    def nova_resize_server_with_http_info(self, request):
        """变更云服务器规格

        变更单台云服务器规格。  对于运行中的弹性云服务器，系统会自动关机，并将弹性云服务器中的数据拷贝到目标节点（目标节点可与源节点相同）后重新启动弹性云服务器。  底层资源不足时，该接口会自动回滚。  该接口不单独使用，需要轮询判断虚拟机状态，当虚拟机同时满足\"status\"为\"VERIFY_RESIZE\"、\"OS-EXT-STS:task_state\"为\"\"、\"OS-EXT-STS:vm_state\"为\"RESIZED\"时，配合“确认变更云服务器规格（POST /v2/{project_id}/servers/{server_id}/action）”或“回退变更云服务器规格（POST /v2/{project_id}/servers/{server_id}/action）”两个接口一起使用。

        :param NovaResizeServerRequest request
        :return: None
        """

        all_params = ['server_id', 'nova_resize_server_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_revert_resize_server(self, request):
        """回退变更云服务器规格

        回退云服务器规格变更。

        :param NovaRevertResizeServerRequest request
        :return: None
        """
        return self.nova_revert_resize_server_with_http_info(request)

    def nova_revert_resize_server_with_http_info(self, request):
        """回退变更云服务器规格

        回退云服务器规格变更。

        :param NovaRevertResizeServerRequest request
        :return: None
        """

        all_params = ['server_id', 'nova_revert_resize_server_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_show_default_quota(self, request):
        """查询默认配额

        查询默认配额。

        :param NovaShowDefaultQuotaRequest request
        :return: NovaShowDefaultQuotaResponse
        """
        return self.nova_show_default_quota_with_http_info(request)

    def nova_show_default_quota_with_http_info(self, request):
        """查询默认配额

        查询默认配额。

        :param NovaShowDefaultQuotaRequest request
        :return: tuple(NovaShowDefaultQuotaResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['open_stack_api_version']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-quota-sets/{project_id}/defaults', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaShowDefaultQuotaResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_show_flavor(self, request):
        """查询云服务器规格详情

        根据云服务器规格ID，查询云服务器规格详情信息。

        :param NovaShowFlavorRequest request
        :return: NovaShowFlavorResponse
        """
        return self.nova_show_flavor_with_http_info(request)

    def nova_show_flavor_with_http_info(self, request):
        """查询云服务器规格详情

        根据云服务器规格ID，查询云服务器规格详情信息。

        :param NovaShowFlavorRequest request
        :return: tuple(NovaShowFlavorResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['flavor_id', 'open_stack_api_version']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'flavor_id' in local_var_params:
            path_params['flavor_id'] = local_var_params['flavor_id']

        query_params = []

        header_params = {}
        if 'open_stack_api_version' in local_var_params:
            header_params['OpenStack-API-Version'] = local_var_params['open_stack_api_version']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/flavors/{flavor_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaShowFlavorResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_show_flavor_extra_specs(self, request):
        """查询云服务器规格extra_specs的详情

        查询指定的规格的详细信息。

        :param NovaShowFlavorExtraSpecsRequest request
        :return: NovaShowFlavorExtraSpecsResponse
        """
        return self.nova_show_flavor_extra_specs_with_http_info(request)

    def nova_show_flavor_extra_specs_with_http_info(self, request):
        """查询云服务器规格extra_specs的详情

        查询指定的规格的详细信息。

        :param NovaShowFlavorExtraSpecsRequest request
        :return: tuple(NovaShowFlavorExtraSpecsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['flavor_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'flavor_id' in local_var_params:
            path_params['flavor_id'] = local_var_params['flavor_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/flavors/{flavor_id}/os-extra_specs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaShowFlavorExtraSpecsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_show_image(self, request):
        """查询指定镜像详情(废弃,不推荐使用)

        查询指定的镜像的详情信息。

        :param NovaShowImageRequest request
        :return: NovaShowImageResponse
        """
        return self.nova_show_image_with_http_info(request)

    def nova_show_image_with_http_info(self, request):
        """查询指定镜像详情(废弃,不推荐使用)

        查询指定的镜像的详情信息。

        :param NovaShowImageRequest request
        :return: tuple(NovaShowImageResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['image_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/images/{image_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaShowImageResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_show_image_metadata(self, request):
        """查询指定镜像的元数据(废弃,不推荐使用)

        获取指定镜像的扩展信息。

        :param NovaShowImageMetadataRequest request
        :return: NovaShowImageMetadataResponse
        """
        return self.nova_show_image_metadata_with_http_info(request)

    def nova_show_image_metadata_with_http_info(self, request):
        """查询指定镜像的元数据(废弃,不推荐使用)

        获取指定镜像的扩展信息。

        :param NovaShowImageMetadataRequest request
        :return: tuple(NovaShowImageMetadataResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['image_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/images/{image_id}/metadata', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaShowImageMetadataResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_show_keypair(self, request):
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
        :return: tuple(NovaShowKeypairResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['keypair_name', 'open_stack_api_version']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-keypairs/{keypair_name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaShowKeypairResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_show_limits(self, request):
        """查询租户配额限制

        查询租户配额限制。  租户只能查询自己的配额限制，不能查询其他租户的配额限制。

        :param NovaShowLimitsRequest request
        :return: NovaShowLimitsResponse
        """
        return self.nova_show_limits_with_http_info(request)

    def nova_show_limits_with_http_info(self, request):
        """查询租户配额限制

        查询租户配额限制。  租户只能查询自己的配额限制，不能查询其他租户的配额限制。

        :param NovaShowLimitsRequest request
        :return: tuple(NovaShowLimitsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['open_stack_api_version']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/limits', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaShowLimitsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_show_quotas(self, request):
        """查询租户配额

        查询配额，包括云服务器、CPU、内存等计算资源的规格。  提供user_id参数，对应user执行相应操作，获取指定user的quota配置。

        :param NovaShowQuotasRequest request
        :return: NovaShowQuotasResponse
        """
        return self.nova_show_quotas_with_http_info(request)

    def nova_show_quotas_with_http_info(self, request):
        """查询租户配额

        查询配额，包括云服务器、CPU、内存等计算资源的规格。  提供user_id参数，对应user执行相应操作，获取指定user的quota配置。

        :param NovaShowQuotasRequest request
        :return: tuple(NovaShowQuotasResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['user_id', 'open_stack_api_version']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in local_var_params:
            query_params.append(('user_id', local_var_params['user_id']))

        header_params = {}
        if 'open_stack_api_version' in local_var_params:
            header_params['OpenStack-API-Version'] = local_var_params['open_stack_api_version']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-quota-sets/{project_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaShowQuotasResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_show_remote_console(self, request):
        """获取远程consoles登录地址（微版本2.6及以上）

        获取弹性云服务器VNC远程登录地址。

        :param NovaShowRemoteConsoleRequest request
        :return: NovaShowRemoteConsoleResponse
        """
        return self.nova_show_remote_console_with_http_info(request)

    def nova_show_remote_console_with_http_info(self, request):
        """获取远程consoles登录地址（微版本2.6及以上）

        获取弹性云服务器VNC远程登录地址。

        :param NovaShowRemoteConsoleRequest request
        :return: tuple(NovaShowRemoteConsoleResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['x_open_stack_nova_api_version', 'server_id', 'nova_show_remote_console_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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
        if 'x_open_stack_nova_api_version' in local_var_params:
            header_params['X-OpenStack-Nova-API-Version'] = local_var_params['x_open_stack_nova_api_version']

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/remote-consoles', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaShowRemoteConsoleResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_show_security_group(self, request):
        """查询安全组详细信息(废弃,不推荐使用)

        查询安全组详细信息。  该接口只能查询入方向安全组规则，如需查询出方向的安全组规则，请参见《虚拟私有云接口参考》的”安全组（原生OpenStack接口）> 查询安全组详情“章节。

        :param NovaShowSecurityGroupRequest request
        :return: NovaShowSecurityGroupResponse
        """
        return self.nova_show_security_group_with_http_info(request)

    def nova_show_security_group_with_http_info(self, request):
        """查询安全组详细信息(废弃,不推荐使用)

        查询安全组详细信息。  该接口只能查询入方向安全组规则，如需查询出方向的安全组规则，请参见《虚拟私有云接口参考》的”安全组（原生OpenStack接口）> 查询安全组详情“章节。

        :param NovaShowSecurityGroupRequest request
        :return: tuple(NovaShowSecurityGroupResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['security_group_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'security_group_id' in local_var_params:
            path_params['security_group_id'] = local_var_params['security_group_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-security-groups/{security_group_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaShowSecurityGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_show_server(self, request):
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
        :return: tuple(NovaShowServerResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id', 'open_stack_api_version']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaShowServerResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_show_server_action(self, request):
        """通过请求ID查询云服务器行为

        查询弹性云服务器的某个请求行为。

        :param NovaShowServerActionRequest request
        :return: NovaShowServerActionResponse
        """
        return self.nova_show_server_action_with_http_info(request)

    def nova_show_server_action_with_http_info(self, request):
        """通过请求ID查询云服务器行为

        查询弹性云服务器的某个请求行为。

        :param NovaShowServerActionRequest request
        :return: tuple(NovaShowServerActionResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['request_id', 'server_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'request_id' in local_var_params:
            path_params['request_id'] = local_var_params['request_id']
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/os-instance-actions/{request_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaShowServerActionResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_show_server_console_logs(self, request):
        """获取弹性云服务器的控制台日志

        显示弹性云服务器控制台日志。

        :param NovaShowServerConsoleLogsRequest request
        :return: NovaShowServerConsoleLogsResponse
        """
        return self.nova_show_server_console_logs_with_http_info(request)

    def nova_show_server_console_logs_with_http_info(self, request):
        """获取弹性云服务器的控制台日志

        显示弹性云服务器控制台日志。

        :param NovaShowServerConsoleLogsRequest request
        :return: tuple(NovaShowServerConsoleLogsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id', 'nova_show_server_console_logs_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaShowServerConsoleLogsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_show_server_group(self, request):
        """查询云服务器组详情

        查询云服务器组详情。

        :param NovaShowServerGroupRequest request
        :return: NovaShowServerGroupResponse
        """
        return self.nova_show_server_group_with_http_info(request)

    def nova_show_server_group_with_http_info(self, request):
        """查询云服务器组详情

        查询云服务器组详情。

        :param NovaShowServerGroupRequest request
        :return: tuple(NovaShowServerGroupResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_group_id', 'open_stack_api_version']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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
        if 'open_stack_api_version' in local_var_params:
            header_params['OpenStack-API-Version'] = local_var_params['open_stack_api_version']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-server-groups/{server_group_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaShowServerGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_show_server_interface(self, request):
        """查询指定云服务器网卡信息

        根据网卡ID，查询云服务器网卡信息。

        :param NovaShowServerInterfaceRequest request
        :return: NovaShowServerInterfaceResponse
        """
        return self.nova_show_server_interface_with_http_info(request)

    def nova_show_server_interface_with_http_info(self, request):
        """查询指定云服务器网卡信息

        根据网卡ID，查询云服务器网卡信息。

        :param NovaShowServerInterfaceRequest request
        :return: tuple(NovaShowServerInterfaceResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['id', 'server_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/os-interface/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaShowServerInterfaceResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_show_server_ip(self, request):
        """查询弹性云服务器的指定网络

        查询指定弹性云服务器的指定网络。

        :param NovaShowServerIpRequest request
        :return: dict(str, list[NovaNetwork])
        """
        return self.nova_show_server_ip_with_http_info(request)

    def nova_show_server_ip_with_http_info(self, request):
        """查询弹性云服务器的指定网络

        查询指定弹性云服务器的指定网络。

        :param NovaShowServerIpRequest request
        :return: tuple(dict(str, list[NovaNetwork]), status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['network_name', 'server_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'network_name' in local_var_params:
            path_params['networkName'] = local_var_params['network_name']
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/ips/{networkName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='dict(str, list[NovaNetwork])',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_show_server_metadata(self, request):
        """查询云服务器元数据列表

        查询弹性云服务器的元数据信息。

        :param NovaShowServerMetadataRequest request
        :return: NovaShowServerMetadataResponse
        """
        return self.nova_show_server_metadata_with_http_info(request)

    def nova_show_server_metadata_with_http_info(self, request):
        """查询云服务器元数据列表

        查询弹性云服务器的元数据信息。

        :param NovaShowServerMetadataRequest request
        :return: tuple(NovaShowServerMetadataResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/metadata', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaShowServerMetadataResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_show_server_metadata_item(self, request):
        """获取云服务器指定Key的元数据

        获取云服务器指定key的元数据信息。

        :param NovaShowServerMetadataItemRequest request
        :return: object
        """
        return self.nova_show_server_metadata_item_with_http_info(request)

    def nova_show_server_metadata_item_with_http_info(self, request):
        """获取云服务器指定Key的元数据

        获取云服务器指定key的元数据信息。

        :param NovaShowServerMetadataItemRequest request
        :return: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['key', 'server_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/metadata/{key}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='object',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_show_server_password(self, request):
        """Windows云服务器获取密码

        当通过支持Cloudbase-init功能的镜像创建Windows云服务器时，获取云服务器初始安装时系统生成的管理员帐户（Administrator帐户或Cloudbase-init设置的帐户）随机密码。  当云服务器启动后，需要等待5~10分钟，保证密码注入完成，才可使用此接口查询到密码。

        :param NovaShowServerPasswordRequest request
        :return: NovaShowServerPasswordResponse
        """
        return self.nova_show_server_password_with_http_info(request)

    def nova_show_server_password_with_http_info(self, request):
        """Windows云服务器获取密码

        当通过支持Cloudbase-init功能的镜像创建Windows云服务器时，获取云服务器初始安装时系统生成的管理员帐户（Administrator帐户或Cloudbase-init设置的帐户）随机密码。  当云服务器启动后，需要等待5~10分钟，保证密码注入完成，才可使用此接口查询到密码。

        :param NovaShowServerPasswordRequest request
        :return: tuple(NovaShowServerPasswordResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/os-server-password', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaShowServerPasswordResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_show_server_tag(self, request):
        """查询云服务器是否存在指定标签

        查看弹性云服务器是否存在指定标签。  需在客户端通过以下HTTP header指定微版本号：X-OpenStack-Nova-API-Version: 2.26。

        :param NovaShowServerTagRequest request
        :return: None
        """
        return self.nova_show_server_tag_with_http_info(request)

    def nova_show_server_tag_with_http_info(self, request):
        """查询云服务器是否存在指定标签

        查看弹性云服务器是否存在指定标签。  需在客户端通过以下HTTP header指定微版本号：X-OpenStack-Nova-API-Version: 2.26。

        :param NovaShowServerTagRequest request
        :return: None
        """

        all_params = ['server_id', 'tag', 'open_stack_api_version']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']
        if 'tag' in local_var_params:
            path_params['tag'] = local_var_params['tag']

        query_params = []

        header_params = {}
        if 'open_stack_api_version' in local_var_params:
            header_params['OpenStack-API-Version'] = local_var_params['open_stack_api_version']

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/tags/{tag}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_show_server_volume(self, request):
        """查询弹性云服务器挂载的单个磁盘信息

        根据磁盘ID，查询云服务器挂载的单个磁盘信息。

        :param NovaShowServerVolumeRequest request
        :return: NovaShowServerVolumeResponse
        """
        return self.nova_show_server_volume_with_http_info(request)

    def nova_show_server_volume_with_http_info(self, request):
        """查询弹性云服务器挂载的单个磁盘信息

        根据磁盘ID，查询云服务器挂载的单个磁盘信息。

        :param NovaShowServerVolumeRequest request
        :return: tuple(NovaShowServerVolumeResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id', 'volume_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/os-volume_attachments/{volume_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaShowServerVolumeResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_show_snapshot(self, request):
        """查询快照（废弃, 不推荐使用）

        查询单独卷快照信息。

        :param NovaShowSnapshotRequest request
        :return: NovaShowSnapshotResponse
        """
        return self.nova_show_snapshot_with_http_info(request)

    def nova_show_snapshot_with_http_info(self, request):
        """查询快照（废弃, 不推荐使用）

        查询单独卷快照信息。

        :param NovaShowSnapshotRequest request
        :return: tuple(NovaShowSnapshotResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['snapshot_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'snapshot_id' in local_var_params:
            path_params['snapshot_id'] = local_var_params['snapshot_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-snapshots/{snapshot_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaShowSnapshotResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_show_volume(self, request):
        """查询磁盘(废弃,不推荐使用)

        本接口提供查询指定磁盘信息的功能。

        :param NovaShowVolumeRequest request
        :return: NovaShowVolumeResponse
        """
        return self.nova_show_volume_with_http_info(request)

    def nova_show_volume_with_http_info(self, request):
        """查询磁盘(废弃,不推荐使用)

        本接口提供查询指定磁盘信息的功能。

        :param NovaShowVolumeRequest request
        :return: tuple(NovaShowVolumeResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['volume_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-volumes/{volume_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaShowVolumeResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_start_server(self, request):
        """启动云服务器

        启动单台云服务器。

        :param NovaStartServerRequest request
        :return: None
        """
        return self.nova_start_server_with_http_info(request)

    def nova_start_server_with_http_info(self, request):
        """启动云服务器

        启动单台云服务器。

        :param NovaStartServerRequest request
        :return: None
        """

        all_params = ['server_id', 'nova_start_server_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_stop_server(self, request):
        """关闭云服务器

        关闭单台云服务器。

        :param NovaStopServerRequest request
        :return: None
        """
        return self.nova_stop_server_with_http_info(request)

    def nova_stop_server_with_http_info(self, request):
        """关闭云服务器

        关闭单台云服务器。

        :param NovaStopServerRequest request
        :return: None
        """

        all_params = ['server_id', 'nova_stop_server_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_unlock_server(self, request):
        """解锁云服务器

        解锁弹性云服务器。  弹性云服务器被解锁定后，将允许普通用户对云服务器执行管理操作。

        :param NovaUnlockServerRequest request
        :return: None
        """
        return self.nova_unlock_server_with_http_info(request)

    def nova_unlock_server_with_http_info(self, request):
        """解锁云服务器

        解锁弹性云服务器。  弹性云服务器被解锁定后，将允许普通用户对云服务器执行管理操作。

        :param NovaUnlockServerRequest request
        :return: None
        """

        all_params = ['server_id', 'nova_unlock_server_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_update_security_group(self, request):
        """更新安全组信息(废弃,不推荐使用)

        更新安全组

        :param NovaUpdateSecurityGroupRequest request
        :return: NovaUpdateSecurityGroupResponse
        """
        return self.nova_update_security_group_with_http_info(request)

    def nova_update_security_group_with_http_info(self, request):
        """更新安全组信息(废弃,不推荐使用)

        更新安全组

        :param NovaUpdateSecurityGroupRequest request
        :return: tuple(NovaUpdateSecurityGroupResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['security_group_id', 'nova_update_security_group_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'security_group_id' in local_var_params:
            path_params['security_group_id'] = local_var_params['security_group_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-security-groups/{security_group_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaUpdateSecurityGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_update_server(self, request):
        """修改云服务器

        修改云服务器信息，目前支持修改云服务器名称及描述。

        :param NovaUpdateServerRequest request
        :return: NovaUpdateServerResponse
        """
        return self.nova_update_server_with_http_info(request)

    def nova_update_server_with_http_info(self, request):
        """修改云服务器

        修改云服务器信息，目前支持修改云服务器名称及描述。

        :param NovaUpdateServerRequest request
        :return: tuple(NovaUpdateServerResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id', 'nova_update_server_request_body', 'open_stack_api_version']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaUpdateServerResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_update_server_metadata(self, request):
        """更新云服务器元数据

        更新云服务器元数据。  - 如果元数据中没有待更新字段，则自动添加该字段。 - 如果元数据中已存在待更新字段，则直接更新字段值。 - 如果元数据中的字段不再请求参数中，则保持不变

        :param NovaUpdateServerMetadataRequest request
        :return: NovaUpdateServerMetadataResponse
        """
        return self.nova_update_server_metadata_with_http_info(request)

    def nova_update_server_metadata_with_http_info(self, request):
        """更新云服务器元数据

        更新云服务器元数据。  - 如果元数据中没有待更新字段，则自动添加该字段。 - 如果元数据中已存在待更新字段，则直接更新字段值。 - 如果元数据中的字段不再请求参数中，则保持不变

        :param NovaUpdateServerMetadataRequest request
        :return: tuple(NovaUpdateServerMetadataResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id', 'nova_update_server_metadata_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/metadata', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaUpdateServerMetadataResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_update_server_metadata_item(self, request):
        """修改云服务器指定Key的元数据

        设置云服务器指定key的元数据。  - 如果元数据中没有待更新字段，则自动添加该字段。 - 如果元数据中已存在待更新字段，则直接更新字段值

        :param NovaUpdateServerMetadataItemRequest request
        :return: NovaUpdateServerMetadataItemResponse
        """
        return self.nova_update_server_metadata_item_with_http_info(request)

    def nova_update_server_metadata_item_with_http_info(self, request):
        """修改云服务器指定Key的元数据

        设置云服务器指定key的元数据。  - 如果元数据中没有待更新字段，则自动添加该字段。 - 如果元数据中已存在待更新字段，则直接更新字段值

        :param NovaUpdateServerMetadataItemRequest request
        :return: tuple(NovaUpdateServerMetadataItemResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['key', 'server_id', 'nova_update_server_metadata_item_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/metadata/{key}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaUpdateServerMetadataItemResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_update_server_tag(self, request):
        """给指定弹性云服务器添加标签

        为弹性云服务器添加一个tag。  需在客户端通过以下HTTP header指定微版本号：X-OpenStack-Nova-API-Version: 2.26。

        :param NovaUpdateServerTagRequest request
        :return: None
        """
        return self.nova_update_server_tag_with_http_info(request)

    def nova_update_server_tag_with_http_info(self, request):
        """给指定弹性云服务器添加标签

        为弹性云服务器添加一个tag。  需在客户端通过以下HTTP header指定微版本号：X-OpenStack-Nova-API-Version: 2.26。

        :param NovaUpdateServerTagRequest request
        :return: None
        """

        all_params = ['server_id', 'tag', 'open_stack_api_version']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']
        if 'tag' in local_var_params:
            path_params['tag'] = local_var_params['tag']

        query_params = []

        header_params = {}
        if 'open_stack_api_version' in local_var_params:
            header_params['OpenStack-API-Version'] = local_var_params['open_stack_api_version']

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/tags/{tag}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_update_server_tags(self, request):
        """创建云服务器标签

        为云服务器添加tags。  需在客户端通过以下HTTP header指定微版本号：X-OpenStack-Nova-API-Version: 2.26。

        :param NovaUpdateServerTagsRequest request
        :return: NovaUpdateServerTagsResponse
        """
        return self.nova_update_server_tags_with_http_info(request)

    def nova_update_server_tags_with_http_info(self, request):
        """创建云服务器标签

        为云服务器添加tags。  需在客户端通过以下HTTP header指定微版本号：X-OpenStack-Nova-API-Version: 2.26。

        :param NovaUpdateServerTagsRequest request
        :return: tuple(NovaUpdateServerTagsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id', 'nova_update_server_tags_request_body', 'open_stack_api_version']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/tags', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaUpdateServerTagsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def register_server_auto_recovery(self, request):
        """管理云服务器自动恢复动作

        配置、删除云服务器自动恢复动作。

        :param RegisterServerAutoRecoveryRequest request
        :return: None
        """
        return self.register_server_auto_recovery_with_http_info(request)

    def register_server_auto_recovery_with_http_info(self, request):
        """管理云服务器自动恢复动作

        配置、删除云服务器自动恢复动作。

        :param RegisterServerAutoRecoveryRequest request
        :return: None
        """

        all_params = ['server_id', 'register_server_auto_recovery_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/{server_id}/autorecovery', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def reinstall_server_with_cloud_init(self, request):
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
        :return: tuple(ReinstallServerWithCloudInitResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id', 'reinstall_server_with_cloud_init_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/cloudservers/{server_id}/reinstallos', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ReinstallServerWithCloudInitResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def reinstall_server_without_cloud_init(self, request):
        """重装弹性云服务器操作系统(未安装Cloud init)

        重装弹性云服务器的操作系统。  该接口支持未安装Cloud-init或Cloudbase-init的镜像。

        :param ReinstallServerWithoutCloudInitRequest request
        :return: ReinstallServerWithoutCloudInitResponse
        """
        return self.reinstall_server_without_cloud_init_with_http_info(request)

    def reinstall_server_without_cloud_init_with_http_info(self, request):
        """重装弹性云服务器操作系统(未安装Cloud init)

        重装弹性云服务器的操作系统。  该接口支持未安装Cloud-init或Cloudbase-init的镜像。

        :param ReinstallServerWithoutCloudInitRequest request
        :return: tuple(ReinstallServerWithoutCloudInitResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id', 'reinstall_server_without_cloud_init_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/{server_id}/reinstallos', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ReinstallServerWithoutCloudInitResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def reset_server_password(self, request):
        """一键重置弹性云服务器密码(企业项目)

        重置弹性云服务器管理帐号（root用户或Administrator用户）的密码。

        :param ResetServerPasswordRequest request
        :return: None
        """
        return self.reset_server_password_with_http_info(request)

    def reset_server_password_with_http_info(self, request):
        """一键重置弹性云服务器密码(企业项目)

        重置弹性云服务器管理帐号（root用户或Administrator用户）的密码。

        :param ResetServerPasswordRequest request
        :return: None
        """

        all_params = ['server_id', 'reset_server_password_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/{server_id}/os-reset-password', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def resize_post_paid_server(self, request):
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
        :return: tuple(ResizePostPaidServerResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id', 'resize_post_paid_server_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/{server_id}/resize', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ResizePostPaidServerResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def resize_server(self, request):
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
        :return: tuple(ResizeServerResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id', 'resize_server_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1.1/{project_id}/cloudservers/{server_id}/resize', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ResizeServerResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def show_reset_password_flag(self, request):
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
        :return: tuple(ShowResetPasswordFlagResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/{server_id}/os-resetpwd-flag', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowResetPasswordFlagResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def show_server(self, request):
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
        :return: tuple(ShowServerResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/{server_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowServerResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def show_server_auto_recovery(self, request):
        """查询云服务器是否配置了自动恢复动作

        查询云服务器是否配置了自动恢复动作。

        :param ShowServerAutoRecoveryRequest request
        :return: ShowServerAutoRecoveryResponse
        """
        return self.show_server_auto_recovery_with_http_info(request)

    def show_server_auto_recovery_with_http_info(self, request):
        """查询云服务器是否配置了自动恢复动作

        查询云服务器是否配置了自动恢复动作。

        :param ShowServerAutoRecoveryRequest request
        :return: tuple(ShowServerAutoRecoveryResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/{server_id}/autorecovery', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowServerAutoRecoveryResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def show_server_block_device(self, request):
        """查询弹性云服务器单个磁盘信息

        查询弹性云服务器挂载的单个磁盘信息。

        :param ShowServerBlockDeviceRequest request
        :return: ShowServerBlockDeviceResponse
        """
        return self.show_server_block_device_with_http_info(request)

    def show_server_block_device_with_http_info(self, request):
        """查询弹性云服务器单个磁盘信息

        查询弹性云服务器挂载的单个磁盘信息。

        :param ShowServerBlockDeviceRequest request
        :return: tuple(ShowServerBlockDeviceResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id', 'volume_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/{server_id}/block_device/{volume_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowServerBlockDeviceResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def show_server_limits(self, request):
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
        :return: tuple(ShowServerLimitsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/limits', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowServerLimitsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def show_server_remote_console(self, request):
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
        :return: tuple(ShowServerRemoteConsoleResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id', 'show_server_remote_console_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/{server_id}/remote_console', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowServerRemoteConsoleResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def show_server_tags(self, request):
        """查询云服务器标签

        - 查询指定云服务器的标签信息。  - 标签管理服务TMS使用该接口查询指定云服务器的全部标签数据。

        :param ShowServerTagsRequest request
        :return: object
        """
        return self.show_server_tags_with_http_info(request)

    def show_server_tags_with_http_info(self, request):
        """查询云服务器标签

        - 查询指定云服务器的标签信息。  - 标签管理服务TMS使用该接口查询指定云服务器的全部标签数据。

        :param ShowServerTagsRequest request
        :return: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/{server_id}/tags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='object',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def show_windows_server_password(self, request):
        """Windows云服务器获取密码(企业项目)

        当通过支持Cloudbase-init功能的镜像创建Windows云服务器时，获取云服务器初始安装时系统生成的管理员帐户（Administrator帐户或Cloudbase-init设置的帐户）随机密码。

        :param ShowWindowsServerPasswordRequest request
        :return: ShowWindowsServerPasswordResponse
        """
        return self.show_windows_server_password_with_http_info(request)

    def show_windows_server_password_with_http_info(self, request):
        """Windows云服务器获取密码(企业项目)

        当通过支持Cloudbase-init功能的镜像创建Windows云服务器时，获取云服务器初始安装时系统生成的管理员帐户（Administrator帐户或Cloudbase-init设置的帐户）随机密码。

        :param ShowWindowsServerPasswordRequest request
        :return: tuple(ShowWindowsServerPasswordResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/{server_id}/os-server-password', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowWindowsServerPasswordResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def update_server(self, request):
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
        :return: tuple(UpdateServerResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id', 'update_server_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/{server_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateServerResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def update_server_metadata(self, request):
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
        :return: tuple(UpdateServerMetadataResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id', 'update_server_metadata_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/{server_id}/metadata', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateServerMetadataResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)


    def batch_create_server_unified_tags(self, request):
        """批量添加云服务器标签(废弃, 不推荐使用)

        为指定云服务器批量添加标签。  标签管理服务TMS使用该接口批量管理云服务器的标签。

        :param BatchCreateServerUnifiedTagsRequest request
        :return: None
        """
        return self.batch_create_server_unified_tags_with_http_info(request)

    def batch_create_server_unified_tags_with_http_info(self, request):
        """批量添加云服务器标签(废弃, 不推荐使用)

        为指定云服务器批量添加标签。  标签管理服务TMS使用该接口批量管理云服务器的标签。

        :param BatchCreateServerUnifiedTagsRequest request
        :return: None
        """

        all_params = ['server_id', 'batch_create_server_unified_tags_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/servers/{server_id}/tags/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def list_server_resize_flavors(self, request):
        """查询云服务器规格变更支持列表(废弃, 不推荐使用)

        变更规格时，部分规格的云服务器之间不能互相变更。您可以通过本接口，通过指定弹性云服务器规格，查询该规格可以变更的规格列表。

        :param ListServerResizeFlavorsRequest request
        :return: ListServerResizeFlavorsResponse
        """
        return self.list_server_resize_flavors_with_http_info(request)

    def list_server_resize_flavors_with_http_info(self, request):
        """查询云服务器规格变更支持列表(废弃, 不推荐使用)

        变更规格时，部分规格的云服务器之间不能互相变更。您可以通过本接口，通过指定弹性云服务器规格，查询该规格可以变更的规格列表。

        :param ListServerResizeFlavorsRequest request
        :return: tuple(ListServerResizeFlavorsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['instance_uuid', 'source_flavor_name', 'sort_key', 'sort_dir', 'limit', 'marker']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_uuid' in local_var_params:
            query_params.append(('instance_uuid', local_var_params['instance_uuid']))
        if 'source_flavor_name' in local_var_params:
            query_params.append(('source_flavor_name', local_var_params['source_flavor_name']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/resize_flavors', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListServerResizeFlavorsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def list_server_unified_tag(self, request):
        """查询项目标签(废弃, 不推荐使用)

        项目（Project）用于将OpenStack的资源（计算资源、存储资源和网络资源）进行分组和隔离。项目可以是一个部门或者一个项目组。一个帐户中可以创建多个项目。  该接口用于查询用户在指定项目所使用的全部标签。

        :param ListServerUnifiedTagRequest request
        :return: ListServerUnifiedTagResponse
        """
        return self.list_server_unified_tag_with_http_info(request)

    def list_server_unified_tag_with_http_info(self, request):
        """查询项目标签(废弃, 不推荐使用)

        项目（Project）用于将OpenStack的资源（计算资源、存储资源和网络资源）进行分组和隔离。项目可以是一个部门或者一个项目组。一个帐户中可以创建多个项目。  该接口用于查询用户在指定项目所使用的全部标签。

        :param ListServerUnifiedTagRequest request
        :return: tuple(ListServerUnifiedTagResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/servers/tags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListServerUnifiedTagResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def list_servers_block_devices(self, request):
        """查询弹性云服务器磁盘信息(废弃, 不推荐使用)

        查询弹性云服务器挂载的磁盘信息。

        :param ListServersBlockDevicesRequest request
        :return: ListServersBlockDevicesResponse
        """
        return self.list_servers_block_devices_with_http_info(request)

    def list_servers_block_devices_with_http_info(self, request):
        """查询弹性云服务器磁盘信息(废弃, 不推荐使用)

        查询弹性云服务器挂载的磁盘信息。

        :param ListServersBlockDevicesRequest request
        :return: tuple(ListServersBlockDevicesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/servers/{server_id}/block_device', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListServersBlockDevicesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def list_servers_by_unified_tag(self, request):
        """按标签查询云服务器列表(废弃, 不推荐使用)

        使用标签过滤弹性云服务器，并返回云服务器使用的所有标签。

        :param ListServersByUnifiedTagRequest request
        :return: ListServersByUnifiedTagResponse
        """
        return self.list_servers_by_unified_tag_with_http_info(request)

    def list_servers_by_unified_tag_with_http_info(self, request):
        """按标签查询云服务器列表(废弃, 不推荐使用)

        使用标签过滤弹性云服务器，并返回云服务器使用的所有标签。

        :param ListServersByUnifiedTagRequest request
        :return: tuple(ListServersByUnifiedTagResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['list_servers_by_unified_tag_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/servers/resource_instances/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListServersByUnifiedTagResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_list_versions(self, request):
        """查询API版本信息列表

        返回Nova当前所有可用的版本。  为了支持功能不断扩展，Nova API支持版本号区分。Nova中有两种形式的版本号：  - \"主版本号\": 具有独立的url。 - \"微版本号\": 通过Http请求头X-OpenStack-Nova-API-Version来使用，从2.27版本后更改为OpenStack-API-Version。

        :param NovaListVersionsRequest request
        :return: NovaListVersionsResponse
        """
        return self.nova_list_versions_with_http_info(request)

    def nova_list_versions_with_http_info(self, request):
        """查询API版本信息列表

        返回Nova当前所有可用的版本。  为了支持功能不断扩展，Nova API支持版本号区分。Nova中有两种形式的版本号：  - \"主版本号\": 具有独立的url。 - \"微版本号\": 通过Http请求头X-OpenStack-Nova-API-Version来使用，从2.27版本后更改为OpenStack-API-Version。

        :param NovaListVersionsRequest request
        :return: tuple(NovaListVersionsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaListVersionsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_show_version(self, request):
        """查询指定API版本信息

        返回指定版本的信息。 为了支持功能不断扩展，Nova API支持版本号区分。Nova中有两种形式的版本号：  - \"主版本号\": 具有独立的url。 - \"微版本号\": 通过Http请求头X-OpenStack-Nova-API-Version来使用，从2.27版本后更改为OpenStack-API-Version。

        :param NovaShowVersionRequest request
        :return: NovaShowVersionResponse
        """
        return self.nova_show_version_with_http_info(request)

    def nova_show_version_with_http_info(self, request):
        """查询指定API版本信息

        返回指定版本的信息。 为了支持功能不断扩展，Nova API支持版本号区分。Nova中有两种形式的版本号：  - \"主版本号\": 具有独立的url。 - \"微版本号\": 通过Http请求头X-OpenStack-Nova-API-Version来使用，从2.27版本后更改为OpenStack-API-Version。

        :param NovaShowVersionRequest request
        :return: tuple(NovaShowVersionResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['api_version']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'api_version' in local_var_params:
            path_params['api_version'] = local_var_params['api_version']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/{api_version}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaShowVersionResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def register_server_monitor(self, request):
        """注册云服务器监控

        将云服务器添加到监控表中。  注册到监控表中的云服务会被ceilometer周期性采集监控数据，包括平台的版本、cpu信息、内存、网卡、磁盘、硬件平台等信息，这些数据上报给云监控。例如SAP云服务器内部的插件会周期性从云监控中查询监控数据，以报表形式呈现给SAP。

        :param RegisterServerMonitorRequest request
        :return: None
        """
        return self.register_server_monitor_with_http_info(request)

    def register_server_monitor_with_http_info(self, request):
        """注册云服务器监控

        将云服务器添加到监控表中。  注册到监控表中的云服务会被ceilometer周期性采集监控数据，包括平台的版本、cpu信息、内存、网卡、磁盘、硬件平台等信息，这些数据上报给云监控。例如SAP云服务器内部的插件会周期性从云监控中查询监控数据，以报表形式呈现给SAP。

        :param RegisterServerMonitorRequest request
        :return: None
        """

        all_params = ['server_id', 'register_server_monitor_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1.0/servers/{server_id}/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def reset_server_os_password(self, request):
        """一键重置弹性云服务器密码

        重置弹性云服务器管理帐号（root用户或Administrator用户）的密码。

        :param ResetServerOsPasswordRequest request
        :return: None
        """
        return self.reset_server_os_password_with_http_info(request)

    def reset_server_os_password_with_http_info(self, request):
        """一键重置弹性云服务器密码

        重置弹性云服务器管理帐号（root用户或Administrator用户）的密码。

        :param ResetServerOsPasswordRequest request
        :return: None
        """

        all_params = ['server_id', 'reset_server_os_password_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/os-reset-password', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def show_server_unified_tags(self, request):
        """查询云服务器标签(废弃, 不推荐使用)

        查询指定云服务器的标签信息。  标签管理服务TMS使用该接口查询指定云服务器的全部标签数据。

        :param ShowServerUnifiedTagsRequest request
        :return: ShowServerUnifiedTagsResponse
        """
        return self.show_server_unified_tags_with_http_info(request)

    def show_server_unified_tags_with_http_info(self, request):
        """查询云服务器标签(废弃, 不推荐使用)

        查询指定云服务器的标签信息。  标签管理服务TMS使用该接口查询指定云服务器的全部标签数据。

        :param ShowServerUnifiedTagsRequest request
        :return: tuple(ShowServerUnifiedTagsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/servers/{server_id}/tags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowServerUnifiedTagsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def show_servers_block_device(self, request):
        """查询弹性云服务器单个磁盘信息(废弃, 不推荐使用)

        查询弹性云服务器挂载的单个磁盘信息。

        :param ShowServersBlockDeviceRequest request
        :return: ShowServersBlockDeviceResponse
        """
        return self.show_servers_block_device_with_http_info(request)

    def show_servers_block_device_with_http_info(self, request):
        """查询弹性云服务器单个磁盘信息(废弃, 不推荐使用)

        查询弹性云服务器挂载的单个磁盘信息。

        :param ShowServersBlockDeviceRequest request
        :return: tuple(ShowServersBlockDeviceResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['server_id', 'volume_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/servers/{server_id}/block_device/{volume_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowServersBlockDeviceResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)


    def create_fpga_image(self, request):
        """创建FPGA镜像

        本接口用于创建FPGA镜像。当前仅支持创建能够加载到Xilinx VU9P芯片的镜像文件。  在创建FPGA镜像前，用户需要提供创建FPGA镜像所需的DCP（Design Checkpoint ）文件，并将该文件存放到OBS（Object Storage Service）桶中。  本接口在完成FPGA镜像的初始化操作后会首先为用户返回FPGA镜像ID，然后通过后端的AFS（Accelerated Engine Image Factory Service）构建集群完成DCP文件到FPGA镜像文件的生成，并将构建过程中产生的日志文件上传到用户OBS桶的指定目录。构建日志文件会按照“{FPGA镜像ID} log.tar”的格式命名，例如“4010a32c5c62bad9015c62dc2290002b log.tar”。  在创建过程中，FPGA镜像的状态会不断变化。当状态为active或error时，表示创建完成。  > 状态说明   initialling：创建FPGA镜像任务初始化中；  scheduling：FPGA镜像等待调度创建；  creating：FPGA镜像正在创建中；  active：FPGA镜像可以正常使用；  error：FPGA镜像创建失败。  创建配额：单个租户一次最多只能创建一个FPGA镜像。当租户尝试同时创建多个FPGA镜像时，将创建失败。

        :param CreateFpgaImageRequest request
        :return: CreateFpgaImageResponse
        """
        return self.create_fpga_image_with_http_info(request)

    def create_fpga_image_with_http_info(self, request):
        """创建FPGA镜像

        本接口用于创建FPGA镜像。当前仅支持创建能够加载到Xilinx VU9P芯片的镜像文件。  在创建FPGA镜像前，用户需要提供创建FPGA镜像所需的DCP（Design Checkpoint ）文件，并将该文件存放到OBS（Object Storage Service）桶中。  本接口在完成FPGA镜像的初始化操作后会首先为用户返回FPGA镜像ID，然后通过后端的AFS（Accelerated Engine Image Factory Service）构建集群完成DCP文件到FPGA镜像文件的生成，并将构建过程中产生的日志文件上传到用户OBS桶的指定目录。构建日志文件会按照“{FPGA镜像ID} log.tar”的格式命名，例如“4010a32c5c62bad9015c62dc2290002b log.tar”。  在创建过程中，FPGA镜像的状态会不断变化。当状态为active或error时，表示创建完成。  > 状态说明   initialling：创建FPGA镜像任务初始化中；  scheduling：FPGA镜像等待调度创建；  creating：FPGA镜像正在创建中；  active：FPGA镜像可以正常使用；  error：FPGA镜像创建失败。  创建配额：单个租户一次最多只能创建一个FPGA镜像。当租户尝试同时创建多个FPGA镜像时，将创建失败。

        :param CreateFpgaImageRequest request
        :return: tuple(CreateFpgaImageResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['create_fpga_image_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2/{project_id}/cloudservers/fpga_image', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateFpgaImageResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def create_fpga_image_association(self, request):
        """关联FPGA镜像与弹性云服务器镜像

        本接口用于创建FPGA镜像与弹性云服务器镜像之间的关联映射关系。

        :param CreateFpgaImageAssociationRequest request
        :return: None
        """
        return self.create_fpga_image_association_with_http_info(request)

    def create_fpga_image_association_with_http_info(self, request):
        """关联FPGA镜像与弹性云服务器镜像

        本接口用于创建FPGA镜像与弹性云服务器镜像之间的关联映射关系。

        :param CreateFpgaImageAssociationRequest request
        :return: None
        """

        all_params = ['fpga_image_id', 'create_fpga_image_association_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'fpga_image_id' in local_var_params:
            path_params['fpga_image_id'] = local_var_params['fpga_image_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/fpga_image/{fpga_image_id}/association', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def delete_fpga_image(self, request):
        """删除FPGA镜像

        本接口用于删除FPGA镜像。

        :param DeleteFpgaImageRequest request
        :return: None
        """
        return self.delete_fpga_image_with_http_info(request)

    def delete_fpga_image_with_http_info(self, request):
        """删除FPGA镜像

        本接口用于删除FPGA镜像。

        :param DeleteFpgaImageRequest request
        :return: None
        """

        all_params = ['fpga_image_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'fpga_image_id' in local_var_params:
            path_params['fpga_image_id'] = local_var_params['fpga_image_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/fpga_image/{fpga_image_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def delete_fpga_image_association(self, request):
        """解关联FPGA镜像与弹性云服务器镜像

        本接口用于删除FPGA镜像与弹性云服务器镜像之间的关联映射关系。

        :param DeleteFpgaImageAssociationRequest request
        :return: None
        """
        return self.delete_fpga_image_association_with_http_info(request)

    def delete_fpga_image_association_with_http_info(self, request):
        """解关联FPGA镜像与弹性云服务器镜像

        本接口用于删除FPGA镜像与弹性云服务器镜像之间的关联映射关系。

        :param DeleteFpgaImageAssociationRequest request
        :return: None
        """

        all_params = ['fpga_image_id', 'delete_fpga_image_association_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'fpga_image_id' in local_var_params:
            path_params['fpga_image_id'] = local_var_params['fpga_image_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/fpga_image/{fpga_image_id}/association', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def list_fpga_image_associations(self, request):
        """查询关联列表

        本接口用于查询租户可见的FPGA镜像与弹性云服务器镜像之间的关联映射关系列表。

        :param ListFpgaImageAssociationsRequest request
        :return: ListFpgaImageAssociationsResponse
        """
        return self.list_fpga_image_associations_with_http_info(request)

    def list_fpga_image_associations_with_http_info(self, request):
        """查询关联列表

        本接口用于查询租户可见的FPGA镜像与弹性云服务器镜像之间的关联映射关系列表。

        :param ListFpgaImageAssociationsRequest request
        :return: tuple(ListFpgaImageAssociationsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['fpga_image_id', 'image_id', 'page']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fpga_image_id' in local_var_params:
            query_params.append(('fpga_image_id', local_var_params['fpga_image_id']))
        if 'image_id' in local_var_params:
            query_params.append(('image_id', local_var_params['image_id']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/fpga_image/associations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListFpgaImageAssociationsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def list_fpga_images(self, request):
        """查询FPGA镜像详情列表

        本接口用于查询租户拥有的FPGA镜像详情列表。

        :param ListFpgaImagesRequest request
        :return: ListFpgaImagesResponse
        """
        return self.list_fpga_images_with_http_info(request)

    def list_fpga_images_with_http_info(self, request):
        """查询FPGA镜像详情列表

        本接口用于查询租户拥有的FPGA镜像详情列表。

        :param ListFpgaImagesRequest request
        :return: tuple(ListFpgaImagesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['page', 'size']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/fpga_image/detail', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListFpgaImagesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def register_fpga_image(self, request):
        """注册FPGA镜像

        本接口用于注册FPGA镜像。  FPGA镜像是指用户开发的FPGA逻辑文件，通常也称为AEI（Accelerated Engine Image）。在注册FPGA镜像时，该逻辑文件需要存放在用户的OBS（Object Storage Service）桶中。

        :param RegisterFpgaImageRequest request
        :return: RegisterFpgaImageResponse
        """
        return self.register_fpga_image_with_http_info(request)

    def register_fpga_image_with_http_info(self, request):
        """注册FPGA镜像

        本接口用于注册FPGA镜像。  FPGA镜像是指用户开发的FPGA逻辑文件，通常也称为AEI（Accelerated Engine Image）。在注册FPGA镜像时，该逻辑文件需要存放在用户的OBS（Object Storage Service）桶中。

        :param RegisterFpgaImageRequest request
        :return: tuple(RegisterFpgaImageResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['register_fpga_image_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/cloudservers/fpga_image', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='RegisterFpgaImageResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)


    def nova_add_floating_ip(self, request):
        """分配浮动IP(废弃, 不推荐使用)

        将浮动IP绑定到一台弹性云服务器上。

        :param NovaAddFloatingIpRequest request
        :return: None
        """
        return self.nova_add_floating_ip_with_http_info(request)

    def nova_add_floating_ip_with_http_info(self, request):
        """分配浮动IP(废弃, 不推荐使用)

        将浮动IP绑定到一台弹性云服务器上。

        :param NovaAddFloatingIpRequest request
        :return: None
        """

        all_params = ['server_id', 'nova_add_floating_ip_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_create_floating_ip(self, request):
        """创建浮动IP（废弃, 不推荐使用）

        创建浮动IP。

        :param NovaCreateFloatingIpRequest request
        :return: NovaCreateFloatingIpResponse
        """
        return self.nova_create_floating_ip_with_http_info(request)

    def nova_create_floating_ip_with_http_info(self, request):
        """创建浮动IP（废弃, 不推荐使用）

        创建浮动IP。

        :param NovaCreateFloatingIpRequest request
        :return: tuple(NovaCreateFloatingIpResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['nova_create_floating_ip_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-floating-ips', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaCreateFloatingIpResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_delete_floating_ip(self, request):
        """删除浮动IP（废弃, 不推荐使用）

        删除浮动IP地址。

        :param NovaDeleteFloatingIpRequest request
        :return: None
        """
        return self.nova_delete_floating_ip_with_http_info(request)

    def nova_delete_floating_ip_with_http_info(self, request):
        """删除浮动IP（废弃, 不推荐使用）

        删除浮动IP地址。

        :param NovaDeleteFloatingIpRequest request
        :return: None
        """

        all_params = ['floating_ip_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'floating_ip_id' in local_var_params:
            path_params['floating_ip_id'] = local_var_params['floating_ip_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-floating-ips/{floating_ip_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_list_floating_i_ps(self, request):
        """查询浮动IP列表（废弃, 不推荐使用）

        查询浮动IP列表。

        :param NovaListFloatingIPsRequest request
        :return: NovaListFloatingIPsResponse
        """
        return self.nova_list_floating_i_ps_with_http_info(request)

    def nova_list_floating_i_ps_with_http_info(self, request):
        """查询浮动IP列表（废弃, 不推荐使用）

        查询浮动IP列表。

        :param NovaListFloatingIPsRequest request
        :return: tuple(NovaListFloatingIPsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-floating-ips', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaListFloatingIPsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_list_floating_ip_pools(self, request):
        """查询浮动IP资源池列表（废弃, 不推荐使用）

        查询浮动IP资源池列表。

        :param NovaListFloatingIpPoolsRequest request
        :return: NovaListFloatingIpPoolsResponse
        """
        return self.nova_list_floating_ip_pools_with_http_info(request)

    def nova_list_floating_ip_pools_with_http_info(self, request):
        """查询浮动IP资源池列表（废弃, 不推荐使用）

        查询浮动IP资源池列表。

        :param NovaListFloatingIpPoolsRequest request
        :return: tuple(NovaListFloatingIpPoolsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-floating-ip-pools', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaListFloatingIpPoolsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_remove_floating_ip(self, request):
        """移除浮动IP（废弃, 不推荐使用）

        从云服务器上解绑浮动IP。

        :param NovaRemoveFloatingIpRequest request
        :return: None
        """
        return self.nova_remove_floating_ip_with_http_info(request)

    def nova_remove_floating_ip_with_http_info(self, request):
        """移除浮动IP（废弃, 不推荐使用）

        从云服务器上解绑浮动IP。

        :param NovaRemoveFloatingIpRequest request
        :return: None
        """

        all_params = ['server_id', 'nova_remove_floating_ip_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/servers/{server_id}/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def nova_show_floating_ip(self, request):
        """查询浮动IP（废弃, 不推荐使用）

        根据浮动IP的ID查询浮动IP详情。

        :param NovaShowFloatingIpRequest request
        :return: NovaShowFloatingIpResponse
        """
        return self.nova_show_floating_ip_with_http_info(request)

    def nova_show_floating_ip_with_http_info(self, request):
        """查询浮动IP（废弃, 不推荐使用）

        根据浮动IP的ID查询浮动IP详情。

        :param NovaShowFloatingIpRequest request
        :return: tuple(NovaShowFloatingIpResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['floating_ip_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'floating_ip_id' in local_var_params:
            path_params['floating_ip_id'] = local_var_params['floating_ip_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.1/{project_id}/os-floating-ips/{floating_ip_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NovaShowFloatingIpResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)


    def show_job(self, request):
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
        :return: tuple(ShowJobResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['job_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/jobs/{job_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowJobResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)


    def call_api(self, resource_path, method,
                 path_params=None, query_params=None, header_params=None,
                 body=None, post_params=None,
                 response_type=None, auth_settings=None,  collection_formats=None):
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
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :return:
            Return the response directly.
        """
        return self.do_http_request(method, resource_path, path_params,
                                    query_params, header_params, body, post_params,
                                    response_type, collection_formats)
