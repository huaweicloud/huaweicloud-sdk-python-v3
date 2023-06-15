# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class CcmClient(Client):
    def __init__(self):
        super(CcmClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkccm.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls, "GlobalCredentials")

        if clazz.__name__ != "CcmClient":
            raise TypeError("client type error, support client type is CcmClient")

        return ClientBuilder(clazz, "GlobalCredentials")

    def batch_create_ca_tags(self, request):
        """批量创建CA标签

        批量创建CA标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateCaTags
        :type request: :class:`huaweicloudsdkccm.v1.BatchCreateCaTagsRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.BatchCreateCaTagsResponse`
        """
        return self._batch_create_ca_tags_with_http_info(request)

    def _batch_create_ca_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/private-certificate-authorities/{ca_id}/tags/create',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreateCaTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_create_cert_tags(self, request):
        """批量创建证书标签

        批量创建证书标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateCertTags
        :type request: :class:`huaweicloudsdkccm.v1.BatchCreateCertTagsRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.BatchCreateCertTagsResponse`
        """
        return self._batch_create_cert_tags_with_http_info(request)

    def _batch_create_cert_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/private-certificates/{certificate_id}/tags/create',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreateCertTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_ca_tags(self, request):
        """批量删除CA标签

        批量删除CA标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteCaTags
        :type request: :class:`huaweicloudsdkccm.v1.BatchDeleteCaTagsRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.BatchDeleteCaTagsResponse`
        """
        return self._batch_delete_ca_tags_with_http_info(request)

    def _batch_delete_ca_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/private-certificate-authorities/{ca_id}/tags/delete',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteCaTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_cert_tags(self, request):
        """批量删除证书标签

        批量删除证书标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteCertTags
        :type request: :class:`huaweicloudsdkccm.v1.BatchDeleteCertTagsRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.BatchDeleteCertTagsResponse`
        """
        return self._batch_delete_cert_tags_with_http_info(request)

    def _batch_delete_cert_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/private-certificates/{certificate_id}/tags/delete',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteCertTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def count_ca_resource_instances(self, request):
        """根据标签查询CA数量

        根据标签查询CA数量。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountCaResourceInstances
        :type request: :class:`huaweicloudsdkccm.v1.CountCaResourceInstancesRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.CountCaResourceInstancesResponse`
        """
        return self._count_ca_resource_instances_with_http_info(request)

    def _count_ca_resource_instances_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/private-certificate-authorities/resource-instances/count',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CountCaResourceInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def count_cert_resource_instances(self, request):
        """根据标签查询证书数量

        根据标签查询证书数量。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountCertResourceInstances
        :type request: :class:`huaweicloudsdkccm.v1.CountCertResourceInstancesRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.CountCertResourceInstancesResponse`
        """
        return self._count_cert_resource_instances_with_http_info(request)

    def _count_cert_resource_instances_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/private-certificates/resource-instances/count',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CountCertResourceInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_ca_tag(self, request):
        """创建CA标签

        创建CA标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCaTag
        :type request: :class:`huaweicloudsdkccm.v1.CreateCaTagRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.CreateCaTagResponse`
        """
        return self._create_ca_tag_with_http_info(request)

    def _create_ca_tag_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/private-certificate-authorities/{ca_id}/tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCaTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_cert_tag(self, request):
        """创建证书标签

        创建证书标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCertTag
        :type request: :class:`huaweicloudsdkccm.v1.CreateCertTagRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.CreateCertTagResponse`
        """
        return self._create_cert_tag_with_http_info(request)

    def _create_cert_tag_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/private-certificates/{certificate_id}/tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCertTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_certificate(self, request):
        """申请证书

        申请证书。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCertificate
        :type request: :class:`huaweicloudsdkccm.v1.CreateCertificateRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.CreateCertificateResponse`
        """
        return self._create_certificate_with_http_info(request)

    def _create_certificate_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/private-certificates',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_certificate_authority_obs_agency(self, request):
        """创建委托

        用户给PCA创建OBS委托授权，用于访问OBS桶，更新吊销列表。
        &gt; 用户所使用账号token需要具备安全管理员（secu_admin）权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCertificateAuthorityObsAgency
        :type request: :class:`huaweicloudsdkccm.v1.CreateCertificateAuthorityObsAgencyRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.CreateCertificateAuthorityObsAgencyResponse`
        """
        return self._create_certificate_authority_obs_agency_with_http_info(request)

    def _create_certificate_authority_obs_agency_with_http_info(self, request):
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
            resource_path='/v1/private-certificate-authorities/obs/agencies',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCertificateAuthorityObsAgencyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

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
        return self._create_certificate_by_csr_with_http_info(request)

    def _create_certificate_by_csr_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/private-certificates/csr',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCertificateByCsrResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_certificate(self, request):
        """删除证书

        删除证书。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCertificate
        :type request: :class:`huaweicloudsdkccm.v1.DeleteCertificateRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.DeleteCertificateResponse`
        """
        return self._delete_certificate_with_http_info(request)

    def _delete_certificate_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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
            resource_path='/v1/private-certificates/{certificate_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disable_certificate_authority_crl(self, request):
        """禁用CRL

        禁用当前CA的CRL。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisableCertificateAuthorityCrl
        :type request: :class:`huaweicloudsdkccm.v1.DisableCertificateAuthorityCrlRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.DisableCertificateAuthorityCrlResponse`
        """
        return self._disable_certificate_authority_crl_with_http_info(request)

    def _disable_certificate_authority_crl_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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
            resource_path='/v1/private-certificate-authorities/{ca_id}/crl/disable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisableCertificateAuthorityCrlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def enable_certificate_authority_crl(self, request):
        """启用CRL

        启用当前CA的CRL。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableCertificateAuthorityCrl
        :type request: :class:`huaweicloudsdkccm.v1.EnableCertificateAuthorityCrlRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.EnableCertificateAuthorityCrlResponse`
        """
        return self._enable_certificate_authority_crl_with_http_info(request)

    def _enable_certificate_authority_crl_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/private-certificate-authorities/{ca_id}/crl/enable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='EnableCertificateAuthorityCrlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

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
                  - type &#x3D; \&quot;**OTHER**\&quot;时，压缩包中包含五个文件：**chain.pem**（证书链，内容为PEM格式）、**signCert.key**（签名证书密钥文件，内容为PEM格式，若导出证书时设置密码，则为加密后的私钥）、**signCert.pem**（签名证书，内容为PEM格式）、**encSm2EnvelopedKey.key**（加密证书的国密标准SM2数字信封文件，内容为BASE64编码）、**encCert.pem**（加密证书，内容为PEM格式）。
                - 导入CSR签发证书
                  - type &#x3D; \&quot;**APACHE**\&quot;或\&quot;**IIS**\&quot;或\&quot;**NGINX**\&quot;或\&quot;**TOMCAT**\&quot;时，暂时未定义；
                  - type &#x3D; \&quot;**OTHER**\&quot;时，压缩包中包含四个文件：**chain.pem**（证书链，内容为PEM格式）、**signCert.pem**（签名证书，内容为PEM格式）、**encSm2EnvelopedKey.key**（加密证书的国密标准SM2数字信封文件，内容为BASE64编码）、**encCert.pem**（加密证书，内容为PEM格式）。
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
                    - **enc_sm2_enveloped_key**（加密证书的国密GMT0009标准规范SM2数字信封文件，BASE64编码）。
                - 导入CSR签发证书
                  - type &#x3D; \&quot;**APACHE**\&quot;或\&quot;**IIS**\&quot;或\&quot;**NGINX**\&quot;或\&quot;**TOMCAT**\&quot;时，暂时未定义；
                  - type &#x3D; \&quot;**OTHER**\&quot;时，返回参数如下：
                    - **certificate_chain**（证书链，PEM格式）；
                    - **certificate**（签名证书内容，PEM格式）；
                    - **enc_certificate**（加密证书内容，PEM格式）；
                    - **enc_sm2_enveloped_key**（加密证书的国密GMT0009标准规范SM2数字信封文件，BASE64编码）。
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
        return self._export_certificate_with_http_info(request)

    def _export_certificate_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/private-certificates/{certificate_id}/export',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExportCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_ca_resource_instances(self, request):
        """根据标签查询CA列表

        根据标签查询CA列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCaResourceInstances
        :type request: :class:`huaweicloudsdkccm.v1.ListCaResourceInstancesRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ListCaResourceInstancesResponse`
        """
        return self._list_ca_resource_instances_with_http_info(request)

    def _list_ca_resource_instances_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/private-certificate-authorities/resource-instances/filter',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCaResourceInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_ca_tags(self, request):
        """根据CA查询标签列表

        根据CA证书ID查询此CA的标签列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCaTags
        :type request: :class:`huaweicloudsdkccm.v1.ListCaTagsRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ListCaTagsResponse`
        """
        return self._list_ca_tags_with_http_info(request)

    def _list_ca_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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
            resource_path='/v1/private-certificate-authorities/{ca_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCaTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_cert_resource_instances(self, request):
        """根据标签查询证书列表

        根据标签查询证书列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCertResourceInstances
        :type request: :class:`huaweicloudsdkccm.v1.ListCertResourceInstancesRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ListCertResourceInstancesResponse`
        """
        return self._list_cert_resource_instances_with_http_info(request)

    def _list_cert_resource_instances_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/private-certificates/resource-instances/filter',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCertResourceInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_cert_tags(self, request):
        """根据证书查询标签列表

        根据证书ID查询此证书的标签列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCertTags
        :type request: :class:`huaweicloudsdkccm.v1.ListCertTagsRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ListCertTagsResponse`
        """
        return self._list_cert_tags_with_http_info(request)

    def _list_cert_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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
            resource_path='/v1/private-certificates/{certificate_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCertTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_certificate(self, request):
        """查询私有证书列表

        查询私有证书列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCertificate
        :type request: :class:`huaweicloudsdkccm.v1.ListCertificateRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ListCertificateResponse`
        """
        return self._list_certificate_with_http_info(request)

    def _list_certificate_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/private-certificates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_certificate_authority_obs_bucket(self, request):
        """查询OBS桶列表

        查询OBS桶列表。
        &gt; 只有用户创建了委托授权，方可使用此接口。创建委托授权参见本文档：**证书吊销处理&gt;创建委托**。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCertificateAuthorityObsBucket
        :type request: :class:`huaweicloudsdkccm.v1.ListCertificateAuthorityObsBucketRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ListCertificateAuthorityObsBucketResponse`
        """
        return self._list_certificate_authority_obs_bucket_with_http_info(request)

    def _list_certificate_authority_obs_bucket_with_http_info(self, request):
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
            resource_path='/v1/private-certificate-authorities/obs/buckets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCertificateAuthorityObsBucketResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_domain_ca_tags(self, request):
        """查询所有CA标签列表

        查询所有CA标签列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDomainCaTags
        :type request: :class:`huaweicloudsdkccm.v1.ListDomainCaTagsRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ListDomainCaTagsResponse`
        """
        return self._list_domain_ca_tags_with_http_info(request)

    def _list_domain_ca_tags_with_http_info(self, request):
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
            resource_path='/v1/private-certificate-authorities/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDomainCaTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_domain_cert_tags(self, request):
        """查询所有证书标签列表

        查询所有证书标签列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDomainCertTags
        :type request: :class:`huaweicloudsdkccm.v1.ListDomainCertTagsRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ListDomainCertTagsResponse`
        """
        return self._list_domain_cert_tags_with_http_info(request)

    def _list_domain_cert_tags_with_http_info(self, request):
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
            resource_path='/v1/private-certificates/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDomainCertTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def parse_certificate_signing_request(self, request):
        """解析CSR

        解析CSR。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ParseCertificateSigningRequest
        :type request: :class:`huaweicloudsdkccm.v1.ParseCertificateSigningRequestRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ParseCertificateSigningRequestResponse`
        """
        return self._parse_certificate_signing_request_with_http_info(request)

    def _parse_certificate_signing_request_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/private-certificates/csr/parse',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ParseCertificateSigningRequestResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def revoke_certificate(self, request):
        """吊销证书

        吊销证书。
        &gt; 注：当不想填写吊销理由时，请求body体请置为\&quot;**{}**\&quot;，否则将会报错。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RevokeCertificate
        :type request: :class:`huaweicloudsdkccm.v1.RevokeCertificateRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.RevokeCertificateResponse`
        """
        return self._revoke_certificate_with_http_info(request)

    def _revoke_certificate_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/private-certificates/{certificate_id}/revoke',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RevokeCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_certificate(self, request):
        """查询证书详情

        查询证书详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCertificate
        :type request: :class:`huaweicloudsdkccm.v1.ShowCertificateRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ShowCertificateResponse`
        """
        return self._show_certificate_with_http_info(request)

    def _show_certificate_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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
            resource_path='/v1/private-certificates/{certificate_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_certificate_authority_obs_agency(self, request):
        """查看是否具有委托权限

        查看是否具有委托权限。
        &gt; 用户所使用账号token需要具备安全管理员（secu_admin）权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCertificateAuthorityObsAgency
        :type request: :class:`huaweicloudsdkccm.v1.ShowCertificateAuthorityObsAgencyRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ShowCertificateAuthorityObsAgencyResponse`
        """
        return self._show_certificate_authority_obs_agency_with_http_info(request)

    def _show_certificate_authority_obs_agency_with_http_info(self, request):
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
            resource_path='/v1/private-certificate-authorities/obs/agencies',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCertificateAuthorityObsAgencyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_certificate_quota(self, request):
        """查询私有证书配额

        查询私有证书配额。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCertificateQuota
        :type request: :class:`huaweicloudsdkccm.v1.ShowCertificateQuotaRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ShowCertificateQuotaResponse`
        """
        return self._show_certificate_quota_with_http_info(request)

    def _show_certificate_quota_with_http_info(self, request):
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
            resource_path='/v1/private-certificates/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCertificateQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

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
        return self._create_certificate_authority_with_http_info(request)

    def _create_certificate_authority_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/private-certificate-authorities',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCertificateAuthorityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_certificate_authority(self, request):
        """删除CA

        计划删除CA。计划多少天后删除CA证书，可设置7天～30天内删除。
        &gt; 只有当证书状态为”待激活“或”已禁用“状态时，才可删除。”待激活“状态下，将会立即删除证书，不支持延迟删除。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCertificateAuthority
        :type request: :class:`huaweicloudsdkccm.v1.DeleteCertificateAuthorityRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.DeleteCertificateAuthorityResponse`
        """
        return self._delete_certificate_authority_with_http_info(request)

    def _delete_certificate_authority_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/private-certificate-authorities/{ca_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteCertificateAuthorityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disable_certificate_authority(self, request):
        """禁用CA

        禁用CA。
        &gt; 只有当证书处于\&quot;已激活\&quot;或\&quot;已过期\&quot;状态时，可进行禁用操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisableCertificateAuthority
        :type request: :class:`huaweicloudsdkccm.v1.DisableCertificateAuthorityRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.DisableCertificateAuthorityResponse`
        """
        return self._disable_certificate_authority_with_http_info(request)

    def _disable_certificate_authority_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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
            resource_path='/v1/private-certificate-authorities/{ca_id}/disable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisableCertificateAuthorityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def enable_certificate_authority(self, request):
        """启用CA

        启用CA。
        &gt; 注：只有当证书处于\&quot;已禁用\&quot;状态时，可进行启用操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableCertificateAuthority
        :type request: :class:`huaweicloudsdkccm.v1.EnableCertificateAuthorityRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.EnableCertificateAuthorityResponse`
        """
        return self._enable_certificate_authority_with_http_info(request)

    def _enable_certificate_authority_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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
            resource_path='/v1/private-certificate-authorities/{ca_id}/enable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='EnableCertificateAuthorityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def export_certificate_authority_certificate(self, request):
        """导出CA证书

        导出CA证书。
        &gt; 注：只有当证书处于\&quot;已激活\&quot;或\&quot;已过期\&quot;时，可进行导出操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportCertificateAuthorityCertificate
        :type request: :class:`huaweicloudsdkccm.v1.ExportCertificateAuthorityCertificateRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ExportCertificateAuthorityCertificateResponse`
        """
        return self._export_certificate_authority_certificate_with_http_info(request)

    def _export_certificate_authority_certificate_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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
            resource_path='/v1/private-certificate-authorities/{ca_id}/export',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExportCertificateAuthorityCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def export_certificate_authority_csr(self, request):
        """导出CA的证书签名请求（CSR）

        导出CA的证书签名请求。
        &gt; 只有当CA处于\&quot;待激活\&quot;状态时，可导出证书签名请求。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportCertificateAuthorityCsr
        :type request: :class:`huaweicloudsdkccm.v1.ExportCertificateAuthorityCsrRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ExportCertificateAuthorityCsrResponse`
        """
        return self._export_certificate_authority_csr_with_http_info(request)

    def _export_certificate_authority_csr_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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
            resource_path='/v1/private-certificate-authorities/{ca_id}/csr',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExportCertificateAuthorityCsrResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

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
        return self._import_certificate_authority_certificate_with_http_info(request)

    def _import_certificate_authority_certificate_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/private-certificate-authorities/{ca_id}/import',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ImportCertificateAuthorityCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def issue_certificate_authority_certificate(self, request):
        """激活CA

        激活CA。
        &gt; 只有当证书处于\&quot;待激活\&quot;状态时，可进行激活操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for IssueCertificateAuthorityCertificate
        :type request: :class:`huaweicloudsdkccm.v1.IssueCertificateAuthorityCertificateRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.IssueCertificateAuthorityCertificateResponse`
        """
        return self._issue_certificate_authority_certificate_with_http_info(request)

    def _issue_certificate_authority_certificate_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/private-certificate-authorities/{ca_id}/activate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='IssueCertificateAuthorityCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_certificate_authority(self, request):
        """查询CA列表

        查询CA列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCertificateAuthority
        :type request: :class:`huaweicloudsdkccm.v1.ListCertificateAuthorityRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ListCertificateAuthorityResponse`
        """
        return self._list_certificate_authority_with_http_info(request)

    def _list_certificate_authority_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/private-certificate-authorities',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCertificateAuthorityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restore_certificate_authority(self, request):
        """恢复CA

        恢复CA，将处于“计划删除”状态的CA证书，重新恢复为“已禁用”状态。
        &gt; 注：只有处于“计划删除”状态的CA证书，才可进行恢复操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestoreCertificateAuthority
        :type request: :class:`huaweicloudsdkccm.v1.RestoreCertificateAuthorityRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.RestoreCertificateAuthorityResponse`
        """
        return self._restore_certificate_authority_with_http_info(request)

    def _restore_certificate_authority_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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
            resource_path='/v1/private-certificate-authorities/{ca_id}/restore',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RestoreCertificateAuthorityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def revoke_certificate_authority(self, request):
        """吊销CA

        吊销子CA。
        &gt; 注：当不想填写吊销理由时，请求body体请置为\&quot;**{}**\&quot;，否则将会报错。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RevokeCertificateAuthority
        :type request: :class:`huaweicloudsdkccm.v1.RevokeCertificateAuthorityRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.RevokeCertificateAuthorityResponse`
        """
        return self._revoke_certificate_authority_with_http_info(request)

    def _revoke_certificate_authority_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/private-certificate-authorities/{ca_id}/revoke',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RevokeCertificateAuthorityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_certificate_authority(self, request):
        """查询CA详情

        查询CA详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCertificateAuthority
        :type request: :class:`huaweicloudsdkccm.v1.ShowCertificateAuthorityRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ShowCertificateAuthorityResponse`
        """
        return self._show_certificate_authority_with_http_info(request)

    def _show_certificate_authority_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ca_id' in local_var_params:
            path_params['ca_id'] = local_var_params['ca_id']

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
            resource_path='/v1/private-certificate-authorities/{ca_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCertificateAuthorityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_certificate_authority_quota(self, request):
        """查询CA配额

        查询CA证书配额。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCertificateAuthorityQuota
        :type request: :class:`huaweicloudsdkccm.v1.ShowCertificateAuthorityQuotaRequest`
        :rtype: :class:`huaweicloudsdkccm.v1.ShowCertificateAuthorityQuotaResponse`
        """
        return self._show_certificate_authority_quota_with_http_info(request)

    def _show_certificate_authority_quota_with_http_info(self, request):
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
            resource_path='/v1/private-certificate-authorities/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCertificateAuthorityQuotaResponse',
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
