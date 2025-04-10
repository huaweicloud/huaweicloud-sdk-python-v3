# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetAuditlogPolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keep_days': 'int',
        'reserve_auditlogs': 'str',
        'audit_scope': 'str',
        'audit_types': 'list[str]'
    }

    attribute_map = {
        'keep_days': 'keep_days',
        'reserve_auditlogs': 'reserve_auditlogs',
        'audit_scope': 'audit_scope',
        'audit_types': 'audit_types'
    }

    def __init__(self, keep_days=None, reserve_auditlogs=None, audit_scope=None, audit_types=None):
        r"""SetAuditlogPolicyRequestBody

        The model defined in huaweicloud sdk

        :param keep_days: 审计日志保存天数，取值范围0，7~732。 - 取值0，表示关闭审计日志策略。 - 取值7~732，表示开启审计日志策略，并设置审计日志保存天数为该值。
        :type keep_days: int
        :param reserve_auditlogs: 仅关闭审计日志策略时有效。 - true（默认），表示关闭审计日志策略的同时，保留历史审计日志。 - false，表示关闭审计日志策略的同时，删除已有的历史审计日志。
        :type reserve_auditlogs: str
        :param audit_scope: 仅打开审计日志策略时有效，并且为空时，默认全部。审计范围。请输入数据库或集合名称，多个库或集合请用英文逗号分隔。若名称中有英文逗号，请在逗号前添加“$”符号，用以区分分隔符。
        :type audit_scope: str
        :param audit_types: 仅打开审计日志策略时有效，并且为空时，默认全部。审计类型。支持insert，delete，update，query等。
        :type audit_types: list[str]
        """
        
        

        self._keep_days = None
        self._reserve_auditlogs = None
        self._audit_scope = None
        self._audit_types = None
        self.discriminator = None

        self.keep_days = keep_days
        if reserve_auditlogs is not None:
            self.reserve_auditlogs = reserve_auditlogs
        if audit_scope is not None:
            self.audit_scope = audit_scope
        if audit_types is not None:
            self.audit_types = audit_types

    @property
    def keep_days(self):
        r"""Gets the keep_days of this SetAuditlogPolicyRequestBody.

        审计日志保存天数，取值范围0，7~732。 - 取值0，表示关闭审计日志策略。 - 取值7~732，表示开启审计日志策略，并设置审计日志保存天数为该值。

        :return: The keep_days of this SetAuditlogPolicyRequestBody.
        :rtype: int
        """
        return self._keep_days

    @keep_days.setter
    def keep_days(self, keep_days):
        r"""Sets the keep_days of this SetAuditlogPolicyRequestBody.

        审计日志保存天数，取值范围0，7~732。 - 取值0，表示关闭审计日志策略。 - 取值7~732，表示开启审计日志策略，并设置审计日志保存天数为该值。

        :param keep_days: The keep_days of this SetAuditlogPolicyRequestBody.
        :type keep_days: int
        """
        self._keep_days = keep_days

    @property
    def reserve_auditlogs(self):
        r"""Gets the reserve_auditlogs of this SetAuditlogPolicyRequestBody.

        仅关闭审计日志策略时有效。 - true（默认），表示关闭审计日志策略的同时，保留历史审计日志。 - false，表示关闭审计日志策略的同时，删除已有的历史审计日志。

        :return: The reserve_auditlogs of this SetAuditlogPolicyRequestBody.
        :rtype: str
        """
        return self._reserve_auditlogs

    @reserve_auditlogs.setter
    def reserve_auditlogs(self, reserve_auditlogs):
        r"""Sets the reserve_auditlogs of this SetAuditlogPolicyRequestBody.

        仅关闭审计日志策略时有效。 - true（默认），表示关闭审计日志策略的同时，保留历史审计日志。 - false，表示关闭审计日志策略的同时，删除已有的历史审计日志。

        :param reserve_auditlogs: The reserve_auditlogs of this SetAuditlogPolicyRequestBody.
        :type reserve_auditlogs: str
        """
        self._reserve_auditlogs = reserve_auditlogs

    @property
    def audit_scope(self):
        r"""Gets the audit_scope of this SetAuditlogPolicyRequestBody.

        仅打开审计日志策略时有效，并且为空时，默认全部。审计范围。请输入数据库或集合名称，多个库或集合请用英文逗号分隔。若名称中有英文逗号，请在逗号前添加“$”符号，用以区分分隔符。

        :return: The audit_scope of this SetAuditlogPolicyRequestBody.
        :rtype: str
        """
        return self._audit_scope

    @audit_scope.setter
    def audit_scope(self, audit_scope):
        r"""Sets the audit_scope of this SetAuditlogPolicyRequestBody.

        仅打开审计日志策略时有效，并且为空时，默认全部。审计范围。请输入数据库或集合名称，多个库或集合请用英文逗号分隔。若名称中有英文逗号，请在逗号前添加“$”符号，用以区分分隔符。

        :param audit_scope: The audit_scope of this SetAuditlogPolicyRequestBody.
        :type audit_scope: str
        """
        self._audit_scope = audit_scope

    @property
    def audit_types(self):
        r"""Gets the audit_types of this SetAuditlogPolicyRequestBody.

        仅打开审计日志策略时有效，并且为空时，默认全部。审计类型。支持insert，delete，update，query等。

        :return: The audit_types of this SetAuditlogPolicyRequestBody.
        :rtype: list[str]
        """
        return self._audit_types

    @audit_types.setter
    def audit_types(self, audit_types):
        r"""Sets the audit_types of this SetAuditlogPolicyRequestBody.

        仅打开审计日志策略时有效，并且为空时，默认全部。审计类型。支持insert，delete，update，query等。

        :param audit_types: The audit_types of this SetAuditlogPolicyRequestBody.
        :type audit_types: list[str]
        """
        self._audit_types = audit_types

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SetAuditlogPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
