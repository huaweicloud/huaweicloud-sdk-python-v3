# coding: utf-8

import pprint
import re

import six





class TracksInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'channel_layout': 'str',
        'language': 'str'
    }

    attribute_map = {
        'channel_layout': 'channel_layout',
        'language': 'language'
    }

    def __init__(self, channel_layout=None, language=None):
        """TracksInfo - a model defined in huaweicloud sdk"""
        
        

        self._channel_layout = None
        self._language = None
        self.discriminator = None

        if channel_layout is not None:
            self.channel_layout = channel_layout
        if language is not None:
            self.language = language

    @property
    def channel_layout(self):
        """Gets the channel_layout of this TracksInfo.

        音频轨的声道layout 

        :return: The channel_layout of this TracksInfo.
        :rtype: str
        """
        return self._channel_layout

    @channel_layout.setter
    def channel_layout(self, channel_layout):
        """Sets the channel_layout of this TracksInfo.

        音频轨的声道layout 

        :param channel_layout: The channel_layout of this TracksInfo.
        :type: str
        """
        self._channel_layout = channel_layout

    @property
    def language(self):
        """Gets the language of this TracksInfo.

        音频轨对应语言描述 

        :return: The language of this TracksInfo.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this TracksInfo.

        音频轨对应语言描述 

        :param language: The language of this TracksInfo.
        :type: str
        """
        self._language = language

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
        if not isinstance(other, TracksInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
