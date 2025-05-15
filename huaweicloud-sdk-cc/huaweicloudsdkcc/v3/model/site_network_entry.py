# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SiteNetworkEntry:

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
        'name': 'str',
        'description': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'domain_id': 'str',
        'state': 'SiteNetworkStateEnum',
        'enterprise_project_id': 'str',
        'apply_policy_id': 'str',
        'tags': 'list[Tag]',
        'topology': 'SiteNetworkTopologyEnum',
        'connections': 'list[SiteConnection]',
        'sites': 'list[SiteInformation]',
        'hub_site': 'SiteInformation',
        'spoke_sites': 'list[SiteInformation]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'domain_id': 'domain_id',
        'state': 'state',
        'enterprise_project_id': 'enterprise_project_id',
        'apply_policy_id': 'apply_policy_id',
        'tags': 'tags',
        'topology': 'topology',
        'connections': 'connections',
        'sites': 'sites',
        'hub_site': 'hub_site',
        'spoke_sites': 'spoke_sites'
    }

    def __init__(self, id=None, name=None, description=None, created_at=None, updated_at=None, domain_id=None, state=None, enterprise_project_id=None, apply_policy_id=None, tags=None, topology=None, connections=None, sites=None, hub_site=None, spoke_sites=None):
        r"""SiteNetworkEntry

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param name: 实例名称。
        :type name: str
        :param description: 实例描述。不支持 &lt;&gt;。
        :type description: str
        :param created_at: 实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type created_at: datetime
        :param updated_at: 实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type updated_at: datetime
        :param domain_id: 实例所属账号ID。
        :type domain_id: str
        :param state: 
        :type state: :class:`huaweicloudsdkcc.v3.SiteNetworkStateEnum`
        :param enterprise_project_id: 实例所属企业项目ID。
        :type enterprise_project_id: str
        :param apply_policy_id: 应用策略ID。
        :type apply_policy_id: str
        :param tags: 实例标签。
        :type tags: list[:class:`huaweicloudsdkcc.v3.Tag`]
        :param topology: 
        :type topology: :class:`huaweicloudsdkcc.v3.SiteNetworkTopologyEnum`
        :param connections: 分支连接列表。
        :type connections: list[:class:`huaweicloudsdkcc.v3.SiteConnection`]
        :param sites: 点对点拓扑或者网状拓扑中的节点。
        :type sites: list[:class:`huaweicloudsdkcc.v3.SiteInformation`]
        :param hub_site: 
        :type hub_site: :class:`huaweicloudsdkcc.v3.SiteInformation`
        :param spoke_sites: 分支列表。
        :type spoke_sites: list[:class:`huaweicloudsdkcc.v3.SiteInformation`]
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self._domain_id = None
        self._state = None
        self._enterprise_project_id = None
        self._apply_policy_id = None
        self._tags = None
        self._topology = None
        self._connections = None
        self._sites = None
        self._hub_site = None
        self._spoke_sites = None
        self.discriminator = None

        self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.domain_id = domain_id
        self.state = state
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.apply_policy_id = apply_policy_id
        if tags is not None:
            self.tags = tags
        self.topology = topology
        self.connections = connections
        if sites is not None:
            self.sites = sites
        if hub_site is not None:
            self.hub_site = hub_site
        if spoke_sites is not None:
            self.spoke_sites = spoke_sites

    @property
    def id(self):
        r"""Gets the id of this SiteNetworkEntry.

        实例ID。

        :return: The id of this SiteNetworkEntry.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SiteNetworkEntry.

        实例ID。

        :param id: The id of this SiteNetworkEntry.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this SiteNetworkEntry.

        实例名称。

        :return: The name of this SiteNetworkEntry.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SiteNetworkEntry.

        实例名称。

        :param name: The name of this SiteNetworkEntry.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this SiteNetworkEntry.

        实例描述。不支持 <>。

        :return: The description of this SiteNetworkEntry.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SiteNetworkEntry.

        实例描述。不支持 <>。

        :param description: The description of this SiteNetworkEntry.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        r"""Gets the created_at of this SiteNetworkEntry.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The created_at of this SiteNetworkEntry.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this SiteNetworkEntry.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param created_at: The created_at of this SiteNetworkEntry.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this SiteNetworkEntry.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The updated_at of this SiteNetworkEntry.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this SiteNetworkEntry.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param updated_at: The updated_at of this SiteNetworkEntry.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def domain_id(self):
        r"""Gets the domain_id of this SiteNetworkEntry.

        实例所属账号ID。

        :return: The domain_id of this SiteNetworkEntry.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this SiteNetworkEntry.

        实例所属账号ID。

        :param domain_id: The domain_id of this SiteNetworkEntry.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def state(self):
        r"""Gets the state of this SiteNetworkEntry.

        :return: The state of this SiteNetworkEntry.
        :rtype: :class:`huaweicloudsdkcc.v3.SiteNetworkStateEnum`
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this SiteNetworkEntry.

        :param state: The state of this SiteNetworkEntry.
        :type state: :class:`huaweicloudsdkcc.v3.SiteNetworkStateEnum`
        """
        self._state = state

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this SiteNetworkEntry.

        实例所属企业项目ID。

        :return: The enterprise_project_id of this SiteNetworkEntry.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this SiteNetworkEntry.

        实例所属企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this SiteNetworkEntry.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def apply_policy_id(self):
        r"""Gets the apply_policy_id of this SiteNetworkEntry.

        应用策略ID。

        :return: The apply_policy_id of this SiteNetworkEntry.
        :rtype: str
        """
        return self._apply_policy_id

    @apply_policy_id.setter
    def apply_policy_id(self, apply_policy_id):
        r"""Sets the apply_policy_id of this SiteNetworkEntry.

        应用策略ID。

        :param apply_policy_id: The apply_policy_id of this SiteNetworkEntry.
        :type apply_policy_id: str
        """
        self._apply_policy_id = apply_policy_id

    @property
    def tags(self):
        r"""Gets the tags of this SiteNetworkEntry.

        实例标签。

        :return: The tags of this SiteNetworkEntry.
        :rtype: list[:class:`huaweicloudsdkcc.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this SiteNetworkEntry.

        实例标签。

        :param tags: The tags of this SiteNetworkEntry.
        :type tags: list[:class:`huaweicloudsdkcc.v3.Tag`]
        """
        self._tags = tags

    @property
    def topology(self):
        r"""Gets the topology of this SiteNetworkEntry.

        :return: The topology of this SiteNetworkEntry.
        :rtype: :class:`huaweicloudsdkcc.v3.SiteNetworkTopologyEnum`
        """
        return self._topology

    @topology.setter
    def topology(self, topology):
        r"""Sets the topology of this SiteNetworkEntry.

        :param topology: The topology of this SiteNetworkEntry.
        :type topology: :class:`huaweicloudsdkcc.v3.SiteNetworkTopologyEnum`
        """
        self._topology = topology

    @property
    def connections(self):
        r"""Gets the connections of this SiteNetworkEntry.

        分支连接列表。

        :return: The connections of this SiteNetworkEntry.
        :rtype: list[:class:`huaweicloudsdkcc.v3.SiteConnection`]
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        r"""Sets the connections of this SiteNetworkEntry.

        分支连接列表。

        :param connections: The connections of this SiteNetworkEntry.
        :type connections: list[:class:`huaweicloudsdkcc.v3.SiteConnection`]
        """
        self._connections = connections

    @property
    def sites(self):
        r"""Gets the sites of this SiteNetworkEntry.

        点对点拓扑或者网状拓扑中的节点。

        :return: The sites of this SiteNetworkEntry.
        :rtype: list[:class:`huaweicloudsdkcc.v3.SiteInformation`]
        """
        return self._sites

    @sites.setter
    def sites(self, sites):
        r"""Sets the sites of this SiteNetworkEntry.

        点对点拓扑或者网状拓扑中的节点。

        :param sites: The sites of this SiteNetworkEntry.
        :type sites: list[:class:`huaweicloudsdkcc.v3.SiteInformation`]
        """
        self._sites = sites

    @property
    def hub_site(self):
        r"""Gets the hub_site of this SiteNetworkEntry.

        :return: The hub_site of this SiteNetworkEntry.
        :rtype: :class:`huaweicloudsdkcc.v3.SiteInformation`
        """
        return self._hub_site

    @hub_site.setter
    def hub_site(self, hub_site):
        r"""Sets the hub_site of this SiteNetworkEntry.

        :param hub_site: The hub_site of this SiteNetworkEntry.
        :type hub_site: :class:`huaweicloudsdkcc.v3.SiteInformation`
        """
        self._hub_site = hub_site

    @property
    def spoke_sites(self):
        r"""Gets the spoke_sites of this SiteNetworkEntry.

        分支列表。

        :return: The spoke_sites of this SiteNetworkEntry.
        :rtype: list[:class:`huaweicloudsdkcc.v3.SiteInformation`]
        """
        return self._spoke_sites

    @spoke_sites.setter
    def spoke_sites(self, spoke_sites):
        r"""Sets the spoke_sites of this SiteNetworkEntry.

        分支列表。

        :param spoke_sites: The spoke_sites of this SiteNetworkEntry.
        :type spoke_sites: list[:class:`huaweicloudsdkcc.v3.SiteInformation`]
        """
        self._spoke_sites = spoke_sites

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
        if not isinstance(other, SiteNetworkEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
