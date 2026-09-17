# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkItemFlowInfoVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'process_instance': 'WorkItemFlowProcessInstanceVO',
        'process_nodes': 'list[WorkItemFlowProcessNodeVO]',
        'current_process_node': 'WorkItemFlowProcessNodeVO',
        'next_flow': 'list[FlowsInfoVO]',
        'fail_result': 'str'
    }

    attribute_map = {
        'process_instance': 'process_instance',
        'process_nodes': 'process_nodes',
        'current_process_node': 'current_process_node',
        'next_flow': 'next_flow',
        'fail_result': 'fail_result'
    }

    def __init__(self, process_instance=None, process_nodes=None, current_process_node=None, next_flow=None, fail_result=None):
        r"""WorkItemFlowInfoVO

        The model defined in huaweicloud sdk

        :param process_instance: 
        :type process_instance: :class:`huaweicloudsdkprojectman.v4.WorkItemFlowProcessInstanceVO`
        :param process_nodes: **参数解释**： 工作项关联的全部工作流节点列表。 **取值范围**： 不涉及。
        :type process_nodes: list[:class:`huaweicloudsdkprojectman.v4.WorkItemFlowProcessNodeVO`]
        :param current_process_node: 
        :type current_process_node: :class:`huaweicloudsdkprojectman.v4.WorkItemFlowProcessNodeVO`
        :param next_flow: **参数解释**： 可以流转的流转线信息。 **取值范围**： 不涉及。
        :type next_flow: list[:class:`huaweicloudsdkprojectman.v4.FlowsInfoVO`]
        :param fail_result: **参数解释**： 流转失败时的失败原因。 **取值范围**： 不涉及。
        :type fail_result: str
        """
        
        

        self._process_instance = None
        self._process_nodes = None
        self._current_process_node = None
        self._next_flow = None
        self._fail_result = None
        self.discriminator = None

        if process_instance is not None:
            self.process_instance = process_instance
        if process_nodes is not None:
            self.process_nodes = process_nodes
        if current_process_node is not None:
            self.current_process_node = current_process_node
        if next_flow is not None:
            self.next_flow = next_flow
        if fail_result is not None:
            self.fail_result = fail_result

    @property
    def process_instance(self):
        r"""Gets the process_instance of this WorkItemFlowInfoVO.

        :return: The process_instance of this WorkItemFlowInfoVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.WorkItemFlowProcessInstanceVO`
        """
        return self._process_instance

    @process_instance.setter
    def process_instance(self, process_instance):
        r"""Sets the process_instance of this WorkItemFlowInfoVO.

        :param process_instance: The process_instance of this WorkItemFlowInfoVO.
        :type process_instance: :class:`huaweicloudsdkprojectman.v4.WorkItemFlowProcessInstanceVO`
        """
        self._process_instance = process_instance

    @property
    def process_nodes(self):
        r"""Gets the process_nodes of this WorkItemFlowInfoVO.

        **参数解释**： 工作项关联的全部工作流节点列表。 **取值范围**： 不涉及。

        :return: The process_nodes of this WorkItemFlowInfoVO.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.WorkItemFlowProcessNodeVO`]
        """
        return self._process_nodes

    @process_nodes.setter
    def process_nodes(self, process_nodes):
        r"""Sets the process_nodes of this WorkItemFlowInfoVO.

        **参数解释**： 工作项关联的全部工作流节点列表。 **取值范围**： 不涉及。

        :param process_nodes: The process_nodes of this WorkItemFlowInfoVO.
        :type process_nodes: list[:class:`huaweicloudsdkprojectman.v4.WorkItemFlowProcessNodeVO`]
        """
        self._process_nodes = process_nodes

    @property
    def current_process_node(self):
        r"""Gets the current_process_node of this WorkItemFlowInfoVO.

        :return: The current_process_node of this WorkItemFlowInfoVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.WorkItemFlowProcessNodeVO`
        """
        return self._current_process_node

    @current_process_node.setter
    def current_process_node(self, current_process_node):
        r"""Sets the current_process_node of this WorkItemFlowInfoVO.

        :param current_process_node: The current_process_node of this WorkItemFlowInfoVO.
        :type current_process_node: :class:`huaweicloudsdkprojectman.v4.WorkItemFlowProcessNodeVO`
        """
        self._current_process_node = current_process_node

    @property
    def next_flow(self):
        r"""Gets the next_flow of this WorkItemFlowInfoVO.

        **参数解释**： 可以流转的流转线信息。 **取值范围**： 不涉及。

        :return: The next_flow of this WorkItemFlowInfoVO.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.FlowsInfoVO`]
        """
        return self._next_flow

    @next_flow.setter
    def next_flow(self, next_flow):
        r"""Sets the next_flow of this WorkItemFlowInfoVO.

        **参数解释**： 可以流转的流转线信息。 **取值范围**： 不涉及。

        :param next_flow: The next_flow of this WorkItemFlowInfoVO.
        :type next_flow: list[:class:`huaweicloudsdkprojectman.v4.FlowsInfoVO`]
        """
        self._next_flow = next_flow

    @property
    def fail_result(self):
        r"""Gets the fail_result of this WorkItemFlowInfoVO.

        **参数解释**： 流转失败时的失败原因。 **取值范围**： 不涉及。

        :return: The fail_result of this WorkItemFlowInfoVO.
        :rtype: str
        """
        return self._fail_result

    @fail_result.setter
    def fail_result(self, fail_result):
        r"""Sets the fail_result of this WorkItemFlowInfoVO.

        **参数解释**： 流转失败时的失败原因。 **取值范围**： 不涉及。

        :param fail_result: The fail_result of this WorkItemFlowInfoVO.
        :type fail_result: str
        """
        self._fail_result = fail_result

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
        if not isinstance(other, WorkItemFlowInfoVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
