# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LiveAudioConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_id': 'str',
        'audio_url': 'str',
        'subtitle_url': 'str'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'audio_url': 'audio_url',
        'subtitle_url': 'subtitle_url'
    }

    def __init__(self, asset_id=None, audio_url=None, subtitle_url=None):
        r"""LiveAudioConfig

        The model defined in huaweicloud sdk

        :param asset_id: **参数解释**： 插入音频资产的资产id，外部资产信息无需填写。若填写，可以从资产库中查询。 **约束限制**： 不涉及 **取值范围**： 字符长度0-64位。 **默认取值**： 不涉及。
        :type asset_id: str
        :param audio_url: **参数解释**： 音频URL。 **约束限制**： 仅支持MP3格式，大小&lt;100MB。输出会自动转化为单声道16KHZ采样。 **取值范围**： 字符长度0-2048位。 **默认取值**： 不涉及。
        :type audio_url: str
        :param subtitle_url: **参数解释**： 音频对应的字幕文件URL。 **约束限制**： 仅SRT格式，大小&lt;1MB。 **取值范围**： 字符长度0-2048位。 **默认取值**： 不涉及。
        :type subtitle_url: str
        """
        
        

        self._asset_id = None
        self._audio_url = None
        self._subtitle_url = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if audio_url is not None:
            self.audio_url = audio_url
        if subtitle_url is not None:
            self.subtitle_url = subtitle_url

    @property
    def asset_id(self):
        r"""Gets the asset_id of this LiveAudioConfig.

        **参数解释**： 插入音频资产的资产id，外部资产信息无需填写。若填写，可以从资产库中查询。 **约束限制**： 不涉及 **取值范围**： 字符长度0-64位。 **默认取值**： 不涉及。

        :return: The asset_id of this LiveAudioConfig.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this LiveAudioConfig.

        **参数解释**： 插入音频资产的资产id，外部资产信息无需填写。若填写，可以从资产库中查询。 **约束限制**： 不涉及 **取值范围**： 字符长度0-64位。 **默认取值**： 不涉及。

        :param asset_id: The asset_id of this LiveAudioConfig.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def audio_url(self):
        r"""Gets the audio_url of this LiveAudioConfig.

        **参数解释**： 音频URL。 **约束限制**： 仅支持MP3格式，大小<100MB。输出会自动转化为单声道16KHZ采样。 **取值范围**： 字符长度0-2048位。 **默认取值**： 不涉及。

        :return: The audio_url of this LiveAudioConfig.
        :rtype: str
        """
        return self._audio_url

    @audio_url.setter
    def audio_url(self, audio_url):
        r"""Sets the audio_url of this LiveAudioConfig.

        **参数解释**： 音频URL。 **约束限制**： 仅支持MP3格式，大小<100MB。输出会自动转化为单声道16KHZ采样。 **取值范围**： 字符长度0-2048位。 **默认取值**： 不涉及。

        :param audio_url: The audio_url of this LiveAudioConfig.
        :type audio_url: str
        """
        self._audio_url = audio_url

    @property
    def subtitle_url(self):
        r"""Gets the subtitle_url of this LiveAudioConfig.

        **参数解释**： 音频对应的字幕文件URL。 **约束限制**： 仅SRT格式，大小<1MB。 **取值范围**： 字符长度0-2048位。 **默认取值**： 不涉及。

        :return: The subtitle_url of this LiveAudioConfig.
        :rtype: str
        """
        return self._subtitle_url

    @subtitle_url.setter
    def subtitle_url(self, subtitle_url):
        r"""Sets the subtitle_url of this LiveAudioConfig.

        **参数解释**： 音频对应的字幕文件URL。 **约束限制**： 仅SRT格式，大小<1MB。 **取值范围**： 字符长度0-2048位。 **默认取值**： 不涉及。

        :param subtitle_url: The subtitle_url of this LiveAudioConfig.
        :type subtitle_url: str
        """
        self._subtitle_url = subtitle_url

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
        if not isinstance(other, LiveAudioConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
