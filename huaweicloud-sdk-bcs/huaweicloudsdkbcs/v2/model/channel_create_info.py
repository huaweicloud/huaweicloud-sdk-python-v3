# coding: utf-8

import pprint
import re

import six





class ChannelCreateInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'channel_name': 'str',
        'channel_description': 'str'
    }

    attribute_map = {
        'channel_name': 'channel_name',
        'channel_description': 'channel_description'
    }

    def __init__(self, channel_name=None, channel_description=None):
        """ChannelCreateInfo - a model defined in huaweicloud sdk"""
        
        

        self._channel_name = None
        self._channel_description = None
        self.discriminator = None

        self.channel_name = channel_name
        if channel_description is not None:
            self.channel_description = channel_description

    @property
    def channel_name(self):
        """Gets the channel_name of this ChannelCreateInfo.

        通道名称，字符串长度4-24，必须包含a-z，0-9，以小写字母开头，以小写字母或者数字结尾

        :return: The channel_name of this ChannelCreateInfo.
        :rtype: str
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name):
        """Sets the channel_name of this ChannelCreateInfo.

        通道名称，字符串长度4-24，必须包含a-z，0-9，以小写字母开头，以小写字母或者数字结尾

        :param channel_name: The channel_name of this ChannelCreateInfo.
        :type: str
        """
        self._channel_name = channel_name

    @property
    def channel_description(self):
        """Gets the channel_description of this ChannelCreateInfo.

        通道描述

        :return: The channel_description of this ChannelCreateInfo.
        :rtype: str
        """
        return self._channel_description

    @channel_description.setter
    def channel_description(self, channel_description):
        """Sets the channel_description of this ChannelCreateInfo.

        通道描述

        :param channel_description: The channel_description of this ChannelCreateInfo.
        :type: str
        """
        self._channel_description = channel_description

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
        if not isinstance(other, ChannelCreateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
