# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuditResultSystemAuditResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'audit_time': 'int',
        'errors': 'list[AuditResultSystemAuditResultErrors]'
    }

    attribute_map = {
        'audit_time': 'audit_time',
        'errors': 'errors'
    }

    def __init__(self, audit_time=None, errors=None):
        r"""AuditResultSystemAuditResult

        The model defined in huaweicloud sdk

        :param audit_time: 操作时间。
        :type audit_time: int
        :param errors: 错误列表。
        :type errors: list[:class:`huaweicloudsdkmetastudio.v1.AuditResultSystemAuditResultErrors`]
        """
        
        

        self._audit_time = None
        self._errors = None
        self.discriminator = None

        if audit_time is not None:
            self.audit_time = audit_time
        if errors is not None:
            self.errors = errors

    @property
    def audit_time(self):
        r"""Gets the audit_time of this AuditResultSystemAuditResult.

        操作时间。

        :return: The audit_time of this AuditResultSystemAuditResult.
        :rtype: int
        """
        return self._audit_time

    @audit_time.setter
    def audit_time(self, audit_time):
        r"""Sets the audit_time of this AuditResultSystemAuditResult.

        操作时间。

        :param audit_time: The audit_time of this AuditResultSystemAuditResult.
        :type audit_time: int
        """
        self._audit_time = audit_time

    @property
    def errors(self):
        r"""Gets the errors of this AuditResultSystemAuditResult.

        错误列表。

        :return: The errors of this AuditResultSystemAuditResult.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.AuditResultSystemAuditResultErrors`]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        r"""Sets the errors of this AuditResultSystemAuditResult.

        错误列表。

        :param errors: The errors of this AuditResultSystemAuditResult.
        :type errors: list[:class:`huaweicloudsdkmetastudio.v1.AuditResultSystemAuditResultErrors`]
        """
        self._errors = errors

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
        if not isinstance(other, AuditResultSystemAuditResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
