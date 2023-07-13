# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RtcServerRoomInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'app': 'str',
        'room_id': 'str',
        'state': 'str',
        'duration': 'int',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'app': 'app',
        'room_id': 'room_id',
        'state': 'state',
        'duration': 'duration',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, domain=None, app=None, room_id=None, state=None, duration=None, start_time=None, end_time=None):
        """RtcServerRoomInfo

        The model defined in huaweicloud sdk

        :param domain: 域名
        :type domain: str
        :param app: 应用标识
        :type app: str
        :param room_id: 房间ID
        :type room_id: str
        :param state: 房间状态，取值如下：  - RUNNING：开启中  - CLOSED：已关闭 
        :type state: str
        :param duration: 房间持续时长
        :type duration: int
        :param start_time: 房间开始时间，即第一个用户加入房间时间，UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T07:00:00Z 
        :type start_time: str
        :param end_time: 房间关闭时间，即最后一个room_uuid关闭的时间，UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T07:00:00Z，若房间未关闭，则返回 “-” 
        :type end_time: str
        """
        
        

        self._domain = None
        self._app = None
        self._room_id = None
        self._state = None
        self._duration = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if app is not None:
            self.app = app
        if room_id is not None:
            self.room_id = room_id
        if state is not None:
            self.state = state
        if duration is not None:
            self.duration = duration
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def domain(self):
        """Gets the domain of this RtcServerRoomInfo.

        域名

        :return: The domain of this RtcServerRoomInfo.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this RtcServerRoomInfo.

        域名

        :param domain: The domain of this RtcServerRoomInfo.
        :type domain: str
        """
        self._domain = domain

    @property
    def app(self):
        """Gets the app of this RtcServerRoomInfo.

        应用标识

        :return: The app of this RtcServerRoomInfo.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this RtcServerRoomInfo.

        应用标识

        :param app: The app of this RtcServerRoomInfo.
        :type app: str
        """
        self._app = app

    @property
    def room_id(self):
        """Gets the room_id of this RtcServerRoomInfo.

        房间ID

        :return: The room_id of this RtcServerRoomInfo.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this RtcServerRoomInfo.

        房间ID

        :param room_id: The room_id of this RtcServerRoomInfo.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def state(self):
        """Gets the state of this RtcServerRoomInfo.

        房间状态，取值如下：  - RUNNING：开启中  - CLOSED：已关闭 

        :return: The state of this RtcServerRoomInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this RtcServerRoomInfo.

        房间状态，取值如下：  - RUNNING：开启中  - CLOSED：已关闭 

        :param state: The state of this RtcServerRoomInfo.
        :type state: str
        """
        self._state = state

    @property
    def duration(self):
        """Gets the duration of this RtcServerRoomInfo.

        房间持续时长

        :return: The duration of this RtcServerRoomInfo.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this RtcServerRoomInfo.

        房间持续时长

        :param duration: The duration of this RtcServerRoomInfo.
        :type duration: int
        """
        self._duration = duration

    @property
    def start_time(self):
        """Gets the start_time of this RtcServerRoomInfo.

        房间开始时间，即第一个用户加入房间时间，UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T07:00:00Z 

        :return: The start_time of this RtcServerRoomInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this RtcServerRoomInfo.

        房间开始时间，即第一个用户加入房间时间，UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T07:00:00Z 

        :param start_time: The start_time of this RtcServerRoomInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this RtcServerRoomInfo.

        房间关闭时间，即最后一个room_uuid关闭的时间，UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T07:00:00Z，若房间未关闭，则返回 “-” 

        :return: The end_time of this RtcServerRoomInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this RtcServerRoomInfo.

        房间关闭时间，即最后一个room_uuid关闭的时间，UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T07:00:00Z，若房间未关闭，则返回 “-” 

        :param end_time: The end_time of this RtcServerRoomInfo.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, RtcServerRoomInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
