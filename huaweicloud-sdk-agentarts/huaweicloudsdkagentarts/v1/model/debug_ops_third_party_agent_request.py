# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DebugOpsThirdPartyAgentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_id': 'str',
        'body': 'DebugOpsThirdPartyAgentRequestBody'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'body': 'body'
    }

    def __init__(self, agent_id=None, body=None):
        r"""DebugOpsThirdPartyAgentRequest

        The model defined in huaweicloud sdk

        :param agent_id: **参数解释：** 合成任务的唯一标识符（ID），该参数用于在路径中指定特定的合成任务，以便执行查询、停止或删除等操作。获取方式：可通过创建合成任务接口返回的id获取，或通过查询合成任务列表接口获取。 **约束限制：** 不涉及。 **取值范围：** 1~36个字符，通常采用标准UUID格式。 **默认取值：** 不涉及。
        :type agent_id: str
        :param body: Body of the DebugOpsThirdPartyAgentRequest
        :type body: :class:`huaweicloudsdkagentarts.v1.DebugOpsThirdPartyAgentRequestBody`
        """
        
        

        self._agent_id = None
        self._body = None
        self.discriminator = None

        self.agent_id = agent_id
        if body is not None:
            self.body = body

    @property
    def agent_id(self):
        r"""Gets the agent_id of this DebugOpsThirdPartyAgentRequest.

        **参数解释：** 合成任务的唯一标识符（ID），该参数用于在路径中指定特定的合成任务，以便执行查询、停止或删除等操作。获取方式：可通过创建合成任务接口返回的id获取，或通过查询合成任务列表接口获取。 **约束限制：** 不涉及。 **取值范围：** 1~36个字符，通常采用标准UUID格式。 **默认取值：** 不涉及。

        :return: The agent_id of this DebugOpsThirdPartyAgentRequest.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this DebugOpsThirdPartyAgentRequest.

        **参数解释：** 合成任务的唯一标识符（ID），该参数用于在路径中指定特定的合成任务，以便执行查询、停止或删除等操作。获取方式：可通过创建合成任务接口返回的id获取，或通过查询合成任务列表接口获取。 **约束限制：** 不涉及。 **取值范围：** 1~36个字符，通常采用标准UUID格式。 **默认取值：** 不涉及。

        :param agent_id: The agent_id of this DebugOpsThirdPartyAgentRequest.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def body(self):
        r"""Gets the body of this DebugOpsThirdPartyAgentRequest.

        :return: The body of this DebugOpsThirdPartyAgentRequest.
        :rtype: :class:`huaweicloudsdkagentarts.v1.DebugOpsThirdPartyAgentRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this DebugOpsThirdPartyAgentRequest.

        :param body: The body of this DebugOpsThirdPartyAgentRequest.
        :type body: :class:`huaweicloudsdkagentarts.v1.DebugOpsThirdPartyAgentRequestBody`
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
        if not isinstance(other, DebugOpsThirdPartyAgentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
