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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdksfsturbo'")


class SFSTurboAsyncClient(Client):
    def __init__(self):
        super(SFSTurboAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdksfsturbo.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "SFSTurboAsyncClient":
                raise TypeError("client type error, support client type is SFSTurboAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_add_shared_tags_async(self, request):
        """批量添加共享标签

        指定共享批量添加标签。
        
        一个共享上最多有10个标签。
        一个共享上的多个标签的key不允许重复。
        此接口为幂等接口：如果要添加的key在共享上已存在，则覆盖更新标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAddSharedTags
        :type request: :class:`huaweicloudsdksfsturbo.v1.BatchAddSharedTagsRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.BatchAddSharedTagsResponse`
        """
        http_info = self._batch_add_shared_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_add_shared_tags_async_invoker(self, request):
        http_info = self._batch_add_shared_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_add_shared_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/sfs-turbo/{share_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAddSharedTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

        query_params = []

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

    def change_security_group_async(self, request):
        """修改文件系统绑定的安全组

        修改SFS Turbo文件系统绑定的安全组。修改安全组为异步任务，可以通过“查询单个文件系统”返回的子状态字段“sub_status”来判断是否修改安全组状态，子状态为“232”即为修改安全组成功。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeSecurityGroup
        :type request: :class:`huaweicloudsdksfsturbo.v1.ChangeSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ChangeSecurityGroupResponse`
        """
        http_info = self._change_security_group_http_info(request)
        return self._call_api(**http_info)

    def change_security_group_async_invoker(self, request):
        http_info = self._change_security_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_security_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares/{share_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeSecurityGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

        query_params = []

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

    def change_share_name_async(self, request):
        """修改文件系统名称

        修改文件系统名称
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeShareName
        :type request: :class:`huaweicloudsdksfsturbo.v1.ChangeShareNameRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ChangeShareNameResponse`
        """
        http_info = self._change_share_name_http_info(request)
        return self._call_api(**http_info)

    def change_share_name_async_invoker(self, request):
        http_info = self._change_share_name_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_share_name_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares/{share_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeShareNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

        query_params = []

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

    def create_backend_target_async(self, request):
        """创建文件系统后端存储库

        创建文件系统后端存储库
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateBackendTarget
        :type request: :class:`huaweicloudsdksfsturbo.v1.CreateBackendTargetRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.CreateBackendTargetResponse`
        """
        http_info = self._create_backend_target_http_info(request)
        return self._call_api(**http_info)

    def create_backend_target_async_invoker(self, request):
        http_info = self._create_backend_target_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_backend_target_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares/{share_id}/targets",
            "request_type": request.__class__.__name__,
            "response_type": "CreateBackendTargetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def create_fs_dir_async(self, request):
        """创建目录

        创建目录
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateFsDir
        :type request: :class:`huaweicloudsdksfsturbo.v1.CreateFsDirRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.CreateFsDirResponse`
        """
        http_info = self._create_fs_dir_http_info(request)
        return self._call_api(**http_info)

    def create_fs_dir_async_invoker(self, request):
        http_info = self._create_fs_dir_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_fs_dir_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares/{share_id}/fs/dir",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFsDirResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

        query_params = []

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

    def create_fs_dir_quota_async(self, request):
        """创建目标文件夹quota

        创建目标文件夹quota。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateFsDirQuota
        :type request: :class:`huaweicloudsdksfsturbo.v1.CreateFsDirQuotaRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.CreateFsDirQuotaResponse`
        """
        http_info = self._create_fs_dir_quota_http_info(request)
        return self._call_api(**http_info)

    def create_fs_dir_quota_async_invoker(self, request):
        http_info = self._create_fs_dir_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_fs_dir_quota_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares/{share_id}/fs/dir-quota",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFsDirQuotaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

        query_params = []

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

    def create_fs_task_async(self, request):
        """创建文件系统异步任务

        创建文件系统异步任务（该接口目前仅支持“华南-广州-友好用户环境”，“华南-广州”，“华南-深圳”，“西南-贵阳一”，“华北-乌兰察布一”，“华北-北京一”，“华北-北京二”，“华北-北京四”，“华东-上海一”）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateFsTask
        :type request: :class:`huaweicloudsdksfsturbo.v1.CreateFsTaskRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.CreateFsTaskResponse`
        """
        http_info = self._create_fs_task_http_info(request)
        return self._call_api(**http_info)

    def create_fs_task_async_invoker(self, request):
        http_info = self._create_fs_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_fs_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares/{share_id}/fs/{feature}/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFsTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']
        if 'feature' in local_var_params:
            path_params['feature'] = local_var_params['feature']

        query_params = []

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

    def create_hpc_cache_task_async(self, request):
        """创建SFSTurbo 和 OBS 之间的联动任务

        创建SFSTurbo 和 OBS 之间的联动任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateHpcCacheTask
        :type request: :class:`huaweicloudsdksfsturbo.v1.CreateHpcCacheTaskRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.CreateHpcCacheTaskResponse`
        """
        http_info = self._create_hpc_cache_task_http_info(request)
        return self._call_api(**http_info)

    def create_hpc_cache_task_async_invoker(self, request):
        http_info = self._create_hpc_cache_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_hpc_cache_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/sfs-turbo/{share_id}/hpc-cache/task",
            "request_type": request.__class__.__name__,
            "response_type": "CreateHpcCacheTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def create_perm_rule_async(self, request):
        """创建权限规则

        创建权限规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePermRule
        :type request: :class:`huaweicloudsdksfsturbo.v1.CreatePermRuleRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.CreatePermRuleResponse`
        """
        http_info = self._create_perm_rule_http_info(request)
        return self._call_api(**http_info)

    def create_perm_rule_async_invoker(self, request):
        http_info = self._create_perm_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_perm_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares/{share_id}/fs/perm-rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePermRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

        query_params = []

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

    def create_share_async(self, request):
        """创建文件系统

        创建文件系统。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateShare
        :type request: :class:`huaweicloudsdksfsturbo.v1.CreateShareRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.CreateShareResponse`
        """
        http_info = self._create_share_http_info(request)
        return self._call_api(**http_info)

    def create_share_async_invoker(self, request):
        http_info = self._create_share_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_share_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares",
            "request_type": request.__class__.__name__,
            "response_type": "CreateShareResponse"
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

    def create_shared_tag_async(self, request):
        """创建共享标签

        指定共享添加一个标签。
        一个共享上最多有10个标签。
        一个共享上的多个标签的key不允许重复。
        此接口为幂等接口：如果要添加的key在共享上已存在，则覆盖更新标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSharedTag
        :type request: :class:`huaweicloudsdksfsturbo.v1.CreateSharedTagRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.CreateSharedTagResponse`
        """
        http_info = self._create_shared_tag_http_info(request)
        return self._call_api(**http_info)

    def create_shared_tag_async_invoker(self, request):
        http_info = self._create_shared_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_shared_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/sfs-turbo/{share_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSharedTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

        query_params = []

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

    def delete_backend_target_async(self, request):
        """删除文件系统后端存储库

        删除文件系统后端存储库
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBackendTarget
        :type request: :class:`huaweicloudsdksfsturbo.v1.DeleteBackendTargetRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.DeleteBackendTargetResponse`
        """
        http_info = self._delete_backend_target_http_info(request)
        return self._call_api(**http_info)

    def delete_backend_target_async_invoker(self, request):
        http_info = self._delete_backend_target_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_backend_target_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares/{share_id}/targets/{target_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBackendTargetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']
        if 'target_id' in local_var_params:
            path_params['target_id'] = local_var_params['target_id']

        query_params = []
        if 'delete_data_in_file_system' in local_var_params:
            query_params.append(('delete_data_in_file_system', local_var_params['delete_data_in_file_system']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_fs_dir_async(self, request):
        """删除文件系统目录

        删除文件系统目录
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteFsDir
        :type request: :class:`huaweicloudsdksfsturbo.v1.DeleteFsDirRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.DeleteFsDirResponse`
        """
        http_info = self._delete_fs_dir_http_info(request)
        return self._call_api(**http_info)

    def delete_fs_dir_async_invoker(self, request):
        http_info = self._delete_fs_dir_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_fs_dir_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares/{share_id}/fs/dir",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteFsDirResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

        query_params = []

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

    def delete_fs_dir_quota_async(self, request):
        """删除目标文件夹quota

        删除目标文件夹quota。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteFsDirQuota
        :type request: :class:`huaweicloudsdksfsturbo.v1.DeleteFsDirQuotaRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.DeleteFsDirQuotaResponse`
        """
        http_info = self._delete_fs_dir_quota_http_info(request)
        return self._call_api(**http_info)

    def delete_fs_dir_quota_async_invoker(self, request):
        http_info = self._delete_fs_dir_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_fs_dir_quota_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares/{share_id}/fs/dir-quota",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteFsDirQuotaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

        query_params = []

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

    def delete_fs_task_async(self, request):
        """取消/删除文件系统异步任务

        如果异步任务正在执行，则取消并删除任务；否则，删除任务。（该接口目前仅支持“华南-广州-友好用户环境”，“华南-广州”，“华南-深圳”，“西南-贵阳一”，“华北-乌兰察布一”，“华北-北京一”，“华北-北京二”，“华北-北京四”，“华东-上海一”）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteFsTask
        :type request: :class:`huaweicloudsdksfsturbo.v1.DeleteFsTaskRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.DeleteFsTaskResponse`
        """
        http_info = self._delete_fs_task_http_info(request)
        return self._call_api(**http_info)

    def delete_fs_task_async_invoker(self, request):
        http_info = self._delete_fs_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_fs_task_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares/{share_id}/fs/{feature}/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteFsTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']
        if 'feature' in local_var_params:
            path_params['feature'] = local_var_params['feature']
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

    def delete_perm_rule_async(self, request):
        """删除权限规则

        删除权限规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePermRule
        :type request: :class:`huaweicloudsdksfsturbo.v1.DeletePermRuleRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.DeletePermRuleResponse`
        """
        http_info = self._delete_perm_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_perm_rule_async_invoker(self, request):
        http_info = self._delete_perm_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_perm_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares/{share_id}/fs/perm-rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePermRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_share_async(self, request):
        """删除文件系统

        删除文件系统。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteShare
        :type request: :class:`huaweicloudsdksfsturbo.v1.DeleteShareRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.DeleteShareResponse`
        """
        http_info = self._delete_share_http_info(request)
        return self._call_api(**http_info)

    def delete_share_async_invoker(self, request):
        http_info = self._delete_share_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_share_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares/{share_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteShareResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_shared_tag_async(self, request):
        """删除共享标签

        指定共享删除一个标签。当共享中不存在指定要删除的key时，接口调用将会返回404错误。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSharedTag
        :type request: :class:`huaweicloudsdksfsturbo.v1.DeleteSharedTagRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.DeleteSharedTagResponse`
        """
        http_info = self._delete_shared_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_shared_tag_async_invoker(self, request):
        http_info = self._delete_shared_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_shared_tag_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/sfs-turbo/{share_id}/tags/{key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSharedTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']
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

    def expand_share_async(self, request):
        """扩容文件系统

        扩容文件系统。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExpandShare
        :type request: :class:`huaweicloudsdksfsturbo.v1.ExpandShareRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ExpandShareResponse`
        """
        http_info = self._expand_share_http_info(request)
        return self._call_api(**http_info)

    def expand_share_async_invoker(self, request):
        http_info = self._expand_share_http_info(request)
        return AsyncInvoker(self, http_info)

    def _expand_share_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares/{share_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "ExpandShareResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

        query_params = []

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

    def list_backend_targets_async(self, request):
        """查询文件系统后端存储库列表

        查询文件系统后端存储库列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBackendTargets
        :type request: :class:`huaweicloudsdksfsturbo.v1.ListBackendTargetsRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ListBackendTargetsResponse`
        """
        http_info = self._list_backend_targets_http_info(request)
        return self._call_api(**http_info)

    def list_backend_targets_async_invoker(self, request):
        http_info = self._list_backend_targets_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_backend_targets_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares/{share_id}/targets",
            "request_type": request.__class__.__name__,
            "response_type": "ListBackendTargetsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

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

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_fs_tasks_async(self, request):
        """获取文件系统异步任务列表

        获取文件系统异步任务列表（该接口目前仅支持“华南-广州-友好用户环境”，“华南-广州”，“华南-深圳”，“西南-贵阳一”，“华北-乌兰察布一”，“华北-北京一”，“华北-北京二”，“华北-北京四”，“华东-上海一”）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFsTasks
        :type request: :class:`huaweicloudsdksfsturbo.v1.ListFsTasksRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ListFsTasksResponse`
        """
        http_info = self._list_fs_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_fs_tasks_async_invoker(self, request):
        http_info = self._list_fs_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_fs_tasks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares/{share_id}/fs/{feature}/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListFsTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']
        if 'feature' in local_var_params:
            path_params['feature'] = local_var_params['feature']

        query_params = []
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

    def list_hpc_cache_tasks_async(self, request):
        """查询联动任务详情列表

        查询联动任务详情列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHpcCacheTasks
        :type request: :class:`huaweicloudsdksfsturbo.v1.ListHpcCacheTasksRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ListHpcCacheTasksResponse`
        """
        http_info = self._list_hpc_cache_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_hpc_cache_tasks_async_invoker(self, request):
        http_info = self._list_hpc_cache_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_hpc_cache_tasks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/sfs-turbo/{share_id}/hpc-cache/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListHpcCacheTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
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

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_perm_rules_async(self, request):
        """查询文件系统的权限规则列表

        查询文件系统的权限规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPermRules
        :type request: :class:`huaweicloudsdksfsturbo.v1.ListPermRulesRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ListPermRulesResponse`
        """
        http_info = self._list_perm_rules_http_info(request)
        return self._call_api(**http_info)

    def list_perm_rules_async_invoker(self, request):
        http_info = self._list_perm_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_perm_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares/{share_id}/fs/perm-rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListPermRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_shared_tags_async(self, request):
        """查询租户所有共享的标签

        查询租户所有共享的标签集合。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSharedTags
        :type request: :class:`huaweicloudsdksfsturbo.v1.ListSharedTagsRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ListSharedTagsResponse`
        """
        http_info = self._list_shared_tags_http_info(request)
        return self._call_api(**http_info)

    def list_shared_tags_async_invoker(self, request):
        http_info = self._list_shared_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_shared_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/sfs-turbo/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListSharedTagsResponse"
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

    def list_shares_async(self, request):
        """获取文件系统列表

        获取文件系统列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListShares
        :type request: :class:`huaweicloudsdksfsturbo.v1.ListSharesRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ListSharesResponse`
        """
        http_info = self._list_shares_http_info(request)
        return self._call_api(**http_info)

    def list_shares_async_invoker(self, request):
        http_info = self._list_shares_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_shares_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ListSharesResponse"
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

    def set_hpc_cache_backend_async(self, request):
        """配置hpc缓存型后端信息

        配置hpc缓存型后端信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetHpcCacheBackend
        :type request: :class:`huaweicloudsdksfsturbo.v1.SetHpcCacheBackendRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.SetHpcCacheBackendResponse`
        """
        http_info = self._set_hpc_cache_backend_http_info(request)
        return self._call_api(**http_info)

    def set_hpc_cache_backend_async_invoker(self, request):
        http_info = self._set_hpc_cache_backend_http_info(request)
        return AsyncInvoker(self, http_info)

    def _set_hpc_cache_backend_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares/{share_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "SetHpcCacheBackendResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_backend_target_info_async(self, request):
        """获取文件系统后端存储库详细信息

        获取文件系统后端存储库详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBackendTargetInfo
        :type request: :class:`huaweicloudsdksfsturbo.v1.ShowBackendTargetInfoRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ShowBackendTargetInfoResponse`
        """
        http_info = self._show_backend_target_info_http_info(request)
        return self._call_api(**http_info)

    def show_backend_target_info_async_invoker(self, request):
        http_info = self._show_backend_target_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_backend_target_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares/{share_id}/targets/{target_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBackendTargetInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']
        if 'target_id' in local_var_params:
            path_params['target_id'] = local_var_params['target_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_fs_dir_async(self, request):
        """查询目录是否存在

        查询目录是否存在
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowFsDir
        :type request: :class:`huaweicloudsdksfsturbo.v1.ShowFsDirRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ShowFsDirResponse`
        """
        http_info = self._show_fs_dir_http_info(request)
        return self._call_api(**http_info)

    def show_fs_dir_async_invoker(self, request):
        http_info = self._show_fs_dir_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_fs_dir_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares/{share_id}/fs/dir",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFsDirResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

        query_params = []
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_fs_dir_quota_async(self, request):
        """查询目标文件夹quota

        查询目标文件夹quota
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowFsDirQuota
        :type request: :class:`huaweicloudsdksfsturbo.v1.ShowFsDirQuotaRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ShowFsDirQuotaResponse`
        """
        http_info = self._show_fs_dir_quota_http_info(request)
        return self._call_api(**http_info)

    def show_fs_dir_quota_async_invoker(self, request):
        http_info = self._show_fs_dir_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_fs_dir_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares/{share_id}/fs/dir-quota",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFsDirQuotaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

        query_params = []
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_fs_dir_usage_async(self, request):
        """查询目录资源使用情况

        查询目录资源使用情况(包括子目录的资源)。后端有5min的缓存时间，查询的数据可能有延迟。（该接口目前仅支持“华南-广州-友好用户环境”，“华南-广州”，“华南-深圳”，“西南-贵阳一”，“华北-乌兰察布一”，“华北-北京一”，“华北-北京二”，“华北-北京四”，“华东-上海一”）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowFsDirUsage
        :type request: :class:`huaweicloudsdksfsturbo.v1.ShowFsDirUsageRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ShowFsDirUsageResponse`
        """
        http_info = self._show_fs_dir_usage_http_info(request)
        return self._call_api(**http_info)

    def show_fs_dir_usage_async_invoker(self, request):
        http_info = self._show_fs_dir_usage_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_fs_dir_usage_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares/{share_id}/fs/dir-usage",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFsDirUsageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

        query_params = []
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_fs_task_async(self, request):
        """获取文件系统异步任务详情

        获取文件系统异步任务详情（该接口目前仅支持“华南-广州-友好用户环境”，“华南-广州”，“华南-深圳”，“西南-贵阳一”，“华北-乌兰察布一”，“华北-北京一”，“华北-北京二”，“华北-北京四”，“华东-上海一”）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowFsTask
        :type request: :class:`huaweicloudsdksfsturbo.v1.ShowFsTaskRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ShowFsTaskResponse`
        """
        http_info = self._show_fs_task_http_info(request)
        return self._call_api(**http_info)

    def show_fs_task_async_invoker(self, request):
        http_info = self._show_fs_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_fs_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares/{share_id}/fs/{feature}/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFsTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']
        if 'feature' in local_var_params:
            path_params['feature'] = local_var_params['feature']
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

    def show_hpc_cache_task_async(self, request):
        """查询联动任务详情

        查询联动任务详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHpcCacheTask
        :type request: :class:`huaweicloudsdksfsturbo.v1.ShowHpcCacheTaskRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ShowHpcCacheTaskResponse`
        """
        http_info = self._show_hpc_cache_task_http_info(request)
        return self._call_api(**http_info)

    def show_hpc_cache_task_async_invoker(self, request):
        http_info = self._show_hpc_cache_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_hpc_cache_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/sfs-turbo/{share_id}/hpc-cache/task/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHpcCacheTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_perm_rule_async(self, request):
        """查询文件系统的某一个权限规则

        查询文件系统的某一个权限规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPermRule
        :type request: :class:`huaweicloudsdksfsturbo.v1.ShowPermRuleRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ShowPermRuleResponse`
        """
        http_info = self._show_perm_rule_http_info(request)
        return self._call_api(**http_info)

    def show_perm_rule_async_invoker(self, request):
        http_info = self._show_perm_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_perm_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares/{share_id}/fs/perm-rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPermRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_share_async(self, request):
        """查询文件系统详细信息

        查询SFS Turbo文件系统详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowShare
        :type request: :class:`huaweicloudsdksfsturbo.v1.ShowShareRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ShowShareResponse`
        """
        http_info = self._show_share_http_info(request)
        return self._call_api(**http_info)

    def show_share_async_invoker(self, request):
        http_info = self._show_share_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_share_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares/{share_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowShareResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_shared_tags_async(self, request):
        """查询共享标签

        查询指定共享的所有标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSharedTags
        :type request: :class:`huaweicloudsdksfsturbo.v1.ShowSharedTagsRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ShowSharedTagsResponse`
        """
        http_info = self._show_shared_tags_http_info(request)
        return self._call_api(**http_info)

    def show_shared_tags_async_invoker(self, request):
        http_info = self._show_shared_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_shared_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/sfs-turbo/{share_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSharedTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_fs_dir_quota_async(self, request):
        """更新目标文件夹quota

        更新目标文件夹quota
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateFsDirQuota
        :type request: :class:`huaweicloudsdksfsturbo.v1.UpdateFsDirQuotaRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.UpdateFsDirQuotaResponse`
        """
        http_info = self._update_fs_dir_quota_http_info(request)
        return self._call_api(**http_info)

    def update_fs_dir_quota_async_invoker(self, request):
        http_info = self._update_fs_dir_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_fs_dir_quota_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares/{share_id}/fs/dir-quota",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateFsDirQuotaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

        query_params = []

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

    def update_hpc_share_async(self, request):
        """更新文件系统

        设置文件系统冷数据淘汰时间
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateHpcShare
        :type request: :class:`huaweicloudsdksfsturbo.v1.UpdateHpcShareRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.UpdateHpcShareResponse`
        """
        http_info = self._update_hpc_share_http_info(request)
        return self._call_api(**http_info)

    def update_hpc_share_async_invoker(self, request):
        http_info = self._update_hpc_share_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_hpc_share_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares/{share_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHpcShareResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def update_perm_rule_async(self, request):
        """修改权限规则

        修改权限规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePermRule
        :type request: :class:`huaweicloudsdksfsturbo.v1.UpdatePermRuleRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.UpdatePermRuleResponse`
        """
        http_info = self._update_perm_rule_http_info(request)
        return self._call_api(**http_info)

    def update_perm_rule_async_invoker(self, request):
        http_info = self._update_perm_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_perm_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/sfs-turbo/shares/{share_id}/fs/perm-rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePermRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

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
