# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AnimationAssetMeta:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'style_id': 'str',
        'duration': 'float',
        'auto_analysis': 'bool',
        'voice_delay': 'float',
        'animation_insert_restriction': 'str'
    }

    attribute_map = {
        'style_id': 'style_id',
        'duration': 'duration',
        'auto_analysis': 'auto_analysis',
        'voice_delay': 'voice_delay',
        'animation_insert_restriction': 'animation_insert_restriction'
    }

    def __init__(self, style_id=None, duration=None, auto_analysis=None, voice_delay=None, animation_insert_restriction=None):
        """AnimationAssetMeta

        The model defined in huaweicloud sdk

        :param style_id: 数字人模型风格ID。
        :type style_id: str
        :param duration: 动作动画时长。
        :type duration: float
        :param auto_analysis: 动作是否需要自动解析。
        :type auto_analysis: bool
        :param voice_delay: 语音延迟播放时长。  单位秒。  使用场景举例：入场动画3秒，voice_delay设置成4秒，则语音从入场动画开始后第4秒开始播放。
        :type voice_delay: float
        :param animation_insert_restriction: 动画插入位置限制。 * ONLY_BEGINNING：视频制作时，动画只允许出现在起始位置。 * ONLY_END：视频制作时，动画只允许出现在结束位置。
        :type animation_insert_restriction: str
        """
        
        

        self._style_id = None
        self._duration = None
        self._auto_analysis = None
        self._voice_delay = None
        self._animation_insert_restriction = None
        self.discriminator = None

        if style_id is not None:
            self.style_id = style_id
        if duration is not None:
            self.duration = duration
        if auto_analysis is not None:
            self.auto_analysis = auto_analysis
        if voice_delay is not None:
            self.voice_delay = voice_delay
        if animation_insert_restriction is not None:
            self.animation_insert_restriction = animation_insert_restriction

    @property
    def style_id(self):
        """Gets the style_id of this AnimationAssetMeta.

        数字人模型风格ID。

        :return: The style_id of this AnimationAssetMeta.
        :rtype: str
        """
        return self._style_id

    @style_id.setter
    def style_id(self, style_id):
        """Sets the style_id of this AnimationAssetMeta.

        数字人模型风格ID。

        :param style_id: The style_id of this AnimationAssetMeta.
        :type style_id: str
        """
        self._style_id = style_id

    @property
    def duration(self):
        """Gets the duration of this AnimationAssetMeta.

        动作动画时长。

        :return: The duration of this AnimationAssetMeta.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this AnimationAssetMeta.

        动作动画时长。

        :param duration: The duration of this AnimationAssetMeta.
        :type duration: float
        """
        self._duration = duration

    @property
    def auto_analysis(self):
        """Gets the auto_analysis of this AnimationAssetMeta.

        动作是否需要自动解析。

        :return: The auto_analysis of this AnimationAssetMeta.
        :rtype: bool
        """
        return self._auto_analysis

    @auto_analysis.setter
    def auto_analysis(self, auto_analysis):
        """Sets the auto_analysis of this AnimationAssetMeta.

        动作是否需要自动解析。

        :param auto_analysis: The auto_analysis of this AnimationAssetMeta.
        :type auto_analysis: bool
        """
        self._auto_analysis = auto_analysis

    @property
    def voice_delay(self):
        """Gets the voice_delay of this AnimationAssetMeta.

        语音延迟播放时长。  单位秒。  使用场景举例：入场动画3秒，voice_delay设置成4秒，则语音从入场动画开始后第4秒开始播放。

        :return: The voice_delay of this AnimationAssetMeta.
        :rtype: float
        """
        return self._voice_delay

    @voice_delay.setter
    def voice_delay(self, voice_delay):
        """Sets the voice_delay of this AnimationAssetMeta.

        语音延迟播放时长。  单位秒。  使用场景举例：入场动画3秒，voice_delay设置成4秒，则语音从入场动画开始后第4秒开始播放。

        :param voice_delay: The voice_delay of this AnimationAssetMeta.
        :type voice_delay: float
        """
        self._voice_delay = voice_delay

    @property
    def animation_insert_restriction(self):
        """Gets the animation_insert_restriction of this AnimationAssetMeta.

        动画插入位置限制。 * ONLY_BEGINNING：视频制作时，动画只允许出现在起始位置。 * ONLY_END：视频制作时，动画只允许出现在结束位置。

        :return: The animation_insert_restriction of this AnimationAssetMeta.
        :rtype: str
        """
        return self._animation_insert_restriction

    @animation_insert_restriction.setter
    def animation_insert_restriction(self, animation_insert_restriction):
        """Sets the animation_insert_restriction of this AnimationAssetMeta.

        动画插入位置限制。 * ONLY_BEGINNING：视频制作时，动画只允许出现在起始位置。 * ONLY_END：视频制作时，动画只允许出现在结束位置。

        :param animation_insert_restriction: The animation_insert_restriction of this AnimationAssetMeta.
        :type animation_insert_restriction: str
        """
        self._animation_insert_restriction = animation_insert_restriction

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
        if not isinstance(other, AnimationAssetMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
