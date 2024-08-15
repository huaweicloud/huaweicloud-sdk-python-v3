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
        'name': 'str',
        'provider': 'str',
        'type': 'str',
        'project_id': 'str',
        'region_id': 'str',
        'ep_id': 'str',
        'tags': 'list[Tag]',
        'agent_id': 'str',
        'agent_state': 'str',
        'properties': 'dict(str, object)',
        'ingest_properties': 'dict(str, str)',
        'is_delegated': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'resource_id': 'resource_id',
        'name': 'name',
        'provider': 'provider',
        'type': 'type',
        'project_id': 'project_id',
        'region_id': 'region_id',
        'ep_id': 'ep_id',
        'tags': 'tags',
        'agent_id': 'agent_id',
        'agent_state': 'agent_state',
        'properties': 'properties',
        'ingest_properties': 'ingest_properties',
        'is_delegated': 'is_delegated'
    }

    def __init__(self, id=None, resource_id=None, name=None, provider=None, type=None, project_id=None, region_id=None, ep_id=None, tags=None, agent_id=None, agent_state=None, properties=None, ingest_properties=None, is_delegated=None):
        """BatchListResourceResponseData

        The model defined in huaweicloud sdk

        :param id: CMDB分配的资源ID
        :type id: str
        :param resource_id: 云服务分配的资源ID
        :type resource_id: str
        :param name: 资源名称
        :type name: str
        :param provider: 云服务名称
        :type provider: str
        :param type: 资源类型
        :type type: str
        :param project_id: Openstack中的项目I
        :type project_id: str
        :param region_id: region ID
        :type region_id: str
        :param ep_id: 企业项目ID
        :type ep_id: str
        :param tags: 资源标签
        :type tags: list[:class:`huaweicloudsdkcoc.v1.Tag`]
        :param agent_id: uniAgent唯一id
        :type agent_id: str
        :param agent_state: uniAgent状态
        :type agent_state: str
        :param properties: 资源详细属性
        :type properties: dict(str, object)
        :param ingest_properties: 采集属性
        :type ingest_properties: dict(str, str)
        :param is_delegated: 是否已托管
        :type is_delegated: bool
        """
        
        

        self._id = None
        self._resource_id = None
        self._name = None
        self._provider = None
        self._type = None
        self._project_id = None
        self._region_id = None
        self._ep_id = None
        self._tags = None
        self._agent_id = None
        self._agent_state = None
        self._properties = None
        self._ingest_properties = None
        self._is_delegated = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if resource_id is not None:
            self.resource_id = resource_id
        if name is not None:
            self.name = name
        if provider is not None:
            self.provider = provider
        if type is not None:
            self.type = type
        if project_id is not None:
            self.project_id = project_id
        if region_id is not None:
            self.region_id = region_id
        if ep_id is not None:
            self.ep_id = ep_id
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

    @property
    def id(self):
        """Gets the id of this BatchListResourceResponseData.

        CMDB分配的资源ID

        :return: The id of this BatchListResourceResponseData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BatchListResourceResponseData.

        CMDB分配的资源ID

        :param id: The id of this BatchListResourceResponseData.
        :type id: str
        """
        self._id = id

    @property
    def resource_id(self):
        """Gets the resource_id of this BatchListResourceResponseData.

        云服务分配的资源ID

        :return: The resource_id of this BatchListResourceResponseData.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this BatchListResourceResponseData.

        云服务分配的资源ID

        :param resource_id: The resource_id of this BatchListResourceResponseData.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def name(self):
        """Gets the name of this BatchListResourceResponseData.

        资源名称

        :return: The name of this BatchListResourceResponseData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BatchListResourceResponseData.

        资源名称

        :param name: The name of this BatchListResourceResponseData.
        :type name: str
        """
        self._name = name

    @property
    def provider(self):
        """Gets the provider of this BatchListResourceResponseData.

        云服务名称

        :return: The provider of this BatchListResourceResponseData.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this BatchListResourceResponseData.

        云服务名称

        :param provider: The provider of this BatchListResourceResponseData.
        :type provider: str
        """
        self._provider = provider

    @property
    def type(self):
        """Gets the type of this BatchListResourceResponseData.

        资源类型

        :return: The type of this BatchListResourceResponseData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BatchListResourceResponseData.

        资源类型

        :param type: The type of this BatchListResourceResponseData.
        :type type: str
        """
        self._type = type

    @property
    def project_id(self):
        """Gets the project_id of this BatchListResourceResponseData.

        Openstack中的项目I

        :return: The project_id of this BatchListResourceResponseData.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this BatchListResourceResponseData.

        Openstack中的项目I

        :param project_id: The project_id of this BatchListResourceResponseData.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region_id(self):
        """Gets the region_id of this BatchListResourceResponseData.

        region ID

        :return: The region_id of this BatchListResourceResponseData.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this BatchListResourceResponseData.

        region ID

        :param region_id: The region_id of this BatchListResourceResponseData.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def ep_id(self):
        """Gets the ep_id of this BatchListResourceResponseData.

        企业项目ID

        :return: The ep_id of this BatchListResourceResponseData.
        :rtype: str
        """
        return self._ep_id

    @ep_id.setter
    def ep_id(self, ep_id):
        """Sets the ep_id of this BatchListResourceResponseData.

        企业项目ID

        :param ep_id: The ep_id of this BatchListResourceResponseData.
        :type ep_id: str
        """
        self._ep_id = ep_id

    @property
    def tags(self):
        """Gets the tags of this BatchListResourceResponseData.

        资源标签

        :return: The tags of this BatchListResourceResponseData.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this BatchListResourceResponseData.

        资源标签

        :param tags: The tags of this BatchListResourceResponseData.
        :type tags: list[:class:`huaweicloudsdkcoc.v1.Tag`]
        """
        self._tags = tags

    @property
    def agent_id(self):
        """Gets the agent_id of this BatchListResourceResponseData.

        uniAgent唯一id

        :return: The agent_id of this BatchListResourceResponseData.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this BatchListResourceResponseData.

        uniAgent唯一id

        :param agent_id: The agent_id of this BatchListResourceResponseData.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def agent_state(self):
        """Gets the agent_state of this BatchListResourceResponseData.

        uniAgent状态

        :return: The agent_state of this BatchListResourceResponseData.
        :rtype: str
        """
        return self._agent_state

    @agent_state.setter
    def agent_state(self, agent_state):
        """Sets the agent_state of this BatchListResourceResponseData.

        uniAgent状态

        :param agent_state: The agent_state of this BatchListResourceResponseData.
        :type agent_state: str
        """
        self._agent_state = agent_state

    @property
    def properties(self):
        """Gets the properties of this BatchListResourceResponseData.

        资源详细属性

        :return: The properties of this BatchListResourceResponseData.
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this BatchListResourceResponseData.

        资源详细属性

        :param properties: The properties of this BatchListResourceResponseData.
        :type properties: dict(str, object)
        """
        self._properties = properties

    @property
    def ingest_properties(self):
        """Gets the ingest_properties of this BatchListResourceResponseData.

        采集属性

        :return: The ingest_properties of this BatchListResourceResponseData.
        :rtype: dict(str, str)
        """
        return self._ingest_properties

    @ingest_properties.setter
    def ingest_properties(self, ingest_properties):
        """Sets the ingest_properties of this BatchListResourceResponseData.

        采集属性

        :param ingest_properties: The ingest_properties of this BatchListResourceResponseData.
        :type ingest_properties: dict(str, str)
        """
        self._ingest_properties = ingest_properties

    @property
    def is_delegated(self):
        """Gets the is_delegated of this BatchListResourceResponseData.

        是否已托管

        :return: The is_delegated of this BatchListResourceResponseData.
        :rtype: bool
        """
        return self._is_delegated

    @is_delegated.setter
    def is_delegated(self, is_delegated):
        """Sets the is_delegated of this BatchListResourceResponseData.

        是否已托管

        :param is_delegated: The is_delegated of this BatchListResourceResponseData.
        :type is_delegated: bool
        """
        self._is_delegated = is_delegated

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
