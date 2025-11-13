# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllAssistantModelsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'chain_of_thought': 'bool',
        'function_of_call': 'bool',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'chain_of_thought': 'chain_of_thought',
        'function_of_call': 'function_of_call',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, chain_of_thought=None, function_of_call=None, status=None, type=None):
        r"""ListAllAssistantModelsRequest

        The model defined in huaweicloud sdk

        :param chain_of_thought: **参数解释**： 是否支持思维链。 **约束限制**： 不涉及 **取值范围**： * true：支持思维链 * false：不支持思维链 **默认取值**： 不涉及 
        :type chain_of_thought: bool
        :param function_of_call: **参数解释**： 是否支持工具调用。 **约束限制**： 不涉及 **取值范围**： * true：支持工具调用 * false：不支持工具调用 **默认取值**： 不涉及 
        :type function_of_call: bool
        :param status: **参数解释**： 模型服务状态。 **约束限制**： 不涉及 **取值范围**： * available：已接入 * unavailable：未接入 **默认取值**： 不涉及 
        :type status: str
        :param type: **参数解释**： 模型类型。 **约束限制**： 不涉及 **取值范围**： * chat：文本对话模型 * embedding：嵌入式模型 **默认取值**： 不涉及 
        :type type: str
        """
        
        

        self._chain_of_thought = None
        self._function_of_call = None
        self._status = None
        self._type = None
        self.discriminator = None

        if chain_of_thought is not None:
            self.chain_of_thought = chain_of_thought
        if function_of_call is not None:
            self.function_of_call = function_of_call
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type

    @property
    def chain_of_thought(self):
        r"""Gets the chain_of_thought of this ListAllAssistantModelsRequest.

        **参数解释**： 是否支持思维链。 **约束限制**： 不涉及 **取值范围**： * true：支持思维链 * false：不支持思维链 **默认取值**： 不涉及 

        :return: The chain_of_thought of this ListAllAssistantModelsRequest.
        :rtype: bool
        """
        return self._chain_of_thought

    @chain_of_thought.setter
    def chain_of_thought(self, chain_of_thought):
        r"""Sets the chain_of_thought of this ListAllAssistantModelsRequest.

        **参数解释**： 是否支持思维链。 **约束限制**： 不涉及 **取值范围**： * true：支持思维链 * false：不支持思维链 **默认取值**： 不涉及 

        :param chain_of_thought: The chain_of_thought of this ListAllAssistantModelsRequest.
        :type chain_of_thought: bool
        """
        self._chain_of_thought = chain_of_thought

    @property
    def function_of_call(self):
        r"""Gets the function_of_call of this ListAllAssistantModelsRequest.

        **参数解释**： 是否支持工具调用。 **约束限制**： 不涉及 **取值范围**： * true：支持工具调用 * false：不支持工具调用 **默认取值**： 不涉及 

        :return: The function_of_call of this ListAllAssistantModelsRequest.
        :rtype: bool
        """
        return self._function_of_call

    @function_of_call.setter
    def function_of_call(self, function_of_call):
        r"""Sets the function_of_call of this ListAllAssistantModelsRequest.

        **参数解释**： 是否支持工具调用。 **约束限制**： 不涉及 **取值范围**： * true：支持工具调用 * false：不支持工具调用 **默认取值**： 不涉及 

        :param function_of_call: The function_of_call of this ListAllAssistantModelsRequest.
        :type function_of_call: bool
        """
        self._function_of_call = function_of_call

    @property
    def status(self):
        r"""Gets the status of this ListAllAssistantModelsRequest.

        **参数解释**： 模型服务状态。 **约束限制**： 不涉及 **取值范围**： * available：已接入 * unavailable：未接入 **默认取值**： 不涉及 

        :return: The status of this ListAllAssistantModelsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListAllAssistantModelsRequest.

        **参数解释**： 模型服务状态。 **约束限制**： 不涉及 **取值范围**： * available：已接入 * unavailable：未接入 **默认取值**： 不涉及 

        :param status: The status of this ListAllAssistantModelsRequest.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this ListAllAssistantModelsRequest.

        **参数解释**： 模型类型。 **约束限制**： 不涉及 **取值范围**： * chat：文本对话模型 * embedding：嵌入式模型 **默认取值**： 不涉及 

        :return: The type of this ListAllAssistantModelsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListAllAssistantModelsRequest.

        **参数解释**： 模型类型。 **约束限制**： 不涉及 **取值范围**： * chat：文本对话模型 * embedding：嵌入式模型 **默认取值**： 不涉及 

        :param type: The type of this ListAllAssistantModelsRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ListAllAssistantModelsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
