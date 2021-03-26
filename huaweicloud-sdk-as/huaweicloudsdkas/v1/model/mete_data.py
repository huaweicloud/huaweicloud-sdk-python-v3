# coding: utf-8

import pprint
import re

import six





class MeteData:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'user_defined_key_value_pairs': 'str'
    }

    attribute_map = {
        'user_defined_key_value_pairs': 'User-defined_key-value_pairs'
    }

    def __init__(self, user_defined_key_value_pairs=None):
        """MeteData - a model defined in huaweicloud sdk"""
        
        

        self._user_defined_key_value_pairs = None
        self.discriminator = None

        if user_defined_key_value_pairs is not None:
            self.user_defined_key_value_pairs = user_defined_key_value_pairs

    @property
    def user_defined_key_value_pairs(self):
        """Gets the user_defined_key_value_pairs of this MeteData.

        metadata键、值。

        :return: The user_defined_key_value_pairs of this MeteData.
        :rtype: str
        """
        return self._user_defined_key_value_pairs

    @user_defined_key_value_pairs.setter
    def user_defined_key_value_pairs(self, user_defined_key_value_pairs):
        """Sets the user_defined_key_value_pairs of this MeteData.

        metadata键、值。

        :param user_defined_key_value_pairs: The user_defined_key_value_pairs of this MeteData.
        :type: str
        """
        self._user_defined_key_value_pairs = user_defined_key_value_pairs

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
        if not isinstance(other, MeteData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
