# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EncoderSettingsExpandAudioDescriptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'audio_selector_name': 'str',
        'language_code_control': 'str',
        'language_code': 'str',
        'stream_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'audio_selector_name': 'audio_selector_name',
        'language_code_control': 'language_code_control',
        'language_code': 'language_code',
        'stream_name': 'stream_name'
    }

    def __init__(self, name=None, audio_selector_name=None, language_code_control=None, language_code=None, stream_name=None):
        r"""EncoderSettingsExpandAudioDescriptions

        The model defined in huaweicloud sdk

        :param name: 音频输出配置的名称。仅支持大小写字母，数字，中划线（-），下划线（_）。  同一个频道不同的音频输出配置名称，不允许重复。
        :type name: str
        :param audio_selector_name: 音频选择器名称
        :type audio_selector_name: str
        :param language_code_control: 语言代码控制。这里的设置不会修改音频实际的语言，只会修改音频对外展示的语言。  包含如下选项： - FOLLOW_INPUT：如果所选音频选择器对应的输出音频有语言，则与其保持一致，否则会以这里配置的语言代码和流名称进行兜底。推荐当前选项，为默认值。 - USE_CONFIGURED：用户根据实际情况自定义输出音频的语言和流名称。
        :type language_code_control: str
        :param language_code: 语言代码，输入2或3个小写字母。
        :type language_code: str
        :param stream_name: 流名称
        :type stream_name: str
        """
        
        

        self._name = None
        self._audio_selector_name = None
        self._language_code_control = None
        self._language_code = None
        self._stream_name = None
        self.discriminator = None

        self.name = name
        self.audio_selector_name = audio_selector_name
        if language_code_control is not None:
            self.language_code_control = language_code_control
        if language_code is not None:
            self.language_code = language_code
        if stream_name is not None:
            self.stream_name = stream_name

    @property
    def name(self):
        r"""Gets the name of this EncoderSettingsExpandAudioDescriptions.

        音频输出配置的名称。仅支持大小写字母，数字，中划线（-），下划线（_）。  同一个频道不同的音频输出配置名称，不允许重复。

        :return: The name of this EncoderSettingsExpandAudioDescriptions.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EncoderSettingsExpandAudioDescriptions.

        音频输出配置的名称。仅支持大小写字母，数字，中划线（-），下划线（_）。  同一个频道不同的音频输出配置名称，不允许重复。

        :param name: The name of this EncoderSettingsExpandAudioDescriptions.
        :type name: str
        """
        self._name = name

    @property
    def audio_selector_name(self):
        r"""Gets the audio_selector_name of this EncoderSettingsExpandAudioDescriptions.

        音频选择器名称

        :return: The audio_selector_name of this EncoderSettingsExpandAudioDescriptions.
        :rtype: str
        """
        return self._audio_selector_name

    @audio_selector_name.setter
    def audio_selector_name(self, audio_selector_name):
        r"""Sets the audio_selector_name of this EncoderSettingsExpandAudioDescriptions.

        音频选择器名称

        :param audio_selector_name: The audio_selector_name of this EncoderSettingsExpandAudioDescriptions.
        :type audio_selector_name: str
        """
        self._audio_selector_name = audio_selector_name

    @property
    def language_code_control(self):
        r"""Gets the language_code_control of this EncoderSettingsExpandAudioDescriptions.

        语言代码控制。这里的设置不会修改音频实际的语言，只会修改音频对外展示的语言。  包含如下选项： - FOLLOW_INPUT：如果所选音频选择器对应的输出音频有语言，则与其保持一致，否则会以这里配置的语言代码和流名称进行兜底。推荐当前选项，为默认值。 - USE_CONFIGURED：用户根据实际情况自定义输出音频的语言和流名称。

        :return: The language_code_control of this EncoderSettingsExpandAudioDescriptions.
        :rtype: str
        """
        return self._language_code_control

    @language_code_control.setter
    def language_code_control(self, language_code_control):
        r"""Sets the language_code_control of this EncoderSettingsExpandAudioDescriptions.

        语言代码控制。这里的设置不会修改音频实际的语言，只会修改音频对外展示的语言。  包含如下选项： - FOLLOW_INPUT：如果所选音频选择器对应的输出音频有语言，则与其保持一致，否则会以这里配置的语言代码和流名称进行兜底。推荐当前选项，为默认值。 - USE_CONFIGURED：用户根据实际情况自定义输出音频的语言和流名称。

        :param language_code_control: The language_code_control of this EncoderSettingsExpandAudioDescriptions.
        :type language_code_control: str
        """
        self._language_code_control = language_code_control

    @property
    def language_code(self):
        r"""Gets the language_code of this EncoderSettingsExpandAudioDescriptions.

        语言代码，输入2或3个小写字母。

        :return: The language_code of this EncoderSettingsExpandAudioDescriptions.
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        r"""Sets the language_code of this EncoderSettingsExpandAudioDescriptions.

        语言代码，输入2或3个小写字母。

        :param language_code: The language_code of this EncoderSettingsExpandAudioDescriptions.
        :type language_code: str
        """
        self._language_code = language_code

    @property
    def stream_name(self):
        r"""Gets the stream_name of this EncoderSettingsExpandAudioDescriptions.

        流名称

        :return: The stream_name of this EncoderSettingsExpandAudioDescriptions.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        r"""Sets the stream_name of this EncoderSettingsExpandAudioDescriptions.

        流名称

        :param stream_name: The stream_name of this EncoderSettingsExpandAudioDescriptions.
        :type stream_name: str
        """
        self._stream_name = stream_name

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
        if not isinstance(other, EncoderSettingsExpandAudioDescriptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
