# coding: utf-8

import pprint
import re

import six





class ResourcePrice:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'arch': 'str',
        'price': 'float',
        'size': 'str',
        'type': 'str'
    }

    attribute_map = {
        'arch': 'arch',
        'price': 'price',
        'size': 'size',
        'type': 'type'
    }

    def __init__(self, arch=None, price=None, size=None, type=None):
        """ResourcePrice - a model defined in huaweicloud sdk"""
        
        

        self._arch = None
        self._price = None
        self._size = None
        self._type = None
        self.discriminator = None

        if arch is not None:
            self.arch = arch
        if price is not None:
            self.price = price
        if size is not None:
            self.size = size
        if type is not None:
            self.type = type

    @property
    def arch(self):
        """Gets the arch of this ResourcePrice.

        cpu架构 x86|arm

        :return: The arch of this ResourcePrice.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this ResourcePrice.

        cpu架构 x86|arm

        :param arch: The arch of this ResourcePrice.
        :type: str
        """
        self._arch = arch

    @property
    def price(self):
        """Gets the price of this ResourcePrice.

        价格

        :return: The price of this ResourcePrice.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this ResourcePrice.

        价格

        :param price: The price of this ResourcePrice.
        :type: float
        """
        self._price = price

    @property
    def size(self):
        """Gets the size of this ResourcePrice.

        规格。 类型为'storage'时，size值可以为5GB，10GB，20GB。 类型为'cpuMemory'时，arch为'x86'，size值可以为1U1G，2U4G；arch为'arm'，size值可以为4U8G。

        :return: The size of this ResourcePrice.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ResourcePrice.

        规格。 类型为'storage'时，size值可以为5GB，10GB，20GB。 类型为'cpuMemory'时，arch为'x86'，size值可以为1U1G，2U4G；arch为'arm'，size值可以为4U8G。

        :param size: The size of this ResourcePrice.
        :type: str
        """
        self._size = size

    @property
    def type(self):
        """Gets the type of this ResourcePrice.

        类型。目前可以取值storage，cpuMemory

        :return: The type of this ResourcePrice.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResourcePrice.

        类型。目前可以取值storage，cpuMemory

        :param type: The type of this ResourcePrice.
        :type: str
        """
        self._type = type

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
        if not isinstance(other, ResourcePrice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
