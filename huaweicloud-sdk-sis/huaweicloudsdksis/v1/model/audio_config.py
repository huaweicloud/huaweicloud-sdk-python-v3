# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AudioConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'audio_format': 'str',
        'language': 'str',
        'mode': 'str'
    }

    attribute_map = {
        'audio_format': 'audio_format',
        'language': 'language',
        'mode': 'mode'
    }

    def __init__(self, audio_format=None, language=None, mode=None):
        """AudioConfig

        The model defined in huaweicloud sdk

        :param audio_format: 语音的格式。不填写此字段，则默认为auto。注意音频不论何种格式，均要求采样率在16000Hz以上。  auto  自动判断，系统会自动判断并支持WAV（内部支持pcm/ulaw/alaw编码格式）、MP3、M4A、ogg-opus、AMR等格式。推荐使用此取值。  wav  wav格式。  aac  aac格式。  mp3  mp3格式。  amr  amr格式。  m4a  m4a格式。  opus  ogg-opus格式。 
        :type audio_format: str
        :param language: 评测语言  en_gb  英语-英式口音。
        :type language: str
        :param mode: 评测模式  word 单词模式  sentence 句子模式
        :type mode: str
        """
        
        

        self._audio_format = None
        self._language = None
        self._mode = None
        self.discriminator = None

        if audio_format is not None:
            self.audio_format = audio_format
        self.language = language
        self.mode = mode

    @property
    def audio_format(self):
        """Gets the audio_format of this AudioConfig.

        语音的格式。不填写此字段，则默认为auto。注意音频不论何种格式，均要求采样率在16000Hz以上。  auto  自动判断，系统会自动判断并支持WAV（内部支持pcm/ulaw/alaw编码格式）、MP3、M4A、ogg-opus、AMR等格式。推荐使用此取值。  wav  wav格式。  aac  aac格式。  mp3  mp3格式。  amr  amr格式。  m4a  m4a格式。  opus  ogg-opus格式。 

        :return: The audio_format of this AudioConfig.
        :rtype: str
        """
        return self._audio_format

    @audio_format.setter
    def audio_format(self, audio_format):
        """Sets the audio_format of this AudioConfig.

        语音的格式。不填写此字段，则默认为auto。注意音频不论何种格式，均要求采样率在16000Hz以上。  auto  自动判断，系统会自动判断并支持WAV（内部支持pcm/ulaw/alaw编码格式）、MP3、M4A、ogg-opus、AMR等格式。推荐使用此取值。  wav  wav格式。  aac  aac格式。  mp3  mp3格式。  amr  amr格式。  m4a  m4a格式。  opus  ogg-opus格式。 

        :param audio_format: The audio_format of this AudioConfig.
        :type audio_format: str
        """
        self._audio_format = audio_format

    @property
    def language(self):
        """Gets the language of this AudioConfig.

        评测语言  en_gb  英语-英式口音。

        :return: The language of this AudioConfig.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this AudioConfig.

        评测语言  en_gb  英语-英式口音。

        :param language: The language of this AudioConfig.
        :type language: str
        """
        self._language = language

    @property
    def mode(self):
        """Gets the mode of this AudioConfig.

        评测模式  word 单词模式  sentence 句子模式

        :return: The mode of this AudioConfig.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this AudioConfig.

        评测模式  word 单词模式  sentence 句子模式

        :param mode: The mode of this AudioConfig.
        :type mode: str
        """
        self._mode = mode

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
        if not isinstance(other, AudioConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
