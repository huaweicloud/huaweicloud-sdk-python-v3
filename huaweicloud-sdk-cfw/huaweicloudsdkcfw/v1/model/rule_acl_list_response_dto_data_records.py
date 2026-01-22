# coding: utf-8

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
        'order_id': 'int',
        'applications': 'list[str]',
        'address_type': 'int',
        'name': 'str',
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
        'modified_date': 'str',
        'last_open_time': 'str',
        'tag': 'TagsVO'
    }

    attribute_map = {
        'rule_id': 'rule_id',
        'order_id': 'order_id',
        'applications': 'applications',
        'address_type': 'address_type',
        'name': 'name',
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
        'modified_date': 'modified_date',
        'last_open_time': 'last_open_time',
        'tag': 'tag'
    }

    def __init__(self, rule_id=None, order_id=None, applications=None, address_type=None, name=None, direction=None, action_type=None, status=None, description=None, long_connect_time=None, long_connect_enable=None, long_connect_time_hour=None, long_connect_time_minute=None, long_connect_time_second=None, source=None, destination=None, service=None, type=None, created_date=None, modified_date=None, last_open_time=None, tag=None):
        r"""RuleAclListResponseDTODataRecords

        The model defined in huaweicloud sdk

        :param rule_id: **参数解释**： 规则ID **取值范围**： 不涉及
        :type rule_id: str
        :param order_id: **参数解释**： 排序id **取值范围**： 不涉及
        :type order_id: int
        :param applications: **参数解释**： 应用列表 **取值范围**： 不涉及
        :type applications: list[str]
        :param address_type: 参数解释： IP地址的互联网协议类型，用于指定IP地址的互联网协议，由客户指定 约束限制： 不涉及 取值范围： 0：IPv4 1：IPv6 默认取值： 不涉及
        :type address_type: int
        :param name: **参数解释**： 规则名称 **取值范围**： 不涉及
        :type name: str
        :param direction: **参数解释**： 规则方向 **取值范围**： 0：外到内1：内到外
        :type direction: int
        :param action_type: **参数解释**： 规则动作类型，用于区分规则对流量的动作 **取值范围**： 0表示允许通行（permit），1表示拒绝通行（deny）
        :type action_type: int
        :param status: **参数解释**： 规则启用状态，用于区分规则是否启用 **取值范围**： 0表示启用，1表示禁用
        :type status: int
        :param description: **参数解释**： 规则描述，用于描述规则的用途。 **取值范围**： 不涉及
        :type description: str
        :param long_connect_time: **参数解释**： 长连接时长（s）。 **取值范围**： 1-86400000。
        :type long_connect_time: int
        :param long_connect_enable: **参数解释**： 用于表示是否支持长连接。 **取值范围**： 0表示不支持，1表示支持
        :type long_connect_enable: int
        :param long_connect_time_hour: **参数解释**： 长连接时长对应小时数（h）。 **取值范围**： 0-24000。
        :type long_connect_time_hour: int
        :param long_connect_time_minute: **参数解释**： 长连接时长对应分钟数（min）。 **取值范围**： 0-60。
        :type long_connect_time_minute: int
        :param long_connect_time_second: **参数解释**： 长连接时长对应秒数（s）。 **取值范围**： 0-60。
        :type long_connect_time_second: int
        :param source: 
        :type source: :class:`huaweicloudsdkcfw.v1.RuleAddressDtoForResponse`
        :param destination: 
        :type destination: :class:`huaweicloudsdkcfw.v1.RuleAddressDtoForResponse`
        :param service: 
        :type service: :class:`huaweicloudsdkcfw.v1.RuleServiceDtoForResponse`
        :param type: **参数解释**： 规则类型，用于区分不同防护对象设置规则类型。 **取值范围**：  0：互联网边界规则，源（source）和目的（destination）地址需要为公网IP或域名； 1：VPC间规则，源（source）和目的（destination）地址需要为私有ip； 2：NAT规则，源（source）地址需要为私网IP，目的地址为公网IP或域名。
        :type type: int
        :param created_date: **参数解释**： 规则创建时间。 **取值范围**： 不涉及
        :type created_date: str
        :param modified_date: **参数解释**： 规则修改时间。 **取值范围**： 不涉及
        :type modified_date: str
        :param last_open_time: **参数解释**： 规则最后开启时间。 **取值范围**： 不涉及
        :type last_open_time: str
        :param tag: 
        :type tag: :class:`huaweicloudsdkcfw.v1.TagsVO`
        """
        
        

        self._rule_id = None
        self._order_id = None
        self._applications = None
        self._address_type = None
        self._name = None
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
        self._modified_date = None
        self._last_open_time = None
        self._tag = None
        self.discriminator = None

        if rule_id is not None:
            self.rule_id = rule_id
        if order_id is not None:
            self.order_id = order_id
        if applications is not None:
            self.applications = applications
        if address_type is not None:
            self.address_type = address_type
        if name is not None:
            self.name = name
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
        if modified_date is not None:
            self.modified_date = modified_date
        if last_open_time is not None:
            self.last_open_time = last_open_time
        if tag is not None:
            self.tag = tag

    @property
    def rule_id(self):
        r"""Gets the rule_id of this RuleAclListResponseDTODataRecords.

        **参数解释**： 规则ID **取值范围**： 不涉及

        :return: The rule_id of this RuleAclListResponseDTODataRecords.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this RuleAclListResponseDTODataRecords.

        **参数解释**： 规则ID **取值范围**： 不涉及

        :param rule_id: The rule_id of this RuleAclListResponseDTODataRecords.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def order_id(self):
        r"""Gets the order_id of this RuleAclListResponseDTODataRecords.

        **参数解释**： 排序id **取值范围**： 不涉及

        :return: The order_id of this RuleAclListResponseDTODataRecords.
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this RuleAclListResponseDTODataRecords.

        **参数解释**： 排序id **取值范围**： 不涉及

        :param order_id: The order_id of this RuleAclListResponseDTODataRecords.
        :type order_id: int
        """
        self._order_id = order_id

    @property
    def applications(self):
        r"""Gets the applications of this RuleAclListResponseDTODataRecords.

        **参数解释**： 应用列表 **取值范围**： 不涉及

        :return: The applications of this RuleAclListResponseDTODataRecords.
        :rtype: list[str]
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        r"""Sets the applications of this RuleAclListResponseDTODataRecords.

        **参数解释**： 应用列表 **取值范围**： 不涉及

        :param applications: The applications of this RuleAclListResponseDTODataRecords.
        :type applications: list[str]
        """
        self._applications = applications

    @property
    def address_type(self):
        r"""Gets the address_type of this RuleAclListResponseDTODataRecords.

        参数解释： IP地址的互联网协议类型，用于指定IP地址的互联网协议，由客户指定 约束限制： 不涉及 取值范围： 0：IPv4 1：IPv6 默认取值： 不涉及

        :return: The address_type of this RuleAclListResponseDTODataRecords.
        :rtype: int
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        r"""Sets the address_type of this RuleAclListResponseDTODataRecords.

        参数解释： IP地址的互联网协议类型，用于指定IP地址的互联网协议，由客户指定 约束限制： 不涉及 取值范围： 0：IPv4 1：IPv6 默认取值： 不涉及

        :param address_type: The address_type of this RuleAclListResponseDTODataRecords.
        :type address_type: int
        """
        self._address_type = address_type

    @property
    def name(self):
        r"""Gets the name of this RuleAclListResponseDTODataRecords.

        **参数解释**： 规则名称 **取值范围**： 不涉及

        :return: The name of this RuleAclListResponseDTODataRecords.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RuleAclListResponseDTODataRecords.

        **参数解释**： 规则名称 **取值范围**： 不涉及

        :param name: The name of this RuleAclListResponseDTODataRecords.
        :type name: str
        """
        self._name = name

    @property
    def direction(self):
        r"""Gets the direction of this RuleAclListResponseDTODataRecords.

        **参数解释**： 规则方向 **取值范围**： 0：外到内1：内到外

        :return: The direction of this RuleAclListResponseDTODataRecords.
        :rtype: int
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        r"""Sets the direction of this RuleAclListResponseDTODataRecords.

        **参数解释**： 规则方向 **取值范围**： 0：外到内1：内到外

        :param direction: The direction of this RuleAclListResponseDTODataRecords.
        :type direction: int
        """
        self._direction = direction

    @property
    def action_type(self):
        r"""Gets the action_type of this RuleAclListResponseDTODataRecords.

        **参数解释**： 规则动作类型，用于区分规则对流量的动作 **取值范围**： 0表示允许通行（permit），1表示拒绝通行（deny）

        :return: The action_type of this RuleAclListResponseDTODataRecords.
        :rtype: int
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        r"""Sets the action_type of this RuleAclListResponseDTODataRecords.

        **参数解释**： 规则动作类型，用于区分规则对流量的动作 **取值范围**： 0表示允许通行（permit），1表示拒绝通行（deny）

        :param action_type: The action_type of this RuleAclListResponseDTODataRecords.
        :type action_type: int
        """
        self._action_type = action_type

    @property
    def status(self):
        r"""Gets the status of this RuleAclListResponseDTODataRecords.

        **参数解释**： 规则启用状态，用于区分规则是否启用 **取值范围**： 0表示启用，1表示禁用

        :return: The status of this RuleAclListResponseDTODataRecords.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RuleAclListResponseDTODataRecords.

        **参数解释**： 规则启用状态，用于区分规则是否启用 **取值范围**： 0表示启用，1表示禁用

        :param status: The status of this RuleAclListResponseDTODataRecords.
        :type status: int
        """
        self._status = status

    @property
    def description(self):
        r"""Gets the description of this RuleAclListResponseDTODataRecords.

        **参数解释**： 规则描述，用于描述规则的用途。 **取值范围**： 不涉及

        :return: The description of this RuleAclListResponseDTODataRecords.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RuleAclListResponseDTODataRecords.

        **参数解释**： 规则描述，用于描述规则的用途。 **取值范围**： 不涉及

        :param description: The description of this RuleAclListResponseDTODataRecords.
        :type description: str
        """
        self._description = description

    @property
    def long_connect_time(self):
        r"""Gets the long_connect_time of this RuleAclListResponseDTODataRecords.

        **参数解释**： 长连接时长（s）。 **取值范围**： 1-86400000。

        :return: The long_connect_time of this RuleAclListResponseDTODataRecords.
        :rtype: int
        """
        return self._long_connect_time

    @long_connect_time.setter
    def long_connect_time(self, long_connect_time):
        r"""Sets the long_connect_time of this RuleAclListResponseDTODataRecords.

        **参数解释**： 长连接时长（s）。 **取值范围**： 1-86400000。

        :param long_connect_time: The long_connect_time of this RuleAclListResponseDTODataRecords.
        :type long_connect_time: int
        """
        self._long_connect_time = long_connect_time

    @property
    def long_connect_enable(self):
        r"""Gets the long_connect_enable of this RuleAclListResponseDTODataRecords.

        **参数解释**： 用于表示是否支持长连接。 **取值范围**： 0表示不支持，1表示支持

        :return: The long_connect_enable of this RuleAclListResponseDTODataRecords.
        :rtype: int
        """
        return self._long_connect_enable

    @long_connect_enable.setter
    def long_connect_enable(self, long_connect_enable):
        r"""Sets the long_connect_enable of this RuleAclListResponseDTODataRecords.

        **参数解释**： 用于表示是否支持长连接。 **取值范围**： 0表示不支持，1表示支持

        :param long_connect_enable: The long_connect_enable of this RuleAclListResponseDTODataRecords.
        :type long_connect_enable: int
        """
        self._long_connect_enable = long_connect_enable

    @property
    def long_connect_time_hour(self):
        r"""Gets the long_connect_time_hour of this RuleAclListResponseDTODataRecords.

        **参数解释**： 长连接时长对应小时数（h）。 **取值范围**： 0-24000。

        :return: The long_connect_time_hour of this RuleAclListResponseDTODataRecords.
        :rtype: int
        """
        return self._long_connect_time_hour

    @long_connect_time_hour.setter
    def long_connect_time_hour(self, long_connect_time_hour):
        r"""Sets the long_connect_time_hour of this RuleAclListResponseDTODataRecords.

        **参数解释**： 长连接时长对应小时数（h）。 **取值范围**： 0-24000。

        :param long_connect_time_hour: The long_connect_time_hour of this RuleAclListResponseDTODataRecords.
        :type long_connect_time_hour: int
        """
        self._long_connect_time_hour = long_connect_time_hour

    @property
    def long_connect_time_minute(self):
        r"""Gets the long_connect_time_minute of this RuleAclListResponseDTODataRecords.

        **参数解释**： 长连接时长对应分钟数（min）。 **取值范围**： 0-60。

        :return: The long_connect_time_minute of this RuleAclListResponseDTODataRecords.
        :rtype: int
        """
        return self._long_connect_time_minute

    @long_connect_time_minute.setter
    def long_connect_time_minute(self, long_connect_time_minute):
        r"""Sets the long_connect_time_minute of this RuleAclListResponseDTODataRecords.

        **参数解释**： 长连接时长对应分钟数（min）。 **取值范围**： 0-60。

        :param long_connect_time_minute: The long_connect_time_minute of this RuleAclListResponseDTODataRecords.
        :type long_connect_time_minute: int
        """
        self._long_connect_time_minute = long_connect_time_minute

    @property
    def long_connect_time_second(self):
        r"""Gets the long_connect_time_second of this RuleAclListResponseDTODataRecords.

        **参数解释**： 长连接时长对应秒数（s）。 **取值范围**： 0-60。

        :return: The long_connect_time_second of this RuleAclListResponseDTODataRecords.
        :rtype: int
        """
        return self._long_connect_time_second

    @long_connect_time_second.setter
    def long_connect_time_second(self, long_connect_time_second):
        r"""Sets the long_connect_time_second of this RuleAclListResponseDTODataRecords.

        **参数解释**： 长连接时长对应秒数（s）。 **取值范围**： 0-60。

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

        **参数解释**： 规则类型，用于区分不同防护对象设置规则类型。 **取值范围**：  0：互联网边界规则，源（source）和目的（destination）地址需要为公网IP或域名； 1：VPC间规则，源（source）和目的（destination）地址需要为私有ip； 2：NAT规则，源（source）地址需要为私网IP，目的地址为公网IP或域名。

        :return: The type of this RuleAclListResponseDTODataRecords.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RuleAclListResponseDTODataRecords.

        **参数解释**： 规则类型，用于区分不同防护对象设置规则类型。 **取值范围**：  0：互联网边界规则，源（source）和目的（destination）地址需要为公网IP或域名； 1：VPC间规则，源（source）和目的（destination）地址需要为私有ip； 2：NAT规则，源（source）地址需要为私网IP，目的地址为公网IP或域名。

        :param type: The type of this RuleAclListResponseDTODataRecords.
        :type type: int
        """
        self._type = type

    @property
    def created_date(self):
        r"""Gets the created_date of this RuleAclListResponseDTODataRecords.

        **参数解释**： 规则创建时间。 **取值范围**： 不涉及

        :return: The created_date of this RuleAclListResponseDTODataRecords.
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this RuleAclListResponseDTODataRecords.

        **参数解释**： 规则创建时间。 **取值范围**： 不涉及

        :param created_date: The created_date of this RuleAclListResponseDTODataRecords.
        :type created_date: str
        """
        self._created_date = created_date

    @property
    def modified_date(self):
        r"""Gets the modified_date of this RuleAclListResponseDTODataRecords.

        **参数解释**： 规则修改时间。 **取值范围**： 不涉及

        :return: The modified_date of this RuleAclListResponseDTODataRecords.
        :rtype: str
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        r"""Sets the modified_date of this RuleAclListResponseDTODataRecords.

        **参数解释**： 规则修改时间。 **取值范围**： 不涉及

        :param modified_date: The modified_date of this RuleAclListResponseDTODataRecords.
        :type modified_date: str
        """
        self._modified_date = modified_date

    @property
    def last_open_time(self):
        r"""Gets the last_open_time of this RuleAclListResponseDTODataRecords.

        **参数解释**： 规则最后开启时间。 **取值范围**： 不涉及

        :return: The last_open_time of this RuleAclListResponseDTODataRecords.
        :rtype: str
        """
        return self._last_open_time

    @last_open_time.setter
    def last_open_time(self, last_open_time):
        r"""Sets the last_open_time of this RuleAclListResponseDTODataRecords.

        **参数解释**： 规则最后开启时间。 **取值范围**： 不涉及

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
        if not isinstance(other, RuleAclListResponseDTODataRecords):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
