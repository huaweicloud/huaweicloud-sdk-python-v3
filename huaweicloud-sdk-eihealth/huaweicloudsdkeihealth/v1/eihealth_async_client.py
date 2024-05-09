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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkeihealth'")


class EiHealthAsyncClient(Client):
    def __init__(self):
        super(EiHealthAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkeihealth.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "EiHealthAsyncClient":
                raise TypeError("client type error, support client type is EiHealthAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_drug_database_file_async(self, request):
        """数据库追加文件

        数据库追加文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddDrugDatabaseFile
        :type request: :class:`huaweicloudsdkeihealth.v1.AddDrugDatabaseFileRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.AddDrugDatabaseFileResponse`
        """
        http_info = self._add_drug_database_file_http_info(request)
        return self._call_api(**http_info)

    def add_drug_database_file_async_invoker(self, request):
        http_info = self._add_drug_database_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_drug_database_file_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/drug/databases/{database_id}/data",
            "request_type": request.__class__.__name__,
            "response_type": "AddDrugDatabaseFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'database_id' in local_var_params:
            path_params['database_id'] = local_var_params['database_id']

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

    def batch_cancel_job_async(self, request):
        """批量取消作业

        批量取消作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCancelJob
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchCancelJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchCancelJobResponse`
        """
        http_info = self._batch_cancel_job_http_info(request)
        return self._call_api(**http_info)

    def batch_cancel_job_async_invoker(self, request):
        http_info = self._batch_cancel_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_cancel_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/batch-terminate",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCancelJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []

        header_params = {}
        if 'x_force' in local_var_params:
            header_params['X-Force'] = local_var_params['x_force']

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

    def batch_delete_data_async(self, request):
        """批量删除项目数据

        批量删除项目数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteData
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchDeleteDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchDeleteDataResponse`
        """
        http_info = self._batch_delete_data_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_data_async_invoker(self, request):
        http_info = self._batch_delete_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_data_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def batch_delete_job_async(self, request):
        """批量删除作业

        批量删除作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteJob
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchDeleteJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchDeleteJobResponse`
        """
        http_info = self._batch_delete_job_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_job_async_invoker(self, request):
        http_info = self._batch_delete_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def batch_delete_label_async(self, request):
        """批量删除标签

        批量删除标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteLabel
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchDeleteLabelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchDeleteLabelResponse`
        """
        http_info = self._batch_delete_label_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_label_async_invoker(self, request):
        http_info = self._batch_delete_label_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_label_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/system/labels/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteLabelResponse"
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

    def batch_delete_member_async(self, request):
        """批量删除项目成员

        批量删除项目成员
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteMember
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchDeleteMemberRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchDeleteMemberResponse`
        """
        http_info = self._batch_delete_member_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_member_async_invoker(self, request):
        http_info = self._batch_delete_member_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_member_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/members/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteMemberResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def batch_delete_notice_async(self, request):
        """批量删除通知消息

        批量删除通知消息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteNotice
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchDeleteNoticeRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchDeleteNoticeResponse`
        """
        http_info = self._batch_delete_notice_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_notice_async_invoker(self, request):
        http_info = self._batch_delete_notice_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_notice_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/notices/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteNoticeResponse"
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

    def batch_delete_tag_async(self, request):
        """批量删除镜像tag

        批量删除镜像tag
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteTag
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchDeleteTagRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchDeleteTagResponse`
        """
        http_info = self._batch_delete_tag_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_tag_async_invoker(self, request):
        http_info = self._batch_delete_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images/{image_id}/tags/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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

    def batch_download_resource_stat_data_async(self, request):
        """批量获取资源统计数据

        批量获取资源统计数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDownloadResourceStatData
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchDownloadResourceStatDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchDownloadResourceStatDataResponse`
        """
        http_info = self._batch_download_resource_stat_data_http_info(request)
        return self._call_api(**http_info)

    def batch_download_resource_stat_data_async_invoker(self, request):
        http_info = self._batch_download_resource_stat_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_download_resource_stat_data_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/metric-data/batch-stat-metric-data",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDownloadResourceStatDataResponse"
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

    def batch_import_app_async(self, request):
        """导入应用

        批量导入应用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchImportApp
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchImportAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchImportAppResponse`
        """
        http_info = self._batch_import_app_http_info(request)
        return self._call_api(**http_info)

    def batch_import_app_async_invoker(self, request):
        http_info = self._batch_import_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_import_app_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/apps/batch-import",
            "request_type": request.__class__.__name__,
            "response_type": "BatchImportAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def batch_retry_job_async(self, request):
        """批量重试作业

        批量重试作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchRetryJob
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchRetryJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchRetryJobResponse`
        """
        http_info = self._batch_retry_job_http_info(request)
        return self._call_api(**http_info)

    def batch_retry_job_async_invoker(self, request):
        http_info = self._batch_retry_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_retry_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/batch-retry",
            "request_type": request.__class__.__name__,
            "response_type": "BatchRetryJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def batch_update_node_label_async(self, request):
        """设置节点标签

        设置节点标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchUpdateNodeLabel
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchUpdateNodeLabelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchUpdateNodeLabelResponse`
        """
        http_info = self._batch_update_node_label_http_info(request)
        return self._call_api(**http_info)

    def batch_update_node_label_async_invoker(self, request):
        http_info = self._batch_update_node_label_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_update_node_label_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/system/nodes/{server_id}/labels",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateNodeLabelResponse"
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

    def batch_update_notice_async(self, request):
        """批量更新消息

        批量更新消息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchUpdateNotice
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchUpdateNoticeRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchUpdateNoticeResponse`
        """
        http_info = self._batch_update_notice_http_info(request)
        return self._call_api(**http_info)

    def batch_update_notice_async_invoker(self, request):
        http_info = self._batch_update_notice_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_update_notice_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/notices/batch-update",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateNoticeResponse"
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

    def cancel_data_job_async(self, request):
        """取消数据作业

        取消数据作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CancelDataJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CancelDataJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CancelDataJobResponse`
        """
        http_info = self._cancel_data_job_http_info(request)
        return self._call_api(**http_info)

    def cancel_data_job_async_invoker(self, request):
        http_info = self._cancel_data_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _cancel_data_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/data-jobs/{data_job_id}/cancel",
            "request_type": request.__class__.__name__,
            "response_type": "CancelDataJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'data_job_id' in local_var_params:
            path_params['data_job_id'] = local_var_params['data_job_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def cancel_drug_job_async(self, request):
        """取消药物作业

        取消药物作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CancelDrugJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CancelDrugJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CancelDrugJobResponse`
        """
        http_info = self._cancel_drug_job_http_info(request)
        return self._call_api(**http_info)

    def cancel_drug_job_async_invoker(self, request):
        http_info = self._cancel_drug_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _cancel_drug_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/{job_id}/cancel",
            "request_type": request.__class__.__name__,
            "response_type": "CancelDrugJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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

    def cancel_job_async(self, request):
        """取消或强制停止作业调度

        取消或强制作业调度
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CancelJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CancelJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CancelJobResponse`
        """
        http_info = self._cancel_job_http_info(request)
        return self._call_api(**http_info)

    def cancel_job_async_invoker(self, request):
        http_info = self._cancel_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _cancel_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}/terminate",
            "request_type": request.__class__.__name__,
            "response_type": "CancelJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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

    def change_password_async(self, request):
        """修改密码

        修改密码
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangePassword
        :type request: :class:`huaweicloudsdkeihealth.v1.ChangePasswordRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ChangePasswordResponse`
        """
        http_info = self._change_password_http_info(request)
        return self._call_api(**http_info)

    def change_password_async_invoker(self, request):
        http_info = self._change_password_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_password_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/users/{user_id}/password",
            "request_type": request.__class__.__name__,
            "response_type": "ChangePasswordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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

    def check_email_connection_async(self, request):
        """邮箱连通性测试

        邮箱连通性测试
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckEmailConnection
        :type request: :class:`huaweicloudsdkeihealth.v1.CheckEmailConnectionRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CheckEmailConnectionResponse`
        """
        http_info = self._check_email_connection_http_info(request)
        return self._call_api(**http_info)

    def check_email_connection_async_invoker(self, request):
        http_info = self._check_email_connection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_email_connection_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/messages/email-connection-test",
            "request_type": request.__class__.__name__,
            "response_type": "CheckEmailConnectionResponse"
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

    def check_token_verification_async(self, request):
        """校验token

        校验token是否可访问当前环境
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckTokenVerification
        :type request: :class:`huaweicloudsdkeihealth.v1.CheckTokenVerificationRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CheckTokenVerificationResponse`
        """
        http_info = self._check_token_verification_http_info(request)
        return self._call_api(**http_info)

    def check_token_verification_async_invoker(self, request):
        http_info = self._check_token_verification_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_token_verification_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/users/token-verification",
            "request_type": request.__class__.__name__,
            "response_type": "CheckTokenVerificationResponse"
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

    def copy_data_async(self, request):
        """复制项目数据

        复制项目数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CopyData
        :type request: :class:`huaweicloudsdkeihealth.v1.CopyDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CopyDataResponse`
        """
        http_info = self._copy_data_http_info(request)
        return self._call_api(**http_info)

    def copy_data_async_invoker(self, request):
        http_info = self._copy_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _copy_data_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/clone",
            "request_type": request.__class__.__name__,
            "response_type": "CopyDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def create_admet_job_async(self, request):
        """创建分子属性预测作业

        创建分子属性预测作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAdmetJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateAdmetJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateAdmetJobResponse`
        """
        http_info = self._create_admet_job_http_info(request)
        return self._call_api(**http_info)

    def create_admet_job_async_invoker(self, request):
        http_info = self._create_admet_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_admet_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/admet",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAdmetJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def create_app_async(self, request):
        """创建应用

        创建应用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateApp
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateAppResponse`
        """
        http_info = self._create_app_http_info(request)
        return self._call_api(**http_info)

    def create_app_async_invoker(self, request):
        http_info = self._create_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_app_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/apps",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def create_auto_job_async(self, request):
        """创建自动作业模板

        创建自动作业模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAutoJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateAutoJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateAutoJobResponse`
        """
        http_info = self._create_auto_job_http_info(request)
        return self._call_api(**http_info)

    def create_auto_job_async_invoker(self, request):
        http_info = self._create_auto_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_auto_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/auto-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAutoJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def create_backup_async(self, request):
        """归档数据

        将需要归档的重要数据拷贝到数据归档桶
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateBackup
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateBackupRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateBackupResponse`
        """
        http_info = self._create_backup_http_info(request)
        return self._call_api(**http_info)

    def create_backup_async_invoker(self, request):
        http_info = self._create_backup_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_backup_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/backups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateBackupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def create_cluster_job_async(self, request):
        """创建分子聚类作业

        创建分子聚类作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateClusterJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateClusterJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateClusterJobResponse`
        """
        http_info = self._create_cluster_job_http_info(request)
        return self._call_api(**http_info)

    def create_cluster_job_async_invoker(self, request):
        http_info = self._create_cluster_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_cluster_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/{job_id}/cluster",
            "request_type": request.__class__.__name__,
            "response_type": "CreateClusterJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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

    def create_code_async(self, request):
        """发送验证码

        发送验证码
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCode
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateCodeRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateCodeResponse`
        """
        http_info = self._create_code_http_info(request)
        return self._call_api(**http_info)

    def create_code_async_invoker(self, request):
        http_info = self._create_code_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_code_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/users/{user_id}/verification-code",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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

    def create_computing_resource_async(self, request):
        """购买计算资源

        购买计算资源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateComputingResource
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateComputingResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateComputingResourceResponse`
        """
        http_info = self._create_computing_resource_http_info(request)
        return self._call_api(**http_info)

    def create_computing_resource_async_invoker(self, request):
        http_info = self._create_computing_resource_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_computing_resource_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/system/computing-resources",
            "request_type": request.__class__.__name__,
            "response_type": "CreateComputingResourceResponse"
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

    def create_data_async(self, request):
        """创建文件夹

        创建文件夹
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateData
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDataResponse`
        """
        http_info = self._create_data_http_info(request)
        return self._call_api(**http_info)

    def create_data_async_invoker(self, request):
        http_info = self._create_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_data_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def create_database_data_async(self, request):
        """插入单条数据

        插入单条数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDatabaseData
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDatabaseDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDatabaseDataResponse`
        """
        http_info = self._create_database_data_http_info(request)
        return self._call_api(**http_info)

    def create_database_data_async_invoker(self, request):
        http_info = self._create_database_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_database_data_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases/{database_id}/data/insert",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDatabaseDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'database_id' in local_var_params:
            path_params['database_id'] = local_var_params['database_id']

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

    def create_database_resource_async(self, request):
        """购买数据库资源

        购买数据库资源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDatabaseResource
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDatabaseResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDatabaseResourceResponse`
        """
        http_info = self._create_database_resource_http_info(request)
        return self._call_api(**http_info)

    def create_database_resource_async_invoker(self, request):
        http_info = self._create_database_resource_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_database_resource_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/system/database-resources",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDatabaseResourceResponse"
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

    def create_docking_job_async(self, request):
        """创建分子对接作业

        创建分子对接作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDockingJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDockingJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDockingJobResponse`
        """
        http_info = self._create_docking_job_http_info(request)
        return self._call_api(**http_info)

    def create_docking_job_async_invoker(self, request):
        http_info = self._create_docking_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_docking_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/docking",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDockingJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def create_drug_database_async(self, request):
        """创建数据库

        创建数据库
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDrugDatabase
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDrugDatabaseRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDrugDatabaseResponse`
        """
        http_info = self._create_drug_database_http_info(request)
        return self._call_api(**http_info)

    def create_drug_database_async_invoker(self, request):
        http_info = self._create_drug_database_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_drug_database_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/drug/databases",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDrugDatabaseResponse"
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

    def create_drug_model_async(self, request):
        """创建模型

        创建模型
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDrugModel
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDrugModelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDrugModelResponse`
        """
        http_info = self._create_drug_model_http_info(request)
        return self._call_api(**http_info)

    def create_drug_model_async_invoker(self, request):
        http_info = self._create_drug_model_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_drug_model_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/drug-models",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDrugModelResponse"
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

    def create_fep_job_async(self, request):
        """创建自由能微扰作业

        创建自由能微扰作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateFepJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateFepJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateFepJobResponse`
        """
        http_info = self._create_fep_job_http_info(request)
        return self._call_api(**http_info)

    def create_fep_job_async_invoker(self, request):
        http_info = self._create_fep_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_fep_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/fep",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFepJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def create_image_async(self, request):
        """创建镜像

        创建镜像
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateImage
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateImageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateImageResponse`
        """
        http_info = self._create_image_http_info(request)
        return self._call_api(**http_info)

    def create_image_async_invoker(self, request):
        http_info = self._create_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_image_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images",
            "request_type": request.__class__.__name__,
            "response_type": "CreateImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def create_instance_async(self, request):
        """创建数据库实例

        创建数据库实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInstance
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateInstanceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateInstanceResponse`
        """
        http_info = self._create_instance_http_info(request)
        return self._call_api(**http_info)

    def create_instance_async_invoker(self, request):
        http_info = self._create_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def create_label_async(self, request):
        """创建标签

        创建标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateLabel
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateLabelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateLabelResponse`
        """
        http_info = self._create_label_http_info(request)
        return self._call_api(**http_info)

    def create_label_async_invoker(self, request):
        http_info = self._create_label_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_label_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/system/labels",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLabelResponse"
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

    def create_label_page_async(self, request):
        """创建标签页面

        创建标签页面
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateLabelPage
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateLabelPageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateLabelPageResponse`
        """
        http_info = self._create_label_page_http_info(request)
        return self._call_api(**http_info)

    def create_label_page_async_invoker(self, request):
        http_info = self._create_label_page_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_label_page_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/label-pages",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLabelPageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def create_mol_batch_download_task_async(self, request):
        """创建分子或分子复合物批量下载任务

        创建分子或分子复合物批量下载任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMolBatchDownloadTask
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateMolBatchDownloadTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateMolBatchDownloadTaskResponse`
        """
        http_info = self._create_mol_batch_download_task_http_info(request)
        return self._call_api(**http_info)

    def create_mol_batch_download_task_async_invoker(self, request):
        http_info = self._create_mol_batch_download_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_mol_batch_download_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/toolkit/batch-download",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMolBatchDownloadTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def create_optm_job_async(self, request):
        """创建分子优化作业

        创建分子优化作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateOptmJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateOptmJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateOptmJobResponse`
        """
        http_info = self._create_optm_job_http_info(request)
        return self._call_api(**http_info)

    def create_optm_job_async_invoker(self, request):
        http_info = self._create_optm_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_optm_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/optimization",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOptmJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def create_performance_resource_async(self, request):
        """购买性能加速资源

        购买性能加速资源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePerformanceResource
        :type request: :class:`huaweicloudsdkeihealth.v1.CreatePerformanceResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreatePerformanceResourceResponse`
        """
        http_info = self._create_performance_resource_http_info(request)
        return self._call_api(**http_info)

    def create_performance_resource_async_invoker(self, request):
        http_info = self._create_performance_resource_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_performance_resource_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/system/performance-resources",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePerformanceResourceResponse"
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

    def create_pocket_detection_job_async(self, request):
        """创建靶点口袋发现作业

        创建靶点口袋发现作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePocketDetectionJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreatePocketDetectionJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreatePocketDetectionJobResponse`
        """
        http_info = self._create_pocket_detection_job_http_info(request)
        return self._call_api(**http_info)

    def create_pocket_detection_job_async_invoker(self, request):
        http_info = self._create_pocket_detection_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_pocket_detection_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/pocket-detection",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePocketDetectionJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def create_pocket_mol_design_job_async(self, request):
        """创建靶点口袋分子设计作业

        创建靶点口袋分子设计作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePocketMolDesignJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreatePocketMolDesignJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreatePocketMolDesignJobResponse`
        """
        http_info = self._create_pocket_mol_design_job_http_info(request)
        return self._call_api(**http_info)

    def create_pocket_mol_design_job_async_invoker(self, request):
        http_info = self._create_pocket_mol_design_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_pocket_mol_design_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/pocket-mol-design",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePocketMolDesignJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def create_project_async(self, request):
        """创建项目

        创建项目
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateProject
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateProjectRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateProjectResponse`
        """
        http_info = self._create_project_http_info(request)
        return self._call_api(**http_info)

    def create_project_async_invoker(self, request):
        http_info = self._create_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_project_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects",
            "request_type": request.__class__.__name__,
            "response_type": "CreateProjectResponse"
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

    def create_scale_out_policy_async(self, request):
        """创建扩容策略

        创建扩容策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateScaleOutPolicy
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateScaleOutPolicyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateScaleOutPolicyResponse`
        """
        http_info = self._create_scale_out_policy_http_info(request)
        return self._call_api(**http_info)

    def create_scale_out_policy_async_invoker(self, request):
        http_info = self._create_scale_out_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_scale_out_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/system/autoscaler/scale-out-policies",
            "request_type": request.__class__.__name__,
            "response_type": "CreateScaleOutPolicyResponse"
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

    def create_search_job_async(self, request):
        """创建分子搜索作业

        创建分子搜索作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSearchJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateSearchJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateSearchJobResponse`
        """
        http_info = self._create_search_job_http_info(request)
        return self._call_api(**http_info)

    def create_search_job_async_invoker(self, request):
        http_info = self._create_search_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_search_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/search",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSearchJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def create_study_async(self, request):
        """创建study

        创建study
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateStudy
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateStudyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateStudyResponse`
        """
        http_info = self._create_study_http_info(request)
        return self._call_api(**http_info)

    def create_study_async_invoker(self, request):
        http_info = self._create_study_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_study_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/studies",
            "request_type": request.__class__.__name__,
            "response_type": "CreateStudyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def create_study_job_async(self, request):
        """创建study作业

        创建study作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateStudyJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateStudyJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateStudyJobResponse`
        """
        http_info = self._create_study_job_http_info(request)
        return self._call_api(**http_info)

    def create_study_job_async_invoker(self, request):
        http_info = self._create_study_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_study_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/studies/{study_id}/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateStudyJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'study_id' in local_var_params:
            path_params['study_id'] = local_var_params['study_id']

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

    def create_synthesis_job_async(self, request):
        """创建分子合成路径规划作业

        创建分子合成路径规划作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSynthesisJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateSynthesisJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateSynthesisJobResponse`
        """
        http_info = self._create_synthesis_job_http_info(request)
        return self._call_api(**http_info)

    def create_synthesis_job_async_invoker(self, request):
        http_info = self._create_synthesis_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_synthesis_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/synthesis",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSynthesisJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def create_template_async(self, request):
        """创建模板

        创建模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTemplate
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateTemplateRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateTemplateResponse`
        """
        http_info = self._create_template_http_info(request)
        return self._call_api(**http_info)

    def create_template_async_invoker(self, request):
        http_info = self._create_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_template_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/templates",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def create_user_async(self, request):
        """创建用户

        创建用户
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateUser
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateUserRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateUserResponse`
        """
        http_info = self._create_user_http_info(request)
        return self._call_api(**http_info)

    def create_user_async_invoker(self, request):
        http_info = self._create_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_user_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "CreateUserResponse"
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

    def create_workflow_async(self, request):
        """创建流程

        创建流程
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateWorkflowResponse`
        """
        http_info = self._create_workflow_http_info(request)
        return self._call_api(**http_info)

    def create_workflow_async_invoker(self, request):
        http_info = self._create_workflow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_workflow_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/workflows",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWorkflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def delete_app_async(self, request):
        """删除应用

        删除应用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteApp
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteAppResponse`
        """
        http_info = self._delete_app_http_info(request)
        return self._call_api(**http_info)

    def delete_app_async_invoker(self, request):
        http_info = self._delete_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_app_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def delete_asset_version_async(self, request):
        """删除资产指定版本

        删除资产指定版本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAssetVersion
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteAssetVersionRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteAssetVersionResponse`
        """
        http_info = self._delete_asset_version_http_info(request)
        return self._call_api(**http_info)

    def delete_asset_version_async_invoker(self, request):
        http_info = self._delete_asset_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_asset_version_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/assets/{asset_id}/versions/{version}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAssetVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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

    def delete_auto_job_async(self, request):
        """删除自动作业模板

        删除自动作业模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAutoJob
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteAutoJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteAutoJobResponse`
        """
        http_info = self._delete_auto_job_http_info(request)
        return self._call_api(**http_info)

    def delete_auto_job_async_invoker(self, request):
        http_info = self._delete_auto_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_auto_job_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/auto-jobs/{auto_job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAutoJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'auto_job_id' in local_var_params:
            path_params['auto_job_id'] = local_var_params['auto_job_id']

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

    def delete_backup_async(self, request):
        """删除归档

        删除指定的归档
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBackup
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteBackupRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteBackupResponse`
        """
        http_info = self._delete_backup_http_info(request)
        return self._call_api(**http_info)

    def delete_backup_async_invoker(self, request):
        http_info = self._delete_backup_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_backup_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/backups/{backup_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBackupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def delete_computing_resource_async(self, request):
        """删除计算资源

        删除计算资源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteComputingResource
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteComputingResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteComputingResourceResponse`
        """
        http_info = self._delete_computing_resource_http_info(request)
        return self._call_api(**http_info)

    def delete_computing_resource_async_invoker(self, request):
        http_info = self._delete_computing_resource_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_computing_resource_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/system/computing-resources/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteComputingResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def delete_data_job_async(self, request):
        """删除数据作业

        删除数据作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDataJob
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteDataJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteDataJobResponse`
        """
        http_info = self._delete_data_job_http_info(request)
        return self._call_api(**http_info)

    def delete_data_job_async_invoker(self, request):
        http_info = self._delete_data_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_data_job_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/data-jobs/{data_job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDataJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'data_job_id' in local_var_params:
            path_params['data_job_id'] = local_var_params['data_job_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def delete_database_data_async(self, request):
        """删除数据

        删除指定行数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDatabaseData
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteDatabaseDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteDatabaseDataResponse`
        """
        http_info = self._delete_database_data_http_info(request)
        return self._call_api(**http_info)

    def delete_database_data_async_invoker(self, request):
        http_info = self._delete_database_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_database_data_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases/{database_id}/data/{row_num}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDatabaseDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'database_id' in local_var_params:
            path_params['database_id'] = local_var_params['database_id']
        if 'row_num' in local_var_params:
            path_params['row_num'] = local_var_params['row_num']

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

    def delete_database_resource_async(self, request):
        """删除数据库资源

        删除数据库资源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDatabaseResource
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteDatabaseResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteDatabaseResourceResponse`
        """
        http_info = self._delete_database_resource_http_info(request)
        return self._call_api(**http_info)

    def delete_database_resource_async_invoker(self, request):
        http_info = self._delete_database_resource_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_database_resource_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/system/database-resources/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDatabaseResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def delete_drug_database_async(self, request):
        """删除数据库

        删除数据库
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDrugDatabase
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteDrugDatabaseRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteDrugDatabaseResponse`
        """
        http_info = self._delete_drug_database_http_info(request)
        return self._call_api(**http_info)

    def delete_drug_database_async_invoker(self, request):
        http_info = self._delete_drug_database_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_drug_database_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/drug/databases/{database_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDrugDatabaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'database_id' in local_var_params:
            path_params['database_id'] = local_var_params['database_id']

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

    def delete_drug_job_async(self, request):
        """删除药物作业

        删除药物作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDrugJob
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteDrugJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteDrugJobResponse`
        """
        http_info = self._delete_drug_job_http_info(request)
        return self._call_api(**http_info)

    def delete_drug_job_async_invoker(self, request):
        http_info = self._delete_drug_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_drug_job_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDrugJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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

    def delete_drug_model_async(self, request):
        """删除模型

        删除模型
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDrugModel
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteDrugModelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteDrugModelResponse`
        """
        http_info = self._delete_drug_model_http_info(request)
        return self._call_api(**http_info)

    def delete_drug_model_async_invoker(self, request):
        http_info = self._delete_drug_model_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_drug_model_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/drug-models/{model_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDrugModelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'model_id' in local_var_params:
            path_params['model_id'] = local_var_params['model_id']

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

    def delete_image_async(self, request):
        """删除镜像仓库

        删除镜像仓库
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteImage
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteImageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteImageResponse`
        """
        http_info = self._delete_image_http_info(request)
        return self._call_api(**http_info)

    def delete_image_async_invoker(self, request):
        http_info = self._delete_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_image_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images/{image_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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

    def delete_instance_async(self, request):
        """删除实例

        删除实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteInstance
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteInstanceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteInstanceResponse`
        """
        http_info = self._delete_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_async_invoker(self, request):
        http_info = self._delete_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_instance_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases/{database_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'database_id' in local_var_params:
            path_params['database_id'] = local_var_params['database_id']

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

    def delete_job_async(self, request):
        """删除作业

        删除作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteJob
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteJobResponse`
        """
        http_info = self._delete_job_http_info(request)
        return self._call_api(**http_info)

    def delete_job_async_invoker(self, request):
        http_info = self._delete_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_job_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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

    def delete_label_async(self, request):
        """删除标签

        删除标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteLabel
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteLabelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteLabelResponse`
        """
        http_info = self._delete_label_http_info(request)
        return self._call_api(**http_info)

    def delete_label_async_invoker(self, request):
        http_info = self._delete_label_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_label_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/system/labels/{label_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLabelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'label_id' in local_var_params:
            path_params['label_id'] = local_var_params['label_id']

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

    def delete_label_page_async(self, request):
        """删除标签页面

        删除标签页面
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteLabelPage
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteLabelPageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteLabelPageResponse`
        """
        http_info = self._delete_label_page_http_info(request)
        return self._call_api(**http_info)

    def delete_label_page_async_invoker(self, request):
        http_info = self._delete_label_page_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_label_page_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/label-pages/{label_page_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLabelPageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'label_page_id' in local_var_params:
            path_params['label_page_id'] = local_var_params['label_page_id']

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

    def delete_member_async(self, request):
        """移除项目成员

        移除项目成员
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteMember
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteMemberRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteMemberResponse`
        """
        http_info = self._delete_member_http_info(request)
        return self._call_api(**http_info)

    def delete_member_async_invoker(self, request):
        http_info = self._delete_member_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_member_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/members/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMemberResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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

    def delete_message_email_config_async(self, request):
        """删除消息邮件配置

        删除消息邮件配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteMessageEmailConfig
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteMessageEmailConfigRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteMessageEmailConfigResponse`
        """
        http_info = self._delete_message_email_config_http_info(request)
        return self._call_api(**http_info)

    def delete_message_email_config_async_invoker(self, request):
        http_info = self._delete_message_email_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_message_email_config_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/messages/email-server-config",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMessageEmailConfigResponse"
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

    def delete_performance_resource_async(self, request):
        """删除性能加速资源

        删除性能加速资源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePerformanceResource
        :type request: :class:`huaweicloudsdkeihealth.v1.DeletePerformanceResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeletePerformanceResourceResponse`
        """
        http_info = self._delete_performance_resource_http_info(request)
        return self._call_api(**http_info)

    def delete_performance_resource_async_invoker(self, request):
        http_info = self._delete_performance_resource_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_performance_resource_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/system/performance-resources/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePerformanceResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def delete_project_async(self, request):
        """删除项目

        删除项目
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteProject
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteProjectRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteProjectResponse`
        """
        http_info = self._delete_project_http_info(request)
        return self._call_api(**http_info)

    def delete_project_async_invoker(self, request):
        http_info = self._delete_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_project_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []

        header_params = {}
        if 'x_delete_now' in local_var_params:
            header_params['X-Delete-Now'] = local_var_params['x_delete_now']

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

    def delete_scale_out_policy_async(self, request):
        """删除扩容策略

        删除扩容策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteScaleOutPolicy
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteScaleOutPolicyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteScaleOutPolicyResponse`
        """
        http_info = self._delete_scale_out_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_scale_out_policy_async_invoker(self, request):
        http_info = self._delete_scale_out_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_scale_out_policy_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/system/autoscaler/scale-out-policies/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteScaleOutPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def delete_star_async(self, request):
        """取消收藏

        取消收藏
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteStar
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteStarRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteStarResponse`
        """
        http_info = self._delete_star_http_info(request)
        return self._call_api(**http_info)

    def delete_star_async_invoker(self, request):
        http_info = self._delete_star_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_star_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/assets/{asset_id}/stars",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteStarResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

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

    def delete_study_async(self, request):
        """删除study

        删除study
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteStudy
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteStudyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteStudyResponse`
        """
        http_info = self._delete_study_http_info(request)
        return self._call_api(**http_info)

    def delete_study_async_invoker(self, request):
        http_info = self._delete_study_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_study_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/studies/{study_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteStudyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'study_id' in local_var_params:
            path_params['study_id'] = local_var_params['study_id']

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

    def delete_tag_async(self, request):
        """删除指定镜像tag

        删除指定镜像tag
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTag
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteTagRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteTagResponse`
        """
        http_info = self._delete_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_tag_async_invoker(self, request):
        http_info = self._delete_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_tag_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images/{image_id}/tags/{tag}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']
        if 'tag' in local_var_params:
            path_params['tag'] = local_var_params['tag']

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

    def delete_template_async(self, request):
        """删除模板

        删除模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTemplate
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteTemplateRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteTemplateResponse`
        """
        http_info = self._delete_template_http_info(request)
        return self._call_api(**http_info)

    def delete_template_async_invoker(self, request):
        http_info = self._delete_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_template_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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

    def delete_user_async(self, request):
        """删除用户

        删除用户
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteUser
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteUserRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteUserResponse`
        """
        http_info = self._delete_user_http_info(request)
        return self._call_api(**http_info)

    def delete_user_async_invoker(self, request):
        http_info = self._delete_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_user_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/users/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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

    def delete_workflow_async(self, request):
        """删除流程

        删除流程
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteWorkflowResponse`
        """
        http_info = self._delete_workflow_http_info(request)
        return self._call_api(**http_info)

    def delete_workflow_async_invoker(self, request):
        http_info = self._delete_workflow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_workflow_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/workflows/{workflow_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteWorkflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

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

    def download_data_job_log_async(self, request):
        """下载数据作业执行日志

        下载数据作业执行日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadDataJobLog
        :type request: :class:`huaweicloudsdkeihealth.v1.DownloadDataJobLogRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DownloadDataJobLogResponse`
        """
        http_info = self._download_data_job_log_http_info(request)
        return self._call_api(**http_info)

    def download_data_job_log_async_invoker(self, request):
        http_info = self._download_data_job_log_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_data_job_log_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/data-jobs/{data_job_id}/logs",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadDataJobLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'data_job_id' in local_var_params:
            path_params['data_job_id'] = local_var_params['data_job_id']

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

    def download_data_trace_async(self, request):
        """下载近一万条审计日志

        下载近一万条审计日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadDataTrace
        :type request: :class:`huaweicloudsdkeihealth.v1.DownloadDataTraceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DownloadDataTraceResponse`
        """
        http_info = self._download_data_trace_http_info(request)
        return self._call_api(**http_info)

    def download_data_trace_async_invoker(self, request):
        http_info = self._download_data_trace_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_data_trace_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/data-traces",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadDataTraceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []

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

    def execute_asset_action_async(self, request):
        """操作资产发布状态

        操作资产发布状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteAssetAction
        :type request: :class:`huaweicloudsdkeihealth.v1.ExecuteAssetActionRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ExecuteAssetActionResponse`
        """
        http_info = self._execute_asset_action_http_info(request)
        return self._call_api(**http_info)

    def execute_asset_action_async_invoker(self, request):
        http_info = self._execute_asset_action_http_info(request)
        return AsyncInvoker(self, http_info)

    def _execute_asset_action_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/assets/{asset_id}/versions/{version}/action",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteAssetActionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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

    def execute_job_async(self, request):
        """启动作业

        启动作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ExecuteJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ExecuteJobResponse`
        """
        http_info = self._execute_job_http_info(request)
        return self._call_api(**http_info)

    def execute_job_async_invoker(self, request):
        http_info = self._execute_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _execute_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def generate_complex_combine_async(self, request):
        """将传入的蛋白和小分子拼接成复合物结构

        将传入的蛋白和小分子拼接成复合物结构
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GenerateComplexCombine
        :type request: :class:`huaweicloudsdkeihealth.v1.GenerateComplexCombineRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.GenerateComplexCombineResponse`
        """
        http_info = self._generate_complex_combine_http_info(request)
        return self._call_api(**http_info)

    def generate_complex_combine_async_invoker(self, request):
        http_info = self._generate_complex_combine_http_info(request)
        return AsyncInvoker(self, http_info)

    def _generate_complex_combine_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/toolkit/complex-combine",
            "request_type": request.__class__.__name__,
            "response_type": "GenerateComplexCombineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def generate_pocket_file_async(self, request):
        """根据center、size、padding参数生成可渲染的口袋文件内容

        根据center、size、padding参数生成可渲染的口袋文件内容
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GeneratePocketFile
        :type request: :class:`huaweicloudsdkeihealth.v1.GeneratePocketFileRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.GeneratePocketFileResponse`
        """
        http_info = self._generate_pocket_file_http_info(request)
        return self._call_api(**http_info)

    def generate_pocket_file_async_invoker(self, request):
        http_info = self._generate_pocket_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _generate_pocket_file_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/toolkit/pocket",
            "request_type": request.__class__.__name__,
            "response_type": "GeneratePocketFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def generate_surface_points_async(self, request):
        """根据表面离散点坐标集生成可渲染的文件内容

        根据表面离散点坐标集生成可渲染的文件内容
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GenerateSurfacePoints
        :type request: :class:`huaweicloudsdkeihealth.v1.GenerateSurfacePointsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.GenerateSurfacePointsResponse`
        """
        http_info = self._generate_surface_points_http_info(request)
        return self._call_api(**http_info)

    def generate_surface_points_async_invoker(self, request):
        http_info = self._generate_surface_points_http_info(request)
        return AsyncInvoker(self, http_info)

    def _generate_surface_points_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/toolkit/surface-points",
            "request_type": request.__class__.__name__,
            "response_type": "GenerateSurfacePointsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def import_data_async(self, request):
        """导入项目数据

        导入项目数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportData
        :type request: :class:`huaweicloudsdkeihealth.v1.ImportDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImportDataResponse`
        """
        http_info = self._import_data_http_info(request)
        return self._call_api(**http_info)

    def import_data_async_invoker(self, request):
        http_info = self._import_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _import_data_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def import_database_data_async(self, request):
        """导入数据

        导入数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportDatabaseData
        :type request: :class:`huaweicloudsdkeihealth.v1.ImportDatabaseDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImportDatabaseDataResponse`
        """
        http_info = self._import_database_data_http_info(request)
        return self._call_api(**http_info)

    def import_database_data_async_invoker(self, request):
        http_info = self._import_database_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _import_database_data_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases/{database_id}/data",
            "request_type": request.__class__.__name__,
            "response_type": "ImportDatabaseDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'database_id' in local_var_params:
            path_params['database_id'] = local_var_params['database_id']

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

    def import_image_async(self, request):
        """导入镜像

        导入镜像
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportImage
        :type request: :class:`huaweicloudsdkeihealth.v1.ImportImageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImportImageResponse`
        """
        http_info = self._import_image_http_info(request)
        return self._call_api(**http_info)

    def import_image_async_invoker(self, request):
        http_info = self._import_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _import_image_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images/import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def import_network_data_async(self, request):
        """导入网上数据

        导入网上数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportNetworkData
        :type request: :class:`huaweicloudsdkeihealth.v1.ImportNetworkDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImportNetworkDataResponse`
        """
        http_info = self._import_network_data_http_info(request)
        return self._call_api(**http_info)

    def import_network_data_async_invoker(self, request):
        http_info = self._import_network_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _import_network_data_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/import-from-network",
            "request_type": request.__class__.__name__,
            "response_type": "ImportNetworkDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def import_template_async(self, request):
        """从其他项目导入模板

        从其他项目导入模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportTemplate
        :type request: :class:`huaweicloudsdkeihealth.v1.ImportTemplateRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImportTemplateResponse`
        """
        http_info = self._import_template_http_info(request)
        return self._call_api(**http_info)

    def import_template_async_invoker(self, request):
        http_info = self._import_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _import_template_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/templates/batch-import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def import_user_async(self, request):
        """导入用户

        导入用户
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportUser
        :type request: :class:`huaweicloudsdkeihealth.v1.ImportUserRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImportUserResponse`
        """
        http_info = self._import_user_http_info(request)
        return self._call_api(**http_info)

    def import_user_async_invoker(self, request):
        http_info = self._import_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _import_user_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/users/import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportUserResponse"
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

    def import_workflow_async(self, request):
        """导入流程

        导入流程
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.ImportWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImportWorkflowResponse`
        """
        http_info = self._import_workflow_http_info(request)
        return self._call_api(**http_info)

    def import_workflow_async_invoker(self, request):
        http_info = self._import_workflow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _import_workflow_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/workflows/import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportWorkflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def list_app_async(self, request):
        """获取应用列表

        获取应用列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApp
        :type request: :class:`huaweicloudsdkeihealth.v1.ListAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListAppResponse`
        """
        http_info = self._list_app_http_info(request)
        return self._call_api(**http_info)

    def list_app_async_invoker(self, request):
        http_info = self._list_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_app_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/apps",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))

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

    def list_archive_configs_async(self, request):
        """获取跨域归档配置

        获取跨域归档配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListArchiveConfigs
        :type request: :class:`huaweicloudsdkeihealth.v1.ListArchiveConfigsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListArchiveConfigsResponse`
        """
        http_info = self._list_archive_configs_http_info(request)
        return self._call_api(**http_info)

    def list_archive_configs_async_invoker(self, request):
        http_info = self._list_archive_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_archive_configs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/archive-configs",
            "request_type": request.__class__.__name__,
            "response_type": "ListArchiveConfigsResponse"
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

    def list_asset_async(self, request):
        """获取资产列表

        获取资产列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAsset
        :type request: :class:`huaweicloudsdkeihealth.v1.ListAssetRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListAssetResponse`
        """
        http_info = self._list_asset_http_info(request)
        return self._call_api(**http_info)

    def list_asset_async_invoker(self, request):
        http_info = self._list_asset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_asset_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/assets",
            "request_type": request.__class__.__name__,
            "response_type": "ListAssetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'categories' in local_var_params:
            query_params.append(('categories', local_var_params['categories']))
        if 'key_word' in local_var_params:
            query_params.append(('key_word', local_var_params['key_word']))
        if 'labels' in local_var_params:
            query_params.append(('labels', local_var_params['labels']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'publishers' in local_var_params:
            query_params.append(('publishers', local_var_params['publishers']))
        if 'scope' in local_var_params:
            query_params.append(('scope', local_var_params['scope']))
        if 'vendor_ids' in local_var_params:
            query_params.append(('vendor_ids', local_var_params['vendor_ids']))

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

    def list_auto_job_async(self, request):
        """获取自动作业模板列表

        获取自动作业模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAutoJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ListAutoJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListAutoJobResponse`
        """
        http_info = self._list_auto_job_http_info(request)
        return self._call_api(**http_info)

    def list_auto_job_async_invoker(self, request):
        http_info = self._list_auto_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_auto_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/auto-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListAutoJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

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

    def list_backup_async(self, request):
        """查询归档列表

        分页查询用户管理的项目的所有历史归档记录
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBackup
        :type request: :class:`huaweicloudsdkeihealth.v1.ListBackupRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListBackupResponse`
        """
        http_info = self._list_backup_http_info(request)
        return self._call_api(**http_info)

    def list_backup_async_invoker(self, request):
        http_info = self._list_backup_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_backup_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/backups",
            "request_type": request.__class__.__name__,
            "response_type": "ListBackupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))

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

    def list_bucket_async(self, request):
        """获取桶列表

        获取桶列表(包含当前项目桶和引用项目桶)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBucket
        :type request: :class:`huaweicloudsdkeihealth.v1.ListBucketRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListBucketResponse`
        """
        http_info = self._list_bucket_http_info(request)
        return self._call_api(**http_info)

    def list_bucket_async_invoker(self, request):
        http_info = self._list_bucket_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_bucket_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/buckets",
            "request_type": request.__class__.__name__,
            "response_type": "ListBucketResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def list_checkpoint_async(self, request):
        """获取数据作业执行日志

        获取数据作业执行日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCheckpoint
        :type request: :class:`huaweicloudsdkeihealth.v1.ListCheckpointRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListCheckpointResponse`
        """
        http_info = self._list_checkpoint_http_info(request)
        return self._call_api(**http_info)

    def list_checkpoint_async_invoker(self, request):
        http_info = self._list_checkpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_checkpoint_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/data-jobs/{data_job_id}/checkpoints",
            "request_type": request.__class__.__name__,
            "response_type": "ListCheckpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'data_job_id' in local_var_params:
            path_params['data_job_id'] = local_var_params['data_job_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def list_cluster_all_node_label_async(self, request):
        """获取节点标签集

        获取节点标签集
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListClusterAllNodeLabel
        :type request: :class:`huaweicloudsdkeihealth.v1.ListClusterAllNodeLabelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListClusterAllNodeLabelResponse`
        """
        http_info = self._list_cluster_all_node_label_http_info(request)
        return self._call_api(**http_info)

    def list_cluster_all_node_label_async_invoker(self, request):
        http_info = self._list_cluster_all_node_label_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cluster_all_node_label_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/cluster/labels",
            "request_type": request.__class__.__name__,
            "response_type": "ListClusterAllNodeLabelResponse"
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

    def list_computing_resource_flavors_async(self, request):
        """查询计算资源规格

        查询计算资源规格
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListComputingResourceFlavors
        :type request: :class:`huaweicloudsdkeihealth.v1.ListComputingResourceFlavorsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListComputingResourceFlavorsResponse`
        """
        http_info = self._list_computing_resource_flavors_http_info(request)
        return self._call_api(**http_info)

    def list_computing_resource_flavors_async_invoker(self, request):
        http_info = self._list_computing_resource_flavors_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_computing_resource_flavors_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/computing-resources/flavors",
            "request_type": request.__class__.__name__,
            "response_type": "ListComputingResourceFlavorsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'availability_zone_id' in local_var_params:
            query_params.append(('availability_zone_id', local_var_params['availability_zone_id']))

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

    def list_computing_resources_async(self, request):
        """查询计算资源

        查询计算资源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListComputingResources
        :type request: :class:`huaweicloudsdkeihealth.v1.ListComputingResourcesRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListComputingResourcesResponse`
        """
        http_info = self._list_computing_resources_http_info(request)
        return self._call_api(**http_info)

    def list_computing_resources_async_invoker(self, request):
        http_info = self._list_computing_resources_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_computing_resources_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/computing-resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListComputingResourcesResponse"
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

    def list_data_async(self, request):
        """查询数据列表

        查询指定目录下的数据列表，如果不指定默认查询根目录
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListData
        :type request: :class:`huaweicloudsdkeihealth.v1.ListDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListDataResponse`
        """
        http_info = self._list_data_http_info(request)
        return self._call_api(**http_info)

    def list_data_async_invoker(self, request):
        http_info = self._list_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_data_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas",
            "request_type": request.__class__.__name__,
            "response_type": "ListDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))
        if 'search_key' in local_var_params:
            query_params.append(('search_key', local_var_params['search_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
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

    def list_data_job_async(self, request):
        """获取数据作业列表

        获取数据作业列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDataJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ListDataJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListDataJobResponse`
        """
        http_info = self._list_data_job_http_info(request)
        return self._call_api(**http_info)

    def list_data_job_async_invoker(self, request):
        http_info = self._list_data_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_data_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/data-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListDataJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'creator' in local_var_params:
            query_params.append(('creator', local_var_params['creator']))
        if 'from_time' in local_var_params:
            query_params.append(('from_time', local_var_params['from_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'to_time' in local_var_params:
            query_params.append(('to_time', local_var_params['to_time']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'finish_from_time' in local_var_params:
            query_params.append(('finish_from_time', local_var_params['finish_from_time']))
        if 'finish_to_time' in local_var_params:
            query_params.append(('finish_to_time', local_var_params['finish_to_time']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))

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

    def list_database_data_async(self, request):
        """查询数据

        查询数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDatabaseData
        :type request: :class:`huaweicloudsdkeihealth.v1.ListDatabaseDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListDatabaseDataResponse`
        """
        http_info = self._list_database_data_http_info(request)
        return self._call_api(**http_info)

    def list_database_data_async_invoker(self, request):
        http_info = self._list_database_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_database_data_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases/{database_id}/data",
            "request_type": request.__class__.__name__,
            "response_type": "ListDatabaseDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'database_id' in local_var_params:
            path_params['database_id'] = local_var_params['database_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'query' in local_var_params:
            query_params.append(('query', local_var_params['query']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

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

    def list_database_resource_async(self, request):
        """查询数据库资源

        查询数据库资源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDatabaseResource
        :type request: :class:`huaweicloudsdkeihealth.v1.ListDatabaseResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListDatabaseResourceResponse`
        """
        http_info = self._list_database_resource_http_info(request)
        return self._call_api(**http_info)

    def list_database_resource_async_invoker(self, request):
        http_info = self._list_database_resource_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_database_resource_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/database-resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListDatabaseResourceResponse"
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

        response_headers = ["X-Resource-Mappings", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_database_resource_flavor_async(self, request):
        """获取数据库资源规格列表

        获取数据库资源规格列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDatabaseResourceFlavor
        :type request: :class:`huaweicloudsdkeihealth.v1.ListDatabaseResourceFlavorRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListDatabaseResourceFlavorResponse`
        """
        http_info = self._list_database_resource_flavor_http_info(request)
        return self._call_api(**http_info)

    def list_database_resource_flavor_async_invoker(self, request):
        http_info = self._list_database_resource_flavor_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_database_resource_flavor_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/database-resources/flavors",
            "request_type": request.__class__.__name__,
            "response_type": "ListDatabaseResourceFlavorResponse"
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

    def list_drug_database_async(self, request):
        """获取数据库列表

        获取数据库列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDrugDatabase
        :type request: :class:`huaweicloudsdkeihealth.v1.ListDrugDatabaseRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListDrugDatabaseResponse`
        """
        http_info = self._list_drug_database_http_info(request)
        return self._call_api(**http_info)

    def list_drug_database_async_invoker(self, request):
        http_info = self._list_drug_database_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_drug_database_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/drug/databases",
            "request_type": request.__class__.__name__,
            "response_type": "ListDrugDatabaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search_key' in local_var_params:
            query_params.append(('search_key', local_var_params['search_key']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
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

    def list_drug_job_async(self, request):
        """获取药物作业列表

        获取药物作业列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDrugJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ListDrugJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListDrugJobResponse`
        """
        http_info = self._list_drug_job_http_info(request)
        return self._call_api(**http_info)

    def list_drug_job_async_invoker(self, request):
        http_info = self._list_drug_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_drug_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListDrugJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'job_name' in local_var_params:
            query_params.append(('job_name', local_var_params['job_name']))
        if 'labels' in local_var_params:
            query_params.append(('labels', local_var_params['labels']))
            collection_formats['labels'] = 'csv'
        if 'status_list' in local_var_params:
            query_params.append(('status_list', local_var_params['status_list']))
            collection_formats['status_list'] = 'csv'
        if 'type_list' in local_var_params:
            query_params.append(('type_list', local_var_params['type_list']))
            collection_formats['type_list'] = 'csv'
        if 'create_start_time' in local_var_params:
            query_params.append(('create_start_time', local_var_params['create_start_time']))
        if 'create_end_time' in local_var_params:
            query_params.append(('create_end_time', local_var_params['create_end_time']))
        if 'finish_start_time' in local_var_params:
            query_params.append(('finish_start_time', local_var_params['finish_start_time']))
        if 'finish_end_time' in local_var_params:
            query_params.append(('finish_end_time', local_var_params['finish_end_time']))
        if 'total_time_range' in local_var_params:
            query_params.append(('total_time_range', local_var_params['total_time_range']))

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

    def list_drug_model_async(self, request):
        """获取模型列表

        获取模型列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDrugModel
        :type request: :class:`huaweicloudsdkeihealth.v1.ListDrugModelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListDrugModelResponse`
        """
        http_info = self._list_drug_model_http_info(request)
        return self._call_api(**http_info)

    def list_drug_model_async_invoker(self, request):
        http_info = self._list_drug_model_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_drug_model_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/drug-models",
            "request_type": request.__class__.__name__,
            "response_type": "ListDrugModelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search_key' in local_var_params:
            query_params.append(('search_key', local_var_params['search_key']))
        if 'creator_list' in local_var_params:
            query_params.append(('creator_list', local_var_params['creator_list']))
            collection_formats['creator_list'] = 'csv'
        if 'type_list' in local_var_params:
            query_params.append(('type_list', local_var_params['type_list']))
            collection_formats['type_list'] = 'csv'
        if 'status_list' in local_var_params:
            query_params.append(('status_list', local_var_params['status_list']))
            collection_formats['status_list'] = 'csv'
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'create_start_time' in local_var_params:
            query_params.append(('create_start_time', local_var_params['create_start_time']))
        if 'create_end_time' in local_var_params:
            query_params.append(('create_end_time', local_var_params['create_end_time']))
        if 'finish_start_time' in local_var_params:
            query_params.append(('finish_start_time', local_var_params['finish_start_time']))
        if 'finish_end_time' in local_var_params:
            query_params.append(('finish_end_time', local_var_params['finish_end_time']))
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

    def list_global_workflow_statistic_async(self, request):
        """统计全局流程、作业信息

        统计全局流程、作业信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGlobalWorkflowStatistic
        :type request: :class:`huaweicloudsdkeihealth.v1.ListGlobalWorkflowStatisticRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListGlobalWorkflowStatisticResponse`
        """
        http_info = self._list_global_workflow_statistic_http_info(request)
        return self._call_api(**http_info)

    def list_global_workflow_statistic_async_invoker(self, request):
        http_info = self._list_global_workflow_statistic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_global_workflow_statistic_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/workflow-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ListGlobalWorkflowStatisticResponse"
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

    def list_iam_group_users_async(self, request):
        """查询IAM用户组的用户列表

        查询IAM用户组的用户列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListIamGroupUsers
        :type request: :class:`huaweicloudsdkeihealth.v1.ListIamGroupUsersRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListIamGroupUsersResponse`
        """
        http_info = self._list_iam_group_users_http_info(request)
        return self._call_api(**http_info)

    def list_iam_group_users_async_invoker(self, request):
        http_info = self._list_iam_group_users_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_iam_group_users_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/iam/groups/{group_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "ListIamGroupUsersResponse"
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

    def list_iam_groups_async(self, request):
        """查询IAM用户组列表

        查询IAM用户组列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListIamGroups
        :type request: :class:`huaweicloudsdkeihealth.v1.ListIamGroupsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListIamGroupsResponse`
        """
        http_info = self._list_iam_groups_http_info(request)
        return self._call_api(**http_info)

    def list_iam_groups_async_invoker(self, request):
        http_info = self._list_iam_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_iam_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/iam/groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListIamGroupsResponse"
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

    def list_iam_users_async(self, request):
        """查询IAM用户列表

        查询IAM用户列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListIamUsers
        :type request: :class:`huaweicloudsdkeihealth.v1.ListIamUsersRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListIamUsersResponse`
        """
        http_info = self._list_iam_users_http_info(request)
        return self._call_api(**http_info)

    def list_iam_users_async_invoker(self, request):
        http_info = self._list_iam_users_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_iam_users_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/iam/users",
            "request_type": request.__class__.__name__,
            "response_type": "ListIamUsersResponse"
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

    def list_image_async(self, request):
        """获取镜像列表

        获取镜像列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListImage
        :type request: :class:`huaweicloudsdkeihealth.v1.ListImageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListImageResponse`
        """
        http_info = self._list_image_http_info(request)
        return self._call_api(**http_info)

    def list_image_async_invoker(self, request):
        http_info = self._list_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_image_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images",
            "request_type": request.__class__.__name__,
            "response_type": "ListImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'show_empty' in local_var_params:
            query_params.append(('show_empty', local_var_params['show_empty']))

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

    def list_image_tag_async(self, request):
        """获取指定镜像的tag列表

        获取指定镜像的tag列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListImageTag
        :type request: :class:`huaweicloudsdkeihealth.v1.ListImageTagRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListImageTagResponse`
        """
        http_info = self._list_image_tag_http_info(request)
        return self._call_api(**http_info)

    def list_image_tag_async_invoker(self, request):
        http_info = self._list_image_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_image_tag_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images/{image_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListImageTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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

    def list_instance_async(self, request):
        """获取实例列表

        获取实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstance
        :type request: :class:`huaweicloudsdkeihealth.v1.ListInstanceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListInstanceResponse`
        """
        http_info = self._list_instance_http_info(request)
        return self._call_api(**http_info)

    def list_instance_async_invoker(self, request):
        http_info = self._list_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instance_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def list_job_async(self, request):
        """获取作业列表

        获取作业列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ListJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListJobResponse`
        """
        http_info = self._list_job_http_info(request)
        return self._call_api(**http_info)

    def list_job_async_invoker(self, request):
        http_info = self._list_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'job_name' in local_var_params:
            query_params.append(('job_name', local_var_params['job_name']))
        if 'labels' in local_var_params:
            query_params.append(('labels', local_var_params['labels']))
            collection_formats['labels'] = 'csv'
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'tool_name' in local_var_params:
            query_params.append(('tool_name', local_var_params['tool_name']))
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'finish_start_time' in local_var_params:
            query_params.append(('finish_start_time', local_var_params['finish_start_time']))
        if 'finish_end_time' in local_var_params:
            query_params.append(('finish_end_time', local_var_params['finish_end_time']))

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

    def list_label_async(self, request):
        """获取标签列表

        获取标签列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLabel
        :type request: :class:`huaweicloudsdkeihealth.v1.ListLabelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListLabelResponse`
        """
        http_info = self._list_label_http_info(request)
        return self._call_api(**http_info)

    def list_label_async_invoker(self, request):
        http_info = self._list_label_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_label_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/labels",
            "request_type": request.__class__.__name__,
            "response_type": "ListLabelResponse"
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

    def list_label_page_async(self, request):
        """获取标签页面列表

        获取标签页面列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLabelPage
        :type request: :class:`huaweicloudsdkeihealth.v1.ListLabelPageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListLabelPageResponse`
        """
        http_info = self._list_label_page_http_info(request)
        return self._call_api(**http_info)

    def list_label_page_async_invoker(self, request):
        http_info = self._list_label_page_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_label_page_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/label-pages",
            "request_type": request.__class__.__name__,
            "response_type": "ListLabelPageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def list_message_async(self, request):
        """获取消息列表

        从消息中心获取当前用户有权限查看的消息列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMessage
        :type request: :class:`huaweicloudsdkeihealth.v1.ListMessageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListMessageResponse`
        """
        http_info = self._list_message_http_info(request)
        return self._call_api(**http_info)

    def list_message_async_invoker(self, request):
        http_info = self._list_message_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_message_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/messages",
            "request_type": request.__class__.__name__,
            "response_type": "ListMessageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'eihealth_project_name' in local_var_params:
            query_params.append(('eihealth_project_name', local_var_params['eihealth_project_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'message_type' in local_var_params:
            query_params.append(('message_type', local_var_params['message_type']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'operator' in local_var_params:
            query_params.append(('operator', local_var_params['operator']))
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

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

    def list_message_statistics_async(self, request):
        """统计消息信息

        统计消息信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMessageStatistics
        :type request: :class:`huaweicloudsdkeihealth.v1.ListMessageStatisticsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListMessageStatisticsResponse`
        """
        http_info = self._list_message_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_message_statistics_async_invoker(self, request):
        http_info = self._list_message_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_message_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/messages/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ListMessageStatisticsResponse"
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

    def list_mfa_async(self, request):
        """获取可用的认证方法

        获取可用的认证方法
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMfa
        :type request: :class:`huaweicloudsdkeihealth.v1.ListMfaRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListMfaResponse`
        """
        http_info = self._list_mfa_http_info(request)
        return self._call_api(**http_info)

    def list_mfa_async_invoker(self, request):
        http_info = self._list_mfa_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_mfa_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/users/{user_id}/mfa/methods",
            "request_type": request.__class__.__name__,
            "response_type": "ListMfaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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

    def list_node_label_async(self, request):
        """获取节点标签集

        获取节点标签集
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNodeLabel
        :type request: :class:`huaweicloudsdkeihealth.v1.ListNodeLabelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListNodeLabelResponse`
        """
        http_info = self._list_node_label_http_info(request)
        return self._call_api(**http_info)

    def list_node_label_async_invoker(self, request):
        http_info = self._list_node_label_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_node_label_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/nodes/{server_id}/labels",
            "request_type": request.__class__.__name__,
            "response_type": "ListNodeLabelResponse"
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

    def list_nodes_async(self, request):
        """获取策略关联计算资源列表

        获取策略关联计算资源列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNodes
        :type request: :class:`huaweicloudsdkeihealth.v1.ListNodesRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListNodesResponse`
        """
        http_info = self._list_nodes_http_info(request)
        return self._call_api(**http_info)

    def list_nodes_async_invoker(self, request):
        http_info = self._list_nodes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_nodes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/autoscaler/scale-out-policies/{id}/computing-resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListNodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def list_notice_async(self, request):
        """获取通知消息列表

        获取通知消息列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNotice
        :type request: :class:`huaweicloudsdkeihealth.v1.ListNoticeRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListNoticeResponse`
        """
        http_info = self._list_notice_http_info(request)
        return self._call_api(**http_info)

    def list_notice_async_invoker(self, request):
        http_info = self._list_notice_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_notice_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/notices",
            "request_type": request.__class__.__name__,
            "response_type": "ListNoticeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'is_read' in local_var_params:
            query_params.append(('is_read', local_var_params['is_read']))
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

    def list_performance_resource_stat_async(self, request):
        """获取性能加速资源上统计信息

        获取性能加速资源上统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPerformanceResourceStat
        :type request: :class:`huaweicloudsdkeihealth.v1.ListPerformanceResourceStatRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListPerformanceResourceStatResponse`
        """
        http_info = self._list_performance_resource_stat_http_info(request)
        return self._call_api(**http_info)

    def list_performance_resource_stat_async_invoker(self, request):
        http_info = self._list_performance_resource_stat_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_performance_resource_stat_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/performance-resources-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ListPerformanceResourceStatResponse"
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

    def list_performance_resources_async(self, request):
        """查询性能加速资源

        查询性能加速资源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPerformanceResources
        :type request: :class:`huaweicloudsdkeihealth.v1.ListPerformanceResourcesRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListPerformanceResourcesResponse`
        """
        http_info = self._list_performance_resources_http_info(request)
        return self._call_api(**http_info)

    def list_performance_resources_async_invoker(self, request):
        http_info = self._list_performance_resources_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_performance_resources_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/performance-resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListPerformanceResourcesResponse"
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

    def list_policy_events_async(self, request):
        """获取策略事件

        获取策略事件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPolicyEvents
        :type request: :class:`huaweicloudsdkeihealth.v1.ListPolicyEventsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListPolicyEventsResponse`
        """
        http_info = self._list_policy_events_http_info(request)
        return self._call_api(**http_info)

    def list_policy_events_async_invoker(self, request):
        http_info = self._list_policy_events_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_policy_events_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/autoscaler/scale-out-policies/{id}/events",
            "request_type": request.__class__.__name__,
            "response_type": "ListPolicyEventsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def list_preset_label_async(self, request):
        """获取预置标签列表

        获取预置标签列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPresetLabel
        :type request: :class:`huaweicloudsdkeihealth.v1.ListPresetLabelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListPresetLabelResponse`
        """
        http_info = self._list_preset_label_http_info(request)
        return self._call_api(**http_info)

    def list_preset_label_async_invoker(self, request):
        http_info = self._list_preset_label_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_preset_label_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/preset-labels",
            "request_type": request.__class__.__name__,
            "response_type": "ListPresetLabelResponse"
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

    def list_project_async(self, request):
        """获取项目列表

        获取项目列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProject
        :type request: :class:`huaweicloudsdkeihealth.v1.ListProjectRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListProjectResponse`
        """
        http_info = self._list_project_http_info(request)
        return self._call_api(**http_info)

    def list_project_async_invoker(self, request):
        http_info = self._list_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_project_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectResponse"
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

    def list_property_async(self, request):
        """获取属性值列表

        获取属性值列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProperty
        :type request: :class:`huaweicloudsdkeihealth.v1.ListPropertyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListPropertyResponse`
        """
        http_info = self._list_property_http_info(request)
        return self._call_api(**http_info)

    def list_property_async_invoker(self, request):
        http_info = self._list_property_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_property_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/assets/properties",
            "request_type": request.__class__.__name__,
            "response_type": "ListPropertyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if '_property' in local_var_params:
            query_params.append(('property', local_var_params['_property']))

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

    def list_quota_async(self, request):
        """获取当前系统配额及资源使用情况

        获取当前系统配额及资源使用情况
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListQuota
        :type request: :class:`huaweicloudsdkeihealth.v1.ListQuotaRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListQuotaResponse`
        """
        http_info = self._list_quota_http_info(request)
        return self._call_api(**http_info)

    def list_quota_async_invoker(self, request):
        http_info = self._list_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ListQuotaResponse"
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

    def list_scale_out_policy_async(self, request):
        """查询扩容策略列表

        查询扩容策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListScaleOutPolicy
        :type request: :class:`huaweicloudsdkeihealth.v1.ListScaleOutPolicyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListScaleOutPolicyResponse`
        """
        http_info = self._list_scale_out_policy_http_info(request)
        return self._call_api(**http_info)

    def list_scale_out_policy_async_invoker(self, request):
        http_info = self._list_scale_out_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_scale_out_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/autoscaler/scale-out-policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListScaleOutPolicyResponse"
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

    def list_scaling_history_async(self, request):
        """获取策略伸缩历史

        获取策略伸缩历史
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListScalingHistory
        :type request: :class:`huaweicloudsdkeihealth.v1.ListScalingHistoryRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListScalingHistoryResponse`
        """
        http_info = self._list_scaling_history_http_info(request)
        return self._call_api(**http_info)

    def list_scaling_history_async_invoker(self, request):
        http_info = self._list_scaling_history_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_scaling_history_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/autoscaler/scale-out-policies/{id}/histories",
            "request_type": request.__class__.__name__,
            "response_type": "ListScalingHistoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def list_star_async(self, request):
        """获取收藏资产列表

        获取收藏资产列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListStar
        :type request: :class:`huaweicloudsdkeihealth.v1.ListStarRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListStarResponse`
        """
        http_info = self._list_star_http_info(request)
        return self._call_api(**http_info)

    def list_star_async_invoker(self, request):
        http_info = self._list_star_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_star_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/assets/stars",
            "request_type": request.__class__.__name__,
            "response_type": "ListStarResponse"
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

    def list_storage_resources_async(self, request):
        """查询存储资源

        查询存储资源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListStorageResources
        :type request: :class:`huaweicloudsdkeihealth.v1.ListStorageResourcesRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListStorageResourcesResponse`
        """
        http_info = self._list_storage_resources_http_info(request)
        return self._call_api(**http_info)

    def list_storage_resources_async_invoker(self, request):
        http_info = self._list_storage_resources_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_storage_resources_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/storage-resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListStorageResourcesResponse"
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

    def list_study_async(self, request):
        """列举study

        列举study
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListStudy
        :type request: :class:`huaweicloudsdkeihealth.v1.ListStudyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListStudyResponse`
        """
        http_info = self._list_study_http_info(request)
        return self._call_api(**http_info)

    def list_study_async_invoker(self, request):
        http_info = self._list_study_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_study_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/studies",
            "request_type": request.__class__.__name__,
            "response_type": "ListStudyResponse"
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

    def list_study_job_async(self, request):
        """列举study所有作业

        列举study所有作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListStudyJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ListStudyJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListStudyJobResponse`
        """
        http_info = self._list_study_job_http_info(request)
        return self._call_api(**http_info)

    def list_study_job_async_invoker(self, request):
        http_info = self._list_study_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_study_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/studies/{study_id}/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListStudyJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'study_id' in local_var_params:
            path_params['study_id'] = local_var_params['study_id']

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

    def list_template_async(self, request):
        """查询模板列表

        查询模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTemplate
        :type request: :class:`huaweicloudsdkeihealth.v1.ListTemplateRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListTemplateResponse`
        """
        http_info = self._list_template_http_info(request)
        return self._call_api(**http_info)

    def list_template_async_invoker(self, request):
        http_info = self._list_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def list_user_async(self, request):
        """获取用户列表

        获取用户列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUser
        :type request: :class:`huaweicloudsdkeihealth.v1.ListUserRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListUserResponse`
        """
        http_info = self._list_user_http_info(request)
        return self._call_api(**http_info)

    def list_user_async_invoker(self, request):
        http_info = self._list_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_user_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "ListUserResponse"
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

    def list_vendor_async(self, request):
        """获取供应商列表

        获取供应商列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVendor
        :type request: :class:`huaweicloudsdkeihealth.v1.ListVendorRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListVendorResponse`
        """
        http_info = self._list_vendor_http_info(request)
        return self._call_api(**http_info)

    def list_vendor_async_invoker(self, request):
        http_info = self._list_vendor_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_vendor_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/vendors",
            "request_type": request.__class__.__name__,
            "response_type": "ListVendorResponse"
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

    def list_workflow_async(self, request):
        """获取流程列表

        获取流程列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.ListWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListWorkflowResponse`
        """
        http_info = self._list_workflow_http_info(request)
        return self._call_api(**http_info)

    def list_workflow_async_invoker(self, request):
        http_info = self._list_workflow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_workflow_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/workflows",
            "request_type": request.__class__.__name__,
            "response_type": "ListWorkflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))

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

    def list_workflow_statistic_async(self, request):
        """统计应用、流程、作业数目

        统计应用、流程、作业数目
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWorkflowStatistic
        :type request: :class:`huaweicloudsdkeihealth.v1.ListWorkflowStatisticRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListWorkflowStatisticResponse`
        """
        http_info = self._list_workflow_statistic_http_info(request)
        return self._call_api(**http_info)

    def list_workflow_statistic_async_invoker(self, request):
        http_info = self._list_workflow_statistic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_workflow_statistic_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ListWorkflowStatisticResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def publish_app_async(self, request):
        """发布应用

        发布应用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PublishApp
        :type request: :class:`huaweicloudsdkeihealth.v1.PublishAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.PublishAppResponse`
        """
        http_info = self._publish_app_http_info(request)
        return self._call_api(**http_info)

    def publish_app_async_invoker(self, request):
        http_info = self._publish_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _publish_app_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/apps/{app_id}/publish",
            "request_type": request.__class__.__name__,
            "response_type": "PublishAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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

    def publish_data_async(self, request):
        """发布数据资产

        发布数据资产
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PublishData
        :type request: :class:`huaweicloudsdkeihealth.v1.PublishDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.PublishDataResponse`
        """
        http_info = self._publish_data_http_info(request)
        return self._call_api(**http_info)

    def publish_data_async_invoker(self, request):
        http_info = self._publish_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _publish_data_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/publish",
            "request_type": request.__class__.__name__,
            "response_type": "PublishDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def publish_image_async(self, request):
        """发布镜像

        发布镜像
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PublishImage
        :type request: :class:`huaweicloudsdkeihealth.v1.PublishImageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.PublishImageResponse`
        """
        http_info = self._publish_image_http_info(request)
        return self._call_api(**http_info)

    def publish_image_async_invoker(self, request):
        http_info = self._publish_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _publish_image_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images/publish",
            "request_type": request.__class__.__name__,
            "response_type": "PublishImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def publish_workflow_async(self, request):
        """发布流程

        发布流程
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PublishWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.PublishWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.PublishWorkflowResponse`
        """
        http_info = self._publish_workflow_http_info(request)
        return self._call_api(**http_info)

    def publish_workflow_async_invoker(self, request):
        http_info = self._publish_workflow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _publish_workflow_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/workflows/{workflow_id}/publish",
            "request_type": request.__class__.__name__,
            "response_type": "PublishWorkflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

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

    def quote_data_async(self, request):
        """引用项目数据

        引用项目数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for QuoteData
        :type request: :class:`huaweicloudsdkeihealth.v1.QuoteDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.QuoteDataResponse`
        """
        http_info = self._quote_data_http_info(request)
        return self._call_api(**http_info)

    def quote_data_async_invoker(self, request):
        http_info = self._quote_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _quote_data_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/quote",
            "request_type": request.__class__.__name__,
            "response_type": "QuoteDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def quote_instance_async(self, request):
        """引用数据库实例

        引用数据库实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for QuoteInstance
        :type request: :class:`huaweicloudsdkeihealth.v1.QuoteInstanceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.QuoteInstanceResponse`
        """
        http_info = self._quote_instance_http_info(request)
        return self._call_api(**http_info)

    def quote_instance_async_invoker(self, request):
        http_info = self._quote_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _quote_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases/batch-quote",
            "request_type": request.__class__.__name__,
            "response_type": "QuoteInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def reboot_node_async(self, request):
        """重启计算资源

        重启计算资源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RebootNode
        :type request: :class:`huaweicloudsdkeihealth.v1.RebootNodeRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.RebootNodeResponse`
        """
        http_info = self._reboot_node_http_info(request)
        return self._call_api(**http_info)

    def reboot_node_async_invoker(self, request):
        http_info = self._reboot_node_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reboot_node_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/system/computing-resources/{id}/reboot",
            "request_type": request.__class__.__name__,
            "response_type": "RebootNodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'force' in local_var_params:
            query_params.append(('force', local_var_params['force']))

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

    def restore_backup_async(self, request):
        """恢复归档

        将指定的归档数据拷贝到目标项目的某个目录下
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestoreBackup
        :type request: :class:`huaweicloudsdkeihealth.v1.RestoreBackupRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.RestoreBackupResponse`
        """
        http_info = self._restore_backup_http_info(request)
        return self._call_api(**http_info)

    def restore_backup_async_invoker(self, request):
        http_info = self._restore_backup_http_info(request)
        return AsyncInvoker(self, http_info)

    def _restore_backup_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/backups/{backup_id}/restore",
            "request_type": request.__class__.__name__,
            "response_type": "RestoreBackupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def retry_data_job_async(self, request):
        """重试数据作业

        重试数据作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RetryDataJob
        :type request: :class:`huaweicloudsdkeihealth.v1.RetryDataJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.RetryDataJobResponse`
        """
        http_info = self._retry_data_job_http_info(request)
        return self._call_api(**http_info)

    def retry_data_job_async_invoker(self, request):
        http_info = self._retry_data_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _retry_data_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/data-jobs/{data_job_id}/retry",
            "request_type": request.__class__.__name__,
            "response_type": "RetryDataJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'data_job_id' in local_var_params:
            path_params['data_job_id'] = local_var_params['data_job_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def retry_job_async(self, request):
        """重试作业

        重试作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RetryJob
        :type request: :class:`huaweicloudsdkeihealth.v1.RetryJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.RetryJobResponse`
        """
        http_info = self._retry_job_http_info(request)
        return self._call_api(**http_info)

    def retry_job_async_invoker(self, request):
        http_info = self._retry_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _retry_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}/retry",
            "request_type": request.__class__.__name__,
            "response_type": "RetryJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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

    def show3d_structure_content_async(self, request):
        """获取生成study作业3D结构的内容

        获取生成study作业3D结构的内容
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for Show3dStructureContent
        :type request: :class:`huaweicloudsdkeihealth.v1.Show3dStructureContentRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.Show3dStructureContentResponse`
        """
        http_info = self._show3d_structure_content_http_info(request)
        return self._call_api(**http_info)

    def show3d_structure_content_async_invoker(self, request):
        http_info = self._show3d_structure_content_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show3d_structure_content_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/studies/{study_id}/jobs/{job_id}/3d-structure",
            "request_type": request.__class__.__name__,
            "response_type": "Show3dStructureContentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'study_id' in local_var_params:
            path_params['study_id'] = local_var_params['study_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'ligand' in local_var_params:
            query_params.append(('ligand', local_var_params['ligand']))
        if 'receptor' in local_var_params:
            query_params.append(('receptor', local_var_params['receptor']))

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

    def show_admet_job_async(self, request):
        """查询分子属性预测作业详情

        查询分子属性预测作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAdmetJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowAdmetJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowAdmetJobResponse`
        """
        http_info = self._show_admet_job_http_info(request)
        return self._call_api(**http_info)

    def show_admet_job_async_invoker(self, request):
        http_info = self._show_admet_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_admet_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/admet/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAdmetJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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

    def show_app_async(self, request):
        """获取应用详情

        获取应用详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowApp
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowAppResponse`
        """
        http_info = self._show_app_http_info(request)
        return self._call_api(**http_info)

    def show_app_async_invoker(self, request):
        http_info = self._show_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_app_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def show_asset_async(self, request):
        """查询资产详情

        查询资产详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAsset
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowAssetRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowAssetResponse`
        """
        http_info = self._show_asset_http_info(request)
        return self._call_api(**http_info)

    def show_asset_async_invoker(self, request):
        http_info = self._show_asset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_asset_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/assets/{asset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAssetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

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

    def show_asset_version_async(self, request):
        """查询资产版本详情

        查询资产版本详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAssetVersion
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowAssetVersionRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowAssetVersionResponse`
        """
        http_info = self._show_asset_version_http_info(request)
        return self._call_api(**http_info)

    def show_asset_version_async_invoker(self, request):
        http_info = self._show_asset_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_asset_version_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/assets/{asset_id}/versions/{version}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAssetVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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

    def show_auto_job_async(self, request):
        """查询自动作业模板

        查询自动作业模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAutoJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowAutoJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowAutoJobResponse`
        """
        http_info = self._show_auto_job_http_info(request)
        return self._call_api(**http_info)

    def show_auto_job_async_invoker(self, request):
        http_info = self._show_auto_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_auto_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/auto-jobs/{auto_job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutoJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'auto_job_id' in local_var_params:
            path_params['auto_job_id'] = local_var_params['auto_job_id']

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

    def show_backup_path_async(self, request):
        """获取指定归档的全数据清单

        根据归档ID获取该归档的全数据清单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBackupPath
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowBackupPathRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowBackupPathResponse`
        """
        http_info = self._show_backup_path_http_info(request)
        return self._call_api(**http_info)

    def show_backup_path_async_invoker(self, request):
        http_info = self._show_backup_path_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_backup_path_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/backups/{backup_id}/paths",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBackupPathResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def show_bms_devices_async(self, request):
        """查询bms计算资源显卡id列表

        查询bms计算资源显卡id列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBmsDevices
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowBmsDevicesRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowBmsDevicesResponse`
        """
        http_info = self._show_bms_devices_http_info(request)
        return self._call_api(**http_info)

    def show_bms_devices_async_invoker(self, request):
        http_info = self._show_bms_devices_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_bms_devices_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/computing-resources/{id}/devices",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBmsDevicesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def show_bucket_storage_async(self, request):
        """获取桶存量信息

        获取桶存量信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBucketStorage
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowBucketStorageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowBucketStorageResponse`
        """
        http_info = self._show_bucket_storage_http_info(request)
        return self._call_api(**http_info)

    def show_bucket_storage_async_invoker(self, request):
        http_info = self._show_bucket_storage_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_bucket_storage_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/bucket-storage",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBucketStorageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def show_data_async(self, request):
        """获取数据详情

        获取指定数据对象的详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowData
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowDataResponse`
        """
        http_info = self._show_data_http_info(request)
        return self._call_api(**http_info)

    def show_data_async_invoker(self, request):
        http_info = self._show_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_data_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/{path}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'path' in local_var_params:
            path_params['path'] = local_var_params['path']

        query_params = []

        header_params = {}
        if 'x_need_content' in local_var_params:
            header_params['X-Need-Content'] = local_var_params['x_need_content']

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

    def show_data_job_async(self, request):
        """获取数据作业详细信息

        获取数据作业详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDataJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowDataJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowDataJobResponse`
        """
        http_info = self._show_data_job_http_info(request)
        return self._call_api(**http_info)

    def show_data_job_async_invoker(self, request):
        http_info = self._show_data_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_data_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/data-jobs/{data_job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDataJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'data_job_id' in local_var_params:
            path_params['data_job_id'] = local_var_params['data_job_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def show_data_policy_async(self, request):
        """查询项目级数据权限控制策略

        查询项目级数据权限控制策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDataPolicy
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowDataPolicyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowDataPolicyResponse`
        """
        http_info = self._show_data_policy_http_info(request)
        return self._call_api(**http_info)

    def show_data_policy_async_invoker(self, request):
        http_info = self._show_data_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_data_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDataPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def show_docker_login_async(self, request):
        """获取docker login指令

        获取docker login指令
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDockerLogin
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowDockerLoginRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowDockerLoginResponse`
        """
        http_info = self._show_docker_login_http_info(request)
        return self._call_api(**http_info)

    def show_docker_login_async_invoker(self, request):
        http_info = self._show_docker_login_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_docker_login_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images/docker-login-cmd",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDockerLoginResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def show_docking_job_async(self, request):
        """查询分子对接作业详情

        查询分子对接作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDockingJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowDockingJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowDockingJobResponse`
        """
        http_info = self._show_docking_job_http_info(request)
        return self._call_api(**http_info)

    def show_docking_job_async_invoker(self, request):
        http_info = self._show_docking_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_docking_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/docking/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDockingJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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

    def show_env_async(self, request):
        """查询系统配置列表

        获取系统配置列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEnv
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowEnvRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowEnvResponse`
        """
        http_info = self._show_env_http_info(request)
        return self._call_api(**http_info)

    def show_env_async_invoker(self, request):
        http_info = self._show_env_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_env_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/configs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEnvResponse"
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

    def show_evs_quota_async(self, request):
        """获取EVS配额及使用情况

        获取EVS配额及使用情况
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEvsQuota
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowEvsQuotaRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowEvsQuotaResponse`
        """
        http_info = self._show_evs_quota_http_info(request)
        return self._call_api(**http_info)

    def show_evs_quota_async_invoker(self, request):
        http_info = self._show_evs_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_evs_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/computing-resources/evs-quota",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEvsQuotaResponse"
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

    def show_extremum_info_async(self, request):
        """获取study作业的最值信息

        获取study作业的最值信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowExtremumInfo
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowExtremumInfoRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowExtremumInfoResponse`
        """
        http_info = self._show_extremum_info_http_info(request)
        return self._call_api(**http_info)

    def show_extremum_info_async_invoker(self, request):
        http_info = self._show_extremum_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_extremum_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/studies/{study_id}/jobs/{job_id}/extremum",
            "request_type": request.__class__.__name__,
            "response_type": "ShowExtremumInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'study_id' in local_var_params:
            path_params['study_id'] = local_var_params['study_id']
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

    def show_fep_job_async(self, request):
        """查询自由能微扰作业详情

        查询自由能微扰作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowFepJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowFepJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowFepJobResponse`
        """
        http_info = self._show_fep_job_http_info(request)
        return self._call_api(**http_info)

    def show_fep_job_async_invoker(self, request):
        http_info = self._show_fep_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_fep_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/fep/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFepJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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

    def show_instance_async(self, request):
        """查询实例详情

        查询实例详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstance
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowInstanceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowInstanceResponse`
        """
        http_info = self._show_instance_http_info(request)
        return self._call_api(**http_info)

    def show_instance_async_invoker(self, request):
        http_info = self._show_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_instance_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases/{database_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'database_id' in local_var_params:
            path_params['database_id'] = local_var_params['database_id']

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

    def show_job_async(self, request):
        """获取作业详情

        获取作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowJobResponse`
        """
        http_info = self._show_job_http_info(request)
        return self._call_api(**http_info)

    def show_job_async_invoker(self, request):
        http_info = self._show_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_addition_info' in local_var_params:
            header_params['X-Addition-Info'] = local_var_params['x_addition_info']

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

    def show_job_config_async(self, request):
        """获取作业配置

        获取作业配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobConfig
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowJobConfigRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowJobConfigResponse`
        """
        http_info = self._show_job_config_http_info(request)
        return self._call_api(**http_info)

    def show_job_config_async_invoker(self, request):
        http_info = self._show_job_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/job-config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobConfigResponse"
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

    def show_job_event_async(self, request):
        """获取作业事件

        获取作业事件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobEvent
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowJobEventRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowJobEventResponse`
        """
        http_info = self._show_job_event_http_info(request)
        return self._call_api(**http_info)

    def show_job_event_async_invoker(self, request):
        http_info = self._show_job_event_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_event_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}/events",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobEventResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

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

    def show_job_log_async(self, request):
        """获取作业日志

        获取作业日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobLog
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowJobLogRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowJobLogResponse`
        """
        http_info = self._show_job_log_http_info(request)
        return self._call_api(**http_info)

    def show_job_log_async_invoker(self, request):
        http_info = self._show_job_log_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_log_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}/logs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'task_name' in local_var_params:
            query_params.append(('task_name', local_var_params['task_name']))
        if 'task_index' in local_var_params:
            query_params.append(('task_index', local_var_params['task_index']))

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

    def show_left_quota_async(self, request):
        """获取节点剩余配额

        获取节点剩余配额
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowLeftQuota
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowLeftQuotaRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowLeftQuotaResponse`
        """
        http_info = self._show_left_quota_http_info(request)
        return self._call_api(**http_info)

    def show_left_quota_async_invoker(self, request):
        http_info = self._show_left_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_left_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/computing-resources/quota",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLeftQuotaResponse"
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

    def show_message_clear_rule_async(self, request):
        """获取消息清理规则

        获取消息清理规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMessageClearRule
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowMessageClearRuleRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowMessageClearRuleResponse`
        """
        http_info = self._show_message_clear_rule_http_info(request)
        return self._call_api(**http_info)

    def show_message_clear_rule_async_invoker(self, request):
        http_info = self._show_message_clear_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_message_clear_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/messages/rules",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMessageClearRuleResponse"
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

    def show_message_email_config_async(self, request):
        """获取消息邮件配置

        获取消息邮件配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMessageEmailConfig
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowMessageEmailConfigRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowMessageEmailConfigResponse`
        """
        http_info = self._show_message_email_config_http_info(request)
        return self._call_api(**http_info)

    def show_message_email_config_async_invoker(self, request):
        http_info = self._show_message_email_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_message_email_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/messages/email-server-config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMessageEmailConfigResponse"
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

    def show_message_receive_config_async(self, request):
        """获取用户邮件配置

        获取用户邮件配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMessageReceiveConfig
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowMessageReceiveConfigRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowMessageReceiveConfigResponse`
        """
        http_info = self._show_message_receive_config_http_info(request)
        return self._call_api(**http_info)

    def show_message_receive_config_async_invoker(self, request):
        http_info = self._show_message_receive_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_message_receive_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/messages/email-client-config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMessageReceiveConfigResponse"
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

    def show_mol_batch_download_task_async(self, request):
        """查询分子或分子复合物批量下载任务详情

        查询分子或分子复合物批量下载任务详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMolBatchDownloadTask
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowMolBatchDownloadTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowMolBatchDownloadTaskResponse`
        """
        http_info = self._show_mol_batch_download_task_http_info(request)
        return self._call_api(**http_info)

    def show_mol_batch_download_task_async_invoker(self, request):
        http_info = self._show_mol_batch_download_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_mol_batch_download_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/toolkit/batch-download/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMolBatchDownloadTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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

    def show_optm_job_async(self, request):
        """查询分子优化作业详情

        查询分子优化作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOptmJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowOptmJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowOptmJobResponse`
        """
        http_info = self._show_optm_job_http_info(request)
        return self._call_api(**http_info)

    def show_optm_job_async_invoker(self, request):
        http_info = self._show_optm_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_optm_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/optimization/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOptmJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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

    def show_pocket_detection_job_async(self, request):
        """查询靶点口袋发现作业详情

        查询靶点口袋发现作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPocketDetectionJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowPocketDetectionJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowPocketDetectionJobResponse`
        """
        http_info = self._show_pocket_detection_job_http_info(request)
        return self._call_api(**http_info)

    def show_pocket_detection_job_async_invoker(self, request):
        http_info = self._show_pocket_detection_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_pocket_detection_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/pocket-detection/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPocketDetectionJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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

    def show_pocket_mol_design_job_async(self, request):
        """查询靶点口袋分子设计作业详情

        查询靶点口袋分子设计作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPocketMolDesignJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowPocketMolDesignJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowPocketMolDesignJobResponse`
        """
        http_info = self._show_pocket_mol_design_job_http_info(request)
        return self._call_api(**http_info)

    def show_pocket_mol_design_job_async_invoker(self, request):
        http_info = self._show_pocket_mol_design_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_pocket_mol_design_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/pocket-mol-design/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPocketMolDesignJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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

    def show_project_async(self, request):
        """获取项目详情

        获取项目详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProject
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowProjectRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowProjectResponse`
        """
        http_info = self._show_project_http_info(request)
        return self._call_api(**http_info)

    def show_project_async_invoker(self, request):
        http_info = self._show_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_project_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []

        header_params = {}
        if 'x_bucket_name' in local_var_params:
            header_params['X-Bucket-Name'] = local_var_params['x_bucket_name']
        if 'x_namespace_name' in local_var_params:
            header_params['X-Namespace-Name'] = local_var_params['x_namespace_name']

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

    def show_project_trace_async(self, request):
        """获取项目审计日志

        获取项目审计日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProjectTrace
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowProjectTraceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowProjectTraceResponse`
        """
        http_info = self._show_project_trace_http_info(request)
        return self._call_api(**http_info)

    def show_project_trace_async_invoker(self, request):
        http_info = self._show_project_trace_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_project_trace_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/project-traces",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectTraceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))
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

    def show_project_trace_data_async(self, request):
        """获取指定审计日志

        获取指定审计日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProjectTraceData
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowProjectTraceDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowProjectTraceDataResponse`
        """
        http_info = self._show_project_trace_data_http_info(request)
        return self._call_api(**http_info)

    def show_project_trace_data_async_invoker(self, request):
        http_info = self._show_project_trace_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_project_trace_data_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/project-traces/{path}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectTraceDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'path' in local_var_params:
            path_params['path'] = local_var_params['path']

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

    def show_project_tracker_async(self, request):
        """获取项目审计日志追踪器

        获取项目审计日志追踪器
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProjectTracker
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowProjectTrackerRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowProjectTrackerResponse`
        """
        http_info = self._show_project_tracker_http_info(request)
        return self._call_api(**http_info)

    def show_project_tracker_async_invoker(self, request):
        http_info = self._show_project_tracker_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_project_tracker_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/project-tracker",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectTrackerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def show_resource_metric_data_async(self, request):
        """获取资源监控数据

        获取资源监控数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourceMetricData
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowResourceMetricDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowResourceMetricDataResponse`
        """
        http_info = self._show_resource_metric_data_http_info(request)
        return self._call_api(**http_info)

    def show_resource_metric_data_async_invoker(self, request):
        http_info = self._show_resource_metric_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_resource_metric_data_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/metric-data",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourceMetricDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'from_time' in local_var_params:
            query_params.append(('from_time', local_var_params['from_time']))
        if 'to_time' in local_var_params:
            query_params.append(('to_time', local_var_params['to_time']))
        if 'period' in local_var_params:
            query_params.append(('period', local_var_params['period']))
        if 'method' in local_var_params:
            query_params.append(('method', local_var_params['method']))
        if 'metric_name' in local_var_params:
            query_params.append(('metric_name', local_var_params['metric_name']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'device_id' in local_var_params:
            query_params.append(('device_id', local_var_params['device_id']))

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

    def show_scale_in_policy_async(self, request):
        """查询缩容策略

        查询缩容策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowScaleInPolicy
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowScaleInPolicyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowScaleInPolicyResponse`
        """
        http_info = self._show_scale_in_policy_http_info(request)
        return self._call_api(**http_info)

    def show_scale_in_policy_async_invoker(self, request):
        http_info = self._show_scale_in_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_scale_in_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/autoscaler/scale-in-policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowScaleInPolicyResponse"
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

    def show_scale_out_policy_async(self, request):
        """获取扩容策略详情

        获取扩容策略详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowScaleOutPolicy
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowScaleOutPolicyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowScaleOutPolicyResponse`
        """
        http_info = self._show_scale_out_policy_http_info(request)
        return self._call_api(**http_info)

    def show_scale_out_policy_async_invoker(self, request):
        http_info = self._show_scale_out_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_scale_out_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/autoscaler/scale-out-policies/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowScaleOutPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def show_schedule_async(self, request):
        """查询计算资源调度信息

        查询计算资源调度信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSchedule
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowScheduleRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowScheduleResponse`
        """
        http_info = self._show_schedule_http_info(request)
        return self._call_api(**http_info)

    def show_schedule_async_invoker(self, request):
        http_info = self._show_schedule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_schedule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/computing-resources/{id}/schedule",
            "request_type": request.__class__.__name__,
            "response_type": "ShowScheduleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def show_search_job_async(self, request):
        """查询分子搜索作业详情

        查询分子搜索作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSearchJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowSearchJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowSearchJobResponse`
        """
        http_info = self._show_search_job_http_info(request)
        return self._call_api(**http_info)

    def show_search_job_async_invoker(self, request):
        http_info = self._show_search_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_search_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/search/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSearchJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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

    def show_synthesis_job_async(self, request):
        """查询分子合成路径规划作业详情

        查询分子合成路径规划作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSynthesisJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowSynthesisJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowSynthesisJobResponse`
        """
        http_info = self._show_synthesis_job_http_info(request)
        return self._call_api(**http_info)

    def show_synthesis_job_async_invoker(self, request):
        http_info = self._show_synthesis_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_synthesis_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/synthesis/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSynthesisJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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

    def show_task_events_async(self, request):
        """获取子任务启动事件

        获取子任务启动事件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTaskEvents
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowTaskEventsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowTaskEventsResponse`
        """
        http_info = self._show_task_events_http_info(request)
        return self._call_api(**http_info)

    def show_task_events_async_invoker(self, request):
        http_info = self._show_task_events_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_task_events_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}/tasks/{task_name}/events",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTaskEventsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'task_name' in local_var_params:
            path_params['task_name'] = local_var_params['task_name']

        query_params = []
        if 'task_index' in local_var_params:
            query_params.append(('task_index', local_var_params['task_index']))

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

    def show_task_instance_events_async(self, request):
        """获取子任务中实例的事件

        获取子任务中实例的事件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTaskInstanceEvents
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstanceEventsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstanceEventsResponse`
        """
        http_info = self._show_task_instance_events_http_info(request)
        return self._call_api(**http_info)

    def show_task_instance_events_async_invoker(self, request):
        http_info = self._show_task_instance_events_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_task_instance_events_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}/tasks/{task_name}/instances/{instance_name}/events",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTaskInstanceEventsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'task_name' in local_var_params:
            path_params['task_name'] = local_var_params['task_name']
        if 'instance_name' in local_var_params:
            path_params['instance_name'] = local_var_params['instance_name']

        query_params = []
        if 'task_index' in local_var_params:
            query_params.append(('task_index', local_var_params['task_index']))

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

    def show_task_instance_metric_data_async(self, request):
        """获取子任务中实例的资源监控数据

        获取子任务中实例的资源监控数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTaskInstanceMetricData
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstanceMetricDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstanceMetricDataResponse`
        """
        http_info = self._show_task_instance_metric_data_http_info(request)
        return self._call_api(**http_info)

    def show_task_instance_metric_data_async_invoker(self, request):
        http_info = self._show_task_instance_metric_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_task_instance_metric_data_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}/tasks/{task_name}/instances/{instance_name}/metric-data",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTaskInstanceMetricDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'task_name' in local_var_params:
            path_params['task_name'] = local_var_params['task_name']
        if 'instance_name' in local_var_params:
            path_params['instance_name'] = local_var_params['instance_name']

        query_params = []
        if 'task_index' in local_var_params:
            query_params.append(('task_index', local_var_params['task_index']))
        if 'from_time' in local_var_params:
            query_params.append(('from_time', local_var_params['from_time']))
        if 'to_time' in local_var_params:
            query_params.append(('to_time', local_var_params['to_time']))
        if 'method' in local_var_params:
            query_params.append(('method', local_var_params['method']))
        if 'metric_name' in local_var_params:
            query_params.append(('metric_name', local_var_params['metric_name']))

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

    def show_task_instance_pod_async(self, request):
        """获取子任务中实例的pod信息

        获取子任务中实例的pod信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTaskInstancePod
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstancePodRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstancePodResponse`
        """
        http_info = self._show_task_instance_pod_http_info(request)
        return self._call_api(**http_info)

    def show_task_instance_pod_async_invoker(self, request):
        http_info = self._show_task_instance_pod_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_task_instance_pod_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}/tasks/{task_name}/instances/{instance_name}/pod",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTaskInstancePodResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'task_name' in local_var_params:
            path_params['task_name'] = local_var_params['task_name']
        if 'instance_name' in local_var_params:
            path_params['instance_name'] = local_var_params['instance_name']

        query_params = []
        if 'task_index' in local_var_params:
            query_params.append(('task_index', local_var_params['task_index']))

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

    def show_task_instances_async(self, request):
        """获取子任务实例信息

        获取子任务实例信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTaskInstances
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstancesRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstancesResponse`
        """
        http_info = self._show_task_instances_http_info(request)
        return self._call_api(**http_info)

    def show_task_instances_async_invoker(self, request):
        http_info = self._show_task_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_task_instances_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}/tasks/{task_name}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTaskInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'task_name' in local_var_params:
            path_params['task_name'] = local_var_params['task_name']

        query_params = []
        if 'task_index' in local_var_params:
            query_params.append(('task_index', local_var_params['task_index']))

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

    def show_template_async(self, request):
        """查询模板详情

        查询模板详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTemplate
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowTemplateRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowTemplateResponse`
        """
        http_info = self._show_template_http_info(request)
        return self._call_api(**http_info)

    def show_template_async_invoker(self, request):
        http_info = self._show_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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

    def show_user_async(self, request):
        """获取指定用户详情

        获取指定用户详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowUser
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowUserRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowUserResponse`
        """
        http_info = self._show_user_http_info(request)
        return self._call_api(**http_info)

    def show_user_async_invoker(self, request):
        http_info = self._show_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_user_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/users/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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

    def show_user_setting_async(self, request):
        """查询用户设置

        查询用户设置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowUserSetting
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowUserSettingRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowUserSettingResponse`
        """
        http_info = self._show_user_setting_http_info(request)
        return self._call_api(**http_info)

    def show_user_setting_async_invoker(self, request):
        http_info = self._show_user_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_user_setting_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/users/{user_id}/settings",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUserSettingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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

    def show_vendor_async(self, request):
        """获取供应商配置

        获取供应商配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVendor
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowVendorRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowVendorResponse`
        """
        http_info = self._show_vendor_http_info(request)
        return self._call_api(**http_info)

    def show_vendor_async_invoker(self, request):
        http_info = self._show_vendor_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_vendor_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/vendor-config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVendorResponse"
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

    def show_workflow_async(self, request):
        """获取流程详情

        获取流程详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowWorkflowResponse`
        """
        http_info = self._show_workflow_http_info(request)
        return self._call_api(**http_info)

    def show_workflow_async_invoker(self, request):
        http_info = self._show_workflow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_workflow_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/workflows/{workflow_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWorkflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

        query_params = []

        header_params = {}
        if 'show_param_detail' in local_var_params:
            header_params['Show-Param-Detail'] = local_var_params['show_param_detail']

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

    def start_auto_job_async(self, request):
        """启动自动作业

        启动自动作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartAutoJob
        :type request: :class:`huaweicloudsdkeihealth.v1.StartAutoJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.StartAutoJobResponse`
        """
        http_info = self._start_auto_job_http_info(request)
        return self._call_api(**http_info)

    def start_auto_job_async_invoker(self, request):
        http_info = self._start_auto_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_auto_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/auto-jobs/{auto_job_id}/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartAutoJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'auto_job_id' in local_var_params:
            path_params['auto_job_id'] = local_var_params['auto_job_id']

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

    def start_node_async(self, request):
        """启动计算资源

        启动计算资源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartNode
        :type request: :class:`huaweicloudsdkeihealth.v1.StartNodeRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.StartNodeResponse`
        """
        http_info = self._start_node_http_info(request)
        return self._call_api(**http_info)

    def start_node_async_invoker(self, request):
        http_info = self._start_node_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_node_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/system/computing-resources/{id}/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartNodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def start_scale_out_policy_async(self, request):
        """启动自动扩容策略

        启动自动扩容策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartScaleOutPolicy
        :type request: :class:`huaweicloudsdkeihealth.v1.StartScaleOutPolicyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.StartScaleOutPolicyResponse`
        """
        http_info = self._start_scale_out_policy_http_info(request)
        return self._call_api(**http_info)

    def start_scale_out_policy_async_invoker(self, request):
        http_info = self._start_scale_out_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_scale_out_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/system/autoscaler/scale-out-policies/{id}/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartScaleOutPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def stop_auto_job_async(self, request):
        """停止自动作业

        停止自动作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopAutoJob
        :type request: :class:`huaweicloudsdkeihealth.v1.StopAutoJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.StopAutoJobResponse`
        """
        http_info = self._stop_auto_job_http_info(request)
        return self._call_api(**http_info)

    def stop_auto_job_async_invoker(self, request):
        http_info = self._stop_auto_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_auto_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/auto-jobs/{auto_job_id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopAutoJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'auto_job_id' in local_var_params:
            path_params['auto_job_id'] = local_var_params['auto_job_id']

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

    def stop_node_async(self, request):
        """关闭计算资源

        关闭计算资源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopNode
        :type request: :class:`huaweicloudsdkeihealth.v1.StopNodeRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.StopNodeResponse`
        """
        http_info = self._stop_node_http_info(request)
        return self._call_api(**http_info)

    def stop_node_async_invoker(self, request):
        http_info = self._stop_node_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_node_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/system/computing-resources/{id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopNodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'force' in local_var_params:
            query_params.append(('force', local_var_params['force']))

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

    def stop_scale_out_policy_async(self, request):
        """停用自动扩容策略

        停用自动扩容策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopScaleOutPolicy
        :type request: :class:`huaweicloudsdkeihealth.v1.StopScaleOutPolicyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.StopScaleOutPolicyResponse`
        """
        http_info = self._stop_scale_out_policy_http_info(request)
        return self._call_api(**http_info)

    def stop_scale_out_policy_async_invoker(self, request):
        http_info = self._stop_scale_out_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_scale_out_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/system/autoscaler/scale-out-policies/{id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopScaleOutPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def subscribe_app_async(self, request):
        """订阅应用

        订阅应用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SubscribeApp
        :type request: :class:`huaweicloudsdkeihealth.v1.SubscribeAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.SubscribeAppResponse`
        """
        http_info = self._subscribe_app_http_info(request)
        return self._call_api(**http_info)

    def subscribe_app_async_invoker(self, request):
        http_info = self._subscribe_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _subscribe_app_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/apps/subscribe",
            "request_type": request.__class__.__name__,
            "response_type": "SubscribeAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def subscribe_data_async(self, request):
        """订阅资产市场数据

        订阅资产市场数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SubscribeData
        :type request: :class:`huaweicloudsdkeihealth.v1.SubscribeDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.SubscribeDataResponse`
        """
        http_info = self._subscribe_data_http_info(request)
        return self._call_api(**http_info)

    def subscribe_data_async_invoker(self, request):
        http_info = self._subscribe_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _subscribe_data_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/subscribe",
            "request_type": request.__class__.__name__,
            "response_type": "SubscribeDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def subscribe_image_async(self, request):
        """订阅镜像

        订阅镜像
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SubscribeImage
        :type request: :class:`huaweicloudsdkeihealth.v1.SubscribeImageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.SubscribeImageResponse`
        """
        http_info = self._subscribe_image_http_info(request)
        return self._call_api(**http_info)

    def subscribe_image_async_invoker(self, request):
        http_info = self._subscribe_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _subscribe_image_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images/subscribe",
            "request_type": request.__class__.__name__,
            "response_type": "SubscribeImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def subscribe_workflow_async(self, request):
        """订阅流程

        订阅流程
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SubscribeWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.SubscribeWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.SubscribeWorkflowResponse`
        """
        http_info = self._subscribe_workflow_http_info(request)
        return self._call_api(**http_info)

    def subscribe_workflow_async_invoker(self, request):
        http_info = self._subscribe_workflow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _subscribe_workflow_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/workflows/subscribe",
            "request_type": request.__class__.__name__,
            "response_type": "SubscribeWorkflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def transfer_project_async(self, request):
        """转移项目

        转移项目
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for TransferProject
        :type request: :class:`huaweicloudsdkeihealth.v1.TransferProjectRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.TransferProjectResponse`
        """
        http_info = self._transfer_project_http_info(request)
        return self._call_api(**http_info)

    def transfer_project_async_invoker(self, request):
        http_info = self._transfer_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _transfer_project_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/transfer",
            "request_type": request.__class__.__name__,
            "response_type": "TransferProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def update_app_async(self, request):
        """更新应用

        更新应用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateApp
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateAppResponse`
        """
        http_info = self._update_app_http_info(request)
        return self._call_api(**http_info)

    def update_app_async_invoker(self, request):
        http_info = self._update_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_app_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def update_archive_config_async(self, request):
        """修改跨域归档设置

        修改跨域归档设置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateArchiveConfig
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateArchiveConfigRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateArchiveConfigResponse`
        """
        http_info = self._update_archive_config_http_info(request)
        return self._call_api(**http_info)

    def update_archive_config_async_invoker(self, request):
        http_info = self._update_archive_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_archive_config_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/system/archive-configs/{region_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateArchiveConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'region_id' in local_var_params:
            path_params['region_id'] = local_var_params['region_id']

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

    def update_asset_version_async(self, request):
        """更新资产指定版本的信息

        更新资产指定版本的信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAssetVersion
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateAssetVersionRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateAssetVersionResponse`
        """
        http_info = self._update_asset_version_http_info(request)
        return self._call_api(**http_info)

    def update_asset_version_async_invoker(self, request):
        http_info = self._update_asset_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_asset_version_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/assets/{asset_id}/versions/{version}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAssetVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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

    def update_auto_job_async(self, request):
        """更新自动作业模板

        更新自动作业模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAutoJob
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateAutoJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateAutoJobResponse`
        """
        http_info = self._update_auto_job_http_info(request)
        return self._call_api(**http_info)

    def update_auto_job_async_invoker(self, request):
        http_info = self._update_auto_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_auto_job_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/auto-jobs/{auto_job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAutoJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'auto_job_id' in local_var_params:
            path_params['auto_job_id'] = local_var_params['auto_job_id']

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

    def update_data_path_policy_async(self, request):
        """设置数据对象策略

        设置数据对象策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDataPathPolicy
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateDataPathPolicyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateDataPathPolicyResponse`
        """
        http_info = self._update_data_path_policy_http_info(request)
        return self._call_api(**http_info)

    def update_data_path_policy_async_invoker(self, request):
        http_info = self._update_data_path_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_data_path_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/{path}/policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDataPathPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'path' in local_var_params:
            path_params['path'] = local_var_params['path']

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

    def update_data_policy_async(self, request):
        """设置项目级权限控制策略

        设置项目级权限控制策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDataPolicy
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateDataPolicyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateDataPolicyResponse`
        """
        http_info = self._update_data_policy_http_info(request)
        return self._call_api(**http_info)

    def update_data_policy_async_invoker(self, request):
        http_info = self._update_data_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_data_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDataPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def update_database_data_async(self, request):
        """更新数据

        更新数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDatabaseData
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateDatabaseDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateDatabaseDataResponse`
        """
        http_info = self._update_database_data_http_info(request)
        return self._call_api(**http_info)

    def update_database_data_async_invoker(self, request):
        http_info = self._update_database_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_database_data_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases/{database_id}/data/{row_num}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDatabaseDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'database_id' in local_var_params:
            path_params['database_id'] = local_var_params['database_id']
        if 'row_num' in local_var_params:
            path_params['row_num'] = local_var_params['row_num']

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

    def update_drug_database_async(self, request):
        """更新药物数据库

        更新药物数据库
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDrugDatabase
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateDrugDatabaseRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateDrugDatabaseResponse`
        """
        http_info = self._update_drug_database_http_info(request)
        return self._call_api(**http_info)

    def update_drug_database_async_invoker(self, request):
        http_info = self._update_drug_database_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_drug_database_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/drug/databases/{database_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDrugDatabaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'database_id' in local_var_params:
            path_params['database_id'] = local_var_params['database_id']

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

    def update_drug_job_async(self, request):
        """更新药物作业

        更新药物作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDrugJob
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateDrugJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateDrugJobResponse`
        """
        http_info = self._update_drug_job_http_info(request)
        return self._call_api(**http_info)

    def update_drug_job_async_invoker(self, request):
        http_info = self._update_drug_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_drug_job_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDrugJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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

    def update_drug_model_async(self, request):
        """更新药物模型

        更新药物模型
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDrugModel
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateDrugModelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateDrugModelResponse`
        """
        http_info = self._update_drug_model_http_info(request)
        return self._call_api(**http_info)

    def update_drug_model_async_invoker(self, request):
        http_info = self._update_drug_model_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_drug_model_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/drug-models/{model_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDrugModelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'model_id' in local_var_params:
            path_params['model_id'] = local_var_params['model_id']

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

    def update_image_async(self, request):
        """更新镜像描述信息或者类型

        更新镜像描述信息或者类型
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateImage
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateImageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateImageResponse`
        """
        http_info = self._update_image_http_info(request)
        return self._call_api(**http_info)

    def update_image_async_invoker(self, request):
        http_info = self._update_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_image_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images/{image_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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

    def update_init_password_async(self, request):
        """新用户重置密码

        新用户重置密码
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInitPassword
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateInitPasswordRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateInitPasswordResponse`
        """
        http_info = self._update_init_password_http_info(request)
        return self._call_api(**http_info)

    def update_init_password_async_invoker(self, request):
        http_info = self._update_init_password_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_init_password_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/users/{user_id}/init-password",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInitPasswordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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

    def update_job_async(self, request):
        """更新作业

        更新作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateJob
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateJobResponse`
        """
        http_info = self._update_job_http_info(request)
        return self._call_api(**http_info)

    def update_job_async_invoker(self, request):
        http_info = self._update_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_job_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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

    def update_job_config_async(self, request):
        """设置作业配置

        设置作业配置，目前支持修改作业保存条数(1万条-1000万条)，默认设置为500万条；
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateJobConfig
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateJobConfigRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateJobConfigResponse`
        """
        http_info = self._update_job_config_http_info(request)
        return self._call_api(**http_info)

    def update_job_config_async_invoker(self, request):
        http_info = self._update_job_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_job_config_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/system/job-config",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateJobConfigResponse"
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

    def update_member_async(self, request):
        """更新或者添加项目成员角色

        更新或者添加项目成员角色
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMember
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateMemberRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateMemberResponse`
        """
        http_info = self._update_member_http_info(request)
        return self._call_api(**http_info)

    def update_member_async_invoker(self, request):
        http_info = self._update_member_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_member_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/members/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMemberResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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

    def update_message_clear_rule_request_body_async(self, request):
        """设置消息清理规则

        设置消息清理规则，支持修改记录数(1W-1000W)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMessageClearRuleRequestBody
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateMessageClearRuleRequestBodyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateMessageClearRuleRequestBodyResponse`
        """
        http_info = self._update_message_clear_rule_request_body_http_info(request)
        return self._call_api(**http_info)

    def update_message_clear_rule_request_body_async_invoker(self, request):
        http_info = self._update_message_clear_rule_request_body_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_message_clear_rule_request_body_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/messages/rules",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMessageClearRuleRequestBodyResponse"
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

    def update_message_email_config_async(self, request):
        """设置消息邮件配置

        设置消息邮件配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMessageEmailConfig
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateMessageEmailConfigRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateMessageEmailConfigResponse`
        """
        http_info = self._update_message_email_config_http_info(request)
        return self._call_api(**http_info)

    def update_message_email_config_async_invoker(self, request):
        http_info = self._update_message_email_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_message_email_config_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/messages/email-server-config",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMessageEmailConfigResponse"
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

    def update_message_receive_config_async(self, request):
        """设置用户邮件配置

        设置用户邮件配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMessageReceiveConfig
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateMessageReceiveConfigRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateMessageReceiveConfigResponse`
        """
        http_info = self._update_message_receive_config_http_info(request)
        return self._call_api(**http_info)

    def update_message_receive_config_async_invoker(self, request):
        http_info = self._update_message_receive_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_message_receive_config_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/messages/email-client-config",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMessageReceiveConfigResponse"
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

    def update_performance_resource_async(self, request):
        """更新性能加速资源配置

        更新性能加速资源配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePerformanceResource
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdatePerformanceResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdatePerformanceResourceResponse`
        """
        http_info = self._update_performance_resource_http_info(request)
        return self._call_api(**http_info)

    def update_performance_resource_async_invoker(self, request):
        http_info = self._update_performance_resource_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_performance_resource_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/system/performance-resources/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePerformanceResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def update_project_async(self, request):
        """更新项目

        更新项目
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateProject
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateProjectRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateProjectResponse`
        """
        http_info = self._update_project_http_info(request)
        return self._call_api(**http_info)

    def update_project_async_invoker(self, request):
        http_info = self._update_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_project_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def update_project_tracker_async(self, request):
        """更新项目审计日志追踪器配置

        更新项目审计日志追踪器配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateProjectTracker
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateProjectTrackerRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateProjectTrackerResponse`
        """
        http_info = self._update_project_tracker_http_info(request)
        return self._call_api(**http_info)

    def update_project_tracker_async_invoker(self, request):
        http_info = self._update_project_tracker_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_project_tracker_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/project-tracker",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProjectTrackerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def update_scale_in_policy_async(self, request):
        """修改缩容策略

        修改缩容策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateScaleInPolicy
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateScaleInPolicyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateScaleInPolicyResponse`
        """
        http_info = self._update_scale_in_policy_http_info(request)
        return self._call_api(**http_info)

    def update_scale_in_policy_async_invoker(self, request):
        http_info = self._update_scale_in_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_scale_in_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/system/autoscaler/scale-in-policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateScaleInPolicyResponse"
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

    def update_scale_out_policy_async(self, request):
        """修改扩容策略

        修改扩容策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateScaleOutPolicy
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateScaleOutPolicyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateScaleOutPolicyResponse`
        """
        http_info = self._update_scale_out_policy_http_info(request)
        return self._call_api(**http_info)

    def update_scale_out_policy_async_invoker(self, request):
        http_info = self._update_scale_out_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_scale_out_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/system/autoscaler/scale-out-policies/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateScaleOutPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def update_schedule_async(self, request):
        """修改计算资源调度信息

        修改计算资源调度信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSchedule
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateScheduleRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateScheduleResponse`
        """
        http_info = self._update_schedule_http_info(request)
        return self._call_api(**http_info)

    def update_schedule_async_invoker(self, request):
        http_info = self._update_schedule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_schedule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/system/computing-resources/{id}/schedule",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateScheduleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def update_star_async(self, request):
        """收藏资产

        收藏资产
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateStar
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateStarRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateStarResponse`
        """
        http_info = self._update_star_http_info(request)
        return self._call_api(**http_info)

    def update_star_async_invoker(self, request):
        http_info = self._update_star_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_star_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/assets/{asset_id}/stars",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateStarResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

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

    def update_user_async(self, request):
        """修改用户基本信息

        修改用户基本信息（邮箱，手机）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateUser
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateUserRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateUserResponse`
        """
        http_info = self._update_user_http_info(request)
        return self._call_api(**http_info)

    def update_user_async_invoker(self, request):
        http_info = self._update_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_user_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/users/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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

    def update_user_by_domain_async(self, request):
        """最终租户修改子用户

        最终租户修改子用户
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateUserByDomain
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateUserByDomainRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateUserByDomainResponse`
        """
        http_info = self._update_user_by_domain_http_info(request)
        return self._call_api(**http_info)

    def update_user_by_domain_async_invoker(self, request):
        http_info = self._update_user_by_domain_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_user_by_domain_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/users/{user_id}/domain-change-info",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateUserByDomainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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

    def update_user_role_async(self, request):
        """更新用户角色

        更新用户角色
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateUserRole
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateUserRoleRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateUserRoleResponse`
        """
        http_info = self._update_user_role_http_info(request)
        return self._call_api(**http_info)

    def update_user_role_async_invoker(self, request):
        http_info = self._update_user_role_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_user_role_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/users/{user_id}/role",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateUserRoleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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

    def update_user_setting_async(self, request):
        """更新用户设置

        更新用户设置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateUserSetting
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateUserSettingRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateUserSettingResponse`
        """
        http_info = self._update_user_setting_http_info(request)
        return self._call_api(**http_info)

    def update_user_setting_async_invoker(self, request):
        http_info = self._update_user_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_user_setting_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/users/{user_id}/settings",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateUserSettingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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

    def update_vendor_async(self, request):
        """设置供应商配置

        设置供应商配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateVendor
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateVendorRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateVendorResponse`
        """
        http_info = self._update_vendor_http_info(request)
        return self._call_api(**http_info)

    def update_vendor_async_invoker(self, request):
        http_info = self._update_vendor_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_vendor_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/system/vendor-config",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateVendorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']
        if 'name' in local_var_params:
            form_params['name'] = local_var_params['name']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_workflow_async(self, request):
        """更新流程

        更新流程
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateWorkflowResponse`
        """
        http_info = self._update_workflow_http_info(request)
        return self._call_api(**http_info)

    def update_workflow_async_invoker(self, request):
        http_info = self._update_workflow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_workflow_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/workflows/{workflow_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateWorkflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

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

    def upload_data_async(self, request):
        """上传数据文件

        上传数据文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UploadData
        :type request: :class:`huaweicloudsdkeihealth.v1.UploadDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UploadDataResponse`
        """
        http_info = self._upload_data_http_info(request)
        return self._call_api(**http_info)

    def upload_data_async_invoker(self, request):
        http_info = self._upload_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upload_data_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/upload",
            "request_type": request.__class__.__name__,
            "response_type": "UploadDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []

        header_params = {}

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']
        if 'target_folder' in local_var_params:
            form_params['target_folder'] = local_var_params['target_folder']
        if 'part_number' in local_var_params:
            form_params['part_number'] = local_var_params['part_number']
        if 'total_part' in local_var_params:
            form_params['total_part'] = local_var_params['total_part']
        if 'multipart_id' in local_var_params:
            form_params['multipart_id'] = local_var_params['multipart_id']
        if 'file_name' in local_var_params:
            form_params['file_name'] = local_var_params['file_name']
        if 'md5' in local_var_params:
            form_params['md5'] = local_var_params['md5']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def upload_template_async(self, request):
        """上传模板

        上传模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UploadTemplate
        :type request: :class:`huaweicloudsdkeihealth.v1.UploadTemplateRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UploadTemplateResponse`
        """
        http_info = self._upload_template_http_info(request)
        return self._call_api(**http_info)

    def upload_template_async_invoker(self, request):
        http_info = self._upload_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upload_template_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/templates/upload",
            "request_type": request.__class__.__name__,
            "response_type": "UploadTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []

        header_params = {}

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def validate_code_async(self, request):
        """预验证

        预验证
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ValidateCode
        :type request: :class:`huaweicloudsdkeihealth.v1.ValidateCodeRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ValidateCodeResponse`
        """
        http_info = self._validate_code_http_info(request)
        return self._call_api(**http_info)

    def validate_code_async_invoker(self, request):
        http_info = self._validate_code_http_info(request)
        return AsyncInvoker(self, http_info)

    def _validate_code_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/users/{user_id}/code-verify",
            "request_type": request.__class__.__name__,
            "response_type": "ValidateCodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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

    def show_admet_properties_async(self, request):
        """ADMET属性预测接口

        计算小分子的物化性质，包括吸收(adsorption)、分布(distribution)、代谢(metabolism)、清除(excretion)与毒性(toxicity)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAdmetProperties
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowAdmetPropertiesRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowAdmetPropertiesResponse`
        """
        http_info = self._show_admet_properties_http_info(request)
        return self._call_api(**http_info)

    def show_admet_properties_async_invoker(self, request):
        http_info = self._show_admet_properties_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_admet_properties_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/admet",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAdmetPropertiesResponse"
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

    def create_cpi_task_async(self, request):
        """新建CPI任务接口

        输入蛋白序列、小分子库，创建分子-蛋白互作预测任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCpiTask
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateCpiTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateCpiTaskResponse`
        """
        http_info = self._create_cpi_task_http_info(request)
        return self._call_api(**http_info)

    def create_cpi_task_async_invoker(self, request):
        http_info = self._create_cpi_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_cpi_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/task/cpi",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCpiTaskResponse"
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

    def show_cpi_task_result_async(self, request):
        """查询CPI任务

        通过CPI任务ID查询CPI任务状态及结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCpiTaskResult
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowCpiTaskResultRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowCpiTaskResultResponse`
        """
        http_info = self._show_cpi_task_result_http_info(request)
        return self._call_api(**http_info)

    def show_cpi_task_result_async_invoker(self, request):
        http_info = self._show_cpi_task_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_cpi_task_result_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/task/cpi/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCpiTaskResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def create_css_cluster_async(self, request):
        """绑定CSS集群

        绑定CSS集群
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCssCluster
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateCssClusterRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateCssClusterResponse`
        """
        http_info = self._create_css_cluster_http_info(request)
        return self._call_api(**http_info)

    def create_css_cluster_async_invoker(self, request):
        http_info = self._create_css_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_css_cluster_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/drug/css-clusters",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCssClusterResponse"
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

    def delete_css_cluster_async(self, request):
        """CSS集群解绑

        CSS集群解绑
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCssCluster
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteCssClusterRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteCssClusterResponse`
        """
        http_info = self._delete_css_cluster_http_info(request)
        return self._call_api(**http_info)

    def delete_css_cluster_async_invoker(self, request):
        http_info = self._delete_css_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_css_cluster_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/drug/css-clusters/{css_cluster_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCssClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'css_cluster_id' in local_var_params:
            path_params['css_cluster_id'] = local_var_params['css_cluster_id']

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

    def list_css_cluster_async(self, request):
        """获取CSS集群列表

        获取CSS集群列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCssCluster
        :type request: :class:`huaweicloudsdkeihealth.v1.ListCssClusterRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListCssClusterResponse`
        """
        http_info = self._list_css_cluster_http_info(request)
        return self._call_api(**http_info)

    def list_css_cluster_async_invoker(self, request):
        http_info = self._list_css_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_css_cluster_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/drug/css-clusters",
            "request_type": request.__class__.__name__,
            "response_type": "ListCssClusterResponse"
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

    def list_term_tenant_css_cluster_async(self, request):
        """获取最终租户CSS集群列表

        获取最终租户CSS集群列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTermTenantCssCluster
        :type request: :class:`huaweicloudsdkeihealth.v1.ListTermTenantCssClusterRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListTermTenantCssClusterResponse`
        """
        http_info = self._list_term_tenant_css_cluster_http_info(request)
        return self._call_api(**http_info)

    def list_term_tenant_css_cluster_async_invoker(self, request):
        http_info = self._list_term_tenant_css_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_term_tenant_css_cluster_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/css/clusters",
            "request_type": request.__class__.__name__,
            "response_type": "ListTermTenantCssClusterResponse"
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

    def validate_css_connection_async(self, request):
        """测试CSS集群连接

        测试CSS集群连接
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ValidateCssConnection
        :type request: :class:`huaweicloudsdkeihealth.v1.ValidateCssConnectionRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ValidateCssConnectionResponse`
        """
        http_info = self._validate_css_connection_http_info(request)
        return self._call_api(**http_info)

    def validate_css_connection_async_invoker(self, request):
        http_info = self._validate_css_connection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _validate_css_connection_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/drug/css-clusters/connection",
            "request_type": request.__class__.__name__,
            "response_type": "ValidateCssConnectionResponse"
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

    def create_custom_props_task_async(self, request):
        """新建自定义属性任务接口

        输入自定义属性的任务数据，创建自定义属性建模任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCustomPropsTask
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateCustomPropsTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateCustomPropsTaskResponse`
        """
        http_info = self._create_custom_props_task_http_info(request)
        return self._call_api(**http_info)

    def create_custom_props_task_async_invoker(self, request):
        http_info = self._create_custom_props_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_custom_props_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/custom-props",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCustomPropsTaskResponse"
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

    def show_custom_props_task_result_async(self, request):
        """查询自定义属性任务

        通过自定义属性任务ID查询任务状态及结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCustomPropsTaskResult
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowCustomPropsTaskResultRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowCustomPropsTaskResultResponse`
        """
        http_info = self._show_custom_props_task_result_http_info(request)
        return self._call_api(**http_info)

    def show_custom_props_task_result_async_invoker(self, request):
        http_info = self._show_custom_props_task_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_custom_props_task_result_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/custom-props/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCustomPropsTaskResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def create_generation_task_async(self, request):
        """新建分子生成任务接口

        输入分子属性约束，创建分子生成任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateGenerationTask
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateGenerationTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateGenerationTaskResponse`
        """
        http_info = self._create_generation_task_http_info(request)
        return self._call_api(**http_info)

    def create_generation_task_async_invoker(self, request):
        http_info = self._create_generation_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_generation_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/task/generation",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGenerationTaskResponse"
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

    def show_generation_task_result_async(self, request):
        """查询分子生成任务

        通过分子生成任务ID查询分子生成任务状态及结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGenerationTaskResult
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowGenerationTaskResultRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowGenerationTaskResultResponse`
        """
        http_info = self._show_generation_task_result_http_info(request)
        return self._call_api(**http_info)

    def show_generation_task_result_async_invoker(self, request):
        http_info = self._show_generation_task_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_generation_task_result_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/task/generation/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGenerationTaskResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def check_drug_ligand_difference_async(self, request):
        """计算配体间的3D结构差异

        计算配体间的3D结构差异
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckDrugLigandDifference
        :type request: :class:`huaweicloudsdkeihealth.v1.CheckDrugLigandDifferenceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CheckDrugLigandDifferenceResponse`
        """
        http_info = self._check_drug_ligand_difference_http_info(request)
        return self._call_api(**http_info)

    def check_drug_ligand_difference_async_invoker(self, request):
        http_info = self._check_drug_ligand_difference_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_drug_ligand_difference_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/ligand/diff3d",
            "request_type": request.__class__.__name__,
            "response_type": "CheckDrugLigandDifferenceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def create_drug_ligand_interaction2d_svg_async(self, request):
        """生成相互作用2D图

        生成相互作用2D图，若不提供配体文件，则受体文件中必须包含配体；若提供配体文件，则受体中的配体（若有）则会被忽略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDrugLigandInteraction2dSvg
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandInteraction2dSvgRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandInteraction2dSvgResponse`
        """
        http_info = self._create_drug_ligand_interaction2d_svg_http_info(request)
        return self._call_api(**http_info)

    def create_drug_ligand_interaction2d_svg_async_invoker(self, request):
        http_info = self._create_drug_ligand_interaction2d_svg_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_drug_ligand_interaction2d_svg_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/ligand/interaction2d",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDrugLigandInteraction2dSvgResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def create_drug_ligand_preview_task_async(self, request):
        """创建配体文件预览任务

        创建配体文件预览任务，支持SMI、SDF、PDB、MOL2
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDrugLigandPreviewTask
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandPreviewTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandPreviewTaskResponse`
        """
        http_info = self._create_drug_ligand_preview_task_http_info(request)
        return self._call_api(**http_info)

    def create_drug_ligand_preview_task_async_invoker(self, request):
        http_info = self._create_drug_ligand_preview_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_drug_ligand_preview_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/ligand/preview",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDrugLigandPreviewTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def create_drug_ligand_sdf_async(self, request):
        """生成分子SDF三维结构

        生成分子SDF三维结构
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDrugLigandSdf
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandSdfRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandSdfResponse`
        """
        http_info = self._create_drug_ligand_sdf_http_info(request)
        return self._call_api(**http_info)

    def create_drug_ligand_sdf_async_invoker(self, request):
        http_info = self._create_drug_ligand_sdf_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_drug_ligand_sdf_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/ligand/sdf",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDrugLigandSdfResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def create_drug_ligand_similarity_graph_task_async(self, request):
        """创建配体相似性图计算任务

        创建配体相似性图计算任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDrugLigandSimilarityGraphTask
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandSimilarityGraphTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandSimilarityGraphTaskResponse`
        """
        http_info = self._create_drug_ligand_similarity_graph_task_http_info(request)
        return self._call_api(**http_info)

    def create_drug_ligand_similarity_graph_task_async_invoker(self, request):
        http_info = self._create_drug_ligand_similarity_graph_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_drug_ligand_similarity_graph_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/ligand/similarity-graph",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDrugLigandSimilarityGraphTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def create_drug_ligand_svg_async(self, request):
        """生成分子SVG图

        生成分子SVG图
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDrugLigandSvg
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandSvgRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandSvgResponse`
        """
        http_info = self._create_drug_ligand_svg_http_info(request)
        return self._call_api(**http_info)

    def create_drug_ligand_svg_async_invoker(self, request):
        http_info = self._create_drug_ligand_svg_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_drug_ligand_svg_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/ligand/svg",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDrugLigandSvgResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def delete_drug_ligand_preview_task_async(self, request):
        """删除配体文件预览任务

        删除配体文件预览任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDrugLigandPreviewTask
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteDrugLigandPreviewTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteDrugLigandPreviewTaskResponse`
        """
        http_info = self._delete_drug_ligand_preview_task_http_info(request)
        return self._call_api(**http_info)

    def delete_drug_ligand_preview_task_async_invoker(self, request):
        http_info = self._delete_drug_ligand_preview_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_drug_ligand_preview_task_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/ligand/preview/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDrugLigandPreviewTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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

    def delete_drug_ligand_similarity_graph_task_async(self, request):
        """删除配体相似性图计算任务

        删除配体相似性图计算任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDrugLigandSimilarityGraphTask
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteDrugLigandSimilarityGraphTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteDrugLigandSimilarityGraphTaskResponse`
        """
        http_info = self._delete_drug_ligand_similarity_graph_task_http_info(request)
        return self._call_api(**http_info)

    def delete_drug_ligand_similarity_graph_task_async_invoker(self, request):
        http_info = self._delete_drug_ligand_similarity_graph_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_drug_ligand_similarity_graph_task_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/ligand/similarity-graph/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDrugLigandSimilarityGraphTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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

    def parse_drug_receptor_info_async(self, request):
        """受体信息解析

        受体信息解析，如果有多个受体蛋白则只处理第一个，如果一个受体蛋白里结合了多个配体，则最多只处理前10个
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ParseDrugReceptorInfo
        :type request: :class:`huaweicloudsdkeihealth.v1.ParseDrugReceptorInfoRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ParseDrugReceptorInfoResponse`
        """
        http_info = self._parse_drug_receptor_info_http_info(request)
        return self._call_api(**http_info)

    def parse_drug_receptor_info_async_invoker(self, request):
        http_info = self._parse_drug_receptor_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _parse_drug_receptor_info_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/receptor/info",
            "request_type": request.__class__.__name__,
            "response_type": "ParseDrugReceptorInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def recognize_drug_receptor_pocket_async(self, request):
        """受体口袋检测

        检测受体口袋，检测类型基于配体，基于氨基酸残基，自动检测，自定义和全局对接
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RecognizeDrugReceptorPocket
        :type request: :class:`huaweicloudsdkeihealth.v1.RecognizeDrugReceptorPocketRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.RecognizeDrugReceptorPocketResponse`
        """
        http_info = self._recognize_drug_receptor_pocket_http_info(request)
        return self._call_api(**http_info)

    def recognize_drug_receptor_pocket_async_invoker(self, request):
        http_info = self._recognize_drug_receptor_pocket_http_info(request)
        return AsyncInvoker(self, http_info)

    def _recognize_drug_receptor_pocket_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/receptor/pocket",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeDrugReceptorPocketResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def run_drug_ligand_to_smiles_conversion_async(self, request):
        """配体格式转换为SMILES

        配体格式转换为SMILES，若配体文件中存在多个分子，则只取第一个返回
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunDrugLigandToSmilesConversion
        :type request: :class:`huaweicloudsdkeihealth.v1.RunDrugLigandToSmilesConversionRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.RunDrugLigandToSmilesConversionResponse`
        """
        http_info = self._run_drug_ligand_to_smiles_conversion_http_info(request)
        return self._call_api(**http_info)

    def run_drug_ligand_to_smiles_conversion_async_invoker(self, request):
        http_info = self._run_drug_ligand_to_smiles_conversion_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_drug_ligand_to_smiles_conversion_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/ligand/smiles",
            "request_type": request.__class__.__name__,
            "response_type": "RunDrugLigandToSmilesConversionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def run_drug_receptor_preprocess_async(self, request):
        """受体预处理

        受体预处理，用于前端显示预处理后的受体
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunDrugReceptorPreprocess
        :type request: :class:`huaweicloudsdkeihealth.v1.RunDrugReceptorPreprocessRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.RunDrugReceptorPreprocessResponse`
        """
        http_info = self._run_drug_receptor_preprocess_http_info(request)
        return self._call_api(**http_info)

    def run_drug_receptor_preprocess_async_invoker(self, request):
        http_info = self._run_drug_receptor_preprocess_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_drug_receptor_preprocess_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/receptor/preprocess",
            "request_type": request.__class__.__name__,
            "response_type": "RunDrugReceptorPreprocessResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def show_drug_ligand_preview_task_async(self, request):
        """查询配体文件预览任务

        查询配体文件预览任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDrugLigandPreviewTask
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowDrugLigandPreviewTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowDrugLigandPreviewTaskResponse`
        """
        http_info = self._show_drug_ligand_preview_task_http_info(request)
        return self._call_api(**http_info)

    def show_drug_ligand_preview_task_async_invoker(self, request):
        http_info = self._show_drug_ligand_preview_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_drug_ligand_preview_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/ligand/preview/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDrugLigandPreviewTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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

    def show_drug_ligand_similarity_graph_task_async(self, request):
        """查询配体相似性图计算任务

        查询配体相似性图计算任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDrugLigandSimilarityGraphTask
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowDrugLigandSimilarityGraphTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowDrugLigandSimilarityGraphTaskResponse`
        """
        http_info = self._show_drug_ligand_similarity_graph_task_http_info(request)
        return self._call_api(**http_info)

    def show_drug_ligand_similarity_graph_task_async_invoker(self, request):
        http_info = self._show_drug_ligand_similarity_graph_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_drug_ligand_similarity_graph_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/ligand/similarity-graph/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDrugLigandSimilarityGraphTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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

    def download_data_async(self, request):
        """文件下载

        文件下载
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadData
        :type request: :class:`huaweicloudsdkeihealth.v1.DownloadDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DownloadDataResponse`
        """
        http_info = self._download_data_http_info(request)
        return self._call_api(**http_info)

    def download_data_async_invoker(self, request):
        http_info = self._download_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_data_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/data/download",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def show_overview_async(self, request):
        """获取医疗平台信息

        获取医疗平台信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOverview
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowOverviewRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowOverviewResponse`
        """
        http_info = self._show_overview_http_info(request)
        return self._call_api(**http_info)

    def show_overview_async_invoker(self, request):
        http_info = self._show_overview_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_overview_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/overview",
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

    def clean_nextflow_cache_async(self, request):
        """清理Nextflow缓存

        清理Nextflow缓存
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CleanNextflowCache
        :type request: :class:`huaweicloudsdkeihealth.v1.CleanNextflowCacheRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CleanNextflowCacheResponse`
        """
        http_info = self._clean_nextflow_cache_http_info(request)
        return self._call_api(**http_info)

    def clean_nextflow_cache_async_invoker(self, request):
        http_info = self._clean_nextflow_cache_http_info(request)
        return AsyncInvoker(self, http_info)

    def _clean_nextflow_cache_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/nextflow/clean-cache",
            "request_type": request.__class__.__name__,
            "response_type": "CleanNextflowCacheResponse"
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

    def create_nextflow_job_async(self, request):
        """创建nextflow作业

        创建nextflow作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateNextflowJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateNextflowJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateNextflowJobResponse`
        """
        http_info = self._create_nextflow_job_http_info(request)
        return self._call_api(**http_info)

    def create_nextflow_job_async_invoker(self, request):
        http_info = self._create_nextflow_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_nextflow_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateNextflowJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []

        header_params = {}

        form_params = {}
        if 'name' in local_var_params:
            form_params['name'] = local_var_params['name']
        if 'description' in local_var_params:
            form_params['description'] = local_var_params['description']
        if 'labels' in local_var_params:
            form_params['labels'] = local_var_params['labels']
            collection_formats['labels'] = 'csv'
        if 'workflow_id' in local_var_params:
            form_params['workflow_id'] = local_var_params['workflow_id']
        if 'params' in local_var_params:
            form_params['params'] = local_var_params['params']
        if 'priority' in local_var_params:
            form_params['priority'] = local_var_params['priority']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_nextflow_workflow_async(self, request):
        """创建流程

        创建流程
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateNextflowWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateNextflowWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateNextflowWorkflowResponse`
        """
        http_info = self._create_nextflow_workflow_http_info(request)
        return self._call_api(**http_info)

    def create_nextflow_workflow_async_invoker(self, request):
        http_info = self._create_nextflow_workflow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_nextflow_workflow_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/workflows",
            "request_type": request.__class__.__name__,
            "response_type": "CreateNextflowWorkflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []

        header_params = {}

        form_params = {}
        if 'workflow_file' in local_var_params:
            form_params['workflow_file'] = local_var_params['workflow_file']
        if 'name' in local_var_params:
            form_params['name'] = local_var_params['name']
        if 'description' in local_var_params:
            form_params['description'] = local_var_params['description']
        if 'labels' in local_var_params:
            form_params['labels'] = local_var_params['labels']
            collection_formats['labels'] = 'csv'
        if 'main_file' in local_var_params:
            form_params['main_file'] = local_var_params['main_file']
        if 'params' in local_var_params:
            form_params['params'] = local_var_params['params']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_nextflow_job_async(self, request):
        """删除Nextflow作业

        删除Nextflow作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteNextflowJob
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteNextflowJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteNextflowJobResponse`
        """
        http_info = self._delete_nextflow_job_http_info(request)
        return self._call_api(**http_info)

    def delete_nextflow_job_async_invoker(self, request):
        http_info = self._delete_nextflow_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_nextflow_job_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNextflowJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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

    def delete_nextflow_workflow_async(self, request):
        """删除流程

        删除流程
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteNextflowWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteNextflowWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteNextflowWorkflowResponse`
        """
        http_info = self._delete_nextflow_workflow_http_info(request)
        return self._call_api(**http_info)

    def delete_nextflow_workflow_async_invoker(self, request):
        http_info = self._delete_nextflow_workflow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_nextflow_workflow_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/workflows/{workflow_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNextflowWorkflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

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

    def install_nextflow_async(self, request):
        """安装Nextflow

        安装Nextflow（file和version参数必须提供其中一种）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for InstallNextflow
        :type request: :class:`huaweicloudsdkeihealth.v1.InstallNextflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.InstallNextflowResponse`
        """
        http_info = self._install_nextflow_http_info(request)
        return self._call_api(**http_info)

    def install_nextflow_async_invoker(self, request):
        http_info = self._install_nextflow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _install_nextflow_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/nextflow/engines",
            "request_type": request.__class__.__name__,
            "response_type": "InstallNextflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']
        if 'part_number' in local_var_params:
            form_params['part_number'] = local_var_params['part_number']
        if 'total_part' in local_var_params:
            form_params['total_part'] = local_var_params['total_part']
        if 'multipart_id' in local_var_params:
            form_params['multipart_id'] = local_var_params['multipart_id']
        if 'file_name' in local_var_params:
            form_params['file_name'] = local_var_params['file_name']
        if 'version' in local_var_params:
            form_params['version'] = local_var_params['version']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_nextflow_job_async(self, request):
        """查询nextflow作业列表

        查询nextflow作业列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNextflowJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ListNextflowJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListNextflowJobResponse`
        """
        http_info = self._list_nextflow_job_http_info(request)
        return self._call_api(**http_info)

    def list_nextflow_job_async_invoker(self, request):
        http_info = self._list_nextflow_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_nextflow_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListNextflowJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'job_name' in local_var_params:
            query_params.append(('job_name', local_var_params['job_name']))
        if 'labels' in local_var_params:
            query_params.append(('labels', local_var_params['labels']))
            collection_formats['labels'] = 'csv'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'workflow_name' in local_var_params:
            query_params.append(('workflow_name', local_var_params['workflow_name']))
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'create_start_time' in local_var_params:
            query_params.append(('create_start_time', local_var_params['create_start_time']))
        if 'create_end_time' in local_var_params:
            query_params.append(('create_end_time', local_var_params['create_end_time']))
        if 'finish_start_time' in local_var_params:
            query_params.append(('finish_start_time', local_var_params['finish_start_time']))
        if 'finish_end_time' in local_var_params:
            query_params.append(('finish_end_time', local_var_params['finish_end_time']))

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

    def list_nextflow_task_async(self, request):
        """获取task列表

        获取task列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNextflowTask
        :type request: :class:`huaweicloudsdkeihealth.v1.ListNextflowTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListNextflowTaskResponse`
        """
        http_info = self._list_nextflow_task_http_info(request)
        return self._call_api(**http_info)

    def list_nextflow_task_async_invoker(self, request):
        http_info = self._list_nextflow_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_nextflow_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/jobs/{job_id}/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListNextflowTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'search_key' in local_var_params:
            query_params.append(('search_key', local_var_params['search_key']))

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

    def list_nextflow_version_async(self, request):
        """查询Nextflow版本列表

        查询Nextflow版本列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNextflowVersion
        :type request: :class:`huaweicloudsdkeihealth.v1.ListNextflowVersionRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListNextflowVersionResponse`
        """
        http_info = self._list_nextflow_version_http_info(request)
        return self._call_api(**http_info)

    def list_nextflow_version_async_invoker(self, request):
        http_info = self._list_nextflow_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_nextflow_version_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/nextflow/versions",
            "request_type": request.__class__.__name__,
            "response_type": "ListNextflowVersionResponse"
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

    def list_nextflow_workflow_async(self, request):
        """获取流程列表

        获取流程列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNextflowWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.ListNextflowWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListNextflowWorkflowResponse`
        """
        http_info = self._list_nextflow_workflow_http_info(request)
        return self._call_api(**http_info)

    def list_nextflow_workflow_async_invoker(self, request):
        http_info = self._list_nextflow_workflow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_nextflow_workflow_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/workflows",
            "request_type": request.__class__.__name__,
            "response_type": "ListNextflowWorkflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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

    def retry_nextflow_job_async(self, request):
        """重试Nextflow作业

        重试Nextflow作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RetryNextflowJob
        :type request: :class:`huaweicloudsdkeihealth.v1.RetryNextflowJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.RetryNextflowJobResponse`
        """
        http_info = self._retry_nextflow_job_http_info(request)
        return self._call_api(**http_info)

    def retry_nextflow_job_async_invoker(self, request):
        http_info = self._retry_nextflow_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _retry_nextflow_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/jobs/{job_id}/retry",
            "request_type": request.__class__.__name__,
            "response_type": "RetryNextflowJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}

        form_params = {}
        if 'params' in local_var_params:
            form_params['params'] = local_var_params['params']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_nextflow_async(self, request):
        """查询Nextflow配置详情

        查询Nextflow配置详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNextflow
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowNextflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowNextflowResponse`
        """
        http_info = self._show_nextflow_http_info(request)
        return self._call_api(**http_info)

    def show_nextflow_async_invoker(self, request):
        http_info = self._show_nextflow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_nextflow_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/nextflow/engines/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNextflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def show_nextflow_job_async(self, request):
        """获取Nextflow作业详情

        获取Nextflow作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNextflowJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowNextflowJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowNextflowJobResponse`
        """
        http_info = self._show_nextflow_job_http_info(request)
        return self._call_api(**http_info)

    def show_nextflow_job_async_invoker(self, request):
        http_info = self._show_nextflow_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_nextflow_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNextflowJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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

    def show_nextflow_job_log_async(self, request):
        """获取Nextflow作业日志

        获取Nextflow作业日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNextflowJobLog
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowNextflowJobLogRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowNextflowJobLogResponse`
        """
        http_info = self._show_nextflow_job_log_http_info(request)
        return self._call_api(**http_info)

    def show_nextflow_job_log_async_invoker(self, request):
        http_info = self._show_nextflow_job_log_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_nextflow_job_log_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/jobs/{job_id}/logs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNextflowJobLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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

    def show_nextflow_job_reports_async(self, request):
        """获取Nextflow作业报告

        获取Nextflow作业报告
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNextflowJobReports
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowNextflowJobReportsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowNextflowJobReportsResponse`
        """
        http_info = self._show_nextflow_job_reports_http_info(request)
        return self._call_api(**http_info)

    def show_nextflow_job_reports_async_invoker(self, request):
        http_info = self._show_nextflow_job_reports_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_nextflow_job_reports_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/jobs/{job_id}/reports",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNextflowJobReportsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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

    def show_nextflow_task_detail_async(self, request):
        """获取task详情

        获取task详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNextflowTaskDetail
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowNextflowTaskDetailRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowNextflowTaskDetailResponse`
        """
        http_info = self._show_nextflow_task_detail_http_info(request)
        return self._call_api(**http_info)

    def show_nextflow_task_detail_async_invoker(self, request):
        http_info = self._show_nextflow_task_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_nextflow_task_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/jobs/{job_id}/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNextflowTaskDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
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

    def show_nextflow_task_log_async(self, request):
        """获取Nextflow任务日志

        获取Nextflow任务日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNextflowTaskLog
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowNextflowTaskLogRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowNextflowTaskLogResponse`
        """
        http_info = self._show_nextflow_task_log_http_info(request)
        return self._call_api(**http_info)

    def show_nextflow_task_log_async_invoker(self, request):
        http_info = self._show_nextflow_task_log_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_nextflow_task_log_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/jobs/{job_id}/tasks/{task_id}/logs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNextflowTaskLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
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

    def show_nextflow_workflow_async(self, request):
        """获取流程详情

        获取流程详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNextflowWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowNextflowWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowNextflowWorkflowResponse`
        """
        http_info = self._show_nextflow_workflow_http_info(request)
        return self._call_api(**http_info)

    def show_nextflow_workflow_async_invoker(self, request):
        http_info = self._show_nextflow_workflow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_nextflow_workflow_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/workflows/{workflow_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNextflowWorkflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

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

    def stop_nextflow_job_async(self, request):
        """停止Nextflow作业

        停止Nextflow作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopNextflowJob
        :type request: :class:`huaweicloudsdkeihealth.v1.StopNextflowJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.StopNextflowJobResponse`
        """
        http_info = self._stop_nextflow_job_http_info(request)
        return self._call_api(**http_info)

    def stop_nextflow_job_async_invoker(self, request):
        http_info = self._stop_nextflow_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_nextflow_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/jobs/{job_id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopNextflowJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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

    def uninstall_nextflow_async(self, request):
        """卸载Nextflow

        卸载Nextflow
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UninstallNextflow
        :type request: :class:`huaweicloudsdkeihealth.v1.UninstallNextflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UninstallNextflowResponse`
        """
        http_info = self._uninstall_nextflow_http_info(request)
        return self._call_api(**http_info)

    def uninstall_nextflow_async_invoker(self, request):
        http_info = self._uninstall_nextflow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _uninstall_nextflow_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/nextflow/engines/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UninstallNextflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def update_nextflow_workflow_async(self, request):
        """更新流程

        更新流程
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateNextflowWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateNextflowWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateNextflowWorkflowResponse`
        """
        http_info = self._update_nextflow_workflow_http_info(request)
        return self._call_api(**http_info)

    def update_nextflow_workflow_async_invoker(self, request):
        http_info = self._update_nextflow_workflow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_nextflow_workflow_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/workflows/{workflow_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNextflowWorkflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

        query_params = []

        header_params = {}

        form_params = {}
        if 'workflow_file' in local_var_params:
            form_params['workflow_file'] = local_var_params['workflow_file']
        if 'description' in local_var_params:
            form_params['description'] = local_var_params['description']
        if 'labels' in local_var_params:
            form_params['labels'] = local_var_params['labels']
            collection_formats['labels'] = 'csv'
        if 'main_file' in local_var_params:
            form_params['main_file'] = local_var_params['main_file']
        if 'params' in local_var_params:
            form_params['params'] = local_var_params['params']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_obs_bucket_async(self, request):
        """获取用户OBS桶列表

        获取用户OBS桶列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListObsBucket
        :type request: :class:`huaweicloudsdkeihealth.v1.ListObsBucketRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListObsBucketResponse`
        """
        http_info = self._list_obs_bucket_http_info(request)
        return self._call_api(**http_info)

    def list_obs_bucket_async_invoker(self, request):
        http_info = self._list_obs_bucket_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_obs_bucket_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/customer-buckets",
            "request_type": request.__class__.__name__,
            "response_type": "ListObsBucketResponse"
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

    def list_obs_bucket_object_async(self, request):
        """获取用户OBS桶内对象

        获取用户OBS桶内对象
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListObsBucketObject
        :type request: :class:`huaweicloudsdkeihealth.v1.ListObsBucketObjectRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListObsBucketObjectResponse`
        """
        http_info = self._list_obs_bucket_object_http_info(request)
        return self._call_api(**http_info)

    def list_obs_bucket_object_async_invoker(self, request):
        http_info = self._list_obs_bucket_object_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_obs_bucket_object_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/customer-buckets/{bucket_name}/objects",
            "request_type": request.__class__.__name__,
            "response_type": "ListObsBucketObjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'bucket_name' in local_var_params:
            path_params['bucket_name'] = local_var_params['bucket_name']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))
        if 'search_key' in local_var_params:
            query_params.append(('search_key', local_var_params['search_key']))

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

    def create_optimization_task_async(self, request):
        """新建分子优化任务接口

        输入起始小分子以及属性约束，创建分子优化任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateOptimizationTask
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateOptimizationTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateOptimizationTaskResponse`
        """
        http_info = self._create_optimization_task_http_info(request)
        return self._call_api(**http_info)

    def create_optimization_task_async_invoker(self, request):
        http_info = self._create_optimization_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_optimization_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/task/optimization",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOptimizationTaskResponse"
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

    def show_optimization_task_result_async(self, request):
        """查询分子优化任务

        通过分子优化任务ID查询分子优化任务状态及结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOptimizationTaskResult
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowOptimizationTaskResultRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowOptimizationTaskResultResponse`
        """
        http_info = self._show_optimization_task_result_http_info(request)
        return self._call_api(**http_info)

    def show_optimization_task_result_async_invoker(self, request):
        http_info = self._show_optimization_task_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_optimization_task_result_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/task/optimization/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOptimizationTaskResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def create_search_task_async(self, request):
        """新建分子搜索任务接口

        输入要查询的分子以及查询条件，创建分子搜索任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSearchTask
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateSearchTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateSearchTaskResponse`
        """
        http_info = self._create_search_task_http_info(request)
        return self._call_api(**http_info)

    def create_search_task_async_invoker(self, request):
        http_info = self._create_search_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_search_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/task/search",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSearchTaskResponse"
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

    def show_search_task_result_async(self, request):
        """查询分子搜索任务

        通过分子搜索任务ID查询分子搜索任务状态及结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSearchTaskResult
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowSearchTaskResultRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowSearchTaskResultResponse`
        """
        http_info = self._show_search_task_result_http_info(request)
        return self._call_api(**http_info)

    def show_search_task_result_async_invoker(self, request):
        http_info = self._show_search_task_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_search_task_result_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/task/search/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSearchTaskResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def create_synthesis_task_async(self, request):
        """新建分子合成路径规划任务接口

        输入要进行合成路径规划的分子以及输出可行方案的个数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSynthesisTask
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateSynthesisTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateSynthesisTaskResponse`
        """
        http_info = self._create_synthesis_task_http_info(request)
        return self._call_api(**http_info)

    def create_synthesis_task_async_invoker(self, request):
        http_info = self._create_synthesis_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_synthesis_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/task/synthesis",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSynthesisTaskResponse"
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

    def show_synthesis_task_result_async(self, request):
        """查询分子合成路径规划任务

        通过分子合成路径规划任务ID查询分子合成路径规划任务状态及结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSynthesisTaskResult
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowSynthesisTaskResultRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowSynthesisTaskResultResponse`
        """
        http_info = self._show_synthesis_task_result_http_info(request)
        return self._call_api(**http_info)

    def show_synthesis_task_result_async_invoker(self, request):
        http_info = self._show_synthesis_task_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_synthesis_task_result_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/task/synthesis/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSynthesisTaskResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def create_notebook_async(self, request):
        """创建notebook

        创建notebook
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateNotebook
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateNotebookRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateNotebookResponse`
        """
        http_info = self._create_notebook_http_info(request)
        return self._call_api(**http_info)

    def create_notebook_async_invoker(self, request):
        http_info = self._create_notebook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_notebook_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/notebooks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateNotebookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def delete_notebook_async(self, request):
        """删除notebook

        删除notebook
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteNotebook
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteNotebookRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteNotebookResponse`
        """
        http_info = self._delete_notebook_http_info(request)
        return self._call_api(**http_info)

    def delete_notebook_async_invoker(self, request):
        http_info = self._delete_notebook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_notebook_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/notebooks/{notebook_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNotebookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'notebook_id' in local_var_params:
            path_params['notebook_id'] = local_var_params['notebook_id']

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

    def list_notebook_async(self, request):
        """获取notebook列表

        获取notebook列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNotebook
        :type request: :class:`huaweicloudsdkeihealth.v1.ListNotebookRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListNotebookResponse`
        """
        http_info = self._list_notebook_http_info(request)
        return self._call_api(**http_info)

    def list_notebook_async_invoker(self, request):
        http_info = self._list_notebook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_notebook_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/notebooks",
            "request_type": request.__class__.__name__,
            "response_type": "ListNotebookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

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

    def list_notebook_tool_async(self, request):
        """获取notebook工作环境

        获取notebook工作环境
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNotebookTool
        :type request: :class:`huaweicloudsdkeihealth.v1.ListNotebookToolRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListNotebookToolResponse`
        """
        http_info = self._list_notebook_tool_http_info(request)
        return self._call_api(**http_info)

    def list_notebook_tool_async_invoker(self, request):
        http_info = self._list_notebook_tool_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_notebook_tool_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/notebooks/tools",
            "request_type": request.__class__.__name__,
            "response_type": "ListNotebookToolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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

    def show_notebook_async(self, request):
        """获取notebook详情

        获取notebook详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNotebook
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowNotebookRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowNotebookResponse`
        """
        http_info = self._show_notebook_http_info(request)
        return self._call_api(**http_info)

    def show_notebook_async_invoker(self, request):
        http_info = self._show_notebook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_notebook_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/notebooks/{notebook_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNotebookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'notebook_id' in local_var_params:
            path_params['notebook_id'] = local_var_params['notebook_id']

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

    def show_notebook_token_async(self, request):
        """获取notebook鉴权信息

        获取notebook鉴权信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNotebookToken
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowNotebookTokenRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowNotebookTokenResponse`
        """
        http_info = self._show_notebook_token_http_info(request)
        return self._call_api(**http_info)

    def show_notebook_token_async_invoker(self, request):
        http_info = self._show_notebook_token_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_notebook_token_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/notebooks/{notebook_id}/token",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNotebookTokenResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'notebook_id' in local_var_params:
            path_params['notebook_id'] = local_var_params['notebook_id']

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

    def stop_or_start_notebook_async(self, request):
        """启停notebook

        启停notebook
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopOrStartNotebook
        :type request: :class:`huaweicloudsdkeihealth.v1.StopOrStartNotebookRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.StopOrStartNotebookResponse`
        """
        http_info = self._stop_or_start_notebook_http_info(request)
        return self._call_api(**http_info)

    def stop_or_start_notebook_async_invoker(self, request):
        http_info = self._stop_or_start_notebook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_or_start_notebook_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/notebooks/{notebook_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "StopOrStartNotebookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'notebook_id' in local_var_params:
            path_params['notebook_id'] = local_var_params['notebook_id']

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

    def update_notebook_async(self, request):
        """更新notebook

        更新notebook
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateNotebook
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateNotebookRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateNotebookResponse`
        """
        http_info = self._update_notebook_http_info(request)
        return self._call_api(**http_info)

    def update_notebook_async_invoker(self, request):
        http_info = self._update_notebook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_notebook_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/notebooks/{notebook_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNotebookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'notebook_id' in local_var_params:
            path_params['notebook_id'] = local_var_params['notebook_id']

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
