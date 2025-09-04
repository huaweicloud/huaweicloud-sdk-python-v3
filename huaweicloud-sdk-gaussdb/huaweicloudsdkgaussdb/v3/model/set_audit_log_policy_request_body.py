# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetAuditLogPolicyRequestBody:

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
        'reserve_audit_logs': 'bool',
        'audit_types': 'list[str]'
    }

    attribute_map = {
        'keep_days': 'keep_days',
        'reserve_audit_logs': 'reserve_audit_logs',
        'audit_types': 'audit_types'
    }

    def __init__(self, keep_days=None, reserve_audit_logs=None, audit_types=None):
        r"""SetAuditLogPolicyRequestBody

        The model defined in huaweicloud sdk

        :param keep_days: **参数解释**：  审计日志保存天数，0表示关闭审计日志策略。  **约束限制**：  不涉及。  **取值范围**：  0~732。  **默认取值**：  7。
        :type keep_days: int
        :param reserve_audit_logs: **参数解释**：  仅关闭审计日志策略时有效。 - true（默认），表示关闭审计日志策略的同时，保留历史审计日志。 - false，表示关闭审计日志策略的同时，删除已有的历史审计日志。  **约束限制**：  不涉及。  **取值范围**：  true|false。  **默认取值**：  true。
        :type reserve_audit_logs: bool
        :param audit_types: **参数解释**：  审计记录的操作类型，动态范围。空表示不过滤任何操作类型。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type audit_types: list[str]
        """
        
        

        self._keep_days = None
        self._reserve_audit_logs = None
        self._audit_types = None
        self.discriminator = None

        self.keep_days = keep_days
        if reserve_audit_logs is not None:
            self.reserve_audit_logs = reserve_audit_logs
        if audit_types is not None:
            self.audit_types = audit_types

    @property
    def keep_days(self):
        r"""Gets the keep_days of this SetAuditLogPolicyRequestBody.

        **参数解释**：  审计日志保存天数，0表示关闭审计日志策略。  **约束限制**：  不涉及。  **取值范围**：  0~732。  **默认取值**：  7。

        :return: The keep_days of this SetAuditLogPolicyRequestBody.
        :rtype: int
        """
        return self._keep_days

    @keep_days.setter
    def keep_days(self, keep_days):
        r"""Sets the keep_days of this SetAuditLogPolicyRequestBody.

        **参数解释**：  审计日志保存天数，0表示关闭审计日志策略。  **约束限制**：  不涉及。  **取值范围**：  0~732。  **默认取值**：  7。

        :param keep_days: The keep_days of this SetAuditLogPolicyRequestBody.
        :type keep_days: int
        """
        self._keep_days = keep_days

    @property
    def reserve_audit_logs(self):
        r"""Gets the reserve_audit_logs of this SetAuditLogPolicyRequestBody.

        **参数解释**：  仅关闭审计日志策略时有效。 - true（默认），表示关闭审计日志策略的同时，保留历史审计日志。 - false，表示关闭审计日志策略的同时，删除已有的历史审计日志。  **约束限制**：  不涉及。  **取值范围**：  true|false。  **默认取值**：  true。

        :return: The reserve_audit_logs of this SetAuditLogPolicyRequestBody.
        :rtype: bool
        """
        return self._reserve_audit_logs

    @reserve_audit_logs.setter
    def reserve_audit_logs(self, reserve_audit_logs):
        r"""Sets the reserve_audit_logs of this SetAuditLogPolicyRequestBody.

        **参数解释**：  仅关闭审计日志策略时有效。 - true（默认），表示关闭审计日志策略的同时，保留历史审计日志。 - false，表示关闭审计日志策略的同时，删除已有的历史审计日志。  **约束限制**：  不涉及。  **取值范围**：  true|false。  **默认取值**：  true。

        :param reserve_audit_logs: The reserve_audit_logs of this SetAuditLogPolicyRequestBody.
        :type reserve_audit_logs: bool
        """
        self._reserve_audit_logs = reserve_audit_logs

    @property
    def audit_types(self):
        r"""Gets the audit_types of this SetAuditLogPolicyRequestBody.

        **参数解释**：  审计记录的操作类型，动态范围。空表示不过滤任何操作类型。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The audit_types of this SetAuditLogPolicyRequestBody.
        :rtype: list[str]
        """
        return self._audit_types

    @audit_types.setter
    def audit_types(self, audit_types):
        r"""Sets the audit_types of this SetAuditLogPolicyRequestBody.

        **参数解释**：  审计记录的操作类型，动态范围。空表示不过滤任何操作类型。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param audit_types: The audit_types of this SetAuditLogPolicyRequestBody.
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
        if not isinstance(other, SetAuditLogPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
