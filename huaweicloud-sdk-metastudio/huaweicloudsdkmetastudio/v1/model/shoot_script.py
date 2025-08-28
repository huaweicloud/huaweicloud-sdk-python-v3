# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShootScript:

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
        'audio_duration': 'float',
        'audio_drive_action_config': 'list[AudioDriveActionConfig]',
        'audio_drive_file_external_url': 'str',
        'background_config': 'list[BackgroundConfigInfo]',
        'layer_config': 'list[LayerConfig]',
        'audio_config': 'AudioInfo'
    }

    attribute_map = {
        'script_type': 'script_type',
        'text_config': 'text_config',
        'audio_duration': 'audio_duration',
        'audio_drive_action_config': 'audio_drive_action_config',
        'audio_drive_file_external_url': 'audio_drive_file_external_url',
        'background_config': 'background_config',
        'layer_config': 'layer_config',
        'audio_config': 'audio_config'
    }

    def __init__(self, script_type=None, text_config=None, audio_duration=None, audio_drive_action_config=None, audio_drive_file_external_url=None, background_config=None, layer_config=None, audio_config=None):
        r"""ShootScript

        The model defined in huaweicloud sdk

        :param script_type: **参数解释**： 脚本类型，即视频制作的驱动方式 **约束限制**： 不涉及 **取值范围** * TEXT: 文本驱动，即通过TTS合成语音 * AUDIO: 语音驱动
        :type script_type: str
        :param text_config: 
        :type text_config: :class:`huaweicloudsdkmetastudio.v1.TextConfig`
        :param audio_duration: 语音驱动时，音频时长，单位秒。 &gt; * 创建剧本时此参数可以不设置，音频文件上传成功后，通过更新剧本接口设置 &gt; * 查询剧本详情时，返回音频时长，用于预估视频时长
        :type audio_duration: float
        :param audio_drive_action_config: 语音驱动时的动作配置。
        :type audio_drive_action_config: list[:class:`huaweicloudsdkmetastudio.v1.AudioDriveActionConfig`]
        :param audio_drive_file_external_url: 语音驱动音频文件外部下载URL。  &gt; * 只支持分身数字人视频制作  &gt; * 需要先申请开通白名单后，才允许通过外部URL的音频文件来驱动分身数字人视频。  &gt; * 音频文件需要存放在华为云OBS
        :type audio_drive_file_external_url: str
        :param background_config: 背景配置。
        :type background_config: list[:class:`huaweicloudsdkmetastudio.v1.BackgroundConfigInfo`]
        :param layer_config: 图层配置。
        :type layer_config: list[:class:`huaweicloudsdkmetastudio.v1.LayerConfig`]
        :param audio_config: 
        :type audio_config: :class:`huaweicloudsdkmetastudio.v1.AudioInfo`
        """
        
        

        self._script_type = None
        self._text_config = None
        self._audio_duration = None
        self._audio_drive_action_config = None
        self._audio_drive_file_external_url = None
        self._background_config = None
        self._layer_config = None
        self._audio_config = None
        self.discriminator = None

        if script_type is not None:
            self.script_type = script_type
        if text_config is not None:
            self.text_config = text_config
        if audio_duration is not None:
            self.audio_duration = audio_duration
        if audio_drive_action_config is not None:
            self.audio_drive_action_config = audio_drive_action_config
        if audio_drive_file_external_url is not None:
            self.audio_drive_file_external_url = audio_drive_file_external_url
        if background_config is not None:
            self.background_config = background_config
        if layer_config is not None:
            self.layer_config = layer_config
        if audio_config is not None:
            self.audio_config = audio_config

    @property
    def script_type(self):
        r"""Gets the script_type of this ShootScript.

        **参数解释**： 脚本类型，即视频制作的驱动方式 **约束限制**： 不涉及 **取值范围** * TEXT: 文本驱动，即通过TTS合成语音 * AUDIO: 语音驱动

        :return: The script_type of this ShootScript.
        :rtype: str
        """
        return self._script_type

    @script_type.setter
    def script_type(self, script_type):
        r"""Sets the script_type of this ShootScript.

        **参数解释**： 脚本类型，即视频制作的驱动方式 **约束限制**： 不涉及 **取值范围** * TEXT: 文本驱动，即通过TTS合成语音 * AUDIO: 语音驱动

        :param script_type: The script_type of this ShootScript.
        :type script_type: str
        """
        self._script_type = script_type

    @property
    def text_config(self):
        r"""Gets the text_config of this ShootScript.

        :return: The text_config of this ShootScript.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.TextConfig`
        """
        return self._text_config

    @text_config.setter
    def text_config(self, text_config):
        r"""Sets the text_config of this ShootScript.

        :param text_config: The text_config of this ShootScript.
        :type text_config: :class:`huaweicloudsdkmetastudio.v1.TextConfig`
        """
        self._text_config = text_config

    @property
    def audio_duration(self):
        r"""Gets the audio_duration of this ShootScript.

        语音驱动时，音频时长，单位秒。 > * 创建剧本时此参数可以不设置，音频文件上传成功后，通过更新剧本接口设置 > * 查询剧本详情时，返回音频时长，用于预估视频时长

        :return: The audio_duration of this ShootScript.
        :rtype: float
        """
        return self._audio_duration

    @audio_duration.setter
    def audio_duration(self, audio_duration):
        r"""Sets the audio_duration of this ShootScript.

        语音驱动时，音频时长，单位秒。 > * 创建剧本时此参数可以不设置，音频文件上传成功后，通过更新剧本接口设置 > * 查询剧本详情时，返回音频时长，用于预估视频时长

        :param audio_duration: The audio_duration of this ShootScript.
        :type audio_duration: float
        """
        self._audio_duration = audio_duration

    @property
    def audio_drive_action_config(self):
        r"""Gets the audio_drive_action_config of this ShootScript.

        语音驱动时的动作配置。

        :return: The audio_drive_action_config of this ShootScript.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.AudioDriveActionConfig`]
        """
        return self._audio_drive_action_config

    @audio_drive_action_config.setter
    def audio_drive_action_config(self, audio_drive_action_config):
        r"""Sets the audio_drive_action_config of this ShootScript.

        语音驱动时的动作配置。

        :param audio_drive_action_config: The audio_drive_action_config of this ShootScript.
        :type audio_drive_action_config: list[:class:`huaweicloudsdkmetastudio.v1.AudioDriveActionConfig`]
        """
        self._audio_drive_action_config = audio_drive_action_config

    @property
    def audio_drive_file_external_url(self):
        r"""Gets the audio_drive_file_external_url of this ShootScript.

        语音驱动音频文件外部下载URL。  > * 只支持分身数字人视频制作  > * 需要先申请开通白名单后，才允许通过外部URL的音频文件来驱动分身数字人视频。  > * 音频文件需要存放在华为云OBS

        :return: The audio_drive_file_external_url of this ShootScript.
        :rtype: str
        """
        return self._audio_drive_file_external_url

    @audio_drive_file_external_url.setter
    def audio_drive_file_external_url(self, audio_drive_file_external_url):
        r"""Sets the audio_drive_file_external_url of this ShootScript.

        语音驱动音频文件外部下载URL。  > * 只支持分身数字人视频制作  > * 需要先申请开通白名单后，才允许通过外部URL的音频文件来驱动分身数字人视频。  > * 音频文件需要存放在华为云OBS

        :param audio_drive_file_external_url: The audio_drive_file_external_url of this ShootScript.
        :type audio_drive_file_external_url: str
        """
        self._audio_drive_file_external_url = audio_drive_file_external_url

    @property
    def background_config(self):
        r"""Gets the background_config of this ShootScript.

        背景配置。

        :return: The background_config of this ShootScript.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.BackgroundConfigInfo`]
        """
        return self._background_config

    @background_config.setter
    def background_config(self, background_config):
        r"""Sets the background_config of this ShootScript.

        背景配置。

        :param background_config: The background_config of this ShootScript.
        :type background_config: list[:class:`huaweicloudsdkmetastudio.v1.BackgroundConfigInfo`]
        """
        self._background_config = background_config

    @property
    def layer_config(self):
        r"""Gets the layer_config of this ShootScript.

        图层配置。

        :return: The layer_config of this ShootScript.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.LayerConfig`]
        """
        return self._layer_config

    @layer_config.setter
    def layer_config(self, layer_config):
        r"""Sets the layer_config of this ShootScript.

        图层配置。

        :param layer_config: The layer_config of this ShootScript.
        :type layer_config: list[:class:`huaweicloudsdkmetastudio.v1.LayerConfig`]
        """
        self._layer_config = layer_config

    @property
    def audio_config(self):
        r"""Gets the audio_config of this ShootScript.

        :return: The audio_config of this ShootScript.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.AudioInfo`
        """
        return self._audio_config

    @audio_config.setter
    def audio_config(self, audio_config):
        r"""Sets the audio_config of this ShootScript.

        :param audio_config: The audio_config of this ShootScript.
        :type audio_config: :class:`huaweicloudsdkmetastudio.v1.AudioInfo`
        """
        self._audio_config = audio_config

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
        if not isinstance(other, ShootScript):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
