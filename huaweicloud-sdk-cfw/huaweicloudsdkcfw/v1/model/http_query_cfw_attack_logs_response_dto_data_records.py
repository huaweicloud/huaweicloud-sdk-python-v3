# coding: utf-8

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
        'event_time': 'int',
        'attack_type': 'str',
        'attack_rule': 'str',
        'level': 'str',
        'source': 'str',
        'packet_length': 'int',
        'attack_rule_id': 'str',
        'hit_time': 'int',
        'log_id': 'str',
        'src_ip': 'str',
        'src_port': 'int',
        'dst_ip': 'str',
        'dst_port': 'int',
        'protocol': 'str',
        'packet': 'str',
        'app': 'str',
        'packet_messages': 'list[PacketMessage]',
        'src_region_id': 'str',
        'src_region_name': 'str',
        'dst_region_id': 'str',
        'dst_region_name': 'str',
        'src_province_id': 'str',
        'src_province_name': 'str',
        'src_city_id': 'str',
        'src_city_name': 'str',
        'dst_province_id': 'str',
        'dst_province_name': 'str',
        'dst_city_id': 'str',
        'dst_city_name': 'str'
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
        'packet_messages': 'packetMessages',
        'src_region_id': 'src_region_id',
        'src_region_name': 'src_region_name',
        'dst_region_id': 'dst_region_id',
        'dst_region_name': 'dst_region_name',
        'src_province_id': 'src_province_id',
        'src_province_name': 'src_province_name',
        'src_city_id': 'src_city_id',
        'src_city_name': 'src_city_name',
        'dst_province_id': 'dst_province_id',
        'dst_province_name': 'dst_province_name',
        'dst_city_id': 'dst_city_id',
        'dst_city_name': 'dst_city_name'
    }

    def __init__(self, direction=None, action=None, event_time=None, attack_type=None, attack_rule=None, level=None, source=None, packet_length=None, attack_rule_id=None, hit_time=None, log_id=None, src_ip=None, src_port=None, dst_ip=None, dst_port=None, protocol=None, packet=None, app=None, packet_messages=None, src_region_id=None, src_region_name=None, dst_region_id=None, dst_region_name=None, src_province_id=None, src_province_name=None, src_city_id=None, src_city_name=None, dst_province_id=None, dst_province_name=None, dst_city_id=None, dst_city_name=None):
        r"""HttpQueryCfwAttackLogsResponseDTODataRecords

        The model defined in huaweicloud sdk

        :param direction: 方向，包含in2out，out2in
        :type direction: str
        :param action: 动作包含permit，deny
        :type action: str
        :param event_time: 事件时间，以毫秒为单位的时间戳，如1718936272648
        :type event_time: int
        :param attack_type: 攻击类型
        :type attack_type: str
        :param attack_rule: 攻击规则
        :type attack_rule: str
        :param level: 威胁等级，包括CRITICAL、HIGH、MEDIUM、LOW
        :type level: str
        :param source: 来源
        :type source: str
        :param packet_length: 报文长度
        :type packet_length: int
        :param attack_rule_id: 攻击规则id
        :type attack_rule_id: str
        :param hit_time: 命中时间，以毫秒为单位的时间戳，如1718936272648
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
        :param protocol: 协议类型，包含TCP, UDP,ICMP,ICMPV6等。
        :type protocol: str
        :param packet: 攻击日志报文
        :type packet: str
        :param app: 规则应用类型包括：“HTTP”，\&quot;HTTPS\&quot;，\&quot;TLS1\&quot;，“DNS”，“SSH”，“MYSQL”，“SMTP”，“RDP”，“RDPS”，“VNC”，“POP3”，“IMAP4”，“SMTPS”，“POP3S”，“FTPS”，“ANY”,“BGP”等。
        :type app: str
        :param packet_messages: 攻击报文信息
        :type packet_messages: list[:class:`huaweicloudsdkcfw.v1.PacketMessage`]
        :param src_region_id: 源区域id
        :type src_region_id: str
        :param src_region_name: 源区域名称
        :type src_region_name: str
        :param dst_region_id: 目的区域id
        :type dst_region_id: str
        :param dst_region_name: 目的区域名称
        :type dst_region_name: str
        :param src_province_id: 源省份id
        :type src_province_id: str
        :param src_province_name: 源省份名称
        :type src_province_name: str
        :param src_city_id: 源城市id
        :type src_city_id: str
        :param src_city_name: 源城市名称
        :type src_city_name: str
        :param dst_province_id: 目的省份id
        :type dst_province_id: str
        :param dst_province_name: 目的省份名称
        :type dst_province_name: str
        :param dst_city_id: 目的城市id
        :type dst_city_id: str
        :param dst_city_name: 目的城市名称
        :type dst_city_name: str
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
        self._src_region_id = None
        self._src_region_name = None
        self._dst_region_id = None
        self._dst_region_name = None
        self._src_province_id = None
        self._src_province_name = None
        self._src_city_id = None
        self._src_city_name = None
        self._dst_province_id = None
        self._dst_province_name = None
        self._dst_city_id = None
        self._dst_city_name = None
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
        if src_region_id is not None:
            self.src_region_id = src_region_id
        if src_region_name is not None:
            self.src_region_name = src_region_name
        if dst_region_id is not None:
            self.dst_region_id = dst_region_id
        if dst_region_name is not None:
            self.dst_region_name = dst_region_name
        if src_province_id is not None:
            self.src_province_id = src_province_id
        if src_province_name is not None:
            self.src_province_name = src_province_name
        if src_city_id is not None:
            self.src_city_id = src_city_id
        if src_city_name is not None:
            self.src_city_name = src_city_name
        if dst_province_id is not None:
            self.dst_province_id = dst_province_id
        if dst_province_name is not None:
            self.dst_province_name = dst_province_name
        if dst_city_id is not None:
            self.dst_city_id = dst_city_id
        if dst_city_name is not None:
            self.dst_city_name = dst_city_name

    @property
    def direction(self):
        r"""Gets the direction of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        方向，包含in2out，out2in

        :return: The direction of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        r"""Sets the direction of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        方向，包含in2out，out2in

        :param direction: The direction of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type direction: str
        """
        self._direction = direction

    @property
    def action(self):
        r"""Gets the action of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        动作包含permit，deny

        :return: The action of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        动作包含permit，deny

        :param action: The action of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type action: str
        """
        self._action = action

    @property
    def event_time(self):
        r"""Gets the event_time of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        事件时间，以毫秒为单位的时间戳，如1718936272648

        :return: The event_time of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: int
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        r"""Sets the event_time of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        事件时间，以毫秒为单位的时间戳，如1718936272648

        :param event_time: The event_time of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type event_time: int
        """
        self._event_time = event_time

    @property
    def attack_type(self):
        r"""Gets the attack_type of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        攻击类型

        :return: The attack_type of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._attack_type

    @attack_type.setter
    def attack_type(self, attack_type):
        r"""Sets the attack_type of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        攻击类型

        :param attack_type: The attack_type of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type attack_type: str
        """
        self._attack_type = attack_type

    @property
    def attack_rule(self):
        r"""Gets the attack_rule of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        攻击规则

        :return: The attack_rule of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._attack_rule

    @attack_rule.setter
    def attack_rule(self, attack_rule):
        r"""Sets the attack_rule of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        攻击规则

        :param attack_rule: The attack_rule of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type attack_rule: str
        """
        self._attack_rule = attack_rule

    @property
    def level(self):
        r"""Gets the level of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        威胁等级，包括CRITICAL、HIGH、MEDIUM、LOW

        :return: The level of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        威胁等级，包括CRITICAL、HIGH、MEDIUM、LOW

        :param level: The level of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type level: str
        """
        self._level = level

    @property
    def source(self):
        r"""Gets the source of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        来源

        :return: The source of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        来源

        :param source: The source of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type source: str
        """
        self._source = source

    @property
    def packet_length(self):
        r"""Gets the packet_length of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        报文长度

        :return: The packet_length of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: int
        """
        return self._packet_length

    @packet_length.setter
    def packet_length(self, packet_length):
        r"""Sets the packet_length of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        报文长度

        :param packet_length: The packet_length of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type packet_length: int
        """
        self._packet_length = packet_length

    @property
    def attack_rule_id(self):
        r"""Gets the attack_rule_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        攻击规则id

        :return: The attack_rule_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._attack_rule_id

    @attack_rule_id.setter
    def attack_rule_id(self, attack_rule_id):
        r"""Sets the attack_rule_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        攻击规则id

        :param attack_rule_id: The attack_rule_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type attack_rule_id: str
        """
        self._attack_rule_id = attack_rule_id

    @property
    def hit_time(self):
        r"""Gets the hit_time of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        命中时间，以毫秒为单位的时间戳，如1718936272648

        :return: The hit_time of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: int
        """
        return self._hit_time

    @hit_time.setter
    def hit_time(self, hit_time):
        r"""Sets the hit_time of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        命中时间，以毫秒为单位的时间戳，如1718936272648

        :param hit_time: The hit_time of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type hit_time: int
        """
        self._hit_time = hit_time

    @property
    def log_id(self):
        r"""Gets the log_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        日志ID

        :return: The log_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._log_id

    @log_id.setter
    def log_id(self, log_id):
        r"""Sets the log_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        日志ID

        :param log_id: The log_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type log_id: str
        """
        self._log_id = log_id

    @property
    def src_ip(self):
        r"""Gets the src_ip of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        源IP

        :return: The src_ip of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._src_ip

    @src_ip.setter
    def src_ip(self, src_ip):
        r"""Sets the src_ip of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        源IP

        :param src_ip: The src_ip of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type src_ip: str
        """
        self._src_ip = src_ip

    @property
    def src_port(self):
        r"""Gets the src_port of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        源端口

        :return: The src_port of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: int
        """
        return self._src_port

    @src_port.setter
    def src_port(self, src_port):
        r"""Sets the src_port of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        源端口

        :param src_port: The src_port of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type src_port: int
        """
        self._src_port = src_port

    @property
    def dst_ip(self):
        r"""Gets the dst_ip of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        目的IP

        :return: The dst_ip of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._dst_ip

    @dst_ip.setter
    def dst_ip(self, dst_ip):
        r"""Sets the dst_ip of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        目的IP

        :param dst_ip: The dst_ip of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type dst_ip: str
        """
        self._dst_ip = dst_ip

    @property
    def dst_port(self):
        r"""Gets the dst_port of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        目的端口

        :return: The dst_port of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: int
        """
        return self._dst_port

    @dst_port.setter
    def dst_port(self, dst_port):
        r"""Sets the dst_port of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        目的端口

        :param dst_port: The dst_port of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type dst_port: int
        """
        self._dst_port = dst_port

    @property
    def protocol(self):
        r"""Gets the protocol of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        协议类型，包含TCP, UDP,ICMP,ICMPV6等。

        :return: The protocol of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        协议类型，包含TCP, UDP,ICMP,ICMPV6等。

        :param protocol: The protocol of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def packet(self):
        r"""Gets the packet of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        攻击日志报文

        :return: The packet of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._packet

    @packet.setter
    def packet(self, packet):
        r"""Sets the packet of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        攻击日志报文

        :param packet: The packet of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type packet: str
        """
        self._packet = packet

    @property
    def app(self):
        r"""Gets the app of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        规则应用类型包括：“HTTP”，\"HTTPS\"，\"TLS1\"，“DNS”，“SSH”，“MYSQL”，“SMTP”，“RDP”，“RDPS”，“VNC”，“POP3”，“IMAP4”，“SMTPS”，“POP3S”，“FTPS”，“ANY”,“BGP”等。

        :return: The app of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        规则应用类型包括：“HTTP”，\"HTTPS\"，\"TLS1\"，“DNS”，“SSH”，“MYSQL”，“SMTP”，“RDP”，“RDPS”，“VNC”，“POP3”，“IMAP4”，“SMTPS”，“POP3S”，“FTPS”，“ANY”,“BGP”等。

        :param app: The app of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type app: str
        """
        self._app = app

    @property
    def packet_messages(self):
        r"""Gets the packet_messages of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        攻击报文信息

        :return: The packet_messages of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.PacketMessage`]
        """
        return self._packet_messages

    @packet_messages.setter
    def packet_messages(self, packet_messages):
        r"""Sets the packet_messages of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        攻击报文信息

        :param packet_messages: The packet_messages of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type packet_messages: list[:class:`huaweicloudsdkcfw.v1.PacketMessage`]
        """
        self._packet_messages = packet_messages

    @property
    def src_region_id(self):
        r"""Gets the src_region_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        源区域id

        :return: The src_region_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._src_region_id

    @src_region_id.setter
    def src_region_id(self, src_region_id):
        r"""Sets the src_region_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        源区域id

        :param src_region_id: The src_region_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type src_region_id: str
        """
        self._src_region_id = src_region_id

    @property
    def src_region_name(self):
        r"""Gets the src_region_name of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        源区域名称

        :return: The src_region_name of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._src_region_name

    @src_region_name.setter
    def src_region_name(self, src_region_name):
        r"""Sets the src_region_name of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        源区域名称

        :param src_region_name: The src_region_name of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type src_region_name: str
        """
        self._src_region_name = src_region_name

    @property
    def dst_region_id(self):
        r"""Gets the dst_region_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        目的区域id

        :return: The dst_region_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._dst_region_id

    @dst_region_id.setter
    def dst_region_id(self, dst_region_id):
        r"""Sets the dst_region_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        目的区域id

        :param dst_region_id: The dst_region_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type dst_region_id: str
        """
        self._dst_region_id = dst_region_id

    @property
    def dst_region_name(self):
        r"""Gets the dst_region_name of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        目的区域名称

        :return: The dst_region_name of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._dst_region_name

    @dst_region_name.setter
    def dst_region_name(self, dst_region_name):
        r"""Sets the dst_region_name of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        目的区域名称

        :param dst_region_name: The dst_region_name of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type dst_region_name: str
        """
        self._dst_region_name = dst_region_name

    @property
    def src_province_id(self):
        r"""Gets the src_province_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        源省份id

        :return: The src_province_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._src_province_id

    @src_province_id.setter
    def src_province_id(self, src_province_id):
        r"""Sets the src_province_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        源省份id

        :param src_province_id: The src_province_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type src_province_id: str
        """
        self._src_province_id = src_province_id

    @property
    def src_province_name(self):
        r"""Gets the src_province_name of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        源省份名称

        :return: The src_province_name of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._src_province_name

    @src_province_name.setter
    def src_province_name(self, src_province_name):
        r"""Sets the src_province_name of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        源省份名称

        :param src_province_name: The src_province_name of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type src_province_name: str
        """
        self._src_province_name = src_province_name

    @property
    def src_city_id(self):
        r"""Gets the src_city_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        源城市id

        :return: The src_city_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._src_city_id

    @src_city_id.setter
    def src_city_id(self, src_city_id):
        r"""Sets the src_city_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        源城市id

        :param src_city_id: The src_city_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type src_city_id: str
        """
        self._src_city_id = src_city_id

    @property
    def src_city_name(self):
        r"""Gets the src_city_name of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        源城市名称

        :return: The src_city_name of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._src_city_name

    @src_city_name.setter
    def src_city_name(self, src_city_name):
        r"""Sets the src_city_name of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        源城市名称

        :param src_city_name: The src_city_name of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type src_city_name: str
        """
        self._src_city_name = src_city_name

    @property
    def dst_province_id(self):
        r"""Gets the dst_province_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        目的省份id

        :return: The dst_province_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._dst_province_id

    @dst_province_id.setter
    def dst_province_id(self, dst_province_id):
        r"""Sets the dst_province_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        目的省份id

        :param dst_province_id: The dst_province_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type dst_province_id: str
        """
        self._dst_province_id = dst_province_id

    @property
    def dst_province_name(self):
        r"""Gets the dst_province_name of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        目的省份名称

        :return: The dst_province_name of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._dst_province_name

    @dst_province_name.setter
    def dst_province_name(self, dst_province_name):
        r"""Sets the dst_province_name of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        目的省份名称

        :param dst_province_name: The dst_province_name of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type dst_province_name: str
        """
        self._dst_province_name = dst_province_name

    @property
    def dst_city_id(self):
        r"""Gets the dst_city_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        目的城市id

        :return: The dst_city_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._dst_city_id

    @dst_city_id.setter
    def dst_city_id(self, dst_city_id):
        r"""Sets the dst_city_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        目的城市id

        :param dst_city_id: The dst_city_id of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type dst_city_id: str
        """
        self._dst_city_id = dst_city_id

    @property
    def dst_city_name(self):
        r"""Gets the dst_city_name of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        目的城市名称

        :return: The dst_city_name of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._dst_city_name

    @dst_city_name.setter
    def dst_city_name(self, dst_city_name):
        r"""Sets the dst_city_name of this HttpQueryCfwAttackLogsResponseDTODataRecords.

        目的城市名称

        :param dst_city_name: The dst_city_name of this HttpQueryCfwAttackLogsResponseDTODataRecords.
        :type dst_city_name: str
        """
        self._dst_city_name = dst_city_name

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
