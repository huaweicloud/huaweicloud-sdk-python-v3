# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpQueryCfwAttackLogsResponseDTODataRecords:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'direction': 'str',
        'action': 'str',
        'event_time': 'str',
        'attack_type': 'str',
        'attack_rule': 'str',
        'level': 'str',
        'source': 'str',
        'packet_length': 'int',
        'attack_rule_id': 'int',
        'hit_time': 'int',
        'log_id': 'str',
        'src_ip': 'str',
        'src_port': 'int',
        'dst_ip': 'str',
        'dst_port': 'int',
        'protocol': 'str',
        'packet': 'Packet',
        'app': 'str',
        'packet_messages': 'list[PacketMessage]'
    }

    attribute_map = {
        'direction': 'direction',
        'action': 'action',
        'event_time': 'event_time',
        'attack_type': 'attack_type',
        'attack_rule': 'attack_rule',
        'level': 'level',
        'source': 'source',
        'packet_length': 'packet_length',
        'attack_rule_id': 'attack_rule_id',
        'hit_time': 'hit_time',
        'log_id': 'log_id',
        'src_ip': 'src_ip',
        'src_port': 'src_port',
        'dst_ip': 'dst_ip',
        'dst_port': 'dst_port',
        'protocol': 'protocol',
        'packet': 'packet',
        'app': 'app',
        'packet_messages': 'packetMessages'
    }

    def __init__(self, direction=None, action=None, event_time=None, attack_type=None, attack_rule=None, level=None, source=None, packet_length=None, attack_rule_id=None, hit_time=None, log_id=None, src_ip=None, src_port=None, dst_ip=None, dst_port=None, protocol=None, packet=None, app=None, packet_messages=None):
        """HttpQueryCfwAttackLogsResponseDTODataRecords

        The model defined in huaweicloud sdk

        :param direction: 方向，有内到外和外到内两种
        :type direction: str
        :param action: 动作
        :type action: str
        :param event_time: 事件时间
        :type event_time: str
        :param attack_type: 攻击类型
        :type attack_type: str
        :param attack_rule: 攻击规则
        :type attack_rule: str
        :param level: 威胁等级
        :type level: str
        :param source: 来源
        :type source: str
        :param packet_length: 报文长度
        :type packet_length: int
        :param attack_rule_id: 攻击规则id
        :type attack_rule_id: int
        :param hit_time: 命中时间
        :type hit_time: int
        :param log_id: 日志ID
        :type log_id: str
        :param src_ip: 源IP
        :type src_ip: str
        :param src_port: 源端口
        :type src_port: int
        :param dst_ip: 目的IP
        :type dst_ip: str
        :param dst_port: 目的端口
        :type dst_port: int
        :param protocol: 协议
        :type protocol: str
        :param packet: 
        :type packet: :class:`huaweicloudsdkcfw.v1.Packet`
        :param app: 应用协议
        :type app: str
        :param packet_messages: 攻击报文信息
        :type packet_messages: list[:class:`huaweicloudsdkcfw.v1.PacketMessage`]
        """
        
        

        self._direction = None
        self._action = None
        self._event_time = None
        self._attack_type = None
        self._attack_rule = None
        self._level = None
        self._source = None
        self._packet_length = None
        self._attack_rule_id = None
        self._hit_time = None
        self._log_id = None
        self._src_ip = None
        self._src_port = None
        self._dst_ip = None
        self._dst_port = None
        self._protocol = None
        self._packet = None
        self._app = None
        self._packet_messages = None
        self.discriminator = None

        if direction is not None:
            self.direction = direction
        if action is not None:
            self.action = action
        if event_time is not None:
            self.event_time = event_time
        if attack_type is not None:
            self.attack_type = attack_type
        if attack_rule is not None:
            self.attack_rule = attack_rule
        if level is not None:
            self.level = level
        if source is not None:
            self.source = source
        if packet_length is not None:
            self.packet_length = packet_length
        if attack_rule_id is not None:
            self.attack_rule_id = attack_rule_id
        if hit_time is not None:
            self.hit_time = hit_time
        if log_id is not None:
            self.log_id = log_id
        if src_ip is not None:
            self.src_ip = src_ip
        if src_port is not None:
            self.src_port = src_port
        if dst_ip is not None:
            self.dst_ip = dst_ip
        if dst_port is not None:
            self.dst_port = dst_port
        if protocol is not None:
            self.protocol = protocol
        if packet is not None:
            self.packet = packet
        if app is not None:
            self.app = app
        if packet_messages is not None:
            self.packet_messages = packet_messages

    @property
    def direction(self):
        """Gets the direction of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        方向，有内到外和外到内两种

        :return: The direction of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        方向，有内到外和外到内两种

        :param direction: The direction of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type direction: str
        """
        self._direction = direction

    @property
    def action(self):
        """Gets the action of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        动作

        :return: The action of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        动作

        :param action: The action of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type action: str
        """
        self._action = action

    @property
    def event_time(self):
        """Gets the event_time of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        事件时间

        :return: The event_time of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """Sets the event_time of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        事件时间

        :param event_time: The event_time of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type event_time: str
        """
        self._event_time = event_time

    @property
    def attack_type(self):
        """Gets the attack_type of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        攻击类型

        :return: The attack_type of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._attack_type

    @attack_type.setter
    def attack_type(self, attack_type):
        """Sets the attack_type of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        攻击类型

        :param attack_type: The attack_type of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type attack_type: str
        """
        self._attack_type = attack_type

    @property
    def attack_rule(self):
        """Gets the attack_rule of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        攻击规则

        :return: The attack_rule of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._attack_rule

    @attack_rule.setter
    def attack_rule(self, attack_rule):
        """Sets the attack_rule of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        攻击规则

        :param attack_rule: The attack_rule of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type attack_rule: str
        """
        self._attack_rule = attack_rule

    @property
    def level(self):
        """Gets the level of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        威胁等级

        :return: The level of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        威胁等级

        :param level: The level of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type level: str
        """
        self._level = level

    @property
    def source(self):
        """Gets the source of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        来源

        :return: The source of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        来源

        :param source: The source of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type source: str
        """
        self._source = source

    @property
    def packet_length(self):
        """Gets the packet_length of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        报文长度

        :return: The packet_length of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: int
        """
        return self._packet_length

    @packet_length.setter
    def packet_length(self, packet_length):
        """Sets the packet_length of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        报文长度

        :param packet_length: The packet_length of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type packet_length: int
        """
        self._packet_length = packet_length

    @property
    def attack_rule_id(self):
        """Gets the attack_rule_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        攻击规则id

        :return: The attack_rule_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: int
        """
        return self._attack_rule_id

    @attack_rule_id.setter
    def attack_rule_id(self, attack_rule_id):
        """Sets the attack_rule_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        攻击规则id

        :param attack_rule_id: The attack_rule_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type attack_rule_id: int
        """
        self._attack_rule_id = attack_rule_id

    @property
    def hit_time(self):
        """Gets the hit_time of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        命中时间

        :return: The hit_time of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: int
        """
        return self._hit_time

    @hit_time.setter
    def hit_time(self, hit_time):
        """Sets the hit_time of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        命中时间

        :param hit_time: The hit_time of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type hit_time: int
        """
        self._hit_time = hit_time

    @property
    def log_id(self):
        """Gets the log_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        日志ID

        :return: The log_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._log_id

    @log_id.setter
    def log_id(self, log_id):
        """Sets the log_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        日志ID

        :param log_id: The log_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type log_id: str
        """
        self._log_id = log_id

    @property
    def src_ip(self):
        """Gets the src_ip of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        源IP

        :return: The src_ip of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._src_ip

    @src_ip.setter
    def src_ip(self, src_ip):
        """Sets the src_ip of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        源IP

        :param src_ip: The src_ip of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type src_ip: str
        """
        self._src_ip = src_ip

    @property
    def src_port(self):
        """Gets the src_port of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        源端口

        :return: The src_port of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: int
        """
        return self._src_port

    @src_port.setter
    def src_port(self, src_port):
        """Sets the src_port of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        源端口

        :param src_port: The src_port of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type src_port: int
        """
        self._src_port = src_port

    @property
    def dst_ip(self):
        """Gets the dst_ip of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        目的IP

        :return: The dst_ip of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._dst_ip

    @dst_ip.setter
    def dst_ip(self, dst_ip):
        """Sets the dst_ip of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        目的IP

        :param dst_ip: The dst_ip of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type dst_ip: str
        """
        self._dst_ip = dst_ip

    @property
    def dst_port(self):
        """Gets the dst_port of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        目的端口

        :return: The dst_port of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: int
        """
        return self._dst_port

    @dst_port.setter
    def dst_port(self, dst_port):
        """Sets the dst_port of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        目的端口

        :param dst_port: The dst_port of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type dst_port: int
        """
        self._dst_port = dst_port

    @property
    def protocol(self):
        """Gets the protocol of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        协议

        :return: The protocol of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        协议

        :param protocol: The protocol of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def packet(self):
        """Gets the packet of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        :return: The packet of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: :class:`huaweicloudsdkcfw.v1.Packet`
        """
        return self._packet

    @packet.setter
    def packet(self, packet):
        """Sets the packet of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        :param packet: The packet of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type packet: :class:`huaweicloudsdkcfw.v1.Packet`
        """
        self._packet = packet

    @property
    def app(self):
        """Gets the app of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        应用协议

        :return: The app of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        应用协议

        :param app: The app of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type app: str
        """
        self._app = app

    @property
    def packet_messages(self):
        """Gets the packet_messages of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        攻击报文信息

        :return: The packet_messages of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.PacketMessage`]
        """
        return self._packet_messages

    @packet_messages.setter
    def packet_messages(self, packet_messages):
        """Sets the packet_messages of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        攻击报文信息

        :param packet_messages: The packet_messages of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type packet_messages: list[:class:`huaweicloudsdkcfw.v1.PacketMessage`]
        """
        self._packet_messages = packet_messages

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
        if not isinstance(other, HttpQueryCfwAttackLogsResponseDTODataRecords):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
