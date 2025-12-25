# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuditResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'audit_info_list': 'list[AuditDO]',
        'total': 'int'
    }

    attribute_map = {
        'audit_info_list': 'auditInfoList',
        'total': 'total'
    }

    def __init__(self, audit_info_list=None, total=None):
        r"""AuditResult

        The model defined in huaweicloud sdk

        :param audit_info_list: **参数解释**： 审计日志列表。  **取值范围**： 不涉及。
        :type audit_info_list: list[:class:`huaweicloudsdkcodeartsartifact.v2.AuditDO`]
        :param total: **参数解释**： 审计日志条数。  **取值范围**： 不涉及。
        :type total: int
        """
        
        

        self._audit_info_list = None
        self._total = None
        self.discriminator = None

        if audit_info_list is not None:
            self.audit_info_list = audit_info_list
        if total is not None:
            self.total = total

    @property
    def audit_info_list(self):
        r"""Gets the audit_info_list of this AuditResult.

        **参数解释**： 审计日志列表。  **取值范围**： 不涉及。

        :return: The audit_info_list of this AuditResult.
        :rtype: list[:class:`huaweicloudsdkcodeartsartifact.v2.AuditDO`]
        """
        return self._audit_info_list

    @audit_info_list.setter
    def audit_info_list(self, audit_info_list):
        r"""Sets the audit_info_list of this AuditResult.

        **参数解释**： 审计日志列表。  **取值范围**： 不涉及。

        :param audit_info_list: The audit_info_list of this AuditResult.
        :type audit_info_list: list[:class:`huaweicloudsdkcodeartsartifact.v2.AuditDO`]
        """
        self._audit_info_list = audit_info_list

    @property
    def total(self):
        r"""Gets the total of this AuditResult.

        **参数解释**： 审计日志条数。  **取值范围**： 不涉及。

        :return: The total of this AuditResult.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this AuditResult.

        **参数解释**： 审计日志条数。  **取值范围**： 不涉及。

        :param total: The total of this AuditResult.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AuditResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
