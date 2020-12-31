# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

import six

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class CbrAsyncClient(Client):
    """
    :param configuration: .Configuration object for this client
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def __init__(self):
        super(CbrAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcbr.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "CbrClient":
            raise TypeError("client type error, support client type is CbrClient")

        return ClientBuilder(clazz)

    def add_member_async(self, request):
        """添加备份成员

        添加备份可共享的成员，只有云服务器备份可以添加备份共享成员，且仅支持在同一区域的不同用户间共享。

        :param AddMemberRequest request
        :return: AddMemberResponse
        """
        return self.add_member_with_http_info(request)

    def add_member_with_http_info(self, request):
        """添加备份成员

        添加备份可共享的成员，只有云服务器备份可以添加备份共享成员，且仅支持在同一区域的不同用户间共享。

        :param AddMemberRequest request
        :return: AddMemberResponse
        """

        all_params = ['backup_id', 'add_member_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/backups/{backup_id}/members',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_vault_resource_async(self, request):
        """添加资源

        存储库添加资源

        :param AddVaultResourceRequest request
        :return: AddVaultResourceResponse
        """
        return self.add_vault_resource_with_http_info(request)

    def add_vault_resource_with_http_info(self, request):
        """添加资源

        存储库添加资源

        :param AddVaultResourceRequest request
        :return: AddVaultResourceResponse
        """

        all_params = ['vault_id', 'add_vault_resource_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'vault_id' in local_var_params:
            path_params['vault_id'] = local_var_params['vault_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/vaults/{vault_id}/addresources',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddVaultResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def associate_vault_policy_async(self, request):
        """设置存储库策略

        存储库设置策略

        :param AssociateVaultPolicyRequest request
        :return: AssociateVaultPolicyResponse
        """
        return self.associate_vault_policy_with_http_info(request)

    def associate_vault_policy_with_http_info(self, request):
        """设置存储库策略

        存储库设置策略

        :param AssociateVaultPolicyRequest request
        :return: AssociateVaultPolicyResponse
        """

        all_params = ['vault_id', 'associate_vault_policy_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'vault_id' in local_var_params:
            path_params['vault_id'] = local_var_params['vault_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/vaults/{vault_id}/associatepolicy',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AssociateVaultPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_create_and_delete_vault_tags_async(self, request):
        """批量添加删除存储库资源标签

        为指定实例批量添加或删除标签 标签管理服务需要使用该接口批量管理实例的标签。 一个资源上最多有10个标签。 此接口为幂等接口：     创建时如果请求体中存在重复key则报错。     创建时，不允许重复key，如果数据库存在就覆盖。     删除时，允许重复key。     删除时，如果删除的标签不存在，默认处理成功,删除时不对标签字符集范围做校验。key长度127个字符，value为255个字符。删除时tags结构体不能缺失，key不能为空，或者空字符串。

        :param BatchCreateAndDeleteVaultTagsRequest request
        :return: BatchCreateAndDeleteVaultTagsResponse
        """
        return self.batch_create_and_delete_vault_tags_with_http_info(request)

    def batch_create_and_delete_vault_tags_with_http_info(self, request):
        """批量添加删除存储库资源标签

        为指定实例批量添加或删除标签 标签管理服务需要使用该接口批量管理实例的标签。 一个资源上最多有10个标签。 此接口为幂等接口：     创建时如果请求体中存在重复key则报错。     创建时，不允许重复key，如果数据库存在就覆盖。     删除时，允许重复key。     删除时，如果删除的标签不存在，默认处理成功,删除时不对标签字符集范围做校验。key长度127个字符，value为255个字符。删除时tags结构体不能缺失，key不能为空，或者空字符串。

        :param BatchCreateAndDeleteVaultTagsRequest request
        :return: BatchCreateAndDeleteVaultTagsResponse
        """

        all_params = ['vault_id', 'batch_create_and_delete_vault_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'vault_id' in local_var_params:
            path_params['vault_id'] = local_var_params['vault_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/vault/{vault_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchCreateAndDeleteVaultTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def copy_backup_async(self, request):
        """复制备份

        跨区域复制备份。

        :param CopyBackupRequest request
        :return: CopyBackupResponse
        """
        return self.copy_backup_with_http_info(request)

    def copy_backup_with_http_info(self, request):
        """复制备份

        跨区域复制备份。

        :param CopyBackupRequest request
        :return: CopyBackupResponse
        """

        all_params = ['backup_id', 'copy_backup_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/backups/{backup_id}/replicate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CopyBackupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def copy_checkpoint_async(self, request):
        """复制备份还原点

        执行复制

        :param CopyCheckpointRequest request
        :return: CopyCheckpointResponse
        """
        return self.copy_checkpoint_with_http_info(request)

    def copy_checkpoint_with_http_info(self, request):
        """复制备份还原点

        执行复制

        :param CopyCheckpointRequest request
        :return: CopyCheckpointResponse
        """

        all_params = ['copy_checkpoint_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/checkpoints/replicate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CopyCheckpointResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_checkpoint_async(self, request):
        """创建备份还原点

        对存储库执行备份，生成备份还原点

        :param CreateCheckpointRequest request
        :return: CreateCheckpointResponse
        """
        return self.create_checkpoint_with_http_info(request)

    def create_checkpoint_with_http_info(self, request):
        """创建备份还原点

        对存储库执行备份，生成备份还原点

        :param CreateCheckpointRequest request
        :return: CreateCheckpointResponse
        """

        all_params = ['create_checkpoint_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/checkpoints',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateCheckpointResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_policy_async(self, request):
        """创建策略

        [创建策略，策略分为备份策略和复制策略。](tag:hws,hws_hk) [创建备份策略。](tag:dt,ocb,tlf,sbc,fcs_vm,ctc)

        :param CreatePolicyRequest request
        :return: CreatePolicyResponse
        """
        return self.create_policy_with_http_info(request)

    def create_policy_with_http_info(self, request):
        """创建策略

        [创建策略，策略分为备份策略和复制策略。](tag:hws,hws_hk) [创建备份策略。](tag:dt,ocb,tlf,sbc,fcs_vm,ctc)

        :param CreatePolicyRequest request
        :return: CreatePolicyResponse
        """

        all_params = ['create_policy_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/policies',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreatePolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_vault_async(self, request):
        """创建存储库

        创建存储库

        :param CreateVaultRequest request
        :return: CreateVaultResponse
        """
        return self.create_vault_with_http_info(request)

    def create_vault_with_http_info(self, request):
        """创建存储库

        创建存储库

        :param CreateVaultRequest request
        :return: CreateVaultResponse
        """

        all_params = ['create_vault_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/vaults',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateVaultResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_vault_tags_async(self, request):
        """添加存储库资源标签

        一个资源上最多有10个标签。 此接口为幂等接口：创建时，如果创建的标签已经存在（key相同），则覆盖。

        :param CreateVaultTagsRequest request
        :return: CreateVaultTagsResponse
        """
        return self.create_vault_tags_with_http_info(request)

    def create_vault_tags_with_http_info(self, request):
        """添加存储库资源标签

        一个资源上最多有10个标签。 此接口为幂等接口：创建时，如果创建的标签已经存在（key相同），则覆盖。

        :param CreateVaultTagsRequest request
        :return: CreateVaultTagsResponse
        """

        all_params = ['vault_id', 'create_vault_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'vault_id' in local_var_params:
            path_params['vault_id'] = local_var_params['vault_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/vault/{vault_id}/tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateVaultTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_backup_async(self, request):
        """删除备份

        删除单个备份。

        :param DeleteBackupRequest request
        :return: DeleteBackupResponse
        """
        return self.delete_backup_with_http_info(request)

    def delete_backup_with_http_info(self, request):
        """删除备份

        删除单个备份。

        :param DeleteBackupRequest request
        :return: DeleteBackupResponse
        """

        all_params = ['backup_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']

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
            resource_path='/v3/{project_id}/backups/{backup_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteBackupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_member_async(self, request):
        """删除指定备份成员

        删除指定的备份共享成员

        :param DeleteMemberRequest request
        :return: DeleteMemberResponse
        """
        return self.delete_member_with_http_info(request)

    def delete_member_with_http_info(self, request):
        """删除指定备份成员

        删除指定的备份共享成员

        :param DeleteMemberRequest request
        :return: DeleteMemberResponse
        """

        all_params = ['backup_id', 'member_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']
        if 'member_id' in local_var_params:
            path_params['member_id'] = local_var_params['member_id']

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
            resource_path='/v3/{project_id}/backups/{backup_id}/members/{member_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_policy_async(self, request):
        """删除策略

        删除策略

        :param DeletePolicyRequest request
        :return: DeletePolicyResponse
        """
        return self.delete_policy_with_http_info(request)

    def delete_policy_with_http_info(self, request):
        """删除策略

        删除策略

        :param DeletePolicyRequest request
        :return: DeletePolicyResponse
        """

        all_params = ['policy_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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
            resource_path='/v3/{project_id}/policies/{policy_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeletePolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_vault_async(self, request):
        """删除存储库

        删除存储库。若删除储存库，将一并删除存储库中的所有备份。

        :param DeleteVaultRequest request
        :return: DeleteVaultResponse
        """
        return self.delete_vault_with_http_info(request)

    def delete_vault_with_http_info(self, request):
        """删除存储库

        删除存储库。若删除储存库，将一并删除存储库中的所有备份。

        :param DeleteVaultRequest request
        :return: DeleteVaultResponse
        """

        all_params = ['vault_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'vault_id' in local_var_params:
            path_params['vault_id'] = local_var_params['vault_id']

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
            resource_path='/v3/{project_id}/vaults/{vault_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteVaultResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_vault_tag_async(self, request):
        """删除存储库资源标签

        幂等接口：删除时，如果删除的标签不存在，返回404。Key不能为空或者空字符串。

        :param DeleteVaultTagRequest request
        :return: DeleteVaultTagResponse
        """
        return self.delete_vault_tag_with_http_info(request)

    def delete_vault_tag_with_http_info(self, request):
        """删除存储库资源标签

        幂等接口：删除时，如果删除的标签不存在，返回404。Key不能为空或者空字符串。

        :param DeleteVaultTagRequest request
        :return: DeleteVaultTagResponse
        """

        all_params = ['key', 'vault_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']
        if 'vault_id' in local_var_params:
            path_params['vault_id'] = local_var_params['vault_id']

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
            resource_path='/v3/{project_id}/vault/{vault_id}/tags/{key}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteVaultTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def disassociate_vault_policy_async(self, request):
        """解除存储库策略

        存储库解除策略

        :param DisassociateVaultPolicyRequest request
        :return: DisassociateVaultPolicyResponse
        """
        return self.disassociate_vault_policy_with_http_info(request)

    def disassociate_vault_policy_with_http_info(self, request):
        """解除存储库策略

        存储库解除策略

        :param DisassociateVaultPolicyRequest request
        :return: DisassociateVaultPolicyResponse
        """

        all_params = ['vault_id', 'disassociate_vault_policy_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'vault_id' in local_var_params:
            path_params['vault_id'] = local_var_params['vault_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/vaults/{vault_id}/dissociatepolicy',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DisassociateVaultPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def import_backup_async(self, request):
        """同步备份

        同步备份副本

        :param ImportBackupRequest request
        :return: ImportBackupResponse
        """
        return self.import_backup_with_http_info(request)

    def import_backup_with_http_info(self, request):
        """同步备份

        同步备份副本

        :param ImportBackupRequest request
        :return: ImportBackupResponse
        """

        all_params = ['import_backup_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/backups/sync',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ImportBackupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_backups_async(self, request):
        """查询所有备份

        查询所有副本

        :param ListBackupsRequest request
        :return: ListBackupsResponse
        """
        return self.list_backups_with_http_info(request)

    def list_backups_with_http_info(self, request):
        """查询所有备份

        查询所有副本

        :param ListBackupsRequest request
        :return: ListBackupsResponse
        """

        all_params = ['checkpoint_id', 'dec', 'end_time', 'image_type', 'limit', 'marker', 'name', 'offset', 'resource_az', 'resource_id', 'resource_name', 'resource_type', 'sort', 'start_time', 'status', 'vault_id', 'enterprise_project_id', 'own_type', 'member_status', 'parent_id', 'used_percent']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/backups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListBackupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_op_logs_async(self, request):
        """查询任务列表

        查询任务列表

        :param ListOpLogsRequest request
        :return: ListOpLogsResponse
        """
        return self.list_op_logs_with_http_info(request)

    def list_op_logs_with_http_info(self, request):
        """查询任务列表

        查询任务列表

        :param ListOpLogsRequest request
        :return: ListOpLogsResponse
        """

        all_params = ['end_time', 'limit', 'offset', 'operation_type', 'provider_id', 'resource_id', 'resource_name', 'start_time', 'status', 'vault_id', 'vault_name', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/operation-logs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListOpLogsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_policies_async(self, request):
        """查询策略列表

        查询策略列表

        :param ListPoliciesRequest request
        :return: ListPoliciesResponse
        """
        return self.list_policies_with_http_info(request)

    def list_policies_with_http_info(self, request):
        """查询策略列表

        查询策略列表

        :param ListPoliciesRequest request
        :return: ListPoliciesResponse
        """

        all_params = ['operation_type', 'vault_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'operation_type' in local_var_params:
            query_params.append(('operation_type', local_var_params['operation_type']))
        if 'vault_id' in local_var_params:
            query_params.append(('vault_id', local_var_params['vault_id']))

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
            resource_path='/v3/{project_id}/policies',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPoliciesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_protectable_async(self, request):
        """查询可保护资源

        查询可保护性资源列表

        :param ListProtectableRequest request
        :return: ListProtectableResponse
        """
        return self.list_protectable_with_http_info(request)

    def list_protectable_with_http_info(self, request):
        """查询可保护资源

        查询可保护性资源列表

        :param ListProtectableRequest request
        :return: ListProtectableResponse
        """

        all_params = ['protectable_type', 'limit', 'marker', 'name', 'offset', 'status', 'id', 'server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/protectables/{protectable_type}/instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListProtectableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_vault_async(self, request):
        """查询存储库列表

        查询存储库列表

        :param ListVaultRequest request
        :return: ListVaultResponse
        """
        return self.list_vault_with_http_info(request)

    def list_vault_with_http_info(self, request):
        """查询存储库列表

        查询存储库列表

        :param ListVaultRequest request
        :return: ListVaultResponse
        """

        all_params = ['limit', 'name', 'offset', 'cloud_type', 'protect_type', 'object_type', 'enterprise_project_id', 'id', 'policy_id', 'status', 'resource_ids']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
        if 'policy_id' in local_var_params:
            query_params.append(('policy_id', local_var_params['policy_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'resource_ids' in local_var_params:
            query_params.append(('resource_ids', local_var_params['resource_ids']))

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
            resource_path='/v3/{project_id}/vaults',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListVaultResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def migrate_vault_resource_async(self, request):
        """迁移资源

        支持资源迁移到另一个存储库，不删除备份。

        :param MigrateVaultResourceRequest request
        :return: MigrateVaultResourceResponse
        """
        return self.migrate_vault_resource_with_http_info(request)

    def migrate_vault_resource_with_http_info(self, request):
        """迁移资源

        支持资源迁移到另一个存储库，不删除备份。

        :param MigrateVaultResourceRequest request
        :return: MigrateVaultResourceResponse
        """

        all_params = ['vault_id', 'migrate_vault_resource_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'vault_id' in local_var_params:
            path_params['vault_id'] = local_var_params['vault_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/vaults/{vault_id}/migrateresources',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='MigrateVaultResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def remove_vault_resource_async(self, request):
        """移除资源

        移除存储库中的资源，若移除资源，将一并删除该资源在保管库中的备份

        :param RemoveVaultResourceRequest request
        :return: RemoveVaultResourceResponse
        """
        return self.remove_vault_resource_with_http_info(request)

    def remove_vault_resource_with_http_info(self, request):
        """移除资源

        移除存储库中的资源，若移除资源，将一并删除该资源在保管库中的备份

        :param RemoveVaultResourceRequest request
        :return: RemoveVaultResourceResponse
        """

        all_params = ['vault_id', 'remove_vault_resource_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'vault_id' in local_var_params:
            path_params['vault_id'] = local_var_params['vault_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/vaults/{vault_id}/removeresources',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RemoveVaultResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def restore_backup_async(self, request):
        """备份恢复

        恢复备份数据

        :param RestoreBackupRequest request
        :return: RestoreBackupResponse
        """
        return self.restore_backup_with_http_info(request)

    def restore_backup_with_http_info(self, request):
        """备份恢复

        恢复备份数据

        :param RestoreBackupRequest request
        :return: RestoreBackupResponse
        """

        all_params = ['backup_id', 'restore_backup_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/backups/{backup_id}/restore',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RestoreBackupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_backup_async(self, request):
        """查询指定备份

        根据指定id查询单个副本。

        :param ShowBackupRequest request
        :return: ShowBackupResponse
        """
        return self.show_backup_with_http_info(request)

    def show_backup_with_http_info(self, request):
        """查询指定备份

        根据指定id查询单个副本。

        :param ShowBackupRequest request
        :return: ShowBackupResponse
        """

        all_params = ['backup_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']

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
            resource_path='/v3/{project_id}/backups/{backup_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowBackupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_checkpoint_async(self, request):
        """查询备份还原点

        根据还原点ID查询指定还原点

        :param ShowCheckpointRequest request
        :return: ShowCheckpointResponse
        """
        return self.show_checkpoint_with_http_info(request)

    def show_checkpoint_with_http_info(self, request):
        """查询备份还原点

        根据还原点ID查询指定还原点

        :param ShowCheckpointRequest request
        :return: ShowCheckpointResponse
        """

        all_params = ['checkpoint_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'checkpoint_id' in local_var_params:
            path_params['checkpoint_id'] = local_var_params['checkpoint_id']

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
            resource_path='/v3/{project_id}/checkpoints/{checkpoint_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCheckpointResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_member_detail_async(self, request):
        """获取备份成员详情

        获取备份成员的详情

        :param ShowMemberDetailRequest request
        :return: ShowMemberDetailResponse
        """
        return self.show_member_detail_with_http_info(request)

    def show_member_detail_with_http_info(self, request):
        """获取备份成员详情

        获取备份成员的详情

        :param ShowMemberDetailRequest request
        :return: ShowMemberDetailResponse
        """

        all_params = ['backup_id', 'member_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']
        if 'member_id' in local_var_params:
            path_params['member_id'] = local_var_params['member_id']

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
            resource_path='/v3/{project_id}/backups/{backup_id}/members/{member_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMemberDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_members_detail_async(self, request):
        """获取备份成员列表

        获取备份共享成员的列表信息

        :param ShowMembersDetailRequest request
        :return: ShowMembersDetailResponse
        """
        return self.show_members_detail_with_http_info(request)

    def show_members_detail_with_http_info(self, request):
        """获取备份成员列表

        获取备份共享成员的列表信息

        :param ShowMembersDetailRequest request
        :return: ShowMembersDetailResponse
        """

        all_params = ['backup_id', 'dest_project_id', 'image_id', 'status', 'vault_id', 'limit', 'marker', 'offset', 'sort']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/backups/{backup_id}/members',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMembersDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_op_log_async(self, request):
        """查询单个任务

        根据指定任务ID查询任务

        :param ShowOpLogRequest request
        :return: ShowOpLogResponse
        """
        return self.show_op_log_with_http_info(request)

    def show_op_log_with_http_info(self, request):
        """查询单个任务

        根据指定任务ID查询任务

        :param ShowOpLogRequest request
        :return: ShowOpLogResponse
        """

        all_params = ['operation_log_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'operation_log_id' in local_var_params:
            path_params['operation_log_id'] = local_var_params['operation_log_id']

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
            resource_path='/v3/{project_id}/operation-logs/{operation_log_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowOpLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_policy_async(self, request):
        """查询单个策略

        查询单个策略

        :param ShowPolicyRequest request
        :return: ShowPolicyResponse
        """
        return self.show_policy_with_http_info(request)

    def show_policy_with_http_info(self, request):
        """查询单个策略

        查询单个策略

        :param ShowPolicyRequest request
        :return: ShowPolicyResponse
        """

        all_params = ['policy_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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
            resource_path='/v3/{project_id}/policies/{policy_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_protectable_async(self, request):
        """查询指定可保护资源

        根据ID查询可保护性资源

        :param ShowProtectableRequest request
        :return: ShowProtectableResponse
        """
        return self.show_protectable_with_http_info(request)

    def show_protectable_with_http_info(self, request):
        """查询指定可保护资源

        根据ID查询可保护性资源

        :param ShowProtectableRequest request
        :return: ShowProtectableResponse
        """

        all_params = ['instance_id', 'protectable_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'protectable_type' in local_var_params:
            path_params['protectable_type'] = local_var_params['protectable_type']

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
            resource_path='/v3/{project_id}/protectables/{protectable_type}/instances/{instance_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowProtectableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_replication_capabilities_async(self, request):
        """查询复制能力

        查询本区域的复制能力

        :param ShowReplicationCapabilitiesRequest request
        :return: ShowReplicationCapabilitiesResponse
        """
        return self.show_replication_capabilities_with_http_info(request)

    def show_replication_capabilities_with_http_info(self, request):
        """查询复制能力

        查询本区域的复制能力

        :param ShowReplicationCapabilitiesRequest request
        :return: ShowReplicationCapabilitiesResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/replication-capabilities',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowReplicationCapabilitiesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_vault_async(self, request):
        """查询指定存储库

        根据ID查询指定存储库

        :param ShowVaultRequest request
        :return: ShowVaultResponse
        """
        return self.show_vault_with_http_info(request)

    def show_vault_with_http_info(self, request):
        """查询指定存储库

        根据ID查询指定存储库

        :param ShowVaultRequest request
        :return: ShowVaultResponse
        """

        all_params = ['vault_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'vault_id' in local_var_params:
            path_params['vault_id'] = local_var_params['vault_id']

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
            resource_path='/v3/{project_id}/vaults/{vault_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowVaultResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_vault_project_tag_async(self, request):
        """查询存储库项目标签

        查询租户在指定Region和实例类型的所有标签集合 标签管理服务需要能够列出当前租户全部已使用的标签集合，为各服务Console打标签和过滤实例时提供标签联想功能

        :param ShowVaultProjectTagRequest request
        :return: ShowVaultProjectTagResponse
        """
        return self.show_vault_project_tag_with_http_info(request)

    def show_vault_project_tag_with_http_info(self, request):
        """查询存储库项目标签

        查询租户在指定Region和实例类型的所有标签集合 标签管理服务需要能够列出当前租户全部已使用的标签集合，为各服务Console打标签和过滤实例时提供标签联想功能

        :param ShowVaultProjectTagRequest request
        :return: ShowVaultProjectTagResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/vault/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowVaultProjectTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_vault_resource_instances_async(self, request):
        """查询存储库资源实例

        使用标签过滤实例 标签管理服务需要提供按标签过滤各服务实例并汇总显示在列表中，需要各服务提供查询能力

        :param ShowVaultResourceInstancesRequest request
        :return: ShowVaultResourceInstancesResponse
        """
        return self.show_vault_resource_instances_with_http_info(request)

    def show_vault_resource_instances_with_http_info(self, request):
        """查询存储库资源实例

        使用标签过滤实例 标签管理服务需要提供按标签过滤各服务实例并汇总显示在列表中，需要各服务提供查询能力

        :param ShowVaultResourceInstancesRequest request
        :return: ShowVaultResourceInstancesResponse
        """

        all_params = ['show_vault_resource_instances_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/vault/resource_instances/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowVaultResourceInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_vault_tag_async(self, request):
        """查询存储库资源标签

        查询指定实例的标签信息 标签管理服务需要使用该接口查询指定实例的全部标签数据

        :param ShowVaultTagRequest request
        :return: ShowVaultTagResponse
        """
        return self.show_vault_tag_with_http_info(request)

    def show_vault_tag_with_http_info(self, request):
        """查询存储库资源标签

        查询指定实例的标签信息 标签管理服务需要使用该接口查询指定实例的全部标签数据

        :param ShowVaultTagRequest request
        :return: ShowVaultTagResponse
        """

        all_params = ['vault_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'vault_id' in local_var_params:
            path_params['vault_id'] = local_var_params['vault_id']

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
            resource_path='/v3/{project_id}/vault/{vault_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowVaultTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_member_status_async(self, request):
        """更新备份成员状态

        更新备份共享成员的状态，需要接收方执行此API。

        :param UpdateMemberStatusRequest request
        :return: UpdateMemberStatusResponse
        """
        return self.update_member_status_with_http_info(request)

    def update_member_status_with_http_info(self, request):
        """更新备份成员状态

        更新备份共享成员的状态，需要接收方执行此API。

        :param UpdateMemberStatusRequest request
        :return: UpdateMemberStatusResponse
        """

        all_params = ['member_id', 'backup_id', 'update_member_status_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'member_id' in local_var_params:
            path_params['member_id'] = local_var_params['member_id']
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/backups/{backup_id}/members/{member_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateMemberStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_policy_async(self, request):
        """修改策略

        修改策略

        :param UpdatePolicyRequest request
        :return: UpdatePolicyResponse
        """
        return self.update_policy_with_http_info(request)

    def update_policy_with_http_info(self, request):
        """修改策略

        修改策略

        :param UpdatePolicyRequest request
        :return: UpdatePolicyResponse
        """

        all_params = ['policy_id', 'update_policy_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/policies/{policy_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_vault_async(self, request):
        """修改存储库

        根据存储库ID修改存储库

        :param UpdateVaultRequest request
        :return: UpdateVaultResponse
        """
        return self.update_vault_with_http_info(request)

    def update_vault_with_http_info(self, request):
        """修改存储库

        根据存储库ID修改存储库

        :param UpdateVaultRequest request
        :return: UpdateVaultResponse
        """

        all_params = ['vault_id', 'update_vault_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'vault_id' in local_var_params:
            path_params['vault_id'] = local_var_params['vault_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/vaults/{vault_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateVaultResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
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
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type,
	    async_request=True)
