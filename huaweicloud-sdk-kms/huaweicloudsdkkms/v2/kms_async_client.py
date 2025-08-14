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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkkms'")


class KmsAsyncClient(Client):
    def __init__(self):
        super(KmsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkkms.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "KmsAsyncClient":
                raise TypeError("client type error, support client type is KmsAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def associate_alias_async(self, request):
        r"""associate_alias

        关联别名。
        你可以将别名从原密钥关联到另一个新的密钥
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateAlias
        :type request: :class:`huaweicloudsdkkms.v2.AssociateAliasRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.AssociateAliasResponse`
        """
        http_info = self._associate_alias_http_info(request)
        return self._call_api(**http_info)

    def associate_alias_async_invoker(self, request):
        http_info = self._associate_alias_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_alias_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/alias/associate",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateAliasResponse"
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

    def batch_create_kms_tags_async(self, request):
        r"""批量添加删除密钥标签

        - 功能介绍：批量添加删除密钥标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateKmsTags
        :type request: :class:`huaweicloudsdkkms.v2.BatchCreateKmsTagsRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.BatchCreateKmsTagsResponse`
        """
        http_info = self._batch_create_kms_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_kms_tags_async_invoker(self, request):
        http_info = self._batch_create_kms_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_kms_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/{key_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateKmsTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'key_id' in local_var_params:
            path_params['key_id'] = local_var_params['key_id']

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

    def cancel_grant_async(self, request):
        r"""撤销授权

        - 功能介绍：撤销授权，授权用户撤销被授权用户操作密钥的权限。
        - 说明：
           - 创建密钥的用户才能撤销该密钥授权。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CancelGrant
        :type request: :class:`huaweicloudsdkkms.v2.CancelGrantRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.CancelGrantResponse`
        """
        http_info = self._cancel_grant_http_info(request)
        return self._call_api(**http_info)

    def cancel_grant_async_invoker(self, request):
        http_info = self._cancel_grant_http_info(request)
        return AsyncInvoker(self, http_info)

    def _cancel_grant_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/revoke-grant",
            "request_type": request.__class__.__name__,
            "response_type": "CancelGrantResponse"
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

    def cancel_key_deletion_async(self, request):
        r"""取消计划删除密钥

        - 功能介绍：取消计划删除密钥。
        - 说明：密钥处于“计划删除”状态才能取消计划删除密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CancelKeyDeletion
        :type request: :class:`huaweicloudsdkkms.v2.CancelKeyDeletionRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.CancelKeyDeletionResponse`
        """
        http_info = self._cancel_key_deletion_http_info(request)
        return self._call_api(**http_info)

    def cancel_key_deletion_async_invoker(self, request):
        http_info = self._cancel_key_deletion_http_info(request)
        return AsyncInvoker(self, http_info)

    def _cancel_key_deletion_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/cancel-key-deletion",
            "request_type": request.__class__.__name__,
            "response_type": "CancelKeyDeletionResponse"
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

    def cancel_self_grant_async(self, request):
        r"""退役授权

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
        http_info = self._cancel_self_grant_http_info(request)
        return self._call_api(**http_info)

    def cancel_self_grant_async_invoker(self, request):
        http_info = self._cancel_self_grant_http_info(request)
        return AsyncInvoker(self, http_info)

    def _cancel_self_grant_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/retire-grant",
            "request_type": request.__class__.__name__,
            "response_type": "CancelSelfGrantResponse"
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

    def create_alias_async(self, request):
        r"""create_alias

        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAlias
        :type request: :class:`huaweicloudsdkkms.v2.CreateAliasRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.CreateAliasResponse`
        """
        http_info = self._create_alias_http_info(request)
        return self._call_api(**http_info)

    def create_alias_async_invoker(self, request):
        http_info = self._create_alias_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_alias_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/aliases",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAliasResponse"
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

    def create_datakey_async(self, request):
        r"""创建数据密钥

        - 功能介绍：创建数据密钥，返回结果包含明文和密文。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDatakey
        :type request: :class:`huaweicloudsdkkms.v2.CreateDatakeyRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.CreateDatakeyResponse`
        """
        http_info = self._create_datakey_http_info(request)
        return self._call_api(**http_info)

    def create_datakey_async_invoker(self, request):
        http_info = self._create_datakey_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_datakey_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/create-datakey",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDatakeyResponse"
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

    def create_datakey_without_plaintext_async(self, request):
        r"""创建不含明文数据密钥

        - 功能介绍：创建数据密钥，返回结果只包含密文。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDatakeyWithoutPlaintext
        :type request: :class:`huaweicloudsdkkms.v2.CreateDatakeyWithoutPlaintextRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.CreateDatakeyWithoutPlaintextResponse`
        """
        http_info = self._create_datakey_without_plaintext_http_info(request)
        return self._call_api(**http_info)

    def create_datakey_without_plaintext_async_invoker(self, request):
        http_info = self._create_datakey_without_plaintext_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_datakey_without_plaintext_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/create-datakey-without-plaintext",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDatakeyWithoutPlaintextResponse"
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

    def create_ec_datakey_pair_async(self, request):
        r"""创建EC数据密钥对

        - 功能介绍：创建EC数据密钥对，返回结果包含明文公钥和密文私钥，根据参数决定是否返回明文私钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEcDatakeyPair
        :type request: :class:`huaweicloudsdkkms.v2.CreateEcDatakeyPairRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.CreateEcDatakeyPairResponse`
        """
        http_info = self._create_ec_datakey_pair_http_info(request)
        return self._call_api(**http_info)

    def create_ec_datakey_pair_async_invoker(self, request):
        http_info = self._create_ec_datakey_pair_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_ec_datakey_pair_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/create-ec-datakey-pair",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEcDatakeyPairResponse"
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

    def create_grant_async(self, request):
        r"""创建授权

        - 功能介绍：创建授权，被授权用户可以对授权密钥进行操作。
        - 说明：
           - 服务默认主密钥（密钥别名后缀为“/default”）不可以授权。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateGrant
        :type request: :class:`huaweicloudsdkkms.v2.CreateGrantRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.CreateGrantResponse`
        """
        http_info = self._create_grant_http_info(request)
        return self._call_api(**http_info)

    def create_grant_async_invoker(self, request):
        http_info = self._create_grant_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_grant_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/create-grant",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGrantResponse"
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

    def create_key_async(self, request):
        r"""创建密钥

        创建用户主密钥，用户主密钥可以为对称密钥或非对称密钥。
        - 对称密钥为长度为256位AES密钥或者128位SM4密钥，可用于小量数据的加密或者用于加密数据密钥。
        - 非对称密钥可以为RSA密钥对或者ECC密钥对（包含SM2密钥对），可用于加解密数据、数字签名及验签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateKey
        :type request: :class:`huaweicloudsdkkms.v2.CreateKeyRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.CreateKeyResponse`
        """
        http_info = self._create_key_http_info(request)
        return self._call_api(**http_info)

    def create_key_async_invoker(self, request):
        http_info = self._create_key_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_key_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/create-key",
            "request_type": request.__class__.__name__,
            "response_type": "CreateKeyResponse"
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

    def create_key_store_async(self, request):
        r"""创建专属密钥库

        - \&quot;创建租户专属密钥库，专属密钥库使用DHSM实例作为密钥的存储\&quot;
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateKeyStore
        :type request: :class:`huaweicloudsdkkms.v2.CreateKeyStoreRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.CreateKeyStoreResponse`
        """
        http_info = self._create_key_store_http_info(request)
        return self._call_api(**http_info)

    def create_key_store_async_invoker(self, request):
        http_info = self._create_key_store_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_key_store_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/keystores",
            "request_type": request.__class__.__name__,
            "response_type": "CreateKeyStoreResponse"
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

    def create_kms_tag_async(self, request):
        r"""添加密钥标签

        - 功能介绍：添加密钥标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateKmsTag
        :type request: :class:`huaweicloudsdkkms.v2.CreateKmsTagRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.CreateKmsTagResponse`
        """
        http_info = self._create_kms_tag_http_info(request)
        return self._call_api(**http_info)

    def create_kms_tag_async_invoker(self, request):
        http_info = self._create_kms_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_kms_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/{key_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreateKmsTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'key_id' in local_var_params:
            path_params['key_id'] = local_var_params['key_id']

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

    def create_parameters_for_import_async(self, request):
        r"""获取密钥导入参数

        - 功能介绍：获取导入密钥的必要参数，包括密钥导入令牌和密钥加密公钥。
        - 说明：返回的公钥类型默认为RSA_2048。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateParametersForImport
        :type request: :class:`huaweicloudsdkkms.v2.CreateParametersForImportRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.CreateParametersForImportResponse`
        """
        http_info = self._create_parameters_for_import_http_info(request)
        return self._call_api(**http_info)

    def create_parameters_for_import_async_invoker(self, request):
        http_info = self._create_parameters_for_import_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_parameters_for_import_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/get-parameters-for-import",
            "request_type": request.__class__.__name__,
            "response_type": "CreateParametersForImportResponse"
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

    def create_pin_async(self, request):
        r"""创建PIN码

        - 功能介绍：创建pin码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePin
        :type request: :class:`huaweicloudsdkkms.v2.CreatePinRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.CreatePinResponse`
        """
        http_info = self._create_pin_http_info(request)
        return self._call_api(**http_info)

    def create_pin_async_invoker(self, request):
        http_info = self._create_pin_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_pin_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/create-pin",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePinResponse"
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

    def create_random_async(self, request):
        r"""创建随机数

        - 功能介绍：
          生成8~8192bit范围内的随机数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRandom
        :type request: :class:`huaweicloudsdkkms.v2.CreateRandomRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.CreateRandomResponse`
        """
        http_info = self._create_random_http_info(request)
        return self._call_api(**http_info)

    def create_random_async_invoker(self, request):
        http_info = self._create_random_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_random_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/gen-random",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRandomResponse"
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

    def create_rsa_datakey_pair_async(self, request):
        r"""创建RSA数据密钥对

        - 功能介绍：创建rsa数据密钥对，返回结果包含明文公钥和密文私钥，根据参数决定是否返回明文私钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRsaDatakeyPair
        :type request: :class:`huaweicloudsdkkms.v2.CreateRsaDatakeyPairRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.CreateRsaDatakeyPairResponse`
        """
        http_info = self._create_rsa_datakey_pair_http_info(request)
        return self._call_api(**http_info)

    def create_rsa_datakey_pair_async_invoker(self, request):
        http_info = self._create_rsa_datakey_pair_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_rsa_datakey_pair_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/create-rsa-datakey-pair",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRsaDatakeyPairResponse"
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

    def decrypt_data_async(self, request):
        r"""解密数据

        - 功能介绍：解密数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DecryptData
        :type request: :class:`huaweicloudsdkkms.v2.DecryptDataRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.DecryptDataResponse`
        """
        http_info = self._decrypt_data_http_info(request)
        return self._call_api(**http_info)

    def decrypt_data_async_invoker(self, request):
        http_info = self._decrypt_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _decrypt_data_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/decrypt-data",
            "request_type": request.__class__.__name__,
            "response_type": "DecryptDataResponse"
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

    def decrypt_datakey_async(self, request):
        r"""解密数据密钥

        - 功能介绍：解密数据密钥，用指定的主密钥解密数据密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DecryptDatakey
        :type request: :class:`huaweicloudsdkkms.v2.DecryptDatakeyRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.DecryptDatakeyResponse`
        """
        http_info = self._decrypt_datakey_http_info(request)
        return self._call_api(**http_info)

    def decrypt_datakey_async_invoker(self, request):
        http_info = self._decrypt_datakey_http_info(request)
        return AsyncInvoker(self, http_info)

    def _decrypt_datakey_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/decrypt-datakey",
            "request_type": request.__class__.__name__,
            "response_type": "DecryptDatakeyResponse"
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

    def delete_alias_async(self, request):
        r"""delete_alias

        删除别名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAlias
        :type request: :class:`huaweicloudsdkkms.v2.DeleteAliasRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.DeleteAliasResponse`
        """
        http_info = self._delete_alias_http_info(request)
        return self._call_api(**http_info)

    def delete_alias_async_invoker(self, request):
        http_info = self._delete_alias_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_alias_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/kms/aliases",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAliasResponse"
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

    def delete_imported_key_material_async(self, request):
        r"""删除密钥材料

        - 功能介绍：删除密钥材料信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteImportedKeyMaterial
        :type request: :class:`huaweicloudsdkkms.v2.DeleteImportedKeyMaterialRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.DeleteImportedKeyMaterialResponse`
        """
        http_info = self._delete_imported_key_material_http_info(request)
        return self._call_api(**http_info)

    def delete_imported_key_material_async_invoker(self, request):
        http_info = self._delete_imported_key_material_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_imported_key_material_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/delete-imported-key-material",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteImportedKeyMaterialResponse"
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

    def delete_key_async(self, request):
        r"""计划删除密钥

        - 功能介绍：计划多少天后删除密钥，可设置7天～1096天内删除密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteKey
        :type request: :class:`huaweicloudsdkkms.v2.DeleteKeyRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.DeleteKeyResponse`
        """
        http_info = self._delete_key_http_info(request)
        return self._call_api(**http_info)

    def delete_key_async_invoker(self, request):
        http_info = self._delete_key_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_key_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/schedule-key-deletion",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteKeyResponse"
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

    def delete_key_store_async(self, request):
        r"""删除专属密钥库

        删除租户专属密钥库
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteKeyStore
        :type request: :class:`huaweicloudsdkkms.v2.DeleteKeyStoreRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.DeleteKeyStoreResponse`
        """
        http_info = self._delete_key_store_http_info(request)
        return self._call_api(**http_info)

    def delete_key_store_async_invoker(self, request):
        http_info = self._delete_key_store_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_key_store_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/keystores/{keystore_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteKeyStoreResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'keystore_id' in local_var_params:
            path_params['keystore_id'] = local_var_params['keystore_id']

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

    def delete_tag_async(self, request):
        r"""删除密钥标签

        - 功能介绍：删除密钥标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTag
        :type request: :class:`huaweicloudsdkkms.v2.DeleteTagRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.DeleteTagResponse`
        """
        http_info = self._delete_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_tag_async_invoker(self, request):
        http_info = self._delete_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_tag_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/kms/{key_id}/tags/{key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def disable_key_async(self, request):
        r"""禁用密钥

        - 功能介绍：禁用密钥，密钥禁用后不可以使用。
        - 说明：密钥为启用状态才能禁用密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisableKey
        :type request: :class:`huaweicloudsdkkms.v2.DisableKeyRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.DisableKeyResponse`
        """
        http_info = self._disable_key_http_info(request)
        return self._call_api(**http_info)

    def disable_key_async_invoker(self, request):
        http_info = self._disable_key_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disable_key_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/disable-key",
            "request_type": request.__class__.__name__,
            "response_type": "DisableKeyResponse"
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

    def disable_key_rotation_async(self, request):
        r"""关闭密钥轮换

        - 功能介绍：关闭用户主密钥轮换。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisableKeyRotation
        :type request: :class:`huaweicloudsdkkms.v2.DisableKeyRotationRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.DisableKeyRotationResponse`
        """
        http_info = self._disable_key_rotation_http_info(request)
        return self._call_api(**http_info)

    def disable_key_rotation_async_invoker(self, request):
        http_info = self._disable_key_rotation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disable_key_rotation_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/disable-key-rotation",
            "request_type": request.__class__.__name__,
            "response_type": "DisableKeyRotationResponse"
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

    def disable_key_store_async(self, request):
        r"""禁用专属密钥库

        禁用租户专属密钥库
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisableKeyStore
        :type request: :class:`huaweicloudsdkkms.v2.DisableKeyStoreRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.DisableKeyStoreResponse`
        """
        http_info = self._disable_key_store_http_info(request)
        return self._call_api(**http_info)

    def disable_key_store_async_invoker(self, request):
        http_info = self._disable_key_store_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disable_key_store_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/keystores/{keystore_id}/disable",
            "request_type": request.__class__.__name__,
            "response_type": "DisableKeyStoreResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'keystore_id' in local_var_params:
            path_params['keystore_id'] = local_var_params['keystore_id']

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

    def enable_key_async(self, request):
        r"""启用密钥

        - 功能介绍：启用密钥，密钥启用后才可以使用。
        - 说明：密钥为禁用状态才能启用密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableKey
        :type request: :class:`huaweicloudsdkkms.v2.EnableKeyRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.EnableKeyResponse`
        """
        http_info = self._enable_key_http_info(request)
        return self._call_api(**http_info)

    def enable_key_async_invoker(self, request):
        http_info = self._enable_key_http_info(request)
        return AsyncInvoker(self, http_info)

    def _enable_key_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/enable-key",
            "request_type": request.__class__.__name__,
            "response_type": "EnableKeyResponse"
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

    def enable_key_rotation_async(self, request):
        r"""开启密钥轮换

        - 功能介绍：开启用户主密钥轮换。
        - 说明：
          - 开启密钥轮换后，默认轮换间隔时间为365天。
          - 默认主密钥及外部导入密钥不支持轮换操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableKeyRotation
        :type request: :class:`huaweicloudsdkkms.v2.EnableKeyRotationRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.EnableKeyRotationResponse`
        """
        http_info = self._enable_key_rotation_http_info(request)
        return self._call_api(**http_info)

    def enable_key_rotation_async_invoker(self, request):
        http_info = self._enable_key_rotation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _enable_key_rotation_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/enable-key-rotation",
            "request_type": request.__class__.__name__,
            "response_type": "EnableKeyRotationResponse"
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

    def enable_key_store_async(self, request):
        r"""启用专属密钥库

        启用租户专属密钥库
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableKeyStore
        :type request: :class:`huaweicloudsdkkms.v2.EnableKeyStoreRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.EnableKeyStoreResponse`
        """
        http_info = self._enable_key_store_http_info(request)
        return self._call_api(**http_info)

    def enable_key_store_async_invoker(self, request):
        http_info = self._enable_key_store_http_info(request)
        return AsyncInvoker(self, http_info)

    def _enable_key_store_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/keystores/{keystore_id}/enable",
            "request_type": request.__class__.__name__,
            "response_type": "EnableKeyStoreResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'keystore_id' in local_var_params:
            path_params['keystore_id'] = local_var_params['keystore_id']

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

    def encrypt_data_async(self, request):
        r"""加密数据

        - 功能介绍：加密数据，用指定的用户主密钥加密数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EncryptData
        :type request: :class:`huaweicloudsdkkms.v2.EncryptDataRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.EncryptDataResponse`
        """
        http_info = self._encrypt_data_http_info(request)
        return self._call_api(**http_info)

    def encrypt_data_async_invoker(self, request):
        http_info = self._encrypt_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _encrypt_data_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/encrypt-data",
            "request_type": request.__class__.__name__,
            "response_type": "EncryptDataResponse"
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

    def encrypt_datakey_async(self, request):
        r"""加密数据密钥

        - 功能介绍：加密数据密钥，用指定的主密钥加密数据密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EncryptDatakey
        :type request: :class:`huaweicloudsdkkms.v2.EncryptDatakeyRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.EncryptDatakeyResponse`
        """
        http_info = self._encrypt_datakey_http_info(request)
        return self._call_api(**http_info)

    def encrypt_datakey_async_invoker(self, request):
        http_info = self._encrypt_datakey_http_info(request)
        return AsyncInvoker(self, http_info)

    def _encrypt_datakey_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/encrypt-datakey",
            "request_type": request.__class__.__name__,
            "response_type": "EncryptDatakeyResponse"
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

    def generate_mac_async(self, request):
        r"""生成消息验证码

        功能介绍：生成消息验证码
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GenerateMac
        :type request: :class:`huaweicloudsdkkms.v2.GenerateMacRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.GenerateMacResponse`
        """
        http_info = self._generate_mac_http_info(request)
        return self._call_api(**http_info)

    def generate_mac_async_invoker(self, request):
        http_info = self._generate_mac_http_info(request)
        return AsyncInvoker(self, http_info)

    def _generate_mac_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/generate-mac",
            "request_type": request.__class__.__name__,
            "response_type": "GenerateMacResponse"
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

    def import_key_material_async(self, request):
        r"""导入密钥材料

        - 功能介绍：导入密钥材料。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportKeyMaterial
        :type request: :class:`huaweicloudsdkkms.v2.ImportKeyMaterialRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ImportKeyMaterialResponse`
        """
        http_info = self._import_key_material_http_info(request)
        return self._call_api(**http_info)

    def import_key_material_async_invoker(self, request):
        http_info = self._import_key_material_http_info(request)
        return AsyncInvoker(self, http_info)

    def _import_key_material_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/import-key-material",
            "request_type": request.__class__.__name__,
            "response_type": "ImportKeyMaterialResponse"
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

    def list_aliases_async(self, request):
        r"""list_aliases

        查询一个密钥关联的所有别名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAliases
        :type request: :class:`huaweicloudsdkkms.v2.ListAliasesRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ListAliasesResponse`
        """
        http_info = self._list_aliases_http_info(request)
        return self._call_api(**http_info)

    def list_aliases_async_invoker(self, request):
        http_info = self._list_aliases_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_aliases_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/kms/aliases",
            "request_type": request.__class__.__name__,
            "response_type": "ListAliasesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'key_id' in local_var_params:
            query_params.append(('key_id', local_var_params['key_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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

    def list_grants_async(self, request):
        r"""查询授权列表

        - 功能介绍：查询密钥的授权列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGrants
        :type request: :class:`huaweicloudsdkkms.v2.ListGrantsRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ListGrantsResponse`
        """
        http_info = self._list_grants_http_info(request)
        return self._call_api(**http_info)

    def list_grants_async_invoker(self, request):
        http_info = self._list_grants_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_grants_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/list-grants",
            "request_type": request.__class__.__name__,
            "response_type": "ListGrantsResponse"
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

    def list_key_detail_async(self, request):
        r"""查询密钥信息

        - 功能介绍：查询密钥详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKeyDetail
        :type request: :class:`huaweicloudsdkkms.v2.ListKeyDetailRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ListKeyDetailResponse`
        """
        http_info = self._list_key_detail_http_info(request)
        return self._call_api(**http_info)

    def list_key_detail_async_invoker(self, request):
        http_info = self._list_key_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_key_detail_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/describe-key",
            "request_type": request.__class__.__name__,
            "response_type": "ListKeyDetailResponse"
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

    def list_key_stores_async(self, request):
        r"""查询专属密钥库列表

        查询租户专属密钥库列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKeyStores
        :type request: :class:`huaweicloudsdkkms.v2.ListKeyStoresRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ListKeyStoresResponse`
        """
        http_info = self._list_key_stores_http_info(request)
        return self._call_api(**http_info)

    def list_key_stores_async_invoker(self, request):
        http_info = self._list_key_stores_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_key_stores_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/keystores",
            "request_type": request.__class__.__name__,
            "response_type": "ListKeyStoresResponse"
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

    def list_keys_async(self, request):
        r"""查询密钥列表

        - 功能介绍：查询用户所有密钥列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKeys
        :type request: :class:`huaweicloudsdkkms.v2.ListKeysRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ListKeysResponse`
        """
        http_info = self._list_keys_http_info(request)
        return self._call_api(**http_info)

    def list_keys_async_invoker(self, request):
        http_info = self._list_keys_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_keys_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/list-keys",
            "request_type": request.__class__.__name__,
            "response_type": "ListKeysResponse"
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

    def list_kms_by_tags_async(self, request):
        r"""查询密钥实例

        - 功能介绍：查询密钥实例。通过标签过滤，查询指定用户主密钥的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKmsByTags
        :type request: :class:`huaweicloudsdkkms.v2.ListKmsByTagsRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ListKmsByTagsResponse`
        """
        http_info = self._list_kms_by_tags_http_info(request)
        return self._call_api(**http_info)

    def list_kms_by_tags_async_invoker(self, request):
        http_info = self._list_kms_by_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_kms_by_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/{resource_instances}/action",
            "request_type": request.__class__.__name__,
            "response_type": "ListKmsByTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_instances' in local_var_params:
            path_params['resource_instances'] = local_var_params['resource_instances']

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

    def list_kms_tags_async(self, request):
        r"""查询项目标签

        - 功能介绍：查询用户在指定项目下的所有标签集合。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKmsTags
        :type request: :class:`huaweicloudsdkkms.v2.ListKmsTagsRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ListKmsTagsResponse`
        """
        http_info = self._list_kms_tags_http_info(request)
        return self._call_api(**http_info)

    def list_kms_tags_async_invoker(self, request):
        http_info = self._list_kms_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_kms_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/kms/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListKmsTagsResponse"
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

    def list_retirable_grants_async(self, request):
        r"""查询可退役授权列表

        - 功能介绍：查询用户可以退役的授权列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRetirableGrants
        :type request: :class:`huaweicloudsdkkms.v2.ListRetirableGrantsRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ListRetirableGrantsResponse`
        """
        http_info = self._list_retirable_grants_http_info(request)
        return self._call_api(**http_info)

    def list_retirable_grants_async_invoker(self, request):
        http_info = self._list_retirable_grants_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_retirable_grants_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/list-retirable-grants",
            "request_type": request.__class__.__name__,
            "response_type": "ListRetirableGrantsResponse"
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

    def list_support_regions_async(self, request):
        r"""查询跨区域密钥所支持的区域

        - 功能介绍：查询跨区域密钥所支持的区域。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSupportRegions
        :type request: :class:`huaweicloudsdkkms.v2.ListSupportRegionsRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ListSupportRegionsResponse`
        """
        http_info = self._list_support_regions_http_info(request)
        return self._call_api(**http_info)

    def list_support_regions_async_invoker(self, request):
        http_info = self._list_support_regions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_support_regions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/kms/regions",
            "request_type": request.__class__.__name__,
            "response_type": "ListSupportRegionsResponse"
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

    def replicate_key_async(self, request):
        r"""复制密钥到指定区域

        将本区域的密钥复制到指定区域。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ReplicateKey
        :type request: :class:`huaweicloudsdkkms.v2.ReplicateKeyRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ReplicateKeyResponse`
        """
        http_info = self._replicate_key_http_info(request)
        return self._call_api(**http_info)

    def replicate_key_async_invoker(self, request):
        http_info = self._replicate_key_http_info(request)
        return AsyncInvoker(self, http_info)

    def _replicate_key_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/kms/keys/{key_id}/replicate",
            "request_type": request.__class__.__name__,
            "response_type": "ReplicateKeyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'key_id' in local_var_params:
            path_params['key_id'] = local_var_params['key_id']

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

    def show_key_rotation_status_async(self, request):
        r"""查询密钥轮换状态

        - 功能介绍：查询用户主密钥轮换状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowKeyRotationStatus
        :type request: :class:`huaweicloudsdkkms.v2.ShowKeyRotationStatusRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ShowKeyRotationStatusResponse`
        """
        http_info = self._show_key_rotation_status_http_info(request)
        return self._call_api(**http_info)

    def show_key_rotation_status_async_invoker(self, request):
        http_info = self._show_key_rotation_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_key_rotation_status_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/get-key-rotation-status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowKeyRotationStatusResponse"
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

    def show_key_store_async(self, request):
        r"""获取专属密钥库

        获取租户专属密钥库
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowKeyStore
        :type request: :class:`huaweicloudsdkkms.v2.ShowKeyStoreRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ShowKeyStoreResponse`
        """
        http_info = self._show_key_store_http_info(request)
        return self._call_api(**http_info)

    def show_key_store_async_invoker(self, request):
        http_info = self._show_key_store_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_key_store_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/keystores/{keystore_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowKeyStoreResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'keystore_id' in local_var_params:
            path_params['keystore_id'] = local_var_params['keystore_id']

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

    def show_kms_tags_async(self, request):
        r"""查询密钥标签

        - 功能介绍：查询密钥标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowKmsTags
        :type request: :class:`huaweicloudsdkkms.v2.ShowKmsTagsRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ShowKmsTagsResponse`
        """
        http_info = self._show_kms_tags_http_info(request)
        return self._call_api(**http_info)

    def show_kms_tags_async_invoker(self, request):
        http_info = self._show_kms_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_kms_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/kms/{key_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowKmsTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'key_id' in local_var_params:
            path_params['key_id'] = local_var_params['key_id']

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

    def show_public_key_async(self, request):
        r"""查询公钥信息

        - 查询用户指定非对称密钥的公钥信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPublicKey
        :type request: :class:`huaweicloudsdkkms.v2.ShowPublicKeyRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ShowPublicKeyResponse`
        """
        http_info = self._show_public_key_http_info(request)
        return self._call_api(**http_info)

    def show_public_key_async_invoker(self, request):
        http_info = self._show_public_key_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_public_key_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/get-publickey",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPublicKeyResponse"
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

    def show_user_instances_async(self, request):
        r"""查询实例数

        - 功能介绍：查询实例数，获取用户已经创建的用户主密钥数量。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowUserInstances
        :type request: :class:`huaweicloudsdkkms.v2.ShowUserInstancesRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ShowUserInstancesResponse`
        """
        http_info = self._show_user_instances_http_info(request)
        return self._call_api(**http_info)

    def show_user_instances_async_invoker(self, request):
        http_info = self._show_user_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_user_instances_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/kms/user-instances",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUserInstancesResponse"
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

    def show_user_quotas_async(self, request):
        r"""查询配额

        - 功能介绍：查询配额，查询用户可以创建的用户主密钥配额总数及当前使用量信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowUserQuotas
        :type request: :class:`huaweicloudsdkkms.v2.ShowUserQuotasRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ShowUserQuotasResponse`
        """
        http_info = self._show_user_quotas_http_info(request)
        return self._call_api(**http_info)

    def show_user_quotas_async_invoker(self, request):
        http_info = self._show_user_quotas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_user_quotas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/kms/user-quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUserQuotasResponse"
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

    def sign_async(self, request):
        r"""签名数据

        - 功能介绍：使用非对称密钥的私钥对消息或消息摘要进行数字签名。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for Sign
        :type request: :class:`huaweicloudsdkkms.v2.SignRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.SignResponse`
        """
        http_info = self._sign_http_info(request)
        return self._call_api(**http_info)

    def sign_async_invoker(self, request):
        http_info = self._sign_http_info(request)
        return AsyncInvoker(self, http_info)

    def _sign_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/sign",
            "request_type": request.__class__.__name__,
            "response_type": "SignResponse"
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

    def update_key_alias_async(self, request):
        r"""修改密钥别名

        - 功能介绍：修改用户主密钥别名。
        - 说明：
           - 服务默认主密钥（密钥别名后缀为“/default”）不可以修改。
           - 密钥处于“计划删除”状态，密钥别名不可以修改。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateKeyAlias
        :type request: :class:`huaweicloudsdkkms.v2.UpdateKeyAliasRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.UpdateKeyAliasResponse`
        """
        http_info = self._update_key_alias_http_info(request)
        return self._call_api(**http_info)

    def update_key_alias_async_invoker(self, request):
        http_info = self._update_key_alias_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_key_alias_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/update-key-alias",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateKeyAliasResponse"
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

    def update_key_description_async(self, request):
        r"""修改密钥描述

        - 功能介绍：修改用户主密钥描述信息。
        - 说明：
           - 服务默认主密钥（密钥别名后缀为“/default”）不可以修改。
           - 密钥处于“计划删除”状态，密钥描述不可以修改。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateKeyDescription
        :type request: :class:`huaweicloudsdkkms.v2.UpdateKeyDescriptionRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.UpdateKeyDescriptionResponse`
        """
        http_info = self._update_key_description_http_info(request)
        return self._call_api(**http_info)

    def update_key_description_async_invoker(self, request):
        http_info = self._update_key_description_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_key_description_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/update-key-description",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateKeyDescriptionResponse"
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

    def update_key_rotation_interval_async(self, request):
        r"""修改密钥轮换周期

        - 功能介绍：修改用户主密钥轮换周期。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateKeyRotationInterval
        :type request: :class:`huaweicloudsdkkms.v2.UpdateKeyRotationIntervalRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.UpdateKeyRotationIntervalResponse`
        """
        http_info = self._update_key_rotation_interval_http_info(request)
        return self._call_api(**http_info)

    def update_key_rotation_interval_async_invoker(self, request):
        http_info = self._update_key_rotation_interval_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_key_rotation_interval_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/update-key-rotation-interval",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateKeyRotationIntervalResponse"
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

    def update_primary_region_async(self, request):
        r"""修改密钥所属的主区域

        修改密钥所属的主区域。修改后当前区域会变为副本区域。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePrimaryRegion
        :type request: :class:`huaweicloudsdkkms.v2.UpdatePrimaryRegionRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.UpdatePrimaryRegionResponse`
        """
        http_info = self._update_primary_region_http_info(request)
        return self._call_api(**http_info)

    def update_primary_region_async_invoker(self, request):
        http_info = self._update_primary_region_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_primary_region_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/kms/keys/{key_id}/update-primary-region",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePrimaryRegionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'key_id' in local_var_params:
            path_params['key_id'] = local_var_params['key_id']

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

    def validate_signature_async(self, request):
        r"""验证签名

        - 功能介绍：使用非对称密钥的私钥对消息或消息摘要进行签名验证。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ValidateSignature
        :type request: :class:`huaweicloudsdkkms.v2.ValidateSignatureRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ValidateSignatureResponse`
        """
        http_info = self._validate_signature_http_info(request)
        return self._call_api(**http_info)

    def validate_signature_async_invoker(self, request):
        http_info = self._validate_signature_http_info(request)
        return AsyncInvoker(self, http_info)

    def _validate_signature_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/verify",
            "request_type": request.__class__.__name__,
            "response_type": "ValidateSignatureResponse"
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

    def verify_mac_async(self, request):
        r"""校验消息验证码

        功能介绍：校验消息验证码
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for VerifyMac
        :type request: :class:`huaweicloudsdkkms.v2.VerifyMacRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.VerifyMacResponse`
        """
        http_info = self._verify_mac_http_info(request)
        return self._call_api(**http_info)

    def verify_mac_async_invoker(self, request):
        http_info = self._verify_mac_http_info(request)
        return AsyncInvoker(self, http_info)

    def _verify_mac_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/kms/verify-mac",
            "request_type": request.__class__.__name__,
            "response_type": "VerifyMacResponse"
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

    def show_version_async(self, request):
        r"""查询指定版本信息

        - 功能介绍：查指定API版本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVersion
        :type request: :class:`huaweicloudsdkkms.v2.ShowVersionRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ShowVersionResponse`
        """
        http_info = self._show_version_http_info(request)
        return self._call_api(**http_info)

    def show_version_async_invoker(self, request):
        http_info = self._show_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_version_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/{version_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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

    def show_versions_async(self, request):
        r"""查询版本信息列表

        - 功能介绍：查询API版本信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVersions
        :type request: :class:`huaweicloudsdkkms.v2.ShowVersionsRequest`
        :rtype: :class:`huaweicloudsdkkms.v2.ShowVersionsResponse`
        """
        http_info = self._show_versions_http_info(request)
        return self._call_api(**http_info)

    def show_versions_async_invoker(self, request):
        http_info = self._show_versions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_versions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVersionsResponse"
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
