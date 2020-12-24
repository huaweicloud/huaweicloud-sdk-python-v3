# coding: utf-8

import pprint
import re

import six





class EnlargeVolume:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'size': 'int',
        'is_auto_pay': 'bool'
    }

    attribute_map = {
        'size': 'size',
        'is_auto_pay': 'is_auto_pay'
    }

    def __init__(self, size=None, is_auto_pay=None):
        """EnlargeVolume - a model defined in huaweicloud sdk"""
        
        

        self._size = None
        self._is_auto_pay = None
        self.discriminator = None

        self.size = size
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def size(self):
        """Gets the size of this EnlargeVolume.

        扩容到该参数指定的大小，单位为GB。

        :return: The size of this EnlargeVolume.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this EnlargeVolume.

        扩容到该参数指定的大小，单位为GB。

        :param size: The size of this EnlargeVolume.
        :type: int
        """
        self._size = size

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this EnlargeVolume.

        变更包周期实例的规格时可指定，表示是否自动从客户的账户中支付。

        :return: The is_auto_pay of this EnlargeVolume.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this EnlargeVolume.

        变更包周期实例的规格时可指定，表示是否自动从客户的账户中支付。

        :param is_auto_pay: The is_auto_pay of this EnlargeVolume.
        :type: bool
        """
        self._is_auto_pay = is_auto_pay

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
        if not isinstance(other, EnlargeVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
