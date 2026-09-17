# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkItemFlowProcessInstanceVO:

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
        'flow_state': 'int',
        'workflow_entry_id': 'str',
        'category': 'str'
    }

    attribute_map = {
        'id': 'id',
        'flow_state': 'flow_state',
        'workflow_entry_id': 'workflow_entry_id',
        'category': 'category'
    }

    def __init__(self, id=None, flow_state=None, workflow_entry_id=None, category=None):
        r"""WorkItemFlowProcessInstanceVO

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 工作项工作流实例ID。 **取值范围**： 不涉及。
        :type id: str
        :param flow_state: **参数解释**： 工作流实例是否挂起。 **取值范围**：  1: 运行  2: 挂起
        :type flow_state: int
        :param workflow_entry_id: **参数解释**： 工作流入口ID。 **取值范围**： 不涉及。
        :type workflow_entry_id: str
        :param category: **参数解释**： 工作流分类。 **取值范围**： 不涉及。
        :type category: str
        """
        
        

        self._id = None
        self._flow_state = None
        self._workflow_entry_id = None
        self._category = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if flow_state is not None:
            self.flow_state = flow_state
        if workflow_entry_id is not None:
            self.workflow_entry_id = workflow_entry_id
        if category is not None:
            self.category = category

    @property
    def id(self):
        r"""Gets the id of this WorkItemFlowProcessInstanceVO.

        **参数解释**： 工作项工作流实例ID。 **取值范围**： 不涉及。

        :return: The id of this WorkItemFlowProcessInstanceVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this WorkItemFlowProcessInstanceVO.

        **参数解释**： 工作项工作流实例ID。 **取值范围**： 不涉及。

        :param id: The id of this WorkItemFlowProcessInstanceVO.
        :type id: str
        """
        self._id = id

    @property
    def flow_state(self):
        r"""Gets the flow_state of this WorkItemFlowProcessInstanceVO.

        **参数解释**： 工作流实例是否挂起。 **取值范围**：  1: 运行  2: 挂起

        :return: The flow_state of this WorkItemFlowProcessInstanceVO.
        :rtype: int
        """
        return self._flow_state

    @flow_state.setter
    def flow_state(self, flow_state):
        r"""Sets the flow_state of this WorkItemFlowProcessInstanceVO.

        **参数解释**： 工作流实例是否挂起。 **取值范围**：  1: 运行  2: 挂起

        :param flow_state: The flow_state of this WorkItemFlowProcessInstanceVO.
        :type flow_state: int
        """
        self._flow_state = flow_state

    @property
    def workflow_entry_id(self):
        r"""Gets the workflow_entry_id of this WorkItemFlowProcessInstanceVO.

        **参数解释**： 工作流入口ID。 **取值范围**： 不涉及。

        :return: The workflow_entry_id of this WorkItemFlowProcessInstanceVO.
        :rtype: str
        """
        return self._workflow_entry_id

    @workflow_entry_id.setter
    def workflow_entry_id(self, workflow_entry_id):
        r"""Sets the workflow_entry_id of this WorkItemFlowProcessInstanceVO.

        **参数解释**： 工作流入口ID。 **取值范围**： 不涉及。

        :param workflow_entry_id: The workflow_entry_id of this WorkItemFlowProcessInstanceVO.
        :type workflow_entry_id: str
        """
        self._workflow_entry_id = workflow_entry_id

    @property
    def category(self):
        r"""Gets the category of this WorkItemFlowProcessInstanceVO.

        **参数解释**： 工作流分类。 **取值范围**： 不涉及。

        :return: The category of this WorkItemFlowProcessInstanceVO.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this WorkItemFlowProcessInstanceVO.

        **参数解释**： 工作流分类。 **取值范围**： 不涉及。

        :param category: The category of this WorkItemFlowProcessInstanceVO.
        :type category: str
        """
        self._category = category

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
        if not isinstance(other, WorkItemFlowProcessInstanceVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
