# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EvaluationOpsLLMConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'system_prompt': 'str',
        'model_config': 'EvaluationOpsModelConfig'
    }

    attribute_map = {
        'system_prompt': 'system_prompt',
        'model_config': 'model_config'
    }

    def __init__(self, system_prompt=None, model_config=None):
        r"""EvaluationOpsLLMConfig

        The model defined in huaweicloud sdk

        :param system_prompt: **参数解释：** 系统提示词（System Prompt），定义模型的角色与规则。 **约束限制：** 0到10000字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type system_prompt: str
        :param model_config: 
        :type model_config: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsModelConfig`
        """
        
        

        self._system_prompt = None
        self._model_config = None
        self.discriminator = None

        if system_prompt is not None:
            self.system_prompt = system_prompt
        if model_config is not None:
            self.model_config = model_config

    @property
    def system_prompt(self):
        r"""Gets the system_prompt of this EvaluationOpsLLMConfig.

        **参数解释：** 系统提示词（System Prompt），定义模型的角色与规则。 **约束限制：** 0到10000字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The system_prompt of this EvaluationOpsLLMConfig.
        :rtype: str
        """
        return self._system_prompt

    @system_prompt.setter
    def system_prompt(self, system_prompt):
        r"""Sets the system_prompt of this EvaluationOpsLLMConfig.

        **参数解释：** 系统提示词（System Prompt），定义模型的角色与规则。 **约束限制：** 0到10000字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param system_prompt: The system_prompt of this EvaluationOpsLLMConfig.
        :type system_prompt: str
        """
        self._system_prompt = system_prompt

    @property
    def model_config(self):
        r"""Gets the model_config of this EvaluationOpsLLMConfig.

        :return: The model_config of this EvaluationOpsLLMConfig.
        :rtype: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsModelConfig`
        """
        return self._model_config

    @model_config.setter
    def model_config(self, model_config):
        r"""Sets the model_config of this EvaluationOpsLLMConfig.

        :param model_config: The model_config of this EvaluationOpsLLMConfig.
        :type model_config: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsModelConfig`
        """
        self._model_config = model_config

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
        if not isinstance(other, EvaluationOpsLLMConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
