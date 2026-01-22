# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddRuleAclDtoRules:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'sequence': 'OrderRuleAclDto',
        'address_type': 'int',
        'action_type': 'int',
        'status': 'int',
        'applications': 'list[str]',
        'long_connect_time': 'int',
        'long_connect_time_hour': 'int',
        'long_connect_time_minute': 'int',
        'long_connect_time_second': 'int',
        'long_connect_enable': 'int',
        'description': 'str',
        'direction': 'int',
        'source': 'RuleAddressDtoForRequest',
        'destination': 'RuleAddressDtoForRequest',
        'service': 'RuleServiceDto',
        'tag': 'TagsVO'
    }

    attribute_map = {
        'name': 'name',
        'sequence': 'sequence',
        'address_type': 'address_type',
        'action_type': 'action_type',
        'status': 'status',
        'applications': 'applications',
        'long_connect_time': 'long_connect_time',
        'long_connect_time_hour': 'long_connect_time_hour',
        'long_connect_time_minute': 'long_connect_time_minute',
        'long_connect_time_second': 'long_connect_time_second',
        'long_connect_enable': 'long_connect_enable',
        'description': 'description',
        'direction': 'direction',
        'source': 'source',
        'destination': 'destination',
        'service': 'service',
        'tag': 'tag'
    }

    def __init__(self, name=None, sequence=None, address_type=None, action_type=None, status=None, applications=None, long_connect_time=None, long_connect_time_hour=None, long_connect_time_minute=None, long_connect_time_second=None, long_connect_enable=None, description=None, direction=None, source=None, destination=None, service=None, tag=None):
        r"""AddRuleAclDtoRules

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 规则名称，由用户定义，用于标识规则 **约束限制**： 字符串长度为0到255 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type name: str
        :param sequence: 
        :type sequence: :class:`huaweicloudsdkcfw.v1.OrderRuleAclDto`
        :param address_type: **参数解释**： IP地址的互联网协议类型，用于指定IP地址的互联网协议，由客户指定 **约束限制**： 不涉及 **取值范围**： 0表示IPv4，1表示IPv6 **默认取值**： 不涉及
        :type address_type: int
        :param action_type: **参数解释**： 规则动作类型，用于区分规则对流量的动作 **约束限制**： 仅能使用数字0和1 **取值范围**： 0表示允许通行（permit），1表示拒绝通行（deny） **默认取值**： 不涉及
        :type action_type: int
        :param status: **参数解释**： 规则启用状态，用于区分规则是否启用 **约束限制**： 仅能使用数字0和1 **取值范围**： 0表示启用，1表示禁用 **默认取值**： 不涉及
        :type status: int
        :param applications: **参数解释**： 规则应用协议列表 **约束限制**： 不涉及 **取值范围**： 规则应用类型包括：“HTTP”，\&quot;HTTPS\&quot;，\&quot;TLS1\&quot;，“DNS”，“SSH”，“MYSQL”，“SMTP”，“RDP”，“RDPS”，“VNC”，“POP3”，“IMAP4”，“SMTPS”，“POP3S”，“FTPS”，“ANY”，“BGP”等。 **默认取值**： 不涉及
        :type applications: list[str]
        :param long_connect_time: **参数解释**： 长连接时长（s），用于表示流量产生会话保持的最大时长。 **约束限制**： 仅能为数字 **取值范围**： 1-86400000。 **默认取值**： 不涉及
        :type long_connect_time: int
        :param long_connect_time_hour: **参数解释**： 长连接时长对应小时数（h）。 **约束限制**： 仅能为数字 **取值范围**： 0-24000。 **默认取值**： 不涉及
        :type long_connect_time_hour: int
        :param long_connect_time_minute: **参数解释**： 长连接时长对应分钟数（min）。 **约束限制**： 仅能为数字 **取值范围**： 0-60。 **默认取值**： 不涉及
        :type long_connect_time_minute: int
        :param long_connect_time_second: **参数解释**： 长连接时长对应秒数（s）。 **约束限制**： 仅能为数字 **取值范围**： 0-60。 **默认取值**： 不涉及
        :type long_connect_time_second: int
        :param long_connect_enable: **参数解释**： 用于表示是否支持长连接。 **约束限制**： 不涉及 **取值范围**： 0表示不支持，1表示支持 **默认取值**： 不涉及
        :type long_connect_enable: int
        :param description: **参数解释**： 规则描述，用于描述规则的用途。 **约束限制**： 不涉及 **取值范围**： 长度在0-255之间 **默认取值**： 不涉及
        :type description: str
        :param direction: **参数解释**： 规则方向，用于指定规则是从云上至云下，还是云下至云上 **约束限制**： 当规则type&#x3D;0（互联网规则）或者type&#x3D; 2（NAT规则）时方向值必填 **取值范围**： 0表示外到内（云下到云上），1表示内到外（云上到云下）， **默认取值**： 不涉及
        :type direction: int
        :param source: 
        :type source: :class:`huaweicloudsdkcfw.v1.RuleAddressDtoForRequest`
        :param destination: 
        :type destination: :class:`huaweicloudsdkcfw.v1.RuleAddressDtoForRequest`
        :param service: 
        :type service: :class:`huaweicloudsdkcfw.v1.RuleServiceDto`
        :param tag: 
        :type tag: :class:`huaweicloudsdkcfw.v1.TagsVO`
        """
        
        

        self._name = None
        self._sequence = None
        self._address_type = None
        self._action_type = None
        self._status = None
        self._applications = None
        self._long_connect_time = None
        self._long_connect_time_hour = None
        self._long_connect_time_minute = None
        self._long_connect_time_second = None
        self._long_connect_enable = None
        self._description = None
        self._direction = None
        self._source = None
        self._destination = None
        self._service = None
        self._tag = None
        self.discriminator = None

        self.name = name
        self.sequence = sequence
        self.address_type = address_type
        self.action_type = action_type
        self.status = status
        if applications is not None:
            self.applications = applications
        if long_connect_time is not None:
            self.long_connect_time = long_connect_time
        if long_connect_time_hour is not None:
            self.long_connect_time_hour = long_connect_time_hour
        if long_connect_time_minute is not None:
            self.long_connect_time_minute = long_connect_time_minute
        if long_connect_time_second is not None:
            self.long_connect_time_second = long_connect_time_second
        self.long_connect_enable = long_connect_enable
        if description is not None:
            self.description = description
        if direction is not None:
            self.direction = direction
        self.source = source
        self.destination = destination
        self.service = service
        if tag is not None:
            self.tag = tag

    @property
    def name(self):
        r"""Gets the name of this AddRuleAclDtoRules.

        **参数解释**： 规则名称，由用户定义，用于标识规则 **约束限制**： 字符串长度为0到255 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The name of this AddRuleAclDtoRules.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AddRuleAclDtoRules.

        **参数解释**： 规则名称，由用户定义，用于标识规则 **约束限制**： 字符串长度为0到255 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param name: The name of this AddRuleAclDtoRules.
        :type name: str
        """
        self._name = name

    @property
    def sequence(self):
        r"""Gets the sequence of this AddRuleAclDtoRules.

        :return: The sequence of this AddRuleAclDtoRules.
        :rtype: :class:`huaweicloudsdkcfw.v1.OrderRuleAclDto`
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        r"""Sets the sequence of this AddRuleAclDtoRules.

        :param sequence: The sequence of this AddRuleAclDtoRules.
        :type sequence: :class:`huaweicloudsdkcfw.v1.OrderRuleAclDto`
        """
        self._sequence = sequence

    @property
    def address_type(self):
        r"""Gets the address_type of this AddRuleAclDtoRules.

        **参数解释**： IP地址的互联网协议类型，用于指定IP地址的互联网协议，由客户指定 **约束限制**： 不涉及 **取值范围**： 0表示IPv4，1表示IPv6 **默认取值**： 不涉及

        :return: The address_type of this AddRuleAclDtoRules.
        :rtype: int
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        r"""Sets the address_type of this AddRuleAclDtoRules.

        **参数解释**： IP地址的互联网协议类型，用于指定IP地址的互联网协议，由客户指定 **约束限制**： 不涉及 **取值范围**： 0表示IPv4，1表示IPv6 **默认取值**： 不涉及

        :param address_type: The address_type of this AddRuleAclDtoRules.
        :type address_type: int
        """
        self._address_type = address_type

    @property
    def action_type(self):
        r"""Gets the action_type of this AddRuleAclDtoRules.

        **参数解释**： 规则动作类型，用于区分规则对流量的动作 **约束限制**： 仅能使用数字0和1 **取值范围**： 0表示允许通行（permit），1表示拒绝通行（deny） **默认取值**： 不涉及

        :return: The action_type of this AddRuleAclDtoRules.
        :rtype: int
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        r"""Sets the action_type of this AddRuleAclDtoRules.

        **参数解释**： 规则动作类型，用于区分规则对流量的动作 **约束限制**： 仅能使用数字0和1 **取值范围**： 0表示允许通行（permit），1表示拒绝通行（deny） **默认取值**： 不涉及

        :param action_type: The action_type of this AddRuleAclDtoRules.
        :type action_type: int
        """
        self._action_type = action_type

    @property
    def status(self):
        r"""Gets the status of this AddRuleAclDtoRules.

        **参数解释**： 规则启用状态，用于区分规则是否启用 **约束限制**： 仅能使用数字0和1 **取值范围**： 0表示启用，1表示禁用 **默认取值**： 不涉及

        :return: The status of this AddRuleAclDtoRules.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AddRuleAclDtoRules.

        **参数解释**： 规则启用状态，用于区分规则是否启用 **约束限制**： 仅能使用数字0和1 **取值范围**： 0表示启用，1表示禁用 **默认取值**： 不涉及

        :param status: The status of this AddRuleAclDtoRules.
        :type status: int
        """
        self._status = status

    @property
    def applications(self):
        r"""Gets the applications of this AddRuleAclDtoRules.

        **参数解释**： 规则应用协议列表 **约束限制**： 不涉及 **取值范围**： 规则应用类型包括：“HTTP”，\"HTTPS\"，\"TLS1\"，“DNS”，“SSH”，“MYSQL”，“SMTP”，“RDP”，“RDPS”，“VNC”，“POP3”，“IMAP4”，“SMTPS”，“POP3S”，“FTPS”，“ANY”，“BGP”等。 **默认取值**： 不涉及

        :return: The applications of this AddRuleAclDtoRules.
        :rtype: list[str]
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        r"""Sets the applications of this AddRuleAclDtoRules.

        **参数解释**： 规则应用协议列表 **约束限制**： 不涉及 **取值范围**： 规则应用类型包括：“HTTP”，\"HTTPS\"，\"TLS1\"，“DNS”，“SSH”，“MYSQL”，“SMTP”，“RDP”，“RDPS”，“VNC”，“POP3”，“IMAP4”，“SMTPS”，“POP3S”，“FTPS”，“ANY”，“BGP”等。 **默认取值**： 不涉及

        :param applications: The applications of this AddRuleAclDtoRules.
        :type applications: list[str]
        """
        self._applications = applications

    @property
    def long_connect_time(self):
        r"""Gets the long_connect_time of this AddRuleAclDtoRules.

        **参数解释**： 长连接时长（s），用于表示流量产生会话保持的最大时长。 **约束限制**： 仅能为数字 **取值范围**： 1-86400000。 **默认取值**： 不涉及

        :return: The long_connect_time of this AddRuleAclDtoRules.
        :rtype: int
        """
        return self._long_connect_time

    @long_connect_time.setter
    def long_connect_time(self, long_connect_time):
        r"""Sets the long_connect_time of this AddRuleAclDtoRules.

        **参数解释**： 长连接时长（s），用于表示流量产生会话保持的最大时长。 **约束限制**： 仅能为数字 **取值范围**： 1-86400000。 **默认取值**： 不涉及

        :param long_connect_time: The long_connect_time of this AddRuleAclDtoRules.
        :type long_connect_time: int
        """
        self._long_connect_time = long_connect_time

    @property
    def long_connect_time_hour(self):
        r"""Gets the long_connect_time_hour of this AddRuleAclDtoRules.

        **参数解释**： 长连接时长对应小时数（h）。 **约束限制**： 仅能为数字 **取值范围**： 0-24000。 **默认取值**： 不涉及

        :return: The long_connect_time_hour of this AddRuleAclDtoRules.
        :rtype: int
        """
        return self._long_connect_time_hour

    @long_connect_time_hour.setter
    def long_connect_time_hour(self, long_connect_time_hour):
        r"""Sets the long_connect_time_hour of this AddRuleAclDtoRules.

        **参数解释**： 长连接时长对应小时数（h）。 **约束限制**： 仅能为数字 **取值范围**： 0-24000。 **默认取值**： 不涉及

        :param long_connect_time_hour: The long_connect_time_hour of this AddRuleAclDtoRules.
        :type long_connect_time_hour: int
        """
        self._long_connect_time_hour = long_connect_time_hour

    @property
    def long_connect_time_minute(self):
        r"""Gets the long_connect_time_minute of this AddRuleAclDtoRules.

        **参数解释**： 长连接时长对应分钟数（min）。 **约束限制**： 仅能为数字 **取值范围**： 0-60。 **默认取值**： 不涉及

        :return: The long_connect_time_minute of this AddRuleAclDtoRules.
        :rtype: int
        """
        return self._long_connect_time_minute

    @long_connect_time_minute.setter
    def long_connect_time_minute(self, long_connect_time_minute):
        r"""Sets the long_connect_time_minute of this AddRuleAclDtoRules.

        **参数解释**： 长连接时长对应分钟数（min）。 **约束限制**： 仅能为数字 **取值范围**： 0-60。 **默认取值**： 不涉及

        :param long_connect_time_minute: The long_connect_time_minute of this AddRuleAclDtoRules.
        :type long_connect_time_minute: int
        """
        self._long_connect_time_minute = long_connect_time_minute

    @property
    def long_connect_time_second(self):
        r"""Gets the long_connect_time_second of this AddRuleAclDtoRules.

        **参数解释**： 长连接时长对应秒数（s）。 **约束限制**： 仅能为数字 **取值范围**： 0-60。 **默认取值**： 不涉及

        :return: The long_connect_time_second of this AddRuleAclDtoRules.
        :rtype: int
        """
        return self._long_connect_time_second

    @long_connect_time_second.setter
    def long_connect_time_second(self, long_connect_time_second):
        r"""Sets the long_connect_time_second of this AddRuleAclDtoRules.

        **参数解释**： 长连接时长对应秒数（s）。 **约束限制**： 仅能为数字 **取值范围**： 0-60。 **默认取值**： 不涉及

        :param long_connect_time_second: The long_connect_time_second of this AddRuleAclDtoRules.
        :type long_connect_time_second: int
        """
        self._long_connect_time_second = long_connect_time_second

    @property
    def long_connect_enable(self):
        r"""Gets the long_connect_enable of this AddRuleAclDtoRules.

        **参数解释**： 用于表示是否支持长连接。 **约束限制**： 不涉及 **取值范围**： 0表示不支持，1表示支持 **默认取值**： 不涉及

        :return: The long_connect_enable of this AddRuleAclDtoRules.
        :rtype: int
        """
        return self._long_connect_enable

    @long_connect_enable.setter
    def long_connect_enable(self, long_connect_enable):
        r"""Sets the long_connect_enable of this AddRuleAclDtoRules.

        **参数解释**： 用于表示是否支持长连接。 **约束限制**： 不涉及 **取值范围**： 0表示不支持，1表示支持 **默认取值**： 不涉及

        :param long_connect_enable: The long_connect_enable of this AddRuleAclDtoRules.
        :type long_connect_enable: int
        """
        self._long_connect_enable = long_connect_enable

    @property
    def description(self):
        r"""Gets the description of this AddRuleAclDtoRules.

        **参数解释**： 规则描述，用于描述规则的用途。 **约束限制**： 不涉及 **取值范围**： 长度在0-255之间 **默认取值**： 不涉及

        :return: The description of this AddRuleAclDtoRules.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AddRuleAclDtoRules.

        **参数解释**： 规则描述，用于描述规则的用途。 **约束限制**： 不涉及 **取值范围**： 长度在0-255之间 **默认取值**： 不涉及

        :param description: The description of this AddRuleAclDtoRules.
        :type description: str
        """
        self._description = description

    @property
    def direction(self):
        r"""Gets the direction of this AddRuleAclDtoRules.

        **参数解释**： 规则方向，用于指定规则是从云上至云下，还是云下至云上 **约束限制**： 当规则type=0（互联网规则）或者type= 2（NAT规则）时方向值必填 **取值范围**： 0表示外到内（云下到云上），1表示内到外（云上到云下）， **默认取值**： 不涉及

        :return: The direction of this AddRuleAclDtoRules.
        :rtype: int
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        r"""Sets the direction of this AddRuleAclDtoRules.

        **参数解释**： 规则方向，用于指定规则是从云上至云下，还是云下至云上 **约束限制**： 当规则type=0（互联网规则）或者type= 2（NAT规则）时方向值必填 **取值范围**： 0表示外到内（云下到云上），1表示内到外（云上到云下）， **默认取值**： 不涉及

        :param direction: The direction of this AddRuleAclDtoRules.
        :type direction: int
        """
        self._direction = direction

    @property
    def source(self):
        r"""Gets the source of this AddRuleAclDtoRules.

        :return: The source of this AddRuleAclDtoRules.
        :rtype: :class:`huaweicloudsdkcfw.v1.RuleAddressDtoForRequest`
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this AddRuleAclDtoRules.

        :param source: The source of this AddRuleAclDtoRules.
        :type source: :class:`huaweicloudsdkcfw.v1.RuleAddressDtoForRequest`
        """
        self._source = source

    @property
    def destination(self):
        r"""Gets the destination of this AddRuleAclDtoRules.

        :return: The destination of this AddRuleAclDtoRules.
        :rtype: :class:`huaweicloudsdkcfw.v1.RuleAddressDtoForRequest`
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        r"""Sets the destination of this AddRuleAclDtoRules.

        :param destination: The destination of this AddRuleAclDtoRules.
        :type destination: :class:`huaweicloudsdkcfw.v1.RuleAddressDtoForRequest`
        """
        self._destination = destination

    @property
    def service(self):
        r"""Gets the service of this AddRuleAclDtoRules.

        :return: The service of this AddRuleAclDtoRules.
        :rtype: :class:`huaweicloudsdkcfw.v1.RuleServiceDto`
        """
        return self._service

    @service.setter
    def service(self, service):
        r"""Sets the service of this AddRuleAclDtoRules.

        :param service: The service of this AddRuleAclDtoRules.
        :type service: :class:`huaweicloudsdkcfw.v1.RuleServiceDto`
        """
        self._service = service

    @property
    def tag(self):
        r"""Gets the tag of this AddRuleAclDtoRules.

        :return: The tag of this AddRuleAclDtoRules.
        :rtype: :class:`huaweicloudsdkcfw.v1.TagsVO`
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this AddRuleAclDtoRules.

        :param tag: The tag of this AddRuleAclDtoRules.
        :type tag: :class:`huaweicloudsdkcfw.v1.TagsVO`
        """
        self._tag = tag

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
        if not isinstance(other, AddRuleAclDtoRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
