# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class DataArtsStudioClient(Client):
    def __init__(self):
        super(DataArtsStudioClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdataartsstudio.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "DataArtsStudioClient":
            raise TypeError("client type error, support client type is DataArtsStudioClient")

        return ClientBuilder(clazz)

    def add_tag_to_asset(self, request):
        """标签关联到资产

        标签关联到资产
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddTagToAsset
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.AddTagToAssetRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.AddTagToAssetResponse`
        """
        return self._add_tag_to_asset_with_http_info(request)

    def _add_tag_to_asset_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/tags/{term_guid}/assignedentities',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddTagToAssetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_work_space_users(self, request):
        """添加工作空间用户

        添加工作空间用户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddWorkSpaceUsers
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.AddWorkSpaceUsersRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.AddWorkSpaceUsersResponse`
        """
        return self._add_work_space_users_with_http_info(request)

    def _add_work_space_users_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

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
            resource_path='/v2/{project_id}/{workspace_id}/users',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddWorkSpaceUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_classification_to_entity(self, request):
        """资产关联分类

        将一个分类关联到一个或多个指定guid的资产上
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateClassificationToEntity
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.AssociateClassificationToEntityRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.AssociateClassificationToEntityResponse`
        """
        return self._associate_classification_to_entity_with_http_info(request)

    def _associate_classification_to_entity_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/asset/entities/guid/{guid}/classification',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociateClassificationToEntityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_security_level_to_entitie(self, request):
        """资产关联密级

        关联资产到密级，资产关联指定密级
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateSecurityLevelToEntitie
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.AssociateSecurityLevelToEntitieRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.AssociateSecurityLevelToEntitieResponse`
        """
        return self._associate_security_level_to_entitie_with_http_info(request)

    def _associate_security_level_to_entitie_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/asset/entities/guid/{guid}/security-level',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociateSecurityLevelToEntitieResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_approve_apply(self, request):
        """审核申请

        审核申请
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchApproveApply
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.BatchApproveApplyRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BatchApproveApplyResponse`
        """
        return self._batch_approve_apply_with_http_info(request)

    def _batch_approve_apply_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/service/applys',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchApproveApplyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_associate_classification_to_entities(self, request):
        """批量资产关联分类

        批量资产关联分类：只支持对数据表的列和OBS对象添加分类
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchAssociateClassificationToEntities
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.BatchAssociateClassificationToEntitiesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BatchAssociateClassificationToEntitiesResponse`
        """
        return self._batch_associate_classification_to_entities_with_http_info(request)

    def _batch_associate_classification_to_entities_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v3/{project_id}/asset/entities/classification',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchAssociateClassificationToEntitiesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_associate_security_level_to_entities(self, request):
        """批量资产关联密级

        批量资产关联密级：单个密级关联到多个资产上
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchAssociateSecurityLevelToEntities
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.BatchAssociateSecurityLevelToEntitiesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BatchAssociateSecurityLevelToEntitiesResponse`
        """
        return self._batch_associate_security_level_to_entities_with_http_info(request)

    def _batch_associate_security_level_to_entities_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v3/{project_id}/asset/entities/security-level',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchAssociateSecurityLevelToEntitiesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_templates(self, request):
        """批量删除规则模板

        批量删除规则模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteTemplates
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.BatchDeleteTemplatesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BatchDeleteTemplatesResponse`
        """
        return self._batch_delete_templates_with_http_info(request)

    def _batch_delete_templates_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/quality/rule-templates/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_offline(self, request):
        """批量下线

        批量下线
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchOffline
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.BatchOfflineRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BatchOfflineResponse`
        """
        return self._batch_offline_with_http_info(request)

    def _batch_offline_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/design/approvals/batch-offline',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchOfflineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_publish(self, request):
        """批量发布

        批量发布
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchPublish
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.BatchPublishRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BatchPublishResponse`
        """
        return self._batch_publish_with_http_info(request)

    def _batch_publish_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/design/approvals/batch-publish',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchPublishResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_catalog(self, request):
        """修改流程架构

        修改流程架构
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeCatalog
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ChangeCatalogRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ChangeCatalogResponse`
        """
        return self._change_catalog_with_http_info(request)

    def _change_catalog_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/design/biz/catalogs',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeCatalogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_resource(self, request):
        """规格变更接口

        规格变更接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeResource
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ChangeResourceRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ChangeResourceResponse`
        """
        return self._change_resource_with_http_info(request)

    def _change_resource_with_http_info(self, request):
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/change-resource',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_subjects(self, request):
        """修改或删除主题层级

        修改或删除主题层级
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeSubjects
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ChangeSubjectsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ChangeSubjectsResponse`
        """
        return self._change_subjects_with_http_info(request)

    def _change_subjects_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/design/subject-levels',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeSubjectsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_dimension_status(self, request):
        """查看逆向维度表任务

        查看逆向维度表任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckDimensionStatus
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CheckDimensionStatusRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CheckDimensionStatusResponse`
        """
        return self._check_dimension_status_with_http_info(request)

    def _check_dimension_status_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/dimension/database',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CheckDimensionStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_fact_logic_table_status(self, request):
        """查看逆向事实表任务

        查看逆向事实表任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckFactLogicTableStatus
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CheckFactLogicTableStatusRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CheckFactLogicTableStatusResponse`
        """
        return self._check_fact_logic_table_status_with_http_info(request)

    def _check_fact_logic_table_status_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/fact-logic-tables/database',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CheckFactLogicTableStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def confirm_approvals(self, request):
        """审批单处理

        审批驳回/通过，单个或多个 action-id&#x3D;reject/resolve
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ConfirmApprovals
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ConfirmApprovalsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ConfirmApprovalsResponse`
        """
        return self._confirm_approvals_with_http_info(request)

    def _confirm_approvals_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/design/approvals/action',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ConfirmApprovalsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def confirm_message(self, request):
        """处理消息

        处理消息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ConfirmMessage
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ConfirmMessageRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ConfirmMessageResponse`
        """
        return self._confirm_message_with_http_info(request)

    def _confirm_message_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/service/messages',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ConfirmMessageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def count_all_models(self, request):
        """关系建模统计信息

        关系建模统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountAllModels
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CountAllModelsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CountAllModelsResponse`
        """
        return self._count_all_models_with_http_info(request)

    def _count_all_models_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/models/statistic',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CountAllModelsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def count_overviews(self, request):
        """总览统计信息

        总览统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountOverviews
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CountOverviewsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CountOverviewsResponse`
        """
        return self._count_overviews_with_http_info(request)

    def _count_overviews_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/definitions/statistic',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CountOverviewsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def count_standards(self, request):
        """标准覆盖率统计信息

        标准覆盖率统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountStandards
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CountStandardsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CountStandardsResponse`
        """
        return self._count_standards_with_http_info(request)

    def _count_standards_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/definitions/statistic/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CountStandardsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def count_table_models(self, request):
        """模型统计信息

        模型统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountTableModels
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CountTableModelsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CountTableModelsResponse`
        """
        return self._count_table_models_with_http_info(request)

    def _count_table_models_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/table-models/statistic',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CountTableModelsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_app(self, request):
        """创建应用

        创建应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateApp
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateAppRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateAppResponse`
        """
        return self._create_app_with_http_info(request)

    def _create_app_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/service/apps',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_approver(self, request):
        """创建审批人

        创建审批人
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateApprover
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateApproverRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateApproverResponse`
        """
        return self._create_approver_with_http_info(request)

    def _create_approver_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/design/approvals/users',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateApproverResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_biz_metric(self, request):
        """创建业务指标

        创建业务指标
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateBizMetric
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateBizMetricRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateBizMetricResponse`
        """
        return self._create_biz_metric_with_http_info(request)

    def _create_biz_metric_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/design/biz-metrics',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateBizMetricResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_catalog(self, request):
        """创建流程架构

        创建流程架构
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCatalog
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateCatalogRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateCatalogResponse`
        """
        return self._create_catalog_with_http_info(request)

    def _create_catalog_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/design/biz/catalogs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCatalogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_code_table(self, request):
        """创建码表

        创建码表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCodeTable
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateCodeTableRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateCodeTableResponse`
        """
        return self._create_code_table_with_http_info(request)

    def _create_code_table_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/design/code-tables',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCodeTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_connections(self, request):
        """创建数据连接

        创建数据连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateConnections
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateConnectionsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateConnectionsResponse`
        """
        return self._create_connections_with_http_info(request)

    def _create_connections_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v1/{project_id}/data-connections',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateConnectionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_directory(self, request):
        """创建目录

        创建目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDirectory
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateDirectoryRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateDirectoryResponse`
        """
        return self._create_directory_with_http_info(request)

    def _create_directory_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/design/directorys',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDirectoryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_factory_env(self, request):
        """创建环境变量

        创建环境变量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFactoryEnv
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateFactoryEnvRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateFactoryEnvResponse`
        """
        return self._create_factory_env_with_http_info(request)

    def _create_factory_env_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["status_code", "is_success", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/factory/env',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateFactoryEnvResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_factory_supplement_data_instance(self, request):
        """创建补数据实例的接口

        创建一个补数据实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFactorySupplementDataInstance
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateFactorySupplementDataInstanceRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateFactorySupplementDataInstanceResponse`
        """
        return self._create_factory_supplement_data_instance_with_http_info(request)

    def _create_factory_supplement_data_instance_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/factory/supplement-data',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateFactorySupplementDataInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_manager_work_space(self, request):
        """创建工作空间

        创建工作空间
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateManagerWorkSpace
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateManagerWorkSpaceRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateManagerWorkSpaceResponse`
        """
        return self._create_manager_work_space_with_http_info(request)

    def _create_manager_work_space_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v1/{project_id}/workspaces/{instance_id}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateManagerWorkSpaceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_or_update_asset(self, request):
        """添加或修改资产

        添加或修改资产
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateOrUpdateAsset
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateOrUpdateAssetRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateOrUpdateAssetResponse`
        """
        return self._create_or_update_asset_with_http_info(request)

    def _create_or_update_asset_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v3/{project_id}/asset',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateOrUpdateAssetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_service_catalog(self, request):
        """创建服务目录

        创建服务目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateServiceCatalog
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateServiceCatalogRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateServiceCatalogResponse`
        """
        return self._create_service_catalog_with_http_info(request)

    def _create_service_catalog_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/service/servicecatalogs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateServiceCatalogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_standard(self, request):
        """创建数据标准

        创建数据标准
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateStandard
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateStandardRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateStandardResponse`
        """
        return self._create_standard_with_http_info(request)

    def _create_standard_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/design/standards',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateStandardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_standard_template(self, request):
        """创建数据标准模板

        创建数据标准模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateStandardTemplate
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateStandardTemplateRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateStandardTemplateResponse`
        """
        return self._create_standard_template_with_http_info(request)

    def _create_standard_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/design/standards/templates',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateStandardTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_subject(self, request):
        """创建主题

        创建主题
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSubject
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateSubjectRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateSubjectResponse`
        """
        return self._create_subject_with_http_info(request)

    def _create_subject_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/design/subjects',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSubjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_subject_new(self, request):
        """创建主题(新)

        创建主题(新)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSubjectNew
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateSubjectNewRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateSubjectNewResponse`
        """
        return self._create_subject_new_with_http_info(request)

    def _create_subject_new_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v3/{project_id}/design/subjects',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSubjectNewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_table_model(self, request):
        """创建模型实体

        创建一个模型实体，包括逻辑实体或物理数据表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTableModel
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateTableModelRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateTableModelResponse`
        """
        return self._create_table_model_with_http_info(request)

    def _create_table_model_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/design/table-model',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTableModelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_task(self, request):
        """创建采集任务

        创建采集任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTask
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateTaskRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateTaskResponse`
        """
        return self._create_task_with_http_info(request)

    def _create_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v3/{project_id}/metadata/tasks/create',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_template(self, request):
        """创建规则模板

        创建规则模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTemplate
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateTemplateRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateTemplateResponse`
        """
        return self._create_template_with_http_info(request)

    def _create_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/quality/rule-templates',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_workspace(self, request):
        """新建模型工作区

        新建模型工作区
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateWorkspace
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateWorkspaceRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateWorkspaceResponse`
        """
        return self._create_workspace_with_http_info(request)

    def _create_workspace_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/design/workspaces',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateWorkspaceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def debug_dataconnection(self, request):
        """测试创建数据连接

        测试创建数据连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DebugDataconnection
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DebugDataconnectionRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DebugDataconnectionResponse`
        """
        return self._debug_dataconnection_with_http_info(request)

    def _debug_dataconnection_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v1/{project_id}/data-connections/validation',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DebugDataconnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_app(self, request):
        """删除应用

        删除应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApp
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteAppRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteAppResponse`
        """
        return self._delete_app_with_http_info(request)

    def _delete_app_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/apps/{app_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_approver(self, request):
        """删除审批人

        删除审批人
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApprover
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteApproverRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteApproverResponse`
        """
        return self._delete_approver_with_http_info(request)

    def _delete_approver_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/approvals/users',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteApproverResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_asset(self, request):
        """删除资产

        删除资产
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAsset
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteAssetRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteAssetResponse`
        """
        return self._delete_asset_with_http_info(request)

    def _delete_asset_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/asset/{guid}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAssetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_biz_metric(self, request):
        """删除业务指标

        删除业务指标
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBizMetric
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteBizMetricRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteBizMetricResponse`
        """
        return self._delete_biz_metric_with_http_info(request)

    def _delete_biz_metric_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/design/biz-metrics',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteBizMetricResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_catalog(self, request):
        """删除流程架构

        删除流程架构
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCatalog
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteCatalogRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteCatalogResponse`
        """
        return self._delete_catalog_with_http_info(request)

    def _delete_catalog_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/design/biz/catalogs',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteCatalogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_classification_from_entities(self, request):
        """移除资产关联的分类

        移除资产关联分类：
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteClassificationFromEntities
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteClassificationFromEntitiesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteClassificationFromEntitiesResponse`
        """
        return self._delete_classification_from_entities_with_http_info(request)

    def _delete_classification_from_entities_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/asset/entities/guid/{guid}/classification',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteClassificationFromEntitiesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_code_table(self, request):
        """删除码表

        删除码表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCodeTable
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteCodeTableRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteCodeTableResponse`
        """
        return self._delete_code_table_with_http_info(request)

    def _delete_code_table_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/design/code-tables',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteCodeTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_dataconnection(self, request):
        """删除数据连接

        删除数据连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDataconnection
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteDataconnectionRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteDataconnectionResponse`
        """
        return self._delete_dataconnection_with_http_info(request)

    def _delete_dataconnection_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/data-connections/{data_connection_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDataconnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_directory(self, request):
        """删除目录

        删除目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDirectory
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteDirectoryRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteDirectoryResponse`
        """
        return self._delete_directory_with_http_info(request)

    def _delete_directory_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/directorys',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDirectoryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_security_level_from_entity(self, request):
        """移除资产关联密级

        移除资产关联密级
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSecurityLevelFromEntity
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteSecurityLevelFromEntityRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteSecurityLevelFromEntityResponse`
        """
        return self._delete_security_level_from_entity_with_http_info(request)

    def _delete_security_level_from_entity_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/asset/entities/guid/{guid}/security-level',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSecurityLevelFromEntityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_service_catalog(self, request):
        """批量删除目录

        批量删除目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteServiceCatalog
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteServiceCatalogRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteServiceCatalogResponse`
        """
        return self._delete_service_catalog_with_http_info(request)

    def _delete_service_catalog_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/service/servicecatalogs/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteServiceCatalogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_standard(self, request):
        """删除数据标准

        删除数据标准
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteStandard
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteStandardRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteStandardResponse`
        """
        return self._delete_standard_with_http_info(request)

    def _delete_standard_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/design/standards',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteStandardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_standard_template(self, request):
        """删除数据标准模板

        删除数据标准模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteStandardTemplate
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteStandardTemplateRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteStandardTemplateResponse`
        """
        return self._delete_standard_template_with_http_info(request)

    def _delete_standard_template_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/standards/templates',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteStandardTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_subject(self, request):
        """删除主题

        删除主题
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSubject
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteSubjectRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteSubjectResponse`
        """
        return self._delete_subject_with_http_info(request)

    def _delete_subject_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/design/subjects',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSubjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_subject_new(self, request):
        """删除主题(新)

        删除主题(新)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSubjectNew
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteSubjectNewRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteSubjectNewResponse`
        """
        return self._delete_subject_new_with_http_info(request)

    def _delete_subject_new_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v3/{project_id}/design/subjects',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSubjectNewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_table_model(self, request):
        """删除模型实体

        删除一个模型实体，包括逻辑实体或物理数据表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTableModel
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteTableModelRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteTableModelResponse`
        """
        return self._delete_table_model_with_http_info(request)

    def _delete_table_model_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/design/table-model',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTableModelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_task_info(self, request):
        """删除单个采集任务

        删除单个采集任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTaskInfo
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteTaskInfoRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteTaskInfoResponse`
        """
        return self._delete_task_info_with_http_info(request)

    def _delete_task_info_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/metadata/tasks/{task_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTaskInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_workspaces(self, request):
        """删除模型工作区

        删除模型工作区
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteWorkspaces
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteWorkspacesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteWorkspacesResponse`
        """
        return self._delete_workspaces_with_http_info(request)

    def _delete_workspaces_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/workspaces',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteWorkspacesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_workspaceusers(self, request):
        """删除工作空间用户

        删除工作空间用户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteWorkspaceusers
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteWorkspaceusersRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteWorkspaceusersResponse`
        """
        return self._delete_workspaceusers_with_http_info(request)

    def _delete_workspaceusers_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

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
            resource_path='/v2/{project_id}/{workspace_id}/delete-users',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteWorkspaceusersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_task_action(self, request):
        """启动、调度、停止采集任务

        启动、调度、停止采集任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteTaskAction
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ExecuteTaskActionRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ExecuteTaskActionResponse`
        """
        return self._execute_task_action_with_http_info(request)

    def _execute_task_action_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/metadata/tasks/{task_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteTaskActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def import_result(self, request):
        """查询导入结果

        查询导入excel的处理结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportResult
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ImportResultRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ImportResultResponse`
        """
        return self._import_result_with_http_info(request)

    def _import_result_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/catelogs/process-import',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ImportResultResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def initialize_standard_template(self, request):
        """初始化数据标准模板

        初始化模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for InitializeStandardTemplate
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.InitializeStandardTemplateRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.InitializeStandardTemplateResponse`
        """
        return self._initialize_standard_template_with_http_info(request)

    def _initialize_standard_template_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/design/standards/templates/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='InitializeStandardTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_aggregation_logic_tables(self, request):
        """查找汇总表

        通过中英文名称、创建者、审核人、状态、修改时间分页查找汇总表信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAggregationLogicTables
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListAggregationLogicTablesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListAggregationLogicTablesResponse`
        """
        return self._list_aggregation_logic_tables_with_http_info(request)

    def _list_aggregation_logic_tables_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/aggregation-logic-tables',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAggregationLogicTablesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_all_catalog_list(self, request):
        """获取当前目录下的所有类型列表

        获取当前目录下的所有类型列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAllCatalogList
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListAllCatalogListRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListAllCatalogListResponse`
        """
        return self._list_all_catalog_list_with_http_info(request)

    def _list_all_catalog_list_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/servicecatalogs/{catalog_id}/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAllCatalogListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_all_standards(self, request):
        """获取数据标准

        获取数据标准
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAllStandards
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListAllStandardsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListAllStandardsResponse`
        """
        return self._list_all_standards_with_http_info(request)

    def _list_all_standards_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/standards',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAllStandardsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_api_catalog_list(self, request):
        """获取当前目录下的api列表

        获取当前目录下的api列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApiCatalogList
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListApiCatalogListRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListApiCatalogListResponse`
        """
        return self._list_api_catalog_list_with_http_info(request)

    def _list_api_catalog_list_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/servicecatalogs/{catalog_id}/apis',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApiCatalogListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_api_top_n(self, request):
        """查询指定api 应用调用topN

        查询指定api 应用调用topN
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApiTopN
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListApiTopNRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListApiTopNResponse`
        """
        return self._list_api_top_n_with_http_info(request)

    def _list_api_top_n_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/statistic/apis-top-n/{api_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApiTopNResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apic_groups(self, request):
        """获取网关分组

        获取网关分组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApicGroups
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListApicGroupsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListApicGroupsResponse`
        """
        return self._list_apic_groups_with_http_info(request)

    def _list_apic_groups_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/apigw/instances/{apig_instance_id}/groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApicGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apic_instances(self, request):
        """获取网关实例

        获取网关实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApicInstances
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListApicInstancesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListApicInstancesResponse`
        """
        return self._list_apic_instances_with_http_info(request)

    def _list_apic_instances_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/apigw/instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApicInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apis_top(self, request):
        """查询api 服务调用topN

        查询api 服务调用topN
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApisTop
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListApisTopRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListApisTopResponse`
        """
        return self._list_apis_top_with_http_info(request)

    def _list_apis_top_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/statistic/apis-top-n',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApisTopResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apply(self, request):
        """查询申请列表

        查询申请列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApply
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListApplyRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListApplyResponse`
        """
        return self._list_apply_with_http_info(request)

    def _list_apply_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/applys',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApplyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_approvers(self, request):
        """查询审批人列表

        查询审批人列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApprovers
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListApproversRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListApproversResponse`
        """
        return self._list_approvers_with_http_info(request)

    def _list_approvers_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/approvals/users',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApproversResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apps(self, request):
        """查询应用列表

        查询应用列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApps
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListAppsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListAppsResponse`
        """
        return self._list_apps_with_http_info(request)

    def _list_apps_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/apps',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAppsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apps_top(self, request):
        """查询app 服务使用topN

        查询app 服务使用topN
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAppsTop
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListAppsTopRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListAppsTopResponse`
        """
        return self._list_apps_top_with_http_info(request)

    def _list_apps_top_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/statistic/apps-top-n',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAppsTopResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_biz_metric_dimensions(self, request):
        """查看指标维度信息

        查看指标维度信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBizMetricDimensions
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListBizMetricDimensionsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListBizMetricDimensionsResponse`
        """
        return self._list_biz_metric_dimensions_with_http_info(request)

    def _list_biz_metric_dimensions_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/biz-metrics/dimensions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBizMetricDimensionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_biz_metric_owners(self, request):
        """查看指标指标责任人信息

        查看指标指标责任人信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBizMetricOwners
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListBizMetricOwnersRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListBizMetricOwnersResponse`
        """
        return self._list_biz_metric_owners_with_http_info(request)

    def _list_biz_metric_owners_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/biz-metrics/owners',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBizMetricOwnersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_biz_metrics(self, request):
        """查询业务指标信息

        通过名称、创建者、修改时间分页查找业务指标信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBizMetrics
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListBizMetricsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListBizMetricsResponse`
        """
        return self._list_biz_metrics_with_http_info(request)

    def _list_biz_metrics_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/biz-metrics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBizMetricsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_business(self, request):
        """获取主题树信息

        获取数据资产主题树信息l1，l2，l3
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBusiness
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListBusinessRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListBusinessResponse`
        """
        return self._list_business_with_http_info(request)

    def _list_business_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/subjects/business',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBusinessResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_catalog_list(self, request):
        """获取当前目录下的目录列表（全量）

        获取当前目录下的目录列表（全量）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCatalogList
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListCatalogListRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListCatalogListResponse`
        """
        return self._list_catalog_list_with_http_info(request)

    def _list_catalog_list_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/servicecatalogs/{catalog_id}/catalogs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCatalogListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_catalog_tree(self, request):
        """获取所有流程架构目录树

        获取所有目录树
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCatalogTree
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListCatalogTreeRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListCatalogTreeResponse`
        """
        return self._list_catalog_tree_with_http_info(request)

    def _list_catalog_tree_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/biz/catalogs/tree',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCatalogTreeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_category(self, request):
        """获取作业目录

        获取作业目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCategory
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListCategoryRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListCategoryResponse`
        """
        return self._list_category_with_http_info(request)

    def _list_category_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/quality/categories',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCategoryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_columns(self, request):
        """获取数据源中表的字段

        获取数据源中表的字段
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListColumns
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListColumnsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListColumnsResponse`
        """
        return self._list_columns_with_http_info(request)

    def _list_columns_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/{connection_id}/datatables/{table_id}/columns',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListColumnsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_compound_metrics(self, request):
        """查找复合指标

        通过中英文名称、创建者、审核人、状态、修改时间、l3Id分页查找复合指标信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCompoundMetrics
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListCompoundMetricsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListCompoundMetricsResponse`
        """
        return self._list_compound_metrics_with_http_info(request)

    def _list_compound_metrics_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/compound-metrics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCompoundMetricsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_condition(self, request):
        """查找业务限定

        通过中英文名称、描述、创建者、审核人、限定分组id、修改时间状态分页查找限定信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCondition
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListConditionRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListConditionResponse`
        """
        return self._list_condition_with_http_info(request)

    def _list_condition_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/conditions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListConditionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_consistency_task(self, request):
        """获取对账作业列表

        获取对账作业列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConsistencyTask
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListConsistencyTaskRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListConsistencyTaskResponse`
        """
        return self._list_consistency_task_with_http_info(request)

    def _list_consistency_task_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/quality/consistency-tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListConsistencyTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_data_arts_studio_instances(self, request):
        """获取实例列表

        获取实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDataArtsStudioInstances
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListDataArtsStudioInstancesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListDataArtsStudioInstancesResponse`
        """
        return self._list_data_arts_studio_instances_with_http_info(request)

    def _list_data_arts_studio_instances_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDataArtsStudioInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_data_tables(self, request):
        """获取数据源中的表

        获取数据源中的表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDataTables
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListDataTablesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListDataTablesResponse`
        """
        return self._list_data_tables_with_http_info(request)

    def _list_data_tables_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/{connection_id}/datatables',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDataTablesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_databases(self, request):
        """获取数据库列表

        获取数据库列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDatabases
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListDatabasesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListDatabasesResponse`
        """
        return self._list_databases_with_http_info(request)

    def _list_databases_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/{connection_id}/databases',
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

    def list_dataconnections(self, request):
        """查询数据连接列表

        查询数据连接列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDataconnections
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListDataconnectionsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListDataconnectionsResponse`
        """
        return self._list_dataconnections_with_http_info(request)

    def _list_dataconnections_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/data-connections',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDataconnectionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_derivative_indexes(self, request):
        """查找衍生指标

        通过中英文名称、创建者、审核人、状态、修改时间、l3Id分页查找衍生指标信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDerivativeIndexes
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListDerivativeIndexesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListDerivativeIndexesResponse`
        """
        return self._list_derivative_indexes_with_http_info(request)

    def _list_derivative_indexes_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/derivative-indexs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDerivativeIndexesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_dimension_groups(self, request):
        """查看维度颗粒度

        查询维度颗粒度, 依据tableId查询涉及所有维度，不传tableId查询所有维度组颗粒度
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDimensionGroups
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListDimensionGroupsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListDimensionGroupsResponse`
        """
        return self._list_dimension_groups_with_http_info(request)

    def _list_dimension_groups_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/dimension/groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDimensionGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_dimension_logic_tables(self, request):
        """查找维度表

        通过中英文名称、创建者、审核人、状态、修改时间分页查找维度表信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDimensionLogicTables
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListDimensionLogicTablesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListDimensionLogicTablesResponse`
        """
        return self._list_dimension_logic_tables_with_http_info(request)

    def _list_dimension_logic_tables_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/dimension-logic-tables',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDimensionLogicTablesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_dimensions(self, request):
        """查找维度

        通过中英文名称、描述、创建者、审核人、状态、l3Id、派生指标idList、修改时间分页查找维度信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDimensions
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListDimensionsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListDimensionsResponse`
        """
        return self._list_dimensions_with_http_info(request)

    def _list_dimensions_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/dimensions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDimensionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_directories(self, request):
        """获取所有目录

        获取所有目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDirectories
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListDirectoriesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListDirectoriesResponse`
        """
        return self._list_directories_with_http_info(request)

    def _list_directories_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/directorys',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDirectoriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_fact_logic_tables(self, request):
        """查找事实表

        通过中英文名称、创建者、审核人、状态、修改时间分页查找事实表信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFactLogicTables
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListFactLogicTablesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListFactLogicTablesResponse`
        """
        return self._list_fact_logic_tables_with_http_info(request)

    def _list_fact_logic_tables_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/fact-logic-tables',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFactLogicTablesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instances(self, request):
        """获取任务执行结果列表

        获取任务执行结果列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstances
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListInstancesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListInstancesResponse`
        """
        return self._list_instances_with_http_info(request)

    def _list_instances_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/quality/instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_manager_work_spaces(self, request):
        """获取工作空间列表

        获取工作空间列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListManagerWorkSpaces
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListManagerWorkSpacesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListManagerWorkSpacesResponse`
        """
        return self._list_manager_work_spaces_with_http_info(request)

    def _list_manager_work_spaces_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{instance_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListManagerWorkSpacesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_message(self, request):
        """查询消息列表

        查询消息列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMessage
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListMessageRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListMessageResponse`
        """
        return self._list_message_with_http_info(request)

    def _list_message_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/messages',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListMessageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_metric_relations(self, request):
        """获取指标关联信息

        获取当前指标图谱
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMetricRelations
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListMetricRelationsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListMetricRelationsResponse`
        """
        return self._list_metric_relations_with_http_info(request)

    def _list_metric_relations_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/metric-relations/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListMetricRelationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_quality_task(self, request):
        """获取质量作业列表

        获取质量作业列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQualityTask
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListQualityTaskRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListQualityTaskResponse`
        """
        return self._list_quality_task_with_http_info(request)

    def _list_quality_task_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/quality/quality-tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListQualityTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_quality_task_lists(self, request):
        """获取质量作业列表V1

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQualityTaskLists
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListQualityTaskListsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListQualityTaskListsResponse`
        """
        return self._list_quality_task_lists_with_http_info(request)

    def _list_quality_task_lists_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/quality/rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListQualityTaskListsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_quality_templates(self, request):
        """获取规则模板列表

        分页获取规则模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQualityTemplates
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListQualityTemplatesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListQualityTemplatesResponse`
        """
        return self._list_quality_templates_with_http_info(request)

    def _list_quality_templates_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/quality/rule-templates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListQualityTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_relations(self, request):
        """关系

        通过名称、等分页查找关系信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRelations
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListRelationsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListRelationsResponse`
        """
        return self._list_relations_with_http_info(request)

    def _list_relations_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/relation',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRelationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_schemas(self, request):
        """获取schemas

        获取schemas,目前只有DWS和采用postgresql驱动的RDS数据源支持schema,请在调用前确认该数据源是否支持schema字段
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSchemas
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListSchemasRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListSchemasResponse`
        """
        return self._list_schemas_with_http_info(request)

    def _list_schemas_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/{connection_id}/schemas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSchemasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_subject_levels(self, request):
        """获取主题层级

        获取主题层级
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSubjectLevels
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListSubjectLevelsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListSubjectLevelsResponse`
        """
        return self._list_subject_levels_with_http_info(request)

    def _list_subject_levels_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/subject-levels',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSubjectLevelsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_table_model_relations(self, request):
        """查询模型下所有关系

        查询模型下所有关系
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTableModelRelations
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListTableModelRelationsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListTableModelRelationsResponse`
        """
        return self._list_table_model_relations_with_http_info(request)

    def _list_table_model_relations_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/{model_id}/table-model/relation',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTableModelRelationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_table_models(self, request):
        """查找模型实体列表

        通过中英文名称、创建者、审核人、状态、修改时间分页查找模型实体信息，包含逻辑实体、表或属性。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTableModels
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListTableModelsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListTableModelsResponse`
        """
        return self._list_table_models_with_http_info(request)

    def _list_table_models_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/table-model',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTableModelsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_workspace_roles(self, request):
        """获取工作空间用户角色

        获取工作空间用户角色
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWorkspaceRoles
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListWorkspaceRolesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListWorkspaceRolesResponse`
        """
        return self._list_workspace_roles_with_http_info(request)

    def _list_workspace_roles_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/users/role',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListWorkspaceRolesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_workspaces(self, request):
        """获取模型

        获取模型
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWorkspaces
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListWorkspacesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListWorkspacesResponse`
        """
        return self._list_workspaces_with_http_info(request)

    def _list_workspaces_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/workspaces',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListWorkspacesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_workspaceusers(self, request):
        """获取工作空间用户信息

        获取工作空间用户信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWorkspaceusers
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListWorkspaceusersRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListWorkspaceusersResponse`
        """
        return self._list_workspaceusers_with_http_info(request)

    def _list_workspaceusers_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/{workspace_id}/users',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListWorkspaceusersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def migrate_api(self, request):
        """批量移动api至新目录

        批量移动api至新目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for MigrateApi
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.MigrateApiRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.MigrateApiResponse`
        """
        return self._migrate_api_with_http_info(request)

    def _migrate_api_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/service/servicecatalogs/apis/batch-move',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='MigrateApiResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def migrate_catalog(self, request):
        """移动当前目录至新目录

        移动当前目录至新目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for MigrateCatalog
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.MigrateCatalogRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.MigrateCatalogResponse`
        """
        return self._migrate_catalog_with_http_info(request)

    def _migrate_catalog_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/service/servicecatalogs/{catalog_id}/move',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='MigrateCatalogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def modify_customized_fields(self, request):
        """修改自定义项

        修改自定义项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyCustomizedFields
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ModifyCustomizedFieldsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ModifyCustomizedFieldsResponse`
        """
        return self._modify_customized_fields_with_http_info(request)

    def _modify_customized_fields_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/design/customized-fields',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ModifyCustomizedFieldsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def pay_for_dgc_one_key(self, request):
        """DataArtsStudio实例一键购买接口

        DataArtsStudio实例一键购买接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PayForDgcOneKey
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.PayForDgcOneKeyRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.PayForDgcOneKeyResponse`
        """
        return self._pay_for_dgc_one_key_with_http_info(request)

    def _pay_for_dgc_one_key_with_http_info(self, request):
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/instances/onekey-purchase',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='PayForDgcOneKeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reset_link_attribute_and_standard(self, request):
        """关联属性与数据标准

        关联属性与数据标准
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetLinkAttributeAndStandard
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ResetLinkAttributeAndStandardRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ResetLinkAttributeAndStandardResponse`
        """
        return self._reset_link_attribute_and_standard_with_http_info(request)

    def _reset_link_attribute_and_standard_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/design/standards/attribute',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResetLinkAttributeAndStandardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def rollback_approval(self, request):
        """撤回审批单

        撤回审批单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RollbackApproval
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.RollbackApprovalRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.RollbackApprovalResponse`
        """
        return self._rollback_approval_with_http_info(request)

    def _rollback_approval_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/approvals',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RollbackApprovalResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_approvals(self, request):
        """获取审批单

        获取审批单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchApprovals
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchApprovalsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchApprovalsResponse`
        """
        return self._search_approvals_with_http_info(request)

    def _search_approvals_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/approvals',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchApprovalsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_atomic_indexes(self, request):
        """查找原子指标

        通过中英文名称、创建者、审核人、状态、修改时间分页查找原子指标信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchAtomicIndexes
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchAtomicIndexesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchAtomicIndexesResponse`
        """
        return self._search_atomic_indexes_with_http_info(request)

    def _search_atomic_indexes_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/atomic-indexs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchAtomicIndexesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_authorize_app(self, request):
        """查询API已授权的APP

        查询API已授权的APP
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchAuthorizeApp
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchAuthorizeAppRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchAuthorizeAppResponse`
        """
        return self._search_authorize_app_with_http_info(request)

    def _search_authorize_app_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/authorize/apis/{api_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchAuthorizeAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_bind_api(self, request):
        """查询APP已拥有授权的API

        查询APP已拥有授权的API
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchBindApi
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchBindApiRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchBindApiResponse`
        """
        return self._search_bind_api_with_http_info(request)

    def _search_bind_api_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/authorize/apps/{app_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchBindApiResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_catalogs(self, request):
        """查询流程架构列表

        查询流程架构列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchCatalogs
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchCatalogsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchCatalogsResponse`
        """
        return self._search_catalogs_with_http_info(request)

    def _search_catalogs_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/biz/catalogs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchCatalogsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_code_table_values(self, request):
        """查看码表字段值

        查看码表字段值
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchCodeTableValues
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchCodeTableValuesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchCodeTableValuesResponse`
        """
        return self._search_code_table_values_with_http_info(request)

    def _search_code_table_values_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/code-tables/{id}/values',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchCodeTableValuesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_code_tables(self, request):
        """查询码表列表

        查询码表列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchCodeTables
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchCodeTablesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchCodeTablesResponse`
        """
        return self._search_code_tables_with_http_info(request)

    def _search_code_tables_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/code-tables',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchCodeTablesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_customized_fields(self, request):
        """查询自定义项

        查询自定义项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchCustomizedFields
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchCustomizedFieldsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchCustomizedFieldsResponse`
        """
        return self._search_customized_fields_with_http_info(request)

    def _search_customized_fields_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/customized-fields',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchCustomizedFieldsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_dw_by_type(self, request):
        """获取数据连接信息

        获取指定类型下的数据连接信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchDwByType
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchDwByTypeRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchDwByTypeResponse`
        """
        return self._search_dw_by_type_with_http_info(request)

    def _search_dw_by_type_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/atlas/data-warehouses',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchDwByTypeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_id_by_path(self, request):
        """通过路径获取id

        通过路径获取id
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchIdByPath
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchIdByPathRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchIdByPathResponse`
        """
        return self._search_id_by_path_with_http_info(request)

    def _search_id_by_path_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/servicecatalogs/ids',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchIdByPathResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_subject(self, request):
        """查找主题列表

        通过名称、创建者、责任人、状态、修改时间分页查找主题
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchSubject
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchSubjectRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchSubjectResponse`
        """
        return self._search_subject_with_http_info(request)

    def _search_subject_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/subjects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchSubjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_subject_new(self, request):
        """查找主题列表(新)

        查找主题(新)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchSubjectNew
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchSubjectNewRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchSubjectNewResponse`
        """
        return self._search_subject_new_with_http_info(request)

    def _search_subject_new_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/design/subjects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchSubjectNewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_versions(self, request):
        """查找版本信息

        通过名称、创建者、修改时间查找版本信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchVersions
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchVersionsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchVersionsResponse`
        """
        return self._search_versions_with_http_info(request)

    def _search_versions_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/versions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchVersionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_aggregation_logic_table_by_id(self, request):
        """查看汇总表详情

        通过id查看汇总表的详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAggregationLogicTableById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowAggregationLogicTableByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowAggregationLogicTableByIdResponse`
        """
        return self._show_aggregation_logic_table_by_id_with_http_info(request)

    def _show_aggregation_logic_table_by_id_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/aggregation-logic-tables/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAggregationLogicTableByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_api_dashboard(self, request):
        """查询指定api 仪表板数据详情

        查询指定api 仪表板数据详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApiDashboard
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowApiDashboardRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowApiDashboardResponse`
        """
        return self._show_api_dashboard_with_http_info(request)

    def _show_api_dashboard_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/statistic/apis-dashboards/{api_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowApiDashboardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_apis_dashboard(self, request):
        """查询api 仪表板数据详情

        查询api 仪表板数据详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApisDashboard
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowApisDashboardRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowApisDashboardResponse`
        """
        return self._show_apis_dashboard_with_http_info(request)

    def _show_apis_dashboard_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/statistic/apis-dashboards',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowApisDashboardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_apis_detail(self, request):
        """查询api 统计数据详情

        查询api 统计数据详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApisDetail
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowApisDetailRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowApisDetailResponse`
        """
        return self._show_apis_detail_with_http_info(request)

    def _show_apis_detail_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/statistic/apis-detail/{api_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowApisDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_apis_overview(self, request):
        """查询统计用户相关的总览开发指标

        查询统计用户相关的总览开发指标
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApisOverview
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowApisOverviewRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowApisOverviewResponse`
        """
        return self._show_apis_overview_with_http_info(request)

    def _show_apis_overview_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/statistic/apis-overview',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowApisOverviewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_app_info(self, request):
        """查询应用详情

        查询应用详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAppInfo
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowAppInfoRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowAppInfoResponse`
        """
        return self._show_app_info_with_http_info(request)

    def _show_app_info_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/apps/{app_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAppInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_apply_detail(self, request):
        """获取申请详情

        获取申请详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApplyDetail
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowApplyDetailRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowApplyDetailResponse`
        """
        return self._show_apply_detail_with_http_info(request)

    def _show_apply_detail_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/applys/{apply_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowApplyDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_apps_dashboard(self, request):
        """查询app 仪表板数据详情

        查询app 仪表板数据详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAppsDashboard
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowAppsDashboardRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowAppsDashboardResponse`
        """
        return self._show_apps_dashboard_with_http_info(request)

    def _show_apps_dashboard_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/statistic/apps-dashboards',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAppsDashboardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_apps_detail(self, request):
        """查询app 统计数据详情

        查询app 统计数据详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAppsDetail
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowAppsDetailRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowAppsDetailResponse`
        """
        return self._show_apps_detail_with_http_info(request)

    def _show_apps_detail_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/statistic/apps-detail/{app_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAppsDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_apps_overview(self, request):
        """查询统计用户相关的总览调用指标

        查询统计用户相关的总览调用指标
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAppsOverview
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowAppsOverviewRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowAppsOverviewResponse`
        """
        return self._show_apps_overview_with_http_info(request)

    def _show_apps_overview_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/statistic/apps-overview',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAppsOverviewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_atomic_index_by_id(self, request):
        """查看原子指标详情

        通过id获取指标详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAtomicIndexById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowAtomicIndexByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowAtomicIndexByIdResponse`
        """
        return self._show_atomic_index_by_id_with_http_info(request)

    def _show_atomic_index_by_id_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/atomic-indexs/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAtomicIndexByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_biz_catalog_detail(self, request):
        """查找流程架构详情

        查找流程架构详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBizCatalogDetail
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowBizCatalogDetailRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowBizCatalogDetailResponse`
        """
        return self._show_biz_catalog_detail_with_http_info(request)

    def _show_biz_catalog_detail_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/biz/catalogs/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowBizCatalogDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_biz_metric_by_id(self, request):
        """查看指标详情

        通过id查看指标的详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBizMetricById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowBizMetricByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowBizMetricByIdResponse`
        """
        return self._show_biz_metric_by_id_with_http_info(request)

    def _show_biz_metric_by_id_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/biz-metrics/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowBizMetricByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_business_assets(self, request):
        """查询业务资产

        业务资产查询接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBusinessAssets
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowBusinessAssetsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowBusinessAssetsResponse`
        """
        return self._show_business_assets_with_http_info(request)

    def _show_business_assets_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v3/{project_id}/asset/business-assets/search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowBusinessAssetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_business_assets_statistic(self, request):
        """获取业务资产统计信息

        获取业务资产统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBusinessAssetsStatistic
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowBusinessAssetsStatisticRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowBusinessAssetsStatisticResponse`
        """
        return self._show_business_assets_statistic_with_http_info(request)

    def _show_business_assets_statistic_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/asset/statistic/assets/business-assets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowBusinessAssetsStatisticResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_catalog_detail(self, request):
        """查询服务目录

        查询服务目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCatalogDetail
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowCatalogDetailRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowCatalogDetailResponse`
        """
        return self._show_catalog_detail_with_http_info(request)

    def _show_catalog_detail_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/servicecatalogs/{catalog_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCatalogDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_code_table_by_id(self, request):
        """查看码表详情

        通过id查看码表的详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCodeTableById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowCodeTableByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowCodeTableByIdResponse`
        """
        return self._show_code_table_by_id_with_http_info(request)

    def _show_code_table_by_id_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/code-tables/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCodeTableByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_compound_metric_by_id(self, request):
        """查看复合指标详情

        通过id获取复合指标详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCompoundMetricById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowCompoundMetricByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowCompoundMetricByIdResponse`
        """
        return self._show_compound_metric_by_id_with_http_info(request)

    def _show_compound_metric_by_id_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/compound-metrics/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCompoundMetricByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_condition_by_id(self, request):
        """查看限定详情

        通过id查看限定详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowConditionById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowConditionByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowConditionByIdResponse`
        """
        return self._show_condition_by_id_with_http_info(request)

    def _show_condition_by_id_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/conditions/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowConditionByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_consistency_task_detail(self, request):
        """获取对账作业详情

        获取对账作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowConsistencyTaskDetail
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowConsistencyTaskDetailRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowConsistencyTaskDetailResponse`
        """
        return self._show_consistency_task_detail_with_http_info(request)

    def _show_consistency_task_detail_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/quality/consistency-tasks/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowConsistencyTaskDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_data_profile(self, request):
        """资产信息

        查询概要
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDataProfile
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowDataProfileRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowDataProfileResponse`
        """
        return self._show_data_profile_with_http_info(request)

    def _show_data_profile_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/asset/profile',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDataProfileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_dataconnection(self, request):
        """查询单个数据连接信息

        查询单个数据连接信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDataconnection
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowDataconnectionRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowDataconnectionResponse`
        """
        return self._show_dataconnection_with_http_info(request)

    def _show_dataconnection_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/data-connections/{data_connection_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDataconnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_derivative_index_by_id(self, request):
        """查看衍生指标详情

        通过id获取衍生详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDerivativeIndexById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowDerivativeIndexByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowDerivativeIndexByIdResponse`
        """
        return self._show_derivative_index_by_id_with_http_info(request)

    def _show_derivative_index_by_id_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/derivative-indexs/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDerivativeIndexByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_dimension_by_id(self, request):
        """查看维度详情

        通过id查看维度详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDimensionById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowDimensionByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowDimensionByIdResponse`
        """
        return self._show_dimension_by_id_with_http_info(request)

    def _show_dimension_by_id_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/dimensions/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDimensionByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_dimension_logic_table_by_id(self, request):
        """查看维度表详情

        通过id查看维度表的详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDimensionLogicTableById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowDimensionLogicTableByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowDimensionLogicTableByIdResponse`
        """
        return self._show_dimension_logic_table_by_id_with_http_info(request)

    def _show_dimension_logic_table_by_id_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/dimension-logic-tables/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDimensionLogicTableByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_entities(self, request):
        """查询技术资产

        查询技术资产
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEntities
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowEntitiesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowEntitiesResponse`
        """
        return self._show_entities_with_http_info(request)

    def _show_entities_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v3/{project_id}/asset/entities/search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEntitiesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_entity_info_by_guid(self, request):
        """根据guid获取资产详情

        根据表guid可以获取表的详情信息，表的详情信息包含column的信息，也可以根据column的guid直接获取column的信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEntityInfoByGuid
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowEntityInfoByGuidRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowEntityInfoByGuidResponse`
        """
        return self._show_entity_info_by_guid_with_http_info(request)

    def _show_entity_info_by_guid_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/asset/entities/{guid}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEntityInfoByGuidResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_fact_logic_table_by_id(self, request):
        """查看事实表详情

        通过id查看事实表的详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFactLogicTableById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowFactLogicTableByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowFactLogicTableByIdResponse`
        """
        return self._show_fact_logic_table_by_id_with_http_info(request)

    def _show_fact_logic_table_by_id_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/fact-logic-tables/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowFactLogicTableByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_factory_env(self, request):
        """查询环境变量信息

        查询环境变量信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFactoryEnv
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowFactoryEnvRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowFactoryEnvResponse`
        """
        return self._show_factory_env_with_http_info(request)

    def _show_factory_env_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/factory/env',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowFactoryEnvResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_factory_supplement_data(self, request):
        """查询所有的补数据实例

        查询所有的补数据实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFactorySupplementData
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowFactorySupplementDataRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowFactorySupplementDataResponse`
        """
        return self._show_factory_supplement_data_with_http_info(request)

    def _show_factory_supplement_data_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/factory/supplement-data',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowFactorySupplementDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_glossary_list(self, request):
        """查询标签列表

        查询标签列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGlossaryList
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowGlossaryListRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowGlossaryListResponse`
        """
        return self._show_glossary_list_with_http_info(request)

    def _show_glossary_list_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowGlossaryListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_instance_log(self, request):
        """获取任务日志

        获取任务日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceLog
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowInstanceLogRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowInstanceLogResponse`
        """
        return self._show_instance_log_with_http_info(request)

    def _show_instance_log_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/metadata/tasks/{task_id}/{instance_id}/log',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowInstanceLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_instance_result(self, request):
        """获取实例结果

        获取实例结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceResult
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowInstanceResultRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowInstanceResultResponse`
        """
        return self._show_instance_result_with_http_info(request)

    def _show_instance_result_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/quality/instances/{instance_id}/result',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowInstanceResultResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_message_detail(self, request):
        """获取消息详情

        获取消息详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMessageDetail
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowMessageDetailRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowMessageDetailResponse`
        """
        return self._show_message_detail_with_http_info(request)

    def _show_message_detail_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/messages/{message_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowMessageDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_metric_assets(self, request):
        """查询指标资产

        指标资产查询接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMetricAssets
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowMetricAssetsRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowMetricAssetsResponse`
        """
        return self._show_metric_assets_with_http_info(request)

    def _show_metric_assets_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v3/{project_id}/asset/metric-assets/search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowMetricAssetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_metric_tree(self, request):
        """查询指标资产目录树

        查询指标资产目录树
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMetricTree
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowMetricTreeRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowMetricTreeResponse`
        """
        return self._show_metric_tree_with_http_info(request)

    def _show_metric_tree_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/asset/metric-tree',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowMetricTreeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_path_by_id(self, request):
        """通过id获取路径

        通过id获取路径
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPathById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowPathByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowPathByIdResponse`
        """
        return self._show_path_by_id_with_http_info(request)

    def _show_path_by_id_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/servicecatalogs/{catalog_id}/paths',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPathByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_path_object_by_id(self, request):
        """通过id获取路径对象

        通过id获取路径对象
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPathObjectById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowPathObjectByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowPathObjectByIdResponse`
        """
        return self._show_path_object_by_id_with_http_info(request)

    def _show_path_object_by_id_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/servicecatalogs/{catalog_id}/layerpaths',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPathObjectByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_quality_task_detail(self, request):
        """获取质量作业详情

        获取质量作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowQualityTaskDetail
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowQualityTaskDetailRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowQualityTaskDetailResponse`
        """
        return self._show_quality_task_detail_with_http_info(request)

    def _show_quality_task_detail_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/quality/quality-tasks/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowQualityTaskDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_relation_by_id(self, request):
        """查看关系详情

        通过id获取关系详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRelationById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowRelationByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowRelationByIdResponse`
        """
        return self._show_relation_by_id_with_http_info(request)

    def _show_relation_by_id_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/relation/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowRelationByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_standard_by_id(self, request):
        """查看数据标准详情

        通过id获取数据标准详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowStandardById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowStandardByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowStandardByIdResponse`
        """
        return self._show_standard_by_id_with_http_info(request)

    def _show_standard_by_id_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/standards/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowStandardByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_standard_template(self, request):
        """查询数据标准模板

        查询数据标准模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowStandardTemplate
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowStandardTemplateRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowStandardTemplateResponse`
        """
        return self._show_standard_template_with_http_info(request)

    def _show_standard_template_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/standards/templates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowStandardTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_table_model_by_id(self, request):
        """查看表模型详情

        通过id获取模型表详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTableModelById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowTableModelByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowTableModelByIdResponse`
        """
        return self._show_table_model_by_id_with_http_info(request)

    def _show_table_model_by_id_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/table-model/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTableModelByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_task_info(self, request):
        """查询采集任务详情

        查询采集任务详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTaskInfo
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowTaskInfoRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowTaskInfoResponse`
        """
        return self._show_task_info_with_http_info(request)

    def _show_task_info_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/metadata/tasks/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTaskInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_task_list(self, request):
        """查询采集任务列表

        查询采集任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTaskList
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowTaskListRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowTaskListResponse`
        """
        return self._show_task_list_with_http_info(request)

    def _show_task_list_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v3/{project_id}/metadata/tasks/search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTaskListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_technical_assets_statistic(self, request):
        """获取技术资产统计信息

        获取技术资产统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTechnicalAssetsStatistic
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowTechnicalAssetsStatisticRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowTechnicalAssetsStatisticResponse`
        """
        return self._show_technical_assets_statistic_with_http_info(request)

    def _show_technical_assets_statistic_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/asset/statistic/assets/technical-assets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTechnicalAssetsStatisticResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_templates_detail(self, request):
        """获取规则模板详情

        获取规则模板详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTemplatesDetail
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowTemplatesDetailRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowTemplatesDetailResponse`
        """
        return self._show_templates_detail_with_http_info(request)

    def _show_templates_detail_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/quality/rule-templates/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTemplatesDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_unrelated_table(self, request):
        """无血缘关系表查询

        无血缘关系表查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUnrelatedTable
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowUnrelatedTableRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowUnrelatedTableResponse`
        """
        return self._show_unrelated_table_with_http_info(request)

    def _show_unrelated_table_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v3/{project_id}/lineage/search/unrelated/table',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowUnrelatedTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_work_space(self, request):
        """获取单个工作空间信息

        获取单个工作空间信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowWorkSpace
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowWorkSpaceRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowWorkSpaceResponse`
        """
        return self._show_work_space_with_http_info(request)

    def _show_work_space_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{instance_id}/{workspace_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowWorkSpaceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_workspace_detail_by_id(self, request):
        """查询模型详情

        查询物理模型或逻辑模型的工作区空间详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowWorkspaceDetailById
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowWorkspaceDetailByIdRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowWorkspaceDetailByIdResponse`
        """
        return self._show_workspace_detail_by_id_with_http_info(request)

    def _show_workspace_detail_by_id_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/design/workspaces/{model_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowWorkspaceDetailByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_factory_supplement_data_instance(self, request):
        """停止一个补数据实例

        停止一个补数据实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopFactorySupplementDataInstance
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.StopFactorySupplementDataInstanceRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.StopFactorySupplementDataInstanceResponse`
        """
        return self._stop_factory_supplement_data_instance_with_http_info(request)

    def _stop_factory_supplement_data_instance_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/factory/supplement-data/{instance_name}/stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopFactorySupplementDataInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_app(self, request):
        """更新应用

        更新应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateApp
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateAppRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateAppResponse`
        """
        return self._update_app_with_http_info(request)

    def _update_app_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/service/apps/{app_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_biz_metric(self, request):
        """更新业务指标

        更新业务指标
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateBizMetric
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateBizMetricRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateBizMetricResponse`
        """
        return self._update_biz_metric_with_http_info(request)

    def _update_biz_metric_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/design/biz-metrics',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateBizMetricResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_catalog(self, request):
        """更新服务目录

        更新服务目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCatalog
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateCatalogRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateCatalogResponse`
        """
        return self._update_catalog_with_http_info(request)

    def _update_catalog_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/service/servicecatalogs/{catalog_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateCatalogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_code_table(self, request):
        """修改码表

        修改码表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCodeTable
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateCodeTableRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateCodeTableResponse`
        """
        return self._update_code_table_with_http_info(request)

    def _update_code_table_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/design/code-tables/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateCodeTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_code_table_values(self, request):
        """编辑码表字段值

        编辑码表字段值
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCodeTableValues
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateCodeTableValuesRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateCodeTableValuesResponse`
        """
        return self._update_code_table_values_with_http_info(request)

    def _update_code_table_values_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/design/code-tables/{id}/values',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateCodeTableValuesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_dataconnection(self, request):
        """更新数据连接信息

        更新数据连接信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDataconnection
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateDataconnectionRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateDataconnectionResponse`
        """
        return self._update_dataconnection_with_http_info(request)

    def _update_dataconnection_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/data-connections/{data_connection_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDataconnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_directory(self, request):
        """修改目录

        修改目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDirectory
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateDirectoryRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateDirectoryResponse`
        """
        return self._update_directory_with_http_info(request)

    def _update_directory_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/design/directorys',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDirectoryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_standard(self, request):
        """修改数据标准

        修改数据标准
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateStandard
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateStandardRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateStandardResponse`
        """
        return self._update_standard_with_http_info(request)

    def _update_standard_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/design/standards/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateStandardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_standard_template(self, request):
        """修改数据标准模板

        修改数据标准模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateStandardTemplate
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateStandardTemplateRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateStandardTemplateResponse`
        """
        return self._update_standard_template_with_http_info(request)

    def _update_standard_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/design/standards/templates',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateStandardTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_subject(self, request):
        """修改主题

        修改主题
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSubject
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateSubjectRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateSubjectResponse`
        """
        return self._update_subject_with_http_info(request)

    def _update_subject_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/design/subjects',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateSubjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_subject_new(self, request):
        """修改主题(新)

        修改主题(新)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSubjectNew
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateSubjectNewRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateSubjectNewResponse`
        """
        return self._update_subject_new_with_http_info(request)

    def _update_subject_new_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v3/{project_id}/design/subjects',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateSubjectNewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_table_model(self, request):
        """更新模型实体

        更新一个模型实体，包括逻辑实体或物理数据表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTableModel
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateTableModelRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateTableModelResponse`
        """
        return self._update_table_model_with_http_info(request)

    def _update_table_model_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/design/table-model',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateTableModelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_task_info(self, request):
        """编辑采集任务

        编辑采集任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTaskInfo
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateTaskInfoRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateTaskInfoResponse`
        """
        return self._update_task_info_with_http_info(request)

    def _update_task_info_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/metadata/tasks/{task_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateTaskInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_template(self, request):
        """更新规则模板

        更新规则模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTemplate
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateTemplateRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateTemplateResponse`
        """
        return self._update_template_with_http_info(request)

    def _update_template_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/quality/rule-templates/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_work_space_user_or_group(self, request):
        """编辑工作空间用户或用户组

        编辑工作空间用户或用户组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateWorkSpaceUserOrGroup
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateWorkSpaceUserOrGroupRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateWorkSpaceUserOrGroupResponse`
        """
        return self._update_work_space_user_or_group_with_http_info(request)

    def _update_work_space_user_or_group_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/{workspace_id}/users/{user_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateWorkSpaceUserOrGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_workspace(self, request):
        """更新模型工作区

        更新模型工作区
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateWorkspace
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateWorkspaceRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateWorkspaceResponse`
        """
        return self._update_workspace_with_http_info(request)

    def _update_workspace_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v2/{project_id}/design/workspaces',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateWorkspaceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def authorize_action_api_to_instance(self, request):
        """API授权操作(授权/取消授权/申请/续约)

        API授权操作(授权/取消授权/申请/续约)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AuthorizeActionApiToInstance
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.AuthorizeActionApiToInstanceRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.AuthorizeActionApiToInstanceResponse`
        """
        return self._authorize_action_api_to_instance_with_http_info(request)

    def _authorize_action_api_to_instance_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/service/apis/authorize/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AuthorizeActionApiToInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def authorize_api_to_instance(self, request):
        """批量授权API

        批量授权API
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AuthorizeApiToInstance
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.AuthorizeApiToInstanceRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.AuthorizeApiToInstanceResponse`
        """
        return self._authorize_api_to_instance_with_http_info(request)

    def _authorize_api_to_instance_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/service/apis/{api_id}/instances/{instance_id}/authorize',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AuthorizeApiToInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_api(self, request):
        """创建API

        创建API
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateApi
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.CreateApiRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateApiResponse`
        """
        return self._create_api_with_http_info(request)

    def _create_api_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/service/apis',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateApiResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def debug_api(self, request):
        """调试API

        调试API
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DebugApi
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DebugApiRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DebugApiResponse`
        """
        return self._debug_api_with_http_info(request)

    def _debug_api_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/service/apis/{api_id}/instances/{instance_id}/test',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DebugApiResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_api(self, request):
        """批量删除API

        批量删除API
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApi
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.DeleteApiRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DeleteApiResponse`
        """
        return self._delete_api_with_http_info(request)

    def _delete_api_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/service/apis/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteApiResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_api_to_instance(self, request):
        """API操作(下线/停用/恢复)

        API操作(下线/停用/恢复)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteApiToInstance
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ExecuteApiToInstanceRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ExecuteApiToInstanceResponse`
        """
        return self._execute_api_to_instance_with_http_info(request)

    def _execute_api_to_instance_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/service/apis/{api_id}/instances/{instance_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteApiToInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apis(self, request):
        """查询API列表

        查询API列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApis
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListApisRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListApisResponse`
        """
        return self._list_apis_with_http_info(request)

    def _list_apis_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/apis',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApisResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instance_list(self, request):
        """查看API不同操作对应的实例信息

        查看API不同操作对应的实例信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceList
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ListInstanceListRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ListInstanceListResponse`
        """
        return self._list_instance_list_with_http_info(request)

    def _list_instance_list_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/apis/{api_id}/instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListInstanceListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def publish_api(self, request):
        """发布/下线/停用/恢复API

        发布/下线/停用/恢复API
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PublishApi
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.PublishApiRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.PublishApiResponse`
        """
        return self._publish_api_with_http_info(request)

    def _publish_api_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/service/apis/publish',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='PublishApiResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def publish_api_to_instance(self, request):
        """发布API

        发布API
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PublishApiToInstance
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.PublishApiToInstanceRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.PublishApiToInstanceResponse`
        """
        return self._publish_api_to_instance_with_http_info(request)

    def _publish_api_to_instance_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/service/apis/{api_id}/instances/{instance_id}/publish',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='PublishApiToInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_debug_info(self, request):
        """查看API调试信息

        查看API调试信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchDebugInfo
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchDebugInfoRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchDebugInfoResponse`
        """
        return self._search_debug_info_with_http_info(request)

    def _search_debug_info_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/apis/{api_id}/debug-info',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchDebugInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_publish_info(self, request):
        """查看API发布信息

        查看API发布信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchPublishInfo
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.SearchPublishInfoRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SearchPublishInfoResponse`
        """
        return self._search_publish_info_with_http_info(request)

    def _search_publish_info_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/apis/{api_id}/publish-info',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchPublishInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_api(self, request):
        """查询API信息

        查询API信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApi
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.ShowApiRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowApiResponse`
        """
        return self._show_api_with_http_info(request)

    def _show_api_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service/apis/{api_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowApiResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_api(self, request):
        """更新API

        更新API
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateApi
        :type request: :class:`huaweicloudsdkdataartsstudio.v1.UpdateApiRequest`
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.UpdateApiResponse`
        """
        return self._update_api_with_http_info(request)

    def _update_api_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/service/apis/{api_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateApiResponse',
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
