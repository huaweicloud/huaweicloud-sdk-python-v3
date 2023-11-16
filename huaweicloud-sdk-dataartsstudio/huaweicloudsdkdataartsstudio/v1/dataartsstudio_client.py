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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkdataartsstudio'")


class DataArtsStudioClient(Client):
    def __init__(self):
        super(DataArtsStudioClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdataartsstudio.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "DataArtsStudioClient":
                raise TypeError("client type error, support client type is DataArtsStudioClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_tag_to_asset(self, request):
        """标签关联到资产

        标签关联到资产
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddTagToAsset
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.AddTagToAssetRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.AddTagToAssetResponse`
        """
        http_info = self._add_tag_to_asset_http_info(request)
        return self._call_api(**http_info)

    def add_tag_to_asset_invoker(self, request):
        http_info = self._add_tag_to_asset_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_tag_to_asset_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/tags/{term_guid}/assignedentities",
            "request_type": request.__class__.__name__,
            "response_type": "AddTagToAssetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'term_guid' in local_var_params:
            path_params['term_guid'] = local_var_params['term_guid']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def add_work_space_users(self, request):
        """添加工作空间用户

        添加工作空间用户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddWorkSpaceUsers
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.AddWorkSpaceUsersRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.AddWorkSpaceUsersResponse`
        """
        http_info = self._add_work_space_users_http_info(request)
        return self._call_api(**http_info)

    def add_work_space_users_invoker(self, request):
        http_info = self._add_work_space_users_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_work_space_users_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{workspace_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "AddWorkSpaceUsersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

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

    def associate_classification_to_entity(self, request):
        """资产关联分类

        将一个分类关联到一个或多个指定guid的资产上
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateClassificationToEntity
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.AssociateClassificationToEntityRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.AssociateClassificationToEntityResponse`
        """
        http_info = self._associate_classification_to_entity_http_info(request)
        return self._call_api(**http_info)

    def associate_classification_to_entity_invoker(self, request):
        http_info = self._associate_classification_to_entity_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _associate_classification_to_entity_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/asset/entities/guid/{guid}/classification",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateClassificationToEntityResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'guid' in local_var_params:
            path_params['guid'] = local_var_params['guid']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def associate_security_level_to_entitie(self, request):
        """资产关联密级

        关联资产到密级，资产关联指定密级
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateSecurityLevelToEntitie
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.AssociateSecurityLevelToEntitieRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.AssociateSecurityLevelToEntitieResponse`
        """
        http_info = self._associate_security_level_to_entitie_http_info(request)
        return self._call_api(**http_info)

    def associate_security_level_to_entitie_invoker(self, request):
        http_info = self._associate_security_level_to_entitie_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _associate_security_level_to_entitie_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/asset/entities/guid/{guid}/security-level",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateSecurityLevelToEntitieResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'guid' in local_var_params:
            path_params['guid'] = local_var_params['guid']

        query_params = []
        if 'security_level' in local_var_params:
            query_params.append(('security-level', local_var_params['security_level']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_approve_apply(self, request):
        """审核申请

        审核申请
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchApproveApply
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.BatchApproveApplyRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BatchApproveApplyResponse`
        """
        http_info = self._batch_approve_apply_http_info(request)
        return self._call_api(**http_info)

    def batch_approve_apply_invoker(self, request):
        http_info = self._batch_approve_apply_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_approve_apply_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/service/applys",
            "request_type": request.__class__.__name__,
            "response_type": "BatchApproveApplyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_associate_classification_to_entities(self, request):
        """批量资产关联分类

        批量资产关联分类：只支持对数据表的列和OBS对象添加分类
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchAssociateClassificationToEntities
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.BatchAssociateClassificationToEntitiesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BatchAssociateClassificationToEntitiesResponse`
        """
        http_info = self._batch_associate_classification_to_entities_http_info(request)
        return self._call_api(**http_info)

    def batch_associate_classification_to_entities_invoker(self, request):
        http_info = self._batch_associate_classification_to_entities_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_associate_classification_to_entities_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/asset/entities/classification",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAssociateClassificationToEntitiesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def batch_associate_security_level_to_entities(self, request):
        """批量资产关联密级

        批量资产关联密级：单个密级关联到多个资产上
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchAssociateSecurityLevelToEntities
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.BatchAssociateSecurityLevelToEntitiesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BatchAssociateSecurityLevelToEntitiesResponse`
        """
        http_info = self._batch_associate_security_level_to_entities_http_info(request)
        return self._call_api(**http_info)

    def batch_associate_security_level_to_entities_invoker(self, request):
        http_info = self._batch_associate_security_level_to_entities_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_associate_security_level_to_entities_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/asset/entities/security-level",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAssociateSecurityLevelToEntitiesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def batch_delete_templates(self, request):
        """批量删除规则模板

        批量删除规则模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteTemplates
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.BatchDeleteTemplatesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BatchDeleteTemplatesResponse`
        """
        http_info = self._batch_delete_templates_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_templates_invoker(self, request):
        http_info = self._batch_delete_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_templates_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/quality/rule-templates/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def batch_offline(self, request):
        """批量下线

        批量下线
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchOffline
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.BatchOfflineRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BatchOfflineResponse`
        """
        http_info = self._batch_offline_http_info(request)
        return self._call_api(**http_info)

    def batch_offline_invoker(self, request):
        http_info = self._batch_offline_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_offline_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/design/approvals/batch-offline",
            "request_type": request.__class__.__name__,
            "response_type": "BatchOfflineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def batch_publish(self, request):
        """批量发布

        批量发布
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchPublish
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.BatchPublishRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BatchPublishResponse`
        """
        http_info = self._batch_publish_http_info(request)
        return self._call_api(**http_info)

    def batch_publish_invoker(self, request):
        http_info = self._batch_publish_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_publish_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/design/approvals/batch-publish",
            "request_type": request.__class__.__name__,
            "response_type": "BatchPublishResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def batch_sync_metadata(self, request):
        """元数据实时同步接口(邀测)

        元数据实时同步接口，支持批量。该接口功能处于邀测阶段，后续将随功能公测将逐步开放。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchSyncMetadata
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.BatchSyncMetadataRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BatchSyncMetadataResponse`
        """
        http_info = self._batch_sync_metadata_http_info(request)
        return self._call_api(**http_info)

    def batch_sync_metadata_invoker(self, request):
        http_info = self._batch_sync_metadata_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_sync_metadata_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/metadata/async-bulk",
            "request_type": request.__class__.__name__,
            "response_type": "BatchSyncMetadataResponse"
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

    def change_catalog(self, request):
        """修改流程架构

        修改流程架构
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeCatalog
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ChangeCatalogRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ChangeCatalogResponse`
        """
        http_info = self._change_catalog_http_info(request)
        return self._call_api(**http_info)

    def change_catalog_invoker(self, request):
        http_info = self._change_catalog_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_catalog_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/design/biz/catalogs",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeCatalogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def change_resource(self, request):
        """规格变更接口

        规格变更接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeResource
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ChangeResourceRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ChangeResourceResponse`
        """
        http_info = self._change_resource_http_info(request)
        return self._call_api(**http_info)

    def change_resource_invoker(self, request):
        http_info = self._change_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_resource_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/change-resource",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeResourceResponse"
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

    def change_subjects(self, request):
        """修改或删除主题层级

        修改或删除主题层级
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeSubjects
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ChangeSubjectsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ChangeSubjectsResponse`
        """
        http_info = self._change_subjects_http_info(request)
        return self._call_api(**http_info)

    def change_subjects_invoker(self, request):
        http_info = self._change_subjects_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_subjects_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/design/subject-levels",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeSubjectsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def check_dimension_status(self, request):
        """查看逆向维度表任务

        查看逆向维度表任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckDimensionStatus
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CheckDimensionStatusRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CheckDimensionStatusResponse`
        """
        http_info = self._check_dimension_status_http_info(request)
        return self._call_api(**http_info)

    def check_dimension_status_invoker(self, request):
        http_info = self._check_dimension_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_dimension_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/dimension/database",
            "request_type": request.__class__.__name__,
            "response_type": "CheckDimensionStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def check_fact_logic_table_status(self, request):
        """查看逆向事实表任务

        查看逆向事实表任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckFactLogicTableStatus
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CheckFactLogicTableStatusRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CheckFactLogicTableStatusResponse`
        """
        http_info = self._check_fact_logic_table_status_http_info(request)
        return self._call_api(**http_info)

    def check_fact_logic_table_status_invoker(self, request):
        http_info = self._check_fact_logic_table_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_fact_logic_table_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/fact-logic-tables/database",
            "request_type": request.__class__.__name__,
            "response_type": "CheckFactLogicTableStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def confirm_approvals(self, request):
        """审批单处理

        审批驳回/通过，单个或多个 action-id&#x3D;reject/resolve
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ConfirmApprovals
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ConfirmApprovalsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ConfirmApprovalsResponse`
        """
        http_info = self._confirm_approvals_http_info(request)
        return self._call_api(**http_info)

    def confirm_approvals_invoker(self, request):
        http_info = self._confirm_approvals_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _confirm_approvals_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/design/approvals/action",
            "request_type": request.__class__.__name__,
            "response_type": "ConfirmApprovalsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action-id', local_var_params['action_id']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def confirm_message(self, request):
        """处理消息

        处理消息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ConfirmMessage
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ConfirmMessageRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ConfirmMessageResponse`
        """
        http_info = self._confirm_message_http_info(request)
        return self._call_api(**http_info)

    def confirm_message_invoker(self, request):
        http_info = self._confirm_message_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _confirm_message_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/service/messages",
            "request_type": request.__class__.__name__,
            "response_type": "ConfirmMessageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def count_all_models(self, request):
        """关系建模统计信息

        关系建模统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountAllModels
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CountAllModelsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CountAllModelsResponse`
        """
        http_info = self._count_all_models_http_info(request)
        return self._call_api(**http_info)

    def count_all_models_invoker(self, request):
        http_info = self._count_all_models_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _count_all_models_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/models/statistic",
            "request_type": request.__class__.__name__,
            "response_type": "CountAllModelsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def count_overviews(self, request):
        """总览统计信息

        总览统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountOverviews
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CountOverviewsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CountOverviewsResponse`
        """
        http_info = self._count_overviews_http_info(request)
        return self._call_api(**http_info)

    def count_overviews_invoker(self, request):
        http_info = self._count_overviews_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _count_overviews_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/definitions/statistic",
            "request_type": request.__class__.__name__,
            "response_type": "CountOverviewsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def count_standards(self, request):
        """标准覆盖率统计信息

        标准覆盖率统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountStandards
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CountStandardsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CountStandardsResponse`
        """
        http_info = self._count_standards_http_info(request)
        return self._call_api(**http_info)

    def count_standards_invoker(self, request):
        http_info = self._count_standards_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _count_standards_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/definitions/statistic/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "CountStandardsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'biz_type' in local_var_params:
            query_params.append(('biz_type', local_var_params['biz_type']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def count_table_models(self, request):
        """模型统计信息

        模型统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountTableModels
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CountTableModelsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CountTableModelsResponse`
        """
        http_info = self._count_table_models_http_info(request)
        return self._call_api(**http_info)

    def count_table_models_invoker(self, request):
        http_info = self._count_table_models_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _count_table_models_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/table-models/statistic",
            "request_type": request.__class__.__name__,
            "response_type": "CountTableModelsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'model_id' in local_var_params:
            query_params.append(('model_id', local_var_params['model_id']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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
        """创建应用

        创建应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateApp
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateAppRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateAppResponse`
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
            "resource_path": "/v1/{project_id}/service/apps",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

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

    def create_approver(self, request):
        """创建审批人

        创建审批人
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateApprover
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateApproverRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateApproverResponse`
        """
        http_info = self._create_approver_http_info(request)
        return self._call_api(**http_info)

    def create_approver_invoker(self, request):
        http_info = self._create_approver_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_approver_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/design/approvals/users",
            "request_type": request.__class__.__name__,
            "response_type": "CreateApproverResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_biz_metric(self, request):
        """创建业务指标

        创建业务指标
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateBizMetric
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateBizMetricRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateBizMetricResponse`
        """
        http_info = self._create_biz_metric_http_info(request)
        return self._call_api(**http_info)

    def create_biz_metric_invoker(self, request):
        http_info = self._create_biz_metric_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_biz_metric_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/design/biz-metrics",
            "request_type": request.__class__.__name__,
            "response_type": "CreateBizMetricResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def create_catalog(self, request):
        """创建流程架构

        创建流程架构
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCatalog
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateCatalogRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateCatalogResponse`
        """
        http_info = self._create_catalog_http_info(request)
        return self._call_api(**http_info)

    def create_catalog_invoker(self, request):
        http_info = self._create_catalog_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_catalog_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/design/biz/catalogs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCatalogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def create_code_table(self, request):
        """创建码表

        创建码表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCodeTable
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateCodeTableRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateCodeTableResponse`
        """
        http_info = self._create_code_table_http_info(request)
        return self._call_api(**http_info)

    def create_code_table_invoker(self, request):
        http_info = self._create_code_table_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_code_table_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/design/code-tables",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCodeTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def create_connections(self, request):
        """创建数据连接

        创建数据连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateConnections
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateConnectionsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateConnectionsResponse`
        """
        http_info = self._create_connections_http_info(request)
        return self._call_api(**http_info)

    def create_connections_invoker(self, request):
        http_info = self._create_connections_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_connections_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/data-connections",
            "request_type": request.__class__.__name__,
            "response_type": "CreateConnectionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_directory(self, request):
        """创建目录

        创建目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDirectory
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateDirectoryRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateDirectoryResponse`
        """
        http_info = self._create_directory_http_info(request)
        return self._call_api(**http_info)

    def create_directory_invoker(self, request):
        http_info = self._create_directory_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_directory_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/design/directorys",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDirectoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def create_factory_env(self, request):
        """创建环境变量

        创建环境变量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFactoryEnv
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateFactoryEnvRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateFactoryEnvResponse`
        """
        http_info = self._create_factory_env_http_info(request)
        return self._call_api(**http_info)

    def create_factory_env_invoker(self, request):
        http_info = self._create_factory_env_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_factory_env_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/factory/env",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFactoryEnvResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["status_code", "is_success", ]

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

    def create_factory_supplement_data_instance(self, request):
        """创建补数据实例的接口

        创建一个补数据实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFactorySupplementDataInstance
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateFactorySupplementDataInstanceRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateFactorySupplementDataInstanceResponse`
        """
        http_info = self._create_factory_supplement_data_instance_http_info(request)
        return self._call_api(**http_info)

    def create_factory_supplement_data_instance_invoker(self, request):
        http_info = self._create_factory_supplement_data_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_factory_supplement_data_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/factory/supplement-data",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFactorySupplementDataInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def create_manager_work_space(self, request):
        """创建工作空间

        创建工作空间
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateManagerWorkSpace
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateManagerWorkSpaceRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateManagerWorkSpaceResponse`
        """
        http_info = self._create_manager_work_space_http_info(request)
        return self._call_api(**http_info)

    def create_manager_work_space_invoker(self, request):
        http_info = self._create_manager_work_space_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_manager_work_space_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CreateManagerWorkSpaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

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

    def create_or_update_asset(self, request):
        """添加或修改资产

        添加或修改资产
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateOrUpdateAsset
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateOrUpdateAssetRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateOrUpdateAssetResponse`
        """
        http_info = self._create_or_update_asset_http_info(request)
        return self._call_api(**http_info)

    def create_or_update_asset_invoker(self, request):
        http_info = self._create_or_update_asset_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_or_update_asset_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/asset",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOrUpdateAssetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_service_catalog(self, request):
        """创建服务目录

        创建服务目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateServiceCatalog
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateServiceCatalogRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateServiceCatalogResponse`
        """
        http_info = self._create_service_catalog_http_info(request)
        return self._call_api(**http_info)

    def create_service_catalog_invoker(self, request):
        http_info = self._create_service_catalog_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_service_catalog_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/service/servicecatalogs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateServiceCatalogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

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

    def create_standard(self, request):
        """创建数据标准

        创建数据标准
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateStandard
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateStandardRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateStandardResponse`
        """
        http_info = self._create_standard_http_info(request)
        return self._call_api(**http_info)

    def create_standard_invoker(self, request):
        http_info = self._create_standard_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_standard_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/design/standards",
            "request_type": request.__class__.__name__,
            "response_type": "CreateStandardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def create_standard_template(self, request):
        """创建数据标准模板

        创建数据标准模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateStandardTemplate
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateStandardTemplateRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateStandardTemplateResponse`
        """
        http_info = self._create_standard_template_http_info(request)
        return self._call_api(**http_info)

    def create_standard_template_invoker(self, request):
        http_info = self._create_standard_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_standard_template_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/design/standards/templates",
            "request_type": request.__class__.__name__,
            "response_type": "CreateStandardTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def create_subject(self, request):
        """创建主题

        创建主题
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSubject
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateSubjectRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateSubjectResponse`
        """
        http_info = self._create_subject_http_info(request)
        return self._call_api(**http_info)

    def create_subject_invoker(self, request):
        http_info = self._create_subject_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_subject_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/design/subjects",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSubjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def create_subject_new(self, request):
        """创建主题(新)

        创建主题(新)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSubjectNew
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateSubjectNewRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateSubjectNewResponse`
        """
        http_info = self._create_subject_new_http_info(request)
        return self._call_api(**http_info)

    def create_subject_new_invoker(self, request):
        http_info = self._create_subject_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_subject_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/design/subjects",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSubjectNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def create_table_model(self, request):
        """创建模型实体

        创建一个模型实体，包括逻辑实体或物理数据表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTableModel
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateTableModelRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateTableModelResponse`
        """
        http_info = self._create_table_model_http_info(request)
        return self._call_api(**http_info)

    def create_table_model_invoker(self, request):
        http_info = self._create_table_model_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_table_model_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/design/table-model",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTableModelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def create_task(self, request):
        """创建采集任务

        创建采集任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTask
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateTaskRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateTaskResponse`
        """
        http_info = self._create_task_http_info(request)
        return self._call_api(**http_info)

    def create_task_invoker(self, request):
        http_info = self._create_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/metadata/tasks/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def create_template(self, request):
        """创建规则模板

        创建规则模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTemplate
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateTemplateRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateTemplateResponse`
        """
        http_info = self._create_template_http_info(request)
        return self._call_api(**http_info)

    def create_template_invoker(self, request):
        http_info = self._create_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_template_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/quality/rule-templates",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def create_workspace(self, request):
        """新建模型工作区

        新建模型工作区
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateWorkspace
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateWorkspaceRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateWorkspaceResponse`
        """
        http_info = self._create_workspace_http_info(request)
        return self._call_api(**http_info)

    def create_workspace_invoker(self, request):
        http_info = self._create_workspace_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_workspace_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/design/workspaces",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWorkspaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def debug_dataconnection(self, request):
        """测试创建数据连接

        测试创建数据连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DebugDataconnection
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DebugDataconnectionRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DebugDataconnectionResponse`
        """
        http_info = self._debug_dataconnection_http_info(request)
        return self._call_api(**http_info)

    def debug_dataconnection_invoker(self, request):
        http_info = self._debug_dataconnection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _debug_dataconnection_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/data-connections/validation",
            "request_type": request.__class__.__name__,
            "response_type": "DebugDataconnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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
        """删除应用

        删除应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApp
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteAppRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteAppResponse`
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
            "resource_path": "/v1/{project_id}/service/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_approver(self, request):
        """删除审批人

        删除审批人
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApprover
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteApproverRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteApproverResponse`
        """
        http_info = self._delete_approver_http_info(request)
        return self._call_api(**http_info)

    def delete_approver_invoker(self, request):
        http_info = self._delete_approver_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_approver_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/design/approvals/users",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteApproverResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'approver_ids' in local_var_params:
            query_params.append(('approver_ids', local_var_params['approver_ids']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_asset(self, request):
        """删除资产

        删除资产
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAsset
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteAssetRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteAssetResponse`
        """
        http_info = self._delete_asset_http_info(request)
        return self._call_api(**http_info)

    def delete_asset_invoker(self, request):
        http_info = self._delete_asset_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_asset_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/asset/{guid}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAssetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'guid' in local_var_params:
            path_params['guid'] = local_var_params['guid']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_biz_metric(self, request):
        """删除业务指标

        删除业务指标
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBizMetric
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteBizMetricRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteBizMetricResponse`
        """
        http_info = self._delete_biz_metric_http_info(request)
        return self._call_api(**http_info)

    def delete_biz_metric_invoker(self, request):
        http_info = self._delete_biz_metric_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_biz_metric_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/design/biz-metrics",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBizMetricResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def delete_catalog(self, request):
        """删除流程架构

        删除流程架构
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCatalog
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteCatalogRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteCatalogResponse`
        """
        http_info = self._delete_catalog_http_info(request)
        return self._call_api(**http_info)

    def delete_catalog_invoker(self, request):
        http_info = self._delete_catalog_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_catalog_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/design/biz/catalogs",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCatalogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def delete_classification_from_entities(self, request):
        """移除资产关联的分类

        移除资产关联分类：
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteClassificationFromEntities
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteClassificationFromEntitiesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteClassificationFromEntitiesResponse`
        """
        http_info = self._delete_classification_from_entities_http_info(request)
        return self._call_api(**http_info)

    def delete_classification_from_entities_invoker(self, request):
        http_info = self._delete_classification_from_entities_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_classification_from_entities_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/asset/entities/guid/{guid}/classification",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteClassificationFromEntitiesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'guid' in local_var_params:
            path_params['guid'] = local_var_params['guid']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def delete_code_table(self, request):
        """删除码表

        删除码表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCodeTable
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteCodeTableRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteCodeTableResponse`
        """
        http_info = self._delete_code_table_http_info(request)
        return self._call_api(**http_info)

    def delete_code_table_invoker(self, request):
        http_info = self._delete_code_table_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_code_table_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/design/code-tables",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCodeTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def delete_dataconnection(self, request):
        """删除数据连接

        删除数据连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDataconnection
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteDataconnectionRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteDataconnectionResponse`
        """
        http_info = self._delete_dataconnection_http_info(request)
        return self._call_api(**http_info)

    def delete_dataconnection_invoker(self, request):
        http_info = self._delete_dataconnection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_dataconnection_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/data-connections/{data_connection_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDataconnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'data_connection_id' in local_var_params:
            path_params['data_connection_id'] = local_var_params['data_connection_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_directory(self, request):
        """删除目录

        删除目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDirectory
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteDirectoryRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteDirectoryResponse`
        """
        http_info = self._delete_directory_http_info(request)
        return self._call_api(**http_info)

    def delete_directory_invoker(self, request):
        http_info = self._delete_directory_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_directory_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/design/directorys",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDirectoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ids' in local_var_params:
            query_params.append(('ids', local_var_params['ids']))
            collection_formats['ids'] = 'csv'

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_security_level_from_entity(self, request):
        """移除资产关联密级

        移除资产关联密级
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSecurityLevelFromEntity
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteSecurityLevelFromEntityRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteSecurityLevelFromEntityResponse`
        """
        http_info = self._delete_security_level_from_entity_http_info(request)
        return self._call_api(**http_info)

    def delete_security_level_from_entity_invoker(self, request):
        http_info = self._delete_security_level_from_entity_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_security_level_from_entity_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/asset/entities/guid/{guid}/security-level",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSecurityLevelFromEntityResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'guid' in local_var_params:
            path_params['guid'] = local_var_params['guid']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_service_catalog(self, request):
        """批量删除目录

        批量删除目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteServiceCatalog
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteServiceCatalogRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteServiceCatalogResponse`
        """
        http_info = self._delete_service_catalog_http_info(request)
        return self._call_api(**http_info)

    def delete_service_catalog_invoker(self, request):
        http_info = self._delete_service_catalog_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_service_catalog_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/service/servicecatalogs/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteServiceCatalogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

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

    def delete_standard(self, request):
        """删除数据标准

        删除数据标准
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteStandard
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteStandardRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteStandardResponse`
        """
        http_info = self._delete_standard_http_info(request)
        return self._call_api(**http_info)

    def delete_standard_invoker(self, request):
        http_info = self._delete_standard_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_standard_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/design/standards",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteStandardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def delete_standard_template(self, request):
        """删除数据标准模板

        删除数据标准模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteStandardTemplate
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteStandardTemplateRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteStandardTemplateResponse`
        """
        http_info = self._delete_standard_template_http_info(request)
        return self._call_api(**http_info)

    def delete_standard_template_invoker(self, request):
        http_info = self._delete_standard_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_standard_template_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/design/standards/templates",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteStandardTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ids' in local_var_params:
            query_params.append(('ids', local_var_params['ids']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_subject(self, request):
        """删除主题

        删除主题
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSubject
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteSubjectRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteSubjectResponse`
        """
        http_info = self._delete_subject_http_info(request)
        return self._call_api(**http_info)

    def delete_subject_invoker(self, request):
        http_info = self._delete_subject_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_subject_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/design/subjects",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSubjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def delete_subject_new(self, request):
        """删除主题(新)

        删除主题(新)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSubjectNew
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteSubjectNewRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteSubjectNewResponse`
        """
        http_info = self._delete_subject_new_http_info(request)
        return self._call_api(**http_info)

    def delete_subject_new_invoker(self, request):
        http_info = self._delete_subject_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_subject_new_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/design/subjects",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSubjectNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def delete_table_model(self, request):
        """删除模型实体

        删除一个模型实体，包括逻辑实体或物理数据表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTableModel
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteTableModelRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteTableModelResponse`
        """
        http_info = self._delete_table_model_http_info(request)
        return self._call_api(**http_info)

    def delete_table_model_invoker(self, request):
        http_info = self._delete_table_model_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_table_model_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/design/table-model",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTableModelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def delete_task_info(self, request):
        """删除单个采集任务

        删除单个采集任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTaskInfo
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteTaskInfoRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteTaskInfoResponse`
        """
        http_info = self._delete_task_info_http_info(request)
        return self._call_api(**http_info)

    def delete_task_info_invoker(self, request):
        http_info = self._delete_task_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_task_info_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/metadata/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTaskInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_workspaces(self, request):
        """删除模型工作区

        删除模型工作区
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteWorkspaces
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteWorkspacesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteWorkspacesResponse`
        """
        http_info = self._delete_workspaces_http_info(request)
        return self._call_api(**http_info)

    def delete_workspaces_invoker(self, request):
        http_info = self._delete_workspaces_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_workspaces_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/design/workspaces",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteWorkspacesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ids' in local_var_params:
            query_params.append(('ids', local_var_params['ids']))
            collection_formats['ids'] = 'csv'

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_workspaceusers(self, request):
        """删除工作空间用户

        删除工作空间用户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteWorkspaceusers
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteWorkspaceusersRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteWorkspaceusersResponse`
        """
        http_info = self._delete_workspaceusers_http_info(request)
        return self._call_api(**http_info)

    def delete_workspaceusers_invoker(self, request):
        http_info = self._delete_workspaceusers_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_workspaceusers_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{workspace_id}/delete-users",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteWorkspaceusersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

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

    def execute_task_action(self, request):
        """启动、调度、停止采集任务

        启动、调度、停止采集任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteTaskAction
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ExecuteTaskActionRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ExecuteTaskActionResponse`
        """
        http_info = self._execute_task_action_http_info(request)
        return self._call_api(**http_info)

    def execute_task_action_invoker(self, request):
        http_info = self._execute_task_action_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_task_action_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/metadata/tasks/{task_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteTaskActionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def import_result(self, request):
        """查询导入结果

        查询导入excel的处理结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportResult
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ImportResultRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ImportResultResponse`
        """
        http_info = self._import_result_http_info(request)
        return self._call_api(**http_info)

    def import_result_invoker(self, request):
        http_info = self._import_result_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_result_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/catelogs/process-import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uuid' in local_var_params:
            query_params.append(('uuid', local_var_params['uuid']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def initialize_standard_template(self, request):
        """初始化数据标准模板

        初始化模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for InitializeStandardTemplate
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.InitializeStandardTemplateRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.InitializeStandardTemplateResponse`
        """
        http_info = self._initialize_standard_template_http_info(request)
        return self._call_api(**http_info)

    def initialize_standard_template_invoker(self, request):
        http_info = self._initialize_standard_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _initialize_standard_template_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/design/standards/templates/action",
            "request_type": request.__class__.__name__,
            "response_type": "InitializeStandardTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action-id', local_var_params['action_id']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def list_aggregation_logic_tables(self, request):
        """查找汇总表

        通过中英文名称、创建者、审核人、状态、修改时间分页查找汇总表信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAggregationLogicTables
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListAggregationLogicTablesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListAggregationLogicTablesResponse`
        """
        http_info = self._list_aggregation_logic_tables_http_info(request)
        return self._call_api(**http_info)

    def list_aggregation_logic_tables_invoker(self, request):
        http_info = self._list_aggregation_logic_tables_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_aggregation_logic_tables_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/aggregation-logic-tables",
            "request_type": request.__class__.__name__,
            "response_type": "ListAggregationLogicTablesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'create_by' in local_var_params:
            query_params.append(('create_by', local_var_params['create_by']))
        if 'approver' in local_var_params:
            query_params.append(('approver', local_var_params['approver']))
        if 'owner' in local_var_params:
            query_params.append(('owner', local_var_params['owner']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'sync_status' in local_var_params:
            query_params.append(('sync_status', local_var_params['sync_status']))
        if 'sync_key' in local_var_params:
            query_params.append(('sync_key', local_var_params['sync_key']))
            collection_formats['sync_key'] = 'csv'
        if 'l3_id' in local_var_params:
            query_params.append(('l3_id', local_var_params['l3_id']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'biz_catalog_id' in local_var_params:
            query_params.append(('biz_catalog_id', local_var_params['biz_catalog_id']))
        if 'auto_generate' in local_var_params:
            query_params.append(('auto_generate', local_var_params['auto_generate']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_all_catalog_list(self, request):
        """获取当前目录下的所有类型列表

        获取当前目录下的所有类型列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAllCatalogList
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListAllCatalogListRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListAllCatalogListResponse`
        """
        http_info = self._list_all_catalog_list_http_info(request)
        return self._call_api(**http_info)

    def list_all_catalog_list_invoker(self, request):
        http_info = self._list_all_catalog_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_all_catalog_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/servicecatalogs/{catalog_id}/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllCatalogListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'catalog_id' in local_var_params:
            path_params['catalog_id'] = local_var_params['catalog_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_all_standards(self, request):
        """获取数据标准

        获取数据标准
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAllStandards
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListAllStandardsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListAllStandardsResponse`
        """
        http_info = self._list_all_standards_http_info(request)
        return self._call_api(**http_info)

    def list_all_standards_invoker(self, request):
        http_info = self._list_all_standards_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_all_standards_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/standards",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllStandardsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'directory_id' in local_var_params:
            query_params.append(('directory_id', local_var_params['directory_id']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_api_catalog_list(self, request):
        """获取当前目录下的api列表

        获取当前目录下的api列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApiCatalogList
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListApiCatalogListRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListApiCatalogListResponse`
        """
        http_info = self._list_api_catalog_list_http_info(request)
        return self._call_api(**http_info)

    def list_api_catalog_list_invoker(self, request):
        http_info = self._list_api_catalog_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_api_catalog_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/servicecatalogs/{catalog_id}/apis",
            "request_type": request.__class__.__name__,
            "response_type": "ListApiCatalogListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'catalog_id' in local_var_params:
            path_params['catalog_id'] = local_var_params['catalog_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_api_top_n(self, request):
        """查询指定api 应用调用topN

        查询指定api 应用调用topN
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApiTopN
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListApiTopNRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListApiTopNResponse`
        """
        http_info = self._list_api_top_n_http_info(request)
        return self._call_api(**http_info)

    def list_api_top_n_invoker(self, request):
        http_info = self._list_api_top_n_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_api_top_n_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/statistic/apis-top-n/{api_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListApiTopNResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'time_unit' in local_var_params:
            query_params.append(('time_unit', local_var_params['time_unit']))
        if 'top_num' in local_var_params:
            query_params.append(('top_num', local_var_params['top_num']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_apic_groups(self, request):
        """获取网关分组

        获取网关分组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApicGroups
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListApicGroupsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListApicGroupsResponse`
        """
        http_info = self._list_apic_groups_http_info(request)
        return self._call_api(**http_info)

    def list_apic_groups_invoker(self, request):
        http_info = self._list_apic_groups_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_apic_groups_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/apigw/instances/{apig_instance_id}/groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListApicGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'apig_instance_id' in local_var_params:
            path_params['apig_instance_id'] = local_var_params['apig_instance_id']

        query_params = []
        if 'apig_type' in local_var_params:
            query_params.append(('apig_type', local_var_params['apig_type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_apic_instances(self, request):
        """获取网关实例

        获取网关实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApicInstances
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListApicInstancesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListApicInstancesResponse`
        """
        http_info = self._list_apic_instances_http_info(request)
        return self._call_api(**http_info)

    def list_apic_instances_invoker(self, request):
        http_info = self._list_apic_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_apic_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/apigw/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListApicInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'apig_type' in local_var_params:
            query_params.append(('apig_type', local_var_params['apig_type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_apis_top(self, request):
        """查询api 服务调用topN

        查询api 服务调用topN
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApisTop
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListApisTopRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListApisTopResponse`
        """
        http_info = self._list_apis_top_http_info(request)
        return self._call_api(**http_info)

    def list_apis_top_invoker(self, request):
        http_info = self._list_apis_top_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_apis_top_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/statistic/apis-top-n",
            "request_type": request.__class__.__name__,
            "response_type": "ListApisTopResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'time_unit' in local_var_params:
            query_params.append(('time_unit', local_var_params['time_unit']))
        if 'top_num' in local_var_params:
            query_params.append(('top_num', local_var_params['top_num']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_apply(self, request):
        """查询申请列表

        查询申请列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApply
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListApplyRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListApplyResponse`
        """
        http_info = self._list_apply_http_info(request)
        return self._call_api(**http_info)

    def list_apply_invoker(self, request):
        http_info = self._list_apply_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_apply_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/applys",
            "request_type": request.__class__.__name__,
            "response_type": "ListApplyResponse"
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
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))
        if 'query_type' in local_var_params:
            query_params.append(('query_type', local_var_params['query_type']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_approvers(self, request):
        """查询审批人列表

        查询审批人列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApprovers
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListApproversRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListApproversResponse`
        """
        http_info = self._list_approvers_http_info(request)
        return self._call_api(**http_info)

    def list_approvers_invoker(self, request):
        http_info = self._list_approvers_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_approvers_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/approvals/users",
            "request_type": request.__class__.__name__,
            "response_type": "ListApproversResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'approver_name' in local_var_params:
            query_params.append(('approver_name', local_var_params['approver_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_apps(self, request):
        """查询应用列表

        查询应用列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApps
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListAppsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListAppsResponse`
        """
        http_info = self._list_apps_http_info(request)
        return self._call_api(**http_info)

    def list_apps_invoker(self, request):
        http_info = self._list_apps_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_apps_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/apps",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppsResponse"
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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'app_type' in local_var_params:
            query_params.append(('app_type', local_var_params['app_type']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_apps_top(self, request):
        """查询app 服务使用topN

        查询app 服务使用topN
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAppsTop
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListAppsTopRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListAppsTopResponse`
        """
        http_info = self._list_apps_top_http_info(request)
        return self._call_api(**http_info)

    def list_apps_top_invoker(self, request):
        http_info = self._list_apps_top_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_apps_top_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/statistic/apps-top-n",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppsTopResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'time_unit' in local_var_params:
            query_params.append(('time_unit', local_var_params['time_unit']))
        if 'top_num' in local_var_params:
            query_params.append(('top_num', local_var_params['top_num']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_biz_metric_dimensions(self, request):
        """查看指标维度信息

        查看指标维度信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBizMetricDimensions
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListBizMetricDimensionsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListBizMetricDimensionsResponse`
        """
        http_info = self._list_biz_metric_dimensions_http_info(request)
        return self._call_api(**http_info)

    def list_biz_metric_dimensions_invoker(self, request):
        http_info = self._list_biz_metric_dimensions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_biz_metric_dimensions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/biz-metrics/dimensions",
            "request_type": request.__class__.__name__,
            "response_type": "ListBizMetricDimensionsResponse"
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
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_biz_metric_owners(self, request):
        """查看指标指标责任人信息

        查看指标指标责任人信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBizMetricOwners
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListBizMetricOwnersRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListBizMetricOwnersResponse`
        """
        http_info = self._list_biz_metric_owners_http_info(request)
        return self._call_api(**http_info)

    def list_biz_metric_owners_invoker(self, request):
        http_info = self._list_biz_metric_owners_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_biz_metric_owners_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/biz-metrics/owners",
            "request_type": request.__class__.__name__,
            "response_type": "ListBizMetricOwnersResponse"
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
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_biz_metrics(self, request):
        """查询业务指标信息

        通过名称、创建者、修改时间分页查找业务指标信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBizMetrics
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListBizMetricsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListBizMetricsResponse`
        """
        http_info = self._list_biz_metrics_http_info(request)
        return self._call_api(**http_info)

    def list_biz_metrics_invoker(self, request):
        http_info = self._list_biz_metrics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_biz_metrics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/biz-metrics",
            "request_type": request.__class__.__name__,
            "response_type": "ListBizMetricsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'create_by' in local_var_params:
            query_params.append(('create_by', local_var_params['create_by']))
        if 'owner' in local_var_params:
            query_params.append(('owner', local_var_params['owner']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'sync_status' in local_var_params:
            query_params.append(('sync_status', local_var_params['sync_status']))
        if 'sync_key' in local_var_params:
            query_params.append(('sync_key', local_var_params['sync_key']))
            collection_formats['sync_key'] = 'csv'
        if 'biz_catalog_id' in local_var_params:
            query_params.append(('biz_catalog_id', local_var_params['biz_catalog_id']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_business(self, request):
        """获取主题树信息

        获取数据资产主题树信息l1，l2，l3
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBusiness
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListBusinessRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListBusinessResponse`
        """
        http_info = self._list_business_http_info(request)
        return self._call_api(**http_info)

    def list_business_invoker(self, request):
        http_info = self._list_business_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_business_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/subjects/business",
            "request_type": request.__class__.__name__,
            "response_type": "ListBusinessResponse"
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
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_catalog_list(self, request):
        """获取当前目录下的目录列表（全量）

        获取当前目录下的目录列表（全量）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCatalogList
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListCatalogListRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListCatalogListResponse`
        """
        http_info = self._list_catalog_list_http_info(request)
        return self._call_api(**http_info)

    def list_catalog_list_invoker(self, request):
        http_info = self._list_catalog_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_catalog_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/servicecatalogs/{catalog_id}/catalogs",
            "request_type": request.__class__.__name__,
            "response_type": "ListCatalogListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'catalog_id' in local_var_params:
            path_params['catalog_id'] = local_var_params['catalog_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_catalog_tree(self, request):
        """获取所有流程架构目录树

        获取所有目录树
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCatalogTree
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListCatalogTreeRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListCatalogTreeResponse`
        """
        http_info = self._list_catalog_tree_http_info(request)
        return self._call_api(**http_info)

    def list_catalog_tree_invoker(self, request):
        http_info = self._list_catalog_tree_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_catalog_tree_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/biz/catalogs/tree",
            "request_type": request.__class__.__name__,
            "response_type": "ListCatalogTreeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_category(self, request):
        """获取作业目录

        获取作业目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCategory
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListCategoryRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListCategoryResponse`
        """
        http_info = self._list_category_http_info(request)
        return self._call_api(**http_info)

    def list_category_invoker(self, request):
        http_info = self._list_category_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_category_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/quality/categories",
            "request_type": request.__class__.__name__,
            "response_type": "ListCategoryResponse"
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
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'accept' in local_var_params:
            header_params['accept'] = local_var_params['accept']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_columns(self, request):
        """获取数据源中表的字段

        获取数据源中表的字段
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListColumns
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListColumnsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListColumnsResponse`
        """
        http_info = self._list_columns_http_info(request)
        return self._call_api(**http_info)

    def list_columns_invoker(self, request):
        http_info = self._list_columns_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_columns_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/{connection_id}/datatables/{table_id}/columns",
            "request_type": request.__class__.__name__,
            "response_type": "ListColumnsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']
        if 'table_id' in local_var_params:
            path_params['table_id'] = local_var_params['table_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_compound_metrics(self, request):
        """查找复合指标

        通过中英文名称、创建者、审核人、状态、修改时间、l3Id分页查找复合指标信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCompoundMetrics
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListCompoundMetricsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListCompoundMetricsResponse`
        """
        http_info = self._list_compound_metrics_http_info(request)
        return self._call_api(**http_info)

    def list_compound_metrics_invoker(self, request):
        http_info = self._list_compound_metrics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_compound_metrics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/compound-metrics",
            "request_type": request.__class__.__name__,
            "response_type": "ListCompoundMetricsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'create_by' in local_var_params:
            query_params.append(('create_by', local_var_params['create_by']))
        if 'approver' in local_var_params:
            query_params.append(('approver', local_var_params['approver']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'dimension_group' in local_var_params:
            query_params.append(('dimension_group', local_var_params['dimension_group']))
        if 'atomic_index_id' in local_var_params:
            query_params.append(('atomic_index_id', local_var_params['atomic_index_id']))
        if 'l3_id' in local_var_params:
            query_params.append(('l3_id', local_var_params['l3_id']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_condition(self, request):
        """查找业务限定

        通过中英文名称、描述、创建者、审核人、限定分组id、修改时间状态分页查找限定信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCondition
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListConditionRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListConditionResponse`
        """
        http_info = self._list_condition_http_info(request)
        return self._call_api(**http_info)

    def list_condition_invoker(self, request):
        http_info = self._list_condition_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_condition_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/conditions",
            "request_type": request.__class__.__name__,
            "response_type": "ListConditionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'create_by' in local_var_params:
            query_params.append(('create_by', local_var_params['create_by']))
        if 'approver' in local_var_params:
            query_params.append(('approver', local_var_params['approver']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_consistency_task(self, request):
        """获取对账作业列表

        获取对账作业列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConsistencyTask
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListConsistencyTaskRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListConsistencyTaskResponse`
        """
        http_info = self._list_consistency_task_http_info(request)
        return self._call_api(**http_info)

    def list_consistency_task_invoker(self, request):
        http_info = self._list_consistency_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_consistency_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/quality/consistency-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListConsistencyTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'category_id' in local_var_params:
            query_params.append(('category_id', local_var_params['category_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'schedule_status' in local_var_params:
            query_params.append(('schedule_status', local_var_params['schedule_status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'creator' in local_var_params:
            query_params.append(('creator', local_var_params['creator']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_data_arts_studio_instances(self, request):
        """获取实例列表

        获取实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDataArtsStudioInstances
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListDataArtsStudioInstancesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListDataArtsStudioInstancesResponse`
        """
        http_info = self._list_data_arts_studio_instances_http_info(request)
        return self._call_api(**http_info)

    def list_data_arts_studio_instances_invoker(self, request):
        http_info = self._list_data_arts_studio_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_data_arts_studio_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListDataArtsStudioInstancesResponse"
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

    def list_data_tables(self, request):
        """获取数据源中的表

        获取数据源中的表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDataTables
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListDataTablesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListDataTablesResponse`
        """
        http_info = self._list_data_tables_http_info(request)
        return self._call_api(**http_info)

    def list_data_tables_invoker(self, request):
        http_info = self._list_data_tables_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_data_tables_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/{connection_id}/datatables",
            "request_type": request.__class__.__name__,
            "response_type": "ListDataTablesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

        query_params = []
        if 'database_name' in local_var_params:
            query_params.append(('database_name', local_var_params['database_name']))
        if 'table_name' in local_var_params:
            query_params.append(('table_name', local_var_params['table_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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
        """获取数据库列表

        获取数据库列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDatabases
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListDatabasesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListDatabasesResponse`
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
            "resource_path": "/v2/{project_id}/{connection_id}/databases",
            "request_type": request.__class__.__name__,
            "response_type": "ListDatabasesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_dataconnections(self, request):
        """查询数据连接列表

        查询数据连接列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDataconnections
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListDataconnectionsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListDataconnectionsResponse`
        """
        http_info = self._list_dataconnections_http_info(request)
        return self._call_api(**http_info)

    def list_dataconnections_invoker(self, request):
        http_info = self._list_dataconnections_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_dataconnections_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/data-connections",
            "request_type": request.__class__.__name__,
            "response_type": "ListDataconnectionsResponse"
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
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_derivative_indexes(self, request):
        """查找衍生指标

        通过中英文名称、创建者、审核人、状态、修改时间、l3Id分页查找衍生指标信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDerivativeIndexes
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListDerivativeIndexesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListDerivativeIndexesResponse`
        """
        http_info = self._list_derivative_indexes_http_info(request)
        return self._call_api(**http_info)

    def list_derivative_indexes_invoker(self, request):
        http_info = self._list_derivative_indexes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_derivative_indexes_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/derivative-indexs",
            "request_type": request.__class__.__name__,
            "response_type": "ListDerivativeIndexesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'create_by' in local_var_params:
            query_params.append(('create_by', local_var_params['create_by']))
        if 'approver' in local_var_params:
            query_params.append(('approver', local_var_params['approver']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'dimension_id' in local_var_params:
            query_params.append(('dimension_id', local_var_params['dimension_id']))
        if 'dimension_group' in local_var_params:
            query_params.append(('dimension_group', local_var_params['dimension_group']))
        if 'atomic_index_id' in local_var_params:
            query_params.append(('atomic_index_id', local_var_params['atomic_index_id']))
        if 'all_metrics' in local_var_params:
            query_params.append(('all_metrics', local_var_params['all_metrics']))
        if 'dw_type' in local_var_params:
            query_params.append(('dw_type', local_var_params['dw_type']))
        if 'l3_id' in local_var_params:
            query_params.append(('l3_id', local_var_params['l3_id']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_dimension_groups(self, request):
        """查看维度颗粒度

        查询维度颗粒度, 依据tableId查询涉及所有维度，不传tableId查询所有维度组颗粒度
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDimensionGroups
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListDimensionGroupsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListDimensionGroupsResponse`
        """
        http_info = self._list_dimension_groups_http_info(request)
        return self._call_api(**http_info)

    def list_dimension_groups_invoker(self, request):
        http_info = self._list_dimension_groups_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_dimension_groups_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/dimension/groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListDimensionGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'table_id' in local_var_params:
            query_params.append(('table_id', local_var_params['table_id']))
        if 'biz_type' in local_var_params:
            query_params.append(('biz_type', local_var_params['biz_type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_dimension_logic_tables(self, request):
        """查找维度表

        通过中英文名称、创建者、审核人、状态、修改时间分页查找维度表信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDimensionLogicTables
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListDimensionLogicTablesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListDimensionLogicTablesResponse`
        """
        http_info = self._list_dimension_logic_tables_http_info(request)
        return self._call_api(**http_info)

    def list_dimension_logic_tables_invoker(self, request):
        http_info = self._list_dimension_logic_tables_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_dimension_logic_tables_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/dimension-logic-tables",
            "request_type": request.__class__.__name__,
            "response_type": "ListDimensionLogicTablesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'create_by' in local_var_params:
            query_params.append(('create_by', local_var_params['create_by']))
        if 'approver' in local_var_params:
            query_params.append(('approver', local_var_params['approver']))
        if 'owner' in local_var_params:
            query_params.append(('owner', local_var_params['owner']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'sync_status' in local_var_params:
            query_params.append(('sync_status', local_var_params['sync_status']))
        if 'sync_key' in local_var_params:
            query_params.append(('sync_key', local_var_params['sync_key']))
            collection_formats['sync_key'] = 'csv'
        if 'l2_id' in local_var_params:
            query_params.append(('l2_id', local_var_params['l2_id']))
        if 'dimension_id' in local_var_params:
            query_params.append(('dimension_id', local_var_params['dimension_id']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'biz_catalog_id' in local_var_params:
            query_params.append(('biz_catalog_id', local_var_params['biz_catalog_id']))
        if 'dimension_type' in local_var_params:
            query_params.append(('dimension_type', local_var_params['dimension_type']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_dimensions(self, request):
        """查找维度

        通过中英文名称、描述、创建者、审核人、状态、l3Id、派生指标idList、修改时间分页查找维度信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDimensions
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListDimensionsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListDimensionsResponse`
        """
        http_info = self._list_dimensions_http_info(request)
        return self._call_api(**http_info)

    def list_dimensions_invoker(self, request):
        http_info = self._list_dimensions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_dimensions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/dimensions",
            "request_type": request.__class__.__name__,
            "response_type": "ListDimensionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'create_by' in local_var_params:
            query_params.append(('create_by', local_var_params['create_by']))
        if 'approver' in local_var_params:
            query_params.append(('approver', local_var_params['approver']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'l2_id' in local_var_params:
            query_params.append(('l2_id', local_var_params['l2_id']))
        if 'derivative_ids' in local_var_params:
            query_params.append(('derivative_ids', local_var_params['derivative_ids']))
            collection_formats['derivative_ids'] = 'csv'
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'fact_logic_id' in local_var_params:
            query_params.append(('fact_logic_id', local_var_params['fact_logic_id']))
        if 'dimension_type' in local_var_params:
            query_params.append(('dimension_type', local_var_params['dimension_type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'biz_catalog_id' in local_var_params:
            query_params.append(('biz_catalog_id', local_var_params['biz_catalog_id']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_directories(self, request):
        """获取所有目录

        获取所有目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDirectories
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListDirectoriesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListDirectoriesResponse`
        """
        http_info = self._list_directories_http_info(request)
        return self._call_api(**http_info)

    def list_directories_invoker(self, request):
        http_info = self._list_directories_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_directories_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/directorys",
            "request_type": request.__class__.__name__,
            "response_type": "ListDirectoriesResponse"
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
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_fact_logic_tables(self, request):
        """查找事实表

        通过中英文名称、创建者、审核人、状态、修改时间分页查找事实表信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFactLogicTables
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListFactLogicTablesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListFactLogicTablesResponse`
        """
        http_info = self._list_fact_logic_tables_http_info(request)
        return self._call_api(**http_info)

    def list_fact_logic_tables_invoker(self, request):
        http_info = self._list_fact_logic_tables_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_fact_logic_tables_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/fact-logic-tables",
            "request_type": request.__class__.__name__,
            "response_type": "ListFactLogicTablesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'create_by' in local_var_params:
            query_params.append(('create_by', local_var_params['create_by']))
        if 'approver' in local_var_params:
            query_params.append(('approver', local_var_params['approver']))
        if 'owner' in local_var_params:
            query_params.append(('owner', local_var_params['owner']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'sync_status' in local_var_params:
            query_params.append(('sync_status', local_var_params['sync_status']))
        if 'sync_key' in local_var_params:
            query_params.append(('sync_key', local_var_params['sync_key']))
            collection_formats['sync_key'] = 'csv'
        if 'l3_id' in local_var_params:
            query_params.append(('l3_id', local_var_params['l3_id']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'biz_catalog_id' in local_var_params:
            query_params.append(('biz_catalog_id', local_var_params['biz_catalog_id']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_instances(self, request):
        """获取任务执行结果列表

        获取任务执行结果列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstances
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListInstancesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListInstancesResponse`
        """
        http_info = self._list_instances_http_info(request)
        return self._call_api(**http_info)

    def list_instances_invoker(self, request):
        http_info = self._list_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/quality/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'task_type' in local_var_params:
            query_params.append(('task_type', local_var_params['task_type']))
        if 'run_status' in local_var_params:
            query_params.append(('run_status', local_var_params['run_status']))
        if 'notify_status' in local_var_params:
            query_params.append(('notify_status', local_var_params['notify_status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_manager_work_spaces(self, request):
        """获取工作空间列表

        获取工作空间列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListManagerWorkSpaces
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListManagerWorkSpacesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListManagerWorkSpacesResponse`
        """
        http_info = self._list_manager_work_spaces_http_info(request)
        return self._call_api(**http_info)

    def list_manager_work_spaces_invoker(self, request):
        http_info = self._list_manager_work_spaces_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_manager_work_spaces_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListManagerWorkSpacesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_message(self, request):
        """查询消息列表

        查询消息列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMessage
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListMessageRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListMessageResponse`
        """
        http_info = self._list_message_http_info(request)
        return self._call_api(**http_info)

    def list_message_invoker(self, request):
        http_info = self._list_message_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_message_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/messages",
            "request_type": request.__class__.__name__,
            "response_type": "ListMessageResponse"
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
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_metric_relations(self, request):
        """获取指标关联信息

        获取当前指标图谱
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMetricRelations
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListMetricRelationsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListMetricRelationsResponse`
        """
        http_info = self._list_metric_relations_http_info(request)
        return self._call_api(**http_info)

    def list_metric_relations_invoker(self, request):
        http_info = self._list_metric_relations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_metric_relations_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/metric-relations/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListMetricRelationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'biz_type' in local_var_params:
            query_params.append(('biz_type', local_var_params['biz_type']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_quality_task(self, request):
        """获取质量作业列表

        获取质量作业列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQualityTask
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListQualityTaskRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListQualityTaskResponse`
        """
        http_info = self._list_quality_task_http_info(request)
        return self._call_api(**http_info)

    def list_quality_task_invoker(self, request):
        http_info = self._list_quality_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_quality_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/quality/quality-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListQualityTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'category_id' in local_var_params:
            query_params.append(('category_id', local_var_params['category_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'schedule_status' in local_var_params:
            query_params.append(('schedule_status', local_var_params['schedule_status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'creator' in local_var_params:
            query_params.append(('creator', local_var_params['creator']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_quality_task_lists(self, request):
        """获取质量作业列表V1

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQualityTaskLists
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListQualityTaskListsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListQualityTaskListsResponse`
        """
        http_info = self._list_quality_task_lists_http_info(request)
        return self._call_api(**http_info)

    def list_quality_task_lists_invoker(self, request):
        http_info = self._list_quality_task_lists_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_quality_task_lists_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/quality/rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListQualityTaskListsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'category_id' in local_var_params:
            query_params.append(('category_id', local_var_params['category_id']))
        if 'rule_name' in local_var_params:
            query_params.append(('rule_name', local_var_params['rule_name']))
        if 'schedule_status' in local_var_params:
            query_params.append(('schedule_status', local_var_params['schedule_status']))
        if 'schedule_period' in local_var_params:
            query_params.append(('schedule_period', local_var_params['schedule_period']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'result_status' in local_var_params:
            query_params.append(('result_status', local_var_params['result_status']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_quality_templates(self, request):
        """获取规则模板列表

        分页获取规则模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQualityTemplates
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListQualityTemplatesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListQualityTemplatesResponse`
        """
        http_info = self._list_quality_templates_http_info(request)
        return self._call_api(**http_info)

    def list_quality_templates_invoker(self, request):
        http_info = self._list_quality_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_quality_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/quality/rule-templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListQualityTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'category_id' in local_var_params:
            query_params.append(('category_id', local_var_params['category_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'system_template' in local_var_params:
            query_params.append(('system_template', local_var_params['system_template']))
        if 'creator' in local_var_params:
            query_params.append(('creator', local_var_params['creator']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_relations(self, request):
        """关系

        通过名称、等分页查找关系信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRelations
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListRelationsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListRelationsResponse`
        """
        http_info = self._list_relations_http_info(request)
        return self._call_api(**http_info)

    def list_relations_invoker(self, request):
        http_info = self._list_relations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_relations_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/relation",
            "request_type": request.__class__.__name__,
            "response_type": "ListRelationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'create_by' in local_var_params:
            query_params.append(('create_by', local_var_params['create_by']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_schemas(self, request):
        """获取schemas

        获取schemas,目前只有DWS和采用postgresql驱动的RDS数据源支持schema,请在调用前确认该数据源是否支持schema字段
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSchemas
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListSchemasRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListSchemasResponse`
        """
        http_info = self._list_schemas_http_info(request)
        return self._call_api(**http_info)

    def list_schemas_invoker(self, request):
        http_info = self._list_schemas_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_schemas_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/{connection_id}/schemas",
            "request_type": request.__class__.__name__,
            "response_type": "ListSchemasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

        query_params = []
        if 'database_name' in local_var_params:
            query_params.append(('database_name', local_var_params['database_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_subject_levels(self, request):
        """获取主题层级

        获取主题层级
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSubjectLevels
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListSubjectLevelsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListSubjectLevelsResponse`
        """
        http_info = self._list_subject_levels_http_info(request)
        return self._call_api(**http_info)

    def list_subject_levels_invoker(self, request):
        http_info = self._list_subject_levels_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_subject_levels_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/subject-levels",
            "request_type": request.__class__.__name__,
            "response_type": "ListSubjectLevelsResponse"
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
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_table_model_relations(self, request):
        """查询模型下所有关系

        查询模型下所有关系
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTableModelRelations
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListTableModelRelationsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListTableModelRelationsResponse`
        """
        http_info = self._list_table_model_relations_http_info(request)
        return self._call_api(**http_info)

    def list_table_model_relations_invoker(self, request):
        http_info = self._list_table_model_relations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_table_model_relations_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/{model_id}/table-model/relation",
            "request_type": request.__class__.__name__,
            "response_type": "ListTableModelRelationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'model_id' in local_var_params:
            path_params['model_id'] = local_var_params['model_id']

        query_params = []
        if 'table_ids' in local_var_params:
            query_params.append(('table_ids', local_var_params['table_ids']))
        if 'biz_type' in local_var_params:
            query_params.append(('biz_type', local_var_params['biz_type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_table_models(self, request):
        """查找模型实体列表

        通过中英文名称、创建者、审核人、状态、修改时间分页查找模型实体信息，包含逻辑实体、表或属性。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTableModels
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListTableModelsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListTableModelsResponse`
        """
        http_info = self._list_table_models_http_info(request)
        return self._call_api(**http_info)

    def list_table_models_invoker(self, request):
        http_info = self._list_table_models_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_table_models_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/table-model",
            "request_type": request.__class__.__name__,
            "response_type": "ListTableModelsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'create_by' in local_var_params:
            query_params.append(('create_by', local_var_params['create_by']))
        if 'approver' in local_var_params:
            query_params.append(('approver', local_var_params['approver']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'sync_status' in local_var_params:
            query_params.append(('sync_status', local_var_params['sync_status']))
        if 'sync_key' in local_var_params:
            query_params.append(('sync_key', local_var_params['sync_key']))
            collection_formats['sync_key'] = 'csv'
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'model_id' in local_var_params:
            query_params.append(('model_id', local_var_params['model_id']))
        if 'biz_catalog_id' in local_var_params:
            query_params.append(('biz_catalog_id', local_var_params['biz_catalog_id']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_workspace_roles(self, request):
        """获取工作空间用户角色

        获取工作空间用户角色
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWorkspaceRoles
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListWorkspaceRolesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListWorkspaceRolesResponse`
        """
        http_info = self._list_workspace_roles_http_info(request)
        return self._call_api(**http_info)

    def list_workspace_roles_invoker(self, request):
        http_info = self._list_workspace_roles_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_workspace_roles_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/users/role",
            "request_type": request.__class__.__name__,
            "response_type": "ListWorkspaceRolesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_workspaces(self, request):
        """获取模型

        获取模型
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWorkspaces
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListWorkspacesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListWorkspacesResponse`
        """
        http_info = self._list_workspaces_http_info(request)
        return self._call_api(**http_info)

    def list_workspaces_invoker(self, request):
        http_info = self._list_workspaces_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_workspaces_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/workspaces",
            "request_type": request.__class__.__name__,
            "response_type": "ListWorkspacesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'workspace_type' in local_var_params:
            query_params.append(('workspace_type', local_var_params['workspace_type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'dw_type' in local_var_params:
            query_params.append(('dw_type', local_var_params['dw_type']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_workspaceusers(self, request):
        """获取工作空间用户信息

        获取工作空间用户信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWorkspaceusers
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListWorkspaceusersRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListWorkspaceusersResponse`
        """
        http_info = self._list_workspaceusers_http_info(request)
        return self._call_api(**http_info)

    def list_workspaceusers_invoker(self, request):
        http_info = self._list_workspaceusers_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_workspaceusers_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/{workspace_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "ListWorkspaceusersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

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

    def migrate_api(self, request):
        """批量移动api至新目录

        批量移动api至新目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for MigrateApi
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.MigrateApiRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.MigrateApiResponse`
        """
        http_info = self._migrate_api_http_info(request)
        return self._call_api(**http_info)

    def migrate_api_invoker(self, request):
        http_info = self._migrate_api_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _migrate_api_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/service/servicecatalogs/apis/batch-move",
            "request_type": request.__class__.__name__,
            "response_type": "MigrateApiResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

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

    def migrate_catalog(self, request):
        """移动当前目录至新目录

        移动当前目录至新目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for MigrateCatalog
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.MigrateCatalogRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.MigrateCatalogResponse`
        """
        http_info = self._migrate_catalog_http_info(request)
        return self._call_api(**http_info)

    def migrate_catalog_invoker(self, request):
        http_info = self._migrate_catalog_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _migrate_catalog_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/service/servicecatalogs/{catalog_id}/move",
            "request_type": request.__class__.__name__,
            "response_type": "MigrateCatalogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'catalog_id' in local_var_params:
            path_params['catalog_id'] = local_var_params['catalog_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

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

    def modify_customized_fields(self, request):
        """修改自定义项

        修改自定义项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyCustomizedFields
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ModifyCustomizedFieldsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ModifyCustomizedFieldsResponse`
        """
        http_info = self._modify_customized_fields_http_info(request)
        return self._call_api(**http_info)

    def modify_customized_fields_invoker(self, request):
        http_info = self._modify_customized_fields_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_customized_fields_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/design/customized-fields",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyCustomizedFieldsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def parse_user_behavior(self, request):
        """用户行为分析

        用户行为分析
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ParseUserBehavior
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ParseUserBehaviorRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ParseUserBehaviorResponse`
        """
        http_info = self._parse_user_behavior_http_info(request)
        return self._call_api(**http_info)

    def parse_user_behavior_invoker(self, request):
        http_info = self._parse_user_behavior_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _parse_user_behavior_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/datamap/uba",
            "request_type": request.__class__.__name__,
            "response_type": "ParseUserBehaviorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance' in local_var_params:
            header_params['instance'] = local_var_params['instance']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def pay_for_dgc_one_key(self, request):
        """DataArtsStudio实例一键购买接口

        DataArtsStudio实例一键购买接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PayForDgcOneKey
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.PayForDgcOneKeyRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.PayForDgcOneKeyResponse`
        """
        http_info = self._pay_for_dgc_one_key_http_info(request)
        return self._call_api(**http_info)

    def pay_for_dgc_one_key_invoker(self, request):
        http_info = self._pay_for_dgc_one_key_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _pay_for_dgc_one_key_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/onekey-purchase",
            "request_type": request.__class__.__name__,
            "response_type": "PayForDgcOneKeyResponse"
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

    def reset_link_attribute_and_standard(self, request):
        """关联属性与数据标准

        关联属性与数据标准
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetLinkAttributeAndStandard
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ResetLinkAttributeAndStandardRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ResetLinkAttributeAndStandardResponse`
        """
        http_info = self._reset_link_attribute_and_standard_http_info(request)
        return self._call_api(**http_info)

    def reset_link_attribute_and_standard_invoker(self, request):
        http_info = self._reset_link_attribute_and_standard_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_link_attribute_and_standard_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/design/standards/attribute",
            "request_type": request.__class__.__name__,
            "response_type": "ResetLinkAttributeAndStandardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def rollback_approval(self, request):
        """撤回审批单

        撤回审批单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RollbackApproval
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.RollbackApprovalRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.RollbackApprovalResponse`
        """
        http_info = self._rollback_approval_http_info(request)
        return self._call_api(**http_info)

    def rollback_approval_invoker(self, request):
        http_info = self._rollback_approval_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _rollback_approval_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/design/approvals",
            "request_type": request.__class__.__name__,
            "response_type": "RollbackApprovalResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ids' in local_var_params:
            query_params.append(('ids', local_var_params['ids']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def search_approvals(self, request):
        """获取审批单

        获取审批单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchApprovals
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchApprovalsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchApprovalsResponse`
        """
        http_info = self._search_approvals_http_info(request)
        return self._call_api(**http_info)

    def search_approvals_invoker(self, request):
        http_info = self._search_approvals_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_approvals_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/approvals",
            "request_type": request.__class__.__name__,
            "response_type": "SearchApprovalsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'biz_id' in local_var_params:
            query_params.append(('biz_id', local_var_params['biz_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'create_by' in local_var_params:
            query_params.append(('create_by', local_var_params['create_by']))
        if 'approver' in local_var_params:
            query_params.append(('approver', local_var_params['approver']))
        if 'approval_status' in local_var_params:
            query_params.append(('approval_status', local_var_params['approval_status']))
        if 'approval_status_detail' in local_var_params:
            query_params.append(('approval_status_detail', local_var_params['approval_status_detail']))
        if 'approval_type' in local_var_params:
            query_params.append(('approval_type', local_var_params['approval_type']))
        if 'biz_type' in local_var_params:
            query_params.append(('biz_type', local_var_params['biz_type']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def search_atomic_indexes(self, request):
        """查找原子指标

        通过中英文名称、创建者、审核人、状态、修改时间分页查找原子指标信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchAtomicIndexes
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchAtomicIndexesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchAtomicIndexesResponse`
        """
        http_info = self._search_atomic_indexes_http_info(request)
        return self._call_api(**http_info)

    def search_atomic_indexes_invoker(self, request):
        http_info = self._search_atomic_indexes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_atomic_indexes_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/atomic-indexs",
            "request_type": request.__class__.__name__,
            "response_type": "SearchAtomicIndexesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'create_by' in local_var_params:
            query_params.append(('create_by', local_var_params['create_by']))
        if 'approver' in local_var_params:
            query_params.append(('approver', local_var_params['approver']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'l3_id' in local_var_params:
            query_params.append(('l3_id', local_var_params['l3_id']))
        if 'table_id' in local_var_params:
            query_params.append(('table_id', local_var_params['table_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def search_authorize_app(self, request):
        """查询API已授权的APP

        查询API已授权的APP
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchAuthorizeApp
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchAuthorizeAppRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchAuthorizeAppResponse`
        """
        http_info = self._search_authorize_app_http_info(request)
        return self._call_api(**http_info)

    def search_authorize_app_invoker(self, request):
        http_info = self._search_authorize_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_authorize_app_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/authorize/apis/{api_id}",
            "request_type": request.__class__.__name__,
            "response_type": "SearchAuthorizeAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def search_bind_api(self, request):
        """查询APP已拥有授权的API

        查询APP已拥有授权的API
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchBindApi
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchBindApiRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchBindApiResponse`
        """
        http_info = self._search_bind_api_http_info(request)
        return self._call_api(**http_info)

    def search_bind_api_invoker(self, request):
        http_info = self._search_bind_api_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_bind_api_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/authorize/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "SearchBindApiResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def search_catalogs(self, request):
        """查询流程架构列表

        查询流程架构列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchCatalogs
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchCatalogsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchCatalogsResponse`
        """
        http_info = self._search_catalogs_http_info(request)
        return self._call_api(**http_info)

    def search_catalogs_invoker(self, request):
        http_info = self._search_catalogs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_catalogs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/biz/catalogs",
            "request_type": request.__class__.__name__,
            "response_type": "SearchCatalogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'create_by' in local_var_params:
            query_params.append(('create_by', local_var_params['create_by']))
        if 'owner' in local_var_params:
            query_params.append(('owner', local_var_params['owner']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def search_code_table_values(self, request):
        """查看码表字段值

        查看码表字段值
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchCodeTableValues
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchCodeTableValuesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchCodeTableValuesResponse`
        """
        http_info = self._search_code_table_values_http_info(request)
        return self._call_api(**http_info)

    def search_code_table_values_invoker(self, request):
        http_info = self._search_code_table_values_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_code_table_values_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/code-tables/{id}/values",
            "request_type": request.__class__.__name__,
            "response_type": "SearchCodeTableValuesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def search_code_tables(self, request):
        """查询码表列表

        查询码表列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchCodeTables
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchCodeTablesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchCodeTablesResponse`
        """
        http_info = self._search_code_tables_http_info(request)
        return self._call_api(**http_info)

    def search_code_tables_invoker(self, request):
        http_info = self._search_code_tables_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_code_tables_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/code-tables",
            "request_type": request.__class__.__name__,
            "response_type": "SearchCodeTablesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'create_by' in local_var_params:
            query_params.append(('create_by', local_var_params['create_by']))
        if 'approver' in local_var_params:
            query_params.append(('approver', local_var_params['approver']))
        if 'directory_id' in local_var_params:
            query_params.append(('directory_id', local_var_params['directory_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def search_customized_fields(self, request):
        """查询自定义项

        查询自定义项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchCustomizedFields
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchCustomizedFieldsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchCustomizedFieldsResponse`
        """
        http_info = self._search_customized_fields_http_info(request)
        return self._call_api(**http_info)

    def search_customized_fields_invoker(self, request):
        http_info = self._search_customized_fields_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_customized_fields_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/customized-fields",
            "request_type": request.__class__.__name__,
            "response_type": "SearchCustomizedFieldsResponse"
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
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def search_dw_by_type(self, request):
        """获取数据连接信息

        获取指定类型下的数据连接信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchDwByType
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchDwByTypeRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchDwByTypeResponse`
        """
        http_info = self._search_dw_by_type_http_info(request)
        return self._call_api(**http_info)

    def search_dw_by_type_invoker(self, request):
        http_info = self._search_dw_by_type_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_dw_by_type_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/atlas/data-warehouses",
            "request_type": request.__class__.__name__,
            "response_type": "SearchDwByTypeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'force_refresh' in local_var_params:
            query_params.append(('force_refresh', local_var_params['force_refresh']))
        if 'dw_type' in local_var_params:
            query_params.append(('dw_type', local_var_params['dw_type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def search_id_by_path(self, request):
        """通过路径获取id

        通过路径获取id
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchIdByPath
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchIdByPathRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchIdByPathResponse`
        """
        http_info = self._search_id_by_path_http_info(request)
        return self._call_api(**http_info)

    def search_id_by_path_invoker(self, request):
        http_info = self._search_id_by_path_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_id_by_path_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/servicecatalogs/ids",
            "request_type": request.__class__.__name__,
            "response_type": "SearchIdByPathResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def search_subject(self, request):
        """查找主题列表

        通过名称、创建者、责任人、状态、修改时间分页查找主题
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchSubject
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchSubjectRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchSubjectResponse`
        """
        http_info = self._search_subject_http_info(request)
        return self._call_api(**http_info)

    def search_subject_invoker(self, request):
        http_info = self._search_subject_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_subject_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/subjects",
            "request_type": request.__class__.__name__,
            "response_type": "SearchSubjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'create_by' in local_var_params:
            query_params.append(('create_by', local_var_params['create_by']))
        if 'owner' in local_var_params:
            query_params.append(('owner', local_var_params['owner']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'parent_id' in local_var_params:
            query_params.append(('parent_id', local_var_params['parent_id']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def search_subject_new(self, request):
        """查找主题列表(新)

        查找主题(新)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchSubjectNew
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchSubjectNewRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchSubjectNewResponse`
        """
        http_info = self._search_subject_new_http_info(request)
        return self._call_api(**http_info)

    def search_subject_new_invoker(self, request):
        http_info = self._search_subject_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_subject_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/design/subjects",
            "request_type": request.__class__.__name__,
            "response_type": "SearchSubjectNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'create_by' in local_var_params:
            query_params.append(('create_by', local_var_params['create_by']))
        if 'owner' in local_var_params:
            query_params.append(('owner', local_var_params['owner']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'parent_id' in local_var_params:
            query_params.append(('parent_id', local_var_params['parent_id']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def search_versions(self, request):
        """查找版本信息

        通过名称、创建者、修改时间查找版本信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchVersions
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchVersionsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchVersionsResponse`
        """
        http_info = self._search_versions_http_info(request)
        return self._call_api(**http_info)

    def search_versions_invoker(self, request):
        http_info = self._search_versions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_versions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/versions",
            "request_type": request.__class__.__name__,
            "response_type": "SearchVersionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'create_by' in local_var_params:
            query_params.append(('create_by', local_var_params['create_by']))
        if 'biz_id' in local_var_params:
            query_params.append(('biz_id', local_var_params['biz_id']))
        if 'biz_type' in local_var_params:
            query_params.append(('biz_type', local_var_params['biz_type']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_aggregation_logic_table_by_id(self, request):
        """查看汇总表详情

        通过id查看汇总表的详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAggregationLogicTableById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowAggregationLogicTableByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowAggregationLogicTableByIdResponse`
        """
        http_info = self._show_aggregation_logic_table_by_id_http_info(request)
        return self._call_api(**http_info)

    def show_aggregation_logic_table_by_id_invoker(self, request):
        http_info = self._show_aggregation_logic_table_by_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_aggregation_logic_table_by_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/aggregation-logic-tables/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAggregationLogicTableByIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'latest' in local_var_params:
            query_params.append(('latest', local_var_params['latest']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_api_dashboard(self, request):
        """查询指定api 仪表板数据详情

        查询指定api 仪表板数据详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApiDashboard
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowApiDashboardRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowApiDashboardResponse`
        """
        http_info = self._show_api_dashboard_http_info(request)
        return self._call_api(**http_info)

    def show_api_dashboard_invoker(self, request):
        http_info = self._show_api_dashboard_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_api_dashboard_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/statistic/apis-dashboards/{api_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApiDashboardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'time_unit' in local_var_params:
            query_params.append(('time_unit', local_var_params['time_unit']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_apis_dashboard(self, request):
        """查询api 仪表板数据详情

        查询api 仪表板数据详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApisDashboard
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowApisDashboardRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowApisDashboardResponse`
        """
        http_info = self._show_apis_dashboard_http_info(request)
        return self._call_api(**http_info)

    def show_apis_dashboard_invoker(self, request):
        http_info = self._show_apis_dashboard_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_apis_dashboard_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/statistic/apis-dashboards",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApisDashboardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'time_unit' in local_var_params:
            query_params.append(('time_unit', local_var_params['time_unit']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_apis_detail(self, request):
        """查询api 统计数据详情

        查询api 统计数据详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApisDetail
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowApisDetailRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowApisDetailResponse`
        """
        http_info = self._show_apis_detail_http_info(request)
        return self._call_api(**http_info)

    def show_apis_detail_invoker(self, request):
        http_info = self._show_apis_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_apis_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/statistic/apis-detail/{api_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApisDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'time_unit' in local_var_params:
            query_params.append(('time_unit', local_var_params['time_unit']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_apis_overview(self, request):
        """查询统计用户相关的总览开发指标

        查询统计用户相关的总览开发指标
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApisOverview
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowApisOverviewRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowApisOverviewResponse`
        """
        http_info = self._show_apis_overview_http_info(request)
        return self._call_api(**http_info)

    def show_apis_overview_invoker(self, request):
        http_info = self._show_apis_overview_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_apis_overview_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/statistic/apis-overview",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApisOverviewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'time_unit' in local_var_params:
            query_params.append(('time_unit', local_var_params['time_unit']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_app_info(self, request):
        """查询应用详情

        查询应用详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAppInfo
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowAppInfoRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowAppInfoResponse`
        """
        http_info = self._show_app_info_http_info(request)
        return self._call_api(**http_info)

    def show_app_info_invoker(self, request):
        http_info = self._show_app_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_app_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_apply_detail(self, request):
        """获取申请详情

        获取申请详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApplyDetail
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowApplyDetailRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowApplyDetailResponse`
        """
        http_info = self._show_apply_detail_http_info(request)
        return self._call_api(**http_info)

    def show_apply_detail_invoker(self, request):
        http_info = self._show_apply_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_apply_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/applys/{apply_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApplyDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'apply_id' in local_var_params:
            path_params['apply_id'] = local_var_params['apply_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_apps_dashboard(self, request):
        """查询app 仪表板数据详情

        查询app 仪表板数据详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAppsDashboard
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowAppsDashboardRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowAppsDashboardResponse`
        """
        http_info = self._show_apps_dashboard_http_info(request)
        return self._call_api(**http_info)

    def show_apps_dashboard_invoker(self, request):
        http_info = self._show_apps_dashboard_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_apps_dashboard_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/statistic/apps-dashboards",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppsDashboardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'time_unit' in local_var_params:
            query_params.append(('time_unit', local_var_params['time_unit']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_apps_detail(self, request):
        """查询app 统计数据详情

        查询app 统计数据详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAppsDetail
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowAppsDetailRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowAppsDetailResponse`
        """
        http_info = self._show_apps_detail_http_info(request)
        return self._call_api(**http_info)

    def show_apps_detail_invoker(self, request):
        http_info = self._show_apps_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_apps_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/statistic/apps-detail/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppsDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'time_unit' in local_var_params:
            query_params.append(('time_unit', local_var_params['time_unit']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_apps_overview(self, request):
        """查询统计用户相关的总览调用指标

        查询统计用户相关的总览调用指标
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAppsOverview
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowAppsOverviewRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowAppsOverviewResponse`
        """
        http_info = self._show_apps_overview_http_info(request)
        return self._call_api(**http_info)

    def show_apps_overview_invoker(self, request):
        http_info = self._show_apps_overview_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_apps_overview_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/statistic/apps-overview",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppsOverviewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'time_unit' in local_var_params:
            query_params.append(('time_unit', local_var_params['time_unit']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_atomic_index_by_id(self, request):
        """查看原子指标详情

        通过id获取指标详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAtomicIndexById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowAtomicIndexByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowAtomicIndexByIdResponse`
        """
        http_info = self._show_atomic_index_by_id_http_info(request)
        return self._call_api(**http_info)

    def show_atomic_index_by_id_invoker(self, request):
        http_info = self._show_atomic_index_by_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_atomic_index_by_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/atomic-indexs/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAtomicIndexByIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'latest' in local_var_params:
            query_params.append(('latest', local_var_params['latest']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_biz_catalog_detail(self, request):
        """查找流程架构详情

        查找流程架构详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBizCatalogDetail
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowBizCatalogDetailRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowBizCatalogDetailResponse`
        """
        http_info = self._show_biz_catalog_detail_http_info(request)
        return self._call_api(**http_info)

    def show_biz_catalog_detail_invoker(self, request):
        http_info = self._show_biz_catalog_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_biz_catalog_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/biz/catalogs/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBizCatalogDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_biz_metric_by_id(self, request):
        """查看指标详情

        通过id查看指标的详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBizMetricById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowBizMetricByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowBizMetricByIdResponse`
        """
        http_info = self._show_biz_metric_by_id_http_info(request)
        return self._call_api(**http_info)

    def show_biz_metric_by_id_invoker(self, request):
        http_info = self._show_biz_metric_by_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_biz_metric_by_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/biz-metrics/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBizMetricByIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'latest' in local_var_params:
            query_params.append(('latest', local_var_params['latest']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_business_assets(self, request):
        """查询业务资产

        业务资产查询接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBusinessAssets
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowBusinessAssetsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowBusinessAssetsResponse`
        """
        http_info = self._show_business_assets_http_info(request)
        return self._call_api(**http_info)

    def show_business_assets_invoker(self, request):
        http_info = self._show_business_assets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_business_assets_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/asset/business-assets/search",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBusinessAssetsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def show_business_assets_statistic(self, request):
        """获取业务资产统计信息

        获取业务资产统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBusinessAssetsStatistic
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowBusinessAssetsStatisticRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowBusinessAssetsStatisticResponse`
        """
        http_info = self._show_business_assets_statistic_http_info(request)
        return self._call_api(**http_info)

    def show_business_assets_statistic_invoker(self, request):
        http_info = self._show_business_assets_statistic_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_business_assets_statistic_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/asset/statistic/assets/business-assets",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBusinessAssetsStatisticResponse"
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
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_catalog_detail(self, request):
        """查询服务目录

        查询服务目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCatalogDetail
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowCatalogDetailRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowCatalogDetailResponse`
        """
        http_info = self._show_catalog_detail_http_info(request)
        return self._call_api(**http_info)

    def show_catalog_detail_invoker(self, request):
        http_info = self._show_catalog_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_catalog_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/servicecatalogs/{catalog_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCatalogDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'catalog_id' in local_var_params:
            path_params['catalog_id'] = local_var_params['catalog_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_code_table_by_id(self, request):
        """查看码表详情

        通过id查看码表的详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCodeTableById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowCodeTableByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowCodeTableByIdResponse`
        """
        http_info = self._show_code_table_by_id_http_info(request)
        return self._call_api(**http_info)

    def show_code_table_by_id_invoker(self, request):
        http_info = self._show_code_table_by_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_code_table_by_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/code-tables/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCodeTableByIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_compound_metric_by_id(self, request):
        """查看复合指标详情

        通过id获取复合指标详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCompoundMetricById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowCompoundMetricByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowCompoundMetricByIdResponse`
        """
        http_info = self._show_compound_metric_by_id_http_info(request)
        return self._call_api(**http_info)

    def show_compound_metric_by_id_invoker(self, request):
        http_info = self._show_compound_metric_by_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_compound_metric_by_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/compound-metrics/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCompoundMetricByIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'latest' in local_var_params:
            query_params.append(('latest', local_var_params['latest']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_condition_by_id(self, request):
        """查看限定详情

        通过id查看限定详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowConditionById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowConditionByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowConditionByIdResponse`
        """
        http_info = self._show_condition_by_id_http_info(request)
        return self._call_api(**http_info)

    def show_condition_by_id_invoker(self, request):
        http_info = self._show_condition_by_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_condition_by_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/conditions/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConditionByIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'latest' in local_var_params:
            query_params.append(('latest', local_var_params['latest']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_consistency_task_detail(self, request):
        """获取对账作业详情

        获取对账作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowConsistencyTaskDetail
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowConsistencyTaskDetailRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowConsistencyTaskDetailResponse`
        """
        http_info = self._show_consistency_task_detail_http_info(request)
        return self._call_api(**http_info)

    def show_consistency_task_detail_invoker(self, request):
        http_info = self._show_consistency_task_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_consistency_task_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/quality/consistency-tasks/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConsistencyTaskDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_data_profile(self, request):
        """资产信息

        查询概要
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDataProfile
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowDataProfileRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowDataProfileResponse`
        """
        http_info = self._show_data_profile_http_info(request)
        return self._call_api(**http_info)

    def show_data_profile_invoker(self, request):
        http_info = self._show_data_profile_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_data_profile_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/asset/profile",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDataProfileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'dw_id' in local_var_params:
            query_params.append(('dw_id', local_var_params['dw_id']))
        if 'db_type' in local_var_params:
            query_params.append(('db_type', local_var_params['db_type']))
        if 'database_name' in local_var_params:
            query_params.append(('database_name', local_var_params['database_name']))
        if 'table_name' in local_var_params:
            query_params.append(('table_name', local_var_params['table_name']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_data_sets(self, request):
        """资产搜索

        资产搜索
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDataSets
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowDataSetsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowDataSetsResponse`
        """
        http_info = self._show_data_sets_http_info(request)
        return self._call_api(**http_info)

    def show_data_sets_invoker(self, request):
        http_info = self._show_data_sets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_data_sets_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/datamap/entities/search",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDataSetsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance' in local_var_params:
            header_params['instance'] = local_var_params['instance']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_dataconnection(self, request):
        """查询单个数据连接信息

        查询单个数据连接信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDataconnection
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowDataconnectionRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowDataconnectionResponse`
        """
        http_info = self._show_dataconnection_http_info(request)
        return self._call_api(**http_info)

    def show_dataconnection_invoker(self, request):
        http_info = self._show_dataconnection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_dataconnection_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/data-connections/{data_connection_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDataconnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'data_connection_id' in local_var_params:
            path_params['data_connection_id'] = local_var_params['data_connection_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_derivative_index_by_id(self, request):
        """查看衍生指标详情

        通过id获取衍生详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDerivativeIndexById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowDerivativeIndexByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowDerivativeIndexByIdResponse`
        """
        http_info = self._show_derivative_index_by_id_http_info(request)
        return self._call_api(**http_info)

    def show_derivative_index_by_id_invoker(self, request):
        http_info = self._show_derivative_index_by_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_derivative_index_by_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/derivative-indexs/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDerivativeIndexByIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'latest' in local_var_params:
            query_params.append(('latest', local_var_params['latest']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_dimension_by_id(self, request):
        """查看维度详情

        通过id查看维度详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDimensionById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowDimensionByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowDimensionByIdResponse`
        """
        http_info = self._show_dimension_by_id_http_info(request)
        return self._call_api(**http_info)

    def show_dimension_by_id_invoker(self, request):
        http_info = self._show_dimension_by_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_dimension_by_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/dimensions/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDimensionByIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'latest' in local_var_params:
            query_params.append(('latest', local_var_params['latest']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_dimension_logic_table_by_id(self, request):
        """查看维度表详情

        通过id查看维度表的详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDimensionLogicTableById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowDimensionLogicTableByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowDimensionLogicTableByIdResponse`
        """
        http_info = self._show_dimension_logic_table_by_id_http_info(request)
        return self._call_api(**http_info)

    def show_dimension_logic_table_by_id_invoker(self, request):
        http_info = self._show_dimension_logic_table_by_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_dimension_logic_table_by_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/dimension-logic-tables/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDimensionLogicTableByIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'latest' in local_var_params:
            query_params.append(('latest', local_var_params['latest']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_entities(self, request):
        """查询技术资产

        查询技术资产
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEntities
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowEntitiesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowEntitiesResponse`
        """
        http_info = self._show_entities_http_info(request)
        return self._call_api(**http_info)

    def show_entities_invoker(self, request):
        http_info = self._show_entities_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_entities_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/asset/entities/search",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEntitiesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_entity_info_by_guid(self, request):
        """根据guid获取资产详情

        根据表guid可以获取表的详情信息，表的详情信息包含column的信息，也可以根据column的guid直接获取column的信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEntityInfoByGuid
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowEntityInfoByGuidRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowEntityInfoByGuidResponse`
        """
        http_info = self._show_entity_info_by_guid_http_info(request)
        return self._call_api(**http_info)

    def show_entity_info_by_guid_invoker(self, request):
        http_info = self._show_entity_info_by_guid_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_entity_info_by_guid_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/asset/entities/{guid}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEntityInfoByGuidResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'guid' in local_var_params:
            path_params['guid'] = local_var_params['guid']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_fact_logic_table_by_id(self, request):
        """查看事实表详情

        通过id查看事实表的详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFactLogicTableById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowFactLogicTableByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowFactLogicTableByIdResponse`
        """
        http_info = self._show_fact_logic_table_by_id_http_info(request)
        return self._call_api(**http_info)

    def show_fact_logic_table_by_id_invoker(self, request):
        http_info = self._show_fact_logic_table_by_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_fact_logic_table_by_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/fact-logic-tables/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFactLogicTableByIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'latest' in local_var_params:
            query_params.append(('latest', local_var_params['latest']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_factory_env(self, request):
        """查询环境变量信息

        查询环境变量信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFactoryEnv
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowFactoryEnvRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowFactoryEnvResponse`
        """
        http_info = self._show_factory_env_http_info(request)
        return self._call_api(**http_info)

    def show_factory_env_invoker(self, request):
        http_info = self._show_factory_env_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_factory_env_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/factory/env",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFactoryEnvResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_factory_supplement_data(self, request):
        """查询所有的补数据实例

        查询所有的补数据实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFactorySupplementData
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowFactorySupplementDataRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowFactorySupplementDataResponse`
        """
        http_info = self._show_factory_supplement_data_http_info(request)
        return self._call_api(**http_info)

    def show_factory_supplement_data_invoker(self, request):
        http_info = self._show_factory_supplement_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_factory_supplement_data_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/factory/supplement-data",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFactorySupplementDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_date' in local_var_params:
            query_params.append(('start_date', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('end_date', local_var_params['end_date']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def show_glossary_list(self, request):
        """查询标签列表

        查询标签列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGlossaryList
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowGlossaryListRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowGlossaryListResponse`
        """
        http_info = self._show_glossary_list_http_info(request)
        return self._call_api(**http_info)

    def show_glossary_list_invoker(self, request):
        http_info = self._show_glossary_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_glossary_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGlossaryListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'create_user' in local_var_params:
            query_params.append(('create_user', local_var_params['create_user']))
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))
        if 'end' in local_var_params:
            query_params.append(('end', local_var_params['end']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_by' in local_var_params:
            query_params.append(('sort_by', local_var_params['sort_by']))
        if 'sort_order' in local_var_params:
            query_params.append(('sort_order', local_var_params['sort_order']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_instance_log(self, request):
        """获取任务日志

        获取任务日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceLog
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowInstanceLogRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowInstanceLogResponse`
        """
        http_info = self._show_instance_log_http_info(request)
        return self._call_api(**http_info)

    def show_instance_log_invoker(self, request):
        http_info = self._show_instance_log_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_log_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/metadata/tasks/{task_id}/{instance_id}/log",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def show_instance_result(self, request):
        """获取实例结果

        获取实例结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceResult
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowInstanceResultRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowInstanceResultResponse`
        """
        http_info = self._show_instance_result_http_info(request)
        return self._call_api(**http_info)

    def show_instance_result_invoker(self, request):
        http_info = self._show_instance_result_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_result_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/quality/instances/{instance_id}/result",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_message_detail(self, request):
        """获取消息详情

        获取消息详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMessageDetail
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowMessageDetailRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowMessageDetailResponse`
        """
        http_info = self._show_message_detail_http_info(request)
        return self._call_api(**http_info)

    def show_message_detail_invoker(self, request):
        http_info = self._show_message_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_message_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/messages/{message_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMessageDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'message_id' in local_var_params:
            path_params['message_id'] = local_var_params['message_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_metric_assets(self, request):
        """查询指标资产

        指标资产查询接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMetricAssets
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowMetricAssetsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowMetricAssetsResponse`
        """
        http_info = self._show_metric_assets_http_info(request)
        return self._call_api(**http_info)

    def show_metric_assets_invoker(self, request):
        http_info = self._show_metric_assets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_metric_assets_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/asset/metric-assets/search",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMetricAssetsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def show_metric_tree(self, request):
        """查询指标资产目录树

        查询指标资产目录树
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMetricTree
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowMetricTreeRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowMetricTreeResponse`
        """
        http_info = self._show_metric_tree_http_info(request)
        return self._call_api(**http_info)

    def show_metric_tree_invoker(self, request):
        http_info = self._show_metric_tree_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_metric_tree_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/asset/metric-tree",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMetricTreeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_path_by_id(self, request):
        """通过id获取路径

        通过id获取路径
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPathById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowPathByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowPathByIdResponse`
        """
        http_info = self._show_path_by_id_http_info(request)
        return self._call_api(**http_info)

    def show_path_by_id_invoker(self, request):
        http_info = self._show_path_by_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_path_by_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/servicecatalogs/{catalog_id}/paths",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPathByIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'catalog_id' in local_var_params:
            path_params['catalog_id'] = local_var_params['catalog_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_path_object_by_id(self, request):
        """通过id获取路径对象

        通过id获取路径对象
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPathObjectById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowPathObjectByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowPathObjectByIdResponse`
        """
        http_info = self._show_path_object_by_id_http_info(request)
        return self._call_api(**http_info)

    def show_path_object_by_id_invoker(self, request):
        http_info = self._show_path_object_by_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_path_object_by_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/servicecatalogs/{catalog_id}/layerpaths",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPathObjectByIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'catalog_id' in local_var_params:
            path_params['catalog_id'] = local_var_params['catalog_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_quality_task_detail(self, request):
        """获取质量作业详情

        获取质量作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowQualityTaskDetail
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowQualityTaskDetailRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowQualityTaskDetailResponse`
        """
        http_info = self._show_quality_task_detail_http_info(request)
        return self._call_api(**http_info)

    def show_quality_task_detail_invoker(self, request):
        http_info = self._show_quality_task_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_quality_task_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/quality/quality-tasks/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowQualityTaskDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_relation_by_id(self, request):
        """查看关系详情

        通过id获取关系详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRelationById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowRelationByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowRelationByIdResponse`
        """
        http_info = self._show_relation_by_id_http_info(request)
        return self._call_api(**http_info)

    def show_relation_by_id_invoker(self, request):
        http_info = self._show_relation_by_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_relation_by_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/relation/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRelationByIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'latest' in local_var_params:
            query_params.append(('latest', local_var_params['latest']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_standard_by_id(self, request):
        """查看数据标准详情

        通过id获取数据标准详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowStandardById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowStandardByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowStandardByIdResponse`
        """
        http_info = self._show_standard_by_id_http_info(request)
        return self._call_api(**http_info)

    def show_standard_by_id_invoker(self, request):
        http_info = self._show_standard_by_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_standard_by_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/standards/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowStandardByIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_standard_template(self, request):
        """查询数据标准模板

        查询数据标准模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowStandardTemplate
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowStandardTemplateRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowStandardTemplateResponse`
        """
        http_info = self._show_standard_template_http_info(request)
        return self._call_api(**http_info)

    def show_standard_template_invoker(self, request):
        http_info = self._show_standard_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_standard_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/standards/templates",
            "request_type": request.__class__.__name__,
            "response_type": "ShowStandardTemplateResponse"
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
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_table_model_by_id(self, request):
        """查看表模型详情

        通过id获取模型表详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTableModelById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowTableModelByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowTableModelByIdResponse`
        """
        http_info = self._show_table_model_by_id_http_info(request)
        return self._call_api(**http_info)

    def show_table_model_by_id_invoker(self, request):
        http_info = self._show_table_model_by_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_table_model_by_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/table-model/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTableModelByIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'latest' in local_var_params:
            query_params.append(('latest', local_var_params['latest']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_tags(self, request):
        """搜索查询标签分页展示

        搜索查询标签分页展示
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTags
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowTagsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowTagsResponse`
        """
        http_info = self._show_tags_http_info(request)
        return self._call_api(**http_info)

    def show_tags_invoker(self, request):
        http_info = self._show_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/datamap/tags/search",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance' in local_var_params:
            header_params['instance'] = local_var_params['instance']

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

    def show_task_info(self, request):
        """查询采集任务详情

        查询采集任务详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTaskInfo
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowTaskInfoRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowTaskInfoResponse`
        """
        http_info = self._show_task_info_http_info(request)
        return self._call_api(**http_info)

    def show_task_info_invoker(self, request):
        http_info = self._show_task_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_task_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/metadata/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTaskInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_task_list(self, request):
        """查询采集任务列表

        查询采集任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTaskList
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowTaskListRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowTaskListResponse`
        """
        http_info = self._show_task_list_http_info(request)
        return self._call_api(**http_info)

    def show_task_list_invoker(self, request):
        http_info = self._show_task_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_task_list_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/metadata/tasks/search",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTaskListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def show_technical_assets_statistic(self, request):
        """获取技术资产统计信息

        获取技术资产统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTechnicalAssetsStatistic
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowTechnicalAssetsStatisticRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowTechnicalAssetsStatisticResponse`
        """
        http_info = self._show_technical_assets_statistic_http_info(request)
        return self._call_api(**http_info)

    def show_technical_assets_statistic_invoker(self, request):
        http_info = self._show_technical_assets_statistic_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_technical_assets_statistic_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/asset/statistic/assets/technical-assets",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTechnicalAssetsStatisticResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_templates_detail(self, request):
        """获取规则模板详情

        获取规则模板详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTemplatesDetail
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowTemplatesDetailRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowTemplatesDetailResponse`
        """
        http_info = self._show_templates_detail_http_info(request)
        return self._call_api(**http_info)

    def show_templates_detail_invoker(self, request):
        http_info = self._show_templates_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_templates_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/quality/rule-templates/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTemplatesDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_unrelated_table(self, request):
        """无血缘关系表查询

        无血缘关系表查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUnrelatedTable
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowUnrelatedTableRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowUnrelatedTableResponse`
        """
        http_info = self._show_unrelated_table_http_info(request)
        return self._call_api(**http_info)

    def show_unrelated_table_invoker(self, request):
        http_info = self._show_unrelated_table_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_unrelated_table_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/lineage/search/unrelated/table",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUnrelatedTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def show_work_space(self, request):
        """获取单个工作空间信息

        获取单个工作空间信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowWorkSpace
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowWorkSpaceRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowWorkSpaceResponse`
        """
        http_info = self._show_work_space_http_info(request)
        return self._call_api(**http_info)

    def show_work_space_invoker(self, request):
        http_info = self._show_work_space_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_work_space_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{instance_id}/{workspace_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWorkSpaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_workspace_detail_by_id(self, request):
        """查询模型详情

        查询物理模型或逻辑模型的工作区空间详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowWorkspaceDetailById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowWorkspaceDetailByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowWorkspaceDetailByIdResponse`
        """
        http_info = self._show_workspace_detail_by_id_http_info(request)
        return self._call_api(**http_info)

    def show_workspace_detail_by_id_invoker(self, request):
        http_info = self._show_workspace_detail_by_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_workspace_detail_by_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/design/workspaces/{model_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWorkspaceDetailByIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'model_id' in local_var_params:
            path_params['model_id'] = local_var_params['model_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def stop_factory_supplement_data_instance(self, request):
        """停止一个补数据实例

        停止一个补数据实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopFactorySupplementDataInstance
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.StopFactorySupplementDataInstanceRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.StopFactorySupplementDataInstanceResponse`
        """
        http_info = self._stop_factory_supplement_data_instance_http_info(request)
        return self._call_api(**http_info)

    def stop_factory_supplement_data_instance_invoker(self, request):
        http_info = self._stop_factory_supplement_data_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_factory_supplement_data_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/factory/supplement-data/{instance_name}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopFactorySupplementDataInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_name' in local_var_params:
            path_params['instance_name'] = local_var_params['instance_name']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def update_app(self, request):
        """更新应用

        更新应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateApp
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateAppRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateAppResponse`
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
            "resource_path": "/v1/{project_id}/service/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

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

    def update_biz_metric(self, request):
        """更新业务指标

        更新业务指标
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateBizMetric
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateBizMetricRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateBizMetricResponse`
        """
        http_info = self._update_biz_metric_http_info(request)
        return self._call_api(**http_info)

    def update_biz_metric_invoker(self, request):
        http_info = self._update_biz_metric_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_biz_metric_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/design/biz-metrics",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateBizMetricResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def update_catalog(self, request):
        """更新服务目录

        更新服务目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCatalog
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateCatalogRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateCatalogResponse`
        """
        http_info = self._update_catalog_http_info(request)
        return self._call_api(**http_info)

    def update_catalog_invoker(self, request):
        http_info = self._update_catalog_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_catalog_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/service/servicecatalogs/{catalog_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCatalogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'catalog_id' in local_var_params:
            path_params['catalog_id'] = local_var_params['catalog_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

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

    def update_code_table(self, request):
        """修改码表

        修改码表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCodeTable
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateCodeTableRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateCodeTableResponse`
        """
        http_info = self._update_code_table_http_info(request)
        return self._call_api(**http_info)

    def update_code_table_invoker(self, request):
        http_info = self._update_code_table_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_code_table_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/design/code-tables/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCodeTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def update_code_table_values(self, request):
        """编辑码表字段值

        编辑码表字段值
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCodeTableValues
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateCodeTableValuesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateCodeTableValuesResponse`
        """
        http_info = self._update_code_table_values_http_info(request)
        return self._call_api(**http_info)

    def update_code_table_values_invoker(self, request):
        http_info = self._update_code_table_values_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_code_table_values_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/design/code-tables/{id}/values",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCodeTableValuesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def update_dataconnection(self, request):
        """更新数据连接信息

        更新数据连接信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDataconnection
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateDataconnectionRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateDataconnectionResponse`
        """
        http_info = self._update_dataconnection_http_info(request)
        return self._call_api(**http_info)

    def update_dataconnection_invoker(self, request):
        http_info = self._update_dataconnection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_dataconnection_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/data-connections/{data_connection_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDataconnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'data_connection_id' in local_var_params:
            path_params['data_connection_id'] = local_var_params['data_connection_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_directory(self, request):
        """修改目录

        修改目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDirectory
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateDirectoryRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateDirectoryResponse`
        """
        http_info = self._update_directory_http_info(request)
        return self._call_api(**http_info)

    def update_directory_invoker(self, request):
        http_info = self._update_directory_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_directory_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/design/directorys",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDirectoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def update_factory_job_name(self, request):
        """修改作业名称

        修改作业名称
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateFactoryJobName
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateFactoryJobNameRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateFactoryJobNameResponse`
        """
        http_info = self._update_factory_job_name_http_info(request)
        return self._call_api(**http_info)

    def update_factory_job_name_invoker(self, request):
        http_info = self._update_factory_job_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_factory_job_name_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/factory/jobs/{job_name}/rename",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateFactoryJobNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_name' in local_var_params:
            path_params['job_name'] = local_var_params['job_name']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'host' in local_var_params:
            header_params['Host'] = local_var_params['host']

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

    def update_standard(self, request):
        """修改数据标准

        修改数据标准
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateStandard
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateStandardRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateStandardResponse`
        """
        http_info = self._update_standard_http_info(request)
        return self._call_api(**http_info)

    def update_standard_invoker(self, request):
        http_info = self._update_standard_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_standard_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/design/standards/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateStandardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def update_standard_template(self, request):
        """修改数据标准模板

        修改数据标准模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateStandardTemplate
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateStandardTemplateRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateStandardTemplateResponse`
        """
        http_info = self._update_standard_template_http_info(request)
        return self._call_api(**http_info)

    def update_standard_template_invoker(self, request):
        http_info = self._update_standard_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_standard_template_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/design/standards/templates",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateStandardTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def update_subject(self, request):
        """修改主题

        修改主题
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSubject
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateSubjectRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateSubjectResponse`
        """
        http_info = self._update_subject_http_info(request)
        return self._call_api(**http_info)

    def update_subject_invoker(self, request):
        http_info = self._update_subject_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_subject_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/design/subjects",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSubjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def update_subject_new(self, request):
        """修改主题(新)

        修改主题(新)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSubjectNew
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateSubjectNewRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateSubjectNewResponse`
        """
        http_info = self._update_subject_new_http_info(request)
        return self._call_api(**http_info)

    def update_subject_new_invoker(self, request):
        http_info = self._update_subject_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_subject_new_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/design/subjects",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSubjectNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def update_table_model(self, request):
        """更新模型实体

        更新一个模型实体，包括逻辑实体或物理数据表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTableModel
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateTableModelRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateTableModelResponse`
        """
        http_info = self._update_table_model_http_info(request)
        return self._call_api(**http_info)

    def update_table_model_invoker(self, request):
        http_info = self._update_table_model_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_table_model_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/design/table-model",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTableModelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def update_task_info(self, request):
        """编辑采集任务

        编辑采集任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTaskInfo
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateTaskInfoRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateTaskInfoResponse`
        """
        http_info = self._update_task_info_http_info(request)
        return self._call_api(**http_info)

    def update_task_info_invoker(self, request):
        http_info = self._update_task_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_task_info_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/metadata/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTaskInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def update_template(self, request):
        """更新规则模板

        更新规则模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTemplate
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateTemplateRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateTemplateResponse`
        """
        http_info = self._update_template_http_info(request)
        return self._call_api(**http_info)

    def update_template_invoker(self, request):
        http_info = self._update_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_template_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/quality/rule-templates/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def update_work_space_user_or_group(self, request):
        """编辑工作空间用户或用户组

        编辑工作空间用户或用户组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateWorkSpaceUserOrGroup
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateWorkSpaceUserOrGroupRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateWorkSpaceUserOrGroupResponse`
        """
        http_info = self._update_work_space_user_or_group_http_info(request)
        return self._call_api(**http_info)

    def update_work_space_user_or_group_invoker(self, request):
        http_info = self._update_work_space_user_or_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_work_space_user_or_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/{workspace_id}/users/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateWorkSpaceUserOrGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
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

    def update_workspace(self, request):
        """更新模型工作区

        更新模型工作区
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateWorkspace
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateWorkspaceRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateWorkspaceResponse`
        """
        http_info = self._update_workspace_http_info(request)
        return self._call_api(**http_info)

    def update_workspace_invoker(self, request):
        http_info = self._update_workspace_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_workspace_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/design/workspaces",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateWorkspaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def authorize_action_api_to_instance(self, request):
        """API授权操作(授权/取消授权/申请/续约)

        API授权操作(授权/取消授权/申请/续约)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AuthorizeActionApiToInstance
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.AuthorizeActionApiToInstanceRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.AuthorizeActionApiToInstanceResponse`
        """
        http_info = self._authorize_action_api_to_instance_http_info(request)
        return self._call_api(**http_info)

    def authorize_action_api_to_instance_invoker(self, request):
        http_info = self._authorize_action_api_to_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _authorize_action_api_to_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/service/apis/authorize/action",
            "request_type": request.__class__.__name__,
            "response_type": "AuthorizeActionApiToInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

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

    def authorize_api_to_instance(self, request):
        """批量授权API

        批量授权API
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AuthorizeApiToInstance
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.AuthorizeApiToInstanceRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.AuthorizeApiToInstanceResponse`
        """
        http_info = self._authorize_api_to_instance_http_info(request)
        return self._call_api(**http_info)

    def authorize_api_to_instance_invoker(self, request):
        http_info = self._authorize_api_to_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _authorize_api_to_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/service/apis/{api_id}/instances/{instance_id}/authorize",
            "request_type": request.__class__.__name__,
            "response_type": "AuthorizeApiToInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

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

    def create_api(self, request):
        """创建API

        创建API
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateApi
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateApiRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateApiResponse`
        """
        http_info = self._create_api_http_info(request)
        return self._call_api(**http_info)

    def create_api_invoker(self, request):
        http_info = self._create_api_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_api_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/service/apis",
            "request_type": request.__class__.__name__,
            "response_type": "CreateApiResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

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

    def debug_api(self, request):
        """调试API

        调试API
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DebugApi
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DebugApiRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DebugApiResponse`
        """
        http_info = self._debug_api_http_info(request)
        return self._call_api(**http_info)

    def debug_api_invoker(self, request):
        http_info = self._debug_api_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _debug_api_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/service/apis/{api_id}/instances/{instance_id}/test",
            "request_type": request.__class__.__name__,
            "response_type": "DebugApiResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

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

    def delete_api(self, request):
        """批量删除API

        批量删除API
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApi
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteApiRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteApiResponse`
        """
        http_info = self._delete_api_http_info(request)
        return self._call_api(**http_info)

    def delete_api_invoker(self, request):
        http_info = self._delete_api_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_api_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/service/apis/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteApiResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

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

    def execute_api_to_instance(self, request):
        """API操作(下线/停用/恢复)

        API操作(下线/停用/恢复)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteApiToInstance
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ExecuteApiToInstanceRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ExecuteApiToInstanceResponse`
        """
        http_info = self._execute_api_to_instance_http_info(request)
        return self._call_api(**http_info)

    def execute_api_to_instance_invoker(self, request):
        http_info = self._execute_api_to_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_api_to_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/service/apis/{api_id}/instances/{instance_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteApiToInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

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

    def list_apis(self, request):
        """查询API列表

        查询API列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApis
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListApisRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListApisResponse`
        """
        http_info = self._list_apis_http_info(request)
        return self._call_api(**http_info)

    def list_apis_invoker(self, request):
        http_info = self._list_apis_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_apis_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/apis",
            "request_type": request.__class__.__name__,
            "response_type": "ListApisResponse"
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
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_instance_list(self, request):
        """查看API不同操作对应的实例信息

        查看API不同操作对应的实例信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceList
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListInstanceListRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListInstanceListResponse`
        """
        http_info = self._list_instance_list_http_info(request)
        return self._call_api(**http_info)

    def list_instance_list_invoker(self, request):
        http_info = self._list_instance_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/apis/{api_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))
        if 'show_all' in local_var_params:
            query_params.append(('show_all', local_var_params['show_all']))
        if 'check_status' in local_var_params:
            query_params.append(('check_status', local_var_params['check_status']))
        if 'check_debug' in local_var_params:
            query_params.append(('check_debug', local_var_params['check_debug']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def publish_api(self, request):
        """发布/下线/停用/恢复API

        发布/下线/停用/恢复API
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PublishApi
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.PublishApiRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.PublishApiResponse`
        """
        http_info = self._publish_api_http_info(request)
        return self._call_api(**http_info)

    def publish_api_invoker(self, request):
        http_info = self._publish_api_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _publish_api_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/service/apis/publish",
            "request_type": request.__class__.__name__,
            "response_type": "PublishApiResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def publish_api_to_instance(self, request):
        """发布API

        发布API
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PublishApiToInstance
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.PublishApiToInstanceRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.PublishApiToInstanceResponse`
        """
        http_info = self._publish_api_to_instance_http_info(request)
        return self._call_api(**http_info)

    def publish_api_to_instance_invoker(self, request):
        http_info = self._publish_api_to_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _publish_api_to_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/service/apis/{api_id}/instances/{instance_id}/publish",
            "request_type": request.__class__.__name__,
            "response_type": "PublishApiToInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

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

    def search_debug_info(self, request):
        """查看API调试信息

        查看API调试信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchDebugInfo
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchDebugInfoRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchDebugInfoResponse`
        """
        http_info = self._search_debug_info_http_info(request)
        return self._call_api(**http_info)

    def search_debug_info_invoker(self, request):
        http_info = self._search_debug_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_debug_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/apis/{api_id}/debug-info",
            "request_type": request.__class__.__name__,
            "response_type": "SearchDebugInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def search_publish_info(self, request):
        """查看API发布信息

        查看API发布信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchPublishInfo
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchPublishInfoRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchPublishInfoResponse`
        """
        http_info = self._search_publish_info_http_info(request)
        return self._call_api(**http_info)

    def search_publish_info_invoker(self, request):
        http_info = self._search_publish_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_publish_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/apis/{api_id}/publish-info",
            "request_type": request.__class__.__name__,
            "response_type": "SearchPublishInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_api(self, request):
        """查询API信息

        查询API信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApi
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowApiRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowApiResponse`
        """
        http_info = self._show_api_http_info(request)
        return self._call_api(**http_info)

    def show_api_invoker(self, request):
        http_info = self._show_api_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_api_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service/apis/{api_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApiResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_api(self, request):
        """更新API

        更新API
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateApi
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateApiRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateApiResponse`
        """
        http_info = self._update_api_http_info(request)
        return self._call_api(**http_info)

    def update_api_invoker(self, request):
        http_info = self._update_api_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_api_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/service/apis/{api_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateApiResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']
        if 'dlm_type' in local_var_params:
            header_params['Dlm-Type'] = local_var_params['dlm_type']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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
