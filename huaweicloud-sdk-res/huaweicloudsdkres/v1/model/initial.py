# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Initial:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'initial_method': 'str',
        'mean_value': 'float',
        'standard_deviation': 'float',
        'min_value': 'float',
        'max_value': 'float'
    }

    attribute_map = {
        'initial_method': 'initial_method',
        'mean_value': 'mean_value',
        'standard_deviation': 'standard_deviation',
        'min_value': 'min_value',
        'max_value': 'max_value'
    }

    def __init__(self, initial_method=None, mean_value=None, standard_deviation=None, min_value=None, max_value=None):
        """Initial

        The model defined in huaweicloud sdk

        :param initial_method: 初始化方法。
        :type initial_method: str
        :param mean_value: 平均值。
        :type mean_value: float
        :param standard_deviation: 标准差。
        :type standard_deviation: float
        :param min_value: 最小值。
        :type min_value: float
        :param max_value: 最大值。
        :type max_value: float
        """
        
        

        self._initial_method = None
        self._mean_value = None
        self._standard_deviation = None
        self._min_value = None
        self._max_value = None
        self.discriminator = None

        self.initial_method = initial_method
        if mean_value is not None:
            self.mean_value = mean_value
        if standard_deviation is not None:
            self.standard_deviation = standard_deviation
        if min_value is not None:
            self.min_value = min_value
        if max_value is not None:
            self.max_value = max_value

    @property
    def initial_method(self):
        """Gets the initial_method of this Initial.

        初始化方法。

        :return: The initial_method of this Initial.
        :rtype: str
        """
        return self._initial_method

    @initial_method.setter
    def initial_method(self, initial_method):
        """Sets the initial_method of this Initial.

        初始化方法。

        :param initial_method: The initial_method of this Initial.
        :type initial_method: str
        """
        self._initial_method = initial_method

    @property
    def mean_value(self):
        """Gets the mean_value of this Initial.

        平均值。

        :return: The mean_value of this Initial.
        :rtype: float
        """
        return self._mean_value

    @mean_value.setter
    def mean_value(self, mean_value):
        """Sets the mean_value of this Initial.

        平均值。

        :param mean_value: The mean_value of this Initial.
        :type mean_value: float
        """
        self._mean_value = mean_value

    @property
    def standard_deviation(self):
        """Gets the standard_deviation of this Initial.

        标准差。

        :return: The standard_deviation of this Initial.
        :rtype: float
        """
        return self._standard_deviation

    @standard_deviation.setter
    def standard_deviation(self, standard_deviation):
        """Sets the standard_deviation of this Initial.

        标准差。

        :param standard_deviation: The standard_deviation of this Initial.
        :type standard_deviation: float
        """
        self._standard_deviation = standard_deviation

    @property
    def min_value(self):
        """Gets the min_value of this Initial.

        最小值。

        :return: The min_value of this Initial.
        :rtype: float
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """Sets the min_value of this Initial.

        最小值。

        :param min_value: The min_value of this Initial.
        :type min_value: float
        """
        self._min_value = min_value

    @property
    def max_value(self):
        """Gets the max_value of this Initial.

        最大值。

        :return: The max_value of this Initial.
        :rtype: float
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """Sets the max_value of this Initial.

        最大值。

        :param max_value: The max_value of this Initial.
        :type max_value: float
        """
        self._max_value = max_value

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
        if not isinstance(other, Initial):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
