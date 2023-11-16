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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdktics'")


class TicsAsyncClient(Client):
    def __init__(self):
        super(TicsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdktics.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "TicsAsyncClient":
                raise TypeError("client type error, support client type is TicsAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def list_agents_async(self, request):
        """获取计算节点列表

        功能描述：用户可以使用该接口获取可信节点信息列表。支持节点名称与联盟名称的模糊查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAgents
        :type request: :class:`huaweicloudsdktics.v1.ListAgentsRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ListAgentsResponse`
        """
        http_info = self._list_agents_http_info(request)
        return self._call_api(**http_info)

    def list_agents_async_invoker(self, request):
        http_info = self._list_agents_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_agents_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/agents",
            "request_type": request.__class__.__name__,
            "response_type": "ListAgentsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'agent_name' in local_var_params:
            query_params.append(('agent_name', local_var_params['agent_name']))
        if 'league_name' in local_var_params:
            query_params.append(('league_name', local_var_params['league_name']))

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

    def list_audit_info_async(self, request):
        """查询审计日志

        查询审计日志信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAuditInfo
        :type request: :class:`huaweicloudsdktics.v1.ListAuditInfoRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ListAuditInfoResponse`
        """
        http_info = self._list_audit_info_http_info(request)
        return self._call_api(**http_info)

    def list_audit_info_async_invoker(self, request):
        http_info = self._list_audit_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_audit_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/leagues/{league_id}/audit-info",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'league_id' in local_var_params:
            path_params['league_id'] = local_var_params['league_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
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

    def list_fl_job_async(self, request):
        """查询联邦学习作业列表

        查询联邦学习作业列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFlJob
        :type request: :class:`huaweicloudsdktics.v1.ListFlJobRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ListFlJobResponse`
        """
        http_info = self._list_fl_job_http_info(request)
        return self._call_api(**http_info)

    def list_fl_job_async_invoker(self, request):
        http_info = self._list_fl_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_fl_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/leagues/{league_id}/fl-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListFlJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'league_id' in local_var_params:
            path_params['league_id'] = local_var_params['league_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
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

    def list_instance_history_async(self, request):
        """查询作业的历史实例列表

        查询作业的历史实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstanceHistory
        :type request: :class:`huaweicloudsdktics.v1.ListInstanceHistoryRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ListInstanceHistoryResponse`
        """
        http_info = self._list_instance_history_http_info(request)
        return self._call_api(**http_info)

    def list_instance_history_async_invoker(self, request):
        http_info = self._list_instance_history_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instance_history_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/leagues/{league_id}/job-instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceHistoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'league_id' in local_var_params:
            path_params['league_id'] = local_var_params['league_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))

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

    def list_league_datasets_async(self, request):
        """查询联盟已注册数据集列表

        功能描述：用户可以使用该接口查询联盟已注册数据集列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLeagueDatasets
        :type request: :class:`huaweicloudsdktics.v1.ListLeagueDatasetsRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ListLeagueDatasetsResponse`
        """
        http_info = self._list_league_datasets_http_info(request)
        return self._call_api(**http_info)

    def list_league_datasets_async_invoker(self, request):
        http_info = self._list_league_datasets_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_league_datasets_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/leagues/{league_id}/datasets",
            "request_type": request.__class__.__name__,
            "response_type": "ListLeagueDatasetsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'league_id' in local_var_params:
            path_params['league_id'] = local_var_params['league_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'dataset_name' in local_var_params:
            query_params.append(('dataset_name', local_var_params['dataset_name']))
        if 'partner_name' in local_var_params:
            query_params.append(('partner_name', local_var_params['partner_name']))

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

    def list_leagues_async(self, request):
        """获取联盟列表

        功能描述：用户可以使用该接口获取联盟列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLeagues
        :type request: :class:`huaweicloudsdktics.v1.ListLeaguesRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ListLeaguesResponse`
        """
        http_info = self._list_leagues_http_info(request)
        return self._call_api(**http_info)

    def list_leagues_async_invoker(self, request):
        http_info = self._list_leagues_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_leagues_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/league-info",
            "request_type": request.__class__.__name__,
            "response_type": "ListLeaguesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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

    def list_nodes_async(self, request):
        """查询联盟节点列表

        功能描述：用户可以使用该接口查询联盟可信节点（包含聚合节点和计算节点）列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNodes
        :type request: :class:`huaweicloudsdktics.v1.ListNodesRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ListNodesResponse`
        """
        http_info = self._list_nodes_http_info(request)
        return self._call_api(**http_info)

    def list_nodes_async_invoker(self, request):
        http_info = self._list_nodes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_nodes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/leagues/{league_id}/nodes",
            "request_type": request.__class__.__name__,
            "response_type": "ListNodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'league_id' in local_var_params:
            path_params['league_id'] = local_var_params['league_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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

    def list_notices_async(self, request):
        """查询通知管理列表

        功能描述：用户可以使用该接口查询通知管理列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNotices
        :type request: :class:`huaweicloudsdktics.v1.ListNoticesRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ListNoticesResponse`
        """
        http_info = self._list_notices_http_info(request)
        return self._call_api(**http_info)

    def list_notices_async_invoker(self, request):
        http_info = self._list_notices_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_notices_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/notices",
            "request_type": request.__class__.__name__,
            "response_type": "ListNoticesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
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

    def list_partners_async(self, request):
        """获取联盟组员信息

        功能描述：用户可以使用该接口获取联盟组员信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPartners
        :type request: :class:`huaweicloudsdktics.v1.ListPartnersRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ListPartnersResponse`
        """
        http_info = self._list_partners_http_info(request)
        return self._call_api(**http_info)

    def list_partners_async_invoker(self, request):
        http_info = self._list_partners_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_partners_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/leagues/{league_id}/partners",
            "request_type": request.__class__.__name__,
            "response_type": "ListPartnersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'league_id' in local_var_params:
            path_params['league_id'] = local_var_params['league_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
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

    def list_sql_job_async(self, request):
        """查询联邦分析作业列表

        查询联邦分析作业列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSqlJob
        :type request: :class:`huaweicloudsdktics.v1.ListSqlJobRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ListSqlJobResponse`
        """
        http_info = self._list_sql_job_http_info(request)
        return self._call_api(**http_info)

    def list_sql_job_async_invoker(self, request):
        http_info = self._list_sql_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_sql_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/leagues/{league_id}/sql-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListSqlJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'league_id' in local_var_params:
            path_params['league_id'] = local_var_params['league_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
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

    def show_agent_detail_async(self, request):
        """获取计算节点详情信息

        功能描述：用户可以使用该接口获取单个可信计算节点详情信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAgentDetail
        :type request: :class:`huaweicloudsdktics.v1.ShowAgentDetailRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ShowAgentDetailResponse`
        """
        http_info = self._show_agent_detail_http_info(request)
        return self._call_api(**http_info)

    def show_agent_detail_async_invoker(self, request):
        http_info = self._show_agent_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_agent_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/agents/{agent_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAgentDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agent_id' in local_var_params:
            path_params['agent_id'] = local_var_params['agent_id']

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

    def show_dataset_statistics_async(self, request):
        """数据集统计

        用户可以使用该接口进行联盟数据集统计。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDatasetStatistics
        :type request: :class:`huaweicloudsdktics.v1.ShowDatasetStatisticsRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ShowDatasetStatisticsResponse`
        """
        http_info = self._show_dataset_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_dataset_statistics_async_invoker(self, request):
        http_info = self._show_dataset_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_dataset_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/leagues/{league_id}/datasets-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDatasetStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'league_id' in local_var_params:
            path_params['league_id'] = local_var_params['league_id']

        query_params = []
        if 'start_date' in local_var_params:
            query_params.append(('start_date', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('end_date', local_var_params['end_date']))

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

    def show_instance_report_async(self, request):
        """查询实例执行报告

        查询实例执行报告
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstanceReport
        :type request: :class:`huaweicloudsdktics.v1.ShowInstanceReportRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ShowInstanceReportResponse`
        """
        http_info = self._show_instance_report_http_info(request)
        return self._call_api(**http_info)

    def show_instance_report_async_invoker(self, request):
        http_info = self._show_instance_report_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_instance_report_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/leagues/{league_id}/job-instances/{instance_id}/report",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceReportResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'league_id' in local_var_params:
            path_params['league_id'] = local_var_params['league_id']

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

    def show_job_instance_dag_async(self, request):
        """获取实例执行图

        获取实例执行图
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobInstanceDag
        :type request: :class:`huaweicloudsdktics.v1.ShowJobInstanceDagRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ShowJobInstanceDagResponse`
        """
        http_info = self._show_job_instance_dag_http_info(request)
        return self._call_api(**http_info)

    def show_job_instance_dag_async_invoker(self, request):
        http_info = self._show_job_instance_dag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_instance_dag_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/leagues/{league_id}/job-instances/{instance_id}/dag",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobInstanceDagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'league_id' in local_var_params:
            path_params['league_id'] = local_var_params['league_id']

        query_params = []
        if 'round_id' in local_var_params:
            query_params.append(('round_id', local_var_params['round_id']))

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

    def show_job_statistics_async(self, request):
        """作业统计

        功能描述：用户可以使用该接口进行联盟作业统计。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobStatistics
        :type request: :class:`huaweicloudsdktics.v1.ShowJobStatisticsRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ShowJobStatisticsResponse`
        """
        http_info = self._show_job_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_job_statistics_async_invoker(self, request):
        http_info = self._show_job_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/leagues/{league_id}/jobs-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'league_id' in local_var_params:
            path_params['league_id'] = local_var_params['league_id']

        query_params = []
        if 'start_date' in local_var_params:
            query_params.append(('start_date', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('end_date', local_var_params['end_date']))

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

    def show_league_async(self, request):
        """获取联盟详细信息

        功能描述：用户可以使用该接口获取联盟详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowLeague
        :type request: :class:`huaweicloudsdktics.v1.ShowLeagueRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ShowLeagueResponse`
        """
        http_info = self._show_league_http_info(request)
        return self._call_api(**http_info)

    def show_league_async_invoker(self, request):
        http_info = self._show_league_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_league_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/leagues/{league_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLeagueResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'league_id' in local_var_params:
            path_params['league_id'] = local_var_params['league_id']

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

    def show_overview_async(self, request):
        """查询租户下统计信息

        查询当前租户的联盟及代理统计数量
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOverview
        :type request: :class:`huaweicloudsdktics.v1.ShowOverviewRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ShowOverviewResponse`
        """
        http_info = self._show_overview_http_info(request)
        return self._call_api(**http_info)

    def show_overview_async_invoker(self, request):
        http_info = self._show_overview_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_overview_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/overview/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOverviewResponse"
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

    def show_partner_statistics_async(self, request):
        """合作方统计

        功能描述：用户可以使用该接口进行联盟合作方统计。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPartnerStatistics
        :type request: :class:`huaweicloudsdktics.v1.ShowPartnerStatisticsRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ShowPartnerStatisticsResponse`
        """
        http_info = self._show_partner_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_partner_statistics_async_invoker(self, request):
        http_info = self._show_partner_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_partner_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/leagues/{league_id}/partners-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPartnerStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'league_id' in local_var_params:
            path_params['league_id'] = local_var_params['league_id']

        query_params = []
        if 'start_date' in local_var_params:
            query_params.append(('start_date', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('end_date', local_var_params['end_date']))

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

    def update_league_async(self, request):
        """更新联盟信息

        功能描述：用户可以使用接口更新联盟信息（包含联盟描述，联盟版本，隐私保护等级，查分隐私开关）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateLeague
        :type request: :class:`huaweicloudsdktics.v1.UpdateLeagueRequest`
        :rtype: :class:`huaweicloudsdktics.v1.UpdateLeagueResponse`
        """
        http_info = self._update_league_http_info(request)
        return self._call_api(**http_info)

    def update_league_async_invoker(self, request):
        http_info = self._update_league_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_league_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/leagues/{league_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLeagueResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'league_id' in local_var_params:
            path_params['league_id'] = local_var_params['league_id']

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
