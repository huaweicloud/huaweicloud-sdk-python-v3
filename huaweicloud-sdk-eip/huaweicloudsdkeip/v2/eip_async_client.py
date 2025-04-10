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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkeip'")


class EipAsyncClient(Client):
    def __init__(self):
        super(EipAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkeip.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "EipAsyncClient":
                raise TypeError("client type error, support client type is EipAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_publicips_into_shared_bandwidth_async(self, request):
        r"""共享带宽插入弹性公网IP

        共享带宽插入弹性公网IP。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddPublicipsIntoSharedBandwidth
        :type request: :class:`huaweicloudsdkeip.v2.AddPublicipsIntoSharedBandwidthRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.AddPublicipsIntoSharedBandwidthResponse`
        """
        http_info = self._add_publicips_into_shared_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def add_publicips_into_shared_bandwidth_async_invoker(self, request):
        http_info = self._add_publicips_into_shared_bandwidth_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_publicips_into_shared_bandwidth_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/bandwidths/{bandwidth_id}/insert",
            "request_type": request.__class__.__name__,
            "response_type": "AddPublicipsIntoSharedBandwidthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'bandwidth_id' in local_var_params:
            path_params['bandwidth_id'] = local_var_params['bandwidth_id']

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

    def batch_create_shared_bandwidths_async(self, request):
        r"""批量创建共享带宽

        批量创建共享带宽。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateSharedBandwidths
        :type request: :class:`huaweicloudsdkeip.v2.BatchCreateSharedBandwidthsRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.BatchCreateSharedBandwidthsResponse`
        """
        http_info = self._batch_create_shared_bandwidths_http_info(request)
        return self._call_api(**http_info)

    def batch_create_shared_bandwidths_async_invoker(self, request):
        http_info = self._batch_create_shared_bandwidths_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_shared_bandwidths_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/batch-bandwidths",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateSharedBandwidthsResponse"
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

    def batch_modify_bandwidth_async(self, request):
        r"""批量更新带宽

        批量更新带宽，共享带宽和包周期带宽该接口不适用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchModifyBandwidth
        :type request: :class:`huaweicloudsdkeip.v2.BatchModifyBandwidthRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.BatchModifyBandwidthResponse`
        """
        http_info = self._batch_modify_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def batch_modify_bandwidth_async_invoker(self, request):
        http_info = self._batch_modify_bandwidth_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_modify_bandwidth_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/batch-bandwidths/modify",
            "request_type": request.__class__.__name__,
            "response_type": "BatchModifyBandwidthResponse"
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

    def change_bandwidth_to_period_async(self, request):
        r"""按需转包API

        租户按需转包接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeBandwidthToPeriod
        :type request: :class:`huaweicloudsdkeip.v2.ChangeBandwidthToPeriodRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.ChangeBandwidthToPeriodResponse`
        """
        http_info = self._change_bandwidth_to_period_http_info(request)
        return self._call_api(**http_info)

    def change_bandwidth_to_period_async_invoker(self, request):
        http_info = self._change_bandwidth_to_period_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_bandwidth_to_period_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/bandwidths/change-to-period",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeBandwidthToPeriodResponse"
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

    def create_shared_bandwidth_async(self, request):
        r"""创建共享带宽

        创建共享带宽。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSharedBandwidth
        :type request: :class:`huaweicloudsdkeip.v2.CreateSharedBandwidthRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.CreateSharedBandwidthResponse`
        """
        http_info = self._create_shared_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def create_shared_bandwidth_async_invoker(self, request):
        http_info = self._create_shared_bandwidth_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_shared_bandwidth_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/bandwidths",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSharedBandwidthResponse"
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

    def delete_shared_bandwidth_async(self, request):
        r"""删除共享带宽

        删除共享带宽。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSharedBandwidth
        :type request: :class:`huaweicloudsdkeip.v2.DeleteSharedBandwidthRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.DeleteSharedBandwidthResponse`
        """
        http_info = self._delete_shared_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def delete_shared_bandwidth_async_invoker(self, request):
        http_info = self._delete_shared_bandwidth_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_shared_bandwidth_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/{project_id}/bandwidths/{bandwidth_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSharedBandwidthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'bandwidth_id' in local_var_params:
            path_params['bandwidth_id'] = local_var_params['bandwidth_id']

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

    def list_bandwidth_pkg_async(self, request):
        r"""查询带宽加油包列表

        查询带宽加油包列表信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBandwidthPkg
        :type request: :class:`huaweicloudsdkeip.v2.ListBandwidthPkgRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.ListBandwidthPkgResponse`
        """
        http_info = self._list_bandwidth_pkg_http_info(request)
        return self._call_api(**http_info)

    def list_bandwidth_pkg_async_invoker(self, request):
        http_info = self._list_bandwidth_pkg_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_bandwidth_pkg_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/bandwidthpkgs",
            "request_type": request.__class__.__name__,
            "response_type": "ListBandwidthPkgResponse"
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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

    def list_bandwidths_async(self, request):
        r"""查询带宽列表

        查询带宽列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBandwidths
        :type request: :class:`huaweicloudsdkeip.v2.ListBandwidthsRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.ListBandwidthsResponse`
        """
        http_info = self._list_bandwidths_http_info(request)
        return self._call_api(**http_info)

    def list_bandwidths_async_invoker(self, request):
        http_info = self._list_bandwidths_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_bandwidths_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/bandwidths",
            "request_type": request.__class__.__name__,
            "response_type": "ListBandwidthsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'share_type' in local_var_params:
            query_params.append(('share_type', local_var_params['share_type']))

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

    def list_quotas_async(self, request):
        r"""查询配额接口

        查询配额
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListQuotas
        :type request: :class:`huaweicloudsdkeip.v2.ListQuotasRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.ListQuotasResponse`
        """
        http_info = self._list_quotas_http_info(request)
        return self._call_api(**http_info)

    def list_quotas_async_invoker(self, request):
        http_info = self._list_quotas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_quotas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ListQuotasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

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

    def remove_publicips_from_shared_bandwidth_async(self, request):
        r"""共享带宽移除弹性公网IP

        共享带宽移除弹性公网IP。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RemovePublicipsFromSharedBandwidth
        :type request: :class:`huaweicloudsdkeip.v2.RemovePublicipsFromSharedBandwidthRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.RemovePublicipsFromSharedBandwidthResponse`
        """
        http_info = self._remove_publicips_from_shared_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def remove_publicips_from_shared_bandwidth_async_invoker(self, request):
        http_info = self._remove_publicips_from_shared_bandwidth_http_info(request)
        return AsyncInvoker(self, http_info)

    def _remove_publicips_from_shared_bandwidth_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/bandwidths/{bandwidth_id}/remove",
            "request_type": request.__class__.__name__,
            "response_type": "RemovePublicipsFromSharedBandwidthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'bandwidth_id' in local_var_params:
            path_params['bandwidth_id'] = local_var_params['bandwidth_id']

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

    def show_bandwidth_async(self, request):
        r"""查询带宽

        查询带宽
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBandwidth
        :type request: :class:`huaweicloudsdkeip.v2.ShowBandwidthRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.ShowBandwidthResponse`
        """
        http_info = self._show_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def show_bandwidth_async_invoker(self, request):
        http_info = self._show_bandwidth_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_bandwidth_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/bandwidths/{bandwidth_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBandwidthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'bandwidth_id' in local_var_params:
            path_params['bandwidth_id'] = local_var_params['bandwidth_id']

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

    def update_bandwidth_async(self, request):
        r"""更新带宽

        更新带宽。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateBandwidth
        :type request: :class:`huaweicloudsdkeip.v2.UpdateBandwidthRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.UpdateBandwidthResponse`
        """
        http_info = self._update_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def update_bandwidth_async_invoker(self, request):
        http_info = self._update_bandwidth_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_bandwidth_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/bandwidths/{bandwidth_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateBandwidthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'bandwidth_id' in local_var_params:
            path_params['bandwidth_id'] = local_var_params['bandwidth_id']

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

    def update_pre_paid_bandwidth_async(self, request):
        r"""更新包周期带宽

        更新带宽。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePrePaidBandwidth
        :type request: :class:`huaweicloudsdkeip.v2.UpdatePrePaidBandwidthRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.UpdatePrePaidBandwidthResponse`
        """
        http_info = self._update_pre_paid_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def update_pre_paid_bandwidth_async_invoker(self, request):
        http_info = self._update_pre_paid_bandwidth_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_pre_paid_bandwidth_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.0/{project_id}/bandwidths/{bandwidth_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePrePaidBandwidthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'bandwidth_id' in local_var_params:
            path_params['bandwidth_id'] = local_var_params['bandwidth_id']

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

    def batch_create_publicip_tags_async(self, request):
        r"""批量创建弹性公网IP资源标签

        为指定的弹性公网IP资源实例批量添加标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreatePublicipTags
        :type request: :class:`huaweicloudsdkeip.v2.BatchCreatePublicipTagsRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.BatchCreatePublicipTagsResponse`
        """
        http_info = self._batch_create_publicip_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_publicip_tags_async_invoker(self, request):
        http_info = self._batch_create_publicip_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_publicip_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/publicips/{publicip_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreatePublicipTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']

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

    def batch_create_publicips_async(self, request):
        r"""批量创建弹性公网IP

        批量创建弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreatePublicips
        :type request: :class:`huaweicloudsdkeip.v2.BatchCreatePublicipsRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.BatchCreatePublicipsResponse`
        """
        http_info = self._batch_create_publicips_http_info(request)
        return self._call_api(**http_info)

    def batch_create_publicips_async_invoker(self, request):
        http_info = self._batch_create_publicips_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_publicips_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/batchpublicips",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreatePublicipsResponse"
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

    def batch_delete_public_ip_async(self, request):
        r"""批量删除弹性公网IP

        批量删除弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeletePublicIp
        :type request: :class:`huaweicloudsdkeip.v2.BatchDeletePublicIpRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.BatchDeletePublicIpResponse`
        """
        http_info = self._batch_delete_public_ip_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_public_ip_async_invoker(self, request):
        http_info = self._batch_delete_public_ip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_public_ip_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/batchpublicips",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeletePublicIpResponse"
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

    def batch_delete_publicip_tags_async(self, request):
        r"""批量删除弹性公网IP资源标签

        为指定的弹性公网IP资源实例批量删除标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeletePublicipTags
        :type request: :class:`huaweicloudsdkeip.v2.BatchDeletePublicipTagsRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.BatchDeletePublicipTagsResponse`
        """
        http_info = self._batch_delete_publicip_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_publicip_tags_async_invoker(self, request):
        http_info = self._batch_delete_publicip_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_publicip_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/publicips/{publicip_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeletePublicipTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']

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

    def batch_disassociate_publicips_async(self, request):
        r"""批量解绑弹性公网IP

        批量解绑弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDisassociatePublicips
        :type request: :class:`huaweicloudsdkeip.v2.BatchDisassociatePublicipsRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.BatchDisassociatePublicipsResponse`
        """
        http_info = self._batch_disassociate_publicips_http_info(request)
        return self._call_api(**http_info)

    def batch_disassociate_publicips_async_invoker(self, request):
        http_info = self._batch_disassociate_publicips_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_disassociate_publicips_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v2/{project_id}/batchpublicips",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDisassociatePublicipsResponse"
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

    def change_publicip_to_period_async(self, request):
        r"""按需转包接口

        租户按需转包接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangePublicipToPeriod
        :type request: :class:`huaweicloudsdkeip.v2.ChangePublicipToPeriodRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.ChangePublicipToPeriodResponse`
        """
        http_info = self._change_publicip_to_period_http_info(request)
        return self._call_api(**http_info)

    def change_publicip_to_period_async_invoker(self, request):
        http_info = self._change_publicip_to_period_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_publicip_to_period_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/publicips/change-to-period",
            "request_type": request.__class__.__name__,
            "response_type": "ChangePublicipToPeriodResponse"
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

    def count_public_ip_async(self, request):
        r"""查询PublicIp数量

        查询PublicIp数量
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CountPublicIp
        :type request: :class:`huaweicloudsdkeip.v2.CountPublicIpRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.CountPublicIpResponse`
        """
        http_info = self._count_public_ip_http_info(request)
        return self._call_api(**http_info)

    def count_public_ip_async_invoker(self, request):
        http_info = self._count_public_ip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _count_public_ip_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/elasticips",
            "request_type": request.__class__.__name__,
            "response_type": "CountPublicIpResponse"
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

    def count_public_ip_instance_async(self, request):
        r"""查询PublicIp实例数

        查询PublicIp实例数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CountPublicIpInstance
        :type request: :class:`huaweicloudsdkeip.v2.CountPublicIpInstanceRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.CountPublicIpInstanceResponse`
        """
        http_info = self._count_public_ip_instance_http_info(request)
        return self._call_api(**http_info)

    def count_public_ip_instance_async_invoker(self, request):
        http_info = self._count_public_ip_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _count_public_ip_instance_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/publicip/instances",
            "request_type": request.__class__.__name__,
            "response_type": "CountPublicIpInstanceResponse"
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

    def create_pre_paid_publicip_async(self, request):
        r"""申请包周期弹性公网IP

        申请包年包月的弹性公网IP。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePrePaidPublicip
        :type request: :class:`huaweicloudsdkeip.v2.CreatePrePaidPublicipRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.CreatePrePaidPublicipResponse`
        """
        http_info = self._create_pre_paid_publicip_http_info(request)
        return self._call_api(**http_info)

    def create_pre_paid_publicip_async_invoker(self, request):
        http_info = self._create_pre_paid_publicip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_pre_paid_publicip_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/publicips",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePrePaidPublicipResponse"
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

    def create_publicip_async(self, request):
        r"""申请弹性公网IP

        申请弹性公网IP，支持IPv4和IPv6。
         弹性公网IP（Elastic IP）提供独立的公网IP资源，包括公网IP地址与公网出口带宽服务。可以与弹性云服务器、裸金属服务器、虚拟IP、弹性负载均衡、NAT网关等资源灵活地绑定及解绑。拥有多种灵活的计费方式，可以满足各种业务场景的需要。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePublicip
        :type request: :class:`huaweicloudsdkeip.v2.CreatePublicipRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.CreatePublicipResponse`
        """
        http_info = self._create_publicip_http_info(request)
        return self._call_api(**http_info)

    def create_publicip_async_invoker(self, request):
        http_info = self._create_publicip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_publicip_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/publicips",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePublicipResponse"
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

    def create_publicip_tag_async(self, request):
        r"""创建弹性公网IP资源标签

        给指定弹性IP资源实例增加标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePublicipTag
        :type request: :class:`huaweicloudsdkeip.v2.CreatePublicipTagRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.CreatePublicipTagResponse`
        """
        http_info = self._create_publicip_tag_http_info(request)
        return self._call_api(**http_info)

    def create_publicip_tag_async_invoker(self, request):
        http_info = self._create_publicip_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_publicip_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/publicips/{publicip_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePublicipTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']

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

    def delete_publicip_async(self, request):
        r"""删除弹性公网IP

        删除弹性公网IP,绑定状态eip不允许直接删除。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePublicip
        :type request: :class:`huaweicloudsdkeip.v2.DeletePublicipRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.DeletePublicipResponse`
        """
        http_info = self._delete_publicip_http_info(request)
        return self._call_api(**http_info)

    def delete_publicip_async_invoker(self, request):
        http_info = self._delete_publicip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_publicip_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/publicips/{publicip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePublicipResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']

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

    def delete_publicip_tag_async(self, request):
        r"""删除弹性公网IP的标签

        删除指定弹性公网IP的标签信息。其中project_id是项目ID，publicip_id 是要操作的弹性公网IP的id。key是要删除标签的键。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePublicipTag
        :type request: :class:`huaweicloudsdkeip.v2.DeletePublicipTagRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.DeletePublicipTagResponse`
        """
        http_info = self._delete_publicip_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_publicip_tag_async_invoker(self, request):
        http_info = self._delete_publicip_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_publicip_tag_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/{project_id}/publicips/{publicip_id}/tags/{key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePublicipTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']

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

    def list_publicip_tags_async(self, request):
        r"""查询租户的弹性公网IP标签

        查询租户在指定区域和实例类型的所有标签集合。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPublicipTags
        :type request: :class:`huaweicloudsdkeip.v2.ListPublicipTagsRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.ListPublicipTagsResponse`
        """
        http_info = self._list_publicip_tags_http_info(request)
        return self._call_api(**http_info)

    def list_publicip_tags_async_invoker(self, request):
        http_info = self._list_publicip_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_publicip_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/publicips/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListPublicipTagsResponse"
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

    def list_publicips_async(self, request):
        r"""查询弹性公网IP列表

        查询弹性公网IP列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPublicips
        :type request: :class:`huaweicloudsdkeip.v2.ListPublicipsRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.ListPublicipsResponse`
        """
        http_info = self._list_publicips_http_info(request)
        return self._call_api(**http_info)

    def list_publicips_async_invoker(self, request):
        http_info = self._list_publicips_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_publicips_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/publicips",
            "request_type": request.__class__.__name__,
            "response_type": "ListPublicipsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'ip_version' in local_var_params:
            query_params.append(('ip_version', local_var_params['ip_version']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'port_id' in local_var_params:
            query_params.append(('port_id', local_var_params['port_id']))
            collection_formats['port_id'] = 'multi'
        if 'public_ip_address' in local_var_params:
            query_params.append(('public_ip_address', local_var_params['public_ip_address']))
            collection_formats['public_ip_address'] = 'multi'
        if 'private_ip_address' in local_var_params:
            query_params.append(('private_ip_address', local_var_params['private_ip_address']))
            collection_formats['private_ip_address'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'allow_share_bandwidth_type_any' in local_var_params:
            query_params.append(('allow_share_bandwidth_type_any', local_var_params['allow_share_bandwidth_type_any']))
            collection_formats['allow_share_bandwidth_type_any'] = 'multi'

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

    def list_publicips_by_tags_async(self, request):
        r"""按标签查询弹性公网IP列表

        使用标签过滤弹性公网IP。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPublicipsByTags
        :type request: :class:`huaweicloudsdkeip.v2.ListPublicipsByTagsRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.ListPublicipsByTagsResponse`
        """
        http_info = self._list_publicips_by_tags_http_info(request)
        return self._call_api(**http_info)

    def list_publicips_by_tags_async_invoker(self, request):
        http_info = self._list_publicips_by_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_publicips_by_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/publicips/resource_instances/action",
            "request_type": request.__class__.__name__,
            "response_type": "ListPublicipsByTagsResponse"
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

    def show_public_ip_type_async(self, request):
        r"""查询PublicIp类型

        查询PublicIp类型
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPublicIpType
        :type request: :class:`huaweicloudsdkeip.v2.ShowPublicIpTypeRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.ShowPublicIpTypeResponse`
        """
        http_info = self._show_public_ip_type_http_info(request)
        return self._call_api(**http_info)

    def show_public_ip_type_async_invoker(self, request):
        http_info = self._show_public_ip_type_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_public_ip_type_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/publicip_types",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPublicIpTypeResponse"
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

    def show_publicip_async(self, request):
        r"""查询弹性公网IP

        查询指定的弹性公网IP。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPublicip
        :type request: :class:`huaweicloudsdkeip.v2.ShowPublicipRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.ShowPublicipResponse`
        """
        http_info = self._show_publicip_http_info(request)
        return self._call_api(**http_info)

    def show_publicip_async_invoker(self, request):
        http_info = self._show_publicip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_publicip_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/publicips/{publicip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPublicipResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']

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

    def show_publicip_tags_async(self, request):
        r"""查询弹性公网IP的标签

        查询指定弹性IP实例的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPublicipTags
        :type request: :class:`huaweicloudsdkeip.v2.ShowPublicipTagsRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.ShowPublicipTagsResponse`
        """
        http_info = self._show_publicip_tags_http_info(request)
        return self._call_api(**http_info)

    def show_publicip_tags_async_invoker(self, request):
        http_info = self._show_publicip_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_publicip_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/publicips/{publicip_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPublicipTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']

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

    def update_publicip_async(self, request):
        r"""更新弹性公网IP

        更新弹性公网IP，将弹性公网IP跟一个网卡绑定或者解绑定，转换IP地址版本类型。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePublicip
        :type request: :class:`huaweicloudsdkeip.v2.UpdatePublicipRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.UpdatePublicipResponse`
        """
        http_info = self._update_publicip_http_info(request)
        return self._call_api(**http_info)

    def update_publicip_async_invoker(self, request):
        http_info = self._update_publicip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_publicip_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/publicips/{publicip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePublicipResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']

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

    def show_resources_job_detail_async(self, request):
        r"""查询Job状态接口

        查询Job状态接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourcesJobDetail
        :type request: :class:`huaweicloudsdkeip.v2.ShowResourcesJobDetailRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.ShowResourcesJobDetailResponse`
        """
        http_info = self._show_resources_job_detail_http_info(request)
        return self._call_api(**http_info)

    def show_resources_job_detail_async_invoker(self, request):
        http_info = self._show_resources_job_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_resources_job_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourcesJobDetailResponse"
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

    def neutron_create_floating_ip_async(self, request):
        r"""创建浮动IP

        创建浮动IP的外部网络UUID，请使用GET /v2.0/networks?router:external&#x3D;True或neutron net-external-list方式获取。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronCreateFloatingIp
        :type request: :class:`huaweicloudsdkeip.v2.NeutronCreateFloatingIpRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.NeutronCreateFloatingIpResponse`
        """
        http_info = self._neutron_create_floating_ip_http_info(request)
        return self._call_api(**http_info)

    def neutron_create_floating_ip_async_invoker(self, request):
        http_info = self._neutron_create_floating_ip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _neutron_create_floating_ip_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/floatingips",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronCreateFloatingIpResponse"
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

    def neutron_delete_floating_ip_async(self, request):
        r"""删除浮动IP

        删除指定的浮动IP。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronDeleteFloatingIp
        :type request: :class:`huaweicloudsdkeip.v2.NeutronDeleteFloatingIpRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.NeutronDeleteFloatingIpResponse`
        """
        http_info = self._neutron_delete_floating_ip_http_info(request)
        return self._call_api(**http_info)

    def neutron_delete_floating_ip_async_invoker(self, request):
        http_info = self._neutron_delete_floating_ip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _neutron_delete_floating_ip_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/floatingips/{floatingip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronDeleteFloatingIpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'floatingip_id' in local_var_params:
            path_params['floatingip_id'] = local_var_params['floatingip_id']

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

    def neutron_list_floating_ips_async(self, request):
        r"""查询浮动IP列表

        查询提交请求的租户有权限操作的所有浮动IP地址。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronListFloatingIps
        :type request: :class:`huaweicloudsdkeip.v2.NeutronListFloatingIpsRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.NeutronListFloatingIpsResponse`
        """
        http_info = self._neutron_list_floating_ips_http_info(request)
        return self._call_api(**http_info)

    def neutron_list_floating_ips_async_invoker(self, request):
        http_info = self._neutron_list_floating_ips_http_info(request)
        return AsyncInvoker(self, http_info)

    def _neutron_list_floating_ips_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/floatingips",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronListFloatingIpsResponse"
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
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'floating_ip_address' in local_var_params:
            query_params.append(('floating_ip_address', local_var_params['floating_ip_address']))
        if 'router_id' in local_var_params:
            query_params.append(('router_id', local_var_params['router_id']))
        if 'port_id' in local_var_params:
            query_params.append(('port_id', local_var_params['port_id']))
        if 'fixed_ip_address' in local_var_params:
            query_params.append(('fixed_ip_address', local_var_params['fixed_ip_address']))
        if 'tenant_id' in local_var_params:
            query_params.append(('tenant_id', local_var_params['tenant_id']))
        if 'floating_network_id' in local_var_params:
            query_params.append(('floating_network_id', local_var_params['floating_network_id']))

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

    def neutron_show_floating_ip_async(self, request):
        r"""查询浮动IP

        查询浮动IP详情，包括浮动IP状态，浮动IP所属路由器ID，浮动IP的外部网络ID等等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronShowFloatingIp
        :type request: :class:`huaweicloudsdkeip.v2.NeutronShowFloatingIpRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.NeutronShowFloatingIpResponse`
        """
        http_info = self._neutron_show_floating_ip_http_info(request)
        return self._call_api(**http_info)

    def neutron_show_floating_ip_async_invoker(self, request):
        http_info = self._neutron_show_floating_ip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _neutron_show_floating_ip_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/floatingips/{floatingip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronShowFloatingIpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'floatingip_id' in local_var_params:
            path_params['floatingip_id'] = local_var_params['floatingip_id']

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

    def neutron_update_floating_ip_async(self, request):
        r"""更新浮动IP

        更新浮动IP。
         更新时需在URL中给出浮动IP地址的ID。
         port_id 为空，则表示浮动IP从端口解绑。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronUpdateFloatingIp
        :type request: :class:`huaweicloudsdkeip.v2.NeutronUpdateFloatingIpRequest`
        :rtype: :class:`huaweicloudsdkeip.v2.NeutronUpdateFloatingIpResponse`
        """
        http_info = self._neutron_update_floating_ip_http_info(request)
        return self._call_api(**http_info)

    def neutron_update_floating_ip_async_invoker(self, request):
        http_info = self._neutron_update_floating_ip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _neutron_update_floating_ip_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.0/floatingips/{floatingip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronUpdateFloatingIpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'floatingip_id' in local_var_params:
            path_params['floatingip_id'] = local_var_params['floatingip_id']

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
