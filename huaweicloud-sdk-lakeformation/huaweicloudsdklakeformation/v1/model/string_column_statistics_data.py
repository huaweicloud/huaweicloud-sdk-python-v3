# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StringColumnStatisticsData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'average_length': 'float',
        'maximum_length': 'int',
        'number_of_null': 'int',
        'number_of_distinct_value': 'int',
        'bit_vector': 'str'
    }

    attribute_map = {
        'average_length': 'average_length',
        'maximum_length': 'maximum_length',
        'number_of_null': 'number_of_null',
        'number_of_distinct_value': 'number_of_distinct_value',
        'bit_vector': 'bit_vector'
    }

    def __init__(self, average_length=None, maximum_length=None, number_of_null=None, number_of_distinct_value=None, bit_vector=None):
        r"""StringColumnStatisticsData

        The model defined in huaweicloud sdk

        :param average_length: 列中字符串平均长度
        :type average_length: float
        :param maximum_length: 列中字符串最长长度
        :type maximum_length: int
        :param number_of_null: 列中空值个数
        :type number_of_null: int
        :param number_of_distinct_value: 列中去重后字符串个数
        :type number_of_distinct_value: int
        :param bit_vector: 估算唯一值使用的位图
        :type bit_vector: str
        """
        
        

        self._average_length = None
        self._maximum_length = None
        self._number_of_null = None
        self._number_of_distinct_value = None
        self._bit_vector = None
        self.discriminator = None

        self.average_length = average_length
        self.maximum_length = maximum_length
        self.number_of_null = number_of_null
        self.number_of_distinct_value = number_of_distinct_value
        if bit_vector is not None:
            self.bit_vector = bit_vector

    @property
    def average_length(self):
        r"""Gets the average_length of this StringColumnStatisticsData.

        列中字符串平均长度

        :return: The average_length of this StringColumnStatisticsData.
        :rtype: float
        """
        return self._average_length

    @average_length.setter
    def average_length(self, average_length):
        r"""Sets the average_length of this StringColumnStatisticsData.

        列中字符串平均长度

        :param average_length: The average_length of this StringColumnStatisticsData.
        :type average_length: float
        """
        self._average_length = average_length

    @property
    def maximum_length(self):
        r"""Gets the maximum_length of this StringColumnStatisticsData.

        列中字符串最长长度

        :return: The maximum_length of this StringColumnStatisticsData.
        :rtype: int
        """
        return self._maximum_length

    @maximum_length.setter
    def maximum_length(self, maximum_length):
        r"""Sets the maximum_length of this StringColumnStatisticsData.

        列中字符串最长长度

        :param maximum_length: The maximum_length of this StringColumnStatisticsData.
        :type maximum_length: int
        """
        self._maximum_length = maximum_length

    @property
    def number_of_null(self):
        r"""Gets the number_of_null of this StringColumnStatisticsData.

        列中空值个数

        :return: The number_of_null of this StringColumnStatisticsData.
        :rtype: int
        """
        return self._number_of_null

    @number_of_null.setter
    def number_of_null(self, number_of_null):
        r"""Sets the number_of_null of this StringColumnStatisticsData.

        列中空值个数

        :param number_of_null: The number_of_null of this StringColumnStatisticsData.
        :type number_of_null: int
        """
        self._number_of_null = number_of_null

    @property
    def number_of_distinct_value(self):
        r"""Gets the number_of_distinct_value of this StringColumnStatisticsData.

        列中去重后字符串个数

        :return: The number_of_distinct_value of this StringColumnStatisticsData.
        :rtype: int
        """
        return self._number_of_distinct_value

    @number_of_distinct_value.setter
    def number_of_distinct_value(self, number_of_distinct_value):
        r"""Sets the number_of_distinct_value of this StringColumnStatisticsData.

        列中去重后字符串个数

        :param number_of_distinct_value: The number_of_distinct_value of this StringColumnStatisticsData.
        :type number_of_distinct_value: int
        """
        self._number_of_distinct_value = number_of_distinct_value

    @property
    def bit_vector(self):
        r"""Gets the bit_vector of this StringColumnStatisticsData.

        估算唯一值使用的位图

        :return: The bit_vector of this StringColumnStatisticsData.
        :rtype: str
        """
        return self._bit_vector

    @bit_vector.setter
    def bit_vector(self, bit_vector):
        r"""Sets the bit_vector of this StringColumnStatisticsData.

        估算唯一值使用的位图

        :param bit_vector: The bit_vector of this StringColumnStatisticsData.
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
        if not isinstance(other, StringColumnStatisticsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
