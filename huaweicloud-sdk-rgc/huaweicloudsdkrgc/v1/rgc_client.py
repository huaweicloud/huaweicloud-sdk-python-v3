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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkrgc'")


class RgcClient(Client):
    def __init__(self):
        super(RgcClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkrgc.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "RgcClient":
                raise TypeError("client type error, support client type is RgcClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def disable_control(self, request):
        """关闭控制策略

        关闭组织下的某个单元的某个控制策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisableControl
        :type request: :class:`huaweicloudsdkrgc.v1.DisableControlRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.DisableControlResponse`
        """
        http_info = self._disable_control_http_info(request)
        return self._call_api(**http_info)

    def disable_control_invoker(self, request):
        http_info = self._disable_control_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disable_control_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/governance/control/disable",
            "request_type": request.__class__.__name__,
            "response_type": "DisableControlResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def enable_control(self, request):
        """开启控制策略

        给组织下的某个单元开启某个控制策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableControl
        :type request: :class:`huaweicloudsdkrgc.v1.EnableControlRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.EnableControlResponse`
        """
        http_info = self._enable_control_http_info(request)
        return self._call_api(**http_info)

    def enable_control_invoker(self, request):
        http_info = self._enable_control_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_control_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/governance/control/enable",
            "request_type": request.__class__.__name__,
            "response_type": "EnableControlResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_config_rule_compliance(self, request):
        """查询账号的合规性状态

        查询组织里某个账号下开启的所有控制策略的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConfigRuleCompliance
        :type request: :class:`huaweicloudsdkrgc.v1.ListConfigRuleComplianceRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.ListConfigRuleComplianceResponse`
        """
        http_info = self._list_config_rule_compliance_http_info(request)
        return self._call_api(**http_info)

    def list_config_rule_compliance_invoker(self, request):
        http_info = self._list_config_rule_compliance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_config_rule_compliance_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/governance/account/{account_id}/config-rule-compliances",
            "request_type": request.__class__.__name__,
            "response_type": "ListConfigRuleComplianceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'account_id' in local_var_params:
            path_params['account_id'] = local_var_params['account_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_control_violations(self, request):
        """查询不合规信息

        查询组织里所有不合规的资源信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListControlViolations
        :type request: :class:`huaweicloudsdkrgc.v1.ListControlViolationsRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.ListControlViolationsResponse`
        """
        http_info = self._list_control_violations_http_info(request)
        return self._call_api(**http_info)

    def list_control_violations_invoker(self, request):
        http_info = self._list_control_violations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_control_violations_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/governance/control-violations",
            "request_type": request.__class__.__name__,
            "response_type": "ListControlViolationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_id' in local_var_params:
            query_params.append(('account_id', local_var_params['account_id']))
        if 'organization_unit_id' in local_var_params:
            query_params.append(('organization_unit_id', local_var_params['organization_unit_id']))

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_controls(self, request):
        """查询控制策略

        查询RGC服务里所有的预置控制策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListControls
        :type request: :class:`huaweicloudsdkrgc.v1.ListControlsRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.ListControlsResponse`
        """
        http_info = self._list_controls_http_info(request)
        return self._call_api(**http_info)

    def list_controls_invoker(self, request):
        http_info = self._list_controls_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_controls_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/governance/controls",
            "request_type": request.__class__.__name__,
            "response_type": "ListControlsResponse"
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
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_controls_for_account(self, request):
        """查询账号下开启的控制策略

        查询组织里某个账号开启的所有控制策略信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListControlsForAccount
        :type request: :class:`huaweicloudsdkrgc.v1.ListControlsForAccountRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.ListControlsForAccountResponse`
        """
        http_info = self._list_controls_for_account_http_info(request)
        return self._call_api(**http_info)

    def list_controls_for_account_invoker(self, request):
        http_info = self._list_controls_for_account_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_controls_for_account_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/governance/managed-account/{managed_account_id}/controls",
            "request_type": request.__class__.__name__,
            "response_type": "ListControlsForAccountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'managed_account_id' in local_var_params:
            path_params['managed_account_id'] = local_var_params['managed_account_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_controls_for_organization_unit(self, request):
        """查询OU下开启的控制策略

        查询组织里某个OU开启的所有控制策略信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListControlsForOrganizationUnit
        :type request: :class:`huaweicloudsdkrgc.v1.ListControlsForOrganizationUnitRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.ListControlsForOrganizationUnitResponse`
        """
        http_info = self._list_controls_for_organization_unit_http_info(request)
        return self._call_api(**http_info)

    def list_controls_for_organization_unit_invoker(self, request):
        http_info = self._list_controls_for_organization_unit_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_controls_for_organization_unit_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/governance/managed-organization-unit/{managed_organization_unit_id}/controls",
            "request_type": request.__class__.__name__,
            "response_type": "ListControlsForOrganizationUnitResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'managed_organization_unit_id' in local_var_params:
            path_params['managed_organization_unit_id'] = local_var_params['managed_organization_unit_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_drift_details(self, request):
        """查询漂移信息

        查询Landing Zone的所有漂移详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDriftDetails
        :type request: :class:`huaweicloudsdkrgc.v1.ListDriftDetailsRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.ListDriftDetailsResponse`
        """
        http_info = self._list_drift_details_http_info(request)
        return self._call_api(**http_info)

    def list_drift_details_invoker(self, request):
        http_info = self._list_drift_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_drift_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/governance/drift-details",
            "request_type": request.__class__.__name__,
            "response_type": "ListDriftDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_enabled_controls(self, request):
        """查询开启的控制策略

        查询组织里开启的所有控制策略信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEnabledControls
        :type request: :class:`huaweicloudsdkrgc.v1.ListEnabledControlsRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.ListEnabledControlsResponse`
        """
        http_info = self._list_enabled_controls_http_info(request)
        return self._call_api(**http_info)

    def list_enabled_controls_invoker(self, request):
        http_info = self._list_enabled_controls_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_enabled_controls_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/governance/enabled-controls",
            "request_type": request.__class__.__name__,
            "response_type": "ListEnabledControlsResponse"
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
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_compliance_status_for_account(self, request):
        """查询账号的合规状态

        查询组织里某个账号的资源合规状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowComplianceStatusForAccount
        :type request: :class:`huaweicloudsdkrgc.v1.ShowComplianceStatusForAccountRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.ShowComplianceStatusForAccountResponse`
        """
        http_info = self._show_compliance_status_for_account_http_info(request)
        return self._call_api(**http_info)

    def show_compliance_status_for_account_invoker(self, request):
        http_info = self._show_compliance_status_for_account_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_compliance_status_for_account_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/governance/managed-account/{managed_account_id}/compliance-status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowComplianceStatusForAccountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'managed_account_id' in local_var_params:
            path_params['managed_account_id'] = local_var_params['managed_account_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_compliance_status_for_organization_unit(self, request):
        """查询OU的合规状态

        查询组织里某个OU下所有账号的资源合规状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowComplianceStatusForOrganizationUnit
        :type request: :class:`huaweicloudsdkrgc.v1.ShowComplianceStatusForOrganizationUnitRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.ShowComplianceStatusForOrganizationUnitResponse`
        """
        http_info = self._show_compliance_status_for_organization_unit_http_info(request)
        return self._call_api(**http_info)

    def show_compliance_status_for_organization_unit_invoker(self, request):
        http_info = self._show_compliance_status_for_organization_unit_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_compliance_status_for_organization_unit_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/governance/managed-organization-unit/{managed_organization_unit_id}/compliance-status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowComplianceStatusForOrganizationUnitResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'managed_organization_unit_id' in local_var_params:
            path_params['managed_organization_unit_id'] = local_var_params['managed_organization_unit_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_control(self, request):
        """查询控制策略详细信息

        查询单个预置的控制策略详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowControl
        :type request: :class:`huaweicloudsdkrgc.v1.ShowControlRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.ShowControlResponse`
        """
        http_info = self._show_control_http_info(request)
        return self._call_api(**http_info)

    def show_control_invoker(self, request):
        http_info = self._show_control_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_control_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/governance/controls/{control_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowControlResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'control_id' in local_var_params:
            path_params['control_id'] = local_var_params['control_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_control_operate(self, request):
        """查询控制策略操作状态

        根据操作ID查询返回指定ID的操作状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowControlOperate
        :type request: :class:`huaweicloudsdkrgc.v1.ShowControlOperateRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.ShowControlOperateResponse`
        """
        http_info = self._show_control_operate_http_info(request)
        return self._call_api(**http_info)

    def show_control_operate_invoker(self, request):
        http_info = self._show_control_operate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_control_operate_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/governance/operated-controls/{control_operate_request_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowControlOperateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'control_operate_request_id' in local_var_params:
            path_params['control_operate_request_id'] = local_var_params['control_operate_request_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_controls_for_organization_unit(self, request):
        """查询OU开启的控制策略

        查询组织里某个OU下开启的某个控制策略的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowControlsForOrganizationUnit
        :type request: :class:`huaweicloudsdkrgc.v1.ShowControlsForOrganizationUnitRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.ShowControlsForOrganizationUnitResponse`
        """
        http_info = self._show_controls_for_organization_unit_http_info(request)
        return self._call_api(**http_info)

    def show_controls_for_organization_unit_invoker(self, request):
        http_info = self._show_controls_for_organization_unit_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_controls_for_organization_unit_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/governance/managed-organization-unit/{managed_organization_unit_id}/controls/{control_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowControlsForOrganizationUnitResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'managed_organization_unit_id' in local_var_params:
            path_params['managed_organization_unit_id'] = local_var_params['managed_organization_unit_id']
        if 'control_id' in local_var_params:
            path_params['control_id'] = local_var_params['control_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def check_launch(self, request):
        """设置Landing Zone前检查

        在设置Landing Zone之前，检查当前区域是否可以设置Landing Zone。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckLaunch
        :type request: :class:`huaweicloudsdkrgc.v1.CheckLaunchRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.CheckLaunchResponse`
        """
        http_info = self._check_launch_http_info(request)
        return self._call_api(**http_info)

    def check_launch_invoker(self, request):
        http_info = self._check_launch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_launch_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/landing-zone/pre-launch-check",
            "request_type": request.__class__.__name__,
            "response_type": "CheckLaunchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def setup_landing_zone(self, request):
        """设置Landing Zone

        在当前区域创建或者更新Landing Zone。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetupLandingZone
        :type request: :class:`huaweicloudsdkrgc.v1.SetupLandingZoneRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.SetupLandingZoneResponse`
        """
        http_info = self._setup_landing_zone_http_info(request)
        return self._call_api(**http_info)

    def setup_landing_zone_invoker(self, request):
        http_info = self._setup_landing_zone_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _setup_landing_zone_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/landing-zone/setup",
            "request_type": request.__class__.__name__,
            "response_type": "SetupLandingZoneResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_available_updates(self, request):
        """获取Landing Zone可更新状态

        获取Landing Zone当前是否需要升级更新。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAvailableUpdates
        :type request: :class:`huaweicloudsdkrgc.v1.ShowAvailableUpdatesRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.ShowAvailableUpdatesResponse`
        """
        http_info = self._show_available_updates_http_info(request)
        return self._call_api(**http_info)

    def show_available_updates_invoker(self, request):
        http_info = self._show_available_updates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_available_updates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/landing-zone/available-updates",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAvailableUpdatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_home_region(self, request):
        """查询主区域

        查询Landing Zone的主区域。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowHomeRegion
        :type request: :class:`huaweicloudsdkrgc.v1.ShowHomeRegionRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.ShowHomeRegionResponse`
        """
        http_info = self._show_home_region_http_info(request)
        return self._call_api(**http_info)

    def show_home_region_invoker(self, request):
        http_info = self._show_home_region_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_home_region_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/landing-zone/home-region",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHomeRegionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_landing_zone_configuration(self, request):
        """获取Landing Zone的配置

        获取当前客户的Landing Zone的所有配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLandingZoneConfiguration
        :type request: :class:`huaweicloudsdkrgc.v1.ShowLandingZoneConfigurationRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.ShowLandingZoneConfigurationResponse`
        """
        http_info = self._show_landing_zone_configuration_http_info(request)
        return self._call_api(**http_info)

    def show_landing_zone_configuration_invoker(self, request):
        http_info = self._show_landing_zone_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_landing_zone_configuration_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/landing-zone/configuration",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLandingZoneConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_landing_zone_identity_center(self, request):
        """获取当前客户的Identity Center用户信息

        获取当前客户的Identity Center用户信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLandingZoneIdentityCenter
        :type request: :class:`huaweicloudsdkrgc.v1.ShowLandingZoneIdentityCenterRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.ShowLandingZoneIdentityCenterResponse`
        """
        http_info = self._show_landing_zone_identity_center_http_info(request)
        return self._call_api(**http_info)

    def show_landing_zone_identity_center_invoker(self, request):
        http_info = self._show_landing_zone_identity_center_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_landing_zone_identity_center_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/landing-zone/identity-center",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLandingZoneIdentityCenterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_landing_zone_status(self, request):
        """查询Landing Zone设置状态

        查询Landing Zone的设置状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLandingZoneStatus
        :type request: :class:`huaweicloudsdkrgc.v1.ShowLandingZoneStatusRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.ShowLandingZoneStatusResponse`
        """
        http_info = self._show_landing_zone_status_http_info(request)
        return self._call_api(**http_info)

    def show_landing_zone_status_invoker(self, request):
        http_info = self._show_landing_zone_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_landing_zone_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/landing-zone/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLandingZoneStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_account(self, request):
        """创建账号

        在组织里的某个OU下创建账号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAccount
        :type request: :class:`huaweicloudsdkrgc.v1.CreateAccountRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.CreateAccountResponse`
        """
        http_info = self._create_account_http_info(request)
        return self._call_api(**http_info)

    def create_account_invoker(self, request):
        http_info = self._create_account_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_account_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/managed-organization/managed-accounts",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAccountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_managed_organizational_units(self, request):
        """删除注册的OU

        在组织里删除已注册的OU。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteManagedOrganizationalUnits
        :type request: :class:`huaweicloudsdkrgc.v1.DeleteManagedOrganizationalUnitsRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.DeleteManagedOrganizationalUnitsResponse`
        """
        http_info = self._delete_managed_organizational_units_http_info(request)
        return self._call_api(**http_info)

    def delete_managed_organizational_units_invoker(self, request):
        http_info = self._delete_managed_organizational_units_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_managed_organizational_units_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/managed-organization/managed-organization-unit/{managed_organization_unit_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteManagedOrganizationalUnitsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'managed_organization_unit_id' in local_var_params:
            path_params['managed_organization_unit_id'] = local_var_params['managed_organization_unit_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def deregister_organizational_unit(self, request):
        """去注册OU

        将组织里的某个OU从RGC服务里取消注册。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeregisterOrganizationalUnit
        :type request: :class:`huaweicloudsdkrgc.v1.DeregisterOrganizationalUnitRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.DeregisterOrganizationalUnitResponse`
        """
        http_info = self._deregister_organizational_unit_http_info(request)
        return self._call_api(**http_info)

    def deregister_organizational_unit_invoker(self, request):
        http_info = self._deregister_organizational_unit_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _deregister_organizational_unit_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/managed-organization/managed-organization-unit/{managed_organization_unit_id}/de-register",
            "request_type": request.__class__.__name__,
            "response_type": "DeregisterOrganizationalUnitResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'managed_organization_unit_id' in local_var_params:
            path_params['managed_organization_unit_id'] = local_var_params['managed_organization_unit_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_managed_accounts(self, request):
        """查询注册的账号信息

        查询组织里所有注册的账号信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListManagedAccounts
        :type request: :class:`huaweicloudsdkrgc.v1.ListManagedAccountsRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.ListManagedAccountsResponse`
        """
        http_info = self._list_managed_accounts_http_info(request)
        return self._call_api(**http_info)

    def list_managed_accounts_invoker(self, request):
        http_info = self._list_managed_accounts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_managed_accounts_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/managed-organization/managed-accounts",
            "request_type": request.__class__.__name__,
            "response_type": "ListManagedAccountsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'control_id' in local_var_params:
            query_params.append(('control_id', local_var_params['control_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_managed_accounts_for_parent(self, request):
        """查询纳管OU下的账号信息

        查询组织里某个注册OU下的所有账号信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListManagedAccountsForParent
        :type request: :class:`huaweicloudsdkrgc.v1.ListManagedAccountsForParentRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.ListManagedAccountsForParentResponse`
        """
        http_info = self._list_managed_accounts_for_parent_http_info(request)
        return self._call_api(**http_info)

    def list_managed_accounts_for_parent_invoker(self, request):
        http_info = self._list_managed_accounts_for_parent_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_managed_accounts_for_parent_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/managed-organization/managed-organization-unit/{managed_organization_unit_id}/managed-accounts",
            "request_type": request.__class__.__name__,
            "response_type": "ListManagedAccountsForParentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'managed_organization_unit_id' in local_var_params:
            path_params['managed_organization_unit_id'] = local_var_params['managed_organization_unit_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_managed_organizational_units(self, request):
        """查询纳管的OU信息

        查询组织里所有通过RGC服务注册的OU信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListManagedOrganizationalUnits
        :type request: :class:`huaweicloudsdkrgc.v1.ListManagedOrganizationalUnitsRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.ListManagedOrganizationalUnitsResponse`
        """
        http_info = self._list_managed_organizational_units_http_info(request)
        return self._call_api(**http_info)

    def list_managed_organizational_units_invoker(self, request):
        http_info = self._list_managed_organizational_units_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_managed_organizational_units_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/managed-organization/managed-organization-units",
            "request_type": request.__class__.__name__,
            "response_type": "ListManagedOrganizationalUnitsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'control_id' in local_var_params:
            query_params.append(('control_id', local_var_params['control_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def register_organizational_unit(self, request):
        """注册OU

        将组织里的某个OU注册到RGC服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RegisterOrganizationalUnit
        :type request: :class:`huaweicloudsdkrgc.v1.RegisterOrganizationalUnitRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.RegisterOrganizationalUnitResponse`
        """
        http_info = self._register_organizational_unit_http_info(request)
        return self._call_api(**http_info)

    def register_organizational_unit_invoker(self, request):
        http_info = self._register_organizational_unit_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _register_organizational_unit_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/managed-organization/organization-unit/{organization_unit_id}/register",
            "request_type": request.__class__.__name__,
            "response_type": "RegisterOrganizationalUnitResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'organization_unit_id' in local_var_params:
            path_params['organization_unit_id'] = local_var_params['organization_unit_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_managed_account(self, request):
        """查询注册的账号信息

        查询组织里某个注册的账号信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowManagedAccount
        :type request: :class:`huaweicloudsdkrgc.v1.ShowManagedAccountRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.ShowManagedAccountResponse`
        """
        http_info = self._show_managed_account_http_info(request)
        return self._call_api(**http_info)

    def show_managed_account_invoker(self, request):
        http_info = self._show_managed_account_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_managed_account_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/managed-organization/managed-account/{managed_account_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowManagedAccountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'managed_account_id' in local_var_params:
            path_params['managed_account_id'] = local_var_params['managed_account_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_managed_core_account(self, request):
        """查询核心账号

        查询组织里的所有核心账号信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowManagedCoreAccount
        :type request: :class:`huaweicloudsdkrgc.v1.ShowManagedCoreAccountRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.ShowManagedCoreAccountResponse`
        """
        http_info = self._show_managed_core_account_http_info(request)
        return self._call_api(**http_info)

    def show_managed_core_account_invoker(self, request):
        http_info = self._show_managed_core_account_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_managed_core_account_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/managed-organization/managed-core-account",
            "request_type": request.__class__.__name__,
            "response_type": "ShowManagedCoreAccountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_type' in local_var_params:
            query_params.append(('account_type', local_var_params['account_type']))

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_managed_organizational_unit(self, request):
        """查询纳管的OU信息

        查询在RGC服务里注册的OU信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowManagedOrganizationalUnit
        :type request: :class:`huaweicloudsdkrgc.v1.ShowManagedOrganizationalUnitRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.ShowManagedOrganizationalUnitResponse`
        """
        http_info = self._show_managed_organizational_unit_http_info(request)
        return self._call_api(**http_info)

    def show_managed_organizational_unit_invoker(self, request):
        http_info = self._show_managed_organizational_unit_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_managed_organizational_unit_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/managed-organization/managed-organization-unit/{managed_organization_unit_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowManagedOrganizationalUnitResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'managed_organization_unit_id' in local_var_params:
            path_params['managed_organization_unit_id'] = local_var_params['managed_organization_unit_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_operation(self, request):
        """查询注册过程信息

        查询在RGC服务里注册/取消注册的过程信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOperation
        :type request: :class:`huaweicloudsdkrgc.v1.ShowOperationRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.ShowOperationResponse`
        """
        http_info = self._show_operation_http_info(request)
        return self._call_api(**http_info)

    def show_operation_invoker(self, request):
        http_info = self._show_operation_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_operation_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/managed-organization/{operation_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOperationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'operation_id' in local_var_params:
            path_params['operation_id'] = local_var_params['operation_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_managed_account(self, request):
        """更新注册的账号

        更新组织里某个已在RGC服务注册的账号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateManagedAccount
        :type request: :class:`huaweicloudsdkrgc.v1.UpdateManagedAccountRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.UpdateManagedAccountResponse`
        """
        http_info = self._update_managed_account_http_info(request)
        return self._call_api(**http_info)

    def update_managed_account_invoker(self, request):
        http_info = self._update_managed_account_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_managed_account_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/managed-organization/managed-account/{managed_account_id}/update",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateManagedAccountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'managed_account_id' in local_var_params:
            path_params['managed_account_id'] = local_var_params['managed_account_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

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
