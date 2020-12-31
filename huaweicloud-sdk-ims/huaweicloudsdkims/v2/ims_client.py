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


class ImsClient(Client):
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
        super(ImsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkims.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "ImsClient":
            raise TypeError("client type error, support client type is ImsClient")

        return ClientBuilder(clazz)

    def batch_add_members(self, request):
        """批量添加镜像成员

        该接口为扩展接口，主要用于镜像共享时用户将多个镜像共享给多个用户。 该接口为异步接口，返回job_id说明任务下发成功，查询异步任务状态，如果是success说明任务执行成功，如果是failed说明任务执行失败。如何查询异步任务，请参见异步任务查询。

        :param BatchAddMembersRequest request
        :return: BatchAddMembersResponse
        """
        return self.batch_add_members_with_http_info(request)

    def batch_add_members_with_http_info(self, request):
        """批量添加镜像成员

        该接口为扩展接口，主要用于镜像共享时用户将多个镜像共享给多个用户。 该接口为异步接口，返回job_id说明任务下发成功，查询异步任务状态，如果是success说明任务执行成功，如果是failed说明任务执行失败。如何查询异步任务，请参见异步任务查询。

        :param BatchAddMembersRequest request
        :return: BatchAddMembersResponse
        """

        all_params = ['members']
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
            resource_path='/v1/cloudimages/members',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchAddMembersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_delete_members(self, request):
        """批量删除镜像成员

        该接口为扩展接口，主要用于取消镜像共享。 该接口为异步接口，返回job_id说明任务下发成功，查询异步任务状态，如果是success说明任务执行成功，如果是failed说明任务执行失败。如何查询异步任务，请参见异步任务查询。

        :param BatchDeleteMembersRequest request
        :return: BatchDeleteMembersResponse
        """
        return self.batch_delete_members_with_http_info(request)

    def batch_delete_members_with_http_info(self, request):
        """批量删除镜像成员

        该接口为扩展接口，主要用于取消镜像共享。 该接口为异步接口，返回job_id说明任务下发成功，查询异步任务状态，如果是success说明任务执行成功，如果是failed说明任务执行失败。如何查询异步任务，请参见异步任务查询。

        :param BatchDeleteMembersRequest request
        :return: BatchDeleteMembersResponse
        """

        all_params = ['members']
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
            resource_path='/v1/cloudimages/members',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteMembersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_update_members(self, request):
        """批量更新镜像成员状态

        该接口为扩展接口，主要用于用户接受或者拒绝多个共享镜像时批量更新镜像成员的状态。 该接口为异步接口，返回job_id说明任务下发成功，查询异步任务状态，如果是success说明任务执行成功，如果是failed说明任务执行失败。如何查询异步任务，请参见异步任务查询。

        :param BatchUpdateMembersRequest request
        :return: BatchUpdateMembersResponse
        """
        return self.batch_update_members_with_http_info(request)

    def batch_update_members_with_http_info(self, request):
        """批量更新镜像成员状态

        该接口为扩展接口，主要用于用户接受或者拒绝多个共享镜像时批量更新镜像成员的状态。 该接口为异步接口，返回job_id说明任务下发成功，查询异步任务状态，如果是success说明任务执行成功，如果是failed说明任务执行失败。如何查询异步任务，请参见异步任务查询。

        :param BatchUpdateMembersRequest request
        :return: BatchUpdateMembersResponse
        """

        all_params = ['members']
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
            resource_path='/v1/cloudimages/members',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchUpdateMembersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def copy_image_cross_region(self, request):
        """跨Region复制镜像

        该接口为扩展接口，用户在一个区域制作的私有镜像，可以通过跨Region复制镜像将镜像复制到其他区域，在其他区域发放相同类型的云服务器，帮助用户实现区域间的业务迁移。 该接口为异步接口，返回job_id说明任务下发成功，查询异步任务状态，如果是success说明任务执行成功，如果是failed说明任务执行失败。 如何查询异步任务，请参见异步任务进度查询。

        :param CopyImageCrossRegionRequest request
        :return: CopyImageCrossRegionResponse
        """
        return self.copy_image_cross_region_with_http_info(request)

    def copy_image_cross_region_with_http_info(self, request):
        """跨Region复制镜像

        该接口为扩展接口，用户在一个区域制作的私有镜像，可以通过跨Region复制镜像将镜像复制到其他区域，在其他区域发放相同类型的云服务器，帮助用户实现区域间的业务迁移。 该接口为异步接口，返回job_id说明任务下发成功，查询异步任务状态，如果是success说明任务执行成功，如果是failed说明任务执行失败。 如何查询异步任务，请参见异步任务进度查询。

        :param CopyImageCrossRegionRequest request
        :return: CopyImageCrossRegionResponse
        """

        all_params = ['image_id', 'bodyparam']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v1/cloudimages/{image_id}/cross_region_copy',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CopyImageCrossRegionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def copy_image_in_region(self, request):
        """Region内复制镜像

        该接口为扩展接口，主要用于用户将一个已有镜像复制为另一个镜像。复制镜像时，可以更改镜像的加密等属性，以满足不同的场景。 该接口为异步接口，返回job_id说明任务下发成功，查询异步任务状态，如果是success说明任务执行成功，如果是failed说明任务执行失败。如何查询异步任务，请参见异步任务查询。

        :param CopyImageInRegionRequest request
        :return: CopyImageInRegionResponse
        """
        return self.copy_image_in_region_with_http_info(request)

    def copy_image_in_region_with_http_info(self, request):
        """Region内复制镜像

        该接口为扩展接口，主要用于用户将一个已有镜像复制为另一个镜像。复制镜像时，可以更改镜像的加密等属性，以满足不同的场景。 该接口为异步接口，返回job_id说明任务下发成功，查询异步任务状态，如果是success说明任务执行成功，如果是failed说明任务执行失败。如何查询异步任务，请参见异步任务查询。

        :param CopyImageInRegionRequest request
        :return: CopyImageInRegionResponse
        """

        all_params = ['image_id', 'bodyparam']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v1/cloudimages/{image_id}/copy',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CopyImageInRegionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_data_image(self, request):
        """使用外部镜像文件制作数据镜像

        使用上传至OBS桶中的外部数据卷镜像文件制作数据镜像。作为异步接口，调用成功，只是说明后台收到了制作请求，镜像是否制作成功需要通过异步任务查询接口查询该任务的执行状态。具体请参考异步任务查询。

        :param CreateDataImageRequest request
        :return: CreateDataImageResponse
        """
        return self.create_data_image_with_http_info(request)

    def create_data_image_with_http_info(self, request):
        """使用外部镜像文件制作数据镜像

        使用上传至OBS桶中的外部数据卷镜像文件制作数据镜像。作为异步接口，调用成功，只是说明后台收到了制作请求，镜像是否制作成功需要通过异步任务查询接口查询该任务的执行状态。具体请参考异步任务查询。

        :param CreateDataImageRequest request
        :return: CreateDataImageResponse
        """

        all_params = ['bodyparam']
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
            resource_path='/v1/cloudimages/dataimages/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateDataImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_image(self, request):
        """制作镜像

        本接口用于制作私有镜像，支持： 使用云服务器制作私有镜像。 使用上传至OBS桶中的外部镜像文件制作私有镜像。 使用数据卷制作系统盘镜像。 作为异步接口，调用成功，只是说明云平台收到了制作请求，镜像是否制作成功需要通过异步任务查询接口查询该任务的执行状态，具体请参考异步任务查询。

        :param CreateImageRequest request
        :return: CreateImageResponse
        """
        return self.create_image_with_http_info(request)

    def create_image_with_http_info(self, request):
        """制作镜像

        本接口用于制作私有镜像，支持： 使用云服务器制作私有镜像。 使用上传至OBS桶中的外部镜像文件制作私有镜像。 使用数据卷制作系统盘镜像。 作为异步接口，调用成功，只是说明云平台收到了制作请求，镜像是否制作成功需要通过异步任务查询接口查询该任务的执行状态，具体请参考异步任务查询。

        :param CreateImageRequest request
        :return: CreateImageResponse
        """

        all_params = ['ec_sbodyparam']
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
            resource_path='/v2/cloudimages/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_or_update_tags(self, request):
        """增加或修改标签

        该接口主要用于为某个镜像增加或修改一个自定义标签。通过自定义标签，用户可以将镜像进行分类。

        :param CreateOrUpdateTagsRequest request
        :return: CreateOrUpdateTagsResponse
        """
        return self.create_or_update_tags_with_http_info(request)

    def create_or_update_tags_with_http_info(self, request):
        """增加或修改标签

        该接口主要用于为某个镜像增加或修改一个自定义标签。通过自定义标签，用户可以将镜像进行分类。

        :param CreateOrUpdateTagsRequest request
        :return: CreateOrUpdateTagsResponse
        """

        all_params = ['bodyparam']
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
            resource_path='/v1/cloudimages/tags',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateOrUpdateTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_whole_image(self, request):
        """制作整机镜像

        使用云服务器或者云服务器备份制作整机镜像。作为异步接口，调用成功，只是说明后台收到了制作整机镜像的请求，镜像是否制作成功需要通过异步任务查询接口查询该任务的执行状态，具体请参考异步任务查询。

        :param CreateWholeImageRequest request
        :return: CreateWholeImageResponse
        """
        return self.create_whole_image_with_http_info(request)

    def create_whole_image_with_http_info(self, request):
        """制作整机镜像

        使用云服务器或者云服务器备份制作整机镜像。作为异步接口，调用成功，只是说明后台收到了制作整机镜像的请求，镜像是否制作成功需要通过异步任务查询接口查询该任务的执行状态，具体请参考异步任务查询。

        :param CreateWholeImageRequest request
        :return: CreateWholeImageResponse
        """

        all_params = ['ec_smakewholeimagebody']
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
            resource_path='/v1/cloudimages/wholeimages/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateWholeImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def export_image(self, request):
        """导出镜像

        该接口为扩展接口，用于用户将自己的私有镜像导出到指定的OBS桶中。

        :param ExportImageRequest request
        :return: ExportImageResponse
        """
        return self.export_image_with_http_info(request)

    def export_image_with_http_info(self, request):
        """导出镜像

        该接口为扩展接口，用于用户将自己的私有镜像导出到指定的OBS桶中。

        :param ExportImageRequest request
        :return: ExportImageResponse
        """

        all_params = ['image_id', 'bodyparam']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v1/cloudimages/{image_id}/file',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ExportImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def import_image_quick(self, request):
        """镜像文件快速导入

        使用上传至OBS桶中的超大外部镜像文件制作私有镜像，目前仅支持RAW或ZVHD2格式镜像文件。且要求镜像文件大小不能超过1TB。 由于快速导入功能要求提前转换镜像文件格式为RAW或ZVHD2格式，因此镜像文件小于128GB时推荐您优先使用常规的创建私有镜像的方式。 作为异步接口，调用成功，只是说明后台收到了制作请求，镜像是否制作成功需要通过异步任务查询接口查询该任务的执行状态，具体请参考异步任务查询。

        :param ImportImageQuickRequest request
        :return: ImportImageQuickResponse
        """
        return self.import_image_quick_with_http_info(request)

    def import_image_quick_with_http_info(self, request):
        """镜像文件快速导入

        使用上传至OBS桶中的超大外部镜像文件制作私有镜像，目前仅支持RAW或ZVHD2格式镜像文件。且要求镜像文件大小不能超过1TB。 由于快速导入功能要求提前转换镜像文件格式为RAW或ZVHD2格式，因此镜像文件小于128GB时推荐您优先使用常规的创建私有镜像的方式。 作为异步接口，调用成功，只是说明后台收到了制作请求，镜像是否制作成功需要通过异步任务查询接口查询该任务的执行状态，具体请参考异步任务查询。

        :param ImportImageQuickRequest request
        :return: ImportImageQuickResponse
        """

        all_params = ['file_create_ims']
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
            resource_path='/v2/cloudimages/quickimport/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ImportImageQuickResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_images(self, request):
        """查询镜像列表

        根据不同条件查询镜像列表信息。 可以在URI后面用‘?’和‘&’添加不同的查询条件组合，请参考请求样例。

        :param ListImagesRequest request
        :return: ListImagesResponse
        """
        return self.list_images_with_http_info(request)

    def list_images_with_http_info(self, request):
        """查询镜像列表

        根据不同条件查询镜像列表信息。 可以在URI后面用‘?’和‘&’添加不同的查询条件组合，请参考请求样例。

        :param ListImagesRequest request
        :return: ListImagesResponse
        """

        all_params = ['imagetype', 'isregistered', 'os_bit', 'os_type', 'platform', 'support_diskintensive', 'support_highperformance', 'support_kvm', 'support_kvm_gpu_type', 'support_kvm_infiniband', 'support_largememory', 'support_xen', 'support_xen_gpu_type', 'support_xen_hana', 'container_format', 'disk_format', 'enterprise_project_id', 'id', 'limit', 'marker', 'member_status', 'min_disk', 'min_ram', 'name', 'owner', 'protected', 'sort_dir', 'sort_key', 'status', 'tag', 'virtual_env_type', 'visibility', 'x_sdk_date', 'flavor_id', 'created_at', 'updated_at', 'architecture']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/cloudimages',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListImagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_os_versions(self, request):
        """查询镜像支持的OS列表

        查询当前区域弹性云服务器的OS兼容性列表。

        :param ListOsVersionsRequest request
        :return: ListOsVersionsResponse
        """
        return self.list_os_versions_with_http_info(request)

    def list_os_versions_with_http_info(self, request):
        """查询镜像支持的OS列表

        查询当前区域弹性云服务器的OS兼容性列表。

        :param ListOsVersionsRequest request
        :return: ListOsVersionsResponse
        """

        all_params = ['tag']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))

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
            resource_path='/v1/cloudimages/os_version',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListOsVersionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_tags(self, request):
        """按条件查询租户镜像标签列表

        根据不同条件查询镜像标签列表信息。

        :param ListTagsRequest request
        :return: ListTagsResponse
        """
        return self.list_tags_with_http_info(request)

    def list_tags_with_http_info(self, request):
        """按条件查询租户镜像标签列表

        根据不同条件查询镜像标签列表信息。

        :param ListTagsRequest request
        :return: ListTagsResponse
        """

        all_params = ['limit', 'page', 'imagetype', 'id', 'status', 'name', 'min_disk', 'platform', 'os_type', 'member_status', 'virtual_env_type', 'enterprise_project_id', 'architecture', 'created_at', 'updated_at']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/cloudimages/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def register_image(self, request):
        """注册镜像

        该接口用于将镜像文件注册为云平台未初始化的私有镜像。 使用该接口注册镜像的具体步骤如下： 将镜像文件上传到OBS个人桶中。具体操作请参见《对象存储服务客户端指南（OBS Browser）》或《对象存储服务API参考》。 使用创建镜像元数据接口创建镜像元数据。调用成功后，保存该镜像的ID。创建镜像元数据请参考创建镜像元数据（OpenStack原生）。 根据2得到的镜像ID，使用注册镜像接口注册OBS桶中的镜像文件。 注册镜像接口作为异步接口，调用成功后，说明后台收到了注册请求。需要根据镜像ID查询该镜像状态验证镜像注册是否成功。当镜像状态变为“active”时，表示镜像注册成功。 如何查询异步任务，请参见异步任务查询。

        :param RegisterImageRequest request
        :return: RegisterImageResponse
        """
        return self.register_image_with_http_info(request)

    def register_image_with_http_info(self, request):
        """注册镜像

        该接口用于将镜像文件注册为云平台未初始化的私有镜像。 使用该接口注册镜像的具体步骤如下： 将镜像文件上传到OBS个人桶中。具体操作请参见《对象存储服务客户端指南（OBS Browser）》或《对象存储服务API参考》。 使用创建镜像元数据接口创建镜像元数据。调用成功后，保存该镜像的ID。创建镜像元数据请参考创建镜像元数据（OpenStack原生）。 根据2得到的镜像ID，使用注册镜像接口注册OBS桶中的镜像文件。 注册镜像接口作为异步接口，调用成功后，说明后台收到了注册请求。需要根据镜像ID查询该镜像状态验证镜像注册是否成功。当镜像状态变为“active”时，表示镜像注册成功。 如何查询异步任务，请参见异步任务查询。

        :param RegisterImageRequest request
        :return: RegisterImageResponse
        """

        all_params = ['image_id', 'bodyparam']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v1/cloudimages/{image_id}/upload',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RegisterImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_image_quota(self, request):
        """查询镜像配额

        该接口为扩展接口，主要用于查询租户在当前Region的私有镜像的配额数量。

        :param ShowImageQuotaRequest request
        :return: ShowImageQuotaResponse
        """
        return self.show_image_quota_with_http_info(request)

    def show_image_quota_with_http_info(self, request):
        """查询镜像配额

        该接口为扩展接口，主要用于查询租户在当前Region的私有镜像的配额数量。

        :param ShowImageQuotaRequest request
        :return: ShowImageQuotaResponse
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
            resource_path='/v1/cloudimages/quota',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowImageQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_image(self, request):
        """更新镜像信息

        更新镜像信息接口，主要用于镜像属性的修改。当前仅支持可用（active）状态的镜像更新相关信息。

        :param UpdateImageRequest request
        :return: UpdateImageResponse
        """
        return self.update_image_with_http_info(request)

    def update_image_with_http_info(self, request):
        """更新镜像信息

        更新镜像信息接口，主要用于镜像属性的修改。当前仅支持可用（active）状态的镜像更新相关信息。

        :param UpdateImageRequest request
        :return: UpdateImageResponse
        """

        all_params = ['image_id', 'bodyparam']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v2/cloudimages/{image_id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def glance_add_image_member(self, request):
        """添加镜像成员（OpenStack原生）

        用户共享镜像给其他用户时，使用该接口向该镜像成员中添加接受镜像用户的项目ID。

        :param GlanceAddImageMemberRequest request
        :return: GlanceAddImageMemberResponse
        """
        return self.glance_add_image_member_with_http_info(request)

    def glance_add_image_member_with_http_info(self, request):
        """添加镜像成员（OpenStack原生）

        用户共享镜像给其他用户时，使用该接口向该镜像成员中添加接受镜像用户的项目ID。

        :param GlanceAddImageMemberRequest request
        :return: GlanceAddImageMemberResponse
        """

        all_params = ['image_id', 'add_member_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v2/images/{image_id}/members',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='GlanceAddImageMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def glance_create_image_metadata(self, request):
        """创建镜像元数据（OpenStack原生）

        创建镜像元数据。调用创建镜像元数据接口成功后，只是创建了镜像的元数据，镜像对应的实际镜像文件并不存在

        :param GlanceCreateImageMetadataRequest request
        :return: GlanceCreateImageMetadataResponse
        """
        return self.glance_create_image_metadata_with_http_info(request)

    def glance_create_image_metadata_with_http_info(self, request):
        """创建镜像元数据（OpenStack原生）

        创建镜像元数据。调用创建镜像元数据接口成功后，只是创建了镜像的元数据，镜像对应的实际镜像文件并不存在

        :param GlanceCreateImageMetadataRequest request
        :return: GlanceCreateImageMetadataResponse
        """

        all_params = ['bodyparam']
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
            resource_path='/v2/images',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='GlanceCreateImageMetadataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def glance_create_tag(self, request):
        """增加标签（OpenStack原生）

        该接口主要用于为某个镜像添加一个自定义标签。通过自定义标签，用户可以将镜像进行分类。

        :param GlanceCreateTagRequest request
        :return: GlanceCreateTagResponse
        """
        return self.glance_create_tag_with_http_info(request)

    def glance_create_tag_with_http_info(self, request):
        """增加标签（OpenStack原生）

        该接口主要用于为某个镜像添加一个自定义标签。通过自定义标签，用户可以将镜像进行分类。

        :param GlanceCreateTagRequest request
        :return: GlanceCreateTagResponse
        """

        all_params = ['image_id', 'tag']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']
        if 'tag' in local_var_params:
            path_params['tag'] = local_var_params['tag']

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
            resource_path='/v2/images/{image_id}/tags/{tag}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='GlanceCreateTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def glance_delete_image(self, request):
        """删除镜像（OpenStack原生）

        该接口主要用于删除镜像，用户可以通过该接口将自己的私有镜像删除。

        :param GlanceDeleteImageRequest request
        :return: GlanceDeleteImageResponse
        """
        return self.glance_delete_image_with_http_info(request)

    def glance_delete_image_with_http_info(self, request):
        """删除镜像（OpenStack原生）

        该接口主要用于删除镜像，用户可以通过该接口将自己的私有镜像删除。

        :param GlanceDeleteImageRequest request
        :return: GlanceDeleteImageResponse
        """

        all_params = ['image_id', 'delete_image_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v2/images/{image_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='GlanceDeleteImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def glance_delete_image_member(self, request):
        """删除指定的镜像成员（OpenStack原生）

        该接口用于取消对某个用户的镜像共享。

        :param GlanceDeleteImageMemberRequest request
        :return: GlanceDeleteImageMemberResponse
        """
        return self.glance_delete_image_member_with_http_info(request)

    def glance_delete_image_member_with_http_info(self, request):
        """删除指定的镜像成员（OpenStack原生）

        该接口用于取消对某个用户的镜像共享。

        :param GlanceDeleteImageMemberRequest request
        :return: GlanceDeleteImageMemberResponse
        """

        all_params = ['image_id', 'member_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']
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
            resource_path='/v2/images/{image_id}/members/{member_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='GlanceDeleteImageMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def glance_delete_tag(self, request):
        """删除标签（OpenStack原生）

        该接口主要用于删除某个镜像的自定义标签，通过该接口，用户可以将私有镜像中一些不用的标签删除。

        :param GlanceDeleteTagRequest request
        :return: GlanceDeleteTagResponse
        """
        return self.glance_delete_tag_with_http_info(request)

    def glance_delete_tag_with_http_info(self, request):
        """删除标签（OpenStack原生）

        该接口主要用于删除某个镜像的自定义标签，通过该接口，用户可以将私有镜像中一些不用的标签删除。

        :param GlanceDeleteTagRequest request
        :return: GlanceDeleteTagResponse
        """

        all_params = ['image_id', 'tag']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']
        if 'tag' in local_var_params:
            path_params['tag'] = local_var_params['tag']

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
            resource_path='/v2/images/{image_id}/tags/{tag}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='GlanceDeleteTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def glance_list_image_member_schemas(self, request):
        """查询镜像成员列表视图（OpenStack原生）

        该接口主要用于查询镜像成员列表视图，通过视图，用户可以了解到镜像成员包含哪些属性，同时也可以了解每个属性的数据类型。

        :param GlanceListImageMemberSchemasRequest request
        :return: GlanceListImageMemberSchemasResponse
        """
        return self.glance_list_image_member_schemas_with_http_info(request)

    def glance_list_image_member_schemas_with_http_info(self, request):
        """查询镜像成员列表视图（OpenStack原生）

        该接口主要用于查询镜像成员列表视图，通过视图，用户可以了解到镜像成员包含哪些属性，同时也可以了解每个属性的数据类型。

        :param GlanceListImageMemberSchemasRequest request
        :return: GlanceListImageMemberSchemasResponse
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
            resource_path='/v2/schemas/members',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='GlanceListImageMemberSchemasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def glance_list_image_members(self, request):
        """获取镜像成员列表（OpenStack原生）

        该接口用于共享镜像过程中，获取接受该镜像的成员列表。

        :param GlanceListImageMembersRequest request
        :return: GlanceListImageMembersResponse
        """
        return self.glance_list_image_members_with_http_info(request)

    def glance_list_image_members_with_http_info(self, request):
        """获取镜像成员列表（OpenStack原生）

        该接口用于共享镜像过程中，获取接受该镜像的成员列表。

        :param GlanceListImageMembersRequest request
        :return: GlanceListImageMembersResponse
        """

        all_params = ['image_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v2/images/{image_id}/members',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='GlanceListImageMembersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def glance_list_image_schemas(self, request):
        """查询镜像列表视图（OpenStack原生）

        该接口主要用于查询镜像列表视图，通过该接口用户可以了解到镜像列表的详细情况和数据结构。

        :param GlanceListImageSchemasRequest request
        :return: GlanceListImageSchemasResponse
        """
        return self.glance_list_image_schemas_with_http_info(request)

    def glance_list_image_schemas_with_http_info(self, request):
        """查询镜像列表视图（OpenStack原生）

        该接口主要用于查询镜像列表视图，通过该接口用户可以了解到镜像列表的详细情况和数据结构。

        :param GlanceListImageSchemasRequest request
        :return: GlanceListImageSchemasResponse
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
            resource_path='/v2/schemas/images',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='GlanceListImageSchemasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def glance_list_images(self, request):
        """查询镜像列表（OpenStack原生）

        获取镜像列表。 使用本接口查询镜像列表时，需要使用分页查询才能返回全部的镜像列表。 分页说明 分页是指返回一组镜像的一个子集，在返回的时候会存在下个子集的链接和首个子集的链接，默认返回的子集中数量为25，用户也可以通过使用limit和marker两个参数自己分页，指定返回子集中需要返回的数量。 响应中的参数first是查询首页的URL。next是查询下一页的URL。当查询镜像列表最后一页时，不存在next。

        :param GlanceListImagesRequest request
        :return: GlanceListImagesResponse
        """
        return self.glance_list_images_with_http_info(request)

    def glance_list_images_with_http_info(self, request):
        """查询镜像列表（OpenStack原生）

        获取镜像列表。 使用本接口查询镜像列表时，需要使用分页查询才能返回全部的镜像列表。 分页说明 分页是指返回一组镜像的一个子集，在返回的时候会存在下个子集的链接和首个子集的链接，默认返回的子集中数量为25，用户也可以通过使用limit和marker两个参数自己分页，指定返回子集中需要返回的数量。 响应中的参数first是查询首页的URL。next是查询下一页的URL。当查询镜像列表最后一页时，不存在next。

        :param GlanceListImagesRequest request
        :return: GlanceListImagesResponse
        """

        all_params = ['imagetype', 'isregistered', 'os_bit', 'os_type', 'platform', 'support_diskintensive', 'support_highperformance', 'support_kvm', 'support_kvm_gpu_type', 'support_kvm_infiniband', 'support_largememory', 'support_xen', 'support_xen_gpu_type', 'support_xen_hana', 'container_format', 'disk_format', 'id', 'limit', 'marker', 'member_status', 'min_disk', 'min_ram', 'name', 'owner', 'protected', 'sort_dir', 'sort_key', 'status', 'tag', 'visibility', 'created_at', 'updated_at']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/images',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='GlanceListImagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def glance_show_image(self, request):
        """查询镜像详情（OpenStack原生）

        查询单个镜像详情，用户可以通过该接口查询单个私有或者公共镜像的详情

        :param GlanceShowImageRequest request
        :return: GlanceShowImageResponse
        """
        return self.glance_show_image_with_http_info(request)

    def glance_show_image_with_http_info(self, request):
        """查询镜像详情（OpenStack原生）

        查询单个镜像详情，用户可以通过该接口查询单个私有或者公共镜像的详情

        :param GlanceShowImageRequest request
        :return: GlanceShowImageResponse
        """

        all_params = ['image_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v2/images/{image_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='GlanceShowImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def glance_show_image_member(self, request):
        """获取镜像成员详情（OpenStack原生）

        该接口主要用于镜像共享中查询某个镜像成员的详情。

        :param GlanceShowImageMemberRequest request
        :return: GlanceShowImageMemberResponse
        """
        return self.glance_show_image_member_with_http_info(request)

    def glance_show_image_member_with_http_info(self, request):
        """获取镜像成员详情（OpenStack原生）

        该接口主要用于镜像共享中查询某个镜像成员的详情。

        :param GlanceShowImageMemberRequest request
        :return: GlanceShowImageMemberResponse
        """

        all_params = ['image_id', 'member_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']
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
            resource_path='/v2/images/{image_id}/members/{member_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='GlanceShowImageMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def glance_show_image_member_schemas(self, request):
        """查询镜像成员视图（OpenStack原生）

        该接口主要用于查询镜像成员视图，通过视图，用户可以了解到镜像成员包含哪些属性，同时也可以了解每个属性的数据类型。

        :param GlanceShowImageMemberSchemasRequest request
        :return: GlanceShowImageMemberSchemasResponse
        """
        return self.glance_show_image_member_schemas_with_http_info(request)

    def glance_show_image_member_schemas_with_http_info(self, request):
        """查询镜像成员视图（OpenStack原生）

        该接口主要用于查询镜像成员视图，通过视图，用户可以了解到镜像成员包含哪些属性，同时也可以了解每个属性的数据类型。

        :param GlanceShowImageMemberSchemasRequest request
        :return: GlanceShowImageMemberSchemasResponse
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
            resource_path='/v2/schemas/member',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='GlanceShowImageMemberSchemasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def glance_show_image_schemas(self, request):
        """查询镜像视图（OpenStack原生）

        该接口主要用于查询镜像视图，通过视图，用户可以了解到镜像包含哪些属性，同时也可以了解每个属性的数据类型等。

        :param GlanceShowImageSchemasRequest request
        :return: GlanceShowImageSchemasResponse
        """
        return self.glance_show_image_schemas_with_http_info(request)

    def glance_show_image_schemas_with_http_info(self, request):
        """查询镜像视图（OpenStack原生）

        该接口主要用于查询镜像视图，通过视图，用户可以了解到镜像包含哪些属性，同时也可以了解每个属性的数据类型等。

        :param GlanceShowImageSchemasRequest request
        :return: GlanceShowImageSchemasResponse
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
            resource_path='/v2/schemas/image',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='GlanceShowImageSchemasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def glance_update_image(self, request):
        """更新镜像信息（OpenStack原生）

        修改镜像信息

        :param GlanceUpdateImageRequest request
        :return: GlanceUpdateImageResponse
        """
        return self.glance_update_image_with_http_info(request)

    def glance_update_image_with_http_info(self, request):
        """更新镜像信息（OpenStack原生）

        修改镜像信息

        :param GlanceUpdateImageRequest request
        :return: GlanceUpdateImageResponse
        """

        all_params = ['image_id', 'bodyparam']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v2/images/{image_id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='GlanceUpdateImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def glance_update_image_member(self, request):
        """更新镜像成员状态（OpenStack原生）

        用户接受或者拒绝共享镜像时，使用该接口更新镜像成员的状态。

        :param GlanceUpdateImageMemberRequest request
        :return: GlanceUpdateImageMemberResponse
        """
        return self.glance_update_image_member_with_http_info(request)

    def glance_update_image_member_with_http_info(self, request):
        """更新镜像成员状态（OpenStack原生）

        用户接受或者拒绝共享镜像时，使用该接口更新镜像成员的状态。

        :param GlanceUpdateImageMemberRequest request
        :return: GlanceUpdateImageMemberResponse
        """

        all_params = ['image_id', 'member_id', 'member_status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']
        if 'member_id' in local_var_params:
            path_params['member_id'] = local_var_params['member_id']

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
            resource_path='/v2/images/{image_id}/members/{member_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='GlanceUpdateImageMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_job(self, request):
        """查询job状态

        该接口为扩展接口，主要用于查询异步接口执行情况，比如查询导出镜像任务的执行状态。

        :param ShowJobRequest request
        :return: ShowJobResponse
        """
        return self.show_job_with_http_info(request)

    def show_job_with_http_info(self, request):
        """查询job状态

        该接口为扩展接口，主要用于查询异步接口执行情况，比如查询导出镜像任务的执行状态。

        :param ShowJobRequest request
        :return: ShowJobResponse
        """

        all_params = ['job_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1/{project_id}/jobs/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowJobResponse',
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
        :param header_params: Header parameters to be placed in the request header.
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
            request_type=request_type)
