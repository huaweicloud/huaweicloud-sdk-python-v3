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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdksmsapi'")


class SMSApiAsyncClient(Client):
    def __init__(self):
        super(SMSApiAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdksmsapi.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "SMSApiCredentials")
        else:
            if clazz.__name__ != "SMSApiAsyncClient":
                raise TypeError("client type error, support client type is SMSApiAsyncClient")
            client_builder = ClientBuilder(clazz, "SMSApiCredentials")

        

        return client_builder

    def batch_send_diff_sms_async(self, request):
        r"""发送分批短信

        发送分批短信
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchSendDiffSms
        :type request: :class:`huaweicloudsdksmsapi.v1.BatchSendDiffSmsRequest`
        :rtype: :class:`huaweicloudsdksmsapi.v1.BatchSendDiffSmsResponse`
        """
        http_info = self._batch_send_diff_sms_http_info(request)
        return self._call_api(**http_info)

    def batch_send_diff_sms_async_invoker(self, request):
        http_info = self._batch_send_diff_sms_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_send_diff_sms_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/sms/batchSendDiffSms/v1",
            "request_type": request.__class__.__name__,
            "response_type": "BatchSendDiffSmsResponse"
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

    def batch_send_sms_async(self, request):
        r"""发送短信

        ## 典型场景 ##
         SP调用此接口发送短信。
        ## 接口功能 ##
         该接口用于SP请求短信平台向指定用户发送短信。
        ## 使用说明 ##
             前提条件
          i.  已在短信平台获取该短信能力开放应用的app_key、app_secret。
        
            注意事项
          a.  群发短信时，如果“to”参数携带的号码中包含除数字和+之外的其他字符，则无法向该参数携带的所有号码发送短信。如果“to”参数携带的所有号码只包含数字和+，但部分号码不符合号码规则要求，则在响应消息中会通过状态码标识发送失败的号码，不影响其他正常号码的短信发送。号码之间以英文逗号分隔，每个号码最大长度为21位，最多允许携带500个号码。
          b. 本接口支持特殊AK/SK认证。
          c.  X-Sdk-Date不能与发送请求时的本地时间相差太大（15分钟），否则会导致鉴权失败。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchSendSms
        :type request: :class:`huaweicloudsdksmsapi.v1.BatchSendSmsRequest`
        :rtype: :class:`huaweicloudsdksmsapi.v1.BatchSendSmsResponse`
        """
        http_info = self._batch_send_sms_http_info(request)
        return self._call_api(**http_info)

    def batch_send_sms_async_invoker(self, request):
        http_info = self._batch_send_sms_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_send_sms_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/sms/batchSendSms/v1",
            "request_type": request.__class__.__name__,
            "response_type": "BatchSendSmsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}
        if '_from' in local_var_params:
            form_params['from'] = local_var_params['_from']
        if 'to' in local_var_params:
            form_params['to'] = local_var_params['to']
        if 'template_id' in local_var_params:
            form_params['templateId'] = local_var_params['template_id']
        if 'template_paras' in local_var_params:
            form_params['templateParas'] = local_var_params['template_paras']
        if 'status_callback' in local_var_params:
            form_params['statusCallback'] = local_var_params['status_callback']
        if 'extend' in local_var_params:
            form_params['extend'] = local_var_params['extend']
        if 'signature' in local_var_params:
            form_params['signature'] = local_var_params['signature']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/x-www-form-urlencoded'])

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
