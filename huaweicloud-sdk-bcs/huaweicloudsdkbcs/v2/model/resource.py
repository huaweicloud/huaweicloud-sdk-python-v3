# coding: utf-8

import pprint
import re

import six





class Resource:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'unit': 'str',
        'min': 'int',
        'max': 'int',
        'quota': 'int',
        'used': 'int',
        'free': 'int'
    }

    attribute_map = {
        'type': 'type',
        'unit': 'unit',
        'min': 'min',
        'max': 'max',
        'quota': 'quota',
        'used': 'used',
        'free': 'free'
    }

    def __init__(self, type=None, unit=None, min=None, max=None, quota=None, used=None, free=None):
        """Resource - a model defined in huaweicloud sdk"""
        
        

        self._type = None
        self._unit = None
        self._min = None
        self._max = None
        self._quota = None
        self._used = None
        self._free = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if unit is not None:
            self.unit = unit
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if quota is not None:
            self.quota = quota
        if used is not None:
            self.used = used
        if free is not None:
            self.free = free

    @property
    def type(self):
        """Gets the type of this Resource.

        资源类型，包含instance（服务实例数）和peers（总peer数）两种

        :return: The type of this Resource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Resource.

        资源类型，包含instance（服务实例数）和peers（总peer数）两种

        :param type: The type of this Resource.
        :type: str
        """
        self._type = type

    @property
    def unit(self):
        """Gets the unit of this Resource.

        单位

        :return: The unit of this Resource.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Resource.

        单位

        :param unit: The unit of this Resource.
        :type: str
        """
        self._unit = unit

    @property
    def min(self):
        """Gets the min of this Resource.

        最小值

        :return: The min of this Resource.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this Resource.

        最小值

        :param min: The min of this Resource.
        :type: int
        """
        self._min = min

    @property
    def max(self):
        """Gets the max of this Resource.

        最大值

        :return: The max of this Resource.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this Resource.

        最大值

        :param max: The max of this Resource.
        :type: int
        """
        self._max = max

    @property
    def quota(self):
        """Gets the quota of this Resource.

        配额

        :return: The quota of this Resource.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this Resource.

        配额

        :param quota: The quota of this Resource.
        :type: int
        """
        self._quota = quota

    @property
    def used(self):
        """Gets the used of this Resource.

        已使用配额

        :return: The used of this Resource.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this Resource.

        已使用配额

        :param used: The used of this Resource.
        :type: int
        """
        self._used = used

    @property
    def free(self):
        """Gets the free of this Resource.

        剩余配额

        :return: The free of this Resource.
        :rtype: int
        """
        return self._free

    @free.setter
    def free(self, free):
        """Sets the free of this Resource.

        剩余配额

        :param free: The free of this Resource.
        :type: int
        """
        self._free = free

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
        if not isinstance(other, Resource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
