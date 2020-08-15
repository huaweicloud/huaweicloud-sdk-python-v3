# coding: utf-8

import pprint
import re

import six





class DigitalWatermark:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'profile': 'str'
    }

    attribute_map = {
        'profile': 'profile'
    }

    def __init__(self, profile='MEDIUM'):
        """DigitalWatermark - a model defined in huaweicloud sdk"""
        
        

        self._profile = None
        self.discriminator = None

        self.profile = profile

    @property
    def profile(self):
        """Gets the profile of this DigitalWatermark.

        数字水印属性。 - ROBUST：水印鲁棒性最高 - MEDIUM：水印鲁棒性和视频质量折中(默认，暂时只支持该选项) - QUALITY：视频质量最好 - MEZZ：具有最高感官质量的水印 - CAMCORDING：最强大的水印配置文件，支持摄录攻击 

        :return: The profile of this DigitalWatermark.
        :rtype: str
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this DigitalWatermark.

        数字水印属性。 - ROBUST：水印鲁棒性最高 - MEDIUM：水印鲁棒性和视频质量折中(默认，暂时只支持该选项) - QUALITY：视频质量最好 - MEZZ：具有最高感官质量的水印 - CAMCORDING：最强大的水印配置文件，支持摄录攻击 

        :param profile: The profile of this DigitalWatermark.
        :type: str
        """
        self._profile = profile

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
        if not isinstance(other, DigitalWatermark):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
