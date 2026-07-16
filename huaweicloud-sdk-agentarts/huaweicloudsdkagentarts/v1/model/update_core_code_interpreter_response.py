# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCoreCodeInterpreterResponse(SdkResponse):

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
        'execution_agency_name': 'str',
        'agent_gateway_id': 'str',
        'workload_identity': 'CoreToolsWorkloadIdentity',
        'access_endpoint': 'str',
        'observability': 'CoreToolsObservability',
        'tags': 'list[CoreToolsTag]',
        'status': 'str',
        'updated_by': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'execution_agency_name': 'execution_agency_name',
        'agent_gateway_id': 'agent_gateway_id',
        'workload_identity': 'workload_identity',
        'access_endpoint': 'access_endpoint',
        'observability': 'observability',
        'tags': 'tags',
        'status': 'status',
        'updated_by': 'updated_by'
    }

    def __init__(self, id=None, name=None, description=None, created_at=None, updated_at=None, execution_agency_name=None, agent_gateway_id=None, workload_identity=None, access_endpoint=None, observability=None, tags=None, status=None, updated_by=None):
        r"""UpdateCoreCodeInterpreterResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 工具ID。 **取值范围：** 符合UUID规则^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$的36位字符串。
        :type id: str
        :param name: **参数解释：** 工具的名称。 **取值范围：** 符合正则^[a-z][a-z0-9-]{0,38}[a-z0-9]$，即必须以小写字母开头，小写字母或数字结尾，中间可包含数字、小写字母、中划线，字符长度必须在2-40个字符之间。
        :type name: str
        :param description: **参数解释：** 工具的描述。 **取值范围：** 任意字符，长度不能超过4096个字符
        :type description: str
        :param created_at: **参数解释：** 创建时间。 **取值范围：** ISO 8601格式的时间字符串，例如：2026-04-09T08:29:59.922+00:00。
        :type created_at: datetime
        :param updated_at: **参数解释：** 更新时间。 **取值范围：** ISO 8601格式的时间字符串，例如：2026-04-09T08:29:59.922+00:00。
        :type updated_at: datetime
        :param execution_agency_name: **参数解释：** 为工具提供访问云服务的权限的IAM委托名。 **取值范围：** IAM委托名长度必须在1-64个字符之间，字符规则以IAM服务校验规则为准。
        :type execution_agency_name: str
        :param agent_gateway_id: **参数解释：** 工具入口的AgentGateway的ID。 **取值范围：** 符合UUID规则 ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$的36位字符串。
        :type agent_gateway_id: str
        :param workload_identity: 
        :type workload_identity: :class:`huaweicloudsdkagentarts.v1.CoreToolsWorkloadIdentity`
        :param access_endpoint: **参数解释：** 访问域名。 **取值范围：** 不涉及。
        :type access_endpoint: str
        :param observability: 
        :type observability: :class:`huaweicloudsdkagentarts.v1.CoreToolsObservability`
        :param tags: **参数解释：** 资源标签。 **取值范围：** 不涉及。
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreToolsTag`]
        :param status: **参数解释：** 工具状态。 **取值范围：** - RUNNING：运行中。 - DELETING：删除中。 - DELETE_FAILED：删除失败。
        :type status: str
        :param updated_by: **参数解释：** 更新用户。 **取值范围：** 更新用户的IAM用户ID。
        :type updated_by: str
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self._execution_agency_name = None
        self._agent_gateway_id = None
        self._workload_identity = None
        self._access_endpoint = None
        self._observability = None
        self._tags = None
        self._status = None
        self._updated_by = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if execution_agency_name is not None:
            self.execution_agency_name = execution_agency_name
        if agent_gateway_id is not None:
            self.agent_gateway_id = agent_gateway_id
        if workload_identity is not None:
            self.workload_identity = workload_identity
        if access_endpoint is not None:
            self.access_endpoint = access_endpoint
        if observability is not None:
            self.observability = observability
        if tags is not None:
            self.tags = tags
        if status is not None:
            self.status = status
        if updated_by is not None:
            self.updated_by = updated_by

    @property
    def id(self):
        r"""Gets the id of this UpdateCoreCodeInterpreterResponse.

        **参数解释：** 工具ID。 **取值范围：** 符合UUID规则^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$的36位字符串。

        :return: The id of this UpdateCoreCodeInterpreterResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateCoreCodeInterpreterResponse.

        **参数解释：** 工具ID。 **取值范围：** 符合UUID规则^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$的36位字符串。

        :param id: The id of this UpdateCoreCodeInterpreterResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UpdateCoreCodeInterpreterResponse.

        **参数解释：** 工具的名称。 **取值范围：** 符合正则^[a-z][a-z0-9-]{0,38}[a-z0-9]$，即必须以小写字母开头，小写字母或数字结尾，中间可包含数字、小写字母、中划线，字符长度必须在2-40个字符之间。

        :return: The name of this UpdateCoreCodeInterpreterResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateCoreCodeInterpreterResponse.

        **参数解释：** 工具的名称。 **取值范围：** 符合正则^[a-z][a-z0-9-]{0,38}[a-z0-9]$，即必须以小写字母开头，小写字母或数字结尾，中间可包含数字、小写字母、中划线，字符长度必须在2-40个字符之间。

        :param name: The name of this UpdateCoreCodeInterpreterResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateCoreCodeInterpreterResponse.

        **参数解释：** 工具的描述。 **取值范围：** 任意字符，长度不能超过4096个字符

        :return: The description of this UpdateCoreCodeInterpreterResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateCoreCodeInterpreterResponse.

        **参数解释：** 工具的描述。 **取值范围：** 任意字符，长度不能超过4096个字符

        :param description: The description of this UpdateCoreCodeInterpreterResponse.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        r"""Gets the created_at of this UpdateCoreCodeInterpreterResponse.

        **参数解释：** 创建时间。 **取值范围：** ISO 8601格式的时间字符串，例如：2026-04-09T08:29:59.922+00:00。

        :return: The created_at of this UpdateCoreCodeInterpreterResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this UpdateCoreCodeInterpreterResponse.

        **参数解释：** 创建时间。 **取值范围：** ISO 8601格式的时间字符串，例如：2026-04-09T08:29:59.922+00:00。

        :param created_at: The created_at of this UpdateCoreCodeInterpreterResponse.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this UpdateCoreCodeInterpreterResponse.

        **参数解释：** 更新时间。 **取值范围：** ISO 8601格式的时间字符串，例如：2026-04-09T08:29:59.922+00:00。

        :return: The updated_at of this UpdateCoreCodeInterpreterResponse.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this UpdateCoreCodeInterpreterResponse.

        **参数解释：** 更新时间。 **取值范围：** ISO 8601格式的时间字符串，例如：2026-04-09T08:29:59.922+00:00。

        :param updated_at: The updated_at of this UpdateCoreCodeInterpreterResponse.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def execution_agency_name(self):
        r"""Gets the execution_agency_name of this UpdateCoreCodeInterpreterResponse.

        **参数解释：** 为工具提供访问云服务的权限的IAM委托名。 **取值范围：** IAM委托名长度必须在1-64个字符之间，字符规则以IAM服务校验规则为准。

        :return: The execution_agency_name of this UpdateCoreCodeInterpreterResponse.
        :rtype: str
        """
        return self._execution_agency_name

    @execution_agency_name.setter
    def execution_agency_name(self, execution_agency_name):
        r"""Sets the execution_agency_name of this UpdateCoreCodeInterpreterResponse.

        **参数解释：** 为工具提供访问云服务的权限的IAM委托名。 **取值范围：** IAM委托名长度必须在1-64个字符之间，字符规则以IAM服务校验规则为准。

        :param execution_agency_name: The execution_agency_name of this UpdateCoreCodeInterpreterResponse.
        :type execution_agency_name: str
        """
        self._execution_agency_name = execution_agency_name

    @property
    def agent_gateway_id(self):
        r"""Gets the agent_gateway_id of this UpdateCoreCodeInterpreterResponse.

        **参数解释：** 工具入口的AgentGateway的ID。 **取值范围：** 符合UUID规则 ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$的36位字符串。

        :return: The agent_gateway_id of this UpdateCoreCodeInterpreterResponse.
        :rtype: str
        """
        return self._agent_gateway_id

    @agent_gateway_id.setter
    def agent_gateway_id(self, agent_gateway_id):
        r"""Sets the agent_gateway_id of this UpdateCoreCodeInterpreterResponse.

        **参数解释：** 工具入口的AgentGateway的ID。 **取值范围：** 符合UUID规则 ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$的36位字符串。

        :param agent_gateway_id: The agent_gateway_id of this UpdateCoreCodeInterpreterResponse.
        :type agent_gateway_id: str
        """
        self._agent_gateway_id = agent_gateway_id

    @property
    def workload_identity(self):
        r"""Gets the workload_identity of this UpdateCoreCodeInterpreterResponse.

        :return: The workload_identity of this UpdateCoreCodeInterpreterResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreToolsWorkloadIdentity`
        """
        return self._workload_identity

    @workload_identity.setter
    def workload_identity(self, workload_identity):
        r"""Sets the workload_identity of this UpdateCoreCodeInterpreterResponse.

        :param workload_identity: The workload_identity of this UpdateCoreCodeInterpreterResponse.
        :type workload_identity: :class:`huaweicloudsdkagentarts.v1.CoreToolsWorkloadIdentity`
        """
        self._workload_identity = workload_identity

    @property
    def access_endpoint(self):
        r"""Gets the access_endpoint of this UpdateCoreCodeInterpreterResponse.

        **参数解释：** 访问域名。 **取值范围：** 不涉及。

        :return: The access_endpoint of this UpdateCoreCodeInterpreterResponse.
        :rtype: str
        """
        return self._access_endpoint

    @access_endpoint.setter
    def access_endpoint(self, access_endpoint):
        r"""Sets the access_endpoint of this UpdateCoreCodeInterpreterResponse.

        **参数解释：** 访问域名。 **取值范围：** 不涉及。

        :param access_endpoint: The access_endpoint of this UpdateCoreCodeInterpreterResponse.
        :type access_endpoint: str
        """
        self._access_endpoint = access_endpoint

    @property
    def observability(self):
        r"""Gets the observability of this UpdateCoreCodeInterpreterResponse.

        :return: The observability of this UpdateCoreCodeInterpreterResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreToolsObservability`
        """
        return self._observability

    @observability.setter
    def observability(self, observability):
        r"""Sets the observability of this UpdateCoreCodeInterpreterResponse.

        :param observability: The observability of this UpdateCoreCodeInterpreterResponse.
        :type observability: :class:`huaweicloudsdkagentarts.v1.CoreToolsObservability`
        """
        self._observability = observability

    @property
    def tags(self):
        r"""Gets the tags of this UpdateCoreCodeInterpreterResponse.

        **参数解释：** 资源标签。 **取值范围：** 不涉及。

        :return: The tags of this UpdateCoreCodeInterpreterResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreToolsTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this UpdateCoreCodeInterpreterResponse.

        **参数解释：** 资源标签。 **取值范围：** 不涉及。

        :param tags: The tags of this UpdateCoreCodeInterpreterResponse.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreToolsTag`]
        """
        self._tags = tags

    @property
    def status(self):
        r"""Gets the status of this UpdateCoreCodeInterpreterResponse.

        **参数解释：** 工具状态。 **取值范围：** - RUNNING：运行中。 - DELETING：删除中。 - DELETE_FAILED：删除失败。

        :return: The status of this UpdateCoreCodeInterpreterResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateCoreCodeInterpreterResponse.

        **参数解释：** 工具状态。 **取值范围：** - RUNNING：运行中。 - DELETING：删除中。 - DELETE_FAILED：删除失败。

        :param status: The status of this UpdateCoreCodeInterpreterResponse.
        :type status: str
        """
        self._status = status

    @property
    def updated_by(self):
        r"""Gets the updated_by of this UpdateCoreCodeInterpreterResponse.

        **参数解释：** 更新用户。 **取值范围：** 更新用户的IAM用户ID。

        :return: The updated_by of this UpdateCoreCodeInterpreterResponse.
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        r"""Sets the updated_by of this UpdateCoreCodeInterpreterResponse.

        **参数解释：** 更新用户。 **取值范围：** 更新用户的IAM用户ID。

        :param updated_by: The updated_by of this UpdateCoreCodeInterpreterResponse.
        :type updated_by: str
        """
        self._updated_by = updated_by

    def to_dict(self):
        import warnings
        warnings.warn("UpdateCoreCodeInterpreterResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, UpdateCoreCodeInterpreterResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
