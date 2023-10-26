# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class DliClient(Client):
    def __init__(self):
        super(DliClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdli.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "DliClient":
                raise TypeError("client type error, support client type is DliClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_job_templates(self, request):
        """创建作业模板

        该API用于创建作业模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateJobTemplates
        :type request: :class:`huaweicloudsdkdli.v1.CreateJobTemplatesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateJobTemplatesResponse`
        """
        return self._create_job_templates_with_http_info(request)

    def _create_job_templates_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/templates',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateJobTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_sql_templates(self, request):
        """存储指定SQL语句

        该API用于存储指定的SQL语句，后续可以重复使用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSqlTemplates
        :type request: :class:`huaweicloudsdkdli.v1.CreateSqlTemplatesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateSqlTemplatesResponse`
        """
        return self._create_sql_templates_with_http_info(request)

    def _create_sql_templates_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/sqls',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSqlTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_sql_templates(self, request):
        """批量删除SQL模板

        该API用于批量删除SQL模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSqlTemplates
        :type request: :class:`huaweicloudsdkdli.v1.DeleteSqlTemplatesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.DeleteSqlTemplatesResponse`
        """
        return self._delete_sql_templates_with_http_info(request)

    def _delete_sql_templates_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/sqls-deletion',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSqlTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_job_templates(self, request):
        """查询作业模板列表

        该API用于查询作业模板列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListJobTemplates
        :type request: :class:`huaweicloudsdkdli.v1.ListJobTemplatesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListJobTemplatesResponse`
        """
        return self._list_job_templates_with_http_info(request)

    def _list_job_templates_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'keyword' in local_var_params:
            query_params.append(('keyword', local_var_params['keyword']))
        if 'page_size' in local_var_params:
            query_params.append(('page-size', local_var_params['page_size']))
        if 'current_page' in local_var_params:
            query_params.append(('current-page', local_var_params['current_page']))

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
            resource_path='/v3/{project_id}/templates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListJobTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job_template(self, request):
        """获取作业模板

        该API用于获取作业模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJobTemplate
        :type request: :class:`huaweicloudsdkdli.v1.ShowJobTemplateRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowJobTemplateResponse`
        """
        return self._show_job_template_with_http_info(request)

    def _show_job_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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
            resource_path='/v3/{project_id}/templates/{template_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowJobTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_sql_sample_templates(self, request):
        """查询所有SQL样例模板

        该API用于查询所有SQL样例模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSqlSampleTemplates
        :type request: :class:`huaweicloudsdkdli.v1.ShowSqlSampleTemplatesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowSqlSampleTemplatesResponse`
        """
        return self._show_sql_sample_templates_with_http_info(request)

    def _show_sql_sample_templates_with_http_info(self, request):
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
            resource_path='/v1.0/{project_id}/sqls/sample',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSqlSampleTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_sql_templates(self, request):
        """查看所有SQL模板

        该API用查看用户保存的所有SQL模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSqlTemplates
        :type request: :class:`huaweicloudsdkdli.v1.ShowSqlTemplatesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowSqlTemplatesResponse`
        """
        return self._show_sql_templates_with_http_info(request)

    def _show_sql_templates_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in local_var_params:
            query_params.append(('keyword', local_var_params['keyword']))

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
            resource_path='/v1.0/{project_id}/sqls',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSqlTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_job_templates(self, request):
        """修改作业模板

        该API用于修改作业模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateJobTemplates
        :type request: :class:`huaweicloudsdkdli.v1.UpdateJobTemplatesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateJobTemplatesResponse`
        """
        return self._update_job_templates_with_http_info(request)

    def _update_job_templates_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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
            resource_path='/v3/{project_id}/templates/{template_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateJobTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_sql_templates(self, request):
        """更新SQL模板

        该API用于更新SQL模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSqlTemplates
        :type request: :class:`huaweicloudsdkdli.v1.UpdateSqlTemplatesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateSqlTemplatesResponse`
        """
        return self._update_sql_templates_with_http_info(request)

    def _update_sql_templates_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sql_id' in local_var_params:
            path_params['sql_id'] = local_var_params['sql_id']

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
            resource_path='/v1.0/{project_id}/sqls/{sql_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateSqlTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_connection_queue(self, request):
        """绑定队列

        该API用于在已创建的增强型跨源中绑定队列。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateConnectionQueue
        :type request: :class:`huaweicloudsdkdli.v1.AssociateConnectionQueueRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.AssociateConnectionQueueResponse`
        """
        return self._associate_connection_queue_with_http_info(request)

    def _associate_connection_queue_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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
            resource_path='/v2.0/{project_id}/datasource/enhanced-connections/{connection_id}/associate-queue',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociateConnectionQueueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_queue_to_elastic_resource_pool(self, request):
        """关联队列到弹性资源池

        关联队列到弹性资源池
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateQueueToElasticResourcePool
        :type request: :class:`huaweicloudsdkdli.v1.AssociateQueueToElasticResourcePoolRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.AssociateQueueToElasticResourcePoolResponse`
        """
        return self._associate_queue_to_elastic_resource_pool_with_http_info(request)

    def _associate_queue_to_elastic_resource_pool_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'elastic_resource_pool_name' in local_var_params:
            path_params['elastic_resource_pool_name'] = local_var_params['elastic_resource_pool_name']

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
            resource_path='/v3/{project_id}/elastic-resource-pools/{elastic_resource_pool_name}/queues',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociateQueueToElasticResourcePoolResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def authorize_resource(self, request):
        """数据赋权（用户、项目）

        该API用于将DLI资源权限赋给、回收、更新指定的其他用户或项目。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AuthorizeResource
        :type request: :class:`huaweicloudsdkdli.v1.AuthorizeResourceRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.AuthorizeResourceResponse`
        """
        return self._authorize_resource_with_http_info(request)

    def _authorize_resource_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/authorization',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AuthorizeResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_queue_plans(self, request):
        """批量删除队列定时扩缩容计划

        该API用于批量删除队列定时扩缩容计划。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteQueuePlans
        :type request: :class:`huaweicloudsdkdli.v1.BatchDeleteQueuePlansRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.BatchDeleteQueuePlansResponse`
        """
        return self._batch_delete_queue_plans_with_http_info(request)

    def _batch_delete_queue_plans_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'queue_name' in local_var_params:
            path_params['queue_name'] = local_var_params['queue_name']

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
            resource_path='/v1/{project_id}/queues/{queue_name}/plans/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteQueuePlansResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_authorization(self, request):
        """数据赋权（用户）

        该API用于将数据库或数据表的数据权限赋给指定的其他用户。
        说明：
        被赋权用户所在用户组的所属区域需具有Tenant Guest权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeAuthorization
        :type request: :class:`huaweicloudsdkdli.v1.ChangeAuthorizationRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ChangeAuthorizationResponse`
        """
        return self._change_authorization_with_http_info(request)

    def _change_authorization_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/user-authorization',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeAuthorizationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_queue_plan(self, request):
        """修改队列定时扩缩容计划

        该API用于修改指定ID的队列定时扩缩容计划。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeQueuePlan
        :type request: :class:`huaweicloudsdkdli.v1.ChangeQueuePlanRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ChangeQueuePlanResponse`
        """
        return self._change_queue_plan_with_http_info(request)

    def _change_queue_plan_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'plan_id' in local_var_params:
            path_params['plan_id'] = local_var_params['plan_id']
        if 'queue_name' in local_var_params:
            path_params['queue_name'] = local_var_params['queue_name']

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
            resource_path='/v1/{project_id}/queues/{queue_name}/plans/{plan_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeQueuePlanResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_connection(self, request):
        """创建地址连通性请求

        创建地址连通性请求API接口，往指定集群发送地址连通性测试请求，并将测试地址插入表内
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckConnection
        :type request: :class:`huaweicloudsdkdli.v1.CheckConnectionRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CheckConnectionResponse`
        """
        return self._check_connection_with_http_info(request)

    def _check_connection_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'queue_name' in local_var_params:
            path_params['queue_name'] = local_var_params['queue_name']

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
            resource_path='/v1.0/{project_id}/queues/{queue_name}/connection-test',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CheckConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_auth_info(self, request):
        """创建跨源认证

        该API用于创建跨源认证。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAuthInfo
        :type request: :class:`huaweicloudsdkdli.v1.CreateAuthInfoRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateAuthInfoResponse`
        """
        return self._create_auth_info_with_http_info(request)

    def _create_auth_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/datasource/auth-infos',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAuthInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_datasource_connection(self, request):
        """创建经典型跨源连接

        该API用于创建与其他服务的经典型跨源连接。
        说明：
        如果需要了解Console界面的使用方法，可参考经典型跨源连接。
        系统default队列不支持创建跨源连接。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDatasourceConnection
        :type request: :class:`huaweicloudsdkdli.v1.CreateDatasourceConnectionRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateDatasourceConnectionResponse`
        """
        return self._create_datasource_connection_with_http_info(request)

    def _create_datasource_connection_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/datasource-connection',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDatasourceConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_dli_agency(self, request):
        """创建DLI委托

        创建DLI委托
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDliAgency
        :type request: :class:`huaweicloudsdkdli.v1.CreateDliAgencyRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateDliAgencyResponse`
        """
        return self._create_dli_agency_with_http_info(request)

    def _create_dli_agency_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/agency',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDliAgencyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_elastic_resource_pool(self, request):
        """创建弹性资源池

        创建弹性资源池
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateElasticResourcePool
        :type request: :class:`huaweicloudsdkdli.v1.CreateElasticResourcePoolRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateElasticResourcePoolResponse`
        """
        return self._create_elastic_resource_pool_with_http_info(request)

    def _create_elastic_resource_pool_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elastic-resource-pools',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateElasticResourcePoolResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_enhanced_connection(self, request):
        """创建增强型跨源连接

        该API用于创建与其他服务的增强型跨源连接。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEnhancedConnection
        :type request: :class:`huaweicloudsdkdli.v1.CreateEnhancedConnectionRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateEnhancedConnectionResponse`
        """
        return self._create_enhanced_connection_with_http_info(request)

    def _create_enhanced_connection_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/datasource/enhanced-connections',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateEnhancedConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_enhanced_connection_routes(self, request):
        """创建路由

        该API用于创建跨源需要的路由。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEnhancedConnectionRoutes
        :type request: :class:`huaweicloudsdkdli.v1.CreateEnhancedConnectionRoutesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateEnhancedConnectionRoutesResponse`
        """
        return self._create_enhanced_connection_routes_with_http_info(request)

    def _create_enhanced_connection_routes_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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
            resource_path='/v2.0/{project_id}/datasource/enhanced-connections/{connection_id}/routes',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateEnhancedConnectionRoutesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_global_value(self, request):
        """创建DLI全局变量

        创建全局变量。全局变量用于替换SQL作业中的敏感数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateGlobalValue
        :type request: :class:`huaweicloudsdkdli.v1.CreateGlobalValueRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateGlobalValueResponse`
        """
        return self._create_global_value_with_http_info(request)

    def _create_global_value_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/variables',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateGlobalValueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_queue(self, request):
        """创建队列

        该API用于创建队列，该队列将会绑定用户指定的计算资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateQueue
        :type request: :class:`huaweicloudsdkdli.v1.CreateQueueRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateQueueResponse`
        """
        return self._create_queue_with_http_info(request)

    def _create_queue_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/queues',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateQueueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_queue_plan(self, request):
        """创建队列定时扩缩容计划

        创建队列定时扩缩容计划接口，对指定的队列创建定时规格变更计划。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateQueuePlan
        :type request: :class:`huaweicloudsdkdli.v1.CreateQueuePlanRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateQueuePlanResponse`
        """
        return self._create_queue_plan_with_http_info(request)

    def _create_queue_plan_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'queue_name' in local_var_params:
            path_params['queue_name'] = local_var_params['queue_name']

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
            resource_path='/v1/{project_id}/queues/{queue_name}/plans',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateQueuePlanResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_auth_info(self, request):
        """删除跨源认证

        该API用于删除跨源认证信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAuthInfo
        :type request: :class:`huaweicloudsdkdli.v1.DeleteAuthInfoRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.DeleteAuthInfoResponse`
        """
        return self._delete_auth_info_with_http_info(request)

    def _delete_auth_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'auth_info_name' in local_var_params:
            path_params['auth_info_name'] = local_var_params['auth_info_name']

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
            resource_path='/v2.0/{project_id}/datasource/auth-infos/{auth_info_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAuthInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_datasource_connection(self, request):
        """删除经典型跨源连接

        该API用于删除已创建的经典型跨源连接。
        说明：
        创建中的连接，无法删除。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDatasourceConnection
        :type request: :class:`huaweicloudsdkdli.v1.DeleteDatasourceConnectionRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.DeleteDatasourceConnectionResponse`
        """
        return self._delete_datasource_connection_with_http_info(request)

    def _delete_datasource_connection_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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
            resource_path='/v2.0/{project_id}/datasource-connection/{connection_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDatasourceConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_elastic_resource_pool(self, request):
        """删除弹性资源池

        删除弹性资源池
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteElasticResourcePool
        :type request: :class:`huaweicloudsdkdli.v1.DeleteElasticResourcePoolRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.DeleteElasticResourcePoolResponse`
        """
        return self._delete_elastic_resource_pool_with_http_info(request)

    def _delete_elastic_resource_pool_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'elastic_resource_pool_name' in local_var_params:
            path_params['elastic_resource_pool_name'] = local_var_params['elastic_resource_pool_name']

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
            resource_path='/v3/{project_id}/elastic-resource-pools/{elastic_resource_pool_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteElasticResourcePoolResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_enhanced_connection(self, request):
        """删除增强型跨源连接

        该API用于删除已创建的增强型跨源连接。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEnhancedConnection
        :type request: :class:`huaweicloudsdkdli.v1.DeleteEnhancedConnectionRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.DeleteEnhancedConnectionResponse`
        """
        return self._delete_enhanced_connection_with_http_info(request)

    def _delete_enhanced_connection_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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
            resource_path='/v2.0/{project_id}/datasource/enhanced-connections/{connection_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEnhancedConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_enhanced_connection_routes(self, request):
        """删除路由

        该API用于删除跨源需要的路由。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEnhancedConnectionRoutes
        :type request: :class:`huaweicloudsdkdli.v1.DeleteEnhancedConnectionRoutesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.DeleteEnhancedConnectionRoutesResponse`
        """
        return self._delete_enhanced_connection_routes_with_http_info(request)

    def _delete_enhanced_connection_routes_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']

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
            resource_path='/v2.0/{project_id}/datasource/enhanced-connections/{connection_id}/routes/{name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEnhancedConnectionRoutesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_global_value(self, request):
        """删除DLI全局变量

        删除全局变量。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteGlobalValue
        :type request: :class:`huaweicloudsdkdli.v1.DeleteGlobalValueRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.DeleteGlobalValueResponse`
        """
        return self._delete_global_value_with_http_info(request)

    def _delete_global_value_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'var_name' in local_var_params:
            path_params['var_name'] = local_var_params['var_name']

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
            resource_path='/v1.0/{project_id}/variables/{var_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteGlobalValueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_queue(self, request):
        """删除队列

        该API用于删除指定队列。
        说明：
        若指定队列正在执行任务，则不允许删除。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteQueue
        :type request: :class:`huaweicloudsdkdli.v1.DeleteQueueRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.DeleteQueueResponse`
        """
        return self._delete_queue_with_http_info(request)

    def _delete_queue_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'queue_name' in local_var_params:
            path_params['queue_name'] = local_var_params['queue_name']

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
            resource_path='/v1.0/{project_id}/queues/{queue_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteQueueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_queue_plan(self, request):
        """单个删除队列定时扩缩容计划

        该API用于删除指定ID的队列定时扩缩容计划。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteQueuePlan
        :type request: :class:`huaweicloudsdkdli.v1.DeleteQueuePlanRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.DeleteQueuePlanResponse`
        """
        return self._delete_queue_plan_with_http_info(request)

    def _delete_queue_plan_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'plan_id' in local_var_params:
            path_params['plan_id'] = local_var_params['plan_id']
        if 'queue_name' in local_var_params:
            path_params['queue_name'] = local_var_params['queue_name']

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
            resource_path='/v1/{project_id}/queues/{queue_name}/plans/{plan_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteQueuePlanResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_resource(self, request):
        """删除组内资源包

        该API用于删除某个project某个分组下的资源包
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteResource
        :type request: :class:`huaweicloudsdkdli.v1.DeleteResourceRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.DeleteResourceResponse`
        """
        return self._delete_resource_with_http_info(request)

    def _delete_resource_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_name' in local_var_params:
            path_params['resource_name'] = local_var_params['resource_name']

        query_params = []
        if 'group' in local_var_params:
            query_params.append(('group', local_var_params['group']))

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
            resource_path='/v2.0/{project_id}/resources/{resource_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disassociate_connection_queue(self, request):
        """解绑队列

        该API用于在增强型跨源中解绑已绑定的队列。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisassociateConnectionQueue
        :type request: :class:`huaweicloudsdkdli.v1.DisassociateConnectionQueueRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.DisassociateConnectionQueueResponse`
        """
        return self._disassociate_connection_queue_with_http_info(request)

    def _disassociate_connection_queue_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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
            resource_path='/v2.0/{project_id}/datasource/enhanced-connections/{connection_id}/disassociate-queue',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisassociateConnectionQueueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_auth_info(self, request):
        """获取跨源认证列表

        该API用于查询跨源认证信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuthInfo
        :type request: :class:`huaweicloudsdkdli.v1.ListAuthInfoRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListAuthInfoResponse`
        """
        return self._list_auth_info_with_http_info(request)

    def _list_auth_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'auth_info_name' in local_var_params:
            query_params.append(('auth_info_name', local_var_params['auth_info_name']))
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
            resource_path='/v2.0/{project_id}/datasource/auth-infos',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAuthInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_database_users(self, request):
        """查看数据库的使用者

        该API用于查询可以使用的指定队列的所有用户名称。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDatabaseUsers
        :type request: :class:`huaweicloudsdkdli.v1.ListDatabaseUsersRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListDatabaseUsersResponse`
        """
        return self._list_database_users_with_http_info(request)

    def _list_database_users_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']

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
            resource_path='/v1.0/{project_id}/databases/{database_name}/users',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDatabaseUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_datasource_connections(self, request):
        """查询经典型跨源连接列表

        该API用于查询该用户已创建的经典型跨源连接列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDatasourceConnections
        :type request: :class:`huaweicloudsdkdli.v1.ListDatasourceConnectionsRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListDatasourceConnectionsResponse`
        """
        return self._list_datasource_connections_with_http_info(request)

    def _list_datasource_connections_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))

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
            resource_path='/v2.0/{project_id}/datasource-connection',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDatasourceConnectionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_elastic_resource_pool_queues(self, request):
        """查询弹性资源池所属队列

        查询弹性资源池所属队列
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListElasticResourcePoolQueues
        :type request: :class:`huaweicloudsdkdli.v1.ListElasticResourcePoolQueuesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListElasticResourcePoolQueuesResponse`
        """
        return self._list_elastic_resource_pool_queues_with_http_info(request)

    def _list_elastic_resource_pool_queues_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'elastic_resource_pool_name' in local_var_params:
            path_params['elastic_resource_pool_name'] = local_var_params['elastic_resource_pool_name']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'queue_name' in local_var_params:
            query_params.append(('queue_name', local_var_params['queue_name']))

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
            resource_path='/v3/{project_id}/elastic-resource-pools/{elastic_resource_pool_name}/queues',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListElasticResourcePoolQueuesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_elastic_resource_pool_scale_records(self, request):
        """弹性资源池扩缩容历史记录

        查询当前弹性资源池扩缩容历史记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListElasticResourcePoolScaleRecords
        :type request: :class:`huaweicloudsdkdli.v1.ListElasticResourcePoolScaleRecordsRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListElasticResourcePoolScaleRecordsResponse`
        """
        return self._list_elastic_resource_pool_scale_records_with_http_info(request)

    def _list_elastic_resource_pool_scale_records_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'elastic_resource_pool_name' in local_var_params:
            path_params['elastic_resource_pool_name'] = local_var_params['elastic_resource_pool_name']

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Auth-Token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elastic-resource-pools/{elastic_resource_pool_name}/scale-records',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListElasticResourcePoolScaleRecordsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_elastic_resource_pools(self, request):
        """查询所有弹性资源池

        查询所有弹性资源池
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListElasticResourcePools
        :type request: :class:`huaweicloudsdkdli.v1.ListElasticResourcePoolsRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListElasticResourcePoolsResponse`
        """
        return self._list_elastic_resource_pools_with_http_info(request)

    def _list_elastic_resource_pools_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))

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
            resource_path='/v3/{project_id}/elastic-resource-pools',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListElasticResourcePoolsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_enhanced_connections(self, request):
        """查询增强型跨源连接列表

        该API用于查询该用户已创建的增强型跨源连接列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEnhancedConnections
        :type request: :class:`huaweicloudsdkdli.v1.ListEnhancedConnectionsRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListEnhancedConnectionsResponse`
        """
        return self._list_enhanced_connections_with_http_info(request)

    def _list_enhanced_connections_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))

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
            resource_path='/v2.0/{project_id}/datasource/enhanced-connections',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEnhancedConnectionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_global_values(self, request):
        """查询DLI全局变量列表

        查询全局变量列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGlobalValues
        :type request: :class:`huaweicloudsdkdli.v1.ListGlobalValuesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListGlobalValuesResponse`
        """
        return self._list_global_values_with_http_info(request)

    def _list_global_values_with_http_info(self, request):
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
            resource_path='/v1.0/{project_id}/variables',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListGlobalValuesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_queue_plans(self, request):
        """查看队列定时扩缩容计划

        查看队列定时扩缩容计划接口，列出指定队列定时规格变更计划。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQueuePlans
        :type request: :class:`huaweicloudsdkdli.v1.ListQueuePlansRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListQueuePlansResponse`
        """
        return self._list_queue_plans_with_http_info(request)

    def _list_queue_plans_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'queue_name' in local_var_params:
            path_params['queue_name'] = local_var_params['queue_name']

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
            resource_path='/v1/{project_id}/queues/{queue_name}/plans',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListQueuePlansResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_queue_users(self, request):
        """查看队列的使用者

        该API用于查询可以使用的指定队列的所有用户名称。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQueueUsers
        :type request: :class:`huaweicloudsdkdli.v1.ListQueueUsersRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListQueueUsersResponse`
        """
        return self._list_queue_users_with_http_info(request)

    def _list_queue_users_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'queue_name' in local_var_params:
            path_params['queue_name'] = local_var_params['queue_name']

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
            resource_path='/v1.0/{project_id}/queues/{queue_name}/users',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListQueueUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_queues(self, request):
        """查询所有队列

        该API用于列出该project下所有的队列。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQueues
        :type request: :class:`huaweicloudsdkdli.v1.ListQueuesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListQueuesResponse`
        """
        return self._list_queues_with_http_info(request)

    def _list_queues_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'queue_type' in local_var_params:
            query_params.append(('queue_type', local_var_params['queue_type']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'with_charge_info' in local_var_params:
            query_params.append(('with-charge-info', local_var_params['with_charge_info']))
        if 'with_priv' in local_var_params:
            query_params.append(('with-priv', local_var_params['with_priv']))

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
            resource_path='/v1.0/{project_id}/queues',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListQueuesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_resources(self, request):
        """查看分组资源列表

        该API用于查看某个project下的所有资源，其中包含Group。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResources
        :type request: :class:`huaweicloudsdkdli.v1.ListResourcesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListResourcesResponse`
        """
        return self._list_resources_with_http_info(request)

    def _list_resources_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'kind' in local_var_params:
            query_params.append(('kind', local_var_params['kind']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))

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
            resource_path='/v2.0/{project_id}/resources',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_table_privileges(self, request):
        """查看表的用户权限

        该API用于查询指定用户在表上的权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTablePrivileges
        :type request: :class:`huaweicloudsdkdli.v1.ListTablePrivilegesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListTablePrivilegesResponse`
        """
        return self._list_table_privileges_with_http_info(request)

    def _list_table_privileges_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'table_name' in local_var_params:
            path_params['table_name'] = local_var_params['table_name']
        if 'user_name' in local_var_params:
            path_params['user_name'] = local_var_params['user_name']

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
            resource_path='/v1.0/{project_id}/databases/{database_name}/tables/{table_name}/users/{user_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTablePrivilegesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_table_users(self, request):
        """查看表的使用者

        该API用于查看有权访问指定表或表的列的所有用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTableUsers
        :type request: :class:`huaweicloudsdkdli.v1.ListTableUsersRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListTableUsersResponse`
        """
        return self._list_table_users_with_http_info(request)

    def _list_table_users_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'table_name' in local_var_params:
            path_params['table_name'] = local_var_params['table_name']

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
            resource_path='/v1.0/{project_id}/databases/{database_name}/tables/{table_name}/users',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTableUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def register_authorized_queue(self, request):
        """队列赋权

        该API用于与其他用户共享指定的队列，可以给用户赋使用指定的队列的权限或者收回使用权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RegisterAuthorizedQueue
        :type request: :class:`huaweicloudsdkdli.v1.RegisterAuthorizedQueueRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.RegisterAuthorizedQueueResponse`
        """
        return self._register_authorized_queue_with_http_info(request)

    def _register_authorized_queue_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/queues/user-authorization',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RegisterAuthorizedQueueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_queue_action(self, request):
        """重启/扩容/缩容队列

        该功能用于重新启动队列、扩容队列、缩容队列。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunQueueAction
        :type request: :class:`huaweicloudsdkdli.v1.RunQueueActionRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.RunQueueActionResponse`
        """
        return self._run_queue_action_with_http_info(request)

    def _run_queue_action_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'queue_name' in local_var_params:
            path_params['queue_name'] = local_var_params['queue_name']

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
            resource_path='/v1.0/{project_id}/queues/{queue_name}/action',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunQueueActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_datasource_connection(self, request):
        """查询经典型跨源连接

        该API用于查询该用户指定的已创建的经典型跨源连接。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDatasourceConnection
        :type request: :class:`huaweicloudsdkdli.v1.ShowDatasourceConnectionRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowDatasourceConnectionResponse`
        """
        return self._show_datasource_connection_with_http_info(request)

    def _show_datasource_connection_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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
            resource_path='/v2.0/{project_id}/datasource-connection/{connection_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDatasourceConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_dli_agency(self, request):
        """获取dli委托信息

        获取dli委托信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDliAgency
        :type request: :class:`huaweicloudsdkdli.v1.ShowDliAgencyRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowDliAgencyResponse`
        """
        return self._show_dli_agency_with_http_info(request)

    def _show_dli_agency_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/agency',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDliAgencyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_enhanced_connection(self, request):
        """查询增强型跨源连接

        该API用于查询该用户指定的已创建的增强型跨源连接。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEnhancedConnection
        :type request: :class:`huaweicloudsdkdli.v1.ShowEnhancedConnectionRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowEnhancedConnectionResponse`
        """
        return self._show_enhanced_connection_with_http_info(request)

    def _show_enhanced_connection_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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
            resource_path='/v2.0/{project_id}/datasource/enhanced-connections/{connection_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEnhancedConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_enhanced_privilege(self, request):
        """查询增强型跨源授权信息

        该API用于查询增强型跨源连接授权的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEnhancedPrivilege
        :type request: :class:`huaweicloudsdkdli.v1.ShowEnhancedPrivilegeRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowEnhancedPrivilegeResponse`
        """
        return self._show_enhanced_privilege_with_http_info(request)

    def _show_enhanced_privilege_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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
            resource_path='/v2.0/{project_id}/datasource/enhanced-connections/{connection_id}/privileges',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEnhancedPrivilegeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_node_connectivity(self, request):
        """查询指定地址连通性测试详情

        该API用于在连通性测试提交后查询连通性结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNodeConnectivity
        :type request: :class:`huaweicloudsdkdli.v1.ShowNodeConnectivityRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowNodeConnectivityResponse`
        """
        return self._show_node_connectivity_with_http_info(request)

    def _show_node_connectivity_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'queue_name' in local_var_params:
            path_params['queue_name'] = local_var_params['queue_name']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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
            resource_path='/v1.0/{project_id}/queues/{queue_name}/connection-test/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowNodeConnectivityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_object_user(self, request):
        """查看赋权对象的用者权限信息

        获取对象赋权用户的权限信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowObjectUser
        :type request: :class:`huaweicloudsdkdli.v1.ShowObjectUserRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowObjectUserResponse`
        """
        return self._show_object_user_with_http_info(request)

    def _show_object_user_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'object' in local_var_params:
            query_params.append(('object', local_var_params['object']))

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
            resource_path='/v1.0/{project_id}/authorization/privileges',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowObjectUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_queue_detail(self, request):
        """查询队列详情

        该API用于列出该project下指定的队列详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowQueueDetail
        :type request: :class:`huaweicloudsdkdli.v1.ShowQueueDetailRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowQueueDetailResponse`
        """
        return self._show_queue_detail_with_http_info(request)

    def _show_queue_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'queue_name' in local_var_params:
            path_params['queue_name'] = local_var_params['queue_name']

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
            resource_path='/v1.0/{project_id}/queues/{queue_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowQueueDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_resource_info(self, request):
        """查看组内资源包

        该API用于查看某个project某个分组下的具体资源信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowResourceInfo
        :type request: :class:`huaweicloudsdkdli.v1.ShowResourceInfoRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowResourceInfoResponse`
        """
        return self._show_resource_info_with_http_info(request)

    def _show_resource_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_name' in local_var_params:
            path_params['resource_name'] = local_var_params['resource_name']

        query_params = []
        if 'group' in local_var_params:
            query_params.append(('group', local_var_params['group']))

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
            resource_path='/v2.0/{project_id}/resources/{resource_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowResourceInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_auth_info(self, request):
        """更新跨源认证

        该API用于更新跨源认证信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAuthInfo
        :type request: :class:`huaweicloudsdkdli.v1.UpdateAuthInfoRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateAuthInfoResponse`
        """
        return self._update_auth_info_with_http_info(request)

    def _update_auth_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/datasource/auth-infos',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAuthInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_elastic_resource_pool(self, request):
        """修改弹性资源池信息

        修改弹性资源池信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateElasticResourcePool
        :type request: :class:`huaweicloudsdkdli.v1.UpdateElasticResourcePoolRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateElasticResourcePoolResponse`
        """
        return self._update_elastic_resource_pool_with_http_info(request)

    def _update_elastic_resource_pool_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'elastic_resource_pool_name' in local_var_params:
            path_params['elastic_resource_pool_name'] = local_var_params['elastic_resource_pool_name']

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
            resource_path='/v3/{project_id}/elastic-resource-pools/{elastic_resource_pool_name}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateElasticResourcePoolResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_elastic_resource_pool_queue_info(self, request):
        """修改弹性资源池关联的队列优先级

        设置弹性资源池指定队列的扩缩容策略信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateElasticResourcePoolQueueInfo
        :type request: :class:`huaweicloudsdkdli.v1.UpdateElasticResourcePoolQueueInfoRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateElasticResourcePoolQueueInfoResponse`
        """
        return self._update_elastic_resource_pool_queue_info_with_http_info(request)

    def _update_elastic_resource_pool_queue_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'elastic_resource_pool_name' in local_var_params:
            path_params['elastic_resource_pool_name'] = local_var_params['elastic_resource_pool_name']
        if 'queue_name' in local_var_params:
            path_params['queue_name'] = local_var_params['queue_name']

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
            resource_path='/v3/{project_id}/elastic-resource-pools/{elastic_resource_pool_name}/queues/{queue_name}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateElasticResourcePoolQueueInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_global_value(self, request):
        """修改DLI全局变量

        修改全局变量。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateGlobalValue
        :type request: :class:`huaweicloudsdkdli.v1.UpdateGlobalValueRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateGlobalValueResponse`
        """
        return self._update_global_value_with_http_info(request)

    def _update_global_value_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'var_name' in local_var_params:
            path_params['var_name'] = local_var_params['var_name']

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
            resource_path='/v1.0/{project_id}/variables/{var_name}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateGlobalValueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_group_or_resource_owner(self, request):
        """修改组或者资源包拥有者

        用于修改程序包的owner。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateGroupOrResourceOwner
        :type request: :class:`huaweicloudsdkdli.v1.UpdateGroupOrResourceOwnerRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateGroupOrResourceOwnerResponse`
        """
        return self._update_group_or_resource_owner_with_http_info(request)

    def _update_group_or_resource_owner_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/resources/owner',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateGroupOrResourceOwnerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_host_massage(self, request):
        """修改增强型跨源主机信息

        该API用于在跨源中修改数据源主机信息，仅支持全量覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateHostMassage
        :type request: :class:`huaweicloudsdkdli.v1.UpdateHostMassageRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateHostMassageResponse`
        """
        return self._update_host_massage_with_http_info(request)

    def _update_host_massage_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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
            resource_path='/v2.0/{project_id}/datasource/enhanced-connections/{connection_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateHostMassageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_queue_cidr(self, request):
        """修改队列网段

        该功能用于修改包年包月队列网段。
        说明：
        如果待修改网段的队列中有正在提交或正在运行的作业，或者改队列已经绑定了增强型跨源，将不支持修改网段操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateQueueCidr
        :type request: :class:`huaweicloudsdkdli.v1.UpdateQueueCidrRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateQueueCidrResponse`
        """
        return self._update_queue_cidr_with_http_info(request)

    def _update_queue_cidr_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'queue_name' in local_var_params:
            path_params['queue_name'] = local_var_params['queue_name']

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
            resource_path='/v1.0/{project_id}/queues/{queue_name}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateQueueCidrResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def upload_files(self, request):
        """上传file类型分组资源

        该API用于在project下上传file类型模块。
        说明： 上传同名file模块时，新模块将会覆盖旧模块。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadFiles
        :type request: :class:`huaweicloudsdkdli.v1.UploadFilesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UploadFilesResponse`
        """
        return self._upload_files_with_http_info(request)

    def _upload_files_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'user_id' in local_var_params:
            header_params['USER-ID'] = local_var_params['user_id']

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
            resource_path='/v2.0/{project_id}/resources/files',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UploadFilesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def upload_jars(self, request):
        """上传jar类型分组资源

        该API用于在project下上传jar类型分组资源。
        说明：上传同名资源模块时，新模块将会覆盖旧模块。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadJars
        :type request: :class:`huaweicloudsdkdli.v1.UploadJarsRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UploadJarsResponse`
        """
        return self._upload_jars_with_http_info(request)

    def _upload_jars_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'user_id' in local_var_params:
            header_params['USER-ID'] = local_var_params['user_id']

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
            resource_path='/v2.0/{project_id}/resources/jars',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UploadJarsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def upload_python_files(self, request):
        """上传pyfile类型分组资源

        该API用于在project下的上传pyfile类型模块。
        说明： 上传同名pyfile类型模块时，新模块将会覆盖旧模块。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadPythonFiles
        :type request: :class:`huaweicloudsdkdli.v1.UploadPythonFilesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UploadPythonFilesResponse`
        """
        return self._upload_python_files_with_http_info(request)

    def _upload_python_files_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'user_id' in local_var_params:
            header_params['USER-ID'] = local_var_params['user_id']

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
            resource_path='/v2.0/{project_id}/resources/pyfiles',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UploadPythonFilesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def upload_resources(self, request):
        """上传分组资源

        该API用于上传分组资源到某个project下。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadResources
        :type request: :class:`huaweicloudsdkdli.v1.UploadResourcesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UploadResourcesResponse`
        """
        return self._upload_resources_with_http_info(request)

    def _upload_resources_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'user_id' in local_var_params:
            header_params['USER-ID'] = local_var_params['user_id']

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
            resource_path='/v2.0/{project_id}/resources',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UploadResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_flink_jobs(self, request):
        """批量删除Flink作业

        批量删除任何状态的作业。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteFlinkJobs
        :type request: :class:`huaweicloudsdkdli.v1.BatchDeleteFlinkJobsRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.BatchDeleteFlinkJobsResponse`
        """
        return self._batch_delete_flink_jobs_with_http_info(request)

    def _batch_delete_flink_jobs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/streaming/jobs/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteFlinkJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_run_flink_jobs(self, request):
        """批量运行Flink作业

        触发批量运行Flink作业。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchRunFlinkJobs
        :type request: :class:`huaweicloudsdkdli.v1.BatchRunFlinkJobsRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.BatchRunFlinkJobsResponse`
        """
        return self._batch_run_flink_jobs_with_http_info(request)

    def _batch_run_flink_jobs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/streaming/jobs/run',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchRunFlinkJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_flink_job_status_report(self, request):
        """边缘Flink作业状态信息上报

        该API用于处理边缘Flink作业状态上报信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeFlinkJobStatusReport
        :type request: :class:`huaweicloudsdkdli.v1.ChangeFlinkJobStatusReportRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ChangeFlinkJobStatusReportResponse`
        """
        return self._change_flink_job_status_report_with_http_info(request)

    def _change_flink_job_status_report_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/edgesrv/job-report',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeFlinkJobStatusReportResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_flink_jar(self, request):
        """新建Flink Jar作业

        用户自定义作业目前支持jar格式，运行在独享集群中。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFlinkJar
        :type request: :class:`huaweicloudsdkdli.v1.CreateFlinkJarRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateFlinkJarResponse`
        """
        return self._create_flink_jar_with_http_info(request)

    def _create_flink_jar_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/streaming/flink-jobs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateFlinkJarResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_flink_sql_job(self, request):
        """新建Flink SQL作业

        通过POST方式，提交流式SQL作业，请求体为JSON格式。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFlinkSqlJob
        :type request: :class:`huaweicloudsdkdli.v1.CreateFlinkSqlJobRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateFlinkSqlJobResponse`
        """
        return self._create_flink_sql_job_with_http_info(request)

    def _create_flink_sql_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/streaming/sql-jobs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateFlinkSqlJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_flink_template(self, request):
        """新建Flink作业模板

        在DLI服务中新建一个Flink作业模板，最多100个。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFlinkTemplate
        :type request: :class:`huaweicloudsdkdli.v1.CreateFlinkTemplateRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateFlinkTemplateResponse`
        """
        return self._create_flink_template_with_http_info(request)

    def _create_flink_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/streaming/job-templates',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateFlinkTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_ief_message_channel(self, request):
        """创建IEF消息通道

        该API用于创建IEF消息通道
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateIefMessageChannel
        :type request: :class:`huaweicloudsdkdli.v1.CreateIefMessageChannelRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateIefMessageChannelResponse`
        """
        return self._create_ief_message_channel_with_http_info(request)

    def _create_ief_message_channel_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/edgesrv/message-channel',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateIefMessageChannelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_ief_system_events(self, request):
        """IEF系统事件上报

        该API用于处理IEF系统事件上报
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateIefSystemEvents
        :type request: :class:`huaweicloudsdkdli.v1.CreateIefSystemEventsRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateIefSystemEventsResponse`
        """
        return self._create_ief_system_events_with_http_info(request)

    def _create_ief_system_events_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/edgesrv/system-events',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateIefSystemEventsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_stream_graph(self, request):
        """生成flink SQL作业的静态流图

        生成flink SQL作业的静态流图
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateStreamGraph
        :type request: :class:`huaweicloudsdkdli.v1.CreateStreamGraphRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateStreamGraphResponse`
        """
        return self._create_stream_graph_with_http_info(request)

    def _create_stream_graph_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v3/{project_id}/streaming/jobs/{job_id}/gen-graph',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateStreamGraphResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_flink_job(self, request):
        """删除作业

        删除任何状态的作业。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteFlinkJob
        :type request: :class:`huaweicloudsdkdli.v1.DeleteFlinkJobRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.DeleteFlinkJobResponse`
        """
        return self._delete_flink_job_with_http_info(request)

    def _delete_flink_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1.0/{project_id}/streaming/jobs/{job_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteFlinkJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_flink_template(self, request):
        """删除Flink作业模板

        删除一个Flink作业模板，即使当前模板正在被作业使用，也允许删除。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteFlinkTemplate
        :type request: :class:`huaweicloudsdkdli.v1.DeleteFlinkTemplateRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.DeleteFlinkTemplateResponse`
        """
        return self._delete_flink_template_with_http_info(request)

    def _delete_flink_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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
            resource_path='/v1.0/{project_id}/streaming/job-templates/{template_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteFlinkTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def export_flink_job(self, request):
        """flink作业导出

        通过POST方式，导出flink作业，请求体为JSON格式。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportFlinkJob
        :type request: :class:`huaweicloudsdkdli.v1.ExportFlinkJobRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ExportFlinkJobResponse`
        """
        return self._export_flink_job_with_http_info(request)

    def _export_flink_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/streaming/jobs/export',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExportFlinkJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def import_flink_job(self, request):
        """flink作业导入

        通过POST方式，导入flink作业，请求体为JSON格式。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportFlinkJob
        :type request: :class:`huaweicloudsdkdli.v1.ImportFlinkJobRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ImportFlinkJobResponse`
        """
        return self._import_flink_job_with_http_info(request)

    def _import_flink_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/streaming/jobs/import',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ImportFlinkJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_flink_jobs(self, request):
        """查询Flink作业列表

        查询当前用户的作业列表，可以根据作业ID作为ID，查询大于ID或小于ID的限定条数的作业，默认查询全部状态的作业，也可以设定运行中或其他状态条件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFlinkJobs
        :type request: :class:`huaweicloudsdkdli.v1.ListFlinkJobsRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListFlinkJobsResponse`
        """
        return self._list_flink_jobs_with_http_info(request)

    def _list_flink_jobs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_type' in local_var_params:
            query_params.append(('job_type', local_var_params['job_type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'queue_name' in local_var_params:
            query_params.append(('queue_name', local_var_params['queue_name']))
        if 'root_job_id' in local_var_params:
            query_params.append(('root_job_id', local_var_params['root_job_id']))
        if 'show_detail' in local_var_params:
            query_params.append(('show_detail', local_var_params['show_detail']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'sys_enterprise_project_name' in local_var_params:
            query_params.append(('sys_enterprise_project_name', local_var_params['sys_enterprise_project_name']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))

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
            resource_path='/v1.0/{project_id}/streaming/jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFlinkJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_flink_templates(self, request):
        """查询Flink作业模板列表

        查询Flink作业模板列表。当前只支持查询用户自定义模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFlinkTemplates
        :type request: :class:`huaweicloudsdkdli.v1.ListFlinkTemplatesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListFlinkTemplatesResponse`
        """
        return self._list_flink_templates_with_http_info(request)

    def _list_flink_templates_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))

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
            resource_path='/v1.0/{project_id}/streaming/job-templates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFlinkTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def register_bucket(self, request):
        """OBS授权给DLI服务

        用户主动授权OBS桶的操作权限给DLI服务, 用于保存用户作业的checkpoint、作业的运行日志等。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RegisterBucket
        :type request: :class:`huaweicloudsdkdli.v1.RegisterBucketRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.RegisterBucketResponse`
        """
        return self._register_bucket_with_http_info(request)

    def _register_bucket_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/dli/obs-authorize',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RegisterBucketResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_ief_job_action_call_back(self, request):
        """边缘Flink作业Action状态回调

        该API用于处理IEF Flink作业action回调信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunIefJobActionCallBack
        :type request: :class:`huaweicloudsdkdli.v1.RunIefJobActionCallBackRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.RunIefJobActionCallBackResponse`
        """
        return self._run_ief_job_action_call_back_with_http_info(request)

    def _run_ief_job_action_call_back_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/edgesrv/messages',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunIefJobActionCallBackResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_flink_execute_graph(self, request):
        """查询Flink作业执行计划

        查询Flink作业执行计划。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFlinkExecuteGraph
        :type request: :class:`huaweicloudsdkdli.v1.ShowFlinkExecuteGraphRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowFlinkExecuteGraphResponse`
        """
        return self._show_flink_execute_graph_with_http_info(request)

    def _show_flink_execute_graph_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1.0/{project_id}/streaming/jobs/{job_id}/execute-graph',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowFlinkExecuteGraphResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_flink_job(self, request):
        """查询Flink作业详情

        查看一个Flink作业的详情信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFlinkJob
        :type request: :class:`huaweicloudsdkdli.v1.ShowFlinkJobRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowFlinkJobResponse`
        """
        return self._show_flink_job_with_http_info(request)

    def _show_flink_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1.0/{project_id}/streaming/jobs/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowFlinkJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_flink_metric(self, request):
        """查询Flink作业监控信息

        查询Flink作业监控信息, 支持同时查询多个Flink作业的监控信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFlinkMetric
        :type request: :class:`huaweicloudsdkdli.v1.ShowFlinkMetricRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowFlinkMetricResponse`
        """
        return self._show_flink_metric_with_http_info(request)

    def _show_flink_metric_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/streaming/jobs/metrics',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowFlinkMetricResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_flink_jobs(self, request):
        """批量停止Flink作业

        批量停止正在运行的Flink作业。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopFlinkJobs
        :type request: :class:`huaweicloudsdkdli.v1.StopFlinkJobsRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.StopFlinkJobsResponse`
        """
        return self._stop_flink_jobs_with_http_info(request)

    def _stop_flink_jobs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/streaming/jobs/stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopFlinkJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_flink_jar(self, request):
        """更新Flink Jar作业

        更新用户自定义作业，目前支持jar格式，运行在独享集群中。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateFlinkJar
        :type request: :class:`huaweicloudsdkdli.v1.UpdateFlinkJarRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateFlinkJarResponse`
        """
        return self._update_flink_jar_with_http_info(request)

    def _update_flink_jar_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1.0/{project_id}/streaming/flink-jobs/{job_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateFlinkJarResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_flink_sql(self, request):
        """更新Flink SQL作业

        Stream SQL的语法扩展了Apache Flink SQL。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateFlinkSql
        :type request: :class:`huaweicloudsdkdli.v1.UpdateFlinkSqlRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateFlinkSqlResponse`
        """
        return self._update_flink_sql_with_http_info(request)

    def _update_flink_sql_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1.0/{project_id}/streaming/sql-jobs/{job_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateFlinkSqlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_flink_template(self, request):
        """更新Flink作业模板

        对DLI服务中已有的Flink作业模板进行更新。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateFlinkTemplate
        :type request: :class:`huaweicloudsdkdli.v1.UpdateFlinkTemplateRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateFlinkTemplateResponse`
        """
        return self._update_flink_template_with_http_info(request)

    def _update_flink_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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
            resource_path='/v1.0/{project_id}/streaming/job-templates/{template_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateFlinkTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cancel_sql_job(self, request):
        """取消作业

        该API用于取消已经提交的作业，若作业已经执行结束或失败则无法取消。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelSqlJob
        :type request: :class:`huaweicloudsdkdli.v1.CancelSqlJobRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CancelSqlJobResponse`
        """
        return self._cancel_sql_job_with_http_info(request)

    def _cancel_sql_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1.0/{project_id}/jobs/{job_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CancelSqlJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_sql(self, request):
        """检查SQL语法

        该API用于检查SQL语法。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckSql
        :type request: :class:`huaweicloudsdkdli.v1.CheckSqlRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CheckSqlResponse`
        """
        return self._check_sql_with_http_info(request)

    def _check_sql_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/jobs/check-sql',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CheckSqlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_database(self, request):
        """创建数据库

        该API用于新增数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDatabase
        :type request: :class:`huaweicloudsdkdli.v1.CreateDatabaseRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateDatabaseResponse`
        """
        return self._create_database_with_http_info(request)

    def _create_database_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/databases',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDatabaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_sql_job(self, request):
        """提交SQL作业

        该API用于通过执行SQL语句的方式向队列提交作业。
        
        作业包含以下类型：DDL、DCL、IMPORT、QUERY和INSERT。其中，IMPORT与导入数据的功能一致，区别仅在于实现方式不同。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSqlJob
        :type request: :class:`huaweicloudsdkdli.v1.CreateSqlJobRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateSqlJobResponse`
        """
        return self._create_sql_job_with_http_info(request)

    def _create_sql_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/jobs/submit-job',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSqlJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_table(self, request):
        """创建表

        该API用于创建新的表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTable
        :type request: :class:`huaweicloudsdkdli.v1.CreateTableRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateTableResponse`
        """
        return self._create_table_with_http_info(request)

    def _create_table_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']

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
            resource_path='/v1.0/{project_id}/databases/{database_name}/tables',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_database(self, request):
        """删除数据库

        该API用于删除空数据库，若待删除的数据库中存在表，则需先删除其中的所有表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDatabase
        :type request: :class:`huaweicloudsdkdli.v1.DeleteDatabaseRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.DeleteDatabaseResponse`
        """
        return self._delete_database_with_http_info(request)

    def _delete_database_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']

        query_params = []
        if '_async' in local_var_params:
            query_params.append(('async', local_var_params['_async']))
        if 'cascade' in local_var_params:
            query_params.append(('cascade', local_var_params['cascade']))

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
            resource_path='/v1.0/{project_id}/databases/{database_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDatabaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_table(self, request):
        """删除表

        该API用于删除指定的表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTable
        :type request: :class:`huaweicloudsdkdli.v1.DeleteTableRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.DeleteTableResponse`
        """
        return self._delete_table_with_http_info(request)

    def _delete_table_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'table_name' in local_var_params:
            path_params['table_name'] = local_var_params['table_name']

        query_params = []
        if '_async' in local_var_params:
            query_params.append(('async', local_var_params['_async']))

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
            resource_path='/v1.0/{project_id}/databases/{database_name}/tables/{table_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def export_sql_job_result(self, request):
        """导出查询结果

        该API用于将SQL语句的查询结果导出到OBS对象存储中，只支持导出“QUERY”类型作业的查询结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportSqlJobResult
        :type request: :class:`huaweicloudsdkdli.v1.ExportSqlJobResultRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ExportSqlJobResultResponse`
        """
        return self._export_sql_job_result_with_http_info(request)

    def _export_sql_job_result_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1.0/{project_id}/jobs/{job_id}/export-result',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExportSqlJobResultResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def export_table(self, request):
        """导出查询结果

        该API用于将SQL语句的查询结果导出到OBS对象存储中，只支持导出“QUERY”类型作业的查询结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportTable
        :type request: :class:`huaweicloudsdkdli.v1.ExportTableRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ExportTableResponse`
        """
        return self._export_table_with_http_info(request)

    def _export_table_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/jobs/export-table',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExportTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def import_table(self, request):
        """导入数据

        该API用于将数据从文件导入DLI或OBS表，目前仅支持将OBS上的数据导入DLI或OBS中。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportTable
        :type request: :class:`huaweicloudsdkdli.v1.ImportTableRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ImportTableResponse`
        """
        return self._import_table_with_http_info(request)

    def _import_table_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/jobs/import-table',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ImportTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_all_tables(self, request):
        """查询所有表

        该API用于查询指定数据库下符合过滤条件的或所有的表信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAllTables
        :type request: :class:`huaweicloudsdkdli.v1.ListAllTablesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListAllTablesResponse`
        """
        return self._list_all_tables_with_http_info(request)

    def _list_all_tables_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']

        query_params = []
        if 'current_page' in local_var_params:
            query_params.append(('current-page', local_var_params['current_page']))
        if 'keyword' in local_var_params:
            query_params.append(('keyword', local_var_params['keyword']))
        if 'page_size' in local_var_params:
            query_params.append(('page-size', local_var_params['page_size']))
        if 'table_type' in local_var_params:
            query_params.append(('table-type', local_var_params['table_type']))
        if 'with_detail' in local_var_params:
            query_params.append(('with-detail', local_var_params['with_detail']))
        if 'with_priv' in local_var_params:
            query_params.append(('with-priv', local_var_params['with_priv']))

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
            resource_path='/v1.0/{project_id}/databases/{database_name}/tables',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAllTablesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_databases(self, request):
        """查询所有数据库

        该API用于查询出所有的数据库信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDatabases
        :type request: :class:`huaweicloudsdkdli.v1.ListDatabasesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListDatabasesResponse`
        """
        return self._list_databases_with_http_info(request)

    def _list_databases_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in local_var_params:
            query_params.append(('keyword', local_var_params['keyword']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'with_priv' in local_var_params:
            query_params.append(('with-priv', local_var_params['with_priv']))

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
            resource_path='/v1.0/{project_id}/databases',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDatabasesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_sql_jobs(self, request):
        """查询所有作业

        该API用于查询当前工程下面的所有作业的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSqlJobs
        :type request: :class:`huaweicloudsdkdli.v1.ListSqlJobsRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListSqlJobsResponse`
        """
        return self._list_sql_jobs_with_http_info(request)

    def _list_sql_jobs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'current_page' in local_var_params:
            query_params.append(('current-page', local_var_params['current_page']))
        if 'db_name' in local_var_params:
            query_params.append(('db_name', local_var_params['db_name']))
        if 'end' in local_var_params:
            query_params.append(('end', local_var_params['end']))
        if 'engine_type' in local_var_params:
            query_params.append(('engine-type', local_var_params['engine_type']))
        if 'job_status' in local_var_params:
            query_params.append(('job-status', local_var_params['job_status']))
        if 'job_type' in local_var_params:
            query_params.append(('job-type', local_var_params['job_type']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'owner' in local_var_params:
            query_params.append(('owner', local_var_params['owner']))
        if 'page_size' in local_var_params:
            query_params.append(('page-size', local_var_params['page_size']))
        if 'queue_name' in local_var_params:
            query_params.append(('queue_name', local_var_params['queue_name']))
        if 'sql_pattern' in local_var_params:
            query_params.append(('sql_pattern', local_var_params['sql_pattern']))
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))
        if 'table_name' in local_var_params:
            query_params.append(('table_name', local_var_params['table_name']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))

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
            resource_path='/v1.0/{project_id}/jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSqlJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def preview_job_result(self, request):
        """预览SQL作业查询结果

        该API用于在执行SQL查询语句的作业完成后，查看该作业执行的结果。目前仅支持查看“QUERY”类型作业的执行结果。
        该API只能查看前1000条的结果记录，若要查看全部的结果记录，需要先导出查询结果再进行查看。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PreviewJobResult
        :type request: :class:`huaweicloudsdkdli.v1.PreviewJobResultRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.PreviewJobResultResponse`
        """
        return self._preview_job_result_with_http_info(request)

    def _preview_job_result_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'queue_name' in local_var_params:
            query_params.append(('queue-name', local_var_params['queue_name']))

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
            resource_path='/v1.0/{project_id}/jobs/{job_id}/preview',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='PreviewJobResultResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_describe_table(self, request):
        """描述表信息

        该API用于描述指定表的元数据信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDescribeTable
        :type request: :class:`huaweicloudsdkdli.v1.ShowDescribeTableRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowDescribeTableResponse`
        """
        return self._show_describe_table_with_http_info(request)

    def _show_describe_table_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'table_name' in local_var_params:
            path_params['table_name'] = local_var_params['table_name']

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
            resource_path='/v1.0/{project_id}/databases/{database_name}/tables/{table_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDescribeTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job_progress(self, request):
        """查询作业执行进度信息

        该API用于获取作业执行进度信息，如果作业正在执行，可以获取到子作业的信息，如果作业刚开始或者已经结束，不可以获取到子作业信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJobProgress
        :type request: :class:`huaweicloudsdkdli.v1.ShowJobProgressRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowJobProgressResponse`
        """
        return self._show_job_progress_with_http_info(request)

    def _show_job_progress_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1/{project_id}/jobs/{job_id}/progress',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowJobProgressResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_partitions(self, request):
        """获取分区信息列表

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPartitions
        :type request: :class:`huaweicloudsdkdli.v1.ShowPartitionsRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowPartitionsResponse`
        """
        return self._show_partitions_with_http_info(request)

    def _show_partitions_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'table_name' in local_var_params:
            path_params['table_name'] = local_var_params['table_name']

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
            resource_path='/v1.0/{project_id}/databases/{database_name}/tables/{table_name}/partitions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPartitionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_sql_job_detail(self, request):
        """查询作业详细信息

        该API用于查询作业的详细信息，如作业的databasename、tablename、file size和export mode等信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSqlJobDetail
        :type request: :class:`huaweicloudsdkdli.v1.ShowSqlJobDetailRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowSqlJobDetailResponse`
        """
        return self._show_sql_job_detail_with_http_info(request)

    def _show_sql_job_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1.0/{project_id}/jobs/{job_id}/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSqlJobDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_sql_job_status(self, request):
        """查询作业状态

        该API用于在作业提交后查询作业状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSqlJobStatus
        :type request: :class:`huaweicloudsdkdli.v1.ShowSqlJobStatusRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowSqlJobStatusResponse`
        """
        return self._show_sql_job_status_with_http_info(request)

    def _show_sql_job_status_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1.0/{project_id}/jobs/{job_id}/status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSqlJobStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_table_content(self, request):
        """预览表内容

        该API用于用于预览表中前10行的内容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTableContent
        :type request: :class:`huaweicloudsdkdli.v1.ShowTableContentRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowTableContentResponse`
        """
        return self._show_table_content_with_http_info(request)

    def _show_table_content_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'table_name' in local_var_params:
            path_params['table_name'] = local_var_params['table_name']

        query_params = []
        if 'mode' in local_var_params:
            query_params.append(('mode', local_var_params['mode']))

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
            resource_path='/v1.0/{project_id}/databases/{database_name}/tables/{table_name}/preview',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTableContentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_database_owner(self, request):
        """修改数据库用户

        用于修改数据库的owner。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDatabaseOwner
        :type request: :class:`huaweicloudsdkdli.v1.UpdateDatabaseOwnerRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateDatabaseOwnerResponse`
        """
        return self._update_database_owner_with_http_info(request)

    def _update_database_owner_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']

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
            resource_path='/v1.0/{project_id}/databases/{database_name}/owner',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDatabaseOwnerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_table_owner(self, request):
        """修改表用户

        用于修改表的owner。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTableOwner
        :type request: :class:`huaweicloudsdkdli.v1.UpdateTableOwnerRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateTableOwnerResponse`
        """
        return self._update_table_owner_with_http_info(request)

    def _update_table_owner_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']
        if 'table_name' in local_var_params:
            path_params['table_name'] = local_var_params['table_name']

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
            resource_path='/v1.0/{project_id}/databases/{database_name}/tables/{table_name}/owner',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateTableOwnerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cancel_batch_job(self, request):
        """取消批处理作业

        该API用于取消批处理作业。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelBatchJob
        :type request: :class:`huaweicloudsdkdli.v1.CancelBatchJobRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CancelBatchJobResponse`
        """
        return self._cancel_batch_job_with_http_info(request)

    def _cancel_batch_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'batch_id' in local_var_params:
            path_params['batch_id'] = local_var_params['batch_id']

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
            resource_path='/v2.0/{project_id}/batches/{batch_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CancelBatchJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_batch_job(self, request):
        """创建批处理作业

        该API用于在某个队列上创建作业。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateBatchJob
        :type request: :class:`huaweicloudsdkdli.v1.CreateBatchJobRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateBatchJobResponse`
        """
        return self._create_batch_job_with_http_info(request)

    def _create_batch_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'user_id' in local_var_params:
            header_params['USER-ID'] = local_var_params['user_id']

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
            resource_path='/v2.0/{project_id}/batches',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateBatchJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_batches(self, request):
        """查询批处理作业列表

        该API用于查询Project下某队列批处理作业的列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBatches
        :type request: :class:`huaweicloudsdkdli.v1.ListBatchesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListBatchesResponse`
        """
        return self._list_batches_with_http_info(request)

    def _list_batches_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cluster_name' in local_var_params:
            query_params.append(('cluster_name', local_var_params['cluster_name']))
        if 'end' in local_var_params:
            query_params.append(('end', local_var_params['end']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'job_name' in local_var_params:
            query_params.append(('job-name', local_var_params['job_name']))
        if 'job_id' in local_var_params:
            query_params.append(('job-id', local_var_params['job_id']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'queue_name' in local_var_params:
            query_params.append(('queue_name', local_var_params['queue_name']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))

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
            resource_path='/v2.0/{project_id}/batches',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBatchesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_batch_info(self, request):
        """查询批处理作业详情

        该API用于根据批处理作业的id查询作业详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBatchInfo
        :type request: :class:`huaweicloudsdkdli.v1.ShowBatchInfoRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowBatchInfoResponse`
        """
        return self._show_batch_info_with_http_info(request)

    def _show_batch_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'batch_id' in local_var_params:
            path_params['batch_id'] = local_var_params['batch_id']

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
            resource_path='/v2.0/{project_id}/batches/{batch_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowBatchInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_batch_log(self, request):
        """查询批处理作业日志

        该API用于查询批处理作业的后台日志。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBatchLog
        :type request: :class:`huaweicloudsdkdli.v1.ShowBatchLogRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowBatchLogResponse`
        """
        return self._show_batch_log_with_http_info(request)

    def _show_batch_log_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'batch_id' in local_var_params:
            path_params['batch_id'] = local_var_params['batch_id']

        query_params = []
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'index' in local_var_params:
            query_params.append(('index', local_var_params['index']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))
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
            resource_path='/v2.0/{project_id}/batches/{batch_id}/log',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowBatchLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_batch_state(self, request):
        """查询批处理作业状态

        该API用于查询批处理作业的状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBatchState
        :type request: :class:`huaweicloudsdkdli.v1.ShowBatchStateRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowBatchStateResponse`
        """
        return self._show_batch_state_with_http_info(request)

    def _show_batch_state_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'batch_id' in local_var_params:
            path_params['batch_id'] = local_var_params['batch_id']

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
            resource_path='/v2.0/{project_id}/batches/{batch_id}/state',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowBatchStateResponse',
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
