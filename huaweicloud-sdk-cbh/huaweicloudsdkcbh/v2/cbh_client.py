# coding: utf-8

from __future__ import absolute_import

import importlib
import warnings

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest
try:
    from huaweicloudsdkcore.invoker.invoker import SyncInvoker
except ImportError as e:
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcbh'")


class CbhClient(Client):
    def __init__(self):
        super(CbhClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcbh.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CbhClient":
                raise TypeError("client type error, support client type is CbhClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_create_instance_tag(self, request):
        """操作堡垒机实例资源标签

        操作堡垒机实例资源标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateInstanceTag
        :type request: :class:`huaweicloudsdkcbh.v2.BatchCreateInstanceTagRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.BatchCreateInstanceTagResponse`
        """
        http_info = self._batch_create_instance_tag_http_info(request)
        return self._call_api(**http_info)

    def batch_create_instance_tag_invoker(self, request):
        http_info = self._batch_create_instance_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_instance_tag_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cbs/instance/{resource_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateInstanceTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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

    def change_instance_type(self, request):
        """修改单机堡垒机实例类型

        修改单机堡垒机实例类型。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeInstanceType
        :type request: :class:`huaweicloudsdkcbh.v2.ChangeInstanceTypeRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.ChangeInstanceTypeResponse`
        """
        http_info = self._change_instance_type_http_info(request)
        return self._call_api(**http_info)

    def change_instance_type_invoker(self, request):
        http_info = self._change_instance_type_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_instance_type_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/cbs/instance/type",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeInstanceTypeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'server_id' in local_var_params:
            query_params.append(('server_id', local_var_params['server_id']))
        if 'availability_zone' in local_var_params:
            query_params.append(('availability_zone', local_var_params['availability_zone']))
        if 'is_auto_pay' in local_var_params:
            query_params.append(('is_auto_pay', local_var_params['is_auto_pay']))

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

    def count_instances_by_tag(self, request):
        """统计符合标签条件的实例数量

        统计符合标签条件的实例数量。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountInstancesByTag
        :type request: :class:`huaweicloudsdkcbh.v2.CountInstancesByTagRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.CountInstancesByTagResponse`
        """
        http_info = self._count_instances_by_tag_http_info(request)
        return self._call_api(**http_info)

    def count_instances_by_tag_invoker(self, request):
        http_info = self._count_instances_by_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _count_instances_by_tag_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cbs/instance/count",
            "request_type": request.__class__.__name__,
            "response_type": "CountInstancesByTagResponse"
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

    def create_instance(self, request):
        """创建堡垒机实例

        创建云堡垒机实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstance
        :type request: :class:`huaweicloudsdkcbh.v2.CreateInstanceRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.CreateInstanceResponse`
        """
        http_info = self._create_instance_http_info(request)
        return self._call_api(**http_info)

    def create_instance_invoker(self, request):
        http_info = self._create_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cbs/instance",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceResponse"
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

    def delete_instance(self, request):
        """删除故障云堡垒机实例

        删除云堡垒机故障实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstance
        :type request: :class:`huaweicloudsdkcbh.v2.DeleteInstanceRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.DeleteInstanceResponse`
        """
        http_info = self._delete_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_invoker(self, request):
        http_info = self._delete_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_instance_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/cbs/instance",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))

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

    def install_instance_eip(self, request):
        """堡垒机实例绑定弹性公网IP

        云堡垒机实例绑定弹性公网IP。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for InstallInstanceEip
        :type request: :class:`huaweicloudsdkcbh.v2.InstallInstanceEipRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.InstallInstanceEipResponse`
        """
        http_info = self._install_instance_eip_http_info(request)
        return self._call_api(**http_info)

    def install_instance_eip_invoker(self, request):
        http_info = self._install_instance_eip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _install_instance_eip_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cbs/instance/{server_id}/eip/bind",
            "request_type": request.__class__.__name__,
            "response_type": "InstallInstanceEipResponse"
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

    def list_available_zones(self, request):
        """获取服务可用区信息

        获取云堡垒机服务可用区信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAvailableZones
        :type request: :class:`huaweicloudsdkcbh.v2.ListAvailableZonesRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.ListAvailableZonesResponse`
        """
        http_info = self._list_available_zones_http_info(request)
        return self._call_api(**http_info)

    def list_available_zones_invoker(self, request):
        http_info = self._list_available_zones_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_available_zones_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cbs/available-zone",
            "request_type": request.__class__.__name__,
            "response_type": "ListAvailableZonesResponse"
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

    def list_instances(self, request):
        """获取堡垒机实例列表

        获取当前租户下的堡垒机实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstances
        :type request: :class:`huaweicloudsdkcbh.v2.ListInstancesRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.ListInstancesResponse`
        """
        http_info = self._list_instances_http_info(request)
        return self._call_api(**http_info)

    def list_instances_invoker(self, request):
        http_info = self._list_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cbs/instance/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))

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

    def list_instances_by_tag(self, request):
        """使用标签过滤实例

        使用标签过滤实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstancesByTag
        :type request: :class:`huaweicloudsdkcbh.v2.ListInstancesByTagRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.ListInstancesByTagResponse`
        """
        http_info = self._list_instances_by_tag_http_info(request)
        return self._call_api(**http_info)

    def list_instances_by_tag_invoker(self, request):
        http_info = self._list_instances_by_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instances_by_tag_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cbs/instance/filter",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstancesByTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'limit' in local_var_params:
            header_params['limit'] = local_var_params['limit']
        if 'offset' in local_var_params:
            header_params['offset'] = local_var_params['offset']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
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

    def list_specifications(self, request):
        """查询云堡垒机规格信息

        查询云堡垒机规格信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSpecifications
        :type request: :class:`huaweicloudsdkcbh.v2.ListSpecificationsRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.ListSpecificationsResponse`
        """
        http_info = self._list_specifications_http_info(request)
        return self._call_api(**http_info)

    def list_specifications_invoker(self, request):
        http_info = self._list_specifications_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_specifications_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cbs/instance/specification",
            "request_type": request.__class__.__name__,
            "response_type": "ListSpecificationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))
        if 'spec_code' in local_var_params:
            query_params.append(('spec_code', local_var_params['spec_code']))

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

    def list_tags(self, request):
        """查询租户在项目中的资源标签集合

        查询租户在项目中的资源标签集合。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTags
        :type request: :class:`huaweicloudsdkcbh.v2.ListTagsRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.ListTagsResponse`
        """
        http_info = self._list_tags_http_info(request)
        return self._call_api(**http_info)

    def list_tags_invoker(self, request):
        http_info = self._list_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cbs/instance/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListTagsResponse"
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

    def login_instance(self, request):
        """IAM用户登录堡垒机实例console

        IAM用户登录堡垒机实例console。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for LoginInstance
        :type request: :class:`huaweicloudsdkcbh.v2.LoginInstanceRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.LoginInstanceResponse`
        """
        http_info = self._login_instance_http_info(request)
        return self._call_api(**http_info)

    def login_instance_invoker(self, request):
        http_info = self._login_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _login_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cbs/instance/login",
            "request_type": request.__class__.__name__,
            "response_type": "LoginInstanceResponse"
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

    def login_instance_admin(self, request):
        """用户登录堡垒机实例admin的console

        用户登录堡垒机实例admin的console。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for LoginInstanceAdmin
        :type request: :class:`huaweicloudsdkcbh.v2.LoginInstanceAdminRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.LoginInstanceAdminResponse`
        """
        http_info = self._login_instance_admin_http_info(request)
        return self._call_api(**http_info)

    def login_instance_admin_invoker(self, request):
        http_info = self._login_instance_admin_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _login_instance_admin_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cbs/instances/{server_id}/admin-url",
            "request_type": request.__class__.__name__,
            "response_type": "LoginInstanceAdminResponse"
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

    def reboot_instance(self, request):
        """重启堡垒机实例

        重启云堡垒机实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RebootInstance
        :type request: :class:`huaweicloudsdkcbh.v2.RebootInstanceRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.RebootInstanceResponse`
        """
        http_info = self._reboot_instance_http_info(request)
        return self._call_api(**http_info)

    def reboot_instance_invoker(self, request):
        http_info = self._reboot_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reboot_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cbs/instance/reboot",
            "request_type": request.__class__.__name__,
            "response_type": "RebootInstanceResponse"
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

    def register_authorization(self, request):
        """租户创建或取消云堡垒机服务的委托授权

        租户创建或取消云堡垒机服务的委托授权。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RegisterAuthorization
        :type request: :class:`huaweicloudsdkcbh.v2.RegisterAuthorizationRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.RegisterAuthorizationResponse`
        """
        http_info = self._register_authorization_http_info(request)
        return self._call_api(**http_info)

    def register_authorization_invoker(self, request):
        http_info = self._register_authorization_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _register_authorization_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cbs/agency/authorization",
            "request_type": request.__class__.__name__,
            "response_type": "RegisterAuthorizationResponse"
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

    def reset_instance_login_method(self, request):
        """重置堡垒机实例admin登录方式

        重置堡垒机实例admin用户登录方式。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetInstanceLoginMethod
        :type request: :class:`huaweicloudsdkcbh.v2.ResetInstanceLoginMethodRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.ResetInstanceLoginMethodResponse`
        """
        http_info = self._reset_instance_login_method_http_info(request)
        return self._call_api(**http_info)

    def reset_instance_login_method_invoker(self, request):
        http_info = self._reset_instance_login_method_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_instance_login_method_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/cbs/instance/login-method",
            "request_type": request.__class__.__name__,
            "response_type": "ResetInstanceLoginMethodResponse"
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

    def reset_instance_password(self, request):
        """重置堡垒机实例admin密码

        重置云堡垒机实例web登录admin用户密码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetInstancePassword
        :type request: :class:`huaweicloudsdkcbh.v2.ResetInstancePasswordRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.ResetInstancePasswordResponse`
        """
        http_info = self._reset_instance_password_http_info(request)
        return self._call_api(**http_info)

    def reset_instance_password_invoker(self, request):
        http_info = self._reset_instance_password_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_instance_password_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/cbs/instance/password",
            "request_type": request.__class__.__name__,
            "response_type": "ResetInstancePasswordResponse"
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

    def resize_instance(self, request):
        """变更堡垒机实例

        变更云堡垒机实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResizeInstance
        :type request: :class:`huaweicloudsdkcbh.v2.ResizeInstanceRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.ResizeInstanceResponse`
        """
        http_info = self._resize_instance_http_info(request)
        return self._call_api(**http_info)

    def resize_instance_invoker(self, request):
        http_info = self._resize_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _resize_instance_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/cbs/instance",
            "request_type": request.__class__.__name__,
            "response_type": "ResizeInstanceResponse"
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

    def rollback_instance(self, request):
        """回退升级的堡垒机实例

        回退升级的云堡垒机实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RollbackInstance
        :type request: :class:`huaweicloudsdkcbh.v2.RollbackInstanceRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.RollbackInstanceResponse`
        """
        http_info = self._rollback_instance_http_info(request)
        return self._call_api(**http_info)

    def rollback_instance_invoker(self, request):
        http_info = self._rollback_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _rollback_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cbs/instance/rollback",
            "request_type": request.__class__.__name__,
            "response_type": "RollbackInstanceResponse"
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

    def show_authorization(self, request):
        """获取租户给云堡垒机服务委托授权信息

        获取租户给云堡垒机服务委托授权信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAuthorization
        :type request: :class:`huaweicloudsdkcbh.v2.ShowAuthorizationRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.ShowAuthorizationResponse`
        """
        http_info = self._show_authorization_http_info(request)
        return self._call_api(**http_info)

    def show_authorization_invoker(self, request):
        http_info = self._show_authorization_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_authorization_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cbs/agency/authorization",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuthorizationResponse"
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

    def show_ecs_quota(self, request):
        """获取创建堡垒机实例所需ECS资源配额

        获取当前租户所选择的可用分区里的堡垒机ECS规格是否可用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEcsQuota
        :type request: :class:`huaweicloudsdkcbh.v2.ShowEcsQuotaRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.ShowEcsQuotaResponse`
        """
        http_info = self._show_ecs_quota_http_info(request)
        return self._call_api(**http_info)

    def show_ecs_quota_invoker(self, request):
        http_info = self._show_ecs_quota_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_ecs_quota_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cbs/instance/ecs-quota",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEcsQuotaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'availability_zone' in local_var_params:
            query_params.append(('availability_zone', local_var_params['availability_zone']))
        if 'resource_spec_code' in local_var_params:
            query_params.append(('resource_spec_code', local_var_params['resource_spec_code']))

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

    def show_instance_status(self, request):
        """获取堡垒机实例状态信息

        获取堡垒机实例状态信息（未删除实例）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceStatus
        :type request: :class:`huaweicloudsdkcbh.v2.ShowInstanceStatusRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.ShowInstanceStatusResponse`
        """
        http_info = self._show_instance_status_http_info(request)
        return self._call_api(**http_info)

    def show_instance_status_invoker(self, request):
        http_info = self._show_instance_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cbs/instance/{server_id}/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceStatusResponse"
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

    def show_instance_tags(self, request):
        """查询堡垒机实例资源的标签信息

        查询堡垒机实例资源的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceTags
        :type request: :class:`huaweicloudsdkcbh.v2.ShowInstanceTagsRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.ShowInstanceTagsResponse`
        """
        http_info = self._show_instance_tags_http_info(request)
        return self._call_api(**http_info)

    def show_instance_tags_invoker(self, request):
        http_info = self._show_instance_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cbs/instance/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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

    def show_om_url(self, request):
        """获取运维链接

        获取运维链接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOmUrl
        :type request: :class:`huaweicloudsdkcbh.v2.ShowOmUrlRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.ShowOmUrlResponse`
        """
        http_info = self._show_om_url_http_info(request)
        return self._call_api(**http_info)

    def show_om_url_invoker(self, request):
        http_info = self._show_om_url_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_om_url_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cbs/instance/get-om-url",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOmUrlResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'server_id' in local_var_params:
            query_params.append(('server_id', local_var_params['server_id']))
        if 'ip_address' in local_var_params:
            query_params.append(('ip_address', local_var_params['ip_address']))
        if 'host_account_name' in local_var_params:
            query_params.append(('host_account_name', local_var_params['host_account_name']))

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

    def show_quota(self, request):
        """获取堡垒机实例配额

        获取堡垒机实例配额信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowQuota
        :type request: :class:`huaweicloudsdkcbh.v2.ShowQuotaRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.ShowQuotaResponse`
        """
        http_info = self._show_quota_http_info(request)
        return self._call_api(**http_info)

    def show_quota_invoker(self, request):
        http_info = self._show_quota_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_quota_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cbs/instance/quota",
            "request_type": request.__class__.__name__,
            "response_type": "ShowQuotaResponse"
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

    def start_instance(self, request):
        """启动堡垒机实例

        启动云堡垒机实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartInstance
        :type request: :class:`huaweicloudsdkcbh.v2.StartInstanceRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.StartInstanceResponse`
        """
        http_info = self._start_instance_http_info(request)
        return self._call_api(**http_info)

    def start_instance_invoker(self, request):
        http_info = self._start_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cbs/instance/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartInstanceResponse"
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

    def stop_instance(self, request):
        """关闭堡垒机实例

        关闭云堡垒机实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopInstance
        :type request: :class:`huaweicloudsdkcbh.v2.StopInstanceRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.StopInstanceResponse`
        """
        http_info = self._stop_instance_http_info(request)
        return self._call_api(**http_info)

    def stop_instance_invoker(self, request):
        http_info = self._stop_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cbs/instance/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopInstanceResponse"
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

    def switch_instance_vpc(self, request):
        """切换堡垒机虚拟私有云

        切换堡垒机虚拟私有云
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchInstanceVpc
        :type request: :class:`huaweicloudsdkcbh.v2.SwitchInstanceVpcRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.SwitchInstanceVpcResponse`
        """
        http_info = self._switch_instance_vpc_http_info(request)
        return self._call_api(**http_info)

    def switch_instance_vpc_invoker(self, request):
        http_info = self._switch_instance_vpc_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_instance_vpc_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/cbs/instance/vpc",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchInstanceVpcResponse"
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

    def uninstall_instance_eip(self, request):
        """堡垒机实例解绑弹性公网IP

        为云堡垒机实例解绑弹性公网IP。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UninstallInstanceEip
        :type request: :class:`huaweicloudsdkcbh.v2.UninstallInstanceEipRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.UninstallInstanceEipResponse`
        """
        http_info = self._uninstall_instance_eip_http_info(request)
        return self._call_api(**http_info)

    def uninstall_instance_eip_invoker(self, request):
        http_info = self._uninstall_instance_eip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _uninstall_instance_eip_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cbs/instance/{server_id}/eip/unbind",
            "request_type": request.__class__.__name__,
            "response_type": "UninstallInstanceEipResponse"
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

    def update_instance_security_group(self, request):
        """修改堡垒机实例安全组

        修改堡垒机实例安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceSecurityGroup
        :type request: :class:`huaweicloudsdkcbh.v2.UpdateInstanceSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.UpdateInstanceSecurityGroupResponse`
        """
        http_info = self._update_instance_security_group_http_info(request)
        return self._call_api(**http_info)

    def update_instance_security_group_invoker(self, request):
        http_info = self._update_instance_security_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_security_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/cbs/instance/{server_id}/security-groups",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceSecurityGroupResponse"
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

    def upgrade_instance(self, request):
        """升级堡垒机实例

        升级云堡垒机实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpgradeInstance
        :type request: :class:`huaweicloudsdkcbh.v2.UpgradeInstanceRequest`
        :rtype: :class:`huaweicloudsdkcbh.v2.UpgradeInstanceResponse`
        """
        http_info = self._upgrade_instance_http_info(request)
        return self._call_api(**http_info)

    def upgrade_instance_invoker(self, request):
        http_info = self._upgrade_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upgrade_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cbs/instance/upgrade",
            "request_type": request.__class__.__name__,
            "response_type": "UpgradeInstanceResponse"
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
        :param header_params: Header parameters to be placed in the request header.
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
            request_type=request_type)
