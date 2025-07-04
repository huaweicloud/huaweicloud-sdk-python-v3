# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleAclListResponseDTODataRecords:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_id': 'str',
        'applications': 'list[str]',
        'address_type': 'int',
        'name': 'str',
        'order_id': 'int',
        'direction': 'int',
        'action_type': 'int',
        'status': 'int',
        'description': 'str',
        'long_connect_time': 'int',
        'long_connect_enable': 'int',
        'long_connect_time_hour': 'int',
        'long_connect_time_minute': 'int',
        'long_connect_time_second': 'int',
        'source': 'RuleAddressDtoForResponse',
        'destination': 'RuleAddressDtoForResponse',
        'service': 'RuleServiceDtoForResponse',
        'type': 'int',
        'created_date': 'str',
        'last_open_time': 'str',
        'tag': 'TagsVO'
    }

    attribute_map = {
        'rule_id': 'rule_id',
        'applications': 'applications',
        'address_type': 'address_type',
        'name': 'name',
        'order_id': 'order_id',
        'direction': 'direction',
        'action_type': 'action_type',
        'status': 'status',
        'description': 'description',
        'long_connect_time': 'long_connect_time',
        'long_connect_enable': 'long_connect_enable',
        'long_connect_time_hour': 'long_connect_time_hour',
        'long_connect_time_minute': 'long_connect_time_minute',
        'long_connect_time_second': 'long_connect_time_second',
        'source': 'source',
        'destination': 'destination',
        'service': 'service',
        'type': 'type',
        'created_date': 'created_date',
        'last_open_time': 'last_open_time',
        'tag': 'tag'
    }

    def __init__(self, rule_id=None, applications=None, address_type=None, name=None, order_id=None, direction=None, action_type=None, status=None, description=None, long_connect_time=None, long_connect_enable=None, long_connect_time_hour=None, long_connect_time_minute=None, long_connect_time_second=None, source=None, destination=None, service=None, type=None, created_date=None, last_open_time=None, tag=None):
        r"""RuleAclListResponseDTODataRecords

        The model defined in huaweicloud sdk

        :param rule_id: 规则id
        :type rule_id: str
        :param applications: 应用列表
        :type applications: list[str]
        :param address_type: 地址类型0 ipv4，1 ipv6
        :type address_type: int
        :param name: 规则名称
        :type name: str
        :param order_id: 排序id
        :type order_id: int
        :param direction: 规则方向0：外到内1：内到外
        :type direction: int
        :param action_type: 动作0：permit，1：deny
        :type action_type: int
        :param status: 规则下发状态 0：禁用，1：启用
        :type status: int
        :param description: 描述
        :type description: str
        :param long_connect_time: 长连接时长
        :type long_connect_time: int
        :param long_connect_enable: 长连接支持
        :type long_connect_enable: int
        :param long_connect_time_hour: 长连接时长对应小时
        :type long_connect_time_hour: int
        :param long_connect_time_minute: 长连接时长对应分钟
        :type long_connect_time_minute: int
        :param long_connect_time_second: 长连接时长秒
        :type long_connect_time_second: int
        :param source: 
        :type source: :class:`huaweicloudsdkcfw.v1.RuleAddressDtoForResponse`
        :param destination: 
        :type destination: :class:`huaweicloudsdkcfw.v1.RuleAddressDtoForResponse`
        :param service: 
        :type service: :class:`huaweicloudsdkcfw.v1.RuleServiceDtoForResponse`
        :param type: 规则类型，0：互联网规则，1：vpc规则，2：nat规则
        :type type: int
        :param created_date: 规则创建时间，例如：\&quot;2024-08-12 08:40:00\&quot;
        :type created_date: str
        :param last_open_time: 规则最后开启时间，例如：\&quot;2024-08-12 08:40:00\&quot;
        :type last_open_time: str
        :param tag: 
        :type tag: :class:`huaweicloudsdkcfw.v1.TagsVO`
        """
        
        

        self._rule_id = None
        self._applications = None
        self._address_type = None
        self._name = None
        self._order_id = None
        self._direction = None
        self._action_type = None
        self._status = None
        self._description = None
        self._long_connect_time = None
        self._long_connect_enable = None
        self._long_connect_time_hour = None
        self._long_connect_time_minute = None
        self._long_connect_time_second = None
        self._source = None
        self._destination = None
        self._service = None
        self._type = None
        self._created_date = None
        self._last_open_time = None
        self._tag = None
        self.discriminator = None

        if rule_id is not None:
            self.rule_id = rule_id
        if applications is not None:
            self.applications = applications
        if address_type is not None:
            self.address_type = address_type
        if name is not None:
            self.name = name
        if order_id is not None:
            self.order_id = order_id
        if direction is not None:
            self.direction = direction
        if action_type is not None:
            self.action_type = action_type
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description
        if long_connect_time is not None:
            self.long_connect_time = long_connect_time
        if long_connect_enable is not None:
            self.long_connect_enable = long_connect_enable
        if long_connect_time_hour is not None:
            self.long_connect_time_hour = long_connect_time_hour
        if long_connect_time_minute is not None:
            self.long_connect_time_minute = long_connect_time_minute
        if long_connect_time_second is not None:
            self.long_connect_time_second = long_connect_time_second
        if source is not None:
            self.source = source
        if destination is not None:
            self.destination = destination
        if service is not None:
            self.service = service
        if type is not None:
            self.type = type
        if created_date is not None:
            self.created_date = created_date
        if last_open_time is not None:
            self.last_open_time = last_open_time
        if tag is not None:
            self.tag = tag

    @property
    def rule_id(self):
        r"""Gets the rule_id of this RuleAclListResponseDTODataRecords.

        规则id

        :return: The rule_id of this RuleAclListResponseDTODataRecords.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this RuleAclListResponseDTODataRecords.

        规则id

        :param rule_id: The rule_id of this RuleAclListResponseDTODataRecords.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def applications(self):
        r"""Gets the applications of this RuleAclListResponseDTODataRecords.

        应用列表

        :return: The applications of this RuleAclListResponseDTODataRecords.
        :rtype: list[str]
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        r"""Sets the applications of this RuleAclListResponseDTODataRecords.

        应用列表

        :param applications: The applications of this RuleAclListResponseDTODataRecords.
        :type applications: list[str]
        """
        self._applications = applications

    @property
    def address_type(self):
        r"""Gets the address_type of this RuleAclListResponseDTODataRecords.

        地址类型0 ipv4，1 ipv6

        :return: The address_type of this RuleAclListResponseDTODataRecords.
        :rtype: int
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        r"""Sets the address_type of this RuleAclListResponseDTODataRecords.

        地址类型0 ipv4，1 ipv6

        :param address_type: The address_type of this RuleAclListResponseDTODataRecords.
        :type address_type: int
        """
        self._address_type = address_type

    @property
    def name(self):
        r"""Gets the name of this RuleAclListResponseDTODataRecords.

        规则名称

        :return: The name of this RuleAclListResponseDTODataRecords.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RuleAclListResponseDTODataRecords.

        规则名称

        :param name: The name of this RuleAclListResponseDTODataRecords.
        :type name: str
        """
        self._name = name

    @property
    def order_id(self):
        r"""Gets the order_id of this RuleAclListResponseDTODataRecords.

        排序id

        :return: The order_id of this RuleAclListResponseDTODataRecords.
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this RuleAclListResponseDTODataRecords.

        排序id

        :param order_id: The order_id of this RuleAclListResponseDTODataRecords.
        :type order_id: int
        """
        self._order_id = order_id

    @property
    def direction(self):
        r"""Gets the direction of this RuleAclListResponseDTODataRecords.

        规则方向0：外到内1：内到外

        :return: The direction of this RuleAclListResponseDTODataRecords.
        :rtype: int
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        r"""Sets the direction of this RuleAclListResponseDTODataRecords.

        规则方向0：外到内1：内到外

        :param direction: The direction of this RuleAclListResponseDTODataRecords.
        :type direction: int
        """
        self._direction = direction

    @property
    def action_type(self):
        r"""Gets the action_type of this RuleAclListResponseDTODataRecords.

        动作0：permit，1：deny

        :return: The action_type of this RuleAclListResponseDTODataRecords.
        :rtype: int
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        r"""Sets the action_type of this RuleAclListResponseDTODataRecords.

        动作0：permit，1：deny

        :param action_type: The action_type of this RuleAclListResponseDTODataRecords.
        :type action_type: int
        """
        self._action_type = action_type

    @property
    def status(self):
        r"""Gets the status of this RuleAclListResponseDTODataRecords.

        规则下发状态 0：禁用，1：启用

        :return: The status of this RuleAclListResponseDTODataRecords.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RuleAclListResponseDTODataRecords.

        规则下发状态 0：禁用，1：启用

        :param status: The status of this RuleAclListResponseDTODataRecords.
        :type status: int
        """
        self._status = status

    @property
    def description(self):
        r"""Gets the description of this RuleAclListResponseDTODataRecords.

        描述

        :return: The description of this RuleAclListResponseDTODataRecords.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RuleAclListResponseDTODataRecords.

        描述

        :param description: The description of this RuleAclListResponseDTODataRecords.
        :type description: str
        """
        self._description = description

    @property
    def long_connect_time(self):
        r"""Gets the long_connect_time of this RuleAclListResponseDTODataRecords.

        长连接时长

        :return: The long_connect_time of this RuleAclListResponseDTODataRecords.
        :rtype: int
        """
        return self._long_connect_time

    @long_connect_time.setter
    def long_connect_time(self, long_connect_time):
        r"""Sets the long_connect_time of this RuleAclListResponseDTODataRecords.

        长连接时长

        :param long_connect_time: The long_connect_time of this RuleAclListResponseDTODataRecords.
        :type long_connect_time: int
        """
        self._long_connect_time = long_connect_time

    @property
    def long_connect_enable(self):
        r"""Gets the long_connect_enable of this RuleAclListResponseDTODataRecords.

        长连接支持

        :return: The long_connect_enable of this RuleAclListResponseDTODataRecords.
        :rtype: int
        """
        return self._long_connect_enable

    @long_connect_enable.setter
    def long_connect_enable(self, long_connect_enable):
        r"""Sets the long_connect_enable of this RuleAclListResponseDTODataRecords.

        长连接支持

        :param long_connect_enable: The long_connect_enable of this RuleAclListResponseDTODataRecords.
        :type long_connect_enable: int
        """
        self._long_connect_enable = long_connect_enable

    @property
    def long_connect_time_hour(self):
        r"""Gets the long_connect_time_hour of this RuleAclListResponseDTODataRecords.

        长连接时长对应小时

        :return: The long_connect_time_hour of this RuleAclListResponseDTODataRecords.
        :rtype: int
        """
        return self._long_connect_time_hour

    @long_connect_time_hour.setter
    def long_connect_time_hour(self, long_connect_time_hour):
        r"""Sets the long_connect_time_hour of this RuleAclListResponseDTODataRecords.

        长连接时长对应小时

        :param long_connect_time_hour: The long_connect_time_hour of this RuleAclListResponseDTODataRecords.
        :type long_connect_time_hour: int
        """
        self._long_connect_time_hour = long_connect_time_hour

    @property
    def long_connect_time_minute(self):
        r"""Gets the long_connect_time_minute of this RuleAclListResponseDTODataRecords.

        长连接时长对应分钟

        :return: The long_connect_time_minute of this RuleAclListResponseDTODataRecords.
        :rtype: int
        """
        return self._long_connect_time_minute

    @long_connect_time_minute.setter
    def long_connect_time_minute(self, long_connect_time_minute):
        r"""Sets the long_connect_time_minute of this RuleAclListResponseDTODataRecords.

        长连接时长对应分钟

        :param long_connect_time_minute: The long_connect_time_minute of this RuleAclListResponseDTODataRecords.
        :type long_connect_time_minute: int
        """
        self._long_connect_time_minute = long_connect_time_minute

    @property
    def long_connect_time_second(self):
        r"""Gets the long_connect_time_second of this RuleAclListResponseDTODataRecords.

        长连接时长秒

        :return: The long_connect_time_second of this RuleAclListResponseDTODataRecords.
        :rtype: int
        """
        return self._long_connect_time_second

    @long_connect_time_second.setter
    def long_connect_time_second(self, long_connect_time_second):
        r"""Sets the long_connect_time_second of this RuleAclListResponseDTODataRecords.

        长连接时长秒

        :param long_connect_time_second: The long_connect_time_second of this RuleAclListResponseDTODataRecords.
        :type long_connect_time_second: int
        """
        self._long_connect_time_second = long_connect_time_second

    @property
    def source(self):
        r"""Gets the source of this RuleAclListResponseDTODataRecords.

        :return: The source of this RuleAclListResponseDTODataRecords.
        :rtype: :class:`huaweicloudsdkcfw.v1.RuleAddressDtoForResponse`
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this RuleAclListResponseDTODataRecords.

        :param source: The source of this RuleAclListResponseDTODataRecords.
        :type source: :class:`huaweicloudsdkcfw.v1.RuleAddressDtoForResponse`
        """
        self._source = source

    @property
    def destination(self):
        r"""Gets the destination of this RuleAclListResponseDTODataRecords.

        :return: The destination of this RuleAclListResponseDTODataRecords.
        :rtype: :class:`huaweicloudsdkcfw.v1.RuleAddressDtoForResponse`
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        r"""Sets the destination of this RuleAclListResponseDTODataRecords.

        :param destination: The destination of this RuleAclListResponseDTODataRecords.
        :type destination: :class:`huaweicloudsdkcfw.v1.RuleAddressDtoForResponse`
        """
        self._destination = destination

    @property
    def service(self):
        r"""Gets the service of this RuleAclListResponseDTODataRecords.

        :return: The service of this RuleAclListResponseDTODataRecords.
        :rtype: :class:`huaweicloudsdkcfw.v1.RuleServiceDtoForResponse`
        """
        return self._service

    @service.setter
    def service(self, service):
        r"""Sets the service of this RuleAclListResponseDTODataRecords.

        :param service: The service of this RuleAclListResponseDTODataRecords.
        :type service: :class:`huaweicloudsdkcfw.v1.RuleServiceDtoForResponse`
        """
        self._service = service

    @property
    def type(self):
        r"""Gets the type of this RuleAclListResponseDTODataRecords.

        规则类型，0：互联网规则，1：vpc规则，2：nat规则

        :return: The type of this RuleAclListResponseDTODataRecords.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RuleAclListResponseDTODataRecords.

        规则类型，0：互联网规则，1：vpc规则，2：nat规则

        :param type: The type of this RuleAclListResponseDTODataRecords.
        :type type: int
        """
        self._type = type

    @property
    def created_date(self):
        r"""Gets the created_date of this RuleAclListResponseDTODataRecords.

        规则创建时间，例如：\"2024-08-12 08:40:00\"

        :return: The created_date of this RuleAclListResponseDTODataRecords.
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this RuleAclListResponseDTODataRecords.

        规则创建时间，例如：\"2024-08-12 08:40:00\"

        :param created_date: The created_date of this RuleAclListResponseDTODataRecords.
        :type created_date: str
        """
        self._created_date = created_date

    @property
    def last_open_time(self):
        r"""Gets the last_open_time of this RuleAclListResponseDTODataRecords.

        规则最后开启时间，例如：\"2024-08-12 08:40:00\"

        :return: The last_open_time of this RuleAclListResponseDTODataRecords.
        :rtype: str
        """
        return self._last_open_time

    @last_open_time.setter
    def last_open_time(self, last_open_time):
        r"""Sets the last_open_time of this RuleAclListResponseDTODataRecords.

        规则最后开启时间，例如：\"2024-08-12 08:40:00\"

        :param last_open_time: The last_open_time of this RuleAclListResponseDTODataRecords.
        :type last_open_time: str
        """
        self._last_open_time = last_open_time

    @property
    def tag(self):
        r"""Gets the tag of this RuleAclListResponseDTODataRecords.

        :return: The tag of this RuleAclListResponseDTODataRecords.
        :rtype: :class:`huaweicloudsdkcfw.v1.TagsVO`
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this RuleAclListResponseDTODataRecords.

        :param tag: The tag of this RuleAclListResponseDTODataRecords.
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
        if not isinstance(other, RuleAclListResponseDTODataRecords):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
