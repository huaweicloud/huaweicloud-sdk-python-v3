# coding: utf-8

import re
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
        'source': 'str',
        'enterprise_project_id': 'str'
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
        'source': 'source',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, start_time=None, end_time=None, src_ip=None, src_port=None, dst_ip=None, dst_port=None, protocol=None, app=None, log_id=None, next_date=None, offset=None, limit=None, fw_instance_id=None, action=None, direction=None, attack_type=None, attack_rule=None, level=None, source=None, enterprise_project_id=None):
        """ListAttackLogsRequest

        The model defined in huaweicloud sdk

        :param start_time: 开始时间
        :type start_time: int
        :param end_time: 结束时间
        :type end_time: int
        :param src_ip: 源IP
        :type src_ip: str
        :param src_port: 源端口号
        :type src_port: int
        :param dst_ip: 目的IP
        :type dst_ip: str
        :param dst_port: 目的端口号
        :type dst_port: int
        :param protocol: 协议类型:TCP为6, UDP为17,ICMP为1,ICMPV6为58,ANY为-1,手动类型不为空，自动类型为空
        :type protocol: str
        :param app: 应用协议
        :type app: str
        :param log_id: 日志ID，当是第一页时为空，不是第一页时不为空
        :type log_id: str
        :param next_date: 下个日期，当是第一页时为空，不是第一页时不为空
        :type next_date: int
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        :param limit: 每页显示个数
        :type limit: int
        :param fw_instance_id: 防火墙实例id，创建云防火墙后用于标志防火墙由系统自动生成的标志id，可通过调用查询防火墙实例接口获得。具体可参考APIExlorer和帮助中心FAQ。
        :type fw_instance_id: str
        :param action: 动作0：permit,1：deny
        :type action: str
        :param direction: 方向0：外到内1：内到外
        :type direction: str
        :param attack_type: 入侵事件类型
        :type attack_type: str
        :param attack_rule: 入侵事件规则
        :type attack_rule: str
        :param level: 威胁等级
        :type level: str
        :param source: 判断来源
        :type source: str
        :param enterprise_project_id: 企业项目id，用户支持企业项目后，由企业项目生成的id。
        :type enterprise_project_id: str
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
        self._source = None
        self._enterprise_project_id = None
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
        if source is not None:
            self.source = source
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def start_time(self):
        """Gets the start_time of this ListAttackLogsRequest.

        开始时间

        :return: The start_time of this ListAttackLogsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListAttackLogsRequest.

        开始时间

        :param start_time: The start_time of this ListAttackLogsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListAttackLogsRequest.

        结束时间

        :return: The end_time of this ListAttackLogsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListAttackLogsRequest.

        结束时间

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

        协议类型:TCP为6, UDP为17,ICMP为1,ICMPV6为58,ANY为-1,手动类型不为空，自动类型为空

        :return: The protocol of this ListAttackLogsRequest.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ListAttackLogsRequest.

        协议类型:TCP为6, UDP为17,ICMP为1,ICMPV6为58,ANY为-1,手动类型不为空，自动类型为空

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

        日志ID，当是第一页时为空，不是第一页时不为空

        :return: The log_id of this ListAttackLogsRequest.
        :rtype: str
        """
        return self._log_id

    @log_id.setter
    def log_id(self, log_id):
        """Sets the log_id of this ListAttackLogsRequest.

        日志ID，当是第一页时为空，不是第一页时不为空

        :param log_id: The log_id of this ListAttackLogsRequest.
        :type log_id: str
        """
        self._log_id = log_id

    @property
    def next_date(self):
        """Gets the next_date of this ListAttackLogsRequest.

        下个日期，当是第一页时为空，不是第一页时不为空

        :return: The next_date of this ListAttackLogsRequest.
        :rtype: int
        """
        return self._next_date

    @next_date.setter
    def next_date(self, next_date):
        """Sets the next_date of this ListAttackLogsRequest.

        下个日期，当是第一页时为空，不是第一页时不为空

        :param next_date: The next_date of this ListAttackLogsRequest.
        :type next_date: int
        """
        self._next_date = next_date

    @property
    def offset(self):
        """Gets the offset of this ListAttackLogsRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ListAttackLogsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAttackLogsRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ListAttackLogsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListAttackLogsRequest.

        每页显示个数

        :return: The limit of this ListAttackLogsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAttackLogsRequest.

        每页显示个数

        :param limit: The limit of this ListAttackLogsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def fw_instance_id(self):
        """Gets the fw_instance_id of this ListAttackLogsRequest.

        防火墙实例id，创建云防火墙后用于标志防火墙由系统自动生成的标志id，可通过调用查询防火墙实例接口获得。具体可参考APIExlorer和帮助中心FAQ。

        :return: The fw_instance_id of this ListAttackLogsRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        """Sets the fw_instance_id of this ListAttackLogsRequest.

        防火墙实例id，创建云防火墙后用于标志防火墙由系统自动生成的标志id，可通过调用查询防火墙实例接口获得。具体可参考APIExlorer和帮助中心FAQ。

        :param fw_instance_id: The fw_instance_id of this ListAttackLogsRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def action(self):
        """Gets the action of this ListAttackLogsRequest.

        动作0：permit,1：deny

        :return: The action of this ListAttackLogsRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ListAttackLogsRequest.

        动作0：permit,1：deny

        :param action: The action of this ListAttackLogsRequest.
        :type action: str
        """
        self._action = action

    @property
    def direction(self):
        """Gets the direction of this ListAttackLogsRequest.

        方向0：外到内1：内到外

        :return: The direction of this ListAttackLogsRequest.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this ListAttackLogsRequest.

        方向0：外到内1：内到外

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

        威胁等级

        :return: The level of this ListAttackLogsRequest.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this ListAttackLogsRequest.

        威胁等级

        :param level: The level of this ListAttackLogsRequest.
        :type level: str
        """
        self._level = level

    @property
    def source(self):
        """Gets the source of this ListAttackLogsRequest.

        判断来源

        :return: The source of this ListAttackLogsRequest.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ListAttackLogsRequest.

        判断来源

        :param source: The source of this ListAttackLogsRequest.
        :type source: str
        """
        self._source = source

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
