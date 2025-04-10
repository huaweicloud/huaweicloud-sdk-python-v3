# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BaseDemand:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'min': 'int',
        'max': 'int'
    }

    attribute_map = {
        'min': 'min',
        'max': 'max'
    }

    def __init__(self, min=None, max=None):
        r"""BaseDemand

        The model defined in huaweicloud sdk

        :param min: 最小数
        :type min: int
        :param max: 最大数，最小值为1，最大值为1000。
        :type max: int
        """
        
        

        self._min = None
        self._max = None
        self.discriminator = None

        self.min = min
        self.max = max

    @property
    def min(self):
        r"""Gets the min of this BaseDemand.

        最小数

        :return: The min of this BaseDemand.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        r"""Sets the min of this BaseDemand.

        最小数

        :param min: The min of this BaseDemand.
        :type min: int
        """
        self._min = min

    @property
    def max(self):
        r"""Gets the max of this BaseDemand.

        最大数，最小值为1，最大值为1000。

        :return: The max of this BaseDemand.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        r"""Sets the max of this BaseDemand.

        最大数，最小值为1，最大值为1000。

        :param max: The max of this BaseDemand.
        :type max: int
        """
        self._max = max

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
        if not isinstance(other, BaseDemand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
