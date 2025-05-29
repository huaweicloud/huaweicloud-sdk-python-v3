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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkscm'")


class ScmAsyncClient(Client):
    def __init__(self):
        super(ScmAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkscm.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials")
        else:
            if clazz.__name__ != "ScmAsyncClient":
                raise TypeError("client type error, support client type is ScmAsyncClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials")

        

        return client_builder

    def apply_certificate_async(self, request):
        r"""申请证书

        申请证书。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ApplyCertificate
        :type request: :class:`huaweicloudsdkscm.v3.ApplyCertificateRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.ApplyCertificateResponse`
        """
        http_info = self._apply_certificate_http_info(request)
        return self._call_api(**http_info)

    def apply_certificate_async_invoker(self, request):
        http_info = self._apply_certificate_http_info(request)
        return AsyncInvoker(self, http_info)

    def _apply_certificate_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/scm/certificates/{certificate_id}/apply",
            "request_type": request.__class__.__name__,
            "response_type": "ApplyCertificateResponse"
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

    def batch_create_or_delete_tags_async(self, request):
        r"""批量创建或删除标签

        批量创建或删除标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateOrDeleteTags
        :type request: :class:`huaweicloudsdkscm.v3.BatchCreateOrDeleteTagsRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.BatchCreateOrDeleteTagsResponse`
        """
        http_info = self._batch_create_or_delete_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_or_delete_tags_async_invoker(self, request):
        http_info = self._batch_create_or_delete_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_or_delete_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/scm/{resource_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateOrDeleteTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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

    def batch_push_certificate_async(self, request):
        r"""批量推送证书

        批量推送SSL证书到弹性负载均衡（Elastic Load Balance，简称ELB）、Web应用防火墙（Web Application Firewall，WAF）、CDN（Content Delivery Network，内容分发网络）等其它华为云产品中。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchPushCertificate
        :type request: :class:`huaweicloudsdkscm.v3.BatchPushCertificateRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.BatchPushCertificateResponse`
        """
        http_info = self._batch_push_certificate_http_info(request)
        return self._call_api(**http_info)

    def batch_push_certificate_async_invoker(self, request):
        http_info = self._batch_push_certificate_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_push_certificate_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/scm/certificates/{certificate_id}/batch-push",
            "request_type": request.__class__.__name__,
            "response_type": "BatchPushCertificateResponse"
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

    def cancel_certificate_request_async(self, request):
        r"""撤回证书申请

        撤回证书申请。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CancelCertificateRequest
        :type request: :class:`huaweicloudsdkscm.v3.CancelCertificateRequestRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.CancelCertificateRequestResponse`
        """
        http_info = self._cancel_certificate_request_http_info(request)
        return self._call_api(**http_info)

    def cancel_certificate_request_async_invoker(self, request):
        http_info = self._cancel_certificate_request_http_info(request)
        return AsyncInvoker(self, http_info)

    def _cancel_certificate_request_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/scm/certificates/{certificate_id}/cancel-cert",
            "request_type": request.__class__.__name__,
            "response_type": "CancelCertificateRequestResponse"
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

    def create_certificate_tag_async(self, request):
        r"""创建标签

        创建标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCertificateTag
        :type request: :class:`huaweicloudsdkscm.v3.CreateCertificateTagRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.CreateCertificateTagResponse`
        """
        http_info = self._create_certificate_tag_http_info(request)
        return self._call_api(**http_info)

    def create_certificate_tag_async_invoker(self, request):
        http_info = self._create_certificate_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_certificate_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/scm/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCertificateTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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

    def delete_certificate_async(self, request):
        r"""删除证书

        删除证书实例，即将证书资源从系统中删除。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCertificate
        :type request: :class:`huaweicloudsdkscm.v3.DeleteCertificateRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.DeleteCertificateResponse`
        """
        http_info = self._delete_certificate_http_info(request)
        return self._call_api(**http_info)

    def delete_certificate_async_invoker(self, request):
        http_info = self._delete_certificate_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_certificate_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/scm/certificates/{certificate_id}",
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

    def deploy_certificate_async(self, request):
        r"""部署证书

        部署SSL证书到弹性负载均衡（Elastic Load Balance，简称ELB）、Web应用防火墙（Web Application Firewall，WAF）、CDN（Content Delivery Network，内容分发网络）等其它华为云产品中。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeployCertificate
        :type request: :class:`huaweicloudsdkscm.v3.DeployCertificateRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.DeployCertificateResponse`
        """
        http_info = self._deploy_certificate_http_info(request)
        return self._call_api(**http_info)

    def deploy_certificate_async_invoker(self, request):
        http_info = self._deploy_certificate_http_info(request)
        return AsyncInvoker(self, http_info)

    def _deploy_certificate_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/scm/certificates/{certificate_id}/deploy",
            "request_type": request.__class__.__name__,
            "response_type": "DeployCertificateResponse"
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

    def export_certificate_async(self, request):
        r"""导出证书

        导出证书。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportCertificate
        :type request: :class:`huaweicloudsdkscm.v3.ExportCertificateRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.ExportCertificateResponse`
        """
        http_info = self._export_certificate_http_info(request)
        return self._call_api(**http_info)

    def export_certificate_async_invoker(self, request):
        http_info = self._export_certificate_http_info(request)
        return AsyncInvoker(self, http_info)

    def _export_certificate_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/scm/certificates/{certificate_id}/export",
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

    def import_certificate_async(self, request):
        r"""导入证书

        导入证书到CCM服务管理。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportCertificate
        :type request: :class:`huaweicloudsdkscm.v3.ImportCertificateRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.ImportCertificateResponse`
        """
        http_info = self._import_certificate_http_info(request)
        return self._call_api(**http_info)

    def import_certificate_async_invoker(self, request):
        http_info = self._import_certificate_http_info(request)
        return AsyncInvoker(self, http_info)

    def _import_certificate_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/scm/certificates/import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportCertificateResponse"
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

    def list_all_tags_async(self, request):
        r"""查询所有标签列表

        查询所有标签列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAllTags
        :type request: :class:`huaweicloudsdkscm.v3.ListAllTagsRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.ListAllTagsResponse`
        """
        http_info = self._list_all_tags_http_info(request)
        return self._call_api(**http_info)

    def list_all_tags_async_invoker(self, request):
        http_info = self._list_all_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_all_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/scm/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllTagsResponse"
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

    def list_certificates_async(self, request):
        r"""查询证书列表

        根据证书名称或绑定域名查询证书列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCertificates
        :type request: :class:`huaweicloudsdkscm.v3.ListCertificatesRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.ListCertificatesResponse`
        """
        http_info = self._list_certificates_http_info(request)
        return self._call_api(**http_info)

    def list_certificates_async_invoker(self, request):
        http_info = self._list_certificates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_certificates_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/scm/certificates",
            "request_type": request.__class__.__name__,
            "response_type": "ListCertificatesResponse"
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
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'deploy_support' in local_var_params:
            query_params.append(('deploy_support', local_var_params['deploy_support']))
        if 'owned_by_self' in local_var_params:
            query_params.append(('owned_by_self', local_var_params['owned_by_self']))
        if 'expired_days_since' in local_var_params:
            query_params.append(('expired_days_since', local_var_params['expired_days_since']))

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

    def list_certificates_by_tag_async(self, request):
        r"""根据标签查询证书列表

        根据标签查询证书列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCertificatesByTag
        :type request: :class:`huaweicloudsdkscm.v3.ListCertificatesByTagRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.ListCertificatesByTagResponse`
        """
        http_info = self._list_certificates_by_tag_http_info(request)
        return self._call_api(**http_info)

    def list_certificates_by_tag_async_invoker(self, request):
        http_info = self._list_certificates_by_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_certificates_by_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/scm/{resource_instances}/action",
            "request_type": request.__class__.__name__,
            "response_type": "ListCertificatesByTagResponse"
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

    def list_deployed_resources_async(self, request):
        r"""查询已部署资源

        查询证书已部署的具体资源。针对已签发和上传的非国密证书。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDeployedResources
        :type request: :class:`huaweicloudsdkscm.v3.ListDeployedResourcesRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.ListDeployedResourcesResponse`
        """
        http_info = self._list_deployed_resources_http_info(request)
        return self._call_api(**http_info)

    def list_deployed_resources_async_invoker(self, request):
        http_info = self._list_deployed_resources_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_deployed_resources_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/scm/deployed-resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListDeployedResourcesResponse"
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

    def list_tags_by_certificate_async(self, request):
        r"""根据证书ID查询标签列表

        根据证书ID查询标签列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTagsByCertificate
        :type request: :class:`huaweicloudsdkscm.v3.ListTagsByCertificateRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.ListTagsByCertificateResponse`
        """
        http_info = self._list_tags_by_certificate_http_info(request)
        return self._call_api(**http_info)

    def list_tags_by_certificate_async_invoker(self, request):
        http_info = self._list_tags_by_certificate_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tags_by_certificate_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/scm/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListTagsByCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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

    def push_certificate_async(self, request):
        r"""推送证书

        推送SSL证书到弹性负载均衡（Elastic Load Balance，简称ELB）、Web应用防火墙（Web Application Firewall，WAF）、CDN（Content Delivery Network，内容分发网络）等其它华为云产品中。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PushCertificate
        :type request: :class:`huaweicloudsdkscm.v3.PushCertificateRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.PushCertificateResponse`
        """
        http_info = self._push_certificate_http_info(request)
        return self._call_api(**http_info)

    def push_certificate_async_invoker(self, request):
        http_info = self._push_certificate_http_info(request)
        return AsyncInvoker(self, http_info)

    def _push_certificate_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/scm/certificates/{certificate_id}/push",
            "request_type": request.__class__.__name__,
            "response_type": "PushCertificateResponse"
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

    def show_certificate_async(self, request):
        r"""获取证书详情

        查询某张证书的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCertificate
        :type request: :class:`huaweicloudsdkscm.v3.ShowCertificateRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.ShowCertificateResponse`
        """
        http_info = self._show_certificate_http_info(request)
        return self._call_api(**http_info)

    def show_certificate_async_invoker(self, request):
        http_info = self._show_certificate_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_certificate_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/scm/certificates/{certificate_id}",
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

    def subscribe_certificate_async(self, request):
        r"""购买SSL证书

        购买SSL证书。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SubscribeCertificate
        :type request: :class:`huaweicloudsdkscm.v3.SubscribeCertificateRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.SubscribeCertificateResponse`
        """
        http_info = self._subscribe_certificate_http_info(request)
        return self._call_api(**http_info)

    def subscribe_certificate_async_invoker(self, request):
        http_info = self._subscribe_certificate_http_info(request)
        return AsyncInvoker(self, http_info)

    def _subscribe_certificate_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/scm/certificates/buy",
            "request_type": request.__class__.__name__,
            "response_type": "SubscribeCertificateResponse"
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

    def unsubscribe_certificate_async(self, request):
        r"""退订证书

        退订证书。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UnsubscribeCertificate
        :type request: :class:`huaweicloudsdkscm.v3.UnsubscribeCertificateRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.UnsubscribeCertificateResponse`
        """
        http_info = self._unsubscribe_certificate_http_info(request)
        return self._call_api(**http_info)

    def unsubscribe_certificate_async_invoker(self, request):
        http_info = self._unsubscribe_certificate_http_info(request)
        return AsyncInvoker(self, http_info)

    def _unsubscribe_certificate_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/scm/certificates/{cert_id}/unsubscribe",
            "request_type": request.__class__.__name__,
            "response_type": "UnsubscribeCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cert_id' in local_var_params:
            path_params['cert_id'] = local_var_params['cert_id']

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

    def create_csr_async(self, request):
        r"""创建CSR

        创建CSR。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCsr
        :type request: :class:`huaweicloudsdkscm.v3.CreateCsrRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.CreateCsrResponse`
        """
        http_info = self._create_csr_http_info(request)
        return self._call_api(**http_info)

    def create_csr_async_invoker(self, request):
        http_info = self._create_csr_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_csr_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/scm/csr",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCsrResponse"
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

    def delete_csr_async(self, request):
        r"""删除CSR

        删除CSR。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCsr
        :type request: :class:`huaweicloudsdkscm.v3.DeleteCsrRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.DeleteCsrResponse`
        """
        http_info = self._delete_csr_http_info(request)
        return self._call_api(**http_info)

    def delete_csr_async_invoker(self, request):
        http_info = self._delete_csr_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_csr_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/scm/csr/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCsrResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def list_csr_async(self, request):
        r"""查询CSR列表

        查询CSR列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCsr
        :type request: :class:`huaweicloudsdkscm.v3.ListCsrRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.ListCsrResponse`
        """
        http_info = self._list_csr_http_info(request)
        return self._call_api(**http_info)

    def list_csr_async_invoker(self, request):
        http_info = self._list_csr_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_csr_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/scm/csr",
            "request_type": request.__class__.__name__,
            "response_type": "ListCsrResponse"
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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'private_key_algo' in local_var_params:
            query_params.append(('private_key_algo', local_var_params['private_key_algo']))

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

    def show_csr_async(self, request):
        r"""查询CSR

        查询CSR。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCsr
        :type request: :class:`huaweicloudsdkscm.v3.ShowCsrRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.ShowCsrResponse`
        """
        http_info = self._show_csr_http_info(request)
        return self._call_api(**http_info)

    def show_csr_async_invoker(self, request):
        http_info = self._show_csr_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_csr_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/scm/csr/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCsrResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def show_csr_private_key_async(self, request):
        r"""查询私钥

        查询私钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCsrPrivateKey
        :type request: :class:`huaweicloudsdkscm.v3.ShowCsrPrivateKeyRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.ShowCsrPrivateKeyResponse`
        """
        http_info = self._show_csr_private_key_http_info(request)
        return self._call_api(**http_info)

    def show_csr_private_key_async_invoker(self, request):
        http_info = self._show_csr_private_key_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_csr_private_key_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/scm/csr/{id}/private-key",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCsrPrivateKeyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def update_csr_async(self, request):
        r"""更新CSR

        更新CSR。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCsr
        :type request: :class:`huaweicloudsdkscm.v3.UpdateCsrRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.UpdateCsrResponse`
        """
        http_info = self._update_csr_http_info(request)
        return self._call_api(**http_info)

    def update_csr_async_invoker(self, request):
        http_info = self._update_csr_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_csr_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/scm/csr/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCsrResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def upload_csr_async(self, request):
        r"""上传CSR

        上传CSR。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UploadCsr
        :type request: :class:`huaweicloudsdkscm.v3.UploadCsrRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.UploadCsrResponse`
        """
        http_info = self._upload_csr_http_info(request)
        return self._call_api(**http_info)

    def upload_csr_async_invoker(self, request):
        http_info = self._upload_csr_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upload_csr_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/scm/csr/upload",
            "request_type": request.__class__.__name__,
            "response_type": "UploadCsrResponse"
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
