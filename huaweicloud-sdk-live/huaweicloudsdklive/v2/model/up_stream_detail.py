# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpStreamDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time': 'str',
        'fps': 'int',
        'rate': 'int',
        'delay': 'int',
        'gop_duration': 'int',
        'last_video_pts': 'int',
        'last_audio_pts': 'int',
        'last_video_audio_pts_diff': 'int'
    }

    attribute_map = {
        'time': 'time',
        'fps': 'fps',
        'rate': 'rate',
        'delay': 'delay',
        'gop_duration': 'gop_duration',
        'last_video_pts': 'last_video_pts',
        'last_audio_pts': 'last_audio_pts',
        'last_video_audio_pts_diff': 'last_video_audio_pts_diff'
    }

    def __init__(self, time=None, fps=None, rate=None, delay=None, gop_duration=None, last_video_pts=None, last_audio_pts=None, last_video_audio_pts_diff=None):
        r"""UpStreamDetail

        The model defined in huaweicloud sdk

        :param time: 采样时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。
        :type time: str
        :param fps: 帧率，单位为fps
        :type fps: int
        :param rate: 码率，单位为Kbps
        :type rate: int
        :param delay: 时延 单位ms
        :type delay: int
        :param gop_duration: 最近一次gop的时长 单位ms
        :type gop_duration: int
        :param last_video_pts: 视频DTS 单位ms
        :type last_video_pts: int
        :param last_audio_pts: 音频DTS 单位ms
        :type last_audio_pts: int
        :param last_video_audio_pts_diff: 音视频DTS差值 单位ms
        :type last_video_audio_pts_diff: int
        """
        
        

        self._time = None
        self._fps = None
        self._rate = None
        self._delay = None
        self._gop_duration = None
        self._last_video_pts = None
        self._last_audio_pts = None
        self._last_video_audio_pts_diff = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if fps is not None:
            self.fps = fps
        if rate is not None:
            self.rate = rate
        if delay is not None:
            self.delay = delay
        if gop_duration is not None:
            self.gop_duration = gop_duration
        if last_video_pts is not None:
            self.last_video_pts = last_video_pts
        if last_audio_pts is not None:
            self.last_audio_pts = last_audio_pts
        if last_video_audio_pts_diff is not None:
            self.last_video_audio_pts_diff = last_video_audio_pts_diff

    @property
    def time(self):
        r"""Gets the time of this UpStreamDetail.

        采样时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。

        :return: The time of this UpStreamDetail.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this UpStreamDetail.

        采样时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。

        :param time: The time of this UpStreamDetail.
        :type time: str
        """
        self._time = time

    @property
    def fps(self):
        r"""Gets the fps of this UpStreamDetail.

        帧率，单位为fps

        :return: The fps of this UpStreamDetail.
        :rtype: int
        """
        return self._fps

    @fps.setter
    def fps(self, fps):
        r"""Sets the fps of this UpStreamDetail.

        帧率，单位为fps

        :param fps: The fps of this UpStreamDetail.
        :type fps: int
        """
        self._fps = fps

    @property
    def rate(self):
        r"""Gets the rate of this UpStreamDetail.

        码率，单位为Kbps

        :return: The rate of this UpStreamDetail.
        :rtype: int
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        r"""Sets the rate of this UpStreamDetail.

        码率，单位为Kbps

        :param rate: The rate of this UpStreamDetail.
        :type rate: int
        """
        self._rate = rate

    @property
    def delay(self):
        r"""Gets the delay of this UpStreamDetail.

        时延 单位ms

        :return: The delay of this UpStreamDetail.
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        r"""Sets the delay of this UpStreamDetail.

        时延 单位ms

        :param delay: The delay of this UpStreamDetail.
        :type delay: int
        """
        self._delay = delay

    @property
    def gop_duration(self):
        r"""Gets the gop_duration of this UpStreamDetail.

        最近一次gop的时长 单位ms

        :return: The gop_duration of this UpStreamDetail.
        :rtype: int
        """
        return self._gop_duration

    @gop_duration.setter
    def gop_duration(self, gop_duration):
        r"""Sets the gop_duration of this UpStreamDetail.

        最近一次gop的时长 单位ms

        :param gop_duration: The gop_duration of this UpStreamDetail.
        :type gop_duration: int
        """
        self._gop_duration = gop_duration

    @property
    def last_video_pts(self):
        r"""Gets the last_video_pts of this UpStreamDetail.

        视频DTS 单位ms

        :return: The last_video_pts of this UpStreamDetail.
        :rtype: int
        """
        return self._last_video_pts

    @last_video_pts.setter
    def last_video_pts(self, last_video_pts):
        r"""Sets the last_video_pts of this UpStreamDetail.

        视频DTS 单位ms

        :param last_video_pts: The last_video_pts of this UpStreamDetail.
        :type last_video_pts: int
        """
        self._last_video_pts = last_video_pts

    @property
    def last_audio_pts(self):
        r"""Gets the last_audio_pts of this UpStreamDetail.

        音频DTS 单位ms

        :return: The last_audio_pts of this UpStreamDetail.
        :rtype: int
        """
        return self._last_audio_pts

    @last_audio_pts.setter
    def last_audio_pts(self, last_audio_pts):
        r"""Sets the last_audio_pts of this UpStreamDetail.

        音频DTS 单位ms

        :param last_audio_pts: The last_audio_pts of this UpStreamDetail.
        :type last_audio_pts: int
        """
        self._last_audio_pts = last_audio_pts

    @property
    def last_video_audio_pts_diff(self):
        r"""Gets the last_video_audio_pts_diff of this UpStreamDetail.

        音视频DTS差值 单位ms

        :return: The last_video_audio_pts_diff of this UpStreamDetail.
        :rtype: int
        """
        return self._last_video_audio_pts_diff

    @last_video_audio_pts_diff.setter
    def last_video_audio_pts_diff(self, last_video_audio_pts_diff):
        r"""Sets the last_video_audio_pts_diff of this UpStreamDetail.

        音视频DTS差值 单位ms

        :param last_video_audio_pts_diff: The last_video_audio_pts_diff of this UpStreamDetail.
        :type last_video_audio_pts_diff: int
        """
        self._last_video_audio_pts_diff = last_video_audio_pts_diff

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
        if not isinstance(other, UpStreamDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
