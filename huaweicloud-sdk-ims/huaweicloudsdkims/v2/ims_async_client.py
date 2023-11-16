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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkims'")


class ImsAsyncClient(Client):
    def __init__(self):
        super(ImsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkims.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "ImsAsyncClient":
                raise TypeError("client type error, support client type is ImsAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_image_tag_async(self, request):
        """添加镜像标签

        该接口用于为指定镜像添加或更新指定的单个标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddImageTag
        :type request: :class:`huaweicloudsdkims.v2.AddImageTagRequest`
        :rtype: :class:`huaweicloudsdkims.v2.AddImageTagResponse`
        """
        http_info = self._add_image_tag_http_info(request)
        return self._call_api(**http_info)

    def add_image_tag_async_invoker(self, request):
        http_info = self._add_image_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_image_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/images/{image_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "AddImageTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def batch_add_members_async(self, request):
        """批量添加镜像成员

        该接口为扩展接口，主要用于镜像共享时用户将多个镜像共享给多个用户。
        该接口为异步接口，返回job_id说明任务下发成功，查询异步任务状态，如果是success说明任务执行成功，如果是failed说明任务执行失败。如何查询异步任务，请参见异步任务查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAddMembers
        :type request: :class:`huaweicloudsdkims.v2.BatchAddMembersRequest`
        :rtype: :class:`huaweicloudsdkims.v2.BatchAddMembersResponse`
        """
        http_info = self._batch_add_members_http_info(request)
        return self._call_api(**http_info)

    def batch_add_members_async_invoker(self, request):
        http_info = self._batch_add_members_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_add_members_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/cloudimages/members",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAddMembersResponse"
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

    def batch_add_or_delete_tags_async(self, request):
        """批量添加删除镜像标签

        该接口用于为指定镜像批量添加/更新、删除标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAddOrDeleteTags
        :type request: :class:`huaweicloudsdkims.v2.BatchAddOrDeleteTagsRequest`
        :rtype: :class:`huaweicloudsdkims.v2.BatchAddOrDeleteTagsResponse`
        """
        http_info = self._batch_add_or_delete_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_add_or_delete_tags_async_invoker(self, request):
        http_info = self._batch_add_or_delete_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_add_or_delete_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/images/{image_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAddOrDeleteTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def batch_delete_members_async(self, request):
        """批量删除镜像成员

        该接口为扩展接口，主要用于取消镜像共享。
        该接口为异步接口，返回job_id说明任务下发成功，查询异步任务状态，如果是success说明任务执行成功，如果是failed说明任务执行失败。如何查询异步任务，请参见异步任务查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteMembers
        :type request: :class:`huaweicloudsdkims.v2.BatchDeleteMembersRequest`
        :rtype: :class:`huaweicloudsdkims.v2.BatchDeleteMembersResponse`
        """
        http_info = self._batch_delete_members_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_members_async_invoker(self, request):
        http_info = self._batch_delete_members_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_members_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/cloudimages/members",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteMembersResponse"
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

    def batch_update_members_async(self, request):
        """批量更新镜像成员状态

        该接口为扩展接口，主要用于用户接受或者拒绝多个共享镜像时批量更新镜像成员的状态。
        该接口为异步接口，返回job_id说明任务下发成功，查询异步任务状态，如果是success说明任务执行成功，如果是failed说明任务执行失败。如何查询异步任务，请参见异步任务查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchUpdateMembers
        :type request: :class:`huaweicloudsdkims.v2.BatchUpdateMembersRequest`
        :rtype: :class:`huaweicloudsdkims.v2.BatchUpdateMembersResponse`
        """
        http_info = self._batch_update_members_http_info(request)
        return self._call_api(**http_info)

    def batch_update_members_async_invoker(self, request):
        http_info = self._batch_update_members_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_update_members_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/cloudimages/members",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateMembersResponse"
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

    def copy_image_cross_region_async(self, request):
        """跨Region复制镜像

        该接口为扩展接口，用户在一个区域制作的私有镜像，可以通过跨Region复制镜像将镜像复制到其他区域，在其他区域发放相同类型的云服务器，帮助用户实现区域间的业务迁移。
        该接口为异步接口，返回job_id说明任务下发成功，查询异步任务状态，如果是success说明任务执行成功，如果是failed说明任务执行失败。
        如何查询异步任务，请参见异步任务进度查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CopyImageCrossRegion
        :type request: :class:`huaweicloudsdkims.v2.CopyImageCrossRegionRequest`
        :rtype: :class:`huaweicloudsdkims.v2.CopyImageCrossRegionResponse`
        """
        http_info = self._copy_image_cross_region_http_info(request)
        return self._call_api(**http_info)

    def copy_image_cross_region_async_invoker(self, request):
        http_info = self._copy_image_cross_region_http_info(request)
        return AsyncInvoker(self, http_info)

    def _copy_image_cross_region_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/cloudimages/{image_id}/cross_region_copy",
            "request_type": request.__class__.__name__,
            "response_type": "CopyImageCrossRegionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def copy_image_in_region_async(self, request):
        """Region内复制镜像

        该接口为扩展接口，主要用于用户将一个已有镜像复制为另一个镜像。复制镜像时，可以更改镜像的加密等属性，以满足不同的场景。
        该接口为异步接口，返回job_id说明任务下发成功，查询异步任务状态，如果是success说明任务执行成功，如果是failed说明任务执行失败。如何查询异步任务，请参见异步任务查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CopyImageInRegion
        :type request: :class:`huaweicloudsdkims.v2.CopyImageInRegionRequest`
        :rtype: :class:`huaweicloudsdkims.v2.CopyImageInRegionResponse`
        """
        http_info = self._copy_image_in_region_http_info(request)
        return self._call_api(**http_info)

    def copy_image_in_region_async_invoker(self, request):
        http_info = self._copy_image_in_region_http_info(request)
        return AsyncInvoker(self, http_info)

    def _copy_image_in_region_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/cloudimages/{image_id}/copy",
            "request_type": request.__class__.__name__,
            "response_type": "CopyImageInRegionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def create_data_image_async(self, request):
        """使用外部镜像文件制作数据镜像

        使用上传至OBS桶中的外部数据卷镜像文件制作数据镜像。作为异步接口，调用成功，只是说明后台收到了制作请求，镜像是否制作成功需要通过异步任务查询接口查询该任务的执行状态。具体请参考异步任务查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDataImage
        :type request: :class:`huaweicloudsdkims.v2.CreateDataImageRequest`
        :rtype: :class:`huaweicloudsdkims.v2.CreateDataImageResponse`
        """
        http_info = self._create_data_image_http_info(request)
        return self._call_api(**http_info)

    def create_data_image_async_invoker(self, request):
        http_info = self._create_data_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_data_image_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/cloudimages/dataimages/action",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDataImageResponse"
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

    def create_image_async(self, request):
        """制作镜像

        本接口用于制作私有镜像，支持：
        - 使用云服务器制作私有镜像。
        - 使用上传至OBS桶中的外部镜像文件制作私有镜像。
        - 使用数据卷制作系统盘镜像。
        
        作为异步接口，调用成功，只是说明云平台收到了制作请求，镜像是否制作成功需要通过异步任务查询接口查询该任务的执行状态，具体请参考异步任务查询。
        
        不同场景必选参数说明：
        
        - 使用云服务器制作镜像时的请求的必选参数：name,instance_id。
        - 使用上传至OBS桶中的外部镜像文件时的请求必选参数：name,image_url,min_disk。
        - 使用数据卷制作系统盘镜像时的请求必选参数：name,volume_id,os_version
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateImage
        :type request: :class:`huaweicloudsdkims.v2.CreateImageRequest`
        :rtype: :class:`huaweicloudsdkims.v2.CreateImageResponse`
        """
        http_info = self._create_image_http_info(request)
        return self._call_api(**http_info)

    def create_image_async_invoker(self, request):
        http_info = self._create_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_image_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/cloudimages/action",
            "request_type": request.__class__.__name__,
            "response_type": "CreateImageResponse"
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

    def create_or_update_tags_async(self, request):
        """增加或修改标签

        该接口主要用于为某个镜像增加或修改一个自定义标签。通过自定义标签，用户可以将镜像进行分类。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateOrUpdateTags
        :type request: :class:`huaweicloudsdkims.v2.CreateOrUpdateTagsRequest`
        :rtype: :class:`huaweicloudsdkims.v2.CreateOrUpdateTagsResponse`
        """
        http_info = self._create_or_update_tags_http_info(request)
        return self._call_api(**http_info)

    def create_or_update_tags_async_invoker(self, request):
        http_info = self._create_or_update_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_or_update_tags_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/cloudimages/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOrUpdateTagsResponse"
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

    def create_whole_image_async(self, request):
        """制作整机镜像

        使用云服务器或者云服务器备份制作整机镜像。作为异步接口，调用成功，只是说明后台收到了制作整机镜像的请求，镜像是否制作成功需要通过异步任务查询接口查询该任务的执行状态，具体请参考异步任务查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWholeImage
        :type request: :class:`huaweicloudsdkims.v2.CreateWholeImageRequest`
        :rtype: :class:`huaweicloudsdkims.v2.CreateWholeImageResponse`
        """
        http_info = self._create_whole_image_http_info(request)
        return self._call_api(**http_info)

    def create_whole_image_async_invoker(self, request):
        http_info = self._create_whole_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_whole_image_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/cloudimages/wholeimages/action",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWholeImageResponse"
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

    def delete_image_tag_async(self, request):
        """删除镜像标签

        该接口用于为镜像删除指定的标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteImageTag
        :type request: :class:`huaweicloudsdkims.v2.DeleteImageTagRequest`
        :rtype: :class:`huaweicloudsdkims.v2.DeleteImageTagResponse`
        """
        http_info = self._delete_image_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_image_tag_async_invoker(self, request):
        http_info = self._delete_image_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_image_tag_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/images/{image_id}/tags/{key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteImageTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']
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

    def export_image_async(self, request):
        """导出镜像

        该接口为扩展接口，用于用户将自己的私有镜像导出到指定的OBS桶中。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportImage
        :type request: :class:`huaweicloudsdkims.v2.ExportImageRequest`
        :rtype: :class:`huaweicloudsdkims.v2.ExportImageResponse`
        """
        http_info = self._export_image_http_info(request)
        return self._call_api(**http_info)

    def export_image_async_invoker(self, request):
        http_info = self._export_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _export_image_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/cloudimages/{image_id}/file",
            "request_type": request.__class__.__name__,
            "response_type": "ExportImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def import_image_quick_async(self, request):
        """镜像文件快速导入

        使用上传至OBS桶中的超大外部镜像文件制作私有镜像，目前仅支持RAW或ZVHD2格式镜像文件。且要求镜像文件大小不能超过1TB。
        由于快速导入功能要求提前转换镜像文件格式为RAW或ZVHD2格式，因此镜像文件小于128GB时推荐您优先使用常规的创建私有镜像的方式。
        作为异步接口，调用成功，只是说明后台收到了制作请求，镜像是否制作成功需要通过异步任务查询接口查询该任务的执行状态，具体请参考异步任务查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportImageQuick
        :type request: :class:`huaweicloudsdkims.v2.ImportImageQuickRequest`
        :rtype: :class:`huaweicloudsdkims.v2.ImportImageQuickResponse`
        """
        http_info = self._import_image_quick_http_info(request)
        return self._call_api(**http_info)

    def import_image_quick_async_invoker(self, request):
        http_info = self._import_image_quick_http_info(request)
        return AsyncInvoker(self, http_info)

    def _import_image_quick_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/cloudimages/quickimport/action",
            "request_type": request.__class__.__name__,
            "response_type": "ImportImageQuickResponse"
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

    def list_image_by_tags_async(self, request):
        """按标签查询镜像

        该接口用于按标签或其他条件对镜像进行过滤或者计数使用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListImageByTags
        :type request: :class:`huaweicloudsdkims.v2.ListImageByTagsRequest`
        :rtype: :class:`huaweicloudsdkims.v2.ListImageByTagsResponse`
        """
        http_info = self._list_image_by_tags_http_info(request)
        return self._call_api(**http_info)

    def list_image_by_tags_async_invoker(self, request):
        http_info = self._list_image_by_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_image_by_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/images/resource_instances/action",
            "request_type": request.__class__.__name__,
            "response_type": "ListImageByTagsResponse"
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

    def list_image_tags_async(self, request):
        """查询镜像标签

        该接口用于为查询指定镜像上的所有标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListImageTags
        :type request: :class:`huaweicloudsdkims.v2.ListImageTagsRequest`
        :rtype: :class:`huaweicloudsdkims.v2.ListImageTagsResponse`
        """
        http_info = self._list_image_tags_http_info(request)
        return self._call_api(**http_info)

    def list_image_tags_async_invoker(self, request):
        http_info = self._list_image_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_image_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/images/{image_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListImageTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def list_images_async(self, request):
        """查询镜像列表

        根据不同条件查询镜像列表信息。
        可以在URI后面用‘?’和‘&amp;’添加不同的查询条件组合，请参考请求样例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListImages
        :type request: :class:`huaweicloudsdkims.v2.ListImagesRequest`
        :rtype: :class:`huaweicloudsdkims.v2.ListImagesResponse`
        """
        http_info = self._list_images_http_info(request)
        return self._call_api(**http_info)

    def list_images_async_invoker(self, request):
        http_info = self._list_images_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_images_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/cloudimages",
            "request_type": request.__class__.__name__,
            "response_type": "ListImagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'imagetype' in local_var_params:
            query_params.append(('__imagetype', local_var_params['imagetype']))
        if 'isregistered' in local_var_params:
            query_params.append(('__isregistered', local_var_params['isregistered']))
        if 'os_bit' in local_var_params:
            query_params.append(('__os_bit', local_var_params['os_bit']))
        if 'os_type' in local_var_params:
            query_params.append(('__os_type', local_var_params['os_type']))
        if 'platform' in local_var_params:
            query_params.append(('__platform', local_var_params['platform']))
        if 'support_diskintensive' in local_var_params:
            query_params.append(('__support_diskintensive', local_var_params['support_diskintensive']))
        if 'support_highperformance' in local_var_params:
            query_params.append(('__support_highperformance', local_var_params['support_highperformance']))
        if 'support_kvm' in local_var_params:
            query_params.append(('__support_kvm', local_var_params['support_kvm']))
        if 'support_kvm_gpu_type' in local_var_params:
            query_params.append(('__support_kvm_gpu_type', local_var_params['support_kvm_gpu_type']))
        if 'support_kvm_infiniband' in local_var_params:
            query_params.append(('__support_kvm_infiniband', local_var_params['support_kvm_infiniband']))
        if 'support_largememory' in local_var_params:
            query_params.append(('__support_largememory', local_var_params['support_largememory']))
        if 'support_xen' in local_var_params:
            query_params.append(('__support_xen', local_var_params['support_xen']))
        if 'support_xen_gpu_type' in local_var_params:
            query_params.append(('__support_xen_gpu_type', local_var_params['support_xen_gpu_type']))
        if 'support_xen_hana' in local_var_params:
            query_params.append(('__support_xen_hana', local_var_params['support_xen_hana']))
        if 'container_format' in local_var_params:
            query_params.append(('container_format', local_var_params['container_format']))
        if 'disk_format' in local_var_params:
            query_params.append(('disk_format', local_var_params['disk_format']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'member_status' in local_var_params:
            query_params.append(('member_status', local_var_params['member_status']))
        if 'min_disk' in local_var_params:
            query_params.append(('min_disk', local_var_params['min_disk']))
        if 'min_ram' in local_var_params:
            query_params.append(('min_ram', local_var_params['min_ram']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'owner' in local_var_params:
            query_params.append(('owner', local_var_params['owner']))
        if 'protected' in local_var_params:
            query_params.append(('protected', local_var_params['protected']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))
        if 'virtual_env_type' in local_var_params:
            query_params.append(('virtual_env_type', local_var_params['virtual_env_type']))
        if 'visibility' in local_var_params:
            query_params.append(('visibility', local_var_params['visibility']))
        if 'flavor_id' in local_var_params:
            query_params.append(('flavor_id', local_var_params['flavor_id']))
        if 'created_at' in local_var_params:
            query_params.append(('created_at', local_var_params['created_at']))
        if 'updated_at' in local_var_params:
            query_params.append(('updated_at', local_var_params['updated_at']))
        if 'architecture' in local_var_params:
            query_params.append(('architecture', local_var_params['architecture']))

        header_params = {}
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_images_tags_async(self, request):
        """查询租户所有镜像标签

        该接口用于为查询租户的所有镜像上的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListImagesTags
        :type request: :class:`huaweicloudsdkims.v2.ListImagesTagsRequest`
        :rtype: :class:`huaweicloudsdkims.v2.ListImagesTagsResponse`
        """
        http_info = self._list_images_tags_http_info(request)
        return self._call_api(**http_info)

    def list_images_tags_async_invoker(self, request):
        http_info = self._list_images_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_images_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/images/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListImagesTagsResponse"
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

    def list_os_versions_async(self, request):
        """查询镜像支持的OS列表

        查询当前区域弹性云服务器的OS兼容性列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOsVersions
        :type request: :class:`huaweicloudsdkims.v2.ListOsVersionsRequest`
        :rtype: :class:`huaweicloudsdkims.v2.ListOsVersionsResponse`
        """
        http_info = self._list_os_versions_http_info(request)
        return self._call_api(**http_info)

    def list_os_versions_async_invoker(self, request):
        http_info = self._list_os_versions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_os_versions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/cloudimages/os_version",
            "request_type": request.__class__.__name__,
            "response_type": "ListOsVersionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_tags_async(self, request):
        """按条件查询租户镜像标签列表

        根据不同条件查询镜像标签列表信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTags
        :type request: :class:`huaweicloudsdkims.v2.ListTagsRequest`
        :rtype: :class:`huaweicloudsdkims.v2.ListTagsResponse`
        """
        http_info = self._list_tags_http_info(request)
        return self._call_api(**http_info)

    def list_tags_async_invoker(self, request):
        http_info = self._list_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/cloudimages/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'imagetype' in local_var_params:
            query_params.append(('__imagetype', local_var_params['imagetype']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'min_disk' in local_var_params:
            query_params.append(('min_disk', local_var_params['min_disk']))
        if 'platform' in local_var_params:
            query_params.append(('__platform', local_var_params['platform']))
        if 'os_type' in local_var_params:
            query_params.append(('__os_type', local_var_params['os_type']))
        if 'member_status' in local_var_params:
            query_params.append(('member_status', local_var_params['member_status']))
        if 'virtual_env_type' in local_var_params:
            query_params.append(('virtual_env_type', local_var_params['virtual_env_type']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'architecture' in local_var_params:
            query_params.append(('architecture', local_var_params['architecture']))
        if 'created_at' in local_var_params:
            query_params.append(('created_at', local_var_params['created_at']))
        if 'updated_at' in local_var_params:
            query_params.append(('updated_at', local_var_params['updated_at']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def register_image_async(self, request):
        """注册镜像

        该接口用于将镜像文件注册为云平台未初始化的私有镜像。
        使用该接口注册镜像的具体步骤如下：
        将镜像文件上传到OBS个人桶中。具体操作请参见《对象存储服务客户端指南（OBS Browser）》或《对象存储服务API参考》。
        使用创建镜像元数据接口创建镜像元数据。调用成功后，保存该镜像的ID。创建镜像元数据请参考创建镜像元数据（OpenStack原生）。
        根据2得到的镜像ID，使用注册镜像接口注册OBS桶中的镜像文件。
        注册镜像接口作为异步接口，调用成功后，说明后台收到了注册请求。需要根据镜像ID查询该镜像状态验证镜像注册是否成功。当镜像状态变为“active”时，表示镜像注册成功。
        如何查询异步任务，请参见异步任务查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RegisterImage
        :type request: :class:`huaweicloudsdkims.v2.RegisterImageRequest`
        :rtype: :class:`huaweicloudsdkims.v2.RegisterImageResponse`
        """
        http_info = self._register_image_http_info(request)
        return self._call_api(**http_info)

    def register_image_async_invoker(self, request):
        http_info = self._register_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _register_image_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/cloudimages/{image_id}/upload",
            "request_type": request.__class__.__name__,
            "response_type": "RegisterImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def show_image_quota_async(self, request):
        """查询镜像配额

        该接口为扩展接口，主要用于查询租户在当前Region的私有镜像的配额数量。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowImageQuota
        :type request: :class:`huaweicloudsdkims.v2.ShowImageQuotaRequest`
        :rtype: :class:`huaweicloudsdkims.v2.ShowImageQuotaResponse`
        """
        http_info = self._show_image_quota_http_info(request)
        return self._call_api(**http_info)

    def show_image_quota_async_invoker(self, request):
        http_info = self._show_image_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_image_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/cloudimages/quota",
            "request_type": request.__class__.__name__,
            "response_type": "ShowImageQuotaResponse"
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

    def show_job_async(self, request):
        """查询job状态

        该接口为扩展接口，主要用于查询异步接口执行情况，比如查询导出镜像任务的执行状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJob
        :type request: :class:`huaweicloudsdkims.v2.ShowJobRequest`
        :rtype: :class:`huaweicloudsdkims.v2.ShowJobResponse`
        """
        http_info = self._show_job_http_info(request)
        return self._call_api(**http_info)

    def show_job_async_invoker(self, request):
        http_info = self._show_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobResponse"
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

    def show_job_progress_async(self, request):
        """异步任务进度查询

        该接口为扩展接口，主要用于查询异步任务进度。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobProgress
        :type request: :class:`huaweicloudsdkims.v2.ShowJobProgressRequest`
        :rtype: :class:`huaweicloudsdkims.v2.ShowJobProgressResponse`
        """
        http_info = self._show_job_progress_http_info(request)
        return self._call_api(**http_info)

    def show_job_progress_async_invoker(self, request):
        http_info = self._show_job_progress_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_progress_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/cloudimages/job/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobProgressResponse"
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

    def update_image_async(self, request):
        """更新镜像信息

        更新镜像信息接口，主要用于镜像属性的修改。当前仅支持可用（active）状态的镜像更新相关信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateImage
        :type request: :class:`huaweicloudsdkims.v2.UpdateImageRequest`
        :rtype: :class:`huaweicloudsdkims.v2.UpdateImageResponse`
        """
        http_info = self._update_image_http_info(request)
        return self._call_api(**http_info)

    def update_image_async_invoker(self, request):
        http_info = self._update_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_image_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v2/cloudimages/{image_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def list_versions_async(self, request):
        """查询版本列表（OpenStack原生）

        查询API的版本信息列表，包括API的版本兼容性、域名信息等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVersions
        :type request: :class:`huaweicloudsdkims.v2.ListVersionsRequest`
        :rtype: :class:`huaweicloudsdkims.v2.ListVersionsResponse`
        """
        http_info = self._list_versions_http_info(request)
        return self._call_api(**http_info)

    def list_versions_async_invoker(self, request):
        http_info = self._list_versions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_versions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/",
            "request_type": request.__class__.__name__,
            "response_type": "ListVersionsResponse"
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

    def show_version_async(self, request):
        """查询版本列表（OpenStack原生）

        查询API的版本信息列表，包括API的版本兼容性、域名信息等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVersion
        :type request: :class:`huaweicloudsdkims.v2.ShowVersionRequest`
        :rtype: :class:`huaweicloudsdkims.v2.ShowVersionResponse`
        """
        http_info = self._show_version_http_info(request)
        return self._call_api(**http_info)

    def show_version_async_invoker(self, request):
        http_info = self._show_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_version_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/{version}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def glance_add_image_member_async(self, request):
        """添加镜像成员（OpenStack原生）

        用户共享镜像给其他用户时，使用该接口向该镜像成员中添加接受镜像用户的项目ID。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GlanceAddImageMember
        :type request: :class:`huaweicloudsdkims.v2.GlanceAddImageMemberRequest`
        :rtype: :class:`huaweicloudsdkims.v2.GlanceAddImageMemberResponse`
        """
        http_info = self._glance_add_image_member_http_info(request)
        return self._call_api(**http_info)

    def glance_add_image_member_async_invoker(self, request):
        http_info = self._glance_add_image_member_http_info(request)
        return AsyncInvoker(self, http_info)

    def _glance_add_image_member_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/images/{image_id}/members",
            "request_type": request.__class__.__name__,
            "response_type": "GlanceAddImageMemberResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def glance_create_image_metadata_async(self, request):
        """创建镜像元数据（OpenStack原生）

        创建镜像元数据。调用创建镜像元数据接口成功后，只是创建了镜像的元数据，镜像对应的实际镜像文件并不存在
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GlanceCreateImageMetadata
        :type request: :class:`huaweicloudsdkims.v2.GlanceCreateImageMetadataRequest`
        :rtype: :class:`huaweicloudsdkims.v2.GlanceCreateImageMetadataResponse`
        """
        http_info = self._glance_create_image_metadata_http_info(request)
        return self._call_api(**http_info)

    def glance_create_image_metadata_async_invoker(self, request):
        http_info = self._glance_create_image_metadata_http_info(request)
        return AsyncInvoker(self, http_info)

    def _glance_create_image_metadata_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/images",
            "request_type": request.__class__.__name__,
            "response_type": "GlanceCreateImageMetadataResponse"
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

    def glance_create_tag_async(self, request):
        """增加标签（OpenStack原生）

        该接口主要用于为某个镜像添加一个自定义标签。通过自定义标签，用户可以将镜像进行分类。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GlanceCreateTag
        :type request: :class:`huaweicloudsdkims.v2.GlanceCreateTagRequest`
        :rtype: :class:`huaweicloudsdkims.v2.GlanceCreateTagResponse`
        """
        http_info = self._glance_create_tag_http_info(request)
        return self._call_api(**http_info)

    def glance_create_tag_async_invoker(self, request):
        http_info = self._glance_create_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _glance_create_tag_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/images/{image_id}/tags/{tag}",
            "request_type": request.__class__.__name__,
            "response_type": "GlanceCreateTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def glance_delete_image_async(self, request):
        """删除镜像（OpenStack原生）

        该接口主要用于删除镜像，用户可以通过该接口将自己的私有镜像删除。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GlanceDeleteImage
        :type request: :class:`huaweicloudsdkims.v2.GlanceDeleteImageRequest`
        :rtype: :class:`huaweicloudsdkims.v2.GlanceDeleteImageResponse`
        """
        http_info = self._glance_delete_image_http_info(request)
        return self._call_api(**http_info)

    def glance_delete_image_async_invoker(self, request):
        http_info = self._glance_delete_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _glance_delete_image_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/images/{image_id}",
            "request_type": request.__class__.__name__,
            "response_type": "GlanceDeleteImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def glance_delete_image_member_async(self, request):
        """删除指定的镜像成员（OpenStack原生）

        该接口用于取消对某个用户的镜像共享。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GlanceDeleteImageMember
        :type request: :class:`huaweicloudsdkims.v2.GlanceDeleteImageMemberRequest`
        :rtype: :class:`huaweicloudsdkims.v2.GlanceDeleteImageMemberResponse`
        """
        http_info = self._glance_delete_image_member_http_info(request)
        return self._call_api(**http_info)

    def glance_delete_image_member_async_invoker(self, request):
        http_info = self._glance_delete_image_member_http_info(request)
        return AsyncInvoker(self, http_info)

    def _glance_delete_image_member_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/images/{image_id}/members/{member_id}",
            "request_type": request.__class__.__name__,
            "response_type": "GlanceDeleteImageMemberResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']
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

    def glance_delete_tag_async(self, request):
        """删除标签（OpenStack原生）

        该接口主要用于删除某个镜像的自定义标签，通过该接口，用户可以将私有镜像中一些不用的标签删除。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GlanceDeleteTag
        :type request: :class:`huaweicloudsdkims.v2.GlanceDeleteTagRequest`
        :rtype: :class:`huaweicloudsdkims.v2.GlanceDeleteTagResponse`
        """
        http_info = self._glance_delete_tag_http_info(request)
        return self._call_api(**http_info)

    def glance_delete_tag_async_invoker(self, request):
        http_info = self._glance_delete_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _glance_delete_tag_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/images/{image_id}/tags/{tag}",
            "request_type": request.__class__.__name__,
            "response_type": "GlanceDeleteTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def glance_list_image_member_schemas_async(self, request):
        """查询镜像成员列表视图（OpenStack原生）

        该接口主要用于查询镜像成员列表视图，通过视图，用户可以了解到镜像成员包含哪些属性，同时也可以了解每个属性的数据类型。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GlanceListImageMemberSchemas
        :type request: :class:`huaweicloudsdkims.v2.GlanceListImageMemberSchemasRequest`
        :rtype: :class:`huaweicloudsdkims.v2.GlanceListImageMemberSchemasResponse`
        """
        http_info = self._glance_list_image_member_schemas_http_info(request)
        return self._call_api(**http_info)

    def glance_list_image_member_schemas_async_invoker(self, request):
        http_info = self._glance_list_image_member_schemas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _glance_list_image_member_schemas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/schemas/members",
            "request_type": request.__class__.__name__,
            "response_type": "GlanceListImageMemberSchemasResponse"
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

    def glance_list_image_members_async(self, request):
        """获取镜像成员列表（OpenStack原生）

        该接口用于共享镜像过程中，获取接受该镜像的成员列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GlanceListImageMembers
        :type request: :class:`huaweicloudsdkims.v2.GlanceListImageMembersRequest`
        :rtype: :class:`huaweicloudsdkims.v2.GlanceListImageMembersResponse`
        """
        http_info = self._glance_list_image_members_http_info(request)
        return self._call_api(**http_info)

    def glance_list_image_members_async_invoker(self, request):
        http_info = self._glance_list_image_members_http_info(request)
        return AsyncInvoker(self, http_info)

    def _glance_list_image_members_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/images/{image_id}/members",
            "request_type": request.__class__.__name__,
            "response_type": "GlanceListImageMembersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def glance_list_image_schemas_async(self, request):
        """查询镜像列表视图（OpenStack原生）

        该接口主要用于查询镜像列表视图，通过该接口用户可以了解到镜像列表的详细情况和数据结构。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GlanceListImageSchemas
        :type request: :class:`huaweicloudsdkims.v2.GlanceListImageSchemasRequest`
        :rtype: :class:`huaweicloudsdkims.v2.GlanceListImageSchemasResponse`
        """
        http_info = self._glance_list_image_schemas_http_info(request)
        return self._call_api(**http_info)

    def glance_list_image_schemas_async_invoker(self, request):
        http_info = self._glance_list_image_schemas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _glance_list_image_schemas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/schemas/images",
            "request_type": request.__class__.__name__,
            "response_type": "GlanceListImageSchemasResponse"
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

    def glance_list_images_async(self, request):
        """查询镜像列表（OpenStack原生）

        获取镜像列表。
        使用本接口查询镜像列表时，需要使用分页查询才能返回全部的镜像列表。
        分页说明
        分页是指返回一组镜像的一个子集，在返回的时候会存在下个子集的链接和首个子集的链接，默认返回的子集中数量为25，用户也可以通过使用limit和marker两个参数自己分页，指定返回子集中需要返回的数量。
        响应中的参数first是查询首页的URL。next是查询下一页的URL。当查询镜像列表最后一页时，不存在next。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GlanceListImages
        :type request: :class:`huaweicloudsdkims.v2.GlanceListImagesRequest`
        :rtype: :class:`huaweicloudsdkims.v2.GlanceListImagesResponse`
        """
        http_info = self._glance_list_images_http_info(request)
        return self._call_api(**http_info)

    def glance_list_images_async_invoker(self, request):
        http_info = self._glance_list_images_http_info(request)
        return AsyncInvoker(self, http_info)

    def _glance_list_images_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/images",
            "request_type": request.__class__.__name__,
            "response_type": "GlanceListImagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'imagetype' in local_var_params:
            query_params.append(('__imagetype', local_var_params['imagetype']))
        if 'isregistered' in local_var_params:
            query_params.append(('__isregistered', local_var_params['isregistered']))
        if 'os_bit' in local_var_params:
            query_params.append(('__os_bit', local_var_params['os_bit']))
        if 'os_type' in local_var_params:
            query_params.append(('__os_type', local_var_params['os_type']))
        if 'platform' in local_var_params:
            query_params.append(('__platform', local_var_params['platform']))
        if 'support_diskintensive' in local_var_params:
            query_params.append(('__support_diskintensive', local_var_params['support_diskintensive']))
        if 'support_highperformance' in local_var_params:
            query_params.append(('__support_highperformance', local_var_params['support_highperformance']))
        if 'support_kvm' in local_var_params:
            query_params.append(('__support_kvm', local_var_params['support_kvm']))
        if 'support_kvm_gpu_type' in local_var_params:
            query_params.append(('__support_kvm_gpu_type', local_var_params['support_kvm_gpu_type']))
        if 'support_kvm_infiniband' in local_var_params:
            query_params.append(('__support_kvm_infiniband', local_var_params['support_kvm_infiniband']))
        if 'support_largememory' in local_var_params:
            query_params.append(('__support_largememory', local_var_params['support_largememory']))
        if 'support_xen' in local_var_params:
            query_params.append(('__support_xen', local_var_params['support_xen']))
        if 'support_xen_gpu_type' in local_var_params:
            query_params.append(('__support_xen_gpu_type', local_var_params['support_xen_gpu_type']))
        if 'support_xen_hana' in local_var_params:
            query_params.append(('__support_xen_hana', local_var_params['support_xen_hana']))
        if 'container_format' in local_var_params:
            query_params.append(('container_format', local_var_params['container_format']))
        if 'disk_format' in local_var_params:
            query_params.append(('disk_format', local_var_params['disk_format']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'member_status' in local_var_params:
            query_params.append(('member_status', local_var_params['member_status']))
        if 'min_disk' in local_var_params:
            query_params.append(('min_disk', local_var_params['min_disk']))
        if 'min_ram' in local_var_params:
            query_params.append(('min_ram', local_var_params['min_ram']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'owner' in local_var_params:
            query_params.append(('owner', local_var_params['owner']))
        if 'protected' in local_var_params:
            query_params.append(('protected', local_var_params['protected']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))
        if 'visibility' in local_var_params:
            query_params.append(('visibility', local_var_params['visibility']))
        if 'created_at' in local_var_params:
            query_params.append(('created_at', local_var_params['created_at']))
        if 'updated_at' in local_var_params:
            query_params.append(('updated_at', local_var_params['updated_at']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def glance_show_image_async(self, request):
        """查询镜像详情（OpenStack原生）

        查询单个镜像详情，用户可以通过该接口查询单个私有或者公共镜像的详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GlanceShowImage
        :type request: :class:`huaweicloudsdkims.v2.GlanceShowImageRequest`
        :rtype: :class:`huaweicloudsdkims.v2.GlanceShowImageResponse`
        """
        http_info = self._glance_show_image_http_info(request)
        return self._call_api(**http_info)

    def glance_show_image_async_invoker(self, request):
        http_info = self._glance_show_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _glance_show_image_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/images/{image_id}",
            "request_type": request.__class__.__name__,
            "response_type": "GlanceShowImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def glance_show_image_member_async(self, request):
        """获取镜像成员详情（OpenStack原生）

        该接口主要用于镜像共享中查询某个镜像成员的详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GlanceShowImageMember
        :type request: :class:`huaweicloudsdkims.v2.GlanceShowImageMemberRequest`
        :rtype: :class:`huaweicloudsdkims.v2.GlanceShowImageMemberResponse`
        """
        http_info = self._glance_show_image_member_http_info(request)
        return self._call_api(**http_info)

    def glance_show_image_member_async_invoker(self, request):
        http_info = self._glance_show_image_member_http_info(request)
        return AsyncInvoker(self, http_info)

    def _glance_show_image_member_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/images/{image_id}/members/{member_id}",
            "request_type": request.__class__.__name__,
            "response_type": "GlanceShowImageMemberResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']
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

    def glance_show_image_member_schemas_async(self, request):
        """查询镜像成员视图（OpenStack原生）

        该接口主要用于查询镜像成员视图，通过视图，用户可以了解到镜像成员包含哪些属性，同时也可以了解每个属性的数据类型。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GlanceShowImageMemberSchemas
        :type request: :class:`huaweicloudsdkims.v2.GlanceShowImageMemberSchemasRequest`
        :rtype: :class:`huaweicloudsdkims.v2.GlanceShowImageMemberSchemasResponse`
        """
        http_info = self._glance_show_image_member_schemas_http_info(request)
        return self._call_api(**http_info)

    def glance_show_image_member_schemas_async_invoker(self, request):
        http_info = self._glance_show_image_member_schemas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _glance_show_image_member_schemas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/schemas/member",
            "request_type": request.__class__.__name__,
            "response_type": "GlanceShowImageMemberSchemasResponse"
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

    def glance_show_image_schemas_async(self, request):
        """查询镜像视图（OpenStack原生）

        该接口主要用于查询镜像视图，通过视图，用户可以了解到镜像包含哪些属性，同时也可以了解每个属性的数据类型等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GlanceShowImageSchemas
        :type request: :class:`huaweicloudsdkims.v2.GlanceShowImageSchemasRequest`
        :rtype: :class:`huaweicloudsdkims.v2.GlanceShowImageSchemasResponse`
        """
        http_info = self._glance_show_image_schemas_http_info(request)
        return self._call_api(**http_info)

    def glance_show_image_schemas_async_invoker(self, request):
        http_info = self._glance_show_image_schemas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _glance_show_image_schemas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/schemas/image",
            "request_type": request.__class__.__name__,
            "response_type": "GlanceShowImageSchemasResponse"
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

    def glance_update_image_async(self, request):
        """更新镜像信息（OpenStack原生）

        修改镜像信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GlanceUpdateImage
        :type request: :class:`huaweicloudsdkims.v2.GlanceUpdateImageRequest`
        :rtype: :class:`huaweicloudsdkims.v2.GlanceUpdateImageResponse`
        """
        http_info = self._glance_update_image_http_info(request)
        return self._call_api(**http_info)

    def glance_update_image_async_invoker(self, request):
        http_info = self._glance_update_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _glance_update_image_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v2/images/{image_id}",
            "request_type": request.__class__.__name__,
            "response_type": "GlanceUpdateImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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
            ['application/openstack-images-v2.1-json-patch'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def glance_update_image_member_async(self, request):
        """更新镜像成员状态（OpenStack原生）

        用户接受或者拒绝共享镜像时，使用该接口更新镜像成员的状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GlanceUpdateImageMember
        :type request: :class:`huaweicloudsdkims.v2.GlanceUpdateImageMemberRequest`
        :rtype: :class:`huaweicloudsdkims.v2.GlanceUpdateImageMemberResponse`
        """
        http_info = self._glance_update_image_member_http_info(request)
        return self._call_api(**http_info)

    def glance_update_image_member_async_invoker(self, request):
        http_info = self._glance_update_image_member_http_info(request)
        return AsyncInvoker(self, http_info)

    def _glance_update_image_member_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/images/{image_id}/members/{member_id}",
            "request_type": request.__class__.__name__,
            "response_type": "GlanceUpdateImageMemberResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']
        if 'member_id' in local_var_params:
            path_params['member_id'] = local_var_params['member_id']

        query_params = []

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
