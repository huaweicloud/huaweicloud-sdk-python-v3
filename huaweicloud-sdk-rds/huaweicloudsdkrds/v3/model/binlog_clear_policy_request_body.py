# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BinlogClearPolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'binlog_retention_hours': 'int'
    }

    attribute_map = {
        'binlog_retention_hours': 'binlog_retention_hours'
    }

    def __init__(self, binlog_retention_hours=None):
        """BinlogClearPolicyRequestBody

        The model defined in huaweicloud sdk

        :param binlog_retention_hours: 取值范围0-7*24
        :type binlog_retention_hours: int
        """
        
        

        self._binlog_retention_hours = None
        self.discriminator = None

        self.binlog_retention_hours = binlog_retention_hours

    @property
    def binlog_retention_hours(self):
        """Gets the binlog_retention_hours of this BinlogClearPolicyRequestBody.

        取值范围0-7*24

        :return: The binlog_retention_hours of this BinlogClearPolicyRequestBody.
        :rtype: int
        """
        return self._binlog_retention_hours

    @binlog_retention_hours.setter
    def binlog_retention_hours(self, binlog_retention_hours):
        """Sets the binlog_retention_hours of this BinlogClearPolicyRequestBody.

        取值范围0-7*24

        :param binlog_retention_hours: The binlog_retention_hours of this BinlogClearPolicyRequestBody.
        :type binlog_retention_hours: int
        """
        self._binlog_retention_hours = binlog_retention_hours

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
        if not isinstance(other, BinlogClearPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
