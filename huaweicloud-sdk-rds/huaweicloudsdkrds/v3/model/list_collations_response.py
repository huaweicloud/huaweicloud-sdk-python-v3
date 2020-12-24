# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListCollationsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'char_sets': 'list[str]'
    }

    attribute_map = {
        'char_sets': 'charSets'
    }

    def __init__(self, char_sets=None):
        """ListCollationsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._char_sets = None
        self.discriminator = None

        if char_sets is not None:
            self.char_sets = char_sets

    @property
    def char_sets(self):
        """Gets the char_sets of this ListCollationsResponse.

        字符集信息列表

        :return: The char_sets of this ListCollationsResponse.
        :rtype: list[str]
        """
        return self._char_sets

    @char_sets.setter
    def char_sets(self, char_sets):
        """Sets the char_sets of this ListCollationsResponse.

        字符集信息列表

        :param char_sets: The char_sets of this ListCollationsResponse.
        :type: list[str]
        """
        self._char_sets = char_sets

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
        if not isinstance(other, ListCollationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
