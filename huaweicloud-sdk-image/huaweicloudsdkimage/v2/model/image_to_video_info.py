# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageToVideoInfo:

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
        'to_gif': 'int',
        'gif_compress': 'float',
        'image_durations': 'list[float]',
        'resolution': 'list[int]',
        'fps': 'int',
        'animation_duration': 'float'
    }

    attribute_map = {
        'bgm_url': 'bgm_url',
        'to_gif': 'to_gif',
        'gif_compress': 'gif_compress',
        'image_durations': 'image_durations',
        'resolution': 'resolution',
        'fps': 'fps',
        'animation_duration': 'animation_duration'
    }

    def __init__(self, bgm_url=None, to_gif=None, gif_compress=None, image_durations=None, resolution=None, fps=None, animation_duration=None):
        """ImageToVideoInfo

        The model defined in huaweicloud sdk

        :param bgm_url: 背景音乐url
        :type bgm_url: str
        :param to_gif: 生成视频或gif开关，1生成gif，0生成视频，默认为视频
        :type to_gif: int
        :param gif_compress: gif分辨率压缩率，gif最终分辨率为最终合成视频分辨率*gif_compress
        :type gif_compress: float
        :param image_durations: 图像展示时间List
        :type image_durations: list[float]
        :param resolution: 分辨率
        :type resolution: list[int]
        :param fps: 视频帧率，默认30
        :type fps: int
        :param animation_duration: 动画转场时间，默认1s
        :type animation_duration: float
        """
        
        

        self._bgm_url = None
        self._to_gif = None
        self._gif_compress = None
        self._image_durations = None
        self._resolution = None
        self._fps = None
        self._animation_duration = None
        self.discriminator = None

        if bgm_url is not None:
            self.bgm_url = bgm_url
        if to_gif is not None:
            self.to_gif = to_gif
        if gif_compress is not None:
            self.gif_compress = gif_compress
        if image_durations is not None:
            self.image_durations = image_durations
        if resolution is not None:
            self.resolution = resolution
        if fps is not None:
            self.fps = fps
        if animation_duration is not None:
            self.animation_duration = animation_duration

    @property
    def bgm_url(self):
        """Gets the bgm_url of this ImageToVideoInfo.

        背景音乐url

        :return: The bgm_url of this ImageToVideoInfo.
        :rtype: str
        """
        return self._bgm_url

    @bgm_url.setter
    def bgm_url(self, bgm_url):
        """Sets the bgm_url of this ImageToVideoInfo.

        背景音乐url

        :param bgm_url: The bgm_url of this ImageToVideoInfo.
        :type bgm_url: str
        """
        self._bgm_url = bgm_url

    @property
    def to_gif(self):
        """Gets the to_gif of this ImageToVideoInfo.

        生成视频或gif开关，1生成gif，0生成视频，默认为视频

        :return: The to_gif of this ImageToVideoInfo.
        :rtype: int
        """
        return self._to_gif

    @to_gif.setter
    def to_gif(self, to_gif):
        """Sets the to_gif of this ImageToVideoInfo.

        生成视频或gif开关，1生成gif，0生成视频，默认为视频

        :param to_gif: The to_gif of this ImageToVideoInfo.
        :type to_gif: int
        """
        self._to_gif = to_gif

    @property
    def gif_compress(self):
        """Gets the gif_compress of this ImageToVideoInfo.

        gif分辨率压缩率，gif最终分辨率为最终合成视频分辨率*gif_compress

        :return: The gif_compress of this ImageToVideoInfo.
        :rtype: float
        """
        return self._gif_compress

    @gif_compress.setter
    def gif_compress(self, gif_compress):
        """Sets the gif_compress of this ImageToVideoInfo.

        gif分辨率压缩率，gif最终分辨率为最终合成视频分辨率*gif_compress

        :param gif_compress: The gif_compress of this ImageToVideoInfo.
        :type gif_compress: float
        """
        self._gif_compress = gif_compress

    @property
    def image_durations(self):
        """Gets the image_durations of this ImageToVideoInfo.

        图像展示时间List

        :return: The image_durations of this ImageToVideoInfo.
        :rtype: list[float]
        """
        return self._image_durations

    @image_durations.setter
    def image_durations(self, image_durations):
        """Sets the image_durations of this ImageToVideoInfo.

        图像展示时间List

        :param image_durations: The image_durations of this ImageToVideoInfo.
        :type image_durations: list[float]
        """
        self._image_durations = image_durations

    @property
    def resolution(self):
        """Gets the resolution of this ImageToVideoInfo.

        分辨率

        :return: The resolution of this ImageToVideoInfo.
        :rtype: list[int]
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this ImageToVideoInfo.

        分辨率

        :param resolution: The resolution of this ImageToVideoInfo.
        :type resolution: list[int]
        """
        self._resolution = resolution

    @property
    def fps(self):
        """Gets the fps of this ImageToVideoInfo.

        视频帧率，默认30

        :return: The fps of this ImageToVideoInfo.
        :rtype: int
        """
        return self._fps

    @fps.setter
    def fps(self, fps):
        """Sets the fps of this ImageToVideoInfo.

        视频帧率，默认30

        :param fps: The fps of this ImageToVideoInfo.
        :type fps: int
        """
        self._fps = fps

    @property
    def animation_duration(self):
        """Gets the animation_duration of this ImageToVideoInfo.

        动画转场时间，默认1s

        :return: The animation_duration of this ImageToVideoInfo.
        :rtype: float
        """
        return self._animation_duration

    @animation_duration.setter
    def animation_duration(self, animation_duration):
        """Sets the animation_duration of this ImageToVideoInfo.

        动画转场时间，默认1s

        :param animation_duration: The animation_duration of this ImageToVideoInfo.
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
        if not isinstance(other, ImageToVideoInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
