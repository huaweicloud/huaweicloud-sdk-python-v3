# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReadWrite:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'accept_count': 'int',
        'accept_rate': 'int',
        'channel_id': 'str',
        'channel_instance_count': 'int',
        'heart_beat': 'str',
        'heart_beat_time': 'int',
        'latest_transmission_time': 'datetime',
        'minion_id': 'str',
        'send_count': 'int',
        'send_rate': 'int'
    }

    attribute_map = {
        'accept_count': 'accept_count',
        'accept_rate': 'accept_rate',
        'channel_id': 'channel_id',
        'channel_instance_count': 'channel_instance_count',
        'heart_beat': 'heart_beat',
        'heart_beat_time': 'heart_beat_time',
        'latest_transmission_time': 'latest_transmission_time',
        'minion_id': 'minion_id',
        'send_count': 'send_count',
        'send_rate': 'send_rate'
    }

    def __init__(self, accept_count=None, accept_rate=None, channel_id=None, channel_instance_count=None, heart_beat=None, heart_beat_time=None, latest_transmission_time=None, minion_id=None, send_count=None, send_rate=None):
        r"""ReadWrite

        The model defined in huaweicloud sdk

        :param accept_count: 数值
        :type accept_count: int
        :param accept_rate: 数值
        :type accept_rate: int
        :param channel_id: UUID
        :type channel_id: str
        :param channel_instance_count: 采集通道实例的数量
        :type channel_instance_count: int
        :param heart_beat: **参数解释**: 节点是否成功收到心跳信号 - ONLINE 在线 - OFFLINE 离线  **约束限制** 不涉及 **取值范围**: - ONLINE - OFFLINE  **默认值** 不涉及
        :type heart_beat: str
        :param heart_beat_time: 最后一次接收到心跳信号的时间
        :type heart_beat_time: int
        :param latest_transmission_time: 最后一次传输的时间
        :type latest_transmission_time: datetime
        :param minion_id: UUID
        :type minion_id: str
        :param send_count: 数值
        :type send_count: int
        :param send_rate: 数值
        :type send_rate: int
        """
        
        

        self._accept_count = None
        self._accept_rate = None
        self._channel_id = None
        self._channel_instance_count = None
        self._heart_beat = None
        self._heart_beat_time = None
        self._latest_transmission_time = None
        self._minion_id = None
        self._send_count = None
        self._send_rate = None
        self.discriminator = None

        if accept_count is not None:
            self.accept_count = accept_count
        if accept_rate is not None:
            self.accept_rate = accept_rate
        if channel_id is not None:
            self.channel_id = channel_id
        if channel_instance_count is not None:
            self.channel_instance_count = channel_instance_count
        if heart_beat is not None:
            self.heart_beat = heart_beat
        if heart_beat_time is not None:
            self.heart_beat_time = heart_beat_time
        if latest_transmission_time is not None:
            self.latest_transmission_time = latest_transmission_time
        if minion_id is not None:
            self.minion_id = minion_id
        if send_count is not None:
            self.send_count = send_count
        if send_rate is not None:
            self.send_rate = send_rate

    @property
    def accept_count(self):
        r"""Gets the accept_count of this ReadWrite.

        数值

        :return: The accept_count of this ReadWrite.
        :rtype: int
        """
        return self._accept_count

    @accept_count.setter
    def accept_count(self, accept_count):
        r"""Sets the accept_count of this ReadWrite.

        数值

        :param accept_count: The accept_count of this ReadWrite.
        :type accept_count: int
        """
        self._accept_count = accept_count

    @property
    def accept_rate(self):
        r"""Gets the accept_rate of this ReadWrite.

        数值

        :return: The accept_rate of this ReadWrite.
        :rtype: int
        """
        return self._accept_rate

    @accept_rate.setter
    def accept_rate(self, accept_rate):
        r"""Sets the accept_rate of this ReadWrite.

        数值

        :param accept_rate: The accept_rate of this ReadWrite.
        :type accept_rate: int
        """
        self._accept_rate = accept_rate

    @property
    def channel_id(self):
        r"""Gets the channel_id of this ReadWrite.

        UUID

        :return: The channel_id of this ReadWrite.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        r"""Sets the channel_id of this ReadWrite.

        UUID

        :param channel_id: The channel_id of this ReadWrite.
        :type channel_id: str
        """
        self._channel_id = channel_id

    @property
    def channel_instance_count(self):
        r"""Gets the channel_instance_count of this ReadWrite.

        采集通道实例的数量

        :return: The channel_instance_count of this ReadWrite.
        :rtype: int
        """
        return self._channel_instance_count

    @channel_instance_count.setter
    def channel_instance_count(self, channel_instance_count):
        r"""Sets the channel_instance_count of this ReadWrite.

        采集通道实例的数量

        :param channel_instance_count: The channel_instance_count of this ReadWrite.
        :type channel_instance_count: int
        """
        self._channel_instance_count = channel_instance_count

    @property
    def heart_beat(self):
        r"""Gets the heart_beat of this ReadWrite.

        **参数解释**: 节点是否成功收到心跳信号 - ONLINE 在线 - OFFLINE 离线  **约束限制** 不涉及 **取值范围**: - ONLINE - OFFLINE  **默认值** 不涉及

        :return: The heart_beat of this ReadWrite.
        :rtype: str
        """
        return self._heart_beat

    @heart_beat.setter
    def heart_beat(self, heart_beat):
        r"""Sets the heart_beat of this ReadWrite.

        **参数解释**: 节点是否成功收到心跳信号 - ONLINE 在线 - OFFLINE 离线  **约束限制** 不涉及 **取值范围**: - ONLINE - OFFLINE  **默认值** 不涉及

        :param heart_beat: The heart_beat of this ReadWrite.
        :type heart_beat: str
        """
        self._heart_beat = heart_beat

    @property
    def heart_beat_time(self):
        r"""Gets the heart_beat_time of this ReadWrite.

        最后一次接收到心跳信号的时间

        :return: The heart_beat_time of this ReadWrite.
        :rtype: int
        """
        return self._heart_beat_time

    @heart_beat_time.setter
    def heart_beat_time(self, heart_beat_time):
        r"""Sets the heart_beat_time of this ReadWrite.

        最后一次接收到心跳信号的时间

        :param heart_beat_time: The heart_beat_time of this ReadWrite.
        :type heart_beat_time: int
        """
        self._heart_beat_time = heart_beat_time

    @property
    def latest_transmission_time(self):
        r"""Gets the latest_transmission_time of this ReadWrite.

        最后一次传输的时间

        :return: The latest_transmission_time of this ReadWrite.
        :rtype: datetime
        """
        return self._latest_transmission_time

    @latest_transmission_time.setter
    def latest_transmission_time(self, latest_transmission_time):
        r"""Sets the latest_transmission_time of this ReadWrite.

        最后一次传输的时间

        :param latest_transmission_time: The latest_transmission_time of this ReadWrite.
        :type latest_transmission_time: datetime
        """
        self._latest_transmission_time = latest_transmission_time

    @property
    def minion_id(self):
        r"""Gets the minion_id of this ReadWrite.

        UUID

        :return: The minion_id of this ReadWrite.
        :rtype: str
        """
        return self._minion_id

    @minion_id.setter
    def minion_id(self, minion_id):
        r"""Sets the minion_id of this ReadWrite.

        UUID

        :param minion_id: The minion_id of this ReadWrite.
        :type minion_id: str
        """
        self._minion_id = minion_id

    @property
    def send_count(self):
        r"""Gets the send_count of this ReadWrite.

        数值

        :return: The send_count of this ReadWrite.
        :rtype: int
        """
        return self._send_count

    @send_count.setter
    def send_count(self, send_count):
        r"""Sets the send_count of this ReadWrite.

        数值

        :param send_count: The send_count of this ReadWrite.
        :type send_count: int
        """
        self._send_count = send_count

    @property
    def send_rate(self):
        r"""Gets the send_rate of this ReadWrite.

        数值

        :return: The send_rate of this ReadWrite.
        :rtype: int
        """
        return self._send_rate

    @send_rate.setter
    def send_rate(self, send_rate):
        r"""Sets the send_rate of this ReadWrite.

        数值

        :param send_rate: The send_rate of this ReadWrite.
        :type send_rate: int
        """
        self._send_rate = send_rate

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReadWrite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
