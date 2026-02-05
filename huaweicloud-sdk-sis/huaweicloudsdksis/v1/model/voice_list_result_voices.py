# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VoiceListResultVoices:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'voice_name': 'str',
        'language': 'str'
    }

    attribute_map = {
        'voice_name': 'voice_name',
        'language': 'language'
    }

    def __init__(self, voice_name=None, language=None):
        r"""VoiceListResultVoices

        The model defined in huaweicloud sdk

        :param voice_name: 注册成功的声音名称。
        :type voice_name: str
        :param language: 注册成功的声音语种。
        :type language: str
        """
        
        

        self._voice_name = None
        self._language = None
        self.discriminator = None

        if voice_name is not None:
            self.voice_name = voice_name
        if language is not None:
            self.language = language

    @property
    def voice_name(self):
        r"""Gets the voice_name of this VoiceListResultVoices.

        注册成功的声音名称。

        :return: The voice_name of this VoiceListResultVoices.
        :rtype: str
        """
        return self._voice_name

    @voice_name.setter
    def voice_name(self, voice_name):
        r"""Sets the voice_name of this VoiceListResultVoices.

        注册成功的声音名称。

        :param voice_name: The voice_name of this VoiceListResultVoices.
        :type voice_name: str
        """
        self._voice_name = voice_name

    @property
    def language(self):
        r"""Gets the language of this VoiceListResultVoices.

        注册成功的声音语种。

        :return: The language of this VoiceListResultVoices.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this VoiceListResultVoices.

        注册成功的声音语种。

        :param language: The language of this VoiceListResultVoices.
        :type language: str
        """
        self._language = language

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VoiceListResultVoices):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
