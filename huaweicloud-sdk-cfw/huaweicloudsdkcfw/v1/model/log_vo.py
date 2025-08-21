# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app': 'str',
        'bytes': 'float',
        'direction': 'str',
        'dst_host': 'str',
        'dst_ip': 'str',
        'dst_port': 'int',
        'end_time': 'int',
        'log_id': 'str',
        'packets': 'float',
        'protocol': 'str',
        'src_ip': 'str',
        'src_port': 'int',
        'start_time': 'int',
        'dst_region_id': 'object',
        'dst_region_name': 'str',
        'dst_province_id': 'str',
        'dst_province_name': 'str',
        'dst_city_id': 'str',
        'dst_city_name': 'str',
        'src_region_id': 'str',
        'src_region_name': 'str',
        'src_province_id': 'str',
        'src_province_name': 'str',
        'src_city_id': 'str',
        'src_city_name': 'str',
        'vgw_id': 'str',
        'sctp_verification_tag': 'int',
        'sctp_is_handshake_flow': 'str',
        'qos_rule_id': 'str',
        'qos_rule_name': 'str',
        'qos_channel_id': 'str',
        'qos_channel_name': 'str',
        'qos_drop_packets': 'float',
        'qos_drop_bytes': 'float',
        'qos_rule_type': 'int',
        'qos_channel_type': 'int',
        'action': 'str',
        'url': 'str',
        'hit_time': 'int',
        'rule_id': 'str',
        'rule_name': 'str',
        'rule_type': 'int',
        'attack_rule': 'str',
        'attack_rule_id': 'str',
        'attack_type': 'str',
        'event_time': 'int',
        'level': 'str',
        'packet': 'str',
        'source': 'str',
        'real_ip': 'str',
        'tag': 'int'
    }

    attribute_map = {
        'app': 'app',
        'bytes': 'bytes',
        'direction': 'direction',
        'dst_host': 'dst_host',
        'dst_ip': 'dst_ip',
        'dst_port': 'dst_port',
        'end_time': 'end_time',
        'log_id': 'log_id',
        'packets': 'packets',
        'protocol': 'protocol',
        'src_ip': 'src_ip',
        'src_port': 'src_port',
        'start_time': 'start_time',
        'dst_region_id': 'dst_region_id',
        'dst_region_name': 'dst_region_name',
        'dst_province_id': 'dst_province_id',
        'dst_province_name': 'dst_province_name',
        'dst_city_id': 'dst_city_id',
        'dst_city_name': 'dst_city_name',
        'src_region_id': 'src_region_id',
        'src_region_name': 'src_region_name',
        'src_province_id': 'src_province_id',
        'src_province_name': 'src_province_name',
        'src_city_id': 'src_city_id',
        'src_city_name': 'src_city_name',
        'vgw_id': 'vgw_id',
        'sctp_verification_tag': 'sctp_verification_tag',
        'sctp_is_handshake_flow': 'sctp_is_handshake_flow',
        'qos_rule_id': 'qos_rule_id',
        'qos_rule_name': 'qos_rule_name',
        'qos_channel_id': 'qos_channel_id',
        'qos_channel_name': 'qos_channel_name',
        'qos_drop_packets': 'qos_drop_packets',
        'qos_drop_bytes': 'qos_drop_bytes',
        'qos_rule_type': 'qos_rule_type',
        'qos_channel_type': 'qos_channel_type',
        'action': 'action',
        'url': 'url',
        'hit_time': 'hit_time',
        'rule_id': 'rule_id',
        'rule_name': 'rule_name',
        'rule_type': 'rule_type',
        'attack_rule': 'attack_rule',
        'attack_rule_id': 'attack_rule_id',
        'attack_type': 'attack_type',
        'event_time': 'event_time',
        'level': 'level',
        'packet': 'packet',
        'source': 'source',
        'real_ip': 'real_ip',
        'tag': 'tag'
    }

    def __init__(self, app=None, bytes=None, direction=None, dst_host=None, dst_ip=None, dst_port=None, end_time=None, log_id=None, packets=None, protocol=None, src_ip=None, src_port=None, start_time=None, dst_region_id=None, dst_region_name=None, dst_province_id=None, dst_province_name=None, dst_city_id=None, dst_city_name=None, src_region_id=None, src_region_name=None, src_province_id=None, src_province_name=None, src_city_id=None, src_city_name=None, vgw_id=None, sctp_verification_tag=None, sctp_is_handshake_flow=None, qos_rule_id=None, qos_rule_name=None, qos_channel_id=None, qos_channel_name=None, qos_drop_packets=None, qos_drop_bytes=None, qos_rule_type=None, qos_channel_type=None, action=None, url=None, hit_time=None, rule_id=None, rule_name=None, rule_type=None, attack_rule=None, attack_rule_id=None, attack_type=None, event_time=None, level=None, packet=None, source=None, real_ip=None, tag=None):
        r"""LogVO

        The model defined in huaweicloud sdk

        :param app: **参数解释**： 应用 **取值范围**： 不涉及
        :type app: str
        :param bytes: **参数解释**： 流字节数，流量日志字段 **取值范围**： 不涉及
        :type bytes: float
        :param direction: **参数解释**： 会话方向 **取值范围**： out2in 外到内访问 in2out 内到外访问
        :type direction: str
        :param dst_host: **参数解释**： 流字节数，访问控制日志和流量日志中存在 **取值范围**： 目的网址
        :type dst_host: str
        :param dst_ip: **参数解释**： 目的IP **取值范围**： 不涉及
        :type dst_ip: str
        :param dst_port: **参数解释**： 目的端口 **取值范围**： 不涉及
        :type dst_port: int
        :param end_time: **参数解释**： 会话结束时间，流量日志字段 **取值范围**： 不涉及
        :type end_time: int
        :param log_id: **参数解释**： 日志ID，用于分页查询 **取值范围**： 不涉及
        :type log_id: str
        :param packets: **参数解释**： 流包数，流量日志字段 **取值范围**： 不涉及
        :type packets: float
        :param protocol: **参数解释**： 协议 **取值范围**： 不涉及
        :type protocol: str
        :param src_ip: **参数解释**： 源Ip **取值范围**： 不涉及
        :type src_ip: str
        :param src_port: **参数解释**： 源端口 **取值范围**： 不涉及
        :type src_port: int
        :param start_time: **参数解释**： 会话开始时间，流量日志字段 **取值范围**： 不涉及
        :type start_time: int
        :param dst_region_id: **参数解释**： 目的地区ID **取值范围**： 不涉及
        :type dst_region_id: object
        :param dst_region_name: **参数解释**： 目的地区名称 **取值范围**： 不涉及
        :type dst_region_name: str
        :param dst_province_id: **参数解释**： 目的省份ID **取值范围**： 不涉及
        :type dst_province_id: str
        :param dst_province_name: **参数解释**： 目的省份名称 **取值范围**： 不涉及
        :type dst_province_name: str
        :param dst_city_id: **参数解释**： 目的城市ID **取值范围**： 不涉及
        :type dst_city_id: str
        :param dst_city_name: **参数解释**： 目的城市名称 **取值范围**： 不涉及
        :type dst_city_name: str
        :param src_region_id: **参数解释**： 源地区ID **取值范围**： 不涉及
        :type src_region_id: str
        :param src_region_name: **参数解释**： 源地区名称 **取值范围**： 不涉及
        :type src_region_name: str
        :param src_province_id: **参数解释**： 源省份ID **取值范围**： 不涉及
        :type src_province_id: str
        :param src_province_name: **参数解释**： 源省份名称 **取值范围**： 不涉及
        :type src_province_name: str
        :param src_city_id: **参数解释**： 源城市ID **取值范围**： 不涉及
        :type src_city_id: str
        :param src_city_name: **参数解释**： 源城市名称 **取值范围**： 不涉及
        :type src_city_name: str
        :param vgw_id: **参数解释**： 虚拟网关ID **取值范围**： 不涉及
        :type vgw_id: str
        :param sctp_verification_tag: **参数解释**： sctp验证标签，流量日志字段 **取值范围**： 不涉及
        :type sctp_verification_tag: int
        :param sctp_is_handshake_flow: **参数解释**： sctp握手流，流量日志字段 **取值范围**： 不涉及
        :type sctp_is_handshake_flow: str
        :param qos_rule_id: **参数解释**： qos规则ID，流量日志、访问控制日志存在 **取值范围**： 不涉及
        :type qos_rule_id: str
        :param qos_rule_name: **参数解释**： qos规则名称，流量日志、访问控制日志存在 **取值范围**： 不涉及
        :type qos_rule_name: str
        :param qos_channel_id: **参数解释**： qos通道ID，流量日志字段 **取值范围**： 不涉及
        :type qos_channel_id: str
        :param qos_channel_name: **参数解释**： qos通道名称，流量日志字段 **取值范围**： 不涉及
        :type qos_channel_name: str
        :param qos_drop_packets: **参数解释**： qos丢包数，流量日志字段 **取值范围**： 不涉及
        :type qos_drop_packets: float
        :param qos_drop_bytes: **参数解释**： qos丢弃字节，流量日志字段 **取值范围**： 不涉及
        :type qos_drop_bytes: float
        :param qos_rule_type: **参数解释**： qos规则类型，流量日志、访问控制日志存在 **取值范围**： 不涉及
        :type qos_rule_type: int
        :param qos_channel_type: **参数解释**： qos通道类型，流量日志字段 **取值范围**： 不涉及
        :type qos_channel_type: int
        :param action: **参数解释**： 动作，攻击日志、访问控制日志、URL日志存在 **取值范围**： 不涉及
        :type action: str
        :param url: **参数解释**： url，URL日志字段 **取值范围**： 不涉及
        :type url: str
        :param hit_time: **参数解释**： 命中时间，访问控制日志、URL日志存在 **取值范围**： 不涉及
        :type hit_time: int
        :param rule_id: **参数解释**： 规则ID，访问控制日志、URL日志存在 **取值范围**： 不涉及
        :type rule_id: str
        :param rule_name: **参数解释**： 规则名称，访问控制日志、URL日志存在 **取值范围**： 不涉及
        :type rule_name: str
        :param rule_type: **参数解释**： 规则类型，访问控制日志和URL日志字段 **取值范围**： 不涉及
        :type rule_type: int
        :param attack_rule: **参数解释**： 规则类型，攻击日志字段 **取值范围**： 不涉及
        :type attack_rule: str
        :param attack_rule_id: **参数解释**： 攻击规则ID，攻击日志字段 **取值范围**： 不涉及
        :type attack_rule_id: str
        :param attack_type: **参数解释**： 攻击类型，攻击日志字段 **取值范围**： 不涉及
        :type attack_type: str
        :param event_time: **参数解释**： 事件时间，攻击日志字段 **取值范围**： 不涉及
        :type event_time: int
        :param level: **参数解释**： 攻击等级，攻击日志字段 **取值范围**： 不涉及
        :type level: str
        :param packet: **参数解释**： 规则载荷，攻击日志字段 **取值范围**： 不涉及
        :type packet: str
        :param source: **参数解释**： 攻击来源，攻击日志字段 **取值范围**： 不涉及
        :type source: str
        :param real_ip: **参数解释**： 真实IP，攻击日志字段 **取值范围**： 不涉及
        :type real_ip: str
        :param tag: **参数解释**： 标签类型，攻击日志字段 **取值范围**： 1 WAF回源IP
        :type tag: int
        """
        
        

        self._app = None
        self._bytes = None
        self._direction = None
        self._dst_host = None
        self._dst_ip = None
        self._dst_port = None
        self._end_time = None
        self._log_id = None
        self._packets = None
        self._protocol = None
        self._src_ip = None
        self._src_port = None
        self._start_time = None
        self._dst_region_id = None
        self._dst_region_name = None
        self._dst_province_id = None
        self._dst_province_name = None
        self._dst_city_id = None
        self._dst_city_name = None
        self._src_region_id = None
        self._src_region_name = None
        self._src_province_id = None
        self._src_province_name = None
        self._src_city_id = None
        self._src_city_name = None
        self._vgw_id = None
        self._sctp_verification_tag = None
        self._sctp_is_handshake_flow = None
        self._qos_rule_id = None
        self._qos_rule_name = None
        self._qos_channel_id = None
        self._qos_channel_name = None
        self._qos_drop_packets = None
        self._qos_drop_bytes = None
        self._qos_rule_type = None
        self._qos_channel_type = None
        self._action = None
        self._url = None
        self._hit_time = None
        self._rule_id = None
        self._rule_name = None
        self._rule_type = None
        self._attack_rule = None
        self._attack_rule_id = None
        self._attack_type = None
        self._event_time = None
        self._level = None
        self._packet = None
        self._source = None
        self._real_ip = None
        self._tag = None
        self.discriminator = None

        if app is not None:
            self.app = app
        if bytes is not None:
            self.bytes = bytes
        if direction is not None:
            self.direction = direction
        if dst_host is not None:
            self.dst_host = dst_host
        if dst_ip is not None:
            self.dst_ip = dst_ip
        if dst_port is not None:
            self.dst_port = dst_port
        if end_time is not None:
            self.end_time = end_time
        if log_id is not None:
            self.log_id = log_id
        if packets is not None:
            self.packets = packets
        if protocol is not None:
            self.protocol = protocol
        if src_ip is not None:
            self.src_ip = src_ip
        if src_port is not None:
            self.src_port = src_port
        if start_time is not None:
            self.start_time = start_time
        if dst_region_id is not None:
            self.dst_region_id = dst_region_id
        if dst_region_name is not None:
            self.dst_region_name = dst_region_name
        if dst_province_id is not None:
            self.dst_province_id = dst_province_id
        if dst_province_name is not None:
            self.dst_province_name = dst_province_name
        if dst_city_id is not None:
            self.dst_city_id = dst_city_id
        if dst_city_name is not None:
            self.dst_city_name = dst_city_name
        if src_region_id is not None:
            self.src_region_id = src_region_id
        if src_region_name is not None:
            self.src_region_name = src_region_name
        if src_province_id is not None:
            self.src_province_id = src_province_id
        if src_province_name is not None:
            self.src_province_name = src_province_name
        if src_city_id is not None:
            self.src_city_id = src_city_id
        if src_city_name is not None:
            self.src_city_name = src_city_name
        if vgw_id is not None:
            self.vgw_id = vgw_id
        if sctp_verification_tag is not None:
            self.sctp_verification_tag = sctp_verification_tag
        if sctp_is_handshake_flow is not None:
            self.sctp_is_handshake_flow = sctp_is_handshake_flow
        if qos_rule_id is not None:
            self.qos_rule_id = qos_rule_id
        if qos_rule_name is not None:
            self.qos_rule_name = qos_rule_name
        if qos_channel_id is not None:
            self.qos_channel_id = qos_channel_id
        if qos_channel_name is not None:
            self.qos_channel_name = qos_channel_name
        if qos_drop_packets is not None:
            self.qos_drop_packets = qos_drop_packets
        if qos_drop_bytes is not None:
            self.qos_drop_bytes = qos_drop_bytes
        if qos_rule_type is not None:
            self.qos_rule_type = qos_rule_type
        if qos_channel_type is not None:
            self.qos_channel_type = qos_channel_type
        if action is not None:
            self.action = action
        if url is not None:
            self.url = url
        if hit_time is not None:
            self.hit_time = hit_time
        if rule_id is not None:
            self.rule_id = rule_id
        if rule_name is not None:
            self.rule_name = rule_name
        if rule_type is not None:
            self.rule_type = rule_type
        if attack_rule is not None:
            self.attack_rule = attack_rule
        if attack_rule_id is not None:
            self.attack_rule_id = attack_rule_id
        if attack_type is not None:
            self.attack_type = attack_type
        if event_time is not None:
            self.event_time = event_time
        if level is not None:
            self.level = level
        if packet is not None:
            self.packet = packet
        if source is not None:
            self.source = source
        if real_ip is not None:
            self.real_ip = real_ip
        if tag is not None:
            self.tag = tag

    @property
    def app(self):
        r"""Gets the app of this LogVO.

        **参数解释**： 应用 **取值范围**： 不涉及

        :return: The app of this LogVO.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this LogVO.

        **参数解释**： 应用 **取值范围**： 不涉及

        :param app: The app of this LogVO.
        :type app: str
        """
        self._app = app

    @property
    def bytes(self):
        r"""Gets the bytes of this LogVO.

        **参数解释**： 流字节数，流量日志字段 **取值范围**： 不涉及

        :return: The bytes of this LogVO.
        :rtype: float
        """
        return self._bytes

    @bytes.setter
    def bytes(self, bytes):
        r"""Sets the bytes of this LogVO.

        **参数解释**： 流字节数，流量日志字段 **取值范围**： 不涉及

        :param bytes: The bytes of this LogVO.
        :type bytes: float
        """
        self._bytes = bytes

    @property
    def direction(self):
        r"""Gets the direction of this LogVO.

        **参数解释**： 会话方向 **取值范围**： out2in 外到内访问 in2out 内到外访问

        :return: The direction of this LogVO.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        r"""Sets the direction of this LogVO.

        **参数解释**： 会话方向 **取值范围**： out2in 外到内访问 in2out 内到外访问

        :param direction: The direction of this LogVO.
        :type direction: str
        """
        self._direction = direction

    @property
    def dst_host(self):
        r"""Gets the dst_host of this LogVO.

        **参数解释**： 流字节数，访问控制日志和流量日志中存在 **取值范围**： 目的网址

        :return: The dst_host of this LogVO.
        :rtype: str
        """
        return self._dst_host

    @dst_host.setter
    def dst_host(self, dst_host):
        r"""Sets the dst_host of this LogVO.

        **参数解释**： 流字节数，访问控制日志和流量日志中存在 **取值范围**： 目的网址

        :param dst_host: The dst_host of this LogVO.
        :type dst_host: str
        """
        self._dst_host = dst_host

    @property
    def dst_ip(self):
        r"""Gets the dst_ip of this LogVO.

        **参数解释**： 目的IP **取值范围**： 不涉及

        :return: The dst_ip of this LogVO.
        :rtype: str
        """
        return self._dst_ip

    @dst_ip.setter
    def dst_ip(self, dst_ip):
        r"""Sets the dst_ip of this LogVO.

        **参数解释**： 目的IP **取值范围**： 不涉及

        :param dst_ip: The dst_ip of this LogVO.
        :type dst_ip: str
        """
        self._dst_ip = dst_ip

    @property
    def dst_port(self):
        r"""Gets the dst_port of this LogVO.

        **参数解释**： 目的端口 **取值范围**： 不涉及

        :return: The dst_port of this LogVO.
        :rtype: int
        """
        return self._dst_port

    @dst_port.setter
    def dst_port(self, dst_port):
        r"""Sets the dst_port of this LogVO.

        **参数解释**： 目的端口 **取值范围**： 不涉及

        :param dst_port: The dst_port of this LogVO.
        :type dst_port: int
        """
        self._dst_port = dst_port

    @property
    def end_time(self):
        r"""Gets the end_time of this LogVO.

        **参数解释**： 会话结束时间，流量日志字段 **取值范围**： 不涉及

        :return: The end_time of this LogVO.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this LogVO.

        **参数解释**： 会话结束时间，流量日志字段 **取值范围**： 不涉及

        :param end_time: The end_time of this LogVO.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def log_id(self):
        r"""Gets the log_id of this LogVO.

        **参数解释**： 日志ID，用于分页查询 **取值范围**： 不涉及

        :return: The log_id of this LogVO.
        :rtype: str
        """
        return self._log_id

    @log_id.setter
    def log_id(self, log_id):
        r"""Sets the log_id of this LogVO.

        **参数解释**： 日志ID，用于分页查询 **取值范围**： 不涉及

        :param log_id: The log_id of this LogVO.
        :type log_id: str
        """
        self._log_id = log_id

    @property
    def packets(self):
        r"""Gets the packets of this LogVO.

        **参数解释**： 流包数，流量日志字段 **取值范围**： 不涉及

        :return: The packets of this LogVO.
        :rtype: float
        """
        return self._packets

    @packets.setter
    def packets(self, packets):
        r"""Sets the packets of this LogVO.

        **参数解释**： 流包数，流量日志字段 **取值范围**： 不涉及

        :param packets: The packets of this LogVO.
        :type packets: float
        """
        self._packets = packets

    @property
    def protocol(self):
        r"""Gets the protocol of this LogVO.

        **参数解释**： 协议 **取值范围**： 不涉及

        :return: The protocol of this LogVO.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this LogVO.

        **参数解释**： 协议 **取值范围**： 不涉及

        :param protocol: The protocol of this LogVO.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def src_ip(self):
        r"""Gets the src_ip of this LogVO.

        **参数解释**： 源Ip **取值范围**： 不涉及

        :return: The src_ip of this LogVO.
        :rtype: str
        """
        return self._src_ip

    @src_ip.setter
    def src_ip(self, src_ip):
        r"""Sets the src_ip of this LogVO.

        **参数解释**： 源Ip **取值范围**： 不涉及

        :param src_ip: The src_ip of this LogVO.
        :type src_ip: str
        """
        self._src_ip = src_ip

    @property
    def src_port(self):
        r"""Gets the src_port of this LogVO.

        **参数解释**： 源端口 **取值范围**： 不涉及

        :return: The src_port of this LogVO.
        :rtype: int
        """
        return self._src_port

    @src_port.setter
    def src_port(self, src_port):
        r"""Sets the src_port of this LogVO.

        **参数解释**： 源端口 **取值范围**： 不涉及

        :param src_port: The src_port of this LogVO.
        :type src_port: int
        """
        self._src_port = src_port

    @property
    def start_time(self):
        r"""Gets the start_time of this LogVO.

        **参数解释**： 会话开始时间，流量日志字段 **取值范围**： 不涉及

        :return: The start_time of this LogVO.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this LogVO.

        **参数解释**： 会话开始时间，流量日志字段 **取值范围**： 不涉及

        :param start_time: The start_time of this LogVO.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def dst_region_id(self):
        r"""Gets the dst_region_id of this LogVO.

        **参数解释**： 目的地区ID **取值范围**： 不涉及

        :return: The dst_region_id of this LogVO.
        :rtype: object
        """
        return self._dst_region_id

    @dst_region_id.setter
    def dst_region_id(self, dst_region_id):
        r"""Sets the dst_region_id of this LogVO.

        **参数解释**： 目的地区ID **取值范围**： 不涉及

        :param dst_region_id: The dst_region_id of this LogVO.
        :type dst_region_id: object
        """
        self._dst_region_id = dst_region_id

    @property
    def dst_region_name(self):
        r"""Gets the dst_region_name of this LogVO.

        **参数解释**： 目的地区名称 **取值范围**： 不涉及

        :return: The dst_region_name of this LogVO.
        :rtype: str
        """
        return self._dst_region_name

    @dst_region_name.setter
    def dst_region_name(self, dst_region_name):
        r"""Sets the dst_region_name of this LogVO.

        **参数解释**： 目的地区名称 **取值范围**： 不涉及

        :param dst_region_name: The dst_region_name of this LogVO.
        :type dst_region_name: str
        """
        self._dst_region_name = dst_region_name

    @property
    def dst_province_id(self):
        r"""Gets the dst_province_id of this LogVO.

        **参数解释**： 目的省份ID **取值范围**： 不涉及

        :return: The dst_province_id of this LogVO.
        :rtype: str
        """
        return self._dst_province_id

    @dst_province_id.setter
    def dst_province_id(self, dst_province_id):
        r"""Sets the dst_province_id of this LogVO.

        **参数解释**： 目的省份ID **取值范围**： 不涉及

        :param dst_province_id: The dst_province_id of this LogVO.
        :type dst_province_id: str
        """
        self._dst_province_id = dst_province_id

    @property
    def dst_province_name(self):
        r"""Gets the dst_province_name of this LogVO.

        **参数解释**： 目的省份名称 **取值范围**： 不涉及

        :return: The dst_province_name of this LogVO.
        :rtype: str
        """
        return self._dst_province_name

    @dst_province_name.setter
    def dst_province_name(self, dst_province_name):
        r"""Sets the dst_province_name of this LogVO.

        **参数解释**： 目的省份名称 **取值范围**： 不涉及

        :param dst_province_name: The dst_province_name of this LogVO.
        :type dst_province_name: str
        """
        self._dst_province_name = dst_province_name

    @property
    def dst_city_id(self):
        r"""Gets the dst_city_id of this LogVO.

        **参数解释**： 目的城市ID **取值范围**： 不涉及

        :return: The dst_city_id of this LogVO.
        :rtype: str
        """
        return self._dst_city_id

    @dst_city_id.setter
    def dst_city_id(self, dst_city_id):
        r"""Sets the dst_city_id of this LogVO.

        **参数解释**： 目的城市ID **取值范围**： 不涉及

        :param dst_city_id: The dst_city_id of this LogVO.
        :type dst_city_id: str
        """
        self._dst_city_id = dst_city_id

    @property
    def dst_city_name(self):
        r"""Gets the dst_city_name of this LogVO.

        **参数解释**： 目的城市名称 **取值范围**： 不涉及

        :return: The dst_city_name of this LogVO.
        :rtype: str
        """
        return self._dst_city_name

    @dst_city_name.setter
    def dst_city_name(self, dst_city_name):
        r"""Sets the dst_city_name of this LogVO.

        **参数解释**： 目的城市名称 **取值范围**： 不涉及

        :param dst_city_name: The dst_city_name of this LogVO.
        :type dst_city_name: str
        """
        self._dst_city_name = dst_city_name

    @property
    def src_region_id(self):
        r"""Gets the src_region_id of this LogVO.

        **参数解释**： 源地区ID **取值范围**： 不涉及

        :return: The src_region_id of this LogVO.
        :rtype: str
        """
        return self._src_region_id

    @src_region_id.setter
    def src_region_id(self, src_region_id):
        r"""Sets the src_region_id of this LogVO.

        **参数解释**： 源地区ID **取值范围**： 不涉及

        :param src_region_id: The src_region_id of this LogVO.
        :type src_region_id: str
        """
        self._src_region_id = src_region_id

    @property
    def src_region_name(self):
        r"""Gets the src_region_name of this LogVO.

        **参数解释**： 源地区名称 **取值范围**： 不涉及

        :return: The src_region_name of this LogVO.
        :rtype: str
        """
        return self._src_region_name

    @src_region_name.setter
    def src_region_name(self, src_region_name):
        r"""Sets the src_region_name of this LogVO.

        **参数解释**： 源地区名称 **取值范围**： 不涉及

        :param src_region_name: The src_region_name of this LogVO.
        :type src_region_name: str
        """
        self._src_region_name = src_region_name

    @property
    def src_province_id(self):
        r"""Gets the src_province_id of this LogVO.

        **参数解释**： 源省份ID **取值范围**： 不涉及

        :return: The src_province_id of this LogVO.
        :rtype: str
        """
        return self._src_province_id

    @src_province_id.setter
    def src_province_id(self, src_province_id):
        r"""Sets the src_province_id of this LogVO.

        **参数解释**： 源省份ID **取值范围**： 不涉及

        :param src_province_id: The src_province_id of this LogVO.
        :type src_province_id: str
        """
        self._src_province_id = src_province_id

    @property
    def src_province_name(self):
        r"""Gets the src_province_name of this LogVO.

        **参数解释**： 源省份名称 **取值范围**： 不涉及

        :return: The src_province_name of this LogVO.
        :rtype: str
        """
        return self._src_province_name

    @src_province_name.setter
    def src_province_name(self, src_province_name):
        r"""Sets the src_province_name of this LogVO.

        **参数解释**： 源省份名称 **取值范围**： 不涉及

        :param src_province_name: The src_province_name of this LogVO.
        :type src_province_name: str
        """
        self._src_province_name = src_province_name

    @property
    def src_city_id(self):
        r"""Gets the src_city_id of this LogVO.

        **参数解释**： 源城市ID **取值范围**： 不涉及

        :return: The src_city_id of this LogVO.
        :rtype: str
        """
        return self._src_city_id

    @src_city_id.setter
    def src_city_id(self, src_city_id):
        r"""Sets the src_city_id of this LogVO.

        **参数解释**： 源城市ID **取值范围**： 不涉及

        :param src_city_id: The src_city_id of this LogVO.
        :type src_city_id: str
        """
        self._src_city_id = src_city_id

    @property
    def src_city_name(self):
        r"""Gets the src_city_name of this LogVO.

        **参数解释**： 源城市名称 **取值范围**： 不涉及

        :return: The src_city_name of this LogVO.
        :rtype: str
        """
        return self._src_city_name

    @src_city_name.setter
    def src_city_name(self, src_city_name):
        r"""Sets the src_city_name of this LogVO.

        **参数解释**： 源城市名称 **取值范围**： 不涉及

        :param src_city_name: The src_city_name of this LogVO.
        :type src_city_name: str
        """
        self._src_city_name = src_city_name

    @property
    def vgw_id(self):
        r"""Gets the vgw_id of this LogVO.

        **参数解释**： 虚拟网关ID **取值范围**： 不涉及

        :return: The vgw_id of this LogVO.
        :rtype: str
        """
        return self._vgw_id

    @vgw_id.setter
    def vgw_id(self, vgw_id):
        r"""Sets the vgw_id of this LogVO.

        **参数解释**： 虚拟网关ID **取值范围**： 不涉及

        :param vgw_id: The vgw_id of this LogVO.
        :type vgw_id: str
        """
        self._vgw_id = vgw_id

    @property
    def sctp_verification_tag(self):
        r"""Gets the sctp_verification_tag of this LogVO.

        **参数解释**： sctp验证标签，流量日志字段 **取值范围**： 不涉及

        :return: The sctp_verification_tag of this LogVO.
        :rtype: int
        """
        return self._sctp_verification_tag

    @sctp_verification_tag.setter
    def sctp_verification_tag(self, sctp_verification_tag):
        r"""Sets the sctp_verification_tag of this LogVO.

        **参数解释**： sctp验证标签，流量日志字段 **取值范围**： 不涉及

        :param sctp_verification_tag: The sctp_verification_tag of this LogVO.
        :type sctp_verification_tag: int
        """
        self._sctp_verification_tag = sctp_verification_tag

    @property
    def sctp_is_handshake_flow(self):
        r"""Gets the sctp_is_handshake_flow of this LogVO.

        **参数解释**： sctp握手流，流量日志字段 **取值范围**： 不涉及

        :return: The sctp_is_handshake_flow of this LogVO.
        :rtype: str
        """
        return self._sctp_is_handshake_flow

    @sctp_is_handshake_flow.setter
    def sctp_is_handshake_flow(self, sctp_is_handshake_flow):
        r"""Sets the sctp_is_handshake_flow of this LogVO.

        **参数解释**： sctp握手流，流量日志字段 **取值范围**： 不涉及

        :param sctp_is_handshake_flow: The sctp_is_handshake_flow of this LogVO.
        :type sctp_is_handshake_flow: str
        """
        self._sctp_is_handshake_flow = sctp_is_handshake_flow

    @property
    def qos_rule_id(self):
        r"""Gets the qos_rule_id of this LogVO.

        **参数解释**： qos规则ID，流量日志、访问控制日志存在 **取值范围**： 不涉及

        :return: The qos_rule_id of this LogVO.
        :rtype: str
        """
        return self._qos_rule_id

    @qos_rule_id.setter
    def qos_rule_id(self, qos_rule_id):
        r"""Sets the qos_rule_id of this LogVO.

        **参数解释**： qos规则ID，流量日志、访问控制日志存在 **取值范围**： 不涉及

        :param qos_rule_id: The qos_rule_id of this LogVO.
        :type qos_rule_id: str
        """
        self._qos_rule_id = qos_rule_id

    @property
    def qos_rule_name(self):
        r"""Gets the qos_rule_name of this LogVO.

        **参数解释**： qos规则名称，流量日志、访问控制日志存在 **取值范围**： 不涉及

        :return: The qos_rule_name of this LogVO.
        :rtype: str
        """
        return self._qos_rule_name

    @qos_rule_name.setter
    def qos_rule_name(self, qos_rule_name):
        r"""Sets the qos_rule_name of this LogVO.

        **参数解释**： qos规则名称，流量日志、访问控制日志存在 **取值范围**： 不涉及

        :param qos_rule_name: The qos_rule_name of this LogVO.
        :type qos_rule_name: str
        """
        self._qos_rule_name = qos_rule_name

    @property
    def qos_channel_id(self):
        r"""Gets the qos_channel_id of this LogVO.

        **参数解释**： qos通道ID，流量日志字段 **取值范围**： 不涉及

        :return: The qos_channel_id of this LogVO.
        :rtype: str
        """
        return self._qos_channel_id

    @qos_channel_id.setter
    def qos_channel_id(self, qos_channel_id):
        r"""Sets the qos_channel_id of this LogVO.

        **参数解释**： qos通道ID，流量日志字段 **取值范围**： 不涉及

        :param qos_channel_id: The qos_channel_id of this LogVO.
        :type qos_channel_id: str
        """
        self._qos_channel_id = qos_channel_id

    @property
    def qos_channel_name(self):
        r"""Gets the qos_channel_name of this LogVO.

        **参数解释**： qos通道名称，流量日志字段 **取值范围**： 不涉及

        :return: The qos_channel_name of this LogVO.
        :rtype: str
        """
        return self._qos_channel_name

    @qos_channel_name.setter
    def qos_channel_name(self, qos_channel_name):
        r"""Sets the qos_channel_name of this LogVO.

        **参数解释**： qos通道名称，流量日志字段 **取值范围**： 不涉及

        :param qos_channel_name: The qos_channel_name of this LogVO.
        :type qos_channel_name: str
        """
        self._qos_channel_name = qos_channel_name

    @property
    def qos_drop_packets(self):
        r"""Gets the qos_drop_packets of this LogVO.

        **参数解释**： qos丢包数，流量日志字段 **取值范围**： 不涉及

        :return: The qos_drop_packets of this LogVO.
        :rtype: float
        """
        return self._qos_drop_packets

    @qos_drop_packets.setter
    def qos_drop_packets(self, qos_drop_packets):
        r"""Sets the qos_drop_packets of this LogVO.

        **参数解释**： qos丢包数，流量日志字段 **取值范围**： 不涉及

        :param qos_drop_packets: The qos_drop_packets of this LogVO.
        :type qos_drop_packets: float
        """
        self._qos_drop_packets = qos_drop_packets

    @property
    def qos_drop_bytes(self):
        r"""Gets the qos_drop_bytes of this LogVO.

        **参数解释**： qos丢弃字节，流量日志字段 **取值范围**： 不涉及

        :return: The qos_drop_bytes of this LogVO.
        :rtype: float
        """
        return self._qos_drop_bytes

    @qos_drop_bytes.setter
    def qos_drop_bytes(self, qos_drop_bytes):
        r"""Sets the qos_drop_bytes of this LogVO.

        **参数解释**： qos丢弃字节，流量日志字段 **取值范围**： 不涉及

        :param qos_drop_bytes: The qos_drop_bytes of this LogVO.
        :type qos_drop_bytes: float
        """
        self._qos_drop_bytes = qos_drop_bytes

    @property
    def qos_rule_type(self):
        r"""Gets the qos_rule_type of this LogVO.

        **参数解释**： qos规则类型，流量日志、访问控制日志存在 **取值范围**： 不涉及

        :return: The qos_rule_type of this LogVO.
        :rtype: int
        """
        return self._qos_rule_type

    @qos_rule_type.setter
    def qos_rule_type(self, qos_rule_type):
        r"""Sets the qos_rule_type of this LogVO.

        **参数解释**： qos规则类型，流量日志、访问控制日志存在 **取值范围**： 不涉及

        :param qos_rule_type: The qos_rule_type of this LogVO.
        :type qos_rule_type: int
        """
        self._qos_rule_type = qos_rule_type

    @property
    def qos_channel_type(self):
        r"""Gets the qos_channel_type of this LogVO.

        **参数解释**： qos通道类型，流量日志字段 **取值范围**： 不涉及

        :return: The qos_channel_type of this LogVO.
        :rtype: int
        """
        return self._qos_channel_type

    @qos_channel_type.setter
    def qos_channel_type(self, qos_channel_type):
        r"""Sets the qos_channel_type of this LogVO.

        **参数解释**： qos通道类型，流量日志字段 **取值范围**： 不涉及

        :param qos_channel_type: The qos_channel_type of this LogVO.
        :type qos_channel_type: int
        """
        self._qos_channel_type = qos_channel_type

    @property
    def action(self):
        r"""Gets the action of this LogVO.

        **参数解释**： 动作，攻击日志、访问控制日志、URL日志存在 **取值范围**： 不涉及

        :return: The action of this LogVO.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this LogVO.

        **参数解释**： 动作，攻击日志、访问控制日志、URL日志存在 **取值范围**： 不涉及

        :param action: The action of this LogVO.
        :type action: str
        """
        self._action = action

    @property
    def url(self):
        r"""Gets the url of this LogVO.

        **参数解释**： url，URL日志字段 **取值范围**： 不涉及

        :return: The url of this LogVO.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this LogVO.

        **参数解释**： url，URL日志字段 **取值范围**： 不涉及

        :param url: The url of this LogVO.
        :type url: str
        """
        self._url = url

    @property
    def hit_time(self):
        r"""Gets the hit_time of this LogVO.

        **参数解释**： 命中时间，访问控制日志、URL日志存在 **取值范围**： 不涉及

        :return: The hit_time of this LogVO.
        :rtype: int
        """
        return self._hit_time

    @hit_time.setter
    def hit_time(self, hit_time):
        r"""Sets the hit_time of this LogVO.

        **参数解释**： 命中时间，访问控制日志、URL日志存在 **取值范围**： 不涉及

        :param hit_time: The hit_time of this LogVO.
        :type hit_time: int
        """
        self._hit_time = hit_time

    @property
    def rule_id(self):
        r"""Gets the rule_id of this LogVO.

        **参数解释**： 规则ID，访问控制日志、URL日志存在 **取值范围**： 不涉及

        :return: The rule_id of this LogVO.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this LogVO.

        **参数解释**： 规则ID，访问控制日志、URL日志存在 **取值范围**： 不涉及

        :param rule_id: The rule_id of this LogVO.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def rule_name(self):
        r"""Gets the rule_name of this LogVO.

        **参数解释**： 规则名称，访问控制日志、URL日志存在 **取值范围**： 不涉及

        :return: The rule_name of this LogVO.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this LogVO.

        **参数解释**： 规则名称，访问控制日志、URL日志存在 **取值范围**： 不涉及

        :param rule_name: The rule_name of this LogVO.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def rule_type(self):
        r"""Gets the rule_type of this LogVO.

        **参数解释**： 规则类型，访问控制日志和URL日志字段 **取值范围**： 不涉及

        :return: The rule_type of this LogVO.
        :rtype: int
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        r"""Sets the rule_type of this LogVO.

        **参数解释**： 规则类型，访问控制日志和URL日志字段 **取值范围**： 不涉及

        :param rule_type: The rule_type of this LogVO.
        :type rule_type: int
        """
        self._rule_type = rule_type

    @property
    def attack_rule(self):
        r"""Gets the attack_rule of this LogVO.

        **参数解释**： 规则类型，攻击日志字段 **取值范围**： 不涉及

        :return: The attack_rule of this LogVO.
        :rtype: str
        """
        return self._attack_rule

    @attack_rule.setter
    def attack_rule(self, attack_rule):
        r"""Sets the attack_rule of this LogVO.

        **参数解释**： 规则类型，攻击日志字段 **取值范围**： 不涉及

        :param attack_rule: The attack_rule of this LogVO.
        :type attack_rule: str
        """
        self._attack_rule = attack_rule

    @property
    def attack_rule_id(self):
        r"""Gets the attack_rule_id of this LogVO.

        **参数解释**： 攻击规则ID，攻击日志字段 **取值范围**： 不涉及

        :return: The attack_rule_id of this LogVO.
        :rtype: str
        """
        return self._attack_rule_id

    @attack_rule_id.setter
    def attack_rule_id(self, attack_rule_id):
        r"""Sets the attack_rule_id of this LogVO.

        **参数解释**： 攻击规则ID，攻击日志字段 **取值范围**： 不涉及

        :param attack_rule_id: The attack_rule_id of this LogVO.
        :type attack_rule_id: str
        """
        self._attack_rule_id = attack_rule_id

    @property
    def attack_type(self):
        r"""Gets the attack_type of this LogVO.

        **参数解释**： 攻击类型，攻击日志字段 **取值范围**： 不涉及

        :return: The attack_type of this LogVO.
        :rtype: str
        """
        return self._attack_type

    @attack_type.setter
    def attack_type(self, attack_type):
        r"""Sets the attack_type of this LogVO.

        **参数解释**： 攻击类型，攻击日志字段 **取值范围**： 不涉及

        :param attack_type: The attack_type of this LogVO.
        :type attack_type: str
        """
        self._attack_type = attack_type

    @property
    def event_time(self):
        r"""Gets the event_time of this LogVO.

        **参数解释**： 事件时间，攻击日志字段 **取值范围**： 不涉及

        :return: The event_time of this LogVO.
        :rtype: int
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        r"""Sets the event_time of this LogVO.

        **参数解释**： 事件时间，攻击日志字段 **取值范围**： 不涉及

        :param event_time: The event_time of this LogVO.
        :type event_time: int
        """
        self._event_time = event_time

    @property
    def level(self):
        r"""Gets the level of this LogVO.

        **参数解释**： 攻击等级，攻击日志字段 **取值范围**： 不涉及

        :return: The level of this LogVO.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this LogVO.

        **参数解释**： 攻击等级，攻击日志字段 **取值范围**： 不涉及

        :param level: The level of this LogVO.
        :type level: str
        """
        self._level = level

    @property
    def packet(self):
        r"""Gets the packet of this LogVO.

        **参数解释**： 规则载荷，攻击日志字段 **取值范围**： 不涉及

        :return: The packet of this LogVO.
        :rtype: str
        """
        return self._packet

    @packet.setter
    def packet(self, packet):
        r"""Sets the packet of this LogVO.

        **参数解释**： 规则载荷，攻击日志字段 **取值范围**： 不涉及

        :param packet: The packet of this LogVO.
        :type packet: str
        """
        self._packet = packet

    @property
    def source(self):
        r"""Gets the source of this LogVO.

        **参数解释**： 攻击来源，攻击日志字段 **取值范围**： 不涉及

        :return: The source of this LogVO.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this LogVO.

        **参数解释**： 攻击来源，攻击日志字段 **取值范围**： 不涉及

        :param source: The source of this LogVO.
        :type source: str
        """
        self._source = source

    @property
    def real_ip(self):
        r"""Gets the real_ip of this LogVO.

        **参数解释**： 真实IP，攻击日志字段 **取值范围**： 不涉及

        :return: The real_ip of this LogVO.
        :rtype: str
        """
        return self._real_ip

    @real_ip.setter
    def real_ip(self, real_ip):
        r"""Sets the real_ip of this LogVO.

        **参数解释**： 真实IP，攻击日志字段 **取值范围**： 不涉及

        :param real_ip: The real_ip of this LogVO.
        :type real_ip: str
        """
        self._real_ip = real_ip

    @property
    def tag(self):
        r"""Gets the tag of this LogVO.

        **参数解释**： 标签类型，攻击日志字段 **取值范围**： 1 WAF回源IP

        :return: The tag of this LogVO.
        :rtype: int
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this LogVO.

        **参数解释**： 标签类型，攻击日志字段 **取值范围**： 1 WAF回源IP

        :param tag: The tag of this LogVO.
        :type tag: int
        """
        self._tag = tag

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
        if not isinstance(other, LogVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
