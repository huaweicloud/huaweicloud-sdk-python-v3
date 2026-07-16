# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInferServiceClusterResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace_id': 'str',
        'logic_cluster_id': 'str',
        'status': 'str',
        'pool_id': 'str',
        'type': 'str',
        'resource_categories': 'list[str]',
        'project_id': 'str',
        'create_at': 'int',
        'update_at': 'int',
        'flavors': 'list[InferFlavor]'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'logic_cluster_id': 'logic_cluster_id',
        'status': 'status',
        'pool_id': 'pool_id',
        'type': 'type',
        'resource_categories': 'resource_categories',
        'project_id': 'project_id',
        'create_at': 'create_at',
        'update_at': 'update_at',
        'flavors': 'flavors'
    }

    def __init__(self, workspace_id=None, logic_cluster_id=None, status=None, pool_id=None, type=None, resource_categories=None, project_id=None, create_at=None, update_at=None, flavors=None):
        r"""ShowInferServiceClusterResponse

        The model defined in huaweicloud sdk

        :param workspace_id: **参数解释：** 工作空间ID。未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **取值范围：** 不涉及。
        :type workspace_id: str
        :param logic_cluster_id: **参数解释：** 资源池cceID。 **取值范围：** 不涉及。
        :type logic_cluster_id: str
        :param status: **参数解释：** 资源当前状态。 **取值范围：** - ACTIVE ：开启。 - PENDING ：待处理。 - INITIALIZING ：初始化中。 - INITIALIZE_FAILED ：初始化失败。 - DELETED ：已删除。 - DELETING ：删除中。 - DELETE_FAILED ：删除失败。 - MIGRATING : 迁移中。
        :type status: str
        :param pool_id: **参数解释：** 专属资源池ID。 **取值范围：** 不涉及。
        :type pool_id: str
        :param type: **参数解释：** 专属池类型。 **取值范围：** - MANAGED ：公共。 - MANAGED_ROMA ：公共。 - DEDICATED ：专属。 - DEDICATED_ROMA ：专属。
        :type type: str
        :param resource_categories: **参数解释：** 资源池类型。
        :type resource_categories: list[str]
        :param project_id: **参数解释：** [用户项目ID](tag:hws,hws_hk,fcs,fcs_super)[资源空间ID](tag:hcs,hcs_sm)。获取方法请参见[[获取项目ID和名称](modelarts_03_0147.xml)](tag:hws,hws_hk,fcs,fcs_super)[[获取资源空间ID和名称](modelarts_03_0147.xml)](tag:hcs,hcs_sm)。 **取值范围：** 不涉及。
        :type project_id: str
        :param create_at: **参数解释：** 资源池启用的时间，UTC毫秒。 **取值范围：** 不涉及。
        :type create_at: int
        :param update_at: **参数解释：** 资源池最后更新的时间，UTC毫秒。 **取值范围：** 不涉及。
        :type update_at: int
        :param flavors: **参数解释：** 当前专属池支持的规格。
        :type flavors: list[:class:`huaweicloudsdkmodelarts.v1.InferFlavor`]
        """
        
        super().__init__()

        self._workspace_id = None
        self._logic_cluster_id = None
        self._status = None
        self._pool_id = None
        self._type = None
        self._resource_categories = None
        self._project_id = None
        self._create_at = None
        self._update_at = None
        self._flavors = None
        self.discriminator = None

        if workspace_id is not None:
            self.workspace_id = workspace_id
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
        if project_id is not None:
            self.project_id = project_id
        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at
        if flavors is not None:
            self.flavors = flavors

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ShowInferServiceClusterResponse.

        **参数解释：** 工作空间ID。未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **取值范围：** 不涉及。

        :return: The workspace_id of this ShowInferServiceClusterResponse.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ShowInferServiceClusterResponse.

        **参数解释：** 工作空间ID。未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **取值范围：** 不涉及。

        :param workspace_id: The workspace_id of this ShowInferServiceClusterResponse.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def logic_cluster_id(self):
        r"""Gets the logic_cluster_id of this ShowInferServiceClusterResponse.

        **参数解释：** 资源池cceID。 **取值范围：** 不涉及。

        :return: The logic_cluster_id of this ShowInferServiceClusterResponse.
        :rtype: str
        """
        return self._logic_cluster_id

    @logic_cluster_id.setter
    def logic_cluster_id(self, logic_cluster_id):
        r"""Sets the logic_cluster_id of this ShowInferServiceClusterResponse.

        **参数解释：** 资源池cceID。 **取值范围：** 不涉及。

        :param logic_cluster_id: The logic_cluster_id of this ShowInferServiceClusterResponse.
        :type logic_cluster_id: str
        """
        self._logic_cluster_id = logic_cluster_id

    @property
    def status(self):
        r"""Gets the status of this ShowInferServiceClusterResponse.

        **参数解释：** 资源当前状态。 **取值范围：** - ACTIVE ：开启。 - PENDING ：待处理。 - INITIALIZING ：初始化中。 - INITIALIZE_FAILED ：初始化失败。 - DELETED ：已删除。 - DELETING ：删除中。 - DELETE_FAILED ：删除失败。 - MIGRATING : 迁移中。

        :return: The status of this ShowInferServiceClusterResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowInferServiceClusterResponse.

        **参数解释：** 资源当前状态。 **取值范围：** - ACTIVE ：开启。 - PENDING ：待处理。 - INITIALIZING ：初始化中。 - INITIALIZE_FAILED ：初始化失败。 - DELETED ：已删除。 - DELETING ：删除中。 - DELETE_FAILED ：删除失败。 - MIGRATING : 迁移中。

        :param status: The status of this ShowInferServiceClusterResponse.
        :type status: str
        """
        self._status = status

    @property
    def pool_id(self):
        r"""Gets the pool_id of this ShowInferServiceClusterResponse.

        **参数解释：** 专属资源池ID。 **取值范围：** 不涉及。

        :return: The pool_id of this ShowInferServiceClusterResponse.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this ShowInferServiceClusterResponse.

        **参数解释：** 专属资源池ID。 **取值范围：** 不涉及。

        :param pool_id: The pool_id of this ShowInferServiceClusterResponse.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def type(self):
        r"""Gets the type of this ShowInferServiceClusterResponse.

        **参数解释：** 专属池类型。 **取值范围：** - MANAGED ：公共。 - MANAGED_ROMA ：公共。 - DEDICATED ：专属。 - DEDICATED_ROMA ：专属。

        :return: The type of this ShowInferServiceClusterResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowInferServiceClusterResponse.

        **参数解释：** 专属池类型。 **取值范围：** - MANAGED ：公共。 - MANAGED_ROMA ：公共。 - DEDICATED ：专属。 - DEDICATED_ROMA ：专属。

        :param type: The type of this ShowInferServiceClusterResponse.
        :type type: str
        """
        self._type = type

    @property
    def resource_categories(self):
        r"""Gets the resource_categories of this ShowInferServiceClusterResponse.

        **参数解释：** 资源池类型。

        :return: The resource_categories of this ShowInferServiceClusterResponse.
        :rtype: list[str]
        """
        return self._resource_categories

    @resource_categories.setter
    def resource_categories(self, resource_categories):
        r"""Sets the resource_categories of this ShowInferServiceClusterResponse.

        **参数解释：** 资源池类型。

        :param resource_categories: The resource_categories of this ShowInferServiceClusterResponse.
        :type resource_categories: list[str]
        """
        self._resource_categories = resource_categories

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowInferServiceClusterResponse.

        **参数解释：** [用户项目ID](tag:hws,hws_hk,fcs,fcs_super)[资源空间ID](tag:hcs,hcs_sm)。获取方法请参见[[获取项目ID和名称](modelarts_03_0147.xml)](tag:hws,hws_hk,fcs,fcs_super)[[获取资源空间ID和名称](modelarts_03_0147.xml)](tag:hcs,hcs_sm)。 **取值范围：** 不涉及。

        :return: The project_id of this ShowInferServiceClusterResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowInferServiceClusterResponse.

        **参数解释：** [用户项目ID](tag:hws,hws_hk,fcs,fcs_super)[资源空间ID](tag:hcs,hcs_sm)。获取方法请参见[[获取项目ID和名称](modelarts_03_0147.xml)](tag:hws,hws_hk,fcs,fcs_super)[[获取资源空间ID和名称](modelarts_03_0147.xml)](tag:hcs,hcs_sm)。 **取值范围：** 不涉及。

        :param project_id: The project_id of this ShowInferServiceClusterResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def create_at(self):
        r"""Gets the create_at of this ShowInferServiceClusterResponse.

        **参数解释：** 资源池启用的时间，UTC毫秒。 **取值范围：** 不涉及。

        :return: The create_at of this ShowInferServiceClusterResponse.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this ShowInferServiceClusterResponse.

        **参数解释：** 资源池启用的时间，UTC毫秒。 **取值范围：** 不涉及。

        :param create_at: The create_at of this ShowInferServiceClusterResponse.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this ShowInferServiceClusterResponse.

        **参数解释：** 资源池最后更新的时间，UTC毫秒。 **取值范围：** 不涉及。

        :return: The update_at of this ShowInferServiceClusterResponse.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this ShowInferServiceClusterResponse.

        **参数解释：** 资源池最后更新的时间，UTC毫秒。 **取值范围：** 不涉及。

        :param update_at: The update_at of this ShowInferServiceClusterResponse.
        :type update_at: int
        """
        self._update_at = update_at

    @property
    def flavors(self):
        r"""Gets the flavors of this ShowInferServiceClusterResponse.

        **参数解释：** 当前专属池支持的规格。

        :return: The flavors of this ShowInferServiceClusterResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.InferFlavor`]
        """
        return self._flavors

    @flavors.setter
    def flavors(self, flavors):
        r"""Sets the flavors of this ShowInferServiceClusterResponse.

        **参数解释：** 当前专属池支持的规格。

        :param flavors: The flavors of this ShowInferServiceClusterResponse.
        :type flavors: list[:class:`huaweicloudsdkmodelarts.v1.InferFlavor`]
        """
        self._flavors = flavors

    def to_dict(self):
        import warnings
        warnings.warn("ShowInferServiceClusterResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowInferServiceClusterResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
