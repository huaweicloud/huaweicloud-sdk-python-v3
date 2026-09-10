# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateOpsAgentTuningTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_tuning_task_id': 'str',
        'body': 'UpdateOpsAgentTuningTaskRequestBody'
    }

    attribute_map = {
        'agent_tuning_task_id': 'agent_tuning_task_id',
        'body': 'body'
    }

    def __init__(self, agent_tuning_task_id=None, body=None):
        r"""UpdateOpsAgentTuningTaskRequest

        The model defined in huaweicloud sdk

        :param agent_tuning_task_id: **参数解释：** 智能体优化任务ID，标识任务的唯一标识符。获取方法请参考查询智能体优化任务列表。  **约束限制：** 不涉及  **取值范围：** 32位ID字符串。  **默认取值：** 无
        :type agent_tuning_task_id: str
        :param body: Body of the UpdateOpsAgentTuningTaskRequest
        :type body: :class:`huaweicloudsdkagentarts.v1.UpdateOpsAgentTuningTaskRequestBody`
        """
        
        

        self._agent_tuning_task_id = None
        self._body = None
        self.discriminator = None

        self.agent_tuning_task_id = agent_tuning_task_id
        if body is not None:
            self.body = body

    @property
    def agent_tuning_task_id(self):
        r"""Gets the agent_tuning_task_id of this UpdateOpsAgentTuningTaskRequest.

        **参数解释：** 智能体优化任务ID，标识任务的唯一标识符。获取方法请参考查询智能体优化任务列表。  **约束限制：** 不涉及  **取值范围：** 32位ID字符串。  **默认取值：** 无

        :return: The agent_tuning_task_id of this UpdateOpsAgentTuningTaskRequest.
        :rtype: str
        """
        return self._agent_tuning_task_id

    @agent_tuning_task_id.setter
    def agent_tuning_task_id(self, agent_tuning_task_id):
        r"""Sets the agent_tuning_task_id of this UpdateOpsAgentTuningTaskRequest.

        **参数解释：** 智能体优化任务ID，标识任务的唯一标识符。获取方法请参考查询智能体优化任务列表。  **约束限制：** 不涉及  **取值范围：** 32位ID字符串。  **默认取值：** 无

        :param agent_tuning_task_id: The agent_tuning_task_id of this UpdateOpsAgentTuningTaskRequest.
        :type agent_tuning_task_id: str
        """
        self._agent_tuning_task_id = agent_tuning_task_id

    @property
    def body(self):
        r"""Gets the body of this UpdateOpsAgentTuningTaskRequest.

        :return: The body of this UpdateOpsAgentTuningTaskRequest.
        :rtype: :class:`huaweicloudsdkagentarts.v1.UpdateOpsAgentTuningTaskRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateOpsAgentTuningTaskRequest.

        :param body: The body of this UpdateOpsAgentTuningTaskRequest.
        :type body: :class:`huaweicloudsdkagentarts.v1.UpdateOpsAgentTuningTaskRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateOpsAgentTuningTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
