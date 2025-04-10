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
        'reserve_auditlogs': 'bool',
        'audit_types': 'list[str]'
    }

    attribute_map = {
        'keep_days': 'keep_days',
        'reserve_auditlogs': 'reserve_auditlogs',
        'audit_types': 'audit_types'
    }

    def __init__(self, keep_days=None, reserve_auditlogs=None, audit_types=None):
        r"""SetAuditlogPolicyRequestBody

        The model defined in huaweicloud sdk

        :param keep_days: 审计日志保存天数，取值范围0~732。0表示关闭审计日志策略。
        :type keep_days: int
        :param reserve_auditlogs: 仅关闭审计日志策略时有效。  - true（默认），表示关闭审计日志策略的同时，延迟删除已有的历史审计日志。 - false，表示关闭审计日志策略的同时，删除已有的历史审计日志。
        :type reserve_auditlogs: bool
        :param audit_types: 审计记录的操作类型，动态范围。空表示不过滤任何操作类型。
        :type audit_types: list[str]
        """
        
        

        self._keep_days = None
        self._reserve_auditlogs = None
        self._audit_types = None
        self.discriminator = None

        self.keep_days = keep_days
        if reserve_auditlogs is not None:
            self.reserve_auditlogs = reserve_auditlogs
        if audit_types is not None:
            self.audit_types = audit_types

    @property
    def keep_days(self):
        r"""Gets the keep_days of this SetAuditlogPolicyRequestBody.

        审计日志保存天数，取值范围0~732。0表示关闭审计日志策略。

        :return: The keep_days of this SetAuditlogPolicyRequestBody.
        :rtype: int
        """
        return self._keep_days

    @keep_days.setter
    def keep_days(self, keep_days):
        r"""Sets the keep_days of this SetAuditlogPolicyRequestBody.

        审计日志保存天数，取值范围0~732。0表示关闭审计日志策略。

        :param keep_days: The keep_days of this SetAuditlogPolicyRequestBody.
        :type keep_days: int
        """
        self._keep_days = keep_days

    @property
    def reserve_auditlogs(self):
        r"""Gets the reserve_auditlogs of this SetAuditlogPolicyRequestBody.

        仅关闭审计日志策略时有效。  - true（默认），表示关闭审计日志策略的同时，延迟删除已有的历史审计日志。 - false，表示关闭审计日志策略的同时，删除已有的历史审计日志。

        :return: The reserve_auditlogs of this SetAuditlogPolicyRequestBody.
        :rtype: bool
        """
        return self._reserve_auditlogs

    @reserve_auditlogs.setter
    def reserve_auditlogs(self, reserve_auditlogs):
        r"""Sets the reserve_auditlogs of this SetAuditlogPolicyRequestBody.

        仅关闭审计日志策略时有效。  - true（默认），表示关闭审计日志策略的同时，延迟删除已有的历史审计日志。 - false，表示关闭审计日志策略的同时，删除已有的历史审计日志。

        :param reserve_auditlogs: The reserve_auditlogs of this SetAuditlogPolicyRequestBody.
        :type reserve_auditlogs: bool
        """
        self._reserve_auditlogs = reserve_auditlogs

    @property
    def audit_types(self):
        r"""Gets the audit_types of this SetAuditlogPolicyRequestBody.

        审计记录的操作类型，动态范围。空表示不过滤任何操作类型。

        :return: The audit_types of this SetAuditlogPolicyRequestBody.
        :rtype: list[str]
        """
        return self._audit_types

    @audit_types.setter
    def audit_types(self, audit_types):
        r"""Sets the audit_types of this SetAuditlogPolicyRequestBody.

        审计记录的操作类型，动态范围。空表示不过滤任何操作类型。

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
