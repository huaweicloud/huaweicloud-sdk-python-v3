# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAopWorkflowVersionsRequest:

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
        'workflow_id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'workflow_id': 'workflow_id',
        'status': 'status'
    }

    def __init__(self, project_id=None, workspace_id=None, workflow_id=None, status=None):
        r"""ListAopWorkflowVersionsRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type project_id: str
        :param workspace_id: **参数解释**: 工作空间ID **取值范围**: 不涉及
        :type workspace_id: str
        :param workflow_id: **参数解释**: 流程ID **取值范围**: 不涉及
        :type workflow_id: str
        :param status: **参数解释**: 流程的状态 - pending_submit 草稿 - pending_approval 待审核 - publishing 发布中 - publish_failed 发布失败 - not_activated 未激活 - activated 已激活 - rejected 审核拒绝  **取值范围**: - pending_submit - pending_approval - publishing - publish_failed - not_activated - activated - rejected
        :type status: str
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._workflow_id = None
        self._status = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        self.workflow_id = workflow_id
        if status is not None:
            self.status = status

    @property
    def project_id(self):
        r"""Gets the project_id of this ListAopWorkflowVersionsRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The project_id of this ListAopWorkflowVersionsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListAopWorkflowVersionsRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param project_id: The project_id of this ListAopWorkflowVersionsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListAopWorkflowVersionsRequest.

        **参数解释**: 工作空间ID **取值范围**: 不涉及

        :return: The workspace_id of this ListAopWorkflowVersionsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListAopWorkflowVersionsRequest.

        **参数解释**: 工作空间ID **取值范围**: 不涉及

        :param workspace_id: The workspace_id of this ListAopWorkflowVersionsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def workflow_id(self):
        r"""Gets the workflow_id of this ListAopWorkflowVersionsRequest.

        **参数解释**: 流程ID **取值范围**: 不涉及

        :return: The workflow_id of this ListAopWorkflowVersionsRequest.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        r"""Sets the workflow_id of this ListAopWorkflowVersionsRequest.

        **参数解释**: 流程ID **取值范围**: 不涉及

        :param workflow_id: The workflow_id of this ListAopWorkflowVersionsRequest.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def status(self):
        r"""Gets the status of this ListAopWorkflowVersionsRequest.

        **参数解释**: 流程的状态 - pending_submit 草稿 - pending_approval 待审核 - publishing 发布中 - publish_failed 发布失败 - not_activated 未激活 - activated 已激活 - rejected 审核拒绝  **取值范围**: - pending_submit - pending_approval - publishing - publish_failed - not_activated - activated - rejected

        :return: The status of this ListAopWorkflowVersionsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListAopWorkflowVersionsRequest.

        **参数解释**: 流程的状态 - pending_submit 草稿 - pending_approval 待审核 - publishing 发布中 - publish_failed 发布失败 - not_activated 未激活 - activated 已激活 - rejected 审核拒绝  **取值范围**: - pending_submit - pending_approval - publishing - publish_failed - not_activated - activated - rejected

        :param status: The status of this ListAopWorkflowVersionsRequest.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ListAopWorkflowVersionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
