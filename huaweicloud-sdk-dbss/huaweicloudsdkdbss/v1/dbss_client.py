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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkdbss'")


class DbssClient(Client):
    def __init__(self):
        super(DbssClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdbss.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "DbssClient":
                raise TypeError("client type error, support client type is DbssClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_audit_agent(self, request):
        r"""添加审计数据库Agent[待下线]

        添加审计数据库Agent
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddAuditAgent
        :type request: :class:`huaweicloudsdkdbss.v1.AddAuditAgentRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.AddAuditAgentResponse`
        """
        warnings.warn("Method 'add_audit_agent' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._add_audit_agent_http_info(request)
        return self._call_api(**http_info)

    def add_audit_agent_invoker(self, request):
        warnings.warn("Method 'add_audit_agent_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._add_audit_agent_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_audit_agent_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{instance_id}/audit/agents",
            "request_type": request.__class__.__name__,
            "response_type": "AddAuditAgentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def add_audit_database(self, request):
        r"""添加自建数据库[待下线]

        添加自建数据库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddAuditDatabase
        :type request: :class:`huaweicloudsdkdbss.v1.AddAuditDatabaseRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.AddAuditDatabaseResponse`
        """
        warnings.warn("Method 'add_audit_database' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._add_audit_database_http_info(request)
        return self._call_api(**http_info)

    def add_audit_database_invoker(self, request):
        warnings.warn("Method 'add_audit_database_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._add_audit_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_audit_database_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{instance_id}/audit/databases",
            "request_type": request.__class__.__name__,
            "response_type": "AddAuditDatabaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def add_audit_database_new(self, request):
        r"""添加自建数据库

        添加自建数据库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddAuditDatabaseNew
        :type request: :class:`huaweicloudsdkdbss.v1.AddAuditDatabaseNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.AddAuditDatabaseNewResponse`
        """
        http_info = self._add_audit_database_new_http_info(request)
        return self._call_api(**http_info)

    def add_audit_database_new_invoker(self, request):
        http_info = self._add_audit_database_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_audit_database_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/audit/{instance_id}/databases",
            "request_type": request.__class__.__name__,
            "response_type": "AddAuditDatabaseNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def add_rds_database(self, request):
        r"""添加RDS数据库[待下线]

        添加RDS数据库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddRdsDatabase
        :type request: :class:`huaweicloudsdkdbss.v1.AddRdsDatabaseRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.AddRdsDatabaseResponse`
        """
        warnings.warn("Method 'add_rds_database' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._add_rds_database_http_info(request)
        return self._call_api(**http_info)

    def add_rds_database_invoker(self, request):
        warnings.warn("Method 'add_rds_database_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._add_rds_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_rds_database_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{instance_id}/audit/databases/rds",
            "request_type": request.__class__.__name__,
            "response_type": "AddRdsDatabaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def add_rds_database_new(self, request):
        r"""添加RDS数据库

        添加RDS数据库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddRdsDatabaseNew
        :type request: :class:`huaweicloudsdkdbss.v1.AddRdsDatabaseNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.AddRdsDatabaseNewResponse`
        """
        http_info = self._add_rds_database_new_http_info(request)
        return self._call_api(**http_info)

    def add_rds_database_new_invoker(self, request):
        http_info = self._add_rds_database_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_rds_database_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/audit/{instance_id}/databases/rds",
            "request_type": request.__class__.__name__,
            "response_type": "AddRdsDatabaseNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def add_rds_no_agent_database(self, request):
        r"""添加RDS数据库[待下线]

        添加RDS数据库。V1版本已不再维护，待下线
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddRdsNoAgentDatabase
        :type request: :class:`huaweicloudsdkdbss.v1.AddRdsNoAgentDatabaseRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.AddRdsNoAgentDatabaseResponse`
        """
        warnings.warn("Method 'add_rds_no_agent_database' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._add_rds_no_agent_database_http_info(request)
        return self._call_api(**http_info)

    def add_rds_no_agent_database_invoker(self, request):
        warnings.warn("Method 'add_rds_no_agent_database_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._add_rds_no_agent_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_rds_no_agent_database_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{instance_id}/dbss/audit/databases/rds",
            "request_type": request.__class__.__name__,
            "response_type": "AddRdsNoAgentDatabaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def batch_set_audit_alarm_log_status(self, request):
        r"""批量标记

        批量标记
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchSetAuditAlarmLogStatus
        :type request: :class:`huaweicloudsdkdbss.v1.BatchSetAuditAlarmLogStatusRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.BatchSetAuditAlarmLogStatusResponse`
        """
        http_info = self._batch_set_audit_alarm_log_status_http_info(request)
        return self._call_api(**http_info)

    def batch_set_audit_alarm_log_status_invoker(self, request):
        http_info = self._batch_set_audit_alarm_log_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_set_audit_alarm_log_status_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/alarm-log/mark",
            "request_type": request.__class__.__name__,
            "response_type": "BatchSetAuditAlarmLogStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def bind_db_encrypt_eip(self, request):
        r"""绑定数据库加密实例的eip

        绑定数据库加密实例的eip
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BindDbEncryptEip
        :type request: :class:`huaweicloudsdkdbss.v1.BindDbEncryptEipRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.BindDbEncryptEipResponse`
        """
        http_info = self._bind_db_encrypt_eip_http_info(request)
        return self._call_api(**http_info)

    def bind_db_encrypt_eip_invoker(self, request):
        http_info = self._bind_db_encrypt_eip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _bind_db_encrypt_eip_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/db-encrypt/{instance_id}/eip/bind",
            "request_type": request.__class__.__name__,
            "response_type": "BindDbEncryptEipResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def bind_db_om_eip(self, request):
        r"""绑定数据库运维实例的eip

        绑定数据库运维实例的eip
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BindDbOmEip
        :type request: :class:`huaweicloudsdkdbss.v1.BindDbOmEipRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.BindDbOmEipResponse`
        """
        http_info = self._bind_db_om_eip_http_info(request)
        return self._call_api(**http_info)

    def bind_db_om_eip_invoker(self, request):
        http_info = self._bind_db_om_eip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _bind_db_om_eip_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/db-om/{instance_id}/eip/bind",
            "request_type": request.__class__.__name__,
            "response_type": "BindDbOmEipResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def change_db_encrypt_security_group(self, request):
        r"""更改数据库加密实例的安全组

        更改数据库加密实例的安全组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeDbEncryptSecurityGroup
        :type request: :class:`huaweicloudsdkdbss.v1.ChangeDbEncryptSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ChangeDbEncryptSecurityGroupResponse`
        """
        http_info = self._change_db_encrypt_security_group_http_info(request)
        return self._call_api(**http_info)

    def change_db_encrypt_security_group_invoker(self, request):
        http_info = self._change_db_encrypt_security_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_db_encrypt_security_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/db-encrypt/{instance_id}/security-group",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeDbEncryptSecurityGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def change_db_om_security_group(self, request):
        r"""更改数据库运维实例的安全组

        更改数据库运维实例的安全组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeDbOmSecurityGroup
        :type request: :class:`huaweicloudsdkdbss.v1.ChangeDbOmSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ChangeDbOmSecurityGroupResponse`
        """
        http_info = self._change_db_om_security_group_http_info(request)
        return self._call_api(**http_info)

    def change_db_om_security_group_invoker(self, request):
        http_info = self._change_db_om_security_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_db_om_security_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/db-om/{instance_id}/security-group",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeDbOmSecurityGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def confirm_upgrade_audit(self, request):
        r"""触发审计实例升级

        触发审计实例升级
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ConfirmUpgradeAudit
        :type request: :class:`huaweicloudsdkdbss.v1.ConfirmUpgradeAuditRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ConfirmUpgradeAuditResponse`
        """
        http_info = self._confirm_upgrade_audit_http_info(request)
        return self._call_api(**http_info)

    def confirm_upgrade_audit_invoker(self, request):
        http_info = self._confirm_upgrade_audit_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _confirm_upgrade_audit_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{resource_id}/upgrade",
            "request_type": request.__class__.__name__,
            "response_type": "ConfirmUpgradeAuditResponse"
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

    def count_db_account_session(self, request):
        r"""查询数据库用户会话分布

        查询数据库用户会话分布
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountDbAccountSession
        :type request: :class:`huaweicloudsdkdbss.v1.CountDbAccountSessionRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.CountDbAccountSessionResponse`
        """
        http_info = self._count_db_account_session_http_info(request)
        return self._call_api(**http_info)

    def count_db_account_session_invoker(self, request):
        http_info = self._count_db_account_session_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _count_db_account_session_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/statistics/session/db-account",
            "request_type": request.__class__.__name__,
            "response_type": "CountDbAccountSessionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def count_db_client_session(self, request):
        r"""查询客户端会话分布

        查询客户端会话分布
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountDbClientSession
        :type request: :class:`huaweicloudsdkdbss.v1.CountDbClientSessionRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.CountDbClientSessionResponse`
        """
        http_info = self._count_db_client_session_http_info(request)
        return self._call_api(**http_info)

    def count_db_client_session_invoker(self, request):
        http_info = self._count_db_client_session_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _count_db_client_session_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/statistics/session/db-client",
            "request_type": request.__class__.__name__,
            "response_type": "CountDbClientSessionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def count_injection_statistics(self, request):
        r"""获取指定时间段内的sql注入分布统计

        获取指定时间段内的sql注入分布统计
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountInjectionStatistics
        :type request: :class:`huaweicloudsdkdbss.v1.CountInjectionStatisticsRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.CountInjectionStatisticsResponse`
        """
        http_info = self._count_injection_statistics_http_info(request)
        return self._call_api(**http_info)

    def count_injection_statistics_invoker(self, request):
        http_info = self._count_injection_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _count_injection_statistics_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/statistics/trend/sql-injection",
            "request_type": request.__class__.__name__,
            "response_type": "CountInjectionStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def count_operation_statistics(self, request):
        r"""获取指定时间段内的风险操作数量分布统计

        获取指定时间段内的风险操作数量分布统计
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountOperationStatistics
        :type request: :class:`huaweicloudsdkdbss.v1.CountOperationStatisticsRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.CountOperationStatisticsResponse`
        """
        http_info = self._count_operation_statistics_http_info(request)
        return self._call_api(**http_info)

    def count_operation_statistics_invoker(self, request):
        http_info = self._count_operation_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _count_operation_statistics_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/statistics/trend/risk-operation",
            "request_type": request.__class__.__name__,
            "response_type": "CountOperationStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def count_risk_trend_statistics(self, request):
        r"""获取指定时间段内的风险分布统计

        获取指定时间段内的风险分布统计
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountRiskTrendStatistics
        :type request: :class:`huaweicloudsdkdbss.v1.CountRiskTrendStatisticsRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.CountRiskTrendStatisticsResponse`
        """
        http_info = self._count_risk_trend_statistics_http_info(request)
        return self._call_api(**http_info)

    def count_risk_trend_statistics_invoker(self, request):
        http_info = self._count_risk_trend_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _count_risk_trend_statistics_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/statistics/trend/risk-level",
            "request_type": request.__class__.__name__,
            "response_type": "CountRiskTrendStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def count_session_statistics(self, request):
        r"""获取指定时间段内的查询会话统计

        获取指定时间段内的查询会话统计
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountSessionStatistics
        :type request: :class:`huaweicloudsdkdbss.v1.CountSessionStatisticsRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.CountSessionStatisticsResponse`
        """
        http_info = self._count_session_statistics_http_info(request)
        return self._call_api(**http_info)

    def count_session_statistics_invoker(self, request):
        http_info = self._count_session_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _count_session_statistics_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/statistics/trend/session",
            "request_type": request.__class__.__name__,
            "response_type": "CountSessionStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def count_sql_statistics(self, request):
        r"""获取指定时间段内的SQL分布统计

        获取指定时间段内的SQL分布统计
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountSqlStatistics
        :type request: :class:`huaweicloudsdkdbss.v1.CountSqlStatisticsRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.CountSqlStatisticsResponse`
        """
        http_info = self._count_sql_statistics_http_info(request)
        return self._call_api(**http_info)

    def count_sql_statistics_invoker(self, request):
        http_info = self._count_sql_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _count_sql_statistics_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/statistics/trend/sql-type",
            "request_type": request.__class__.__name__,
            "response_type": "CountSqlStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def count_sql_trend_statistics(self, request):
        r"""获取指定时间段内的sql数量分布统计

        获取指定时间段内的sql数量分布统计
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountSqlTrendStatistics
        :type request: :class:`huaweicloudsdkdbss.v1.CountSqlTrendStatisticsRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.CountSqlTrendStatisticsResponse`
        """
        http_info = self._count_sql_trend_statistics_http_info(request)
        return self._call_api(**http_info)

    def count_sql_trend_statistics_invoker(self, request):
        http_info = self._count_sql_trend_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _count_sql_trend_statistics_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/statistics/trend/sql-count",
            "request_type": request.__class__.__name__,
            "response_type": "CountSqlTrendStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def create_db_encrypt_instance_period(self, request):
        r"""按包周期方式购买数据库加密实例

        按需方式购买数据库加密实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDbEncryptInstancePeriod
        :type request: :class:`huaweicloudsdkdbss.v1.CreateDbEncryptInstancePeriodRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.CreateDbEncryptInstancePeriodResponse`
        """
        http_info = self._create_db_encrypt_instance_period_http_info(request)
        return self._call_api(**http_info)

    def create_db_encrypt_instance_period_invoker(self, request):
        http_info = self._create_db_encrypt_instance_period_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_db_encrypt_instance_period_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/db-encrypt/charge/period/order",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDbEncryptInstancePeriodResponse"
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

    def create_db_om_instance_period(self, request):
        r"""包周期购买数据库运维实例

        包周期购买数据库运维实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDbOmInstancePeriod
        :type request: :class:`huaweicloudsdkdbss.v1.CreateDbOmInstancePeriodRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.CreateDbOmInstancePeriodResponse`
        """
        http_info = self._create_db_om_instance_period_http_info(request)
        return self._call_api(**http_info)

    def create_db_om_instance_period_invoker(self, request):
        http_info = self._create_db_om_instance_period_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_db_om_instance_period_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/db-om/charge/period/order",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDbOmInstancePeriodResponse"
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

    def create_instances_period_order(self, request):
        r"""包年包月计费模式创建审计实例[待下线]

        包年包月计费模式创建审计实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstancesPeriodOrder
        :type request: :class:`huaweicloudsdkdbss.v1.CreateInstancesPeriodOrderRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.CreateInstancesPeriodOrderResponse`
        """
        warnings.warn("Method 'create_instances_period_order' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._create_instances_period_order_http_info(request)
        return self._call_api(**http_info)

    def create_instances_period_order_invoker(self, request):
        warnings.warn("Method 'create_instances_period_order_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._create_instances_period_order_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_instances_period_order_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/dbss/audit/charge/period/order",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstancesPeriodOrderResponse"
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

    def create_instances_period_order_new(self, request):
        r"""包年包月计费模式创建审计实例

        包年包月计费模式创建审计实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstancesPeriodOrderNew
        :type request: :class:`huaweicloudsdkdbss.v1.CreateInstancesPeriodOrderNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.CreateInstancesPeriodOrderNewResponse`
        """
        http_info = self._create_instances_period_order_new_http_info(request)
        return self._call_api(**http_info)

    def create_instances_period_order_new_invoker(self, request):
        http_info = self._create_instances_period_order_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_instances_period_order_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/audit/charge/period/order",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstancesPeriodOrderNewResponse"
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

    def create_report(self, request):
        r"""立即生成报表

        立即生成报表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateReport
        :type request: :class:`huaweicloudsdkdbss.v1.CreateReportRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.CreateReportResponse`
        """
        http_info = self._create_report_http_info(request)
        return self._call_api(**http_info)

    def create_report_invoker(self, request):
        http_info = self._create_report_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_report_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/reports/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateReportResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def delete_audit_agent(self, request):
        r"""删除数据库Agent[待下线]

        删除数据库Agent
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAuditAgent
        :type request: :class:`huaweicloudsdkdbss.v1.DeleteAuditAgentRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.DeleteAuditAgentResponse`
        """
        warnings.warn("Method 'delete_audit_agent' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._delete_audit_agent_http_info(request)
        return self._call_api(**http_info)

    def delete_audit_agent_invoker(self, request):
        warnings.warn("Method 'delete_audit_agent_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._delete_audit_agent_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_audit_agent_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/{instance_id}/audit/agents/{agent_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAuditAgentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'agent_id' in local_var_params:
            path_params['agent_id'] = local_var_params['agent_id']

        query_params = []
        if 'db_id' in local_var_params:
            query_params.append(('db_id', local_var_params['db_id']))

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

    def delete_audit_alarm_log(self, request):
        r"""删除告警监控记录

        删除告警监控记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAuditAlarmLog
        :type request: :class:`huaweicloudsdkdbss.v1.DeleteAuditAlarmLogRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.DeleteAuditAlarmLogResponse`
        """
        http_info = self._delete_audit_alarm_log_http_info(request)
        return self._call_api(**http_info)

    def delete_audit_alarm_log_invoker(self, request):
        http_info = self._delete_audit_alarm_log_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_audit_alarm_log_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/alarm-log/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAuditAlarmLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
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

    def delete_audit_backup_task(self, request):
        r"""删除指定备份任务

        删除指定备份任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAuditBackupTask
        :type request: :class:`huaweicloudsdkdbss.v1.DeleteAuditBackupTaskRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.DeleteAuditBackupTaskResponse`
        """
        http_info = self._delete_audit_backup_task_http_info(request)
        return self._call_api(**http_info)

    def delete_audit_backup_task_invoker(self, request):
        http_info = self._delete_audit_backup_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_audit_backup_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/backups/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAuditBackupTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
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

    def delete_audit_database(self, request):
        r"""删除数据库[待下线]

        删除数据库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAuditDatabase
        :type request: :class:`huaweicloudsdkdbss.v1.DeleteAuditDatabaseRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.DeleteAuditDatabaseResponse`
        """
        warnings.warn("Method 'delete_audit_database' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._delete_audit_database_http_info(request)
        return self._call_api(**http_info)

    def delete_audit_database_invoker(self, request):
        warnings.warn("Method 'delete_audit_database_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._delete_audit_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_audit_database_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/{instance_id}/audit/databases/{db_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAuditDatabaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'db_id' in local_var_params:
            path_params['db_id'] = local_var_params['db_id']

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

    def delete_audit_database_new(self, request):
        r"""删除数据库

        删除数据库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAuditDatabaseNew
        :type request: :class:`huaweicloudsdkdbss.v1.DeleteAuditDatabaseNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.DeleteAuditDatabaseNewResponse`
        """
        http_info = self._delete_audit_database_new_http_info(request)
        return self._call_api(**http_info)

    def delete_audit_database_new_invoker(self, request):
        http_info = self._delete_audit_database_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_audit_database_new_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/audit/{instance_id}/databases/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAuditDatabaseNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
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

    def delete_audit_report(self, request):
        r"""删除报表

        删除报表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAuditReport
        :type request: :class:`huaweicloudsdkdbss.v1.DeleteAuditReportRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.DeleteAuditReportResponse`
        """
        http_info = self._delete_audit_report_http_info(request)
        return self._call_api(**http_info)

    def delete_audit_report_invoker(self, request):
        http_info = self._delete_audit_report_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_audit_report_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/reports/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAuditReportResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
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

    def delete_db_encrypt_instance(self, request):
        r"""删除数据库加密实例

        删除数据库加密实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDbEncryptInstance
        :type request: :class:`huaweicloudsdkdbss.v1.DeleteDbEncryptInstanceRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.DeleteDbEncryptInstanceResponse`
        """
        http_info = self._delete_db_encrypt_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_db_encrypt_instance_invoker(self, request):
        http_info = self._delete_db_encrypt_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_db_encrypt_instance_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/db-encrypt/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDbEncryptInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def delete_db_om_instance(self, request):
        r"""删除数据库运维实例

        删除数据库运维实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDbOmInstance
        :type request: :class:`huaweicloudsdkdbss.v1.DeleteDbOmInstanceRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.DeleteDbOmInstanceResponse`
        """
        http_info = self._delete_db_om_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_db_om_instance_invoker(self, request):
        http_info = self._delete_db_om_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_db_om_instance_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/db-om/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDbOmInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def delete_instances(self, request):
        r"""删除审计实例[待下线]

        只有按需计费模式实例没有任务时 或 包周期模式实例状态为故障时，才能执行此操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstances
        :type request: :class:`huaweicloudsdkdbss.v1.DeleteInstancesRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.DeleteInstancesResponse`
        """
        warnings.warn("Method 'delete_instances' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._delete_instances_http_info(request)
        return self._call_api(**http_info)

    def delete_instances_invoker(self, request):
        warnings.warn("Method 'delete_instances_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._delete_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_instances_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/dbss/audit/instances",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstancesResponse"
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

    def delete_instances_new(self, request):
        r"""删除审计实例

        只有按需计费模式实例没有任务时 或 包周期模式实例状态为故障时，才能执行此操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstancesNew
        :type request: :class:`huaweicloudsdkdbss.v1.DeleteInstancesNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.DeleteInstancesNewResponse`
        """
        http_info = self._delete_instances_new_http_info(request)
        return self._call_api(**http_info)

    def delete_instances_new_invoker(self, request):
        http_info = self._delete_instances_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_instances_new_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/audit/instance",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstancesNewResponse"
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

    def download_audit_agent(self, request):
        r"""下载审计Agent[待下线]

        下载审计Agent
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadAuditAgent
        :type request: :class:`huaweicloudsdkdbss.v1.DownloadAuditAgentRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.DownloadAuditAgentResponse`
        """
        warnings.warn("Method 'download_audit_agent' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._download_audit_agent_http_info(request)
        return self._call_api(**http_info)

    def download_audit_agent_invoker(self, request):
        warnings.warn("Method 'download_audit_agent_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._download_audit_agent_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_audit_agent_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/{instance_id}/audit/agents/{agent_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadAuditAgentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'agent_id' in local_var_params:
            path_params['agent_id'] = local_var_params['agent_id']

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

    def download_audit_report(self, request):
        r"""下载报表

        下载报表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadAuditReport
        :type request: :class:`huaweicloudsdkdbss.v1.DownloadAuditReportRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.DownloadAuditReportResponse`
        """
        http_info = self._download_audit_report_http_info(request)
        return self._call_api(**http_info)

    def download_audit_report_invoker(self, request):
        http_info = self._download_audit_report_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_audit_report_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/reports/{id}/download",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadAuditReportResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'local' in local_var_params:
            query_params.append(('local', local_var_params['local']))

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

    def list_alarm_topic_config_info(self, request):
        r"""获取实例告警配置[待下线]

        获取实例告警配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarmTopicConfigInfo
        :type request: :class:`huaweicloudsdkdbss.v1.ListAlarmTopicConfigInfoRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAlarmTopicConfigInfoResponse`
        """
        warnings.warn("Method 'list_alarm_topic_config_info' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_alarm_topic_config_info_http_info(request)
        return self._call_api(**http_info)

    def list_alarm_topic_config_info_invoker(self, request):
        warnings.warn("Method 'list_alarm_topic_config_info_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_alarm_topic_config_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_alarm_topic_config_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/{instance_id}/audit/alarm/topic",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlarmTopicConfigInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_alarm_topic_config_info_new(self, request):
        r"""获取实例告警配置

        获取实例告警配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarmTopicConfigInfoNew
        :type request: :class:`huaweicloudsdkdbss.v1.ListAlarmTopicConfigInfoNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAlarmTopicConfigInfoNewResponse`
        """
        http_info = self._list_alarm_topic_config_info_new_http_info(request)
        return self._call_api(**http_info)

    def list_alarm_topic_config_info_new_invoker(self, request):
        http_info = self._list_alarm_topic_config_info_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_alarm_topic_config_info_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/audit/{instance_id}/alarm/topic",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlarmTopicConfigInfoNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_audit_agent(self, request):
        r"""查询数据库Agent列表[待下线]

        查询数据库Agent列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditAgent
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditAgentRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditAgentResponse`
        """
        warnings.warn("Method 'list_audit_agent' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_audit_agent_http_info(request)
        return self._call_api(**http_info)

    def list_audit_agent_invoker(self, request):
        warnings.warn("Method 'list_audit_agent_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_audit_agent_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_agent_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/{instance_id}/audit/agents",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditAgentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'db_id' in local_var_params:
            query_params.append(('db_id', local_var_params['db_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_audit_alarm_log(self, request):
        r"""查询审计告警信息[待下线]

        查询审计告警信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditAlarmLog
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditAlarmLogRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditAlarmLogResponse`
        """
        warnings.warn("Method 'list_audit_alarm_log' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_audit_alarm_log_http_info(request)
        return self._call_api(**http_info)

    def list_audit_alarm_log_invoker(self, request):
        warnings.warn("Method 'list_audit_alarm_log_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_audit_alarm_log_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_alarm_log_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{instance_id}/audit/alarm-log",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditAlarmLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_audit_alarm_log_new(self, request):
        r"""查询审计告警信息

        查询审计告警信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditAlarmLogNew
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditAlarmLogNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditAlarmLogNewResponse`
        """
        http_info = self._list_audit_alarm_log_new_http_info(request)
        return self._call_api(**http_info)

    def list_audit_alarm_log_new_invoker(self, request):
        http_info = self._list_audit_alarm_log_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_alarm_log_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/audit/{instance_id}/alarm-log",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditAlarmLogNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_audit_backup_info(self, request):
        r"""获取所有备份信息

        获取所有备份信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditBackupInfo
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditBackupInfoRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditBackupInfoResponse`
        """
        http_info = self._list_audit_backup_info_http_info(request)
        return self._call_api(**http_info)

    def list_audit_backup_info_invoker(self, request):
        http_info = self._list_audit_backup_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_backup_info_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/audit/{instance_id}/backups",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditBackupInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_audit_backup_risk_templates(self, request):
        r"""获取风险导出配置列表

        获取风险导出配置列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditBackupRiskTemplates
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditBackupRiskTemplatesRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditBackupRiskTemplatesResponse`
        """
        http_info = self._list_audit_backup_risk_templates_http_info(request)
        return self._call_api(**http_info)

    def list_audit_backup_risk_templates_invoker(self, request):
        http_info = self._list_audit_backup_risk_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_backup_risk_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/backup/risk/templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditBackupRiskTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_audit_databases(self, request):
        r"""查询数据库列表[待下线]

        查询数据库列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditDatabases
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditDatabasesRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditDatabasesResponse`
        """
        warnings.warn("Method 'list_audit_databases' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_audit_databases_http_info(request)
        return self._call_api(**http_info)

    def list_audit_databases_invoker(self, request):
        warnings.warn("Method 'list_audit_databases_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_audit_databases_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_databases_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/{instance_id}/dbss/audit/databases",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditDatabasesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_audit_databases_new(self, request):
        r"""查询数据库列表

        查询数据库列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditDatabasesNew
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditDatabasesNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditDatabasesNewResponse`
        """
        http_info = self._list_audit_databases_new_http_info(request)
        return self._call_api(**http_info)

    def list_audit_databases_new_invoker(self, request):
        http_info = self._list_audit_databases_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_databases_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/audit/{instance_id}/databases",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditDatabasesNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_audit_instance_jobs(self, request):
        r"""查询实例创建任务信息[待下线]

        查询实例创建任务信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditInstanceJobs
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditInstanceJobsRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditInstanceJobsResponse`
        """
        warnings.warn("Method 'list_audit_instance_jobs' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_audit_instance_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_audit_instance_jobs_invoker(self, request):
        warnings.warn("Method 'list_audit_instance_jobs_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_audit_instance_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_instance_jobs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dbss/audit/jobs/{resource_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditInstanceJobsResponse"
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

    def list_audit_instance_jobs_new(self, request):
        r"""查询实例创建任务信息

        查询实例创建任务信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditInstanceJobsNew
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditInstanceJobsNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditInstanceJobsNewResponse`
        """
        http_info = self._list_audit_instance_jobs_new_http_info(request)
        return self._call_api(**http_info)

    def list_audit_instance_jobs_new_invoker(self, request):
        http_info = self._list_audit_instance_jobs_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_instance_jobs_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/audit/{resource_id}/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditInstanceJobsNewResponse"
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

    def list_audit_instances(self, request):
        r"""查询审计实例列表[待下线]

        查询审计实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditInstances
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditInstancesRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditInstancesResponse`
        """
        warnings.warn("Method 'list_audit_instances' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_audit_instances_http_info(request)
        return self._call_api(**http_info)

    def list_audit_instances_invoker(self, request):
        warnings.warn("Method 'list_audit_instances_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_audit_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dbss/audit/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_audit_instances_new(self, request):
        r"""查询审计实例列表

        查询审计实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditInstancesNew
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditInstancesNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditInstancesNewResponse`
        """
        http_info = self._list_audit_instances_new_http_info(request)
        return self._call_api(**http_info)

    def list_audit_instances_new_invoker(self, request):
        http_info = self._list_audit_instances_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_instances_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/audit/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditInstancesNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_audit_obs_buckets(self, request):
        r"""备份或风险导出时，选择obs桶

        备份或风险导出时，选择obs桶
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditObsBuckets
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditObsBucketsRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditObsBucketsResponse`
        """
        http_info = self._list_audit_obs_buckets_http_info(request)
        return self._call_api(**http_info)

    def list_audit_obs_buckets_invoker(self, request):
        http_info = self._list_audit_obs_buckets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_obs_buckets_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/audit/backup/obs-buckets",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditObsBucketsResponse"
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

    def list_audit_operate_logs(self, request):
        r"""查询用户操作日志信息[待下线]

        查询用户操作日志信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditOperateLogs
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditOperateLogsRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditOperateLogsResponse`
        """
        warnings.warn("Method 'list_audit_operate_logs' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_audit_operate_logs_http_info(request)
        return self._call_api(**http_info)

    def list_audit_operate_logs_invoker(self, request):
        warnings.warn("Method 'list_audit_operate_logs_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_audit_operate_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_operate_logs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{instance_id}/dbss/audit/operate-log",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditOperateLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_audit_operate_logs_new(self, request):
        r"""查询用户操作日志信息

        查询用户操作日志信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditOperateLogsNew
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditOperateLogsNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditOperateLogsNewResponse`
        """
        http_info = self._list_audit_operate_logs_new_http_info(request)
        return self._call_api(**http_info)

    def list_audit_operate_logs_new_invoker(self, request):
        http_info = self._list_audit_operate_logs_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_operate_logs_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/operation-log",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditOperateLogsNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_audit_report_templates(self, request):
        r"""获取报表模板

        获取报表模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditReportTemplates
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditReportTemplatesRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditReportTemplatesResponse`
        """
        http_info = self._list_audit_report_templates_http_info(request)
        return self._call_api(**http_info)

    def list_audit_report_templates_invoker(self, request):
        http_info = self._list_audit_report_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_report_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/audit/{instance_id}/reports/templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditReportTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_audit_reports(self, request):
        r"""查询报表

        查询报表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditReports
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditReportsRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditReportsResponse`
        """
        http_info = self._list_audit_reports_http_info(request)
        return self._call_api(**http_info)

    def list_audit_reports_invoker(self, request):
        http_info = self._list_audit_reports_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_reports_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/reports/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditReportsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_audit_rule_risks(self, request):
        r"""查询风险规则策略[待下线]

        查询风险规则策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditRuleRisks
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditRuleRisksRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditRuleRisksResponse`
        """
        warnings.warn("Method 'list_audit_rule_risks' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_audit_rule_risks_http_info(request)
        return self._call_api(**http_info)

    def list_audit_rule_risks_invoker(self, request):
        warnings.warn("Method 'list_audit_rule_risks_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_audit_rule_risks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_rule_risks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/{instance_id}/dbss/audit/rule/risk",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditRuleRisksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'risk_levels' in local_var_params:
            query_params.append(('risk_levels', local_var_params['risk_levels']))

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

    def list_audit_rule_scopes(self, request):
        r"""查询审计范围策略列表[待下线]

        查询审计范围策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditRuleScopes
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditRuleScopesRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditRuleScopesResponse`
        """
        warnings.warn("Method 'list_audit_rule_scopes' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_audit_rule_scopes_http_info(request)
        return self._call_api(**http_info)

    def list_audit_rule_scopes_invoker(self, request):
        warnings.warn("Method 'list_audit_rule_scopes_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_audit_rule_scopes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_rule_scopes_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/{instance_id}/dbss/audit/rule/scopes",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditRuleScopesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_audit_sensitive_masks(self, request):
        r"""查询隐私数据脱敏规则[待下线]

        查询隐私数据脱敏规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditSensitiveMasks
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditSensitiveMasksRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditSensitiveMasksResponse`
        """
        warnings.warn("Method 'list_audit_sensitive_masks' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_audit_sensitive_masks_http_info(request)
        return self._call_api(**http_info)

    def list_audit_sensitive_masks_invoker(self, request):
        warnings.warn("Method 'list_audit_sensitive_masks_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_audit_sensitive_masks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_sensitive_masks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/{instance_id}/dbss/audit/sensitive/masks",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditSensitiveMasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_audit_sqls(self, request):
        r"""查询审计SQL语句[待下线]

        查询审计SQL语句
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditSqls
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditSqlsRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditSqlsResponse`
        """
        warnings.warn("Method 'list_audit_sqls' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_audit_sqls_http_info(request)
        return self._call_api(**http_info)

    def list_audit_sqls_invoker(self, request):
        warnings.warn("Method 'list_audit_sqls_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_audit_sqls_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_sqls_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{instance_id}/audit/sqls",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditSqlsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_audit_sqls_new(self, request):
        r"""查询审计SQL语句

        查询审计SQL语句
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditSqlsNew
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditSqlsNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditSqlsNewResponse`
        """
        http_info = self._list_audit_sqls_new_http_info(request)
        return self._call_api(**http_info)

    def list_audit_sqls_new_invoker(self, request):
        http_info = self._list_audit_sqls_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_sqls_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/audit/{instance_id}/sqls",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditSqlsNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_audit_summary_infos(self, request):
        r"""查询审计汇总信息

        查询审计汇总信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditSummaryInfos
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditSummaryInfosRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditSummaryInfosResponse`
        """
        http_info = self._list_audit_summary_infos_http_info(request)
        return self._call_api(**http_info)

    def list_audit_summary_infos_invoker(self, request):
        http_info = self._list_audit_summary_infos_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_summary_infos_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/audit/summary/info",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditSummaryInfosResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_audit_trend_history(self, request):
        r"""查询趋势历史数据

        查询趋势历史数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditTrendHistory
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditTrendHistoryRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditTrendHistoryResponse`
        """
        http_info = self._list_audit_trend_history_http_info(request)
        return self._call_api(**http_info)

    def list_audit_trend_history_invoker(self, request):
        http_info = self._list_audit_trend_history_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_trend_history_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/audit/{instance_id}/statistics/trend/history",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditTrendHistoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_availability_zone_infos(self, request):
        r"""查询可用区信息[待下线]

        查询可用区信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAvailabilityZoneInfos
        :type request: :class:`huaweicloudsdkdbss.v1.ListAvailabilityZoneInfosRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAvailabilityZoneInfosResponse`
        """
        warnings.warn("Method 'list_availability_zone_infos' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_availability_zone_infos_http_info(request)
        return self._call_api(**http_info)

    def list_availability_zone_infos_invoker(self, request):
        warnings.warn("Method 'list_availability_zone_infos_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_availability_zone_infos_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_availability_zone_infos_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/dbss/audit/availability-zone",
            "request_type": request.__class__.__name__,
            "response_type": "ListAvailabilityZoneInfosResponse"
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

    def list_availability_zone_infos_new(self, request):
        r"""查询可用区信息

        查询可用区信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAvailabilityZoneInfosNew
        :type request: :class:`huaweicloudsdkdbss.v1.ListAvailabilityZoneInfosNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAvailabilityZoneInfosNewResponse`
        """
        http_info = self._list_availability_zone_infos_new_http_info(request)
        return self._call_api(**http_info)

    def list_availability_zone_infos_new_invoker(self, request):
        http_info = self._list_availability_zone_infos_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_availability_zone_infos_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/availability-zone",
            "request_type": request.__class__.__name__,
            "response_type": "ListAvailabilityZoneInfosNewResponse"
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

    def list_db_encrypt_instances(self, request):
        r"""列举数据库加密实例

        列举数据库加密实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDbEncryptInstances
        :type request: :class:`huaweicloudsdkdbss.v1.ListDbEncryptInstancesRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListDbEncryptInstancesResponse`
        """
        http_info = self._list_db_encrypt_instances_http_info(request)
        return self._call_api(**http_info)

    def list_db_encrypt_instances_invoker(self, request):
        http_info = self._list_db_encrypt_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_db_encrypt_instances_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/db-encrypt/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListDbEncryptInstancesResponse"
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

    def list_ecs_specification(self, request):
        r"""查询ECS服务器规格信息[待下线]

        查询ECS服务器规格信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEcsSpecification
        :type request: :class:`huaweicloudsdkdbss.v1.ListEcsSpecificationRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListEcsSpecificationResponse`
        """
        warnings.warn("Method 'list_ecs_specification' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_ecs_specification_http_info(request)
        return self._call_api(**http_info)

    def list_ecs_specification_invoker(self, request):
        warnings.warn("Method 'list_ecs_specification_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_ecs_specification_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ecs_specification_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dbss/audit/specification",
            "request_type": request.__class__.__name__,
            "response_type": "ListEcsSpecificationResponse"
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

    def list_ecs_specification_new(self, request):
        r"""查询ECS服务器规格信息

        查询ECS服务器规格信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEcsSpecificationNew
        :type request: :class:`huaweicloudsdkdbss.v1.ListEcsSpecificationNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListEcsSpecificationNewResponse`
        """
        http_info = self._list_ecs_specification_new_http_info(request)
        return self._call_api(**http_info)

    def list_ecs_specification_new_invoker(self, request):
        http_info = self._list_ecs_specification_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ecs_specification_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/audit/specification",
            "request_type": request.__class__.__name__,
            "response_type": "ListEcsSpecificationNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'image_business_type' in local_var_params:
            query_params.append(('image_business_type', local_var_params['image_business_type']))

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

    def list_instances(self, request):
        r"""获取数据库运维集群实例

        获取数据库运维集群实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstances
        :type request: :class:`huaweicloudsdkdbss.v1.ListInstancesRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListInstancesResponse`
        """
        http_info = self._list_instances_http_info(request)
        return self._call_api(**http_info)

    def list_instances_invoker(self, request):
        http_info = self._list_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instances_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/db-om/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstancesResponse"
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

    def list_rds_databases(self, request):
        r"""查询RDS数据库列表

        查询RDS数据库列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRdsDatabases
        :type request: :class:`huaweicloudsdkdbss.v1.ListRdsDatabasesRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListRdsDatabasesResponse`
        """
        http_info = self._list_rds_databases_http_info(request)
        return self._call_api(**http_info)

    def list_rds_databases_invoker(self, request):
        http_info = self._list_rds_databases_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_rds_databases_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/audit/databases/rds",
            "request_type": request.__class__.__name__,
            "response_type": "ListRdsDatabasesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'db_type' in local_var_params:
            query_params.append(('db_type', local_var_params['db_type']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_sql_injection_rules(self, request):
        r"""查询SQL注入规则策略[待下线]

        查询SQL注入规则策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSqlInjectionRules
        :type request: :class:`huaweicloudsdkdbss.v1.ListSqlInjectionRulesRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListSqlInjectionRulesResponse`
        """
        warnings.warn("Method 'list_sql_injection_rules' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_sql_injection_rules_http_info(request)
        return self._call_api(**http_info)

    def list_sql_injection_rules_invoker(self, request):
        warnings.warn("Method 'list_sql_injection_rules_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_sql_injection_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sql_injection_rules_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{instance_id}/dbss/audit/rule/sql-injections",
            "request_type": request.__class__.__name__,
            "response_type": "ListSqlInjectionRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def reboot_audit_instance(self, request):
        r"""重启审计实例[待下线]

        重启审计实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RebootAuditInstance
        :type request: :class:`huaweicloudsdkdbss.v1.RebootAuditInstanceRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.RebootAuditInstanceResponse`
        """
        warnings.warn("Method 'reboot_audit_instance' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._reboot_audit_instance_http_info(request)
        return self._call_api(**http_info)

    def reboot_audit_instance_invoker(self, request):
        warnings.warn("Method 'reboot_audit_instance_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._reboot_audit_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reboot_audit_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dbss/audit/instance/reboot",
            "request_type": request.__class__.__name__,
            "response_type": "RebootAuditInstanceResponse"
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

    def reboot_audit_instance_new(self, request):
        r"""重启审计实例

        重启审计实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RebootAuditInstanceNew
        :type request: :class:`huaweicloudsdkdbss.v1.RebootAuditInstanceNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.RebootAuditInstanceNewResponse`
        """
        http_info = self._reboot_audit_instance_new_http_info(request)
        return self._call_api(**http_info)

    def reboot_audit_instance_new_invoker(self, request):
        http_info = self._reboot_audit_instance_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reboot_audit_instance_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/instance/reboot",
            "request_type": request.__class__.__name__,
            "response_type": "RebootAuditInstanceNewResponse"
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

    def reboot_db_encrypt_instance(self, request):
        r"""重启数据库加密实例

        重启数据库加密实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RebootDbEncryptInstance
        :type request: :class:`huaweicloudsdkdbss.v1.RebootDbEncryptInstanceRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.RebootDbEncryptInstanceResponse`
        """
        http_info = self._reboot_db_encrypt_instance_http_info(request)
        return self._call_api(**http_info)

    def reboot_db_encrypt_instance_invoker(self, request):
        http_info = self._reboot_db_encrypt_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reboot_db_encrypt_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/db-encrypt/{instance_id}/reboot",
            "request_type": request.__class__.__name__,
            "response_type": "RebootDbEncryptInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def reboot_db_om_instance(self, request):
        r"""重启数据库运维实例

        重启数据库运维实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RebootDbOmInstance
        :type request: :class:`huaweicloudsdkdbss.v1.RebootDbOmInstanceRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.RebootDbOmInstanceResponse`
        """
        http_info = self._reboot_db_om_instance_http_info(request)
        return self._call_api(**http_info)

    def reboot_db_om_instance_invoker(self, request):
        http_info = self._reboot_db_om_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reboot_db_om_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/db-om/{instance_id}/reboot",
            "request_type": request.__class__.__name__,
            "response_type": "RebootDbOmInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def reset_db_encrypt_password(self, request):
        r"""重置数据库加密实例的密码

        重置数据库加密实例的密码
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetDbEncryptPassword
        :type request: :class:`huaweicloudsdkdbss.v1.ResetDbEncryptPasswordRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ResetDbEncryptPasswordResponse`
        """
        http_info = self._reset_db_encrypt_password_http_info(request)
        return self._call_api(**http_info)

    def reset_db_encrypt_password_invoker(self, request):
        http_info = self._reset_db_encrypt_password_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_db_encrypt_password_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/db-encrypt/{instance_id}/password/reset",
            "request_type": request.__class__.__name__,
            "response_type": "ResetDbEncryptPasswordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def reset_db_om_password(self, request):
        r"""重置数据库运维实例的密码

        重置数据库运维实例的密码
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetDbOmPassword
        :type request: :class:`huaweicloudsdkdbss.v1.ResetDbOmPasswordRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ResetDbOmPasswordResponse`
        """
        http_info = self._reset_db_om_password_http_info(request)
        return self._call_api(**http_info)

    def reset_db_om_password_invoker(self, request):
        http_info = self._reset_db_om_password_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_db_om_password_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/db-om/{instance_id}/password/reset",
            "request_type": request.__class__.__name__,
            "response_type": "ResetDbOmPasswordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def restore_audit_backup(self, request):
        r"""恢复备份信息

        恢复备份信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestoreAuditBackup
        :type request: :class:`huaweicloudsdkdbss.v1.RestoreAuditBackupRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.RestoreAuditBackupResponse`
        """
        http_info = self._restore_audit_backup_http_info(request)
        return self._call_api(**http_info)

    def restore_audit_backup_invoker(self, request):
        http_info = self._restore_audit_backup_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restore_audit_backup_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/backup/{id}/restore",
            "request_type": request.__class__.__name__,
            "response_type": "RestoreAuditBackupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
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

    def retry_audit_backup_task(self, request):
        r"""重试备份任务

        重试备份任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RetryAuditBackupTask
        :type request: :class:`huaweicloudsdkdbss.v1.RetryAuditBackupTaskRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.RetryAuditBackupTaskResponse`
        """
        http_info = self._retry_audit_backup_task_http_info(request)
        return self._call_api(**http_info)

    def retry_audit_backup_task_invoker(self, request):
        http_info = self._retry_audit_backup_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _retry_audit_backup_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/backup/{id}/retry",
            "request_type": request.__class__.__name__,
            "response_type": "RetryAuditBackupTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
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

    def set_alarm_topic_config_info(self, request):
        r"""设置实例告警配置[待下线]

        设置实例告警配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetAlarmTopicConfigInfo
        :type request: :class:`huaweicloudsdkdbss.v1.SetAlarmTopicConfigInfoRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.SetAlarmTopicConfigInfoResponse`
        """
        warnings.warn("Method 'set_alarm_topic_config_info' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._set_alarm_topic_config_info_http_info(request)
        return self._call_api(**http_info)

    def set_alarm_topic_config_info_invoker(self, request):
        warnings.warn("Method 'set_alarm_topic_config_info_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._set_alarm_topic_config_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_alarm_topic_config_info_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{instance_id}/audit/alarm/topic",
            "request_type": request.__class__.__name__,
            "response_type": "SetAlarmTopicConfigInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def set_alarm_topic_config_info_new(self, request):
        r"""设置实例告警配置

        设置实例告警配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetAlarmTopicConfigInfoNew
        :type request: :class:`huaweicloudsdkdbss.v1.SetAlarmTopicConfigInfoNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.SetAlarmTopicConfigInfoNewResponse`
        """
        http_info = self._set_alarm_topic_config_info_new_http_info(request)
        return self._call_api(**http_info)

    def set_alarm_topic_config_info_new_invoker(self, request):
        http_info = self._set_alarm_topic_config_info_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_alarm_topic_config_info_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/audit/{instance_id}/alarm/topic",
            "request_type": request.__class__.__name__,
            "response_type": "SetAlarmTopicConfigInfoNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def set_audit_alarm_log_status(self, request):
        r"""标记监控告警

        标记监控告警
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetAuditAlarmLogStatus
        :type request: :class:`huaweicloudsdkdbss.v1.SetAuditAlarmLogStatusRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.SetAuditAlarmLogStatusResponse`
        """
        http_info = self._set_audit_alarm_log_status_http_info(request)
        return self._call_api(**http_info)

    def set_audit_alarm_log_status_invoker(self, request):
        http_info = self._set_audit_alarm_log_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_audit_alarm_log_status_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/alarm-log/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "SetAuditAlarmLogStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
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

    def set_audit_auto_backup_template(self, request):
        r"""获取备份配置信息

        设置备份配置信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetAuditAutoBackupTemplate
        :type request: :class:`huaweicloudsdkdbss.v1.SetAuditAutoBackupTemplateRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.SetAuditAutoBackupTemplateResponse`
        """
        http_info = self._set_audit_auto_backup_template_http_info(request)
        return self._call_api(**http_info)

    def set_audit_auto_backup_template_invoker(self, request):
        http_info = self._set_audit_auto_backup_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_audit_auto_backup_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/backup/template",
            "request_type": request.__class__.__name__,
            "response_type": "SetAuditAutoBackupTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def set_audit_backup_risk_switch(self, request):
        r"""风险导出开关(按DomainId)

        风险导出开关(按DomainId)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetAuditBackupRiskSwitch
        :type request: :class:`huaweicloudsdkdbss.v1.SetAuditBackupRiskSwitchRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.SetAuditBackupRiskSwitchResponse`
        """
        http_info = self._set_audit_backup_risk_switch_http_info(request)
        return self._call_api(**http_info)

    def set_audit_backup_risk_switch_invoker(self, request):
        http_info = self._set_audit_backup_risk_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_audit_backup_risk_switch_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/audit/{instance_id}/backup/risk/switch",
            "request_type": request.__class__.__name__,
            "response_type": "SetAuditBackupRiskSwitchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def set_audit_backup_switch(self, request):
        r"""开启/关闭备份

        开启/关闭备份
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetAuditBackupSwitch
        :type request: :class:`huaweicloudsdkdbss.v1.SetAuditBackupSwitchRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.SetAuditBackupSwitchResponse`
        """
        http_info = self._set_audit_backup_switch_http_info(request)
        return self._call_api(**http_info)

    def set_audit_backup_switch_invoker(self, request):
        http_info = self._set_audit_backup_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_audit_backup_switch_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/audit/{instance_id}/backup/switch",
            "request_type": request.__class__.__name__,
            "response_type": "SetAuditBackupSwitchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def set_audit_instance_time_zone(self, request):
        r"""配置审计实例时区信息

        配置审计实例时区信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetAuditInstanceTimeZone
        :type request: :class:`huaweicloudsdkdbss.v1.SetAuditInstanceTimeZoneRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.SetAuditInstanceTimeZoneResponse`
        """
        http_info = self._set_audit_instance_time_zone_http_info(request)
        return self._call_api(**http_info)

    def set_audit_instance_time_zone_invoker(self, request):
        http_info = self._set_audit_instance_time_zone_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_audit_instance_time_zone_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/timezone",
            "request_type": request.__class__.__name__,
            "response_type": "SetAuditInstanceTimeZoneResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def show_audit_back_risk_template(self, request):
        r"""获取单个风险导出配置

        获取单个风险导出配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAuditBackRiskTemplate
        :type request: :class:`huaweicloudsdkdbss.v1.ShowAuditBackRiskTemplateRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ShowAuditBackRiskTemplateResponse`
        """
        http_info = self._show_audit_back_risk_template_http_info(request)
        return self._call_api(**http_info)

    def show_audit_back_risk_template_invoker(self, request):
        http_info = self._show_audit_back_risk_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_audit_back_risk_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/backup/risk/template/{db_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuditBackRiskTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'db_id' in local_var_params:
            path_params['db_id'] = local_var_params['db_id']

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

    def show_audit_backup_status(self, request):
        r"""获取备份状态

        获取备份状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAuditBackupStatus
        :type request: :class:`huaweicloudsdkdbss.v1.ShowAuditBackupStatusRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ShowAuditBackupStatusResponse`
        """
        http_info = self._show_audit_backup_status_http_info(request)
        return self._call_api(**http_info)

    def show_audit_backup_status_invoker(self, request):
        http_info = self._show_audit_backup_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_audit_backup_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/backup/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuditBackupStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def show_audit_quota(self, request):
        r"""查询账户配额信息[待下线]

        查询账户配额信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAuditQuota
        :type request: :class:`huaweicloudsdkdbss.v1.ShowAuditQuotaRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ShowAuditQuotaResponse`
        """
        warnings.warn("Method 'show_audit_quota' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_audit_quota_http_info(request)
        return self._call_api(**http_info)

    def show_audit_quota_invoker(self, request):
        warnings.warn("Method 'show_audit_quota_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_audit_quota_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_audit_quota_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dbss/audit/quota",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuditQuotaResponse"
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

    def show_audit_quota_new(self, request):
        r"""查询账户配额信息

        查询账户配额信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAuditQuotaNew
        :type request: :class:`huaweicloudsdkdbss.v1.ShowAuditQuotaNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ShowAuditQuotaNewResponse`
        """
        http_info = self._show_audit_quota_new_http_info(request)
        return self._call_api(**http_info)

    def show_audit_quota_new_invoker(self, request):
        http_info = self._show_audit_quota_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_audit_quota_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/audit/quota",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuditQuotaNewResponse"
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

    def show_audit_rule_risk(self, request):
        r"""查询指定风险规则策略[待下线]

        查询指定风险规则策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAuditRuleRisk
        :type request: :class:`huaweicloudsdkdbss.v1.ShowAuditRuleRiskRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ShowAuditRuleRiskResponse`
        """
        warnings.warn("Method 'show_audit_rule_risk' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_audit_rule_risk_http_info(request)
        return self._call_api(**http_info)

    def show_audit_rule_risk_invoker(self, request):
        warnings.warn("Method 'show_audit_rule_risk_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_audit_rule_risk_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_audit_rule_risk_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/{instance_id}/dbss/audit/rule/risk/{risk_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuditRuleRiskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'risk_id' in local_var_params:
            path_params['risk_id'] = local_var_params['risk_id']

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

    def show_audit_statistics(self, request):
        r"""获取租户下所有实例的风险汇总信息

        获取租户下所有实例的风险汇总信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAuditStatistics
        :type request: :class:`huaweicloudsdkdbss.v1.ShowAuditStatisticsRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ShowAuditStatisticsResponse`
        """
        http_info = self._show_audit_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_audit_statistics_invoker(self, request):
        http_info = self._show_audit_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_audit_statistics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/audit/summary/risk/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuditStatisticsResponse"
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

    def show_audit_task_status(self, request):
        r"""获取租户审计信息汇总任务状态

        获取租户审计信息汇总任务状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAuditTaskStatus
        :type request: :class:`huaweicloudsdkdbss.v1.ShowAuditTaskStatusRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ShowAuditTaskStatusResponse`
        """
        http_info = self._show_audit_task_status_http_info(request)
        return self._call_api(**http_info)

    def show_audit_task_status_invoker(self, request):
        http_info = self._show_audit_task_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_audit_task_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/audit/summary/{busi_type}/task-status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuditTaskStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'busi_type' in local_var_params:
            path_params['busi_type'] = local_var_params['busi_type']

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

    def show_audit_topic_report_scheduler_config(self, request):
        r"""获取报表的计划任务配置信息（topic方式）

        获取报表的计划任务配置信息（topic方式）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAuditTopicReportSchedulerConfig
        :type request: :class:`huaweicloudsdkdbss.v1.ShowAuditTopicReportSchedulerConfigRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ShowAuditTopicReportSchedulerConfigResponse`
        """
        http_info = self._show_audit_topic_report_scheduler_config_http_info(request)
        return self._call_api(**http_info)

    def show_audit_topic_report_scheduler_config_invoker(self, request):
        http_info = self._show_audit_topic_report_scheduler_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_audit_topic_report_scheduler_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/audit/{instance_id}/reports/tasks/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuditTopicReportSchedulerConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
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

    def show_audit_upgrade_status(self, request):
        r"""查询租户的实例是否可升级

        查询租户的实例是否可升级
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAuditUpgradeStatus
        :type request: :class:`huaweicloudsdkdbss.v1.ShowAuditUpgradeStatusRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ShowAuditUpgradeStatusResponse`
        """
        http_info = self._show_audit_upgrade_status_http_info(request)
        return self._call_api(**http_info)

    def show_audit_upgrade_status_invoker(self, request):
        http_info = self._show_audit_upgrade_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_audit_upgrade_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/audit/upgrade/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuditUpgradeStatusResponse"
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

    def show_backup_risk_bucket_path(self, request):
        r"""获取风险导出桶名和路径

        获取风险导出桶名和路径
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBackupRiskBucketPath
        :type request: :class:`huaweicloudsdkdbss.v1.ShowBackupRiskBucketPathRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ShowBackupRiskBucketPathResponse`
        """
        http_info = self._show_backup_risk_bucket_path_http_info(request)
        return self._call_api(**http_info)

    def show_backup_risk_bucket_path_invoker(self, request):
        http_info = self._show_backup_risk_bucket_path_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_backup_risk_bucket_path_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/backup/risk/bucket-path",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBackupRiskBucketPathResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def show_instance_monitor_info(self, request):
        r"""获取实例监控数据

        获取实例监控数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceMonitorInfo
        :type request: :class:`huaweicloudsdkdbss.v1.ShowInstanceMonitorInfoRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ShowInstanceMonitorInfoResponse`
        """
        http_info = self._show_instance_monitor_info_http_info(request)
        return self._call_api(**http_info)

    def show_instance_monitor_info_invoker(self, request):
        http_info = self._show_instance_monitor_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_monitor_info_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/system/monitorinfo",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceMonitorInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def show_instance_quota(self, request):
        r"""查询加密/运维增强配额

        查询加密/运维增强配额
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceQuota
        :type request: :class:`huaweicloudsdkdbss.v1.ShowInstanceQuotaRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ShowInstanceQuotaResponse`
        """
        http_info = self._show_instance_quota_http_info(request)
        return self._call_api(**http_info)

    def show_instance_quota_invoker(self, request):
        http_info = self._show_instance_quota_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_quota_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instance/quota",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceQuotaResponse"
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

    def show_server_version(self, request):
        r"""获取管理侧版本信息

        获取管理侧版本信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowServerVersion
        :type request: :class:`huaweicloudsdkdbss.v1.ShowServerVersionRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ShowServerVersionResponse`
        """
        http_info = self._show_server_version_http_info(request)
        return self._call_api(**http_info)

    def show_server_version_invoker(self, request):
        http_info = self._show_server_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_server_version_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/version",
            "request_type": request.__class__.__name__,
            "response_type": "ShowServerVersionResponse"
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

    def show_sql_detail(self, request):
        r"""获取指定SQL语句的详细信息

        获取指定SQL语句的详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSqlDetail
        :type request: :class:`huaweicloudsdkdbss.v1.ShowSqlDetailRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ShowSqlDetailResponse`
        """
        http_info = self._show_sql_detail_http_info(request)
        return self._call_api(**http_info)

    def show_sql_detail_invoker(self, request):
        http_info = self._show_sql_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sql_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/audit/{instance_id}/sqls/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSqlDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
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

    def start_audit_instance(self, request):
        r"""开启审计实例[待下线]

        开启审计实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartAuditInstance
        :type request: :class:`huaweicloudsdkdbss.v1.StartAuditInstanceRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.StartAuditInstanceResponse`
        """
        warnings.warn("Method 'start_audit_instance' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._start_audit_instance_http_info(request)
        return self._call_api(**http_info)

    def start_audit_instance_invoker(self, request):
        warnings.warn("Method 'start_audit_instance_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._start_audit_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_audit_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dbss/audit/instance/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartAuditInstanceResponse"
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

    def start_audit_instance_new(self, request):
        r"""开启审计实例

        开启审计实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartAuditInstanceNew
        :type request: :class:`huaweicloudsdkdbss.v1.StartAuditInstanceNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.StartAuditInstanceNewResponse`
        """
        http_info = self._start_audit_instance_new_http_info(request)
        return self._call_api(**http_info)

    def start_audit_instance_new_invoker(self, request):
        http_info = self._start_audit_instance_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_audit_instance_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/instance/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartAuditInstanceNewResponse"
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

    def start_db_encrypt_instance(self, request):
        r"""启动数据库加密实例

        启动数据库加密实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartDbEncryptInstance
        :type request: :class:`huaweicloudsdkdbss.v1.StartDbEncryptInstanceRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.StartDbEncryptInstanceResponse`
        """
        http_info = self._start_db_encrypt_instance_http_info(request)
        return self._call_api(**http_info)

    def start_db_encrypt_instance_invoker(self, request):
        http_info = self._start_db_encrypt_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_db_encrypt_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/db-encrypt/{instance_id}/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartDbEncryptInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def start_db_om_instance(self, request):
        r"""启动数据库运维实例

        启动数据库运维实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartDbOmInstance
        :type request: :class:`huaweicloudsdkdbss.v1.StartDbOmInstanceRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.StartDbOmInstanceResponse`
        """
        http_info = self._start_db_om_instance_http_info(request)
        return self._call_api(**http_info)

    def start_db_om_instance_invoker(self, request):
        http_info = self._start_db_om_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_db_om_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/db-om/{instance_id}/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartDbOmInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def stop_audit_instance(self, request):
        r"""关闭审计实例[待下线]

        关闭审计实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopAuditInstance
        :type request: :class:`huaweicloudsdkdbss.v1.StopAuditInstanceRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.StopAuditInstanceResponse`
        """
        warnings.warn("Method 'stop_audit_instance' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._stop_audit_instance_http_info(request)
        return self._call_api(**http_info)

    def stop_audit_instance_invoker(self, request):
        warnings.warn("Method 'stop_audit_instance_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._stop_audit_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_audit_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dbss/audit/instance/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopAuditInstanceResponse"
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

    def stop_audit_instance_new(self, request):
        r"""关闭审计实例

        关闭审计实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopAuditInstanceNew
        :type request: :class:`huaweicloudsdkdbss.v1.StopAuditInstanceNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.StopAuditInstanceNewResponse`
        """
        http_info = self._stop_audit_instance_new_http_info(request)
        return self._call_api(**http_info)

    def stop_audit_instance_new_invoker(self, request):
        http_info = self._stop_audit_instance_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_audit_instance_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/instance/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopAuditInstanceNewResponse"
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

    def stop_db_encrypt_instance(self, request):
        r"""停止数据库加密实例

        停止数据库加密实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopDbEncryptInstance
        :type request: :class:`huaweicloudsdkdbss.v1.StopDbEncryptInstanceRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.StopDbEncryptInstanceResponse`
        """
        http_info = self._stop_db_encrypt_instance_http_info(request)
        return self._call_api(**http_info)

    def stop_db_encrypt_instance_invoker(self, request):
        http_info = self._stop_db_encrypt_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_db_encrypt_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/db-encrypt/{instance_id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopDbEncryptInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def stop_db_om_instance(self, request):
        r"""停止数据库运维实例

        停止数据库运维实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopDbOmInstance
        :type request: :class:`huaweicloudsdkdbss.v1.StopDbOmInstanceRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.StopDbOmInstanceResponse`
        """
        http_info = self._stop_db_om_instance_http_info(request)
        return self._call_api(**http_info)

    def stop_db_om_instance_invoker(self, request):
        http_info = self._stop_db_om_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_db_om_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/db-om/{instance_id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopDbOmInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def switch_agent(self, request):
        r"""开启关闭Agent[待下线]

        用于开启和关闭Agent审计的功能，当开启后，开始抓取用户的访问信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchAgent
        :type request: :class:`huaweicloudsdkdbss.v1.SwitchAgentRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.SwitchAgentResponse`
        """
        warnings.warn("Method 'switch_agent' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._switch_agent_http_info(request)
        return self._call_api(**http_info)

    def switch_agent_invoker(self, request):
        warnings.warn("Method 'switch_agent_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._switch_agent_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_agent_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{instance_id}/audit/agent/switch",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchAgentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def switch_audit_database(self, request):
        r"""开启关闭数据库[待下线]

        开启关闭数据库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchAuditDatabase
        :type request: :class:`huaweicloudsdkdbss.v1.SwitchAuditDatabaseRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.SwitchAuditDatabaseResponse`
        """
        warnings.warn("Method 'switch_audit_database' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._switch_audit_database_http_info(request)
        return self._call_api(**http_info)

    def switch_audit_database_invoker(self, request):
        warnings.warn("Method 'switch_audit_database_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._switch_audit_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_audit_database_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{instance_id}/audit/databases/switch",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchAuditDatabaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def switch_audit_database_new(self, request):
        r"""开启关闭数据库

        开启关闭数据库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchAuditDatabaseNew
        :type request: :class:`huaweicloudsdkdbss.v1.SwitchAuditDatabaseNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.SwitchAuditDatabaseNewResponse`
        """
        http_info = self._switch_audit_database_new_http_info(request)
        return self._call_api(**http_info)

    def switch_audit_database_new_invoker(self, request):
        http_info = self._switch_audit_database_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_audit_database_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/audit/{instance_id}/databases/switch",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchAuditDatabaseNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def switch_risk_rule(self, request):
        r"""开启关闭风险规则[待下线]

        开启关闭风险规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchRiskRule
        :type request: :class:`huaweicloudsdkdbss.v1.SwitchRiskRuleRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.SwitchRiskRuleResponse`
        """
        warnings.warn("Method 'switch_risk_rule' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._switch_risk_rule_http_info(request)
        return self._call_api(**http_info)

    def switch_risk_rule_invoker(self, request):
        warnings.warn("Method 'switch_risk_rule_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._switch_risk_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_risk_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{instance_id}/audit/rule/risk/switch",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchRiskRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def unbind_db_encrypt_eip(self, request):
        r"""解绑数据库加密实例的eip

        解绑数据库加密实例的eip
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UnbindDbEncryptEip
        :type request: :class:`huaweicloudsdkdbss.v1.UnbindDbEncryptEipRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.UnbindDbEncryptEipResponse`
        """
        http_info = self._unbind_db_encrypt_eip_http_info(request)
        return self._call_api(**http_info)

    def unbind_db_encrypt_eip_invoker(self, request):
        http_info = self._unbind_db_encrypt_eip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _unbind_db_encrypt_eip_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/db-encrypt/{instance_id}/eip/unbind",
            "request_type": request.__class__.__name__,
            "response_type": "UnbindDbEncryptEipResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def unbind_db_om_eip(self, request):
        r"""解绑数据库运维实例的eip

        解绑数据库运维实例的eip
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UnbindDbOmEip
        :type request: :class:`huaweicloudsdkdbss.v1.UnbindDbOmEipRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.UnbindDbOmEipResponse`
        """
        http_info = self._unbind_db_om_eip_http_info(request)
        return self._call_api(**http_info)

    def unbind_db_om_eip_invoker(self, request):
        http_info = self._unbind_db_om_eip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _unbind_db_om_eip_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/db-om/{instance_id}/eip/unbind",
            "request_type": request.__class__.__name__,
            "response_type": "UnbindDbOmEipResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def update_audit_instance(self, request):
        r"""更新审计实例信息[待下线]

        更新审计实例信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAuditInstance
        :type request: :class:`huaweicloudsdkdbss.v1.UpdateAuditInstanceRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.UpdateAuditInstanceResponse`
        """
        warnings.warn("Method 'update_audit_instance' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_audit_instance_http_info(request)
        return self._call_api(**http_info)

    def update_audit_instance_invoker(self, request):
        warnings.warn("Method 'update_audit_instance_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_audit_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_audit_instance_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/dbss/audit/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAuditInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def update_audit_instance_new(self, request):
        r"""更新审计实例信息

        更新审计实例信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAuditInstanceNew
        :type request: :class:`huaweicloudsdkdbss.v1.UpdateAuditInstanceNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.UpdateAuditInstanceNewResponse`
        """
        http_info = self._update_audit_instance_new_http_info(request)
        return self._call_api(**http_info)

    def update_audit_instance_new_invoker(self, request):
        http_info = self._update_audit_instance_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_audit_instance_new_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/audit/instance/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAuditInstanceNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def update_audit_risk_bucket_path(self, request):
        r"""修改风险导出桶名和路径(按DomainId)

        修改风险导出桶名和路径(按DomainId)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAuditRiskBucketPath
        :type request: :class:`huaweicloudsdkdbss.v1.UpdateAuditRiskBucketPathRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.UpdateAuditRiskBucketPathResponse`
        """
        http_info = self._update_audit_risk_bucket_path_http_info(request)
        return self._call_api(**http_info)

    def update_audit_risk_bucket_path_invoker(self, request):
        http_info = self._update_audit_risk_bucket_path_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_audit_risk_bucket_path_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/audit/{instance_id}/backup/risk/global/bucket-path",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAuditRiskBucketPathResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def update_audit_security_group(self, request):
        r"""修改实例安全组[待下线]

        修改实例安全组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAuditSecurityGroup
        :type request: :class:`huaweicloudsdkdbss.v1.UpdateAuditSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.UpdateAuditSecurityGroupResponse`
        """
        warnings.warn("Method 'update_audit_security_group' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_audit_security_group_http_info(request)
        return self._call_api(**http_info)

    def update_audit_security_group_invoker(self, request):
        warnings.warn("Method 'update_audit_security_group_invoker' of DbssClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_audit_security_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_audit_security_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dbss/audit/security-group",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAuditSecurityGroupResponse"
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

    def update_audit_security_group_new(self, request):
        r"""修改实例安全组

        修改实例安全组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAuditSecurityGroupNew
        :type request: :class:`huaweicloudsdkdbss.v1.UpdateAuditSecurityGroupNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.UpdateAuditSecurityGroupNewResponse`
        """
        http_info = self._update_audit_security_group_new_http_info(request)
        return self._call_api(**http_info)

    def update_audit_security_group_new_invoker(self, request):
        http_info = self._update_audit_security_group_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_audit_security_group_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/security-group",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAuditSecurityGroupNewResponse"
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

    def update_audit_task_status(self, request):
        r"""更新租户审计信息汇总任务状态

        更新租户审计信息汇总任务状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAuditTaskStatus
        :type request: :class:`huaweicloudsdkdbss.v1.UpdateAuditTaskStatusRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.UpdateAuditTaskStatusResponse`
        """
        http_info = self._update_audit_task_status_http_info(request)
        return self._call_api(**http_info)

    def update_audit_task_status_invoker(self, request):
        http_info = self._update_audit_task_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_audit_task_status_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/summary/{busi_type}/task-status",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAuditTaskStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'busi_type' in local_var_params:
            path_params['busi_type'] = local_var_params['busi_type']

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

    def update_audit_topic_report_scheduler_config(self, request):
        r"""更改报表的计划任务配置信息（topic方式）

        更改报表的计划任务配置信息（topic方式）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAuditTopicReportSchedulerConfig
        :type request: :class:`huaweicloudsdkdbss.v1.UpdateAuditTopicReportSchedulerConfigRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.UpdateAuditTopicReportSchedulerConfigResponse`
        """
        http_info = self._update_audit_topic_report_scheduler_config_http_info(request)
        return self._call_api(**http_info)

    def update_audit_topic_report_scheduler_config_invoker(self, request):
        http_info = self._update_audit_topic_report_scheduler_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_audit_topic_report_scheduler_config_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/reports/task",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAuditTopicReportSchedulerConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def update_db_encrypt_instance_name(self, request):
        r"""更改数据库加密实例的名称

        更改数据库加密实例的名称
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDbEncryptInstanceName
        :type request: :class:`huaweicloudsdkdbss.v1.UpdateDbEncryptInstanceNameRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.UpdateDbEncryptInstanceNameResponse`
        """
        http_info = self._update_db_encrypt_instance_name_http_info(request)
        return self._call_api(**http_info)

    def update_db_encrypt_instance_name_invoker(self, request):
        http_info = self._update_db_encrypt_instance_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_db_encrypt_instance_name_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/db-encrypt/{instance_id}/name",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDbEncryptInstanceNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def update_db_om_instance_name(self, request):
        r"""更改数据库运维实例的名称

        更改数据库运维实例的名称
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDbOmInstanceName
        :type request: :class:`huaweicloudsdkdbss.v1.UpdateDbOmInstanceNameRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.UpdateDbOmInstanceNameResponse`
        """
        http_info = self._update_db_om_instance_name_http_info(request)
        return self._call_api(**http_info)

    def update_db_om_instance_name_invoker(self, request):
        http_info = self._update_db_om_instance_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_db_om_instance_name_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/db-om/{instance_id}/name",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDbOmInstanceNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def upload_audit_db_config(self, request):
        r"""往OBS导出审计数据库配置

        往OBS导出审计数据库配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadAuditDbConfig
        :type request: :class:`huaweicloudsdkdbss.v1.UploadAuditDbConfigRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.UploadAuditDbConfigResponse`
        """
        http_info = self._upload_audit_db_config_http_info(request)
        return self._call_api(**http_info)

    def upload_audit_db_config_invoker(self, request):
        http_info = self._upload_audit_db_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upload_audit_db_config_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/databases/configs/obs-upload",
            "request_type": request.__class__.__name__,
            "response_type": "UploadAuditDbConfigResponse"
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

    def add_audit_agent_new(self, request):
        r"""添加审计数据库Agent

        添加审计数据库Agent
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddAuditAgentNew
        :type request: :class:`huaweicloudsdkdbss.v1.AddAuditAgentNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.AddAuditAgentNewResponse`
        """
        http_info = self._add_audit_agent_new_http_info(request)
        return self._call_api(**http_info)

    def add_audit_agent_new_invoker(self, request):
        http_info = self._add_audit_agent_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_audit_agent_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/audit/{instance_id}/agents",
            "request_type": request.__class__.__name__,
            "response_type": "AddAuditAgentNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def create_audit_db_agent(self, request):
        r"""指定agent_id方式添加agent

        指定agent_id方式添加agent
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAuditDbAgent
        :type request: :class:`huaweicloudsdkdbss.v1.CreateAuditDbAgentRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.CreateAuditDbAgentResponse`
        """
        http_info = self._create_audit_db_agent_http_info(request)
        return self._call_api(**http_info)

    def create_audit_db_agent_invoker(self, request):
        http_info = self._create_audit_db_agent_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_audit_db_agent_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/audit/{instance_id}/agents/{agent_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAuditDbAgentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'agent_id' in local_var_params:
            path_params['agent_id'] = local_var_params['agent_id']

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

    def delete_audit_agent_new(self, request):
        r"""删除数据库Agent

        删除数据库Agent
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAuditAgentNew
        :type request: :class:`huaweicloudsdkdbss.v1.DeleteAuditAgentNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.DeleteAuditAgentNewResponse`
        """
        http_info = self._delete_audit_agent_new_http_info(request)
        return self._call_api(**http_info)

    def delete_audit_agent_new_invoker(self, request):
        http_info = self._delete_audit_agent_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_audit_agent_new_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/audit/{instance_id}/agents/{agent_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAuditAgentNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'agent_id' in local_var_params:
            path_params['agent_id'] = local_var_params['agent_id']

        query_params = []
        if 'db_id' in local_var_params:
            query_params.append(('db_id', local_var_params['db_id']))

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

    def download_audit_agent_new(self, request):
        r"""下载审计Agent

        下载审计Agent
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadAuditAgentNew
        :type request: :class:`huaweicloudsdkdbss.v1.DownloadAuditAgentNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.DownloadAuditAgentNewResponse`
        """
        http_info = self._download_audit_agent_new_http_info(request)
        return self._call_api(**http_info)

    def download_audit_agent_new_invoker(self, request):
        http_info = self._download_audit_agent_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_audit_agent_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/audit/{instance_id}/agents/{agent_id}/download",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadAuditAgentNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'agent_id' in local_var_params:
            path_params['agent_id'] = local_var_params['agent_id']

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

    def list_audit_agent_new(self, request):
        r"""查询数据库Agent列表

        查询数据库Agent列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditAgentNew
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditAgentNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditAgentNewResponse`
        """
        http_info = self._list_audit_agent_new_http_info(request)
        return self._call_api(**http_info)

    def list_audit_agent_new_invoker(self, request):
        http_info = self._list_audit_agent_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_agent_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/audit/{instance_id}/agents",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditAgentNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'db_id' in local_var_params:
            query_params.append(('db_id', local_var_params['db_id']))

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

    def switch_agent_new(self, request):
        r"""开启/关闭Agent

        用于开启和关闭Agent审计的功能，当开启后，开始抓取用户的访问信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchAgentNew
        :type request: :class:`huaweicloudsdkdbss.v1.SwitchAgentNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.SwitchAgentNewResponse`
        """
        http_info = self._switch_agent_new_http_info(request)
        return self._call_api(**http_info)

    def switch_agent_new_invoker(self, request):
        http_info = self._switch_agent_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_agent_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/audit/{instance_id}/agent/switch",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchAgentNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def batch_add_audit_whitelist(self, request):
        r"""批量添加白名单

        批量添加白名单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchAddAuditWhitelist
        :type request: :class:`huaweicloudsdkdbss.v1.BatchAddAuditWhitelistRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.BatchAddAuditWhitelistResponse`
        """
        http_info = self._batch_add_audit_whitelist_http_info(request)
        return self._call_api(**http_info)

    def batch_add_audit_whitelist_invoker(self, request):
        http_info = self._batch_add_audit_whitelist_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_add_audit_whitelist_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/whitelists",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAddAuditWhitelistResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def delete_audit_whitelist(self, request):
        r"""批量删除白名单

        批量删除白名单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAuditWhitelist
        :type request: :class:`huaweicloudsdkdbss.v1.DeleteAuditWhitelistRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.DeleteAuditWhitelistResponse`
        """
        http_info = self._delete_audit_whitelist_http_info(request)
        return self._call_api(**http_info)

    def delete_audit_whitelist_invoker(self, request):
        http_info = self._delete_audit_whitelist_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_audit_whitelist_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/whitelists/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAuditWhitelistResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_whitelists(self, request):
        r"""查询白名单列表

        查询白名单列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWhitelists
        :type request: :class:`huaweicloudsdkdbss.v1.ListWhitelistsRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListWhitelistsResponse`
        """
        http_info = self._list_whitelists_http_info(request)
        return self._call_api(**http_info)

    def list_whitelists_invoker(self, request):
        http_info = self._list_whitelists_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_whitelists_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/whitelists",
            "request_type": request.__class__.__name__,
            "response_type": "ListWhitelistsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def update_audit_whitelist(self, request):
        r"""修改白名单

        修改白名单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAuditWhitelist
        :type request: :class:`huaweicloudsdkdbss.v1.UpdateAuditWhitelistRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.UpdateAuditWhitelistResponse`
        """
        http_info = self._update_audit_whitelist_http_info(request)
        return self._call_api(**http_info)

    def update_audit_whitelist_invoker(self, request):
        http_info = self._update_audit_whitelist_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_audit_whitelist_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/whitelists/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAuditWhitelistResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
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

    def batch_add_resource_tag(self, request):
        r"""批量添加资源标签

        批量添加资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchAddResourceTag
        :type request: :class:`huaweicloudsdkdbss.v1.BatchAddResourceTagRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.BatchAddResourceTagResponse`
        """
        http_info = self._batch_add_resource_tag_http_info(request)
        return self._call_api(**http_info)

    def batch_add_resource_tag_invoker(self, request):
        http_info = self._batch_add_resource_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_add_resource_tag_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{resource_type}/{resource_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAddResourceTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
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

    def batch_delete_resource_tag(self, request):
        r"""批量删除资源标签

        批量删除资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteResourceTag
        :type request: :class:`huaweicloudsdkdbss.v1.BatchDeleteResourceTagRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.BatchDeleteResourceTagResponse`
        """
        http_info = self._batch_delete_resource_tag_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_resource_tag_invoker(self, request):
        http_info = self._batch_delete_resource_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_resource_tag_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/{resource_type}/{resource_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteResourceTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
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

    def count_resource_instance_by_tag(self, request):
        r"""根据标签查询资源实例数量

        根据标签查询资源实例数量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountResourceInstanceByTag
        :type request: :class:`huaweicloudsdkdbss.v1.CountResourceInstanceByTagRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.CountResourceInstanceByTagResponse`
        """
        http_info = self._count_resource_instance_by_tag_http_info(request)
        return self._call_api(**http_info)

    def count_resource_instance_by_tag_invoker(self, request):
        http_info = self._count_resource_instance_by_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _count_resource_instance_by_tag_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{resource_type}/resource-instances/count",
            "request_type": request.__class__.__name__,
            "response_type": "CountResourceInstanceByTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def list_audit_tags(self, request):
        r"""获取实例标签

        获取实例标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditTags
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditTagsRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditTagsResponse`
        """
        http_info = self._list_audit_tags_http_info(request)
        return self._call_api(**http_info)

    def list_audit_tags_invoker(self, request):
        http_info = self._list_audit_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/{resource_type}/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
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

    def list_project_resource_tags(self, request):
        r"""查询项目标签

        查询项目标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectResourceTags
        :type request: :class:`huaweicloudsdkdbss.v1.ListProjectResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListProjectResourceTagsResponse`
        """
        http_info = self._list_project_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def list_project_resource_tags_invoker(self, request):
        http_info = self._list_project_resource_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_project_resource_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/{resource_type}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectResourceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def list_resource_instance_by_tag(self, request):
        r"""根据标签查询资源实例列表

        根据标签查询资源实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceInstanceByTag
        :type request: :class:`huaweicloudsdkdbss.v1.ListResourceInstanceByTagRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListResourceInstanceByTagResponse`
        """
        http_info = self._list_resource_instance_by_tag_http_info(request)
        return self._call_api(**http_info)

    def list_resource_instance_by_tag_invoker(self, request):
        http_info = self._list_resource_instance_by_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_resource_instance_by_tag_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{resource_type}/resource-instances/filter",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceInstanceByTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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

    def batch_delete_audit_scope(self, request):
        r"""审计范围规则操作-删除策略

        审计范围规则操作-删除策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteAuditScope
        :type request: :class:`huaweicloudsdkdbss.v1.BatchDeleteAuditScopeRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.BatchDeleteAuditScopeResponse`
        """
        http_info = self._batch_delete_audit_scope_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_audit_scope_invoker(self, request):
        http_info = self._batch_delete_audit_scope_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_audit_scope_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/rule/scopes/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteAuditScopeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def create_audit_risk_rule(self, request):
        r"""添加风险规则

        添加风险规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAuditRiskRule
        :type request: :class:`huaweicloudsdkdbss.v1.CreateAuditRiskRuleRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.CreateAuditRiskRuleResponse`
        """
        http_info = self._create_audit_risk_rule_http_info(request)
        return self._call_api(**http_info)

    def create_audit_risk_rule_invoker(self, request):
        http_info = self._create_audit_risk_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_audit_risk_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/rule/risk",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAuditRiskRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def create_audit_scope_rule(self, request):
        r"""添加审计范围策略

        添加审计范围策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAuditScopeRule
        :type request: :class:`huaweicloudsdkdbss.v1.CreateAuditScopeRuleRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.CreateAuditScopeRuleResponse`
        """
        http_info = self._create_audit_scope_rule_http_info(request)
        return self._call_api(**http_info)

    def create_audit_scope_rule_invoker(self, request):
        http_info = self._create_audit_scope_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_audit_scope_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/rule/scopes",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAuditScopeRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def create_sensitive_mask_rule(self, request):
        r"""增加隐私数据脱敏规则

        增加隐私数据脱敏规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSensitiveMaskRule
        :type request: :class:`huaweicloudsdkdbss.v1.CreateSensitiveMaskRuleRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.CreateSensitiveMaskRuleResponse`
        """
        http_info = self._create_sensitive_mask_rule_http_info(request)
        return self._call_api(**http_info)

    def create_sensitive_mask_rule_invoker(self, request):
        http_info = self._create_sensitive_mask_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_sensitive_mask_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/sensitive/mask/rule",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSensitiveMaskRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def delete_audit_rule_risk(self, request):
        r"""删除风险策略

        删除风险策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAuditRuleRisk
        :type request: :class:`huaweicloudsdkdbss.v1.DeleteAuditRuleRiskRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.DeleteAuditRuleRiskResponse`
        """
        http_info = self._delete_audit_rule_risk_http_info(request)
        return self._call_api(**http_info)

    def delete_audit_rule_risk_invoker(self, request):
        http_info = self._delete_audit_rule_risk_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_audit_rule_risk_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/rule/risk/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAuditRuleRiskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
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

    def delete_audit_scope(self, request):
        r"""删除审计范围策略

        删除审计范围策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAuditScope
        :type request: :class:`huaweicloudsdkdbss.v1.DeleteAuditScopeRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.DeleteAuditScopeResponse`
        """
        http_info = self._delete_audit_scope_http_info(request)
        return self._call_api(**http_info)

    def delete_audit_scope_invoker(self, request):
        http_info = self._delete_audit_scope_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_audit_scope_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/rule/scopes/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAuditScopeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
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

    def delete_sensitive_rules(self, request):
        r"""删除隐私数据脱敏规则

        删除隐私数据脱敏规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSensitiveRules
        :type request: :class:`huaweicloudsdkdbss.v1.DeleteSensitiveRulesRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.DeleteSensitiveRulesResponse`
        """
        http_info = self._delete_sensitive_rules_http_info(request)
        return self._call_api(**http_info)

    def delete_sensitive_rules_invoker(self, request):
        http_info = self._delete_sensitive_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_sensitive_rules_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/sensitive/mask/rule/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSensitiveRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
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

    def list_audit_rule_risks_new(self, request):
        r"""查询风险规则策略

        查询风险规则策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditRuleRisksNew
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditRuleRisksNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditRuleRisksNewResponse`
        """
        http_info = self._list_audit_rule_risks_new_http_info(request)
        return self._call_api(**http_info)

    def list_audit_rule_risks_new_invoker(self, request):
        http_info = self._list_audit_rule_risks_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_rule_risks_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/rule/risk",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditRuleRisksNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'risk_levels' in local_var_params:
            query_params.append(('risk_levels', local_var_params['risk_levels']))
        if 'support_db_classify_rule' in local_var_params:
            query_params.append(('support_db_classify_rule', local_var_params['support_db_classify_rule']))

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

    def list_audit_rule_scopes_new(self, request):
        r"""查询审计范围策略列表

        查询审计范围策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditRuleScopesNew
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditRuleScopesNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditRuleScopesNewResponse`
        """
        http_info = self._list_audit_rule_scopes_new_http_info(request)
        return self._call_api(**http_info)

    def list_audit_rule_scopes_new_invoker(self, request):
        http_info = self._list_audit_rule_scopes_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_rule_scopes_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/rule/scopes",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditRuleScopesNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_audit_sensitive_masks_new(self, request):
        r"""查询隐私数据脱敏规则

        查询隐私数据脱敏规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditSensitiveMasksNew
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditSensitiveMasksNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditSensitiveMasksNewResponse`
        """
        http_info = self._list_audit_sensitive_masks_new_http_info(request)
        return self._call_api(**http_info)

    def list_audit_sensitive_masks_new_invoker(self, request):
        http_info = self._list_audit_sensitive_masks_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_sensitive_masks_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/sensitive/mask/rule",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditSensitiveMasksNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def set_audit_scope_rule_switch(self, request):
        r"""启用禁用策略

        启用禁用策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetAuditScopeRuleSwitch
        :type request: :class:`huaweicloudsdkdbss.v1.SetAuditScopeRuleSwitchRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.SetAuditScopeRuleSwitchResponse`
        """
        http_info = self._set_audit_scope_rule_switch_http_info(request)
        return self._call_api(**http_info)

    def set_audit_scope_rule_switch_invoker(self, request):
        http_info = self._set_audit_scope_rule_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_audit_scope_rule_switch_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/audit/{instance_id}/rule/scopes/switch",
            "request_type": request.__class__.__name__,
            "response_type": "SetAuditScopeRuleSwitchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def set_risk_operation_policy(self, request):
        r"""编辑风险操作策略

        编辑风险操作策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetRiskOperationPolicy
        :type request: :class:`huaweicloudsdkdbss.v1.SetRiskOperationPolicyRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.SetRiskOperationPolicyResponse`
        """
        http_info = self._set_risk_operation_policy_http_info(request)
        return self._call_api(**http_info)

    def set_risk_operation_policy_invoker(self, request):
        http_info = self._set_risk_operation_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_risk_operation_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/audit/{instance_id}/rule/risk/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "SetRiskOperationPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
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

    def set_risk_rule_rank(self, request):
        r"""审计实例风险规则排序

        审计实例风险规则排序
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetRiskRuleRank
        :type request: :class:`huaweicloudsdkdbss.v1.SetRiskRuleRankRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.SetRiskRuleRankResponse`
        """
        http_info = self._set_risk_rule_rank_http_info(request)
        return self._call_api(**http_info)

    def set_risk_rule_rank_invoker(self, request):
        http_info = self._set_risk_rule_rank_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_risk_rule_rank_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/audit/{instance_id}/rule/risk/rank",
            "request_type": request.__class__.__name__,
            "response_type": "SetRiskRuleRankResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def set_sensitive_mask_rule_switch(self, request):
        r"""启用禁用单条隐私数据脱敏规则

        启用禁用隐私数据脱敏规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetSensitiveMaskRuleSwitch
        :type request: :class:`huaweicloudsdkdbss.v1.SetSensitiveMaskRuleSwitchRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.SetSensitiveMaskRuleSwitchResponse`
        """
        http_info = self._set_sensitive_mask_rule_switch_http_info(request)
        return self._call_api(**http_info)

    def set_sensitive_mask_rule_switch_invoker(self, request):
        http_info = self._set_sensitive_mask_rule_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_sensitive_mask_rule_switch_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/audit/{instance_id}/sensitive/mask/rule/switch",
            "request_type": request.__class__.__name__,
            "response_type": "SetSensitiveMaskRuleSwitchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def set_sensitive_result_switch(self, request):
        r"""开启关闭结果集存储

        开启关闭结果集存储
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetSensitiveResultSwitch
        :type request: :class:`huaweicloudsdkdbss.v1.SetSensitiveResultSwitchRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.SetSensitiveResultSwitchResponse`
        """
        http_info = self._set_sensitive_result_switch_http_info(request)
        return self._call_api(**http_info)

    def set_sensitive_result_switch_invoker(self, request):
        http_info = self._set_sensitive_result_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_sensitive_result_switch_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/sensitive/result/switch",
            "request_type": request.__class__.__name__,
            "response_type": "SetSensitiveResultSwitchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def set_sensitive_switch(self, request):
        r"""开启关闭隐私数据脱敏功能

        开启关闭隐私数据脱敏
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetSensitiveSwitch
        :type request: :class:`huaweicloudsdkdbss.v1.SetSensitiveSwitchRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.SetSensitiveSwitchResponse`
        """
        http_info = self._set_sensitive_switch_http_info(request)
        return self._call_api(**http_info)

    def set_sensitive_switch_invoker(self, request):
        http_info = self._set_sensitive_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_sensitive_switch_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/sensitive/mask/switch",
            "request_type": request.__class__.__name__,
            "response_type": "SetSensitiveSwitchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def show_audit_rule_risk_new(self, request):
        r"""查询指定风险规则策略

        查询指定风险规则策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAuditRuleRiskNew
        :type request: :class:`huaweicloudsdkdbss.v1.ShowAuditRuleRiskNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ShowAuditRuleRiskNewResponse`
        """
        http_info = self._show_audit_rule_risk_new_http_info(request)
        return self._call_api(**http_info)

    def show_audit_rule_risk_new_invoker(self, request):
        http_info = self._show_audit_rule_risk_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_audit_rule_risk_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/audit/{instance_id}/rule/risk/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuditRuleRiskNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
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

    def show_sensitive_mask_switch(self, request):
        r"""获取隐私数据脱敏开关

        获取隐私数据脱敏开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSensitiveMaskSwitch
        :type request: :class:`huaweicloudsdkdbss.v1.ShowSensitiveMaskSwitchRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ShowSensitiveMaskSwitchResponse`
        """
        http_info = self._show_sensitive_mask_switch_http_info(request)
        return self._call_api(**http_info)

    def show_sensitive_mask_switch_invoker(self, request):
        http_info = self._show_sensitive_mask_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sensitive_mask_switch_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/sensitive/mask/switch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSensitiveMaskSwitchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def show_sensitive_result_switch(self, request):
        r"""获取隐私数据结果集开关

        获取隐私数据结果集开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSensitiveResultSwitch
        :type request: :class:`huaweicloudsdkdbss.v1.ShowSensitiveResultSwitchRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ShowSensitiveResultSwitchResponse`
        """
        http_info = self._show_sensitive_result_switch_http_info(request)
        return self._call_api(**http_info)

    def show_sensitive_result_switch_invoker(self, request):
        http_info = self._show_sensitive_result_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sensitive_result_switch_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/sensitive/result/switch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSensitiveResultSwitchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def switch_risk_rule_new(self, request):
        r"""开启/关闭风险规则

        开启/关闭风险规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchRiskRuleNew
        :type request: :class:`huaweicloudsdkdbss.v1.SwitchRiskRuleNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.SwitchRiskRuleNewResponse`
        """
        http_info = self._switch_risk_rule_new_http_info(request)
        return self._call_api(**http_info)

    def switch_risk_rule_new_invoker(self, request):
        http_info = self._switch_risk_rule_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_risk_rule_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/audit/{instance_id}/rule/risk/switch",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchRiskRuleNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def update_audit_scope_rule(self, request):
        r"""编辑审计范围规则

        编辑审计范围规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAuditScopeRule
        :type request: :class:`huaweicloudsdkdbss.v1.UpdateAuditScopeRuleRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.UpdateAuditScopeRuleResponse`
        """
        http_info = self._update_audit_scope_rule_http_info(request)
        return self._call_api(**http_info)

    def update_audit_scope_rule_invoker(self, request):
        http_info = self._update_audit_scope_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_audit_scope_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/audit/{instance_id}/rule/scopes/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAuditScopeRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
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

    def update_sensitive_mask_rule(self, request):
        r"""修改编辑隐私数据脱敏规则

        修改编辑隐私数据脱敏规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSensitiveMaskRule
        :type request: :class:`huaweicloudsdkdbss.v1.UpdateSensitiveMaskRuleRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.UpdateSensitiveMaskRuleResponse`
        """
        http_info = self._update_sensitive_mask_rule_http_info(request)
        return self._call_api(**http_info)

    def update_sensitive_mask_rule_invoker(self, request):
        http_info = self._update_sensitive_mask_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_sensitive_mask_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/sensitive/mask/rule/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSensitiveMaskRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
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

    def create_audit_sql_rule(self, request):
        r"""添加sql自定义规则

        添加sql自定义规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAuditSqlRule
        :type request: :class:`huaweicloudsdkdbss.v1.CreateAuditSqlRuleRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.CreateAuditSqlRuleResponse`
        """
        http_info = self._create_audit_sql_rule_http_info(request)
        return self._call_api(**http_info)

    def create_audit_sql_rule_invoker(self, request):
        http_info = self._create_audit_sql_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_audit_sql_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/rule/sql",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAuditSqlRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def delete_audit_rule_sql(self, request):
        r"""删除sql自定义规则

        删除sql自定义规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAuditRuleSql
        :type request: :class:`huaweicloudsdkdbss.v1.DeleteAuditRuleSqlRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.DeleteAuditRuleSqlResponse`
        """
        http_info = self._delete_audit_rule_sql_http_info(request)
        return self._call_api(**http_info)

    def delete_audit_rule_sql_invoker(self, request):
        http_info = self._delete_audit_rule_sql_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_audit_rule_sql_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/rule/sql/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAuditRuleSqlResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
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

    def list_sql_injection_rules_new(self, request):
        r"""查询SQL注入规则策略

        查询SQL注入规则策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSqlInjectionRulesNew
        :type request: :class:`huaweicloudsdkdbss.v1.ListSqlInjectionRulesNewRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListSqlInjectionRulesNewResponse`
        """
        http_info = self._list_sql_injection_rules_new_http_info(request)
        return self._call_api(**http_info)

    def list_sql_injection_rules_new_invoker(self, request):
        http_info = self._list_sql_injection_rules_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sql_injection_rules_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/rule/sqls",
            "request_type": request.__class__.__name__,
            "response_type": "ListSqlInjectionRulesNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def set_audit_sql_rule_switch(self, request):
        r"""开启关闭sql注入策略

        开启关闭sql注入策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetAuditSqlRuleSwitch
        :type request: :class:`huaweicloudsdkdbss.v1.SetAuditSqlRuleSwitchRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.SetAuditSqlRuleSwitchResponse`
        """
        http_info = self._set_audit_sql_rule_switch_http_info(request)
        return self._call_api(**http_info)

    def set_audit_sql_rule_switch_invoker(self, request):
        http_info = self._set_audit_sql_rule_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_audit_sql_rule_switch_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/audit/{instance_id}/rule/sql/switch",
            "request_type": request.__class__.__name__,
            "response_type": "SetAuditSqlRuleSwitchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def set_sql_rule_rank(self, request):
        r"""sql规则优先级排序

        sql规则优先级排序
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetSqlRuleRank
        :type request: :class:`huaweicloudsdkdbss.v1.SetSqlRuleRankRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.SetSqlRuleRankResponse`
        """
        http_info = self._set_sql_rule_rank_http_info(request)
        return self._call_api(**http_info)

    def set_sql_rule_rank_invoker(self, request):
        http_info = self._set_sql_rule_rank_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_sql_rule_rank_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/audit/{instance_id}/rule/sql/rank",
            "request_type": request.__class__.__name__,
            "response_type": "SetSqlRuleRankResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def update_audit_sql_rule(self, request):
        r"""编辑sql自定义规则

        编辑sql自定义规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAuditSqlRule
        :type request: :class:`huaweicloudsdkdbss.v1.UpdateAuditSqlRuleRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.UpdateAuditSqlRuleResponse`
        """
        http_info = self._update_audit_sql_rule_http_info(request)
        return self._call_api(**http_info)

    def update_audit_sql_rule_invoker(self, request):
        http_info = self._update_audit_sql_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_audit_sql_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audit/{instance_id}/rule/sql/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAuditSqlRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
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
