# coding: utf-8

import pprint
import re

import six





class ListInstancesStorageResult:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'size': 'str',
        'used': 'str'
    }

    attribute_map = {
        'size': 'size',
        'used': 'used'
    }

    def __init__(self, size=None, used=None):
        """ListInstancesStorageResult - a model defined in huaweicloud sdk"""
        
        

        self._size = None
        self._used = None
        self.discriminator = None

        if size is not None:
            self.size = size
        if used is not None:
            self.used = used

    @property
    def size(self):
        """Gets the size of this ListInstancesStorageResult.

        磁盘大小。单位：GB。

        :return: The size of this ListInstancesStorageResult.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListInstancesStorageResult.

        磁盘大小。单位：GB。

        :param size: The size of this ListInstancesStorageResult.
        :type: str
        """
        self._size = size

    @property
    def used(self):
        """Gets the used of this ListInstancesStorageResult.

        磁盘使用量。单位：GB。

        :return: The used of this ListInstancesStorageResult.
        :rtype: str
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this ListInstancesStorageResult.

        磁盘使用量。单位：GB。

        :param used: The used of this ListInstancesStorageResult.
        :type: str
        """
        self._used = used

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
        if not isinstance(other, ListInstancesStorageResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
