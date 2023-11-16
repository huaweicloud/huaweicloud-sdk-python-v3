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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkccm'")


class CcmClient(Client):
    def __init__(self):
        super(CcmClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkccm.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials")
        else:
            if clazz.__name__ != "CcmClient":
                raise TypeError("client type error, support client type is CcmClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials")

        

        return client_builder

    def batch_create_ca_tags(self, request):
        """批量创建CA标签

        批量创建CA标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateCaTags
        :type request: :class:`huaweicloudsdkccm.v1.BatchCreateCaTagsRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.BatchCreateCaTagsResponse`
        """
        http_info = self._batch_create_ca_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_ca_tags_invoker(self, request):
        http_info = self._batch_create_ca_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_ca_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-certificate-authorities/{ca_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateCaTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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

    def batch_create_cert_tags(self, request):
        """批量创建证书标签

        批量创建证书标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateCertTags
        :type request: :class:`huaweicloudsdkccm.v1.BatchCreateCertTagsRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.BatchCreateCertTagsResponse`
        """
        http_info = self._batch_create_cert_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_cert_tags_invoker(self, request):
        http_info = self._batch_create_cert_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_cert_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-certificates/{certificate_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateCertTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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

    def batch_delete_ca_tags(self, request):
        """批量删除CA标签

        批量删除CA标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteCaTags
        :type request: :class:`huaweicloudsdkccm.v1.BatchDeleteCaTagsRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.BatchDeleteCaTagsResponse`
        """
        http_info = self._batch_delete_ca_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_ca_tags_invoker(self, request):
        http_info = self._batch_delete_ca_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_ca_tags_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/private-certificate-authorities/{ca_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteCaTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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

    def batch_delete_cert_tags(self, request):
        """批量删除证书标签

        批量删除证书标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteCertTags
        :type request: :class:`huaweicloudsdkccm.v1.BatchDeleteCertTagsRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.BatchDeleteCertTagsResponse`
        """
        http_info = self._batch_delete_cert_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_cert_tags_invoker(self, request):
        http_info = self._batch_delete_cert_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_cert_tags_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/private-certificates/{certificate_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteCertTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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

    def count_ca_resource_instances(self, request):
        """根据标签查询CA数量

        根据标签查询CA数量。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountCaResourceInstances
        :type request: :class:`huaweicloudsdkccm.v1.CountCaResourceInstancesRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.CountCaResourceInstancesResponse`
        """
        http_info = self._count_ca_resource_instances_http_info(request)
        return self._call_api(**http_info)

    def count_ca_resource_instances_invoker(self, request):
        http_info = self._count_ca_resource_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _count_ca_resource_instances_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-certificate-authorities/resource-instances/count",
            "request_type": request.__class__.__name__,
            "response_type": "CountCaResourceInstancesResponse"
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

    def count_cert_resource_instances(self, request):
        """根据标签查询证书数量

        根据标签查询证书数量。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountCertResourceInstances
        :type request: :class:`huaweicloudsdkccm.v1.CountCertResourceInstancesRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.CountCertResourceInstancesResponse`
        """
        http_info = self._count_cert_resource_instances_http_info(request)
        return self._call_api(**http_info)

    def count_cert_resource_instances_invoker(self, request):
        http_info = self._count_cert_resource_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _count_cert_resource_instances_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-certificates/resource-instances/count",
            "request_type": request.__class__.__name__,
            "response_type": "CountCertResourceInstancesResponse"
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

    def create_ca_tag(self, request):
        """创建CA标签

        创建CA标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCaTag
        :type request: :class:`huaweicloudsdkccm.v1.CreateCaTagRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.CreateCaTagResponse`
        """
        http_info = self._create_ca_tag_http_info(request)
        return self._call_api(**http_info)

    def create_ca_tag_invoker(self, request):
        http_info = self._create_ca_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_ca_tag_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-certificate-authorities/{ca_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCaTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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

    def create_cert_tag(self, request):
        """创建证书标签

        创建证书标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCertTag
        :type request: :class:`huaweicloudsdkccm.v1.CreateCertTagRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.CreateCertTagResponse`
        """
        http_info = self._create_cert_tag_http_info(request)
        return self._call_api(**http_info)

    def create_cert_tag_invoker(self, request):
        http_info = self._create_cert_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_cert_tag_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-certificates/{certificate_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCertTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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

    def create_certificate(self, request):
        """申请证书

        申请证书。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCertificate
        :type request: :class:`huaweicloudsdkccm.v1.CreateCertificateRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.CreateCertificateResponse`
        """
        http_info = self._create_certificate_http_info(request)
        return self._call_api(**http_info)

    def create_certificate_invoker(self, request):
        http_info = self._create_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_certificate_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-certificates",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCertificateResponse"
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

    def create_certificate_authority_obs_agency(self, request):
        """创建委托

        用户给PCA创建OBS委托授权，用于访问OBS桶，更新吊销列表。
        &gt; 用户所使用账号token需要具备安全管理员（secu_admin）权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCertificateAuthorityObsAgency
        :type request: :class:`huaweicloudsdkccm.v1.CreateCertificateAuthorityObsAgencyRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.CreateCertificateAuthorityObsAgencyResponse`
        """
        http_info = self._create_certificate_authority_obs_agency_http_info(request)
        return self._call_api(**http_info)

    def create_certificate_authority_obs_agency_invoker(self, request):
        http_info = self._create_certificate_authority_obs_agency_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_certificate_authority_obs_agency_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-certificate-authorities/obs/agencies",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCertificateAuthorityObsAgencyResponse"
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

    def create_certificate_authority_order(self, request):
        """购买CA

        购买CA。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCertificateAuthorityOrder
        :type request: :class:`huaweicloudsdkccm.v1.CreateCertificateAuthorityOrderRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.CreateCertificateAuthorityOrderResponse`
        """
        http_info = self._create_certificate_authority_order_http_info(request)
        return self._call_api(**http_info)

    def create_certificate_authority_order_invoker(self, request):
        http_info = self._create_certificate_authority_order_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_certificate_authority_order_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-certificate-authorities/order",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCertificateAuthorityOrderResponse"
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

    def create_certificate_by_csr(self, request):
        """通过CSR签发证书

        通过CSR签发证书。功能约束如下：
        - 1、当前默认参数如下：
          - CA 默认参数：
              - **keyUsage**: digitalSignature, keyCertSign, cRLSign，优先采用CSR中的参数；
              - **SignatureHashAlgorithm**: SHA384；
              - **PathLength**：0 （可自定义）。
          - 私有证书：
              - **keyUsage**: digitalSignature keyAgreement，优先采用CSR中的参数；
              - **SignatureHashAlgorithm**: SHA384；
        - 2、当传入的type为**INTERMEDIATE_CA**时，创建出的从属CA证书，有以下限制：
          - 不占用CA配额。在查询CA列表时，不会返回该证书；
          - 只支持通过以下两个接口获取其信息：
              - GET /v1/private-certificate-authorities/{ca_id} 获取证书详情
              - POST /v1/private-certificate-authorities/{ca_id}/export 导出证书
          - 本接口返回的**certificate_id**即代表从属CA的**ca_id**；
          - 无法用于签发证书，密钥在用户侧。
        - 3、当type为**ENTITY_CERT**时，创建出的私有证书，有以下特点：
          - 占用私有证书配额。在查询私有证书列表时，会返回该证书；
          - 除了导出时不包含密钥信息（密钥在用户端），其余用法与其它私有证书一致。
        &gt; 注：需要使用“\\r\\n”或“\\n”代替换行符，将CSR转换成一串字符，可参考示例请求。注：目前，证书的组织信息、公钥算法以及公钥内容等均来自CSR文件，暂不支持API传入。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCertificateByCsr
        :type request: :class:`huaweicloudsdkccm.v1.CreateCertificateByCsrRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.CreateCertificateByCsrResponse`
        """
        http_info = self._create_certificate_by_csr_http_info(request)
        return self._call_api(**http_info)

    def create_certificate_by_csr_invoker(self, request):
        http_info = self._create_certificate_by_csr_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_certificate_by_csr_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-certificates/csr",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCertificateByCsrResponse"
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

    def delete_certificate(self, request):
        """删除证书

        删除证书。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCertificate
        :type request: :class:`huaweicloudsdkccm.v1.DeleteCertificateRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.DeleteCertificateResponse`
        """
        http_info = self._delete_certificate_http_info(request)
        return self._call_api(**http_info)

    def delete_certificate_invoker(self, request):
        http_info = self._delete_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_certificate_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/private-certificates/{certificate_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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

    def disable_certificate_authority_crl(self, request):
        """禁用CRL

        禁用当前CA的CRL。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisableCertificateAuthorityCrl
        :type request: :class:`huaweicloudsdkccm.v1.DisableCertificateAuthorityCrlRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.DisableCertificateAuthorityCrlResponse`
        """
        http_info = self._disable_certificate_authority_crl_http_info(request)
        return self._call_api(**http_info)

    def disable_certificate_authority_crl_invoker(self, request):
        http_info = self._disable_certificate_authority_crl_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disable_certificate_authority_crl_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-certificate-authorities/{ca_id}/crl/disable",
            "request_type": request.__class__.__name__,
            "response_type": "DisableCertificateAuthorityCrlResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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

    def enable_certificate_authority_crl(self, request):
        """启用CRL

        启用当前CA的CRL。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableCertificateAuthorityCrl
        :type request: :class:`huaweicloudsdkccm.v1.EnableCertificateAuthorityCrlRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.EnableCertificateAuthorityCrlResponse`
        """
        http_info = self._enable_certificate_authority_crl_http_info(request)
        return self._call_api(**http_info)

    def enable_certificate_authority_crl_invoker(self, request):
        http_info = self._enable_certificate_authority_crl_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_certificate_authority_crl_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-certificate-authorities/{ca_id}/crl/enable",
            "request_type": request.__class__.__name__,
            "response_type": "EnableCertificateAuthorityCrlResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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

    def export_certificate(self, request):
        """导出证书

        导出证书。
          - 国际算法
            - 选择是否压缩时，分以下两种情况：
              - is_compressed为true时，返回文件压缩包，命名为：证书名称_type字段小写字母.zip，如”test_apache.zip“。
                - 系统生成密钥签发证书
                  - type &#x3D; \&quot;**APACHE**\&quot;时，压缩包中包含三个文件：**server.key**（密钥文件，内容为PEM格式，若导出证书时设置密码，则为加密后的私钥）、**chain.crt**（证书链，内容为PEM格式）、**server.crt**（证书，内容为PEM格式）；
                  - type &#x3D; \&quot;**IIS**\&quot;时，压缩包中包含两个文件：**keystorePass.txt**（keystore口令，若导出证书时设置密码，则无此密码文件）、**server.pfx**（PFX证书，证书与证书链包含在同一个文件）；
                  - type &#x3D; \&quot;**NGINX**\&quot;时，压缩包中包含两个文件：**server.key**（密钥文件，内容为PEM格式，若导出证书时设置密码，则为加密后的私钥）、**server.crt**（内容为PEM格式，证书与证书链包含在同一个文件）；
                  - type &#x3D; \&quot;**TOMCAT**\&quot;时，压缩包中包含两个文件：**keystorePass.txt**（keystore口令，若导出证书时设置密码，则无此密码文件）、**server.jks**（JKX证书，证书与证书链包含在同一个文件）；
                  - type &#x3D; \&quot;**OTHER**\&quot;时，压缩包中包含三个文件：**server.key**（密钥文件，内容为PEM格式，若导出证书时设置密码，则为加密后的私钥）、**chain.pem**（证书链）、**server.pem**（证书）。
                - 导入CSR签发证书
                  - type &#x3D; \&quot;**APACHE**\&quot;或\&quot;**IIS**\&quot;或\&quot;**TOMCAT**\&quot;时，压缩包中包含两个文件：**chain.crt**（证书链，内容为PEM格式）、**server.crt**（证书，内容为PEM格式）；
                  - type &#x3D; \&quot;**NGINX**\&quot;时，压缩包中包含一个文件：**server.crt**（证书，内容为PEM格式）；
                  - type &#x3D; \&quot;**OTHER**\&quot;时，压缩包中包含两个文件：**chain.pem**（证书链，内容为PEM格式）、**cert.pem**（证书，内容为PEM格式）。
              - is_compressed为false时，返回json格式，返回的具体参数如下：
                - 系统生成密钥签发证书
                  - type &#x3D; \&quot;**APACHE**\&quot;或\&quot;**NGINX**\&quot;或\&quot;**OTHER**\&quot;时，返回参数如下：
                    - **certificate**（证书内容，PEM格式）；
                    - **certificate_chain**（证书链，PEM格式）；
                    - **private_key**（证书私钥，PEM格式，若导出证书时设置密码，则为加密后的私钥）；
                  - type &#x3D; \&quot;**IIS**\&quot;或\&quot;**TOMCAT**\&quot;时，暂时未定义。
                - 导入CSR签发证书
                  - type &#x3D; \&quot;**APACHE**\&quot;或\&quot;**NGINX**\&quot;或\&quot;**IIS**\&quot;或\&quot;**TOMCAT**\&quot;或\&quot;**OTHER**\&quot;时，返回参数如下：
                    - **certificate**（证书内容，PEM格式）；
                    - **certificate_chain**（证书链，PEM格式）；
          - 国密算法（中国站）
            - 选择是否压缩和是否国密标准时，分以下四种情况：
              - is_compressed为true、is_sm_standard为true时，返回文件压缩包，命名为：证书名称_type字段小写字母.zip，如”test_apache.zip“。
                - 系统生成密钥签发证书
                  - type &#x3D; \&quot;**APACHE**\&quot;或\&quot;**IIS**\&quot;或\&quot;**NGINX**\&quot;或\&quot;**TOMCAT**\&quot;时，暂时未定义；
                  - type &#x3D; \&quot;**OTHER**\&quot;时，压缩包中包含六个文件：**chain.pem**（证书链，内容为PEM格式）、**signCert.key**（签名证书密钥文件，内容为PEM格式，若导出证书时设置密码，则为加密后的私钥）、**signCert.pem**（签名证书，内容为PEM格式）、**encSm2EnvelopedKey.key**（加密证书的国密GMT0009标准规范数字信封文件，内容为BASE64编码）、**signedAndEnvelopedData.key**（加密证书的国密GMT0010标准规范数字信封文件，内容为BASE64编码）、**encCert.pem**（加密证书，内容为PEM格式）。
                - 导入CSR签发证书
                  - type &#x3D; \&quot;**APACHE**\&quot;或\&quot;**IIS**\&quot;或\&quot;**NGINX**\&quot;或\&quot;**TOMCAT**\&quot;时，暂时未定义；
                  - type &#x3D; \&quot;**OTHER**\&quot;时，压缩包中包含五个文件：**chain.pem**（证书链，内容为PEM格式）、**signCert.pem**（签名证书，内容为PEM格式）、**encSm2EnvelopedKey.key**（加密证书的国密GMT0009标准规范数字信封文件，内容为BASE64编码）、**signedAndEnvelopedData.key**（加密证书的国密GMT0010标准规范数字信封文件，内容为BASE64编码）、**encCert.pem**（加密证书，内容为PEM格式）。
              - is_compressed为true、is_sm_standard为false时，返回文件压缩包，命名为：证书名称_type字段小写字母.zip，如”test_apache.zip“。
                - 系统生成密钥签发证书
                  - type &#x3D; \&quot;**APACHE**\&quot;或\&quot;**IIS**\&quot;或\&quot;**NGINX**\&quot;或\&quot;**TOMCAT**\&quot;时，暂时未定义；
                  - type &#x3D; \&quot;**OTHER**\&quot;时，压缩包中包含五个文件：**chain.pem**（证书链，内容为PEM格式）、**signCert.key**（签名证书密钥文件，内容为PEM格式，若导出证书时设置密码，则为加密后的私钥）、**signCert.pem**（签名证书，内容为PEM格式）、**encCert.key**（加密证书密钥文件，内容为PEM格式，若导出证书时设置密码，则为加密后的私钥）、**encCert.pem**（加密证书，内容为PEM格式）。
                - 导入CSR签发证书
                  - type &#x3D; \&quot;**APACHE**\&quot;或\&quot;**IIS**\&quot;或\&quot;**NGINX**\&quot;或\&quot;**TOMCAT**\&quot;时，暂时未定义；
                  - type &#x3D; \&quot;**OTHER**\&quot;时，压缩包中包含四个文件：**chain.pem**（证书链，内容为PEM格式）、**signCert.pem**（签名证书，内容为PEM格式）、**encCert.key**（加密证书密钥文件，内容为PEM格式）、**encCert.pem**（加密证书，内容为PEM格式）。
              - is_compressed为false、is_sm_standard为true时，返回json格式，返回的具体参数如下：
                - 系统生成密钥签发证书
                  - type &#x3D; \&quot;**APACHE**\&quot;或\&quot;**IIS**\&quot;或\&quot;**NGINX**\&quot;或\&quot;**TOMCAT**\&quot;时，暂时未定义；
                  - type &#x3D; \&quot;**OTHER**\&quot;时，返回参数如下：
                    - **certificate_chain**（证书链，PEM格式）；
                    - **certificate**（签名证书内容，PEM格式）；
                    - **private_key**（签名证书私钥，PEM格式，若导出证书时设置密码，则为加密后的私钥）；
                    - **enc_certificate**（加密证书内容，PEM格式）；
                    - **enc_sm2_enveloped_key**（加密证书的国密GMT0009标准规范数字信封文件，BASE64编码）；
                    - **signed_and_enveloped_data**（加密证书的国密GMT0010标准规范数字信封文件，BASE64编码）。
                - 导入CSR签发证书
                  - type &#x3D; \&quot;**APACHE**\&quot;或\&quot;**IIS**\&quot;或\&quot;**NGINX**\&quot;或\&quot;**TOMCAT**\&quot;时，暂时未定义；
                  - type &#x3D; \&quot;**OTHER**\&quot;时，返回参数如下：
                    - **certificate_chain**（证书链，PEM格式）；
                    - **certificate**（签名证书内容，PEM格式）；
                    - **enc_certificate**（加密证书内容，PEM格式）；
                    - **enc_sm2_enveloped_key**（加密证书的国密GMT0009标准规范数字信封文件，BASE64编码）；
                    - **signed_and_enveloped_data**（加密证书的国密GMT0010标准规范数字信封文件，BASE64编码）。
              - is_compressed为false、is_sm_standard为false时，返回json格式，返回的具体参数如下：
                - 系统生成密钥签发证书
                  - type &#x3D; \&quot;**APACHE**\&quot;或\&quot;**IIS**\&quot;或\&quot;**NGINX**\&quot;或\&quot;**TOMCAT**\&quot;时，暂时未定义；
                  - type &#x3D; \&quot;**OTHER**\&quot;时，返回参数如下：
                    - **certificate_chain**（证书链，PEM格式）；
                    - **certificate**（签名证书内容，PEM格式）；
                    - **private_key**（签名证书私钥，PEM格式，若导出证书时设置密码，则为加密后的私钥）；
                    - **enc_certificate**（加密证书内容，PEM格式）；
                    - **enc_private_key**（加密证书私钥，PEM格式，若导出证书时设置密码，则为加密后的私钥）。
                - 导入CSR签发证书
                  - type &#x3D; \&quot;**APACHE**\&quot;或\&quot;**IIS**\&quot;或\&quot;**NGINX**\&quot;或\&quot;**TOMCAT**\&quot;时，暂时未定义；
                  - type &#x3D; \&quot;**OTHER**\&quot;时，返回参数如下：
                    - **certificate_chain**（证书链，PEM格式）；
                    - **certificate**（签名证书内容，PEM格式）；
                    - **enc_certificate**（加密证书内容，PEM格式）；
                    - **enc_private_key**（加密证书私钥，PEM格式）。
        &gt; 只有当证书状态为“已签发”时，可进行导出操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportCertificate
        :type request: :class:`huaweicloudsdkccm.v1.ExportCertificateRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ExportCertificateResponse`
        """
        http_info = self._export_certificate_http_info(request)
        return self._call_api(**http_info)

    def export_certificate_invoker(self, request):
        http_info = self._export_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_certificate_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-certificates/{certificate_id}/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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

    def list_ca_resource_instances(self, request):
        """根据标签查询CA列表

        根据标签查询CA列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCaResourceInstances
        :type request: :class:`huaweicloudsdkccm.v1.ListCaResourceInstancesRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ListCaResourceInstancesResponse`
        """
        http_info = self._list_ca_resource_instances_http_info(request)
        return self._call_api(**http_info)

    def list_ca_resource_instances_invoker(self, request):
        http_info = self._list_ca_resource_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ca_resource_instances_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-certificate-authorities/resource-instances/filter",
            "request_type": request.__class__.__name__,
            "response_type": "ListCaResourceInstancesResponse"
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

    def list_ca_tags(self, request):
        """根据CA查询标签列表

        根据CA证书ID查询此CA的标签列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCaTags
        :type request: :class:`huaweicloudsdkccm.v1.ListCaTagsRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ListCaTagsResponse`
        """
        http_info = self._list_ca_tags_http_info(request)
        return self._call_api(**http_info)

    def list_ca_tags_invoker(self, request):
        http_info = self._list_ca_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ca_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/private-certificate-authorities/{ca_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListCaTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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

    def list_cert_resource_instances(self, request):
        """根据标签查询证书列表

        根据标签查询证书列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCertResourceInstances
        :type request: :class:`huaweicloudsdkccm.v1.ListCertResourceInstancesRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ListCertResourceInstancesResponse`
        """
        http_info = self._list_cert_resource_instances_http_info(request)
        return self._call_api(**http_info)

    def list_cert_resource_instances_invoker(self, request):
        http_info = self._list_cert_resource_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_cert_resource_instances_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-certificates/resource-instances/filter",
            "request_type": request.__class__.__name__,
            "response_type": "ListCertResourceInstancesResponse"
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

    def list_cert_tags(self, request):
        """根据证书查询标签列表

        根据证书ID查询此证书的标签列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCertTags
        :type request: :class:`huaweicloudsdkccm.v1.ListCertTagsRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ListCertTagsResponse`
        """
        http_info = self._list_cert_tags_http_info(request)
        return self._call_api(**http_info)

    def list_cert_tags_invoker(self, request):
        http_info = self._list_cert_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_cert_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/private-certificates/{certificate_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListCertTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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

    def list_certificate(self, request):
        """查询私有证书列表

        查询私有证书列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCertificate
        :type request: :class:`huaweicloudsdkccm.v1.ListCertificateRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ListCertificateResponse`
        """
        http_info = self._list_certificate_http_info(request)
        return self._call_api(**http_info)

    def list_certificate_invoker(self, request):
        http_info = self._list_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_certificate_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/private-certificates",
            "request_type": request.__class__.__name__,
            "response_type": "ListCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

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

    def list_certificate_authority_obs_bucket(self, request):
        """查询OBS桶列表

        查询OBS桶列表。
        &gt; 只有用户创建了委托授权，方可使用此接口。创建委托授权参见本文档：**证书吊销处理&gt;创建委托**。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCertificateAuthorityObsBucket
        :type request: :class:`huaweicloudsdkccm.v1.ListCertificateAuthorityObsBucketRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ListCertificateAuthorityObsBucketResponse`
        """
        http_info = self._list_certificate_authority_obs_bucket_http_info(request)
        return self._call_api(**http_info)

    def list_certificate_authority_obs_bucket_invoker(self, request):
        http_info = self._list_certificate_authority_obs_bucket_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_certificate_authority_obs_bucket_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/private-certificate-authorities/obs/buckets",
            "request_type": request.__class__.__name__,
            "response_type": "ListCertificateAuthorityObsBucketResponse"
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

    def list_domain_ca_tags(self, request):
        """查询所有CA标签列表

        查询所有CA标签列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDomainCaTags
        :type request: :class:`huaweicloudsdkccm.v1.ListDomainCaTagsRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ListDomainCaTagsResponse`
        """
        http_info = self._list_domain_ca_tags_http_info(request)
        return self._call_api(**http_info)

    def list_domain_ca_tags_invoker(self, request):
        http_info = self._list_domain_ca_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_domain_ca_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/private-certificate-authorities/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListDomainCaTagsResponse"
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

    def list_domain_cert_tags(self, request):
        """查询所有证书标签列表

        查询所有证书标签列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDomainCertTags
        :type request: :class:`huaweicloudsdkccm.v1.ListDomainCertTagsRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ListDomainCertTagsResponse`
        """
        http_info = self._list_domain_cert_tags_http_info(request)
        return self._call_api(**http_info)

    def list_domain_cert_tags_invoker(self, request):
        http_info = self._list_domain_cert_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_domain_cert_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/private-certificates/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListDomainCertTagsResponse"
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

    def parse_certificate_signing_request(self, request):
        """解析CSR

        解析CSR。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ParseCertificateSigningRequest
        :type request: :class:`huaweicloudsdkccm.v1.ParseCertificateSigningRequestRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ParseCertificateSigningRequestResponse`
        """
        http_info = self._parse_certificate_signing_request_http_info(request)
        return self._call_api(**http_info)

    def parse_certificate_signing_request_invoker(self, request):
        http_info = self._parse_certificate_signing_request_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _parse_certificate_signing_request_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-certificates/csr/parse",
            "request_type": request.__class__.__name__,
            "response_type": "ParseCertificateSigningRequestResponse"
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

    def revoke_certificate(self, request):
        """吊销证书

        吊销证书。
        &gt; 注：当不想填写吊销理由时，请求body体请置为\&quot;**{}**\&quot;，否则将会报错。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RevokeCertificate
        :type request: :class:`huaweicloudsdkccm.v1.RevokeCertificateRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.RevokeCertificateResponse`
        """
        http_info = self._revoke_certificate_http_info(request)
        return self._call_api(**http_info)

    def revoke_certificate_invoker(self, request):
        http_info = self._revoke_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _revoke_certificate_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-certificates/{certificate_id}/revoke",
            "request_type": request.__class__.__name__,
            "response_type": "RevokeCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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

    def show_certificate(self, request):
        """查询证书详情

        查询证书详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCertificate
        :type request: :class:`huaweicloudsdkccm.v1.ShowCertificateRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ShowCertificateResponse`
        """
        http_info = self._show_certificate_http_info(request)
        return self._call_api(**http_info)

    def show_certificate_invoker(self, request):
        http_info = self._show_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_certificate_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/private-certificates/{certificate_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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

    def show_certificate_authority_obs_agency(self, request):
        """查看是否具有委托权限

        查看是否具有委托权限。
        &gt; 用户所使用账号token需要具备安全管理员（secu_admin）权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCertificateAuthorityObsAgency
        :type request: :class:`huaweicloudsdkccm.v1.ShowCertificateAuthorityObsAgencyRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ShowCertificateAuthorityObsAgencyResponse`
        """
        http_info = self._show_certificate_authority_obs_agency_http_info(request)
        return self._call_api(**http_info)

    def show_certificate_authority_obs_agency_invoker(self, request):
        http_info = self._show_certificate_authority_obs_agency_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_certificate_authority_obs_agency_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/private-certificate-authorities/obs/agencies",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCertificateAuthorityObsAgencyResponse"
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

    def show_certificate_quota(self, request):
        """查询私有证书配额

        查询私有证书配额。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCertificateQuota
        :type request: :class:`huaweicloudsdkccm.v1.ShowCertificateQuotaRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ShowCertificateQuotaResponse`
        """
        http_info = self._show_certificate_quota_http_info(request)
        return self._call_api(**http_info)

    def show_certificate_quota_invoker(self, request):
        http_info = self._show_certificate_quota_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_certificate_quota_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/private-certificates/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCertificateQuotaResponse"
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

    def create_certificate_authority(self, request):
        """创建CA

        创建CA，分以下三种情况：
        - 创建根CA，根据参数介绍中，填写必选值；
        - 创建从属CA，并需要直接激活该证书，根据参数介绍中，填写必选值；
        - 创建从属CA，不需要直接激活该证书，请求body中只需要缺少此三个参数之一即可：issuer_id、signature_algorithm、validity。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCertificateAuthority
        :type request: :class:`huaweicloudsdkccm.v1.CreateCertificateAuthorityRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.CreateCertificateAuthorityResponse`
        """
        http_info = self._create_certificate_authority_http_info(request)
        return self._call_api(**http_info)

    def create_certificate_authority_invoker(self, request):
        http_info = self._create_certificate_authority_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_certificate_authority_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-certificate-authorities",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCertificateAuthorityResponse"
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

    def delete_certificate_authority(self, request):
        """删除CA

        计划删除CA。计划多少天后删除CA证书，可设置7天～30天内删除。
        &gt; 只有当证书状态为”待激活“或”已禁用“状态时，才可删除。”待激活“状态下，将会立即删除证书，不支持延迟删除。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCertificateAuthority
        :type request: :class:`huaweicloudsdkccm.v1.DeleteCertificateAuthorityRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.DeleteCertificateAuthorityResponse`
        """
        http_info = self._delete_certificate_authority_http_info(request)
        return self._call_api(**http_info)

    def delete_certificate_authority_invoker(self, request):
        http_info = self._delete_certificate_authority_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_certificate_authority_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/private-certificate-authorities/{ca_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCertificateAuthorityResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

        query_params = []
        if 'pending_days' in local_var_params:
            query_params.append(('pending_days', local_var_params['pending_days']))

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

    def disable_certificate_authority(self, request):
        """禁用CA

        禁用CA。
        &gt; 只有当证书处于\&quot;已激活\&quot;或\&quot;已过期\&quot;状态时，可进行禁用操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisableCertificateAuthority
        :type request: :class:`huaweicloudsdkccm.v1.DisableCertificateAuthorityRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.DisableCertificateAuthorityResponse`
        """
        http_info = self._disable_certificate_authority_http_info(request)
        return self._call_api(**http_info)

    def disable_certificate_authority_invoker(self, request):
        http_info = self._disable_certificate_authority_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disable_certificate_authority_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-certificate-authorities/{ca_id}/disable",
            "request_type": request.__class__.__name__,
            "response_type": "DisableCertificateAuthorityResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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

    def enable_certificate_authority(self, request):
        """启用CA

        启用CA。
        &gt; 注：只有当证书处于\&quot;已禁用\&quot;状态时，可进行启用操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableCertificateAuthority
        :type request: :class:`huaweicloudsdkccm.v1.EnableCertificateAuthorityRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.EnableCertificateAuthorityResponse`
        """
        http_info = self._enable_certificate_authority_http_info(request)
        return self._call_api(**http_info)

    def enable_certificate_authority_invoker(self, request):
        http_info = self._enable_certificate_authority_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_certificate_authority_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-certificate-authorities/{ca_id}/enable",
            "request_type": request.__class__.__name__,
            "response_type": "EnableCertificateAuthorityResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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

    def export_certificate_authority_certificate(self, request):
        """导出CA证书

        导出CA证书。
        &gt; 注：只有当证书处于\&quot;已激活\&quot;或\&quot;已过期\&quot;时，可进行导出操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportCertificateAuthorityCertificate
        :type request: :class:`huaweicloudsdkccm.v1.ExportCertificateAuthorityCertificateRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ExportCertificateAuthorityCertificateResponse`
        """
        http_info = self._export_certificate_authority_certificate_http_info(request)
        return self._call_api(**http_info)

    def export_certificate_authority_certificate_invoker(self, request):
        http_info = self._export_certificate_authority_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_certificate_authority_certificate_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-certificate-authorities/{ca_id}/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportCertificateAuthorityCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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

    def export_certificate_authority_csr(self, request):
        """导出CA的证书签名请求（CSR）

        导出CA的证书签名请求。
        &gt; 只有当CA处于\&quot;待激活\&quot;状态时，可导出证书签名请求。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportCertificateAuthorityCsr
        :type request: :class:`huaweicloudsdkccm.v1.ExportCertificateAuthorityCsrRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ExportCertificateAuthorityCsrResponse`
        """
        http_info = self._export_certificate_authority_csr_http_info(request)
        return self._call_api(**http_info)

    def export_certificate_authority_csr_invoker(self, request):
        http_info = self._export_certificate_authority_csr_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_certificate_authority_csr_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/private-certificate-authorities/{ca_id}/csr",
            "request_type": request.__class__.__name__,
            "response_type": "ExportCertificateAuthorityCsrResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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

    def import_certificate_authority_certificate(self, request):
        """导入CA证书

        导入CA证书，使用本接口需要满足以下条件：
          - （1）证书为“待激活”状态的从属CA；
          - （2）导入的证书体必须满足以下条件：
              - a、该证书被签发时的证书签名请求必须是从PCA系统中导出；
              - b、其证书链虽然允许不上传，但后期若想要导出完整的证书链，应导入完整的证书链；
              - c、证书体与证书链必须为PEM编码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportCertificateAuthorityCertificate
        :type request: :class:`huaweicloudsdkccm.v1.ImportCertificateAuthorityCertificateRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ImportCertificateAuthorityCertificateResponse`
        """
        http_info = self._import_certificate_authority_certificate_http_info(request)
        return self._call_api(**http_info)

    def import_certificate_authority_certificate_invoker(self, request):
        http_info = self._import_certificate_authority_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_certificate_authority_certificate_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-certificate-authorities/{ca_id}/import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportCertificateAuthorityCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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

    def issue_certificate_authority_certificate(self, request):
        """激活CA

        激活CA。
        &gt; 只有当证书处于\&quot;待激活\&quot;状态时，可进行激活操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for IssueCertificateAuthorityCertificate
        :type request: :class:`huaweicloudsdkccm.v1.IssueCertificateAuthorityCertificateRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.IssueCertificateAuthorityCertificateResponse`
        """
        http_info = self._issue_certificate_authority_certificate_http_info(request)
        return self._call_api(**http_info)

    def issue_certificate_authority_certificate_invoker(self, request):
        http_info = self._issue_certificate_authority_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _issue_certificate_authority_certificate_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-certificate-authorities/{ca_id}/activate",
            "request_type": request.__class__.__name__,
            "response_type": "IssueCertificateAuthorityCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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

    def list_certificate_authority(self, request):
        """查询CA列表

        查询CA列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCertificateAuthority
        :type request: :class:`huaweicloudsdkccm.v1.ListCertificateAuthorityRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ListCertificateAuthorityResponse`
        """
        http_info = self._list_certificate_authority_http_info(request)
        return self._call_api(**http_info)

    def list_certificate_authority_invoker(self, request):
        http_info = self._list_certificate_authority_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_certificate_authority_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/private-certificate-authorities",
            "request_type": request.__class__.__name__,
            "response_type": "ListCertificateAuthorityResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

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

    def restore_certificate_authority(self, request):
        """恢复CA

        恢复CA，将处于“计划删除”状态的CA证书，重新恢复为“已禁用”状态。
        &gt; 注：只有处于“计划删除”状态的CA证书，才可进行恢复操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestoreCertificateAuthority
        :type request: :class:`huaweicloudsdkccm.v1.RestoreCertificateAuthorityRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.RestoreCertificateAuthorityResponse`
        """
        http_info = self._restore_certificate_authority_http_info(request)
        return self._call_api(**http_info)

    def restore_certificate_authority_invoker(self, request):
        http_info = self._restore_certificate_authority_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restore_certificate_authority_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-certificate-authorities/{ca_id}/restore",
            "request_type": request.__class__.__name__,
            "response_type": "RestoreCertificateAuthorityResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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

    def revoke_certificate_authority(self, request):
        """吊销CA

        吊销子CA。
        &gt; 注：当不想填写吊销理由时，请求body体请置为\&quot;**{}**\&quot;，否则将会报错。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RevokeCertificateAuthority
        :type request: :class:`huaweicloudsdkccm.v1.RevokeCertificateAuthorityRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.RevokeCertificateAuthorityResponse`
        """
        http_info = self._revoke_certificate_authority_http_info(request)
        return self._call_api(**http_info)

    def revoke_certificate_authority_invoker(self, request):
        http_info = self._revoke_certificate_authority_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _revoke_certificate_authority_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/private-certificate-authorities/{ca_id}/revoke",
            "request_type": request.__class__.__name__,
            "response_type": "RevokeCertificateAuthorityResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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

    def show_certificate_authority(self, request):
        """查询CA详情

        查询CA详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCertificateAuthority
        :type request: :class:`huaweicloudsdkccm.v1.ShowCertificateAuthorityRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ShowCertificateAuthorityResponse`
        """
        http_info = self._show_certificate_authority_http_info(request)
        return self._call_api(**http_info)

    def show_certificate_authority_invoker(self, request):
        http_info = self._show_certificate_authority_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_certificate_authority_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/private-certificate-authorities/{ca_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCertificateAuthorityResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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

    def show_certificate_authority_quota(self, request):
        """查询CA配额

        查询CA证书配额。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCertificateAuthorityQuota
        :type request: :class:`huaweicloudsdkccm.v1.ShowCertificateAuthorityQuotaRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ShowCertificateAuthorityQuotaResponse`
        """
        http_info = self._show_certificate_authority_quota_http_info(request)
        return self._call_api(**http_info)

    def show_certificate_authority_quota_invoker(self, request):
        http_info = self._show_certificate_authority_quota_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_certificate_authority_quota_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/private-certificate-authorities/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCertificateAuthorityQuotaResponse"
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
