# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Substring:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start': 'int',
        'length': 'int'
    }

    attribute_map = {
        'start': 'start',
        'length': 'length'
    }

    def __init__(self, start=None, length=None):
        r"""Substring

        The model defined in huaweicloud sdk

        :param start: 子字符串的起始索引，从0开始。0表示第一个字符。
        :type start: int
        :param length: 子字符串的长度。
        :type length: int
        """
        
        

        self._start = None
        self._length = None
        self.discriminator = None

        self.start = start
        self.length = length

    @property
    def start(self):
        r"""Gets the start of this Substring.

        子字符串的起始索引，从0开始。0表示第一个字符。

        :return: The start of this Substring.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this Substring.

        子字符串的起始索引，从0开始。0表示第一个字符。

        :param start: The start of this Substring.
        :type start: int
        """
        self._start = start

    @property
    def length(self):
        r"""Gets the length of this Substring.

        子字符串的长度。

        :return: The length of this Substring.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        r"""Sets the length of this Substring.

        子字符串的长度。

        :param length: The length of this Substring.
        :type length: int
        """
        self._length = length

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
        if not isinstance(other, Substring):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
