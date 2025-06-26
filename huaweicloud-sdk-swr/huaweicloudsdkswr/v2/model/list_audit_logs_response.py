# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAuditLogsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'audit_logs': 'list[AuditLog]',
        'total': 'int'
    }

    attribute_map = {
        'audit_logs': 'audit_logs',
        'total': 'total'
    }

    def __init__(self, audit_logs=None, total=None):
        r"""ListAuditLogsResponse

        The model defined in huaweicloud sdk

        :param audit_logs: 审计日志列表
        :type audit_logs: list[:class:`huaweicloudsdkswr.v2.AuditLog`]
        :param total: 审计日志总数
        :type total: int
        """
        
        super(ListAuditLogsResponse, self).__init__()

        self._audit_logs = None
        self._total = None
        self.discriminator = None

        if audit_logs is not None:
            self.audit_logs = audit_logs
        if total is not None:
            self.total = total

    @property
    def audit_logs(self):
        r"""Gets the audit_logs of this ListAuditLogsResponse.

        审计日志列表

        :return: The audit_logs of this ListAuditLogsResponse.
        :rtype: list[:class:`huaweicloudsdkswr.v2.AuditLog`]
        """
        return self._audit_logs

    @audit_logs.setter
    def audit_logs(self, audit_logs):
        r"""Sets the audit_logs of this ListAuditLogsResponse.

        审计日志列表

        :param audit_logs: The audit_logs of this ListAuditLogsResponse.
        :type audit_logs: list[:class:`huaweicloudsdkswr.v2.AuditLog`]
        """
        self._audit_logs = audit_logs

    @property
    def total(self):
        r"""Gets the total of this ListAuditLogsResponse.

        审计日志总数

        :return: The total of this ListAuditLogsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListAuditLogsResponse.

        审计日志总数

        :param total: The total of this ListAuditLogsResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListAuditLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
