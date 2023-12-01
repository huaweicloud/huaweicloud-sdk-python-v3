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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkscm'")


class ScmClient(Client):
    def __init__(self):
        super(ScmClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkscm.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials")
        else:
            if clazz.__name__ != "ScmClient":
                raise TypeError("client type error, support client type is ScmClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials")

        

        return client_builder

    def batch_push_certificate(self, request):
        """批量推送证书

        批量推送SSL证书到弹性负载均衡（Elastic Load Balance，简称ELB）、Web应用防火墙（Web Application Firewall，WAF）、CDN（Content Delivery Network，内容分发网络）等其它云产品多个region中。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchPushCertificate
        :type request: :class:`huaweicloudsdkscm.v3.BatchPushCertificateRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.BatchPushCertificateResponse`
        """
        http_info = self._batch_push_certificate_http_info(request)
        return self._call_api(**http_info)

    def batch_push_certificate_invoker(self, request):
        http_info = self._batch_push_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_push_certificate_http_info(cls, request):
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

    def delete_certificate(self, request):
        """删除证书

        删除证书实例，即将证书资源从系统中删除。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCertificate
        :type request: :class:`huaweicloudsdkscm.v3.DeleteCertificateRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.DeleteCertificateResponse`
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

    def deploy_certificate(self, request):
        """部署证书

        部署SSL证书到弹性负载均衡（Elastic Load Balance，简称ELB）、Web应用防火墙（Web Application Firewall，WAF）、CDN（Content Delivery Network，内容分发网络）等其它云产品中。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeployCertificate
        :type request: :class:`huaweicloudsdkscm.v3.DeployCertificateRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.DeployCertificateResponse`
        """
        http_info = self._deploy_certificate_http_info(request)
        return self._call_api(**http_info)

    def deploy_certificate_invoker(self, request):
        http_info = self._deploy_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _deploy_certificate_http_info(cls, request):
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

    def export_certificate(self, request):
        """导出证书

        导出证书。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportCertificate
        :type request: :class:`huaweicloudsdkscm.v3.ExportCertificateRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.ExportCertificateResponse`
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

    def import_certificate(self, request):
        """导入证书

        导入证书到SCM服务管理。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportCertificate
        :type request: :class:`huaweicloudsdkscm.v3.ImportCertificateRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.ImportCertificateResponse`
        """
        http_info = self._import_certificate_http_info(request)
        return self._call_api(**http_info)

    def import_certificate_invoker(self, request):
        http_info = self._import_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_certificate_http_info(cls, request):
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

    def list_certificates(self, request):
        """查询证书列表

        根据证书名称或绑定域名查询证书列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCertificates
        :type request: :class:`huaweicloudsdkscm.v3.ListCertificatesRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.ListCertificatesResponse`
        """
        http_info = self._list_certificates_http_info(request)
        return self._call_api(**http_info)

    def list_certificates_invoker(self, request):
        http_info = self._list_certificates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_certificates_http_info(cls, request):
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

    def push_certificate(self, request):
        """推送证书

        推送SSL证书到弹性负载均衡（Elastic Load Balance，简称ELB）、Web应用防火墙（Web Application Firewall，WAF）、CDN（Content Delivery Network，内容分发网络）等其它云产品中。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PushCertificate
        :type request: :class:`huaweicloudsdkscm.v3.PushCertificateRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.PushCertificateResponse`
        """
        http_info = self._push_certificate_http_info(request)
        return self._call_api(**http_info)

    def push_certificate_invoker(self, request):
        http_info = self._push_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _push_certificate_http_info(cls, request):
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

    def show_certificate(self, request):
        """获取证书详情

        查询某张证书的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCertificate
        :type request: :class:`huaweicloudsdkscm.v3.ShowCertificateRequest`
        :rtype: :class:`huaweicloudsdkscm.v3.ShowCertificateResponse`
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
