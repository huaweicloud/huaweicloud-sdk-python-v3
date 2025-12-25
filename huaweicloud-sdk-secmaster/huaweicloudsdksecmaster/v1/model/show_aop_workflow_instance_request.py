# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAopWorkflowInstanceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'workspace_id': 'str',
        'instance_id': 'str',
        'show_topology': 'bool'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'instance_id': 'instance_id',
        'show_topology': 'show_topology'
    }

    def __init__(self, project_id=None, workspace_id=None, instance_id=None, show_topology=None):
        r"""ShowAopWorkflowInstanceRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type project_id: str
        :param workspace_id: **参数解释**: 工作空间ID **取值范围**: 不涉及
        :type workspace_id: str
        :param instance_id: **参数解释**: 流程实例的ID **约束限制**: 不涉及
        :type instance_id: str
        :param show_topology: **参数解释**: 是否查询流程拓扑图的信息 - true 查询 - false 不查询  **约束限制**: 不涉及               **取值范围**: - true - false  **默认值**:  false
        :type show_topology: bool
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._instance_id = None
        self._show_topology = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        self.instance_id = instance_id
        if show_topology is not None:
            self.show_topology = show_topology

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowAopWorkflowInstanceRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The project_id of this ShowAopWorkflowInstanceRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowAopWorkflowInstanceRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param project_id: The project_id of this ShowAopWorkflowInstanceRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ShowAopWorkflowInstanceRequest.

        **参数解释**: 工作空间ID **取值范围**: 不涉及

        :return: The workspace_id of this ShowAopWorkflowInstanceRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ShowAopWorkflowInstanceRequest.

        **参数解释**: 工作空间ID **取值范围**: 不涉及

        :param workspace_id: The workspace_id of this ShowAopWorkflowInstanceRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowAopWorkflowInstanceRequest.

        **参数解释**: 流程实例的ID **约束限制**: 不涉及

        :return: The instance_id of this ShowAopWorkflowInstanceRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowAopWorkflowInstanceRequest.

        **参数解释**: 流程实例的ID **约束限制**: 不涉及

        :param instance_id: The instance_id of this ShowAopWorkflowInstanceRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def show_topology(self):
        r"""Gets the show_topology of this ShowAopWorkflowInstanceRequest.

        **参数解释**: 是否查询流程拓扑图的信息 - true 查询 - false 不查询  **约束限制**: 不涉及               **取值范围**: - true - false  **默认值**:  false

        :return: The show_topology of this ShowAopWorkflowInstanceRequest.
        :rtype: bool
        """
        return self._show_topology

    @show_topology.setter
    def show_topology(self, show_topology):
        r"""Sets the show_topology of this ShowAopWorkflowInstanceRequest.

        **参数解释**: 是否查询流程拓扑图的信息 - true 查询 - false 不查询  **约束限制**: 不涉及               **取值范围**: - true - false  **默认值**:  false

        :param show_topology: The show_topology of this ShowAopWorkflowInstanceRequest.
        :type show_topology: bool
        """
        self._show_topology = show_topology

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
        if not isinstance(other, ShowAopWorkflowInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
