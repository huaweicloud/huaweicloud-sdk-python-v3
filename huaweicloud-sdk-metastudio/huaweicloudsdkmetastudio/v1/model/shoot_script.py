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
        'animation_config': 'list[AnimationConfig]',
        'background_config': 'list[BackgroundConfigInfo]',
        'emotion_config': 'list[EmotionConfig]',
        'layer_config': 'list[LayerConfig]'
    }

    attribute_map = {
        'script_type': 'script_type',
        'text_config': 'text_config',
        'animation_config': 'animation_config',
        'background_config': 'background_config',
        'emotion_config': 'emotion_config',
        'layer_config': 'layer_config'
    }

    def __init__(self, script_type=None, text_config=None, animation_config=None, background_config=None, emotion_config=None, layer_config=None):
        """ShootScript

        The model defined in huaweicloud sdk

        :param script_type: 脚本类型，即视频制作的驱动方式。默认TEXT * TEXT: 文本驱动，即通过TTS合成语音 * AUDIO: 语音驱动
        :type script_type: str
        :param text_config: 
        :type text_config: :class:`huaweicloudsdkmetastudio.v1.TextConfig`
        :param animation_config: 动作配置。 &gt; * 推荐使用text_config中插入动作标签，不配置animation_config。 &gt; * 使用animation_config方式配置动作，在整个讲解过程中动作循环播放。 &gt; * 分身数字人视频制作时此参数不生效。
        :type animation_config: list[:class:`huaweicloudsdkmetastudio.v1.AnimationConfig`]
        :param background_config: 背景配置。
        :type background_config: list[:class:`huaweicloudsdkmetastudio.v1.BackgroundConfigInfo`]
        :param emotion_config: 情感标签配置。  &gt; * 分身数字人视频制作时此参数不生效。  &gt; * 推荐在text_config中插入情感标签，此参数将被废弃。
        :type emotion_config: list[:class:`huaweicloudsdkmetastudio.v1.EmotionConfig`]
        :param layer_config: 图层配置。
        :type layer_config: list[:class:`huaweicloudsdkmetastudio.v1.LayerConfig`]
        """
        
        

        self._script_type = None
        self._text_config = None
        self._animation_config = None
        self._background_config = None
        self._emotion_config = None
        self._layer_config = None
        self.discriminator = None

        if script_type is not None:
            self.script_type = script_type
        if text_config is not None:
            self.text_config = text_config
        if animation_config is not None:
            self.animation_config = animation_config
        if background_config is not None:
            self.background_config = background_config
        if emotion_config is not None:
            self.emotion_config = emotion_config
        if layer_config is not None:
            self.layer_config = layer_config

    @property
    def script_type(self):
        """Gets the script_type of this ShootScript.

        脚本类型，即视频制作的驱动方式。默认TEXT * TEXT: 文本驱动，即通过TTS合成语音 * AUDIO: 语音驱动

        :return: The script_type of this ShootScript.
        :rtype: str
        """
        return self._script_type

    @script_type.setter
    def script_type(self, script_type):
        """Sets the script_type of this ShootScript.

        脚本类型，即视频制作的驱动方式。默认TEXT * TEXT: 文本驱动，即通过TTS合成语音 * AUDIO: 语音驱动

        :param script_type: The script_type of this ShootScript.
        :type script_type: str
        """
        self._script_type = script_type

    @property
    def text_config(self):
        """Gets the text_config of this ShootScript.

        :return: The text_config of this ShootScript.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.TextConfig`
        """
        return self._text_config

    @text_config.setter
    def text_config(self, text_config):
        """Sets the text_config of this ShootScript.

        :param text_config: The text_config of this ShootScript.
        :type text_config: :class:`huaweicloudsdkmetastudio.v1.TextConfig`
        """
        self._text_config = text_config

    @property
    def animation_config(self):
        """Gets the animation_config of this ShootScript.

        动作配置。 > * 推荐使用text_config中插入动作标签，不配置animation_config。 > * 使用animation_config方式配置动作，在整个讲解过程中动作循环播放。 > * 分身数字人视频制作时此参数不生效。

        :return: The animation_config of this ShootScript.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.AnimationConfig`]
        """
        return self._animation_config

    @animation_config.setter
    def animation_config(self, animation_config):
        """Sets the animation_config of this ShootScript.

        动作配置。 > * 推荐使用text_config中插入动作标签，不配置animation_config。 > * 使用animation_config方式配置动作，在整个讲解过程中动作循环播放。 > * 分身数字人视频制作时此参数不生效。

        :param animation_config: The animation_config of this ShootScript.
        :type animation_config: list[:class:`huaweicloudsdkmetastudio.v1.AnimationConfig`]
        """
        self._animation_config = animation_config

    @property
    def background_config(self):
        """Gets the background_config of this ShootScript.

        背景配置。

        :return: The background_config of this ShootScript.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.BackgroundConfigInfo`]
        """
        return self._background_config

    @background_config.setter
    def background_config(self, background_config):
        """Sets the background_config of this ShootScript.

        背景配置。

        :param background_config: The background_config of this ShootScript.
        :type background_config: list[:class:`huaweicloudsdkmetastudio.v1.BackgroundConfigInfo`]
        """
        self._background_config = background_config

    @property
    def emotion_config(self):
        """Gets the emotion_config of this ShootScript.

        情感标签配置。  > * 分身数字人视频制作时此参数不生效。  > * 推荐在text_config中插入情感标签，此参数将被废弃。

        :return: The emotion_config of this ShootScript.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.EmotionConfig`]
        """
        return self._emotion_config

    @emotion_config.setter
    def emotion_config(self, emotion_config):
        """Sets the emotion_config of this ShootScript.

        情感标签配置。  > * 分身数字人视频制作时此参数不生效。  > * 推荐在text_config中插入情感标签，此参数将被废弃。

        :param emotion_config: The emotion_config of this ShootScript.
        :type emotion_config: list[:class:`huaweicloudsdkmetastudio.v1.EmotionConfig`]
        """
        self._emotion_config = emotion_config

    @property
    def layer_config(self):
        """Gets the layer_config of this ShootScript.

        图层配置。

        :return: The layer_config of this ShootScript.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.LayerConfig`]
        """
        return self._layer_config

    @layer_config.setter
    def layer_config(self, layer_config):
        """Sets the layer_config of this ShootScript.

        图层配置。

        :param layer_config: The layer_config of this ShootScript.
        :type layer_config: list[:class:`huaweicloudsdkmetastudio.v1.LayerConfig`]
        """
        self._layer_config = layer_config

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
