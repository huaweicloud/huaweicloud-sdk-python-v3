# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupAliResourceRelationQueryResponseData:

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
        'cmdb_resource_id': 'str',
        'group_id': 'str',
        'group_name': 'str',
        'resource_id': 'str',
        'name': 'str',
        'type': 'str',
        'ingest_properties': 'object',
        'zone_id': 'str',
        'inner_ip': 'str',
        'agent_id': 'str',
        'agent_state': 'str',
        'region_id': 'str',
        'create_time': 'str',
        'datasource': 'str'
    }

    attribute_map = {
        'id': 'id',
        'cmdb_resource_id': 'cmdb_resource_id',
        'group_id': 'group_id',
        'group_name': 'group_name',
        'resource_id': 'resource_id',
        'name': 'name',
        'type': 'type',
        'ingest_properties': 'ingest_properties',
        'zone_id': 'zone_id',
        'inner_ip': 'inner_ip',
        'agent_id': 'agent_id',
        'agent_state': 'agent_state',
        'region_id': 'region_id',
        'create_time': 'create_time',
        'datasource': 'datasource'
    }

    def __init__(self, id=None, cmdb_resource_id=None, group_id=None, group_name=None, resource_id=None, name=None, type=None, ingest_properties=None, zone_id=None, inner_ip=None, agent_id=None, agent_state=None, region_id=None, create_time=None, datasource=None):
        r"""GroupAliResourceRelationQueryResponseData

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 分组资源关联的id。 **取值范围：** 不涉及。
        :type id: str
        :param cmdb_resource_id: **参数解释：** CloudCMDB分配的资源uuid。 **取值范围：** 不涉及。
        :type cmdb_resource_id: str
        :param group_id: **参数解释：** 分组id。 **取值范围：** 字符串，长度24个字符。
        :type group_id: str
        :param group_name: **参数解释：** 分组名称。 **取值范围：** 字符串，长度3~60个字符。
        :type group_name: str
        :param resource_id: **参数解释：** 在阿里云存的资源id。 **取值范围：** 不涉及。
        :type resource_id: str
        :param name: **参数解释：** 资源名称。 **取值范围：** 不涉及。
        :type name: str
        :param type: **参数解释：** 资源类型。 **取值范围：** 不涉及。
        :type type: str
        :param ingest_properties: **参数解释：** 数据采集属性。 **取值范围：** 不涉及。
        :type ingest_properties: object
        :param zone_id: **参数解释：** 可用区id。 **取值范围：** 不涉及。
        :type zone_id: str
        :param inner_ip: **参数解释：** 资源内网ip。 **取值范围：** 不涉及。
        :type inner_ip: str
        :param agent_id: **参数解释：** uniagent的id值。 **取值范围：** 不涉及。
        :type agent_id: str
        :param agent_state: **参数解释：** uniagent的状态。 **取值范围：** - ONLINE：运行中。 - OFFLINE：异常。 - INSTALLING：安装中。 - FAILED：安装失败。 - UNINSTALLED：已卸载。 - null：未安装。
        :type agent_state: str
        :param region_id: **参数解释：** 区域id。 **取值范围：** 字符串，长度在0到64个字符之间。
        :type region_id: str
        :param create_time: **参数解释：** 资源创建时间。 **取值范围：** 不涉及。
        :type create_time: str
        :param datasource: **参数解释：** 云厂商账户id。 **取值范围：** 不涉及。
        :type datasource: str
        """
        
        

        self._id = None
        self._cmdb_resource_id = None
        self._group_id = None
        self._group_name = None
        self._resource_id = None
        self._name = None
        self._type = None
        self._ingest_properties = None
        self._zone_id = None
        self._inner_ip = None
        self._agent_id = None
        self._agent_state = None
        self._region_id = None
        self._create_time = None
        self._datasource = None
        self.discriminator = None

        if id is not None:
            self.id = id
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
        if ingest_properties is not None:
            self.ingest_properties = ingest_properties
        if zone_id is not None:
            self.zone_id = zone_id
        if inner_ip is not None:
            self.inner_ip = inner_ip
        if agent_id is not None:
            self.agent_id = agent_id
        if agent_state is not None:
            self.agent_state = agent_state
        if region_id is not None:
            self.region_id = region_id
        if create_time is not None:
            self.create_time = create_time
        if datasource is not None:
            self.datasource = datasource

    @property
    def id(self):
        r"""Gets the id of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** 分组资源关联的id。 **取值范围：** 不涉及。

        :return: The id of this GroupAliResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** 分组资源关联的id。 **取值范围：** 不涉及。

        :param id: The id of this GroupAliResourceRelationQueryResponseData.
        :type id: str
        """
        self._id = id

    @property
    def cmdb_resource_id(self):
        r"""Gets the cmdb_resource_id of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** CloudCMDB分配的资源uuid。 **取值范围：** 不涉及。

        :return: The cmdb_resource_id of this GroupAliResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._cmdb_resource_id

    @cmdb_resource_id.setter
    def cmdb_resource_id(self, cmdb_resource_id):
        r"""Sets the cmdb_resource_id of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** CloudCMDB分配的资源uuid。 **取值范围：** 不涉及。

        :param cmdb_resource_id: The cmdb_resource_id of this GroupAliResourceRelationQueryResponseData.
        :type cmdb_resource_id: str
        """
        self._cmdb_resource_id = cmdb_resource_id

    @property
    def group_id(self):
        r"""Gets the group_id of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** 分组id。 **取值范围：** 字符串，长度24个字符。

        :return: The group_id of this GroupAliResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** 分组id。 **取值范围：** 字符串，长度24个字符。

        :param group_id: The group_id of this GroupAliResourceRelationQueryResponseData.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** 分组名称。 **取值范围：** 字符串，长度3~60个字符。

        :return: The group_name of this GroupAliResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** 分组名称。 **取值范围：** 字符串，长度3~60个字符。

        :param group_name: The group_name of this GroupAliResourceRelationQueryResponseData.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def resource_id(self):
        r"""Gets the resource_id of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** 在阿里云存的资源id。 **取值范围：** 不涉及。

        :return: The resource_id of this GroupAliResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** 在阿里云存的资源id。 **取值范围：** 不涉及。

        :param resource_id: The resource_id of this GroupAliResourceRelationQueryResponseData.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def name(self):
        r"""Gets the name of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** 资源名称。 **取值范围：** 不涉及。

        :return: The name of this GroupAliResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** 资源名称。 **取值范围：** 不涉及。

        :param name: The name of this GroupAliResourceRelationQueryResponseData.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** 资源类型。 **取值范围：** 不涉及。

        :return: The type of this GroupAliResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** 资源类型。 **取值范围：** 不涉及。

        :param type: The type of this GroupAliResourceRelationQueryResponseData.
        :type type: str
        """
        self._type = type

    @property
    def ingest_properties(self):
        r"""Gets the ingest_properties of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** 数据采集属性。 **取值范围：** 不涉及。

        :return: The ingest_properties of this GroupAliResourceRelationQueryResponseData.
        :rtype: object
        """
        return self._ingest_properties

    @ingest_properties.setter
    def ingest_properties(self, ingest_properties):
        r"""Sets the ingest_properties of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** 数据采集属性。 **取值范围：** 不涉及。

        :param ingest_properties: The ingest_properties of this GroupAliResourceRelationQueryResponseData.
        :type ingest_properties: object
        """
        self._ingest_properties = ingest_properties

    @property
    def zone_id(self):
        r"""Gets the zone_id of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** 可用区id。 **取值范围：** 不涉及。

        :return: The zone_id of this GroupAliResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        r"""Sets the zone_id of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** 可用区id。 **取值范围：** 不涉及。

        :param zone_id: The zone_id of this GroupAliResourceRelationQueryResponseData.
        :type zone_id: str
        """
        self._zone_id = zone_id

    @property
    def inner_ip(self):
        r"""Gets the inner_ip of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** 资源内网ip。 **取值范围：** 不涉及。

        :return: The inner_ip of this GroupAliResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._inner_ip

    @inner_ip.setter
    def inner_ip(self, inner_ip):
        r"""Sets the inner_ip of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** 资源内网ip。 **取值范围：** 不涉及。

        :param inner_ip: The inner_ip of this GroupAliResourceRelationQueryResponseData.
        :type inner_ip: str
        """
        self._inner_ip = inner_ip

    @property
    def agent_id(self):
        r"""Gets the agent_id of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** uniagent的id值。 **取值范围：** 不涉及。

        :return: The agent_id of this GroupAliResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** uniagent的id值。 **取值范围：** 不涉及。

        :param agent_id: The agent_id of this GroupAliResourceRelationQueryResponseData.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def agent_state(self):
        r"""Gets the agent_state of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** uniagent的状态。 **取值范围：** - ONLINE：运行中。 - OFFLINE：异常。 - INSTALLING：安装中。 - FAILED：安装失败。 - UNINSTALLED：已卸载。 - null：未安装。

        :return: The agent_state of this GroupAliResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._agent_state

    @agent_state.setter
    def agent_state(self, agent_state):
        r"""Sets the agent_state of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** uniagent的状态。 **取值范围：** - ONLINE：运行中。 - OFFLINE：异常。 - INSTALLING：安装中。 - FAILED：安装失败。 - UNINSTALLED：已卸载。 - null：未安装。

        :param agent_state: The agent_state of this GroupAliResourceRelationQueryResponseData.
        :type agent_state: str
        """
        self._agent_state = agent_state

    @property
    def region_id(self):
        r"""Gets the region_id of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** 区域id。 **取值范围：** 字符串，长度在0到64个字符之间。

        :return: The region_id of this GroupAliResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** 区域id。 **取值范围：** 字符串，长度在0到64个字符之间。

        :param region_id: The region_id of this GroupAliResourceRelationQueryResponseData.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def create_time(self):
        r"""Gets the create_time of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** 资源创建时间。 **取值范围：** 不涉及。

        :return: The create_time of this GroupAliResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** 资源创建时间。 **取值范围：** 不涉及。

        :param create_time: The create_time of this GroupAliResourceRelationQueryResponseData.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def datasource(self):
        r"""Gets the datasource of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** 云厂商账户id。 **取值范围：** 不涉及。

        :return: The datasource of this GroupAliResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._datasource

    @datasource.setter
    def datasource(self, datasource):
        r"""Sets the datasource of this GroupAliResourceRelationQueryResponseData.

        **参数解释：** 云厂商账户id。 **取值范围：** 不涉及。

        :param datasource: The datasource of this GroupAliResourceRelationQueryResponseData.
        :type datasource: str
        """
        self._datasource = datasource

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
        if not isinstance(other, GroupAliResourceRelationQueryResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
