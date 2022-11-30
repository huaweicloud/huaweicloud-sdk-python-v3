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
        self.model_package = importlib.import_module("huaweicloudsdkkms.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "KmsClient":
            raise TypeError("client type error, support client type is KmsClient")

        return ClientBuilder(clazz)

    def batch_create_kms_tags_async(self, request):
        """批量添加删除密钥标签

        - 功能介绍：批量添加删除密钥标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateKmsTags
        :type request: :class:`huaweicloudsdkkms.v2.BatchCreateKmsTagsRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.BatchCreateKmsTagsResponse`
        """
        return self.batch_create_kms_tags_with_http_info(request)

    def batch_create_kms_tags_with_http_info(self, request):
        all_params = ['key_id', 'batch_create_kms_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
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
            resource_path='/v1.0/{project_id}/kms/{key_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreateKmsTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cancel_grant_async(self, request):
        """撤销授权

        - 功能介绍：撤销授权，授权用户撤销被授权用户操作密钥的权限。
        - 说明：
           - 创建密钥的用户才能撤销该密钥授权。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CancelGrant
        :type request: :class:`huaweicloudsdkkms.v2.CancelGrantRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.CancelGrantResponse`
        """
        return self.cancel_grant_with_http_info(request)

    def cancel_grant_with_http_info(self, request):
        all_params = ['cancel_grant_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/revoke-grant',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CancelGrantResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cancel_key_deletion_async(self, request):
        """取消计划删除密钥

        - 功能介绍：取消计划删除密钥。
        - 说明：密钥处于“计划删除”状态才能取消计划删除密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CancelKeyDeletion
        :type request: :class:`huaweicloudsdkkms.v2.CancelKeyDeletionRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.CancelKeyDeletionResponse`
        """
        return self.cancel_key_deletion_with_http_info(request)

    def cancel_key_deletion_with_http_info(self, request):
        all_params = ['cancel_key_deletion_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/cancel-key-deletion',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CancelKeyDeletionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cancel_self_grant_async(self, request):
        """退役授权

        - 功能介绍：退役授权，表示被授权用户不再具有授权密钥的操作权。
          例如：用户A授权用户B可以操作密钥A/key，同时授权用户C可以撤销该授权，
          那么用户A、B、C均可退役该授权，退役授权后，用户B不再可以使用A/key。
        - 须知：
             可执行退役授权的主体包括：
           - 创建授权的用户；
           - 授权中retiring_principal指向的用户；
           - 当授权的操作列表中包含retire-grant时，grantee_principal指向的用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CancelSelfGrant
        :type request: :class:`huaweicloudsdkkms.v2.CancelSelfGrantRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.CancelSelfGrantResponse`
        """
        return self.cancel_self_grant_with_http_info(request)

    def cancel_self_grant_with_http_info(self, request):
        all_params = ['cancel_self_grant_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/retire-grant',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CancelSelfGrantResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_datakey_async(self, request):
        """创建数据密钥

        - 功能介绍：创建数据密钥，返回结果包含明文和密文。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDatakey
        :type request: :class:`huaweicloudsdkkms.v2.CreateDatakeyRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.CreateDatakeyResponse`
        """
        return self.create_datakey_with_http_info(request)

    def create_datakey_with_http_info(self, request):
        all_params = ['create_datakey_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/create-datakey',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDatakeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_datakey_without_plaintext_async(self, request):
        """创建不含明文数据密钥

        - 功能介绍：创建数据密钥，返回结果只包含密文。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDatakeyWithoutPlaintext
        :type request: :class:`huaweicloudsdkkms.v2.CreateDatakeyWithoutPlaintextRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.CreateDatakeyWithoutPlaintextResponse`
        """
        return self.create_datakey_without_plaintext_with_http_info(request)

    def create_datakey_without_plaintext_with_http_info(self, request):
        all_params = ['create_datakey_without_plaintext_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/create-datakey-without-plaintext',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDatakeyWithoutPlaintextResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_grant_async(self, request):
        """创建授权

        - 功能介绍：创建授权，被授权用户可以对授权密钥进行操作。
        - 说明：
           - 服务默认主密钥（密钥别名后缀为“/default”）不可以授权。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateGrant
        :type request: :class:`huaweicloudsdkkms.v2.CreateGrantRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.CreateGrantResponse`
        """
        return self.create_grant_with_http_info(request)

    def create_grant_with_http_info(self, request):
        all_params = ['create_grant_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/create-grant',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateGrantResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_key_async(self, request):
        """创建密钥

        创建用户主密钥，用户主密钥可以为对称密钥或非对称密钥。
        - 对称密钥为长度为256位AES密钥或者128位SM4密钥，可用于小量数据的加密或者用于加密数据密钥。
        - 非对称密钥可以为RSA密钥对或者ECC密钥对（包含SM2密钥对），可用于加解密数据、数字签名及验签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateKey
        :type request: :class:`huaweicloudsdkkms.v2.CreateKeyRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.CreateKeyResponse`
        """
        return self.create_key_with_http_info(request)

    def create_key_with_http_info(self, request):
        all_params = ['create_key_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/create-key',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateKeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_key_store_async(self, request):
        """创建专属密钥库

        - \&quot;创建租户专属密钥库，专属密钥库使用DHSM实例作为密钥的存储\&quot;
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateKeyStore
        :type request: :class:`huaweicloudsdkkms.v2.CreateKeyStoreRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.CreateKeyStoreResponse`
        """
        return self.create_key_store_with_http_info(request)

    def create_key_store_with_http_info(self, request):
        all_params = ['create_key_store_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/keystores',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateKeyStoreResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_kms_tag_async(self, request):
        """添加密钥标签

        - 功能介绍：添加密钥标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateKmsTag
        :type request: :class:`huaweicloudsdkkms.v2.CreateKmsTagRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.CreateKmsTagResponse`
        """
        return self.create_kms_tag_with_http_info(request)

    def create_kms_tag_with_http_info(self, request):
        all_params = ['key_id', 'create_kms_tag_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
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
            resource_path='/v1.0/{project_id}/kms/{key_id}/tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateKmsTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_parameters_for_import_async(self, request):
        """获取密钥导入参数

        - 功能介绍：获取导入密钥的必要参数，包括密钥导入令牌和密钥加密公钥。
        - 说明：返回的公钥类型默认为RSA_2048。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateParametersForImport
        :type request: :class:`huaweicloudsdkkms.v2.CreateParametersForImportRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.CreateParametersForImportResponse`
        """
        return self.create_parameters_for_import_with_http_info(request)

    def create_parameters_for_import_with_http_info(self, request):
        all_params = ['create_parameters_for_import_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/get-parameters-for-import',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateParametersForImportResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_random_async(self, request):
        """创建随机数

        - 功能介绍：
          生成8~8192bit范围内的随机数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRandom
        :type request: :class:`huaweicloudsdkkms.v2.CreateRandomRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.CreateRandomResponse`
        """
        return self.create_random_with_http_info(request)

    def create_random_with_http_info(self, request):
        all_params = ['create_random_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/gen-random',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateRandomResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def decrypt_data_async(self, request):
        """解密数据

        - 功能介绍：解密数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DecryptData
        :type request: :class:`huaweicloudsdkkms.v2.DecryptDataRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.DecryptDataResponse`
        """
        return self.decrypt_data_with_http_info(request)

    def decrypt_data_with_http_info(self, request):
        all_params = ['decrypt_data_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/decrypt-data',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DecryptDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def decrypt_datakey_async(self, request):
        """解密数据密钥

        - 功能介绍：解密数据密钥，用指定的主密钥解密数据密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DecryptDatakey
        :type request: :class:`huaweicloudsdkkms.v2.DecryptDatakeyRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.DecryptDatakeyResponse`
        """
        return self.decrypt_datakey_with_http_info(request)

    def decrypt_datakey_with_http_info(self, request):
        all_params = ['decrypt_datakey_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/decrypt-datakey',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DecryptDatakeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_imported_key_material_async(self, request):
        """删除密钥材料

        - 功能介绍：删除密钥材料信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteImportedKeyMaterial
        :type request: :class:`huaweicloudsdkkms.v2.DeleteImportedKeyMaterialRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.DeleteImportedKeyMaterialResponse`
        """
        return self.delete_imported_key_material_with_http_info(request)

    def delete_imported_key_material_with_http_info(self, request):
        all_params = ['delete_imported_key_material_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/delete-imported-key-material',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteImportedKeyMaterialResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_key_async(self, request):
        """计划删除密钥

        - 功能介绍：计划多少天后删除密钥，可设置7天～1096天内删除密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteKey
        :type request: :class:`huaweicloudsdkkms.v2.DeleteKeyRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.DeleteKeyResponse`
        """
        return self.delete_key_with_http_info(request)

    def delete_key_with_http_info(self, request):
        all_params = ['delete_key_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/schedule-key-deletion',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteKeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_key_store_async(self, request):
        """删除专属密钥库

        删除租户专属密钥库
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteKeyStore
        :type request: :class:`huaweicloudsdkkms.v2.DeleteKeyStoreRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.DeleteKeyStoreResponse`
        """
        return self.delete_key_store_with_http_info(request)

    def delete_key_store_with_http_info(self, request):
        all_params = ['keystore_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'keystore_id' in local_var_params:
            path_params['keystore_id'] = local_var_params['keystore_id']

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
            resource_path='/v1.0/{project_id}/keystores/{keystore_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteKeyStoreResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_tag_async(self, request):
        """删除密钥标签

        - 功能介绍：删除密钥标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTag
        :type request: :class:`huaweicloudsdkkms.v2.DeleteTagRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.DeleteTagResponse`
        """
        return self.delete_tag_with_http_info(request)

    def delete_tag_with_http_info(self, request):
        all_params = ['key_id', 'key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'key_id' in local_var_params:
            path_params['key_id'] = local_var_params['key_id']
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
            resource_path='/v1.0/{project_id}/kms/{key_id}/tags/{key}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disable_key_async(self, request):
        """禁用密钥

        - 功能介绍：禁用密钥，密钥禁用后不可以使用。
        - 说明：密钥为启用状态才能禁用密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisableKey
        :type request: :class:`huaweicloudsdkkms.v2.DisableKeyRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.DisableKeyResponse`
        """
        return self.disable_key_with_http_info(request)

    def disable_key_with_http_info(self, request):
        all_params = ['disable_key_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/disable-key',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisableKeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disable_key_rotation_async(self, request):
        """关闭密钥轮换

        - 功能介绍：关闭用户主密钥轮换。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisableKeyRotation
        :type request: :class:`huaweicloudsdkkms.v2.DisableKeyRotationRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.DisableKeyRotationResponse`
        """
        return self.disable_key_rotation_with_http_info(request)

    def disable_key_rotation_with_http_info(self, request):
        all_params = ['disable_key_rotation_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/disable-key-rotation',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisableKeyRotationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disable_key_store_async(self, request):
        """禁用专属密钥库

        禁用租户专属密钥库
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisableKeyStore
        :type request: :class:`huaweicloudsdkkms.v2.DisableKeyStoreRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.DisableKeyStoreResponse`
        """
        return self.disable_key_store_with_http_info(request)

    def disable_key_store_with_http_info(self, request):
        all_params = ['keystore_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'keystore_id' in local_var_params:
            path_params['keystore_id'] = local_var_params['keystore_id']

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
            resource_path='/v1.0/{project_id}/keystores/{keystore_id}/disable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisableKeyStoreResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def enable_key_async(self, request):
        """启用密钥

        - 功能介绍：启用密钥，密钥启用后才可以使用。
        - 说明：密钥为禁用状态才能启用密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableKey
        :type request: :class:`huaweicloudsdkkms.v2.EnableKeyRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.EnableKeyResponse`
        """
        return self.enable_key_with_http_info(request)

    def enable_key_with_http_info(self, request):
        all_params = ['enable_key_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/enable-key',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='EnableKeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def enable_key_rotation_async(self, request):
        """开启密钥轮换

        - 功能介绍：开启用户主密钥轮换。
        - 说明：
          - 开启密钥轮换后，默认轮换间隔时间为365天。
          - 默认主密钥及外部导入密钥不支持轮换操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableKeyRotation
        :type request: :class:`huaweicloudsdkkms.v2.EnableKeyRotationRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.EnableKeyRotationResponse`
        """
        return self.enable_key_rotation_with_http_info(request)

    def enable_key_rotation_with_http_info(self, request):
        all_params = ['enable_key_rotation_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/enable-key-rotation',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='EnableKeyRotationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def enable_key_store_async(self, request):
        """启用专属密钥库

        启用租户专属密钥库
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableKeyStore
        :type request: :class:`huaweicloudsdkkms.v2.EnableKeyStoreRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.EnableKeyStoreResponse`
        """
        return self.enable_key_store_with_http_info(request)

    def enable_key_store_with_http_info(self, request):
        all_params = ['keystore_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'keystore_id' in local_var_params:
            path_params['keystore_id'] = local_var_params['keystore_id']

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
            resource_path='/v1.0/{project_id}/keystores/{keystore_id}/enable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='EnableKeyStoreResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def encrypt_data_async(self, request):
        """加密数据

        - 功能介绍：加密数据，用指定的用户主密钥加密数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EncryptData
        :type request: :class:`huaweicloudsdkkms.v2.EncryptDataRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.EncryptDataResponse`
        """
        return self.encrypt_data_with_http_info(request)

    def encrypt_data_with_http_info(self, request):
        all_params = ['encrypt_data_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/encrypt-data',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='EncryptDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def encrypt_datakey_async(self, request):
        """加密数据密钥

        - 功能介绍：加密数据密钥，用指定的主密钥加密数据密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EncryptDatakey
        :type request: :class:`huaweicloudsdkkms.v2.EncryptDatakeyRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.EncryptDatakeyResponse`
        """
        return self.encrypt_datakey_with_http_info(request)

    def encrypt_datakey_with_http_info(self, request):
        all_params = ['encrypt_datakey_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/encrypt-datakey',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='EncryptDatakeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def import_key_material_async(self, request):
        """导入密钥材料

        - 功能介绍：导入密钥材料。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportKeyMaterial
        :type request: :class:`huaweicloudsdkkms.v2.ImportKeyMaterialRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ImportKeyMaterialResponse`
        """
        return self.import_key_material_with_http_info(request)

    def import_key_material_with_http_info(self, request):
        all_params = ['import_key_material_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/import-key-material',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ImportKeyMaterialResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_grants_async(self, request):
        """查询授权列表

        - 功能介绍：查询密钥的授权列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGrants
        :type request: :class:`huaweicloudsdkkms.v2.ListGrantsRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ListGrantsResponse`
        """
        return self.list_grants_with_http_info(request)

    def list_grants_with_http_info(self, request):
        all_params = ['list_grants_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/list-grants',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListGrantsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_key_detail_async(self, request):
        """查询密钥信息

        - 功能介绍：查询密钥详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKeyDetail
        :type request: :class:`huaweicloudsdkkms.v2.ListKeyDetailRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ListKeyDetailResponse`
        """
        return self.list_key_detail_with_http_info(request)

    def list_key_detail_with_http_info(self, request):
        all_params = ['list_key_detail_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/describe-key',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListKeyDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_key_stores_async(self, request):
        """查询专属密钥库列表

        查询租户专属密钥库列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKeyStores
        :type request: :class:`huaweicloudsdkkms.v2.ListKeyStoresRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ListKeyStoresResponse`
        """
        return self.list_key_stores_with_http_info(request)

    def list_key_stores_with_http_info(self, request):
        all_params = ['limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/keystores',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListKeyStoresResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_keys_async(self, request):
        """查询密钥列表

        - 功能介绍：查询用户所有密钥列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKeys
        :type request: :class:`huaweicloudsdkkms.v2.ListKeysRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ListKeysResponse`
        """
        return self.list_keys_with_http_info(request)

    def list_keys_with_http_info(self, request):
        all_params = ['list_keys_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/list-keys',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListKeysResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_kms_by_tags_async(self, request):
        """查询密钥实例

        - 功能介绍：查询密钥实例。通过标签过滤，查询指定用户主密钥的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKmsByTags
        :type request: :class:`huaweicloudsdkkms.v2.ListKmsByTagsRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ListKmsByTagsResponse`
        """
        return self.list_kms_by_tags_with_http_info(request)

    def list_kms_by_tags_with_http_info(self, request):
        all_params = ['resource_instances', 'list_kms_by_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_instances' in local_var_params:
            path_params['resource_instances'] = local_var_params['resource_instances']

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
            resource_path='/v1.0/{project_id}/kms/{resource_instances}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListKmsByTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_kms_tags_async(self, request):
        """查询项目标签

        - 功能介绍：查询用户在指定项目下的所有标签集合。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKmsTags
        :type request: :class:`huaweicloudsdkkms.v2.ListKmsTagsRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ListKmsTagsResponse`
        """
        return self.list_kms_tags_with_http_info(request)

    def list_kms_tags_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListKmsTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_retirable_grants_async(self, request):
        """查询可退役授权列表

        - 功能介绍：查询用户可以退役的授权列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRetirableGrants
        :type request: :class:`huaweicloudsdkkms.v2.ListRetirableGrantsRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ListRetirableGrantsResponse`
        """
        return self.list_retirable_grants_with_http_info(request)

    def list_retirable_grants_with_http_info(self, request):
        all_params = ['list_retirable_grants_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/list-retirable-grants',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRetirableGrantsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_key_rotation_status_async(self, request):
        """查询密钥轮换状态

        - 功能介绍：查询用户主密钥轮换状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowKeyRotationStatus
        :type request: :class:`huaweicloudsdkkms.v2.ShowKeyRotationStatusRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ShowKeyRotationStatusResponse`
        """
        return self.show_key_rotation_status_with_http_info(request)

    def show_key_rotation_status_with_http_info(self, request):
        all_params = ['show_key_rotation_status_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/get-key-rotation-status',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowKeyRotationStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_key_store_async(self, request):
        """获取专属密钥库

        获取租户专属密钥库
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowKeyStore
        :type request: :class:`huaweicloudsdkkms.v2.ShowKeyStoreRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ShowKeyStoreResponse`
        """
        return self.show_key_store_with_http_info(request)

    def show_key_store_with_http_info(self, request):
        all_params = ['keystore_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'keystore_id' in local_var_params:
            path_params['keystore_id'] = local_var_params['keystore_id']

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
            resource_path='/v1.0/{project_id}/keystores/{keystore_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowKeyStoreResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_kms_tags_async(self, request):
        """查询密钥标签

        - 功能介绍：查询密钥标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowKmsTags
        :type request: :class:`huaweicloudsdkkms.v2.ShowKmsTagsRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ShowKmsTagsResponse`
        """
        return self.show_kms_tags_with_http_info(request)

    def show_kms_tags_with_http_info(self, request):
        all_params = ['key_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'key_id' in local_var_params:
            path_params['key_id'] = local_var_params['key_id']

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
            resource_path='/v1.0/{project_id}/kms/{key_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowKmsTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_public_key_async(self, request):
        """查询公钥信息

        - 查询用户指定非对称密钥的公钥信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPublicKey
        :type request: :class:`huaweicloudsdkkms.v2.ShowPublicKeyRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ShowPublicKeyResponse`
        """
        return self.show_public_key_with_http_info(request)

    def show_public_key_with_http_info(self, request):
        all_params = ['show_public_key_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/get-publickey',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPublicKeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_user_instances_async(self, request):
        """查询实例数

        - 功能介绍：查询实例数，获取用户已经创建的用户主密钥数量。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowUserInstances
        :type request: :class:`huaweicloudsdkkms.v2.ShowUserInstancesRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ShowUserInstancesResponse`
        """
        return self.show_user_instances_with_http_info(request)

    def show_user_instances_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/user-instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowUserInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_user_quotas_async(self, request):
        """查询配额

        - 功能介绍：查询配额，查询用户可以创建的用户主密钥配额总数及当前使用量信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowUserQuotas
        :type request: :class:`huaweicloudsdkkms.v2.ShowUserQuotasRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ShowUserQuotasResponse`
        """
        return self.show_user_quotas_with_http_info(request)

    def show_user_quotas_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/user-quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowUserQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def sign_async(self, request):
        """签名数据

        - 功能介绍：使用非对称密钥的私钥对消息或消息摘要进行数字签名。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for Sign
        :type request: :class:`huaweicloudsdkkms.v2.SignRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.SignResponse`
        """
        return self.sign_with_http_info(request)

    def sign_with_http_info(self, request):
        all_params = ['sign_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/sign',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SignResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_key_alias_async(self, request):
        """修改密钥别名

        - 功能介绍：修改用户主密钥别名。
        - 说明：
           - 服务默认主密钥（密钥别名后缀为“/default”）不可以修改。
           - 密钥处于“计划删除”状态，密钥别名不可以修改。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateKeyAlias
        :type request: :class:`huaweicloudsdkkms.v2.UpdateKeyAliasRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.UpdateKeyAliasResponse`
        """
        return self.update_key_alias_with_http_info(request)

    def update_key_alias_with_http_info(self, request):
        all_params = ['update_key_alias_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/update-key-alias',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateKeyAliasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_key_description_async(self, request):
        """修改密钥描述

        - 功能介绍：修改用户主密钥描述信息。
        - 说明：
           - 服务默认主密钥（密钥别名后缀为“/default”）不可以修改。
           - 密钥处于“计划删除”状态，密钥描述不可以修改。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateKeyDescription
        :type request: :class:`huaweicloudsdkkms.v2.UpdateKeyDescriptionRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.UpdateKeyDescriptionResponse`
        """
        return self.update_key_description_with_http_info(request)

    def update_key_description_with_http_info(self, request):
        all_params = ['update_key_description_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/update-key-description',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateKeyDescriptionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_key_rotation_interval_async(self, request):
        """修改密钥轮换周期

        - 功能介绍：修改用户主密钥轮换周期。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateKeyRotationInterval
        :type request: :class:`huaweicloudsdkkms.v2.UpdateKeyRotationIntervalRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.UpdateKeyRotationIntervalResponse`
        """
        return self.update_key_rotation_interval_with_http_info(request)

    def update_key_rotation_interval_with_http_info(self, request):
        all_params = ['update_key_rotation_interval_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/update-key-rotation-interval',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateKeyRotationIntervalResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def validate_signature_async(self, request):
        """验证签名

        - 功能介绍：使用非对称密钥的私钥对消息或消息摘要进行签名验证。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ValidateSignature
        :type request: :class:`huaweicloudsdkkms.v2.ValidateSignatureRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ValidateSignatureResponse`
        """
        return self.validate_signature_with_http_info(request)

    def validate_signature_with_http_info(self, request):
        all_params = ['validate_signature_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/kms/verify',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ValidateSignatureResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_version_async(self, request):
        """查询指定版本信息

        - 功能介绍：查指定API版本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVersion
        :type request: :class:`huaweicloudsdkkms.v2.ShowVersionRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ShowVersionResponse`
        """
        return self.show_version_with_http_info(request)

    def show_version_with_http_info(self, request):
        all_params = ['version_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/{version_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_versions_async(self, request):
        """查询版本信息列表

        - 功能介绍：查询API版本信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVersions
        :type request: :class:`huaweicloudsdkkms.v2.ShowVersionsRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ShowVersionsResponse`
        """
        return self.show_versions_with_http_info(request)

    def show_versions_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowVersionsResponse',
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
