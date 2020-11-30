# coding: utf-8

import pprint
import re

import six





class HttpCode:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'code': 'int',
        'count': 'int',
        'proportion': 'float'
    }

    attribute_map = {
        'code': 'code',
        'count': 'count',
        'proportion': 'proportion'
    }

    def __init__(self, code=None, count=None, proportion=None):
        """HttpCode - a model defined in huaweicloud sdk"""
        
        

        self._code = None
        self._count = None
        self._proportion = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if count is not None:
            self.count = count
        if proportion is not None:
            self.proportion = proportion

    @property
    def code(self):
        """Gets the code of this HttpCode.

        状态码

        :return: The code of this HttpCode.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this HttpCode.

        状态码

        :param code: The code of this HttpCode.
        :type: int
        """
        self._code = code

    @property
    def count(self):
        """Gets the count of this HttpCode.

        状态码出现次数

        :return: The count of this HttpCode.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this HttpCode.

        状态码出现次数

        :param count: The count of this HttpCode.
        :type: int
        """
        self._count = count

    @property
    def proportion(self):
        """Gets the proportion of this HttpCode.

        状态码在对应时间点中的占比，保留4位小数。 

        :return: The proportion of this HttpCode.
        :rtype: float
        """
        return self._proportion

    @proportion.setter
    def proportion(self, proportion):
        """Sets the proportion of this HttpCode.

        状态码在对应时间点中的占比，保留4位小数。 

        :param proportion: The proportion of this HttpCode.
        :type: float
        """
        self._proportion = proportion

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HttpCode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
