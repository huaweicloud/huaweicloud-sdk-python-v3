# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

import six

from huaweicloudsdkcore.client import Client
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils


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
        :return: tuple(AddCorpResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['corp_dto', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/sp/corp', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddCorpResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_corp_admin_async(self, request):
        """添加企业管理员

        企业默认管理员添加企业普通管理员

        :param AddCorpAdminRequest request
        :return: None
        """
        return self.add_corp_admin_with_http_info(request)

    def add_corp_admin_with_http_info(self, request):
        """添加企业管理员

        企业默认管理员添加企业普通管理员

        :param AddCorpAdminRequest request
        :return: None
        """

        all_params = ['admin_dto', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/corp/admin', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
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
        :return: tuple(AddDepartmentResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['dept_dto', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/corp/dept', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddDepartmentResponse',
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
        :return: tuple(AddDeviceResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['device_dto', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/corp/device', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddDeviceResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_resource_async(self, request):
        """分配企业资源

        企业新增资源发放。优化适配，该接口同时支持修改，带resourceId后会判断该资源是否存在，存在即修改（支持修改的参数见修改接口），否则按新增处理

        :param AddResourceRequest request
        :return: None
        """
        return self.add_resource_with_http_info(request)

    def add_resource_with_http_info(self, request):
        """分配企业资源

        企业新增资源发放。优化适配，该接口同时支持修改，带resourceId后会判断该资源是否存在，存在即修改（支持修改的参数见修改接口），否则按新增处理

        :param AddResourceRequest request
        :return: None
        """

        all_params = ['corp_id', 'resource_list', 'x_request_id', 'accept_language', 'force_edit_flag']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/sp/corp/{corp_id}/resource', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
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
        :return: tuple(AddUserResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['user_dto', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/corp/member', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddUserResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_vmr_async(self, request):
        """分配专用云会议室

        企业管理员通过该接口将云会议室分配给用户、硬终端（当前仅支持分配TE10、TE20、HUAWEI Board、HUAWEI Bar 500及HUAWEI Box系列硬件终端）。云会议室分配给硬件终端后，需要重启或重新激活硬件终端。若需要管理云会议室、预约会议、录制会议或进行完整的会控操作，请同时将该云会议室分配给会议用户。

        :param AssociateVmrRequest request
        :return: None
        """
        return self.associate_vmr_with_http_info(request)

    def associate_vmr_with_http_info(self, request):
        """分配专用云会议室

        企业管理员通过该接口将云会议室分配给用户、硬终端（当前仅支持分配TE10、TE20、HUAWEI Board、HUAWEI Bar 500及HUAWEI Box系列硬件终端）。云会议室分配给硬件终端后，需要重启或重新激活硬件终端。若需要管理云会议室、预约会议、录制会议或进行完整的会控操作，请同时将该云会议室分配给会议用户。

        :param AssociateVmrRequest request
        :return: None
        """

        all_params = ['account', 'assign_list', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/corp/vmr/assign-to-member/{account}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_corp_admins_async(self, request):
        """批量删除企业管理员

        批量删除企业管理员

        :param BatchDeleteCorpAdminsRequest request
        :return: None
        """
        return self.batch_delete_corp_admins_with_http_info(request)

    def batch_delete_corp_admins_with_http_info(self, request):
        """批量删除企业管理员

        批量删除企业管理员

        :param BatchDeleteCorpAdminsRequest request
        :return: None
        """

        all_params = ['del_list', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/corp/admin/delete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_devices_async(self, request):
        """批量删除终端

        企业管理员通过该接口批量删除终端，返回删除失败的列表。

        :param BatchDeleteDevicesRequest request
        :return: None
        """
        return self.batch_delete_devices_with_http_info(request)

    def batch_delete_devices_with_http_info(self, request):
        """批量删除终端

        企业管理员通过该接口批量删除终端，返回删除失败的列表。

        :param BatchDeleteDevicesRequest request
        :return: None
        """

        all_params = ['del_list', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/corp/device/delete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_users_async(self, request):
        """批量删除用户

        企业管理员通过该接口批量删除企业用户，全量成功或全量失败。

        :param BatchDeleteUsersRequest request
        :return: None
        """
        return self.batch_delete_users_with_http_info(request)

    def batch_delete_users_with_http_info(self, request):
        """批量删除用户

        企业管理员通过该接口批量删除企业用户，全量成功或全量失败。

        :param BatchDeleteUsersRequest request
        :return: None
        """

        all_params = ['del_list', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/corp/member/delete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_update_devices_status_async(self, request):
        """批量修改终端状态

        批量修改终端状态

        :param BatchUpdateDevicesStatusRequest request
        :return: None
        """
        return self.batch_update_devices_status_with_http_info(request)

    def batch_update_devices_status_with_http_info(self, request):
        """批量修改终端状态

        批量修改终端状态

        :param BatchUpdateDevicesStatusRequest request
        :return: None
        """

        all_params = ['value', 'sn_list', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/corp/device/status/{value}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_update_user_status_async(self, request):
        """批量修改用户状态

        企业管理员通过该接口批量修改用户状态，当用户账号数资源或者第三方电子白板资源到期后，若企业内对应资源的用户账号超过数量后会被系统随机自动停用，此时可通过该接口修改用户的状态。

        :param BatchUpdateUserStatusRequest request
        :return: None
        """
        return self.batch_update_user_status_with_http_info(request)

    def batch_update_user_status_with_http_info(self, request):
        """批量修改用户状态

        企业管理员通过该接口批量修改用户状态，当用户账号数资源或者第三方电子白板资源到期后，若企业内对应资源的用户账号超过数量后会被系统随机自动停用，此时可通过该接口修改用户的状态。

        :param BatchUpdateUserStatusRequest request
        :return: None
        """

        all_params = ['value', 'account_list', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/corp/member/status/{value}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
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
        :return: tuple(CheckSlideVerifyCodeResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['slide_verify_code_check_dto', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v1/usg/acs/auth/slideverifycode/check', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CheckSlideVerifyCodeResponse',
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
        :return: tuple(CheckTokenResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['validate_token_req_dto', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/usg/acs/token/validate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CheckTokenResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_veri_code_for_update_user_info_async(self, request):
        """校验手机和邮箱对应的验证码

        企业用户通过该接口校验手机和邮箱对应的验证码，一分钟内记录尝试次数不得超过5次。

        :param CheckVeriCodeForUpdateUserInfoRequest request
        :return: None
        """
        return self.check_veri_code_for_update_user_info_with_http_info(request)

    def check_veri_code_for_update_user_info_with_http_info(self, request):
        """校验手机和邮箱对应的验证码

        企业用户通过该接口校验手机和邮箱对应的验证码，一分钟内记录尝试次数不得超过5次。

        :param CheckVeriCodeForUpdateUserInfoRequest request
        :return: None
        """

        all_params = ['verification_code_dto', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/member/verification-code/verify', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
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
        :return: tuple(CheckVerifyCodeResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['verify_code_check_dto', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v1/usg/acs/verifycode/check', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CheckVerifyCodeResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_corp_async(self, request):
        """SP管理员删除企业

        删除企业

        :param DeleteCorpRequest request
        :return: None
        """
        return self.delete_corp_with_http_info(request)

    def delete_corp_with_http_info(self, request):
        """SP管理员删除企业

        删除企业

        :param DeleteCorpRequest request
        :return: None
        """

        all_params = ['id', 'x_request_id', 'accept_language', 'force_delete']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/sp/corp/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_corp_vmr_async(self, request):
        """删除专用云会议室

        企业管理员通过该接口删除企业的专用云会议室

        :param DeleteCorpVmrRequest request
        :return: None
        """
        return self.delete_corp_vmr_with_http_info(request)

    def delete_corp_vmr_with_http_info(self, request):
        """删除专用云会议室

        企业管理员通过该接口删除企业的专用云会议室

        :param DeleteCorpVmrRequest request
        :return: None
        """

        all_params = ['del_list', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/corp/vmr/delete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_department_async(self, request):
        """删除部门

        企业管理员通过该接口删除部门。

        :param DeleteDepartmentRequest request
        :return: None
        """
        return self.delete_department_with_http_info(request)

    def delete_department_with_http_info(self, request):
        """删除部门

        企业管理员通过该接口删除部门。

        :param DeleteDepartmentRequest request
        :return: None
        """

        all_params = ['dept_code', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/corp/dept/{dept_code}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_resource_async(self, request):
        """删除企业资源

        企业删除资源项，删除资源项后，企业资源总数会自动减少

        :param DeleteResourceRequest request
        :return: None
        """
        return self.delete_resource_with_http_info(request)

    def delete_resource_with_http_info(self, request):
        """删除企业资源

        企业删除资源项，删除资源项后，企业资源总数会自动减少

        :param DeleteResourceRequest request
        :return: None
        """

        all_params = ['corp_id', 'resource_id_list', 'x_request_id', 'accept_language', 'force_edit_flag']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/sp/corp/{corp_id}/resource/delete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disassociate_vmr_async(self, request):
        """从用户或终端回收企业专用VMR

        给企业用户回收vmr，需要做好纵向越权校验，避免企业管理员给其他企业的账号分配

        :param DisassociateVmrRequest request
        :return: None
        """
        return self.disassociate_vmr_with_http_info(request)

    def disassociate_vmr_with_http_info(self, request):
        """从用户或终端回收企业专用VMR

        给企业用户回收vmr，需要做好纵向越权校验，避免企业管理员给其他企业的账号分配

        :param DisassociateVmrRequest request
        :return: None
        """

        all_params = ['account', 'recycle_list', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/corp/vmr/recycle-from-member/{account}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reset_activecode_async(self, request):
        """重置激活码

        当硬终端激活码失效时，企业管理员可以通过该接口重置激活码，使用重新获取的激活码激活终端，每24小时可重新激活5次。

        :param ResetActivecodeRequest request
        :return: None
        """
        return self.reset_activecode_with_http_info(request)

    def reset_activecode_with_http_info(self, request):
        """重置激活码

        当硬终端激活码失效时，企业管理员可以通过该接口重置激活码，使用重新获取的激活码激活终端，每24小时可重新激活5次。

        :param ResetActivecodeRequest request
        :return: None
        """

        all_params = ['sn', 'active_dto', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/corp/device/{sn}/activecode', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reset_pwd_async(self, request):
        """用户重置密码

        该接口提供给用户重置密码功能，服务器收到请求，重新设置用户密码并返回结果。

        :param ResetPwdRequest request
        :return: None
        """
        return self.reset_pwd_with_http_info(request)

    def reset_pwd_with_http_info(self, request):
        """用户重置密码

        该接口提供给用户重置密码功能，服务器收到请求，重新设置用户密码并返回结果。

        :param ResetPwdRequest request
        :return: None
        """

        all_params = ['reset_pwd_req_dtov1', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v1/usg/acs/password/reset', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reset_pwd_by_admin_async(self, request):
        """企业管理员重置企业成员密码

        企业管理员通过该接口提供企业管理员重置企业成员密码的功能。当服务器收到重置密码的请求时，发送新的密码到企业成员的邮箱或者短信，并返回结果。

        :param ResetPwdByAdminRequest request
        :return: None
        """
        return self.reset_pwd_by_admin_with_http_info(request)

    def reset_pwd_by_admin_with_http_info(self, request):
        """企业管理员重置企业成员密码

        企业管理员通过该接口提供企业管理员重置企业成员密码的功能。当服务器收到重置密码的请求时，发送新的密码到企业成员的邮箱或者短信，并返回结果。

        :param ResetPwdByAdminRequest request
        :return: None
        """

        all_params = ['admin_reset_pwd_req_dto', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v1/usg/acs/password/admin/reset', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
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
        :return: tuple(SearchCorpResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/sp/corp', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchCorpResponse',
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
        :return: tuple(SearchCorpAdminsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/corp/admin', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchCorpAdminsResponse',
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
        :return: tuple(SearchCorpDirResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key', 'dept_code', 'query_sub_dept', 'search_scope']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/usg/abs/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchCorpDirResponse',
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
        :return: tuple(SearchCorpVmrResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key', 'status']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/corp/vmr', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchCorpVmrResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_department_by_name_async(self, request):
        """按名称查询所有的部门

        企业管理员通过该接口按名称查询所有的部门。

        :param SearchDepartmentByNameRequest request
        :return: list[QueryDeptResultDTO]
        """
        return self.search_department_by_name_with_http_info(request)

    def search_department_by_name_with_http_info(self, request):
        """按名称查询所有的部门

        企业管理员通过该接口按名称查询所有的部门。

        :param SearchDepartmentByNameRequest request
        :return: tuple(list[QueryDeptResultDTO], status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['x_request_id', 'accept_language', 'dept_name']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/member/dept', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='list[QueryDeptResultDTO]',
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
        :return: tuple(SearchDevicesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key', 'model', 'dept_code', 'enable_sub_dept']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/corp/device', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchDevicesResponse',
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
        :return: tuple(SearchMemberVmrResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key', 'special_vmr']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/member/vmr', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchMemberVmrResponse',
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
        :return: tuple(SearchResourceResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['corp_id', 'x_request_id', 'accept_language', 'offset', 'limit', 'search_key', 'start_expire_date', 'end_expire_date', 'type', 'type_id', 'status']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/sp/corp/{corp_id}/resource', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchResourceResponse',
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
        :return: tuple(SearchResourceOpRecordResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['corp_id', 'x_request_id', 'accept_language', 'offset', 'limit', 'search_key', 'start_expire_date', 'end_expire_date', 'start_operate_date', 'end_operate_date', 'type', 'type_id', 'operate_type']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/sp/corp/{corp_id}/resource-record', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchResourceOpRecordResponse',
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
        :return: tuple(SearchUsersResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['x_request_id', 'accept_language', 'offset', 'limit', 'search_key', 'sort_field', 'is_asc', 'dept_code', 'enable_sub_dept', 'admin_type', 'enable_room', 'status']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/corp/member', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchUsersResponse',
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
        :return: tuple(SendSlideVerifyCodeResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['slide_verify_code_send_dto', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v1/usg/acs/auth/slideverifycode/send', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='SendSlideVerifyCodeResponse',
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
        :return: tuple(SendVeriCodeForChangePwdResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['verify_code_send_dtov1', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v1/usg/acs/verifycode/send', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='SendVeriCodeForChangePwdResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def send_veri_code_for_update_user_info_async(self, request):
        """获取验证码

        获取验证码，向手机或邮箱发送，一分钟内只会发送一次。

        :param SendVeriCodeForUpdateUserInfoRequest request
        :return: None
        """
        return self.send_veri_code_for_update_user_info_with_http_info(request)

    def send_veri_code_for_update_user_info_with_http_info(self, request):
        """获取验证码

        获取验证码，向手机或邮箱发送，一分钟内只会发送一次。

        :param SendVeriCodeForUpdateUserInfoRequest request
        :return: None
        """

        all_params = ['verification_code_dto', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/member/verification-code', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
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
        :return: tuple(ShowCorpResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['id', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/sp/corp/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCorpResponse',
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
        :return: tuple(ShowCorpAdminResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['account', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/corp/admin/{account}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCorpAdminResponse',
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
        :return: tuple(ShowCorpBasicInfoResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/corp', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCorpBasicInfoResponse',
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
        :return: tuple(ShowCorpResourceResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/corp/resource', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCorpResourceResponse',
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
        :return: tuple(ShowDeptAndChildDeptResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['dept_code', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/member/dept/{dept_code}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDeptAndChildDeptResponse',
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
        :return: tuple(ShowDeviceDetailResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['sn', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/corp/device/{sn}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDeviceDetailResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_device_status_async(self, request):
        """查询设备状态

        调用本接口可以查询硬终端的状态。 硬终端与发起查询请求的帐号需在同一企业下，否则会鉴权失败。 

        :param ShowDeviceStatusRequest request
        :return: list[UserStatusDTO]
        """
        return self.show_device_status_with_http_info(request)

    def show_device_status_with_http_info(self, request):
        """查询设备状态

        调用本接口可以查询硬终端的状态。 硬终端与发起查询请求的帐号需在同一企业下，否则会鉴权失败。 

        :param ShowDeviceStatusRequest request
        :return: tuple(list[UserStatusDTO], status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['number', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/usg/acs/ap/userstatus', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='list[UserStatusDTO]',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_device_types_async(self, request):
        """获取所有终端类型

        企业管理员通过该接口获取所有的终端类型。

        :param ShowDeviceTypesRequest request
        :return: list[QueryDeviceTypeResultDTO]
        """
        return self.show_device_types_with_http_info(request)

    def show_device_types_with_http_info(self, request):
        """获取所有终端类型

        企业管理员通过该接口获取所有的终端类型。

        :param ShowDeviceTypesRequest request
        :return: tuple(list[QueryDeviceTypeResultDTO], status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/termdevtype', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='list[QueryDeviceTypeResultDTO]',
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
        :return: tuple(ShowMyInfoResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/member', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMyInfoResponse',
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
        :return: tuple(ShowUserDetailResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['account', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/corp/member/{account}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowUserDetailResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_contact_async(self, request):
        """修改手机或邮箱

        企业用户通过该接口修改手机或邮箱，需要先获取验证码，验证多次失败会禁止修改。

        :param UpdateContactRequest request
        :return: None
        """
        return self.update_contact_with_http_info(request)

    def update_contact_with_http_info(self, request):
        """修改手机或邮箱

        企业用户通过该接口修改手机或邮箱，需要先获取验证码，验证多次失败会禁止修改。

        :param UpdateContactRequest request
        :return: None
        """

        all_params = ['verification_code_dto', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/member/contact', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_corp_async(self, request):
        """SP管理员修改企业

        修改企业，若任一参数为null或者不携带则不修改

        :param UpdateCorpRequest request
        :return: None
        """
        return self.update_corp_with_http_info(request)

    def update_corp_with_http_info(self, request):
        """SP管理员修改企业

        修改企业，若任一参数为null或者不携带则不修改

        :param UpdateCorpRequest request
        :return: None
        """

        all_params = ['id', 'corp_dto', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/sp/corp/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_corp_basic_info_async(self, request):
        """企业管理员修改企业注册信息

        企业管理员通过该接口修改企业注册信息。当前只支持修改地址。

        :param UpdateCorpBasicInfoRequest request
        :return: None
        """
        return self.update_corp_basic_info_with_http_info(request)

    def update_corp_basic_info_with_http_info(self, request):
        """企业管理员修改企业注册信息

        企业管理员通过该接口修改企业注册信息。当前只支持修改地址。

        :param UpdateCorpBasicInfoRequest request
        :return: None
        """

        all_params = ['mod_dto', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/corp', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_department_async(self, request):
        """修改部门

        企业管理员通过该接口修改部门。

        :param UpdateDepartmentRequest request
        :return: None
        """
        return self.update_department_with_http_info(request)

    def update_department_with_http_info(self, request):
        """修改部门

        企业管理员通过该接口修改部门。

        :param UpdateDepartmentRequest request
        :return: None
        """

        all_params = ['dept_code', 'dept_dto', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/corp/dept/{dept_code}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_device_async(self, request):
        """修改终端

        企业管理员通过该接口修改终端。

        :param UpdateDeviceRequest request
        :return: None
        """
        return self.update_device_with_http_info(request)

    def update_device_with_http_info(self, request):
        """修改终端

        企业管理员通过该接口修改终端。

        :param UpdateDeviceRequest request
        :return: None
        """

        all_params = ['sn', 'device_dto', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/corp/device/{sn}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_member_vmr_async(self, request):
        """修改用户云会议室

        企业用户登录后可以修改分配给用户的专用云会议室及个人云会议室。

        :param UpdateMemberVmrRequest request
        :return: None
        """
        return self.update_member_vmr_with_http_info(request)

    def update_member_vmr_with_http_info(self, request):
        """修改用户云会议室

        企业用户登录后可以修改分配给用户的专用云会议室及个人云会议室。

        :param UpdateMemberVmrRequest request
        :return: None
        """

        all_params = ['id', 'mod_dto', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/member/vmr/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_my_info_async(self, request):
        """用户修改自己的信息

        企业用户通过该接口修改自己的信息。

        :param UpdateMyInfoRequest request
        :return: None
        """
        return self.update_my_info_with_http_info(request)

    def update_my_info_with_http_info(self, request):
        """用户修改自己的信息

        企业用户通过该接口修改自己的信息。

        :param UpdateMyInfoRequest request
        :return: None
        """

        all_params = ['member_dto', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/member', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_pwd_async(self, request):
        """修改密码

        企业成员通过该接口提供用户修改密码功能，服务器收到请求，修改用户密码并返回结果。

        :param UpdatePwdRequest request
        :return: None
        """
        return self.update_pwd_with_http_info(request)

    def update_pwd_with_http_info(self, request):
        """修改密码

        企业成员通过该接口提供用户修改密码功能，服务器收到请求，修改用户密码并返回结果。

        :param UpdatePwdRequest request
        :return: None
        """

        all_params = ['mod_pwd_req_dto', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])
        auth_settings = []

        return self.call_api(
            '/v1/usg/acs/password', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_resource_async(self, request):
        """修改企业资源

        企业修改资源的过期时间、停用状态

        :param UpdateResourceRequest request
        :return: None
        """
        return self.update_resource_with_http_info(request)

    def update_resource_with_http_info(self, request):
        """修改企业资源

        企业修改资源的过期时间、停用状态

        :param UpdateResourceRequest request
        :return: None
        """

        all_params = ['corp_id', 'resource_list', 'x_request_id', 'accept_language', 'force_edit_flag']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/sp/corp/{corp_id}/resource', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
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
        :return: tuple(UpdateTokenResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['x_request_id', 'accept_language', 'empty_dto']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/usg/acs/token', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateTokenResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_user_async(self, request):
        """修改用户

        企业管理员通过该接口修改企业用户。

        :param UpdateUserRequest request
        :return: None
        """
        return self.update_user_with_http_info(request)

    def update_user_with_http_info(self, request):
        """修改用户

        企业管理员通过该接口修改企业用户。

        :param UpdateUserRequest request
        :return: None
        """

        all_params = ['account', 'user_dto', 'x_request_id', 'accept_language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

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

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        auth_settings = []

        return self.call_api(
            '/v1/usg/dcs/corp/member/{account}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None,
                 body=None, post_params=None, response_type=None, auth_settings=None, collection_formats=None,
                 request_type=None):
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
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :return:
            Return the response directly.
        """
        return self.do_http_request(method, resource_path, path_params,
                                    query_params, header_params, body, post_params,
                                    response_type, collection_formats, request_type, True)
