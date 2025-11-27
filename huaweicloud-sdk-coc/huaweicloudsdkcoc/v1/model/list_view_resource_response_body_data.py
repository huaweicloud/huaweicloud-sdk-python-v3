# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListViewResourceResponseBodyData:

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
        'view_id': 'str',
        'rms_resource_id': 'str',
        'resource_id': 'str',
        'domain_id': 'str',
        'name': 'str',
        'ep_id': 'str',
        'ep_name': 'str',
        'project_id': 'str',
        'provider': 'str',
        'type': 'str',
        'region_id': 'str',
        'tags': 'list[ListViewResourceResponseBodyTags]',
        'properties': 'object',
        'ingest_properties': 'object',
        'agent_id': 'str',
        'agent_state': 'str',
        'inner_ip': 'str',
        'associated_group_list': 'object'
    }

    attribute_map = {
        'id': 'id',
        'view_id': 'view_id',
        'rms_resource_id': 'rms_resource_id',
        'resource_id': 'resource_id',
        'domain_id': 'domain_id',
        'name': 'name',
        'ep_id': 'ep_id',
        'ep_name': 'ep_name',
        'project_id': 'project_id',
        'provider': 'provider',
        'type': 'type',
        'region_id': 'region_id',
        'tags': 'tags',
        'properties': 'properties',
        'ingest_properties': 'ingest_properties',
        'agent_id': 'agent_id',
        'agent_state': 'agent_state',
        'inner_ip': 'inner_ip',
        'associated_group_list': 'associated_group_list'
    }

    def __init__(self, id=None, view_id=None, rms_resource_id=None, resource_id=None, domain_id=None, name=None, ep_id=None, ep_name=None, project_id=None, provider=None, type=None, region_id=None, tags=None, properties=None, ingest_properties=None, agent_id=None, agent_state=None, inner_ip=None, associated_group_list=None):
        r"""ListViewResourceResponseBodyData

        The model defined in huaweicloud sdk

        :param id: **参数解释：** id。 **取值范围：** 不涉及。
        :type id: str
        :param view_id: **参数解释：** 视图id。 **取值范围：** 不涉及。
        :type view_id: str
        :param rms_resource_id: **参数解释：** 对应rms_resource集合中的id值。 **取值范围：** 不涉及。
        :type rms_resource_id: str
        :param resource_id: **参数解释：** 资源id。。 **取值范围：** 跨账号资源下且视图管理下对应的资源id。
        :type resource_id: str
        :param domain_id: **参数解释：** 租户id。 **取值范围：** 用户登录租户对应的账号ID。
        :type domain_id: str
        :param name: **参数解释：** 资源名称。 **取值范围：** 视图下的资源名称。
        :type name: str
        :param ep_id: **参数解释：** 企业项目ID。 **取值范围：** 请选择[[企业管理](https://support.huaweicloud.com/usermanual-em/em_eps_qs_0400.html)](tag:hws)[[企业管理](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/em_eps_qs_0400.html)](tag:hws_hk)中存在的项目ID。。
        :type ep_id: str
        :param ep_name: **参数解释：** 企业项目名称。 **取值范围：** 不涉及。
        :type ep_name: str
        :param project_id: **参数解释：** Openstack中的项目ID。 **取值范围：** 不涉及。
        :type project_id: str
        :param provider: **参数解释：** 云服务名称。 **取值范围：** 不涉及。
        :type provider: str
        :param type: **参数解释：** 资源类型。 **取值范围：** 不涉及。
        :type type: str
        :param region_id: **参数解释：** 区域id。 **取值范围：** 不涉及。
        :type region_id: str
        :param tags: **参数解释：** 标签键值对。 **取值范围：** 不涉及。
        :type tags: list[:class:`huaweicloudsdkcoc.v1.ListViewResourceResponseBodyTags`]
        :param properties: **参数解释：** 存储资源的附加字段信息，通常用于展示、筛选等。 **取值范围：** 不涉及。
        :type properties: object
        :param ingest_properties: **参数解释：** 数据采集属性,描述视图系统采集该资源时所记录的附加信息。 **取值范围：** 不涉及。
        :type ingest_properties: object
        :param agent_id: **参数解释：** uniagent的id值。 **取值范围：** 不涉及。
        :type agent_id: str
        :param agent_state: **参数解释：** uniagent的状态。 **取值范围：** 不涉及。
        :type agent_state: str
        :param inner_ip: **参数解释：** 资源内网ip。 **取值范围：** 不涉及。
        :type inner_ip: str
        :param associated_group_list: **参数解释：** 绑定的资源组信息列表。 **取值范围：** 不涉及。
        :type associated_group_list: object
        """
        
        

        self._id = None
        self._view_id = None
        self._rms_resource_id = None
        self._resource_id = None
        self._domain_id = None
        self._name = None
        self._ep_id = None
        self._ep_name = None
        self._project_id = None
        self._provider = None
        self._type = None
        self._region_id = None
        self._tags = None
        self._properties = None
        self._ingest_properties = None
        self._agent_id = None
        self._agent_state = None
        self._inner_ip = None
        self._associated_group_list = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if view_id is not None:
            self.view_id = view_id
        if rms_resource_id is not None:
            self.rms_resource_id = rms_resource_id
        if resource_id is not None:
            self.resource_id = resource_id
        if domain_id is not None:
            self.domain_id = domain_id
        if name is not None:
            self.name = name
        if ep_id is not None:
            self.ep_id = ep_id
        if ep_name is not None:
            self.ep_name = ep_name
        if project_id is not None:
            self.project_id = project_id
        if provider is not None:
            self.provider = provider
        if type is not None:
            self.type = type
        if region_id is not None:
            self.region_id = region_id
        if tags is not None:
            self.tags = tags
        if properties is not None:
            self.properties = properties
        if ingest_properties is not None:
            self.ingest_properties = ingest_properties
        if agent_id is not None:
            self.agent_id = agent_id
        if agent_state is not None:
            self.agent_state = agent_state
        if inner_ip is not None:
            self.inner_ip = inner_ip
        if associated_group_list is not None:
            self.associated_group_list = associated_group_list

    @property
    def id(self):
        r"""Gets the id of this ListViewResourceResponseBodyData.

        **参数解释：** id。 **取值范围：** 不涉及。

        :return: The id of this ListViewResourceResponseBodyData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListViewResourceResponseBodyData.

        **参数解释：** id。 **取值范围：** 不涉及。

        :param id: The id of this ListViewResourceResponseBodyData.
        :type id: str
        """
        self._id = id

    @property
    def view_id(self):
        r"""Gets the view_id of this ListViewResourceResponseBodyData.

        **参数解释：** 视图id。 **取值范围：** 不涉及。

        :return: The view_id of this ListViewResourceResponseBodyData.
        :rtype: str
        """
        return self._view_id

    @view_id.setter
    def view_id(self, view_id):
        r"""Sets the view_id of this ListViewResourceResponseBodyData.

        **参数解释：** 视图id。 **取值范围：** 不涉及。

        :param view_id: The view_id of this ListViewResourceResponseBodyData.
        :type view_id: str
        """
        self._view_id = view_id

    @property
    def rms_resource_id(self):
        r"""Gets the rms_resource_id of this ListViewResourceResponseBodyData.

        **参数解释：** 对应rms_resource集合中的id值。 **取值范围：** 不涉及。

        :return: The rms_resource_id of this ListViewResourceResponseBodyData.
        :rtype: str
        """
        return self._rms_resource_id

    @rms_resource_id.setter
    def rms_resource_id(self, rms_resource_id):
        r"""Sets the rms_resource_id of this ListViewResourceResponseBodyData.

        **参数解释：** 对应rms_resource集合中的id值。 **取值范围：** 不涉及。

        :param rms_resource_id: The rms_resource_id of this ListViewResourceResponseBodyData.
        :type rms_resource_id: str
        """
        self._rms_resource_id = rms_resource_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ListViewResourceResponseBodyData.

        **参数解释：** 资源id。。 **取值范围：** 跨账号资源下且视图管理下对应的资源id。

        :return: The resource_id of this ListViewResourceResponseBodyData.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ListViewResourceResponseBodyData.

        **参数解释：** 资源id。。 **取值范围：** 跨账号资源下且视图管理下对应的资源id。

        :param resource_id: The resource_id of this ListViewResourceResponseBodyData.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ListViewResourceResponseBodyData.

        **参数解释：** 租户id。 **取值范围：** 用户登录租户对应的账号ID。

        :return: The domain_id of this ListViewResourceResponseBodyData.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ListViewResourceResponseBodyData.

        **参数解释：** 租户id。 **取值范围：** 用户登录租户对应的账号ID。

        :param domain_id: The domain_id of this ListViewResourceResponseBodyData.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def name(self):
        r"""Gets the name of this ListViewResourceResponseBodyData.

        **参数解释：** 资源名称。 **取值范围：** 视图下的资源名称。

        :return: The name of this ListViewResourceResponseBodyData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListViewResourceResponseBodyData.

        **参数解释：** 资源名称。 **取值范围：** 视图下的资源名称。

        :param name: The name of this ListViewResourceResponseBodyData.
        :type name: str
        """
        self._name = name

    @property
    def ep_id(self):
        r"""Gets the ep_id of this ListViewResourceResponseBodyData.

        **参数解释：** 企业项目ID。 **取值范围：** 请选择[[企业管理](https://support.huaweicloud.com/usermanual-em/em_eps_qs_0400.html)](tag:hws)[[企业管理](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/em_eps_qs_0400.html)](tag:hws_hk)中存在的项目ID。。

        :return: The ep_id of this ListViewResourceResponseBodyData.
        :rtype: str
        """
        return self._ep_id

    @ep_id.setter
    def ep_id(self, ep_id):
        r"""Sets the ep_id of this ListViewResourceResponseBodyData.

        **参数解释：** 企业项目ID。 **取值范围：** 请选择[[企业管理](https://support.huaweicloud.com/usermanual-em/em_eps_qs_0400.html)](tag:hws)[[企业管理](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/em_eps_qs_0400.html)](tag:hws_hk)中存在的项目ID。。

        :param ep_id: The ep_id of this ListViewResourceResponseBodyData.
        :type ep_id: str
        """
        self._ep_id = ep_id

    @property
    def ep_name(self):
        r"""Gets the ep_name of this ListViewResourceResponseBodyData.

        **参数解释：** 企业项目名称。 **取值范围：** 不涉及。

        :return: The ep_name of this ListViewResourceResponseBodyData.
        :rtype: str
        """
        return self._ep_name

    @ep_name.setter
    def ep_name(self, ep_name):
        r"""Sets the ep_name of this ListViewResourceResponseBodyData.

        **参数解释：** 企业项目名称。 **取值范围：** 不涉及。

        :param ep_name: The ep_name of this ListViewResourceResponseBodyData.
        :type ep_name: str
        """
        self._ep_name = ep_name

    @property
    def project_id(self):
        r"""Gets the project_id of this ListViewResourceResponseBodyData.

        **参数解释：** Openstack中的项目ID。 **取值范围：** 不涉及。

        :return: The project_id of this ListViewResourceResponseBodyData.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListViewResourceResponseBodyData.

        **参数解释：** Openstack中的项目ID。 **取值范围：** 不涉及。

        :param project_id: The project_id of this ListViewResourceResponseBodyData.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def provider(self):
        r"""Gets the provider of this ListViewResourceResponseBodyData.

        **参数解释：** 云服务名称。 **取值范围：** 不涉及。

        :return: The provider of this ListViewResourceResponseBodyData.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this ListViewResourceResponseBodyData.

        **参数解释：** 云服务名称。 **取值范围：** 不涉及。

        :param provider: The provider of this ListViewResourceResponseBodyData.
        :type provider: str
        """
        self._provider = provider

    @property
    def type(self):
        r"""Gets the type of this ListViewResourceResponseBodyData.

        **参数解释：** 资源类型。 **取值范围：** 不涉及。

        :return: The type of this ListViewResourceResponseBodyData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListViewResourceResponseBodyData.

        **参数解释：** 资源类型。 **取值范围：** 不涉及。

        :param type: The type of this ListViewResourceResponseBodyData.
        :type type: str
        """
        self._type = type

    @property
    def region_id(self):
        r"""Gets the region_id of this ListViewResourceResponseBodyData.

        **参数解释：** 区域id。 **取值范围：** 不涉及。

        :return: The region_id of this ListViewResourceResponseBodyData.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ListViewResourceResponseBodyData.

        **参数解释：** 区域id。 **取值范围：** 不涉及。

        :param region_id: The region_id of this ListViewResourceResponseBodyData.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def tags(self):
        r"""Gets the tags of this ListViewResourceResponseBodyData.

        **参数解释：** 标签键值对。 **取值范围：** 不涉及。

        :return: The tags of this ListViewResourceResponseBodyData.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ListViewResourceResponseBodyTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListViewResourceResponseBodyData.

        **参数解释：** 标签键值对。 **取值范围：** 不涉及。

        :param tags: The tags of this ListViewResourceResponseBodyData.
        :type tags: list[:class:`huaweicloudsdkcoc.v1.ListViewResourceResponseBodyTags`]
        """
        self._tags = tags

    @property
    def properties(self):
        r"""Gets the properties of this ListViewResourceResponseBodyData.

        **参数解释：** 存储资源的附加字段信息，通常用于展示、筛选等。 **取值范围：** 不涉及。

        :return: The properties of this ListViewResourceResponseBodyData.
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this ListViewResourceResponseBodyData.

        **参数解释：** 存储资源的附加字段信息，通常用于展示、筛选等。 **取值范围：** 不涉及。

        :param properties: The properties of this ListViewResourceResponseBodyData.
        :type properties: object
        """
        self._properties = properties

    @property
    def ingest_properties(self):
        r"""Gets the ingest_properties of this ListViewResourceResponseBodyData.

        **参数解释：** 数据采集属性,描述视图系统采集该资源时所记录的附加信息。 **取值范围：** 不涉及。

        :return: The ingest_properties of this ListViewResourceResponseBodyData.
        :rtype: object
        """
        return self._ingest_properties

    @ingest_properties.setter
    def ingest_properties(self, ingest_properties):
        r"""Sets the ingest_properties of this ListViewResourceResponseBodyData.

        **参数解释：** 数据采集属性,描述视图系统采集该资源时所记录的附加信息。 **取值范围：** 不涉及。

        :param ingest_properties: The ingest_properties of this ListViewResourceResponseBodyData.
        :type ingest_properties: object
        """
        self._ingest_properties = ingest_properties

    @property
    def agent_id(self):
        r"""Gets the agent_id of this ListViewResourceResponseBodyData.

        **参数解释：** uniagent的id值。 **取值范围：** 不涉及。

        :return: The agent_id of this ListViewResourceResponseBodyData.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this ListViewResourceResponseBodyData.

        **参数解释：** uniagent的id值。 **取值范围：** 不涉及。

        :param agent_id: The agent_id of this ListViewResourceResponseBodyData.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def agent_state(self):
        r"""Gets the agent_state of this ListViewResourceResponseBodyData.

        **参数解释：** uniagent的状态。 **取值范围：** 不涉及。

        :return: The agent_state of this ListViewResourceResponseBodyData.
        :rtype: str
        """
        return self._agent_state

    @agent_state.setter
    def agent_state(self, agent_state):
        r"""Sets the agent_state of this ListViewResourceResponseBodyData.

        **参数解释：** uniagent的状态。 **取值范围：** 不涉及。

        :param agent_state: The agent_state of this ListViewResourceResponseBodyData.
        :type agent_state: str
        """
        self._agent_state = agent_state

    @property
    def inner_ip(self):
        r"""Gets the inner_ip of this ListViewResourceResponseBodyData.

        **参数解释：** 资源内网ip。 **取值范围：** 不涉及。

        :return: The inner_ip of this ListViewResourceResponseBodyData.
        :rtype: str
        """
        return self._inner_ip

    @inner_ip.setter
    def inner_ip(self, inner_ip):
        r"""Sets the inner_ip of this ListViewResourceResponseBodyData.

        **参数解释：** 资源内网ip。 **取值范围：** 不涉及。

        :param inner_ip: The inner_ip of this ListViewResourceResponseBodyData.
        :type inner_ip: str
        """
        self._inner_ip = inner_ip

    @property
    def associated_group_list(self):
        r"""Gets the associated_group_list of this ListViewResourceResponseBodyData.

        **参数解释：** 绑定的资源组信息列表。 **取值范围：** 不涉及。

        :return: The associated_group_list of this ListViewResourceResponseBodyData.
        :rtype: object
        """
        return self._associated_group_list

    @associated_group_list.setter
    def associated_group_list(self, associated_group_list):
        r"""Sets the associated_group_list of this ListViewResourceResponseBodyData.

        **参数解释：** 绑定的资源组信息列表。 **取值范围：** 不涉及。

        :param associated_group_list: The associated_group_list of this ListViewResourceResponseBodyData.
        :type associated_group_list: object
        """
        self._associated_group_list = associated_group_list

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
        if not isinstance(other, ListViewResourceResponseBodyData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
