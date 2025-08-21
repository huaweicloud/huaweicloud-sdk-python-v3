# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchListResourceResponseData:

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
        'resource_id': 'str',
        'domain_id': 'str',
        'name': 'str',
        'provider': 'str',
        'type': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'region_id': 'str',
        'ep_id': 'str',
        'ep_name': 'str',
        'tags': 'object',
        'agent_id': 'str',
        'agent_state': 'str',
        'properties': 'object',
        'ingest_properties': 'dict(str, str)',
        'is_delegated': 'bool',
        'inner_ip': 'str',
        'operable': 'str',
        'is_associate_group': 'bool',
        'associated_group_list': 'list[str]',
        'create_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'resource_id': 'resource_id',
        'domain_id': 'domain_id',
        'name': 'name',
        'provider': 'provider',
        'type': 'type',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'region_id': 'region_id',
        'ep_id': 'ep_id',
        'ep_name': 'ep_name',
        'tags': 'tags',
        'agent_id': 'agent_id',
        'agent_state': 'agent_state',
        'properties': 'properties',
        'ingest_properties': 'ingest_properties',
        'is_delegated': 'is_delegated',
        'inner_ip': 'inner_ip',
        'operable': 'operable',
        'is_associate_group': 'is_associate_group',
        'associated_group_list': 'associated_group_list',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, resource_id=None, domain_id=None, name=None, provider=None, type=None, project_id=None, project_name=None, region_id=None, ep_id=None, ep_name=None, tags=None, agent_id=None, agent_state=None, properties=None, ingest_properties=None, is_delegated=None, inner_ip=None, operable=None, is_associate_group=None, associated_group_list=None, create_time=None, update_time=None):
        r"""BatchListResourceResponseData

        The model defined in huaweicloud sdk

        :param id: **参数解释：** CMDB分配的资源ID。 **取值范围：** 不涉及。
        :type id: str
        :param resource_id: **参数解释：** 云服务分配的资源ID。 **取值范围：** 字符串，长度在36个字符。
        :type resource_id: str
        :param domain_id: **参数解释：** 租户id。 **取值范围：** 不涉及。
        :type domain_id: str
        :param name: **参数解释：** 资源名称。 **取值范围：** 字符串，长度3到50个字符之间。
        :type name: str
        :param provider: **参数解释：** 云服务名称。 **取值范围：** 字符串，长度1到64个字符之间。
        :type provider: str
        :param type: **参数解释：** 资源类型。 **取值范围：** 资源类型较多，根据实际业务选择资源类型、常用资源类型如下： - cloudservers：弹性云服务器。 - servers：裸金属服务器。 - clusters：云容器引擎。 - instances：云数据库。
        :type type: str
        :param project_id: **参数解释：** Openstack中的项目ID。 **取值范围：** 字符串，长度32个字符。
        :type project_id: str
        :param project_name: **参数解释：** region的子项目名称。 **取值范围：** 字符串，不超过255个字符。
        :type project_name: str
        :param region_id: **参数解释：** 区域id。 **取值范围：** 字符串，长度0到64个字符。
        :type region_id: str
        :param ep_id: **参数解释：** 企业项目ID。 **取值范围：** 请选择[[企业管理](https://support.huaweicloud.com/usermanual-em/em_eps_qs_0400.html)](tag:hws)[[企业管理](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/em_eps_qs_0400.html)](tag:hws_hk)中存在的项目ID。
        :type ep_id: str
        :param ep_name: **参数解释：** 企业项目名称。 **取值范围：** 由中文、英文字母、数字、下划线、中划线组成，且不能使用任何大小写形式的“default”，不超过255个字符。
        :type ep_name: str
        :param tags: **参数解释：** 资源标签。 **取值范围：** 不涉及。
        :type tags: object
        :param agent_id: **参数解释：** uniagent的id值。 **取值范围：** 不涉及。
        :type agent_id: str
        :param agent_state: **参数解释：** uniagent的状态。 **取值范围：** - ONLINE：运行中。 - OFFLINE：异常。 - INSTALLING：安装中。 - FAILED：安装失败。 - UNINSTALLED：已卸载。 - null：未安装。
        :type agent_state: str
        :param properties: **参数解释：** 资源详细属性。 **取值范围：** 不涉及。
        :type properties: object
        :param ingest_properties: **参数解释：** 采集属性。 **取值范围：** 不涉及。
        :type ingest_properties: dict(str, str)
        :param is_delegated: **参数解释：** 是否已托管。 **取值范围：** - true：已经托管。 - false：未托管。
        :type is_delegated: bool
        :param inner_ip: **参数解释：** 资源内网ip。 **取值范围：** 不涉及。
        :type inner_ip: str
        :param operable: **参数解释：** 用户定义资源是否可运维实例。 **取值范围：** - ENABLE：可运维实例。 - DISABLE：不可运维实例operable字段不存在。
        :type operable: str
        :param is_associate_group: **参数解释：** 是否已被指定分组关联。 **取值范围：** - true：已被指定分组关联。 - false：未被指定分组关联。
        :type is_associate_group: bool
        :param associated_group_list: **参数解释：** 资源所关联的分组信息组成的列表。 **取值范围：** 不涉及。
        :type associated_group_list: list[str]
        :param create_time: **参数解释：** 创建时间，参考ISO8601标准格式。 **取值范围：** 不涉及。
        :type create_time: datetime
        :param update_time: **参数解释：** 修改时间，参考ISO8601标准格式。 **取值范围：** 不涉及。
        :type update_time: datetime
        """
        
        

        self._id = None
        self._resource_id = None
        self._domain_id = None
        self._name = None
        self._provider = None
        self._type = None
        self._project_id = None
        self._project_name = None
        self._region_id = None
        self._ep_id = None
        self._ep_name = None
        self._tags = None
        self._agent_id = None
        self._agent_state = None
        self._properties = None
        self._ingest_properties = None
        self._is_delegated = None
        self._inner_ip = None
        self._operable = None
        self._is_associate_group = None
        self._associated_group_list = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if resource_id is not None:
            self.resource_id = resource_id
        if domain_id is not None:
            self.domain_id = domain_id
        if name is not None:
            self.name = name
        if provider is not None:
            self.provider = provider
        if type is not None:
            self.type = type
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if region_id is not None:
            self.region_id = region_id
        if ep_id is not None:
            self.ep_id = ep_id
        if ep_name is not None:
            self.ep_name = ep_name
        if tags is not None:
            self.tags = tags
        if agent_id is not None:
            self.agent_id = agent_id
        if agent_state is not None:
            self.agent_state = agent_state
        if properties is not None:
            self.properties = properties
        if ingest_properties is not None:
            self.ingest_properties = ingest_properties
        if is_delegated is not None:
            self.is_delegated = is_delegated
        if inner_ip is not None:
            self.inner_ip = inner_ip
        if operable is not None:
            self.operable = operable
        if is_associate_group is not None:
            self.is_associate_group = is_associate_group
        if associated_group_list is not None:
            self.associated_group_list = associated_group_list
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this BatchListResourceResponseData.

        **参数解释：** CMDB分配的资源ID。 **取值范围：** 不涉及。

        :return: The id of this BatchListResourceResponseData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BatchListResourceResponseData.

        **参数解释：** CMDB分配的资源ID。 **取值范围：** 不涉及。

        :param id: The id of this BatchListResourceResponseData.
        :type id: str
        """
        self._id = id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this BatchListResourceResponseData.

        **参数解释：** 云服务分配的资源ID。 **取值范围：** 字符串，长度在36个字符。

        :return: The resource_id of this BatchListResourceResponseData.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this BatchListResourceResponseData.

        **参数解释：** 云服务分配的资源ID。 **取值范围：** 字符串，长度在36个字符。

        :param resource_id: The resource_id of this BatchListResourceResponseData.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this BatchListResourceResponseData.

        **参数解释：** 租户id。 **取值范围：** 不涉及。

        :return: The domain_id of this BatchListResourceResponseData.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this BatchListResourceResponseData.

        **参数解释：** 租户id。 **取值范围：** 不涉及。

        :param domain_id: The domain_id of this BatchListResourceResponseData.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def name(self):
        r"""Gets the name of this BatchListResourceResponseData.

        **参数解释：** 资源名称。 **取值范围：** 字符串，长度3到50个字符之间。

        :return: The name of this BatchListResourceResponseData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BatchListResourceResponseData.

        **参数解释：** 资源名称。 **取值范围：** 字符串，长度3到50个字符之间。

        :param name: The name of this BatchListResourceResponseData.
        :type name: str
        """
        self._name = name

    @property
    def provider(self):
        r"""Gets the provider of this BatchListResourceResponseData.

        **参数解释：** 云服务名称。 **取值范围：** 字符串，长度1到64个字符之间。

        :return: The provider of this BatchListResourceResponseData.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this BatchListResourceResponseData.

        **参数解释：** 云服务名称。 **取值范围：** 字符串，长度1到64个字符之间。

        :param provider: The provider of this BatchListResourceResponseData.
        :type provider: str
        """
        self._provider = provider

    @property
    def type(self):
        r"""Gets the type of this BatchListResourceResponseData.

        **参数解释：** 资源类型。 **取值范围：** 资源类型较多，根据实际业务选择资源类型、常用资源类型如下： - cloudservers：弹性云服务器。 - servers：裸金属服务器。 - clusters：云容器引擎。 - instances：云数据库。

        :return: The type of this BatchListResourceResponseData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this BatchListResourceResponseData.

        **参数解释：** 资源类型。 **取值范围：** 资源类型较多，根据实际业务选择资源类型、常用资源类型如下： - cloudservers：弹性云服务器。 - servers：裸金属服务器。 - clusters：云容器引擎。 - instances：云数据库。

        :param type: The type of this BatchListResourceResponseData.
        :type type: str
        """
        self._type = type

    @property
    def project_id(self):
        r"""Gets the project_id of this BatchListResourceResponseData.

        **参数解释：** Openstack中的项目ID。 **取值范围：** 字符串，长度32个字符。

        :return: The project_id of this BatchListResourceResponseData.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this BatchListResourceResponseData.

        **参数解释：** Openstack中的项目ID。 **取值范围：** 字符串，长度32个字符。

        :param project_id: The project_id of this BatchListResourceResponseData.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        r"""Gets the project_name of this BatchListResourceResponseData.

        **参数解释：** region的子项目名称。 **取值范围：** 字符串，不超过255个字符。

        :return: The project_name of this BatchListResourceResponseData.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this BatchListResourceResponseData.

        **参数解释：** region的子项目名称。 **取值范围：** 字符串，不超过255个字符。

        :param project_name: The project_name of this BatchListResourceResponseData.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def region_id(self):
        r"""Gets the region_id of this BatchListResourceResponseData.

        **参数解释：** 区域id。 **取值范围：** 字符串，长度0到64个字符。

        :return: The region_id of this BatchListResourceResponseData.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this BatchListResourceResponseData.

        **参数解释：** 区域id。 **取值范围：** 字符串，长度0到64个字符。

        :param region_id: The region_id of this BatchListResourceResponseData.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def ep_id(self):
        r"""Gets the ep_id of this BatchListResourceResponseData.

        **参数解释：** 企业项目ID。 **取值范围：** 请选择[[企业管理](https://support.huaweicloud.com/usermanual-em/em_eps_qs_0400.html)](tag:hws)[[企业管理](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/em_eps_qs_0400.html)](tag:hws_hk)中存在的项目ID。

        :return: The ep_id of this BatchListResourceResponseData.
        :rtype: str
        """
        return self._ep_id

    @ep_id.setter
    def ep_id(self, ep_id):
        r"""Sets the ep_id of this BatchListResourceResponseData.

        **参数解释：** 企业项目ID。 **取值范围：** 请选择[[企业管理](https://support.huaweicloud.com/usermanual-em/em_eps_qs_0400.html)](tag:hws)[[企业管理](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/em_eps_qs_0400.html)](tag:hws_hk)中存在的项目ID。

        :param ep_id: The ep_id of this BatchListResourceResponseData.
        :type ep_id: str
        """
        self._ep_id = ep_id

    @property
    def ep_name(self):
        r"""Gets the ep_name of this BatchListResourceResponseData.

        **参数解释：** 企业项目名称。 **取值范围：** 由中文、英文字母、数字、下划线、中划线组成，且不能使用任何大小写形式的“default”，不超过255个字符。

        :return: The ep_name of this BatchListResourceResponseData.
        :rtype: str
        """
        return self._ep_name

    @ep_name.setter
    def ep_name(self, ep_name):
        r"""Sets the ep_name of this BatchListResourceResponseData.

        **参数解释：** 企业项目名称。 **取值范围：** 由中文、英文字母、数字、下划线、中划线组成，且不能使用任何大小写形式的“default”，不超过255个字符。

        :param ep_name: The ep_name of this BatchListResourceResponseData.
        :type ep_name: str
        """
        self._ep_name = ep_name

    @property
    def tags(self):
        r"""Gets the tags of this BatchListResourceResponseData.

        **参数解释：** 资源标签。 **取值范围：** 不涉及。

        :return: The tags of this BatchListResourceResponseData.
        :rtype: object
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this BatchListResourceResponseData.

        **参数解释：** 资源标签。 **取值范围：** 不涉及。

        :param tags: The tags of this BatchListResourceResponseData.
        :type tags: object
        """
        self._tags = tags

    @property
    def agent_id(self):
        r"""Gets the agent_id of this BatchListResourceResponseData.

        **参数解释：** uniagent的id值。 **取值范围：** 不涉及。

        :return: The agent_id of this BatchListResourceResponseData.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this BatchListResourceResponseData.

        **参数解释：** uniagent的id值。 **取值范围：** 不涉及。

        :param agent_id: The agent_id of this BatchListResourceResponseData.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def agent_state(self):
        r"""Gets the agent_state of this BatchListResourceResponseData.

        **参数解释：** uniagent的状态。 **取值范围：** - ONLINE：运行中。 - OFFLINE：异常。 - INSTALLING：安装中。 - FAILED：安装失败。 - UNINSTALLED：已卸载。 - null：未安装。

        :return: The agent_state of this BatchListResourceResponseData.
        :rtype: str
        """
        return self._agent_state

    @agent_state.setter
    def agent_state(self, agent_state):
        r"""Sets the agent_state of this BatchListResourceResponseData.

        **参数解释：** uniagent的状态。 **取值范围：** - ONLINE：运行中。 - OFFLINE：异常。 - INSTALLING：安装中。 - FAILED：安装失败。 - UNINSTALLED：已卸载。 - null：未安装。

        :param agent_state: The agent_state of this BatchListResourceResponseData.
        :type agent_state: str
        """
        self._agent_state = agent_state

    @property
    def properties(self):
        r"""Gets the properties of this BatchListResourceResponseData.

        **参数解释：** 资源详细属性。 **取值范围：** 不涉及。

        :return: The properties of this BatchListResourceResponseData.
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this BatchListResourceResponseData.

        **参数解释：** 资源详细属性。 **取值范围：** 不涉及。

        :param properties: The properties of this BatchListResourceResponseData.
        :type properties: object
        """
        self._properties = properties

    @property
    def ingest_properties(self):
        r"""Gets the ingest_properties of this BatchListResourceResponseData.

        **参数解释：** 采集属性。 **取值范围：** 不涉及。

        :return: The ingest_properties of this BatchListResourceResponseData.
        :rtype: dict(str, str)
        """
        return self._ingest_properties

    @ingest_properties.setter
    def ingest_properties(self, ingest_properties):
        r"""Sets the ingest_properties of this BatchListResourceResponseData.

        **参数解释：** 采集属性。 **取值范围：** 不涉及。

        :param ingest_properties: The ingest_properties of this BatchListResourceResponseData.
        :type ingest_properties: dict(str, str)
        """
        self._ingest_properties = ingest_properties

    @property
    def is_delegated(self):
        r"""Gets the is_delegated of this BatchListResourceResponseData.

        **参数解释：** 是否已托管。 **取值范围：** - true：已经托管。 - false：未托管。

        :return: The is_delegated of this BatchListResourceResponseData.
        :rtype: bool
        """
        return self._is_delegated

    @is_delegated.setter
    def is_delegated(self, is_delegated):
        r"""Sets the is_delegated of this BatchListResourceResponseData.

        **参数解释：** 是否已托管。 **取值范围：** - true：已经托管。 - false：未托管。

        :param is_delegated: The is_delegated of this BatchListResourceResponseData.
        :type is_delegated: bool
        """
        self._is_delegated = is_delegated

    @property
    def inner_ip(self):
        r"""Gets the inner_ip of this BatchListResourceResponseData.

        **参数解释：** 资源内网ip。 **取值范围：** 不涉及。

        :return: The inner_ip of this BatchListResourceResponseData.
        :rtype: str
        """
        return self._inner_ip

    @inner_ip.setter
    def inner_ip(self, inner_ip):
        r"""Sets the inner_ip of this BatchListResourceResponseData.

        **参数解释：** 资源内网ip。 **取值范围：** 不涉及。

        :param inner_ip: The inner_ip of this BatchListResourceResponseData.
        :type inner_ip: str
        """
        self._inner_ip = inner_ip

    @property
    def operable(self):
        r"""Gets the operable of this BatchListResourceResponseData.

        **参数解释：** 用户定义资源是否可运维实例。 **取值范围：** - ENABLE：可运维实例。 - DISABLE：不可运维实例operable字段不存在。

        :return: The operable of this BatchListResourceResponseData.
        :rtype: str
        """
        return self._operable

    @operable.setter
    def operable(self, operable):
        r"""Sets the operable of this BatchListResourceResponseData.

        **参数解释：** 用户定义资源是否可运维实例。 **取值范围：** - ENABLE：可运维实例。 - DISABLE：不可运维实例operable字段不存在。

        :param operable: The operable of this BatchListResourceResponseData.
        :type operable: str
        """
        self._operable = operable

    @property
    def is_associate_group(self):
        r"""Gets the is_associate_group of this BatchListResourceResponseData.

        **参数解释：** 是否已被指定分组关联。 **取值范围：** - true：已被指定分组关联。 - false：未被指定分组关联。

        :return: The is_associate_group of this BatchListResourceResponseData.
        :rtype: bool
        """
        return self._is_associate_group

    @is_associate_group.setter
    def is_associate_group(self, is_associate_group):
        r"""Sets the is_associate_group of this BatchListResourceResponseData.

        **参数解释：** 是否已被指定分组关联。 **取值范围：** - true：已被指定分组关联。 - false：未被指定分组关联。

        :param is_associate_group: The is_associate_group of this BatchListResourceResponseData.
        :type is_associate_group: bool
        """
        self._is_associate_group = is_associate_group

    @property
    def associated_group_list(self):
        r"""Gets the associated_group_list of this BatchListResourceResponseData.

        **参数解释：** 资源所关联的分组信息组成的列表。 **取值范围：** 不涉及。

        :return: The associated_group_list of this BatchListResourceResponseData.
        :rtype: list[str]
        """
        return self._associated_group_list

    @associated_group_list.setter
    def associated_group_list(self, associated_group_list):
        r"""Sets the associated_group_list of this BatchListResourceResponseData.

        **参数解释：** 资源所关联的分组信息组成的列表。 **取值范围：** 不涉及。

        :param associated_group_list: The associated_group_list of this BatchListResourceResponseData.
        :type associated_group_list: list[str]
        """
        self._associated_group_list = associated_group_list

    @property
    def create_time(self):
        r"""Gets the create_time of this BatchListResourceResponseData.

        **参数解释：** 创建时间，参考ISO8601标准格式。 **取值范围：** 不涉及。

        :return: The create_time of this BatchListResourceResponseData.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this BatchListResourceResponseData.

        **参数解释：** 创建时间，参考ISO8601标准格式。 **取值范围：** 不涉及。

        :param create_time: The create_time of this BatchListResourceResponseData.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this BatchListResourceResponseData.

        **参数解释：** 修改时间，参考ISO8601标准格式。 **取值范围：** 不涉及。

        :return: The update_time of this BatchListResourceResponseData.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this BatchListResourceResponseData.

        **参数解释：** 修改时间，参考ISO8601标准格式。 **取值范围：** 不涉及。

        :param update_time: The update_time of this BatchListResourceResponseData.
        :type update_time: datetime
        """
        self._update_time = update_time

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
        if not isinstance(other, BatchListResourceResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
