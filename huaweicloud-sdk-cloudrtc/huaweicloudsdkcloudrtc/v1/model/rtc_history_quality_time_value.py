# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RtcHistoryQualityTimeValue:

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
        'join_success_rate': 'float',
        'join_success_in5secs_rate': 'float',
        'video_freeze_rate': 'float',
        'audio_freeze_rate': 'float',
        'first_video_recv_time': 'int',
        'first_audio_recv_time': 'int',
        'pull_stream_success_rate': 'float',
        'push_stream_success_rate': 'float',
        'video_upstream_excellent_trans_rate': 'float',
        'audio_upstream_excellent_trans_rate': 'float',
        'video_excellent_trans_rate': 'float',
        'audio_excellent_trans_rate': 'float',
        'video_trans_delay': 'float',
        'audio_trans_delay': 'float'
    }

    attribute_map = {
        'date': 'date',
        'join_success_rate': 'join_success_rate',
        'join_success_in5secs_rate': 'join_success_in5secs_rate',
        'video_freeze_rate': 'video_freeze_rate',
        'audio_freeze_rate': 'audio_freeze_rate',
        'first_video_recv_time': 'first_video_recv_time',
        'first_audio_recv_time': 'first_audio_recv_time',
        'pull_stream_success_rate': 'pull_stream_success_rate',
        'push_stream_success_rate': 'push_stream_success_rate',
        'video_upstream_excellent_trans_rate': 'video_upstream_excellent_trans_rate',
        'audio_upstream_excellent_trans_rate': 'audio_upstream_excellent_trans_rate',
        'video_excellent_trans_rate': 'video_excellent_trans_rate',
        'audio_excellent_trans_rate': 'audio_excellent_trans_rate',
        'video_trans_delay': 'video_trans_delay',
        'audio_trans_delay': 'audio_trans_delay'
    }

    def __init__(self, date=None, join_success_rate=None, join_success_in5secs_rate=None, video_freeze_rate=None, audio_freeze_rate=None, first_video_recv_time=None, first_audio_recv_time=None, pull_stream_success_rate=None, push_stream_success_rate=None, video_upstream_excellent_trans_rate=None, audio_upstream_excellent_trans_rate=None, video_excellent_trans_rate=None, audio_excellent_trans_rate=None, video_trans_delay=None, audio_trans_delay=None):
        r"""RtcHistoryQualityTimeValue

        The model defined in huaweicloud sdk

        :param date: 采样时间。日期格式按照ISO8601表示法，并使用UTC时间。格式为YYYY-MM-DD
        :type date: str
        :param join_success_rate: 加入房间成功率参数取值，取值为1代表成功率100%
        :type join_success_rate: float
        :param join_success_in5secs_rate: 5s内加入房间成功率参数取值，取值为1代表成功率100%
        :type join_success_in5secs_rate: float
        :param video_freeze_rate: 视频卡顿率参数取值，取值为1代表卡顿率100%
        :type video_freeze_rate: float
        :param audio_freeze_rate: 音频卡顿率参数取值，取值为1代表卡顿率100%
        :type audio_freeze_rate: float
        :param first_video_recv_time: 首帧视频接收耗时，单位毫秒
        :type first_video_recv_time: int
        :param first_audio_recv_time: 首帧音频接收耗时，单位毫秒
        :type first_audio_recv_time: int
        :param pull_stream_success_rate: 拉流成功率参数取值，取值为1代表成功率100%
        :type pull_stream_success_rate: float
        :param push_stream_success_rate: 推流成功率参数取值，取值为1代表成功率100%
        :type push_stream_success_rate: float
        :param video_upstream_excellent_trans_rate: 客户端视频上行优质传输率，取值为1代表传输率100%
        :type video_upstream_excellent_trans_rate: float
        :param audio_upstream_excellent_trans_rate: 客户端音频上行优质传输率，取值为1代表传输率100%
        :type audio_upstream_excellent_trans_rate: float
        :param video_excellent_trans_rate: 端到端视频优质传输率，取值为1代表传输率100%
        :type video_excellent_trans_rate: float
        :param audio_excellent_trans_rate: 端到端音频优质传输率，取值为1代表传输率100%
        :type audio_excellent_trans_rate: float
        :param video_trans_delay: 端到端视频网络时延，单位为毫秒，取当天所有用户网络延迟的中位数。
        :type video_trans_delay: float
        :param audio_trans_delay: 端到端音频网络时延，单位为毫秒，取当天所有用户网络延迟的中位数。
        :type audio_trans_delay: float
        """
        
        

        self._date = None
        self._join_success_rate = None
        self._join_success_in5secs_rate = None
        self._video_freeze_rate = None
        self._audio_freeze_rate = None
        self._first_video_recv_time = None
        self._first_audio_recv_time = None
        self._pull_stream_success_rate = None
        self._push_stream_success_rate = None
        self._video_upstream_excellent_trans_rate = None
        self._audio_upstream_excellent_trans_rate = None
        self._video_excellent_trans_rate = None
        self._audio_excellent_trans_rate = None
        self._video_trans_delay = None
        self._audio_trans_delay = None
        self.discriminator = None

        if date is not None:
            self.date = date
        if join_success_rate is not None:
            self.join_success_rate = join_success_rate
        if join_success_in5secs_rate is not None:
            self.join_success_in5secs_rate = join_success_in5secs_rate
        if video_freeze_rate is not None:
            self.video_freeze_rate = video_freeze_rate
        if audio_freeze_rate is not None:
            self.audio_freeze_rate = audio_freeze_rate
        if first_video_recv_time is not None:
            self.first_video_recv_time = first_video_recv_time
        if first_audio_recv_time is not None:
            self.first_audio_recv_time = first_audio_recv_time
        if pull_stream_success_rate is not None:
            self.pull_stream_success_rate = pull_stream_success_rate
        if push_stream_success_rate is not None:
            self.push_stream_success_rate = push_stream_success_rate
        if video_upstream_excellent_trans_rate is not None:
            self.video_upstream_excellent_trans_rate = video_upstream_excellent_trans_rate
        if audio_upstream_excellent_trans_rate is not None:
            self.audio_upstream_excellent_trans_rate = audio_upstream_excellent_trans_rate
        if video_excellent_trans_rate is not None:
            self.video_excellent_trans_rate = video_excellent_trans_rate
        if audio_excellent_trans_rate is not None:
            self.audio_excellent_trans_rate = audio_excellent_trans_rate
        if video_trans_delay is not None:
            self.video_trans_delay = video_trans_delay
        if audio_trans_delay is not None:
            self.audio_trans_delay = audio_trans_delay

    @property
    def date(self):
        r"""Gets the date of this RtcHistoryQualityTimeValue.

        采样时间。日期格式按照ISO8601表示法，并使用UTC时间。格式为YYYY-MM-DD

        :return: The date of this RtcHistoryQualityTimeValue.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this RtcHistoryQualityTimeValue.

        采样时间。日期格式按照ISO8601表示法，并使用UTC时间。格式为YYYY-MM-DD

        :param date: The date of this RtcHistoryQualityTimeValue.
        :type date: str
        """
        self._date = date

    @property
    def join_success_rate(self):
        r"""Gets the join_success_rate of this RtcHistoryQualityTimeValue.

        加入房间成功率参数取值，取值为1代表成功率100%

        :return: The join_success_rate of this RtcHistoryQualityTimeValue.
        :rtype: float
        """
        return self._join_success_rate

    @join_success_rate.setter
    def join_success_rate(self, join_success_rate):
        r"""Sets the join_success_rate of this RtcHistoryQualityTimeValue.

        加入房间成功率参数取值，取值为1代表成功率100%

        :param join_success_rate: The join_success_rate of this RtcHistoryQualityTimeValue.
        :type join_success_rate: float
        """
        self._join_success_rate = join_success_rate

    @property
    def join_success_in5secs_rate(self):
        r"""Gets the join_success_in5secs_rate of this RtcHistoryQualityTimeValue.

        5s内加入房间成功率参数取值，取值为1代表成功率100%

        :return: The join_success_in5secs_rate of this RtcHistoryQualityTimeValue.
        :rtype: float
        """
        return self._join_success_in5secs_rate

    @join_success_in5secs_rate.setter
    def join_success_in5secs_rate(self, join_success_in5secs_rate):
        r"""Sets the join_success_in5secs_rate of this RtcHistoryQualityTimeValue.

        5s内加入房间成功率参数取值，取值为1代表成功率100%

        :param join_success_in5secs_rate: The join_success_in5secs_rate of this RtcHistoryQualityTimeValue.
        :type join_success_in5secs_rate: float
        """
        self._join_success_in5secs_rate = join_success_in5secs_rate

    @property
    def video_freeze_rate(self):
        r"""Gets the video_freeze_rate of this RtcHistoryQualityTimeValue.

        视频卡顿率参数取值，取值为1代表卡顿率100%

        :return: The video_freeze_rate of this RtcHistoryQualityTimeValue.
        :rtype: float
        """
        return self._video_freeze_rate

    @video_freeze_rate.setter
    def video_freeze_rate(self, video_freeze_rate):
        r"""Sets the video_freeze_rate of this RtcHistoryQualityTimeValue.

        视频卡顿率参数取值，取值为1代表卡顿率100%

        :param video_freeze_rate: The video_freeze_rate of this RtcHistoryQualityTimeValue.
        :type video_freeze_rate: float
        """
        self._video_freeze_rate = video_freeze_rate

    @property
    def audio_freeze_rate(self):
        r"""Gets the audio_freeze_rate of this RtcHistoryQualityTimeValue.

        音频卡顿率参数取值，取值为1代表卡顿率100%

        :return: The audio_freeze_rate of this RtcHistoryQualityTimeValue.
        :rtype: float
        """
        return self._audio_freeze_rate

    @audio_freeze_rate.setter
    def audio_freeze_rate(self, audio_freeze_rate):
        r"""Sets the audio_freeze_rate of this RtcHistoryQualityTimeValue.

        音频卡顿率参数取值，取值为1代表卡顿率100%

        :param audio_freeze_rate: The audio_freeze_rate of this RtcHistoryQualityTimeValue.
        :type audio_freeze_rate: float
        """
        self._audio_freeze_rate = audio_freeze_rate

    @property
    def first_video_recv_time(self):
        r"""Gets the first_video_recv_time of this RtcHistoryQualityTimeValue.

        首帧视频接收耗时，单位毫秒

        :return: The first_video_recv_time of this RtcHistoryQualityTimeValue.
        :rtype: int
        """
        return self._first_video_recv_time

    @first_video_recv_time.setter
    def first_video_recv_time(self, first_video_recv_time):
        r"""Sets the first_video_recv_time of this RtcHistoryQualityTimeValue.

        首帧视频接收耗时，单位毫秒

        :param first_video_recv_time: The first_video_recv_time of this RtcHistoryQualityTimeValue.
        :type first_video_recv_time: int
        """
        self._first_video_recv_time = first_video_recv_time

    @property
    def first_audio_recv_time(self):
        r"""Gets the first_audio_recv_time of this RtcHistoryQualityTimeValue.

        首帧音频接收耗时，单位毫秒

        :return: The first_audio_recv_time of this RtcHistoryQualityTimeValue.
        :rtype: int
        """
        return self._first_audio_recv_time

    @first_audio_recv_time.setter
    def first_audio_recv_time(self, first_audio_recv_time):
        r"""Sets the first_audio_recv_time of this RtcHistoryQualityTimeValue.

        首帧音频接收耗时，单位毫秒

        :param first_audio_recv_time: The first_audio_recv_time of this RtcHistoryQualityTimeValue.
        :type first_audio_recv_time: int
        """
        self._first_audio_recv_time = first_audio_recv_time

    @property
    def pull_stream_success_rate(self):
        r"""Gets the pull_stream_success_rate of this RtcHistoryQualityTimeValue.

        拉流成功率参数取值，取值为1代表成功率100%

        :return: The pull_stream_success_rate of this RtcHistoryQualityTimeValue.
        :rtype: float
        """
        return self._pull_stream_success_rate

    @pull_stream_success_rate.setter
    def pull_stream_success_rate(self, pull_stream_success_rate):
        r"""Sets the pull_stream_success_rate of this RtcHistoryQualityTimeValue.

        拉流成功率参数取值，取值为1代表成功率100%

        :param pull_stream_success_rate: The pull_stream_success_rate of this RtcHistoryQualityTimeValue.
        :type pull_stream_success_rate: float
        """
        self._pull_stream_success_rate = pull_stream_success_rate

    @property
    def push_stream_success_rate(self):
        r"""Gets the push_stream_success_rate of this RtcHistoryQualityTimeValue.

        推流成功率参数取值，取值为1代表成功率100%

        :return: The push_stream_success_rate of this RtcHistoryQualityTimeValue.
        :rtype: float
        """
        return self._push_stream_success_rate

    @push_stream_success_rate.setter
    def push_stream_success_rate(self, push_stream_success_rate):
        r"""Sets the push_stream_success_rate of this RtcHistoryQualityTimeValue.

        推流成功率参数取值，取值为1代表成功率100%

        :param push_stream_success_rate: The push_stream_success_rate of this RtcHistoryQualityTimeValue.
        :type push_stream_success_rate: float
        """
        self._push_stream_success_rate = push_stream_success_rate

    @property
    def video_upstream_excellent_trans_rate(self):
        r"""Gets the video_upstream_excellent_trans_rate of this RtcHistoryQualityTimeValue.

        客户端视频上行优质传输率，取值为1代表传输率100%

        :return: The video_upstream_excellent_trans_rate of this RtcHistoryQualityTimeValue.
        :rtype: float
        """
        return self._video_upstream_excellent_trans_rate

    @video_upstream_excellent_trans_rate.setter
    def video_upstream_excellent_trans_rate(self, video_upstream_excellent_trans_rate):
        r"""Sets the video_upstream_excellent_trans_rate of this RtcHistoryQualityTimeValue.

        客户端视频上行优质传输率，取值为1代表传输率100%

        :param video_upstream_excellent_trans_rate: The video_upstream_excellent_trans_rate of this RtcHistoryQualityTimeValue.
        :type video_upstream_excellent_trans_rate: float
        """
        self._video_upstream_excellent_trans_rate = video_upstream_excellent_trans_rate

    @property
    def audio_upstream_excellent_trans_rate(self):
        r"""Gets the audio_upstream_excellent_trans_rate of this RtcHistoryQualityTimeValue.

        客户端音频上行优质传输率，取值为1代表传输率100%

        :return: The audio_upstream_excellent_trans_rate of this RtcHistoryQualityTimeValue.
        :rtype: float
        """
        return self._audio_upstream_excellent_trans_rate

    @audio_upstream_excellent_trans_rate.setter
    def audio_upstream_excellent_trans_rate(self, audio_upstream_excellent_trans_rate):
        r"""Sets the audio_upstream_excellent_trans_rate of this RtcHistoryQualityTimeValue.

        客户端音频上行优质传输率，取值为1代表传输率100%

        :param audio_upstream_excellent_trans_rate: The audio_upstream_excellent_trans_rate of this RtcHistoryQualityTimeValue.
        :type audio_upstream_excellent_trans_rate: float
        """
        self._audio_upstream_excellent_trans_rate = audio_upstream_excellent_trans_rate

    @property
    def video_excellent_trans_rate(self):
        r"""Gets the video_excellent_trans_rate of this RtcHistoryQualityTimeValue.

        端到端视频优质传输率，取值为1代表传输率100%

        :return: The video_excellent_trans_rate of this RtcHistoryQualityTimeValue.
        :rtype: float
        """
        return self._video_excellent_trans_rate

    @video_excellent_trans_rate.setter
    def video_excellent_trans_rate(self, video_excellent_trans_rate):
        r"""Sets the video_excellent_trans_rate of this RtcHistoryQualityTimeValue.

        端到端视频优质传输率，取值为1代表传输率100%

        :param video_excellent_trans_rate: The video_excellent_trans_rate of this RtcHistoryQualityTimeValue.
        :type video_excellent_trans_rate: float
        """
        self._video_excellent_trans_rate = video_excellent_trans_rate

    @property
    def audio_excellent_trans_rate(self):
        r"""Gets the audio_excellent_trans_rate of this RtcHistoryQualityTimeValue.

        端到端音频优质传输率，取值为1代表传输率100%

        :return: The audio_excellent_trans_rate of this RtcHistoryQualityTimeValue.
        :rtype: float
        """
        return self._audio_excellent_trans_rate

    @audio_excellent_trans_rate.setter
    def audio_excellent_trans_rate(self, audio_excellent_trans_rate):
        r"""Sets the audio_excellent_trans_rate of this RtcHistoryQualityTimeValue.

        端到端音频优质传输率，取值为1代表传输率100%

        :param audio_excellent_trans_rate: The audio_excellent_trans_rate of this RtcHistoryQualityTimeValue.
        :type audio_excellent_trans_rate: float
        """
        self._audio_excellent_trans_rate = audio_excellent_trans_rate

    @property
    def video_trans_delay(self):
        r"""Gets the video_trans_delay of this RtcHistoryQualityTimeValue.

        端到端视频网络时延，单位为毫秒，取当天所有用户网络延迟的中位数。

        :return: The video_trans_delay of this RtcHistoryQualityTimeValue.
        :rtype: float
        """
        return self._video_trans_delay

    @video_trans_delay.setter
    def video_trans_delay(self, video_trans_delay):
        r"""Sets the video_trans_delay of this RtcHistoryQualityTimeValue.

        端到端视频网络时延，单位为毫秒，取当天所有用户网络延迟的中位数。

        :param video_trans_delay: The video_trans_delay of this RtcHistoryQualityTimeValue.
        :type video_trans_delay: float
        """
        self._video_trans_delay = video_trans_delay

    @property
    def audio_trans_delay(self):
        r"""Gets the audio_trans_delay of this RtcHistoryQualityTimeValue.

        端到端音频网络时延，单位为毫秒，取当天所有用户网络延迟的中位数。

        :return: The audio_trans_delay of this RtcHistoryQualityTimeValue.
        :rtype: float
        """
        return self._audio_trans_delay

    @audio_trans_delay.setter
    def audio_trans_delay(self, audio_trans_delay):
        r"""Sets the audio_trans_delay of this RtcHistoryQualityTimeValue.

        端到端音频网络时延，单位为毫秒，取当天所有用户网络延迟的中位数。

        :param audio_trans_delay: The audio_trans_delay of this RtcHistoryQualityTimeValue.
        :type audio_trans_delay: float
        """
        self._audio_trans_delay = audio_trans_delay

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
        if not isinstance(other, RtcHistoryQualityTimeValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
