# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IntegerRange:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max': 'int',
        'min': 'int',
        'desire': 'int'
    }

    attribute_map = {
        'max': 'max',
        'min': 'min',
        'desire': 'desire'
    }

    def __init__(self, max=None, min=None, desire=None):
        """IntegerRange

        The model defined in huaweicloud sdk

        :param max: 伸缩组最大实例数
        :type max: int
        :param min: 伸缩组最小实例数
        :type min: int
        :param desire: 伸缩组期望实例数
        :type desire: int
        """
        
        

        self._max = None
        self._min = None
        self._desire = None
        self.discriminator = None

        if max is not None:
            self.max = max
        if min is not None:
            self.min = min
        if desire is not None:
            self.desire = desire

    @property
    def max(self):
        """Gets the max of this IntegerRange.

        伸缩组最大实例数

        :return: The max of this IntegerRange.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this IntegerRange.

        伸缩组最大实例数

        :param max: The max of this IntegerRange.
        :type max: int
        """
        self._max = max

    @property
    def min(self):
        """Gets the min of this IntegerRange.

        伸缩组最小实例数

        :return: The min of this IntegerRange.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this IntegerRange.

        伸缩组最小实例数

        :param min: The min of this IntegerRange.
        :type min: int
        """
        self._min = min

    @property
    def desire(self):
        """Gets the desire of this IntegerRange.

        伸缩组期望实例数

        :return: The desire of this IntegerRange.
        :rtype: int
        """
        return self._desire

    @desire.setter
    def desire(self, desire):
        """Sets the desire of this IntegerRange.

        伸缩组期望实例数

        :param desire: The desire of this IntegerRange.
        :type desire: int
        """
        self._desire = desire

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
        if not isinstance(other, IntegerRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
