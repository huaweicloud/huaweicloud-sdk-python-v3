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


class CcmAsyncClient(Client):
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
        super(CcmAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkccm.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls, "GlobalCredentials")

        if clazz.__name__ != "CcmClient":
            raise TypeError("client type error, support client type is CcmClient")

        return ClientBuilder(clazz, "GlobalCredentials")

    def create_certificate_authority_async(self, request):
        """创建CA

        创建CA

        :param CreateCertificateAuthorityRequest request
        :return: CreateCertificateAuthorityResponse
        """
        return self.create_certificate_authority_with_http_info(request)

    def create_certificate_authority_with_http_info(self, request):
        """创建CA

        创建CA

        :param CreateCertificateAuthorityRequest request
        :return: CreateCertificateAuthorityResponse
        """

        all_params = ['create_certificate_authority_request_body']
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
            response_type='CreateCertificateAuthorityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_certificate_authority_async(self, request):
        """删除CA

        删除CA

        :param DeleteCertificateAuthorityRequest request
        :return: DeleteCertificateAuthorityResponse
        """
        return self.delete_certificate_authority_with_http_info(request)

    def delete_certificate_authority_with_http_info(self, request):
        """删除CA

        删除CA

        :param DeleteCertificateAuthorityRequest request
        :return: DeleteCertificateAuthorityResponse
        """

        all_params = ['ca_id', 'pending_days']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='DeleteCertificateAuthorityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def disable_certificate_authority_async(self, request):
        """禁用CA

        禁用CA

        :param DisableCertificateAuthorityRequest request
        :return: DisableCertificateAuthorityResponse
        """
        return self.disable_certificate_authority_with_http_info(request)

    def disable_certificate_authority_with_http_info(self, request):
        """禁用CA

        禁用CA

        :param DisableCertificateAuthorityRequest request
        :return: DisableCertificateAuthorityResponse
        """

        all_params = ['ca_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='DisableCertificateAuthorityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def enable_certificate_authority_async(self, request):
        """启用CA

        启用CA

        :param EnableCertificateAuthorityRequest request
        :return: EnableCertificateAuthorityResponse
        """
        return self.enable_certificate_authority_with_http_info(request)

    def enable_certificate_authority_with_http_info(self, request):
        """启用CA

        启用CA

        :param EnableCertificateAuthorityRequest request
        :return: EnableCertificateAuthorityResponse
        """

        all_params = ['ca_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='EnableCertificateAuthorityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def export_certificate_authority_certificate_async(self, request):
        """导出CA证书

        导出CA证书

        :param ExportCertificateAuthorityCertificateRequest request
        :return: ExportCertificateAuthorityCertificateResponse
        """
        return self.export_certificate_authority_certificate_with_http_info(request)

    def export_certificate_authority_certificate_with_http_info(self, request):
        """导出CA证书

        导出CA证书

        :param ExportCertificateAuthorityCertificateRequest request
        :return: ExportCertificateAuthorityCertificateResponse
        """

        all_params = ['ca_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ExportCertificateAuthorityCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def export_certificate_authority_csr_async(self, request):
        """导出CA的证书签名请求

        导出CA的证书签名请求

        :param ExportCertificateAuthorityCsrRequest request
        :return: ExportCertificateAuthorityCsrResponse
        """
        return self.export_certificate_authority_csr_with_http_info(request)

    def export_certificate_authority_csr_with_http_info(self, request):
        """导出CA的证书签名请求

        导出CA的证书签名请求

        :param ExportCertificateAuthorityCsrRequest request
        :return: ExportCertificateAuthorityCsrResponse
        """

        all_params = ['ca_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ExportCertificateAuthorityCsrResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def import_certificate_authority_certificate_async(self, request):
        """导入CA证书

        导入CA证书

        :param ImportCertificateAuthorityCertificateRequest request
        :return: ImportCertificateAuthorityCertificateResponse
        """
        return self.import_certificate_authority_certificate_with_http_info(request)

    def import_certificate_authority_certificate_with_http_info(self, request):
        """导入CA证书

        导入CA证书

        :param ImportCertificateAuthorityCertificateRequest request
        :return: ImportCertificateAuthorityCertificateResponse
        """

        all_params = ['ca_id', 'import_certificate_authority_certificate_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ImportCertificateAuthorityCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def issue_certificate_authority_certificate_async(self, request):
        """激活CA

        激活CA

        :param IssueCertificateAuthorityCertificateRequest request
        :return: IssueCertificateAuthorityCertificateResponse
        """
        return self.issue_certificate_authority_certificate_with_http_info(request)

    def issue_certificate_authority_certificate_with_http_info(self, request):
        """激活CA

        激活CA

        :param IssueCertificateAuthorityCertificateRequest request
        :return: IssueCertificateAuthorityCertificateResponse
        """

        all_params = ['ca_id', 'issue_certificate_authority_certificate_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1/private-certificate-authorities/{ca_id}/issue',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='IssueCertificateAuthorityCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_certificate_authority_async(self, request):
        """查询CA列表

        查询CA列表

        :param ListCertificateAuthorityRequest request
        :return: ListCertificateAuthorityResponse
        """
        return self.list_certificate_authority_with_http_info(request)

    def list_certificate_authority_with_http_info(self, request):
        """查询CA列表

        查询CA列表

        :param ListCertificateAuthorityRequest request
        :return: ListCertificateAuthorityResponse
        """

        all_params = ['limit', 'name', 'offset', 'status', 'type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ListCertificateAuthorityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def restore_certificate_authority_async(self, request):
        """恢复CA

        恢复CA

        :param RestoreCertificateAuthorityRequest request
        :return: RestoreCertificateAuthorityResponse
        """
        return self.restore_certificate_authority_with_http_info(request)

    def restore_certificate_authority_with_http_info(self, request):
        """恢复CA

        恢复CA

        :param RestoreCertificateAuthorityRequest request
        :return: RestoreCertificateAuthorityResponse
        """

        all_params = ['ca_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='RestoreCertificateAuthorityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_certificate_authority_async(self, request):
        """查询CA详情

        查询CA详情

        :param ShowCertificateAuthorityRequest request
        :return: ShowCertificateAuthorityResponse
        """
        return self.show_certificate_authority_with_http_info(request)

    def show_certificate_authority_with_http_info(self, request):
        """查询CA详情

        查询CA详情

        :param ShowCertificateAuthorityRequest request
        :return: ShowCertificateAuthorityResponse
        """

        all_params = ['ca_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ShowCertificateAuthorityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_certificate_authority_quota_async(self, request):
        """获取CA配额

        获取CA配额

        :param ShowCertificateAuthorityQuotaRequest request
        :return: ShowCertificateAuthorityQuotaResponse
        """
        return self.show_certificate_authority_quota_with_http_info(request)

    def show_certificate_authority_quota_with_http_info(self, request):
        """获取CA配额

        获取CA配额

        :param ShowCertificateAuthorityQuotaRequest request
        :return: ShowCertificateAuthorityQuotaResponse
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
            resource_path='/v1/private-certificate-authorities/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCertificateAuthorityQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_certificate_async(self, request):
        """申请证书

        申请证书

        :param CreateCertificateRequest request
        :return: CreateCertificateResponse
        """
        return self.create_certificate_with_http_info(request)

    def create_certificate_with_http_info(self, request):
        """申请证书

        申请证书

        :param CreateCertificateRequest request
        :return: CreateCertificateResponse
        """

        all_params = ['create_certificate_request_body']
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
            response_type='CreateCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_certificate_by_csr_async(self, request):
        """签发CSR

        签发CSR

        :param CreateCertificateByCsrRequest request
        :return: CreateCertificateByCsrResponse
        """
        return self.create_certificate_by_csr_with_http_info(request)

    def create_certificate_by_csr_with_http_info(self, request):
        """签发CSR

        签发CSR

        :param CreateCertificateByCsrRequest request
        :return: CreateCertificateByCsrResponse
        """

        all_params = ['create_certificate_by_csr_request_body']
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
            response_type='CreateCertificateByCsrResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_certificate_async(self, request):
        """删除证书

        删除证书

        :param DeleteCertificateRequest request
        :return: DeleteCertificateResponse
        """
        return self.delete_certificate_with_http_info(request)

    def delete_certificate_with_http_info(self, request):
        """删除证书

        删除证书

        :param DeleteCertificateRequest request
        :return: DeleteCertificateResponse
        """

        all_params = ['certificate_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='DeleteCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def export_certificate_async(self, request):
        """导出证书

        导出证书

        :param ExportCertificateRequest request
        :return: ExportCertificateResponse
        """
        return self.export_certificate_with_http_info(request)

    def export_certificate_with_http_info(self, request):
        """导出证书

        导出证书

        :param ExportCertificateRequest request
        :return: ExportCertificateResponse
        """

        all_params = ['certificate_id', 'export_certificate_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ExportCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_certificate_async(self, request):
        """查询证书列表

        查询证书列表

        :param ListCertificateRequest request
        :return: ListCertificateResponse
        """
        return self.list_certificate_with_http_info(request)

    def list_certificate_with_http_info(self, request):
        """查询证书列表

        查询证书列表

        :param ListCertificateRequest request
        :return: ListCertificateResponse
        """

        all_params = ['limit', 'name', 'offset', 'status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ListCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def parse_certificate_signing_request_async(self, request):
        """解析证书

        解析证书

        :param ParseCertificateSigningRequestRequest request
        :return: ParseCertificateSigningRequestResponse
        """
        return self.parse_certificate_signing_request_with_http_info(request)

    def parse_certificate_signing_request_with_http_info(self, request):
        """解析证书

        解析证书

        :param ParseCertificateSigningRequestRequest request
        :return: ParseCertificateSigningRequestResponse
        """

        all_params = ['parse_certificate_signing_request_request_body']
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
            response_type='ParseCertificateSigningRequestResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def revoke_certificate_async(self, request):
        """吊销证书

        吊销证书

        :param RevokeCertificateRequest request
        :return: RevokeCertificateResponse
        """
        return self.revoke_certificate_with_http_info(request)

    def revoke_certificate_with_http_info(self, request):
        """吊销证书

        吊销证书

        :param RevokeCertificateRequest request
        :return: RevokeCertificateResponse
        """

        all_params = ['certificate_id', 'revoke_certificate_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='RevokeCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_certificate_async(self, request):
        """查询证书详情

        查询证书详情

        :param ShowCertificateRequest request
        :return: ShowCertificateResponse
        """
        return self.show_certificate_with_http_info(request)

    def show_certificate_with_http_info(self, request):
        """查询证书详情

        查询证书详情

        :param ShowCertificateRequest request
        :return: ShowCertificateResponse
        """

        all_params = ['certificate_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ShowCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_certificate_quota_async(self, request):
        """查询证书配额

        查询证书配额

        :param ShowCertificateQuotaRequest request
        :return: ShowCertificateQuotaResponse
        """
        return self.show_certificate_quota_with_http_info(request)

    def show_certificate_quota_with_http_info(self, request):
        """查询证书配额

        查询证书配额

        :param ShowCertificateQuotaRequest request
        :return: ShowCertificateQuotaResponse
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
            resource_path='/v1/private-certificates/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCertificateQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_certificate_authority_obs_agency_async(self, request):
        """创建委托

        创建委托

        :param CreateCertificateAuthorityObsAgencyRequest request
        :return: CreateCertificateAuthorityObsAgencyResponse
        """
        return self.create_certificate_authority_obs_agency_with_http_info(request)

    def create_certificate_authority_obs_agency_with_http_info(self, request):
        """创建委托

        创建委托

        :param CreateCertificateAuthorityObsAgencyRequest request
        :return: CreateCertificateAuthorityObsAgencyResponse
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
            resource_path='/v1/private-certificate-authorities/obs/agencies',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateCertificateAuthorityObsAgencyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_certificate_authority_obs_bucket_async(self, request):
        """查询OBS桶列表

        查询OBS桶列表

        :param ListCertificateAuthorityObsBucketRequest request
        :return: ListCertificateAuthorityObsBucketResponse
        """
        return self.list_certificate_authority_obs_bucket_with_http_info(request)

    def list_certificate_authority_obs_bucket_with_http_info(self, request):
        """查询OBS桶列表

        查询OBS桶列表

        :param ListCertificateAuthorityObsBucketRequest request
        :return: ListCertificateAuthorityObsBucketResponse
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
            resource_path='/v1/private-certificate-authorities/obs/buckets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCertificateAuthorityObsBucketResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_certificate_authority_obs_agency_async(self, request):
        """查看是否具有委托权限

        查看是否具有委托权限

        :param ShowCertificateAuthorityObsAgencyRequest request
        :return: ShowCertificateAuthorityObsAgencyResponse
        """
        return self.show_certificate_authority_obs_agency_with_http_info(request)

    def show_certificate_authority_obs_agency_with_http_info(self, request):
        """查看是否具有委托权限

        查看是否具有委托权限

        :param ShowCertificateAuthorityObsAgencyRequest request
        :return: ShowCertificateAuthorityObsAgencyResponse
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
            resource_path='/v1/private-certificate-authorities/obs/agencies',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCertificateAuthorityObsAgencyResponse',
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
