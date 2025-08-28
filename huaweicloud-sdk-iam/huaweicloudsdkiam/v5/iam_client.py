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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkiam'")


class IamClient(Client):
    def __init__(self):
        super(IamClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkiam.v5.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials,BasicCredentials,IamCredentials")
        else:
            if clazz.__name__ != "IamClient":
                raise TypeError("client type error, support client type is IamClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials,BasicCredentials,IamCredentials")

        

        return client_builder

    def get_account_summary_v5(self, request):
        r"""获取此账号中IAM实体使用情况和IAM配额的摘要信息

        该接口可以用于获取此账号中IAM实体使用情况和IAM配额的摘要信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetAccountSummaryV5
        :type request: :class:`huaweicloudsdkiam.v5.GetAccountSummaryV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.GetAccountSummaryV5Response`
        """
        http_info = self._get_account_summary_v5_http_info(request)
        return self._call_api(**http_info)

    def get_account_summary_v5_invoker(self, request):
        http_info = self._get_account_summary_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_account_summary_v5_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/account-summary",
            "request_type": request.__class__.__name__,
            "response_type": "GetAccountSummaryV5Response"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_agency_v5(self, request):
        r"""创建信任委托

        该接口可以用于创建信任委托。
        
        &gt; 信任委托只能授予身份策略且仅兼容支持身份策略的云服务，详情见[[支持身份策略与信任委托的云服务列表](https://support.huaweicloud.com/productdesc-iam/iam_01_1224.html)](tag:hws)[[支持身份策略与信任委托的云服务列表](https://support.huaweicloud.com/intl/zh-cn/productdesc-iam/iam_01_1224.html)](tag:hws_hk)[[支持身份策略与信任委托的云服务列表](https://support.huaweicloud.com/eu/productdesc-iam/iam_01_1224.html)](tag:hws_eu)[《统一身份认证用户指南》的“支持身份策略与信任委托的云服务列表”章节](tag:fcs,fcs_vm,ctc,hws_test,g42,tm)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAgencyV5
        :type request: :class:`huaweicloudsdkiam.v5.CreateAgencyV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.CreateAgencyV5Response`
        """
        http_info = self._create_agency_v5_http_info(request)
        return self._call_api(**http_info)

    def create_agency_v5_invoker(self, request):
        http_info = self._create_agency_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_agency_v5_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/agencies",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAgencyV5Response"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_agency_v5(self, request):
        r"""删除信任委托

        该接口可以用于删除信任委托。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAgencyV5
        :type request: :class:`huaweicloudsdkiam.v5.DeleteAgencyV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.DeleteAgencyV5Response`
        """
        http_info = self._delete_agency_v5_http_info(request)
        return self._call_api(**http_info)

    def delete_agency_v5_invoker(self, request):
        http_info = self._delete_agency_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_agency_v5_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/agencies/{agency_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAgencyV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agency_id' in local_var_params:
            path_params['agency_id'] = local_var_params['agency_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_agency_v5(self, request):
        r"""查询委托或信任委托详情

        该接口可以用于查询委托或信任委托详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetAgencyV5
        :type request: :class:`huaweicloudsdkiam.v5.GetAgencyV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.GetAgencyV5Response`
        """
        http_info = self._get_agency_v5_http_info(request)
        return self._call_api(**http_info)

    def get_agency_v5_invoker(self, request):
        http_info = self._get_agency_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_agency_v5_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/agencies/{agency_id}",
            "request_type": request.__class__.__name__,
            "response_type": "GetAgencyV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agency_id' in local_var_params:
            path_params['agency_id'] = local_var_params['agency_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_agencies_v5(self, request):
        r"""查询指定条件下的委托及信任委托列表

        该接口可以用于查询指定条件下的委托及信任委托列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAgenciesV5
        :type request: :class:`huaweicloudsdkiam.v5.ListAgenciesV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.ListAgenciesV5Response`
        """
        http_info = self._list_agencies_v5_http_info(request)
        return self._call_api(**http_info)

    def list_agencies_v5_invoker(self, request):
        http_info = self._list_agencies_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_agencies_v5_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/agencies",
            "request_type": request.__class__.__name__,
            "response_type": "ListAgenciesV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'path_prefix' in local_var_params:
            query_params.append(('path_prefix', local_var_params['path_prefix']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_agency_v5(self, request):
        r"""修改信任委托

        该接口可以用于修改信任委托。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAgencyV5
        :type request: :class:`huaweicloudsdkiam.v5.UpdateAgencyV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.UpdateAgencyV5Response`
        """
        http_info = self._update_agency_v5_http_info(request)
        return self._call_api(**http_info)

    def update_agency_v5_invoker(self, request):
        http_info = self._update_agency_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_agency_v5_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/agencies/{agency_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAgencyV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agency_id' in local_var_params:
            path_params['agency_id'] = local_var_params['agency_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_trust_policy_v5(self, request):
        r"""修改信任委托信任策略

        该接口可以用于修改信任委托信任策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTrustPolicyV5
        :type request: :class:`huaweicloudsdkiam.v5.UpdateTrustPolicyV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.UpdateTrustPolicyV5Response`
        """
        http_info = self._update_trust_policy_v5_http_info(request)
        return self._call_api(**http_info)

    def update_trust_policy_v5_invoker(self, request):
        http_info = self._update_trust_policy_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_trust_policy_v5_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/agencies/{agency_id}/trust-policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTrustPolicyV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agency_id' in local_var_params:
            path_params['agency_id'] = local_var_params['agency_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_asymmetric_signature_switch_v5(self, request):
        r"""获取账号非对称签名开关状态

        该接口用于获取账号非对称签名开关的状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetAsymmetricSignatureSwitchV5
        :type request: :class:`huaweicloudsdkiam.v5.GetAsymmetricSignatureSwitchV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.GetAsymmetricSignatureSwitchV5Response`
        """
        http_info = self._get_asymmetric_signature_switch_v5_http_info(request)
        return self._call_api(**http_info)

    def get_asymmetric_signature_switch_v5_invoker(self, request):
        http_info = self._get_asymmetric_signature_switch_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_asymmetric_signature_switch_v5_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/asymmetric-signature-switch",
            "request_type": request.__class__.__name__,
            "response_type": "GetAsymmetricSignatureSwitchV5Response"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def set_asymmetric_signature_switch_v5(self, request):
        r"""设置账号开启或关闭非对称签名

        该接口用于设置账号开启或关闭非对称签名功能。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetAsymmetricSignatureSwitchV5
        :type request: :class:`huaweicloudsdkiam.v5.SetAsymmetricSignatureSwitchV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.SetAsymmetricSignatureSwitchV5Response`
        """
        http_info = self._set_asymmetric_signature_switch_v5_http_info(request)
        return self._call_api(**http_info)

    def set_asymmetric_signature_switch_v5_invoker(self, request):
        http_info = self._set_asymmetric_signature_switch_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_asymmetric_signature_switch_v5_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/asymmetric-signature-switch",
            "request_type": request.__class__.__name__,
            "response_type": "SetAsymmetricSignatureSwitchV5Response"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_authorization_schema_v5(self, request):
        r"""查询指定服务授权概要

        该接口可以用于查询指定云服务的授权概要。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetAuthorizationSchemaV5
        :type request: :class:`huaweicloudsdkiam.v5.GetAuthorizationSchemaV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.GetAuthorizationSchemaV5Response`
        """
        http_info = self._get_authorization_schema_v5_http_info(request)
        return self._call_api(**http_info)

    def get_authorization_schema_v5_invoker(self, request):
        http_info = self._get_authorization_schema_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_authorization_schema_v5_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/authorization-schemas/services/{service_code}",
            "request_type": request.__class__.__name__,
            "response_type": "GetAuthorizationSchemaV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_code' in local_var_params:
            path_params['service_code'] = local_var_params['service_code']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_registered_services_for_auth_schema_v5(self, request):
        r"""查询已注册云服务列表

        该接口可以用于查询已注册云服务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRegisteredServicesForAuthSchemaV5
        :type request: :class:`huaweicloudsdkiam.v5.ListRegisteredServicesForAuthSchemaV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.ListRegisteredServicesForAuthSchemaV5Response`
        """
        http_info = self._list_registered_services_for_auth_schema_v5_http_info(request)
        return self._call_api(**http_info)

    def list_registered_services_for_auth_schema_v5_invoker(self, request):
        http_info = self._list_registered_services_for_auth_schema_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_registered_services_for_auth_schema_v5_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/authorization-schemas/registered-services",
            "request_type": request.__class__.__name__,
            "response_type": "ListRegisteredServicesForAuthSchemaV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def add_user_to_group_v5(self, request):
        r"""添加IAM用户到用户组

        该接口可以用于添加IAM用户到用户组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddUserToGroupV5
        :type request: :class:`huaweicloudsdkiam.v5.AddUserToGroupV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.AddUserToGroupV5Response`
        """
        http_info = self._add_user_to_group_v5_http_info(request)
        return self._call_api(**http_info)

    def add_user_to_group_v5_invoker(self, request):
        http_info = self._add_user_to_group_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_user_to_group_v5_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/groups/{group_id}/add-user",
            "request_type": request.__class__.__name__,
            "response_type": "AddUserToGroupV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_group_v5(self, request):
        r"""创建用户组

        该接口可以用于创建用户组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateGroupV5
        :type request: :class:`huaweicloudsdkiam.v5.CreateGroupV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.CreateGroupV5Response`
        """
        http_info = self._create_group_v5_http_info(request)
        return self._call_api(**http_info)

    def create_group_v5_invoker(self, request):
        http_info = self._create_group_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_group_v5_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGroupV5Response"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_group_v5(self, request):
        r"""删除用户组

        该接口可以用于删除用户组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteGroupV5
        :type request: :class:`huaweicloudsdkiam.v5.DeleteGroupV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.DeleteGroupV5Response`
        """
        http_info = self._delete_group_v5_http_info(request)
        return self._call_api(**http_info)

    def delete_group_v5_invoker(self, request):
        http_info = self._delete_group_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_group_v5_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGroupV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_groups_v5(self, request):
        r"""查询用户组列表

        该接口可以用于查询用户组列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGroupsV5
        :type request: :class:`huaweicloudsdkiam.v5.ListGroupsV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.ListGroupsV5Response`
        """
        http_info = self._list_groups_v5_http_info(request)
        return self._call_api(**http_info)

    def list_groups_v5_invoker(self, request):
        http_info = self._list_groups_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_groups_v5_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListGroupsV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'user_id' in local_var_params:
            query_params.append(('user_id', local_var_params['user_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def remove_user_from_group_v5(self, request):
        r"""移除用户组中的IAM用户

        该接口可以用于移除用户组中的IAM用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RemoveUserFromGroupV5
        :type request: :class:`huaweicloudsdkiam.v5.RemoveUserFromGroupV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.RemoveUserFromGroupV5Response`
        """
        http_info = self._remove_user_from_group_v5_http_info(request)
        return self._call_api(**http_info)

    def remove_user_from_group_v5_invoker(self, request):
        http_info = self._remove_user_from_group_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _remove_user_from_group_v5_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/groups/{group_id}/remove-user",
            "request_type": request.__class__.__name__,
            "response_type": "RemoveUserFromGroupV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_group_v5(self, request):
        r"""查询用户组详情

        该接口可以用于查询用户组详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGroupV5
        :type request: :class:`huaweicloudsdkiam.v5.ShowGroupV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.ShowGroupV5Response`
        """
        http_info = self._show_group_v5_http_info(request)
        return self._call_api(**http_info)

    def show_group_v5_invoker(self, request):
        http_info = self._show_group_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_group_v5_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGroupV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_group_v5(self, request):
        r"""修改用户组

        该接口可以用于修改用户组信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateGroupV5
        :type request: :class:`huaweicloudsdkiam.v5.UpdateGroupV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.UpdateGroupV5Response`
        """
        http_info = self._update_group_v5_http_info(request)
        return self._call_api(**http_info)

    def update_group_v5_invoker(self, request):
        http_info = self._update_group_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_group_v5_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGroupV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_virtual_mfa_device_v5(self, request):
        r"""创建MFA设备

        该接口可以用于创建MFA设备。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateVirtualMfaDeviceV5
        :type request: :class:`huaweicloudsdkiam.v5.CreateVirtualMfaDeviceV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.CreateVirtualMfaDeviceV5Response`
        """
        http_info = self._create_virtual_mfa_device_v5_http_info(request)
        return self._call_api(**http_info)

    def create_virtual_mfa_device_v5_invoker(self, request):
        http_info = self._create_virtual_mfa_device_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_virtual_mfa_device_v5_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/virtual-mfa-devices",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVirtualMfaDeviceV5Response"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_virtual_mfa_device_v5(self, request):
        r"""删除MFA设备

        该接口可以用于删除MFA设备。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteVirtualMfaDeviceV5
        :type request: :class:`huaweicloudsdkiam.v5.DeleteVirtualMfaDeviceV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.DeleteVirtualMfaDeviceV5Response`
        """
        http_info = self._delete_virtual_mfa_device_v5_http_info(request)
        return self._call_api(**http_info)

    def delete_virtual_mfa_device_v5_invoker(self, request):
        http_info = self._delete_virtual_mfa_device_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_virtual_mfa_device_v5_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/virtual-mfa-devices",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVirtualMfaDeviceV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in local_var_params:
            query_params.append(('user_id', local_var_params['user_id']))
        if 'serial_number' in local_var_params:
            query_params.append(('serial_number', local_var_params['serial_number']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def disable_mfa_device_v5(self, request):
        r"""禁用MFA设备

        该接口可以用于禁用指定的MFA设备并删除其与对应IAM用户的关联。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisableMfaDeviceV5
        :type request: :class:`huaweicloudsdkiam.v5.DisableMfaDeviceV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.DisableMfaDeviceV5Response`
        """
        http_info = self._disable_mfa_device_v5_http_info(request)
        return self._call_api(**http_info)

    def disable_mfa_device_v5_invoker(self, request):
        http_info = self._disable_mfa_device_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disable_mfa_device_v5_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/mfa-devices/disable",
            "request_type": request.__class__.__name__,
            "response_type": "DisableMfaDeviceV5Response"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def enable_mfa_device_v5(self, request):
        r"""启用MFA设备

        该接口可以用于启用指定的MFA设备并将其与指定的IAM用户关联。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableMfaDeviceV5
        :type request: :class:`huaweicloudsdkiam.v5.EnableMfaDeviceV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.EnableMfaDeviceV5Response`
        """
        http_info = self._enable_mfa_device_v5_http_info(request)
        return self._call_api(**http_info)

    def enable_mfa_device_v5_invoker(self, request):
        http_info = self._enable_mfa_device_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_mfa_device_v5_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/mfa-devices/enable",
            "request_type": request.__class__.__name__,
            "response_type": "EnableMfaDeviceV5Response"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_mfa_devices_v5(self, request):
        r"""列举全部MFA设备

        该接口可以用于列举全部MFA设备。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMfaDevicesV5
        :type request: :class:`huaweicloudsdkiam.v5.ListMfaDevicesV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.ListMfaDevicesV5Response`
        """
        http_info = self._list_mfa_devices_v5_http_info(request)
        return self._call_api(**http_info)

    def list_mfa_devices_v5_invoker(self, request):
        http_info = self._list_mfa_devices_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_mfa_devices_v5_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/mfa-devices",
            "request_type": request.__class__.__name__,
            "response_type": "ListMfaDevicesV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in local_var_params:
            query_params.append(('user_id', local_var_params['user_id']))
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_policy_v5(self, request):
        r"""创建自定义身份策略

        该接口可以用于创建一个默认版本为v1的新自定义身份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePolicyV5
        :type request: :class:`huaweicloudsdkiam.v5.CreatePolicyV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.CreatePolicyV5Response`
        """
        http_info = self._create_policy_v5_http_info(request)
        return self._call_api(**http_info)

    def create_policy_v5_invoker(self, request):
        http_info = self._create_policy_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_policy_v5_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/policies",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePolicyV5Response"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_policy_v5(self, request):
        r"""删除自定义身份策略

        该接口可以用于删除一个存在的自定义身份策略，必须确保该自定义身份策略没有附加在任何IAM用户、用户组、委托或信任委托上。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePolicyV5
        :type request: :class:`huaweicloudsdkiam.v5.DeletePolicyV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.DeletePolicyV5Response`
        """
        http_info = self._delete_policy_v5_http_info(request)
        return self._call_api(**http_info)

    def delete_policy_v5_invoker(self, request):
        http_info = self._delete_policy_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_policy_v5_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePolicyV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_policy_v5(self, request):
        r"""通过身份策略ID获取身份策略

        该接口可以用于通过身份策略ID获取身份策略信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetPolicyV5
        :type request: :class:`huaweicloudsdkiam.v5.GetPolicyV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.GetPolicyV5Response`
        """
        http_info = self._get_policy_v5_http_info(request)
        return self._call_api(**http_info)

    def get_policy_v5_invoker(self, request):
        http_info = self._get_policy_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_policy_v5_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "GetPolicyV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_policies_v5(self, request):
        r"""查询所有身份策略

        该接口可以用于查询所有身份策略，包含系统预置身份策略和自定义身份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPoliciesV5
        :type request: :class:`huaweicloudsdkiam.v5.ListPoliciesV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.ListPoliciesV5Response`
        """
        http_info = self._list_policies_v5_http_info(request)
        return self._call_api(**http_info)

    def list_policies_v5_invoker(self, request):
        http_info = self._list_policies_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_policies_v5_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListPoliciesV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'policy_type' in local_var_params:
            query_params.append(('policy_type', local_var_params['policy_type']))
        if 'path_prefix' in local_var_params:
            query_params.append(('path_prefix', local_var_params['path_prefix']))
        if 'only_attached' in local_var_params:
            query_params.append(('only_attached', local_var_params['only_attached']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def attach_agency_policy_v5(self, request):
        r"""为委托或信任委托附加身份策略

        该接口可以用于为指定委托或信任委托附加指定身份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AttachAgencyPolicyV5
        :type request: :class:`huaweicloudsdkiam.v5.AttachAgencyPolicyV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.AttachAgencyPolicyV5Response`
        """
        http_info = self._attach_agency_policy_v5_http_info(request)
        return self._call_api(**http_info)

    def attach_agency_policy_v5_invoker(self, request):
        http_info = self._attach_agency_policy_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _attach_agency_policy_v5_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/policies/{policy_id}/attach-agency",
            "request_type": request.__class__.__name__,
            "response_type": "AttachAgencyPolicyV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def attach_group_policy_v5(self, request):
        r"""为用户组附加身份策略

        该接口可以用于为指定用户组附加指定身份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AttachGroupPolicyV5
        :type request: :class:`huaweicloudsdkiam.v5.AttachGroupPolicyV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.AttachGroupPolicyV5Response`
        """
        http_info = self._attach_group_policy_v5_http_info(request)
        return self._call_api(**http_info)

    def attach_group_policy_v5_invoker(self, request):
        http_info = self._attach_group_policy_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _attach_group_policy_v5_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/policies/{policy_id}/attach-group",
            "request_type": request.__class__.__name__,
            "response_type": "AttachGroupPolicyV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def attach_user_policy_v5(self, request):
        r"""为IAM用户附加身份策略

        该接口可以用于为指定IAM用户附加指定身份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AttachUserPolicyV5
        :type request: :class:`huaweicloudsdkiam.v5.AttachUserPolicyV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.AttachUserPolicyV5Response`
        """
        http_info = self._attach_user_policy_v5_http_info(request)
        return self._call_api(**http_info)

    def attach_user_policy_v5_invoker(self, request):
        http_info = self._attach_user_policy_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _attach_user_policy_v5_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/policies/{policy_id}/attach-user",
            "request_type": request.__class__.__name__,
            "response_type": "AttachUserPolicyV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def detach_agency_policy_v5(self, request):
        r"""从委托或信任委托分离身份策略

        该接口可以用于从指定委托或信任委托中分离指定身份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DetachAgencyPolicyV5
        :type request: :class:`huaweicloudsdkiam.v5.DetachAgencyPolicyV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.DetachAgencyPolicyV5Response`
        """
        http_info = self._detach_agency_policy_v5_http_info(request)
        return self._call_api(**http_info)

    def detach_agency_policy_v5_invoker(self, request):
        http_info = self._detach_agency_policy_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _detach_agency_policy_v5_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/policies/{policy_id}/detach-agency",
            "request_type": request.__class__.__name__,
            "response_type": "DetachAgencyPolicyV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def detach_group_policy_v5(self, request):
        r"""从用户组分离身份策略

        该接口可以用于从指定用户组分离指定身份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DetachGroupPolicyV5
        :type request: :class:`huaweicloudsdkiam.v5.DetachGroupPolicyV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.DetachGroupPolicyV5Response`
        """
        http_info = self._detach_group_policy_v5_http_info(request)
        return self._call_api(**http_info)

    def detach_group_policy_v5_invoker(self, request):
        http_info = self._detach_group_policy_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _detach_group_policy_v5_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/policies/{policy_id}/detach-group",
            "request_type": request.__class__.__name__,
            "response_type": "DetachGroupPolicyV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def detach_user_policy_v5(self, request):
        r"""从IAM用户分离身份策略

        该接口可以用于从指定的IAM用户分离指定身份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DetachUserPolicyV5
        :type request: :class:`huaweicloudsdkiam.v5.DetachUserPolicyV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.DetachUserPolicyV5Response`
        """
        http_info = self._detach_user_policy_v5_http_info(request)
        return self._call_api(**http_info)

    def detach_user_policy_v5_invoker(self, request):
        http_info = self._detach_user_policy_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _detach_user_policy_v5_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/policies/{policy_id}/detach-user",
            "request_type": request.__class__.__name__,
            "response_type": "DetachUserPolicyV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_attached_agency_policies_v5(self, request):
        r"""查询指定委托或信任委托附加的所有身份策略

        该接口可用于查询指定委托或信任委托附加的所有身份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAttachedAgencyPoliciesV5
        :type request: :class:`huaweicloudsdkiam.v5.ListAttachedAgencyPoliciesV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.ListAttachedAgencyPoliciesV5Response`
        """
        http_info = self._list_attached_agency_policies_v5_http_info(request)
        return self._call_api(**http_info)

    def list_attached_agency_policies_v5_invoker(self, request):
        http_info = self._list_attached_agency_policies_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_attached_agency_policies_v5_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/agencies/{agency_id}/attached-policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListAttachedAgencyPoliciesV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agency_id' in local_var_params:
            path_params['agency_id'] = local_var_params['agency_id']

        query_params = []
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_attached_group_policies_v5(self, request):
        r"""查询指定用户组附加的所有身份策略

        该接口可用于查询指定用户组附加的所有身份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAttachedGroupPoliciesV5
        :type request: :class:`huaweicloudsdkiam.v5.ListAttachedGroupPoliciesV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.ListAttachedGroupPoliciesV5Response`
        """
        http_info = self._list_attached_group_policies_v5_http_info(request)
        return self._call_api(**http_info)

    def list_attached_group_policies_v5_invoker(self, request):
        http_info = self._list_attached_group_policies_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_attached_group_policies_v5_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/groups/{group_id}/attached-policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListAttachedGroupPoliciesV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_attached_user_policies_v5(self, request):
        r"""查询指定IAM用户附加的所有身份策略

        该接口可用于查询指定IAM用户附加的所有身份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAttachedUserPoliciesV5
        :type request: :class:`huaweicloudsdkiam.v5.ListAttachedUserPoliciesV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.ListAttachedUserPoliciesV5Response`
        """
        http_info = self._list_attached_user_policies_v5_http_info(request)
        return self._call_api(**http_info)

    def list_attached_user_policies_v5_invoker(self, request):
        http_info = self._list_attached_user_policies_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_attached_user_policies_v5_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/users/{user_id}/attached-policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListAttachedUserPoliciesV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_entities_for_policy_v5(self, request):
        r"""查询指定身份策略附加的所有实体

        该接口可用于查询指定身份策略附加的所有实体。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEntitiesForPolicyV5
        :type request: :class:`huaweicloudsdkiam.v5.ListEntitiesForPolicyV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.ListEntitiesForPolicyV5Response`
        """
        http_info = self._list_entities_for_policy_v5_http_info(request)
        return self._call_api(**http_info)

    def list_entities_for_policy_v5_invoker(self, request):
        http_info = self._list_entities_for_policy_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_entities_for_policy_v5_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/policies/{policy_id}/attached-entities",
            "request_type": request.__class__.__name__,
            "response_type": "ListEntitiesForPolicyV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'entity_type' in local_var_params:
            query_params.append(('entity_type', local_var_params['entity_type']))
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_policy_version_v5(self, request):
        r"""为指定身份策略创建一个新版本

        该接口可以用于为指定身份策略创建一个新版本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePolicyVersionV5
        :type request: :class:`huaweicloudsdkiam.v5.CreatePolicyVersionV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.CreatePolicyVersionV5Response`
        """
        http_info = self._create_policy_version_v5_http_info(request)
        return self._call_api(**http_info)

    def create_policy_version_v5_invoker(self, request):
        http_info = self._create_policy_version_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_policy_version_v5_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/policies/{policy_id}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePolicyVersionV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_policy_version_v5(self, request):
        r"""删除指定身份策略版本

        该接口可以用于删除指定身份策略的指定版本。默认身份策略版本不能被删除。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePolicyVersionV5
        :type request: :class:`huaweicloudsdkiam.v5.DeletePolicyVersionV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.DeletePolicyVersionV5Response`
        """
        http_info = self._delete_policy_version_v5_http_info(request)
        return self._call_api(**http_info)

    def delete_policy_version_v5_invoker(self, request):
        http_info = self._delete_policy_version_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_policy_version_v5_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/policies/{policy_id}/versions/{version_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePolicyVersionV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_policy_version_v5(self, request):
        r"""查询指定身份策略版本

        该接口可以用于查询指定身份策略的指定版本的相关信息，包括身份策略文档。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetPolicyVersionV5
        :type request: :class:`huaweicloudsdkiam.v5.GetPolicyVersionV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.GetPolicyVersionV5Response`
        """
        http_info = self._get_policy_version_v5_http_info(request)
        return self._call_api(**http_info)

    def get_policy_version_v5_invoker(self, request):
        http_info = self._get_policy_version_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_policy_version_v5_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/policies/{policy_id}/versions/{version_id}",
            "request_type": request.__class__.__name__,
            "response_type": "GetPolicyVersionV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_policy_versions_v5(self, request):
        r"""查询指定身份策略的所有版本

        该接口可以用于查询指定身份策略的所有版本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPolicyVersionsV5
        :type request: :class:`huaweicloudsdkiam.v5.ListPolicyVersionsV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.ListPolicyVersionsV5Response`
        """
        http_info = self._list_policy_versions_v5_http_info(request)
        return self._call_api(**http_info)

    def list_policy_versions_v5_invoker(self, request):
        http_info = self._list_policy_versions_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_policy_versions_v5_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/policies/{policy_id}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "ListPolicyVersionsV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def set_default_policy_version_v5(self, request):
        r"""将指定身份策略版本设置为默认版本

        该接口可以用于将指定身份策略的指定版本设置为默认版本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetDefaultPolicyVersionV5
        :type request: :class:`huaweicloudsdkiam.v5.SetDefaultPolicyVersionV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.SetDefaultPolicyVersionV5Response`
        """
        http_info = self._set_default_policy_version_v5_http_info(request)
        return self._call_api(**http_info)

    def set_default_policy_version_v5_invoker(self, request):
        http_info = self._set_default_policy_version_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_default_policy_version_v5_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/policies/{policy_id}/versions/{version_id}/set-default",
            "request_type": request.__class__.__name__,
            "response_type": "SetDefaultPolicyVersionV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_resource_tags_v5(self, request):
        r"""删除指定资源的部分标签

        该接口可以用于删除指定资源的部分标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteResourceTagsV5
        :type request: :class:`huaweicloudsdkiam.v5.DeleteResourceTagsV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.DeleteResourceTagsV5Response`
        """
        http_info = self._delete_resource_tags_v5_http_info(request)
        return self._call_api(**http_info)

    def delete_resource_tags_v5_invoker(self, request):
        http_info = self._delete_resource_tags_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_resource_tags_v5_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{resource_type}/{resource_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteResourceTagsV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_resource_tags_v5(self, request):
        r"""获取指定资源的所有标签

        该接口可以用于获取指定资源的所有标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceTagsV5
        :type request: :class:`huaweicloudsdkiam.v5.ListResourceTagsV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.ListResourceTagsV5Response`
        """
        http_info = self._list_resource_tags_v5_http_info(request)
        return self._call_api(**http_info)

    def list_resource_tags_v5_invoker(self, request):
        http_info = self._list_resource_tags_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_resource_tags_v5_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{resource_type}/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceTagsV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def tag_resource_v5(self, request):
        r"""为IAM资源打上标签

        该接口可以用于为IAM资源打上标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for TagResourceV5
        :type request: :class:`huaweicloudsdkiam.v5.TagResourceV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.TagResourceV5Response`
        """
        http_info = self._tag_resource_v5_http_info(request)
        return self._call_api(**http_info)

    def tag_resource_v5_invoker(self, request):
        http_info = self._tag_resource_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _tag_resource_v5_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{resource_type}/{resource_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "TagResourceV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_login_policy_v5(self, request):
        r"""查询账号登录策略

        该接口可以用于查询账号登录策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLoginPolicyV5
        :type request: :class:`huaweicloudsdkiam.v5.ShowLoginPolicyV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.ShowLoginPolicyV5Response`
        """
        http_info = self._show_login_policy_v5_http_info(request)
        return self._call_api(**http_info)

    def show_login_policy_v5_invoker(self, request):
        http_info = self._show_login_policy_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_login_policy_v5_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/login-policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLoginPolicyV5Response"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_password_policy_v5(self, request):
        r"""查询账号密码策略

        该接口可以用于查询账号密码策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPasswordPolicyV5
        :type request: :class:`huaweicloudsdkiam.v5.ShowPasswordPolicyV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.ShowPasswordPolicyV5Response`
        """
        http_info = self._show_password_policy_v5_http_info(request)
        return self._call_api(**http_info)

    def show_password_policy_v5_invoker(self, request):
        http_info = self._show_password_policy_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_password_policy_v5_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/password-policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPasswordPolicyV5Response"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_token_policy_v5(self, request):
        r"""查询账号的Token策略

        查询账号的Token策略，Token策略控制账号下的所有身份类型（IAM用户、委托、联邦用户）是否允许获取Token（联邦认证获取的unscoped token不受Token策略影响）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTokenPolicyV5
        :type request: :class:`huaweicloudsdkiam.v5.ShowTokenPolicyV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.ShowTokenPolicyV5Response`
        """
        http_info = self._show_token_policy_v5_http_info(request)
        return self._call_api(**http_info)

    def show_token_policy_v5_invoker(self, request):
        http_info = self._show_token_policy_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_token_policy_v5_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/token-policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTokenPolicyV5Response"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_login_policy_v5(self, request):
        r"""修改账号登录策略

        该接口可以用于修改账号登录策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateLoginPolicyV5
        :type request: :class:`huaweicloudsdkiam.v5.UpdateLoginPolicyV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.UpdateLoginPolicyV5Response`
        """
        http_info = self._update_login_policy_v5_http_info(request)
        return self._call_api(**http_info)

    def update_login_policy_v5_invoker(self, request):
        http_info = self._update_login_policy_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_login_policy_v5_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/login-policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLoginPolicyV5Response"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_password_policy_v5(self, request):
        r"""修改账号密码策略

        该接口可以用于修改账号密码策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePasswordPolicyV5
        :type request: :class:`huaweicloudsdkiam.v5.UpdatePasswordPolicyV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.UpdatePasswordPolicyV5Response`
        """
        http_info = self._update_password_policy_v5_http_info(request)
        return self._call_api(**http_info)

    def update_password_policy_v5_invoker(self, request):
        http_info = self._update_password_policy_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_password_policy_v5_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/password-policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePasswordPolicyV5Response"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_token_policy_v5(self, request):
        r"""修改账号的Token策略

        修改账号的Token策略，Token策略控制账号下的所有身份类型（IAM用户、委托、联邦用户）是否允许获取Token（联邦认证获取的unscoped token不受Token策略影响）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTokenPolicyV5
        :type request: :class:`huaweicloudsdkiam.v5.UpdateTokenPolicyV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.UpdateTokenPolicyV5Response`
        """
        http_info = self._update_token_policy_v5_http_info(request)
        return self._call_api(**http_info)

    def update_token_policy_v5_invoker(self, request):
        http_info = self._update_token_policy_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_token_policy_v5_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/token-policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTokenPolicyV5Response"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_service_linked_agency_v5(self, request):
        r"""创建服务关联委托

        该接口可以用于创建服务关联委托。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateServiceLinkedAgencyV5
        :type request: :class:`huaweicloudsdkiam.v5.CreateServiceLinkedAgencyV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.CreateServiceLinkedAgencyV5Response`
        """
        http_info = self._create_service_linked_agency_v5_http_info(request)
        return self._call_api(**http_info)

    def create_service_linked_agency_v5_invoker(self, request):
        http_info = self._create_service_linked_agency_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_service_linked_agency_v5_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/service-linked-agencies",
            "request_type": request.__class__.__name__,
            "response_type": "CreateServiceLinkedAgencyV5Response"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_service_linked_agency_v5(self, request):
        r"""删除服务关联委托

        该接口可以用于服务关联委托删除自己。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteServiceLinkedAgencyV5
        :type request: :class:`huaweicloudsdkiam.v5.DeleteServiceLinkedAgencyV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.DeleteServiceLinkedAgencyV5Response`
        """
        http_info = self._delete_service_linked_agency_v5_http_info(request)
        return self._call_api(**http_info)

    def delete_service_linked_agency_v5_invoker(self, request):
        http_info = self._delete_service_linked_agency_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_service_linked_agency_v5_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/service-linked-agencies/{agency_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteServiceLinkedAgencyV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agency_id' in local_var_params:
            path_params['agency_id'] = local_var_params['agency_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_service_linked_agency_deletion_status_v5(self, request):
        r"""获取服务关联委托删除状态

        该接口可以用于获取服务关联委托删除状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetServiceLinkedAgencyDeletionStatusV5
        :type request: :class:`huaweicloudsdkiam.v5.GetServiceLinkedAgencyDeletionStatusV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.GetServiceLinkedAgencyDeletionStatusV5Response`
        """
        http_info = self._get_service_linked_agency_deletion_status_v5_http_info(request)
        return self._call_api(**http_info)

    def get_service_linked_agency_deletion_status_v5_invoker(self, request):
        http_info = self._get_service_linked_agency_deletion_status_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_service_linked_agency_deletion_status_v5_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/service-linked-agencies/deletion-task/{deletion_task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "GetServiceLinkedAgencyDeletionStatusV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'deletion_task_id' in local_var_params:
            path_params['deletion_task_id'] = local_var_params['deletion_task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_service_principals_v5(self, request):
        r"""获取全部服务主体

        该接口可以用于获取全部服务主体。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListServicePrincipalsV5
        :type request: :class:`huaweicloudsdkiam.v5.ListServicePrincipalsV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.ListServicePrincipalsV5Response`
        """
        http_info = self._list_service_principals_v5_http_info(request)
        return self._call_api(**http_info)

    def list_service_principals_v5_invoker(self, request):
        http_info = self._list_service_principals_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_service_principals_v5_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/service-principals",
            "request_type": request.__class__.__name__,
            "response_type": "ListServicePrincipalsV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_user_v5(self, request):
        r"""创建IAM用户

        该接口可以用于创建IAM用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateUserV5
        :type request: :class:`huaweicloudsdkiam.v5.CreateUserV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.CreateUserV5Response`
        """
        http_info = self._create_user_v5_http_info(request)
        return self._call_api(**http_info)

    def create_user_v5_invoker(self, request):
        http_info = self._create_user_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_user_v5_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/users",
            "request_type": request.__class__.__name__,
            "response_type": "CreateUserV5Response"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_user_v5(self, request):
        r"""删除IAM用户

        该接口可以用于删除指定IAM用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteUserV5
        :type request: :class:`huaweicloudsdkiam.v5.DeleteUserV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.DeleteUserV5Response`
        """
        http_info = self._delete_user_v5_http_info(request)
        return self._call_api(**http_info)

    def delete_user_v5_invoker(self, request):
        http_info = self._delete_user_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_user_v5_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/users/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteUserV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_users_v5(self, request):
        r"""查询IAM用户列表

        该接口可以用于查询IAM用户列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUsersV5
        :type request: :class:`huaweicloudsdkiam.v5.ListUsersV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.ListUsersV5Response`
        """
        http_info = self._list_users_v5_http_info(request)
        return self._call_api(**http_info)

    def list_users_v5_invoker(self, request):
        http_info = self._list_users_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_users_v5_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/users",
            "request_type": request.__class__.__name__,
            "response_type": "ListUsersV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_user_last_login_v5(self, request):
        r"""查询IAM用户最后登录时间

        该接口可以用于查询IAM用户的最后登录时间。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUserLastLoginV5
        :type request: :class:`huaweicloudsdkiam.v5.ShowUserLastLoginV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.ShowUserLastLoginV5Response`
        """
        http_info = self._show_user_last_login_v5_http_info(request)
        return self._call_api(**http_info)

    def show_user_last_login_v5_invoker(self, request):
        http_info = self._show_user_last_login_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_user_last_login_v5_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/users/{user_id}/last-login",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUserLastLoginV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_user_v5(self, request):
        r"""查询IAM用户详情

        该接口可以用于查询IAM用户详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUserV5
        :type request: :class:`huaweicloudsdkiam.v5.ShowUserV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.ShowUserV5Response`
        """
        http_info = self._show_user_v5_http_info(request)
        return self._call_api(**http_info)

    def show_user_v5_invoker(self, request):
        http_info = self._show_user_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_user_v5_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/users/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUserV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_user_v5(self, request):
        r"""修改IAM用户信息

        该接口可以用于修改IAM用户信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateUserV5
        :type request: :class:`huaweicloudsdkiam.v5.UpdateUserV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.UpdateUserV5Response`
        """
        http_info = self._update_user_v5_http_info(request)
        return self._call_api(**http_info)

    def update_user_v5_invoker(self, request):
        http_info = self._update_user_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_user_v5_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/users/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateUserV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def change_password_v5(self, request):
        r"""修改IAM用户密码

        该接口可以用于IAM用户修改自己的密码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangePasswordV5
        :type request: :class:`huaweicloudsdkiam.v5.ChangePasswordV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.ChangePasswordV5Response`
        """
        http_info = self._change_password_v5_http_info(request)
        return self._call_api(**http_info)

    def change_password_v5_invoker(self, request):
        http_info = self._change_password_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_password_v5_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/caller-password",
            "request_type": request.__class__.__name__,
            "response_type": "ChangePasswordV5Response"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_access_key_v5(self, request):
        r"""创建永久访问密钥

        该接口可以用于给IAM用户创建永久访问密钥。
        
        访问密钥（Access Key ID/Secret Access Key，简称AK/SK），是您通过开发工具（API、CLI、SDK）访问的身份凭证，不用于登录控制台。系统通过AK识别访问用户的身份，通过SK进行签名验证，通过加密签名验证可以确保请求的机密性、完整性和请求者身份的正确性。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAccessKeyV5
        :type request: :class:`huaweicloudsdkiam.v5.CreateAccessKeyV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.CreateAccessKeyV5Response`
        """
        http_info = self._create_access_key_v5_http_info(request)
        return self._call_api(**http_info)

    def create_access_key_v5_invoker(self, request):
        http_info = self._create_access_key_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_access_key_v5_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/users/{user_id}/access-keys",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAccessKeyV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_login_profile_v5(self, request):
        r"""创建IAM用户登录信息

        该接口可以用于创建指定IAM用户的登录信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateLoginProfileV5
        :type request: :class:`huaweicloudsdkiam.v5.CreateLoginProfileV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.CreateLoginProfileV5Response`
        """
        http_info = self._create_login_profile_v5_http_info(request)
        return self._call_api(**http_info)

    def create_login_profile_v5_invoker(self, request):
        http_info = self._create_login_profile_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_login_profile_v5_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/users/{user_id}/login-profile",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLoginProfileV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_access_key_v5(self, request):
        r"""删除指定永久访问密钥

        该接口可以用于删除IAM用户的指定永久访问密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAccessKeyV5
        :type request: :class:`huaweicloudsdkiam.v5.DeleteAccessKeyV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.DeleteAccessKeyV5Response`
        """
        http_info = self._delete_access_key_v5_http_info(request)
        return self._call_api(**http_info)

    def delete_access_key_v5_invoker(self, request):
        http_info = self._delete_access_key_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_access_key_v5_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/users/{user_id}/access-keys/{access_key_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAccessKeyV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']
        if 'access_key_id' in local_var_params:
            path_params['access_key_id'] = local_var_params['access_key_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_login_profile_v5(self, request):
        r"""删除IAM用户登录信息

        该接口可以用于删除指定IAM用户的登录信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteLoginProfileV5
        :type request: :class:`huaweicloudsdkiam.v5.DeleteLoginProfileV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.DeleteLoginProfileV5Response`
        """
        http_info = self._delete_login_profile_v5_http_info(request)
        return self._call_api(**http_info)

    def delete_login_profile_v5_invoker(self, request):
        http_info = self._delete_login_profile_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_login_profile_v5_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/users/{user_id}/login-profile",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLoginProfileV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_access_keys_v5(self, request):
        r"""查询所有永久访问密钥

        该接口可以用于查询IAM用户的所有永久访问密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAccessKeysV5
        :type request: :class:`huaweicloudsdkiam.v5.ListAccessKeysV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.ListAccessKeysV5Response`
        """
        http_info = self._list_access_keys_v5_http_info(request)
        return self._call_api(**http_info)

    def list_access_keys_v5_invoker(self, request):
        http_info = self._list_access_keys_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_access_keys_v5_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/users/{user_id}/access-keys",
            "request_type": request.__class__.__name__,
            "response_type": "ListAccessKeysV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_access_key_last_used_v5(self, request):
        r"""查询指定永久访问密钥最后使用时间

        该接口可以用于查询IAM用户的指定永久访问密钥的最后使用时间。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAccessKeyLastUsedV5
        :type request: :class:`huaweicloudsdkiam.v5.ShowAccessKeyLastUsedV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.ShowAccessKeyLastUsedV5Response`
        """
        http_info = self._show_access_key_last_used_v5_http_info(request)
        return self._call_api(**http_info)

    def show_access_key_last_used_v5_invoker(self, request):
        http_info = self._show_access_key_last_used_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_access_key_last_used_v5_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/users/{user_id}/access-keys/{access_key_id}/last-used",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAccessKeyLastUsedV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']
        if 'access_key_id' in local_var_params:
            path_params['access_key_id'] = local_var_params['access_key_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_login_profile_v5(self, request):
        r"""查询IAM用户登录信息

        该接口可以用于查询指定IAM用户的登录信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLoginProfileV5
        :type request: :class:`huaweicloudsdkiam.v5.ShowLoginProfileV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.ShowLoginProfileV5Response`
        """
        http_info = self._show_login_profile_v5_http_info(request)
        return self._call_api(**http_info)

    def show_login_profile_v5_invoker(self, request):
        http_info = self._show_login_profile_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_login_profile_v5_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/users/{user_id}/login-profile",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLoginProfileV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_access_key_v5(self, request):
        r"""修改指定永久访问密钥

        该接口可以用于修改IAM用户的指定永久访问密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAccessKeyV5
        :type request: :class:`huaweicloudsdkiam.v5.UpdateAccessKeyV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.UpdateAccessKeyV5Response`
        """
        http_info = self._update_access_key_v5_http_info(request)
        return self._call_api(**http_info)

    def update_access_key_v5_invoker(self, request):
        http_info = self._update_access_key_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_access_key_v5_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/users/{user_id}/access-keys/{access_key_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAccessKeyV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']
        if 'access_key_id' in local_var_params:
            path_params['access_key_id'] = local_var_params['access_key_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_login_profile_v5(self, request):
        r"""修改IAM用户登录信息

        该接口可以用于修改指定IAM用户的登录信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateLoginProfileV5
        :type request: :class:`huaweicloudsdkiam.v5.UpdateLoginProfileV5Request`
        :rtype: :class:`huaweicloudsdkiam.v5.UpdateLoginProfileV5Response`
        """
        http_info = self._update_login_profile_v5_http_info(request)
        return self._call_api(**http_info)

    def update_login_profile_v5_invoker(self, request):
        http_info = self._update_login_profile_v5_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_login_profile_v5_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/users/{user_id}/login-profile",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLoginProfileV5Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

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
