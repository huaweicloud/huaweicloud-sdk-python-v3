# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DateColumnStatisticsData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'minimum_value': 'datetime',
        'maximum_value': 'datetime',
        'number_of_null': 'int',
        'number_of_distinct_value': 'int',
        'bit_vector': 'str'
    }

    attribute_map = {
        'minimum_value': 'minimum_value',
        'maximum_value': 'maximum_value',
        'number_of_null': 'number_of_null',
        'number_of_distinct_value': 'number_of_distinct_value',
        'bit_vector': 'bit_vector'
    }

    def __init__(self, minimum_value=None, maximum_value=None, number_of_null=None, number_of_distinct_value=None, bit_vector=None):
        """DateColumnStatisticsData

        The model defined in huaweicloud sdk

        :param minimum_value: 列中的最小时间戳
        :type minimum_value: datetime
        :param maximum_value: 列中的最大时间戳
        :type maximum_value: datetime
        :param number_of_null: 列中空值个数
        :type number_of_null: int
        :param number_of_distinct_value: 列中去重后的时间戳个数
        :type number_of_distinct_value: int
        :param bit_vector: 估算唯一值使用的位图
        :type bit_vector: str
        """
        
        

        self._minimum_value = None
        self._maximum_value = None
        self._number_of_null = None
        self._number_of_distinct_value = None
        self._bit_vector = None
        self.discriminator = None

        if minimum_value is not None:
            self.minimum_value = minimum_value
        if maximum_value is not None:
            self.maximum_value = maximum_value
        self.number_of_null = number_of_null
        self.number_of_distinct_value = number_of_distinct_value
        if bit_vector is not None:
            self.bit_vector = bit_vector

    @property
    def minimum_value(self):
        """Gets the minimum_value of this DateColumnStatisticsData.

        列中的最小时间戳

        :return: The minimum_value of this DateColumnStatisticsData.
        :rtype: datetime
        """
        return self._minimum_value

    @minimum_value.setter
    def minimum_value(self, minimum_value):
        """Sets the minimum_value of this DateColumnStatisticsData.

        列中的最小时间戳

        :param minimum_value: The minimum_value of this DateColumnStatisticsData.
        :type minimum_value: datetime
        """
        self._minimum_value = minimum_value

    @property
    def maximum_value(self):
        """Gets the maximum_value of this DateColumnStatisticsData.

        列中的最大时间戳

        :return: The maximum_value of this DateColumnStatisticsData.
        :rtype: datetime
        """
        return self._maximum_value

    @maximum_value.setter
    def maximum_value(self, maximum_value):
        """Sets the maximum_value of this DateColumnStatisticsData.

        列中的最大时间戳

        :param maximum_value: The maximum_value of this DateColumnStatisticsData.
        :type maximum_value: datetime
        """
        self._maximum_value = maximum_value

    @property
    def number_of_null(self):
        """Gets the number_of_null of this DateColumnStatisticsData.

        列中空值个数

        :return: The number_of_null of this DateColumnStatisticsData.
        :rtype: int
        """
        return self._number_of_null

    @number_of_null.setter
    def number_of_null(self, number_of_null):
        """Sets the number_of_null of this DateColumnStatisticsData.

        列中空值个数

        :param number_of_null: The number_of_null of this DateColumnStatisticsData.
        :type number_of_null: int
        """
        self._number_of_null = number_of_null

    @property
    def number_of_distinct_value(self):
        """Gets the number_of_distinct_value of this DateColumnStatisticsData.

        列中去重后的时间戳个数

        :return: The number_of_distinct_value of this DateColumnStatisticsData.
        :rtype: int
        """
        return self._number_of_distinct_value

    @number_of_distinct_value.setter
    def number_of_distinct_value(self, number_of_distinct_value):
        """Sets the number_of_distinct_value of this DateColumnStatisticsData.

        列中去重后的时间戳个数

        :param number_of_distinct_value: The number_of_distinct_value of this DateColumnStatisticsData.
        :type number_of_distinct_value: int
        """
        self._number_of_distinct_value = number_of_distinct_value

    @property
    def bit_vector(self):
        """Gets the bit_vector of this DateColumnStatisticsData.

        估算唯一值使用的位图

        :return: The bit_vector of this DateColumnStatisticsData.
        :rtype: str
        """
        return self._bit_vector

    @bit_vector.setter
    def bit_vector(self, bit_vector):
        """Sets the bit_vector of this DateColumnStatisticsData.

        估算唯一值使用的位图

        :param bit_vector: The bit_vector of this DateColumnStatisticsData.
        :type bit_vector: str
        """
        self._bit_vector = bit_vector

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
        if not isinstance(other, DateColumnStatisticsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
