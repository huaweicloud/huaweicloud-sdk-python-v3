# coding: utf-8

import six

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

        :param name: 规则名称
        :type name: str
        :param sequence: 
        :type sequence: :class:`huaweicloudsdkcfw.v1.OrderRuleAclDto`
        :param address_type: 地址类型，0表示ipv4，1表示ipv6
        :type address_type: int
        :param action_type: 规则动作，0表示允许通行（permit），1表示拒绝通行（deny）
        :type action_type: int
        :param status: 规则启用状态，0表示禁用，1表示启用
        :type status: int
        :param applications: 规则应用列表，规则应用类型包括：“HTTP”，\&quot;HTTPS\&quot;，\&quot;TLS1\&quot;，“DNS”，“SSH”，“MYSQL”，“SMTP”，“RDP”，“RDPS”，“VNC”，“POP3”，“IMAP4”，“SMTPS”，“POP3S”，“FTPS”，“ANY”，“BGP”等。
        :type applications: list[str]
        :param long_connect_time: 长连接时长
        :type long_connect_time: int
        :param long_connect_time_hour: 长连接时长对应小时
        :type long_connect_time_hour: int
        :param long_connect_time_minute: 长连接时长对应分钟
        :type long_connect_time_minute: int
        :param long_connect_time_second: 长连接时长秒
        :type long_connect_time_second: int
        :param long_connect_enable: 是否支持长连接，0表示不支持长连接，1表示支持长连接
        :type long_connect_enable: int
        :param description: 描述
        :type description: str
        :param direction: 方向：0表示外到内，1表示内到外，规则type&#x3D;0（互联网规则）或者type&#x3D; 2（nat规则）时方向值必填
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

        规则名称

        :return: The name of this AddRuleAclDtoRules.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AddRuleAclDtoRules.

        规则名称

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

        地址类型，0表示ipv4，1表示ipv6

        :return: The address_type of this AddRuleAclDtoRules.
        :rtype: int
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        r"""Sets the address_type of this AddRuleAclDtoRules.

        地址类型，0表示ipv4，1表示ipv6

        :param address_type: The address_type of this AddRuleAclDtoRules.
        :type address_type: int
        """
        self._address_type = address_type

    @property
    def action_type(self):
        r"""Gets the action_type of this AddRuleAclDtoRules.

        规则动作，0表示允许通行（permit），1表示拒绝通行（deny）

        :return: The action_type of this AddRuleAclDtoRules.
        :rtype: int
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        r"""Sets the action_type of this AddRuleAclDtoRules.

        规则动作，0表示允许通行（permit），1表示拒绝通行（deny）

        :param action_type: The action_type of this AddRuleAclDtoRules.
        :type action_type: int
        """
        self._action_type = action_type

    @property
    def status(self):
        r"""Gets the status of this AddRuleAclDtoRules.

        规则启用状态，0表示禁用，1表示启用

        :return: The status of this AddRuleAclDtoRules.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AddRuleAclDtoRules.

        规则启用状态，0表示禁用，1表示启用

        :param status: The status of this AddRuleAclDtoRules.
        :type status: int
        """
        self._status = status

    @property
    def applications(self):
        r"""Gets the applications of this AddRuleAclDtoRules.

        规则应用列表，规则应用类型包括：“HTTP”，\"HTTPS\"，\"TLS1\"，“DNS”，“SSH”，“MYSQL”，“SMTP”，“RDP”，“RDPS”，“VNC”，“POP3”，“IMAP4”，“SMTPS”，“POP3S”，“FTPS”，“ANY”，“BGP”等。

        :return: The applications of this AddRuleAclDtoRules.
        :rtype: list[str]
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        r"""Sets the applications of this AddRuleAclDtoRules.

        规则应用列表，规则应用类型包括：“HTTP”，\"HTTPS\"，\"TLS1\"，“DNS”，“SSH”，“MYSQL”，“SMTP”，“RDP”，“RDPS”，“VNC”，“POP3”，“IMAP4”，“SMTPS”，“POP3S”，“FTPS”，“ANY”，“BGP”等。

        :param applications: The applications of this AddRuleAclDtoRules.
        :type applications: list[str]
        """
        self._applications = applications

    @property
    def long_connect_time(self):
        r"""Gets the long_connect_time of this AddRuleAclDtoRules.

        长连接时长

        :return: The long_connect_time of this AddRuleAclDtoRules.
        :rtype: int
        """
        return self._long_connect_time

    @long_connect_time.setter
    def long_connect_time(self, long_connect_time):
        r"""Sets the long_connect_time of this AddRuleAclDtoRules.

        长连接时长

        :param long_connect_time: The long_connect_time of this AddRuleAclDtoRules.
        :type long_connect_time: int
        """
        self._long_connect_time = long_connect_time

    @property
    def long_connect_time_hour(self):
        r"""Gets the long_connect_time_hour of this AddRuleAclDtoRules.

        长连接时长对应小时

        :return: The long_connect_time_hour of this AddRuleAclDtoRules.
        :rtype: int
        """
        return self._long_connect_time_hour

    @long_connect_time_hour.setter
    def long_connect_time_hour(self, long_connect_time_hour):
        r"""Sets the long_connect_time_hour of this AddRuleAclDtoRules.

        长连接时长对应小时

        :param long_connect_time_hour: The long_connect_time_hour of this AddRuleAclDtoRules.
        :type long_connect_time_hour: int
        """
        self._long_connect_time_hour = long_connect_time_hour

    @property
    def long_connect_time_minute(self):
        r"""Gets the long_connect_time_minute of this AddRuleAclDtoRules.

        长连接时长对应分钟

        :return: The long_connect_time_minute of this AddRuleAclDtoRules.
        :rtype: int
        """
        return self._long_connect_time_minute

    @long_connect_time_minute.setter
    def long_connect_time_minute(self, long_connect_time_minute):
        r"""Sets the long_connect_time_minute of this AddRuleAclDtoRules.

        长连接时长对应分钟

        :param long_connect_time_minute: The long_connect_time_minute of this AddRuleAclDtoRules.
        :type long_connect_time_minute: int
        """
        self._long_connect_time_minute = long_connect_time_minute

    @property
    def long_connect_time_second(self):
        r"""Gets the long_connect_time_second of this AddRuleAclDtoRules.

        长连接时长秒

        :return: The long_connect_time_second of this AddRuleAclDtoRules.
        :rtype: int
        """
        return self._long_connect_time_second

    @long_connect_time_second.setter
    def long_connect_time_second(self, long_connect_time_second):
        r"""Sets the long_connect_time_second of this AddRuleAclDtoRules.

        长连接时长秒

        :param long_connect_time_second: The long_connect_time_second of this AddRuleAclDtoRules.
        :type long_connect_time_second: int
        """
        self._long_connect_time_second = long_connect_time_second

    @property
    def long_connect_enable(self):
        r"""Gets the long_connect_enable of this AddRuleAclDtoRules.

        是否支持长连接，0表示不支持长连接，1表示支持长连接

        :return: The long_connect_enable of this AddRuleAclDtoRules.
        :rtype: int
        """
        return self._long_connect_enable

    @long_connect_enable.setter
    def long_connect_enable(self, long_connect_enable):
        r"""Sets the long_connect_enable of this AddRuleAclDtoRules.

        是否支持长连接，0表示不支持长连接，1表示支持长连接

        :param long_connect_enable: The long_connect_enable of this AddRuleAclDtoRules.
        :type long_connect_enable: int
        """
        self._long_connect_enable = long_connect_enable

    @property
    def description(self):
        r"""Gets the description of this AddRuleAclDtoRules.

        描述

        :return: The description of this AddRuleAclDtoRules.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AddRuleAclDtoRules.

        描述

        :param description: The description of this AddRuleAclDtoRules.
        :type description: str
        """
        self._description = description

    @property
    def direction(self):
        r"""Gets the direction of this AddRuleAclDtoRules.

        方向：0表示外到内，1表示内到外，规则type=0（互联网规则）或者type= 2（nat规则）时方向值必填

        :return: The direction of this AddRuleAclDtoRules.
        :rtype: int
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        r"""Sets the direction of this AddRuleAclDtoRules.

        方向：0表示外到内，1表示内到外，规则type=0（互联网规则）或者type= 2（nat规则）时方向值必填

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
        if not isinstance(other, AddRuleAclDtoRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
