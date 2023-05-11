# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlaReportsValue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'timestamp': 'int',
        'value': 'float'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'value': 'value'
    }

    def __init__(self, timestamp=None, value=None):
        """SlaReportsValue

        The model defined in huaweicloud sdk

        :param timestamp: 时间戳
        :type timestamp: int
        :param value: 值
        :type value: float
        """
        
        

        self._timestamp = None
        self._value = None
        self.discriminator = None

        if timestamp is not None:
            self.timestamp = timestamp
        if value is not None:
            self.value = value

    @property
    def timestamp(self):
        """Gets the timestamp of this SlaReportsValue.

        时间戳

        :return: The timestamp of this SlaReportsValue.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this SlaReportsValue.

        时间戳

        :param timestamp: The timestamp of this SlaReportsValue.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def value(self):
        """Gets the value of this SlaReportsValue.

        值

        :return: The value of this SlaReportsValue.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SlaReportsValue.

        值

        :param value: The value of this SlaReportsValue.
        :type value: float
        """
        self._value = value

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
        if not isinstance(other, SlaReportsValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
