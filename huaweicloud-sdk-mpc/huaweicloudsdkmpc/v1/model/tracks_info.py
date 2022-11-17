# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        """TracksInfo

        The model defined in huaweicloud sdk

        :param channel_layout: 音频轨的声道layout 
        :type channel_layout: str
        :param language: 音频轨对应语言描述 
        :type language: str
        """
        
        

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
        :type channel_layout: str
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
        :type language: str
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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TracksInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
