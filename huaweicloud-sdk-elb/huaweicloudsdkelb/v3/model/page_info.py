# coding: utf-8

import pprint
import re

import six





class PageInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'previous_marker': 'str',
        'next_marker': 'str',
        'current_count': 'int'
    }

    attribute_map = {
        'previous_marker': 'previous_marker',
        'next_marker': 'next_marker',
        'current_count': 'current_count'
    }

    def __init__(self, previous_marker=None, next_marker=None, current_count=None):
        """PageInfo - a model defined in huaweicloud sdk"""
        
        

        self._previous_marker = None
        self._next_marker = None
        self._current_count = None
        self.discriminator = None

        self.previous_marker = previous_marker
        if next_marker is not None:
            self.next_marker = next_marker
        self.current_count = current_count

    @property
    def previous_marker(self):
        """Gets the previous_marker of this PageInfo.

        分页查询结果中第一条记录的ID

        :return: The previous_marker of this PageInfo.
        :rtype: str
        """
        return self._previous_marker

    @previous_marker.setter
    def previous_marker(self, previous_marker):
        """Sets the previous_marker of this PageInfo.

        分页查询结果中第一条记录的ID

        :param previous_marker: The previous_marker of this PageInfo.
        :type: str
        """
        self._previous_marker = previous_marker

    @property
    def next_marker(self):
        """Gets the next_marker of this PageInfo.

        分页查询结果中最后一条记录的ID。

        :return: The next_marker of this PageInfo.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        """Sets the next_marker of this PageInfo.

        分页查询结果中最后一条记录的ID。

        :param next_marker: The next_marker of this PageInfo.
        :type: str
        """
        self._next_marker = next_marker

    @property
    def current_count(self):
        """Gets the current_count of this PageInfo.

        当前的记录数。

        :return: The current_count of this PageInfo.
        :rtype: int
        """
        return self._current_count

    @current_count.setter
    def current_count(self, current_count):
        """Sets the current_count of this PageInfo.

        当前的记录数。

        :param current_count: The current_count of this PageInfo.
        :type: int
        """
        self._current_count = current_count

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
        if not isinstance(other, PageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
