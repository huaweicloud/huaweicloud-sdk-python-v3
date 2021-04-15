# coding: utf-8

import pprint
import re

import six





class VideoExtendSettings:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'preset': 'str'
    }

    attribute_map = {
        'preset': 'preset'
    }

    def __init__(self, preset=None):
        """VideoExtendSettings - a model defined in huaweicloud sdk"""
        
        

        self._preset = None
        self.discriminator = None

        if preset is not None:
            self.preset = preset

    @property
    def preset(self):
        """Gets the preset of this VideoExtendSettings.

        扩展编码质量等级，用于覆盖模板中的同名参数。取值如下： - SPEED - HIGHQUALITY 

        :return: The preset of this VideoExtendSettings.
        :rtype: str
        """
        return self._preset

    @preset.setter
    def preset(self, preset):
        """Sets the preset of this VideoExtendSettings.

        扩展编码质量等级，用于覆盖模板中的同名参数。取值如下： - SPEED - HIGHQUALITY 

        :param preset: The preset of this VideoExtendSettings.
        :type: str
        """
        self._preset = preset

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
        if not isinstance(other, VideoExtendSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
