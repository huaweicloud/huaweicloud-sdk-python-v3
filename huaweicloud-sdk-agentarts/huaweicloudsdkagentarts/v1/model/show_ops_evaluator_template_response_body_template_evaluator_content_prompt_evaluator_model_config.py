# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorModelConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_tokens': 'int',
        'model_id': 'str',
        'model_name': 'str',
        'temperature': 'float',
        'top_p': 'float'
    }

    attribute_map = {
        'max_tokens': 'max_tokens',
        'model_id': 'model_id',
        'model_name': 'model_name',
        'temperature': 'temperature',
        'top_p': 'top_p'
    }

    def __init__(self, max_tokens=None, model_id=None, model_name=None, temperature=None, top_p=None):
        r"""ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorModelConfig

        The model defined in huaweicloud sdk

        :param max_tokens: **参数解释：** 最大Token限制模型生成长度。 **取值范围：** 由具体模型能力决定。 
        :type max_tokens: int
        :param model_id: **参数解释：** 模型的唯一标识符。 **取值范围：** 系统预置的模型ID。 
        :type model_id: str
        :param model_name: **参数解释：** 模型的显示名称。 **取值范围：** 不涉及。 
        :type model_name: str
        :param temperature: **参数解释：** 温度控制生成内容的随机性。 **取值范围：** 不涉及。 
        :type temperature: float
        :param top_p: **参数解释：** 核采样控制词汇选择范围。 **取值范围：** 不涉及。 
        :type top_p: float
        """
        
        

        self._max_tokens = None
        self._model_id = None
        self._model_name = None
        self._temperature = None
        self._top_p = None
        self.discriminator = None

        if max_tokens is not None:
            self.max_tokens = max_tokens
        if model_id is not None:
            self.model_id = model_id
        if model_name is not None:
            self.model_name = model_name
        if temperature is not None:
            self.temperature = temperature
        if top_p is not None:
            self.top_p = top_p

    @property
    def max_tokens(self):
        r"""Gets the max_tokens of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorModelConfig.

        **参数解释：** 最大Token限制模型生成长度。 **取值范围：** 由具体模型能力决定。 

        :return: The max_tokens of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorModelConfig.
        :rtype: int
        """
        return self._max_tokens

    @max_tokens.setter
    def max_tokens(self, max_tokens):
        r"""Sets the max_tokens of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorModelConfig.

        **参数解释：** 最大Token限制模型生成长度。 **取值范围：** 由具体模型能力决定。 

        :param max_tokens: The max_tokens of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorModelConfig.
        :type max_tokens: int
        """
        self._max_tokens = max_tokens

    @property
    def model_id(self):
        r"""Gets the model_id of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorModelConfig.

        **参数解释：** 模型的唯一标识符。 **取值范围：** 系统预置的模型ID。 

        :return: The model_id of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorModelConfig.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        r"""Sets the model_id of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorModelConfig.

        **参数解释：** 模型的唯一标识符。 **取值范围：** 系统预置的模型ID。 

        :param model_id: The model_id of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorModelConfig.
        :type model_id: str
        """
        self._model_id = model_id

    @property
    def model_name(self):
        r"""Gets the model_name of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorModelConfig.

        **参数解释：** 模型的显示名称。 **取值范围：** 不涉及。 

        :return: The model_name of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorModelConfig.
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        r"""Sets the model_name of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorModelConfig.

        **参数解释：** 模型的显示名称。 **取值范围：** 不涉及。 

        :param model_name: The model_name of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorModelConfig.
        :type model_name: str
        """
        self._model_name = model_name

    @property
    def temperature(self):
        r"""Gets the temperature of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorModelConfig.

        **参数解释：** 温度控制生成内容的随机性。 **取值范围：** 不涉及。 

        :return: The temperature of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorModelConfig.
        :rtype: float
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        r"""Sets the temperature of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorModelConfig.

        **参数解释：** 温度控制生成内容的随机性。 **取值范围：** 不涉及。 

        :param temperature: The temperature of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorModelConfig.
        :type temperature: float
        """
        self._temperature = temperature

    @property
    def top_p(self):
        r"""Gets the top_p of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorModelConfig.

        **参数解释：** 核采样控制词汇选择范围。 **取值范围：** 不涉及。 

        :return: The top_p of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorModelConfig.
        :rtype: float
        """
        return self._top_p

    @top_p.setter
    def top_p(self, top_p):
        r"""Sets the top_p of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorModelConfig.

        **参数解释：** 核采样控制词汇选择范围。 **取值范围：** 不涉及。 

        :param top_p: The top_p of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorModelConfig.
        :type top_p: float
        """
        self._top_p = top_p

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
        if not isinstance(other, ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorModelConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
