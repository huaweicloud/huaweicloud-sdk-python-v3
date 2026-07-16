# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'logic_cluster_id': 'str',
        'status': 'str',
        'pool_id': 'str',
        'type': 'str',
        'resource_categories': 'str',
        'workspace_id': 'str',
        'create_at': 'str',
        'update_at': 'str',
        'project_id': 'str',
        'domain_id': 'str',
        'flavors': 'list[Flavor]',
        'is_allow_root': 'bool'
    }

    attribute_map = {
        'logic_cluster_id': 'logic_cluster_id',
        'status': 'status',
        'pool_id': 'pool_id',
        'type': 'type',
        'resource_categories': 'resource_categories',
        'workspace_id': 'workspace_id',
        'create_at': 'create_at',
        'update_at': 'update_at',
        'project_id': 'project_id',
        'domain_id': 'domain_id',
        'flavors': 'flavors',
        'is_allow_root': 'is_allow_root'
    }

    def __init__(self, logic_cluster_id=None, status=None, pool_id=None, type=None, resource_categories=None, workspace_id=None, create_at=None, update_at=None, project_id=None, domain_id=None, flavors=None, is_allow_root=None):
        r"""ShowClusterResponse

        The model defined in huaweicloud sdk

        :param logic_cluster_id: **参数解释**： 逻辑资源池ID。 **取值范围**： 不涉及。
        :type logic_cluster_id: str
        :param status: **参数解释**：资源池状态。 **取值范围**：枚举类型，取值如下： - PENDING：等待中。 - INITIALIZING：初始化中。 - INITIALIZE_FAILED：初始化失败。 - ACTIVE：可用。 - DELETING：删除中。 - DELETED：已删除。 - DELETE_FAILED：删除失败。 - MIGRATING：迁移中。
        :type status: str
        :param pool_id: **参数解释**：资源池ID。 **取值范围**：不涉及。
        :type pool_id: str
        :param type: **参数解释**：资源池类型。  **取值范围**：枚举类型，取值如下： - MANAGED：公共池。 - DEDICATED：专属池。
        :type type: str
        :param resource_categories: **参数解释**：资源类别。 **取值范围**：枚举类型，取值如下： - GPU - CPU - ASCEND
        :type resource_categories: str
        :param workspace_id: **参数解释**：工作空间ID。获取方法请参见[[查询工作空间列表](ListWorkspace.xml)](tag:hc,hk)。未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **取值范围**：不涉及。
        :type workspace_id: str
        :param create_at: **参数解释**：实例创建的时间，UTC毫秒。 **取值范围**：不涉及。
        :type create_at: str
        :param update_at: **参数解释**：实例最后更新的时间，UTC毫秒。 **取值范围**：不涉及。
        :type update_at: str
        :param project_id: **参数解释**：用户项目ID，获取方法请参见[获取项目ID和名称](modelarts_03_0147.xml)。 **取值范围**：不涉及。
        :type project_id: str
        :param domain_id: **参数解释**：账号ID。 **取值范围**：不涉及。
        :type domain_id: str
        :param flavors: **参数解释**：资源池规格。
        :type flavors: list[:class:`huaweicloudsdkmodelarts.v1.Flavor`]
        :param is_allow_root: **参数解释**：资源池是否允许实例以root启动。
        :type is_allow_root: bool
        """
        
        super().__init__()

        self._logic_cluster_id = None
        self._status = None
        self._pool_id = None
        self._type = None
        self._resource_categories = None
        self._workspace_id = None
        self._create_at = None
        self._update_at = None
        self._project_id = None
        self._domain_id = None
        self._flavors = None
        self._is_allow_root = None
        self.discriminator = None

        if logic_cluster_id is not None:
            self.logic_cluster_id = logic_cluster_id
        if status is not None:
            self.status = status
        if pool_id is not None:
            self.pool_id = pool_id
        if type is not None:
            self.type = type
        if resource_categories is not None:
            self.resource_categories = resource_categories
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at
        if project_id is not None:
            self.project_id = project_id
        if domain_id is not None:
            self.domain_id = domain_id
        if flavors is not None:
            self.flavors = flavors
        if is_allow_root is not None:
            self.is_allow_root = is_allow_root

    @property
    def logic_cluster_id(self):
        r"""Gets the logic_cluster_id of this ShowClusterResponse.

        **参数解释**： 逻辑资源池ID。 **取值范围**： 不涉及。

        :return: The logic_cluster_id of this ShowClusterResponse.
        :rtype: str
        """
        return self._logic_cluster_id

    @logic_cluster_id.setter
    def logic_cluster_id(self, logic_cluster_id):
        r"""Sets the logic_cluster_id of this ShowClusterResponse.

        **参数解释**： 逻辑资源池ID。 **取值范围**： 不涉及。

        :param logic_cluster_id: The logic_cluster_id of this ShowClusterResponse.
        :type logic_cluster_id: str
        """
        self._logic_cluster_id = logic_cluster_id

    @property
    def status(self):
        r"""Gets the status of this ShowClusterResponse.

        **参数解释**：资源池状态。 **取值范围**：枚举类型，取值如下： - PENDING：等待中。 - INITIALIZING：初始化中。 - INITIALIZE_FAILED：初始化失败。 - ACTIVE：可用。 - DELETING：删除中。 - DELETED：已删除。 - DELETE_FAILED：删除失败。 - MIGRATING：迁移中。

        :return: The status of this ShowClusterResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowClusterResponse.

        **参数解释**：资源池状态。 **取值范围**：枚举类型，取值如下： - PENDING：等待中。 - INITIALIZING：初始化中。 - INITIALIZE_FAILED：初始化失败。 - ACTIVE：可用。 - DELETING：删除中。 - DELETED：已删除。 - DELETE_FAILED：删除失败。 - MIGRATING：迁移中。

        :param status: The status of this ShowClusterResponse.
        :type status: str
        """
        self._status = status

    @property
    def pool_id(self):
        r"""Gets the pool_id of this ShowClusterResponse.

        **参数解释**：资源池ID。 **取值范围**：不涉及。

        :return: The pool_id of this ShowClusterResponse.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this ShowClusterResponse.

        **参数解释**：资源池ID。 **取值范围**：不涉及。

        :param pool_id: The pool_id of this ShowClusterResponse.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def type(self):
        r"""Gets the type of this ShowClusterResponse.

        **参数解释**：资源池类型。  **取值范围**：枚举类型，取值如下： - MANAGED：公共池。 - DEDICATED：专属池。

        :return: The type of this ShowClusterResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowClusterResponse.

        **参数解释**：资源池类型。  **取值范围**：枚举类型，取值如下： - MANAGED：公共池。 - DEDICATED：专属池。

        :param type: The type of this ShowClusterResponse.
        :type type: str
        """
        self._type = type

    @property
    def resource_categories(self):
        r"""Gets the resource_categories of this ShowClusterResponse.

        **参数解释**：资源类别。 **取值范围**：枚举类型，取值如下： - GPU - CPU - ASCEND

        :return: The resource_categories of this ShowClusterResponse.
        :rtype: str
        """
        return self._resource_categories

    @resource_categories.setter
    def resource_categories(self, resource_categories):
        r"""Sets the resource_categories of this ShowClusterResponse.

        **参数解释**：资源类别。 **取值范围**：枚举类型，取值如下： - GPU - CPU - ASCEND

        :param resource_categories: The resource_categories of this ShowClusterResponse.
        :type resource_categories: str
        """
        self._resource_categories = resource_categories

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ShowClusterResponse.

        **参数解释**：工作空间ID。获取方法请参见[[查询工作空间列表](ListWorkspace.xml)](tag:hc,hk)。未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **取值范围**：不涉及。

        :return: The workspace_id of this ShowClusterResponse.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ShowClusterResponse.

        **参数解释**：工作空间ID。获取方法请参见[[查询工作空间列表](ListWorkspace.xml)](tag:hc,hk)。未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **取值范围**：不涉及。

        :param workspace_id: The workspace_id of this ShowClusterResponse.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def create_at(self):
        r"""Gets the create_at of this ShowClusterResponse.

        **参数解释**：实例创建的时间，UTC毫秒。 **取值范围**：不涉及。

        :return: The create_at of this ShowClusterResponse.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this ShowClusterResponse.

        **参数解释**：实例创建的时间，UTC毫秒。 **取值范围**：不涉及。

        :param create_at: The create_at of this ShowClusterResponse.
        :type create_at: str
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this ShowClusterResponse.

        **参数解释**：实例最后更新的时间，UTC毫秒。 **取值范围**：不涉及。

        :return: The update_at of this ShowClusterResponse.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this ShowClusterResponse.

        **参数解释**：实例最后更新的时间，UTC毫秒。 **取值范围**：不涉及。

        :param update_at: The update_at of this ShowClusterResponse.
        :type update_at: str
        """
        self._update_at = update_at

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowClusterResponse.

        **参数解释**：用户项目ID，获取方法请参见[获取项目ID和名称](modelarts_03_0147.xml)。 **取值范围**：不涉及。

        :return: The project_id of this ShowClusterResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowClusterResponse.

        **参数解释**：用户项目ID，获取方法请参见[获取项目ID和名称](modelarts_03_0147.xml)。 **取值范围**：不涉及。

        :param project_id: The project_id of this ShowClusterResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowClusterResponse.

        **参数解释**：账号ID。 **取值范围**：不涉及。

        :return: The domain_id of this ShowClusterResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowClusterResponse.

        **参数解释**：账号ID。 **取值范围**：不涉及。

        :param domain_id: The domain_id of this ShowClusterResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def flavors(self):
        r"""Gets the flavors of this ShowClusterResponse.

        **参数解释**：资源池规格。

        :return: The flavors of this ShowClusterResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.Flavor`]
        """
        return self._flavors

    @flavors.setter
    def flavors(self, flavors):
        r"""Sets the flavors of this ShowClusterResponse.

        **参数解释**：资源池规格。

        :param flavors: The flavors of this ShowClusterResponse.
        :type flavors: list[:class:`huaweicloudsdkmodelarts.v1.Flavor`]
        """
        self._flavors = flavors

    @property
    def is_allow_root(self):
        r"""Gets the is_allow_root of this ShowClusterResponse.

        **参数解释**：资源池是否允许实例以root启动。

        :return: The is_allow_root of this ShowClusterResponse.
        :rtype: bool
        """
        return self._is_allow_root

    @is_allow_root.setter
    def is_allow_root(self, is_allow_root):
        r"""Sets the is_allow_root of this ShowClusterResponse.

        **参数解释**：资源池是否允许实例以root启动。

        :param is_allow_root: The is_allow_root of this ShowClusterResponse.
        :type is_allow_root: bool
        """
        self._is_allow_root = is_allow_root

    def to_dict(self):
        import warnings
        warnings.warn("ShowClusterResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowClusterResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
