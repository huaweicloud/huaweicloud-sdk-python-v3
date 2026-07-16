# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreRunAgentRuntimeBasic:

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
        'description': 'str',
        'name': 'str',
        'latest_version': 'str',
        'created_at': 'datetime',
        'agent_gateway_id': 'str',
        'updated_at': 'datetime',
        'workload_identity_urn': 'str',
        'tags': 'list[CoreRunTagItemResp]',
        'arch': 'str'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'name': 'name',
        'latest_version': 'latest_version',
        'created_at': 'created_at',
        'agent_gateway_id': 'agent_gateway_id',
        'updated_at': 'updated_at',
        'workload_identity_urn': 'workload_identity_urn',
        'tags': 'tags',
        'arch': 'arch'
    }

    def __init__(self, id=None, description=None, name=None, latest_version=None, created_at=None, agent_gateway_id=None, updated_at=None, workload_identity_urn=None, tags=None, arch=None):
        r"""CoreRunAgentRuntimeBasic

        The model defined in huaweicloud sdk

        :param id: **参数解释**: AgentRuntime唯一标识。 
        :type id: str
        :param description: **参数解释**: 描述信息。 
        :type description: str
        :param name: **参数解释**: Agent名称。 
        :type name: str
        :param latest_version: **参数解释**: 最新版本名称。 
        :type latest_version: str
        :param created_at: **参数解释**: 创建时间。 
        :type created_at: datetime
        :param agent_gateway_id: **参数解释**: Agent Gateway ID。 
        :type agent_gateway_id: str
        :param updated_at: **参数解释**: 最后更新时间。 
        :type updated_at: datetime
        :param workload_identity_urn: **参数解释**: Identity URN。 
        :type workload_identity_urn: str
        :param tags: **参数解释**: 标签配置列表。 
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreRunTagItemResp`]
        :param arch: **参数解释**: 运行时架构。 **取值范围**: arm64、x86_64
        :type arch: str
        """
        
        

        self._id = None
        self._description = None
        self._name = None
        self._latest_version = None
        self._created_at = None
        self._agent_gateway_id = None
        self._updated_at = None
        self._workload_identity_urn = None
        self._tags = None
        self._arch = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if latest_version is not None:
            self.latest_version = latest_version
        if created_at is not None:
            self.created_at = created_at
        if agent_gateway_id is not None:
            self.agent_gateway_id = agent_gateway_id
        if updated_at is not None:
            self.updated_at = updated_at
        if workload_identity_urn is not None:
            self.workload_identity_urn = workload_identity_urn
        if tags is not None:
            self.tags = tags
        if arch is not None:
            self.arch = arch

    @property
    def id(self):
        r"""Gets the id of this CoreRunAgentRuntimeBasic.

        **参数解释**: AgentRuntime唯一标识。 

        :return: The id of this CoreRunAgentRuntimeBasic.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CoreRunAgentRuntimeBasic.

        **参数解释**: AgentRuntime唯一标识。 

        :param id: The id of this CoreRunAgentRuntimeBasic.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        r"""Gets the description of this CoreRunAgentRuntimeBasic.

        **参数解释**: 描述信息。 

        :return: The description of this CoreRunAgentRuntimeBasic.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CoreRunAgentRuntimeBasic.

        **参数解释**: 描述信息。 

        :param description: The description of this CoreRunAgentRuntimeBasic.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        r"""Gets the name of this CoreRunAgentRuntimeBasic.

        **参数解释**: Agent名称。 

        :return: The name of this CoreRunAgentRuntimeBasic.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CoreRunAgentRuntimeBasic.

        **参数解释**: Agent名称。 

        :param name: The name of this CoreRunAgentRuntimeBasic.
        :type name: str
        """
        self._name = name

    @property
    def latest_version(self):
        r"""Gets the latest_version of this CoreRunAgentRuntimeBasic.

        **参数解释**: 最新版本名称。 

        :return: The latest_version of this CoreRunAgentRuntimeBasic.
        :rtype: str
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        r"""Sets the latest_version of this CoreRunAgentRuntimeBasic.

        **参数解释**: 最新版本名称。 

        :param latest_version: The latest_version of this CoreRunAgentRuntimeBasic.
        :type latest_version: str
        """
        self._latest_version = latest_version

    @property
    def created_at(self):
        r"""Gets the created_at of this CoreRunAgentRuntimeBasic.

        **参数解释**: 创建时间。 

        :return: The created_at of this CoreRunAgentRuntimeBasic.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CoreRunAgentRuntimeBasic.

        **参数解释**: 创建时间。 

        :param created_at: The created_at of this CoreRunAgentRuntimeBasic.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def agent_gateway_id(self):
        r"""Gets the agent_gateway_id of this CoreRunAgentRuntimeBasic.

        **参数解释**: Agent Gateway ID。 

        :return: The agent_gateway_id of this CoreRunAgentRuntimeBasic.
        :rtype: str
        """
        return self._agent_gateway_id

    @agent_gateway_id.setter
    def agent_gateway_id(self, agent_gateway_id):
        r"""Sets the agent_gateway_id of this CoreRunAgentRuntimeBasic.

        **参数解释**: Agent Gateway ID。 

        :param agent_gateway_id: The agent_gateway_id of this CoreRunAgentRuntimeBasic.
        :type agent_gateway_id: str
        """
        self._agent_gateway_id = agent_gateway_id

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CoreRunAgentRuntimeBasic.

        **参数解释**: 最后更新时间。 

        :return: The updated_at of this CoreRunAgentRuntimeBasic.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CoreRunAgentRuntimeBasic.

        **参数解释**: 最后更新时间。 

        :param updated_at: The updated_at of this CoreRunAgentRuntimeBasic.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def workload_identity_urn(self):
        r"""Gets the workload_identity_urn of this CoreRunAgentRuntimeBasic.

        **参数解释**: Identity URN。 

        :return: The workload_identity_urn of this CoreRunAgentRuntimeBasic.
        :rtype: str
        """
        return self._workload_identity_urn

    @workload_identity_urn.setter
    def workload_identity_urn(self, workload_identity_urn):
        r"""Sets the workload_identity_urn of this CoreRunAgentRuntimeBasic.

        **参数解释**: Identity URN。 

        :param workload_identity_urn: The workload_identity_urn of this CoreRunAgentRuntimeBasic.
        :type workload_identity_urn: str
        """
        self._workload_identity_urn = workload_identity_urn

    @property
    def tags(self):
        r"""Gets the tags of this CoreRunAgentRuntimeBasic.

        **参数解释**: 标签配置列表。 

        :return: The tags of this CoreRunAgentRuntimeBasic.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreRunTagItemResp`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CoreRunAgentRuntimeBasic.

        **参数解释**: 标签配置列表。 

        :param tags: The tags of this CoreRunAgentRuntimeBasic.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreRunTagItemResp`]
        """
        self._tags = tags

    @property
    def arch(self):
        r"""Gets the arch of this CoreRunAgentRuntimeBasic.

        **参数解释**: 运行时架构。 **取值范围**: arm64、x86_64

        :return: The arch of this CoreRunAgentRuntimeBasic.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this CoreRunAgentRuntimeBasic.

        **参数解释**: 运行时架构。 **取值范围**: arm64、x86_64

        :param arch: The arch of this CoreRunAgentRuntimeBasic.
        :type arch: str
        """
        self._arch = arch

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
        if not isinstance(other, CoreRunAgentRuntimeBasic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
