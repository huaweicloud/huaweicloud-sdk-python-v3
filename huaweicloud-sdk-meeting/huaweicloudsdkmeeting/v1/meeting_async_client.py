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


class MeetingAsyncClient(Client):
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
        super(MeetingAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkmeeting.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @staticmethod
    def new_builder(clazz):
        return ClientBuilder(clazz, "MeetingCredentials")

    def add_corp_async(self, request):
        """SP管理员创建企业

        创建企业，默认管理员及分配资源。

        :param AddCorpRequest request
        :return: AddCorpResponse
        """
        return self.add_corp_with_http_info(request)

    def add_corp_with_http_info(self, request):
        """SP管理员创建企业

        创建企业，默认管理员及分配资源。

        :param AddCorpRequest request
        :return: AddCorpResponse
        """

        all_params = ['corp_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/sp/corp',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddCorpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_corp_admin_async(self, request):
        """添加企业管理员

        企业默认管理员添加企业普通管理员

        :param AddCorpAdminRequest request
        :return: AddCorpAdminResponse
        """
        return self.add_corp_admin_with_http_info(request)

    def add_corp_admin_with_http_info(self, request):
        """添加企业管理员

        企业默认管理员添加企业普通管理员

        :param AddCorpAdminRequest request
        :return: AddCorpAdminResponse
        """

        all_params = ['admin_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/admin',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddCorpAdminResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_department_async(self, request):
        """添加部门

        企业管理员通过该接口添加部门，最多支持10级部门，每级子部门最多支持100个，默认企业最大部门数量为3000个。

        :param AddDepartmentRequest request
        :return: AddDepartmentResponse
        """
        return self.add_department_with_http_info(request)

    def add_department_with_http_info(self, request):
        """添加部门

        企业管理员通过该接口添加部门，最多支持10级部门，每级子部门最多支持100个，默认企业最大部门数量为3000个。

        :param AddDepartmentRequest request
        :return: AddDepartmentResponse
        """

        all_params = ['dept_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/dept',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddDepartmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_device_async(self, request):
        """增加终端

        企业管理员通过该接口添加硬终端。

        :param AddDeviceRequest request
        :return: AddDeviceResponse
        """
        return self.add_device_with_http_info(request)

    def add_device_with_http_info(self, request):
        """增加终端

        企业管理员通过该接口添加硬终端。

        :param AddDeviceRequest request
        :return: AddDeviceResponse
        """

        all_params = ['device_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/device',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_program_async(self, request):
        """新增全球窗节目

        新增全球窗节目

        :param AddProgramRequest request
        :return: AddProgramResponse
        """
        return self.add_program_with_http_info(request)

    def add_program_with_http_info(self, request):
        """新增全球窗节目

        新增全球窗节目

        :param AddProgramRequest request
        :return: AddProgramResponse
        """

        all_params = ['program_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/sss/programs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddProgramResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_publication_async(self, request):
        """新增全球窗发布

        新增全球窗发布

        :param AddPublicationRequest request
        :return: AddPublicationResponse
        """
        return self.add_publication_with_http_info(request)

    def add_publication_with_http_info(self, request):
        """新增全球窗发布

        新增全球窗发布

        :param AddPublicationRequest request
        :return: AddPublicationResponse
        """

        all_params = ['publication_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/sss/publications',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddPublicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_resource_async(self, request):
        """分配企业资源

        企业新增资源发放。优化适配，该接口同时支持修改，带resourceId后会判断该资源是否存在，存在即修改（支持修改的参数见修改接口），否则按新增处理

        :param AddResourceRequest request
        :return: AddResourceResponse
        """
        return self.add_resource_with_http_info(request)

    def add_resource_with_http_info(self, request):
        """分配企业资源

        企业新增资源发放。优化适配，该接口同时支持修改，带resourceId后会判断该资源是否存在，存在即修改（支持修改的参数见修改接口），否则按新增处理

        :param AddResourceRequest request
        :return: AddResourceResponse
        """

        all_params = ['corp_id', 'resource_list', 'x_request_id', 'accept_language', 'force_edit_flag']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'corp_id' in local_var_params:
            path_params['corp_id'] = local_var_params['corp_id']

        query_params = []
        if 'force_edit_flag' in local_var_params:
            query_params.append(('forceEditFlag', local_var_params['force_edit_flag']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/sp/corp/{corp_id}/resource',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_to_personal_space_async(self, request):
        """保存会议纪要到个人云空间

        用户使用手机扫码后，手机端请求服务端将当前会议纪要文件保存到个人云空间。二维码内容  cloudlink://cloudlink.huawei.com/h5page?action=SAVE_MEETING_FILE&key1=value1&key2=value2    key/value的个数可能变化，终端解析后，在发起后续请求时，将所有key/value存为map，作为入参即可。

        :param AddToPersonalSpaceRequest request
        :return: AddToPersonalSpaceResponse
        """
        return self.add_to_personal_space_with_http_info(request)

    def add_to_personal_space_with_http_info(self, request):
        """保存会议纪要到个人云空间

        用户使用手机扫码后，手机端请求服务端将当前会议纪要文件保存到个人云空间。二维码内容  cloudlink://cloudlink.huawei.com/h5page?action=SAVE_MEETING_FILE&key1=value1&key2=value2    key/value的个数可能变化，终端解析后，在发起后续请求时，将所有key/value存为map，作为入参即可。

        :param AddToPersonalSpaceRequest request
        :return: AddToPersonalSpaceResponse
        """

        all_params = ['info', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/sss/meeting-files/save-to-personal-space',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddToPersonalSpaceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_user_async(self, request):
        """添加用户

        企业管理员通过该接口添加企业用户。

        :param AddUserRequest request
        :return: AddUserResponse
        """
        return self.add_user_with_http_info(request)

    def add_user_with_http_info(self, request):
        """添加用户

        企业管理员通过该接口添加企业用户。

        :param AddUserRequest request
        :return: AddUserResponse
        """

        all_params = ['user_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/member',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def allow_guest_unmute_async(self, request):
        """与会者自己解除静音

        决定与会者是否可以自己解除静音。

        :param AllowGuestUnmuteRequest request
        :return: AllowGuestUnmuteResponse
        """
        return self.allow_guest_unmute_with_http_info(request)

    def allow_guest_unmute_with_http_info(self, request):
        """与会者自己解除静音

        决定与会者是否可以自己解除静音。

        :param AllowGuestUnmuteRequest request
        :return: AllowGuestUnmuteResponse
        """

        all_params = ['conference_id', 'x_conference_authorization', 'req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/mute/guestUnMute',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AllowGuestUnmuteResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def associate_vmr_async(self, request):
        """分配专用云会议室

        企业管理员通过该接口将云会议室分配给用户、硬终端（当前仅支持分配TE10、TE20、HUAWEI Board、HUAWEI Bar 500及HUAWEI Box系列硬件终端）。云会议室分配给硬件终端后，需要重启或重新激活硬件终端。若需要管理云会议室、预约会议、录制会议或进行完整的会控操作，请同时将该云会议室分配给会议用户。

        :param AssociateVmrRequest request
        :return: AssociateVmrResponse
        """
        return self.associate_vmr_with_http_info(request)

    def associate_vmr_with_http_info(self, request):
        """分配专用云会议室

        企业管理员通过该接口将云会议室分配给用户、硬终端（当前仅支持分配TE10、TE20、HUAWEI Board、HUAWEI Bar 500及HUAWEI Box系列硬件终端）。云会议室分配给硬件终端后，需要重启或重新激活硬件终端。若需要管理云会议室、预约会议、录制会议或进行完整的会控操作，请同时将该云会议室分配给会议用户。

        :param AssociateVmrRequest request
        :return: AssociateVmrResponse
        """

        all_params = ['account', 'assign_list', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'account' in local_var_params:
            path_params['account'] = local_var_params['account']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/vmr/assign-to-member/{account}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AssociateVmrResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_delete_corp_admins_async(self, request):
        """批量删除企业管理员

        批量删除企业管理员

        :param BatchDeleteCorpAdminsRequest request
        :return: BatchDeleteCorpAdminsResponse
        """
        return self.batch_delete_corp_admins_with_http_info(request)

    def batch_delete_corp_admins_with_http_info(self, request):
        """批量删除企业管理员

        批量删除企业管理员

        :param BatchDeleteCorpAdminsRequest request
        :return: BatchDeleteCorpAdminsResponse
        """

        all_params = ['del_list', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/admin/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteCorpAdminsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_delete_devices_async(self, request):
        """批量删除终端

        企业管理员通过该接口批量删除终端，返回删除失败的列表。

        :param BatchDeleteDevicesRequest request
        :return: BatchDeleteDevicesResponse
        """
        return self.batch_delete_devices_with_http_info(request)

    def batch_delete_devices_with_http_info(self, request):
        """批量删除终端

        企业管理员通过该接口批量删除终端，返回删除失败的列表。

        :param BatchDeleteDevicesRequest request
        :return: BatchDeleteDevicesResponse
        """

        all_params = ['del_list', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/device/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteDevicesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_delete_materials_async(self, request):
        """删除全球窗素材

        删除全球窗素材

        :param BatchDeleteMaterialsRequest request
        :return: BatchDeleteMaterialsResponse
        """
        return self.batch_delete_materials_with_http_info(request)

    def batch_delete_materials_with_http_info(self, request):
        """删除全球窗素材

        删除全球窗素材

        :param BatchDeleteMaterialsRequest request
        :return: BatchDeleteMaterialsResponse
        """

        all_params = ['ids_request_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/sss/materials/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteMaterialsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_delete_programs_async(self, request):
        """删除全球窗节目

        删除全球窗节目

        :param BatchDeleteProgramsRequest request
        :return: BatchDeleteProgramsResponse
        """
        return self.batch_delete_programs_with_http_info(request)

    def batch_delete_programs_with_http_info(self, request):
        """删除全球窗节目

        删除全球窗节目

        :param BatchDeleteProgramsRequest request
        :return: BatchDeleteProgramsResponse
        """

        all_params = ['ids_request_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/sss/programs/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteProgramsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_delete_publications_async(self, request):
        """删除全球窗发布

        删除全球窗发布

        :param BatchDeletePublicationsRequest request
        :return: BatchDeletePublicationsResponse
        """
        return self.batch_delete_publications_with_http_info(request)

    def batch_delete_publications_with_http_info(self, request):
        """删除全球窗发布

        删除全球窗发布

        :param BatchDeletePublicationsRequest request
        :return: BatchDeletePublicationsResponse
        """

        all_params = ['ids_request_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/sss/publications/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeletePublicationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_delete_users_async(self, request):
        """批量删除用户

        企业管理员通过该接口批量删除企业用户，全量成功或全量失败。

        :param BatchDeleteUsersRequest request
        :return: BatchDeleteUsersResponse
        """
        return self.batch_delete_users_with_http_info(request)

    def batch_delete_users_with_http_info(self, request):
        """批量删除用户

        企业管理员通过该接口批量删除企业用户，全量成功或全量失败。

        :param BatchDeleteUsersRequest request
        :return: BatchDeleteUsersResponse
        """

        all_params = ['del_list', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/member/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_update_devices_status_async(self, request):
        """批量修改终端状态

        批量修改终端状态

        :param BatchUpdateDevicesStatusRequest request
        :return: BatchUpdateDevicesStatusResponse
        """
        return self.batch_update_devices_status_with_http_info(request)

    def batch_update_devices_status_with_http_info(self, request):
        """批量修改终端状态

        批量修改终端状态

        :param BatchUpdateDevicesStatusRequest request
        :return: BatchUpdateDevicesStatusResponse
        """

        all_params = ['value', 'sn_list', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'value' in local_var_params:
            path_params['value'] = local_var_params['value']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/device/status/{value}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchUpdateDevicesStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_update_user_status_async(self, request):
        """批量修改用户状态

        企业管理员通过该接口批量修改用户状态，当用户账号数资源或者第三方电子白板资源到期后，若企业内对应资源的用户账号超过数量后会被系统随机自动停用，此时可通过该接口修改用户的状态。

        :param BatchUpdateUserStatusRequest request
        :return: BatchUpdateUserStatusResponse
        """
        return self.batch_update_user_status_with_http_info(request)

    def batch_update_user_status_with_http_info(self, request):
        """批量修改用户状态

        企业管理员通过该接口批量修改用户状态，当用户账号数资源或者第三方电子白板资源到期后，若企业内对应资源的用户账号超过数量后会被系统随机自动停用，此时可通过该接口修改用户的状态。

        :param BatchUpdateUserStatusRequest request
        :return: BatchUpdateUserStatusResponse
        """

        all_params = ['value', 'account_list', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'value' in local_var_params:
            path_params['value'] = local_var_params['value']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/member/status/{value}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchUpdateUserStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def broadcast_participant_async(self, request):
        """广播会场

        同一时间，只允许一个与会者被广播。

        :param BroadcastParticipantRequest request
        :return: BroadcastParticipantResponse
        """
        return self.broadcast_participant_with_http_info(request)

    def broadcast_participant_with_http_info(self, request):
        """广播会场

        同一时间，只允许一个与会者被广播。

        :param BroadcastParticipantRequest request
        :return: BroadcastParticipantResponse
        """

        all_params = ['conference_id', 'participant_id', 'x_conference_authorization']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'participant_id' in local_var_params:
            query_params.append(('participantID', local_var_params['participant_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/control/conferences/participants/broadcast',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BroadcastParticipantResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def cancel_meeting_async(self, request):
        """取消预约会议

        取消预约会议。

        :param CancelMeetingRequest request
        :return: CancelMeetingResponse
        """
        return self.cancel_meeting_with_http_info(request)

    def cancel_meeting_with_http_info(self, request):
        """取消预约会议

        取消预约会议。

        :param CancelMeetingRequest request
        :return: CancelMeetingResponse
        """

        all_params = ['conference_id', 'user_uuid', 'type', 'x_authorization_type', 'x_site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/conferences',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CancelMeetingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def check_slide_verify_code_async(self, request):
        """校验滑块验证码

        该接口提供校验滑块验证码。服务器收到请求，返回校验结果。用户在前台界面通过滑块操作匹配图形，使得抠图和原图吻合。然后服务器进行校验滑块验证码。

        :param CheckSlideVerifyCodeRequest request
        :return: CheckSlideVerifyCodeResponse
        """
        return self.check_slide_verify_code_with_http_info(request)

    def check_slide_verify_code_with_http_info(self, request):
        """校验滑块验证码

        该接口提供校验滑块验证码。服务器收到请求，返回校验结果。用户在前台界面通过滑块操作匹配图形，使得抠图和原图吻合。然后服务器进行校验滑块验证码。

        :param CheckSlideVerifyCodeRequest request
        :return: CheckSlideVerifyCodeResponse
        """

        all_params = ['slide_verify_code_check_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/acs/auth/slideverifycode/check',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CheckSlideVerifyCodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def check_token_async(self, request):
        """校验Token

        该接口提供校验token合法性功能。服务器收到请求后，验证token合法性并返回结果。如果参数needGenNewToken为true时，生成新的token并返回。

        :param CheckTokenRequest request
        :return: CheckTokenResponse
        """
        return self.check_token_with_http_info(request)

    def check_token_with_http_info(self, request):
        """校验Token

        该接口提供校验token合法性功能。服务器收到请求后，验证token合法性并返回结果。如果参数needGenNewToken为true时，生成新的token并返回。

        :param CheckTokenRequest request
        :return: CheckTokenResponse
        """

        all_params = ['validate_token_req_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/acs/token/validate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CheckTokenResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def check_veri_code_for_update_user_info_async(self, request):
        """校验手机和邮箱对应的验证码

        企业用户通过该接口校验手机和邮箱对应的验证码，一分钟内记录尝试次数不得超过5次。

        :param CheckVeriCodeForUpdateUserInfoRequest request
        :return: CheckVeriCodeForUpdateUserInfoResponse
        """
        return self.check_veri_code_for_update_user_info_with_http_info(request)

    def check_veri_code_for_update_user_info_with_http_info(self, request):
        """校验手机和邮箱对应的验证码

        企业用户通过该接口校验手机和邮箱对应的验证码，一分钟内记录尝试次数不得超过5次。

        :param CheckVeriCodeForUpdateUserInfoRequest request
        :return: CheckVeriCodeForUpdateUserInfoResponse
        """

        all_params = ['verification_code_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/member/verification-code/verify',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CheckVeriCodeForUpdateUserInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def check_verify_code_async(self, request):
        """校验验证码

        该接口提供校验验证码，服务器收到请求，返回结果。

        :param CheckVerifyCodeRequest request
        :return: CheckVerifyCodeResponse
        """
        return self.check_verify_code_with_http_info(request)

    def check_verify_code_with_http_info(self, request):
        """校验验证码

        该接口提供校验验证码，服务器收到请求，返回结果。

        :param CheckVerifyCodeRequest request
        :return: CheckVerifyCodeResponse
        """

        all_params = ['verify_code_check_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/acs/verifycode/check',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CheckVerifyCodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_anonymous_auth_random_async(self, request):
        """匿名用户会议鉴权

        未登陆终端，通过输入会议ID进行会议鉴权，返回鉴权随机数。如果需要密码则返回需要会议密码错误码，然后终端弹出输入会议ID输入框，用户输入密码后，终端再次调用该接口进行鉴权。

        :param CreateAnonymousAuthRandomRequest request
        :return: CreateAnonymousAuthRandomResponse
        """
        return self.create_anonymous_auth_random_with_http_info(request)

    def create_anonymous_auth_random_with_http_info(self, request):
        """匿名用户会议鉴权

        未登陆终端，通过输入会议ID进行会议鉴权，返回鉴权随机数。如果需要密码则返回需要会议密码错误码，然后终端弹出输入会议ID输入框，用户输入密码后，终端再次调用该接口进行鉴权。

        :param CreateAnonymousAuthRandomRequest request
        :return: CreateAnonymousAuthRandomResponse
        """

        all_params = ['conference_id', 'x_password']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_password' in local_var_params:
            header_params['X-Password'] = local_var_params['x_password']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/conferences/anonymous/auth',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAnonymousAuthRandomResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_conf_token_async(self, request):
        """获取会控Token

        获取会控授权令牌，然后会议会被拉起。

        :param CreateConfTokenRequest request
        :return: CreateConfTokenResponse
        """
        return self.create_conf_token_with_http_info(request)

    def create_conf_token_with_http_info(self, request):
        """获取会控Token

        获取会控授权令牌，然后会议会被拉起。

        :param CreateConfTokenRequest request
        :return: CreateConfTokenResponse
        """

        all_params = ['conference_id', 'x_password', 'x_login_type', 'x_conference_authorization', 'x_nonce']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']
        if 'x_password' in local_var_params:
            header_params['X-Password'] = local_var_params['x_password']
        if 'x_login_type' in local_var_params:
            header_params['X-Login-Type'] = local_var_params['x_login_type']
        if 'x_nonce' in local_var_params:
            header_params['X-Nonce'] = local_var_params['x_nonce']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/control/conferences/token',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateConfTokenResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_meeting_async(self, request):
        """创建会议

        您可根据需要创建立即会议和预约会议。

        :param CreateMeetingRequest request
        :return: CreateMeetingResponse
        """
        return self.create_meeting_with_http_info(request)

    def create_meeting_with_http_info(self, request):
        """创建会议

        您可根据需要创建立即会议和预约会议。

        :param CreateMeetingRequest request
        :return: CreateMeetingResponse
        """

        all_params = ['req_body', 'user_uuid', 'x_authorization_type', 'x_site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

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
            resource_path='/v1/mmc/management/conferences',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateMeetingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_attendees_async(self, request):
        """删除与会者

        删除与会者。

        :param DeleteAttendeesRequest request
        :return: DeleteAttendeesResponse
        """
        return self.delete_attendees_with_http_info(request)

    def delete_attendees_with_http_info(self, request):
        """删除与会者

        删除与会者。

        :param DeleteAttendeesRequest request
        :return: DeleteAttendeesResponse
        """

        all_params = ['conference_id', 'x_conference_authorization', 'req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/attendees/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteAttendeesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_corp_async(self, request):
        """SP管理员删除企业

        删除企业

        :param DeleteCorpRequest request
        :return: DeleteCorpResponse
        """
        return self.delete_corp_with_http_info(request)

    def delete_corp_with_http_info(self, request):
        """SP管理员删除企业

        删除企业

        :param DeleteCorpRequest request
        :return: DeleteCorpResponse
        """

        all_params = ['id', 'x_request_id', 'accept_language', 'force_delete']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'force_delete' in local_var_params:
            query_params.append(('forceDelete', local_var_params['force_delete']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/sp/corp/{id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteCorpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_corp_vmr_async(self, request):
        """删除专用云会议室

        企业管理员通过该接口删除企业的专用云会议室

        :param DeleteCorpVmrRequest request
        :return: DeleteCorpVmrResponse
        """
        return self.delete_corp_vmr_with_http_info(request)

    def delete_corp_vmr_with_http_info(self, request):
        """删除专用云会议室

        企业管理员通过该接口删除企业的专用云会议室

        :param DeleteCorpVmrRequest request
        :return: DeleteCorpVmrResponse
        """

        all_params = ['del_list', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/vmr/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteCorpVmrResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_department_async(self, request):
        """删除部门

        企业管理员通过该接口删除部门。

        :param DeleteDepartmentRequest request
        :return: DeleteDepartmentResponse
        """
        return self.delete_department_with_http_info(request)

    def delete_department_with_http_info(self, request):
        """删除部门

        企业管理员通过该接口删除部门。

        :param DeleteDepartmentRequest request
        :return: DeleteDepartmentResponse
        """

        all_params = ['dept_code', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'dept_code' in local_var_params:
            path_params['dept_code'] = local_var_params['dept_code']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/corp/dept/{dept_code}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteDepartmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_recordings_async(self, request):
        """批量删除录制

        批量删除录制。

        :param DeleteRecordingsRequest request
        :return: DeleteRecordingsResponse
        """
        return self.delete_recordings_with_http_info(request)

    def delete_recordings_with_http_info(self, request):
        """批量删除录制

        批量删除录制。

        :param DeleteRecordingsRequest request
        :return: DeleteRecordingsResponse
        """

        all_params = ['conf_uui_ds', 'user_uuid', 'x_authorization_type', 'x_site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conf_uui_ds' in local_var_params:
            query_params.append(('confUUIDs', local_var_params['conf_uui_ds']))
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/record/files',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteRecordingsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_resource_async(self, request):
        """删除企业资源

        企业删除资源项，删除资源项后，企业资源总数会自动减少

        :param DeleteResourceRequest request
        :return: DeleteResourceResponse
        """
        return self.delete_resource_with_http_info(request)

    def delete_resource_with_http_info(self, request):
        """删除企业资源

        企业删除资源项，删除资源项后，企业资源总数会自动减少

        :param DeleteResourceRequest request
        :return: DeleteResourceResponse
        """

        all_params = ['corp_id', 'resource_id_list', 'x_request_id', 'accept_language', 'force_edit_flag']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'corp_id' in local_var_params:
            path_params['corp_id'] = local_var_params['corp_id']

        query_params = []
        if 'force_edit_flag' in local_var_params:
            query_params.append(('forceEditFlag', local_var_params['force_edit_flag']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/sp/corp/{corp_id}/resource/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def disassociate_vmr_async(self, request):
        """从用户或终端回收企业专用VMR

        给企业用户回收vmr，需要做好纵向越权校验，避免企业管理员给其他企业的账号分配

        :param DisassociateVmrRequest request
        :return: DisassociateVmrResponse
        """
        return self.disassociate_vmr_with_http_info(request)

    def disassociate_vmr_with_http_info(self, request):
        """从用户或终端回收企业专用VMR

        给企业用户回收vmr，需要做好纵向越权校验，避免企业管理员给其他企业的账号分配

        :param DisassociateVmrRequest request
        :return: DisassociateVmrResponse
        """

        all_params = ['account', 'recycle_list', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'account' in local_var_params:
            path_params['account'] = local_var_params['account']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/vmr/recycle-from-member/{account}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DisassociateVmrResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def edit_meeting_async(self, request):
        """编辑预约会议

        编辑预约会议。会议开始后，不能被编辑。

        :param EditMeetingRequest request
        :return: EditMeetingResponse
        """
        return self.edit_meeting_with_http_info(request)

    def edit_meeting_with_http_info(self, request):
        """编辑预约会议

        编辑预约会议。会议开始后，不能被编辑。

        :param EditMeetingRequest request
        :return: EditMeetingResponse
        """

        all_params = ['conference_id', 'req_body', 'user_uuid', 'x_authorization_type', 'x_site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

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
            resource_path='/v1/mmc/management/conferences',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='EditMeetingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def hand_async(self, request):
        """举手

        所有来宾可以举手。来宾举手后，可以取消自己的举手。主持人可以取消所有来宾的举手。

        :param HandRequest request
        :return: HandResponse
        """
        return self.hand_with_http_info(request)

    def hand_with_http_info(self, request):
        """举手

        所有来宾可以举手。来宾举手后，可以取消自己的举手。主持人可以取消所有来宾的举手。

        :param HandRequest request
        :return: HandResponse
        """

        all_params = ['conference_id', 'participant_id', 'x_conference_authorization', 'rest_hands_up_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'participant_id' in local_var_params:
            query_params.append(('participantID', local_var_params['participant_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/participants/hands',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='HandResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def hang_up_async(self, request):
        """挂断与会者

        挂断正在通话中的与会者。

        :param HangUpRequest request
        :return: HangUpResponse
        """
        return self.hang_up_with_http_info(request)

    def hang_up_with_http_info(self, request):
        """挂断与会者

        挂断正在通话中的与会者。

        :param HangUpRequest request
        :return: HangUpResponse
        """

        all_params = ['conference_id', 'x_conference_authorization', 'req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/participants/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='HangUpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def invite_participant_async(self, request):
        """邀请与会者

        邀请与会者加入会议。

        :param InviteParticipantRequest request
        :return: InviteParticipantResponse
        """
        return self.invite_participant_with_http_info(request)

    def invite_participant_with_http_info(self, request):
        """邀请与会者

        邀请与会者加入会议。

        :param InviteParticipantRequest request
        :return: InviteParticipantResponse
        """

        all_params = ['conference_id', 'x_conference_authorization', 'req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/participants',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='InviteParticipantResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def invite_with_pwd_async(self, request):
        """通过会议ID和密码邀请与会者

        通过会议ID和密码邀请与会者

        :param InviteWithPwdRequest request
        :return: InviteWithPwdResponse
        """
        return self.invite_with_pwd_with_http_info(request)

    def invite_with_pwd_with_http_info(self, request):
        """通过会议ID和密码邀请与会者

        通过会议ID和密码邀请与会者

        :param InviteWithPwdRequest request
        :return: InviteWithPwdResponse
        """

        all_params = ['conference_id', 'req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}

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
            resource_path='/v1/mmc/control/conferences/inviteWithPwd',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='InviteWithPwdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def live_async(self, request):
        """启停会议直播

        启动或停止会议直播。

        :param LiveRequest request
        :return: LiveResponse
        """
        return self.live_with_http_info(request)

    def live_with_http_info(self, request):
        """启停会议直播

        启动或停止会议直播。

        :param LiveRequest request
        :return: LiveResponse
        """

        all_params = ['conference_id', 'x_conference_authorization', 'rest_set_live_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/live',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='LiveResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def lock_meeting_async(self, request):
        """锁定会议

        锁定或解锁会议。锁定会议后，不允许与会者加入会议。

        :param LockMeetingRequest request
        :return: LockMeetingResponse
        """
        return self.lock_meeting_with_http_info(request)

    def lock_meeting_with_http_info(self, request):
        """锁定会议

        锁定或解锁会议。锁定会议后，不允许与会者加入会议。

        :param LockMeetingRequest request
        :return: LockMeetingResponse
        """

        all_params = ['conference_id', 'x_conference_authorization', 'rest_lock_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/lock',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='LockMeetingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def lock_view_async(self, request):
        """锁定会场视频源

        锁定或者解锁某在线会场的视频源。

        :param LockViewRequest request
        :return: LockViewResponse
        """
        return self.lock_view_with_http_info(request)

    def lock_view_with_http_info(self, request):
        """锁定会场视频源

        锁定或者解锁某在线会场的视频源。

        :param LockViewRequest request
        :return: LockViewResponse
        """

        all_params = ['conference_id', 'participant_id', 'x_conference_authorization', 'req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'participant_id' in local_var_params:
            query_params.append(('participantID', local_var_params['participant_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/lockView',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='LockViewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def mute_meeting_async(self, request):
        """全场静音

        主持人可以通过该接口静音/取消静音整个会议所有与会者（主持人除外）。

        :param MuteMeetingRequest request
        :return: MuteMeetingResponse
        """
        return self.mute_meeting_with_http_info(request)

    def mute_meeting_with_http_info(self, request):
        """全场静音

        主持人可以通过该接口静音/取消静音整个会议所有与会者（主持人除外）。

        :param MuteMeetingRequest request
        :return: MuteMeetingResponse
        """

        all_params = ['conference_id', 'x_conference_authorization', 'rest_mute_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/mute',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='MuteMeetingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def mute_participant_async(self, request):
        """静音与会者

        主持人可以静音/取消静音任意与会者，来宾也可静音/取消静音自己。

        :param MuteParticipantRequest request
        :return: MuteParticipantResponse
        """
        return self.mute_participant_with_http_info(request)

    def mute_participant_with_http_info(self, request):
        """静音与会者

        主持人可以静音/取消静音任意与会者，来宾也可静音/取消静音自己。

        :param MuteParticipantRequest request
        :return: MuteParticipantResponse
        """

        all_params = ['conference_id', 'participant_id', 'x_conference_authorization', 'rest_mute_participant_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'participant_id' in local_var_params:
            query_params.append(('participantID', local_var_params['participant_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/participants/mute',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='MuteParticipantResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def prolong_meeting_async(self, request):
        """延长会议

        延长会议。

        :param ProlongMeetingRequest request
        :return: ProlongMeetingResponse
        """
        return self.prolong_meeting_with_http_info(request)

    def prolong_meeting_with_http_info(self, request):
        """延长会议

        延长会议。

        :param ProlongMeetingRequest request
        :return: ProlongMeetingResponse
        """

        all_params = ['conference_id', 'x_conference_authorization', 'rest_prolong_dur_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/duration',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ProlongMeetingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def record_async(self, request):
        """启停会议录制

        启动或停止会议录制。

        :param RecordRequest request
        :return: RecordResponse
        """
        return self.record_with_http_info(request)

    def record_with_http_info(self, request):
        """启停会议录制

        启动或停止会议录制。

        :param RecordRequest request
        :return: RecordResponse
        """

        all_params = ['conference_id', 'x_conference_authorization', 'rest_set_record_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/record',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RecordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def rename_participant_async(self, request):
        """重命名与会者

        重命名某个与会者。

        :param RenameParticipantRequest request
        :return: RenameParticipantResponse
        """
        return self.rename_participant_with_http_info(request)

    def rename_participant_with_http_info(self, request):
        """重命名与会者

        重命名某个与会者。

        :param RenameParticipantRequest request
        :return: RenameParticipantResponse
        """

        all_params = ['conference_id', 'x_conference_authorization', 'rest_rename_part_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/participants/name',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RenameParticipantResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def reset_activecode_async(self, request):
        """重置激活码

        当硬终端激活码失效时，企业管理员可以通过该接口重置激活码，使用重新获取的激活码激活终端，每24小时可重新激活5次。

        :param ResetActivecodeRequest request
        :return: ResetActivecodeResponse
        """
        return self.reset_activecode_with_http_info(request)

    def reset_activecode_with_http_info(self, request):
        """重置激活码

        当硬终端激活码失效时，企业管理员可以通过该接口重置激活码，使用重新获取的激活码激活终端，每24小时可重新激活5次。

        :param ResetActivecodeRequest request
        :return: ResetActivecodeResponse
        """

        all_params = ['sn', 'active_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'sn' in local_var_params:
            path_params['sn'] = local_var_params['sn']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/device/{sn}/activecode',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ResetActivecodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def reset_pwd_async(self, request):
        """用户重置密码

        该接口提供给用户重置密码功能，服务器收到请求，重新设置用户密码并返回结果。

        :param ResetPwdRequest request
        :return: ResetPwdResponse
        """
        return self.reset_pwd_with_http_info(request)

    def reset_pwd_with_http_info(self, request):
        """用户重置密码

        该接口提供给用户重置密码功能，服务器收到请求，重新设置用户密码并返回结果。

        :param ResetPwdRequest request
        :return: ResetPwdResponse
        """

        all_params = ['reset_pwd_req_dtov1', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/acs/password/reset',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ResetPwdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def reset_pwd_by_admin_async(self, request):
        """企业管理员重置企业成员密码

        企业管理员通过该接口提供企业管理员重置企业成员密码的功能。当服务器收到重置密码的请求时，发送新的密码到企业成员的邮箱或者短信，并返回结果。

        :param ResetPwdByAdminRequest request
        :return: ResetPwdByAdminResponse
        """
        return self.reset_pwd_by_admin_with_http_info(request)

    def reset_pwd_by_admin_with_http_info(self, request):
        """企业管理员重置企业成员密码

        企业管理员通过该接口提供企业管理员重置企业成员密码的功能。当服务器收到重置密码的请求时，发送新的密码到企业成员的邮箱或者短信，并返回结果。

        :param ResetPwdByAdminRequest request
        :return: ResetPwdByAdminResponse
        """

        all_params = ['admin_reset_pwd_req_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/acs/password/admin/reset',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ResetPwdByAdminResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def rollcall_participant_async(self, request):
        """点名会场

        同一时间，只允许一个与会者被点名。点名会场的效果是除了主持人外，点名与会者为非静音状态，未点名的与会者统一为静音状态。

        :param RollcallParticipantRequest request
        :return: RollcallParticipantResponse
        """
        return self.rollcall_participant_with_http_info(request)

    def rollcall_participant_with_http_info(self, request):
        """点名会场

        同一时间，只允许一个与会者被点名。点名会场的效果是除了主持人外，点名与会者为非静音状态，未点名的与会者统一为静音状态。

        :param RollcallParticipantRequest request
        :return: RollcallParticipantResponse
        """

        all_params = ['conference_id', 'participant_id', 'x_conference_authorization']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'participant_id' in local_var_params:
            query_params.append(('participantID', local_var_params['participant_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/control/conferences/participants/rollCall',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RollcallParticipantResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def search_attendance_records_of_his_meeting_async(self, request):
        """查询历史会议的与会者记录

        查询指定历史会议的与会者记录。

        :param SearchAttendanceRecordsOfHisMeetingRequest request
        :return: SearchAttendanceRecordsOfHisMeetingResponse
        """
        return self.search_attendance_records_of_his_meeting_with_http_info(request)

    def search_attendance_records_of_his_meeting_with_http_info(self, request):
        """查询历史会议的与会者记录

        查询指定历史会议的与会者记录。

        :param SearchAttendanceRecordsOfHisMeetingRequest request
        :return: SearchAttendanceRecordsOfHisMeetingResponse
        """

        all_params = ['conf_uuid', 'offset', 'limit', 'search_key', 'user_uuid', 'x_authorization_type', 'x_site_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conf_uuid' in local_var_params:
            query_params.append(('confUUID', local_var_params['conf_uuid']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/conferences/history/confAttendeeRecord',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchAttendanceRecordsOfHisMeetingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def search_corp_async(self, request):
        """SP管理员分页搜索企业

        分页搜索企业,支持名称、企业ID搜索

        :param SearchCorpRequest request
        :return: SearchCorpResponse
        """
        return self.search_corp_with_http_info(request)

    def search_corp_with_http_info(self, request):
        """SP管理员分页搜索企业

        分页搜索企业,支持名称、企业ID搜索

        :param SearchCorpRequest request
        :return: SearchCorpResponse
        """

        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/sp/corp',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchCorpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def search_corp_admins_async(self, request):
        """分页查询企业管理员

        通过该接口分页查询企业管理员。

        :param SearchCorpAdminsRequest request
        :return: SearchCorpAdminsResponse
        """
        return self.search_corp_admins_with_http_info(request)

    def search_corp_admins_with_http_info(self, request):
        """分页查询企业管理员

        通过该接口分页查询企业管理员。

        :param SearchCorpAdminsRequest request
        :return: SearchCorpAdminsResponse
        """

        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/corp/admin',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchCorpAdminsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def search_corp_dir_async(self, request):
        """查询企业通讯录

        企业用户（含管理员）通过该接口查询该企业的通讯录。

        :param SearchCorpDirRequest request
        :return: SearchCorpDirResponse
        """
        return self.search_corp_dir_with_http_info(request)

    def search_corp_dir_with_http_info(self, request):
        """查询企业通讯录

        企业用户（含管理员）通过该接口查询该企业的通讯录。

        :param SearchCorpDirRequest request
        :return: SearchCorpDirResponse
        """

        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key', 'dept_code', 'query_sub_dept', 'search_scope']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'dept_code' in local_var_params:
            query_params.append(('deptCode', local_var_params['dept_code']))
        if 'query_sub_dept' in local_var_params:
            query_params.append(('querySubDept', local_var_params['query_sub_dept']))
        if 'search_scope' in local_var_params:
            query_params.append(('searchScope', local_var_params['search_scope']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/abs/users',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchCorpDirResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def search_corp_vmr_async(self, request):
        """分页查询专用云会议室

        企业管理员通过该接口分页查询企业的专用云会议室。

        :param SearchCorpVmrRequest request
        :return: SearchCorpVmrResponse
        """
        return self.search_corp_vmr_with_http_info(request)

    def search_corp_vmr_with_http_info(self, request):
        """分页查询专用云会议室

        企业管理员通过该接口分页查询企业的专用云会议室。

        :param SearchCorpVmrRequest request
        :return: SearchCorpVmrResponse
        """

        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key', 'status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/corp/vmr',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchCorpVmrResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def search_ctl_records_of_his_meeting_async(self, request):
        """查询历史会议的会控记录

        查询指定历史会议的会控记录。

        :param SearchCtlRecordsOfHisMeetingRequest request
        :return: SearchCtlRecordsOfHisMeetingResponse
        """
        return self.search_ctl_records_of_his_meeting_with_http_info(request)

    def search_ctl_records_of_his_meeting_with_http_info(self, request):
        """查询历史会议的会控记录

        查询指定历史会议的会控记录。

        :param SearchCtlRecordsOfHisMeetingRequest request
        :return: SearchCtlRecordsOfHisMeetingResponse
        """

        all_params = ['conf_uuid', 'offset', 'limit', 'user_uuid', 'x_authorization_type', 'x_site_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conf_uuid' in local_var_params:
            query_params.append(('confUUID', local_var_params['conf_uuid']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/conferences/history/confCtlRecord',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchCtlRecordsOfHisMeetingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def search_department_by_name_async(self, request):
        """按名称查询所有的部门

        企业管理员通过该接口按名称查询所有的部门。

        :param SearchDepartmentByNameRequest request
        :return: SearchDepartmentByNameResponse
        """
        return self.search_department_by_name_with_http_info(request)

    def search_department_by_name_with_http_info(self, request):
        """按名称查询所有的部门

        企业管理员通过该接口按名称查询所有的部门。

        :param SearchDepartmentByNameRequest request
        :return: SearchDepartmentByNameResponse
        """

        all_params = ['dept_name', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'dept_name' in local_var_params:
            query_params.append(('deptName', local_var_params['dept_name']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/member/dept',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchDepartmentByNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def search_devices_async(self, request):
        """分页查询终端

        企业管理员通过该接口分页查询终端信息。

        :param SearchDevicesRequest request
        :return: SearchDevicesResponse
        """
        return self.search_devices_with_http_info(request)

    def search_devices_with_http_info(self, request):
        """分页查询终端

        企业管理员通过该接口分页查询终端信息。

        :param SearchDevicesRequest request
        :return: SearchDevicesResponse
        """

        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key', 'model', 'dept_code', 'enable_sub_dept']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'model' in local_var_params:
            query_params.append(('model', local_var_params['model']))
        if 'dept_code' in local_var_params:
            query_params.append(('deptCode', local_var_params['dept_code']))
        if 'enable_sub_dept' in local_var_params:
            query_params.append(('enableSubDept', local_var_params['enable_sub_dept']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/corp/device',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchDevicesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def search_his_meetings_async(self, request):
        """查询历史会议列表

        管理员可以查询管理权限域内所有的历史会议，普通用户仅能查询当前帐号管理的历史会议。不带查询参数时，默认查询权限范围内的历史会议。

        :param SearchHisMeetingsRequest request
        :return: SearchHisMeetingsResponse
        """
        return self.search_his_meetings_with_http_info(request)

    def search_his_meetings_with_http_info(self, request):
        """查询历史会议列表

        管理员可以查询管理权限域内所有的历史会议，普通用户仅能查询当前帐号管理的历史会议。不带查询参数时，默认查询权限范围内的历史会议。

        :param SearchHisMeetingsRequest request
        :return: SearchHisMeetingsResponse
        """

        all_params = ['start_date', 'end_date', 'user_uuid', 'offset', 'limit', 'search_key', 'query_all', 'sort_type', 'x_authorization_type', 'x_site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'query_all' in local_var_params:
            query_params.append(('queryAll', local_var_params['query_all']))
        if 'start_date' in local_var_params:
            query_params.append(('startDate', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('endDate', local_var_params['end_date']))
        if 'sort_type' in local_var_params:
            query_params.append(('sortType', local_var_params['sort_type']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/conferences/history',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchHisMeetingsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def search_materials_async(self, request):
        """分页查询全球窗素材

        分页查询全球窗素材

        :param SearchMaterialsRequest request
        :return: SearchMaterialsResponse
        """
        return self.search_materials_with_http_info(request)

    def search_materials_with_http_info(self, request):
        """分页查询全球窗素材

        分页查询全球窗素材

        :param SearchMaterialsRequest request
        :return: SearchMaterialsResponse
        """

        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/sss/materials',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchMaterialsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def search_meeting_file_list_async(self, request):
        """查询会议纪要列表

        用户查询自己的会议纪要列表

        :param SearchMeetingFileListRequest request
        :return: SearchMeetingFileListResponse
        """
        return self.search_meeting_file_list_with_http_info(request)

    def search_meeting_file_list_with_http_info(self, request):
        """查询会议纪要列表

        用户查询自己的会议纪要列表

        :param SearchMeetingFileListRequest request
        :return: SearchMeetingFileListResponse
        """

        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/sss/meeting-files',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchMeetingFileListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def search_meetings_async(self, request):
        """查询会议列表

        管理员可以查询管理权限域内所有的会议，普通用户仅能查询当前帐号管理的会议。不带查询参数时，默认查询权限范围内正在召开或还未召开的会议。

        :param SearchMeetingsRequest request
        :return: SearchMeetingsResponse
        """
        return self.search_meetings_with_http_info(request)

    def search_meetings_with_http_info(self, request):
        """查询会议列表

        管理员可以查询管理权限域内所有的会议，普通用户仅能查询当前帐号管理的会议。不带查询参数时，默认查询权限范围内正在召开或还未召开的会议。

        :param SearchMeetingsRequest request
        :return: SearchMeetingsResponse
        """

        all_params = ['user_uuid', 'offset', 'limit', 'query_all', 'search_key', 'query_conf_mode', 'sort_type', 'x_authorization_type', 'x_site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'query_all' in local_var_params:
            query_params.append(('queryAll', local_var_params['query_all']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'query_conf_mode' in local_var_params:
            query_params.append(('queryConfMode', local_var_params['query_conf_mode']))
        if 'sort_type' in local_var_params:
            query_params.append(('sortType', local_var_params['sort_type']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/conferences',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchMeetingsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def search_member_vmr_async(self, request):
        """分页查询用户云会议室

        企业用户通过该接口查询个人已分配的云会议室，包括个人及专用两种。

        :param SearchMemberVmrRequest request
        :return: SearchMemberVmrResponse
        """
        return self.search_member_vmr_with_http_info(request)

    def search_member_vmr_with_http_info(self, request):
        """分页查询用户云会议室

        企业用户通过该接口查询个人已分配的云会议室，包括个人及专用两种。

        :param SearchMemberVmrRequest request
        :return: SearchMemberVmrResponse
        """

        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key', 'special_vmr']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'special_vmr' in local_var_params:
            query_params.append(('specialVmr', local_var_params['special_vmr']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/member/vmr',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchMemberVmrResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def search_online_meetings_async(self, request):
        """查询在线会议列表

        管理员可以查询管理权限域内所有在线会议，普通用户仅能查询当前自己帐号管理的在线会议。不带查询参数时，默认查询权限范围内的在线会议，按开始时间升序排列。

        :param SearchOnlineMeetingsRequest request
        :return: SearchOnlineMeetingsResponse
        """
        return self.search_online_meetings_with_http_info(request)

    def search_online_meetings_with_http_info(self, request):
        """查询在线会议列表

        管理员可以查询管理权限域内所有在线会议，普通用户仅能查询当前自己帐号管理的在线会议。不带查询参数时，默认查询权限范围内的在线会议，按开始时间升序排列。

        :param SearchOnlineMeetingsRequest request
        :return: SearchOnlineMeetingsResponse
        """

        all_params = ['user_uuid', 'offset', 'limit', 'query_all', 'search_key', 'x_authorization_type', 'x_site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'query_all' in local_var_params:
            query_params.append(('queryAll', local_var_params['query_all']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/conferences/online',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchOnlineMeetingsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def search_programs_async(self, request):
        """查询全球窗节目

        获取全球窗节目

        :param SearchProgramsRequest request
        :return: SearchProgramsResponse
        """
        return self.search_programs_with_http_info(request)

    def search_programs_with_http_info(self, request):
        """查询全球窗节目

        获取全球窗节目

        :param SearchProgramsRequest request
        :return: SearchProgramsResponse
        """

        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/sss/programs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchProgramsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def search_publications_async(self, request):
        """查询全球窗发布

        获取全球窗发布

        :param SearchPublicationsRequest request
        :return: SearchPublicationsResponse
        """
        return self.search_publications_with_http_info(request)

    def search_publications_with_http_info(self, request):
        """查询全球窗发布

        获取全球窗发布

        :param SearchPublicationsRequest request
        :return: SearchPublicationsResponse
        """

        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/sss/publications',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchPublicationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def search_recordings_async(self, request):
        """查询录制列表

        管理员可以查询管理权限域内所有的录制，普通用户仅能查询当前帐号管理的录制。不带查询参数时，默认查询权限范围内的录制。

        :param SearchRecordingsRequest request
        :return: SearchRecordingsResponse
        """
        return self.search_recordings_with_http_info(request)

    def search_recordings_with_http_info(self, request):
        """查询录制列表

        管理员可以查询管理权限域内所有的录制，普通用户仅能查询当前帐号管理的录制。不带查询参数时，默认查询权限范围内的录制。

        :param SearchRecordingsRequest request
        :return: SearchRecordingsResponse
        """

        all_params = ['start_date', 'end_date', 'user_uuid', 'offset', 'limit', 'query_all', 'search_key', 'sort_type', 'x_authorization_type', 'x_site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'query_all' in local_var_params:
            query_params.append(('queryAll', local_var_params['query_all']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'start_date' in local_var_params:
            query_params.append(('startDate', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('endDate', local_var_params['end_date']))
        if 'sort_type' in local_var_params:
            query_params.append(('sortType', local_var_params['sort_type']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/record/files',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchRecordingsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def search_resource_async(self, request):
        """分页查询企业资源

        sp根据条件查询企业的资源项

        :param SearchResourceRequest request
        :return: SearchResourceResponse
        """
        return self.search_resource_with_http_info(request)

    def search_resource_with_http_info(self, request):
        """分页查询企业资源

        sp根据条件查询企业的资源项

        :param SearchResourceRequest request
        :return: SearchResourceResponse
        """

        all_params = ['corp_id', 'x_request_id', 'accept_language', 'offset', 'limit', 'search_key', 'start_expire_date', 'end_expire_date', 'type', 'type_id', 'status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'corp_id' in local_var_params:
            path_params['corp_id'] = local_var_params['corp_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'start_expire_date' in local_var_params:
            query_params.append(('startExpireDate', local_var_params['start_expire_date']))
        if 'end_expire_date' in local_var_params:
            query_params.append(('endExpireDate', local_var_params['end_expire_date']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'type_id' in local_var_params:
            query_params.append(('typeId', local_var_params['type_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/sp/corp/{corp_id}/resource',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def search_resource_op_record_async(self, request):
        """分页查询企业资源操作记录

        sp根据条件查询企业的资源操作记录，支持根据resourceId模糊搜索

        :param SearchResourceOpRecordRequest request
        :return: SearchResourceOpRecordResponse
        """
        return self.search_resource_op_record_with_http_info(request)

    def search_resource_op_record_with_http_info(self, request):
        """分页查询企业资源操作记录

        sp根据条件查询企业的资源操作记录，支持根据resourceId模糊搜索

        :param SearchResourceOpRecordRequest request
        :return: SearchResourceOpRecordResponse
        """

        all_params = ['corp_id', 'x_request_id', 'accept_language', 'offset', 'limit', 'search_key', 'start_expire_date', 'end_expire_date', 'start_operate_date', 'end_operate_date', 'type', 'type_id', 'operate_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'corp_id' in local_var_params:
            path_params['corp_id'] = local_var_params['corp_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'start_expire_date' in local_var_params:
            query_params.append(('startExpireDate', local_var_params['start_expire_date']))
        if 'end_expire_date' in local_var_params:
            query_params.append(('endExpireDate', local_var_params['end_expire_date']))
        if 'start_operate_date' in local_var_params:
            query_params.append(('startOperateDate', local_var_params['start_operate_date']))
        if 'end_operate_date' in local_var_params:
            query_params.append(('endOperateDate', local_var_params['end_operate_date']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'type_id' in local_var_params:
            query_params.append(('typeId', local_var_params['type_id']))
        if 'operate_type' in local_var_params:
            query_params.append(('operateType', local_var_params['operate_type']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/sp/corp/{corp_id}/resource-record',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchResourceOpRecordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def search_users_async(self, request):
        """分页查询用户

        企业管理员通过该接口分页查询企业用户。

        :param SearchUsersRequest request
        :return: SearchUsersResponse
        """
        return self.search_users_with_http_info(request)

    def search_users_with_http_info(self, request):
        """分页查询用户

        企业管理员通过该接口分页查询企业用户。

        :param SearchUsersRequest request
        :return: SearchUsersResponse
        """

        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key', 'sort_field', 'is_asc', 'dept_code', 'enable_sub_dept', 'admin_type', 'enable_room', 'user_type', 'status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'sort_field' in local_var_params:
            query_params.append(('sortField', local_var_params['sort_field']))
        if 'is_asc' in local_var_params:
            query_params.append(('isAsc', local_var_params['is_asc']))
        if 'dept_code' in local_var_params:
            query_params.append(('deptCode', local_var_params['dept_code']))
        if 'enable_sub_dept' in local_var_params:
            query_params.append(('enableSubDept', local_var_params['enable_sub_dept']))
        if 'admin_type' in local_var_params:
            query_params.append(('adminType', local_var_params['admin_type']))
        if 'enable_room' in local_var_params:
            query_params.append(('enableRoom', local_var_params['enable_room']))
        if 'user_type' in local_var_params:
            query_params.append(('userType', local_var_params['user_type']))
            collection_formats['userType'] = 'csv'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/corp/member',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def send_slide_verify_code_async(self, request):
        """发送滑块验证码

        该接口提供发送滑块验证码。服务器收到请求，返回抠图以及抠图后的原图等结果。需要在前台界面显示出抠图以及抠图后的原图，用户通过滑块操作来匹配图形。

        :param SendSlideVerifyCodeRequest request
        :return: SendSlideVerifyCodeResponse
        """
        return self.send_slide_verify_code_with_http_info(request)

    def send_slide_verify_code_with_http_info(self, request):
        """发送滑块验证码

        该接口提供发送滑块验证码。服务器收到请求，返回抠图以及抠图后的原图等结果。需要在前台界面显示出抠图以及抠图后的原图，用户通过滑块操作来匹配图形。

        :param SendSlideVerifyCodeRequest request
        :return: SendSlideVerifyCodeResponse
        """

        all_params = ['slide_verify_code_send_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/acs/auth/slideverifycode/send',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SendSlideVerifyCodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def send_veri_code_for_change_pwd_async(self, request):
        """发送验证码

        该接口提供发送验证码，服务器收到请求，发送验证码到邮箱或者短信并返回结果。用户在前台界面通过滑块验证后，再进行发送验证码操作。

        :param SendVeriCodeForChangePwdRequest request
        :return: SendVeriCodeForChangePwdResponse
        """
        return self.send_veri_code_for_change_pwd_with_http_info(request)

    def send_veri_code_for_change_pwd_with_http_info(self, request):
        """发送验证码

        该接口提供发送验证码，服务器收到请求，发送验证码到邮箱或者短信并返回结果。用户在前台界面通过滑块验证后，再进行发送验证码操作。

        :param SendVeriCodeForChangePwdRequest request
        :return: SendVeriCodeForChangePwdResponse
        """

        all_params = ['verify_code_send_dtov1', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/acs/verifycode/send',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SendVeriCodeForChangePwdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def send_veri_code_for_update_user_info_async(self, request):
        """获取验证码

        获取验证码，向手机或邮箱发送，一分钟内只会发送一次。

        :param SendVeriCodeForUpdateUserInfoRequest request
        :return: SendVeriCodeForUpdateUserInfoResponse
        """
        return self.send_veri_code_for_update_user_info_with_http_info(request)

    def send_veri_code_for_update_user_info_with_http_info(self, request):
        """获取验证码

        获取验证码，向手机或邮箱发送，一分钟内只会发送一次。

        :param SendVeriCodeForUpdateUserInfoRequest request
        :return: SendVeriCodeForUpdateUserInfoResponse
        """

        all_params = ['verification_code_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/member/verification-code',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SendVeriCodeForUpdateUserInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def set_custom_multi_picture_async(self, request):
        """设置自定义多画面

        场景描述：会议管理员在confportal手动设置多画面 功能描述：提供给会议管理员手动设置多画面的功能

        :param SetCustomMultiPictureRequest request
        :return: SetCustomMultiPictureResponse
        """
        return self.set_custom_multi_picture_with_http_info(request)

    def set_custom_multi_picture_with_http_info(self, request):
        """设置自定义多画面

        场景描述：会议管理员在confportal手动设置多画面 功能描述：提供给会议管理员手动设置多画面的功能

        :param SetCustomMultiPictureRequest request
        :return: SetCustomMultiPictureResponse
        """

        all_params = ['conference_id', 'x_conference_authorization', 'req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/display/customMultiPicture',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SetCustomMultiPictureResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def set_host_view_async(self, request):
        """主持人选看

        用于主持人轮询、主持人选看多画面、主持人选看会场操作。目前只适用于硬终端为主持人的场景。

        :param SetHostViewRequest request
        :return: SetHostViewResponse
        """
        return self.set_host_view_with_http_info(request)

    def set_host_view_with_http_info(self, request):
        """主持人选看

        用于主持人轮询、主持人选看多画面、主持人选看会场操作。目前只适用于硬终端为主持人的场景。

        :param SetHostViewRequest request
        :return: SetHostViewResponse
        """

        all_params = ['conference_id', 'x_conference_authorization', 'req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/chairView',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SetHostViewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def set_multi_picture_async(self, request):
        """设置多画面

        设置会议多画面。

        :param SetMultiPictureRequest request
        :return: SetMultiPictureResponse
        """
        return self.set_multi_picture_with_http_info(request)

    def set_multi_picture_with_http_info(self, request):
        """设置多画面

        设置会议多画面。

        :param SetMultiPictureRequest request
        :return: SetMultiPictureResponse
        """

        all_params = ['conference_id', 'x_conference_authorization', 'req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/display/multiPicture',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SetMultiPictureResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def set_participant_view_async(self, request):
        """会场选看

        目前只适用于硬终端选看其他会场人的场景。

        :param SetParticipantViewRequest request
        :return: SetParticipantViewResponse
        """
        return self.set_participant_view_with_http_info(request)

    def set_participant_view_with_http_info(self, request):
        """会场选看

        目前只适用于硬终端选看其他会场人的场景。

        :param SetParticipantViewRequest request
        :return: SetParticipantViewResponse
        """

        all_params = ['conference_id', 'participant_id', 'x_conference_authorization', 'req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'participant_id' in local_var_params:
            query_params.append(('participantID', local_var_params['participant_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/partView',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SetParticipantViewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def set_role_async(self, request):
        """申请主持人

        申请或释放主持人。普通用户可申请主持人，主持人可释放主持人权限。

        :param SetRoleRequest request
        :return: SetRoleResponse
        """
        return self.set_role_with_http_info(request)

    def set_role_with_http_info(self, request):
        """申请主持人

        申请或释放主持人。普通用户可申请主持人，主持人可释放主持人权限。

        :param SetRoleRequest request
        :return: SetRoleResponse
        """

        all_params = ['conference_id', 'participant_id', 'x_conference_authorization', 'rest_chair_token_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'participant_id' in local_var_params:
            query_params.append(('participantID', local_var_params['participant_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/participants/role',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SetRoleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_conf_org_async(self, request):
        """通过会议ID查询企业ID

        与某个会议在同一个SP下的用户，可以通过会议ID查询到该会议对应的企业ID。

        :param ShowConfOrgRequest request
        :return: ShowConfOrgResponse
        """
        return self.show_conf_org_with_http_info(request)

    def show_conf_org_with_http_info(self, request):
        """通过会议ID查询企业ID

        与某个会议在同一个SP下的用户，可以通过会议ID查询到该会议对应的企业ID。

        :param ShowConfOrgRequest request
        :return: ShowConfOrgResponse
        """

        all_params = ['conference_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/conferences/confOrg',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowConfOrgResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_corp_async(self, request):
        """SP管理员查询企业

        获取企业

        :param ShowCorpRequest request
        :return: ShowCorpResponse
        """
        return self.show_corp_with_http_info(request)

    def show_corp_with_http_info(self, request):
        """SP管理员查询企业

        获取企业

        :param ShowCorpRequest request
        :return: ShowCorpResponse
        """

        all_params = ['id', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/sp/corp/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCorpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_corp_admin_async(self, request):
        """查询企业管理员

        通过该接口查询企业管理员。

        :param ShowCorpAdminRequest request
        :return: ShowCorpAdminResponse
        """
        return self.show_corp_admin_with_http_info(request)

    def show_corp_admin_with_http_info(self, request):
        """查询企业管理员

        通过该接口查询企业管理员。

        :param ShowCorpAdminRequest request
        :return: ShowCorpAdminResponse
        """

        all_params = ['account', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'account' in local_var_params:
            path_params['account'] = local_var_params['account']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/corp/admin/{account}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCorpAdminResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_corp_basic_info_async(self, request):
        """企业管理员查询企业注册信息

        企业管理员通过该接口查询企业注册信息。

        :param ShowCorpBasicInfoRequest request
        :return: ShowCorpBasicInfoResponse
        """
        return self.show_corp_basic_info_with_http_info(request)

    def show_corp_basic_info_with_http_info(self, request):
        """企业管理员查询企业注册信息

        企业管理员通过该接口查询企业注册信息。

        :param ShowCorpBasicInfoRequest request
        :return: ShowCorpBasicInfoResponse
        """

        all_params = ['x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/corp',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCorpBasicInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_corp_resource_async(self, request):
        """企业管理员查询企业内资源及业务权限

        企业管理员通过该接口查询企业内资源及业务权限，包括查询已使用的资源情况。

        :param ShowCorpResourceRequest request
        :return: ShowCorpResourceResponse
        """
        return self.show_corp_resource_with_http_info(request)

    def show_corp_resource_with_http_info(self, request):
        """企业管理员查询企业内资源及业务权限

        企业管理员通过该接口查询企业内资源及业务权限，包括查询已使用的资源情况。

        :param ShowCorpResourceRequest request
        :return: ShowCorpResourceResponse
        """

        all_params = ['x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/corp/resource',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCorpResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_dept_and_child_dept_async(self, request):
        """查询部门及其一级子部门列表

        企业管理员通过该接口查询部门及其一级子部门列表。

        :param ShowDeptAndChildDeptRequest request
        :return: ShowDeptAndChildDeptResponse
        """
        return self.show_dept_and_child_dept_with_http_info(request)

    def show_dept_and_child_dept_with_http_info(self, request):
        """查询部门及其一级子部门列表

        企业管理员通过该接口查询部门及其一级子部门列表。

        :param ShowDeptAndChildDeptRequest request
        :return: ShowDeptAndChildDeptResponse
        """

        all_params = ['dept_code', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'dept_code' in local_var_params:
            path_params['dept_code'] = local_var_params['dept_code']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/member/dept/{dept_code}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDeptAndChildDeptResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_device_detail_async(self, request):
        """查询终端详情

        企业管理员通过该接口查询终端详情。

        :param ShowDeviceDetailRequest request
        :return: ShowDeviceDetailResponse
        """
        return self.show_device_detail_with_http_info(request)

    def show_device_detail_with_http_info(self, request):
        """查询终端详情

        企业管理员通过该接口查询终端详情。

        :param ShowDeviceDetailRequest request
        :return: ShowDeviceDetailResponse
        """

        all_params = ['sn', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'sn' in local_var_params:
            path_params['sn'] = local_var_params['sn']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/corp/device/{sn}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDeviceDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_device_status_async(self, request):
        """查询设备状态

        调用本接口可以查询硬终端的状态。 硬终端与发起查询请求的帐号需在同一企业下，否则会鉴权失败。 

        :param ShowDeviceStatusRequest request
        :return: ShowDeviceStatusResponse
        """
        return self.show_device_status_with_http_info(request)

    def show_device_status_with_http_info(self, request):
        """查询设备状态

        调用本接口可以查询硬终端的状态。 硬终端与发起查询请求的帐号需在同一企业下，否则会鉴权失败。 

        :param ShowDeviceStatusRequest request
        :return: ShowDeviceStatusResponse
        """

        all_params = ['number', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/acs/ap/userstatus',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDeviceStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_device_types_async(self, request):
        """获取所有终端类型

        企业管理员通过该接口获取所有的终端类型。

        :param ShowDeviceTypesRequest request
        :return: ShowDeviceTypesResponse
        """
        return self.show_device_types_with_http_info(request)

    def show_device_types_with_http_info(self, request):
        """获取所有终端类型

        企业管理员通过该接口获取所有的终端类型。

        :param ShowDeviceTypesRequest request
        :return: ShowDeviceTypesResponse
        """

        all_params = ['x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/termdevtype',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDeviceTypesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_his_meeting_detail_async(self, request):
        """查询历史会议详情

        管理员可以查询管理权限域内所有的历史会议详情，普通用户仅能查询当前帐号管理的历史会议详情。

        :param ShowHisMeetingDetailRequest request
        :return: ShowHisMeetingDetailResponse
        """
        return self.show_his_meeting_detail_with_http_info(request)

    def show_his_meeting_detail_with_http_info(self, request):
        """查询历史会议详情

        管理员可以查询管理权限域内所有的历史会议详情，普通用户仅能查询当前帐号管理的历史会议详情。

        :param ShowHisMeetingDetailRequest request
        :return: ShowHisMeetingDetailResponse
        """

        all_params = ['conf_uuid', 'offset', 'limit', 'search_key', 'user_uuid', 'x_type', 'x_query_type', 'x_authorization_type', 'x_site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conf_uuid' in local_var_params:
            query_params.append(('confUUID', local_var_params['conf_uuid']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))

        header_params = {}
        if 'x_type' in local_var_params:
            header_params['X-Type'] = local_var_params['x_type']
        if 'x_query_type' in local_var_params:
            header_params['X-Query-Type'] = local_var_params['x_query_type']
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/conferences/history/confDetail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowHisMeetingDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_meeting_detail_async(self, request):
        """查询会议详情

        管理员可以查询管理权限域内所有会议的详情，普通用户仅能查询当前帐号管理的会议详情。

        :param ShowMeetingDetailRequest request
        :return: ShowMeetingDetailResponse
        """
        return self.show_meeting_detail_with_http_info(request)

    def show_meeting_detail_with_http_info(self, request):
        """查询会议详情

        管理员可以查询管理权限域内所有会议的详情，普通用户仅能查询当前帐号管理的会议详情。

        :param ShowMeetingDetailRequest request
        :return: ShowMeetingDetailResponse
        """

        all_params = ['conference_id', 'offset', 'limit', 'search_key', 'user_uuid', 'x_type', 'x_query_type', 'x_authorization_type', 'x_site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))

        header_params = {}
        if 'x_type' in local_var_params:
            header_params['X-Type'] = local_var_params['x_type']
        if 'x_query_type' in local_var_params:
            header_params['X-Query-Type'] = local_var_params['x_query_type']
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/conferences/confDetail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMeetingDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_meeting_file_async(self, request):
        """查询会议纪要详情

        用户查询单个会议纪要详情（主要目的是为了得到外链）。 IdeaHub是使用fileCode来查，所以终端保持一致。

        :param ShowMeetingFileRequest request
        :return: ShowMeetingFileResponse
        """
        return self.show_meeting_file_with_http_info(request)

    def show_meeting_file_with_http_info(self, request):
        """查询会议纪要详情

        用户查询单个会议纪要详情（主要目的是为了得到外链）。 IdeaHub是使用fileCode来查，所以终端保持一致。

        :param ShowMeetingFileRequest request
        :return: ShowMeetingFileResponse
        """

        all_params = ['file_code', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'file_code' in local_var_params:
            path_params['file_code'] = local_var_params['file_code']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/sss/meeting-files/{file_code}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMeetingFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_meeting_file_list_async(self, request):
        """打开会议纪要文件列表

        用户使用手机扫码后，手机端请求服务端，让服务端通知指定IdeaHub打开指定用户的会议纪要文件列表。二维码内容  cloudlink://cloudlink.huawei.com/h5page?action=OPEN_MEETING_FILE_LIST&key1=value1&key2=value2    key/value的个数可能变化，终端解析后，在发起后续请求时，将所有key/value存为map，作为入参即可。

        :param ShowMeetingFileListRequest request
        :return: ShowMeetingFileListResponse
        """
        return self.show_meeting_file_list_with_http_info(request)

    def show_meeting_file_list_with_http_info(self, request):
        """打开会议纪要文件列表

        用户使用手机扫码后，手机端请求服务端，让服务端通知指定IdeaHub打开指定用户的会议纪要文件列表。二维码内容  cloudlink://cloudlink.huawei.com/h5page?action=OPEN_MEETING_FILE_LIST&key1=value1&key2=value2    key/value的个数可能变化，终端解析后，在发起后续请求时，将所有key/value存为map，作为入参即可。

        :param ShowMeetingFileListRequest request
        :return: ShowMeetingFileListResponse
        """

        all_params = ['info', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/sss/meeting-files/open-meeting-file-list',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMeetingFileListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_my_info_async(self, request):
        """用户查询自己的信息

        企业用户通过该接口查询自己的信息。

        :param ShowMyInfoRequest request
        :return: ShowMyInfoResponse
        """
        return self.show_my_info_with_http_info(request)

    def show_my_info_with_http_info(self, request):
        """用户查询自己的信息

        企业用户通过该接口查询自己的信息。

        :param ShowMyInfoRequest request
        :return: ShowMyInfoResponse
        """

        all_params = ['x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/member',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMyInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_online_meeting_detail_async(self, request):
        """查询在线会议详情

        管理员可以查询管理权限域内所有的在线会议详情，普通用户仅能查询当前自己的帐号管理的在线会议详情。

        :param ShowOnlineMeetingDetailRequest request
        :return: ShowOnlineMeetingDetailResponse
        """
        return self.show_online_meeting_detail_with_http_info(request)

    def show_online_meeting_detail_with_http_info(self, request):
        """查询在线会议详情

        管理员可以查询管理权限域内所有的在线会议详情，普通用户仅能查询当前自己的帐号管理的在线会议详情。

        :param ShowOnlineMeetingDetailRequest request
        :return: ShowOnlineMeetingDetailResponse
        """

        all_params = ['conference_id', 'offset', 'limit', 'search_key', 'user_uuid', 'x_type', 'x_query_type', 'x_authorization_type', 'x_site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))

        header_params = {}
        if 'x_type' in local_var_params:
            header_params['X-Type'] = local_var_params['x_type']
        if 'x_query_type' in local_var_params:
            header_params['X-Query-Type'] = local_var_params['x_query_type']
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/conferences/online/confDetail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowOnlineMeetingDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_program_async(self, request):
        """根据ID查询节目详情

        根据ID获取节目详情

        :param ShowProgramRequest request
        :return: ShowProgramResponse
        """
        return self.show_program_with_http_info(request)

    def show_program_with_http_info(self, request):
        """根据ID查询节目详情

        根据ID获取节目详情

        :param ShowProgramRequest request
        :return: ShowProgramResponse
        """

        all_params = ['id', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/sss/programs/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowProgramResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_publication_async(self, request):
        """根据ID查询全球窗发布详情

        根据ID获取发布详情

        :param ShowPublicationRequest request
        :return: ShowPublicationResponse
        """
        return self.show_publication_with_http_info(request)

    def show_publication_with_http_info(self, request):
        """根据ID查询全球窗发布详情

        根据ID获取发布详情

        :param ShowPublicationRequest request
        :return: ShowPublicationResponse
        """

        all_params = ['id', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/sss/publications/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPublicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_real_time_info_of_meeting_async(self, request):
        """查询会议实时信息

        查询会议实时信息

        :param ShowRealTimeInfoOfMeetingRequest request
        :return: ShowRealTimeInfoOfMeetingResponse
        """
        return self.show_real_time_info_of_meeting_with_http_info(request)

    def show_real_time_info_of_meeting_with_http_info(self, request):
        """查询会议实时信息

        查询会议实时信息

        :param ShowRealTimeInfoOfMeetingRequest request
        :return: ShowRealTimeInfoOfMeetingResponse
        """

        all_params = ['conference_id', 'x_conference_authorization']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/control/conferences/realTimeInfo',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRealTimeInfoOfMeetingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_recording_detail_async(self, request):
        """查询录制详情

        查询某个录制详情。

        :param ShowRecordingDetailRequest request
        :return: ShowRecordingDetailResponse
        """
        return self.show_recording_detail_with_http_info(request)

    def show_recording_detail_with_http_info(self, request):
        """查询录制详情

        查询某个录制详情。

        :param ShowRecordingDetailRequest request
        :return: ShowRecordingDetailResponse
        """

        all_params = ['conf_uuid', 'user_uuid', 'x_authorization_type', 'x_site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conf_uuid' in local_var_params:
            query_params.append(('confUUID', local_var_params['conf_uuid']))
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/conferences/record/files',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRecordingDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_region_info_of_meeting_async(self, request):
        """查询会议所在区域信息

        查询会议所在区域信息，如果会议不存在或者会议未召开，返回对应的错误码。

        :param ShowRegionInfoOfMeetingRequest request
        :return: ShowRegionInfoOfMeetingResponse
        """
        return self.show_region_info_of_meeting_with_http_info(request)

    def show_region_info_of_meeting_with_http_info(self, request):
        """查询会议所在区域信息

        查询会议所在区域信息，如果会议不存在或者会议未召开，返回对应的错误码。

        :param ShowRegionInfoOfMeetingRequest request
        :return: ShowRegionInfoOfMeetingResponse
        """

        all_params = ['conference_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/conferences/region/info',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRegionInfoOfMeetingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_sp_res_async(self, request):
        """查询SP的共享资源使用信息

        SP管理查询所属SP的共享资源使用信息

        :param ShowSpResRequest request
        :return: ShowSpResResponse
        """
        return self.show_sp_res_with_http_info(request)

    def show_sp_res_with_http_info(self, request):
        """查询SP的共享资源使用信息

        SP管理查询所属SP的共享资源使用信息

        :param ShowSpResRequest request
        :return: ShowSpResResponse
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


        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/management/spRes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowSpResResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_user_detail_async(self, request):
        """查询用户详情

        企业管理员通过该接口查询企业用户详情

        :param ShowUserDetailRequest request
        :return: ShowUserDetailResponse
        """
        return self.show_user_detail_with_http_info(request)

    def show_user_detail_with_http_info(self, request):
        """查询用户详情

        企业管理员通过该接口查询企业用户详情

        :param ShowUserDetailRequest request
        :return: ShowUserDetailResponse
        """

        all_params = ['account', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'account' in local_var_params:
            path_params['account'] = local_var_params['account']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/dcs/corp/member/{account}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowUserDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def stop_meeting_async(self, request):
        """结束会议

        结束会议。

        :param StopMeetingRequest request
        :return: StopMeetingResponse
        """
        return self.stop_meeting_with_http_info(request)

    def stop_meeting_with_http_info(self, request):
        """结束会议

        结束会议。

        :param StopMeetingRequest request
        :return: StopMeetingResponse
        """

        all_params = ['conference_id', 'x_conference_authorization']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/mmc/control/conferences/stop',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StopMeetingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def switch_mode_async(self, request):
        """切换视频显示策略

        切换视频显示策略

        :param SwitchModeRequest request
        :return: SwitchModeResponse
        """
        return self.switch_mode_with_http_info(request)

    def switch_mode_with_http_info(self, request):
        """切换视频显示策略

        切换视频显示策略

        :param SwitchModeRequest request
        :return: SwitchModeResponse
        """

        all_params = ['conference_id', 'x_conference_authorization', 'req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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
            resource_path='/v1/mmc/control/conferences/display/mode',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SwitchModeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_contact_async(self, request):
        """修改手机或邮箱

        企业用户通过该接口修改手机或邮箱，需要先获取验证码，验证多次失败会禁止修改。

        :param UpdateContactRequest request
        :return: UpdateContactResponse
        """
        return self.update_contact_with_http_info(request)

    def update_contact_with_http_info(self, request):
        """修改手机或邮箱

        企业用户通过该接口修改手机或邮箱，需要先获取验证码，验证多次失败会禁止修改。

        :param UpdateContactRequest request
        :return: UpdateContactResponse
        """

        all_params = ['verification_code_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/member/contact',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateContactResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_corp_async(self, request):
        """SP管理员修改企业

        修改企业，若任一参数为null或者不携带则不修改

        :param UpdateCorpRequest request
        :return: UpdateCorpResponse
        """
        return self.update_corp_with_http_info(request)

    def update_corp_with_http_info(self, request):
        """SP管理员修改企业

        修改企业，若任一参数为null或者不携带则不修改

        :param UpdateCorpRequest request
        :return: UpdateCorpResponse
        """

        all_params = ['id', 'corp_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/sp/corp/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateCorpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_corp_basic_info_async(self, request):
        """企业管理员修改企业注册信息

        企业管理员通过该接口修改企业注册信息。当前只支持修改地址。

        :param UpdateCorpBasicInfoRequest request
        :return: UpdateCorpBasicInfoResponse
        """
        return self.update_corp_basic_info_with_http_info(request)

    def update_corp_basic_info_with_http_info(self, request):
        """企业管理员修改企业注册信息

        企业管理员通过该接口修改企业注册信息。当前只支持修改地址。

        :param UpdateCorpBasicInfoRequest request
        :return: UpdateCorpBasicInfoResponse
        """

        all_params = ['mod_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateCorpBasicInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_department_async(self, request):
        """修改部门

        企业管理员通过该接口修改部门。

        :param UpdateDepartmentRequest request
        :return: UpdateDepartmentResponse
        """
        return self.update_department_with_http_info(request)

    def update_department_with_http_info(self, request):
        """修改部门

        企业管理员通过该接口修改部门。

        :param UpdateDepartmentRequest request
        :return: UpdateDepartmentResponse
        """

        all_params = ['dept_code', 'dept_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'dept_code' in local_var_params:
            path_params['dept_code'] = local_var_params['dept_code']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/dept/{dept_code}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateDepartmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_device_async(self, request):
        """修改终端

        企业管理员通过该接口修改终端。

        :param UpdateDeviceRequest request
        :return: UpdateDeviceResponse
        """
        return self.update_device_with_http_info(request)

    def update_device_with_http_info(self, request):
        """修改终端

        企业管理员通过该接口修改终端。

        :param UpdateDeviceRequest request
        :return: UpdateDeviceResponse
        """

        all_params = ['sn', 'device_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'sn' in local_var_params:
            path_params['sn'] = local_var_params['sn']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/device/{sn}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_material_async(self, request):
        """更新全球窗素材

        更新全球窗素材

        :param UpdateMaterialRequest request
        :return: UpdateMaterialResponse
        """
        return self.update_material_with_http_info(request)

    def update_material_with_http_info(self, request):
        """更新全球窗素材

        更新全球窗素材

        :param UpdateMaterialRequest request
        :return: UpdateMaterialResponse
        """

        all_params = ['id', 'update_material_request_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/sss/materials/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateMaterialResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_member_vmr_async(self, request):
        """修改用户云会议室

        企业用户登录后可以修改分配给用户的专用云会议室及个人云会议室。

        :param UpdateMemberVmrRequest request
        :return: UpdateMemberVmrResponse
        """
        return self.update_member_vmr_with_http_info(request)

    def update_member_vmr_with_http_info(self, request):
        """修改用户云会议室

        企业用户登录后可以修改分配给用户的专用云会议室及个人云会议室。

        :param UpdateMemberVmrRequest request
        :return: UpdateMemberVmrResponse
        """

        all_params = ['id', 'mod_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/member/vmr/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateMemberVmrResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_my_info_async(self, request):
        """用户修改自己的信息

        企业用户通过该接口修改自己的信息。

        :param UpdateMyInfoRequest request
        :return: UpdateMyInfoResponse
        """
        return self.update_my_info_with_http_info(request)

    def update_my_info_with_http_info(self, request):
        """用户修改自己的信息

        企业用户通过该接口修改自己的信息。

        :param UpdateMyInfoRequest request
        :return: UpdateMyInfoResponse
        """

        all_params = ['member_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/member',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateMyInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_program_async(self, request):
        """更新全球窗节目

        更新全球窗节目

        :param UpdateProgramRequest request
        :return: UpdateProgramResponse
        """
        return self.update_program_with_http_info(request)

    def update_program_with_http_info(self, request):
        """更新全球窗节目

        更新全球窗节目

        :param UpdateProgramRequest request
        :return: UpdateProgramResponse
        """

        all_params = ['id', 'program_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/sss/programs/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateProgramResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_publication_async(self, request):
        """修改全球窗发布

        修改全球窗发布

        :param UpdatePublicationRequest request
        :return: UpdatePublicationResponse
        """
        return self.update_publication_with_http_info(request)

    def update_publication_with_http_info(self, request):
        """修改全球窗发布

        修改全球窗发布

        :param UpdatePublicationRequest request
        :return: UpdatePublicationResponse
        """

        all_params = ['id', 'publication_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/sss/publications/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePublicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_pwd_async(self, request):
        """修改密码

        企业成员通过该接口提供用户修改密码功能，服务器收到请求，修改用户密码并返回结果。

        :param UpdatePwdRequest request
        :return: UpdatePwdResponse
        """
        return self.update_pwd_with_http_info(request)

    def update_pwd_with_http_info(self, request):
        """修改密码

        企业成员通过该接口提供用户修改密码功能，服务器收到请求，修改用户密码并返回结果。

        :param UpdatePwdRequest request
        :return: UpdatePwdResponse
        """

        all_params = ['mod_pwd_req_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/acs/password',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePwdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_resource_async(self, request):
        """修改企业资源

        企业修改资源的过期时间、停用状态

        :param UpdateResourceRequest request
        :return: UpdateResourceResponse
        """
        return self.update_resource_with_http_info(request)

    def update_resource_with_http_info(self, request):
        """修改企业资源

        企业修改资源的过期时间、停用状态

        :param UpdateResourceRequest request
        :return: UpdateResourceResponse
        """

        all_params = ['corp_id', 'resource_list', 'x_request_id', 'accept_language', 'force_edit_flag']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'corp_id' in local_var_params:
            path_params['corp_id'] = local_var_params['corp_id']

        query_params = []
        if 'force_edit_flag' in local_var_params:
            query_params.append(('forceEditFlag', local_var_params['force_edit_flag']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/sp/corp/{corp_id}/resource',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_token_async(self, request):
        """刷新Token

        该接口提供刷新Token功能，根据传入的Token，刷新Token失效时间并返回结果。

        :param UpdateTokenRequest request
        :return: UpdateTokenResponse
        """
        return self.update_token_with_http_info(request)

    def update_token_with_http_info(self, request):
        """刷新Token

        该接口提供刷新Token功能，根据传入的Token，刷新Token失效时间并返回结果。

        :param UpdateTokenRequest request
        :return: UpdateTokenResponse
        """

        all_params = ['x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v1/usg/acs/token',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateTokenResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_user_async(self, request):
        """修改用户

        企业管理员通过该接口修改企业用户。

        :param UpdateUserRequest request
        :return: UpdateUserResponse
        """
        return self.update_user_with_http_info(request)

    def update_user_with_http_info(self, request):
        """修改用户

        企业管理员通过该接口修改企业用户。

        :param UpdateUserRequest request
        :return: UpdateUserResponse
        """

        all_params = ['account', 'user_dto', 'x_request_id', 'accept_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'account' in local_var_params:
            path_params['account'] = local_var_params['account']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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
            resource_path='/v1/usg/dcs/corp/member/{account}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateUserResponse',
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
