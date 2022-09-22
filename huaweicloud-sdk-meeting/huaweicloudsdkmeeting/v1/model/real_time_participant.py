# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RealTimeParticipant:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'pid': 'str',
        'name': 'str',
        'phone': 'str',
        'state': 'int',
        'video': 'int',
        'mute': 'int',
        'hand': 'int'
    }

    attribute_map = {
        'pid': 'pid',
        'name': 'name',
        'phone': 'phone',
        'state': 'state',
        'video': 'video',
        'mute': 'mute',
        'hand': 'hand'
    }

    def __init__(self, pid=None, name=None, phone=None, state=None, video=None, mute=None, hand=None):
        """RealTimeParticipant

        The model defined in huaweicloud sdk

        :param pid: 与会者标识。
        :type pid: str
        :param name: 与会者名称。
        :type name: str
        :param phone: 与会者号码。
        :type phone: str
        :param state: 用户状态。 - 0: 会议中 - 1: 正在呼叫 - 2: 正在加入会议 &gt; 若会场未入会或已离会，则不会显示于在线会场列表。
        :type state: int
        :param video: 音视频能力。 - 0: 音频 - 1: 视频
        :type video: int
        :param mute: 麦克风状态。 - 0: 麦克风打开 - 1: 麦克风关闭
        :type mute: int
        :param hand: 与会者举手状态。 - 0: 未举手 - 1: 举手
        :type hand: int
        """
        
        

        self._pid = None
        self._name = None
        self._phone = None
        self._state = None
        self._video = None
        self._mute = None
        self._hand = None
        self.discriminator = None

        if pid is not None:
            self.pid = pid
        if name is not None:
            self.name = name
        if phone is not None:
            self.phone = phone
        if state is not None:
            self.state = state
        if video is not None:
            self.video = video
        if mute is not None:
            self.mute = mute
        if hand is not None:
            self.hand = hand

    @property
    def pid(self):
        """Gets the pid of this RealTimeParticipant.

        与会者标识。

        :return: The pid of this RealTimeParticipant.
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this RealTimeParticipant.

        与会者标识。

        :param pid: The pid of this RealTimeParticipant.
        :type pid: str
        """
        self._pid = pid

    @property
    def name(self):
        """Gets the name of this RealTimeParticipant.

        与会者名称。

        :return: The name of this RealTimeParticipant.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RealTimeParticipant.

        与会者名称。

        :param name: The name of this RealTimeParticipant.
        :type name: str
        """
        self._name = name

    @property
    def phone(self):
        """Gets the phone of this RealTimeParticipant.

        与会者号码。

        :return: The phone of this RealTimeParticipant.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this RealTimeParticipant.

        与会者号码。

        :param phone: The phone of this RealTimeParticipant.
        :type phone: str
        """
        self._phone = phone

    @property
    def state(self):
        """Gets the state of this RealTimeParticipant.

        用户状态。 - 0: 会议中 - 1: 正在呼叫 - 2: 正在加入会议 > 若会场未入会或已离会，则不会显示于在线会场列表。

        :return: The state of this RealTimeParticipant.
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this RealTimeParticipant.

        用户状态。 - 0: 会议中 - 1: 正在呼叫 - 2: 正在加入会议 > 若会场未入会或已离会，则不会显示于在线会场列表。

        :param state: The state of this RealTimeParticipant.
        :type state: int
        """
        self._state = state

    @property
    def video(self):
        """Gets the video of this RealTimeParticipant.

        音视频能力。 - 0: 音频 - 1: 视频

        :return: The video of this RealTimeParticipant.
        :rtype: int
        """
        return self._video

    @video.setter
    def video(self, video):
        """Sets the video of this RealTimeParticipant.

        音视频能力。 - 0: 音频 - 1: 视频

        :param video: The video of this RealTimeParticipant.
        :type video: int
        """
        self._video = video

    @property
    def mute(self):
        """Gets the mute of this RealTimeParticipant.

        麦克风状态。 - 0: 麦克风打开 - 1: 麦克风关闭

        :return: The mute of this RealTimeParticipant.
        :rtype: int
        """
        return self._mute

    @mute.setter
    def mute(self, mute):
        """Sets the mute of this RealTimeParticipant.

        麦克风状态。 - 0: 麦克风打开 - 1: 麦克风关闭

        :param mute: The mute of this RealTimeParticipant.
        :type mute: int
        """
        self._mute = mute

    @property
    def hand(self):
        """Gets the hand of this RealTimeParticipant.

        与会者举手状态。 - 0: 未举手 - 1: 举手

        :return: The hand of this RealTimeParticipant.
        :rtype: int
        """
        return self._hand

    @hand.setter
    def hand(self, hand):
        """Sets the hand of this RealTimeParticipant.

        与会者举手状态。 - 0: 未举手 - 1: 举手

        :param hand: The hand of this RealTimeParticipant.
        :type hand: int
        """
        self._hand = hand

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
        if not isinstance(other, RealTimeParticipant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
