# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegisterVoiceReqConfig:

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
        r"""RegisterVoiceReqConfig

        The model defined in huaweicloud sdk

        :param voice_name: 注册声音的名称，不能以数字、下划线开头。仅包含大、小写英文字母、数字和下划线，且长度不超过20个字符。一个project id下的声音名称不能重复。
        :type voice_name: str
        :param language: data中语音数据的语种，取值chinese、english。 默认是chinese。
        :type language: str
        """
        
        

        self._voice_name = None
        self._language = None
        self.discriminator = None

        self.voice_name = voice_name
        if language is not None:
            self.language = language

    @property
    def voice_name(self):
        r"""Gets the voice_name of this RegisterVoiceReqConfig.

        注册声音的名称，不能以数字、下划线开头。仅包含大、小写英文字母、数字和下划线，且长度不超过20个字符。一个project id下的声音名称不能重复。

        :return: The voice_name of this RegisterVoiceReqConfig.
        :rtype: str
        """
        return self._voice_name

    @voice_name.setter
    def voice_name(self, voice_name):
        r"""Sets the voice_name of this RegisterVoiceReqConfig.

        注册声音的名称，不能以数字、下划线开头。仅包含大、小写英文字母、数字和下划线，且长度不超过20个字符。一个project id下的声音名称不能重复。

        :param voice_name: The voice_name of this RegisterVoiceReqConfig.
        :type voice_name: str
        """
        self._voice_name = voice_name

    @property
    def language(self):
        r"""Gets the language of this RegisterVoiceReqConfig.

        data中语音数据的语种，取值chinese、english。 默认是chinese。

        :return: The language of this RegisterVoiceReqConfig.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this RegisterVoiceReqConfig.

        data中语音数据的语种，取值chinese、english。 默认是chinese。

        :param language: The language of this RegisterVoiceReqConfig.
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
        if not isinstance(other, RegisterVoiceReqConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
