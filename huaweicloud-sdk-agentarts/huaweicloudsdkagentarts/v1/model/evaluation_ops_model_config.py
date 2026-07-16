# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EvaluationOpsModelConfig:

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
        'model_name': 'str',
        'temperature': 'float',
        'max_tokens': 'int',
        'top_p': 'float',
        'frequency_penalty': 'float'
    }

    attribute_map = {
        'model_id': 'model_id',
        'model_name': 'model_name',
        'temperature': 'temperature',
        'max_tokens': 'max_tokens',
        'top_p': 'top_p',
        'frequency_penalty': 'frequency_penalty'
    }

    def __init__(self, model_id=None, model_name=None, temperature=None, max_tokens=None, top_p=None, frequency_penalty=None):
        r"""EvaluationOpsModelConfig

        The model defined in huaweicloud sdk

        :param model_id: **参数解释：**   指定调用的大模型唯一标识符，通过模型列表接口获取。 
        :type model_id: str
        :param model_name: **参数解释：**   模型的显示名称。 **取值范围：**   任意字符串。 
        :type model_name: str
        :param temperature: **参数解释：**   采样温度参数，用于控制输出的随机性。数值低更聚焦，数值高更具创造性。 **取值范围：**   0.0到2.0。 
        :type temperature: float
        :param max_tokens: **参数解释：**   单次推理生成的最大Token数量限制。 **取值范围：**   1-32000。 
        :type max_tokens: int
        :param top_p: **参数解释：**   核采样参数。 **取值范围：**   0.0到1.0。 
        :type top_p: float
        :param frequency_penalty: **参数解释：**   频率惩罚系数，降低内容重复倾向。 **取值范围：**   -2.0到2.0。 
        :type frequency_penalty: float
        """
        
        

        self._model_id = None
        self._model_name = None
        self._temperature = None
        self._max_tokens = None
        self._top_p = None
        self._frequency_penalty = None
        self.discriminator = None

        self.model_id = model_id
        self.model_name = model_name
        if temperature is not None:
            self.temperature = temperature
        if max_tokens is not None:
            self.max_tokens = max_tokens
        if top_p is not None:
            self.top_p = top_p
        if frequency_penalty is not None:
            self.frequency_penalty = frequency_penalty

    @property
    def model_id(self):
        r"""Gets the model_id of this EvaluationOpsModelConfig.

        **参数解释：**   指定调用的大模型唯一标识符，通过模型列表接口获取。 

        :return: The model_id of this EvaluationOpsModelConfig.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        r"""Sets the model_id of this EvaluationOpsModelConfig.

        **参数解释：**   指定调用的大模型唯一标识符，通过模型列表接口获取。 

        :param model_id: The model_id of this EvaluationOpsModelConfig.
        :type model_id: str
        """
        self._model_id = model_id

    @property
    def model_name(self):
        r"""Gets the model_name of this EvaluationOpsModelConfig.

        **参数解释：**   模型的显示名称。 **取值范围：**   任意字符串。 

        :return: The model_name of this EvaluationOpsModelConfig.
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        r"""Sets the model_name of this EvaluationOpsModelConfig.

        **参数解释：**   模型的显示名称。 **取值范围：**   任意字符串。 

        :param model_name: The model_name of this EvaluationOpsModelConfig.
        :type model_name: str
        """
        self._model_name = model_name

    @property
    def temperature(self):
        r"""Gets the temperature of this EvaluationOpsModelConfig.

        **参数解释：**   采样温度参数，用于控制输出的随机性。数值低更聚焦，数值高更具创造性。 **取值范围：**   0.0到2.0。 

        :return: The temperature of this EvaluationOpsModelConfig.
        :rtype: float
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        r"""Sets the temperature of this EvaluationOpsModelConfig.

        **参数解释：**   采样温度参数，用于控制输出的随机性。数值低更聚焦，数值高更具创造性。 **取值范围：**   0.0到2.0。 

        :param temperature: The temperature of this EvaluationOpsModelConfig.
        :type temperature: float
        """
        self._temperature = temperature

    @property
    def max_tokens(self):
        r"""Gets the max_tokens of this EvaluationOpsModelConfig.

        **参数解释：**   单次推理生成的最大Token数量限制。 **取值范围：**   1-32000。 

        :return: The max_tokens of this EvaluationOpsModelConfig.
        :rtype: int
        """
        return self._max_tokens

    @max_tokens.setter
    def max_tokens(self, max_tokens):
        r"""Sets the max_tokens of this EvaluationOpsModelConfig.

        **参数解释：**   单次推理生成的最大Token数量限制。 **取值范围：**   1-32000。 

        :param max_tokens: The max_tokens of this EvaluationOpsModelConfig.
        :type max_tokens: int
        """
        self._max_tokens = max_tokens

    @property
    def top_p(self):
        r"""Gets the top_p of this EvaluationOpsModelConfig.

        **参数解释：**   核采样参数。 **取值范围：**   0.0到1.0。 

        :return: The top_p of this EvaluationOpsModelConfig.
        :rtype: float
        """
        return self._top_p

    @top_p.setter
    def top_p(self, top_p):
        r"""Sets the top_p of this EvaluationOpsModelConfig.

        **参数解释：**   核采样参数。 **取值范围：**   0.0到1.0。 

        :param top_p: The top_p of this EvaluationOpsModelConfig.
        :type top_p: float
        """
        self._top_p = top_p

    @property
    def frequency_penalty(self):
        r"""Gets the frequency_penalty of this EvaluationOpsModelConfig.

        **参数解释：**   频率惩罚系数，降低内容重复倾向。 **取值范围：**   -2.0到2.0。 

        :return: The frequency_penalty of this EvaluationOpsModelConfig.
        :rtype: float
        """
        return self._frequency_penalty

    @frequency_penalty.setter
    def frequency_penalty(self, frequency_penalty):
        r"""Sets the frequency_penalty of this EvaluationOpsModelConfig.

        **参数解释：**   频率惩罚系数，降低内容重复倾向。 **取值范围：**   -2.0到2.0。 

        :param frequency_penalty: The frequency_penalty of this EvaluationOpsModelConfig.
        :type frequency_penalty: float
        """
        self._frequency_penalty = frequency_penalty

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
        if not isinstance(other, EvaluationOpsModelConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
