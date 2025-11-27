# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupRmsResourceRelationQueryResponseData:

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
        'application_id': 'str',
        'resource_id': 'str',
        'name': 'str',
        'ep_id': 'str',
        'project_id': 'str',
        'ep_name': 'str',
        'provider': 'str',
        'domain_id': 'str',
        'type': 'str',
        'region_id': 'str',
        'inner_ip': 'str',
        'agent_id': 'str',
        'agent_state': 'str',
        'tags': 'list[GroupRmsResourceRelationQueryResponseTags]',
        'ingest_properties': 'object',
        'properties': 'dict(str, str)',
        'operable': 'str',
        'create_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'cmdb_resource_id': 'cmdb_resource_id',
        'group_id': 'group_id',
        'group_name': 'group_name',
        'application_id': 'application_id',
        'resource_id': 'resource_id',
        'name': 'name',
        'ep_id': 'ep_id',
        'project_id': 'project_id',
        'ep_name': 'ep_name',
        'provider': 'provider',
        'domain_id': 'domain_id',
        'type': 'type',
        'region_id': 'region_id',
        'inner_ip': 'inner_ip',
        'agent_id': 'agent_id',
        'agent_state': 'agent_state',
        'tags': 'tags',
        'ingest_properties': 'ingest_properties',
        'properties': 'properties',
        'operable': 'operable',
        'create_time': 'create_time'
    }

    def __init__(self, id=None, cmdb_resource_id=None, group_id=None, group_name=None, application_id=None, resource_id=None, name=None, ep_id=None, project_id=None, ep_name=None, provider=None, domain_id=None, type=None, region_id=None, inner_ip=None, agent_id=None, agent_state=None, tags=None, ingest_properties=None, properties=None, operable=None, create_time=None):
        r"""GroupRmsResourceRelationQueryResponseData

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 分组资源关联的id。 **取值范围：** 不涉及。
        :type id: str
        :param cmdb_resource_id: **参数解释：** CloudCMDB分配的资源uuid。
        :type cmdb_resource_id: str
        :param group_id: **参数解释：** 分组id。 **取值范围：** 不涉及。
        :type group_id: str
        :param group_name: **参数解释：** 分组名称。 **取值范围：** 不涉及。
        :type group_name: str
        :param application_id: **参数解释：** 应用id。 **取值范围：** 长度24。
        :type application_id: str
        :param resource_id: **参数解释：** 资源id。 **取值范围：** 长度36
        :type resource_id: str
        :param name: **参数解释：** 资源名称。 **取值范围：** 长度3到50之间。
        :type name: str
        :param ep_id: **参数解释：** 企业项目id。 **取值范围：** 不涉及。
        :type ep_id: str
        :param project_id: **参数解释：** 项目id。 **取值范围：** 不涉及。
        :type project_id: str
        :param ep_name: **参数解释：** 企业项目名称。 **取值范围：** 不涉及。
        :type ep_name: str
        :param provider: **参数解释：** 云服务名称。 **取值范围：** 不涉及。
        :type provider: str
        :param domain_id: **参数解释：** 租户id。 **取值范围：** 不涉及。
        :type domain_id: str
        :param type: **参数解释：** 资源类型。 **取值范围：** 资源类型较多，根据实际业务选择资源类型、常用资源类型如下： - cloudservers：弹性云服务器。 - servers：裸金属服务器。 - clusters：云容器引擎。 - instances：云数据库。
        :type type: str
        :param region_id: **参数解释：** 区域id。 **取值范围：** 字符串，长度在0到64个字符之间。
        :type region_id: str
        :param inner_ip: **参数解释：** 资源内网ip。 **取值范围：** 不涉及。
        :type inner_ip: str
        :param agent_id: **参数解释：** uniagent的id值。 **取值范围：** 不涉及。
        :type agent_id: str
        :param agent_state: **参数解释：** uniagent的状态。 **取值范围：** - ONLINE：运行中。 - OFFLINE：异常。 - INSTALLING：安装中。 - FAILED：安装失败。 - UNINSTALLED：已卸载。 - null：未安装。
        :type agent_state: str
        :param tags: **参数解释：** 标签键值对。 **取值范围：** 不涉及。
        :type tags: list[:class:`huaweicloudsdkcoc.v1.GroupRmsResourceRelationQueryResponseTags`]
        :param ingest_properties: **参数解释：** 数据采集属性。 **取值范围：** 不涉及。
        :type ingest_properties: object
        :param properties: **参数解释：** 属性。 **取值范围：** 不涉及。
        :type properties: dict(str, str)
        :param operable: **参数解释：** 用户定义资源是否可运维实例。 **取值范围：** - ENABLE：可运维。 - DISABLE：不可运维实例operable字段不存在。
        :type operable: str
        :param create_time: **参数解释：** 创建时间，参考ISO8601标准格式。 **取值范围：** 不涉及。
        :type create_time: datetime
        """
        
        

        self._id = None
        self._cmdb_resource_id = None
        self._group_id = None
        self._group_name = None
        self._application_id = None
        self._resource_id = None
        self._name = None
        self._ep_id = None
        self._project_id = None
        self._ep_name = None
        self._provider = None
        self._domain_id = None
        self._type = None
        self._region_id = None
        self._inner_ip = None
        self._agent_id = None
        self._agent_state = None
        self._tags = None
        self._ingest_properties = None
        self._properties = None
        self._operable = None
        self._create_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if cmdb_resource_id is not None:
            self.cmdb_resource_id = cmdb_resource_id
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if application_id is not None:
            self.application_id = application_id
        if resource_id is not None:
            self.resource_id = resource_id
        if name is not None:
            self.name = name
        if ep_id is not None:
            self.ep_id = ep_id
        if project_id is not None:
            self.project_id = project_id
        if ep_name is not None:
            self.ep_name = ep_name
        if provider is not None:
            self.provider = provider
        if domain_id is not None:
            self.domain_id = domain_id
        if type is not None:
            self.type = type
        if region_id is not None:
            self.region_id = region_id
        if inner_ip is not None:
            self.inner_ip = inner_ip
        if agent_id is not None:
            self.agent_id = agent_id
        if agent_state is not None:
            self.agent_state = agent_state
        if tags is not None:
            self.tags = tags
        if ingest_properties is not None:
            self.ingest_properties = ingest_properties
        if properties is not None:
            self.properties = properties
        if operable is not None:
            self.operable = operable
        if create_time is not None:
            self.create_time = create_time

    @property
    def id(self):
        r"""Gets the id of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 分组资源关联的id。 **取值范围：** 不涉及。

        :return: The id of this GroupRmsResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 分组资源关联的id。 **取值范围：** 不涉及。

        :param id: The id of this GroupRmsResourceRelationQueryResponseData.
        :type id: str
        """
        self._id = id

    @property
    def cmdb_resource_id(self):
        r"""Gets the cmdb_resource_id of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** CloudCMDB分配的资源uuid。

        :return: The cmdb_resource_id of this GroupRmsResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._cmdb_resource_id

    @cmdb_resource_id.setter
    def cmdb_resource_id(self, cmdb_resource_id):
        r"""Sets the cmdb_resource_id of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** CloudCMDB分配的资源uuid。

        :param cmdb_resource_id: The cmdb_resource_id of this GroupRmsResourceRelationQueryResponseData.
        :type cmdb_resource_id: str
        """
        self._cmdb_resource_id = cmdb_resource_id

    @property
    def group_id(self):
        r"""Gets the group_id of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 分组id。 **取值范围：** 不涉及。

        :return: The group_id of this GroupRmsResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 分组id。 **取值范围：** 不涉及。

        :param group_id: The group_id of this GroupRmsResourceRelationQueryResponseData.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 分组名称。 **取值范围：** 不涉及。

        :return: The group_name of this GroupRmsResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 分组名称。 **取值范围：** 不涉及。

        :param group_name: The group_name of this GroupRmsResourceRelationQueryResponseData.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def application_id(self):
        r"""Gets the application_id of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 应用id。 **取值范围：** 长度24。

        :return: The application_id of this GroupRmsResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 应用id。 **取值范围：** 长度24。

        :param application_id: The application_id of this GroupRmsResourceRelationQueryResponseData.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 资源id。 **取值范围：** 长度36

        :return: The resource_id of this GroupRmsResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 资源id。 **取值范围：** 长度36

        :param resource_id: The resource_id of this GroupRmsResourceRelationQueryResponseData.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def name(self):
        r"""Gets the name of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 资源名称。 **取值范围：** 长度3到50之间。

        :return: The name of this GroupRmsResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 资源名称。 **取值范围：** 长度3到50之间。

        :param name: The name of this GroupRmsResourceRelationQueryResponseData.
        :type name: str
        """
        self._name = name

    @property
    def ep_id(self):
        r"""Gets the ep_id of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 企业项目id。 **取值范围：** 不涉及。

        :return: The ep_id of this GroupRmsResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._ep_id

    @ep_id.setter
    def ep_id(self, ep_id):
        r"""Sets the ep_id of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 企业项目id。 **取值范围：** 不涉及。

        :param ep_id: The ep_id of this GroupRmsResourceRelationQueryResponseData.
        :type ep_id: str
        """
        self._ep_id = ep_id

    @property
    def project_id(self):
        r"""Gets the project_id of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 项目id。 **取值范围：** 不涉及。

        :return: The project_id of this GroupRmsResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 项目id。 **取值范围：** 不涉及。

        :param project_id: The project_id of this GroupRmsResourceRelationQueryResponseData.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def ep_name(self):
        r"""Gets the ep_name of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 企业项目名称。 **取值范围：** 不涉及。

        :return: The ep_name of this GroupRmsResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._ep_name

    @ep_name.setter
    def ep_name(self, ep_name):
        r"""Sets the ep_name of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 企业项目名称。 **取值范围：** 不涉及。

        :param ep_name: The ep_name of this GroupRmsResourceRelationQueryResponseData.
        :type ep_name: str
        """
        self._ep_name = ep_name

    @property
    def provider(self):
        r"""Gets the provider of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 云服务名称。 **取值范围：** 不涉及。

        :return: The provider of this GroupRmsResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 云服务名称。 **取值范围：** 不涉及。

        :param provider: The provider of this GroupRmsResourceRelationQueryResponseData.
        :type provider: str
        """
        self._provider = provider

    @property
    def domain_id(self):
        r"""Gets the domain_id of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 租户id。 **取值范围：** 不涉及。

        :return: The domain_id of this GroupRmsResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 租户id。 **取值范围：** 不涉及。

        :param domain_id: The domain_id of this GroupRmsResourceRelationQueryResponseData.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def type(self):
        r"""Gets the type of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 资源类型。 **取值范围：** 资源类型较多，根据实际业务选择资源类型、常用资源类型如下： - cloudservers：弹性云服务器。 - servers：裸金属服务器。 - clusters：云容器引擎。 - instances：云数据库。

        :return: The type of this GroupRmsResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 资源类型。 **取值范围：** 资源类型较多，根据实际业务选择资源类型、常用资源类型如下： - cloudservers：弹性云服务器。 - servers：裸金属服务器。 - clusters：云容器引擎。 - instances：云数据库。

        :param type: The type of this GroupRmsResourceRelationQueryResponseData.
        :type type: str
        """
        self._type = type

    @property
    def region_id(self):
        r"""Gets the region_id of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 区域id。 **取值范围：** 字符串，长度在0到64个字符之间。

        :return: The region_id of this GroupRmsResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 区域id。 **取值范围：** 字符串，长度在0到64个字符之间。

        :param region_id: The region_id of this GroupRmsResourceRelationQueryResponseData.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def inner_ip(self):
        r"""Gets the inner_ip of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 资源内网ip。 **取值范围：** 不涉及。

        :return: The inner_ip of this GroupRmsResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._inner_ip

    @inner_ip.setter
    def inner_ip(self, inner_ip):
        r"""Sets the inner_ip of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 资源内网ip。 **取值范围：** 不涉及。

        :param inner_ip: The inner_ip of this GroupRmsResourceRelationQueryResponseData.
        :type inner_ip: str
        """
        self._inner_ip = inner_ip

    @property
    def agent_id(self):
        r"""Gets the agent_id of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** uniagent的id值。 **取值范围：** 不涉及。

        :return: The agent_id of this GroupRmsResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** uniagent的id值。 **取值范围：** 不涉及。

        :param agent_id: The agent_id of this GroupRmsResourceRelationQueryResponseData.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def agent_state(self):
        r"""Gets the agent_state of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** uniagent的状态。 **取值范围：** - ONLINE：运行中。 - OFFLINE：异常。 - INSTALLING：安装中。 - FAILED：安装失败。 - UNINSTALLED：已卸载。 - null：未安装。

        :return: The agent_state of this GroupRmsResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._agent_state

    @agent_state.setter
    def agent_state(self, agent_state):
        r"""Sets the agent_state of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** uniagent的状态。 **取值范围：** - ONLINE：运行中。 - OFFLINE：异常。 - INSTALLING：安装中。 - FAILED：安装失败。 - UNINSTALLED：已卸载。 - null：未安装。

        :param agent_state: The agent_state of this GroupRmsResourceRelationQueryResponseData.
        :type agent_state: str
        """
        self._agent_state = agent_state

    @property
    def tags(self):
        r"""Gets the tags of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 标签键值对。 **取值范围：** 不涉及。

        :return: The tags of this GroupRmsResourceRelationQueryResponseData.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.GroupRmsResourceRelationQueryResponseTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 标签键值对。 **取值范围：** 不涉及。

        :param tags: The tags of this GroupRmsResourceRelationQueryResponseData.
        :type tags: list[:class:`huaweicloudsdkcoc.v1.GroupRmsResourceRelationQueryResponseTags`]
        """
        self._tags = tags

    @property
    def ingest_properties(self):
        r"""Gets the ingest_properties of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 数据采集属性。 **取值范围：** 不涉及。

        :return: The ingest_properties of this GroupRmsResourceRelationQueryResponseData.
        :rtype: object
        """
        return self._ingest_properties

    @ingest_properties.setter
    def ingest_properties(self, ingest_properties):
        r"""Sets the ingest_properties of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 数据采集属性。 **取值范围：** 不涉及。

        :param ingest_properties: The ingest_properties of this GroupRmsResourceRelationQueryResponseData.
        :type ingest_properties: object
        """
        self._ingest_properties = ingest_properties

    @property
    def properties(self):
        r"""Gets the properties of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 属性。 **取值范围：** 不涉及。

        :return: The properties of this GroupRmsResourceRelationQueryResponseData.
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 属性。 **取值范围：** 不涉及。

        :param properties: The properties of this GroupRmsResourceRelationQueryResponseData.
        :type properties: dict(str, str)
        """
        self._properties = properties

    @property
    def operable(self):
        r"""Gets the operable of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 用户定义资源是否可运维实例。 **取值范围：** - ENABLE：可运维。 - DISABLE：不可运维实例operable字段不存在。

        :return: The operable of this GroupRmsResourceRelationQueryResponseData.
        :rtype: str
        """
        return self._operable

    @operable.setter
    def operable(self, operable):
        r"""Sets the operable of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 用户定义资源是否可运维实例。 **取值范围：** - ENABLE：可运维。 - DISABLE：不可运维实例operable字段不存在。

        :param operable: The operable of this GroupRmsResourceRelationQueryResponseData.
        :type operable: str
        """
        self._operable = operable

    @property
    def create_time(self):
        r"""Gets the create_time of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 创建时间，参考ISO8601标准格式。 **取值范围：** 不涉及。

        :return: The create_time of this GroupRmsResourceRelationQueryResponseData.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this GroupRmsResourceRelationQueryResponseData.

        **参数解释：** 创建时间，参考ISO8601标准格式。 **取值范围：** 不涉及。

        :param create_time: The create_time of this GroupRmsResourceRelationQueryResponseData.
        :type create_time: datetime
        """
        self._create_time = create_time

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
        if not isinstance(other, GroupRmsResourceRelationQueryResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
