# coding: utf-8

import pprint
import re

import six





class AudioTrack:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'int',
        'left': 'int',
        'right': 'int'
    }

    attribute_map = {
        'type': 'type',
        'left': 'left',
        'right': 'right'
    }

    def __init__(self, type=None, left=None, right=None):
        """AudioTrack - a model defined in huaweicloud sdk"""
        
        

        self._type = None
        self._left = None
        self._right = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if left is not None:
            self.left = left
        if right is not None:
            self.right = right

    @property
    def type(self):
        """Gets the type of this AudioTrack.

        音轨选取方式。 - 0：默认选取 - 1：手动选择 

        :return: The type of this AudioTrack.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AudioTrack.

        音轨选取方式。 - 0：默认选取 - 1：手动选择 

        :param type: The type of this AudioTrack.
        :type: int
        """
        self._type = type

    @property
    def left(self):
        """Gets the left of this AudioTrack.

        选取左声道所在的音轨编号。 

        :return: The left of this AudioTrack.
        :rtype: int
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this AudioTrack.

        选取左声道所在的音轨编号。 

        :param left: The left of this AudioTrack.
        :type: int
        """
        self._left = left

    @property
    def right(self):
        """Gets the right of this AudioTrack.

        选取右声道所在的音轨编号。 

        :return: The right of this AudioTrack.
        :rtype: int
        """
        return self._right

    @right.setter
    def right(self, right):
        """Sets the right of this AudioTrack.

        选取右声道所在的音轨编号。 

        :param right: The right of this AudioTrack.
        :type: int
        """
        self._right = right

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
        if not isinstance(other, AudioTrack):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
