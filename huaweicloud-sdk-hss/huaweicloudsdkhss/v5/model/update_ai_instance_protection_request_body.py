# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAiInstanceProtectionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_id_list': 'list[str]',
        'status': 'str'
    }

    attribute_map = {
        'agent_id_list': 'agent_id_list',
        'status': 'status'
    }

    def __init__(self, agent_id_list=None, status=None):
        r"""UpdateAiInstanceProtectionRequestBody

        The model defined in huaweicloud sdk

        :param agent_id_list: 需要修改防护状态的OpenClaw智能体ID列表 **约束限制**： - 单次最多50个 **取值范围**： 智能体实例的agent_id 
        :type agent_id_list: list[str]
        :param status: **参数解释**: 目标防护状态 **取值范围**: - open：开启防护 - close：关闭防 
        :type status: str
        """
        
        

        self._agent_id_list = None
        self._status = None
        self.discriminator = None

        self.agent_id_list = agent_id_list
        self.status = status

    @property
    def agent_id_list(self):
        r"""Gets the agent_id_list of this UpdateAiInstanceProtectionRequestBody.

        需要修改防护状态的OpenClaw智能体ID列表 **约束限制**： - 单次最多50个 **取值范围**： 智能体实例的agent_id 

        :return: The agent_id_list of this UpdateAiInstanceProtectionRequestBody.
        :rtype: list[str]
        """
        return self._agent_id_list

    @agent_id_list.setter
    def agent_id_list(self, agent_id_list):
        r"""Sets the agent_id_list of this UpdateAiInstanceProtectionRequestBody.

        需要修改防护状态的OpenClaw智能体ID列表 **约束限制**： - 单次最多50个 **取值范围**： 智能体实例的agent_id 

        :param agent_id_list: The agent_id_list of this UpdateAiInstanceProtectionRequestBody.
        :type agent_id_list: list[str]
        """
        self._agent_id_list = agent_id_list

    @property
    def status(self):
        r"""Gets the status of this UpdateAiInstanceProtectionRequestBody.

        **参数解释**: 目标防护状态 **取值范围**: - open：开启防护 - close：关闭防 

        :return: The status of this UpdateAiInstanceProtectionRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateAiInstanceProtectionRequestBody.

        **参数解释**: 目标防护状态 **取值范围**: - open：开启防护 - close：关闭防 

        :param status: The status of this UpdateAiInstanceProtectionRequestBody.
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
        if not isinstance(other, UpdateAiInstanceProtectionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
