# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShootScriptDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'script_type': 'str',
        'text_config': 'TextConfig',
        'audio_drive_action_config': 'list[AudioDriveActionConfig]',
        'background_config': 'list[BackgroundConfigInfo]',
        'layer_config': 'list[LayerConfig]',
        'thumbnail_url': 'str'
    }

    attribute_map = {
        'script_type': 'script_type',
        'text_config': 'text_config',
        'audio_drive_action_config': 'audio_drive_action_config',
        'background_config': 'background_config',
        'layer_config': 'layer_config',
        'thumbnail_url': 'thumbnail_url'
    }

    def __init__(self, script_type=None, text_config=None, audio_drive_action_config=None, background_config=None, layer_config=None, thumbnail_url=None):
        """ShootScriptDetail

        The model defined in huaweicloud sdk

        :param script_type: **参数解释**： 脚本类型，即视频制作的驱动方式 **约束限制**： 不涉及 **取值范围** * TEXT: 文本驱动，即通过TTS合成语音 * AUDIO: 语音驱动
        :type script_type: str
        :param text_config: 
        :type text_config: :class:`huaweicloudsdkmetastudio.v1.TextConfig`
        :param audio_drive_action_config: 语音驱动时的动作配置。
        :type audio_drive_action_config: list[:class:`huaweicloudsdkmetastudio.v1.AudioDriveActionConfig`]
        :param background_config: 背景配置。
        :type background_config: list[:class:`huaweicloudsdkmetastudio.v1.BackgroundConfigInfo`]
        :param layer_config: 图层配置。
        :type layer_config: list[:class:`huaweicloudsdkmetastudio.v1.LayerConfig`]
        :param thumbnail_url: **参数解释**： 剧本场景缩略图url。 **约束限制**： 不涉及。 **取值范围**： 字符长度1-2048位。 **默认取值**： 不涉及。
        :type thumbnail_url: str
        """
        
        

        self._script_type = None
        self._text_config = None
        self._audio_drive_action_config = None
        self._background_config = None
        self._layer_config = None
        self._thumbnail_url = None
        self.discriminator = None

        if script_type is not None:
            self.script_type = script_type
        if text_config is not None:
            self.text_config = text_config
        if audio_drive_action_config is not None:
            self.audio_drive_action_config = audio_drive_action_config
        if background_config is not None:
            self.background_config = background_config
        if layer_config is not None:
            self.layer_config = layer_config
        if thumbnail_url is not None:
            self.thumbnail_url = thumbnail_url

    @property
    def script_type(self):
        """Gets the script_type of this ShootScriptDetail.

        **参数解释**： 脚本类型，即视频制作的驱动方式 **约束限制**： 不涉及 **取值范围** * TEXT: 文本驱动，即通过TTS合成语音 * AUDIO: 语音驱动

        :return: The script_type of this ShootScriptDetail.
        :rtype: str
        """
        return self._script_type

    @script_type.setter
    def script_type(self, script_type):
        """Sets the script_type of this ShootScriptDetail.

        **参数解释**： 脚本类型，即视频制作的驱动方式 **约束限制**： 不涉及 **取值范围** * TEXT: 文本驱动，即通过TTS合成语音 * AUDIO: 语音驱动

        :param script_type: The script_type of this ShootScriptDetail.
        :type script_type: str
        """
        self._script_type = script_type

    @property
    def text_config(self):
        """Gets the text_config of this ShootScriptDetail.

        :return: The text_config of this ShootScriptDetail.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.TextConfig`
        """
        return self._text_config

    @text_config.setter
    def text_config(self, text_config):
        """Sets the text_config of this ShootScriptDetail.

        :param text_config: The text_config of this ShootScriptDetail.
        :type text_config: :class:`huaweicloudsdkmetastudio.v1.TextConfig`
        """
        self._text_config = text_config

    @property
    def audio_drive_action_config(self):
        """Gets the audio_drive_action_config of this ShootScriptDetail.

        语音驱动时的动作配置。

        :return: The audio_drive_action_config of this ShootScriptDetail.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.AudioDriveActionConfig`]
        """
        return self._audio_drive_action_config

    @audio_drive_action_config.setter
    def audio_drive_action_config(self, audio_drive_action_config):
        """Sets the audio_drive_action_config of this ShootScriptDetail.

        语音驱动时的动作配置。

        :param audio_drive_action_config: The audio_drive_action_config of this ShootScriptDetail.
        :type audio_drive_action_config: list[:class:`huaweicloudsdkmetastudio.v1.AudioDriveActionConfig`]
        """
        self._audio_drive_action_config = audio_drive_action_config

    @property
    def background_config(self):
        """Gets the background_config of this ShootScriptDetail.

        背景配置。

        :return: The background_config of this ShootScriptDetail.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.BackgroundConfigInfo`]
        """
        return self._background_config

    @background_config.setter
    def background_config(self, background_config):
        """Sets the background_config of this ShootScriptDetail.

        背景配置。

        :param background_config: The background_config of this ShootScriptDetail.
        :type background_config: list[:class:`huaweicloudsdkmetastudio.v1.BackgroundConfigInfo`]
        """
        self._background_config = background_config

    @property
    def layer_config(self):
        """Gets the layer_config of this ShootScriptDetail.

        图层配置。

        :return: The layer_config of this ShootScriptDetail.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.LayerConfig`]
        """
        return self._layer_config

    @layer_config.setter
    def layer_config(self, layer_config):
        """Sets the layer_config of this ShootScriptDetail.

        图层配置。

        :param layer_config: The layer_config of this ShootScriptDetail.
        :type layer_config: list[:class:`huaweicloudsdkmetastudio.v1.LayerConfig`]
        """
        self._layer_config = layer_config

    @property
    def thumbnail_url(self):
        """Gets the thumbnail_url of this ShootScriptDetail.

        **参数解释**： 剧本场景缩略图url。 **约束限制**： 不涉及。 **取值范围**： 字符长度1-2048位。 **默认取值**： 不涉及。

        :return: The thumbnail_url of this ShootScriptDetail.
        :rtype: str
        """
        return self._thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, thumbnail_url):
        """Sets the thumbnail_url of this ShootScriptDetail.

        **参数解释**： 剧本场景缩略图url。 **约束限制**： 不涉及。 **取值范围**： 字符长度1-2048位。 **默认取值**： 不涉及。

        :param thumbnail_url: The thumbnail_url of this ShootScriptDetail.
        :type thumbnail_url: str
        """
        self._thumbnail_url = thumbnail_url

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
        if not isinstance(other, ShootScriptDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
