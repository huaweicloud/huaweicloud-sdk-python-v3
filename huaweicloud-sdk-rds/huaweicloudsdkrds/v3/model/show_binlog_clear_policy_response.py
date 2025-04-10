# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBinlogClearPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'binlog_retention_hours': 'int',
        'binlog_clear_type': 'str'
    }

    attribute_map = {
        'binlog_retention_hours': 'binlog_retention_hours',
        'binlog_clear_type': 'binlog_clear_type'
    }

    def __init__(self, binlog_retention_hours=None, binlog_clear_type=None):
        r"""ShowBinlogClearPolicyResponse

        The model defined in huaweicloud sdk

        :param binlog_retention_hours: binlog保留时长
        :type binlog_retention_hours: int
        :param binlog_clear_type: 二进制日志保留策略,取值：time、fast - time:表示按时长保留二进制文件 - fast:表示快速清理,不保留二进制文件
        :type binlog_clear_type: str
        """
        
        super(ShowBinlogClearPolicyResponse, self).__init__()

        self._binlog_retention_hours = None
        self._binlog_clear_type = None
        self.discriminator = None

        if binlog_retention_hours is not None:
            self.binlog_retention_hours = binlog_retention_hours
        if binlog_clear_type is not None:
            self.binlog_clear_type = binlog_clear_type

    @property
    def binlog_retention_hours(self):
        r"""Gets the binlog_retention_hours of this ShowBinlogClearPolicyResponse.

        binlog保留时长

        :return: The binlog_retention_hours of this ShowBinlogClearPolicyResponse.
        :rtype: int
        """
        return self._binlog_retention_hours

    @binlog_retention_hours.setter
    def binlog_retention_hours(self, binlog_retention_hours):
        r"""Sets the binlog_retention_hours of this ShowBinlogClearPolicyResponse.

        binlog保留时长

        :param binlog_retention_hours: The binlog_retention_hours of this ShowBinlogClearPolicyResponse.
        :type binlog_retention_hours: int
        """
        self._binlog_retention_hours = binlog_retention_hours

    @property
    def binlog_clear_type(self):
        r"""Gets the binlog_clear_type of this ShowBinlogClearPolicyResponse.

        二进制日志保留策略,取值：time、fast - time:表示按时长保留二进制文件 - fast:表示快速清理,不保留二进制文件

        :return: The binlog_clear_type of this ShowBinlogClearPolicyResponse.
        :rtype: str
        """
        return self._binlog_clear_type

    @binlog_clear_type.setter
    def binlog_clear_type(self, binlog_clear_type):
        r"""Sets the binlog_clear_type of this ShowBinlogClearPolicyResponse.

        二进制日志保留策略,取值：time、fast - time:表示按时长保留二进制文件 - fast:表示快速清理,不保留二进制文件

        :param binlog_clear_type: The binlog_clear_type of this ShowBinlogClearPolicyResponse.
        :type binlog_clear_type: str
        """
        self._binlog_clear_type = binlog_clear_type

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
        if not isinstance(other, ShowBinlogClearPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
