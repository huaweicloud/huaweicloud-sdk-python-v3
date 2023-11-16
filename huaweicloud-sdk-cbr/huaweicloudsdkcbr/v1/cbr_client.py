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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcbr'")


class CbrClient(Client):
    def __init__(self):
        super(CbrClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcbr.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CbrClient":
                raise TypeError("client type error, support client type is CbrClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_agent_path(self, request):
        """新增备份路径

        对客户端新增备份路径，新增的路径不会校验是否存在。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddAgentPath
        :type request: :class:`huaweicloudsdkcbr.v1.AddAgentPathRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.AddAgentPathResponse`
        """
        http_info = self._add_agent_path_http_info(request)
        return self._call_api(**http_info)

    def add_agent_path_invoker(self, request):
        http_info = self._add_agent_path_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_agent_path_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/agents/{agent_id}/add-path",
            "request_type": request.__class__.__name__,
            "response_type": "AddAgentPathResponse"
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

    def add_member(self, request):
        """添加备份成员

        添加备份可共享的成员，只有云服务器备份可以添加备份共享成员，且仅支持在同一区域的不同用户间共享。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddMember
        :type request: :class:`huaweicloudsdkcbr.v1.AddMemberRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.AddMemberResponse`
        """
        http_info = self._add_member_http_info(request)
        return self._call_api(**http_info)

    def add_member_invoker(self, request):
        http_info = self._add_member_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_member_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/backups/{backup_id}/members",
            "request_type": request.__class__.__name__,
            "response_type": "AddMemberResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']

        query_params = []

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

    def add_vault_resource(self, request):
        """添加资源

        存储库添加资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddVaultResource
        :type request: :class:`huaweicloudsdkcbr.v1.AddVaultResourceRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.AddVaultResourceResponse`
        """
        http_info = self._add_vault_resource_http_info(request)
        return self._call_api(**http_info)

    def add_vault_resource_invoker(self, request):
        http_info = self._add_vault_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_vault_resource_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/vaults/{vault_id}/addresources",
            "request_type": request.__class__.__name__,
            "response_type": "AddVaultResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vault_id' in local_var_params:
            path_params['vault_id'] = local_var_params['vault_id']

        query_params = []

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

    def associate_vault_policy(self, request):
        """设置存储库策略

        存储库设置策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateVaultPolicy
        :type request: :class:`huaweicloudsdkcbr.v1.AssociateVaultPolicyRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.AssociateVaultPolicyResponse`
        """
        http_info = self._associate_vault_policy_http_info(request)
        return self._call_api(**http_info)

    def associate_vault_policy_invoker(self, request):
        http_info = self._associate_vault_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _associate_vault_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/vaults/{vault_id}/associatepolicy",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateVaultPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vault_id' in local_var_params:
            path_params['vault_id'] = local_var_params['vault_id']

        query_params = []

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

    def batch_create_and_delete_vault_tags(self, request):
        """批量添加删除存储库资源标签

        为指定实例批量添加或删除标签
        标签管理服务需要使用该接口批量管理实例的标签。
        一个资源上最多有10个标签。
        此接口为幂等接口：
            创建时如果请求体中存在重复key则报错。
            创建时，不允许重复key，如果数据库存在就覆盖。
            删除时，允许重复key。
            删除时，如果删除的标签不存在，默认处理成功,删除时不对标签字符集范围做校验。key长度127个字符，value为255个字符。删除时tags结构体不能缺失，key不能为空，或者空字符串。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateAndDeleteVaultTags
        :type request: :class:`huaweicloudsdkcbr.v1.BatchCreateAndDeleteVaultTagsRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.BatchCreateAndDeleteVaultTagsResponse`
        """
        http_info = self._batch_create_and_delete_vault_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_and_delete_vault_tags_invoker(self, request):
        http_info = self._batch_create_and_delete_vault_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_and_delete_vault_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/vault/{vault_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateAndDeleteVaultTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vault_id' in local_var_params:
            path_params['vault_id'] = local_var_params['vault_id']

        query_params = []

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

    def batch_update_vault(self, request):
        """批量修改存储库

        批量修改项目下所有存储库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateVault
        :type request: :class:`huaweicloudsdkcbr.v1.BatchUpdateVaultRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.BatchUpdateVaultResponse`
        """
        http_info = self._batch_update_vault_http_info(request)
        return self._call_api(**http_info)

    def batch_update_vault_invoker(self, request):
        http_info = self._batch_update_vault_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_update_vault_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/vaults/batch-update",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateVaultResponse"
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

    def check_agent(self, request):
        """查询agent状态

        检查应用一致性Agent状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckAgent
        :type request: :class:`huaweicloudsdkcbr.v1.CheckAgentRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.CheckAgentResponse`
        """
        http_info = self._check_agent_http_info(request)
        return self._call_api(**http_info)

    def check_agent_invoker(self, request):
        http_info = self._check_agent_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_agent_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/agent/check",
            "request_type": request.__class__.__name__,
            "response_type": "CheckAgentResponse"
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

    def copy_backup(self, request):
        """复制备份

        跨区域复制备份。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CopyBackup
        :type request: :class:`huaweicloudsdkcbr.v1.CopyBackupRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.CopyBackupResponse`
        """
        http_info = self._copy_backup_http_info(request)
        return self._call_api(**http_info)

    def copy_backup_invoker(self, request):
        http_info = self._copy_backup_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _copy_backup_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/backups/{backup_id}/replicate",
            "request_type": request.__class__.__name__,
            "response_type": "CopyBackupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']

        query_params = []

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

    def copy_checkpoint(self, request):
        """复制备份还原点

        执行复制
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CopyCheckpoint
        :type request: :class:`huaweicloudsdkcbr.v1.CopyCheckpointRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.CopyCheckpointResponse`
        """
        http_info = self._copy_checkpoint_http_info(request)
        return self._call_api(**http_info)

    def copy_checkpoint_invoker(self, request):
        http_info = self._copy_checkpoint_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _copy_checkpoint_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/checkpoints/replicate",
            "request_type": request.__class__.__name__,
            "response_type": "CopyCheckpointResponse"
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

    def create_checkpoint(self, request):
        """创建备份还原点

        对存储库执行备份，生成备份还原点
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCheckpoint
        :type request: :class:`huaweicloudsdkcbr.v1.CreateCheckpointRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.CreateCheckpointResponse`
        """
        http_info = self._create_checkpoint_http_info(request)
        return self._call_api(**http_info)

    def create_checkpoint_invoker(self, request):
        http_info = self._create_checkpoint_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_checkpoint_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/checkpoints",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCheckpointResponse"
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

    def create_policy(self, request):
        """创建策略

        创建策略，策略分为备份策略和复制策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePolicy
        :type request: :class:`huaweicloudsdkcbr.v1.CreatePolicyRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.CreatePolicyResponse`
        """
        http_info = self._create_policy_http_info(request)
        return self._call_api(**http_info)

    def create_policy_invoker(self, request):
        http_info = self._create_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/policies",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePolicyResponse"
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

    def create_post_paid_vault(self, request):
        """创建包周期存储库

        创建包周期存储库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePostPaidVault
        :type request: :class:`huaweicloudsdkcbr.v1.CreatePostPaidVaultRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.CreatePostPaidVaultResponse`
        """
        http_info = self._create_post_paid_vault_http_info(request)
        return self._call_api(**http_info)

    def create_post_paid_vault_invoker(self, request):
        http_info = self._create_post_paid_vault_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_post_paid_vault_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/vaults/order",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePostPaidVaultResponse"
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

    def create_vault(self, request):
        """创建存储库

        创建存储库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateVault
        :type request: :class:`huaweicloudsdkcbr.v1.CreateVaultRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.CreateVaultResponse`
        """
        http_info = self._create_vault_http_info(request)
        return self._call_api(**http_info)

    def create_vault_invoker(self, request):
        http_info = self._create_vault_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_vault_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/vaults",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVaultResponse"
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

    def create_vault_tags(self, request):
        """添加存储库资源标签

        一个资源上最多有10个标签。
        此接口为幂等接口：创建时，如果创建的标签已经存在（key相同），则覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateVaultTags
        :type request: :class:`huaweicloudsdkcbr.v1.CreateVaultTagsRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.CreateVaultTagsResponse`
        """
        http_info = self._create_vault_tags_http_info(request)
        return self._call_api(**http_info)

    def create_vault_tags_invoker(self, request):
        http_info = self._create_vault_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_vault_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/vault/{vault_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVaultTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vault_id' in local_var_params:
            path_params['vault_id'] = local_var_params['vault_id']

        query_params = []

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

    def delete_backup(self, request):
        """删除备份

        删除单个备份。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBackup
        :type request: :class:`huaweicloudsdkcbr.v1.DeleteBackupRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.DeleteBackupResponse`
        """
        http_info = self._delete_backup_http_info(request)
        return self._call_api(**http_info)

    def delete_backup_invoker(self, request):
        http_info = self._delete_backup_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_backup_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/backups/{backup_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBackupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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
        """删除指定备份成员

        删除指定的备份共享成员
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteMember
        :type request: :class:`huaweicloudsdkcbr.v1.DeleteMemberRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.DeleteMemberResponse`
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
            "resource_path": "/v3/{project_id}/backups/{backup_id}/members/{member_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMemberResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']
        if 'member_id' in local_var_params:
            path_params['member_id'] = local_var_params['member_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_policy(self, request):
        """删除策略

        删除策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePolicy
        :type request: :class:`huaweicloudsdkcbr.v1.DeletePolicyRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.DeletePolicyResponse`
        """
        http_info = self._delete_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_policy_invoker(self, request):
        http_info = self._delete_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_policy_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_vault(self, request):
        """删除存储库

        删除存储库。若删除储存库，将一并删除存储库中的所有备份。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteVault
        :type request: :class:`huaweicloudsdkcbr.v1.DeleteVaultRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.DeleteVaultResponse`
        """
        http_info = self._delete_vault_http_info(request)
        return self._call_api(**http_info)

    def delete_vault_invoker(self, request):
        http_info = self._delete_vault_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_vault_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/vaults/{vault_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVaultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vault_id' in local_var_params:
            path_params['vault_id'] = local_var_params['vault_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_vault_tag(self, request):
        """删除存储库资源标签

        幂等接口：删除时，如果删除的标签不存在，返回404。Key不能为空或者空字符串。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteVaultTag
        :type request: :class:`huaweicloudsdkcbr.v1.DeleteVaultTagRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.DeleteVaultTagResponse`
        """
        http_info = self._delete_vault_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_vault_tag_invoker(self, request):
        http_info = self._delete_vault_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_vault_tag_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/vault/{vault_id}/tags/{key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVaultTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']
        if 'vault_id' in local_var_params:
            path_params['vault_id'] = local_var_params['vault_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def disassociate_vault_policy(self, request):
        """解除存储库策略

        存储库解除策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisassociateVaultPolicy
        :type request: :class:`huaweicloudsdkcbr.v1.DisassociateVaultPolicyRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.DisassociateVaultPolicyResponse`
        """
        http_info = self._disassociate_vault_policy_http_info(request)
        return self._call_api(**http_info)

    def disassociate_vault_policy_invoker(self, request):
        http_info = self._disassociate_vault_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disassociate_vault_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/vaults/{vault_id}/dissociatepolicy",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateVaultPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vault_id' in local_var_params:
            path_params['vault_id'] = local_var_params['vault_id']

        query_params = []

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

    def import_backup(self, request):
        """同步备份

        同步线下混合云VMware备份副本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportBackup
        :type request: :class:`huaweicloudsdkcbr.v1.ImportBackupRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.ImportBackupResponse`
        """
        http_info = self._import_backup_http_info(request)
        return self._call_api(**http_info)

    def import_backup_invoker(self, request):
        http_info = self._import_backup_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_backup_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/backups/sync",
            "request_type": request.__class__.__name__,
            "response_type": "ImportBackupResponse"
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

    def import_checkpoint(self, request):
        """同步备份还原点

        针对vault同步备份副本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportCheckpoint
        :type request: :class:`huaweicloudsdkcbr.v1.ImportCheckpointRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.ImportCheckpointResponse`
        """
        http_info = self._import_checkpoint_http_info(request)
        return self._call_api(**http_info)

    def import_checkpoint_invoker(self, request):
        http_info = self._import_checkpoint_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_checkpoint_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/checkpoints/sync",
            "request_type": request.__class__.__name__,
            "response_type": "ImportCheckpointResponse"
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

    def list_agent(self, request):
        """查询客户端列表

        查询客户端列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAgent
        :type request: :class:`huaweicloudsdkcbr.v1.ListAgentRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.ListAgentResponse`
        """
        http_info = self._list_agent_http_info(request)
        return self._call_api(**http_info)

    def list_agent_invoker(self, request):
        http_info = self._list_agent_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_agent_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/agents",
            "request_type": request.__class__.__name__,
            "response_type": "ListAgentResponse"
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
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'agent_id' in local_var_params:
            query_params.append(('agent_id', local_var_params['agent_id']))
            collection_formats['agent_id'] = 'csv'

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_backups(self, request):
        """查询所有备份

        查询所有副本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBackups
        :type request: :class:`huaweicloudsdkcbr.v1.ListBackupsRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.ListBackupsResponse`
        """
        http_info = self._list_backups_http_info(request)
        return self._call_api(**http_info)

    def list_backups_invoker(self, request):
        http_info = self._list_backups_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_backups_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/backups",
            "request_type": request.__class__.__name__,
            "response_type": "ListBackupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'checkpoint_id' in local_var_params:
            query_params.append(('checkpoint_id', local_var_params['checkpoint_id']))
        if 'dec' in local_var_params:
            query_params.append(('dec', local_var_params['dec']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'image_type' in local_var_params:
            query_params.append(('image_type', local_var_params['image_type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'resource_az' in local_var_params:
            query_params.append(('resource_az', local_var_params['resource_az']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'resource_name' in local_var_params:
            query_params.append(('resource_name', local_var_params['resource_name']))
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'vault_id' in local_var_params:
            query_params.append(('vault_id', local_var_params['vault_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'own_type' in local_var_params:
            query_params.append(('own_type', local_var_params['own_type']))
        if 'member_status' in local_var_params:
            query_params.append(('member_status', local_var_params['member_status']))
        if 'parent_id' in local_var_params:
            query_params.append(('parent_id', local_var_params['parent_id']))
        if 'used_percent' in local_var_params:
            query_params.append(('used_percent', local_var_params['used_percent']))
        if 'show_replication' in local_var_params:
            query_params.append(('show_replication', local_var_params['show_replication']))
        if 'incremental' in local_var_params:
            query_params.append(('incremental', local_var_params['incremental']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_domain_projects(self, request):
        """查询租户项目列表

        根据指定租户名称查询项目列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDomainProjects
        :type request: :class:`huaweicloudsdkcbr.v1.ListDomainProjectsRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.ListDomainProjectsResponse`
        """
        http_info = self._list_domain_projects_http_info(request)
        return self._call_api(**http_info)

    def list_domain_projects_invoker(self, request):
        http_info = self._list_domain_projects_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_domain_projects_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/domain/{domain_name}/projects",
            "request_type": request.__class__.__name__,
            "response_type": "ListDomainProjectsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_name' in local_var_params:
            path_params['domain_name'] = local_var_params['domain_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_external_vault(self, request):
        """查询其他区域存储库列表

        查询其他区域的存储库列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListExternalVault
        :type request: :class:`huaweicloudsdkcbr.v1.ListExternalVaultRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.ListExternalVaultResponse`
        """
        http_info = self._list_external_vault_http_info(request)
        return self._call_api(**http_info)

    def list_external_vault_invoker(self, request):
        http_info = self._list_external_vault_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_external_vault_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/vaults/external",
            "request_type": request.__class__.__name__,
            "response_type": "ListExternalVaultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'external_project_id' in local_var_params:
            query_params.append(('external_project_id', local_var_params['external_project_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'protect_type' in local_var_params:
            query_params.append(('protect_type', local_var_params['protect_type']))
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'objcet_type' in local_var_params:
            query_params.append(('objcet_type', local_var_params['objcet_type']))
        if 'cloud_type' in local_var_params:
            query_params.append(('cloud_type', local_var_params['cloud_type']))
        if 'vault_id' in local_var_params:
            query_params.append(('vault_id', local_var_params['vault_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_op_logs(self, request):
        """查询任务列表

        查询任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOpLogs
        :type request: :class:`huaweicloudsdkcbr.v1.ListOpLogsRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.ListOpLogsResponse`
        """
        http_info = self._list_op_logs_http_info(request)
        return self._call_api(**http_info)

    def list_op_logs_invoker(self, request):
        http_info = self._list_op_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_op_logs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/operation-logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListOpLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'operation_type' in local_var_params:
            query_params.append(('operation_type', local_var_params['operation_type']))
        if 'provider_id' in local_var_params:
            query_params.append(('provider_id', local_var_params['provider_id']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'resource_name' in local_var_params:
            query_params.append(('resource_name', local_var_params['resource_name']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'vault_id' in local_var_params:
            query_params.append(('vault_id', local_var_params['vault_id']))
        if 'vault_name' in local_var_params:
            query_params.append(('vault_name', local_var_params['vault_name']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_policies(self, request):
        """查询策略列表

        查询策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPolicies
        :type request: :class:`huaweicloudsdkcbr.v1.ListPoliciesRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.ListPoliciesResponse`
        """
        http_info = self._list_policies_http_info(request)
        return self._call_api(**http_info)

    def list_policies_invoker(self, request):
        http_info = self._list_policies_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_policies_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListPoliciesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'operation_type' in local_var_params:
            query_params.append(('operation_type', local_var_params['operation_type']))
        if 'vault_id' in local_var_params:
            query_params.append(('vault_id', local_var_params['vault_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_projects(self, request):
        """查询租户的项目信息

        查询租户的企业项目信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjects
        :type request: :class:`huaweicloudsdkcbr.v1.ListProjectsRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.ListProjectsResponse`
        """
        http_info = self._list_projects_http_info(request)
        return self._call_api(**http_info)

    def list_projects_invoker(self, request):
        http_info = self._list_projects_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_projects_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/region-projects",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectsResponse"
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

    def list_protectable(self, request):
        """查询可保护资源

        查询可保护性资源列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProtectable
        :type request: :class:`huaweicloudsdkcbr.v1.ListProtectableRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.ListProtectableResponse`
        """
        http_info = self._list_protectable_http_info(request)
        return self._call_api(**http_info)

    def list_protectable_invoker(self, request):
        http_info = self._list_protectable_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_protectable_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/protectables/{protectable_type}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListProtectableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'protectable_type' in local_var_params:
            path_params['protectable_type'] = local_var_params['protectable_type']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'server_id' in local_var_params:
            query_params.append(('server_id', local_var_params['server_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_vault(self, request):
        """查询存储库列表

        查询存储库列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVault
        :type request: :class:`huaweicloudsdkcbr.v1.ListVaultRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.ListVaultResponse`
        """
        http_info = self._list_vault_http_info(request)
        return self._call_api(**http_info)

    def list_vault_invoker(self, request):
        http_info = self._list_vault_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_vault_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/vaults",
            "request_type": request.__class__.__name__,
            "response_type": "ListVaultResponse"
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
        if 'cloud_type' in local_var_params:
            query_params.append(('cloud_type', local_var_params['cloud_type']))
        if 'protect_type' in local_var_params:
            query_params.append(('protect_type', local_var_params['protect_type']))
        if 'object_type' in local_var_params:
            query_params.append(('object_type', local_var_params['object_type']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'csv'
        if 'policy_id' in local_var_params:
            query_params.append(('policy_id', local_var_params['policy_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'resource_ids' in local_var_params:
            query_params.append(('resource_ids', local_var_params['resource_ids']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def migrate_domain(self, request):
        """租户迁移

        将CSBS/VBS资源迁移到CBR。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for MigrateDomain
        :type request: :class:`huaweicloudsdkcbr.v1.MigrateDomainRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.MigrateDomainResponse`
        """
        http_info = self._migrate_domain_http_info(request)
        return self._call_api(**http_info)

    def migrate_domain_invoker(self, request):
        http_info = self._migrate_domain_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _migrate_domain_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/migrates",
            "request_type": request.__class__.__name__,
            "response_type": "MigrateDomainResponse"
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

    def migrate_vault_resource(self, request):
        """迁移资源

        支持资源迁移到另一个存储库，不删除备份。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for MigrateVaultResource
        :type request: :class:`huaweicloudsdkcbr.v1.MigrateVaultResourceRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.MigrateVaultResourceResponse`
        """
        http_info = self._migrate_vault_resource_http_info(request)
        return self._call_api(**http_info)

    def migrate_vault_resource_invoker(self, request):
        http_info = self._migrate_vault_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _migrate_vault_resource_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/vaults/{vault_id}/migrateresources",
            "request_type": request.__class__.__name__,
            "response_type": "MigrateVaultResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vault_id' in local_var_params:
            path_params['vault_id'] = local_var_params['vault_id']

        query_params = []

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

    def register_agent(self, request):
        """注册客户端

        注册客户端，安装时候由Agent调用，无需手动注册。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RegisterAgent
        :type request: :class:`huaweicloudsdkcbr.v1.RegisterAgentRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.RegisterAgentResponse`
        """
        http_info = self._register_agent_http_info(request)
        return self._call_api(**http_info)

    def register_agent_invoker(self, request):
        http_info = self._register_agent_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _register_agent_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/agents",
            "request_type": request.__class__.__name__,
            "response_type": "RegisterAgentResponse"
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

    def remove_agent_path(self, request):
        """移除备份路径

        移除已添加的文件备份路径。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RemoveAgentPath
        :type request: :class:`huaweicloudsdkcbr.v1.RemoveAgentPathRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.RemoveAgentPathResponse`
        """
        http_info = self._remove_agent_path_http_info(request)
        return self._call_api(**http_info)

    def remove_agent_path_invoker(self, request):
        http_info = self._remove_agent_path_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _remove_agent_path_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/agents/{agent_id}/remove-path",
            "request_type": request.__class__.__name__,
            "response_type": "RemoveAgentPathResponse"
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

    def remove_vault_resource(self, request):
        """移除资源

        移除存储库中的资源，若移除资源，将一并删除该资源在保管库中的备份
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RemoveVaultResource
        :type request: :class:`huaweicloudsdkcbr.v1.RemoveVaultResourceRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.RemoveVaultResourceResponse`
        """
        http_info = self._remove_vault_resource_http_info(request)
        return self._call_api(**http_info)

    def remove_vault_resource_invoker(self, request):
        http_info = self._remove_vault_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _remove_vault_resource_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/vaults/{vault_id}/removeresources",
            "request_type": request.__class__.__name__,
            "response_type": "RemoveVaultResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vault_id' in local_var_params:
            path_params['vault_id'] = local_var_params['vault_id']

        query_params = []

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

    def restore_backup(self, request):
        """备份恢复

        恢复备份数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestoreBackup
        :type request: :class:`huaweicloudsdkcbr.v1.RestoreBackupRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.RestoreBackupResponse`
        """
        http_info = self._restore_backup_http_info(request)
        return self._call_api(**http_info)

    def restore_backup_invoker(self, request):
        http_info = self._restore_backup_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restore_backup_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/backups/{backup_id}/restore",
            "request_type": request.__class__.__name__,
            "response_type": "RestoreBackupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']

        query_params = []

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

    def set_vault_resource(self, request):
        """设置存储库资源

        设置存储库资源是否自动备份
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetVaultResource
        :type request: :class:`huaweicloudsdkcbr.v1.SetVaultResourceRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.SetVaultResourceResponse`
        """
        http_info = self._set_vault_resource_http_info(request)
        return self._call_api(**http_info)

    def set_vault_resource_invoker(self, request):
        http_info = self._set_vault_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_vault_resource_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/vaults/{vault_id}/set-resources",
            "request_type": request.__class__.__name__,
            "response_type": "SetVaultResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vault_id' in local_var_params:
            path_params['vault_id'] = local_var_params['vault_id']

        query_params = []

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

    def show_agent(self, request):
        """查询指定客户端

        查询指定客户端
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAgent
        :type request: :class:`huaweicloudsdkcbr.v1.ShowAgentRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.ShowAgentResponse`
        """
        http_info = self._show_agent_http_info(request)
        return self._call_api(**http_info)

    def show_agent_invoker(self, request):
        http_info = self._show_agent_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_agent_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/agents/{agent_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAgentResponse"
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

    def show_backup(self, request):
        """查询指定备份

        根据指定id查询单个副本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBackup
        :type request: :class:`huaweicloudsdkcbr.v1.ShowBackupRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.ShowBackupResponse`
        """
        http_info = self._show_backup_http_info(request)
        return self._call_api(**http_info)

    def show_backup_invoker(self, request):
        http_info = self._show_backup_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_backup_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/backups/{backup_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBackupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_checkpoint(self, request):
        """查询备份还原点

        根据还原点ID查询指定还原点
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCheckpoint
        :type request: :class:`huaweicloudsdkcbr.v1.ShowCheckpointRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.ShowCheckpointResponse`
        """
        http_info = self._show_checkpoint_http_info(request)
        return self._call_api(**http_info)

    def show_checkpoint_invoker(self, request):
        http_info = self._show_checkpoint_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_checkpoint_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/checkpoints/{checkpoint_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCheckpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'checkpoint_id' in local_var_params:
            path_params['checkpoint_id'] = local_var_params['checkpoint_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_domain(self, request):
        """查询租户信息

        由控制台调用的内部接口，用于仅在查询共享备份时获取源project_id的域名信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomain
        :type request: :class:`huaweicloudsdkcbr.v1.ShowDomainRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.ShowDomainResponse`
        """
        http_info = self._show_domain_http_info(request)
        return self._call_api(**http_info)

    def show_domain_invoker(self, request):
        http_info = self._show_domain_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_domain_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/domain/{source_project_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'source_project_id' in local_var_params:
            path_params['source_project_id'] = local_var_params['source_project_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_member_detail(self, request):
        """获取备份成员详情

        获取备份成员的详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMemberDetail
        :type request: :class:`huaweicloudsdkcbr.v1.ShowMemberDetailRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.ShowMemberDetailResponse`
        """
        http_info = self._show_member_detail_http_info(request)
        return self._call_api(**http_info)

    def show_member_detail_invoker(self, request):
        http_info = self._show_member_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_member_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/backups/{backup_id}/members/{member_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMemberDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']
        if 'member_id' in local_var_params:
            path_params['member_id'] = local_var_params['member_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_members_detail(self, request):
        """获取备份成员列表

        获取备份共享成员的列表信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMembersDetail
        :type request: :class:`huaweicloudsdkcbr.v1.ShowMembersDetailRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.ShowMembersDetailResponse`
        """
        http_info = self._show_members_detail_http_info(request)
        return self._call_api(**http_info)

    def show_members_detail_invoker(self, request):
        http_info = self._show_members_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_members_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/backups/{backup_id}/members",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMembersDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']

        query_params = []
        if 'dest_project_id' in local_var_params:
            query_params.append(('dest_project_id', local_var_params['dest_project_id']))
        if 'image_id' in local_var_params:
            query_params.append(('image_id', local_var_params['image_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'vault_id' in local_var_params:
            query_params.append(('vault_id', local_var_params['vault_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_metadata(self, request):
        """查询备份元数据

        查询备份时资源的元数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMetadata
        :type request: :class:`huaweicloudsdkcbr.v1.ShowMetadataRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.ShowMetadataResponse`
        """
        http_info = self._show_metadata_http_info(request)
        return self._call_api(**http_info)

    def show_metadata_invoker(self, request):
        http_info = self._show_metadata_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_metadata_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/backups/{backup_id}/metadata",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMetadataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_migrate_status(self, request):
        """查询迁移

        查询迁移结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMigrateStatus
        :type request: :class:`huaweicloudsdkcbr.v1.ShowMigrateStatusRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.ShowMigrateStatusResponse`
        """
        http_info = self._show_migrate_status_http_info(request)
        return self._call_api(**http_info)

    def show_migrate_status_invoker(self, request):
        http_info = self._show_migrate_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_migrate_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/migrates",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMigrateStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'all_regions' in local_var_params:
            query_params.append(('all_regions', local_var_params['all_regions']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_op_log(self, request):
        """查询单个任务

        根据指定任务ID查询任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOpLog
        :type request: :class:`huaweicloudsdkcbr.v1.ShowOpLogRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.ShowOpLogResponse`
        """
        http_info = self._show_op_log_http_info(request)
        return self._call_api(**http_info)

    def show_op_log_invoker(self, request):
        http_info = self._show_op_log_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_op_log_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/operation-logs/{operation_log_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'operation_log_id' in local_var_params:
            path_params['operation_log_id'] = local_var_params['operation_log_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_policy(self, request):
        """查询单个策略

        查询单个策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPolicy
        :type request: :class:`huaweicloudsdkcbr.v1.ShowPolicyRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.ShowPolicyResponse`
        """
        http_info = self._show_policy_http_info(request)
        return self._call_api(**http_info)

    def show_policy_invoker(self, request):
        http_info = self._show_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_protectable(self, request):
        """查询指定可保护资源

        根据ID查询可保护性资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProtectable
        :type request: :class:`huaweicloudsdkcbr.v1.ShowProtectableRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.ShowProtectableResponse`
        """
        http_info = self._show_protectable_http_info(request)
        return self._call_api(**http_info)

    def show_protectable_invoker(self, request):
        http_info = self._show_protectable_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_protectable_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/protectables/{protectable_type}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProtectableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'protectable_type' in local_var_params:
            path_params['protectable_type'] = local_var_params['protectable_type']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_replication_capabilities(self, request):
        """查询复制能力

        查询本区域的复制能力
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowReplicationCapabilities
        :type request: :class:`huaweicloudsdkcbr.v1.ShowReplicationCapabilitiesRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.ShowReplicationCapabilitiesResponse`
        """
        http_info = self._show_replication_capabilities_http_info(request)
        return self._call_api(**http_info)

    def show_replication_capabilities_invoker(self, request):
        http_info = self._show_replication_capabilities_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_replication_capabilities_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/replication-capabilities",
            "request_type": request.__class__.__name__,
            "response_type": "ShowReplicationCapabilitiesResponse"
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

    def show_storage_usage(self, request):
        """查询容量统计

        查询容量统计
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowStorageUsage
        :type request: :class:`huaweicloudsdkcbr.v1.ShowStorageUsageRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.ShowStorageUsageResponse`
        """
        http_info = self._show_storage_usage_http_info(request)
        return self._call_api(**http_info)

    def show_storage_usage_invoker(self, request):
        http_info = self._show_storage_usage_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_storage_usage_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/storage_usage",
            "request_type": request.__class__.__name__,
            "response_type": "ShowStorageUsageResponse"
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
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_summary(self, request):
        """存储库容量总览

        查询项目下所有存储库的总容量和总使用量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSummary
        :type request: :class:`huaweicloudsdkcbr.v1.ShowSummaryRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.ShowSummaryResponse`
        """
        http_info = self._show_summary_http_info(request)
        return self._call_api(**http_info)

    def show_summary_invoker(self, request):
        http_info = self._show_summary_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_summary_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/vaults/summary",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSummaryResponse"
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

    def show_vault(self, request):
        """查询指定存储库

        根据ID查询指定存储库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVault
        :type request: :class:`huaweicloudsdkcbr.v1.ShowVaultRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.ShowVaultResponse`
        """
        http_info = self._show_vault_http_info(request)
        return self._call_api(**http_info)

    def show_vault_invoker(self, request):
        http_info = self._show_vault_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_vault_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/vaults/{vault_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVaultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vault_id' in local_var_params:
            path_params['vault_id'] = local_var_params['vault_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_vault_project_tag(self, request):
        """查询存储库项目标签

        查询租户在指定Region和实例类型的所有标签集合
        标签管理服务需要能够列出当前租户全部已使用的标签集合，为各服务Console打标签和过滤实例时提供标签联想功能
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVaultProjectTag
        :type request: :class:`huaweicloudsdkcbr.v1.ShowVaultProjectTagRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.ShowVaultProjectTagResponse`
        """
        http_info = self._show_vault_project_tag_http_info(request)
        return self._call_api(**http_info)

    def show_vault_project_tag_invoker(self, request):
        http_info = self._show_vault_project_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_vault_project_tag_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/vault/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVaultProjectTagResponse"
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

    def show_vault_resource_instances(self, request):
        """查询存储库资源实例

        使用标签过滤实例
        标签管理服务需要提供按标签过滤各服务实例并汇总显示在列表中，需要各服务提供查询能力
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVaultResourceInstances
        :type request: :class:`huaweicloudsdkcbr.v1.ShowVaultResourceInstancesRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.ShowVaultResourceInstancesResponse`
        """
        http_info = self._show_vault_resource_instances_http_info(request)
        return self._call_api(**http_info)

    def show_vault_resource_instances_invoker(self, request):
        http_info = self._show_vault_resource_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_vault_resource_instances_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/vault/resource_instances/action",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVaultResourceInstancesResponse"
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

    def show_vault_tag(self, request):
        """查询存储库资源标签

        查询指定实例的标签信息
        标签管理服务需要使用该接口查询指定实例的全部标签数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVaultTag
        :type request: :class:`huaweicloudsdkcbr.v1.ShowVaultTagRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.ShowVaultTagResponse`
        """
        http_info = self._show_vault_tag_http_info(request)
        return self._call_api(**http_info)

    def show_vault_tag_invoker(self, request):
        http_info = self._show_vault_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_vault_tag_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/vault/{vault_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVaultTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vault_id' in local_var_params:
            path_params['vault_id'] = local_var_params['vault_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def unregister_agent(self, request):
        """移除客户端

        移除客户端，移除客户端时将会删除该客户端所有备份，请谨慎操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UnregisterAgent
        :type request: :class:`huaweicloudsdkcbr.v1.UnregisterAgentRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.UnregisterAgentResponse`
        """
        http_info = self._unregister_agent_http_info(request)
        return self._call_api(**http_info)

    def unregister_agent_invoker(self, request):
        http_info = self._unregister_agent_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _unregister_agent_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/agents/{agent_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UnregisterAgentResponse"
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

    def update_agent(self, request):
        """修改客户端

        修改客户端状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAgent
        :type request: :class:`huaweicloudsdkcbr.v1.UpdateAgentRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.UpdateAgentResponse`
        """
        http_info = self._update_agent_http_info(request)
        return self._call_api(**http_info)

    def update_agent_invoker(self, request):
        http_info = self._update_agent_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_agent_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/agents/{agent_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAgentResponse"
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

    def update_backup(self, request):
        """更新备份

        根据备份id更改备份
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateBackup
        :type request: :class:`huaweicloudsdkcbr.v1.UpdateBackupRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.UpdateBackupResponse`
        """
        http_info = self._update_backup_http_info(request)
        return self._call_api(**http_info)

    def update_backup_invoker(self, request):
        http_info = self._update_backup_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_backup_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/backups/{backup_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateBackupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']

        query_params = []

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

    def update_member_status(self, request):
        """更新备份成员状态

        更新备份共享成员的状态，需要接收方执行此API。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateMemberStatus
        :type request: :class:`huaweicloudsdkcbr.v1.UpdateMemberStatusRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.UpdateMemberStatusResponse`
        """
        http_info = self._update_member_status_http_info(request)
        return self._call_api(**http_info)

    def update_member_status_invoker(self, request):
        http_info = self._update_member_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_member_status_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/backups/{backup_id}/members/{member_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMemberStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'member_id' in local_var_params:
            path_params['member_id'] = local_var_params['member_id']
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']

        query_params = []

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

    def update_order(self, request):
        """变更

        订单更新，支付cbc订单后，调用该接口更新包周期产品订单信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateOrder
        :type request: :class:`huaweicloudsdkcbr.v1.UpdateOrderRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.UpdateOrderResponse`
        """
        http_info = self._update_order_http_info(request)
        return self._call_api(**http_info)

    def update_order_invoker(self, request):
        http_info = self._update_order_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_order_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/orders/{order_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateOrderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'order_id' in local_var_params:
            path_params['order_id'] = local_var_params['order_id']

        query_params = []

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

    def update_policy(self, request):
        """修改策略

        修改策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePolicy
        :type request: :class:`huaweicloudsdkcbr.v1.UpdatePolicyRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.UpdatePolicyResponse`
        """
        http_info = self._update_policy_http_info(request)
        return self._call_api(**http_info)

    def update_policy_invoker(self, request):
        http_info = self._update_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []

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

    def update_vault(self, request):
        """修改存储库

        根据存储库ID修改存储库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateVault
        :type request: :class:`huaweicloudsdkcbr.v1.UpdateVaultRequest`
        :rtype: :class:`huaweicloudsdkcbr.v1.UpdateVaultResponse`
        """
        http_info = self._update_vault_http_info(request)
        return self._call_api(**http_info)

    def update_vault_invoker(self, request):
        http_info = self._update_vault_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_vault_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/vaults/{vault_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateVaultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vault_id' in local_var_params:
            path_params['vault_id'] = local_var_params['vault_id']

        query_params = []

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
