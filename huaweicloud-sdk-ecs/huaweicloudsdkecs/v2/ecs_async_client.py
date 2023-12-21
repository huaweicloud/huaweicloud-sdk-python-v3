# coding: utf-8

from __future__ import absolute_import

import importlib
import warnings

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest
try:
    from huaweicloudsdkcore.invoker.invoker import AsyncInvoker
except ImportError as e:
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkecs'")


class EcsAsyncClient(Client):
    def __init__(self):
        super(EcsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkecs.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "EcsAsyncClient":
                raise TypeError("client type error, support client type is EcsAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_server_group_member_async(self, request):
        """添加云服务器组成员

        将云服务器加入云服务器组。添加成功后，如果该云服务器组是反亲和性策略的，则该云服务器与云服务器组中的其他成员尽量分散地创建在不同主机上。如果该云服务器时故障域类型的，则该云服务器会拥有故障域属性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddServerGroupMember
        :type request: :class:`huaweicloudsdkecs.v2.AddServerGroupMemberRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.AddServerGroupMemberResponse`
        """
        http_info = self._add_server_group_member_http_info(request)
        return self._call_api(**http_info)

    def add_server_group_member_async_invoker(self, request):
        http_info = self._add_server_group_member_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_server_group_member_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloudservers/os-server-groups/{server_group_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "AddServerGroupMemberResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_group_id' in local_var_params:
            path_params['server_group_id'] = local_var_params['server_group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

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
        http_info = self._associate_server_virtual_ip_http_info(request)
        return self._call_api(**http_info)

    def associate_server_virtual_ip_async_invoker(self, request):
        http_info = self._associate_server_virtual_ip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_server_virtual_ip_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/cloudservers/nics/{nic_id}",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateServerVirtualIpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'nic_id' in local_var_params:
            path_params['nic_id'] = local_var_params['nic_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def attach_server_volume_async(self, request):
        """弹性云服务器挂载磁盘

        把磁盘挂载到弹性云服务器上。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AttachServerVolume
        :type request: :class:`huaweicloudsdkecs.v2.AttachServerVolumeRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.AttachServerVolumeResponse`
        """
        http_info = self._attach_server_volume_http_info(request)
        return self._call_api(**http_info)

    def attach_server_volume_async_invoker(self, request):
        http_info = self._attach_server_volume_http_info(request)
        return AsyncInvoker(self, http_info)

    def _attach_server_volume_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloudservers/{server_id}/attachvolume",
            "request_type": request.__class__.__name__,
            "response_type": "AttachServerVolumeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_add_server_nics_async(self, request):
        """批量添加云服务器网卡

        给云服务器添加一张或多张网卡。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAddServerNics
        :type request: :class:`huaweicloudsdkecs.v2.BatchAddServerNicsRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.BatchAddServerNicsResponse`
        """
        http_info = self._batch_add_server_nics_http_info(request)
        return self._call_api(**http_info)

    def batch_add_server_nics_async_invoker(self, request):
        http_info = self._batch_add_server_nics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_add_server_nics_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloudservers/{server_id}/nics",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAddServerNicsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_attach_sharable_volumes_async(self, request):
        """批量挂载指定共享盘

        将指定的共享磁盘一次性挂载到多个弹性云服务器，实现批量挂载。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAttachSharableVolumes
        :type request: :class:`huaweicloudsdkecs.v2.BatchAttachSharableVolumesRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.BatchAttachSharableVolumesResponse`
        """
        http_info = self._batch_attach_sharable_volumes_http_info(request)
        return self._call_api(**http_info)

    def batch_attach_sharable_volumes_async_invoker(self, request):
        http_info = self._batch_attach_sharable_volumes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_attach_sharable_volumes_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/batchaction/attachvolumes/{volume_id}",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAttachSharableVolumesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_create_server_tags_async(self, request):
        """批量添加云服务器标签

        - 为指定云服务器批量添加标签。
        
        - 标签管理服务TMS使用该接口批量管理云服务器的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateServerTags
        :type request: :class:`huaweicloudsdkecs.v2.BatchCreateServerTagsRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.BatchCreateServerTagsResponse`
        """
        http_info = self._batch_create_server_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_server_tags_async_invoker(self, request):
        http_info = self._batch_create_server_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_server_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloudservers/{server_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateServerTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_server_nics_async(self, request):
        """批量删除云服务器网卡

        卸载并删除云服务器中的一张或多张网卡。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteServerNics
        :type request: :class:`huaweicloudsdkecs.v2.BatchDeleteServerNicsRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.BatchDeleteServerNicsResponse`
        """
        http_info = self._batch_delete_server_nics_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_server_nics_async_invoker(self, request):
        http_info = self._batch_delete_server_nics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_server_nics_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloudservers/{server_id}/nics/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteServerNicsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_server_tags_async(self, request):
        """批量删除云服务器标签

        - 为指定云服务器批量删除标签。
        
        - 标签管理服务TMS使用该接口批量管理云服务器的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteServerTags
        :type request: :class:`huaweicloudsdkecs.v2.BatchDeleteServerTagsRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.BatchDeleteServerTagsResponse`
        """
        http_info = self._batch_delete_server_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_server_tags_async_invoker(self, request):
        http_info = self._batch_delete_server_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_server_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloudservers/{server_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteServerTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_reboot_servers_async(self, request):
        """批量重启云服务器

        根据给定的云服务器ID列表，批量重启云服务器，一次最多可以重启1000台。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchRebootServers
        :type request: :class:`huaweicloudsdkecs.v2.BatchRebootServersRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.BatchRebootServersResponse`
        """
        http_info = self._batch_reboot_servers_http_info(request)
        return self._call_api(**http_info)

    def batch_reboot_servers_async_invoker(self, request):
        http_info = self._batch_reboot_servers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_reboot_servers_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloudservers/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchRebootServersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_reset_servers_password_async(self, request):
        """批量重置弹性云服务器密码

        批量重置弹性云服务器管理帐号（root用户或Administrator用户）的密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchResetServersPassword
        :type request: :class:`huaweicloudsdkecs.v2.BatchResetServersPasswordRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.BatchResetServersPasswordResponse`
        """
        http_info = self._batch_reset_servers_password_http_info(request)
        return self._call_api(**http_info)

    def batch_reset_servers_password_async_invoker(self, request):
        http_info = self._batch_reset_servers_password_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_reset_servers_password_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/cloudservers/os-reset-passwords",
            "request_type": request.__class__.__name__,
            "response_type": "BatchResetServersPasswordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_start_servers_async(self, request):
        """批量启动云服务器

        根据给定的云服务器ID列表，批量启动云服务器，一次最多可以启动1000台。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchStartServers
        :type request: :class:`huaweicloudsdkecs.v2.BatchStartServersRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.BatchStartServersResponse`
        """
        http_info = self._batch_start_servers_http_info(request)
        return self._call_api(**http_info)

    def batch_start_servers_async_invoker(self, request):
        http_info = self._batch_start_servers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_start_servers_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloudservers/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchStartServersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_stop_servers_async(self, request):
        """批量关闭云服务器

        根据给定的云服务器ID列表，批量关闭云服务器，一次最多可以关闭1000台。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchStopServers
        :type request: :class:`huaweicloudsdkecs.v2.BatchStopServersRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.BatchStopServersResponse`
        """
        http_info = self._batch_stop_servers_http_info(request)
        return self._call_api(**http_info)

    def batch_stop_servers_async_invoker(self, request):
        http_info = self._batch_stop_servers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_stop_servers_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloudservers/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchStopServersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_update_servers_name_async(self, request):
        """批量修改弹性云服务器

        批量修改弹性云服务器信息。
        当前仅支持批量修改云服务器名称，一次最多可以修改1000台。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchUpdateServersName
        :type request: :class:`huaweicloudsdkecs.v2.BatchUpdateServersNameRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.BatchUpdateServersNameResponse`
        """
        http_info = self._batch_update_servers_name_http_info(request)
        return self._call_api(**http_info)

    def batch_update_servers_name_async_invoker(self, request):
        http_info = self._batch_update_servers_name_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_update_servers_name_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/cloudservers/server-name",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateServersNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def change_server_charge_mode_async(self, request):
        """更换云服务器计费模式

        更换云服务器的计费模式
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeServerChargeMode
        :type request: :class:`huaweicloudsdkecs.v2.ChangeServerChargeModeRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ChangeServerChargeModeResponse`
        """
        http_info = self._change_server_charge_mode_http_info(request)
        return self._call_api(**http_info)

    def change_server_charge_mode_async_invoker(self, request):
        http_info = self._change_server_charge_mode_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_server_charge_mode_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloudservers/actions/change-charge-mode",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeServerChargeModeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def change_server_os_with_cloud_init_async(self, request):
        """切换弹性云服务器操作系统(安装Cloud init)

        切换弹性云服务器操作系统。支持弹性云服务器数据盘不变的情况下，使用新镜像重装系统盘。
        
        调用该接口后，系统将卸载系统盘，然后使用新镜像重新创建系统盘，并挂载至弹性云服务器，实现切换操作系统功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeServerOsWithCloudInit
        :type request: :class:`huaweicloudsdkecs.v2.ChangeServerOsWithCloudInitRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ChangeServerOsWithCloudInitResponse`
        """
        http_info = self._change_server_os_with_cloud_init_http_info(request)
        return self._call_api(**http_info)

    def change_server_os_with_cloud_init_async_invoker(self, request):
        http_info = self._change_server_os_with_cloud_init_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_server_os_with_cloud_init_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cloudservers/{server_id}/changeos",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeServerOsWithCloudInitResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def change_server_os_without_cloud_init_async(self, request):
        """切换弹性云服务器操作系统(未安装Cloud init)

        切换弹性云服务器操作系统。
        
        该接口支持未安装Cloud-init或Cloudbase-init的镜像使用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeServerOsWithoutCloudInit
        :type request: :class:`huaweicloudsdkecs.v2.ChangeServerOsWithoutCloudInitRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ChangeServerOsWithoutCloudInitResponse`
        """
        http_info = self._change_server_os_without_cloud_init_http_info(request)
        return self._call_api(**http_info)

    def change_server_os_without_cloud_init_async_invoker(self, request):
        http_info = self._change_server_os_without_cloud_init_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_server_os_without_cloud_init_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloudservers/{server_id}/changeos",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeServerOsWithoutCloudInitResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

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
        http_info = self._create_post_paid_servers_http_info(request)
        return self._call_api(**http_info)

    def create_post_paid_servers_async_invoker(self, request):
        http_info = self._create_post_paid_servers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_post_paid_servers_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloudservers",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePostPaidServersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_client_token' in local_var_params:
            header_params['X-Client-Token'] = local_var_params['x_client_token']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_server_group_async(self, request):
        """创建云服务器组

        创建弹性云服务器组。
        
        与原生的创建云服务器组接口不同之处在于该接口支持企业项目细粒度权限的校验。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateServerGroup
        :type request: :class:`huaweicloudsdkecs.v2.CreateServerGroupRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.CreateServerGroupResponse`
        """
        http_info = self._create_server_group_http_info(request)
        return self._call_api(**http_info)

    def create_server_group_async_invoker(self, request):
        http_info = self._create_server_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_server_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloudservers/os-server-groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateServerGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

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
        http_info = self._create_servers_http_info(request)
        return self._call_api(**http_info)

    def create_servers_async_invoker(self, request):
        http_info = self._create_servers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_servers_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.1/{project_id}/cloudservers",
            "request_type": request.__class__.__name__,
            "response_type": "CreateServersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_client_token' in local_var_params:
            header_params['X-Client-Token'] = local_var_params['x_client_token']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_server_group_async(self, request):
        """删除云服务器组

        删除云服务器组。
        
        与原生的删除云服务器组接口不同之处在于该接口支持企业项目细粒度权限的校验。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteServerGroup
        :type request: :class:`huaweicloudsdkecs.v2.DeleteServerGroupRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.DeleteServerGroupResponse`
        """
        http_info = self._delete_server_group_http_info(request)
        return self._call_api(**http_info)

    def delete_server_group_async_invoker(self, request):
        http_info = self._delete_server_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_server_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/cloudservers/os-server-groups/{server_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteServerGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_group_id' in local_var_params:
            path_params['server_group_id'] = local_var_params['server_group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_server_group_member_async(self, request):
        """删除云服务器组成员

        将弹性云服务器移出云服务器组。移出后，该云服务器与云服务器组中的成员不再遵从反亲和策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteServerGroupMember
        :type request: :class:`huaweicloudsdkecs.v2.DeleteServerGroupMemberRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.DeleteServerGroupMemberResponse`
        """
        http_info = self._delete_server_group_member_http_info(request)
        return self._call_api(**http_info)

    def delete_server_group_member_async_invoker(self, request):
        http_info = self._delete_server_group_member_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_server_group_member_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloudservers/os-server-groups/{server_group_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteServerGroupMemberResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_group_id' in local_var_params:
            path_params['server_group_id'] = local_var_params['server_group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_server_metadata_async(self, request):
        """删除云服务器指定元数据

        删除云服务器指定元数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteServerMetadata
        :type request: :class:`huaweicloudsdkecs.v2.DeleteServerMetadataRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.DeleteServerMetadataResponse`
        """
        http_info = self._delete_server_metadata_http_info(request)
        return self._call_api(**http_info)

    def delete_server_metadata_async_invoker(self, request):
        http_info = self._delete_server_metadata_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_server_metadata_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/cloudservers/{server_id}/metadata/{key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteServerMetadataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_server_password_async(self, request):
        """云服务器清除密码(企业项目)

        清除Windows云服务器初始安装时系统生成的密码记录。清除密码后，不影响云服务器密码登录功能，但不能再使用获取密码功能来查询该云服务器密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteServerPassword
        :type request: :class:`huaweicloudsdkecs.v2.DeleteServerPasswordRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.DeleteServerPasswordResponse`
        """
        http_info = self._delete_server_password_http_info(request)
        return self._call_api(**http_info)

    def delete_server_password_async_invoker(self, request):
        http_info = self._delete_server_password_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_server_password_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/cloudservers/{server_id}/os-server-password",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteServerPasswordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_servers_async(self, request):
        """删除云服务器

        根据指定的云服务器ID列表，删除云服务器。
        
        系统支持删除单台云服务器和批量删除多台云服务器操作，批量删除云服务器时，一次最多可以删除1000台。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteServers
        :type request: :class:`huaweicloudsdkecs.v2.DeleteServersRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.DeleteServersResponse`
        """
        http_info = self._delete_servers_http_info(request)
        return self._call_api(**http_info)

    def delete_servers_async_invoker(self, request):
        http_info = self._delete_servers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_servers_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloudservers/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteServersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def detach_server_volume_async(self, request):
        """弹性云服务器卸载磁盘

        从弹性云服务器中卸载磁盘。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetachServerVolume
        :type request: :class:`huaweicloudsdkecs.v2.DetachServerVolumeRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.DetachServerVolumeResponse`
        """
        http_info = self._detach_server_volume_http_info(request)
        return self._call_api(**http_info)

    def detach_server_volume_async_invoker(self, request):
        http_info = self._detach_server_volume_http_info(request)
        return AsyncInvoker(self, http_info)

    def _detach_server_volume_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/cloudservers/{server_id}/detachvolume/{volume_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DetachServerVolumeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def disassociate_server_virtual_ip_async(self, request):
        """云服务器网卡解绑虚拟IP地址

        虚拟IP地址用于为网卡提供第二个IP地址，同时支持与多个弹性云服务器的网卡绑定，从而实现多个弹性云服务器之间的高可用性。
        
        该接口用于解绑定弹性云服务器网卡的虚拟IP地址。解绑后，网卡不会被删除。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateServerVirtualIp
        :type request: :class:`huaweicloudsdkecs.v2.DisassociateServerVirtualIpRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.DisassociateServerVirtualIpResponse`
        """
        http_info = self._disassociate_server_virtual_ip_http_info(request)
        return self._call_api(**http_info)

    def disassociate_server_virtual_ip_async_invoker(self, request):
        http_info = self._disassociate_server_virtual_ip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disassociate_server_virtual_ip_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/cloudservers/nics/{nic_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateServerVirtualIpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'nic_id' in local_var_params:
            path_params['nic_id'] = local_var_params['nic_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_flavor_sell_policies_async(self, request):
        """查询规格销售策略

        查询规格销售策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFlavorSellPolicies
        :type request: :class:`huaweicloudsdkecs.v2.ListFlavorSellPoliciesRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ListFlavorSellPoliciesResponse`
        """
        http_info = self._list_flavor_sell_policies_http_info(request)
        return self._call_api(**http_info)

    def list_flavor_sell_policies_async_invoker(self, request):
        http_info = self._list_flavor_sell_policies_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_flavor_sell_policies_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloudservers/flavor-sell-policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListFlavorSellPoliciesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'flavor_id' in local_var_params:
            query_params.append(('flavor_id', local_var_params['flavor_id']))
        if 'sell_status' in local_var_params:
            query_params.append(('sell_status', local_var_params['sell_status']))
        if 'sell_mode' in local_var_params:
            query_params.append(('sell_mode', local_var_params['sell_mode']))
        if 'availability_zone_id' in local_var_params:
            query_params.append(('availability_zone_id', local_var_params['availability_zone_id']))
        if 'longest_spot_duration_hours_gt' in local_var_params:
            query_params.append(('longest_spot_duration_hours_gt', local_var_params['longest_spot_duration_hours_gt']))
        if 'largest_spot_duration_count_gt' in local_var_params:
            query_params.append(('largest_spot_duration_count_gt', local_var_params['largest_spot_duration_count_gt']))
        if 'longest_spot_duration_hours' in local_var_params:
            query_params.append(('longest_spot_duration_hours', local_var_params['longest_spot_duration_hours']))
        if 'largest_spot_duration_count' in local_var_params:
            query_params.append(('largest_spot_duration_count', local_var_params['largest_spot_duration_count']))
        if 'interruption_policy' in local_var_params:
            query_params.append(('interruption_policy', local_var_params['interruption_policy']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_flavors_async(self, request):
        """查询规格详情和规格扩展信息列表

        查询云服务器规格详情信息和规格扩展信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFlavors
        :type request: :class:`huaweicloudsdkecs.v2.ListFlavorsRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ListFlavorsResponse`
        """
        http_info = self._list_flavors_http_info(request)
        return self._call_api(**http_info)

    def list_flavors_async_invoker(self, request):
        http_info = self._list_flavors_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_flavors_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloudservers/flavors",
            "request_type": request.__class__.__name__,
            "response_type": "ListFlavorsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'availability_zone' in local_var_params:
            query_params.append(('availability_zone', local_var_params['availability_zone']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_resize_flavors_async(self, request):
        """查询云服务器规格变更支持列表

        变更规格时，部分规格的云服务器之间不能互相变更。您可以通过本接口，通过指定弹性云服务器规格，查询该规格可以变更的规格列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResizeFlavors
        :type request: :class:`huaweicloudsdkecs.v2.ListResizeFlavorsRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ListResizeFlavorsResponse`
        """
        http_info = self._list_resize_flavors_http_info(request)
        return self._call_api(**http_info)

    def list_resize_flavors_async_invoker(self, request):
        http_info = self._list_resize_flavors_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_resize_flavors_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloudservers/resize_flavors",
            "request_type": request.__class__.__name__,
            "response_type": "ListResizeFlavorsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_server_block_devices_async(self, request):
        """查询弹性云服务器挂载磁盘列表详情信息

        查询弹性云服务器挂载的磁盘信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServerBlockDevices
        :type request: :class:`huaweicloudsdkecs.v2.ListServerBlockDevicesRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ListServerBlockDevicesResponse`
        """
        http_info = self._list_server_block_devices_http_info(request)
        return self._call_api(**http_info)

    def list_server_block_devices_async_invoker(self, request):
        http_info = self._list_server_block_devices_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_server_block_devices_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloudservers/{server_id}/block_device",
            "request_type": request.__class__.__name__,
            "response_type": "ListServerBlockDevicesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_server_groups_async(self, request):
        """查询云服务器组列表

        查询弹性云服务器组。
        
        与原生的创建云服务器组接口不同之处在于该接口支持企业项目细粒度权限的校验。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServerGroups
        :type request: :class:`huaweicloudsdkecs.v2.ListServerGroupsRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ListServerGroupsResponse`
        """
        http_info = self._list_server_groups_http_info(request)
        return self._call_api(**http_info)

    def list_server_groups_async_invoker(self, request):
        http_info = self._list_server_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_server_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloudservers/os-server-groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListServerGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_server_interfaces_async(self, request):
        """查询云服务器网卡信息

        查询云服务器网卡信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServerInterfaces
        :type request: :class:`huaweicloudsdkecs.v2.ListServerInterfacesRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ListServerInterfacesResponse`
        """
        http_info = self._list_server_interfaces_http_info(request)
        return self._call_api(**http_info)

    def list_server_interfaces_async_invoker(self, request):
        http_info = self._list_server_interfaces_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_server_interfaces_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloudservers/{server_id}/os-interface",
            "request_type": request.__class__.__name__,
            "response_type": "ListServerInterfacesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_server_tags_async(self, request):
        """查询项目标签

        项目（Project）用于将OpenStack的资源（计算资源、存储资源和网络资源）进行分组和隔离。项目可以是一个部门或者一个项目组。一个帐户中可以创建多个项目。
        
        该接口用于查询用户在指定项目所使用的全部标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServerTags
        :type request: :class:`huaweicloudsdkecs.v2.ListServerTagsRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ListServerTagsResponse`
        """
        http_info = self._list_server_tags_http_info(request)
        return self._call_api(**http_info)

    def list_server_tags_async_invoker(self, request):
        http_info = self._list_server_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_server_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloudservers/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListServerTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_servers_by_tag_async(self, request):
        """按标签查询云服务器列表

        使用标签过滤弹性云服务器，并返回云服务器使用的所有标签和资源列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServersByTag
        :type request: :class:`huaweicloudsdkecs.v2.ListServersByTagRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ListServersByTagResponse`
        """
        warnings.warn("Method 'list_servers_by_tag_async' of EcsAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_servers_by_tag_http_info(request)
        return self._call_api(**http_info)

    def list_servers_by_tag_async_invoker(self, request):
        warnings.warn("Method 'list_servers_by_tag_async_invoker' of EcsAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_servers_by_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_servers_by_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloudservers/resource_instances/action",
            "request_type": request.__class__.__name__,
            "response_type": "ListServersByTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_servers_details_async(self, request):
        """查询云服务器详情列表

        根据用户请求条件从数据库筛选、查询所有的弹性云服务器，并关联相关表获取到弹性云服务器的详细信息。
        
        该接口支持查询弹性云服务器计费方式，以及是否被冻结。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServersDetails
        :type request: :class:`huaweicloudsdkecs.v2.ListServersDetailsRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ListServersDetailsResponse`
        """
        http_info = self._list_servers_details_http_info(request)
        return self._call_api(**http_info)

    def list_servers_details_async_invoker(self, request):
        http_info = self._list_servers_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_servers_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloudservers/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ListServersDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

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
        http_info = self._migrate_server_http_info(request)
        return self._call_api(**http_info)

    def migrate_server_async_invoker(self, request):
        http_info = self._migrate_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _migrate_server_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloudservers/{server_id}/migrate",
            "request_type": request.__class__.__name__,
            "response_type": "MigrateServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def nova_associate_security_group_async(self, request):
        """添加安全组

        为弹性云服务器添加一个安全组。
        
        添加多个安全组时，建议最多为弹性云服务器添加5个安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NovaAssociateSecurityGroup
        :type request: :class:`huaweicloudsdkecs.v2.NovaAssociateSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.NovaAssociateSecurityGroupResponse`
        """
        http_info = self._nova_associate_security_group_http_info(request)
        return self._call_api(**http_info)

    def nova_associate_security_group_async_invoker(self, request):
        http_info = self._nova_associate_security_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _nova_associate_security_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.1/{project_id}/servers/{server_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "NovaAssociateSecurityGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def nova_attach_interface_async(self, request):
        """添加云服务器网卡

        给云服务器添加一张网卡。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NovaAttachInterface
        :type request: :class:`huaweicloudsdkecs.v2.NovaAttachInterfaceRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.NovaAttachInterfaceResponse`
        """
        http_info = self._nova_attach_interface_http_info(request)
        return self._call_api(**http_info)

    def nova_attach_interface_async_invoker(self, request):
        http_info = self._nova_attach_interface_http_info(request)
        return AsyncInvoker(self, http_info)

    def _nova_attach_interface_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.1/{project_id}/servers/{server_id}/os-interface",
            "request_type": request.__class__.__name__,
            "response_type": "NovaAttachInterfaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def nova_create_keypair_async(self, request):
        """创建和导入SSH密钥

        创建SSH密钥，或把公钥导入系统，生成密钥对。
        
        创建SSH密钥成功后，请把响应数据中的私钥内容保存到本地文件，用户使用该私钥登录云服务器云主机。为保证云服务器云主机器安全，私钥数据只能读取一次，请妥善保管。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NovaCreateKeypair
        :type request: :class:`huaweicloudsdkecs.v2.NovaCreateKeypairRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.NovaCreateKeypairResponse`
        """
        http_info = self._nova_create_keypair_http_info(request)
        return self._call_api(**http_info)

    def nova_create_keypair_async_invoker(self, request):
        http_info = self._nova_create_keypair_http_info(request)
        return AsyncInvoker(self, http_info)

    def _nova_create_keypair_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.1/{project_id}/os-keypairs",
            "request_type": request.__class__.__name__,
            "response_type": "NovaCreateKeypairResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'open_stack_api_version' in local_var_params:
            header_params['OpenStack-API-Version'] = local_var_params['open_stack_api_version']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

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
        http_info = self._nova_create_servers_http_info(request)
        return self._call_api(**http_info)

    def nova_create_servers_async_invoker(self, request):
        http_info = self._nova_create_servers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _nova_create_servers_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.1/{project_id}/servers",
            "request_type": request.__class__.__name__,
            "response_type": "NovaCreateServersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'open_stack_api_version' in local_var_params:
            header_params['OpenStack-API-Version'] = local_var_params['open_stack_api_version']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def nova_delete_keypair_async(self, request):
        """删除SSH密钥

        根据SSH密钥的名称，删除指定SSH密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NovaDeleteKeypair
        :type request: :class:`huaweicloudsdkecs.v2.NovaDeleteKeypairRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.NovaDeleteKeypairResponse`
        """
        http_info = self._nova_delete_keypair_http_info(request)
        return self._call_api(**http_info)

    def nova_delete_keypair_async_invoker(self, request):
        http_info = self._nova_delete_keypair_http_info(request)
        return AsyncInvoker(self, http_info)

    def _nova_delete_keypair_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.1/{project_id}/os-keypairs/{keypair_name}",
            "request_type": request.__class__.__name__,
            "response_type": "NovaDeleteKeypairResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'keypair_name' in local_var_params:
            path_params['keypair_name'] = local_var_params['keypair_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def nova_delete_server_async(self, request):
        """删除云服务器

        删除一台云服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NovaDeleteServer
        :type request: :class:`huaweicloudsdkecs.v2.NovaDeleteServerRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.NovaDeleteServerResponse`
        """
        http_info = self._nova_delete_server_http_info(request)
        return self._call_api(**http_info)

    def nova_delete_server_async_invoker(self, request):
        http_info = self._nova_delete_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _nova_delete_server_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.1/{project_id}/servers/{server_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NovaDeleteServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def nova_disassociate_security_group_async(self, request):
        """移除安全组

        移除弹性云服务器中的安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NovaDisassociateSecurityGroup
        :type request: :class:`huaweicloudsdkecs.v2.NovaDisassociateSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.NovaDisassociateSecurityGroupResponse`
        """
        http_info = self._nova_disassociate_security_group_http_info(request)
        return self._call_api(**http_info)

    def nova_disassociate_security_group_async_invoker(self, request):
        http_info = self._nova_disassociate_security_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _nova_disassociate_security_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.1/{project_id}/servers/{server_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "NovaDisassociateSecurityGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def nova_list_availability_zones_async(self, request):
        """查询可用区列表

        查询可用域列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NovaListAvailabilityZones
        :type request: :class:`huaweicloudsdkecs.v2.NovaListAvailabilityZonesRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.NovaListAvailabilityZonesResponse`
        """
        http_info = self._nova_list_availability_zones_http_info(request)
        return self._call_api(**http_info)

    def nova_list_availability_zones_async_invoker(self, request):
        http_info = self._nova_list_availability_zones_http_info(request)
        return AsyncInvoker(self, http_info)

    def _nova_list_availability_zones_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.1/{project_id}/os-availability-zone",
            "request_type": request.__class__.__name__,
            "response_type": "NovaListAvailabilityZonesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def nova_list_keypairs_async(self, request):
        """查询SSH密钥列表

        查询SSH密钥信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NovaListKeypairs
        :type request: :class:`huaweicloudsdkecs.v2.NovaListKeypairsRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.NovaListKeypairsResponse`
        """
        http_info = self._nova_list_keypairs_http_info(request)
        return self._call_api(**http_info)

    def nova_list_keypairs_async_invoker(self, request):
        http_info = self._nova_list_keypairs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _nova_list_keypairs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.1/{project_id}/os-keypairs",
            "request_type": request.__class__.__name__,
            "response_type": "NovaListKeypairsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def nova_list_server_security_groups_async(self, request):
        """查询指定云服务器安全组列表

        查询指定弹性云服务器的安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NovaListServerSecurityGroups
        :type request: :class:`huaweicloudsdkecs.v2.NovaListServerSecurityGroupsRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.NovaListServerSecurityGroupsResponse`
        """
        http_info = self._nova_list_server_security_groups_http_info(request)
        return self._call_api(**http_info)

    def nova_list_server_security_groups_async_invoker(self, request):
        http_info = self._nova_list_server_security_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _nova_list_server_security_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.1/{project_id}/servers/{server_id}/os-security-groups",
            "request_type": request.__class__.__name__,
            "response_type": "NovaListServerSecurityGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def nova_list_servers_details_async(self, request):
        """查询云服务器详情列表

        查询云服务器详情信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NovaListServersDetails
        :type request: :class:`huaweicloudsdkecs.v2.NovaListServersDetailsRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.NovaListServersDetailsResponse`
        """
        http_info = self._nova_list_servers_details_http_info(request)
        return self._call_api(**http_info)

    def nova_list_servers_details_async_invoker(self, request):
        http_info = self._nova_list_servers_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _nova_list_servers_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.1/{project_id}/servers/detail",
            "request_type": request.__class__.__name__,
            "response_type": "NovaListServersDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def nova_show_keypair_async(self, request):
        """查询SSH密钥详情

        根据SSH密钥名称查询指定SSH密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NovaShowKeypair
        :type request: :class:`huaweicloudsdkecs.v2.NovaShowKeypairRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.NovaShowKeypairResponse`
        """
        http_info = self._nova_show_keypair_http_info(request)
        return self._call_api(**http_info)

    def nova_show_keypair_async_invoker(self, request):
        http_info = self._nova_show_keypair_http_info(request)
        return AsyncInvoker(self, http_info)

    def _nova_show_keypair_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.1/{project_id}/os-keypairs/{keypair_name}",
            "request_type": request.__class__.__name__,
            "response_type": "NovaShowKeypairResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def nova_show_server_async(self, request):
        """查询云服务器详情

        根据云服务器ID，查询云服务器的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NovaShowServer
        :type request: :class:`huaweicloudsdkecs.v2.NovaShowServerRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.NovaShowServerResponse`
        """
        http_info = self._nova_show_server_http_info(request)
        return self._call_api(**http_info)

    def nova_show_server_async_invoker(self, request):
        http_info = self._nova_show_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _nova_show_server_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.1/{project_id}/servers/{server_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NovaShowServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def register_server_auto_recovery_async(self, request):
        """管理云服务器自动恢复动作

        配置、删除云服务器自动恢复动作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RegisterServerAutoRecovery
        :type request: :class:`huaweicloudsdkecs.v2.RegisterServerAutoRecoveryRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.RegisterServerAutoRecoveryResponse`
        """
        http_info = self._register_server_auto_recovery_http_info(request)
        return self._call_api(**http_info)

    def register_server_auto_recovery_async_invoker(self, request):
        http_info = self._register_server_auto_recovery_http_info(request)
        return AsyncInvoker(self, http_info)

    def _register_server_auto_recovery_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/cloudservers/{server_id}/autorecovery",
            "request_type": request.__class__.__name__,
            "response_type": "RegisterServerAutoRecoveryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def register_server_monitor_async(self, request):
        """注册云服务器监控

        将云服务器添加到监控表中。
        
        注册到监控表中的云服务会被ceilometer周期性采集监控数据，包括平台的版本、cpu信息、内存、网卡、磁盘、硬件平台等信息，这些数据上报给云监控。例如SAP云服务器内部的插件会周期性从云监控中查询监控数据，以报表形式呈现给SAP。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RegisterServerMonitor
        :type request: :class:`huaweicloudsdkecs.v2.RegisterServerMonitorRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.RegisterServerMonitorResponse`
        """
        http_info = self._register_server_monitor_http_info(request)
        return self._call_api(**http_info)

    def register_server_monitor_async_invoker(self, request):
        http_info = self._register_server_monitor_http_info(request)
        return AsyncInvoker(self, http_info)

    def _register_server_monitor_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/servers/{server_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "RegisterServerMonitorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def reinstall_server_with_cloud_init_async(self, request):
        """重装弹性云服务器操作系统(安装Cloud-init)

        重装弹性云服务器的操作系统。支持弹性云服务器数据盘不变的情况下，使用原镜像重装系统盘。
        
        调用该接口后，系统将卸载系统盘，然后使用原镜像重新创建系统盘，并挂载至弹性云服务器，实现重装操作系统功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ReinstallServerWithCloudInit
        :type request: :class:`huaweicloudsdkecs.v2.ReinstallServerWithCloudInitRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ReinstallServerWithCloudInitResponse`
        """
        http_info = self._reinstall_server_with_cloud_init_http_info(request)
        return self._call_api(**http_info)

    def reinstall_server_with_cloud_init_async_invoker(self, request):
        http_info = self._reinstall_server_with_cloud_init_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reinstall_server_with_cloud_init_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cloudservers/{server_id}/reinstallos",
            "request_type": request.__class__.__name__,
            "response_type": "ReinstallServerWithCloudInitResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def reinstall_server_without_cloud_init_async(self, request):
        """重装弹性云服务器操作系统(未安装Cloud init)

        重装弹性云服务器的操作系统。
        
        该接口支持未安装Cloud-init或Cloudbase-init的镜像。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ReinstallServerWithoutCloudInit
        :type request: :class:`huaweicloudsdkecs.v2.ReinstallServerWithoutCloudInitRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ReinstallServerWithoutCloudInitResponse`
        """
        http_info = self._reinstall_server_without_cloud_init_http_info(request)
        return self._call_api(**http_info)

    def reinstall_server_without_cloud_init_async_invoker(self, request):
        http_info = self._reinstall_server_without_cloud_init_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reinstall_server_without_cloud_init_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloudservers/{server_id}/reinstallos",
            "request_type": request.__class__.__name__,
            "response_type": "ReinstallServerWithoutCloudInitResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def reset_server_password_async(self, request):
        """一键重置弹性云服务器密码(企业项目)

        重置弹性云服务器管理帐号（root用户或Administrator用户）的密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetServerPassword
        :type request: :class:`huaweicloudsdkecs.v2.ResetServerPasswordRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ResetServerPasswordResponse`
        """
        http_info = self._reset_server_password_http_info(request)
        return self._call_api(**http_info)

    def reset_server_password_async_invoker(self, request):
        http_info = self._reset_server_password_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reset_server_password_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/cloudservers/{server_id}/os-reset-password",
            "request_type": request.__class__.__name__,
            "response_type": "ResetServerPasswordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

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
        http_info = self._resize_post_paid_server_http_info(request)
        return self._call_api(**http_info)

    def resize_post_paid_server_async_invoker(self, request):
        http_info = self._resize_post_paid_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _resize_post_paid_server_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloudservers/{server_id}/resize",
            "request_type": request.__class__.__name__,
            "response_type": "ResizePostPaidServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

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
        http_info = self._resize_server_http_info(request)
        return self._call_api(**http_info)

    def resize_server_async_invoker(self, request):
        http_info = self._resize_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _resize_server_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.1/{project_id}/cloudservers/{server_id}/resize",
            "request_type": request.__class__.__name__,
            "response_type": "ResizeServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_reset_password_flag_async(self, request):
        """查询是否支持一键重置密码

        查询弹性云服务器是否支持一键重置密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResetPasswordFlag
        :type request: :class:`huaweicloudsdkecs.v2.ShowResetPasswordFlagRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ShowResetPasswordFlagResponse`
        """
        http_info = self._show_reset_password_flag_http_info(request)
        return self._call_api(**http_info)

    def show_reset_password_flag_async_invoker(self, request):
        http_info = self._show_reset_password_flag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_reset_password_flag_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloudservers/{server_id}/os-resetpwd-flag",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResetPasswordFlagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_server_async(self, request):
        """查询云服务器详情

        查询弹性云服务器的详细信息。
        
        该接口支持查询弹性云服务器的计费方式，以及是否被冻结。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServer
        :type request: :class:`huaweicloudsdkecs.v2.ShowServerRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ShowServerResponse`
        """
        http_info = self._show_server_http_info(request)
        return self._call_api(**http_info)

    def show_server_async_invoker(self, request):
        http_info = self._show_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_server_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloudservers/{server_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_server_auto_recovery_async(self, request):
        """查询云服务器是否配置了自动恢复动作

        查询云服务器是否配置了自动恢复动作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServerAutoRecovery
        :type request: :class:`huaweicloudsdkecs.v2.ShowServerAutoRecoveryRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ShowServerAutoRecoveryResponse`
        """
        http_info = self._show_server_auto_recovery_http_info(request)
        return self._call_api(**http_info)

    def show_server_auto_recovery_async_invoker(self, request):
        http_info = self._show_server_auto_recovery_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_server_auto_recovery_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloudservers/{server_id}/autorecovery",
            "request_type": request.__class__.__name__,
            "response_type": "ShowServerAutoRecoveryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_server_block_device_async(self, request):
        """查询弹性云服务器单个磁盘信息

        查询弹性云服务器挂载的单个磁盘信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServerBlockDevice
        :type request: :class:`huaweicloudsdkecs.v2.ShowServerBlockDeviceRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ShowServerBlockDeviceResponse`
        """
        http_info = self._show_server_block_device_http_info(request)
        return self._call_api(**http_info)

    def show_server_block_device_async_invoker(self, request):
        http_info = self._show_server_block_device_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_server_block_device_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloudservers/{server_id}/block_device/{volume_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowServerBlockDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_server_group_async(self, request):
        """查询云服务器组详情

        查询弹性云服务器组详情。
        
        与原生的创建云服务器组接口不同之处在于该接口支持企业项目细粒度权限的校验。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServerGroup
        :type request: :class:`huaweicloudsdkecs.v2.ShowServerGroupRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ShowServerGroupResponse`
        """
        http_info = self._show_server_group_http_info(request)
        return self._call_api(**http_info)

    def show_server_group_async_invoker(self, request):
        http_info = self._show_server_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_server_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloudservers/os-server-groups/{server_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowServerGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_group_id' in local_var_params:
            path_params['server_group_id'] = local_var_params['server_group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_server_limits_async(self, request):
        """查询租户配额

        查询租户配额信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServerLimits
        :type request: :class:`huaweicloudsdkecs.v2.ShowServerLimitsRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ShowServerLimitsResponse`
        """
        http_info = self._show_server_limits_http_info(request)
        return self._call_api(**http_info)

    def show_server_limits_async_invoker(self, request):
        http_info = self._show_server_limits_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_server_limits_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloudservers/limits",
            "request_type": request.__class__.__name__,
            "response_type": "ShowServerLimitsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_server_password_async(self, request):
        """云服务器获取密码(企业项目)

        当通过支持Cloudbase-init功能的镜像创建Windows云服务器时，获取云服务器初始安装时系统生成的管理员帐户（Administrator帐户或Cloudbase-init设置的帐户）随机密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServerPassword
        :type request: :class:`huaweicloudsdkecs.v2.ShowServerPasswordRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ShowServerPasswordResponse`
        """
        http_info = self._show_server_password_http_info(request)
        return self._call_api(**http_info)

    def show_server_password_async_invoker(self, request):
        http_info = self._show_server_password_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_server_password_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloudservers/{server_id}/os-server-password",
            "request_type": request.__class__.__name__,
            "response_type": "ShowServerPasswordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_server_remote_console_async(self, request):
        """获取VNC远程登录地址

        获取弹性云服务器VNC远程登录地址。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServerRemoteConsole
        :type request: :class:`huaweicloudsdkecs.v2.ShowServerRemoteConsoleRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ShowServerRemoteConsoleResponse`
        """
        http_info = self._show_server_remote_console_http_info(request)
        return self._call_api(**http_info)

    def show_server_remote_console_async_invoker(self, request):
        http_info = self._show_server_remote_console_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_server_remote_console_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloudservers/{server_id}/remote_console",
            "request_type": request.__class__.__name__,
            "response_type": "ShowServerRemoteConsoleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_server_tags_async(self, request):
        """查询云服务器标签

        - 查询指定云服务器的标签信息。
        
        - 标签管理服务TMS使用该接口查询指定云服务器的全部标签数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServerTags
        :type request: :class:`huaweicloudsdkecs.v2.ShowServerTagsRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ShowServerTagsResponse`
        """
        http_info = self._show_server_tags_http_info(request)
        return self._call_api(**http_info)

    def show_server_tags_async_invoker(self, request):
        http_info = self._show_server_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_server_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloudservers/{server_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowServerTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_server_async(self, request):
        """修改云服务器

        修改云服务器信息，目前支持修改云服务器名称及描述和hostname。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateServer
        :type request: :class:`huaweicloudsdkecs.v2.UpdateServerRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.UpdateServerResponse`
        """
        http_info = self._update_server_http_info(request)
        return self._call_api(**http_info)

    def update_server_async_invoker(self, request):
        http_info = self._update_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_server_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/cloudservers/{server_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_server_auto_terminate_time_async(self, request):
        """修改云服务器定时删除时间

        修改按需服务器，设置定时删除时间。如果设置的定时删除时间为空字符串，表示取消定时删除。
        
        该接口支持企业项目细粒度权限的校验，具体细粒度请参见 ecs:cloudServers:put。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateServerAutoTerminateTime
        :type request: :class:`huaweicloudsdkecs.v2.UpdateServerAutoTerminateTimeRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.UpdateServerAutoTerminateTimeResponse`
        """
        http_info = self._update_server_auto_terminate_time_http_info(request)
        return self._call_api(**http_info)

    def update_server_auto_terminate_time_async_invoker(self, request):
        http_info = self._update_server_auto_terminate_time_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_server_auto_terminate_time_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloudservers/{server_id}/actions/update-auto-terminate-time",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateServerAutoTerminateTimeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_server_block_device_async(self, request):
        """修改云服务器挂载的单个磁盘信息

        修改云服务器云主机挂载的单个磁盘信息。&#39;当前仅支持修改delete_on_termination字段。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateServerBlockDevice
        :type request: :class:`huaweicloudsdkecs.v2.UpdateServerBlockDeviceRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.UpdateServerBlockDeviceResponse`
        """
        http_info = self._update_server_block_device_http_info(request)
        return self._call_api(**http_info)

    def update_server_block_device_async_invoker(self, request):
        http_info = self._update_server_block_device_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_server_block_device_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/cloudservers/{server_id}/block_device/{volume_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateServerBlockDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

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
        http_info = self._update_server_metadata_http_info(request)
        return self._call_api(**http_info)

    def update_server_metadata_async_invoker(self, request):
        http_info = self._update_server_metadata_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_server_metadata_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloudservers/{server_id}/metadata",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateServerMetadataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_job_async(self, request):
        """查询任务的执行状态

        查询Job的执行状态。
        
        对于创建云服务器、删除云服务器、云服务器批量操作和网卡操作等异步API，命令下发后，会返回job_id，通过job_id可以查询任务的执行状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJob
        :type request: :class:`huaweicloudsdkecs.v2.ShowJobRequest`
        :rtype: :class:`huaweicloudsdkecs.v2.ShowJobResponse`
        """
        http_info = self._show_job_http_info(request)
        return self._call_api(**http_info)

    def show_job_async_invoker(self, request):
        http_info = self._show_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def _call_api(self, **kwargs):
        try:
            kwargs["async_request"] = True
            return self.do_http_request(**kwargs)
        except TypeError:
            import inspect
            params = inspect.signature(self.do_http_request).parameters
            http_info = {param_name: kwargs.get(param_name) for param_name in params if param_name in kwargs}
            return self.do_http_request(**http_info)

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
