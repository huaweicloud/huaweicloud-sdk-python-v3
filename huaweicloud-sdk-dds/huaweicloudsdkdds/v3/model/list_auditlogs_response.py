# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAuditlogsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_record': 'int',
        'audit_logs': 'list[ListAuditlogsResult]'
    }

    attribute_map = {
        'total_record': 'total_record',
        'audit_logs': 'audit_logs'
    }

    def __init__(self, total_record=None, audit_logs=None):
        """ListAuditlogsResponse

        The model defined in huaweicloud sdk

        :param total_record: 总记录数。
        :type total_record: int
        :param audit_logs: 审计日志具体信息。
        :type audit_logs: list[:class:`huaweicloudsdkdds.v3.ListAuditlogsResult`]
        """
        
        super(ListAuditlogsResponse, self).__init__()

        self._total_record = None
        self._audit_logs = None
        self.discriminator = None

        if total_record is not None:
            self.total_record = total_record
        if audit_logs is not None:
            self.audit_logs = audit_logs

    @property
    def total_record(self):
        """Gets the total_record of this ListAuditlogsResponse.

        总记录数。

        :return: The total_record of this ListAuditlogsResponse.
        :rtype: int
        """
        return self._total_record

    @total_record.setter
    def total_record(self, total_record):
        """Sets the total_record of this ListAuditlogsResponse.

        总记录数。

        :param total_record: The total_record of this ListAuditlogsResponse.
        :type total_record: int
        """
        self._total_record = total_record

    @property
    def audit_logs(self):
        """Gets the audit_logs of this ListAuditlogsResponse.

        审计日志具体信息。

        :return: The audit_logs of this ListAuditlogsResponse.
        :rtype: list[:class:`huaweicloudsdkdds.v3.ListAuditlogsResult`]
        """
        return self._audit_logs

    @audit_logs.setter
    def audit_logs(self, audit_logs):
        """Sets the audit_logs of this ListAuditlogsResponse.

        审计日志具体信息。

        :param audit_logs: The audit_logs of this ListAuditlogsResponse.
        :type audit_logs: list[:class:`huaweicloudsdkdds.v3.ListAuditlogsResult`]
        """
        self._audit_logs = audit_logs

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
        if not isinstance(other, ListAuditlogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
