# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupOtherResourceRelationQueryResponseData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'domain_id': 'str',
        'cmdb_resource_id': 'str',
        'group_id': 'str',
        'group_name': 'str',
        'resource_id': 'str',
        'name': 'str',
        'type': 'str',
        'is_delegated': 'bool',
        'region_id': 'str',
        'inner_ip': 'str',
        'zone_id': 'str',
        'is_host': 'bool',
        'agent_id': 'str',
        'agent_state': 'str',
        'datasource': 'str',
        'description': 'str',
        'properties': 'dict(str, object)',
        'ingest_properties': 'dict(str, object)',
        'xrn': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'domain_id': 'domain_id',
        'cmdb_resource_id': 'cmdb_resource_id',
        'group_id': 'group_id',
        'group_name': 'group_name',
        'resource_id': 'resource_id',
        'name': 'name',
        'type': 'type',
        'is_delegated': 'is_delegated',
        'region_id': 'region_id',
        'inner_ip': 'inner_ip',
        'zone_id': 'zone_id',
        'is_host': 'is_host',
        'agent_id': 'agent_id',
        'agent_state': 'agent_state',
        'datasource': 'datasource',
        'description': 'description',
        'properties': 'properties',
        'ingest_properties': 'ingest_properties',
        'xrn': 'xrn',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, domain_id=None, cmdb_resource_id=None, group_id=None, group_name=None, resource_id=None, name=None, type=None, is_delegated=None, region_id=None, inner_ip=None, zone_id=None, is_host=None, agent_id=None, agent_state=None, datasource=None, description=None, properties=None, ingest_properties=None, xrn=None, create_time=None, update_time=None):
        r"""GroupOtherResourceRelationQueryResponseData

        The model defined in huaweicloud sdk

        :param id: **参数解释：** CMDB生成uuid。 **取值范围：** 不涉及。
        :type id: str
        :param domain_id: **参数解释：** 租户id。 **取值范围：** 字符串，长度32个字符。
        :type domain_id: str
        :param cmdb_resource_id: **参数解释：** CloudCMDB分配的资源uuid。 **取值范围：** 不涉及。
        :type cmdb_resource_id: str
        :param group_id: **参数解释：** 分组id。 **取值范围：** 字符串，长度24个字符。
        :type group_id: str
        :param group_name: **参数解释：** 分组名称。 **取值范围：** 字符串，长度3~60个字符。
        :type group_name: str
        :param resource_id: **参数解释：** 资源id。 **取值范围：** 字符串，长度36个字符。
        :type resource_id: str
        :param name: **参数解释：** 资源名称。 **取值范围：** 字符串，长度3到50个字符串。
        :type name: str
        :param type: **参数解释：** 资源类型。 **取值范围：** - PM：物理机。 - VM：虚拟机。
        :type type: str
        :param is_delegated: **参数解释：** 是否已托管。 **取值范围：** - true：已经托管。 - false：未托管。
        :type is_delegated: bool
        :param region_id: **参数解释：** 区域id。 **取值范围：** 字符串，长度在0到64个字符之间。
        :type region_id: str
        :param inner_ip: **参数解释：** 资源内网ip。 **取值范围：** 不涉及。
        :type inner_ip: str
        :param zone_id: **参数解释：** 可用区id。 **取值范围：** 不涉及。
        :type zone_id: str
        :param is_host: **参数解释：** 是否为主机。 **取值范围：** - true：为主机。 - false： 非主机。
        :type is_host: bool
        :param agent_id: **参数解释：** uniagent的id值。 **取值范围：** 不涉及。
        :type agent_id: str
        :param agent_state: **参数解释：** uniagent的状态。 **取值范围：** - ONLINE：运行中。 - OFFLINE：异常。 - INSTALLING：安装中。 - FAILED：安装失败。 - UNINSTALLED：已卸载。 - null：未安装。
        :type agent_state: str
        :param datasource: **参数解释：** 云厂商账户id。 **取值范围：** 字符串，长度在0到24个字符之间。
        :type datasource: str
        :param description: **参数解释：** 描述。 **取值范围：** 字符串，长度在1到256个字符之间。
        :type description: str
        :param properties: **参数解释：** 属性信息。 **取值范围：** 不涉及。
        :type properties: dict(str, object)
        :param ingest_properties: **参数解释：** 数据采集属性，描述视图系统采集该资源时所记录的附加信息。 **取值范围：** 不涉及。
        :type ingest_properties: dict(str, object)
        :param xrn: **参数解释：** 设备标识。 **取值范围：** 字符串，长度3到50个字符之间。
        :type xrn: str
        :param create_time: **参数解释：** 创建时间。 **取值范围：** 不涉及。
        :type create_time: datetime
        :param update_time: **参数解释：** 更新时间。 **取值范围：** 不涉及。
        :type update_time: datetime
        """
        
        

        self._id = None
        self._domain_id = None
        self._cmdb_resource_id = None
        self._group_id = None
        self._group_name = None
        self._resource_id = None
        self._name = None
        self._type = None
        self._is_delegated = None
        self._region_id = None
        self._inner_ip = None
        self._zone_id = None
        self._is_host = None
        self._agent_id = None
        self._agent_state = None
        self._datasource = None
        self._description = None
        self._properties = None
        self._ingest_properties = None
        self._xrn = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if domain_id is not None:
            self.domain_id = domain_id
        if cmdb_resource_id is not None:
            self.cmdb_resource_id = cmdb_resource_id
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if resource_id is not None:
            self.resource_id = resource_id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if is_delegated is not None:
            self.is_delegated = is_delegated
        if region_id is not None:
            self.region_id = region_id
        if inner_ip is not None:
            self.inner_ip = inner_ip
        if zone_id is not None:
            self.zone_id = zone_id
        if is_host is not None:
            self.is_host = is_host
        if agent_id is not None:
            self.agent_id = agent_id
        if agent_state is not None:
            self.agent_state = agent_state
        if datasource is not None:
            self.datasource = datasource
        if description is not None:
            self.description = description
        if properties is not None:
            self.properties = properties
        if ingest_properties is not None:
            self.ingest_properties = ingest_properties
        if xrn is not None:
            self.xrn = xrn
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** CMDB生成uuid。 **取值范围：** 不涉及。

        :return: The id of this GroupOtherResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** CMDB生成uuid。 **取值范围：** 不涉及。

        :param id: The id of this GroupOtherResourceRelationQueryResponseData.
        :type id: str
        """
        self._id = id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 租户id。 **取值范围：** 字符串，长度32个字符。

        :return: The domain_id of this GroupOtherResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 租户id。 **取值范围：** 字符串，长度32个字符。

        :param domain_id: The domain_id of this GroupOtherResourceRelationQueryResponseData.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def cmdb_resource_id(self):
        r"""Gets the cmdb_resource_id of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** CloudCMDB分配的资源uuid。 **取值范围：** 不涉及。

        :return: The cmdb_resource_id of this GroupOtherResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._cmdb_resource_id

    @cmdb_resource_id.setter
    def cmdb_resource_id(self, cmdb_resource_id):
        r"""Sets the cmdb_resource_id of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** CloudCMDB分配的资源uuid。 **取值范围：** 不涉及。

        :param cmdb_resource_id: The cmdb_resource_id of this GroupOtherResourceRelationQueryResponseData.
        :type cmdb_resource_id: str
        """
        self._cmdb_resource_id = cmdb_resource_id

    @property
    def group_id(self):
        r"""Gets the group_id of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 分组id。 **取值范围：** 字符串，长度24个字符。

        :return: The group_id of this GroupOtherResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 分组id。 **取值范围：** 字符串，长度24个字符。

        :param group_id: The group_id of this GroupOtherResourceRelationQueryResponseData.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 分组名称。 **取值范围：** 字符串，长度3~60个字符。

        :return: The group_name of this GroupOtherResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 分组名称。 **取值范围：** 字符串，长度3~60个字符。

        :param group_name: The group_name of this GroupOtherResourceRelationQueryResponseData.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def resource_id(self):
        r"""Gets the resource_id of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 资源id。 **取值范围：** 字符串，长度36个字符。

        :return: The resource_id of this GroupOtherResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 资源id。 **取值范围：** 字符串，长度36个字符。

        :param resource_id: The resource_id of this GroupOtherResourceRelationQueryResponseData.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def name(self):
        r"""Gets the name of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 资源名称。 **取值范围：** 字符串，长度3到50个字符串。

        :return: The name of this GroupOtherResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 资源名称。 **取值范围：** 字符串，长度3到50个字符串。

        :param name: The name of this GroupOtherResourceRelationQueryResponseData.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 资源类型。 **取值范围：** - PM：物理机。 - VM：虚拟机。

        :return: The type of this GroupOtherResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 资源类型。 **取值范围：** - PM：物理机。 - VM：虚拟机。

        :param type: The type of this GroupOtherResourceRelationQueryResponseData.
        :type type: str
        """
        self._type = type

    @property
    def is_delegated(self):
        r"""Gets the is_delegated of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 是否已托管。 **取值范围：** - true：已经托管。 - false：未托管。

        :return: The is_delegated of this GroupOtherResourceRelationQueryResponseData.
        :rtype: bool
        """
        return self._is_delegated

    @is_delegated.setter
    def is_delegated(self, is_delegated):
        r"""Sets the is_delegated of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 是否已托管。 **取值范围：** - true：已经托管。 - false：未托管。

        :param is_delegated: The is_delegated of this GroupOtherResourceRelationQueryResponseData.
        :type is_delegated: bool
        """
        self._is_delegated = is_delegated

    @property
    def region_id(self):
        r"""Gets the region_id of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 区域id。 **取值范围：** 字符串，长度在0到64个字符之间。

        :return: The region_id of this GroupOtherResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 区域id。 **取值范围：** 字符串，长度在0到64个字符之间。

        :param region_id: The region_id of this GroupOtherResourceRelationQueryResponseData.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def inner_ip(self):
        r"""Gets the inner_ip of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 资源内网ip。 **取值范围：** 不涉及。

        :return: The inner_ip of this GroupOtherResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._inner_ip

    @inner_ip.setter
    def inner_ip(self, inner_ip):
        r"""Sets the inner_ip of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 资源内网ip。 **取值范围：** 不涉及。

        :param inner_ip: The inner_ip of this GroupOtherResourceRelationQueryResponseData.
        :type inner_ip: str
        """
        self._inner_ip = inner_ip

    @property
    def zone_id(self):
        r"""Gets the zone_id of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 可用区id。 **取值范围：** 不涉及。

        :return: The zone_id of this GroupOtherResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        r"""Sets the zone_id of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 可用区id。 **取值范围：** 不涉及。

        :param zone_id: The zone_id of this GroupOtherResourceRelationQueryResponseData.
        :type zone_id: str
        """
        self._zone_id = zone_id

    @property
    def is_host(self):
        r"""Gets the is_host of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 是否为主机。 **取值范围：** - true：为主机。 - false： 非主机。

        :return: The is_host of this GroupOtherResourceRelationQueryResponseData.
        :rtype: bool
        """
        return self._is_host

    @is_host.setter
    def is_host(self, is_host):
        r"""Sets the is_host of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 是否为主机。 **取值范围：** - true：为主机。 - false： 非主机。

        :param is_host: The is_host of this GroupOtherResourceRelationQueryResponseData.
        :type is_host: bool
        """
        self._is_host = is_host

    @property
    def agent_id(self):
        r"""Gets the agent_id of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** uniagent的id值。 **取值范围：** 不涉及。

        :return: The agent_id of this GroupOtherResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** uniagent的id值。 **取值范围：** 不涉及。

        :param agent_id: The agent_id of this GroupOtherResourceRelationQueryResponseData.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def agent_state(self):
        r"""Gets the agent_state of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** uniagent的状态。 **取值范围：** - ONLINE：运行中。 - OFFLINE：异常。 - INSTALLING：安装中。 - FAILED：安装失败。 - UNINSTALLED：已卸载。 - null：未安装。

        :return: The agent_state of this GroupOtherResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._agent_state

    @agent_state.setter
    def agent_state(self, agent_state):
        r"""Sets the agent_state of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** uniagent的状态。 **取值范围：** - ONLINE：运行中。 - OFFLINE：异常。 - INSTALLING：安装中。 - FAILED：安装失败。 - UNINSTALLED：已卸载。 - null：未安装。

        :param agent_state: The agent_state of this GroupOtherResourceRelationQueryResponseData.
        :type agent_state: str
        """
        self._agent_state = agent_state

    @property
    def datasource(self):
        r"""Gets the datasource of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 云厂商账户id。 **取值范围：** 字符串，长度在0到24个字符之间。

        :return: The datasource of this GroupOtherResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._datasource

    @datasource.setter
    def datasource(self, datasource):
        r"""Sets the datasource of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 云厂商账户id。 **取值范围：** 字符串，长度在0到24个字符之间。

        :param datasource: The datasource of this GroupOtherResourceRelationQueryResponseData.
        :type datasource: str
        """
        self._datasource = datasource

    @property
    def description(self):
        r"""Gets the description of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 描述。 **取值范围：** 字符串，长度在1到256个字符之间。

        :return: The description of this GroupOtherResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 描述。 **取值范围：** 字符串，长度在1到256个字符之间。

        :param description: The description of this GroupOtherResourceRelationQueryResponseData.
        :type description: str
        """
        self._description = description

    @property
    def properties(self):
        r"""Gets the properties of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 属性信息。 **取值范围：** 不涉及。

        :return: The properties of this GroupOtherResourceRelationQueryResponseData.
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 属性信息。 **取值范围：** 不涉及。

        :param properties: The properties of this GroupOtherResourceRelationQueryResponseData.
        :type properties: dict(str, object)
        """
        self._properties = properties

    @property
    def ingest_properties(self):
        r"""Gets the ingest_properties of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 数据采集属性，描述视图系统采集该资源时所记录的附加信息。 **取值范围：** 不涉及。

        :return: The ingest_properties of this GroupOtherResourceRelationQueryResponseData.
        :rtype: dict(str, object)
        """
        return self._ingest_properties

    @ingest_properties.setter
    def ingest_properties(self, ingest_properties):
        r"""Sets the ingest_properties of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 数据采集属性，描述视图系统采集该资源时所记录的附加信息。 **取值范围：** 不涉及。

        :param ingest_properties: The ingest_properties of this GroupOtherResourceRelationQueryResponseData.
        :type ingest_properties: dict(str, object)
        """
        self._ingest_properties = ingest_properties

    @property
    def xrn(self):
        r"""Gets the xrn of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 设备标识。 **取值范围：** 字符串，长度3到50个字符之间。

        :return: The xrn of this GroupOtherResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._xrn

    @xrn.setter
    def xrn(self, xrn):
        r"""Sets the xrn of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 设备标识。 **取值范围：** 字符串，长度3到50个字符之间。

        :param xrn: The xrn of this GroupOtherResourceRelationQueryResponseData.
        :type xrn: str
        """
        self._xrn = xrn

    @property
    def create_time(self):
        r"""Gets the create_time of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 创建时间。 **取值范围：** 不涉及。

        :return: The create_time of this GroupOtherResourceRelationQueryResponseData.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 创建时间。 **取值范围：** 不涉及。

        :param create_time: The create_time of this GroupOtherResourceRelationQueryResponseData.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 更新时间。 **取值范围：** 不涉及。

        :return: The update_time of this GroupOtherResourceRelationQueryResponseData.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this GroupOtherResourceRelationQueryResponseData.

        **参数解释：** 更新时间。 **取值范围：** 不涉及。

        :param update_time: The update_time of this GroupOtherResourceRelationQueryResponseData.
        :type update_time: datetime
        """
        self._update_time = update_time

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
        if not isinstance(other, GroupOtherResourceRelationQueryResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
