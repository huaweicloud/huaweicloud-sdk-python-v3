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


class KmsAsyncClient(Client):
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
        super(KmsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkkms.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @staticmethod
    def new_builder(clazz):
        return ClientBuilder(clazz)

    def batch_create_kms_tags_async(self, request):
        """批量添加删除密钥标签

        - 功能介绍：批量添加删除密钥标签。

        :param BatchCreateKmsTagsRequest request
        :return: BatchCreateKmsTagsResponse
        """
        return self.batch_create_kms_tags_with_http_info(request)

    def batch_create_kms_tags_with_http_info(self, request):
        """批量添加删除密钥标签

        - 功能介绍：批量添加删除密钥标签。

        :param BatchCreateKmsTagsRequest request
        :return: BatchCreateKmsTagsResponse
        """

        all_params = ['key_id', 'version_id', 'batch_create_kms_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'key_id' in local_var_params:
            path_params['key_id'] = local_var_params['key_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/{key_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchCreateKmsTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def cancel_grant_async(self, request):
        """撤销授权

        - 功能介绍：撤销授权，授权用户撤销被授权用户操作密钥的权限。 - 说明：    - 创建密钥的用户才能撤销该密钥授权。

        :param CancelGrantRequest request
        :return: CancelGrantResponse
        """
        return self.cancel_grant_with_http_info(request)

    def cancel_grant_with_http_info(self, request):
        """撤销授权

        - 功能介绍：撤销授权，授权用户撤销被授权用户操作密钥的权限。 - 说明：    - 创建密钥的用户才能撤销该密钥授权。

        :param CancelGrantRequest request
        :return: CancelGrantResponse
        """

        all_params = ['version_id', 'cancel_grant_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/revoke-grant',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CancelGrantResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def cancel_key_deletion_async(self, request):
        """取消计划删除密钥

        - 功能介绍：取消计划删除密钥。  - 说明：密钥处于“计划删除”状态才能取消计划删除密钥。

        :param CancelKeyDeletionRequest request
        :return: CancelKeyDeletionResponse
        """
        return self.cancel_key_deletion_with_http_info(request)

    def cancel_key_deletion_with_http_info(self, request):
        """取消计划删除密钥

        - 功能介绍：取消计划删除密钥。  - 说明：密钥处于“计划删除”状态才能取消计划删除密钥。

        :param CancelKeyDeletionRequest request
        :return: CancelKeyDeletionResponse
        """

        all_params = ['version_id', 'cancel_key_deletion_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/cancel-key-deletion',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CancelKeyDeletionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def cancel_self_grant_async(self, request):
        """退役授权

        - 功能介绍：退役授权，表示被授权用户不再具有授权密钥的操作权。   例如：用户A授权用户B可以操作密钥A/key，同时授权用户C可以撤销该授权，   那么用户A、B、C均可退役该授权，退役授权后，用户B不再可以使用A/key。 - 须知：      可执行退役授权的主体包括：    - 创建授权的用户；    - 授权中retiring_principal指向的用户；    - 当授权的操作列表中包含retire-grant时，grantee_principal指向的用户。

        :param CancelSelfGrantRequest request
        :return: CancelSelfGrantResponse
        """
        return self.cancel_self_grant_with_http_info(request)

    def cancel_self_grant_with_http_info(self, request):
        """退役授权

        - 功能介绍：退役授权，表示被授权用户不再具有授权密钥的操作权。   例如：用户A授权用户B可以操作密钥A/key，同时授权用户C可以撤销该授权，   那么用户A、B、C均可退役该授权，退役授权后，用户B不再可以使用A/key。 - 须知：      可执行退役授权的主体包括：    - 创建授权的用户；    - 授权中retiring_principal指向的用户；    - 当授权的操作列表中包含retire-grant时，grantee_principal指向的用户。

        :param CancelSelfGrantRequest request
        :return: CancelSelfGrantResponse
        """

        all_params = ['version_id', 'cancel_self_grant_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/retire-grant',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CancelSelfGrantResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_datakey_async(self, request):
        """创建数据密钥

        - 功能介绍：创建数据密钥，返回结果包含明文和密文。

        :param CreateDatakeyRequest request
        :return: CreateDatakeyResponse
        """
        return self.create_datakey_with_http_info(request)

    def create_datakey_with_http_info(self, request):
        """创建数据密钥

        - 功能介绍：创建数据密钥，返回结果包含明文和密文。

        :param CreateDatakeyRequest request
        :return: CreateDatakeyResponse
        """

        all_params = ['version_id', 'create_datakey_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/create-datakey',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateDatakeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_datakey_without_plaintext_async(self, request):
        """创建不含明文数据密钥

        - 功能介绍：创建数据密钥，返回结果只包含密文。

        :param CreateDatakeyWithoutPlaintextRequest request
        :return: CreateDatakeyWithoutPlaintextResponse
        """
        return self.create_datakey_without_plaintext_with_http_info(request)

    def create_datakey_without_plaintext_with_http_info(self, request):
        """创建不含明文数据密钥

        - 功能介绍：创建数据密钥，返回结果只包含密文。

        :param CreateDatakeyWithoutPlaintextRequest request
        :return: CreateDatakeyWithoutPlaintextResponse
        """

        all_params = ['version_id', 'create_datakey_without_plaintext_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/create-datakey-without-plaintext',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateDatakeyWithoutPlaintextResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_grant_async(self, request):
        """创建授权

        - 功能介绍：创建授权，被授权用户可以对授权密钥进行操作。 - 说明：    - 服务默认主密钥（密钥别名后缀为“/default”）不可以授权。

        :param CreateGrantRequest request
        :return: CreateGrantResponse
        """
        return self.create_grant_with_http_info(request)

    def create_grant_with_http_info(self, request):
        """创建授权

        - 功能介绍：创建授权，被授权用户可以对授权密钥进行操作。 - 说明：    - 服务默认主密钥（密钥别名后缀为“/default”）不可以授权。

        :param CreateGrantRequest request
        :return: CreateGrantResponse
        """

        all_params = ['version_id', 'create_grant_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/create-grant',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateGrantResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_key_async(self, request):
        """创建密钥

        - 功能介绍：创建用户主密钥，可用来加密数据密钥。  - 说明： 别名“/default”为服务默认主密钥的后缀名，由服务自动创建。因此用户创建的主密钥别名不能与服务默认主密钥的别名相同，即后缀名不能为“/default”。对于开通企业项目的用户，服务默认主密钥属于且只能属于默认企业项目下，且不支持企业资源的迁入迁出。服务默认主密钥为用户提供基础的云上加密功能，满足合规要求。因此，在企业多项目下，其他非默认企业项目下的用户均可使用该密钥。若客户有企业管理资源诉求，请自行创建和使用密钥。

        :param CreateKeyRequest request
        :return: CreateKeyResponse
        """
        return self.create_key_with_http_info(request)

    def create_key_with_http_info(self, request):
        """创建密钥

        - 功能介绍：创建用户主密钥，可用来加密数据密钥。  - 说明： 别名“/default”为服务默认主密钥的后缀名，由服务自动创建。因此用户创建的主密钥别名不能与服务默认主密钥的别名相同，即后缀名不能为“/default”。对于开通企业项目的用户，服务默认主密钥属于且只能属于默认企业项目下，且不支持企业资源的迁入迁出。服务默认主密钥为用户提供基础的云上加密功能，满足合规要求。因此，在企业多项目下，其他非默认企业项目下的用户均可使用该密钥。若客户有企业管理资源诉求，请自行创建和使用密钥。

        :param CreateKeyRequest request
        :return: CreateKeyResponse
        """

        all_params = ['version_id', 'create_key_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/create-key',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateKeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_kms_tag_async(self, request):
        """添加密钥标签

        - 功能介绍：添加密钥标签。

        :param CreateKmsTagRequest request
        :return: CreateKmsTagResponse
        """
        return self.create_kms_tag_with_http_info(request)

    def create_kms_tag_with_http_info(self, request):
        """添加密钥标签

        - 功能介绍：添加密钥标签。

        :param CreateKmsTagRequest request
        :return: CreateKmsTagResponse
        """

        all_params = ['version_id', 'key_id', 'create_kms_tag_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']
        if 'key_id' in local_var_params:
            path_params['key_id'] = local_var_params['key_id']

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
            resource_path='/{version_id}/{project_id}/kms/{key_id}/tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateKmsTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_parameters_for_import_async(self, request):
        """获取密钥导入参数

        - 功能介绍：获取导入密钥的必要参数，包括密钥导入令牌和密钥加密公钥。 - 说明：返回的公钥类型默认为RSA_2048。

        :param CreateParametersForImportRequest request
        :return: CreateParametersForImportResponse
        """
        return self.create_parameters_for_import_with_http_info(request)

    def create_parameters_for_import_with_http_info(self, request):
        """获取密钥导入参数

        - 功能介绍：获取导入密钥的必要参数，包括密钥导入令牌和密钥加密公钥。 - 说明：返回的公钥类型默认为RSA_2048。

        :param CreateParametersForImportRequest request
        :return: CreateParametersForImportResponse
        """

        all_params = ['version_id', 'create_parameters_for_import_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/get-parameters-for-import',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateParametersForImportResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_random_async(self, request):
        """创建随机数

        - 功能介绍：   生成8~8192bit范围内的随机数。   生成512bit的随机数。

        :param CreateRandomRequest request
        :return: CreateRandomResponse
        """
        return self.create_random_with_http_info(request)

    def create_random_with_http_info(self, request):
        """创建随机数

        - 功能介绍：   生成8~8192bit范围内的随机数。   生成512bit的随机数。

        :param CreateRandomRequest request
        :return: CreateRandomResponse
        """

        all_params = ['version_id', 'create_random_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/gen-random',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateRandomResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def decrypt_data_async(self, request):
        """解密数据

        - 功能介绍：解密数据。

        :param DecryptDataRequest request
        :return: DecryptDataResponse
        """
        return self.decrypt_data_with_http_info(request)

    def decrypt_data_with_http_info(self, request):
        """解密数据

        - 功能介绍：解密数据。

        :param DecryptDataRequest request
        :return: DecryptDataResponse
        """

        all_params = ['version_id', 'decrypt_data_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/decrypt-data',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DecryptDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def decrypt_datakey_async(self, request):
        """解密数据密钥

        - 功能介绍：解密数据密钥，用指定的主密钥解密数据密钥。

        :param DecryptDatakeyRequest request
        :return: DecryptDatakeyResponse
        """
        return self.decrypt_datakey_with_http_info(request)

    def decrypt_datakey_with_http_info(self, request):
        """解密数据密钥

        - 功能介绍：解密数据密钥，用指定的主密钥解密数据密钥。

        :param DecryptDatakeyRequest request
        :return: DecryptDatakeyResponse
        """

        all_params = ['version_id', 'decrypt_datakey_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/decrypt-datakey',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DecryptDatakeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_imported_key_material_async(self, request):
        """删除密钥材料

        - 功能介绍：删除密钥材料信息。

        :param DeleteImportedKeyMaterialRequest request
        :return: DeleteImportedKeyMaterialResponse
        """
        return self.delete_imported_key_material_with_http_info(request)

    def delete_imported_key_material_with_http_info(self, request):
        """删除密钥材料

        - 功能介绍：删除密钥材料信息。

        :param DeleteImportedKeyMaterialRequest request
        :return: DeleteImportedKeyMaterialResponse
        """

        all_params = ['version_id', 'delete_imported_key_material_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/delete-imported-key-material',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteImportedKeyMaterialResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_key_async(self, request):
        """计划删除密钥

        - 功能介绍：计划多少天后删除密钥，可设置7天～1096天内删除密钥。

        :param DeleteKeyRequest request
        :return: DeleteKeyResponse
        """
        return self.delete_key_with_http_info(request)

    def delete_key_with_http_info(self, request):
        """计划删除密钥

        - 功能介绍：计划多少天后删除密钥，可设置7天～1096天内删除密钥。

        :param DeleteKeyRequest request
        :return: DeleteKeyResponse
        """

        all_params = ['version_id', 'delete_key_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/schedule-key-deletion',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteKeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_tag_async(self, request):
        """删除密钥标签

        - 功能介绍：删除密钥标签。

        :param DeleteTagRequest request
        :return: DeleteTagResponse
        """
        return self.delete_tag_with_http_info(request)

    def delete_tag_with_http_info(self, request):
        """删除密钥标签

        - 功能介绍：删除密钥标签。

        :param DeleteTagRequest request
        :return: DeleteTagResponse
        """

        all_params = ['key_id', 'key', 'version_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'key_id' in local_var_params:
            path_params['key_id'] = local_var_params['key_id']
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/{version_id}/{project_id}/kms/{key_id}/tags/{key}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def disable_key_async(self, request):
        """禁用密钥

        - 功能介绍：禁用密钥，密钥禁用后不可以使用。  - 说明：密钥为启用状态才能禁用密钥。

        :param DisableKeyRequest request
        :return: DisableKeyResponse
        """
        return self.disable_key_with_http_info(request)

    def disable_key_with_http_info(self, request):
        """禁用密钥

        - 功能介绍：禁用密钥，密钥禁用后不可以使用。  - 说明：密钥为启用状态才能禁用密钥。

        :param DisableKeyRequest request
        :return: DisableKeyResponse
        """

        all_params = ['version_id', 'disable_key_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/disable-key',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DisableKeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def disable_key_rotation_async(self, request):
        """关闭密钥轮换

        - 功能介绍：关闭用户主密钥轮换。

        :param DisableKeyRotationRequest request
        :return: DisableKeyRotationResponse
        """
        return self.disable_key_rotation_with_http_info(request)

    def disable_key_rotation_with_http_info(self, request):
        """关闭密钥轮换

        - 功能介绍：关闭用户主密钥轮换。

        :param DisableKeyRotationRequest request
        :return: DisableKeyRotationResponse
        """

        all_params = ['version_id', 'disable_key_rotation_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/disable-key-rotation',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DisableKeyRotationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def enable_key_async(self, request):
        """启用密钥

        - 功能介绍：启用密钥，密钥启用后才可以使用。  - 说明：密钥为禁用状态才能启用密钥。

        :param EnableKeyRequest request
        :return: EnableKeyResponse
        """
        return self.enable_key_with_http_info(request)

    def enable_key_with_http_info(self, request):
        """启用密钥

        - 功能介绍：启用密钥，密钥启用后才可以使用。  - 说明：密钥为禁用状态才能启用密钥。

        :param EnableKeyRequest request
        :return: EnableKeyResponse
        """

        all_params = ['version_id', 'enable_key_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/enable-key',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='EnableKeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def enable_key_rotation_async(self, request):
        """开启密钥轮换

        - 功能介绍：开启用户主密钥轮换。 - 说明：   - 开启密钥轮换后，默认轮询间隔时间为365天。   - 默认主密钥及外部导入密钥不支持轮换操作。

        :param EnableKeyRotationRequest request
        :return: EnableKeyRotationResponse
        """
        return self.enable_key_rotation_with_http_info(request)

    def enable_key_rotation_with_http_info(self, request):
        """开启密钥轮换

        - 功能介绍：开启用户主密钥轮换。 - 说明：   - 开启密钥轮换后，默认轮询间隔时间为365天。   - 默认主密钥及外部导入密钥不支持轮换操作。

        :param EnableKeyRotationRequest request
        :return: EnableKeyRotationResponse
        """

        all_params = ['version_id', 'enable_key_rotation_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/enable-key-rotation',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='EnableKeyRotationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def encrypt_data_async(self, request):
        """加密数据

        - 功能介绍：加密数据，用指定的用户主密钥加密数据。

        :param EncryptDataRequest request
        :return: EncryptDataResponse
        """
        return self.encrypt_data_with_http_info(request)

    def encrypt_data_with_http_info(self, request):
        """加密数据

        - 功能介绍：加密数据，用指定的用户主密钥加密数据。

        :param EncryptDataRequest request
        :return: EncryptDataResponse
        """

        all_params = ['version_id', 'encrypt_data_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/encrypt-data',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='EncryptDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def encrypt_datakey_async(self, request):
        """加密数据密钥

        - 功能介绍：加密数据密钥，用指定的主密钥加密数据密钥。

        :param EncryptDatakeyRequest request
        :return: EncryptDatakeyResponse
        """
        return self.encrypt_datakey_with_http_info(request)

    def encrypt_datakey_with_http_info(self, request):
        """加密数据密钥

        - 功能介绍：加密数据密钥，用指定的主密钥加密数据密钥。

        :param EncryptDatakeyRequest request
        :return: EncryptDatakeyResponse
        """

        all_params = ['version_id', 'encrypt_datakey_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/encrypt-datakey',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='EncryptDatakeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def import_key_material_async(self, request):
        """导入密钥材料

        - 功能介绍：导入密钥材料。

        :param ImportKeyMaterialRequest request
        :return: ImportKeyMaterialResponse
        """
        return self.import_key_material_with_http_info(request)

    def import_key_material_with_http_info(self, request):
        """导入密钥材料

        - 功能介绍：导入密钥材料。

        :param ImportKeyMaterialRequest request
        :return: ImportKeyMaterialResponse
        """

        all_params = ['version_id', 'import_key_material_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/import-key-material',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ImportKeyMaterialResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_grants_async(self, request):
        """查询授权列表

        - 功能介绍：查询密钥的授权列表。

        :param ListGrantsRequest request
        :return: ListGrantsResponse
        """
        return self.list_grants_with_http_info(request)

    def list_grants_with_http_info(self, request):
        """查询授权列表

        - 功能介绍：查询密钥的授权列表。

        :param ListGrantsRequest request
        :return: ListGrantsResponse
        """

        all_params = ['version_id', 'list_grants_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/list-grants',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListGrantsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_key_detail_async(self, request):
        """查询密钥信息

        - 功能介绍：查询密钥详细信息。

        :param ListKeyDetailRequest request
        :return: ListKeyDetailResponse
        """
        return self.list_key_detail_with_http_info(request)

    def list_key_detail_with_http_info(self, request):
        """查询密钥信息

        - 功能介绍：查询密钥详细信息。

        :param ListKeyDetailRequest request
        :return: ListKeyDetailResponse
        """

        all_params = ['version_id', 'list_key_detail_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/describe-key',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListKeyDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_keys_async(self, request):
        """查询密钥列表

        - 功能介绍：查询用户所有密钥列表。

        :param ListKeysRequest request
        :return: ListKeysResponse
        """
        return self.list_keys_with_http_info(request)

    def list_keys_with_http_info(self, request):
        """查询密钥列表

        - 功能介绍：查询用户所有密钥列表。

        :param ListKeysRequest request
        :return: ListKeysResponse
        """

        all_params = ['version_id', 'list_keys_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/list-keys',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListKeysResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_kms_by_tags_async(self, request):
        """查询密钥实例

        - 功能介绍：查询密钥实例。通过标签过滤，查询指定用户主密钥的详细信息。

        :param ListKmsByTagsRequest request
        :return: ListKmsByTagsResponse
        """
        return self.list_kms_by_tags_with_http_info(request)

    def list_kms_by_tags_with_http_info(self, request):
        """查询密钥实例

        - 功能介绍：查询密钥实例。通过标签过滤，查询指定用户主密钥的详细信息。

        :param ListKmsByTagsRequest request
        :return: ListKmsByTagsResponse
        """

        all_params = ['resource_instances', 'version_id', 'list_kms_by_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'resource_instances' in local_var_params:
            path_params['resource_instances'] = local_var_params['resource_instances']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/{resource_instances}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListKmsByTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_kms_tags_async(self, request):
        """查询项目标签

        - 功能介绍：查询用户在指定项目下的所有标签集合。

        :param ListKmsTagsRequest request
        :return: ListKmsTagsResponse
        """
        return self.list_kms_tags_with_http_info(request)

    def list_kms_tags_with_http_info(self, request):
        """查询项目标签

        - 功能介绍：查询用户在指定项目下的所有标签集合。

        :param ListKmsTagsRequest request
        :return: ListKmsTagsResponse
        """

        all_params = ['version_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/{version_id}/{project_id}/kms/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListKmsTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_retirable_grants_async(self, request):
        """查询可退役授权列表

        - 功能介绍：查询用户可以退役的授权列表。

        :param ListRetirableGrantsRequest request
        :return: ListRetirableGrantsResponse
        """
        return self.list_retirable_grants_with_http_info(request)

    def list_retirable_grants_with_http_info(self, request):
        """查询可退役授权列表

        - 功能介绍：查询用户可以退役的授权列表。

        :param ListRetirableGrantsRequest request
        :return: ListRetirableGrantsResponse
        """

        all_params = ['version_id', 'list_retirable_grants_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/list-retirable-grants',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRetirableGrantsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_key_rotation_status_async(self, request):
        """查询密钥轮换状态

        - 功能介绍：查询用户主密钥轮换状态。

        :param ShowKeyRotationStatusRequest request
        :return: ShowKeyRotationStatusResponse
        """
        return self.show_key_rotation_status_with_http_info(request)

    def show_key_rotation_status_with_http_info(self, request):
        """查询密钥轮换状态

        - 功能介绍：查询用户主密钥轮换状态。

        :param ShowKeyRotationStatusRequest request
        :return: ShowKeyRotationStatusResponse
        """

        all_params = ['version_id', 'show_key_rotation_status_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/get-key-rotation-status',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowKeyRotationStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_kms_tags_async(self, request):
        """查询密钥标签

        - 功能介绍：查询密钥标签。

        :param ShowKmsTagsRequest request
        :return: ShowKmsTagsResponse
        """
        return self.show_kms_tags_with_http_info(request)

    def show_kms_tags_with_http_info(self, request):
        """查询密钥标签

        - 功能介绍：查询密钥标签。

        :param ShowKmsTagsRequest request
        :return: ShowKmsTagsResponse
        """

        all_params = ['version_id', 'key_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']
        if 'key_id' in local_var_params:
            path_params['key_id'] = local_var_params['key_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/{version_id}/{project_id}/kms/{key_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowKmsTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_user_instances_async(self, request):
        """查询实例数

        - 功能介绍：查询实例数，获取用户已经创建的用户主密钥数量。

        :param ShowUserInstancesRequest request
        :return: ShowUserInstancesResponse
        """
        return self.show_user_instances_with_http_info(request)

    def show_user_instances_with_http_info(self, request):
        """查询实例数

        - 功能介绍：查询实例数，获取用户已经创建的用户主密钥数量。

        :param ShowUserInstancesRequest request
        :return: ShowUserInstancesResponse
        """

        all_params = ['version_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/{version_id}/{project_id}/kms/user-instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowUserInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_user_quotas_async(self, request):
        """查询配额

        - 功能介绍：查询配额，查询用户可以创建的用户主密钥配额总数及当前使用量信息。

        :param ShowUserQuotasRequest request
        :return: ShowUserQuotasResponse
        """
        return self.show_user_quotas_with_http_info(request)

    def show_user_quotas_with_http_info(self, request):
        """查询配额

        - 功能介绍：查询配额，查询用户可以创建的用户主密钥配额总数及当前使用量信息。

        :param ShowUserQuotasRequest request
        :return: ShowUserQuotasResponse
        """

        all_params = ['version_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/{version_id}/{project_id}/kms/user-quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowUserQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_key_alias_async(self, request):
        """修改密钥别名

        - 功能介绍：修改用户主密钥别名。 - 说明：    - 服务默认主密钥（密钥别名后缀为“/default”）不可以修改。    - 密钥处于“计划删除”状态，密钥别名不可以修改。

        :param UpdateKeyAliasRequest request
        :return: UpdateKeyAliasResponse
        """
        return self.update_key_alias_with_http_info(request)

    def update_key_alias_with_http_info(self, request):
        """修改密钥别名

        - 功能介绍：修改用户主密钥别名。 - 说明：    - 服务默认主密钥（密钥别名后缀为“/default”）不可以修改。    - 密钥处于“计划删除”状态，密钥别名不可以修改。

        :param UpdateKeyAliasRequest request
        :return: UpdateKeyAliasResponse
        """

        all_params = ['version_id', 'update_key_alias_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/update-key-alias',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateKeyAliasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_key_description_async(self, request):
        """修改密钥描述

        - 功能介绍：修改用户主密钥描述信息。 - 说明：    - 服务默认主密钥（密钥别名后缀为“/default”）不可以修改。    - 密钥处于“计划删除”状态，密钥描述不可以修改。

        :param UpdateKeyDescriptionRequest request
        :return: UpdateKeyDescriptionResponse
        """
        return self.update_key_description_with_http_info(request)

    def update_key_description_with_http_info(self, request):
        """修改密钥描述

        - 功能介绍：修改用户主密钥描述信息。 - 说明：    - 服务默认主密钥（密钥别名后缀为“/default”）不可以修改。    - 密钥处于“计划删除”状态，密钥描述不可以修改。

        :param UpdateKeyDescriptionRequest request
        :return: UpdateKeyDescriptionResponse
        """

        all_params = ['version_id', 'update_key_description_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/update-key-description',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateKeyDescriptionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_key_rotation_interval_async(self, request):
        """修改密钥轮换周期

        - 功能介绍：修改用户主密钥轮换周期。

        :param UpdateKeyRotationIntervalRequest request
        :return: UpdateKeyRotationIntervalResponse
        """
        return self.update_key_rotation_interval_with_http_info(request)

    def update_key_rotation_interval_with_http_info(self, request):
        """修改密钥轮换周期

        - 功能介绍：修改用户主密钥轮换周期。

        :param UpdateKeyRotationIntervalRequest request
        :return: UpdateKeyRotationIntervalResponse
        """

        all_params = ['version_id', 'update_key_rotation_interval_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/{version_id}/{project_id}/kms/update-key-rotation-interval',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateKeyRotationIntervalResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_version_async(self, request):
        """查询指定版本信息

        - 功能介绍：查指定API版本信息。

        :param ShowVersionRequest request
        :return: ShowVersionResponse
        """
        return self.show_version_with_http_info(request)

    def show_version_with_http_info(self, request):
        """查询指定版本信息

        - 功能介绍：查指定API版本信息。

        :param ShowVersionRequest request
        :return: ShowVersionResponse
        """

        all_params = ['version_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/{version_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_versions_async(self, request):
        """查询版本信息列表

        - 功能介绍：查询API版本信息列表。

        :param ShowVersionsRequest request
        :return: ShowVersionsResponse
        """
        return self.show_versions_with_http_info(request)

    def show_versions_with_http_info(self, request):
        """查询版本信息列表

        - 功能介绍：查询API版本信息列表。

        :param ShowVersionsRequest request
        :return: ShowVersionsResponse
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
            resource_path='/',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowVersionsResponse',
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
