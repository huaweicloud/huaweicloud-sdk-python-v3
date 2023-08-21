# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TimeSeriesData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time': 'int',
        'value': 'float'
    }

    attribute_map = {
        'time': 'time',
        'value': 'value'
    }

    def __init__(self, time=None, value=None):
        """TimeSeriesData

        The model defined in huaweicloud sdk

        :param time: 13位时间戳
        :type time: int
        :param value: 数据值，单位：Kbps（查询流量时）、次（查询事件时）
        :type value: float
        """
        
        

        self._time = None
        self._value = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if value is not None:
            self.value = value

    @property
    def time(self):
        """Gets the time of this TimeSeriesData.

        13位时间戳

        :return: The time of this TimeSeriesData.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this TimeSeriesData.

        13位时间戳

        :param time: The time of this TimeSeriesData.
        :type time: int
        """
        self._time = time

    @property
    def value(self):
        """Gets the value of this TimeSeriesData.

        数据值，单位：Kbps（查询流量时）、次（查询事件时）

        :return: The value of this TimeSeriesData.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TimeSeriesData.

        数据值，单位：Kbps（查询流量时）、次（查询事件时）

        :param value: The value of this TimeSeriesData.
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
        if not isinstance(other, TimeSeriesData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
