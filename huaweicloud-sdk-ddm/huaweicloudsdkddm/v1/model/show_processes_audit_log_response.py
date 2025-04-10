# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProcessesAuditLogResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'process_audit_logs': 'list[UserProcessAuditLog]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'process_audit_logs': 'process_audit_logs'
    }

    def __init__(self, total_count=None, process_audit_logs=None):
        r"""ShowProcessesAuditLogResponse

        The model defined in huaweicloud sdk

        :param total_count: 总数
        :type total_count: int
        :param process_audit_logs: 日志记录集合
        :type process_audit_logs: list[:class:`huaweicloudsdkddm.v1.UserProcessAuditLog`]
        """
        
        super(ShowProcessesAuditLogResponse, self).__init__()

        self._total_count = None
        self._process_audit_logs = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if process_audit_logs is not None:
            self.process_audit_logs = process_audit_logs

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowProcessesAuditLogResponse.

        总数

        :return: The total_count of this ShowProcessesAuditLogResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowProcessesAuditLogResponse.

        总数

        :param total_count: The total_count of this ShowProcessesAuditLogResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def process_audit_logs(self):
        r"""Gets the process_audit_logs of this ShowProcessesAuditLogResponse.

        日志记录集合

        :return: The process_audit_logs of this ShowProcessesAuditLogResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.UserProcessAuditLog`]
        """
        return self._process_audit_logs

    @process_audit_logs.setter
    def process_audit_logs(self, process_audit_logs):
        r"""Sets the process_audit_logs of this ShowProcessesAuditLogResponse.

        日志记录集合

        :param process_audit_logs: The process_audit_logs of this ShowProcessesAuditLogResponse.
        :type process_audit_logs: list[:class:`huaweicloudsdkddm.v1.UserProcessAuditLog`]
        """
        self._process_audit_logs = process_audit_logs

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
        if not isinstance(other, ShowProcessesAuditLogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
