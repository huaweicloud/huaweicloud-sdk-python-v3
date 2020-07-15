# coding: utf-8

import pprint
import re

import six





class UpdateDesireds:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'shadow': 'list[UpdateDesired]'
    }

    attribute_map = {
        'shadow': 'shadow'
    }

    def __init__(self, shadow=None):
        """UpdateDesireds - a model defined in huaweicloud sdk"""
        
        

        self._shadow = None
        self.discriminator = None

        if shadow is not None:
            self.shadow = shadow

    @property
    def shadow(self):
        """Gets the shadow of this UpdateDesireds.

        设备影子期望值构体。

        :return: The shadow of this UpdateDesireds.
        :rtype: list[UpdateDesired]
        """
        return self._shadow

    @shadow.setter
    def shadow(self, shadow):
        """Sets the shadow of this UpdateDesireds.

        设备影子期望值构体。

        :param shadow: The shadow of this UpdateDesireds.
        :type: list[UpdateDesired]
        """
        self._shadow = shadow

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
        if not isinstance(other, UpdateDesireds):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
