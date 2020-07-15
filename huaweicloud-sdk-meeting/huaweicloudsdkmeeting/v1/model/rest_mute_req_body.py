# coding: utf-8

import pprint
import re

import six





class RestMuteReqBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'is_mute': 'int',
        'allow_unmute_by_oneself': 'int'
    }

    attribute_map = {
        'is_mute': 'isMute',
        'allow_unmute_by_oneself': 'allowUnmuteByOneself'
    }

    def __init__(self, is_mute=None, allow_unmute_by_oneself=1):
        """RestMuteReqBody - a model defined in huaweicloud sdk"""
        
        

        self._is_mute = None
        self._allow_unmute_by_oneself = None
        self.discriminator = None

        self.is_mute = is_mute
        if allow_unmute_by_oneself is not None:
            self.allow_unmute_by_oneself = allow_unmute_by_oneself

    @property
    def is_mute(self):
        """Gets the is_mute of this RestMuteReqBody.

        - 0: 取消静音。 - 1: 静音。

        :return: The is_mute of this RestMuteReqBody.
        :rtype: int
        """
        return self._is_mute

    @is_mute.setter
    def is_mute(self, is_mute):
        """Sets the is_mute of this RestMuteReqBody.

        - 0: 取消静音。 - 1: 静音。

        :param is_mute: The is_mute of this RestMuteReqBody.
        :type: int
        """
        self._is_mute = is_mute

    @property
    def allow_unmute_by_oneself(self):
        """Gets the allow_unmute_by_oneself of this RestMuteReqBody.

        是否允许自己解除静音（仅静音时有效），默认为允许。 - 0: 不允许。 - 1: 允许。

        :return: The allow_unmute_by_oneself of this RestMuteReqBody.
        :rtype: int
        """
        return self._allow_unmute_by_oneself

    @allow_unmute_by_oneself.setter
    def allow_unmute_by_oneself(self, allow_unmute_by_oneself):
        """Sets the allow_unmute_by_oneself of this RestMuteReqBody.

        是否允许自己解除静音（仅静音时有效），默认为允许。 - 0: 不允许。 - 1: 允许。

        :param allow_unmute_by_oneself: The allow_unmute_by_oneself of this RestMuteReqBody.
        :type: int
        """
        self._allow_unmute_by_oneself = allow_unmute_by_oneself

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
        if not isinstance(other, RestMuteReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
