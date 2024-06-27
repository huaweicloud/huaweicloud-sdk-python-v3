# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAttackLogsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'int',
        'end_time': 'int',
        'src_ip': 'str',
        'src_port': 'int',
        'dst_ip': 'str',
        'dst_port': 'int',
        'protocol': 'str',
        'app': 'str',
        'log_id': 'str',
        'next_date': 'int',
        'offset': 'int',
        'limit': 'int',
        'fw_instance_id': 'str',
        'action': 'str',
        'direction': 'str',
        'attack_type': 'str',
        'attack_rule': 'str',
        'level': 'str',
        'enterprise_project_id': 'str',
        'dst_host': 'str',
        'log_type': 'str',
        'attack_rule_id': 'str',
        'src_region_name': 'str',
        'dst_region_name': 'str',
        'src_province_name': 'str',
        'dst_province_name': 'str',
        'src_city_name': 'str',
        'dst_city_name': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'src_ip': 'src_ip',
        'src_port': 'src_port',
        'dst_ip': 'dst_ip',
        'dst_port': 'dst_port',
        'protocol': 'protocol',
        'app': 'app',
        'log_id': 'log_id',
        'next_date': 'next_date',
        'offset': 'offset',
        'limit': 'limit',
        'fw_instance_id': 'fw_instance_id',
        'action': 'action',
        'direction': 'direction',
        'attack_type': 'attack_type',
        'attack_rule': 'attack_rule',
        'level': 'level',
        'enterprise_project_id': 'enterprise_project_id',
        'dst_host': 'dst_host',
        'log_type': 'log_type',
        'attack_rule_id': 'attack_rule_id',
        'src_region_name': 'src_region_name',
        'dst_region_name': 'dst_region_name',
        'src_province_name': 'src_province_name',
        'dst_province_name': 'dst_province_name',
        'src_city_name': 'src_city_name',
        'dst_city_name': 'dst_city_name'
    }

    def __init__(self, start_time=None, end_time=None, src_ip=None, src_port=None, dst_ip=None, dst_port=None, protocol=None, app=None, log_id=None, next_date=None, offset=None, limit=None, fw_instance_id=None, action=None, direction=None, attack_type=None, attack_rule=None, level=None, enterprise_project_id=None, dst_host=None, log_type=None, attack_rule_id=None, src_region_name=None, dst_region_name=None, src_province_name=None, dst_province_name=None, src_city_name=None, dst_city_name=None):
        """ListAttackLogsRequest

        The model defined in huaweicloud sdk

        :param start_time: 开始时间，以毫秒为单位的时间戳，如1718936272648
        :type start_time: int
        :param end_time: 结束时间，以毫秒为单位的时间戳，如1718936272648
        :type end_time: int
        :param src_ip: 源IP
        :type src_ip: str
        :param src_port: 源端口号
        :type src_port: int
        :param dst_ip: 目的IP
        :type dst_ip: str
        :param dst_port: 目的端口号
        :type dst_port: int
        :param protocol: 协议类型，包含TCP, UDP,ICMP,ICMPV6等。
        :type protocol: str
        :param app: 应用协议
        :type app: str
        :param log_id: 文档ID,第一页为空，其他页不为空，其他页可取上一次查询最后一条数据的log_id
        :type log_id: str
        :param next_date: 下个日期，当是第一页时为空，不是第一页时不为空，其他页可取上一次查询最后一条数据的event_time
        :type next_date: int
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于0，首页时为空，非首页时不为空
        :type offset: int
        :param limit: 每页显示个数，范围为1-1024
        :type limit: int
        :param fw_instance_id: 防火墙实例id，创建云防火墙后用于标志防火墙由系统自动生成的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)。
        :type fw_instance_id: str
        :param action: 动作包含permit，deny
        :type action: str
        :param direction: 方向，包含in2out，out2in
        :type direction: str
        :param attack_type: 入侵事件类型
        :type attack_type: str
        :param attack_rule: 入侵事件规则
        :type attack_rule: str
        :param level: 威胁等级，包括CRITICAL、HIGH、MEDIUM、LOW
        :type level: str
        :param enterprise_project_id: 企业项目id，用户支持企业项目后，由企业项目生成的id。
        :type enterprise_project_id: str
        :param dst_host: 目标主机
        :type dst_host: str
        :param log_type: 日志类型包括：internet，vpc，nat
        :type log_type: str
        :param attack_rule_id: 入侵事件id
        :type attack_rule_id: str
        :param src_region_name: 源region名称
        :type src_region_name: str
        :param dst_region_name: 目的region名称
        :type dst_region_name: str
        :param src_province_name: 源省份名称
        :type src_province_name: str
        :param dst_province_name: 目的省份名称
        :type dst_province_name: str
        :param src_city_name: 源城市名称
        :type src_city_name: str
        :param dst_city_name: 目的城市名称
        :type dst_city_name: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._src_ip = None
        self._src_port = None
        self._dst_ip = None
        self._dst_port = None
        self._protocol = None
        self._app = None
        self._log_id = None
        self._next_date = None
        self._offset = None
        self._limit = None
        self._fw_instance_id = None
        self._action = None
        self._direction = None
        self._attack_type = None
        self._attack_rule = None
        self._level = None
        self._enterprise_project_id = None
        self._dst_host = None
        self._log_type = None
        self._attack_rule_id = None
        self._src_region_name = None
        self._dst_region_name = None
        self._src_province_name = None
        self._dst_province_name = None
        self._src_city_name = None
        self._dst_city_name = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
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
        if app is not None:
            self.app = app
        if log_id is not None:
            self.log_id = log_id
        if next_date is not None:
            self.next_date = next_date
        if offset is not None:
            self.offset = offset
        self.limit = limit
        self.fw_instance_id = fw_instance_id
        if action is not None:
            self.action = action
        if direction is not None:
            self.direction = direction
        if attack_type is not None:
            self.attack_type = attack_type
        if attack_rule is not None:
            self.attack_rule = attack_rule
        if level is not None:
            self.level = level
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if dst_host is not None:
            self.dst_host = dst_host
        if log_type is not None:
            self.log_type = log_type
        if attack_rule_id is not None:
            self.attack_rule_id = attack_rule_id
        if src_region_name is not None:
            self.src_region_name = src_region_name
        if dst_region_name is not None:
            self.dst_region_name = dst_region_name
        if src_province_name is not None:
            self.src_province_name = src_province_name
        if dst_province_name is not None:
            self.dst_province_name = dst_province_name
        if src_city_name is not None:
            self.src_city_name = src_city_name
        if dst_city_name is not None:
            self.dst_city_name = dst_city_name

    @property
    def start_time(self):
        """Gets the start_time of this ListAttackLogsRequest.

        开始时间，以毫秒为单位的时间戳，如1718936272648

        :return: The start_time of this ListAttackLogsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListAttackLogsRequest.

        开始时间，以毫秒为单位的时间戳，如1718936272648

        :param start_time: The start_time of this ListAttackLogsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListAttackLogsRequest.

        结束时间，以毫秒为单位的时间戳，如1718936272648

        :return: The end_time of this ListAttackLogsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListAttackLogsRequest.

        结束时间，以毫秒为单位的时间戳，如1718936272648

        :param end_time: The end_time of this ListAttackLogsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def src_ip(self):
        """Gets the src_ip of this ListAttackLogsRequest.

        源IP

        :return: The src_ip of this ListAttackLogsRequest.
        :rtype: str
        """
        return self._src_ip

    @src_ip.setter
    def src_ip(self, src_ip):
        """Sets the src_ip of this ListAttackLogsRequest.

        源IP

        :param src_ip: The src_ip of this ListAttackLogsRequest.
        :type src_ip: str
        """
        self._src_ip = src_ip

    @property
    def src_port(self):
        """Gets the src_port of this ListAttackLogsRequest.

        源端口号

        :return: The src_port of this ListAttackLogsRequest.
        :rtype: int
        """
        return self._src_port

    @src_port.setter
    def src_port(self, src_port):
        """Sets the src_port of this ListAttackLogsRequest.

        源端口号

        :param src_port: The src_port of this ListAttackLogsRequest.
        :type src_port: int
        """
        self._src_port = src_port

    @property
    def dst_ip(self):
        """Gets the dst_ip of this ListAttackLogsRequest.

        目的IP

        :return: The dst_ip of this ListAttackLogsRequest.
        :rtype: str
        """
        return self._dst_ip

    @dst_ip.setter
    def dst_ip(self, dst_ip):
        """Sets the dst_ip of this ListAttackLogsRequest.

        目的IP

        :param dst_ip: The dst_ip of this ListAttackLogsRequest.
        :type dst_ip: str
        """
        self._dst_ip = dst_ip

    @property
    def dst_port(self):
        """Gets the dst_port of this ListAttackLogsRequest.

        目的端口号

        :return: The dst_port of this ListAttackLogsRequest.
        :rtype: int
        """
        return self._dst_port

    @dst_port.setter
    def dst_port(self, dst_port):
        """Sets the dst_port of this ListAttackLogsRequest.

        目的端口号

        :param dst_port: The dst_port of this ListAttackLogsRequest.
        :type dst_port: int
        """
        self._dst_port = dst_port

    @property
    def protocol(self):
        """Gets the protocol of this ListAttackLogsRequest.

        协议类型，包含TCP, UDP,ICMP,ICMPV6等。

        :return: The protocol of this ListAttackLogsRequest.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ListAttackLogsRequest.

        协议类型，包含TCP, UDP,ICMP,ICMPV6等。

        :param protocol: The protocol of this ListAttackLogsRequest.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def app(self):
        """Gets the app of this ListAttackLogsRequest.

        应用协议

        :return: The app of this ListAttackLogsRequest.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this ListAttackLogsRequest.

        应用协议

        :param app: The app of this ListAttackLogsRequest.
        :type app: str
        """
        self._app = app

    @property
    def log_id(self):
        """Gets the log_id of this ListAttackLogsRequest.

        文档ID,第一页为空，其他页不为空，其他页可取上一次查询最后一条数据的log_id

        :return: The log_id of this ListAttackLogsRequest.
        :rtype: str
        """
        return self._log_id

    @log_id.setter
    def log_id(self, log_id):
        """Sets the log_id of this ListAttackLogsRequest.

        文档ID,第一页为空，其他页不为空，其他页可取上一次查询最后一条数据的log_id

        :param log_id: The log_id of this ListAttackLogsRequest.
        :type log_id: str
        """
        self._log_id = log_id

    @property
    def next_date(self):
        """Gets the next_date of this ListAttackLogsRequest.

        下个日期，当是第一页时为空，不是第一页时不为空，其他页可取上一次查询最后一条数据的event_time

        :return: The next_date of this ListAttackLogsRequest.
        :rtype: int
        """
        return self._next_date

    @next_date.setter
    def next_date(self, next_date):
        """Sets the next_date of this ListAttackLogsRequest.

        下个日期，当是第一页时为空，不是第一页时不为空，其他页可取上一次查询最后一条数据的event_time

        :param next_date: The next_date of this ListAttackLogsRequest.
        :type next_date: int
        """
        self._next_date = next_date

    @property
    def offset(self):
        """Gets the offset of this ListAttackLogsRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于0，首页时为空，非首页时不为空

        :return: The offset of this ListAttackLogsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAttackLogsRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于0，首页时为空，非首页时不为空

        :param offset: The offset of this ListAttackLogsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListAttackLogsRequest.

        每页显示个数，范围为1-1024

        :return: The limit of this ListAttackLogsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAttackLogsRequest.

        每页显示个数，范围为1-1024

        :param limit: The limit of this ListAttackLogsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def fw_instance_id(self):
        """Gets the fw_instance_id of this ListAttackLogsRequest.

        防火墙实例id，创建云防火墙后用于标志防火墙由系统自动生成的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)。

        :return: The fw_instance_id of this ListAttackLogsRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        """Sets the fw_instance_id of this ListAttackLogsRequest.

        防火墙实例id，创建云防火墙后用于标志防火墙由系统自动生成的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)。

        :param fw_instance_id: The fw_instance_id of this ListAttackLogsRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def action(self):
        """Gets the action of this ListAttackLogsRequest.

        动作包含permit，deny

        :return: The action of this ListAttackLogsRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ListAttackLogsRequest.

        动作包含permit，deny

        :param action: The action of this ListAttackLogsRequest.
        :type action: str
        """
        self._action = action

    @property
    def direction(self):
        """Gets the direction of this ListAttackLogsRequest.

        方向，包含in2out，out2in

        :return: The direction of this ListAttackLogsRequest.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this ListAttackLogsRequest.

        方向，包含in2out，out2in

        :param direction: The direction of this ListAttackLogsRequest.
        :type direction: str
        """
        self._direction = direction

    @property
    def attack_type(self):
        """Gets the attack_type of this ListAttackLogsRequest.

        入侵事件类型

        :return: The attack_type of this ListAttackLogsRequest.
        :rtype: str
        """
        return self._attack_type

    @attack_type.setter
    def attack_type(self, attack_type):
        """Sets the attack_type of this ListAttackLogsRequest.

        入侵事件类型

        :param attack_type: The attack_type of this ListAttackLogsRequest.
        :type attack_type: str
        """
        self._attack_type = attack_type

    @property
    def attack_rule(self):
        """Gets the attack_rule of this ListAttackLogsRequest.

        入侵事件规则

        :return: The attack_rule of this ListAttackLogsRequest.
        :rtype: str
        """
        return self._attack_rule

    @attack_rule.setter
    def attack_rule(self, attack_rule):
        """Sets the attack_rule of this ListAttackLogsRequest.

        入侵事件规则

        :param attack_rule: The attack_rule of this ListAttackLogsRequest.
        :type attack_rule: str
        """
        self._attack_rule = attack_rule

    @property
    def level(self):
        """Gets the level of this ListAttackLogsRequest.

        威胁等级，包括CRITICAL、HIGH、MEDIUM、LOW

        :return: The level of this ListAttackLogsRequest.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this ListAttackLogsRequest.

        威胁等级，包括CRITICAL、HIGH、MEDIUM、LOW

        :param level: The level of this ListAttackLogsRequest.
        :type level: str
        """
        self._level = level

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListAttackLogsRequest.

        企业项目id，用户支持企业项目后，由企业项目生成的id。

        :return: The enterprise_project_id of this ListAttackLogsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListAttackLogsRequest.

        企业项目id，用户支持企业项目后，由企业项目生成的id。

        :param enterprise_project_id: The enterprise_project_id of this ListAttackLogsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def dst_host(self):
        """Gets the dst_host of this ListAttackLogsRequest.

        目标主机

        :return: The dst_host of this ListAttackLogsRequest.
        :rtype: str
        """
        return self._dst_host

    @dst_host.setter
    def dst_host(self, dst_host):
        """Sets the dst_host of this ListAttackLogsRequest.

        目标主机

        :param dst_host: The dst_host of this ListAttackLogsRequest.
        :type dst_host: str
        """
        self._dst_host = dst_host

    @property
    def log_type(self):
        """Gets the log_type of this ListAttackLogsRequest.

        日志类型包括：internet，vpc，nat

        :return: The log_type of this ListAttackLogsRequest.
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        """Sets the log_type of this ListAttackLogsRequest.

        日志类型包括：internet，vpc，nat

        :param log_type: The log_type of this ListAttackLogsRequest.
        :type log_type: str
        """
        self._log_type = log_type

    @property
    def attack_rule_id(self):
        """Gets the attack_rule_id of this ListAttackLogsRequest.

        入侵事件id

        :return: The attack_rule_id of this ListAttackLogsRequest.
        :rtype: str
        """
        return self._attack_rule_id

    @attack_rule_id.setter
    def attack_rule_id(self, attack_rule_id):
        """Sets the attack_rule_id of this ListAttackLogsRequest.

        入侵事件id

        :param attack_rule_id: The attack_rule_id of this ListAttackLogsRequest.
        :type attack_rule_id: str
        """
        self._attack_rule_id = attack_rule_id

    @property
    def src_region_name(self):
        """Gets the src_region_name of this ListAttackLogsRequest.

        源region名称

        :return: The src_region_name of this ListAttackLogsRequest.
        :rtype: str
        """
        return self._src_region_name

    @src_region_name.setter
    def src_region_name(self, src_region_name):
        """Sets the src_region_name of this ListAttackLogsRequest.

        源region名称

        :param src_region_name: The src_region_name of this ListAttackLogsRequest.
        :type src_region_name: str
        """
        self._src_region_name = src_region_name

    @property
    def dst_region_name(self):
        """Gets the dst_region_name of this ListAttackLogsRequest.

        目的region名称

        :return: The dst_region_name of this ListAttackLogsRequest.
        :rtype: str
        """
        return self._dst_region_name

    @dst_region_name.setter
    def dst_region_name(self, dst_region_name):
        """Sets the dst_region_name of this ListAttackLogsRequest.

        目的region名称

        :param dst_region_name: The dst_region_name of this ListAttackLogsRequest.
        :type dst_region_name: str
        """
        self._dst_region_name = dst_region_name

    @property
    def src_province_name(self):
        """Gets the src_province_name of this ListAttackLogsRequest.

        源省份名称

        :return: The src_province_name of this ListAttackLogsRequest.
        :rtype: str
        """
        return self._src_province_name

    @src_province_name.setter
    def src_province_name(self, src_province_name):
        """Sets the src_province_name of this ListAttackLogsRequest.

        源省份名称

        :param src_province_name: The src_province_name of this ListAttackLogsRequest.
        :type src_province_name: str
        """
        self._src_province_name = src_province_name

    @property
    def dst_province_name(self):
        """Gets the dst_province_name of this ListAttackLogsRequest.

        目的省份名称

        :return: The dst_province_name of this ListAttackLogsRequest.
        :rtype: str
        """
        return self._dst_province_name

    @dst_province_name.setter
    def dst_province_name(self, dst_province_name):
        """Sets the dst_province_name of this ListAttackLogsRequest.

        目的省份名称

        :param dst_province_name: The dst_province_name of this ListAttackLogsRequest.
        :type dst_province_name: str
        """
        self._dst_province_name = dst_province_name

    @property
    def src_city_name(self):
        """Gets the src_city_name of this ListAttackLogsRequest.

        源城市名称

        :return: The src_city_name of this ListAttackLogsRequest.
        :rtype: str
        """
        return self._src_city_name

    @src_city_name.setter
    def src_city_name(self, src_city_name):
        """Sets the src_city_name of this ListAttackLogsRequest.

        源城市名称

        :param src_city_name: The src_city_name of this ListAttackLogsRequest.
        :type src_city_name: str
        """
        self._src_city_name = src_city_name

    @property
    def dst_city_name(self):
        """Gets the dst_city_name of this ListAttackLogsRequest.

        目的城市名称

        :return: The dst_city_name of this ListAttackLogsRequest.
        :rtype: str
        """
        return self._dst_city_name

    @dst_city_name.setter
    def dst_city_name(self, dst_city_name):
        """Sets the dst_city_name of this ListAttackLogsRequest.

        目的城市名称

        :param dst_city_name: The dst_city_name of this ListAttackLogsRequest.
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
        if not isinstance(other, ListAttackLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
