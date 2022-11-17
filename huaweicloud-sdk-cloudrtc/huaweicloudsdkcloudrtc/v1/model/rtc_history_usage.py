# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RtcHistoryUsage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'date': 'str',
        'video_sd': 'int',
        'video_hd': 'int',
        'video_hdp': 'int',
        'audio': 'int',
        'total_duration': 'int'
    }

    attribute_map = {
        'date': 'date',
        'video_sd': 'video_sd',
        'video_hd': 'video_hd',
        'video_hdp': 'video_hdp',
        'audio': 'audio',
        'total_duration': 'total_duration'
    }

    def __init__(self, date=None, video_sd=None, video_hd=None, video_hdp=None, audio=None, total_duration=None):
        """RtcHistoryUsage

        The model defined in huaweicloud sdk

        :param date: 采样时间。日期格式按照ISO8601表示法，并使用UTC时间。格式为YYYY-MM-DD
        :type date: str
        :param video_sd: 标清视频时长，单位秒
        :type video_sd: int
        :param video_hd: 高清视频时长，单位秒
        :type video_hd: int
        :param video_hdp: 超高清视频时长，单位秒
        :type video_hdp: int
        :param audio: 音频时长，单位秒
        :type audio: int
        :param total_duration: 音视频总时长，单位秒
        :type total_duration: int
        """
        
        

        self._date = None
        self._video_sd = None
        self._video_hd = None
        self._video_hdp = None
        self._audio = None
        self._total_duration = None
        self.discriminator = None

        if date is not None:
            self.date = date
        if video_sd is not None:
            self.video_sd = video_sd
        if video_hd is not None:
            self.video_hd = video_hd
        if video_hdp is not None:
            self.video_hdp = video_hdp
        if audio is not None:
            self.audio = audio
        if total_duration is not None:
            self.total_duration = total_duration

    @property
    def date(self):
        """Gets the date of this RtcHistoryUsage.

        采样时间。日期格式按照ISO8601表示法，并使用UTC时间。格式为YYYY-MM-DD

        :return: The date of this RtcHistoryUsage.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this RtcHistoryUsage.

        采样时间。日期格式按照ISO8601表示法，并使用UTC时间。格式为YYYY-MM-DD

        :param date: The date of this RtcHistoryUsage.
        :type date: str
        """
        self._date = date

    @property
    def video_sd(self):
        """Gets the video_sd of this RtcHistoryUsage.

        标清视频时长，单位秒

        :return: The video_sd of this RtcHistoryUsage.
        :rtype: int
        """
        return self._video_sd

    @video_sd.setter
    def video_sd(self, video_sd):
        """Sets the video_sd of this RtcHistoryUsage.

        标清视频时长，单位秒

        :param video_sd: The video_sd of this RtcHistoryUsage.
        :type video_sd: int
        """
        self._video_sd = video_sd

    @property
    def video_hd(self):
        """Gets the video_hd of this RtcHistoryUsage.

        高清视频时长，单位秒

        :return: The video_hd of this RtcHistoryUsage.
        :rtype: int
        """
        return self._video_hd

    @video_hd.setter
    def video_hd(self, video_hd):
        """Sets the video_hd of this RtcHistoryUsage.

        高清视频时长，单位秒

        :param video_hd: The video_hd of this RtcHistoryUsage.
        :type video_hd: int
        """
        self._video_hd = video_hd

    @property
    def video_hdp(self):
        """Gets the video_hdp of this RtcHistoryUsage.

        超高清视频时长，单位秒

        :return: The video_hdp of this RtcHistoryUsage.
        :rtype: int
        """
        return self._video_hdp

    @video_hdp.setter
    def video_hdp(self, video_hdp):
        """Sets the video_hdp of this RtcHistoryUsage.

        超高清视频时长，单位秒

        :param video_hdp: The video_hdp of this RtcHistoryUsage.
        :type video_hdp: int
        """
        self._video_hdp = video_hdp

    @property
    def audio(self):
        """Gets the audio of this RtcHistoryUsage.

        音频时长，单位秒

        :return: The audio of this RtcHistoryUsage.
        :rtype: int
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        """Sets the audio of this RtcHistoryUsage.

        音频时长，单位秒

        :param audio: The audio of this RtcHistoryUsage.
        :type audio: int
        """
        self._audio = audio

    @property
    def total_duration(self):
        """Gets the total_duration of this RtcHistoryUsage.

        音视频总时长，单位秒

        :return: The total_duration of this RtcHistoryUsage.
        :rtype: int
        """
        return self._total_duration

    @total_duration.setter
    def total_duration(self, total_duration):
        """Sets the total_duration of this RtcHistoryUsage.

        音视频总时长，单位秒

        :param total_duration: The total_duration of this RtcHistoryUsage.
        :type total_duration: int
        """
        self._total_duration = total_duration

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
        if not isinstance(other, RtcHistoryUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
