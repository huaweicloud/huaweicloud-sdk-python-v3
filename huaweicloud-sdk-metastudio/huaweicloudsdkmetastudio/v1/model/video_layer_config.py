# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoLayerConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'video_url': 'str',
        'video_cover_url': 'str',
        'loop_count': 'int',
        'video_sound': 'int',
        'is_play_the_entire_video': 'bool'
    }

    attribute_map = {
        'video_url': 'video_url',
        'video_cover_url': 'video_cover_url',
        'loop_count': 'loop_count',
        'video_sound': 'video_sound',
        'is_play_the_entire_video': 'is_play_the_entire_video'
    }

    def __init__(self, video_url=None, video_cover_url=None, loop_count=None, video_sound=None, is_play_the_entire_video=None):
        r"""VideoLayerConfig

        The model defined in huaweicloud sdk

        :param video_url: **参数解释**： 视频文件的URL。 **约束限制**： * 仅直播支持外部URL，其他业务通过资产库查询获取，不支持外部URL。 **取值范围**： 字符长度1-2048位。 **默认取值**： 不涉及。
        :type video_url: str
        :param video_cover_url: **参数解释**： 视频封面文件的URL。 **约束限制**： * 仅直播支持外部URL，其他业务通过资产库查询获取，不支持外部URL。 **取值范围**： 字符长度1-2048位。 **默认取值**： 不涉及。
        :type video_cover_url: str
        :param loop_count: **参数解释**： 循环播放视频次数。  特殊取值： * 0：表示不播放 * -1：表示持续循环播放  **约束限制**： 不涉及。
        :type loop_count: int
        :param video_sound: **参数解释**： 视频声音大小，0 - 100，表示开启视频声音原视频音量的百分比  特殊取值： * 0：表示不开启声音（默认值）  **约束限制**： 不涉及。
        :type video_sound: int
        :param is_play_the_entire_video: **参数解释**： 是否播放完整个视频，true表示播放完整个视频，false表示当场景文本/音频结束时，视频也同时不再播放。  特殊取值： 默认值为false  **约束限制**： 不涉及。
        :type is_play_the_entire_video: bool
        """
        
        

        self._video_url = None
        self._video_cover_url = None
        self._loop_count = None
        self._video_sound = None
        self._is_play_the_entire_video = None
        self.discriminator = None

        if video_url is not None:
            self.video_url = video_url
        if video_cover_url is not None:
            self.video_cover_url = video_cover_url
        if loop_count is not None:
            self.loop_count = loop_count
        if video_sound is not None:
            self.video_sound = video_sound
        if is_play_the_entire_video is not None:
            self.is_play_the_entire_video = is_play_the_entire_video

    @property
    def video_url(self):
        r"""Gets the video_url of this VideoLayerConfig.

        **参数解释**： 视频文件的URL。 **约束限制**： * 仅直播支持外部URL，其他业务通过资产库查询获取，不支持外部URL。 **取值范围**： 字符长度1-2048位。 **默认取值**： 不涉及。

        :return: The video_url of this VideoLayerConfig.
        :rtype: str
        """
        return self._video_url

    @video_url.setter
    def video_url(self, video_url):
        r"""Sets the video_url of this VideoLayerConfig.

        **参数解释**： 视频文件的URL。 **约束限制**： * 仅直播支持外部URL，其他业务通过资产库查询获取，不支持外部URL。 **取值范围**： 字符长度1-2048位。 **默认取值**： 不涉及。

        :param video_url: The video_url of this VideoLayerConfig.
        :type video_url: str
        """
        self._video_url = video_url

    @property
    def video_cover_url(self):
        r"""Gets the video_cover_url of this VideoLayerConfig.

        **参数解释**： 视频封面文件的URL。 **约束限制**： * 仅直播支持外部URL，其他业务通过资产库查询获取，不支持外部URL。 **取值范围**： 字符长度1-2048位。 **默认取值**： 不涉及。

        :return: The video_cover_url of this VideoLayerConfig.
        :rtype: str
        """
        return self._video_cover_url

    @video_cover_url.setter
    def video_cover_url(self, video_cover_url):
        r"""Sets the video_cover_url of this VideoLayerConfig.

        **参数解释**： 视频封面文件的URL。 **约束限制**： * 仅直播支持外部URL，其他业务通过资产库查询获取，不支持外部URL。 **取值范围**： 字符长度1-2048位。 **默认取值**： 不涉及。

        :param video_cover_url: The video_cover_url of this VideoLayerConfig.
        :type video_cover_url: str
        """
        self._video_cover_url = video_cover_url

    @property
    def loop_count(self):
        r"""Gets the loop_count of this VideoLayerConfig.

        **参数解释**： 循环播放视频次数。  特殊取值： * 0：表示不播放 * -1：表示持续循环播放  **约束限制**： 不涉及。

        :return: The loop_count of this VideoLayerConfig.
        :rtype: int
        """
        return self._loop_count

    @loop_count.setter
    def loop_count(self, loop_count):
        r"""Sets the loop_count of this VideoLayerConfig.

        **参数解释**： 循环播放视频次数。  特殊取值： * 0：表示不播放 * -1：表示持续循环播放  **约束限制**： 不涉及。

        :param loop_count: The loop_count of this VideoLayerConfig.
        :type loop_count: int
        """
        self._loop_count = loop_count

    @property
    def video_sound(self):
        r"""Gets the video_sound of this VideoLayerConfig.

        **参数解释**： 视频声音大小，0 - 100，表示开启视频声音原视频音量的百分比  特殊取值： * 0：表示不开启声音（默认值）  **约束限制**： 不涉及。

        :return: The video_sound of this VideoLayerConfig.
        :rtype: int
        """
        return self._video_sound

    @video_sound.setter
    def video_sound(self, video_sound):
        r"""Sets the video_sound of this VideoLayerConfig.

        **参数解释**： 视频声音大小，0 - 100，表示开启视频声音原视频音量的百分比  特殊取值： * 0：表示不开启声音（默认值）  **约束限制**： 不涉及。

        :param video_sound: The video_sound of this VideoLayerConfig.
        :type video_sound: int
        """
        self._video_sound = video_sound

    @property
    def is_play_the_entire_video(self):
        r"""Gets the is_play_the_entire_video of this VideoLayerConfig.

        **参数解释**： 是否播放完整个视频，true表示播放完整个视频，false表示当场景文本/音频结束时，视频也同时不再播放。  特殊取值： 默认值为false  **约束限制**： 不涉及。

        :return: The is_play_the_entire_video of this VideoLayerConfig.
        :rtype: bool
        """
        return self._is_play_the_entire_video

    @is_play_the_entire_video.setter
    def is_play_the_entire_video(self, is_play_the_entire_video):
        r"""Sets the is_play_the_entire_video of this VideoLayerConfig.

        **参数解释**： 是否播放完整个视频，true表示播放完整个视频，false表示当场景文本/音频结束时，视频也同时不再播放。  特殊取值： 默认值为false  **约束限制**： 不涉及。

        :param is_play_the_entire_video: The is_play_the_entire_video of this VideoLayerConfig.
        :type is_play_the_entire_video: bool
        """
        self._is_play_the_entire_video = is_play_the_entire_video

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
        if not isinstance(other, VideoLayerConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
