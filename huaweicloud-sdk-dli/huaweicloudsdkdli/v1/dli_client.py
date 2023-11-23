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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkdli'")


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

    def batch_delete_sql_job_templates(self, request):
        """批量删除SQL模板

        该API用于批量删除SQL模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteSqlJobTemplates
        :type request: :class:`huaweicloudsdkdli.v1.BatchDeleteSqlJobTemplatesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.BatchDeleteSqlJobTemplatesResponse`
        """
        http_info = self._batch_delete_sql_job_templates_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_sql_job_templates_invoker(self, request):
        http_info = self._batch_delete_sql_job_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_sql_job_templates_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/sqls-deletion",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteSqlJobTemplatesResponse"
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

    def create_spark_job_template(self, request):
        """创建作业模板

        该API用于创建作业模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSparkJobTemplate
        :type request: :class:`huaweicloudsdkdli.v1.CreateSparkJobTemplateRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateSparkJobTemplateResponse`
        """
        http_info = self._create_spark_job_template_http_info(request)
        return self._call_api(**http_info)

    def create_spark_job_template_invoker(self, request):
        http_info = self._create_spark_job_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_spark_job_template_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/templates",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSparkJobTemplateResponse"
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

    def create_sql_job_template(self, request):
        """存储指定SQL语句

        该API用于存储指定的SQL语句，后续可以重复使用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSqlJobTemplate
        :type request: :class:`huaweicloudsdkdli.v1.CreateSqlJobTemplateRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateSqlJobTemplateResponse`
        """
        http_info = self._create_sql_job_template_http_info(request)
        return self._call_api(**http_info)

    def create_sql_job_template_invoker(self, request):
        http_info = self._create_sql_job_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_sql_job_template_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/sqls",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSqlJobTemplateResponse"
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

    def list_spark_job_templates(self, request):
        """查询作业模板列表

        该API用于查询作业模板列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSparkJobTemplates
        :type request: :class:`huaweicloudsdkdli.v1.ListSparkJobTemplatesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListSparkJobTemplatesResponse`
        """
        http_info = self._list_spark_job_templates_http_info(request)
        return self._call_api(**http_info)

    def list_spark_job_templates_invoker(self, request):
        http_info = self._list_spark_job_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_spark_job_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListSparkJobTemplatesResponse"
            }

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

    def list_sql_job_templates(self, request):
        """查看所有SQL模板

        该API用查看用户保存的所有SQL模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSqlJobTemplates
        :type request: :class:`huaweicloudsdkdli.v1.ListSqlJobTemplatesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListSqlJobTemplatesResponse`
        """
        http_info = self._list_sql_job_templates_http_info(request)
        return self._call_api(**http_info)

    def list_sql_job_templates_invoker(self, request):
        http_info = self._list_sql_job_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sql_job_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/sqls",
            "request_type": request.__class__.__name__,
            "response_type": "ListSqlJobTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in local_var_params:
            query_params.append(('keyword', local_var_params['keyword']))

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

    def show_spark_job_template(self, request):
        """获取作业模板

        该API用于获取作业模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSparkJobTemplate
        :type request: :class:`huaweicloudsdkdli.v1.ShowSparkJobTemplateRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowSparkJobTemplateResponse`
        """
        http_info = self._show_spark_job_template_http_info(request)
        return self._call_api(**http_info)

    def show_spark_job_template_invoker(self, request):
        http_info = self._show_spark_job_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_spark_job_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSparkJobTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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

    def show_sql_sample_templates(self, request):
        """查询所有SQL样例模板

        该API用于查询所有SQL样例模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSqlSampleTemplates
        :type request: :class:`huaweicloudsdkdli.v1.ShowSqlSampleTemplatesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowSqlSampleTemplatesResponse`
        """
        http_info = self._show_sql_sample_templates_http_info(request)
        return self._call_api(**http_info)

    def show_sql_sample_templates_invoker(self, request):
        http_info = self._show_sql_sample_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sql_sample_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/sqls/sample",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSqlSampleTemplatesResponse"
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

    def update_spark_job_template(self, request):
        """修改作业模板

        该API用于修改作业模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSparkJobTemplate
        :type request: :class:`huaweicloudsdkdli.v1.UpdateSparkJobTemplateRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateSparkJobTemplateResponse`
        """
        http_info = self._update_spark_job_template_http_info(request)
        return self._call_api(**http_info)

    def update_spark_job_template_invoker(self, request):
        http_info = self._update_spark_job_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_spark_job_template_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSparkJobTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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

    def update_sql_job_template(self, request):
        """更新SQL模板

        该API用于更新SQL模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSqlJobTemplate
        :type request: :class:`huaweicloudsdkdli.v1.UpdateSqlJobTemplateRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateSqlJobTemplateResponse`
        """
        http_info = self._update_sql_job_template_http_info(request)
        return self._call_api(**http_info)

    def update_sql_job_template_invoker(self, request):
        http_info = self._update_sql_job_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_sql_job_template_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/sqls/{sql_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSqlJobTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sql_id' in local_var_params:
            path_params['sql_id'] = local_var_params['sql_id']

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

    def associate_queue_to_elastic_resource_pool(self, request):
        """关联队列到弹性资源池

        关联队列到弹性资源池
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateQueueToElasticResourcePool
        :type request: :class:`huaweicloudsdkdli.v1.AssociateQueueToElasticResourcePoolRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.AssociateQueueToElasticResourcePoolResponse`
        """
        http_info = self._associate_queue_to_elastic_resource_pool_http_info(request)
        return self._call_api(**http_info)

    def associate_queue_to_elastic_resource_pool_invoker(self, request):
        http_info = self._associate_queue_to_elastic_resource_pool_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _associate_queue_to_elastic_resource_pool_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/elastic-resource-pools/{elastic_resource_pool_name}/queues",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateQueueToElasticResourcePoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'elastic_resource_pool_name' in local_var_params:
            path_params['elastic_resource_pool_name'] = local_var_params['elastic_resource_pool_name']

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

    def associate_queue_to_enhanced_connection(self, request):
        """绑定队列

        该API用于在已创建的增强型跨源中绑定队列。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateQueueToEnhancedConnection
        :type request: :class:`huaweicloudsdkdli.v1.AssociateQueueToEnhancedConnectionRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.AssociateQueueToEnhancedConnectionResponse`
        """
        http_info = self._associate_queue_to_enhanced_connection_http_info(request)
        return self._call_api(**http_info)

    def associate_queue_to_enhanced_connection_invoker(self, request):
        http_info = self._associate_queue_to_enhanced_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _associate_queue_to_enhanced_connection_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/datasource/enhanced-connections/{connection_id}/associate-queue",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateQueueToEnhancedConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def batch_delete_queue_plans(self, request):
        """批量删除队列定时扩缩容计划

        该API用于批量删除队列定时扩缩容计划。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteQueuePlans
        :type request: :class:`huaweicloudsdkdli.v1.BatchDeleteQueuePlansRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.BatchDeleteQueuePlansResponse`
        """
        http_info = self._batch_delete_queue_plans_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_queue_plans_invoker(self, request):
        http_info = self._batch_delete_queue_plans_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_queue_plans_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/queues/{queue_name}/plans/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteQueuePlansResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'queue_name' in local_var_params:
            path_params['queue_name'] = local_var_params['queue_name']

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
        http_info = self._change_authorization_http_info(request)
        return self._call_api(**http_info)

    def change_authorization_invoker(self, request):
        http_info = self._change_authorization_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_authorization_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/user-authorization",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeAuthorizationResponse"
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

    def change_queue_plan(self, request):
        """修改队列定时扩缩容计划

        该API用于修改指定ID的队列定时扩缩容计划。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeQueuePlan
        :type request: :class:`huaweicloudsdkdli.v1.ChangeQueuePlanRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ChangeQueuePlanResponse`
        """
        http_info = self._change_queue_plan_http_info(request)
        return self._call_api(**http_info)

    def change_queue_plan_invoker(self, request):
        http_info = self._change_queue_plan_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_queue_plan_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/queues/{queue_name}/plans/{plan_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeQueuePlanResponse"
            }

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

    def create_auth_info(self, request):
        """创建跨源认证

        该API用于创建跨源认证。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAuthInfo
        :type request: :class:`huaweicloudsdkdli.v1.CreateAuthInfoRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateAuthInfoResponse`
        """
        http_info = self._create_auth_info_http_info(request)
        return self._call_api(**http_info)

    def create_auth_info_invoker(self, request):
        http_info = self._create_auth_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_auth_info_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/datasource/auth-infos",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAuthInfoResponse"
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

    def create_connectivity_task(self, request):
        """创建地址连通性请求

        创建地址连通性请求API接口，往指定集群发送地址连通性测试请求，并将测试地址插入表内
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateConnectivityTask
        :type request: :class:`huaweicloudsdkdli.v1.CreateConnectivityTaskRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateConnectivityTaskResponse`
        """
        http_info = self._create_connectivity_task_http_info(request)
        return self._call_api(**http_info)

    def create_connectivity_task_invoker(self, request):
        http_info = self._create_connectivity_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_connectivity_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/queues/{queue_name}/connection-test",
            "request_type": request.__class__.__name__,
            "response_type": "CreateConnectivityTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'queue_name' in local_var_params:
            path_params['queue_name'] = local_var_params['queue_name']

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
        http_info = self._create_datasource_connection_http_info(request)
        return self._call_api(**http_info)

    def create_datasource_connection_invoker(self, request):
        http_info = self._create_datasource_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_datasource_connection_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/datasource-connection",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDatasourceConnectionResponse"
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

    def create_dli_agency(self, request):
        """创建DLI委托

        创建DLI委托
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDliAgency
        :type request: :class:`huaweicloudsdkdli.v1.CreateDliAgencyRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateDliAgencyResponse`
        """
        http_info = self._create_dli_agency_http_info(request)
        return self._call_api(**http_info)

    def create_dli_agency_invoker(self, request):
        http_info = self._create_dli_agency_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_dli_agency_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/agency",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDliAgencyResponse"
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

    def create_elastic_resource_pool(self, request):
        """创建弹性资源池

        创建弹性资源池
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateElasticResourcePool
        :type request: :class:`huaweicloudsdkdli.v1.CreateElasticResourcePoolRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateElasticResourcePoolResponse`
        """
        http_info = self._create_elastic_resource_pool_http_info(request)
        return self._call_api(**http_info)

    def create_elastic_resource_pool_invoker(self, request):
        http_info = self._create_elastic_resource_pool_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_elastic_resource_pool_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/elastic-resource-pools",
            "request_type": request.__class__.__name__,
            "response_type": "CreateElasticResourcePoolResponse"
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

    def create_enhanced_connection(self, request):
        """创建增强型跨源连接

        该API用于创建与其他服务的增强型跨源连接。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEnhancedConnection
        :type request: :class:`huaweicloudsdkdli.v1.CreateEnhancedConnectionRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateEnhancedConnectionResponse`
        """
        http_info = self._create_enhanced_connection_http_info(request)
        return self._call_api(**http_info)

    def create_enhanced_connection_invoker(self, request):
        http_info = self._create_enhanced_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_enhanced_connection_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/datasource/enhanced-connections",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEnhancedConnectionResponse"
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

    def create_enhanced_connection_routes(self, request):
        """创建路由

        该API用于创建跨源需要的路由。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEnhancedConnectionRoutes
        :type request: :class:`huaweicloudsdkdli.v1.CreateEnhancedConnectionRoutesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateEnhancedConnectionRoutesResponse`
        """
        http_info = self._create_enhanced_connection_routes_http_info(request)
        return self._call_api(**http_info)

    def create_enhanced_connection_routes_invoker(self, request):
        http_info = self._create_enhanced_connection_routes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_enhanced_connection_routes_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/datasource/enhanced-connections/{connection_id}/routes",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEnhancedConnectionRoutesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def create_global_variable(self, request):
        """创建DLI全局变量

        创建全局变量。全局变量用于替换SQL作业中的敏感数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateGlobalVariable
        :type request: :class:`huaweicloudsdkdli.v1.CreateGlobalVariableRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateGlobalVariableResponse`
        """
        http_info = self._create_global_variable_http_info(request)
        return self._call_api(**http_info)

    def create_global_variable_invoker(self, request):
        http_info = self._create_global_variable_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_global_variable_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/variables",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGlobalVariableResponse"
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

    def create_queue(self, request):
        """创建队列

        该API用于创建队列，该队列将会绑定用户指定的计算资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateQueue
        :type request: :class:`huaweicloudsdkdli.v1.CreateQueueRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateQueueResponse`
        """
        http_info = self._create_queue_http_info(request)
        return self._call_api(**http_info)

    def create_queue_invoker(self, request):
        http_info = self._create_queue_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_queue_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/queues",
            "request_type": request.__class__.__name__,
            "response_type": "CreateQueueResponse"
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

    def create_queue_plan(self, request):
        """创建队列定时扩缩容计划

        创建队列定时扩缩容计划接口，对指定的队列创建定时规格变更计划。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateQueuePlan
        :type request: :class:`huaweicloudsdkdli.v1.CreateQueuePlanRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateQueuePlanResponse`
        """
        http_info = self._create_queue_plan_http_info(request)
        return self._call_api(**http_info)

    def create_queue_plan_invoker(self, request):
        http_info = self._create_queue_plan_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_queue_plan_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/queues/{queue_name}/plans",
            "request_type": request.__class__.__name__,
            "response_type": "CreateQueuePlanResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'queue_name' in local_var_params:
            path_params['queue_name'] = local_var_params['queue_name']

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

    def create_queue_property(self, request):
        """新增队列属性

        该接口用于增加队列属性, 一次可增加多个属性。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateQueueProperty
        :type request: :class:`huaweicloudsdkdli.v1.CreateQueuePropertyRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateQueuePropertyResponse`
        """
        http_info = self._create_queue_property_http_info(request)
        return self._call_api(**http_info)

    def create_queue_property_invoker(self, request):
        http_info = self._create_queue_property_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_queue_property_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/queues/{queue_name}/properties",
            "request_type": request.__class__.__name__,
            "response_type": "CreateQueuePropertyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'queue_name' in local_var_params:
            path_params['queue_name'] = local_var_params['queue_name']

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

    def delete_auth_info(self, request):
        """删除跨源认证

        该API用于删除跨源认证信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAuthInfo
        :type request: :class:`huaweicloudsdkdli.v1.DeleteAuthInfoRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.DeleteAuthInfoResponse`
        """
        http_info = self._delete_auth_info_http_info(request)
        return self._call_api(**http_info)

    def delete_auth_info_invoker(self, request):
        http_info = self._delete_auth_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_auth_info_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/{project_id}/datasource/auth-infos/{auth_info_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAuthInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'auth_info_name' in local_var_params:
            path_params['auth_info_name'] = local_var_params['auth_info_name']

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
        http_info = self._delete_datasource_connection_http_info(request)
        return self._call_api(**http_info)

    def delete_datasource_connection_invoker(self, request):
        http_info = self._delete_datasource_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_datasource_connection_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/{project_id}/datasource-connection/{connection_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDatasourceConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def delete_elastic_resource_pool(self, request):
        """删除弹性资源池

        删除弹性资源池
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteElasticResourcePool
        :type request: :class:`huaweicloudsdkdli.v1.DeleteElasticResourcePoolRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.DeleteElasticResourcePoolResponse`
        """
        http_info = self._delete_elastic_resource_pool_http_info(request)
        return self._call_api(**http_info)

    def delete_elastic_resource_pool_invoker(self, request):
        http_info = self._delete_elastic_resource_pool_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_elastic_resource_pool_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/elastic-resource-pools/{elastic_resource_pool_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteElasticResourcePoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'elastic_resource_pool_name' in local_var_params:
            path_params['elastic_resource_pool_name'] = local_var_params['elastic_resource_pool_name']

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

    def delete_enhanced_connection(self, request):
        """删除增强型跨源连接

        该API用于删除已创建的增强型跨源连接。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEnhancedConnection
        :type request: :class:`huaweicloudsdkdli.v1.DeleteEnhancedConnectionRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.DeleteEnhancedConnectionResponse`
        """
        http_info = self._delete_enhanced_connection_http_info(request)
        return self._call_api(**http_info)

    def delete_enhanced_connection_invoker(self, request):
        http_info = self._delete_enhanced_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_enhanced_connection_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/{project_id}/datasource/enhanced-connections/{connection_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEnhancedConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def delete_enhanced_connection_routes(self, request):
        """删除路由

        该API用于删除跨源需要的路由。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEnhancedConnectionRoutes
        :type request: :class:`huaweicloudsdkdli.v1.DeleteEnhancedConnectionRoutesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.DeleteEnhancedConnectionRoutesResponse`
        """
        http_info = self._delete_enhanced_connection_routes_http_info(request)
        return self._call_api(**http_info)

    def delete_enhanced_connection_routes_invoker(self, request):
        http_info = self._delete_enhanced_connection_routes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_enhanced_connection_routes_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/{project_id}/datasource/enhanced-connections/{connection_id}/routes/{name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEnhancedConnectionRoutesResponse"
            }

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

    def delete_global_variable(self, request):
        """删除DLI全局变量

        删除全局变量。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteGlobalVariable
        :type request: :class:`huaweicloudsdkdli.v1.DeleteGlobalVariableRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.DeleteGlobalVariableResponse`
        """
        http_info = self._delete_global_variable_http_info(request)
        return self._call_api(**http_info)

    def delete_global_variable_invoker(self, request):
        http_info = self._delete_global_variable_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_global_variable_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/variables/{var_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGlobalVariableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'var_name' in local_var_params:
            path_params['var_name'] = local_var_params['var_name']

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
        http_info = self._delete_queue_http_info(request)
        return self._call_api(**http_info)

    def delete_queue_invoker(self, request):
        http_info = self._delete_queue_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_queue_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/queues/{queue_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteQueueResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'queue_name' in local_var_params:
            path_params['queue_name'] = local_var_params['queue_name']

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

    def delete_queue_plan(self, request):
        """单个删除队列定时扩缩容计划

        该API用于删除指定ID的队列定时扩缩容计划。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteQueuePlan
        :type request: :class:`huaweicloudsdkdli.v1.DeleteQueuePlanRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.DeleteQueuePlanResponse`
        """
        http_info = self._delete_queue_plan_http_info(request)
        return self._call_api(**http_info)

    def delete_queue_plan_invoker(self, request):
        http_info = self._delete_queue_plan_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_queue_plan_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/queues/{queue_name}/plans/{plan_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteQueuePlanResponse"
            }

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

    def delete_queue_property(self, request):
        """删除队列的属性

        该接口用于删除队列的属性，一次可删除多个属性值。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteQueueProperty
        :type request: :class:`huaweicloudsdkdli.v1.DeleteQueuePropertyRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.DeleteQueuePropertyResponse`
        """
        http_info = self._delete_queue_property_http_info(request)
        return self._call_api(**http_info)

    def delete_queue_property_invoker(self, request):
        http_info = self._delete_queue_property_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_queue_property_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/queues/{queue_name}/properties",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteQueuePropertyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'queue_name' in local_var_params:
            path_params['queue_name'] = local_var_params['queue_name']

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

    def delete_resource(self, request):
        """删除组内资源包

        该API用于删除某个project某个分组下的资源包
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteResource
        :type request: :class:`huaweicloudsdkdli.v1.DeleteResourceRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.DeleteResourceResponse`
        """
        http_info = self._delete_resource_http_info(request)
        return self._call_api(**http_info)

    def delete_resource_invoker(self, request):
        http_info = self._delete_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_resource_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/{project_id}/resources/{resource_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteResourceResponse"
            }

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

    def disassociate_queue_from_enhanced_connection(self, request):
        """解绑队列

        该API用于在增强型跨源中解绑已绑定的队列。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisassociateQueueFromEnhancedConnection
        :type request: :class:`huaweicloudsdkdli.v1.DisassociateQueueFromEnhancedConnectionRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.DisassociateQueueFromEnhancedConnectionResponse`
        """
        http_info = self._disassociate_queue_from_enhanced_connection_http_info(request)
        return self._call_api(**http_info)

    def disassociate_queue_from_enhanced_connection_invoker(self, request):
        http_info = self._disassociate_queue_from_enhanced_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disassociate_queue_from_enhanced_connection_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/datasource/enhanced-connections/{connection_id}/disassociate-queue",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateQueueFromEnhancedConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def list_auth_info(self, request):
        """获取跨源认证列表

        该API用于查询跨源认证信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuthInfo
        :type request: :class:`huaweicloudsdkdli.v1.ListAuthInfoRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListAuthInfoResponse`
        """
        http_info = self._list_auth_info_http_info(request)
        return self._call_api(**http_info)

    def list_auth_info_invoker(self, request):
        http_info = self._list_auth_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_auth_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/datasource/auth-infos",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuthInfoResponse"
            }

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

    def list_authorization_privileges(self, request):
        """查看赋权对象的用者权限信息

        获取对象赋权用户的权限信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuthorizationPrivileges
        :type request: :class:`huaweicloudsdkdli.v1.ListAuthorizationPrivilegesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListAuthorizationPrivilegesResponse`
        """
        http_info = self._list_authorization_privileges_http_info(request)
        return self._call_api(**http_info)

    def list_authorization_privileges_invoker(self, request):
        http_info = self._list_authorization_privileges_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_authorization_privileges_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/authorization/privileges",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuthorizationPrivilegesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'object' in local_var_params:
            query_params.append(('object', local_var_params['object']))

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

    def list_database_users(self, request):
        """查看数据库的使用者

        该API用于查询可以使用的指定队列的所有用户名称。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDatabaseUsers
        :type request: :class:`huaweicloudsdkdli.v1.ListDatabaseUsersRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListDatabaseUsersResponse`
        """
        http_info = self._list_database_users_http_info(request)
        return self._call_api(**http_info)

    def list_database_users_invoker(self, request):
        http_info = self._list_database_users_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_database_users_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/databases/{database_name}/users",
            "request_type": request.__class__.__name__,
            "response_type": "ListDatabaseUsersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']

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

    def list_datasource_connections(self, request):
        """查询经典型跨源连接列表

        该API用于查询该用户已创建的经典型跨源连接列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDatasourceConnections
        :type request: :class:`huaweicloudsdkdli.v1.ListDatasourceConnectionsRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListDatasourceConnectionsResponse`
        """
        http_info = self._list_datasource_connections_http_info(request)
        return self._call_api(**http_info)

    def list_datasource_connections_invoker(self, request):
        http_info = self._list_datasource_connections_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_datasource_connections_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/datasource-connection",
            "request_type": request.__class__.__name__,
            "response_type": "ListDatasourceConnectionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))

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

    def list_elastic_resource_pool_queues(self, request):
        """查询弹性资源池所属队列

        查询弹性资源池所属队列
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListElasticResourcePoolQueues
        :type request: :class:`huaweicloudsdkdli.v1.ListElasticResourcePoolQueuesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListElasticResourcePoolQueuesResponse`
        """
        http_info = self._list_elastic_resource_pool_queues_http_info(request)
        return self._call_api(**http_info)

    def list_elastic_resource_pool_queues_invoker(self, request):
        http_info = self._list_elastic_resource_pool_queues_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_elastic_resource_pool_queues_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elastic-resource-pools/{elastic_resource_pool_name}/queues",
            "request_type": request.__class__.__name__,
            "response_type": "ListElasticResourcePoolQueuesResponse"
            }

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

    def list_elastic_resource_pool_scale_records(self, request):
        """弹性资源池扩缩容历史记录

        查询当前弹性资源池扩缩容历史记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListElasticResourcePoolScaleRecords
        :type request: :class:`huaweicloudsdkdli.v1.ListElasticResourcePoolScaleRecordsRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListElasticResourcePoolScaleRecordsResponse`
        """
        http_info = self._list_elastic_resource_pool_scale_records_http_info(request)
        return self._call_api(**http_info)

    def list_elastic_resource_pool_scale_records_invoker(self, request):
        http_info = self._list_elastic_resource_pool_scale_records_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_elastic_resource_pool_scale_records_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elastic-resource-pools/{elastic_resource_pool_name}/scale-records",
            "request_type": request.__class__.__name__,
            "response_type": "ListElasticResourcePoolScaleRecordsResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Auth-Token", ]

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

    def list_elastic_resource_pools(self, request):
        """查询所有弹性资源池

        查询所有弹性资源池
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListElasticResourcePools
        :type request: :class:`huaweicloudsdkdli.v1.ListElasticResourcePoolsRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListElasticResourcePoolsResponse`
        """
        http_info = self._list_elastic_resource_pools_http_info(request)
        return self._call_api(**http_info)

    def list_elastic_resource_pools_invoker(self, request):
        http_info = self._list_elastic_resource_pools_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_elastic_resource_pools_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/elastic-resource-pools",
            "request_type": request.__class__.__name__,
            "response_type": "ListElasticResourcePoolsResponse"
            }

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

    def list_enhanced_connections(self, request):
        """查询增强型跨源连接列表

        该API用于查询该用户已创建的增强型跨源连接列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEnhancedConnections
        :type request: :class:`huaweicloudsdkdli.v1.ListEnhancedConnectionsRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListEnhancedConnectionsResponse`
        """
        http_info = self._list_enhanced_connections_http_info(request)
        return self._call_api(**http_info)

    def list_enhanced_connections_invoker(self, request):
        http_info = self._list_enhanced_connections_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_enhanced_connections_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/datasource/enhanced-connections",
            "request_type": request.__class__.__name__,
            "response_type": "ListEnhancedConnectionsResponse"
            }

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

    def list_global_variables(self, request):
        """查询DLI全局变量列表

        查询全局变量列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGlobalVariables
        :type request: :class:`huaweicloudsdkdli.v1.ListGlobalVariablesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListGlobalVariablesResponse`
        """
        http_info = self._list_global_variables_http_info(request)
        return self._call_api(**http_info)

    def list_global_variables_invoker(self, request):
        http_info = self._list_global_variables_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_global_variables_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/variables",
            "request_type": request.__class__.__name__,
            "response_type": "ListGlobalVariablesResponse"
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

    def list_queue_plans(self, request):
        """查看队列定时扩缩容计划

        查看队列定时扩缩容计划接口，列出指定队列定时规格变更计划。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQueuePlans
        :type request: :class:`huaweicloudsdkdli.v1.ListQueuePlansRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListQueuePlansResponse`
        """
        http_info = self._list_queue_plans_http_info(request)
        return self._call_api(**http_info)

    def list_queue_plans_invoker(self, request):
        http_info = self._list_queue_plans_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_queue_plans_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/queues/{queue_name}/plans",
            "request_type": request.__class__.__name__,
            "response_type": "ListQueuePlansResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'queue_name' in local_var_params:
            path_params['queue_name'] = local_var_params['queue_name']

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

    def list_queue_properties(self, request):
        """获取队列属性

        获取队列配置的属性
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQueueProperties
        :type request: :class:`huaweicloudsdkdli.v1.ListQueuePropertiesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListQueuePropertiesResponse`
        """
        http_info = self._list_queue_properties_http_info(request)
        return self._call_api(**http_info)

    def list_queue_properties_invoker(self, request):
        http_info = self._list_queue_properties_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_queue_properties_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/queues/{queue_name}/properties",
            "request_type": request.__class__.__name__,
            "response_type": "ListQueuePropertiesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'queue_name' in local_var_params:
            path_params['queue_name'] = local_var_params['queue_name']

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))

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

    def list_queue_users(self, request):
        """查看队列的使用者

        该API用于查询可以使用的指定队列的所有用户名称。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQueueUsers
        :type request: :class:`huaweicloudsdkdli.v1.ListQueueUsersRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListQueueUsersResponse`
        """
        http_info = self._list_queue_users_http_info(request)
        return self._call_api(**http_info)

    def list_queue_users_invoker(self, request):
        http_info = self._list_queue_users_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_queue_users_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/queues/{queue_name}/users",
            "request_type": request.__class__.__name__,
            "response_type": "ListQueueUsersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'queue_name' in local_var_params:
            path_params['queue_name'] = local_var_params['queue_name']

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

    def list_queues(self, request):
        """查询所有队列

        该API用于列出该project下所有的队列。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQueues
        :type request: :class:`huaweicloudsdkdli.v1.ListQueuesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListQueuesResponse`
        """
        http_info = self._list_queues_http_info(request)
        return self._call_api(**http_info)

    def list_queues_invoker(self, request):
        http_info = self._list_queues_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_queues_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/queues",
            "request_type": request.__class__.__name__,
            "response_type": "ListQueuesResponse"
            }

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

    def list_resources(self, request):
        """查看分组资源列表

        该API用于查看某个project下的所有资源，其中包含Group。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResources
        :type request: :class:`huaweicloudsdkdli.v1.ListResourcesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListResourcesResponse`
        """
        http_info = self._list_resources_http_info(request)
        return self._call_api(**http_info)

    def list_resources_invoker(self, request):
        http_info = self._list_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_resources_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourcesResponse"
            }

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

    def list_table_privileges(self, request):
        """查看表的用户权限

        该API用于查询指定用户在表上的权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTablePrivileges
        :type request: :class:`huaweicloudsdkdli.v1.ListTablePrivilegesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListTablePrivilegesResponse`
        """
        http_info = self._list_table_privileges_http_info(request)
        return self._call_api(**http_info)

    def list_table_privileges_invoker(self, request):
        http_info = self._list_table_privileges_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_table_privileges_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/databases/{database_name}/tables/{table_name}/users/{user_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ListTablePrivilegesResponse"
            }

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

    def list_table_users(self, request):
        """查看表的使用者

        该API用于查看有权访问指定表或表的列的所有用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTableUsers
        :type request: :class:`huaweicloudsdkdli.v1.ListTableUsersRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListTableUsersResponse`
        """
        http_info = self._list_table_users_http_info(request)
        return self._call_api(**http_info)

    def list_table_users_invoker(self, request):
        http_info = self._list_table_users_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_table_users_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/databases/{database_name}/tables/{table_name}/users",
            "request_type": request.__class__.__name__,
            "response_type": "ListTableUsersResponse"
            }

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

    def register_authorized_queue(self, request):
        """队列赋权

        该API用于与其他用户共享指定的队列，可以给用户赋使用指定的队列的权限或者收回使用权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RegisterAuthorizedQueue
        :type request: :class:`huaweicloudsdkdli.v1.RegisterAuthorizedQueueRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.RegisterAuthorizedQueueResponse`
        """
        http_info = self._register_authorized_queue_http_info(request)
        return self._call_api(**http_info)

    def register_authorized_queue_invoker(self, request):
        http_info = self._register_authorized_queue_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _register_authorized_queue_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/queues/user-authorization",
            "request_type": request.__class__.__name__,
            "response_type": "RegisterAuthorizedQueueResponse"
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

    def run_authorization_action(self, request):
        """数据赋权（用户、项目）

        该API用于将DLI资源权限赋给、回收、更新指定的其他用户或项目。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunAuthorizationAction
        :type request: :class:`huaweicloudsdkdli.v1.RunAuthorizationActionRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.RunAuthorizationActionResponse`
        """
        http_info = self._run_authorization_action_http_info(request)
        return self._call_api(**http_info)

    def run_authorization_action_invoker(self, request):
        http_info = self._run_authorization_action_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_authorization_action_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/authorization",
            "request_type": request.__class__.__name__,
            "response_type": "RunAuthorizationActionResponse"
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

    def run_queue_action(self, request):
        """重启/扩容/缩容队列

        该功能用于重新启动队列、扩容队列、缩容队列。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunQueueAction
        :type request: :class:`huaweicloudsdkdli.v1.RunQueueActionRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.RunQueueActionResponse`
        """
        http_info = self._run_queue_action_http_info(request)
        return self._call_api(**http_info)

    def run_queue_action_invoker(self, request):
        http_info = self._run_queue_action_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_queue_action_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/queues/{queue_name}/action",
            "request_type": request.__class__.__name__,
            "response_type": "RunQueueActionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'queue_name' in local_var_params:
            path_params['queue_name'] = local_var_params['queue_name']

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

    def show_connectivity_task(self, request):
        """查询指定地址连通性测试详情

        该API用于在连通性测试提交后查询连通性结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowConnectivityTask
        :type request: :class:`huaweicloudsdkdli.v1.ShowConnectivityTaskRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowConnectivityTaskResponse`
        """
        http_info = self._show_connectivity_task_http_info(request)
        return self._call_api(**http_info)

    def show_connectivity_task_invoker(self, request):
        http_info = self._show_connectivity_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_connectivity_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/queues/{queue_name}/connection-test/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConnectivityTaskResponse"
            }

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

    def show_datasource_connection(self, request):
        """查询经典型跨源连接

        该API用于查询该用户指定的已创建的经典型跨源连接。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDatasourceConnection
        :type request: :class:`huaweicloudsdkdli.v1.ShowDatasourceConnectionRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowDatasourceConnectionResponse`
        """
        http_info = self._show_datasource_connection_http_info(request)
        return self._call_api(**http_info)

    def show_datasource_connection_invoker(self, request):
        http_info = self._show_datasource_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_datasource_connection_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/datasource-connection/{connection_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDatasourceConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def show_dli_agency(self, request):
        """获取dli委托信息

        获取dli委托信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDliAgency
        :type request: :class:`huaweicloudsdkdli.v1.ShowDliAgencyRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowDliAgencyResponse`
        """
        http_info = self._show_dli_agency_http_info(request)
        return self._call_api(**http_info)

    def show_dli_agency_invoker(self, request):
        http_info = self._show_dli_agency_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_dli_agency_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/agency",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDliAgencyResponse"
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

    def show_enhanced_connection(self, request):
        """查询增强型跨源连接

        该API用于查询该用户指定的已创建的增强型跨源连接。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEnhancedConnection
        :type request: :class:`huaweicloudsdkdli.v1.ShowEnhancedConnectionRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowEnhancedConnectionResponse`
        """
        http_info = self._show_enhanced_connection_http_info(request)
        return self._call_api(**http_info)

    def show_enhanced_connection_invoker(self, request):
        http_info = self._show_enhanced_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_enhanced_connection_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/datasource/enhanced-connections/{connection_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEnhancedConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def show_enhanced_connection_privilege(self, request):
        """查询增强型跨源授权信息

        该API用于查询增强型跨源连接授权的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEnhancedConnectionPrivilege
        :type request: :class:`huaweicloudsdkdli.v1.ShowEnhancedConnectionPrivilegeRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowEnhancedConnectionPrivilegeResponse`
        """
        http_info = self._show_enhanced_connection_privilege_http_info(request)
        return self._call_api(**http_info)

    def show_enhanced_connection_privilege_invoker(self, request):
        http_info = self._show_enhanced_connection_privilege_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_enhanced_connection_privilege_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/datasource/enhanced-connections/{connection_id}/privileges",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEnhancedConnectionPrivilegeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def show_queue(self, request):
        """查询队列详情

        该API用于列出该project下指定的队列详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowQueue
        :type request: :class:`huaweicloudsdkdli.v1.ShowQueueRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowQueueResponse`
        """
        http_info = self._show_queue_http_info(request)
        return self._call_api(**http_info)

    def show_queue_invoker(self, request):
        http_info = self._show_queue_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_queue_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/queues/{queue_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowQueueResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'queue_name' in local_var_params:
            path_params['queue_name'] = local_var_params['queue_name']

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

    def show_resource_info(self, request):
        """查看组内资源包

        该API用于查看某个project某个分组下的具体资源信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowResourceInfo
        :type request: :class:`huaweicloudsdkdli.v1.ShowResourceInfoRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowResourceInfoResponse`
        """
        http_info = self._show_resource_info_http_info(request)
        return self._call_api(**http_info)

    def show_resource_info_invoker(self, request):
        http_info = self._show_resource_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_resource_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/resources/{resource_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourceInfoResponse"
            }

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

    def update_auth_info(self, request):
        """更新跨源认证

        该API用于更新跨源认证信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAuthInfo
        :type request: :class:`huaweicloudsdkdli.v1.UpdateAuthInfoRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateAuthInfoResponse`
        """
        http_info = self._update_auth_info_http_info(request)
        return self._call_api(**http_info)

    def update_auth_info_invoker(self, request):
        http_info = self._update_auth_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_auth_info_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.0/{project_id}/datasource/auth-infos",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAuthInfoResponse"
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

    def update_elastic_resource_pool(self, request):
        """修改弹性资源池信息

        修改弹性资源池信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateElasticResourcePool
        :type request: :class:`huaweicloudsdkdli.v1.UpdateElasticResourcePoolRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateElasticResourcePoolResponse`
        """
        http_info = self._update_elastic_resource_pool_http_info(request)
        return self._call_api(**http_info)

    def update_elastic_resource_pool_invoker(self, request):
        http_info = self._update_elastic_resource_pool_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_elastic_resource_pool_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/elastic-resource-pools/{elastic_resource_pool_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateElasticResourcePoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'elastic_resource_pool_name' in local_var_params:
            path_params['elastic_resource_pool_name'] = local_var_params['elastic_resource_pool_name']

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

    def update_elastic_resource_pool_queue(self, request):
        """修改弹性资源池关联的队列优先级

        设置弹性资源池指定队列的扩缩容策略信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateElasticResourcePoolQueue
        :type request: :class:`huaweicloudsdkdli.v1.UpdateElasticResourcePoolQueueRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateElasticResourcePoolQueueResponse`
        """
        http_info = self._update_elastic_resource_pool_queue_http_info(request)
        return self._call_api(**http_info)

    def update_elastic_resource_pool_queue_invoker(self, request):
        http_info = self._update_elastic_resource_pool_queue_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_elastic_resource_pool_queue_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/elastic-resource-pools/{elastic_resource_pool_name}/queues/{queue_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateElasticResourcePoolQueueResponse"
            }

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

    def update_enhanced_connection(self, request):
        """修改增强型跨源主机信息

        该API用于在跨源中修改数据源主机信息，仅支持全量覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateEnhancedConnection
        :type request: :class:`huaweicloudsdkdli.v1.UpdateEnhancedConnectionRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateEnhancedConnectionResponse`
        """
        http_info = self._update_enhanced_connection_http_info(request)
        return self._call_api(**http_info)

    def update_enhanced_connection_invoker(self, request):
        http_info = self._update_enhanced_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_enhanced_connection_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.0/{project_id}/datasource/enhanced-connections/{connection_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEnhancedConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def update_global_variable(self, request):
        """修改DLI全局变量

        修改全局变量。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateGlobalVariable
        :type request: :class:`huaweicloudsdkdli.v1.UpdateGlobalVariableRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateGlobalVariableResponse`
        """
        http_info = self._update_global_variable_http_info(request)
        return self._call_api(**http_info)

    def update_global_variable_invoker(self, request):
        http_info = self._update_global_variable_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_global_variable_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/variables/{var_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGlobalVariableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'var_name' in local_var_params:
            path_params['var_name'] = local_var_params['var_name']

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

    def update_group_or_resource_owner(self, request):
        """修改组或者资源包拥有者

        用于修改程序包的owner。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateGroupOrResourceOwner
        :type request: :class:`huaweicloudsdkdli.v1.UpdateGroupOrResourceOwnerRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateGroupOrResourceOwnerResponse`
        """
        http_info = self._update_group_or_resource_owner_http_info(request)
        return self._call_api(**http_info)

    def update_group_or_resource_owner_invoker(self, request):
        http_info = self._update_group_or_resource_owner_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_group_or_resource_owner_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.0/{project_id}/resources/owner",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGroupOrResourceOwnerResponse"
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
        http_info = self._update_queue_cidr_http_info(request)
        return self._call_api(**http_info)

    def update_queue_cidr_invoker(self, request):
        http_info = self._update_queue_cidr_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_queue_cidr_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/queues/{queue_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateQueueCidrResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'queue_name' in local_var_params:
            path_params['queue_name'] = local_var_params['queue_name']

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

    def update_queue_property(self, request):
        """更新队列属性

        更新队列属性
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateQueueProperty
        :type request: :class:`huaweicloudsdkdli.v1.UpdateQueuePropertyRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateQueuePropertyResponse`
        """
        http_info = self._update_queue_property_http_info(request)
        return self._call_api(**http_info)

    def update_queue_property_invoker(self, request):
        http_info = self._update_queue_property_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_queue_property_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/queues/{queue_name}/properties",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateQueuePropertyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'queue_name' in local_var_params:
            path_params['queue_name'] = local_var_params['queue_name']

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

    def upload_files(self, request):
        """上传file类型分组资源

        该API用于在project下上传file类型模块。
        说明： 上传同名file模块时，新模块将会覆盖旧模块。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadFiles
        :type request: :class:`huaweicloudsdkdli.v1.UploadFilesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UploadFilesResponse`
        """
        http_info = self._upload_files_http_info(request)
        return self._call_api(**http_info)

    def upload_files_invoker(self, request):
        http_info = self._upload_files_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upload_files_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/resources/files",
            "request_type": request.__class__.__name__,
            "response_type": "UploadFilesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'user_id' in local_var_params:
            header_params['USER-ID'] = local_var_params['user_id']

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

    def upload_jars(self, request):
        """上传jar类型分组资源

        该API用于在project下上传jar类型分组资源。
        说明：上传同名资源模块时，新模块将会覆盖旧模块。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadJars
        :type request: :class:`huaweicloudsdkdli.v1.UploadJarsRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UploadJarsResponse`
        """
        http_info = self._upload_jars_http_info(request)
        return self._call_api(**http_info)

    def upload_jars_invoker(self, request):
        http_info = self._upload_jars_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upload_jars_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/resources/jars",
            "request_type": request.__class__.__name__,
            "response_type": "UploadJarsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'user_id' in local_var_params:
            header_params['USER-ID'] = local_var_params['user_id']

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

    def upload_python_files(self, request):
        """上传pyfile类型分组资源

        该API用于在project下的上传pyfile类型模块。
        说明： 上传同名pyfile类型模块时，新模块将会覆盖旧模块。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadPythonFiles
        :type request: :class:`huaweicloudsdkdli.v1.UploadPythonFilesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UploadPythonFilesResponse`
        """
        http_info = self._upload_python_files_http_info(request)
        return self._call_api(**http_info)

    def upload_python_files_invoker(self, request):
        http_info = self._upload_python_files_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upload_python_files_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/resources/pyfiles",
            "request_type": request.__class__.__name__,
            "response_type": "UploadPythonFilesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'user_id' in local_var_params:
            header_params['USER-ID'] = local_var_params['user_id']

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

    def upload_resources(self, request):
        """上传分组资源

        该API用于上传分组资源到某个project下。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadResources
        :type request: :class:`huaweicloudsdkdli.v1.UploadResourcesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UploadResourcesResponse`
        """
        http_info = self._upload_resources_http_info(request)
        return self._call_api(**http_info)

    def upload_resources_invoker(self, request):
        http_info = self._upload_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upload_resources_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/resources",
            "request_type": request.__class__.__name__,
            "response_type": "UploadResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'user_id' in local_var_params:
            header_params['USER-ID'] = local_var_params['user_id']

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

    def batch_delete_flink_jobs(self, request):
        """批量删除Flink作业

        批量删除任何状态的作业。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteFlinkJobs
        :type request: :class:`huaweicloudsdkdli.v1.BatchDeleteFlinkJobsRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.BatchDeleteFlinkJobsResponse`
        """
        http_info = self._batch_delete_flink_jobs_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_flink_jobs_invoker(self, request):
        http_info = self._batch_delete_flink_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_flink_jobs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/streaming/jobs/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteFlinkJobsResponse"
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

    def batch_run_flink_jobs(self, request):
        """批量运行Flink作业

        触发批量运行Flink作业。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchRunFlinkJobs
        :type request: :class:`huaweicloudsdkdli.v1.BatchRunFlinkJobsRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.BatchRunFlinkJobsResponse`
        """
        http_info = self._batch_run_flink_jobs_http_info(request)
        return self._call_api(**http_info)

    def batch_run_flink_jobs_invoker(self, request):
        http_info = self._batch_run_flink_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_run_flink_jobs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/streaming/jobs/run",
            "request_type": request.__class__.__name__,
            "response_type": "BatchRunFlinkJobsResponse"
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

    def change_flink_job_status_report(self, request):
        """边缘Flink作业状态信息上报

        该API用于处理边缘Flink作业状态上报信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeFlinkJobStatusReport
        :type request: :class:`huaweicloudsdkdli.v1.ChangeFlinkJobStatusReportRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ChangeFlinkJobStatusReportResponse`
        """
        http_info = self._change_flink_job_status_report_http_info(request)
        return self._call_api(**http_info)

    def change_flink_job_status_report_invoker(self, request):
        http_info = self._change_flink_job_status_report_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_flink_job_status_report_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/edgesrv/job-report",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeFlinkJobStatusReportResponse"
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

    def create_flink_jar_job(self, request):
        """新建Flink Jar作业

        用户自定义作业目前支持jar格式，运行在独享集群中。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFlinkJarJob
        :type request: :class:`huaweicloudsdkdli.v1.CreateFlinkJarJobRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateFlinkJarJobResponse`
        """
        http_info = self._create_flink_jar_job_http_info(request)
        return self._call_api(**http_info)

    def create_flink_jar_job_invoker(self, request):
        http_info = self._create_flink_jar_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_flink_jar_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/streaming/flink-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFlinkJarJobResponse"
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

    def create_flink_sql_job(self, request):
        """新建Flink SQL作业

        通过POST方式，提交流式SQL作业，请求体为JSON格式。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFlinkSqlJob
        :type request: :class:`huaweicloudsdkdli.v1.CreateFlinkSqlJobRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateFlinkSqlJobResponse`
        """
        http_info = self._create_flink_sql_job_http_info(request)
        return self._call_api(**http_info)

    def create_flink_sql_job_invoker(self, request):
        http_info = self._create_flink_sql_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_flink_sql_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/streaming/sql-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFlinkSqlJobResponse"
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

    def create_flink_sql_job_graph(self, request):
        """生成flink SQL作业的静态流图

        生成flink SQL作业的静态流图
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFlinkSqlJobGraph
        :type request: :class:`huaweicloudsdkdli.v1.CreateFlinkSqlJobGraphRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateFlinkSqlJobGraphResponse`
        """
        http_info = self._create_flink_sql_job_graph_http_info(request)
        return self._call_api(**http_info)

    def create_flink_sql_job_graph_invoker(self, request):
        http_info = self._create_flink_sql_job_graph_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_flink_sql_job_graph_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/streaming/jobs/{job_id}/gen-graph",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFlinkSqlJobGraphResponse"
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

    def create_flink_sql_job_template(self, request):
        """新建Flink作业模板

        在DLI服务中新建一个Flink作业模板，最多100个。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFlinkSqlJobTemplate
        :type request: :class:`huaweicloudsdkdli.v1.CreateFlinkSqlJobTemplateRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateFlinkSqlJobTemplateResponse`
        """
        http_info = self._create_flink_sql_job_template_http_info(request)
        return self._call_api(**http_info)

    def create_flink_sql_job_template_invoker(self, request):
        http_info = self._create_flink_sql_job_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_flink_sql_job_template_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/streaming/job-templates",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFlinkSqlJobTemplateResponse"
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

    def create_ief_message_channel(self, request):
        """创建IEF消息通道

        该API用于创建IEF消息通道
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateIefMessageChannel
        :type request: :class:`huaweicloudsdkdli.v1.CreateIefMessageChannelRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateIefMessageChannelResponse`
        """
        http_info = self._create_ief_message_channel_http_info(request)
        return self._call_api(**http_info)

    def create_ief_message_channel_invoker(self, request):
        http_info = self._create_ief_message_channel_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_ief_message_channel_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/edgesrv/message-channel",
            "request_type": request.__class__.__name__,
            "response_type": "CreateIefMessageChannelResponse"
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

    def create_ief_system_events(self, request):
        """IEF系统事件上报

        该API用于处理IEF系统事件上报
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateIefSystemEvents
        :type request: :class:`huaweicloudsdkdli.v1.CreateIefSystemEventsRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateIefSystemEventsResponse`
        """
        http_info = self._create_ief_system_events_http_info(request)
        return self._call_api(**http_info)

    def create_ief_system_events_invoker(self, request):
        http_info = self._create_ief_system_events_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_ief_system_events_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/edgesrv/system-events",
            "request_type": request.__class__.__name__,
            "response_type": "CreateIefSystemEventsResponse"
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

    def delete_flink_job(self, request):
        """删除作业

        删除任何状态的作业。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteFlinkJob
        :type request: :class:`huaweicloudsdkdli.v1.DeleteFlinkJobRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.DeleteFlinkJobResponse`
        """
        http_info = self._delete_flink_job_http_info(request)
        return self._call_api(**http_info)

    def delete_flink_job_invoker(self, request):
        http_info = self._delete_flink_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_flink_job_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/streaming/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteFlinkJobResponse"
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

    def delete_flink_sql_job_template(self, request):
        """删除Flink作业模板

        删除一个Flink作业模板，即使当前模板正在被作业使用，也允许删除。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteFlinkSqlJobTemplate
        :type request: :class:`huaweicloudsdkdli.v1.DeleteFlinkSqlJobTemplateRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.DeleteFlinkSqlJobTemplateResponse`
        """
        http_info = self._delete_flink_sql_job_template_http_info(request)
        return self._call_api(**http_info)

    def delete_flink_sql_job_template_invoker(self, request):
        http_info = self._delete_flink_sql_job_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_flink_sql_job_template_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/streaming/job-templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteFlinkSqlJobTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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

    def export_flink_jobs(self, request):
        """flink作业导出

        通过POST方式，导出flink作业，请求体为JSON格式。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportFlinkJobs
        :type request: :class:`huaweicloudsdkdli.v1.ExportFlinkJobsRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ExportFlinkJobsResponse`
        """
        http_info = self._export_flink_jobs_http_info(request)
        return self._call_api(**http_info)

    def export_flink_jobs_invoker(self, request):
        http_info = self._export_flink_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_flink_jobs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/streaming/jobs/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportFlinkJobsResponse"
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

    def import_flink_jobs(self, request):
        """flink作业导入

        通过POST方式，导入flink作业，请求体为JSON格式。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportFlinkJobs
        :type request: :class:`huaweicloudsdkdli.v1.ImportFlinkJobsRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ImportFlinkJobsResponse`
        """
        http_info = self._import_flink_jobs_http_info(request)
        return self._call_api(**http_info)

    def import_flink_jobs_invoker(self, request):
        http_info = self._import_flink_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_flink_jobs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/streaming/jobs/import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportFlinkJobsResponse"
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

    def list_flink_jobs(self, request):
        """查询Flink作业列表

        查询当前用户的作业列表，可以根据作业ID作为ID，查询大于ID或小于ID的限定条数的作业，默认查询全部状态的作业，也可以设定运行中或其他状态条件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFlinkJobs
        :type request: :class:`huaweicloudsdkdli.v1.ListFlinkJobsRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListFlinkJobsResponse`
        """
        http_info = self._list_flink_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_flink_jobs_invoker(self, request):
        http_info = self._list_flink_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_flink_jobs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/streaming/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListFlinkJobsResponse"
            }

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

    def list_flink_sql_job_templates(self, request):
        """查询Flink作业模板列表

        查询Flink作业模板列表。当前只支持查询用户自定义模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFlinkSqlJobTemplates
        :type request: :class:`huaweicloudsdkdli.v1.ListFlinkSqlJobTemplatesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListFlinkSqlJobTemplatesResponse`
        """
        http_info = self._list_flink_sql_job_templates_http_info(request)
        return self._call_api(**http_info)

    def list_flink_sql_job_templates_invoker(self, request):
        http_info = self._list_flink_sql_job_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_flink_sql_job_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/streaming/job-templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListFlinkSqlJobTemplatesResponse"
            }

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

    def register_bucket(self, request):
        """OBS授权给DLI服务

        用户主动授权OBS桶的操作权限给DLI服务, 用于保存用户作业的checkpoint、作业的运行日志等。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RegisterBucket
        :type request: :class:`huaweicloudsdkdli.v1.RegisterBucketRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.RegisterBucketResponse`
        """
        http_info = self._register_bucket_http_info(request)
        return self._call_api(**http_info)

    def register_bucket_invoker(self, request):
        http_info = self._register_bucket_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _register_bucket_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/dli/obs-authorize",
            "request_type": request.__class__.__name__,
            "response_type": "RegisterBucketResponse"
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

    def run_ief_job_action_call_back(self, request):
        """边缘Flink作业Action状态回调

        该API用于处理IEF Flink作业action回调信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunIefJobActionCallBack
        :type request: :class:`huaweicloudsdkdli.v1.RunIefJobActionCallBackRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.RunIefJobActionCallBackResponse`
        """
        http_info = self._run_ief_job_action_call_back_http_info(request)
        return self._call_api(**http_info)

    def run_ief_job_action_call_back_invoker(self, request):
        http_info = self._run_ief_job_action_call_back_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_ief_job_action_call_back_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/edgesrv/messages",
            "request_type": request.__class__.__name__,
            "response_type": "RunIefJobActionCallBackResponse"
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

    def show_flink_job(self, request):
        """查询Flink作业详情

        查看一个Flink作业的详情信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFlinkJob
        :type request: :class:`huaweicloudsdkdli.v1.ShowFlinkJobRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowFlinkJobResponse`
        """
        http_info = self._show_flink_job_http_info(request)
        return self._call_api(**http_info)

    def show_flink_job_invoker(self, request):
        http_info = self._show_flink_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_flink_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/streaming/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFlinkJobResponse"
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

    def show_flink_job_execution_graph(self, request):
        """查询Flink作业执行计划

        查询Flink作业执行计划。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFlinkJobExecutionGraph
        :type request: :class:`huaweicloudsdkdli.v1.ShowFlinkJobExecutionGraphRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowFlinkJobExecutionGraphResponse`
        """
        http_info = self._show_flink_job_execution_graph_http_info(request)
        return self._call_api(**http_info)

    def show_flink_job_execution_graph_invoker(self, request):
        http_info = self._show_flink_job_execution_graph_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_flink_job_execution_graph_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/streaming/jobs/{job_id}/execute-graph",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFlinkJobExecutionGraphResponse"
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

    def show_flink_metric(self, request):
        """查询Flink作业监控信息

        查询Flink作业监控信息, 支持同时查询多个Flink作业的监控信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFlinkMetric
        :type request: :class:`huaweicloudsdkdli.v1.ShowFlinkMetricRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowFlinkMetricResponse`
        """
        http_info = self._show_flink_metric_http_info(request)
        return self._call_api(**http_info)

    def show_flink_metric_invoker(self, request):
        http_info = self._show_flink_metric_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_flink_metric_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/streaming/jobs/metrics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFlinkMetricResponse"
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

    def stop_flink_jobs(self, request):
        """批量停止Flink作业

        批量停止正在运行的Flink作业。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopFlinkJobs
        :type request: :class:`huaweicloudsdkdli.v1.StopFlinkJobsRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.StopFlinkJobsResponse`
        """
        http_info = self._stop_flink_jobs_http_info(request)
        return self._call_api(**http_info)

    def stop_flink_jobs_invoker(self, request):
        http_info = self._stop_flink_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_flink_jobs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/streaming/jobs/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopFlinkJobsResponse"
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

    def update_flink_jar_job(self, request):
        """更新Flink Jar作业

        更新用户自定义作业，目前支持jar格式，运行在独享集群中。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateFlinkJarJob
        :type request: :class:`huaweicloudsdkdli.v1.UpdateFlinkJarJobRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateFlinkJarJobResponse`
        """
        http_info = self._update_flink_jar_job_http_info(request)
        return self._call_api(**http_info)

    def update_flink_jar_job_invoker(self, request):
        http_info = self._update_flink_jar_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_flink_jar_job_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/streaming/flink-jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateFlinkJarJobResponse"
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

    def update_flink_sql_job(self, request):
        """更新Flink SQL作业

        Stream SQL的语法扩展了Apache Flink SQL。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateFlinkSqlJob
        :type request: :class:`huaweicloudsdkdli.v1.UpdateFlinkSqlJobRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateFlinkSqlJobResponse`
        """
        http_info = self._update_flink_sql_job_http_info(request)
        return self._call_api(**http_info)

    def update_flink_sql_job_invoker(self, request):
        http_info = self._update_flink_sql_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_flink_sql_job_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/streaming/sql-jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateFlinkSqlJobResponse"
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

    def update_flink_sql_job_template(self, request):
        """更新Flink作业模板

        对DLI服务中已有的Flink作业模板进行更新。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateFlinkSqlJobTemplate
        :type request: :class:`huaweicloudsdkdli.v1.UpdateFlinkSqlJobTemplateRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateFlinkSqlJobTemplateResponse`
        """
        http_info = self._update_flink_sql_job_template_http_info(request)
        return self._call_api(**http_info)

    def update_flink_sql_job_template_invoker(self, request):
        http_info = self._update_flink_sql_job_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_flink_sql_job_template_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/streaming/job-templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateFlinkSqlJobTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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

    def cancel_sql_job(self, request):
        """取消作业

        该API用于取消已经提交的作业，若作业已经执行结束或失败则无法取消。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelSqlJob
        :type request: :class:`huaweicloudsdkdli.v1.CancelSqlJobRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CancelSqlJobResponse`
        """
        http_info = self._cancel_sql_job_http_info(request)
        return self._call_api(**http_info)

    def cancel_sql_job_invoker(self, request):
        http_info = self._cancel_sql_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_sql_job_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CancelSqlJobResponse"
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

    def check_sql(self, request):
        """检查SQL语法

        该API用于检查SQL语法。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckSql
        :type request: :class:`huaweicloudsdkdli.v1.CheckSqlRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CheckSqlResponse`
        """
        http_info = self._check_sql_http_info(request)
        return self._call_api(**http_info)

    def check_sql_invoker(self, request):
        http_info = self._check_sql_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_sql_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/jobs/check-sql",
            "request_type": request.__class__.__name__,
            "response_type": "CheckSqlResponse"
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

    def create_database(self, request):
        """创建数据库

        该API用于新增数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDatabase
        :type request: :class:`huaweicloudsdkdli.v1.CreateDatabaseRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateDatabaseResponse`
        """
        http_info = self._create_database_http_info(request)
        return self._call_api(**http_info)

    def create_database_invoker(self, request):
        http_info = self._create_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_database_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/databases",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDatabaseResponse"
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

    def create_sql_job(self, request):
        """提交SQL作业

        该API用于通过执行SQL语句的方式向队列提交作业。
        
        作业包含以下类型：DDL、DCL、IMPORT、QUERY和INSERT。其中，IMPORT与导入数据的功能一致，区别仅在于实现方式不同。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSqlJob
        :type request: :class:`huaweicloudsdkdli.v1.CreateSqlJobRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateSqlJobResponse`
        """
        http_info = self._create_sql_job_http_info(request)
        return self._call_api(**http_info)

    def create_sql_job_invoker(self, request):
        http_info = self._create_sql_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_sql_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/jobs/submit-job",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSqlJobResponse"
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

    def create_table(self, request):
        """创建表

        该API用于创建新的表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTable
        :type request: :class:`huaweicloudsdkdli.v1.CreateTableRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateTableResponse`
        """
        http_info = self._create_table_http_info(request)
        return self._call_api(**http_info)

    def create_table_invoker(self, request):
        http_info = self._create_table_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_table_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/databases/{database_name}/tables",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']

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

    def delete_database(self, request):
        """删除数据库

        该API用于删除空数据库，若待删除的数据库中存在表，则需先删除其中的所有表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDatabase
        :type request: :class:`huaweicloudsdkdli.v1.DeleteDatabaseRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.DeleteDatabaseResponse`
        """
        http_info = self._delete_database_http_info(request)
        return self._call_api(**http_info)

    def delete_database_invoker(self, request):
        http_info = self._delete_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_database_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/databases/{database_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDatabaseResponse"
            }

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

    def delete_table(self, request):
        """删除表

        该API用于删除指定的表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTable
        :type request: :class:`huaweicloudsdkdli.v1.DeleteTableRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.DeleteTableResponse`
        """
        http_info = self._delete_table_http_info(request)
        return self._call_api(**http_info)

    def delete_table_invoker(self, request):
        http_info = self._delete_table_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_table_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/databases/{database_name}/tables/{table_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTableResponse"
            }

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

    def export_sql_job_result(self, request):
        """导出查询结果

        该API用于将SQL语句的查询结果导出到OBS对象存储中，只支持导出“QUERY”类型作业的查询结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportSqlJobResult
        :type request: :class:`huaweicloudsdkdli.v1.ExportSqlJobResultRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ExportSqlJobResultResponse`
        """
        http_info = self._export_sql_job_result_http_info(request)
        return self._call_api(**http_info)

    def export_sql_job_result_invoker(self, request):
        http_info = self._export_sql_job_result_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_sql_job_result_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/jobs/{job_id}/export-result",
            "request_type": request.__class__.__name__,
            "response_type": "ExportSqlJobResultResponse"
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

    def export_table(self, request):
        """导出查询结果

        该API用于将SQL语句的查询结果导出到OBS对象存储中，只支持导出“QUERY”类型作业的查询结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportTable
        :type request: :class:`huaweicloudsdkdli.v1.ExportTableRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ExportTableResponse`
        """
        http_info = self._export_table_http_info(request)
        return self._call_api(**http_info)

    def export_table_invoker(self, request):
        http_info = self._export_table_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_table_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/jobs/export-table",
            "request_type": request.__class__.__name__,
            "response_type": "ExportTableResponse"
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

    def import_table(self, request):
        """导入数据

        该API用于将数据从文件导入DLI或OBS表，目前仅支持将OBS上的数据导入DLI或OBS中。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportTable
        :type request: :class:`huaweicloudsdkdli.v1.ImportTableRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ImportTableResponse`
        """
        http_info = self._import_table_http_info(request)
        return self._call_api(**http_info)

    def import_table_invoker(self, request):
        http_info = self._import_table_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_table_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/jobs/import-table",
            "request_type": request.__class__.__name__,
            "response_type": "ImportTableResponse"
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

    def list_all_tables(self, request):
        """查询所有表

        该API用于查询指定数据库下符合过滤条件的或所有的表信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAllTables
        :type request: :class:`huaweicloudsdkdli.v1.ListAllTablesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListAllTablesResponse`
        """
        http_info = self._list_all_tables_http_info(request)
        return self._call_api(**http_info)

    def list_all_tables_invoker(self, request):
        http_info = self._list_all_tables_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_all_tables_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/databases/{database_name}/tables",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllTablesResponse"
            }

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

    def list_databases(self, request):
        """查询所有数据库

        该API用于查询出所有的数据库信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDatabases
        :type request: :class:`huaweicloudsdkdli.v1.ListDatabasesRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListDatabasesResponse`
        """
        http_info = self._list_databases_http_info(request)
        return self._call_api(**http_info)

    def list_databases_invoker(self, request):
        http_info = self._list_databases_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_databases_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/databases",
            "request_type": request.__class__.__name__,
            "response_type": "ListDatabasesResponse"
            }

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

    def list_sql_jobs(self, request):
        """查询所有作业

        该API用于查询当前工程下面的所有作业的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSqlJobs
        :type request: :class:`huaweicloudsdkdli.v1.ListSqlJobsRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListSqlJobsResponse`
        """
        http_info = self._list_sql_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_sql_jobs_invoker(self, request):
        http_info = self._list_sql_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sql_jobs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListSqlJobsResponse"
            }

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

    def preview_sql_job_result(self, request):
        """预览SQL作业查询结果

        该API用于在执行SQL查询语句的作业完成后，查看该作业执行的结果。目前仅支持查看“QUERY”类型作业的执行结果。
        该API只能查看前1000条的结果记录，若要查看全部的结果记录，需要先导出查询结果再进行查看。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PreviewSqlJobResult
        :type request: :class:`huaweicloudsdkdli.v1.PreviewSqlJobResultRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.PreviewSqlJobResultResponse`
        """
        http_info = self._preview_sql_job_result_http_info(request)
        return self._call_api(**http_info)

    def preview_sql_job_result_invoker(self, request):
        http_info = self._preview_sql_job_result_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _preview_sql_job_result_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/jobs/{job_id}/preview",
            "request_type": request.__class__.__name__,
            "response_type": "PreviewSqlJobResultResponse"
            }

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

    def show_describe_table(self, request):
        """描述表信息

        该API用于描述指定表的元数据信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDescribeTable
        :type request: :class:`huaweicloudsdkdli.v1.ShowDescribeTableRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowDescribeTableResponse`
        """
        http_info = self._show_describe_table_http_info(request)
        return self._call_api(**http_info)

    def show_describe_table_invoker(self, request):
        http_info = self._show_describe_table_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_describe_table_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/databases/{database_name}/tables/{table_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDescribeTableResponse"
            }

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

    def show_partitions(self, request):
        """获取分区信息列表

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPartitions
        :type request: :class:`huaweicloudsdkdli.v1.ShowPartitionsRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowPartitionsResponse`
        """
        http_info = self._show_partitions_http_info(request)
        return self._call_api(**http_info)

    def show_partitions_invoker(self, request):
        http_info = self._show_partitions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_partitions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/databases/{database_name}/tables/{table_name}/partitions",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPartitionsResponse"
            }

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

    def show_sql_job_detail(self, request):
        """查询作业详细信息

        该API用于查询作业的详细信息，如作业的databasename、tablename、file size和export mode等信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSqlJobDetail
        :type request: :class:`huaweicloudsdkdli.v1.ShowSqlJobDetailRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowSqlJobDetailResponse`
        """
        http_info = self._show_sql_job_detail_http_info(request)
        return self._call_api(**http_info)

    def show_sql_job_detail_invoker(self, request):
        http_info = self._show_sql_job_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sql_job_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/jobs/{job_id}/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSqlJobDetailResponse"
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

    def show_sql_job_progress(self, request):
        """查询作业执行进度信息

        该API用于获取作业执行进度信息，如果作业正在执行，可以获取到子作业的信息，如果作业刚开始或者已经结束，不可以获取到子作业信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSqlJobProgress
        :type request: :class:`huaweicloudsdkdli.v1.ShowSqlJobProgressRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowSqlJobProgressResponse`
        """
        http_info = self._show_sql_job_progress_http_info(request)
        return self._call_api(**http_info)

    def show_sql_job_progress_invoker(self, request):
        http_info = self._show_sql_job_progress_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sql_job_progress_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/jobs/{job_id}/progress",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSqlJobProgressResponse"
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

    def show_sql_job_status(self, request):
        """查询作业状态

        该API用于在作业提交后查询作业状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSqlJobStatus
        :type request: :class:`huaweicloudsdkdli.v1.ShowSqlJobStatusRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowSqlJobStatusResponse`
        """
        http_info = self._show_sql_job_status_http_info(request)
        return self._call_api(**http_info)

    def show_sql_job_status_invoker(self, request):
        http_info = self._show_sql_job_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sql_job_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/jobs/{job_id}/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSqlJobStatusResponse"
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

    def show_table_content(self, request):
        """预览表内容

        该API用于用于预览表中前10行的内容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTableContent
        :type request: :class:`huaweicloudsdkdli.v1.ShowTableContentRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowTableContentResponse`
        """
        http_info = self._show_table_content_http_info(request)
        return self._call_api(**http_info)

    def show_table_content_invoker(self, request):
        http_info = self._show_table_content_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_table_content_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/databases/{database_name}/tables/{table_name}/preview",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTableContentResponse"
            }

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

    def update_database_owner(self, request):
        """修改数据库用户

        用于修改数据库的owner。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDatabaseOwner
        :type request: :class:`huaweicloudsdkdli.v1.UpdateDatabaseOwnerRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateDatabaseOwnerResponse`
        """
        http_info = self._update_database_owner_http_info(request)
        return self._call_api(**http_info)

    def update_database_owner_invoker(self, request):
        http_info = self._update_database_owner_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_database_owner_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/databases/{database_name}/owner",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDatabaseOwnerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']

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

    def update_table_owner(self, request):
        """修改表用户

        用于修改表的owner。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTableOwner
        :type request: :class:`huaweicloudsdkdli.v1.UpdateTableOwnerRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateTableOwnerResponse`
        """
        http_info = self._update_table_owner_http_info(request)
        return self._call_api(**http_info)

    def update_table_owner_invoker(self, request):
        http_info = self._update_table_owner_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_table_owner_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/databases/{database_name}/tables/{table_name}/owner",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTableOwnerResponse"
            }

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

    def cancel_spark_job(self, request):
        """取消批处理作业

        该API用于取消批处理作业。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelSparkJob
        :type request: :class:`huaweicloudsdkdli.v1.CancelSparkJobRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CancelSparkJobResponse`
        """
        http_info = self._cancel_spark_job_http_info(request)
        return self._call_api(**http_info)

    def cancel_spark_job_invoker(self, request):
        http_info = self._cancel_spark_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_spark_job_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/{project_id}/batches/{batch_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CancelSparkJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'batch_id' in local_var_params:
            path_params['batch_id'] = local_var_params['batch_id']

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

    def create_spark_job(self, request):
        """创建批处理作业

        该API用于在某个队列上创建作业。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSparkJob
        :type request: :class:`huaweicloudsdkdli.v1.CreateSparkJobRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.CreateSparkJobResponse`
        """
        http_info = self._create_spark_job_http_info(request)
        return self._call_api(**http_info)

    def create_spark_job_invoker(self, request):
        http_info = self._create_spark_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_spark_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/batches",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSparkJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'user_id' in local_var_params:
            header_params['USER-ID'] = local_var_params['user_id']

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

    def list_spark_jobs(self, request):
        """查询批处理作业列表

        该API用于查询Project下某队列批处理作业的列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSparkJobs
        :type request: :class:`huaweicloudsdkdli.v1.ListSparkJobsRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ListSparkJobsResponse`
        """
        http_info = self._list_spark_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_spark_jobs_invoker(self, request):
        http_info = self._list_spark_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_spark_jobs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/batches",
            "request_type": request.__class__.__name__,
            "response_type": "ListSparkJobsResponse"
            }

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

    def show_batch_log(self, request):
        """查询批处理作业日志

        该API用于查询批处理作业的后台日志。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBatchLog
        :type request: :class:`huaweicloudsdkdli.v1.ShowBatchLogRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowBatchLogResponse`
        """
        http_info = self._show_batch_log_http_info(request)
        return self._call_api(**http_info)

    def show_batch_log_invoker(self, request):
        http_info = self._show_batch_log_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_batch_log_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/batches/{batch_id}/log",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBatchLogResponse"
            }

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

    def show_spark_job(self, request):
        """查询批处理作业详情

        该API用于根据批处理作业的id查询作业详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSparkJob
        :type request: :class:`huaweicloudsdkdli.v1.ShowSparkJobRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowSparkJobResponse`
        """
        http_info = self._show_spark_job_http_info(request)
        return self._call_api(**http_info)

    def show_spark_job_invoker(self, request):
        http_info = self._show_spark_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_spark_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/batches/{batch_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSparkJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'batch_id' in local_var_params:
            path_params['batch_id'] = local_var_params['batch_id']

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

    def show_spark_job_status(self, request):
        """查询批处理作业状态

        该API用于查询批处理作业的状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSparkJobStatus
        :type request: :class:`huaweicloudsdkdli.v1.ShowSparkJobStatusRequest`
        :rtype: :class:`huaweicloudsdkdli.v1.ShowSparkJobStatusResponse`
        """
        http_info = self._show_spark_job_status_http_info(request)
        return self._call_api(**http_info)

    def show_spark_job_status_invoker(self, request):
        http_info = self._show_spark_job_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_spark_job_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/batches/{batch_id}/state",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSparkJobStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'batch_id' in local_var_params:
            path_params['batch_id'] = local_var_params['batch_id']

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
