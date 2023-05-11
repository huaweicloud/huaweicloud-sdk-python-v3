# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RtcHistoryScaleTimeValue:

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
        'user_count': 'int',
        'session_count': 'int',
        'room_count': 'int',
        'max_online_user_count': 'int',
        'max_online_room_count': 'int',
        'communication_duration': 'int',
        'video_communication_duration': 'int',
        'audio_communication_duration': 'int'
    }

    attribute_map = {
        'date': 'date',
        'user_count': 'user_count',
        'session_count': 'session_count',
        'room_count': 'room_count',
        'max_online_user_count': 'max_online_user_count',
        'max_online_room_count': 'max_online_room_count',
        'communication_duration': 'communication_duration',
        'video_communication_duration': 'video_communication_duration',
        'audio_communication_duration': 'audio_communication_duration'
    }

    def __init__(self, date=None, user_count=None, session_count=None, room_count=None, max_online_user_count=None, max_online_room_count=None, communication_duration=None, video_communication_duration=None, audio_communication_duration=None):
        """RtcHistoryScaleTimeValue

        The model defined in huaweicloud sdk

        :param date: 采样时间。日期格式按照ISO8601表示法，并使用UTC时间。格式为YYYY-MM-DD
        :type date: str
        :param user_count: 通话人数，指总的uid个数
        :type user_count: int
        :param session_count: 通话人次，指总的session个数
        :type session_count: int
        :param room_count: 房间数
        :type room_count: int
        :param max_online_user_count: 最大同时在线人数
        :type max_online_user_count: int
        :param max_online_room_count: 最大同时在线房间数
        :type max_online_room_count: int
        :param communication_duration: 音视频通话总时长，单位秒
        :type communication_duration: int
        :param video_communication_duration: 视频通话总时长，单位秒
        :type video_communication_duration: int
        :param audio_communication_duration: 音频通话总时长，单位秒
        :type audio_communication_duration: int
        """
        
        

        self._date = None
        self._user_count = None
        self._session_count = None
        self._room_count = None
        self._max_online_user_count = None
        self._max_online_room_count = None
        self._communication_duration = None
        self._video_communication_duration = None
        self._audio_communication_duration = None
        self.discriminator = None

        if date is not None:
            self.date = date
        if user_count is not None:
            self.user_count = user_count
        if session_count is not None:
            self.session_count = session_count
        if room_count is not None:
            self.room_count = room_count
        if max_online_user_count is not None:
            self.max_online_user_count = max_online_user_count
        if max_online_room_count is not None:
            self.max_online_room_count = max_online_room_count
        if communication_duration is not None:
            self.communication_duration = communication_duration
        if video_communication_duration is not None:
            self.video_communication_duration = video_communication_duration
        if audio_communication_duration is not None:
            self.audio_communication_duration = audio_communication_duration

    @property
    def date(self):
        """Gets the date of this RtcHistoryScaleTimeValue.

        采样时间。日期格式按照ISO8601表示法，并使用UTC时间。格式为YYYY-MM-DD

        :return: The date of this RtcHistoryScaleTimeValue.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this RtcHistoryScaleTimeValue.

        采样时间。日期格式按照ISO8601表示法，并使用UTC时间。格式为YYYY-MM-DD

        :param date: The date of this RtcHistoryScaleTimeValue.
        :type date: str
        """
        self._date = date

    @property
    def user_count(self):
        """Gets the user_count of this RtcHistoryScaleTimeValue.

        通话人数，指总的uid个数

        :return: The user_count of this RtcHistoryScaleTimeValue.
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """Sets the user_count of this RtcHistoryScaleTimeValue.

        通话人数，指总的uid个数

        :param user_count: The user_count of this RtcHistoryScaleTimeValue.
        :type user_count: int
        """
        self._user_count = user_count

    @property
    def session_count(self):
        """Gets the session_count of this RtcHistoryScaleTimeValue.

        通话人次，指总的session个数

        :return: The session_count of this RtcHistoryScaleTimeValue.
        :rtype: int
        """
        return self._session_count

    @session_count.setter
    def session_count(self, session_count):
        """Sets the session_count of this RtcHistoryScaleTimeValue.

        通话人次，指总的session个数

        :param session_count: The session_count of this RtcHistoryScaleTimeValue.
        :type session_count: int
        """
        self._session_count = session_count

    @property
    def room_count(self):
        """Gets the room_count of this RtcHistoryScaleTimeValue.

        房间数

        :return: The room_count of this RtcHistoryScaleTimeValue.
        :rtype: int
        """
        return self._room_count

    @room_count.setter
    def room_count(self, room_count):
        """Sets the room_count of this RtcHistoryScaleTimeValue.

        房间数

        :param room_count: The room_count of this RtcHistoryScaleTimeValue.
        :type room_count: int
        """
        self._room_count = room_count

    @property
    def max_online_user_count(self):
        """Gets the max_online_user_count of this RtcHistoryScaleTimeValue.

        最大同时在线人数

        :return: The max_online_user_count of this RtcHistoryScaleTimeValue.
        :rtype: int
        """
        return self._max_online_user_count

    @max_online_user_count.setter
    def max_online_user_count(self, max_online_user_count):
        """Sets the max_online_user_count of this RtcHistoryScaleTimeValue.

        最大同时在线人数

        :param max_online_user_count: The max_online_user_count of this RtcHistoryScaleTimeValue.
        :type max_online_user_count: int
        """
        self._max_online_user_count = max_online_user_count

    @property
    def max_online_room_count(self):
        """Gets the max_online_room_count of this RtcHistoryScaleTimeValue.

        最大同时在线房间数

        :return: The max_online_room_count of this RtcHistoryScaleTimeValue.
        :rtype: int
        """
        return self._max_online_room_count

    @max_online_room_count.setter
    def max_online_room_count(self, max_online_room_count):
        """Sets the max_online_room_count of this RtcHistoryScaleTimeValue.

        最大同时在线房间数

        :param max_online_room_count: The max_online_room_count of this RtcHistoryScaleTimeValue.
        :type max_online_room_count: int
        """
        self._max_online_room_count = max_online_room_count

    @property
    def communication_duration(self):
        """Gets the communication_duration of this RtcHistoryScaleTimeValue.

        音视频通话总时长，单位秒

        :return: The communication_duration of this RtcHistoryScaleTimeValue.
        :rtype: int
        """
        return self._communication_duration

    @communication_duration.setter
    def communication_duration(self, communication_duration):
        """Sets the communication_duration of this RtcHistoryScaleTimeValue.

        音视频通话总时长，单位秒

        :param communication_duration: The communication_duration of this RtcHistoryScaleTimeValue.
        :type communication_duration: int
        """
        self._communication_duration = communication_duration

    @property
    def video_communication_duration(self):
        """Gets the video_communication_duration of this RtcHistoryScaleTimeValue.

        视频通话总时长，单位秒

        :return: The video_communication_duration of this RtcHistoryScaleTimeValue.
        :rtype: int
        """
        return self._video_communication_duration

    @video_communication_duration.setter
    def video_communication_duration(self, video_communication_duration):
        """Sets the video_communication_duration of this RtcHistoryScaleTimeValue.

        视频通话总时长，单位秒

        :param video_communication_duration: The video_communication_duration of this RtcHistoryScaleTimeValue.
        :type video_communication_duration: int
        """
        self._video_communication_duration = video_communication_duration

    @property
    def audio_communication_duration(self):
        """Gets the audio_communication_duration of this RtcHistoryScaleTimeValue.

        音频通话总时长，单位秒

        :return: The audio_communication_duration of this RtcHistoryScaleTimeValue.
        :rtype: int
        """
        return self._audio_communication_duration

    @audio_communication_duration.setter
    def audio_communication_duration(self, audio_communication_duration):
        """Sets the audio_communication_duration of this RtcHistoryScaleTimeValue.

        音频通话总时长，单位秒

        :param audio_communication_duration: The audio_communication_duration of this RtcHistoryScaleTimeValue.
        :type audio_communication_duration: int
        """
        self._audio_communication_duration = audio_communication_duration

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
        if not isinstance(other, RtcHistoryScaleTimeValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
