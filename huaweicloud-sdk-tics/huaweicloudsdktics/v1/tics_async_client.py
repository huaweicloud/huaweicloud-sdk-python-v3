# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


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
        return self._list_agents_with_http_info(request)

    def _list_agents_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/agents',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAgentsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_audit_info_async(self, request):
        """查询审计日志

        查询审计日志信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAuditInfo
        :type request: :class:`huaweicloudsdktics.v1.ListAuditInfoRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ListAuditInfoResponse`
        """
        return self._list_audit_info_with_http_info(request)

    def _list_audit_info_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/leagues/{league_id}/audit-info',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAuditInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_fl_job_async(self, request):
        """查询联邦学习作业列表

        查询联邦学习作业列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFlJob
        :type request: :class:`huaweicloudsdktics.v1.ListFlJobRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ListFlJobResponse`
        """
        return self._list_fl_job_with_http_info(request)

    def _list_fl_job_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/leagues/{league_id}/fl-jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFlJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instance_history_async(self, request):
        """查询作业的历史实例列表

        查询作业的历史实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstanceHistory
        :type request: :class:`huaweicloudsdktics.v1.ListInstanceHistoryRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ListInstanceHistoryResponse`
        """
        return self._list_instance_history_with_http_info(request)

    def _list_instance_history_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/leagues/{league_id}/job-instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListInstanceHistoryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_league_datasets_async(self, request):
        """查询联盟已注册数据集列表

        功能描述：用户可以使用该接口查询联盟已注册数据集列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLeagueDatasets
        :type request: :class:`huaweicloudsdktics.v1.ListLeagueDatasetsRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ListLeagueDatasetsResponse`
        """
        return self._list_league_datasets_with_http_info(request)

    def _list_league_datasets_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/leagues/{league_id}/datasets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListLeagueDatasetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_leagues_async(self, request):
        """获取联盟列表

        功能描述：用户可以使用该接口获取联盟列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLeagues
        :type request: :class:`huaweicloudsdktics.v1.ListLeaguesRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ListLeaguesResponse`
        """
        return self._list_leagues_with_http_info(request)

    def _list_leagues_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/league-info',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListLeaguesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_nodes_async(self, request):
        """查询联盟节点列表

        功能描述：用户可以使用该接口查询联盟可信节点（包含聚合节点和计算节点）列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNodes
        :type request: :class:`huaweicloudsdktics.v1.ListNodesRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ListNodesResponse`
        """
        return self._list_nodes_with_http_info(request)

    def _list_nodes_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/leagues/{league_id}/nodes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListNodesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_notices_async(self, request):
        """查询通知管理列表

        功能描述：用户可以使用该接口查询通知管理列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNotices
        :type request: :class:`huaweicloudsdktics.v1.ListNoticesRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ListNoticesResponse`
        """
        return self._list_notices_with_http_info(request)

    def _list_notices_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/notices',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListNoticesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_partners_async(self, request):
        """获取联盟组员信息

        功能描述：用户可以使用该接口获取联盟组员信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPartners
        :type request: :class:`huaweicloudsdktics.v1.ListPartnersRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ListPartnersResponse`
        """
        return self._list_partners_with_http_info(request)

    def _list_partners_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/leagues/{league_id}/partners',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPartnersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_sql_job_async(self, request):
        """查询联邦分析作业列表

        查询联邦分析作业列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSqlJob
        :type request: :class:`huaweicloudsdktics.v1.ListSqlJobRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ListSqlJobResponse`
        """
        return self._list_sql_job_with_http_info(request)

    def _list_sql_job_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/leagues/{league_id}/sql-jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSqlJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_agent_detail_async(self, request):
        """获取计算节点详情信息

        功能描述：用户可以使用该接口获取单个可信计算节点详情信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAgentDetail
        :type request: :class:`huaweicloudsdktics.v1.ShowAgentDetailRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ShowAgentDetailResponse`
        """
        return self._show_agent_detail_with_http_info(request)

    def _show_agent_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agent_id' in local_var_params:
            path_params['agent_id'] = local_var_params['agent_id']

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
            resource_path='/v1/{project_id}/agents/{agent_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAgentDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_dataset_statistics_async(self, request):
        """数据集统计

        用户可以使用该接口进行联盟数据集统计。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDatasetStatistics
        :type request: :class:`huaweicloudsdktics.v1.ShowDatasetStatisticsRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ShowDatasetStatisticsResponse`
        """
        return self._show_dataset_statistics_with_http_info(request)

    def _show_dataset_statistics_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/leagues/{league_id}/datasets-statistics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDatasetStatisticsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_instance_report_async(self, request):
        """查询实例执行报告

        查询实例执行报告
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstanceReport
        :type request: :class:`huaweicloudsdktics.v1.ShowInstanceReportRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ShowInstanceReportResponse`
        """
        return self._show_instance_report_with_http_info(request)

    def _show_instance_report_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/leagues/{league_id}/job-instances/{instance_id}/report',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowInstanceReportResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job_instance_dag_async(self, request):
        """获取实例执行图

        获取实例执行图
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobInstanceDag
        :type request: :class:`huaweicloudsdktics.v1.ShowJobInstanceDagRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ShowJobInstanceDagResponse`
        """
        return self._show_job_instance_dag_with_http_info(request)

    def _show_job_instance_dag_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/leagues/{league_id}/job-instances/{instance_id}/dag',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowJobInstanceDagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job_statistics_async(self, request):
        """作业统计

        功能描述：用户可以使用该接口进行联盟作业统计。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobStatistics
        :type request: :class:`huaweicloudsdktics.v1.ShowJobStatisticsRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ShowJobStatisticsResponse`
        """
        return self._show_job_statistics_with_http_info(request)

    def _show_job_statistics_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/leagues/{league_id}/jobs-statistics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowJobStatisticsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_league_async(self, request):
        """获取联盟详细信息

        功能描述：用户可以使用该接口获取联盟详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowLeague
        :type request: :class:`huaweicloudsdktics.v1.ShowLeagueRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ShowLeagueResponse`
        """
        return self._show_league_with_http_info(request)

    def _show_league_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'league_id' in local_var_params:
            path_params['league_id'] = local_var_params['league_id']

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
            resource_path='/v1/{project_id}/leagues/{league_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowLeagueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_overview_async(self, request):
        """查询租户下统计信息

        查询当前租户的联盟及代理统计数量
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOverview
        :type request: :class:`huaweicloudsdktics.v1.ShowOverviewRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ShowOverviewResponse`
        """
        return self._show_overview_with_http_info(request)

    def _show_overview_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1/{project_id}/overview/statistics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowOverviewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_partner_statistics_async(self, request):
        """合作方统计

        功能描述：用户可以使用该接口进行联盟合作方统计。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPartnerStatistics
        :type request: :class:`huaweicloudsdktics.v1.ShowPartnerStatisticsRequest`
        :rtype: :class:`huaweicloudsdktics.v1.ShowPartnerStatisticsResponse`
        """
        return self._show_partner_statistics_with_http_info(request)

    def _show_partner_statistics_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/leagues/{league_id}/partners-statistics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPartnerStatisticsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_league_async(self, request):
        """更新联盟信息

        功能描述：用户可以使用接口更新联盟信息（包含联盟描述，联盟版本，隐私保护等级，查分隐私开关）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateLeague
        :type request: :class:`huaweicloudsdktics.v1.UpdateLeagueRequest`
        :rtype: :class:`huaweicloudsdktics.v1.UpdateLeagueResponse`
        """
        return self._update_league_with_http_info(request)

    def _update_league_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'league_id' in local_var_params:
            path_params['league_id'] = local_var_params['league_id']

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/leagues/{league_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateLeagueResponse',
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
