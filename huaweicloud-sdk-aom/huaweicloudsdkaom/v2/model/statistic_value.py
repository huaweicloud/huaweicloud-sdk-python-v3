# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatisticValue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'statistic': 'str',
        'value': 'float'
    }

    attribute_map = {
        'statistic': 'statistic',
        'value': 'value'
    }

    def __init__(self, statistic=None, value=None):
        """StatisticValue

        The model defined in huaweicloud sdk

        :param statistic: 统计方式。
        :type statistic: str
        :param value: 统计结果。
        :type value: float
        """
        
        

        self._statistic = None
        self._value = None
        self.discriminator = None

        if statistic is not None:
            self.statistic = statistic
        if value is not None:
            self.value = value

    @property
    def statistic(self):
        """Gets the statistic of this StatisticValue.

        统计方式。

        :return: The statistic of this StatisticValue.
        :rtype: str
        """
        return self._statistic

    @statistic.setter
    def statistic(self, statistic):
        """Sets the statistic of this StatisticValue.

        统计方式。

        :param statistic: The statistic of this StatisticValue.
        :type statistic: str
        """
        self._statistic = statistic

    @property
    def value(self):
        """Gets the value of this StatisticValue.

        统计结果。

        :return: The value of this StatisticValue.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this StatisticValue.

        统计结果。

        :param value: The value of this StatisticValue.
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
        if not isinstance(other, StatisticValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
