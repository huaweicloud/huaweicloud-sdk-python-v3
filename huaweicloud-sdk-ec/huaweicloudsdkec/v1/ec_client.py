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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkec'")


class EcClient(Client):
    def __init__(self):
        super(EcClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkec.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials")
        else:
            if clazz.__name__ != "EcClient":
                raise TypeError("client type error, support client type is EcClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials")

        

        return client_builder

    def create_ecn_access_point(self, request):
        """添加新的接入点

        添加新的接入点
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEcnAccessPoint
        :type request: :class:`huaweicloudsdkec.v1.CreateEcnAccessPointRequest`
        :rtype: :class:`huaweicloudsdkec.v1.CreateEcnAccessPointResponse`
        """
        http_info = self._create_ecn_access_point_http_info(request)
        return self._call_api(**http_info)

    def create_ecn_access_point_invoker(self, request):
        http_info = self._create_ecn_access_point_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_ecn_access_point_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/enterprise-connect/enterprise-connect-network/{ecn_id}/access-point",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEcnAccessPointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ecn_id' in local_var_params:
            path_params['ecn_id'] = local_var_params['ecn_id']

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

    def delete_ecn_access_point(self, request):
        """删除接入点

        根据企业连接网络ID，删除接入点
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEcnAccessPoint
        :type request: :class:`huaweicloudsdkec.v1.DeleteEcnAccessPointRequest`
        :rtype: :class:`huaweicloudsdkec.v1.DeleteEcnAccessPointResponse`
        """
        http_info = self._delete_ecn_access_point_http_info(request)
        return self._call_api(**http_info)

    def delete_ecn_access_point_invoker(self, request):
        http_info = self._delete_ecn_access_point_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_ecn_access_point_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{domain_id}/enterprise-connect/enterprise-connect-network/{ecn_id}/access-point/{access_point_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEcnAccessPointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ecn_id' in local_var_params:
            path_params['ecn_id'] = local_var_params['ecn_id']
        if 'access_point_id' in local_var_params:
            path_params['access_point_id'] = local_var_params['access_point_id']

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

    def list_ecn_access_point_by_ecn_id(self, request):
        """查询接入点

        根据企业连接网络ID，查询其下所有接入点
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEcnAccessPointByEcnId
        :type request: :class:`huaweicloudsdkec.v1.ListEcnAccessPointByEcnIdRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ListEcnAccessPointByEcnIdResponse`
        """
        http_info = self._list_ecn_access_point_by_ecn_id_http_info(request)
        return self._call_api(**http_info)

    def list_ecn_access_point_by_ecn_id_invoker(self, request):
        http_info = self._list_ecn_access_point_by_ecn_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ecn_access_point_by_ecn_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/enterprise-connect/enterprise-connect-network/{ecn_id}/access-point",
            "request_type": request.__class__.__name__,
            "response_type": "ListEcnAccessPointByEcnIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ecn_id' in local_var_params:
            path_params['ecn_id'] = local_var_params['ecn_id']

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

    def update_ecn_access_point(self, request):
        """更新接入点

        根据企业连接网络ID，更新接入点
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateEcnAccessPoint
        :type request: :class:`huaweicloudsdkec.v1.UpdateEcnAccessPointRequest`
        :rtype: :class:`huaweicloudsdkec.v1.UpdateEcnAccessPointResponse`
        """
        http_info = self._update_ecn_access_point_http_info(request)
        return self._call_api(**http_info)

    def update_ecn_access_point_invoker(self, request):
        http_info = self._update_ecn_access_point_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_ecn_access_point_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{domain_id}/enterprise-connect/enterprise-connect-network/{ecn_id}/access-point/{access_point_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEcnAccessPointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ecn_id' in local_var_params:
            path_params['ecn_id'] = local_var_params['ecn_id']
        if 'access_point_id' in local_var_params:
            path_params['access_point_id'] = local_var_params['access_point_id']

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

    def add_ecn_with_ieg(self, request):
        """绑定智能企业网关到企业连接网络

        绑定智能企业网关到企业连接网络
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddEcnWithIeg
        :type request: :class:`huaweicloudsdkec.v1.AddEcnWithIegRequest`
        :rtype: :class:`huaweicloudsdkec.v1.AddEcnWithIegResponse`
        """
        http_info = self._add_ecn_with_ieg_http_info(request)
        return self._call_api(**http_info)

    def add_ecn_with_ieg_invoker(self, request):
        http_info = self._add_ecn_with_ieg_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_ecn_with_ieg_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/enterprise-connect/enterprise-connect-network/{ecn_id}/relationship/intelligent-enterprise-gateway",
            "request_type": request.__class__.__name__,
            "response_type": "AddEcnWithIegResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ecn_id' in local_var_params:
            path_params['ecn_id'] = local_var_params['ecn_id']

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

    def delete_ecn_with_ieg(self, request):
        """解除智能企业网关和企业连接网络的绑定

        解除智能企业网关和企业连接网络的绑定
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEcnWithIeg
        :type request: :class:`huaweicloudsdkec.v1.DeleteEcnWithIegRequest`
        :rtype: :class:`huaweicloudsdkec.v1.DeleteEcnWithIegResponse`
        """
        http_info = self._delete_ecn_with_ieg_http_info(request)
        return self._call_api(**http_info)

    def delete_ecn_with_ieg_invoker(self, request):
        http_info = self._delete_ecn_with_ieg_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_ecn_with_ieg_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{domain_id}/enterprise-connect/enterprise-connect-network/{ecn_id}/relationship/intelligent-enterprise-gateway/{relation_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEcnWithIegResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ecn_id' in local_var_params:
            path_params['ecn_id'] = local_var_params['ecn_id']
        if 'relation_id' in local_var_params:
            path_params['relation_id'] = local_var_params['relation_id']

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

    def list_ecn(self, request):
        """查询企业连接网络列表

        查询租户的企业连接网络列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEcn
        :type request: :class:`huaweicloudsdkec.v1.ListEcnRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ListEcnResponse`
        """
        http_info = self._list_ecn_http_info(request)
        return self._call_api(**http_info)

    def list_ecn_invoker(self, request):
        http_info = self._list_ecn_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ecn_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/enterprise-connect/enterprise-connect-network",
            "request_type": request.__class__.__name__,
            "response_type": "ListEcnResponse"
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
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'

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

    def list_ecn_with_ieg(self, request):
        """查询企业连接网络与智能企业网关绑定关系

        根据企业连接网络ID，查询企业连接网络与智能企业网关绑定关系
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEcnWithIeg
        :type request: :class:`huaweicloudsdkec.v1.ListEcnWithIegRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ListEcnWithIegResponse`
        """
        http_info = self._list_ecn_with_ieg_http_info(request)
        return self._call_api(**http_info)

    def list_ecn_with_ieg_invoker(self, request):
        http_info = self._list_ecn_with_ieg_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ecn_with_ieg_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/enterprise-connect/enterprise-connect-network/{ecn_id}/relationship/intelligent-enterprise-gateway",
            "request_type": request.__class__.__name__,
            "response_type": "ListEcnWithIegResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ecn_id' in local_var_params:
            path_params['ecn_id'] = local_var_params['ecn_id']

        query_params = []
        if 'ieg_id' in local_var_params:
            query_params.append(('ieg_id', local_var_params['ieg_id']))

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

    def show_ecn_info(self, request):
        """查询企业连接网络

        根据企业连接网络ID，查询企业连接网络
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEcnInfo
        :type request: :class:`huaweicloudsdkec.v1.ShowEcnInfoRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ShowEcnInfoResponse`
        """
        http_info = self._show_ecn_info_http_info(request)
        return self._call_api(**http_info)

    def show_ecn_info_invoker(self, request):
        http_info = self._show_ecn_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_ecn_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/enterprise-connect/enterprise-connect-network/{ecn_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEcnInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ecn_id' in local_var_params:
            path_params['ecn_id'] = local_var_params['ecn_id']

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

    def show_ecn_with_ieg(self, request):
        """查询企业连接网络与单个智能企业网关绑定关系

        查询企业连接网络与单个智能企业网关绑定关系
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEcnWithIeg
        :type request: :class:`huaweicloudsdkec.v1.ShowEcnWithIegRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ShowEcnWithIegResponse`
        """
        http_info = self._show_ecn_with_ieg_http_info(request)
        return self._call_api(**http_info)

    def show_ecn_with_ieg_invoker(self, request):
        http_info = self._show_ecn_with_ieg_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_ecn_with_ieg_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/enterprise-connect/enterprise-connect-network/{ecn_id}/relationship/intelligent-enterprise-gateway/{relation_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEcnWithIegResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ecn_id' in local_var_params:
            path_params['ecn_id'] = local_var_params['ecn_id']
        if 'relation_id' in local_var_params:
            path_params['relation_id'] = local_var_params['relation_id']

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

    def update_ecn(self, request):
        """更新企业连接网络

        根据企业连接网络ID，更新企业连接网络
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateEcn
        :type request: :class:`huaweicloudsdkec.v1.UpdateEcnRequest`
        :rtype: :class:`huaweicloudsdkec.v1.UpdateEcnResponse`
        """
        http_info = self._update_ecn_http_info(request)
        return self._call_api(**http_info)

    def update_ecn_invoker(self, request):
        http_info = self._update_ecn_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_ecn_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{domain_id}/enterprise-connect/enterprise-connect-network/{ecn_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEcnResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ecn_id' in local_var_params:
            path_params['ecn_id'] = local_var_params['ecn_id']

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

    def create_equipment(self, request):
        """激活智能企业网关设备

        激活智能企业网关设备
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEquipment
        :type request: :class:`huaweicloudsdkec.v1.CreateEquipmentRequest`
        :rtype: :class:`huaweicloudsdkec.v1.CreateEquipmentResponse`
        """
        http_info = self._create_equipment_http_info(request)
        return self._call_api(**http_info)

    def create_equipment_invoker(self, request):
        http_info = self._create_equipment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_equipment_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEquipmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']

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

    def delete_equipment(self, request):
        """移除智能企业网关设备

        移除智能企业网关设备
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEquipment
        :type request: :class:`huaweicloudsdkec.v1.DeleteEquipmentRequest`
        :rtype: :class:`huaweicloudsdkec.v1.DeleteEquipmentResponse`
        """
        http_info = self._delete_equipment_http_info(request)
        return self._call_api(**http_info)

    def delete_equipment_invoker(self, request):
        http_info = self._delete_equipment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_equipment_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEquipmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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

    def generate_initial_configuration(self, request):
        """生成智能企业网关设备初始配置

        生成智能企业网关设备初始配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GenerateInitialConfiguration
        :type request: :class:`huaweicloudsdkec.v1.GenerateInitialConfigurationRequest`
        :rtype: :class:`huaweicloudsdkec.v1.GenerateInitialConfigurationResponse`
        """
        http_info = self._generate_initial_configuration_http_info(request)
        return self._call_api(**http_info)

    def generate_initial_configuration_invoker(self, request):
        http_info = self._generate_initial_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _generate_initial_configuration_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/initial-configuration",
            "request_type": request.__class__.__name__,
            "response_type": "GenerateInitialConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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

    def list_equipments(self, request):
        """查询智能企业网关设备列表

        根据智能企业网关ID，查询智能企业网关设备列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEquipments
        :type request: :class:`huaweicloudsdkec.v1.ListEquipmentsRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ListEquipmentsResponse`
        """
        http_info = self._list_equipments_http_info(request)
        return self._call_api(**http_info)

    def list_equipments_invoker(self, request):
        http_info = self._list_equipments_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_equipments_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment",
            "request_type": request.__class__.__name__,
            "response_type": "ListEquipmentsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']

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

    def reboot_equipment(self, request):
        """重启智能企业网关设备

        重启智能企业网关设备
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RebootEquipment
        :type request: :class:`huaweicloudsdkec.v1.RebootEquipmentRequest`
        :rtype: :class:`huaweicloudsdkec.v1.RebootEquipmentResponse`
        """
        http_info = self._reboot_equipment_http_info(request)
        return self._call_api(**http_info)

    def reboot_equipment_invoker(self, request):
        http_info = self._reboot_equipment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reboot_equipment_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/reboot",
            "request_type": request.__class__.__name__,
            "response_type": "RebootEquipmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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

    def show_equipment_info(self, request):
        """查询智能企业网关设备

        查询智能企业网关设备
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEquipmentInfo
        :type request: :class:`huaweicloudsdkec.v1.ShowEquipmentInfoRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ShowEquipmentInfoResponse`
        """
        http_info = self._show_equipment_info_http_info(request)
        return self._call_api(**http_info)

    def show_equipment_info_invoker(self, request):
        http_info = self._show_equipment_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_equipment_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEquipmentInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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

    def show_equipment_specific_config(self, request):
        """查询智能企业网关设备基础规格配置

        查询智能企业网关设备基础规格配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEquipmentSpecificConfig
        :type request: :class:`huaweicloudsdkec.v1.ShowEquipmentSpecificConfigRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ShowEquipmentSpecificConfigResponse`
        """
        http_info = self._show_equipment_specific_config_http_info(request)
        return self._call_api(**http_info)

    def show_equipment_specific_config_invoker(self, request):
        http_info = self._show_equipment_specific_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_equipment_specific_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/enterprise-connect/equipment-specification/{equipment_type}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEquipmentSpecificConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'equipment_type' in local_var_params:
            path_params['equipment_type'] = local_var_params['equipment_type']

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

    def update_equipment_esn(self, request):
        """修改智能企业网关设备ESN

        修改智能企业网关设备ESN
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateEquipmentEsn
        :type request: :class:`huaweicloudsdkec.v1.UpdateEquipmentEsnRequest`
        :rtype: :class:`huaweicloudsdkec.v1.UpdateEquipmentEsnResponse`
        """
        http_info = self._update_equipment_esn_http_info(request)
        return self._call_api(**http_info)

    def update_equipment_esn_invoker(self, request):
        http_info = self._update_equipment_esn_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_equipment_esn_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/esn",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEquipmentEsnResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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

    def update_equipment_info(self, request):
        """更新智能企业网关设备

        更新智能企业网关设备
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateEquipmentInfo
        :type request: :class:`huaweicloudsdkec.v1.UpdateEquipmentInfoRequest`
        :rtype: :class:`huaweicloudsdkec.v1.UpdateEquipmentInfoResponse`
        """
        http_info = self._update_equipment_info_http_info(request)
        return self._call_api(**http_info)

    def update_equipment_info_invoker(self, request):
        http_info = self._update_equipment_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_equipment_info_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEquipmentInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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

    def create_equipment_lan_config(self, request):
        """创建智能企业网关设备LAN口配置

        创建智能企业网关设备LAN口配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEquipmentLanConfig
        :type request: :class:`huaweicloudsdkec.v1.CreateEquipmentLanConfigRequest`
        :rtype: :class:`huaweicloudsdkec.v1.CreateEquipmentLanConfigResponse`
        """
        http_info = self._create_equipment_lan_config_http_info(request)
        return self._call_api(**http_info)

    def create_equipment_lan_config_invoker(self, request):
        http_info = self._create_equipment_lan_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_equipment_lan_config_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/lan-interface",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEquipmentLanConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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

    def delete_equipment_lan_config(self, request):
        """删除智能企业网关设备LAN口配置

        删除智能企业网关设备LAN口配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEquipmentLanConfig
        :type request: :class:`huaweicloudsdkec.v1.DeleteEquipmentLanConfigRequest`
        :rtype: :class:`huaweicloudsdkec.v1.DeleteEquipmentLanConfigResponse`
        """
        http_info = self._delete_equipment_lan_config_http_info(request)
        return self._call_api(**http_info)

    def delete_equipment_lan_config_invoker(self, request):
        http_info = self._delete_equipment_lan_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_equipment_lan_config_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/lan-interface",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEquipmentLanConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

        query_params = []
        if 'interface_name' in local_var_params:
            query_params.append(('interface_name', local_var_params['interface_name']))
        if 'vlan_id' in local_var_params:
            query_params.append(('vlan_id', local_var_params['vlan_id']))

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

    def list_equipment_interface_name(self, request):
        """查询智能企业网关已配置的接口名字

        查询智能企业网关已配置的接口名字
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEquipmentInterfaceName
        :type request: :class:`huaweicloudsdkec.v1.ListEquipmentInterfaceNameRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ListEquipmentInterfaceNameResponse`
        """
        http_info = self._list_equipment_interface_name_http_info(request)
        return self._call_api(**http_info)

    def list_equipment_interface_name_invoker(self, request):
        http_info = self._list_equipment_interface_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_equipment_interface_name_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/interface-name",
            "request_type": request.__class__.__name__,
            "response_type": "ListEquipmentInterfaceNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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

    def show_equipment_dns_info(self, request):
        """查询智能企业网关设备主备DNS配置

        查询智能企业网关设备主备DNS配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEquipmentDnsInfo
        :type request: :class:`huaweicloudsdkec.v1.ShowEquipmentDnsInfoRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ShowEquipmentDnsInfoResponse`
        """
        http_info = self._show_equipment_dns_info_http_info(request)
        return self._call_api(**http_info)

    def show_equipment_dns_info_invoker(self, request):
        http_info = self._show_equipment_dns_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_equipment_dns_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/lan-interface/dns",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEquipmentDnsInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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

    def show_equipment_lan_info(self, request):
        """查询智能企业网关设备LAN口配置

        查询智能企业网关设备LAN口配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEquipmentLanInfo
        :type request: :class:`huaweicloudsdkec.v1.ShowEquipmentLanInfoRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ShowEquipmentLanInfoResponse`
        """
        http_info = self._show_equipment_lan_info_http_info(request)
        return self._call_api(**http_info)

    def show_equipment_lan_info_invoker(self, request):
        http_info = self._show_equipment_lan_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_equipment_lan_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/lan-interface",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEquipmentLanInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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

    def update_equipment_dns_info(self, request):
        """更新智能企业网关设备主备DNS配置

        更新智能企业网关设备主备DNS配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateEquipmentDnsInfo
        :type request: :class:`huaweicloudsdkec.v1.UpdateEquipmentDnsInfoRequest`
        :rtype: :class:`huaweicloudsdkec.v1.UpdateEquipmentDnsInfoResponse`
        """
        http_info = self._update_equipment_dns_info_http_info(request)
        return self._call_api(**http_info)

    def update_equipment_dns_info_invoker(self, request):
        http_info = self._update_equipment_dns_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_equipment_dns_info_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/lan-interface/dns",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEquipmentDnsInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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

    def update_equipment_lan_config(self, request):
        """更新智能企业网关设备LAN口配置

        更新智能企业网关设备LAN口配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateEquipmentLanConfig
        :type request: :class:`huaweicloudsdkec.v1.UpdateEquipmentLanConfigRequest`
        :rtype: :class:`huaweicloudsdkec.v1.UpdateEquipmentLanConfigResponse`
        """
        http_info = self._update_equipment_lan_config_http_info(request)
        return self._call_api(**http_info)

    def update_equipment_lan_config_invoker(self, request):
        http_info = self._update_equipment_lan_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_equipment_lan_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/lan-interface",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEquipmentLanConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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

    def show_equipment_ospf(self, request):
        """查询智能企业网关设备OSPF配置

        查询智能企业网关设备OSPF配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEquipmentOspf
        :type request: :class:`huaweicloudsdkec.v1.ShowEquipmentOspfRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ShowEquipmentOspfResponse`
        """
        http_info = self._show_equipment_ospf_http_info(request)
        return self._call_api(**http_info)

    def show_equipment_ospf_invoker(self, request):
        http_info = self._show_equipment_ospf_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_equipment_ospf_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/ospf",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEquipmentOspfResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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

    def update_equipment_ospf(self, request):
        """配置智能企业网关设备OSPF协议

        配置智能企业网关设备OSPF协议
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateEquipmentOspf
        :type request: :class:`huaweicloudsdkec.v1.UpdateEquipmentOspfRequest`
        :rtype: :class:`huaweicloudsdkec.v1.UpdateEquipmentOspfResponse`
        """
        http_info = self._update_equipment_ospf_http_info(request)
        return self._call_api(**http_info)

    def update_equipment_ospf_invoker(self, request):
        http_info = self._update_equipment_ospf_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_equipment_ospf_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/ospf",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEquipmentOspfResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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

    def create_equipment_static_route_config(self, request):
        """创建智能企业网关设备静态路由配置

        创建智能企业网关设备静态路由配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEquipmentStaticRouteConfig
        :type request: :class:`huaweicloudsdkec.v1.CreateEquipmentStaticRouteConfigRequest`
        :rtype: :class:`huaweicloudsdkec.v1.CreateEquipmentStaticRouteConfigResponse`
        """
        http_info = self._create_equipment_static_route_config_http_info(request)
        return self._call_api(**http_info)

    def create_equipment_static_route_config_invoker(self, request):
        http_info = self._create_equipment_static_route_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_equipment_static_route_config_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/static-route",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEquipmentStaticRouteConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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

    def delete_equipment_static_route_config(self, request):
        """删除智能企业网关设备静态路由配置

        删除智能企业网关设备静态路由配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEquipmentStaticRouteConfig
        :type request: :class:`huaweicloudsdkec.v1.DeleteEquipmentStaticRouteConfigRequest`
        :rtype: :class:`huaweicloudsdkec.v1.DeleteEquipmentStaticRouteConfigResponse`
        """
        http_info = self._delete_equipment_static_route_config_http_info(request)
        return self._call_api(**http_info)

    def delete_equipment_static_route_config_invoker(self, request):
        http_info = self._delete_equipment_static_route_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_equipment_static_route_config_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/static-route",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEquipmentStaticRouteConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

        query_params = []
        if 'prefix' in local_var_params:
            query_params.append(('prefix', local_var_params['prefix']))
        if 'next_hop' in local_var_params:
            query_params.append(('next_hop', local_var_params['next_hop']))
        if 'interface_name' in local_var_params:
            query_params.append(('interface_name', local_var_params['interface_name']))

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

    def show_equipment_static_route_info(self, request):
        """查询智能企业网关设备静态路由配置

        查询智能企业网关设备静态路由配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEquipmentStaticRouteInfo
        :type request: :class:`huaweicloudsdkec.v1.ShowEquipmentStaticRouteInfoRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ShowEquipmentStaticRouteInfoResponse`
        """
        http_info = self._show_equipment_static_route_info_http_info(request)
        return self._call_api(**http_info)

    def show_equipment_static_route_info_invoker(self, request):
        http_info = self._show_equipment_static_route_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_equipment_static_route_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/static-route",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEquipmentStaticRouteInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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

    def update_equipment_static_route_config(self, request):
        """更新智能企业网关设备静态路由配置

        更新智能企业网关设备静态路由配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateEquipmentStaticRouteConfig
        :type request: :class:`huaweicloudsdkec.v1.UpdateEquipmentStaticRouteConfigRequest`
        :rtype: :class:`huaweicloudsdkec.v1.UpdateEquipmentStaticRouteConfigResponse`
        """
        http_info = self._update_equipment_static_route_config_http_info(request)
        return self._call_api(**http_info)

    def update_equipment_static_route_config_invoker(self, request):
        http_info = self._update_equipment_static_route_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_equipment_static_route_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/static-route",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEquipmentStaticRouteConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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

    def show_equipment_wan_info(self, request):
        """查询智能企业网关设备WAN口配置

        查询智能企业网关设备WAN口配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEquipmentWanInfo
        :type request: :class:`huaweicloudsdkec.v1.ShowEquipmentWanInfoRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ShowEquipmentWanInfoResponse`
        """
        http_info = self._show_equipment_wan_info_http_info(request)
        return self._call_api(**http_info)

    def show_equipment_wan_info_invoker(self, request):
        http_info = self._show_equipment_wan_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_equipment_wan_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/wan-interface",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEquipmentWanInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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

    def update_equipment_wan_config(self, request):
        """更新智能企业网关设备WAN口配置

        更新智能企业网关设备WAN口配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateEquipmentWanConfig
        :type request: :class:`huaweicloudsdkec.v1.UpdateEquipmentWanConfigRequest`
        :rtype: :class:`huaweicloudsdkec.v1.UpdateEquipmentWanConfigResponse`
        """
        http_info = self._update_equipment_wan_config_http_info(request)
        return self._call_api(**http_info)

    def update_equipment_wan_config_invoker(self, request):
        http_info = self._update_equipment_wan_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_equipment_wan_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/wan-interface",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEquipmentWanConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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

    def add_ecn_with_er(self, request):
        """关联企业路由器到企业连接网络

        关联企业路由器到企业连接网络
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddEcnWithEr
        :type request: :class:`huaweicloudsdkec.v1.AddEcnWithErRequest`
        :rtype: :class:`huaweicloudsdkec.v1.AddEcnWithErResponse`
        """
        http_info = self._add_ecn_with_er_http_info(request)
        return self._call_api(**http_info)

    def add_ecn_with_er_invoker(self, request):
        http_info = self._add_ecn_with_er_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_ecn_with_er_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/enterprise-connect/enterprise-connect-network/{ecn_id}/relationship/enterprise-router",
            "request_type": request.__class__.__name__,
            "response_type": "AddEcnWithErResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ecn_id' in local_var_params:
            path_params['ecn_id'] = local_var_params['ecn_id']

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

    def delete_ecn_with_er(self, request):
        """解除企业路由器和企业连接网络的关联

        解除企业路由器和企业连接网络的关联
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEcnWithEr
        :type request: :class:`huaweicloudsdkec.v1.DeleteEcnWithErRequest`
        :rtype: :class:`huaweicloudsdkec.v1.DeleteEcnWithErResponse`
        """
        http_info = self._delete_ecn_with_er_http_info(request)
        return self._call_api(**http_info)

    def delete_ecn_with_er_invoker(self, request):
        http_info = self._delete_ecn_with_er_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_ecn_with_er_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{domain_id}/enterprise-connect/enterprise-connect-network/{ecn_id}/relationship/enterprise-router/{relation_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEcnWithErResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ecn_id' in local_var_params:
            path_params['ecn_id'] = local_var_params['ecn_id']
        if 'relation_id' in local_var_params:
            path_params['relation_id'] = local_var_params['relation_id']

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

    def list_ecn_with_er(self, request):
        """查询企业连接网络网与企业路由器关联关系

        根据企业连接网络ID，查询企业连接网络网与企业路由器关联关系
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEcnWithEr
        :type request: :class:`huaweicloudsdkec.v1.ListEcnWithErRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ListEcnWithErResponse`
        """
        http_info = self._list_ecn_with_er_http_info(request)
        return self._call_api(**http_info)

    def list_ecn_with_er_invoker(self, request):
        http_info = self._list_ecn_with_er_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ecn_with_er_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/enterprise-connect/enterprise-connect-network/{ecn_id}/relationship/enterprise-router",
            "request_type": request.__class__.__name__,
            "response_type": "ListEcnWithErResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ecn_id' in local_var_params:
            path_params['ecn_id'] = local_var_params['ecn_id']

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

    def change_ieg_password(self, request):
        """修改IEG设备admin账户密码

        修改IEG设备admin账户密码
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeIegPassword
        :type request: :class:`huaweicloudsdkec.v1.ChangeIegPasswordRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ChangeIegPasswordResponse`
        """
        http_info = self._change_ieg_password_http_info(request)
        return self._call_api(**http_info)

    def change_ieg_password_invoker(self, request):
        http_info = self._change_ieg_password_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_ieg_password_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/password",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeIegPasswordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']

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

    def list_ieg(self, request):
        """查询租户智能企业网关列表

        查询租户智能企业网关列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIeg
        :type request: :class:`huaweicloudsdkec.v1.ListIegRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ListIegResponse`
        """
        http_info = self._list_ieg_http_info(request)
        return self._call_api(**http_info)

    def list_ieg_invoker(self, request):
        http_info = self._list_ieg_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ieg_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway",
            "request_type": request.__class__.__name__,
            "response_type": "ListIegResponse"
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
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'

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

    def show_ieg_info(self, request):
        """查询租户单个智能企业网关

        根据智能企业网关ID，查询租户智能企业网关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIegInfo
        :type request: :class:`huaweicloudsdkec.v1.ShowIegInfoRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ShowIegInfoResponse`
        """
        http_info = self._show_ieg_info_http_info(request)
        return self._call_api(**http_info)

    def show_ieg_info_invoker(self, request):
        http_info = self._show_ieg_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_ieg_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIegInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']

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

    def switch_equipment_ha_type(self, request):
        """交换双机主备属性

        交换双机主备属性
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchEquipmentHaType
        :type request: :class:`huaweicloudsdkec.v1.SwitchEquipmentHaTypeRequest`
        :rtype: :class:`huaweicloudsdkec.v1.SwitchEquipmentHaTypeResponse`
        """
        http_info = self._switch_equipment_ha_type_http_info(request)
        return self._call_api(**http_info)

    def switch_equipment_ha_type_invoker(self, request):
        http_info = self._switch_equipment_ha_type_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_equipment_ha_type_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/switch-ha-type",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchEquipmentHaTypeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']

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

    def update_ieg(self, request):
        """更新智能企业网关

        根据智能企业网关ID，更新智能企业网关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateIeg
        :type request: :class:`huaweicloudsdkec.v1.UpdateIegRequest`
        :rtype: :class:`huaweicloudsdkec.v1.UpdateIegResponse`
        """
        http_info = self._update_ieg_http_info(request)
        return self._call_api(**http_info)

    def update_ieg_invoker(self, request):
        http_info = self._update_ieg_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_ieg_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateIegResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']

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

    def show_quotas_info(self, request):
        """查询EC相关的指定租户的配额

        查询EC相关的指定租户的配额
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowQuotasInfo
        :type request: :class:`huaweicloudsdkec.v1.ShowQuotasInfoRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ShowQuotasInfoResponse`
        """
        http_info = self._show_quotas_info_http_info(request)
        return self._call_api(**http_info)

    def show_quotas_info_invoker(self, request):
        http_info = self._show_quotas_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_quotas_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/enterprise-connect/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowQuotasInfoResponse"
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

    def add_vrrp_config(self, request):
        """创建vrrp配置

        创建vrrp配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddVrrpConfig
        :type request: :class:`huaweicloudsdkec.v1.AddVrrpConfigRequest`
        :rtype: :class:`huaweicloudsdkec.v1.AddVrrpConfigResponse`
        """
        http_info = self._add_vrrp_config_http_info(request)
        return self._call_api(**http_info)

    def add_vrrp_config_invoker(self, request):
        http_info = self._add_vrrp_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_vrrp_config_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/vrrp-config",
            "request_type": request.__class__.__name__,
            "response_type": "AddVrrpConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']

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

    def delete_vrrp_config(self, request):
        """删除vrrp配置

        删除vrrp配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteVrrpConfig
        :type request: :class:`huaweicloudsdkec.v1.DeleteVrrpConfigRequest`
        :rtype: :class:`huaweicloudsdkec.v1.DeleteVrrpConfigResponse`
        """
        http_info = self._delete_vrrp_config_http_info(request)
        return self._call_api(**http_info)

    def delete_vrrp_config_invoker(self, request):
        http_info = self._delete_vrrp_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_vrrp_config_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/vrrp-config/{virtual_router_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVrrpConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'virtual_router_id' in local_var_params:
            path_params['virtual_router_id'] = local_var_params['virtual_router_id']

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

    def show_vrrp_config(self, request):
        """查询vrrp配置列表

        查询vrrp配置列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVrrpConfig
        :type request: :class:`huaweicloudsdkec.v1.ShowVrrpConfigRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ShowVrrpConfigResponse`
        """
        http_info = self._show_vrrp_config_http_info(request)
        return self._call_api(**http_info)

    def show_vrrp_config_invoker(self, request):
        http_info = self._show_vrrp_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_vrrp_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/vrrp-config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVrrpConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']

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

    def update_vrrp_config(self, request):
        """更新vrrp配置

        更新vrrp配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateVrrpConfig
        :type request: :class:`huaweicloudsdkec.v1.UpdateVrrpConfigRequest`
        :rtype: :class:`huaweicloudsdkec.v1.UpdateVrrpConfigResponse`
        """
        http_info = self._update_vrrp_config_http_info(request)
        return self._call_api(**http_info)

    def update_vrrp_config_invoker(self, request):
        http_info = self._update_vrrp_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_vrrp_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/vrrp-config/{virtual_router_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateVrrpConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'virtual_router_id' in local_var_params:
            path_params['virtual_router_id'] = local_var_params['virtual_router_id']

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
