# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReplyAudioInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'audio_url': 'str',
        'audio_name': 'str'
    }

    attribute_map = {
        'audio_url': 'audio_url',
        'audio_name': 'audio_name'
    }

    def __init__(self, audio_url=None, audio_name=None):
        r"""ReplyAudioInfo

        The model defined in huaweicloud sdk

        :param audio_url: 音频URL
        :type audio_url: str
        :param audio_name: 音频名
        :type audio_name: str
        """
        
        

        self._audio_url = None
        self._audio_name = None
        self.discriminator = None

        if audio_url is not None:
            self.audio_url = audio_url
        if audio_name is not None:
            self.audio_name = audio_name

    @property
    def audio_url(self):
        r"""Gets the audio_url of this ReplyAudioInfo.

        音频URL

        :return: The audio_url of this ReplyAudioInfo.
        :rtype: str
        """
        return self._audio_url

    @audio_url.setter
    def audio_url(self, audio_url):
        r"""Sets the audio_url of this ReplyAudioInfo.

        音频URL

        :param audio_url: The audio_url of this ReplyAudioInfo.
        :type audio_url: str
        """
        self._audio_url = audio_url

    @property
    def audio_name(self):
        r"""Gets the audio_name of this ReplyAudioInfo.

        音频名

        :return: The audio_name of this ReplyAudioInfo.
        :rtype: str
        """
        return self._audio_name

    @audio_name.setter
    def audio_name(self, audio_name):
        r"""Sets the audio_name of this ReplyAudioInfo.

        音频名

        :param audio_name: The audio_name of this ReplyAudioInfo.
        :type audio_name: str
        """
        self._audio_name = audio_name

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
        if not isinstance(other, ReplyAudioInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
