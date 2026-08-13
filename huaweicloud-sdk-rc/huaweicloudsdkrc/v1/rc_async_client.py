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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkrc'")


class RcAsyncClient(Client):
    def __init__(self):
        super().__init__()
        self.model_package = importlib.import_module("huaweicloudsdkrc.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials")
        else:
            if clazz.__name__ != "RcAsyncClient":
                raise TypeError("client type error, support client type is RcAsyncClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials")

        

        return client_builder

    def add_resources_to_group_async(self, request):
        r"""将资源添加到资源组

        将一个或多个资源添加到资源组，需要当前用户有resourcecenter:group:addResource权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddResourcesToGroup
        :type request: :class:`huaweicloudsdkrc.v1.AddResourcesToGroupRequest`
        :rtype: :class:`huaweicloudsdkrc.v1.AddResourcesToGroupResponse`
        """
        http_info = self._add_resources_to_group_http_info(request)
        return self._call_api(**http_info)

    def add_resources_to_group_async_invoker(self, request):
        http_info = self._add_resources_to_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_resources_to_group_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/resource-center/groups/{group_id}/resources",
            "request_type": request.__class__.__name__,
            "response_type": "AddResourcesToGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

    def create_resource_group_async(self, request):
        r"""创建资源分组

        创建一个资源分组，需要当前用户有resourcecenter:group:create权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateResourceGroup
        :type request: :class:`huaweicloudsdkrc.v1.CreateResourceGroupRequest`
        :rtype: :class:`huaweicloudsdkrc.v1.CreateResourceGroupResponse`
        """
        http_info = self._create_resource_group_http_info(request)
        return self._call_api(**http_info)

    def create_resource_group_async_invoker(self, request):
        http_info = self._create_resource_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_resource_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource-center/groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateResourceGroupResponse"
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

    def delete_resource_group_async(self, request):
        r"""删除一个资源分组

        删除一个资源分组，需要当前用户有resourcecenter:group:delete权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteResourceGroup
        :type request: :class:`huaweicloudsdkrc.v1.DeleteResourceGroupRequest`
        :rtype: :class:`huaweicloudsdkrc.v1.DeleteResourceGroupResponse`
        """
        http_info = self._delete_resource_group_http_info(request)
        return self._call_api(**http_info)

    def delete_resource_group_async_invoker(self, request):
        http_info = self._delete_resource_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_resource_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/resource-center/groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteResourceGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

    def list_resource_groups_async(self, request):
        r"""查询资源分组列表

        查询资源分组列表，需要当前用户有resourcecenter:group:list权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResourceGroups
        :type request: :class:`huaweicloudsdkrc.v1.ListResourceGroupsRequest`
        :rtype: :class:`huaweicloudsdkrc.v1.ListResourceGroupsResponse`
        """
        http_info = self._list_resource_groups_http_info(request)
        return self._call_api(**http_info)

    def list_resource_groups_async_invoker(self, request):
        http_info = self._list_resource_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_resource_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-center/groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceGroupsResponse"
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

    def remove_resource_from_group_async(self, request):
        r"""从资源组中移除资源

        从资源组中移除一个资源，需要当前用户有resourcecenter:group:removeResource权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RemoveResourceFromGroup
        :type request: :class:`huaweicloudsdkrc.v1.RemoveResourceFromGroupRequest`
        :rtype: :class:`huaweicloudsdkrc.v1.RemoveResourceFromGroupResponse`
        """
        http_info = self._remove_resource_from_group_http_info(request)
        return self._call_api(**http_info)

    def remove_resource_from_group_async_invoker(self, request):
        http_info = self._remove_resource_from_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _remove_resource_from_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/resource-center/groups/{group_id}/resources/{resource_id}",
            "request_type": request.__class__.__name__,
            "response_type": "RemoveResourceFromGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
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

    def show_resource_group_async(self, request):
        r"""查询一个资源分组

        查询一个资源分组，需要当前用户有resourcecenter:group:get权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourceGroup
        :type request: :class:`huaweicloudsdkrc.v1.ShowResourceGroupRequest`
        :rtype: :class:`huaweicloudsdkrc.v1.ShowResourceGroupResponse`
        """
        http_info = self._show_resource_group_http_info(request)
        return self._call_api(**http_info)

    def show_resource_group_async_invoker(self, request):
        http_info = self._show_resource_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_resource_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-center/groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourceGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

    def update_resource_group_async(self, request):
        r"""修改一个资源分组

        修改一个资源分组，需要当前用户有resourcecenter:group:update权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateResourceGroup
        :type request: :class:`huaweicloudsdkrc.v1.UpdateResourceGroupRequest`
        :rtype: :class:`huaweicloudsdkrc.v1.UpdateResourceGroupResponse`
        """
        http_info = self._update_resource_group_http_info(request)
        return self._call_api(**http_info)

    def update_resource_group_async_invoker(self, request):
        http_info = self._update_resource_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_resource_group_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/resource-center/groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateResourceGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

    def show_resource_relations_async(self, request):
        r"""列举资源关系

        指定资源ID，查询该资源与其他资源的关联关系，需要当前用户有resourcecenter::listResourceRelation权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourceRelations
        :type request: :class:`huaweicloudsdkrc.v1.ShowResourceRelationsRequest`
        :rtype: :class:`huaweicloudsdkrc.v1.ShowResourceRelationsResponse`
        """
        http_info = self._show_resource_relations_http_info(request)
        return self._call_api(**http_info)

    def show_resource_relations_async_invoker(self, request):
        http_info = self._show_resource_relations_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_resource_relations_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-center/resource-relations",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourceRelationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'related_resource_id' in local_var_params:
            query_params.append(('related_resource_id', local_var_params['related_resource_id']))
        if 'related_resource_type' in local_var_params:
            query_params.append(('related_resource_type', local_var_params['related_resource_type']))
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

    def collect_all_resources_summary_async(self, request):
        r"""列举资源概要

        查询当前帐号的资源概览，需要当前用户有rc::listResourceSummary权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CollectAllResourcesSummary
        :type request: :class:`huaweicloudsdkrc.v1.CollectAllResourcesSummaryRequest`
        :rtype: :class:`huaweicloudsdkrc.v1.CollectAllResourcesSummaryResponse`
        """
        http_info = self._collect_all_resources_summary_http_info(request)
        return self._call_api(**http_info)

    def collect_all_resources_summary_async_invoker(self, request):
        http_info = self._collect_all_resources_summary_http_info(request)
        return AsyncInvoker(self, http_info)

    def _collect_all_resources_summary_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-center/all-resources/summary",
            "request_type": request.__class__.__name__,
            "response_type": "CollectAllResourcesSummaryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'csv'
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
            collection_formats['region_id'] = 'csv'
        if 'ep_id' in local_var_params:
            query_params.append(('ep_id', local_var_params['ep_id']))
            collection_formats['ep_id'] = 'csv'
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))
            collection_formats['project_id'] = 'csv'
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
            collection_formats['tags'] = 'multi'

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

    def count_all_resources_async(self, request):
        r"""查询资源数量

        查询资源数量，需要当前用户有resourcecenter::getResourceCount权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CountAllResources
        :type request: :class:`huaweicloudsdkrc.v1.CountAllResourcesRequest`
        :rtype: :class:`huaweicloudsdkrc.v1.CountAllResourcesResponse`
        """
        http_info = self._count_all_resources_http_info(request)
        return self._call_api(**http_info)

    def count_all_resources_async_invoker(self, request):
        http_info = self._count_all_resources_http_info(request)
        return AsyncInvoker(self, http_info)

    def _count_all_resources_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-center/all-resources/count",
            "request_type": request.__class__.__name__,
            "response_type": "CountAllResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'csv'
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
            collection_formats['region_id'] = 'csv'
        if 'ep_id' in local_var_params:
            query_params.append(('ep_id', local_var_params['ep_id']))
            collection_formats['ep_id'] = 'csv'
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))
            collection_formats['project_id'] = 'csv'
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
            collection_formats['tags'] = 'multi'

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

    def list_all_providers_async(self, request):
        r"""列举所有已对接的云服务

        查询所有已对接RC的云服务、资源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAllProviders
        :type request: :class:`huaweicloudsdkrc.v1.ListAllProvidersRequest`
        :rtype: :class:`huaweicloudsdkrc.v1.ListAllProvidersResponse`
        """
        http_info = self._list_all_providers_http_info(request)
        return self._call_api(**http_info)

    def list_all_providers_async_invoker(self, request):
        http_info = self._list_all_providers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_all_providers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-center/all-providers",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllProvidersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_all_resources_async(self, request):
        r"""列举所有资源

        返回当前用户下所有资源，需要当前用户有resourcecenter::listResource权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAllResources
        :type request: :class:`huaweicloudsdkrc.v1.ListAllResourcesRequest`
        :rtype: :class:`huaweicloudsdkrc.v1.ListAllResourcesResponse`
        """
        http_info = self._list_all_resources_http_info(request)
        return self._call_api(**http_info)

    def list_all_resources_async_invoker(self, request):
        http_info = self._list_all_resources_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_all_resources_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-center/all-resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'ep_id' in local_var_params:
            query_params.append(('ep_id', local_var_params['ep_id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
            collection_formats['tags'] = 'multi'
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
            collection_formats['sort_key'] = 'multi'
        if 'sort_value' in local_var_params:
            query_params.append(('sort_value', local_var_params['sort_value']))
            collection_formats['sort_value'] = 'multi'

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

    def list_all_tags_async(self, request):
        r"""列举资源标签

        查询当前帐号下所有资源的标签，需要当前用户有resourcecenter::listResourceTag权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAllTags
        :type request: :class:`huaweicloudsdkrc.v1.ListAllTagsRequest`
        :rtype: :class:`huaweicloudsdkrc.v1.ListAllTagsResponse`
        """
        http_info = self._list_all_tags_http_info(request)
        return self._call_api(**http_info)

    def list_all_tags_async_invoker(self, request):
        http_info = self._list_all_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_all_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-center/all-resources/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'key' in local_var_params:
            query_params.append(('key', local_var_params['key']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_resources_async(self, request):
        r"""列举指定类型的资源

        返回当前租户下特定资源类型的资源，需要当前用户有resourcecenter::listResourceByType权限。比如查询云服务器，对应的RC资源类型是ecs.cloudservers，其中provider为ecs，type为cloudservers。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResources
        :type request: :class:`huaweicloudsdkrc.v1.ListResourcesRequest`
        :rtype: :class:`huaweicloudsdkrc.v1.ListResourcesResponse`
        """
        http_info = self._list_resources_http_info(request)
        return self._call_api(**http_info)

    def list_resources_async_invoker(self, request):
        http_info = self._list_resources_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_resources_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-center/provider/{provider}/type/{type}/resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'provider' in local_var_params:
            path_params['provider'] = local_var_params['provider']
        if 'type' in local_var_params:
            path_params['type'] = local_var_params['type']

        query_params = []
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'ep_id' in local_var_params:
            query_params.append(('ep_id', local_var_params['ep_id']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))
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

    def show_resource_by_id_async(self, request):
        r"""查询指定类型的单个资源

        指定资源ID，返回该资源的详细信息，需要当前用户有resourcecenter::getResourceByType权限。比如查询云服务器，对应的RC资源类型是ecs.cloudservers，其中provider为ecs，type为cloudservers。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourceById
        :type request: :class:`huaweicloudsdkrc.v1.ShowResourceByIdRequest`
        :rtype: :class:`huaweicloudsdkrc.v1.ShowResourceByIdResponse`
        """
        http_info = self._show_resource_by_id_http_info(request)
        return self._call_api(**http_info)

    def show_resource_by_id_async_invoker(self, request):
        http_info = self._show_resource_by_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_resource_by_id_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-center/provider/{provider}/type/{type}/resources/{resource_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourceByIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'provider' in local_var_params:
            path_params['provider'] = local_var_params['provider']
        if 'type' in local_var_params:
            path_params['type'] = local_var_params['type']
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

    def show_resource_detail_async(self, request):
        r"""查询单个资源

        查询当前帐号下的单个资源，需要当前用户有resourcecenter::getResource权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourceDetail
        :type request: :class:`huaweicloudsdkrc.v1.ShowResourceDetailRequest`
        :rtype: :class:`huaweicloudsdkrc.v1.ShowResourceDetailResponse`
        """
        http_info = self._show_resource_detail_http_info(request)
        return self._call_api(**http_info)

    def show_resource_detail_async_invoker(self, request):
        http_info = self._show_resource_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_resource_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-center/all-resources/{resource_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourceDetailResponse"
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
