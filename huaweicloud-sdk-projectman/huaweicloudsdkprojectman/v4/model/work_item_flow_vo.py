# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkItemFlowVO:

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
        'issue_category': 'str',
        'flow_code': 'str',
        'issue_ids': 'list[str]',
        'process_context': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'issue_category': 'issue_category',
        'flow_code': 'flow_code',
        'issue_ids': 'issue_ids',
        'process_context': 'process_context'
    }

    def __init__(self, id=None, issue_category=None, flow_code=None, issue_ids=None, process_context=None):
        r"""WorkItemFlowVO

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 工作项唯一ID。可以通过[查询工作项列表](ListIpdProjectIssues.xml)或者[查询树状工作项](ShowIpdIssueTree.xml)接口获取，响应消息体中的**id**字段的值就是工作项ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type id: str
        :param issue_category: **参数解释**： 工作项类型。 **约束限制**： 不涉及。 **取值范围**： RR、IR、AR、SR、Bug、FE、Task、US、Epic、SF **默认取值**： 不涉及。
        :type issue_category: str
        :param flow_code: **参数解释**： 工作项流转code。可以通过[查询工作项流程信息](ShowIssueWorkItemFlowDetail.xml)接口获取。 响应消息体中的**next_flow**数组为工作流流转线，根据**from_code**当前状态和**to_code**目标状态找到匹配的流转线，流转线的**code**字段的值就是工作项流转code。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type flow_code: str
        :param issue_ids: **参数解释**： 工作项唯一Id数组。可以通过[查询工作项列表](ListIpdProjectIssues.xml)或者[查询树状工作项](ShowIpdIssueTree.xml)接口获取，响应消息体中的**id**字段的值就是工作项ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type issue_ids: list[str]
        :param process_context: **参数解释**： 流转中配置上下文信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type process_context: dict(str, object)
        """
        
        

        self._id = None
        self._issue_category = None
        self._flow_code = None
        self._issue_ids = None
        self._process_context = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.issue_category = issue_category
        self.flow_code = flow_code
        if issue_ids is not None:
            self.issue_ids = issue_ids
        if process_context is not None:
            self.process_context = process_context

    @property
    def id(self):
        r"""Gets the id of this WorkItemFlowVO.

        **参数解释**： 工作项唯一ID。可以通过[查询工作项列表](ListIpdProjectIssues.xml)或者[查询树状工作项](ShowIpdIssueTree.xml)接口获取，响应消息体中的**id**字段的值就是工作项ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The id of this WorkItemFlowVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this WorkItemFlowVO.

        **参数解释**： 工作项唯一ID。可以通过[查询工作项列表](ListIpdProjectIssues.xml)或者[查询树状工作项](ShowIpdIssueTree.xml)接口获取，响应消息体中的**id**字段的值就是工作项ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param id: The id of this WorkItemFlowVO.
        :type id: str
        """
        self._id = id

    @property
    def issue_category(self):
        r"""Gets the issue_category of this WorkItemFlowVO.

        **参数解释**： 工作项类型。 **约束限制**： 不涉及。 **取值范围**： RR、IR、AR、SR、Bug、FE、Task、US、Epic、SF **默认取值**： 不涉及。

        :return: The issue_category of this WorkItemFlowVO.
        :rtype: str
        """
        return self._issue_category

    @issue_category.setter
    def issue_category(self, issue_category):
        r"""Sets the issue_category of this WorkItemFlowVO.

        **参数解释**： 工作项类型。 **约束限制**： 不涉及。 **取值范围**： RR、IR、AR、SR、Bug、FE、Task、US、Epic、SF **默认取值**： 不涉及。

        :param issue_category: The issue_category of this WorkItemFlowVO.
        :type issue_category: str
        """
        self._issue_category = issue_category

    @property
    def flow_code(self):
        r"""Gets the flow_code of this WorkItemFlowVO.

        **参数解释**： 工作项流转code。可以通过[查询工作项流程信息](ShowIssueWorkItemFlowDetail.xml)接口获取。 响应消息体中的**next_flow**数组为工作流流转线，根据**from_code**当前状态和**to_code**目标状态找到匹配的流转线，流转线的**code**字段的值就是工作项流转code。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The flow_code of this WorkItemFlowVO.
        :rtype: str
        """
        return self._flow_code

    @flow_code.setter
    def flow_code(self, flow_code):
        r"""Sets the flow_code of this WorkItemFlowVO.

        **参数解释**： 工作项流转code。可以通过[查询工作项流程信息](ShowIssueWorkItemFlowDetail.xml)接口获取。 响应消息体中的**next_flow**数组为工作流流转线，根据**from_code**当前状态和**to_code**目标状态找到匹配的流转线，流转线的**code**字段的值就是工作项流转code。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param flow_code: The flow_code of this WorkItemFlowVO.
        :type flow_code: str
        """
        self._flow_code = flow_code

    @property
    def issue_ids(self):
        r"""Gets the issue_ids of this WorkItemFlowVO.

        **参数解释**： 工作项唯一Id数组。可以通过[查询工作项列表](ListIpdProjectIssues.xml)或者[查询树状工作项](ShowIpdIssueTree.xml)接口获取，响应消息体中的**id**字段的值就是工作项ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The issue_ids of this WorkItemFlowVO.
        :rtype: list[str]
        """
        return self._issue_ids

    @issue_ids.setter
    def issue_ids(self, issue_ids):
        r"""Sets the issue_ids of this WorkItemFlowVO.

        **参数解释**： 工作项唯一Id数组。可以通过[查询工作项列表](ListIpdProjectIssues.xml)或者[查询树状工作项](ShowIpdIssueTree.xml)接口获取，响应消息体中的**id**字段的值就是工作项ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param issue_ids: The issue_ids of this WorkItemFlowVO.
        :type issue_ids: list[str]
        """
        self._issue_ids = issue_ids

    @property
    def process_context(self):
        r"""Gets the process_context of this WorkItemFlowVO.

        **参数解释**： 流转中配置上下文信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The process_context of this WorkItemFlowVO.
        :rtype: dict(str, object)
        """
        return self._process_context

    @process_context.setter
    def process_context(self, process_context):
        r"""Sets the process_context of this WorkItemFlowVO.

        **参数解释**： 流转中配置上下文信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param process_context: The process_context of this WorkItemFlowVO.
        :type process_context: dict(str, object)
        """
        self._process_context = process_context

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
        if not isinstance(other, WorkItemFlowVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
