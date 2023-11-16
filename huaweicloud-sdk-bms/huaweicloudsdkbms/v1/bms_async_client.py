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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkbms'")


class BmsAsyncClient(Client):
    def __init__(self):
        super(BmsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkbms.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "BmsAsyncClient":
                raise TypeError("client type error, support client type is BmsAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_server_nics_async(self, request):
        """裸金属服务器绑定弹性网卡

        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddServerNics
        :type request: :class:`huaweicloudsdkbms.v1.AddServerNicsRequest`
        :rtype: :class:`huaweicloudsdkbms.v1.AddServerNicsResponse`
        """
        http_info = self._add_server_nics_http_info(request)
        return self._call_api(**http_info)

    def add_server_nics_async_invoker(self, request):
        http_info = self._add_server_nics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_server_nics_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/baremetalservers/{server_id}/nics",
            "request_type": request.__class__.__name__,
            "response_type": "AddServerNicsResponse"
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

    def attach_baremetal_server_volume_async(self, request):
        """裸金属服务器挂载云硬盘

        裸金属服务器创建成功后，如果发现磁盘不够用或者当前磁盘不满足要求，可以将已有云硬盘挂载给裸金属服务器，作为数据盘使用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AttachBaremetalServerVolume
        :type request: :class:`huaweicloudsdkbms.v1.AttachBaremetalServerVolumeRequest`
        :rtype: :class:`huaweicloudsdkbms.v1.AttachBaremetalServerVolumeResponse`
        """
        http_info = self._attach_baremetal_server_volume_http_info(request)
        return self._call_api(**http_info)

    def attach_baremetal_server_volume_async_invoker(self, request):
        http_info = self._attach_baremetal_server_volume_http_info(request)
        return AsyncInvoker(self, http_info)

    def _attach_baremetal_server_volume_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/baremetalservers/{server_id}/attachvolume",
            "request_type": request.__class__.__name__,
            "response_type": "AttachBaremetalServerVolumeResponse"
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

    def batch_create_baremetal_server_tags_async(self, request):
        """批量添加裸金属服务器标签

        - 为指定裸金属服务器批量添加标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateBaremetalServerTags
        :type request: :class:`huaweicloudsdkbms.v1.BatchCreateBaremetalServerTagsRequest`
        :rtype: :class:`huaweicloudsdkbms.v1.BatchCreateBaremetalServerTagsResponse`
        """
        http_info = self._batch_create_baremetal_server_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_baremetal_server_tags_async_invoker(self, request):
        http_info = self._batch_create_baremetal_server_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_baremetal_server_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/baremetalservers/{server_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateBaremetalServerTagsResponse"
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

    def batch_delete_baremetal_server_tags_async(self, request):
        """批量删除l裸金属服务器标签

        - 为指定云服务器批量删除标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteBaremetalServerTags
        :type request: :class:`huaweicloudsdkbms.v1.BatchDeleteBaremetalServerTagsRequest`
        :rtype: :class:`huaweicloudsdkbms.v1.BatchDeleteBaremetalServerTagsResponse`
        """
        http_info = self._batch_delete_baremetal_server_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_baremetal_server_tags_async_invoker(self, request):
        http_info = self._batch_delete_baremetal_server_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_baremetal_server_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/baremetalservers/{server_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteBaremetalServerTagsResponse"
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

    def batch_reboot_baremetal_servers_async(self, request):
        """重启裸金属服务器

        根据给定的裸金属服务器ID列表，批量重启裸金属服务器
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchRebootBaremetalServers
        :type request: :class:`huaweicloudsdkbms.v1.BatchRebootBaremetalServersRequest`
        :rtype: :class:`huaweicloudsdkbms.v1.BatchRebootBaremetalServersResponse`
        """
        http_info = self._batch_reboot_baremetal_servers_http_info(request)
        return self._call_api(**http_info)

    def batch_reboot_baremetal_servers_async_invoker(self, request):
        http_info = self._batch_reboot_baremetal_servers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_reboot_baremetal_servers_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/baremetalservers/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchRebootBaremetalServersResponse"
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

    def batch_start_baremetal_servers_async(self, request):
        """启动裸金属服务器

        根据给定的裸金属服务器ID列表，批量启动裸金属服务器
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchStartBaremetalServers
        :type request: :class:`huaweicloudsdkbms.v1.BatchStartBaremetalServersRequest`
        :rtype: :class:`huaweicloudsdkbms.v1.BatchStartBaremetalServersResponse`
        """
        http_info = self._batch_start_baremetal_servers_http_info(request)
        return self._call_api(**http_info)

    def batch_start_baremetal_servers_async_invoker(self, request):
        http_info = self._batch_start_baremetal_servers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_start_baremetal_servers_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/baremetalservers/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchStartBaremetalServersResponse"
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

    def batch_stop_baremetal_servers_async(self, request):
        """关闭裸金属服务器

        根据给定的裸金属服务器ID列表，批量关闭裸金属服务器
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchStopBaremetalServers
        :type request: :class:`huaweicloudsdkbms.v1.BatchStopBaremetalServersRequest`
        :rtype: :class:`huaweicloudsdkbms.v1.BatchStopBaremetalServersResponse`
        """
        http_info = self._batch_stop_baremetal_servers_http_info(request)
        return self._call_api(**http_info)

    def batch_stop_baremetal_servers_async_invoker(self, request):
        http_info = self._batch_stop_baremetal_servers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_stop_baremetal_servers_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/baremetalservers/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchStopBaremetalServersResponse"
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

    def change_baremetal_server_name_async(self, request):
        """修改裸金属服务器名称

        修改裸金属服务器名称
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeBaremetalServerName
        :type request: :class:`huaweicloudsdkbms.v1.ChangeBaremetalServerNameRequest`
        :rtype: :class:`huaweicloudsdkbms.v1.ChangeBaremetalServerNameResponse`
        """
        http_info = self._change_baremetal_server_name_http_info(request)
        return self._call_api(**http_info)

    def change_baremetal_server_name_async_invoker(self, request):
        http_info = self._change_baremetal_server_name_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_baremetal_server_name_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/baremetalservers/{server_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeBaremetalServerNameResponse"
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

    def change_baremetal_server_os_async(self, request):
        """change_baremetal_server_os

        切换裸金属服务器的操作系统。切换操作系统支持密码或者密钥注入，该接口支持企业项目细粒度权限的校验，具体细粒度请参见 bms:servers:changeOS
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeBaremetalServerOs
        :type request: :class:`huaweicloudsdkbms.v1.ChangeBaremetalServerOsRequest`
        :rtype: :class:`huaweicloudsdkbms.v1.ChangeBaremetalServerOsResponse`
        """
        http_info = self._change_baremetal_server_os_http_info(request)
        return self._call_api(**http_info)

    def change_baremetal_server_os_async_invoker(self, request):
        http_info = self._change_baremetal_server_os_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_baremetal_server_os_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/baremetalservers/{server_id}/changeos",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeBaremetalServerOsResponse"
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

    def create_bare_metal_servers_async(self, request):
        """创建裸金属服务器

        创建一台或多台裸金属服务器,裸金属服务器的登录鉴权方式包括两种：密钥对、密码。为安全起见，推荐使用密钥对方式
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateBareMetalServers
        :type request: :class:`huaweicloudsdkbms.v1.CreateBareMetalServersRequest`
        :rtype: :class:`huaweicloudsdkbms.v1.CreateBareMetalServersResponse`
        """
        http_info = self._create_bare_metal_servers_http_info(request)
        return self._call_api(**http_info)

    def create_bare_metal_servers_async_invoker(self, request):
        http_info = self._create_bare_metal_servers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_bare_metal_servers_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/baremetalservers",
            "request_type": request.__class__.__name__,
            "response_type": "CreateBareMetalServersResponse"
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

    def delete_server_nics_async(self, request):
        """裸金属服务器解绑弹性网卡

        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteServerNics
        :type request: :class:`huaweicloudsdkbms.v1.DeleteServerNicsRequest`
        :rtype: :class:`huaweicloudsdkbms.v1.DeleteServerNicsResponse`
        """
        http_info = self._delete_server_nics_http_info(request)
        return self._call_api(**http_info)

    def delete_server_nics_async_invoker(self, request):
        http_info = self._delete_server_nics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_server_nics_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/baremetalservers/{server_id}/nics/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteServerNicsResponse"
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

    def delete_windows_bare_metal_server_password_async(self, request):
        """Windows裸金属服务器清除密码

        清除Windows裸金属服务器初始安装时系统生成的密码记录。清除密码后，不影响裸金属服务器密码登录功能，但不能再使用获取密码功能来查询该裸金属服务器密码。如果裸金属服务器是通过私有镜像创建的，请确保已安装Cloudbase-init。公共镜像默认已安装该软件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteWindowsBareMetalServerPassword
        :type request: :class:`huaweicloudsdkbms.v1.DeleteWindowsBareMetalServerPasswordRequest`
        :rtype: :class:`huaweicloudsdkbms.v1.DeleteWindowsBareMetalServerPasswordResponse`
        """
        http_info = self._delete_windows_bare_metal_server_password_http_info(request)
        return self._call_api(**http_info)

    def delete_windows_bare_metal_server_password_async_invoker(self, request):
        http_info = self._delete_windows_bare_metal_server_password_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_windows_bare_metal_server_password_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/baremetalservers/{server_id}/os-server-password",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteWindowsBareMetalServerPasswordResponse"
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

    def detach_baremetal_server_volume_async(self, request):
        """裸金属服务器卸载云磁盘

        将挂载至裸金属服务器中的磁盘卸载；对于挂载在系统盘盘位（也就是“/dev/sda”挂载点）上的磁盘，不允许执行卸载操作；对于挂载在数据盘盘位（非“/dev/sda”挂载点）上的磁盘，支持离线卸载和在线卸载（裸金属服务器处于“运行中”状态）磁盘
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetachBaremetalServerVolume
        :type request: :class:`huaweicloudsdkbms.v1.DetachBaremetalServerVolumeRequest`
        :rtype: :class:`huaweicloudsdkbms.v1.DetachBaremetalServerVolumeResponse`
        """
        http_info = self._detach_baremetal_server_volume_http_info(request)
        return self._call_api(**http_info)

    def detach_baremetal_server_volume_async_invoker(self, request):
        http_info = self._detach_baremetal_server_volume_http_info(request)
        return AsyncInvoker(self, http_info)

    def _detach_baremetal_server_volume_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/baremetalservers/{server_id}/detachvolume/{attachment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DetachBaremetalServerVolumeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']
        if 'attachment_id' in local_var_params:
            path_params['attachment_id'] = local_var_params['attachment_id']

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

    def list_bare_metal_server_details_async(self, request):
        """查询裸金属服务器详情

        获取裸金属服务器详细信息，该接口支持查询裸金属服务器的计费方式，以及是否被冻结
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBareMetalServerDetails
        :type request: :class:`huaweicloudsdkbms.v1.ListBareMetalServerDetailsRequest`
        :rtype: :class:`huaweicloudsdkbms.v1.ListBareMetalServerDetailsResponse`
        """
        http_info = self._list_bare_metal_server_details_http_info(request)
        return self._call_api(**http_info)

    def list_bare_metal_server_details_async_invoker(self, request):
        http_info = self._list_bare_metal_server_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_bare_metal_server_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/baremetalservers/{server_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListBareMetalServerDetailsResponse"
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

    def list_bare_metal_servers_async(self, request):
        """查询裸金属服务器详情列表

        用户根据设置的请求条件筛选裸金属服务器，并获取裸金属服务器的详细信息。该接口支持查询裸金属服务器计费方式，以及是否被冻结。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBareMetalServers
        :type request: :class:`huaweicloudsdkbms.v1.ListBareMetalServersRequest`
        :rtype: :class:`huaweicloudsdkbms.v1.ListBareMetalServersResponse`
        """
        http_info = self._list_bare_metal_servers_http_info(request)
        return self._call_api(**http_info)

    def list_bare_metal_servers_async_invoker(self, request):
        http_info = self._list_bare_metal_servers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_bare_metal_servers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/baremetalservers/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ListBareMetalServersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'flavor' in local_var_params:
            query_params.append(('flavor', local_var_params['flavor']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'reservation_id' in local_var_params:
            query_params.append(('reservation_id', local_var_params['reservation_id']))
        if 'detail' in local_var_params:
            query_params.append(('detail', local_var_params['detail']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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

    def list_baremetal_flavor_detail_extends_async(self, request):
        """查询规格详情和规格扩展信息列表

        查询裸金属服务器的规格详情和规格的扩展信息。您可以调用此接口查询“baremetal:extBootType”参数取值，以确认某个规格是否支持快速发放
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBaremetalFlavorDetailExtends
        :type request: :class:`huaweicloudsdkbms.v1.ListBaremetalFlavorDetailExtendsRequest`
        :rtype: :class:`huaweicloudsdkbms.v1.ListBaremetalFlavorDetailExtendsResponse`
        """
        http_info = self._list_baremetal_flavor_detail_extends_http_info(request)
        return self._call_api(**http_info)

    def list_baremetal_flavor_detail_extends_async_invoker(self, request):
        http_info = self._list_baremetal_flavor_detail_extends_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_baremetal_flavor_detail_extends_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/baremetalservers/flavors",
            "request_type": request.__class__.__name__,
            "response_type": "ListBaremetalFlavorDetailExtendsResponse"
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

    def reinstall_baremetal_server_os_async(self, request):
        """重装裸金属服务器操作系统

        重装裸金属服务器的操作系统。快速发放裸金属服务器支持裸金属服务器数据盘不变的情况下，使用原镜像重装系统盘。重装操作系统支持密码或者密钥注入
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ReinstallBaremetalServerOs
        :type request: :class:`huaweicloudsdkbms.v1.ReinstallBaremetalServerOsRequest`
        :rtype: :class:`huaweicloudsdkbms.v1.ReinstallBaremetalServerOsResponse`
        """
        http_info = self._reinstall_baremetal_server_os_http_info(request)
        return self._call_api(**http_info)

    def reinstall_baremetal_server_os_async_invoker(self, request):
        http_info = self._reinstall_baremetal_server_os_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reinstall_baremetal_server_os_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/baremetalservers/{server_id}/reinstallos",
            "request_type": request.__class__.__name__,
            "response_type": "ReinstallBaremetalServerOsResponse"
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

    def reset_pwd_one_click_async(self, request):
        """一键重置裸金属服务器密码

        在裸金属服务器支持一键重置密码功能的前提下，重置裸金属服务器管理帐号（root用户或Administrator用户）的密码。可以通过6.10.1-查询是否支持一键重置密码API查询是否支持一键重置密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetPwdOneClick
        :type request: :class:`huaweicloudsdkbms.v1.ResetPwdOneClickRequest`
        :rtype: :class:`huaweicloudsdkbms.v1.ResetPwdOneClickResponse`
        """
        http_info = self._reset_pwd_one_click_http_info(request)
        return self._call_api(**http_info)

    def reset_pwd_one_click_async_invoker(self, request):
        http_info = self._reset_pwd_one_click_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reset_pwd_one_click_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/baremetalservers/{server_id}/os-reset-password",
            "request_type": request.__class__.__name__,
            "response_type": "ResetPwdOneClickResponse"
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

    def show_baremetal_server_interface_attachments_async(self, request):
        """查询裸金属服务器网卡信息

        查询裸金属服务器的网卡信息，比如网卡的IP地址、MAC地址
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBaremetalServerInterfaceAttachments
        :type request: :class:`huaweicloudsdkbms.v1.ShowBaremetalServerInterfaceAttachmentsRequest`
        :rtype: :class:`huaweicloudsdkbms.v1.ShowBaremetalServerInterfaceAttachmentsResponse`
        """
        http_info = self._show_baremetal_server_interface_attachments_http_info(request)
        return self._call_api(**http_info)

    def show_baremetal_server_interface_attachments_async_invoker(self, request):
        http_info = self._show_baremetal_server_interface_attachments_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_baremetal_server_interface_attachments_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/baremetalservers/{server_id}/os-interface",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBaremetalServerInterfaceAttachmentsResponse"
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

    def show_baremetal_server_tags_async(self, request):
        """查询裸金属服务器标签

        - 查询指定云服务器的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBaremetalServerTags
        :type request: :class:`huaweicloudsdkbms.v1.ShowBaremetalServerTagsRequest`
        :rtype: :class:`huaweicloudsdkbms.v1.ShowBaremetalServerTagsResponse`
        """
        http_info = self._show_baremetal_server_tags_http_info(request)
        return self._call_api(**http_info)

    def show_baremetal_server_tags_async_invoker(self, request):
        http_info = self._show_baremetal_server_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_baremetal_server_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/baremetalservers/{server_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBaremetalServerTagsResponse"
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

    def show_baremetal_server_volume_info_async(self, request):
        """查询裸金属服务器挂载的云硬盘信息

        查询裸金属服务器挂载的磁盘信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBaremetalServerVolumeInfo
        :type request: :class:`huaweicloudsdkbms.v1.ShowBaremetalServerVolumeInfoRequest`
        :rtype: :class:`huaweicloudsdkbms.v1.ShowBaremetalServerVolumeInfoResponse`
        """
        http_info = self._show_baremetal_server_volume_info_http_info(request)
        return self._call_api(**http_info)

    def show_baremetal_server_volume_info_async_invoker(self, request):
        http_info = self._show_baremetal_server_volume_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_baremetal_server_volume_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/baremetalservers/{server_id}/os-volume_attachments",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBaremetalServerVolumeInfoResponse"
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

    def show_reset_pwd_async(self, request):
        """查询是否支持一键重置密码

        查询是否支持一键重置密码
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResetPwd
        :type request: :class:`huaweicloudsdkbms.v1.ShowResetPwdRequest`
        :rtype: :class:`huaweicloudsdkbms.v1.ShowResetPwdResponse`
        """
        http_info = self._show_reset_pwd_http_info(request)
        return self._call_api(**http_info)

    def show_reset_pwd_async_invoker(self, request):
        http_info = self._show_reset_pwd_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_reset_pwd_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/baremetalservers/{server_id}/os-resetpwd-flag",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResetPwdResponse"
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
        """获取裸金属服务器远程登录地址

        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServerRemoteConsole
        :type request: :class:`huaweicloudsdkbms.v1.ShowServerRemoteConsoleRequest`
        :rtype: :class:`huaweicloudsdkbms.v1.ShowServerRemoteConsoleResponse`
        """
        http_info = self._show_server_remote_console_http_info(request)
        return self._call_api(**http_info)

    def show_server_remote_console_async_invoker(self, request):
        http_info = self._show_server_remote_console_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_server_remote_console_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/baremetalservers/{server_id}/remote_console",
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

    def show_tenant_quota_async(self, request):
        """查询租户配额

        查询该租户下，所有资源的配额信息，包括已使用配额
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTenantQuota
        :type request: :class:`huaweicloudsdkbms.v1.ShowTenantQuotaRequest`
        :rtype: :class:`huaweicloudsdkbms.v1.ShowTenantQuotaResponse`
        """
        http_info = self._show_tenant_quota_http_info(request)
        return self._call_api(**http_info)

    def show_tenant_quota_async_invoker(self, request):
        http_info = self._show_tenant_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_tenant_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/baremetalservers/limits",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTenantQuotaResponse"
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

    def show_windows_baremetal_server_pwd_async(self, request):
        """Windows裸金属服务器获取密码

        获取Windows裸金属服务器初始安装时系统生成的管理员帐户（Administrator帐户或Cloudbase-init设置的帐户）随机密码。如果裸金属服务器是通过私有镜像创建的，请确保已安装Cloudbase-init。公共镜像默认已安装该软件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWindowsBaremetalServerPwd
        :type request: :class:`huaweicloudsdkbms.v1.ShowWindowsBaremetalServerPwdRequest`
        :rtype: :class:`huaweicloudsdkbms.v1.ShowWindowsBaremetalServerPwdResponse`
        """
        http_info = self._show_windows_baremetal_server_pwd_http_info(request)
        return self._call_api(**http_info)

    def show_windows_baremetal_server_pwd_async_invoker(self, request):
        http_info = self._show_windows_baremetal_server_pwd_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_windows_baremetal_server_pwd_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/baremetalservers/{server_id}/os-server-password",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWindowsBaremetalServerPwdResponse"
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

    def update_baremetal_server_interface_attachments_async(self, request):
        """修改裸金属服务器弹性网卡的属性

        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateBaremetalServerInterfaceAttachments
        :type request: :class:`huaweicloudsdkbms.v1.UpdateBaremetalServerInterfaceAttachmentsRequest`
        :rtype: :class:`huaweicloudsdkbms.v1.UpdateBaremetalServerInterfaceAttachmentsResponse`
        """
        http_info = self._update_baremetal_server_interface_attachments_http_info(request)
        return self._call_api(**http_info)

    def update_baremetal_server_interface_attachments_async_invoker(self, request):
        http_info = self._update_baremetal_server_interface_attachments_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_baremetal_server_interface_attachments_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/baremetalservers/{server_id}/os-interface/{port_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateBaremetalServerInterfaceAttachmentsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']
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

    def update_baremetal_server_metadata_async(self, request):
        """更新裸金属服务器元数据

        更新裸金属服务器元数据。如果元数据中没有待更新字段，则自动添加该字段。如果元数据中已存在待更新字段，则直接更新字段值；如果元数据中的字段不再请求参数中，则保持不变
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateBaremetalServerMetadata
        :type request: :class:`huaweicloudsdkbms.v1.UpdateBaremetalServerMetadataRequest`
        :rtype: :class:`huaweicloudsdkbms.v1.UpdateBaremetalServerMetadataResponse`
        """
        http_info = self._update_baremetal_server_metadata_http_info(request)
        return self._call_api(**http_info)

    def update_baremetal_server_metadata_async_invoker(self, request):
        http_info = self._update_baremetal_server_metadata_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_baremetal_server_metadata_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/baremetalservers/{server_id}/metadata",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateBaremetalServerMetadataResponse"
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

    def show_specified_version_async(self, request):
        """查询指定API版本信息

        查询裸金属服务指定接口版本的信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSpecifiedVersion
        :type request: :class:`huaweicloudsdkbms.v1.ShowSpecifiedVersionRequest`
        :rtype: :class:`huaweicloudsdkbms.v1.ShowSpecifiedVersionResponse`
        """
        http_info = self._show_specified_version_http_info(request)
        return self._call_api(**http_info)

    def show_specified_version_async_invoker(self, request):
        http_info = self._show_specified_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_specified_version_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/{api_version}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSpecifiedVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'api_version' in local_var_params:
            path_params['api_version'] = local_var_params['api_version']

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

    def show_job_infos_async(self, request):
        """查询Job状态

        查询Job的执行状态。对于创建裸金属服务器物理机、挂卸卷等异步API，命令下发后，会返回job_id，通过job_id可以查询任务的执行状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobInfos
        :type request: :class:`huaweicloudsdkbms.v1.ShowJobInfosRequest`
        :rtype: :class:`huaweicloudsdkbms.v1.ShowJobInfosResponse`
        """
        http_info = self._show_job_infos_http_info(request)
        return self._call_api(**http_info)

    def show_job_infos_async_invoker(self, request):
        http_info = self._show_job_infos_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_infos_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobInfosResponse"
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
