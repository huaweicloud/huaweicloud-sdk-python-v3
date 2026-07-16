# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GenerateOpsEvaluatorEvaluationStepsRequestBodyModelConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'model_id': 'str',
        'max_tokens': 'int',
        'temperature': 'float',
        'top_p': 'float'
    }

    attribute_map = {
        'model_id': 'model_id',
        'max_tokens': 'max_tokens',
        'temperature': 'temperature',
        'top_p': 'top_p'
    }

    def __init__(self, model_id=None, max_tokens=None, temperature=None, top_p=None):
        r"""GenerateOpsEvaluatorEvaluationStepsRequestBodyModelConfig

        The model defined in huaweicloud sdk

        :param model_id: **参数解释：** 用于生成评估步骤的大模型标识符。  **约束限制：** 必须是系统支持的模型ID。  **取值范围：** 1到128个字符，支持英文、数字、点号、下划线（_）、中划线（-）和冒号。  **默认取值：** 不涉及。 
        :type model_id: str
        :param max_tokens: **参数解释：** 模型生成的最大token数量，用于控制输出长度。  **约束限制：** 必须为正整数。  **取值范围：** 1到8192。  **默认取值：** 1000。 
        :type max_tokens: int
        :param temperature: **参数解释：** 温度参数，控制模型输出的随机性和创造性。值越低输出越确定，值越高输出越多样。  **约束限制：** 必须在0到1之间。  **取值范围：** 0到1。  **默认取值：** 0.1。 
        :type temperature: float
        :param top_p: **参数解释：** 核采样参数，控制模型从概率累积分布中采样的范围。  **约束限制：** 必须在0到1之间。  **取值范围：** 0到1。  **默认取值：** 0.3。 
        :type top_p: float
        """
        
        

        self._model_id = None
        self._max_tokens = None
        self._temperature = None
        self._top_p = None
        self.discriminator = None

        self.model_id = model_id
        if max_tokens is not None:
            self.max_tokens = max_tokens
        if temperature is not None:
            self.temperature = temperature
        if top_p is not None:
            self.top_p = top_p

    @property
    def model_id(self):
        r"""Gets the model_id of this GenerateOpsEvaluatorEvaluationStepsRequestBodyModelConfig.

        **参数解释：** 用于生成评估步骤的大模型标识符。  **约束限制：** 必须是系统支持的模型ID。  **取值范围：** 1到128个字符，支持英文、数字、点号、下划线（_）、中划线（-）和冒号。  **默认取值：** 不涉及。 

        :return: The model_id of this GenerateOpsEvaluatorEvaluationStepsRequestBodyModelConfig.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        r"""Sets the model_id of this GenerateOpsEvaluatorEvaluationStepsRequestBodyModelConfig.

        **参数解释：** 用于生成评估步骤的大模型标识符。  **约束限制：** 必须是系统支持的模型ID。  **取值范围：** 1到128个字符，支持英文、数字、点号、下划线（_）、中划线（-）和冒号。  **默认取值：** 不涉及。 

        :param model_id: The model_id of this GenerateOpsEvaluatorEvaluationStepsRequestBodyModelConfig.
        :type model_id: str
        """
        self._model_id = model_id

    @property
    def max_tokens(self):
        r"""Gets the max_tokens of this GenerateOpsEvaluatorEvaluationStepsRequestBodyModelConfig.

        **参数解释：** 模型生成的最大token数量，用于控制输出长度。  **约束限制：** 必须为正整数。  **取值范围：** 1到8192。  **默认取值：** 1000。 

        :return: The max_tokens of this GenerateOpsEvaluatorEvaluationStepsRequestBodyModelConfig.
        :rtype: int
        """
        return self._max_tokens

    @max_tokens.setter
    def max_tokens(self, max_tokens):
        r"""Sets the max_tokens of this GenerateOpsEvaluatorEvaluationStepsRequestBodyModelConfig.

        **参数解释：** 模型生成的最大token数量，用于控制输出长度。  **约束限制：** 必须为正整数。  **取值范围：** 1到8192。  **默认取值：** 1000。 

        :param max_tokens: The max_tokens of this GenerateOpsEvaluatorEvaluationStepsRequestBodyModelConfig.
        :type max_tokens: int
        """
        self._max_tokens = max_tokens

    @property
    def temperature(self):
        r"""Gets the temperature of this GenerateOpsEvaluatorEvaluationStepsRequestBodyModelConfig.

        **参数解释：** 温度参数，控制模型输出的随机性和创造性。值越低输出越确定，值越高输出越多样。  **约束限制：** 必须在0到1之间。  **取值范围：** 0到1。  **默认取值：** 0.1。 

        :return: The temperature of this GenerateOpsEvaluatorEvaluationStepsRequestBodyModelConfig.
        :rtype: float
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        r"""Sets the temperature of this GenerateOpsEvaluatorEvaluationStepsRequestBodyModelConfig.

        **参数解释：** 温度参数，控制模型输出的随机性和创造性。值越低输出越确定，值越高输出越多样。  **约束限制：** 必须在0到1之间。  **取值范围：** 0到1。  **默认取值：** 0.1。 

        :param temperature: The temperature of this GenerateOpsEvaluatorEvaluationStepsRequestBodyModelConfig.
        :type temperature: float
        """
        self._temperature = temperature

    @property
    def top_p(self):
        r"""Gets the top_p of this GenerateOpsEvaluatorEvaluationStepsRequestBodyModelConfig.

        **参数解释：** 核采样参数，控制模型从概率累积分布中采样的范围。  **约束限制：** 必须在0到1之间。  **取值范围：** 0到1。  **默认取值：** 0.3。 

        :return: The top_p of this GenerateOpsEvaluatorEvaluationStepsRequestBodyModelConfig.
        :rtype: float
        """
        return self._top_p

    @top_p.setter
    def top_p(self, top_p):
        r"""Sets the top_p of this GenerateOpsEvaluatorEvaluationStepsRequestBodyModelConfig.

        **参数解释：** 核采样参数，控制模型从概率累积分布中采样的范围。  **约束限制：** 必须在0到1之间。  **取值范围：** 0到1。  **默认取值：** 0.3。 

        :param top_p: The top_p of this GenerateOpsEvaluatorEvaluationStepsRequestBodyModelConfig.
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
        if not isinstance(other, GenerateOpsEvaluatorEvaluationStepsRequestBodyModelConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
