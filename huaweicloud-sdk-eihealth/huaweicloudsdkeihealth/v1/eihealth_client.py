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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkeihealth'")


class EiHealthClient(Client):
    def __init__(self):
        super(EiHealthClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkeihealth.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "EiHealthClient":
                raise TypeError("client type error, support client type is EiHealthClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_drug_database_file(self, request):
        r"""数据库追加文件

        数据库追加文件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddDrugDatabaseFile
        :type request: :class:`huaweicloudsdkeihealth.v1.AddDrugDatabaseFileRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.AddDrugDatabaseFileResponse`
        """
        http_info = self._add_drug_database_file_http_info(request)
        return self._call_api(**http_info)

    def add_drug_database_file_invoker(self, request):
        http_info = self._add_drug_database_file_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_drug_database_file_http_info(cls, request):
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

    def batch_cancel_job(self, request):
        r"""批量取消作业

        批量取消作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCancelJob
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchCancelJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchCancelJobResponse`
        """
        http_info = self._batch_cancel_job_http_info(request)
        return self._call_api(**http_info)

    def batch_cancel_job_invoker(self, request):
        http_info = self._batch_cancel_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_cancel_job_http_info(cls, request):
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

    def batch_delete_data(self, request):
        r"""批量删除项目数据

        批量删除项目数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteData
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchDeleteDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchDeleteDataResponse`
        """
        http_info = self._batch_delete_data_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_data_invoker(self, request):
        http_info = self._batch_delete_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_data_http_info(cls, request):
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

    def batch_delete_job(self, request):
        r"""批量删除作业

        批量删除作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteJob
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchDeleteJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchDeleteJobResponse`
        """
        http_info = self._batch_delete_job_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_job_invoker(self, request):
        http_info = self._batch_delete_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_job_http_info(cls, request):
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

    def batch_delete_label(self, request):
        r"""批量删除标签

        批量删除标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteLabel
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchDeleteLabelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchDeleteLabelResponse`
        """
        http_info = self._batch_delete_label_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_label_invoker(self, request):
        http_info = self._batch_delete_label_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_label_http_info(cls, request):
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

    def batch_import_app(self, request):
        r"""导入应用

        批量导入应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchImportApp
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchImportAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchImportAppResponse`
        """
        http_info = self._batch_import_app_http_info(request)
        return self._call_api(**http_info)

    def batch_import_app_invoker(self, request):
        http_info = self._batch_import_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_import_app_http_info(cls, request):
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

    def batch_retry_job(self, request):
        r"""批量重试作业

        批量重试作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchRetryJob
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchRetryJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchRetryJobResponse`
        """
        http_info = self._batch_retry_job_http_info(request)
        return self._call_api(**http_info)

    def batch_retry_job_invoker(self, request):
        http_info = self._batch_retry_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_retry_job_http_info(cls, request):
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

    def cancel_data_job(self, request):
        r"""取消数据作业

        取消数据作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelDataJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CancelDataJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CancelDataJobResponse`
        """
        http_info = self._cancel_data_job_http_info(request)
        return self._call_api(**http_info)

    def cancel_data_job_invoker(self, request):
        http_info = self._cancel_data_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_data_job_http_info(cls, request):
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

    def cancel_drug_job(self, request):
        r"""取消药物作业

        取消药物作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelDrugJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CancelDrugJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CancelDrugJobResponse`
        """
        http_info = self._cancel_drug_job_http_info(request)
        return self._call_api(**http_info)

    def cancel_drug_job_invoker(self, request):
        http_info = self._cancel_drug_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_drug_job_http_info(cls, request):
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

    def cancel_job(self, request):
        r"""取消或强制停止作业调度

        取消或强制作业调度
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CancelJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CancelJobResponse`
        """
        http_info = self._cancel_job_http_info(request)
        return self._call_api(**http_info)

    def cancel_job_invoker(self, request):
        http_info = self._cancel_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_job_http_info(cls, request):
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

    def change_password(self, request):
        r"""修改密码

        修改密码
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangePassword
        :type request: :class:`huaweicloudsdkeihealth.v1.ChangePasswordRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ChangePasswordResponse`
        """
        http_info = self._change_password_http_info(request)
        return self._call_api(**http_info)

    def change_password_invoker(self, request):
        http_info = self._change_password_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_password_http_info(cls, request):
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

    def check_token_verification(self, request):
        r"""校验token

        校验token是否可访问当前环境
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckTokenVerification
        :type request: :class:`huaweicloudsdkeihealth.v1.CheckTokenVerificationRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CheckTokenVerificationResponse`
        """
        http_info = self._check_token_verification_http_info(request)
        return self._call_api(**http_info)

    def check_token_verification_invoker(self, request):
        http_info = self._check_token_verification_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_token_verification_http_info(cls, request):
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

    def copy_data(self, request):
        r"""复制项目数据

        复制项目数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CopyData
        :type request: :class:`huaweicloudsdkeihealth.v1.CopyDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CopyDataResponse`
        """
        http_info = self._copy_data_http_info(request)
        return self._call_api(**http_info)

    def copy_data_invoker(self, request):
        http_info = self._copy_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _copy_data_http_info(cls, request):
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

    def create_admet_job(self, request):
        r"""创建分子属性预测作业

        创建分子属性预测作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAdmetJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateAdmetJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateAdmetJobResponse`
        """
        http_info = self._create_admet_job_http_info(request)
        return self._call_api(**http_info)

    def create_admet_job_invoker(self, request):
        http_info = self._create_admet_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_admet_job_http_info(cls, request):
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

    def create_app(self, request):
        r"""创建应用

        创建应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateApp
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateAppResponse`
        """
        http_info = self._create_app_http_info(request)
        return self._call_api(**http_info)

    def create_app_invoker(self, request):
        http_info = self._create_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_app_http_info(cls, request):
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

    def create_asset_resource(self, request):
        r"""创建计费资产资源

        创建计费资产资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAssetResource
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateAssetResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateAssetResourceResponse`
        """
        http_info = self._create_asset_resource_http_info(request)
        return self._call_api(**http_info)

    def create_asset_resource_invoker(self, request):
        http_info = self._create_asset_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_asset_resource_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/assets/asset-resources",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAssetResourceResponse"
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

    def create_cluster_job(self, request):
        r"""创建分子聚类作业

        创建分子聚类作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateClusterJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateClusterJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateClusterJobResponse`
        """
        http_info = self._create_cluster_job_http_info(request)
        return self._call_api(**http_info)

    def create_cluster_job_invoker(self, request):
        http_info = self._create_cluster_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_cluster_job_http_info(cls, request):
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

    def create_clustering_job(self, request):
        r"""创建聚类分析作业

        创建聚类分析作业。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateClusteringJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateClusteringJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateClusteringJobResponse`
        """
        http_info = self._create_clustering_job_http_info(request)
        return self._call_api(**http_info)

    def create_clustering_job_invoker(self, request):
        http_info = self._create_clustering_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_clustering_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/clustering",
            "request_type": request.__class__.__name__,
            "response_type": "CreateClusteringJobResponse"
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

    def create_code(self, request):
        r"""发送验证码

        发送验证码
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCode
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateCodeRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateCodeResponse`
        """
        http_info = self._create_code_http_info(request)
        return self._call_api(**http_info)

    def create_code_invoker(self, request):
        http_info = self._create_code_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_code_http_info(cls, request):
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

    def create_computing_cluster(self, request):
        r"""绑定计算集群

        绑定计算集群。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateComputingCluster
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateComputingClusterRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateComputingClusterResponse`
        """
        http_info = self._create_computing_cluster_http_info(request)
        return self._call_api(**http_info)

    def create_computing_cluster_invoker(self, request):
        http_info = self._create_computing_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_computing_cluster_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/system/computing-clusters",
            "request_type": request.__class__.__name__,
            "response_type": "CreateComputingClusterResponse"
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

    def create_data(self, request):
        r"""创建文件夹

        创建文件夹
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateData
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDataResponse`
        """
        http_info = self._create_data_http_info(request)
        return self._call_api(**http_info)

    def create_data_invoker(self, request):
        http_info = self._create_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_data_http_info(cls, request):
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

    def create_docking_job(self, request):
        r"""创建分子对接作业

        创建分子对接作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDockingJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDockingJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDockingJobResponse`
        """
        http_info = self._create_docking_job_http_info(request)
        return self._call_api(**http_info)

    def create_docking_job_invoker(self, request):
        http_info = self._create_docking_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_docking_job_http_info(cls, request):
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

    def create_drug_database(self, request):
        r"""创建数据库

        创建数据库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDrugDatabase
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDrugDatabaseRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDrugDatabaseResponse`
        """
        http_info = self._create_drug_database_http_info(request)
        return self._call_api(**http_info)

    def create_drug_database_invoker(self, request):
        http_info = self._create_drug_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_drug_database_http_info(cls, request):
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

    def create_drug_model(self, request):
        r"""创建模型

        创建模型
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDrugModel
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDrugModelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDrugModelResponse`
        """
        http_info = self._create_drug_model_http_info(request)
        return self._call_api(**http_info)

    def create_drug_model_invoker(self, request):
        http_info = self._create_drug_model_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_drug_model_http_info(cls, request):
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

    def create_drug_model_resource(self, request):
        r"""创建盘古药物分子大模型

        创建盘古药物分子大模型。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDrugModelResource
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDrugModelResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDrugModelResourceResponse`
        """
        http_info = self._create_drug_model_resource_http_info(request)
        return self._call_api(**http_info)

    def create_drug_model_resource_invoker(self, request):
        http_info = self._create_drug_model_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_drug_model_resource_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/drug/drug-model-resources",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDrugModelResourceResponse"
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

    def create_favorite(self, request):
        r"""添加收藏

        添加收藏。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFavorite
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateFavoriteRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateFavoriteResponse`
        """
        http_info = self._create_favorite_http_info(request)
        return self._call_api(**http_info)

    def create_favorite_invoker(self, request):
        http_info = self._create_favorite_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_favorite_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/favorites",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFavoriteResponse"
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

    def create_fep_job(self, request):
        r"""创建自由能微扰作业

        创建自由能微扰作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFepJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateFepJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateFepJobResponse`
        """
        http_info = self._create_fep_job_http_info(request)
        return self._call_api(**http_info)

    def create_fep_job_invoker(self, request):
        http_info = self._create_fep_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_fep_job_http_info(cls, request):
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

    def create_gen_job(self, request):
        r"""创建分子生成作业

        创建分子生成作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateGenJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateGenJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateGenJobResponse`
        """
        http_info = self._create_gen_job_http_info(request)
        return self._call_api(**http_info)

    def create_gen_job_invoker(self, request):
        http_info = self._create_gen_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_gen_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/generation",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGenJobResponse"
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

    def create_image(self, request):
        r"""创建镜像

        创建镜像
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateImage
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateImageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateImageResponse`
        """
        http_info = self._create_image_http_info(request)
        return self._call_api(**http_info)

    def create_image_invoker(self, request):
        http_info = self._create_image_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_image_http_info(cls, request):
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

    def create_label(self, request):
        r"""创建标签

        创建标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateLabel
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateLabelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateLabelResponse`
        """
        http_info = self._create_label_http_info(request)
        return self._call_api(**http_info)

    def create_label_invoker(self, request):
        http_info = self._create_label_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_label_http_info(cls, request):
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

    def create_message_additions(self, request):
        r"""绑定问答额外信息

        绑定问答额外信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateMessageAdditions
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateMessageAdditionsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateMessageAdditionsResponse`
        """
        http_info = self._create_message_additions_http_info(request)
        return self._call_api(**http_info)

    def create_message_additions_invoker(self, request):
        http_info = self._create_message_additions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_message_additions_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/chats/{chat_id}/messages/{message_id}/additions",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMessageAdditionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'chat_id' in local_var_params:
            path_params['chat_id'] = local_var_params['chat_id']
        if 'message_id' in local_var_params:
            path_params['message_id'] = local_var_params['message_id']

        query_params = []

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

    def create_mol_batch_download_task(self, request):
        r"""创建分子或分子复合物批量下载任务

        创建分子或分子复合物批量下载任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateMolBatchDownloadTask
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateMolBatchDownloadTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateMolBatchDownloadTaskResponse`
        """
        http_info = self._create_mol_batch_download_task_http_info(request)
        return self._call_api(**http_info)

    def create_mol_batch_download_task_invoker(self, request):
        http_info = self._create_mol_batch_download_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_mol_batch_download_task_http_info(cls, request):
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

    def create_mol_docking_job(self, request):
        r"""单分子预对接

        单分子预对接。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateMolDockingJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateMolDockingJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateMolDockingJobResponse`
        """
        http_info = self._create_mol_docking_job_http_info(request)
        return self._call_api(**http_info)

    def create_mol_docking_job_invoker(self, request):
        http_info = self._create_mol_docking_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_mol_docking_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/mol-docking",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMolDockingJobResponse"
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

    def create_optm_job(self, request):
        r"""创建分子优化作业

        创建分子优化作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateOptmJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateOptmJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateOptmJobResponse`
        """
        http_info = self._create_optm_job_http_info(request)
        return self._call_api(**http_info)

    def create_optm_job_invoker(self, request):
        http_info = self._create_optm_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_optm_job_http_info(cls, request):
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

    def create_performance_resource(self, request):
        r"""购买性能加速资源

        购买性能加速资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePerformanceResource
        :type request: :class:`huaweicloudsdkeihealth.v1.CreatePerformanceResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreatePerformanceResourceResponse`
        """
        http_info = self._create_performance_resource_http_info(request)
        return self._call_api(**http_info)

    def create_performance_resource_invoker(self, request):
        http_info = self._create_performance_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_performance_resource_http_info(cls, request):
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

    def create_pocket_detection_job(self, request):
        r"""创建靶点口袋发现作业

        创建靶点口袋发现作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePocketDetectionJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreatePocketDetectionJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreatePocketDetectionJobResponse`
        """
        http_info = self._create_pocket_detection_job_http_info(request)
        return self._call_api(**http_info)

    def create_pocket_detection_job_invoker(self, request):
        http_info = self._create_pocket_detection_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_pocket_detection_job_http_info(cls, request):
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

    def create_pocket_mol_design_job(self, request):
        r"""创建靶点口袋分子设计作业

        创建靶点口袋分子设计作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePocketMolDesignJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreatePocketMolDesignJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreatePocketMolDesignJobResponse`
        """
        http_info = self._create_pocket_mol_design_job_http_info(request)
        return self._call_api(**http_info)

    def create_pocket_mol_design_job_invoker(self, request):
        http_info = self._create_pocket_mol_design_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_pocket_mol_design_job_http_info(cls, request):
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

    def create_project(self, request):
        r"""创建项目

        创建项目
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateProject
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateProjectRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateProjectResponse`
        """
        http_info = self._create_project_http_info(request)
        return self._call_api(**http_info)

    def create_project_invoker(self, request):
        http_info = self._create_project_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_project_http_info(cls, request):
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

    def create_search_job(self, request):
        r"""创建分子搜索作业

        创建分子搜索作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSearchJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateSearchJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateSearchJobResponse`
        """
        http_info = self._create_search_job_http_info(request)
        return self._call_api(**http_info)

    def create_search_job_invoker(self, request):
        http_info = self._create_search_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_search_job_http_info(cls, request):
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

    def create_target_opt_job(self, request):
        r"""创建靶点优化作业

        创建靶点优化作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTargetOptJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateTargetOptJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateTargetOptJobResponse`
        """
        http_info = self._create_target_opt_job_http_info(request)
        return self._call_api(**http_info)

    def create_target_opt_job_invoker(self, request):
        http_info = self._create_target_opt_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_target_opt_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/target-optimization",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTargetOptJobResponse"
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

    def create_user(self, request):
        r"""创建用户

        创建用户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateUser
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateUserRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateUserResponse`
        """
        http_info = self._create_user_http_info(request)
        return self._call_api(**http_info)

    def create_user_invoker(self, request):
        http_info = self._create_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_user_http_info(cls, request):
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

    def create_workflow(self, request):
        r"""创建流程

        创建流程
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateWorkflowResponse`
        """
        http_info = self._create_workflow_http_info(request)
        return self._call_api(**http_info)

    def create_workflow_invoker(self, request):
        http_info = self._create_workflow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_workflow_http_info(cls, request):
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

    def delete_app(self, request):
        r"""删除应用

        删除应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApp
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteAppResponse`
        """
        http_info = self._delete_app_http_info(request)
        return self._call_api(**http_info)

    def delete_app_invoker(self, request):
        http_info = self._delete_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_app_http_info(cls, request):
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

    def delete_asset_resource(self, request):
        r"""退订计费资产资源

        退订计费资产资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAssetResource
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteAssetResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteAssetResourceResponse`
        """
        http_info = self._delete_asset_resource_http_info(request)
        return self._call_api(**http_info)

    def delete_asset_resource_invoker(self, request):
        http_info = self._delete_asset_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_asset_resource_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/assets/asset-resources/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAssetResourceResponse"
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

    def delete_chat(self, request):
        r"""删除对话

        删除对话。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteChat
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteChatRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteChatResponse`
        """
        http_info = self._delete_chat_http_info(request)
        return self._call_api(**http_info)

    def delete_chat_invoker(self, request):
        http_info = self._delete_chat_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_chat_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/chats/{chat_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteChatResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'chat_id' in local_var_params:
            path_params['chat_id'] = local_var_params['chat_id']

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

    def delete_computing_cluster(self, request):
        r"""解绑计算集群

        解绑计算集群。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteComputingCluster
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteComputingClusterRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteComputingClusterResponse`
        """
        http_info = self._delete_computing_cluster_http_info(request)
        return self._call_api(**http_info)

    def delete_computing_cluster_invoker(self, request):
        http_info = self._delete_computing_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_computing_cluster_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/system/computing-clusters/{cluster_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteComputingClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def delete_data_job(self, request):
        r"""删除数据作业

        删除数据作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDataJob
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteDataJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteDataJobResponse`
        """
        http_info = self._delete_data_job_http_info(request)
        return self._call_api(**http_info)

    def delete_data_job_invoker(self, request):
        http_info = self._delete_data_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_data_job_http_info(cls, request):
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

    def delete_drug_database(self, request):
        r"""删除数据库

        删除数据库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDrugDatabase
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteDrugDatabaseRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteDrugDatabaseResponse`
        """
        http_info = self._delete_drug_database_http_info(request)
        return self._call_api(**http_info)

    def delete_drug_database_invoker(self, request):
        http_info = self._delete_drug_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_drug_database_http_info(cls, request):
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

    def delete_drug_job(self, request):
        r"""删除药物作业

        删除药物作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDrugJob
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteDrugJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteDrugJobResponse`
        """
        http_info = self._delete_drug_job_http_info(request)
        return self._call_api(**http_info)

    def delete_drug_job_invoker(self, request):
        http_info = self._delete_drug_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_drug_job_http_info(cls, request):
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

    def delete_drug_model(self, request):
        r"""删除模型

        删除模型
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDrugModel
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteDrugModelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteDrugModelResponse`
        """
        http_info = self._delete_drug_model_http_info(request)
        return self._call_api(**http_info)

    def delete_drug_model_invoker(self, request):
        http_info = self._delete_drug_model_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_drug_model_http_info(cls, request):
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

    def delete_drug_model_resource(self, request):
        r"""退订盘古药物分子大模型

        退订盘古药物分子大模型。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDrugModelResource
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteDrugModelResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteDrugModelResourceResponse`
        """
        http_info = self._delete_drug_model_resource_http_info(request)
        return self._call_api(**http_info)

    def delete_drug_model_resource_invoker(self, request):
        http_info = self._delete_drug_model_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_drug_model_resource_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/drug/drug-model-resources/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDrugModelResourceResponse"
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

    def delete_favorite(self, request):
        r"""取消收藏

        取消收藏。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteFavorite
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteFavoriteRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteFavoriteResponse`
        """
        http_info = self._delete_favorite_http_info(request)
        return self._call_api(**http_info)

    def delete_favorite_invoker(self, request):
        http_info = self._delete_favorite_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_favorite_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/favorites/{favorite_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteFavoriteResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'favorite_id' in local_var_params:
            path_params['favorite_id'] = local_var_params['favorite_id']

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

    def delete_image(self, request):
        r"""删除镜像仓库

        删除镜像仓库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteImage
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteImageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteImageResponse`
        """
        http_info = self._delete_image_http_info(request)
        return self._call_api(**http_info)

    def delete_image_invoker(self, request):
        http_info = self._delete_image_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_image_http_info(cls, request):
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

    def delete_job(self, request):
        r"""删除作业

        删除作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteJob
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteJobResponse`
        """
        http_info = self._delete_job_http_info(request)
        return self._call_api(**http_info)

    def delete_job_invoker(self, request):
        http_info = self._delete_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_job_http_info(cls, request):
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

    def delete_label(self, request):
        r"""删除标签

        删除标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteLabel
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteLabelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteLabelResponse`
        """
        http_info = self._delete_label_http_info(request)
        return self._call_api(**http_info)

    def delete_label_invoker(self, request):
        http_info = self._delete_label_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_label_http_info(cls, request):
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

    def delete_member(self, request):
        r"""移除项目成员

        移除项目成员
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteMember
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteMemberRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteMemberResponse`
        """
        http_info = self._delete_member_http_info(request)
        return self._call_api(**http_info)

    def delete_member_invoker(self, request):
        http_info = self._delete_member_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_member_http_info(cls, request):
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

    def delete_performance_resource(self, request):
        r"""删除性能加速资源

        删除性能加速资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePerformanceResource
        :type request: :class:`huaweicloudsdkeihealth.v1.DeletePerformanceResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeletePerformanceResourceResponse`
        """
        http_info = self._delete_performance_resource_http_info(request)
        return self._call_api(**http_info)

    def delete_performance_resource_invoker(self, request):
        http_info = self._delete_performance_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_performance_resource_http_info(cls, request):
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

    def delete_project(self, request):
        r"""删除项目

        删除项目
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteProject
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteProjectRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteProjectResponse`
        """
        http_info = self._delete_project_http_info(request)
        return self._call_api(**http_info)

    def delete_project_invoker(self, request):
        http_info = self._delete_project_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_project_http_info(cls, request):
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

    def delete_tag(self, request):
        r"""删除指定镜像tag

        删除指定镜像tag
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTag
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteTagRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteTagResponse`
        """
        http_info = self._delete_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_tag_invoker(self, request):
        http_info = self._delete_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_tag_http_info(cls, request):
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

    def delete_user(self, request):
        r"""删除用户

        删除用户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteUser
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteUserRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteUserResponse`
        """
        http_info = self._delete_user_http_info(request)
        return self._call_api(**http_info)

    def delete_user_invoker(self, request):
        http_info = self._delete_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_user_http_info(cls, request):
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

    def delete_workflow(self, request):
        r"""删除流程

        删除流程
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteWorkflowResponse`
        """
        http_info = self._delete_workflow_http_info(request)
        return self._call_api(**http_info)

    def delete_workflow_invoker(self, request):
        http_info = self._delete_workflow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_workflow_http_info(cls, request):
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

    def execute_job(self, request):
        r"""启动作业

        启动作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ExecuteJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ExecuteJobResponse`
        """
        http_info = self._execute_job_http_info(request)
        return self._call_api(**http_info)

    def execute_job_invoker(self, request):
        http_info = self._execute_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_job_http_info(cls, request):
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

    def generate_complex_combine(self, request):
        r"""将传入的蛋白和小分子拼接成复合物结构

        将传入的蛋白和小分子拼接成复合物结构
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GenerateComplexCombine
        :type request: :class:`huaweicloudsdkeihealth.v1.GenerateComplexCombineRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.GenerateComplexCombineResponse`
        """
        http_info = self._generate_complex_combine_http_info(request)
        return self._call_api(**http_info)

    def generate_complex_combine_invoker(self, request):
        http_info = self._generate_complex_combine_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _generate_complex_combine_http_info(cls, request):
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

    def generate_pocket_file(self, request):
        r"""根据center、size、padding参数生成可渲染的口袋文件内容

        根据center、size、padding参数生成可渲染的口袋文件内容
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GeneratePocketFile
        :type request: :class:`huaweicloudsdkeihealth.v1.GeneratePocketFileRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.GeneratePocketFileResponse`
        """
        http_info = self._generate_pocket_file_http_info(request)
        return self._call_api(**http_info)

    def generate_pocket_file_invoker(self, request):
        http_info = self._generate_pocket_file_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _generate_pocket_file_http_info(cls, request):
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

    def generate_surface_points(self, request):
        r"""根据表面离散点坐标集生成可渲染的文件内容

        根据表面离散点坐标集生成可渲染的文件内容
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GenerateSurfacePoints
        :type request: :class:`huaweicloudsdkeihealth.v1.GenerateSurfacePointsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.GenerateSurfacePointsResponse`
        """
        http_info = self._generate_surface_points_http_info(request)
        return self._call_api(**http_info)

    def generate_surface_points_invoker(self, request):
        http_info = self._generate_surface_points_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _generate_surface_points_http_info(cls, request):
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

    def import_data(self, request):
        r"""导入项目数据

        导入项目数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportData
        :type request: :class:`huaweicloudsdkeihealth.v1.ImportDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImportDataResponse`
        """
        http_info = self._import_data_http_info(request)
        return self._call_api(**http_info)

    def import_data_invoker(self, request):
        http_info = self._import_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_data_http_info(cls, request):
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

    def import_image(self, request):
        r"""导入镜像

        导入镜像
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportImage
        :type request: :class:`huaweicloudsdkeihealth.v1.ImportImageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImportImageResponse`
        """
        http_info = self._import_image_http_info(request)
        return self._call_api(**http_info)

    def import_image_invoker(self, request):
        http_info = self._import_image_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_image_http_info(cls, request):
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

    def import_network_data(self, request):
        r"""导入网上数据

        导入网上数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportNetworkData
        :type request: :class:`huaweicloudsdkeihealth.v1.ImportNetworkDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImportNetworkDataResponse`
        """
        http_info = self._import_network_data_http_info(request)
        return self._call_api(**http_info)

    def import_network_data_invoker(self, request):
        http_info = self._import_network_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_network_data_http_info(cls, request):
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

    def import_user(self, request):
        r"""导入用户

        导入用户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportUser
        :type request: :class:`huaweicloudsdkeihealth.v1.ImportUserRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImportUserResponse`
        """
        http_info = self._import_user_http_info(request)
        return self._call_api(**http_info)

    def import_user_invoker(self, request):
        http_info = self._import_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_user_http_info(cls, request):
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

    def import_workflow(self, request):
        r"""导入流程

        导入流程
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.ImportWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImportWorkflowResponse`
        """
        http_info = self._import_workflow_http_info(request)
        return self._call_api(**http_info)

    def import_workflow_invoker(self, request):
        http_info = self._import_workflow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_workflow_http_info(cls, request):
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

    def initialize_platform(self, request):
        r"""初始化平台

        初始化平台。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for InitializePlatform
        :type request: :class:`huaweicloudsdkeihealth.v1.InitializePlatformRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.InitializePlatformResponse`
        """
        http_info = self._initialize_platform_http_info(request)
        return self._call_api(**http_info)

    def initialize_platform_invoker(self, request):
        http_info = self._initialize_platform_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _initialize_platform_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/system/init",
            "request_type": request.__class__.__name__,
            "response_type": "InitializePlatformResponse"
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

    def list_app(self, request):
        r"""获取应用列表

        获取应用列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApp
        :type request: :class:`huaweicloudsdkeihealth.v1.ListAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListAppResponse`
        """
        http_info = self._list_app_http_info(request)
        return self._call_api(**http_info)

    def list_app_invoker(self, request):
        http_info = self._list_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_app_http_info(cls, request):
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

    def list_asset(self, request):
        r"""获取资产列表

        获取资产列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAsset
        :type request: :class:`huaweicloudsdkeihealth.v1.ListAssetRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListAssetResponse`
        """
        http_info = self._list_asset_http_info(request)
        return self._call_api(**http_info)

    def list_asset_invoker(self, request):
        http_info = self._list_asset_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_asset_http_info(cls, request):
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

    def list_asset_resource(self, request):
        r"""查询计费资产资源

        查询计费资产资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAssetResource
        :type request: :class:`huaweicloudsdkeihealth.v1.ListAssetResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListAssetResourceResponse`
        """
        http_info = self._list_asset_resource_http_info(request)
        return self._call_api(**http_info)

    def list_asset_resource_invoker(self, request):
        http_info = self._list_asset_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_asset_resource_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/assets/asset-resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListAssetResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'spec_code' in local_var_params:
            query_params.append(('spec_code', local_var_params['spec_code']))
        if 'status_list' in local_var_params:
            query_params.append(('status_list', local_var_params['status_list']))
            collection_formats['status_list'] = 'csv'
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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

    def list_base_model(self, request):
        r"""获取基模型列表

        获取基模型列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBaseModel
        :type request: :class:`huaweicloudsdkeihealth.v1.ListBaseModelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListBaseModelResponse`
        """
        http_info = self._list_base_model_http_info(request)
        return self._call_api(**http_info)

    def list_base_model_invoker(self, request):
        http_info = self._list_base_model_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_base_model_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/base-models",
            "request_type": request.__class__.__name__,
            "response_type": "ListBaseModelResponse"
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

    def list_bucket(self, request):
        r"""获取桶列表

        获取桶列表(包含当前项目桶和引用项目桶)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBucket
        :type request: :class:`huaweicloudsdkeihealth.v1.ListBucketRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListBucketResponse`
        """
        http_info = self._list_bucket_http_info(request)
        return self._call_api(**http_info)

    def list_bucket_invoker(self, request):
        http_info = self._list_bucket_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_bucket_http_info(cls, request):
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

    def list_cce_cluster(self, request):
        r"""获取CCE集群列表

        获取CCE集群列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCceCluster
        :type request: :class:`huaweicloudsdkeihealth.v1.ListCceClusterRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListCceClusterResponse`
        """
        http_info = self._list_cce_cluster_http_info(request)
        return self._call_api(**http_info)

    def list_cce_cluster_invoker(self, request):
        http_info = self._list_cce_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_cce_cluster_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/cce-clusters",
            "request_type": request.__class__.__name__,
            "response_type": "ListCceClusterResponse"
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

    def list_chat(self, request):
        r"""获取对话列表

        获取对话列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListChat
        :type request: :class:`huaweicloudsdkeihealth.v1.ListChatRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListChatResponse`
        """
        http_info = self._list_chat_http_info(request)
        return self._call_api(**http_info)

    def list_chat_invoker(self, request):
        http_info = self._list_chat_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_chat_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/chats",
            "request_type": request.__class__.__name__,
            "response_type": "ListChatResponse"
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
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'title' in local_var_params:
            query_params.append(('title', local_var_params['title']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_cluster_all_node_label(self, request):
        r"""获取节点标签集

        获取节点标签集
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClusterAllNodeLabel
        :type request: :class:`huaweicloudsdkeihealth.v1.ListClusterAllNodeLabelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListClusterAllNodeLabelResponse`
        """
        http_info = self._list_cluster_all_node_label_http_info(request)
        return self._call_api(**http_info)

    def list_cluster_all_node_label_invoker(self, request):
        http_info = self._list_cluster_all_node_label_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_cluster_all_node_label_http_info(cls, request):
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

    def list_cluster_install_step(self, request):
        r"""查询指定集群安装步骤列表

        查询指定集群安装步骤列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClusterInstallStep
        :type request: :class:`huaweicloudsdkeihealth.v1.ListClusterInstallStepRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListClusterInstallStepResponse`
        """
        http_info = self._list_cluster_install_step_http_info(request)
        return self._call_api(**http_info)

    def list_cluster_install_step_invoker(self, request):
        http_info = self._list_cluster_install_step_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_cluster_install_step_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/computing-clusters/{cluster_id}/steps",
            "request_type": request.__class__.__name__,
            "response_type": "ListClusterInstallStepResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def list_computing_cluster(self, request):
        r"""获取计算集群列表

        获取计算集群列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListComputingCluster
        :type request: :class:`huaweicloudsdkeihealth.v1.ListComputingClusterRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListComputingClusterResponse`
        """
        http_info = self._list_computing_cluster_http_info(request)
        return self._call_api(**http_info)

    def list_computing_cluster_invoker(self, request):
        http_info = self._list_computing_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_computing_cluster_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/computing-clusters",
            "request_type": request.__class__.__name__,
            "response_type": "ListComputingClusterResponse"
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

    def list_data(self, request):
        r"""查询数据列表

        查询指定目录下的数据列表，如果不指定默认查询根目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListData
        :type request: :class:`huaweicloudsdkeihealth.v1.ListDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListDataResponse`
        """
        http_info = self._list_data_http_info(request)
        return self._call_api(**http_info)

    def list_data_invoker(self, request):
        http_info = self._list_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_data_http_info(cls, request):
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

    def list_data_job(self, request):
        r"""获取数据作业列表

        获取数据作业列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDataJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ListDataJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListDataJobResponse`
        """
        http_info = self._list_data_job_http_info(request)
        return self._call_api(**http_info)

    def list_data_job_invoker(self, request):
        http_info = self._list_data_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_data_job_http_info(cls, request):
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

    def list_drug_database(self, request):
        r"""获取数据库列表

        获取数据库列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDrugDatabase
        :type request: :class:`huaweicloudsdkeihealth.v1.ListDrugDatabaseRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListDrugDatabaseResponse`
        """
        http_info = self._list_drug_database_http_info(request)
        return self._call_api(**http_info)

    def list_drug_database_invoker(self, request):
        http_info = self._list_drug_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_drug_database_http_info(cls, request):
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

    def list_drug_job(self, request):
        r"""获取药物作业列表

        获取药物作业列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDrugJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ListDrugJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListDrugJobResponse`
        """
        http_info = self._list_drug_job_http_info(request)
        return self._call_api(**http_info)

    def list_drug_job_invoker(self, request):
        http_info = self._list_drug_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_drug_job_http_info(cls, request):
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

    def list_drug_model(self, request):
        r"""获取模型列表

        获取模型列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDrugModel
        :type request: :class:`huaweicloudsdkeihealth.v1.ListDrugModelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListDrugModelResponse`
        """
        http_info = self._list_drug_model_http_info(request)
        return self._call_api(**http_info)

    def list_drug_model_invoker(self, request):
        http_info = self._list_drug_model_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_drug_model_http_info(cls, request):
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
        if 'base_model_list' in local_var_params:
            query_params.append(('base_model_list', local_var_params['base_model_list']))
            collection_formats['base_model_list'] = 'csv'

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_drug_model_resource1(self, request):
        r"""查询盘古药物分子大模型

        查询盘古药物分子大模型。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDrugModelResource1
        :type request: :class:`huaweicloudsdkeihealth.v1.ListDrugModelResource1Request`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListDrugModelResource1Response`
        """
        http_info = self._list_drug_model_resource1_http_info(request)
        return self._call_api(**http_info)

    def list_drug_model_resource1_invoker(self, request):
        http_info = self._list_drug_model_resource1_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_drug_model_resource1_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/drug/drug-model-resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListDrugModelResource1Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'spec_code' in local_var_params:
            query_params.append(('spec_code', local_var_params['spec_code']))
        if 'status_list' in local_var_params:
            query_params.append(('status_list', local_var_params['status_list']))
            collection_formats['status_list'] = 'csv'
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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

    def list_favorite(self, request):
        r"""获取收藏夹列表

        获取收藏夹列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFavorite
        :type request: :class:`huaweicloudsdkeihealth.v1.ListFavoriteRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListFavoriteResponse`
        """
        http_info = self._list_favorite_http_info(request)
        return self._call_api(**http_info)

    def list_favorite_invoker(self, request):
        http_info = self._list_favorite_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_favorite_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/favorites",
            "request_type": request.__class__.__name__,
            "response_type": "ListFavoriteResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'user_name_list' in local_var_params:
            query_params.append(('user_name_list', local_var_params['user_name_list']))
            collection_formats['user_name_list'] = 'csv'
        if 'resource_type_list' in local_var_params:
            query_params.append(('resource_type_list', local_var_params['resource_type_list']))
            collection_formats['resource_type_list'] = 'csv'
        if 'type_list' in local_var_params:
            query_params.append(('type_list', local_var_params['type_list']))
            collection_formats['type_list'] = 'csv'
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'key_word' in local_var_params:
            query_params.append(('key_word', local_var_params['key_word']))
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

    def list_global_workflow_statistic(self, request):
        r"""统计全局流程、作业信息

        统计全局流程、作业信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGlobalWorkflowStatistic
        :type request: :class:`huaweicloudsdkeihealth.v1.ListGlobalWorkflowStatisticRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListGlobalWorkflowStatisticResponse`
        """
        http_info = self._list_global_workflow_statistic_http_info(request)
        return self._call_api(**http_info)

    def list_global_workflow_statistic_invoker(self, request):
        http_info = self._list_global_workflow_statistic_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_global_workflow_statistic_http_info(cls, request):
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

    def list_iam_group_users(self, request):
        r"""查询IAM用户组的用户列表

        查询IAM用户组的用户列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIamGroupUsers
        :type request: :class:`huaweicloudsdkeihealth.v1.ListIamGroupUsersRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListIamGroupUsersResponse`
        """
        http_info = self._list_iam_group_users_http_info(request)
        return self._call_api(**http_info)

    def list_iam_group_users_invoker(self, request):
        http_info = self._list_iam_group_users_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_iam_group_users_http_info(cls, request):
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

    def list_iam_groups(self, request):
        r"""查询IAM用户组列表

        查询IAM用户组列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIamGroups
        :type request: :class:`huaweicloudsdkeihealth.v1.ListIamGroupsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListIamGroupsResponse`
        """
        http_info = self._list_iam_groups_http_info(request)
        return self._call_api(**http_info)

    def list_iam_groups_invoker(self, request):
        http_info = self._list_iam_groups_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_iam_groups_http_info(cls, request):
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

    def list_iam_users(self, request):
        r"""查询IAM用户列表

        查询IAM用户列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIamUsers
        :type request: :class:`huaweicloudsdkeihealth.v1.ListIamUsersRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListIamUsersResponse`
        """
        http_info = self._list_iam_users_http_info(request)
        return self._call_api(**http_info)

    def list_iam_users_invoker(self, request):
        http_info = self._list_iam_users_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_iam_users_http_info(cls, request):
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

    def list_image(self, request):
        r"""获取镜像列表

        获取镜像列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListImage
        :type request: :class:`huaweicloudsdkeihealth.v1.ListImageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListImageResponse`
        """
        http_info = self._list_image_http_info(request)
        return self._call_api(**http_info)

    def list_image_invoker(self, request):
        http_info = self._list_image_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_image_http_info(cls, request):
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

    def list_image_tag(self, request):
        r"""获取指定镜像的tag列表

        获取指定镜像的tag列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListImageTag
        :type request: :class:`huaweicloudsdkeihealth.v1.ListImageTagRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListImageTagResponse`
        """
        http_info = self._list_image_tag_http_info(request)
        return self._call_api(**http_info)

    def list_image_tag_invoker(self, request):
        http_info = self._list_image_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_image_tag_http_info(cls, request):
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

    def list_job(self, request):
        r"""获取作业列表

        获取作业列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ListJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListJobResponse`
        """
        http_info = self._list_job_http_info(request)
        return self._call_api(**http_info)

    def list_job_invoker(self, request):
        http_info = self._list_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_job_http_info(cls, request):
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

    def list_label(self, request):
        r"""获取标签列表

        获取标签列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLabel
        :type request: :class:`huaweicloudsdkeihealth.v1.ListLabelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListLabelResponse`
        """
        http_info = self._list_label_http_info(request)
        return self._call_api(**http_info)

    def list_label_invoker(self, request):
        http_info = self._list_label_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_label_http_info(cls, request):
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

    def list_mfa(self, request):
        r"""获取可用的认证方法

        获取可用的认证方法
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMfa
        :type request: :class:`huaweicloudsdkeihealth.v1.ListMfaRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListMfaResponse`
        """
        http_info = self._list_mfa_http_info(request)
        return self._call_api(**http_info)

    def list_mfa_invoker(self, request):
        http_info = self._list_mfa_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_mfa_http_info(cls, request):
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

    def list_performance_resource_stat(self, request):
        r"""获取性能加速资源上统计信息

        获取性能加速资源上统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPerformanceResourceStat
        :type request: :class:`huaweicloudsdkeihealth.v1.ListPerformanceResourceStatRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListPerformanceResourceStatResponse`
        """
        http_info = self._list_performance_resource_stat_http_info(request)
        return self._call_api(**http_info)

    def list_performance_resource_stat_invoker(self, request):
        http_info = self._list_performance_resource_stat_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_performance_resource_stat_http_info(cls, request):
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

    def list_performance_resources(self, request):
        r"""查询性能加速资源

        查询性能加速资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPerformanceResources
        :type request: :class:`huaweicloudsdkeihealth.v1.ListPerformanceResourcesRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListPerformanceResourcesResponse`
        """
        http_info = self._list_performance_resources_http_info(request)
        return self._call_api(**http_info)

    def list_performance_resources_invoker(self, request):
        http_info = self._list_performance_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_performance_resources_http_info(cls, request):
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

    def list_project(self, request):
        r"""获取空间列表

        获取空间列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProject
        :type request: :class:`huaweicloudsdkeihealth.v1.ListProjectRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListProjectResponse`
        """
        http_info = self._list_project_http_info(request)
        return self._call_api(**http_info)

    def list_project_invoker(self, request):
        http_info = self._list_project_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_project_http_info(cls, request):
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

    def list_project_statistics(self, request):
        r"""获取当前用户所属空间资源统计信息

        获取当前用户所属空间资源统计信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectStatistics
        :type request: :class:`huaweicloudsdkeihealth.v1.ListProjectStatisticsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListProjectStatisticsResponse`
        """
        http_info = self._list_project_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_project_statistics_invoker(self, request):
        http_info = self._list_project_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_project_statistics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectStatisticsResponse"
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

    def list_property(self, request):
        r"""获取属性值列表

        获取属性值列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProperty
        :type request: :class:`huaweicloudsdkeihealth.v1.ListPropertyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListPropertyResponse`
        """
        http_info = self._list_property_http_info(request)
        return self._call_api(**http_info)

    def list_property_invoker(self, request):
        http_info = self._list_property_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_property_http_info(cls, request):
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

    def list_quota(self, request):
        r"""获取当前系统配额及资源使用情况

        获取当前系统配额及资源使用情况
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQuota
        :type request: :class:`huaweicloudsdkeihealth.v1.ListQuotaRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListQuotaResponse`
        """
        http_info = self._list_quota_http_info(request)
        return self._call_api(**http_info)

    def list_quota_invoker(self, request):
        http_info = self._list_quota_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_quota_http_info(cls, request):
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

    def list_sfs_turbos(self, request):
        r"""获取sfs-turbo资源列表

        获取sfs-turbo资源列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSfsTurbos
        :type request: :class:`huaweicloudsdkeihealth.v1.ListSfsTurbosRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListSfsTurbosResponse`
        """
        http_info = self._list_sfs_turbos_http_info(request)
        return self._call_api(**http_info)

    def list_sfs_turbos_invoker(self, request):
        http_info = self._list_sfs_turbos_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sfs_turbos_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/sfs-turbos",
            "request_type": request.__class__.__name__,
            "response_type": "ListSfsTurbosResponse"
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

    def list_user(self, request):
        r"""获取用户列表

        获取用户列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUser
        :type request: :class:`huaweicloudsdkeihealth.v1.ListUserRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListUserResponse`
        """
        http_info = self._list_user_http_info(request)
        return self._call_api(**http_info)

    def list_user_invoker(self, request):
        http_info = self._list_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_user_http_info(cls, request):
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

    def list_user_app(self, request):
        r"""获取用户所属空间的应用列表

        获取用户所属空间的应用列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUserApp
        :type request: :class:`huaweicloudsdkeihealth.v1.ListUserAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListUserAppResponse`
        """
        http_info = self._list_user_app_http_info(request)
        return self._call_api(**http_info)

    def list_user_app_invoker(self, request):
        http_info = self._list_user_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_user_app_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/apps",
            "request_type": request.__class__.__name__,
            "response_type": "ListUserAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'is_creator' in local_var_params:
            query_params.append(('is_creator', local_var_params['is_creator']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'summary' in local_var_params:
            query_params.append(('summary', local_var_params['summary']))
        if 'eihealth_project_names' in local_var_params:
            query_params.append(('eihealth_project_names', local_var_params['eihealth_project_names']))
            collection_formats['eihealth_project_names'] = 'csv'
        if 'labels' in local_var_params:
            query_params.append(('labels', local_var_params['labels']))
            collection_formats['labels'] = 'csv'
        if 'start_create_time' in local_var_params:
            query_params.append(('start_create_time', local_var_params['start_create_time']))
        if 'end_create_time' in local_var_params:
            query_params.append(('end_create_time', local_var_params['end_create_time']))
        if 'start_update_time' in local_var_params:
            query_params.append(('start_update_time', local_var_params['start_update_time']))
        if 'end_update_time' in local_var_params:
            query_params.append(('end_update_time', local_var_params['end_update_time']))
        if 'sort_by' in local_var_params:
            query_params.append(('sort_by', local_var_params['sort_by']))
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

    def list_user_drug_job(self, request):
        r"""获取用户所属空间的药物作业列表

        获取用户所属空间的药物作业列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUserDrugJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ListUserDrugJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListUserDrugJobResponse`
        """
        http_info = self._list_user_drug_job_http_info(request)
        return self._call_api(**http_info)

    def list_user_drug_job_invoker(self, request):
        http_info = self._list_user_drug_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_user_drug_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/drug-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListUserDrugJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'is_creator' in local_var_params:
            query_params.append(('is_creator', local_var_params['is_creator']))
        if 'job_name' in local_var_params:
            query_params.append(('job_name', local_var_params['job_name']))
        if 'eihealth_project_names' in local_var_params:
            query_params.append(('eihealth_project_names', local_var_params['eihealth_project_names']))
            collection_formats['eihealth_project_names'] = 'csv'
        if 'labels' in local_var_params:
            query_params.append(('labels', local_var_params['labels']))
            collection_formats['labels'] = 'csv'
        if 'status_list' in local_var_params:
            query_params.append(('status_list', local_var_params['status_list']))
            collection_formats['status_list'] = 'csv'
        if 'types' in local_var_params:
            query_params.append(('types', local_var_params['types']))
            collection_formats['types'] = 'csv'
        if 'create_start_time' in local_var_params:
            query_params.append(('create_start_time', local_var_params['create_start_time']))
        if 'create_end_time' in local_var_params:
            query_params.append(('create_end_time', local_var_params['create_end_time']))
        if 'finish_start_time' in local_var_params:
            query_params.append(('finish_start_time', local_var_params['finish_start_time']))
        if 'finish_end_time' in local_var_params:
            query_params.append(('finish_end_time', local_var_params['finish_end_time']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
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

    def list_user_image(self, request):
        r"""获取用户所属空间的镜像列表

        获取用户所属空间的镜像列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUserImage
        :type request: :class:`huaweicloudsdkeihealth.v1.ListUserImageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListUserImageResponse`
        """
        http_info = self._list_user_image_http_info(request)
        return self._call_api(**http_info)

    def list_user_image_invoker(self, request):
        http_info = self._list_user_image_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_user_image_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/images",
            "request_type": request.__class__.__name__,
            "response_type": "ListUserImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'is_creator' in local_var_params:
            query_params.append(('is_creator', local_var_params['is_creator']))
        if 'image_id' in local_var_params:
            query_params.append(('image_id', local_var_params['image_id']))
        if 'image_name' in local_var_params:
            query_params.append(('image_name', local_var_params['image_name']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'eihealth_project_names' in local_var_params:
            query_params.append(('eihealth_project_names', local_var_params['eihealth_project_names']))
            collection_formats['eihealth_project_names'] = 'csv'
        if 'source_project_name' in local_var_params:
            query_params.append(('source_project_name', local_var_params['source_project_name']))
        if 'types' in local_var_params:
            query_params.append(('types', local_var_params['types']))
            collection_formats['types'] = 'csv'
        if 'start_create_time' in local_var_params:
            query_params.append(('start_create_time', local_var_params['start_create_time']))
        if 'end_create_time' in local_var_params:
            query_params.append(('end_create_time', local_var_params['end_create_time']))
        if 'start_update_time' in local_var_params:
            query_params.append(('start_update_time', local_var_params['start_update_time']))
        if 'end_update_time' in local_var_params:
            query_params.append(('end_update_time', local_var_params['end_update_time']))
        if 'sort_by' in local_var_params:
            query_params.append(('sort_by', local_var_params['sort_by']))
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

    def list_user_job(self, request):
        r"""获取用户所属空间的作业列表

        获取用户所属空间的作业列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUserJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ListUserJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListUserJobResponse`
        """
        http_info = self._list_user_job_http_info(request)
        return self._call_api(**http_info)

    def list_user_job_invoker(self, request):
        http_info = self._list_user_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_user_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListUserJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'is_creator' in local_var_params:
            query_params.append(('is_creator', local_var_params['is_creator']))
        if 'job_name' in local_var_params:
            query_params.append(('job_name', local_var_params['job_name']))
        if 'eihealth_project_names' in local_var_params:
            query_params.append(('eihealth_project_names', local_var_params['eihealth_project_names']))
            collection_formats['eihealth_project_names'] = 'csv'
        if 'types' in local_var_params:
            query_params.append(('types', local_var_params['types']))
            collection_formats['types'] = 'csv'
        if 'status_list' in local_var_params:
            query_params.append(('status_list', local_var_params['status_list']))
            collection_formats['status_list'] = 'csv'
        if 'labels' in local_var_params:
            query_params.append(('labels', local_var_params['labels']))
            collection_formats['labels'] = 'csv'
        if 'start_create_time' in local_var_params:
            query_params.append(('start_create_time', local_var_params['start_create_time']))
        if 'end_create_time' in local_var_params:
            query_params.append(('end_create_time', local_var_params['end_create_time']))
        if 'start_finish_time' in local_var_params:
            query_params.append(('start_finish_time', local_var_params['start_finish_time']))
        if 'end_finish_time' in local_var_params:
            query_params.append(('end_finish_time', local_var_params['end_finish_time']))
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

    def list_user_workflow(self, request):
        r"""获取用户所属空间的流程列表

        获取用户所属空间的流程列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUserWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.ListUserWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListUserWorkflowResponse`
        """
        http_info = self._list_user_workflow_http_info(request)
        return self._call_api(**http_info)

    def list_user_workflow_invoker(self, request):
        http_info = self._list_user_workflow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_user_workflow_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/workflows",
            "request_type": request.__class__.__name__,
            "response_type": "ListUserWorkflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'is_creator' in local_var_params:
            query_params.append(('is_creator', local_var_params['is_creator']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'summary' in local_var_params:
            query_params.append(('summary', local_var_params['summary']))
        if 'eihealth_project_names' in local_var_params:
            query_params.append(('eihealth_project_names', local_var_params['eihealth_project_names']))
            collection_formats['eihealth_project_names'] = 'csv'
        if 'labels' in local_var_params:
            query_params.append(('labels', local_var_params['labels']))
            collection_formats['labels'] = 'csv'
        if 'start_create_time' in local_var_params:
            query_params.append(('start_create_time', local_var_params['start_create_time']))
        if 'end_create_time' in local_var_params:
            query_params.append(('end_create_time', local_var_params['end_create_time']))
        if 'start_update_time' in local_var_params:
            query_params.append(('start_update_time', local_var_params['start_update_time']))
        if 'end_update_time' in local_var_params:
            query_params.append(('end_update_time', local_var_params['end_update_time']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
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

    def list_vendor(self, request):
        r"""获取供应商列表

        获取供应商列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVendor
        :type request: :class:`huaweicloudsdkeihealth.v1.ListVendorRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListVendorResponse`
        """
        http_info = self._list_vendor_http_info(request)
        return self._call_api(**http_info)

    def list_vendor_invoker(self, request):
        http_info = self._list_vendor_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_vendor_http_info(cls, request):
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

    def list_workflow(self, request):
        r"""获取流程列表

        获取流程列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.ListWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListWorkflowResponse`
        """
        http_info = self._list_workflow_http_info(request)
        return self._call_api(**http_info)

    def list_workflow_invoker(self, request):
        http_info = self._list_workflow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_workflow_http_info(cls, request):
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

    def quote_data(self, request):
        r"""引用项目数据

        引用项目数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for QuoteData
        :type request: :class:`huaweicloudsdkeihealth.v1.QuoteDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.QuoteDataResponse`
        """
        http_info = self._quote_data_http_info(request)
        return self._call_api(**http_info)

    def quote_data_invoker(self, request):
        http_info = self._quote_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _quote_data_http_info(cls, request):
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

    def retry_data_job(self, request):
        r"""重试数据作业

        重试数据作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RetryDataJob
        :type request: :class:`huaweicloudsdkeihealth.v1.RetryDataJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.RetryDataJobResponse`
        """
        http_info = self._retry_data_job_http_info(request)
        return self._call_api(**http_info)

    def retry_data_job_invoker(self, request):
        http_info = self._retry_data_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _retry_data_job_http_info(cls, request):
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

    def retry_job(self, request):
        r"""重试作业

        重试作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RetryJob
        :type request: :class:`huaweicloudsdkeihealth.v1.RetryJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.RetryJobResponse`
        """
        http_info = self._retry_job_http_info(request)
        return self._call_api(**http_info)

    def retry_job_invoker(self, request):
        http_info = self._retry_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _retry_job_http_info(cls, request):
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

    def run_fasta_preprocess(self, request):
        r"""受体预处理（Fasta格式）

        受体预处理（Fasta格式），用于前端计算预期扣费次数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunFastaPreprocess
        :type request: :class:`huaweicloudsdkeihealth.v1.RunFastaPreprocessRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.RunFastaPreprocessResponse`
        """
        http_info = self._run_fasta_preprocess_http_info(request)
        return self._call_api(**http_info)

    def run_fasta_preprocess_invoker(self, request):
        http_info = self._run_fasta_preprocess_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_fasta_preprocess_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/receptor/fasta-preprocess",
            "request_type": request.__class__.__name__,
            "response_type": "RunFastaPreprocessResponse"
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

    def run_format_converter(self, request):
        r"""单分子文件格式转换

        单分子文件格式转换。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunFormatConverter
        :type request: :class:`huaweicloudsdkeihealth.v1.RunFormatConverterRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.RunFormatConverterResponse`
        """
        http_info = self._run_format_converter_http_info(request)
        return self._call_api(**http_info)

    def run_format_converter_invoker(self, request):
        http_info = self._run_format_converter_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_format_converter_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/toolkit/format-converter",
            "request_type": request.__class__.__name__,
            "response_type": "RunFormatConverterResponse"
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

    def show_admet_job(self, request):
        r"""查询分子属性预测作业详情

        查询分子属性预测作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAdmetJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowAdmetJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowAdmetJobResponse`
        """
        http_info = self._show_admet_job_http_info(request)
        return self._call_api(**http_info)

    def show_admet_job_invoker(self, request):
        http_info = self._show_admet_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_admet_job_http_info(cls, request):
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

    def show_agency(self, request):
        r"""获取业务委托

        获取业务委托。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAgency
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowAgencyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowAgencyResponse`
        """
        http_info = self._show_agency_http_info(request)
        return self._call_api(**http_info)

    def show_agency_invoker(self, request):
        http_info = self._show_agency_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_agency_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/agencies",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAgencyResponse"
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

    def show_app(self, request):
        r"""获取应用详情

        获取应用详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApp
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowAppResponse`
        """
        http_info = self._show_app_http_info(request)
        return self._call_api(**http_info)

    def show_app_invoker(self, request):
        http_info = self._show_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_app_http_info(cls, request):
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

    def show_asset(self, request):
        r"""查询资产详情

        查询资产详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAsset
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowAssetRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowAssetResponse`
        """
        http_info = self._show_asset_http_info(request)
        return self._call_api(**http_info)

    def show_asset_invoker(self, request):
        http_info = self._show_asset_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_asset_http_info(cls, request):
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

    def show_asset_version(self, request):
        r"""查询资产版本详情

        查询资产版本详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAssetVersion
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowAssetVersionRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowAssetVersionResponse`
        """
        http_info = self._show_asset_version_http_info(request)
        return self._call_api(**http_info)

    def show_asset_version_invoker(self, request):
        http_info = self._show_asset_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_asset_version_http_info(cls, request):
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

    def show_bucket_storage(self, request):
        r"""获取桶存量信息

        获取桶存量信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBucketStorage
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowBucketStorageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowBucketStorageResponse`
        """
        http_info = self._show_bucket_storage_http_info(request)
        return self._call_api(**http_info)

    def show_bucket_storage_invoker(self, request):
        http_info = self._show_bucket_storage_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_bucket_storage_http_info(cls, request):
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

    def show_chat(self, request):
        r"""获取对话详情

        获取对话详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowChat
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowChatRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowChatResponse`
        """
        http_info = self._show_chat_http_info(request)
        return self._call_api(**http_info)

    def show_chat_invoker(self, request):
        http_info = self._show_chat_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_chat_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/chats/{chat_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowChatResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'chat_id' in local_var_params:
            path_params['chat_id'] = local_var_params['chat_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Chat-Route-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_clustering_job(self, request):
        r"""查询聚类分析作业详情

        查询聚类分析作业详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowClusteringJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowClusteringJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowClusteringJobResponse`
        """
        http_info = self._show_clustering_job_http_info(request)
        return self._call_api(**http_info)

    def show_clustering_job_invoker(self, request):
        http_info = self._show_clustering_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_clustering_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/clustering/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClusteringJobResponse"
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

    def show_data(self, request):
        r"""获取数据详情

        获取指定数据对象的详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowData
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowDataResponse`
        """
        http_info = self._show_data_http_info(request)
        return self._call_api(**http_info)

    def show_data_invoker(self, request):
        http_info = self._show_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_data_http_info(cls, request):
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

    def show_data_job(self, request):
        r"""获取数据作业详细信息

        获取数据作业详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDataJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowDataJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowDataJobResponse`
        """
        http_info = self._show_data_job_http_info(request)
        return self._call_api(**http_info)

    def show_data_job_invoker(self, request):
        http_info = self._show_data_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_data_job_http_info(cls, request):
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

    def show_docker_login(self, request):
        r"""获取docker login指令

        获取docker login指令
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDockerLogin
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowDockerLoginRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowDockerLoginResponse`
        """
        http_info = self._show_docker_login_http_info(request)
        return self._call_api(**http_info)

    def show_docker_login_invoker(self, request):
        http_info = self._show_docker_login_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_docker_login_http_info(cls, request):
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

    def show_docking_job(self, request):
        r"""查询分子对接作业详情

        查询分子对接作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDockingJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowDockingJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowDockingJobResponse`
        """
        http_info = self._show_docking_job_http_info(request)
        return self._call_api(**http_info)

    def show_docking_job_invoker(self, request):
        http_info = self._show_docking_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_docking_job_http_info(cls, request):
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

    def show_env(self, request):
        r"""查询系统配置列表

        获取系统配置列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEnv
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowEnvRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowEnvResponse`
        """
        http_info = self._show_env_http_info(request)
        return self._call_api(**http_info)

    def show_env_invoker(self, request):
        http_info = self._show_env_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_env_http_info(cls, request):
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

    def show_fep_job(self, request):
        r"""查询自由能微扰作业详情

        查询自由能微扰作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFepJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowFepJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowFepJobResponse`
        """
        http_info = self._show_fep_job_http_info(request)
        return self._call_api(**http_info)

    def show_fep_job_invoker(self, request):
        http_info = self._show_fep_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_fep_job_http_info(cls, request):
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

    def show_gen_job(self, request):
        r"""查询分子生成作业详情

        查询分子生成作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGenJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowGenJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowGenJobResponse`
        """
        http_info = self._show_gen_job_http_info(request)
        return self._call_api(**http_info)

    def show_gen_job_invoker(self, request):
        http_info = self._show_gen_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_gen_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/generation/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGenJobResponse"
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

    def show_job(self, request):
        r"""获取作业详情

        获取作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowJobResponse`
        """
        http_info = self._show_job_http_info(request)
        return self._call_api(**http_info)

    def show_job_invoker(self, request):
        http_info = self._show_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_job_http_info(cls, request):
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

    def show_job_event(self, request):
        r"""获取作业事件

        获取作业事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJobEvent
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowJobEventRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowJobEventResponse`
        """
        http_info = self._show_job_event_http_info(request)
        return self._call_api(**http_info)

    def show_job_event_invoker(self, request):
        http_info = self._show_job_event_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_job_event_http_info(cls, request):
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

    def show_job_log(self, request):
        r"""获取作业日志

        获取作业日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJobLog
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowJobLogRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowJobLogResponse`
        """
        http_info = self._show_job_log_http_info(request)
        return self._call_api(**http_info)

    def show_job_log_invoker(self, request):
        http_info = self._show_job_log_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_job_log_http_info(cls, request):
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

    def show_mol_batch_download_task(self, request):
        r"""查询分子或分子复合物批量下载任务详情

        查询分子或分子复合物批量下载任务详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMolBatchDownloadTask
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowMolBatchDownloadTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowMolBatchDownloadTaskResponse`
        """
        http_info = self._show_mol_batch_download_task_http_info(request)
        return self._call_api(**http_info)

    def show_mol_batch_download_task_invoker(self, request):
        http_info = self._show_mol_batch_download_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_mol_batch_download_task_http_info(cls, request):
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

    def show_optm_job(self, request):
        r"""查询分子优化作业详情

        查询分子优化作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOptmJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowOptmJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowOptmJobResponse`
        """
        http_info = self._show_optm_job_http_info(request)
        return self._call_api(**http_info)

    def show_optm_job_invoker(self, request):
        http_info = self._show_optm_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_optm_job_http_info(cls, request):
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

    def show_pocket_detection_job(self, request):
        r"""查询靶点口袋发现作业详情

        查询靶点口袋发现作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPocketDetectionJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowPocketDetectionJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowPocketDetectionJobResponse`
        """
        http_info = self._show_pocket_detection_job_http_info(request)
        return self._call_api(**http_info)

    def show_pocket_detection_job_invoker(self, request):
        http_info = self._show_pocket_detection_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_pocket_detection_job_http_info(cls, request):
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

    def show_pocket_mol_design_job(self, request):
        r"""查询靶点口袋分子设计作业详情

        查询靶点口袋分子设计作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPocketMolDesignJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowPocketMolDesignJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowPocketMolDesignJobResponse`
        """
        http_info = self._show_pocket_mol_design_job_http_info(request)
        return self._call_api(**http_info)

    def show_pocket_mol_design_job_invoker(self, request):
        http_info = self._show_pocket_mol_design_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_pocket_mol_design_job_http_info(cls, request):
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

    def show_project(self, request):
        r"""获取项目详情

        获取项目详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProject
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowProjectRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowProjectResponse`
        """
        http_info = self._show_project_http_info(request)
        return self._call_api(**http_info)

    def show_project_invoker(self, request):
        http_info = self._show_project_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_project_http_info(cls, request):
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

    def show_search_job(self, request):
        r"""查询分子搜索作业详情

        查询分子搜索作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSearchJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowSearchJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowSearchJobResponse`
        """
        http_info = self._show_search_job_http_info(request)
        return self._call_api(**http_info)

    def show_search_job_invoker(self, request):
        http_info = self._show_search_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_search_job_http_info(cls, request):
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

    def show_target_opt_job(self, request):
        r"""查询靶点优化作业详情

        查询靶点优化作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTargetOptJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowTargetOptJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowTargetOptJobResponse`
        """
        http_info = self._show_target_opt_job_http_info(request)
        return self._call_api(**http_info)

    def show_target_opt_job_invoker(self, request):
        http_info = self._show_target_opt_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_target_opt_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/target-optimization/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTargetOptJobResponse"
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

    def show_task_events(self, request):
        r"""获取子任务启动事件

        获取子任务启动事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTaskEvents
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowTaskEventsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowTaskEventsResponse`
        """
        http_info = self._show_task_events_http_info(request)
        return self._call_api(**http_info)

    def show_task_events_invoker(self, request):
        http_info = self._show_task_events_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_task_events_http_info(cls, request):
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

    def show_task_instance_events(self, request):
        r"""获取子任务中实例的事件

        获取子任务中实例的事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTaskInstanceEvents
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstanceEventsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstanceEventsResponse`
        """
        http_info = self._show_task_instance_events_http_info(request)
        return self._call_api(**http_info)

    def show_task_instance_events_invoker(self, request):
        http_info = self._show_task_instance_events_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_task_instance_events_http_info(cls, request):
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

    def show_task_instance_metric_data(self, request):
        r"""获取子任务中实例的资源监控数据

        获取子任务中实例的资源监控数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTaskInstanceMetricData
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstanceMetricDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstanceMetricDataResponse`
        """
        http_info = self._show_task_instance_metric_data_http_info(request)
        return self._call_api(**http_info)

    def show_task_instance_metric_data_invoker(self, request):
        http_info = self._show_task_instance_metric_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_task_instance_metric_data_http_info(cls, request):
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

    def show_task_instance_pod(self, request):
        r"""获取子任务中实例的pod信息

        获取子任务中实例的pod信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTaskInstancePod
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstancePodRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstancePodResponse`
        """
        http_info = self._show_task_instance_pod_http_info(request)
        return self._call_api(**http_info)

    def show_task_instance_pod_invoker(self, request):
        http_info = self._show_task_instance_pod_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_task_instance_pod_http_info(cls, request):
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

    def show_task_instances(self, request):
        r"""获取子任务实例信息

        获取子任务实例信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTaskInstances
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstancesRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstancesResponse`
        """
        http_info = self._show_task_instances_http_info(request)
        return self._call_api(**http_info)

    def show_task_instances_invoker(self, request):
        http_info = self._show_task_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_task_instances_http_info(cls, request):
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

    def show_user(self, request):
        r"""获取指定用户详情

        获取指定用户详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUser
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowUserRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowUserResponse`
        """
        http_info = self._show_user_http_info(request)
        return self._call_api(**http_info)

    def show_user_invoker(self, request):
        http_info = self._show_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_user_http_info(cls, request):
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

    def show_user_setting(self, request):
        r"""查询用户设置

        查询用户设置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUserSetting
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowUserSettingRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowUserSettingResponse`
        """
        http_info = self._show_user_setting_http_info(request)
        return self._call_api(**http_info)

    def show_user_setting_invoker(self, request):
        http_info = self._show_user_setting_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_user_setting_http_info(cls, request):
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

    def show_vendor(self, request):
        r"""获取供应商配置

        获取供应商配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVendor
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowVendorRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowVendorResponse`
        """
        http_info = self._show_vendor_http_info(request)
        return self._call_api(**http_info)

    def show_vendor_invoker(self, request):
        http_info = self._show_vendor_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_vendor_http_info(cls, request):
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

    def show_workflow(self, request):
        r"""获取流程详情

        获取流程详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowWorkflowResponse`
        """
        http_info = self._show_workflow_http_info(request)
        return self._call_api(**http_info)

    def show_workflow_invoker(self, request):
        http_info = self._show_workflow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_workflow_http_info(cls, request):
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

    def subscribe_app(self, request):
        r"""订阅应用

        订阅应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SubscribeApp
        :type request: :class:`huaweicloudsdkeihealth.v1.SubscribeAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.SubscribeAppResponse`
        """
        http_info = self._subscribe_app_http_info(request)
        return self._call_api(**http_info)

    def subscribe_app_invoker(self, request):
        http_info = self._subscribe_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _subscribe_app_http_info(cls, request):
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

    def subscribe_image(self, request):
        r"""订阅镜像

        订阅镜像
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SubscribeImage
        :type request: :class:`huaweicloudsdkeihealth.v1.SubscribeImageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.SubscribeImageResponse`
        """
        http_info = self._subscribe_image_http_info(request)
        return self._call_api(**http_info)

    def subscribe_image_invoker(self, request):
        http_info = self._subscribe_image_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _subscribe_image_http_info(cls, request):
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

    def subscribe_workflow(self, request):
        r"""订阅流程

        订阅流程
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SubscribeWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.SubscribeWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.SubscribeWorkflowResponse`
        """
        http_info = self._subscribe_workflow_http_info(request)
        return self._call_api(**http_info)

    def subscribe_workflow_invoker(self, request):
        http_info = self._subscribe_workflow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _subscribe_workflow_http_info(cls, request):
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

    def transfer_project(self, request):
        r"""转移项目

        转移项目
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for TransferProject
        :type request: :class:`huaweicloudsdkeihealth.v1.TransferProjectRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.TransferProjectResponse`
        """
        http_info = self._transfer_project_http_info(request)
        return self._call_api(**http_info)

    def transfer_project_invoker(self, request):
        http_info = self._transfer_project_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _transfer_project_http_info(cls, request):
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

    def update_agency(self, request):
        r"""更新业务委托

        更新业务委托。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAgency
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateAgencyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateAgencyResponse`
        """
        http_info = self._update_agency_http_info(request)
        return self._call_api(**http_info)

    def update_agency_invoker(self, request):
        http_info = self._update_agency_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_agency_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/system/agencies",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAgencyResponse"
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

    def update_app(self, request):
        r"""更新应用

        更新应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateApp
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateAppResponse`
        """
        http_info = self._update_app_http_info(request)
        return self._call_api(**http_info)

    def update_app_invoker(self, request):
        http_info = self._update_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_app_http_info(cls, request):
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

    def update_chat(self, request):
        r"""更新对话

        更新对话。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateChat
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateChatRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateChatResponse`
        """
        http_info = self._update_chat_http_info(request)
        return self._call_api(**http_info)

    def update_chat_invoker(self, request):
        http_info = self._update_chat_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_chat_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/chats/{chat_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateChatResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'chat_id' in local_var_params:
            path_params['chat_id'] = local_var_params['chat_id']

        query_params = []

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

    def update_drug_database(self, request):
        r"""更新药物数据库

        更新药物数据库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDrugDatabase
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateDrugDatabaseRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateDrugDatabaseResponse`
        """
        http_info = self._update_drug_database_http_info(request)
        return self._call_api(**http_info)

    def update_drug_database_invoker(self, request):
        http_info = self._update_drug_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_drug_database_http_info(cls, request):
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

    def update_drug_job(self, request):
        r"""更新药物作业

        更新药物作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDrugJob
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateDrugJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateDrugJobResponse`
        """
        http_info = self._update_drug_job_http_info(request)
        return self._call_api(**http_info)

    def update_drug_job_invoker(self, request):
        http_info = self._update_drug_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_drug_job_http_info(cls, request):
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

    def update_drug_model(self, request):
        r"""更新药物模型

        更新药物模型
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDrugModel
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateDrugModelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateDrugModelResponse`
        """
        http_info = self._update_drug_model_http_info(request)
        return self._call_api(**http_info)

    def update_drug_model_invoker(self, request):
        http_info = self._update_drug_model_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_drug_model_http_info(cls, request):
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

    def update_image(self, request):
        r"""更新镜像描述信息或者类型

        更新镜像描述信息或者类型
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateImage
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateImageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateImageResponse`
        """
        http_info = self._update_image_http_info(request)
        return self._call_api(**http_info)

    def update_image_invoker(self, request):
        http_info = self._update_image_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_image_http_info(cls, request):
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

    def update_init_password(self, request):
        r"""新用户重置密码

        新用户重置密码
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInitPassword
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateInitPasswordRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateInitPasswordResponse`
        """
        http_info = self._update_init_password_http_info(request)
        return self._call_api(**http_info)

    def update_init_password_invoker(self, request):
        http_info = self._update_init_password_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_init_password_http_info(cls, request):
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

    def update_job(self, request):
        r"""更新作业

        更新作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateJob
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateJobResponse`
        """
        http_info = self._update_job_http_info(request)
        return self._call_api(**http_info)

    def update_job_invoker(self, request):
        http_info = self._update_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_job_http_info(cls, request):
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

    def update_member(self, request):
        r"""更新或者添加项目成员角色

        更新或者添加项目成员角色
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateMember
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateMemberRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateMemberResponse`
        """
        http_info = self._update_member_http_info(request)
        return self._call_api(**http_info)

    def update_member_invoker(self, request):
        http_info = self._update_member_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_member_http_info(cls, request):
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

    def update_performance_resource(self, request):
        r"""更新性能加速资源配置

        更新性能加速资源配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePerformanceResource
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdatePerformanceResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdatePerformanceResourceResponse`
        """
        http_info = self._update_performance_resource_http_info(request)
        return self._call_api(**http_info)

    def update_performance_resource_invoker(self, request):
        http_info = self._update_performance_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_performance_resource_http_info(cls, request):
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

    def update_project(self, request):
        r"""更新项目

        更新项目
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateProject
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateProjectRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateProjectResponse`
        """
        http_info = self._update_project_http_info(request)
        return self._call_api(**http_info)

    def update_project_invoker(self, request):
        http_info = self._update_project_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_project_http_info(cls, request):
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

    def update_top_project(self, request):
        r"""置顶空间

        置顶空间。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTopProject
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateTopProjectRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateTopProjectResponse`
        """
        http_info = self._update_top_project_http_info(request)
        return self._call_api(**http_info)

    def update_top_project_invoker(self, request):
        http_info = self._update_top_project_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_top_project_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/top",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTopProjectResponse"
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

    def update_user(self, request):
        r"""修改用户基本信息

        修改用户基本信息（邮箱，手机）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateUser
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateUserRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateUserResponse`
        """
        http_info = self._update_user_http_info(request)
        return self._call_api(**http_info)

    def update_user_invoker(self, request):
        http_info = self._update_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_user_http_info(cls, request):
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

    def update_user_by_domain(self, request):
        r"""最终租户修改子用户

        最终租户修改子用户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateUserByDomain
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateUserByDomainRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateUserByDomainResponse`
        """
        http_info = self._update_user_by_domain_http_info(request)
        return self._call_api(**http_info)

    def update_user_by_domain_invoker(self, request):
        http_info = self._update_user_by_domain_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_user_by_domain_http_info(cls, request):
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

    def update_user_role(self, request):
        r"""更新用户角色

        更新用户角色
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateUserRole
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateUserRoleRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateUserRoleResponse`
        """
        http_info = self._update_user_role_http_info(request)
        return self._call_api(**http_info)

    def update_user_role_invoker(self, request):
        http_info = self._update_user_role_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_user_role_http_info(cls, request):
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

    def update_user_setting(self, request):
        r"""更新用户设置

        更新用户设置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateUserSetting
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateUserSettingRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateUserSettingResponse`
        """
        http_info = self._update_user_setting_http_info(request)
        return self._call_api(**http_info)

    def update_user_setting_invoker(self, request):
        http_info = self._update_user_setting_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_user_setting_http_info(cls, request):
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

    def update_vendor(self, request):
        r"""设置供应商配置

        设置供应商配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateVendor
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateVendorRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateVendorResponse`
        """
        http_info = self._update_vendor_http_info(request)
        return self._call_api(**http_info)

    def update_vendor_invoker(self, request):
        http_info = self._update_vendor_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_vendor_http_info(cls, request):
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

    def update_workflow(self, request):
        r"""更新流程

        更新流程
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateWorkflowResponse`
        """
        http_info = self._update_workflow_http_info(request)
        return self._call_api(**http_info)

    def update_workflow_invoker(self, request):
        http_info = self._update_workflow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_workflow_http_info(cls, request):
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

    def upload_data(self, request):
        r"""上传数据文件

        上传数据文件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadData
        :type request: :class:`huaweicloudsdkeihealth.v1.UploadDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UploadDataResponse`
        """
        http_info = self._upload_data_http_info(request)
        return self._call_api(**http_info)

    def upload_data_invoker(self, request):
        http_info = self._upload_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upload_data_http_info(cls, request):
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

    def validate_code(self, request):
        r"""预验证

        预验证
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ValidateCode
        :type request: :class:`huaweicloudsdkeihealth.v1.ValidateCodeRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ValidateCodeResponse`
        """
        http_info = self._validate_code_http_info(request)
        return self._call_api(**http_info)

    def validate_code_invoker(self, request):
        http_info = self._validate_code_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _validate_code_http_info(cls, request):
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

    def show_admet_properties(self, request):
        r"""ADMET属性预测接口

        计算小分子的物化性质，包括吸收(adsorption)、分布(distribution)、代谢(metabolism)、清除(excretion)与毒性(toxicity)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAdmetProperties
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowAdmetPropertiesRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowAdmetPropertiesResponse`
        """
        http_info = self._show_admet_properties_http_info(request)
        return self._call_api(**http_info)

    def show_admet_properties_invoker(self, request):
        http_info = self._show_admet_properties_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_admet_properties_http_info(cls, request):
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

    def create_cpi_job(self, request):
        r"""创建CPI作业

        创建CPI作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCpiJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateCpiJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateCpiJobResponse`
        """
        http_info = self._create_cpi_job_http_info(request)
        return self._call_api(**http_info)

    def create_cpi_job_invoker(self, request):
        http_info = self._create_cpi_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_cpi_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/cpi",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCpiJobResponse"
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

    def show_cpi_job(self, request):
        r"""查询CPI作业详情

        查询CPI作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCpiJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowCpiJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowCpiJobResponse`
        """
        http_info = self._show_cpi_job_http_info(request)
        return self._call_api(**http_info)

    def show_cpi_job_invoker(self, request):
        http_info = self._show_cpi_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_cpi_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/cpi/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCpiJobResponse"
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

    def create_css_cluster(self, request):
        r"""绑定CSS集群

        绑定CSS集群
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCssCluster
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateCssClusterRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateCssClusterResponse`
        """
        http_info = self._create_css_cluster_http_info(request)
        return self._call_api(**http_info)

    def create_css_cluster_invoker(self, request):
        http_info = self._create_css_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_css_cluster_http_info(cls, request):
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

    def delete_css_cluster(self, request):
        r"""CSS集群解绑

        CSS集群解绑
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCssCluster
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteCssClusterRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteCssClusterResponse`
        """
        http_info = self._delete_css_cluster_http_info(request)
        return self._call_api(**http_info)

    def delete_css_cluster_invoker(self, request):
        http_info = self._delete_css_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_css_cluster_http_info(cls, request):
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

    def list_css_cluster(self, request):
        r"""获取CSS集群列表

        获取CSS集群列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCssCluster
        :type request: :class:`huaweicloudsdkeihealth.v1.ListCssClusterRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListCssClusterResponse`
        """
        http_info = self._list_css_cluster_http_info(request)
        return self._call_api(**http_info)

    def list_css_cluster_invoker(self, request):
        http_info = self._list_css_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_css_cluster_http_info(cls, request):
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

    def list_term_tenant_css_cluster(self, request):
        r"""获取最终租户CSS集群列表

        获取最终租户CSS集群列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTermTenantCssCluster
        :type request: :class:`huaweicloudsdkeihealth.v1.ListTermTenantCssClusterRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListTermTenantCssClusterResponse`
        """
        http_info = self._list_term_tenant_css_cluster_http_info(request)
        return self._call_api(**http_info)

    def list_term_tenant_css_cluster_invoker(self, request):
        http_info = self._list_term_tenant_css_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_term_tenant_css_cluster_http_info(cls, request):
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

    def validate_css_connection(self, request):
        r"""测试CSS集群连接

        测试CSS集群连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ValidateCssConnection
        :type request: :class:`huaweicloudsdkeihealth.v1.ValidateCssConnectionRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ValidateCssConnectionResponse`
        """
        http_info = self._validate_css_connection_http_info(request)
        return self._call_api(**http_info)

    def validate_css_connection_invoker(self, request):
        http_info = self._validate_css_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _validate_css_connection_http_info(cls, request):
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

    def check_drug_ligand_difference(self, request):
        r"""计算配体间的3D结构差异

        计算配体间的3D结构差异
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckDrugLigandDifference
        :type request: :class:`huaweicloudsdkeihealth.v1.CheckDrugLigandDifferenceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CheckDrugLigandDifferenceResponse`
        """
        http_info = self._check_drug_ligand_difference_http_info(request)
        return self._call_api(**http_info)

    def check_drug_ligand_difference_invoker(self, request):
        http_info = self._check_drug_ligand_difference_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_drug_ligand_difference_http_info(cls, request):
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

    def create_drug_ligand_interaction2d_svg(self, request):
        r"""生成相互作用2D图

        生成相互作用2D图，若不提供配体文件，则受体文件中必须包含配体；若提供配体文件，则受体中的配体（若有）则会被忽略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDrugLigandInteraction2dSvg
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandInteraction2dSvgRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandInteraction2dSvgResponse`
        """
        http_info = self._create_drug_ligand_interaction2d_svg_http_info(request)
        return self._call_api(**http_info)

    def create_drug_ligand_interaction2d_svg_invoker(self, request):
        http_info = self._create_drug_ligand_interaction2d_svg_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_drug_ligand_interaction2d_svg_http_info(cls, request):
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

    def create_drug_ligand_preview_task(self, request):
        r"""创建配体文件预览任务

        创建配体文件预览任务，支持SMI、SDF、PDB、MOL2
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDrugLigandPreviewTask
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandPreviewTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandPreviewTaskResponse`
        """
        http_info = self._create_drug_ligand_preview_task_http_info(request)
        return self._call_api(**http_info)

    def create_drug_ligand_preview_task_invoker(self, request):
        http_info = self._create_drug_ligand_preview_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_drug_ligand_preview_task_http_info(cls, request):
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

    def create_drug_ligand_sdf(self, request):
        r"""生成分子SDF三维结构

        生成分子SDF三维结构
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDrugLigandSdf
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandSdfRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandSdfResponse`
        """
        http_info = self._create_drug_ligand_sdf_http_info(request)
        return self._call_api(**http_info)

    def create_drug_ligand_sdf_invoker(self, request):
        http_info = self._create_drug_ligand_sdf_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_drug_ligand_sdf_http_info(cls, request):
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

    def create_drug_ligand_similarity_graph_task(self, request):
        r"""创建配体相似性图计算任务

        创建配体相似性图计算任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDrugLigandSimilarityGraphTask
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandSimilarityGraphTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandSimilarityGraphTaskResponse`
        """
        http_info = self._create_drug_ligand_similarity_graph_task_http_info(request)
        return self._call_api(**http_info)

    def create_drug_ligand_similarity_graph_task_invoker(self, request):
        http_info = self._create_drug_ligand_similarity_graph_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_drug_ligand_similarity_graph_task_http_info(cls, request):
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

    def create_drug_ligand_svg(self, request):
        r"""生成分子SVG图

        生成分子SVG图
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDrugLigandSvg
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandSvgRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandSvgResponse`
        """
        http_info = self._create_drug_ligand_svg_http_info(request)
        return self._call_api(**http_info)

    def create_drug_ligand_svg_invoker(self, request):
        http_info = self._create_drug_ligand_svg_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_drug_ligand_svg_http_info(cls, request):
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

    def delete_drug_ligand_preview_task(self, request):
        r"""删除配体文件预览任务

        删除配体文件预览任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDrugLigandPreviewTask
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteDrugLigandPreviewTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteDrugLigandPreviewTaskResponse`
        """
        http_info = self._delete_drug_ligand_preview_task_http_info(request)
        return self._call_api(**http_info)

    def delete_drug_ligand_preview_task_invoker(self, request):
        http_info = self._delete_drug_ligand_preview_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_drug_ligand_preview_task_http_info(cls, request):
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

    def delete_drug_ligand_similarity_graph_task(self, request):
        r"""删除配体相似性图计算任务

        删除配体相似性图计算任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDrugLigandSimilarityGraphTask
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteDrugLigandSimilarityGraphTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteDrugLigandSimilarityGraphTaskResponse`
        """
        http_info = self._delete_drug_ligand_similarity_graph_task_http_info(request)
        return self._call_api(**http_info)

    def delete_drug_ligand_similarity_graph_task_invoker(self, request):
        http_info = self._delete_drug_ligand_similarity_graph_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_drug_ligand_similarity_graph_task_http_info(cls, request):
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

    def parse_drug_receptor_info(self, request):
        r"""受体信息解析

        受体信息解析，如果有多个受体蛋白则只处理第一个，如果一个受体蛋白里结合了多个配体，则最多只处理前10个
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ParseDrugReceptorInfo
        :type request: :class:`huaweicloudsdkeihealth.v1.ParseDrugReceptorInfoRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ParseDrugReceptorInfoResponse`
        """
        http_info = self._parse_drug_receptor_info_http_info(request)
        return self._call_api(**http_info)

    def parse_drug_receptor_info_invoker(self, request):
        http_info = self._parse_drug_receptor_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _parse_drug_receptor_info_http_info(cls, request):
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

    def recognize_drug_receptor_pocket(self, request):
        r"""受体口袋检测

        检测受体口袋，检测类型基于配体，基于氨基酸残基，自动检测，自定义和全局对接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeDrugReceptorPocket
        :type request: :class:`huaweicloudsdkeihealth.v1.RecognizeDrugReceptorPocketRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.RecognizeDrugReceptorPocketResponse`
        """
        http_info = self._recognize_drug_receptor_pocket_http_info(request)
        return self._call_api(**http_info)

    def recognize_drug_receptor_pocket_invoker(self, request):
        http_info = self._recognize_drug_receptor_pocket_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_drug_receptor_pocket_http_info(cls, request):
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

    def run_drug_ligand_to_smiles_conversion(self, request):
        r"""配体格式转换为SMILES

        配体格式转换为SMILES，若配体文件中存在多个分子，则只取第一个返回
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunDrugLigandToSmilesConversion
        :type request: :class:`huaweicloudsdkeihealth.v1.RunDrugLigandToSmilesConversionRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.RunDrugLigandToSmilesConversionResponse`
        """
        http_info = self._run_drug_ligand_to_smiles_conversion_http_info(request)
        return self._call_api(**http_info)

    def run_drug_ligand_to_smiles_conversion_invoker(self, request):
        http_info = self._run_drug_ligand_to_smiles_conversion_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_drug_ligand_to_smiles_conversion_http_info(cls, request):
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

    def run_drug_receptor_preprocess(self, request):
        r"""受体预处理

        受体预处理，用于前端显示预处理后的受体
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunDrugReceptorPreprocess
        :type request: :class:`huaweicloudsdkeihealth.v1.RunDrugReceptorPreprocessRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.RunDrugReceptorPreprocessResponse`
        """
        http_info = self._run_drug_receptor_preprocess_http_info(request)
        return self._call_api(**http_info)

    def run_drug_receptor_preprocess_invoker(self, request):
        http_info = self._run_drug_receptor_preprocess_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_drug_receptor_preprocess_http_info(cls, request):
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

    def show_drug_ligand_preview_task(self, request):
        r"""查询配体文件预览任务

        查询配体文件预览任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDrugLigandPreviewTask
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowDrugLigandPreviewTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowDrugLigandPreviewTaskResponse`
        """
        http_info = self._show_drug_ligand_preview_task_http_info(request)
        return self._call_api(**http_info)

    def show_drug_ligand_preview_task_invoker(self, request):
        http_info = self._show_drug_ligand_preview_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_drug_ligand_preview_task_http_info(cls, request):
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

    def show_drug_ligand_similarity_graph_task(self, request):
        r"""查询配体相似性图计算任务

        查询配体相似性图计算任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDrugLigandSimilarityGraphTask
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowDrugLigandSimilarityGraphTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowDrugLigandSimilarityGraphTaskResponse`
        """
        http_info = self._show_drug_ligand_similarity_graph_task_http_info(request)
        return self._call_api(**http_info)

    def show_drug_ligand_similarity_graph_task_invoker(self, request):
        http_info = self._show_drug_ligand_similarity_graph_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_drug_ligand_similarity_graph_task_http_info(cls, request):
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

    def download_data(self, request):
        r"""文件下载

        文件下载
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadData
        :type request: :class:`huaweicloudsdkeihealth.v1.DownloadDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DownloadDataResponse`
        """
        http_info = self._download_data_http_info(request)
        return self._call_api(**http_info)

    def download_data_invoker(self, request):
        http_info = self._download_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_data_http_info(cls, request):
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

    def show_overview(self, request):
        r"""获取医疗平台信息

        获取医疗平台信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOverview
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowOverviewRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowOverviewResponse`
        """
        http_info = self._show_overview_http_info(request)
        return self._call_api(**http_info)

    def show_overview_invoker(self, request):
        http_info = self._show_overview_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_overview_http_info(cls, request):
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

    def download_public_data(self, request):
        r"""文件下载

        文件下载
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadPublicData
        :type request: :class:`huaweicloudsdkeihealth.v1.DownloadPublicDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DownloadPublicDataResponse`
        """
        http_info = self._download_public_data_http_info(request)
        return self._call_api(**http_info)

    def download_public_data_invoker(self, request):
        http_info = self._download_public_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_public_data_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/data/download",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadPublicDataResponse"
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

    def list_obs_bucket(self, request):
        r"""获取用户OBS桶列表

        获取用户OBS桶列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListObsBucket
        :type request: :class:`huaweicloudsdkeihealth.v1.ListObsBucketRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListObsBucketResponse`
        """
        http_info = self._list_obs_bucket_http_info(request)
        return self._call_api(**http_info)

    def list_obs_bucket_invoker(self, request):
        http_info = self._list_obs_bucket_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_obs_bucket_http_info(cls, request):
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

    def list_obs_bucket_object(self, request):
        r"""获取用户OBS桶内对象

        获取用户OBS桶内对象
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListObsBucketObject
        :type request: :class:`huaweicloudsdkeihealth.v1.ListObsBucketObjectRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListObsBucketObjectResponse`
        """
        http_info = self._list_obs_bucket_object_http_info(request)
        return self._call_api(**http_info)

    def list_obs_bucket_object_invoker(self, request):
        http_info = self._list_obs_bucket_object_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_obs_bucket_object_http_info(cls, request):
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

    def create_notebook(self, request):
        r"""创建notebook

        创建notebook
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateNotebook
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateNotebookRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateNotebookResponse`
        """
        http_info = self._create_notebook_http_info(request)
        return self._call_api(**http_info)

    def create_notebook_invoker(self, request):
        http_info = self._create_notebook_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_notebook_http_info(cls, request):
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

    def delete_notebook(self, request):
        r"""删除notebook

        删除notebook
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteNotebook
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteNotebookRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteNotebookResponse`
        """
        http_info = self._delete_notebook_http_info(request)
        return self._call_api(**http_info)

    def delete_notebook_invoker(self, request):
        http_info = self._delete_notebook_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_notebook_http_info(cls, request):
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

    def list_notebook(self, request):
        r"""获取notebook列表

        获取notebook列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNotebook
        :type request: :class:`huaweicloudsdkeihealth.v1.ListNotebookRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListNotebookResponse`
        """
        http_info = self._list_notebook_http_info(request)
        return self._call_api(**http_info)

    def list_notebook_invoker(self, request):
        http_info = self._list_notebook_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_notebook_http_info(cls, request):
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

    def list_notebook_tool(self, request):
        r"""获取notebook工作环境

        获取notebook工作环境
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNotebookTool
        :type request: :class:`huaweicloudsdkeihealth.v1.ListNotebookToolRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListNotebookToolResponse`
        """
        http_info = self._list_notebook_tool_http_info(request)
        return self._call_api(**http_info)

    def list_notebook_tool_invoker(self, request):
        http_info = self._list_notebook_tool_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_notebook_tool_http_info(cls, request):
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

    def list_user_notebook(self, request):
        r"""获取用户所属空间的notebook列表

        获取用户所属空间的notebook列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUserNotebook
        :type request: :class:`huaweicloudsdkeihealth.v1.ListUserNotebookRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListUserNotebookResponse`
        """
        http_info = self._list_user_notebook_http_info(request)
        return self._call_api(**http_info)

    def list_user_notebook_invoker(self, request):
        http_info = self._list_user_notebook_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_user_notebook_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/notebooks",
            "request_type": request.__class__.__name__,
            "response_type": "ListUserNotebookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'notebook_name' in local_var_params:
            query_params.append(('notebook_name', local_var_params['notebook_name']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'image_name' in local_var_params:
            query_params.append(('image_name', local_var_params['image_name']))
        if 'is_creator' in local_var_params:
            query_params.append(('is_creator', local_var_params['is_creator']))
        if 'eihealth_project_names' in local_var_params:
            query_params.append(('eihealth_project_names', local_var_params['eihealth_project_names']))
            collection_formats['eihealth_project_names'] = 'csv'
        if 'statuses' in local_var_params:
            query_params.append(('statuses', local_var_params['statuses']))
            collection_formats['statuses'] = 'csv'
        if 'start_create_time' in local_var_params:
            query_params.append(('start_create_time', local_var_params['start_create_time']))
        if 'end_create_time' in local_var_params:
            query_params.append(('end_create_time', local_var_params['end_create_time']))
        if 'start_update_time' in local_var_params:
            query_params.append(('start_update_time', local_var_params['start_update_time']))
        if 'end_update_time' in local_var_params:
            query_params.append(('end_update_time', local_var_params['end_update_time']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_by' in local_var_params:
            query_params.append(('sort_by', local_var_params['sort_by']))
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

    def show_notebook(self, request):
        r"""获取notebook详情

        获取notebook详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNotebook
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowNotebookRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowNotebookResponse`
        """
        http_info = self._show_notebook_http_info(request)
        return self._call_api(**http_info)

    def show_notebook_invoker(self, request):
        http_info = self._show_notebook_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_notebook_http_info(cls, request):
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

    def show_notebook_token(self, request):
        r"""获取notebook鉴权信息

        获取notebook鉴权信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNotebookToken
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowNotebookTokenRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowNotebookTokenResponse`
        """
        http_info = self._show_notebook_token_http_info(request)
        return self._call_api(**http_info)

    def show_notebook_token_invoker(self, request):
        http_info = self._show_notebook_token_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_notebook_token_http_info(cls, request):
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

    def stop_or_start_notebook(self, request):
        r"""启停notebook

        启停notebook
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopOrStartNotebook
        :type request: :class:`huaweicloudsdkeihealth.v1.StopOrStartNotebookRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.StopOrStartNotebookResponse`
        """
        http_info = self._stop_or_start_notebook_http_info(request)
        return self._call_api(**http_info)

    def stop_or_start_notebook_invoker(self, request):
        http_info = self._stop_or_start_notebook_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_or_start_notebook_http_info(cls, request):
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

    def update_notebook(self, request):
        r"""更新notebook

        更新notebook
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateNotebook
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateNotebookRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateNotebookResponse`
        """
        http_info = self._update_notebook_http_info(request)
        return self._call_api(**http_info)

    def update_notebook_invoker(self, request):
        http_info = self._update_notebook_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_notebook_http_info(cls, request):
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
