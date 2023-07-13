# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class SFSTurboClient(Client):
    def __init__(self):
        super(SFSTurboClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdksfsturbo.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "SFSTurboClient":
            raise TypeError("client type error, support client type is SFSTurboClient")

        return ClientBuilder(clazz)

    def batch_add_shared_tags(self, request):
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
        return self._batch_add_shared_tags_with_http_info(request)

    def _batch_add_shared_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

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
            resource_path='/v1/{project_id}/sfs-turbo/{share_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchAddSharedTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_security_group(self, request):
        """修改文件系统绑定的安全组

        修改SFS Turbo文件系统绑定的安全组。修改安全组为异步任务，可以通过“查询单个文件系统”返回的子状态字段“sub_status”来判断是否修改安全组状态，子状态为“232”即为修改安全组成功。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeSecurityGroup
        :type request: :class:`huaweicloudsdksfsturbo.v1.ChangeSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ChangeSecurityGroupResponse`
        """
        return self._change_security_group_with_http_info(request)

    def _change_security_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

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
            resource_path='/v1/{project_id}/sfs-turbo/shares/{share_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeSecurityGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_share_name(self, request):
        """修改文件系统名称

        修改文件系统名称
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeShareName
        :type request: :class:`huaweicloudsdksfsturbo.v1.ChangeShareNameRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ChangeShareNameResponse`
        """
        return self._change_share_name_with_http_info(request)

    def _change_share_name_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

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
            resource_path='/v1/{project_id}/sfs-turbo/shares/{share_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeShareNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_fs_dir(self, request):
        """创建目录

        创建目录 (目前已上线的局点：上海一、上海二、北京二、北京四、乌兰察布一、广州、贵阳一、中国-香港、亚太-新加坡、亚太-曼谷)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFsDir
        :type request: :class:`huaweicloudsdksfsturbo.v1.CreateFsDirRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.CreateFsDirResponse`
        """
        return self._create_fs_dir_with_http_info(request)

    def _create_fs_dir_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

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
            resource_path='/v1/{project_id}/sfs-turbo/shares/{share_id}/fs/dir',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateFsDirResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_fs_dir_quota(self, request):
        """创建目标文件夹quota

        创建目标文件夹quota。只支持对空目录设置目录quota (目前已上线的局点：上海一、上海二、北京二、北京四、乌兰察布一、广州、贵阳一、中国-香港、亚太-新加坡、亚太-曼谷)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFsDirQuota
        :type request: :class:`huaweicloudsdksfsturbo.v1.CreateFsDirQuotaRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.CreateFsDirQuotaResponse`
        """
        return self._create_fs_dir_quota_with_http_info(request)

    def _create_fs_dir_quota_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

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
            resource_path='/v1/{project_id}/sfs-turbo/shares/{share_id}/fs/dir-quota',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateFsDirQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_share(self, request):
        """创建文件系统

        创建文件系统。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateShare
        :type request: :class:`huaweicloudsdksfsturbo.v1.CreateShareRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.CreateShareResponse`
        """
        return self._create_share_with_http_info(request)

    def _create_share_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/sfs-turbo/shares',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateShareResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_shared_tag(self, request):
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
        return self._create_shared_tag_with_http_info(request)

    def _create_shared_tag_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

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
            resource_path='/v1/{project_id}/sfs-turbo/{share_id}/tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSharedTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_fs_dir(self, request):
        """删除文件系统目录

        删除文件系统目录 (目前已上线的局点：上海一、上海二、北京二、北京四、乌兰察布一、广州、贵阳一、中国-香港、亚太-新加坡、亚太-曼谷)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteFsDir
        :type request: :class:`huaweicloudsdksfsturbo.v1.DeleteFsDirRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.DeleteFsDirResponse`
        """
        return self._delete_fs_dir_with_http_info(request)

    def _delete_fs_dir_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

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
            resource_path='/v1/{project_id}/sfs-turbo/shares/{share_id}/fs/dir',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteFsDirResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_fs_dir_quota(self, request):
        """删除目标文件夹quota

        删除目标文件夹quota。只支持对空目录进行删除quota (目前已上线的局点：上海一、上海二、北京二、北京四、乌兰察布一、广州、贵阳一、中国-香港、亚太-新加坡、亚太-曼谷)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteFsDirQuota
        :type request: :class:`huaweicloudsdksfsturbo.v1.DeleteFsDirQuotaRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.DeleteFsDirQuotaResponse`
        """
        return self._delete_fs_dir_quota_with_http_info(request)

    def _delete_fs_dir_quota_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

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
            resource_path='/v1/{project_id}/sfs-turbo/shares/{share_id}/fs/dir-quota',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteFsDirQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_share(self, request):
        """删除文件系统

        删除文件系统。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteShare
        :type request: :class:`huaweicloudsdksfsturbo.v1.DeleteShareRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.DeleteShareResponse`
        """
        return self._delete_share_with_http_info(request)

    def _delete_share_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

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
            resource_path='/v1/{project_id}/sfs-turbo/shares/{share_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteShareResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_shared_tag(self, request):
        """删除共享标签

        指定共享删除一个标签。当共享中不存在指定要删除的key时，接口调用将会返回404错误。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSharedTag
        :type request: :class:`huaweicloudsdksfsturbo.v1.DeleteSharedTagRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.DeleteSharedTagResponse`
        """
        return self._delete_shared_tag_with_http_info(request)

    def _delete_shared_tag_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/sfs-turbo/{share_id}/tags/{key}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSharedTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def expand_share(self, request):
        """扩容文件系统

        扩容文件系统。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExpandShare
        :type request: :class:`huaweicloudsdksfsturbo.v1.ExpandShareRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ExpandShareResponse`
        """
        return self._expand_share_with_http_info(request)

    def _expand_share_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

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
            resource_path='/v1/{project_id}/sfs-turbo/shares/{share_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExpandShareResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_shared_tags(self, request):
        """查询租户所有共享的标签

        查询租户所有共享的标签集合。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSharedTags
        :type request: :class:`huaweicloudsdksfsturbo.v1.ListSharedTagsRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ListSharedTagsResponse`
        """
        return self._list_shared_tags_with_http_info(request)

    def _list_shared_tags_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/sfs-turbo/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSharedTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_shares(self, request):
        """获取文件系统列表

        获取文件系统列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListShares
        :type request: :class:`huaweicloudsdksfsturbo.v1.ListSharesRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ListSharesResponse`
        """
        return self._list_shares_with_http_info(request)

    def _list_shares_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/sfs-turbo/shares/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSharesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_fs_dir(self, request):
        """查询目录是否存在

        查询目录是否存在 (目前已上线的局点：上海一、上海二、北京二、北京四、乌兰察布一、广州、贵阳一、中国-香港、亚太-新加坡、亚太-曼谷)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFsDir
        :type request: :class:`huaweicloudsdksfsturbo.v1.ShowFsDirRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ShowFsDirResponse`
        """
        return self._show_fs_dir_with_http_info(request)

    def _show_fs_dir_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/sfs-turbo/shares/{share_id}/fs/dir',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowFsDirResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_fs_dir_quota(self, request):
        """查询目标文件夹quota

        查询目标文件夹quota (目前已上线的局点：上海一、上海二、北京二、北京四、乌兰察布一、广州、贵阳一、中国-香港、亚太-新加坡、亚太-曼谷)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFsDirQuota
        :type request: :class:`huaweicloudsdksfsturbo.v1.ShowFsDirQuotaRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ShowFsDirQuotaResponse`
        """
        return self._show_fs_dir_quota_with_http_info(request)

    def _show_fs_dir_quota_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/sfs-turbo/shares/{share_id}/fs/dir-quota',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowFsDirQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_share(self, request):
        """查询文件系统详细信息

        查询SFS Turbo文件系统详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowShare
        :type request: :class:`huaweicloudsdksfsturbo.v1.ShowShareRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ShowShareResponse`
        """
        return self._show_share_with_http_info(request)

    def _show_share_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

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
            resource_path='/v1/{project_id}/sfs-turbo/shares/{share_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowShareResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_shared_tags(self, request):
        """查询共享标签

        查询指定共享的所有标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSharedTags
        :type request: :class:`huaweicloudsdksfsturbo.v1.ShowSharedTagsRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ShowSharedTagsResponse`
        """
        return self._show_shared_tags_with_http_info(request)

    def _show_shared_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

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
            resource_path='/v1/{project_id}/sfs-turbo/{share_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSharedTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_fs_dir_quota(self, request):
        """更新目标文件夹quota

        更新目标文件夹quota (目前已上线的局点：上海一、上海二、北京二、北京四、乌兰察布一、广州、贵阳一、中国-香港、亚太-新加坡、亚太-曼谷)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateFsDirQuota
        :type request: :class:`huaweicloudsdksfsturbo.v1.UpdateFsDirQuotaRequest`
        :rtype: :class:`huaweicloudsdksfsturbo.v1.UpdateFsDirQuotaResponse`
        """
        return self._update_fs_dir_quota_with_http_info(request)

    def _update_fs_dir_quota_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'share_id' in local_var_params:
            path_params['share_id'] = local_var_params['share_id']

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
            resource_path='/v1/{project_id}/sfs-turbo/shares/{share_id}/fs/dir-quota',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateFsDirQuotaResponse',
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
