# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPlaybookAuditLogsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'audit_logs': 'list[AuditLogInfo]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'count': 'count',
        'audit_logs': 'audit_logs',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, count=None, audit_logs=None, x_request_id=None):
        """ListPlaybookAuditLogsResponse

        The model defined in huaweicloud sdk

        :param count: 总条数
        :type count: int
        :param audit_logs: 审计日志列表信息
        :type audit_logs: list[:class:`huaweicloudsdksecmaster.v2.AuditLogInfo`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListPlaybookAuditLogsResponse, self).__init__()

        self._count = None
        self._audit_logs = None
        self._x_request_id = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if audit_logs is not None:
            self.audit_logs = audit_logs
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def count(self):
        """Gets the count of this ListPlaybookAuditLogsResponse.

        总条数

        :return: The count of this ListPlaybookAuditLogsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListPlaybookAuditLogsResponse.

        总条数

        :param count: The count of this ListPlaybookAuditLogsResponse.
        :type count: int
        """
        self._count = count

    @property
    def audit_logs(self):
        """Gets the audit_logs of this ListPlaybookAuditLogsResponse.

        审计日志列表信息

        :return: The audit_logs of this ListPlaybookAuditLogsResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.AuditLogInfo`]
        """
        return self._audit_logs

    @audit_logs.setter
    def audit_logs(self, audit_logs):
        """Sets the audit_logs of this ListPlaybookAuditLogsResponse.

        审计日志列表信息

        :param audit_logs: The audit_logs of this ListPlaybookAuditLogsResponse.
        :type audit_logs: list[:class:`huaweicloudsdksecmaster.v2.AuditLogInfo`]
        """
        self._audit_logs = audit_logs

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListPlaybookAuditLogsResponse.

        :return: The x_request_id of this ListPlaybookAuditLogsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListPlaybookAuditLogsResponse.

        :param x_request_id: The x_request_id of this ListPlaybookAuditLogsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListPlaybookAuditLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
