# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountOtherResourceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_delegated': 'bool',
        'type': 'str',
        'is_delegate_domain': 'bool',
        'name_list': 'list[str]',
        'region_id': 'str',
        'create_since': 'str',
        'create_until': 'str',
        'ip': 'str',
        'os_type': 'str',
        'os_version_list': 'str',
        'agent_state': 'str'
    }

    attribute_map = {
        'is_delegated': 'is_delegated',
        'type': 'type',
        'is_delegate_domain': 'is_delegate_domain',
        'name_list': 'name_list',
        'region_id': 'region_id',
        'create_since': 'create_since',
        'create_until': 'create_until',
        'ip': 'ip',
        'os_type': 'os_type',
        'os_version_list': 'os_version_list',
        'agent_state': 'agent_state'
    }

    def __init__(self, is_delegated=None, type=None, is_delegate_domain=None, name_list=None, region_id=None, create_since=None, create_until=None, ip=None, os_type=None, os_version_list=None, agent_state=None):
        r"""CountOtherResourceRequest

        The model defined in huaweicloud sdk

        :param is_delegated: **参数解释：** 是否已托管。 **约束限制：** 不涉及。 **取值范围：** - true：已经托管。 - false：未托管。 **默认取值：** 不涉及。
        :type is_delegated: bool
        :param type: **参数解释：** 资源类型。 **约束限制：** 不涉及。 **取值范围：** - vm：虚拟机。 - PM：物理机。 - Middleware：中间件设备。 **默认取值：** 不涉及。
        :type type: str
        :param is_delegate_domain: **参数解释：** 是否为sre。 **约束限制：** 不涉及。 **取值范围：** - true：是sre。 - false：非sre。 **默认取值：** 不涉及。
        :type is_delegate_domain: bool
        :param name_list: **参数解释：** 资源名称，支持模糊查询。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type name_list: list[str]
        :param region_id: **参数解释：** 区域id。 **约束限制：** 不涉及。 **取值范围：** 关联的区域region的id。 **默认取值：** 不涉及。
        :type region_id: str
        :param create_since: **参数解释：** 创建时间中的开始日期，参考ISO8601标准格式。 **约束限制：** 开始日期和结束日期，至少有一个日期存在。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type create_since: str
        :param create_until: **参数解释：** 创建时间中的结束日期，参考ISO8601标准格式。 **约束限制：** 开始日期和结束日期，至少有一个日期存在。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type create_until: str
        :param ip: **参数解释：** 私有ip。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type ip: str
        :param os_type: **参数解释：** 操作系统。 **约束限制：** 不涉及。 **取值范围：** - windows：windows操作系统类型。 - linux：linux操作系统类型。 **默认取值：** 不涉及。
        :type os_type: str
        :param os_version_list: **参数解释：** OS版本。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type os_version_list: str
        :param agent_state: **参数解释：** agent状态。 **约束限制：** 不涉及。 **取值范围：** - ONLINE：运行中。 - OFFLINE：异常。 - INSTALLING：安装中。 - FAILED：安装失败。 - UNINSTALLED：已卸载。 - null：未安装。 **默认取值：** 不涉及。
        :type agent_state: str
        """
        
        

        self._is_delegated = None
        self._type = None
        self._is_delegate_domain = None
        self._name_list = None
        self._region_id = None
        self._create_since = None
        self._create_until = None
        self._ip = None
        self._os_type = None
        self._os_version_list = None
        self._agent_state = None
        self.discriminator = None

        if is_delegated is not None:
            self.is_delegated = is_delegated
        if type is not None:
            self.type = type
        if is_delegate_domain is not None:
            self.is_delegate_domain = is_delegate_domain
        if name_list is not None:
            self.name_list = name_list
        if region_id is not None:
            self.region_id = region_id
        if create_since is not None:
            self.create_since = create_since
        if create_until is not None:
            self.create_until = create_until
        if ip is not None:
            self.ip = ip
        if os_type is not None:
            self.os_type = os_type
        if os_version_list is not None:
            self.os_version_list = os_version_list
        if agent_state is not None:
            self.agent_state = agent_state

    @property
    def is_delegated(self):
        r"""Gets the is_delegated of this CountOtherResourceRequest.

        **参数解释：** 是否已托管。 **约束限制：** 不涉及。 **取值范围：** - true：已经托管。 - false：未托管。 **默认取值：** 不涉及。

        :return: The is_delegated of this CountOtherResourceRequest.
        :rtype: bool
        """
        return self._is_delegated

    @is_delegated.setter
    def is_delegated(self, is_delegated):
        r"""Sets the is_delegated of this CountOtherResourceRequest.

        **参数解释：** 是否已托管。 **约束限制：** 不涉及。 **取值范围：** - true：已经托管。 - false：未托管。 **默认取值：** 不涉及。

        :param is_delegated: The is_delegated of this CountOtherResourceRequest.
        :type is_delegated: bool
        """
        self._is_delegated = is_delegated

    @property
    def type(self):
        r"""Gets the type of this CountOtherResourceRequest.

        **参数解释：** 资源类型。 **约束限制：** 不涉及。 **取值范围：** - vm：虚拟机。 - PM：物理机。 - Middleware：中间件设备。 **默认取值：** 不涉及。

        :return: The type of this CountOtherResourceRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CountOtherResourceRequest.

        **参数解释：** 资源类型。 **约束限制：** 不涉及。 **取值范围：** - vm：虚拟机。 - PM：物理机。 - Middleware：中间件设备。 **默认取值：** 不涉及。

        :param type: The type of this CountOtherResourceRequest.
        :type type: str
        """
        self._type = type

    @property
    def is_delegate_domain(self):
        r"""Gets the is_delegate_domain of this CountOtherResourceRequest.

        **参数解释：** 是否为sre。 **约束限制：** 不涉及。 **取值范围：** - true：是sre。 - false：非sre。 **默认取值：** 不涉及。

        :return: The is_delegate_domain of this CountOtherResourceRequest.
        :rtype: bool
        """
        return self._is_delegate_domain

    @is_delegate_domain.setter
    def is_delegate_domain(self, is_delegate_domain):
        r"""Sets the is_delegate_domain of this CountOtherResourceRequest.

        **参数解释：** 是否为sre。 **约束限制：** 不涉及。 **取值范围：** - true：是sre。 - false：非sre。 **默认取值：** 不涉及。

        :param is_delegate_domain: The is_delegate_domain of this CountOtherResourceRequest.
        :type is_delegate_domain: bool
        """
        self._is_delegate_domain = is_delegate_domain

    @property
    def name_list(self):
        r"""Gets the name_list of this CountOtherResourceRequest.

        **参数解释：** 资源名称，支持模糊查询。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The name_list of this CountOtherResourceRequest.
        :rtype: list[str]
        """
        return self._name_list

    @name_list.setter
    def name_list(self, name_list):
        r"""Sets the name_list of this CountOtherResourceRequest.

        **参数解释：** 资源名称，支持模糊查询。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param name_list: The name_list of this CountOtherResourceRequest.
        :type name_list: list[str]
        """
        self._name_list = name_list

    @property
    def region_id(self):
        r"""Gets the region_id of this CountOtherResourceRequest.

        **参数解释：** 区域id。 **约束限制：** 不涉及。 **取值范围：** 关联的区域region的id。 **默认取值：** 不涉及。

        :return: The region_id of this CountOtherResourceRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this CountOtherResourceRequest.

        **参数解释：** 区域id。 **约束限制：** 不涉及。 **取值范围：** 关联的区域region的id。 **默认取值：** 不涉及。

        :param region_id: The region_id of this CountOtherResourceRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def create_since(self):
        r"""Gets the create_since of this CountOtherResourceRequest.

        **参数解释：** 创建时间中的开始日期，参考ISO8601标准格式。 **约束限制：** 开始日期和结束日期，至少有一个日期存在。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The create_since of this CountOtherResourceRequest.
        :rtype: str
        """
        return self._create_since

    @create_since.setter
    def create_since(self, create_since):
        r"""Sets the create_since of this CountOtherResourceRequest.

        **参数解释：** 创建时间中的开始日期，参考ISO8601标准格式。 **约束限制：** 开始日期和结束日期，至少有一个日期存在。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param create_since: The create_since of this CountOtherResourceRequest.
        :type create_since: str
        """
        self._create_since = create_since

    @property
    def create_until(self):
        r"""Gets the create_until of this CountOtherResourceRequest.

        **参数解释：** 创建时间中的结束日期，参考ISO8601标准格式。 **约束限制：** 开始日期和结束日期，至少有一个日期存在。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The create_until of this CountOtherResourceRequest.
        :rtype: str
        """
        return self._create_until

    @create_until.setter
    def create_until(self, create_until):
        r"""Sets the create_until of this CountOtherResourceRequest.

        **参数解释：** 创建时间中的结束日期，参考ISO8601标准格式。 **约束限制：** 开始日期和结束日期，至少有一个日期存在。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param create_until: The create_until of this CountOtherResourceRequest.
        :type create_until: str
        """
        self._create_until = create_until

    @property
    def ip(self):
        r"""Gets the ip of this CountOtherResourceRequest.

        **参数解释：** 私有ip。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The ip of this CountOtherResourceRequest.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this CountOtherResourceRequest.

        **参数解释：** 私有ip。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param ip: The ip of this CountOtherResourceRequest.
        :type ip: str
        """
        self._ip = ip

    @property
    def os_type(self):
        r"""Gets the os_type of this CountOtherResourceRequest.

        **参数解释：** 操作系统。 **约束限制：** 不涉及。 **取值范围：** - windows：windows操作系统类型。 - linux：linux操作系统类型。 **默认取值：** 不涉及。

        :return: The os_type of this CountOtherResourceRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this CountOtherResourceRequest.

        **参数解释：** 操作系统。 **约束限制：** 不涉及。 **取值范围：** - windows：windows操作系统类型。 - linux：linux操作系统类型。 **默认取值：** 不涉及。

        :param os_type: The os_type of this CountOtherResourceRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def os_version_list(self):
        r"""Gets the os_version_list of this CountOtherResourceRequest.

        **参数解释：** OS版本。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The os_version_list of this CountOtherResourceRequest.
        :rtype: str
        """
        return self._os_version_list

    @os_version_list.setter
    def os_version_list(self, os_version_list):
        r"""Sets the os_version_list of this CountOtherResourceRequest.

        **参数解释：** OS版本。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param os_version_list: The os_version_list of this CountOtherResourceRequest.
        :type os_version_list: str
        """
        self._os_version_list = os_version_list

    @property
    def agent_state(self):
        r"""Gets the agent_state of this CountOtherResourceRequest.

        **参数解释：** agent状态。 **约束限制：** 不涉及。 **取值范围：** - ONLINE：运行中。 - OFFLINE：异常。 - INSTALLING：安装中。 - FAILED：安装失败。 - UNINSTALLED：已卸载。 - null：未安装。 **默认取值：** 不涉及。

        :return: The agent_state of this CountOtherResourceRequest.
        :rtype: str
        """
        return self._agent_state

    @agent_state.setter
    def agent_state(self, agent_state):
        r"""Sets the agent_state of this CountOtherResourceRequest.

        **参数解释：** agent状态。 **约束限制：** 不涉及。 **取值范围：** - ONLINE：运行中。 - OFFLINE：异常。 - INSTALLING：安装中。 - FAILED：安装失败。 - UNINSTALLED：已卸载。 - null：未安装。 **默认取值：** 不涉及。

        :param agent_state: The agent_state of this CountOtherResourceRequest.
        :type agent_state: str
        """
        self._agent_state = agent_state

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
        if not isinstance(other, CountOtherResourceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
