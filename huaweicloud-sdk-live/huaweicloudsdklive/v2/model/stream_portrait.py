# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StreamPortrait:

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
        'flow': 'int',
        'play_duration': 'int',
        'request_count': 'int',
        'user_count': 'int',
        'peak_user_count': 'int',
        'peak_bandwidth': 'int',
        'push_duration': 'int'
    }

    attribute_map = {
        'time': 'time',
        'flow': 'flow',
        'play_duration': 'play_duration',
        'request_count': 'request_count',
        'user_count': 'user_count',
        'peak_user_count': 'peak_user_count',
        'peak_bandwidth': 'peak_bandwidth',
        'push_duration': 'push_duration'
    }

    def __init__(self, time=None, flow=None, play_duration=None, request_count=None, user_count=None, peak_user_count=None, peak_bandwidth=None, push_duration=None):
        """StreamPortrait

        The model defined in huaweicloud sdk

        :param time: 统计日期，日期格式按照ISO8601表示法，格式：YYYYMMDD，如20200904。统计该统计日期00:00-23:59时段的播放画像信息。
        :type time: str
        :param flow: 累计流量，单位为byte。
        :type flow: int
        :param play_duration: 累计播放时长,单位为秒。
        :type play_duration: int
        :param request_count: 累计请求次数。
        :type request_count: int
        :param user_count: 累计观看人数,根据IP去重。
        :type user_count: int
        :param peak_user_count: 峰值观看人数,flv/rtmp协议是统计Session会话ID，其它协议统计IP,1分钟的采样数据。
        :type peak_user_count: int
        :param peak_bandwidth: 峰值带宽，单位bps,5分钟的采样数据。
        :type peak_bandwidth: int
        :param push_duration: 累计直播(推流)时长,单位为秒。
        :type push_duration: int
        """
        
        

        self._time = None
        self._flow = None
        self._play_duration = None
        self._request_count = None
        self._user_count = None
        self._peak_user_count = None
        self._peak_bandwidth = None
        self._push_duration = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if flow is not None:
            self.flow = flow
        if play_duration is not None:
            self.play_duration = play_duration
        if request_count is not None:
            self.request_count = request_count
        if user_count is not None:
            self.user_count = user_count
        if peak_user_count is not None:
            self.peak_user_count = peak_user_count
        if peak_bandwidth is not None:
            self.peak_bandwidth = peak_bandwidth
        if push_duration is not None:
            self.push_duration = push_duration

    @property
    def time(self):
        """Gets the time of this StreamPortrait.

        统计日期，日期格式按照ISO8601表示法，格式：YYYYMMDD，如20200904。统计该统计日期00:00-23:59时段的播放画像信息。

        :return: The time of this StreamPortrait.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this StreamPortrait.

        统计日期，日期格式按照ISO8601表示法，格式：YYYYMMDD，如20200904。统计该统计日期00:00-23:59时段的播放画像信息。

        :param time: The time of this StreamPortrait.
        :type time: str
        """
        self._time = time

    @property
    def flow(self):
        """Gets the flow of this StreamPortrait.

        累计流量，单位为byte。

        :return: The flow of this StreamPortrait.
        :rtype: int
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        """Sets the flow of this StreamPortrait.

        累计流量，单位为byte。

        :param flow: The flow of this StreamPortrait.
        :type flow: int
        """
        self._flow = flow

    @property
    def play_duration(self):
        """Gets the play_duration of this StreamPortrait.

        累计播放时长,单位为秒。

        :return: The play_duration of this StreamPortrait.
        :rtype: int
        """
        return self._play_duration

    @play_duration.setter
    def play_duration(self, play_duration):
        """Sets the play_duration of this StreamPortrait.

        累计播放时长,单位为秒。

        :param play_duration: The play_duration of this StreamPortrait.
        :type play_duration: int
        """
        self._play_duration = play_duration

    @property
    def request_count(self):
        """Gets the request_count of this StreamPortrait.

        累计请求次数。

        :return: The request_count of this StreamPortrait.
        :rtype: int
        """
        return self._request_count

    @request_count.setter
    def request_count(self, request_count):
        """Sets the request_count of this StreamPortrait.

        累计请求次数。

        :param request_count: The request_count of this StreamPortrait.
        :type request_count: int
        """
        self._request_count = request_count

    @property
    def user_count(self):
        """Gets the user_count of this StreamPortrait.

        累计观看人数,根据IP去重。

        :return: The user_count of this StreamPortrait.
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """Sets the user_count of this StreamPortrait.

        累计观看人数,根据IP去重。

        :param user_count: The user_count of this StreamPortrait.
        :type user_count: int
        """
        self._user_count = user_count

    @property
    def peak_user_count(self):
        """Gets the peak_user_count of this StreamPortrait.

        峰值观看人数,flv/rtmp协议是统计Session会话ID，其它协议统计IP,1分钟的采样数据。

        :return: The peak_user_count of this StreamPortrait.
        :rtype: int
        """
        return self._peak_user_count

    @peak_user_count.setter
    def peak_user_count(self, peak_user_count):
        """Sets the peak_user_count of this StreamPortrait.

        峰值观看人数,flv/rtmp协议是统计Session会话ID，其它协议统计IP,1分钟的采样数据。

        :param peak_user_count: The peak_user_count of this StreamPortrait.
        :type peak_user_count: int
        """
        self._peak_user_count = peak_user_count

    @property
    def peak_bandwidth(self):
        """Gets the peak_bandwidth of this StreamPortrait.

        峰值带宽，单位bps,5分钟的采样数据。

        :return: The peak_bandwidth of this StreamPortrait.
        :rtype: int
        """
        return self._peak_bandwidth

    @peak_bandwidth.setter
    def peak_bandwidth(self, peak_bandwidth):
        """Sets the peak_bandwidth of this StreamPortrait.

        峰值带宽，单位bps,5分钟的采样数据。

        :param peak_bandwidth: The peak_bandwidth of this StreamPortrait.
        :type peak_bandwidth: int
        """
        self._peak_bandwidth = peak_bandwidth

    @property
    def push_duration(self):
        """Gets the push_duration of this StreamPortrait.

        累计直播(推流)时长,单位为秒。

        :return: The push_duration of this StreamPortrait.
        :rtype: int
        """
        return self._push_duration

    @push_duration.setter
    def push_duration(self, push_duration):
        """Sets the push_duration of this StreamPortrait.

        累计直播(推流)时长,单位为秒。

        :param push_duration: The push_duration of this StreamPortrait.
        :type push_duration: int
        """
        self._push_duration = push_duration

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
        if not isinstance(other, StreamPortrait):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
