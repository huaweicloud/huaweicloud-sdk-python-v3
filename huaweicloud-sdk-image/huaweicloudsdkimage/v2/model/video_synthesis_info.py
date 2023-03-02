# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoSynthesisInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bgm_url': 'str',
        'resolution': 'list[int]',
        'fps': 'int',
        'animation_duration': 'float'
    }

    attribute_map = {
        'bgm_url': 'bgm_url',
        'resolution': 'resolution',
        'fps': 'fps',
        'animation_duration': 'animation_duration'
    }

    def __init__(self, bgm_url=None, resolution=None, fps=None, animation_duration=None):
        """VideoSynthesisInfo

        The model defined in huaweicloud sdk

        :param bgm_url: 背景音乐url
        :type bgm_url: str
        :param resolution: 视频分辨率
        :type resolution: list[int]
        :param fps: 视频帧率
        :type fps: int
        :param animation_duration: 转场动画时间
        :type animation_duration: float
        """
        
        

        self._bgm_url = None
        self._resolution = None
        self._fps = None
        self._animation_duration = None
        self.discriminator = None

        if bgm_url is not None:
            self.bgm_url = bgm_url
        if resolution is not None:
            self.resolution = resolution
        if fps is not None:
            self.fps = fps
        if animation_duration is not None:
            self.animation_duration = animation_duration

    @property
    def bgm_url(self):
        """Gets the bgm_url of this VideoSynthesisInfo.

        背景音乐url

        :return: The bgm_url of this VideoSynthesisInfo.
        :rtype: str
        """
        return self._bgm_url

    @bgm_url.setter
    def bgm_url(self, bgm_url):
        """Sets the bgm_url of this VideoSynthesisInfo.

        背景音乐url

        :param bgm_url: The bgm_url of this VideoSynthesisInfo.
        :type bgm_url: str
        """
        self._bgm_url = bgm_url

    @property
    def resolution(self):
        """Gets the resolution of this VideoSynthesisInfo.

        视频分辨率

        :return: The resolution of this VideoSynthesisInfo.
        :rtype: list[int]
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this VideoSynthesisInfo.

        视频分辨率

        :param resolution: The resolution of this VideoSynthesisInfo.
        :type resolution: list[int]
        """
        self._resolution = resolution

    @property
    def fps(self):
        """Gets the fps of this VideoSynthesisInfo.

        视频帧率

        :return: The fps of this VideoSynthesisInfo.
        :rtype: int
        """
        return self._fps

    @fps.setter
    def fps(self, fps):
        """Sets the fps of this VideoSynthesisInfo.

        视频帧率

        :param fps: The fps of this VideoSynthesisInfo.
        :type fps: int
        """
        self._fps = fps

    @property
    def animation_duration(self):
        """Gets the animation_duration of this VideoSynthesisInfo.

        转场动画时间

        :return: The animation_duration of this VideoSynthesisInfo.
        :rtype: float
        """
        return self._animation_duration

    @animation_duration.setter
    def animation_duration(self, animation_duration):
        """Sets the animation_duration of this VideoSynthesisInfo.

        转场动画时间

        :param animation_duration: The animation_duration of this VideoSynthesisInfo.
        :type animation_duration: float
        """
        self._animation_duration = animation_duration

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
        if not isinstance(other, VideoSynthesisInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
