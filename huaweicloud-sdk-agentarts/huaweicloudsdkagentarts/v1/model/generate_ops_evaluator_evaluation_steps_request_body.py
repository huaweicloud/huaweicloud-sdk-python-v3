# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GenerateOpsEvaluatorEvaluationStepsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'criteria': 'str',
        'model_config': 'GenerateOpsEvaluatorEvaluationStepsRequestBodyModelConfig'
    }

    attribute_map = {
        'criteria': 'criteria',
        'model_config': 'model_config'
    }

    def __init__(self, criteria=None, model_config=None):
        r"""GenerateOpsEvaluatorEvaluationStepsRequestBody

        The model defined in huaweicloud sdk

        :param criteria: **参数解释：** 评估标准描述，用于告知模型需要评估的维度和判断依据。  **约束限制：** - 长度必须在1到20000字符之间。 - 必须包含至少一个用双大括号{{}}包裹的变量。  **取值范围：** 符合自然语言规范的文本，支持中英文。  **示例取值：** \&quot;评估{{actual_output}}是否准确回答了{{input}}，并与{{reference_output}}进行对比\&quot; 
        :type criteria: str
        :param model_config: 
        :type model_config: :class:`huaweicloudsdkagentarts.v1.GenerateOpsEvaluatorEvaluationStepsRequestBodyModelConfig`
        """
        
        

        self._criteria = None
        self._model_config = None
        self.discriminator = None

        self.criteria = criteria
        self.model_config = model_config

    @property
    def criteria(self):
        r"""Gets the criteria of this GenerateOpsEvaluatorEvaluationStepsRequestBody.

        **参数解释：** 评估标准描述，用于告知模型需要评估的维度和判断依据。  **约束限制：** - 长度必须在1到20000字符之间。 - 必须包含至少一个用双大括号{{}}包裹的变量。  **取值范围：** 符合自然语言规范的文本，支持中英文。  **示例取值：** \"评估{{actual_output}}是否准确回答了{{input}}，并与{{reference_output}}进行对比\" 

        :return: The criteria of this GenerateOpsEvaluatorEvaluationStepsRequestBody.
        :rtype: str
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria):
        r"""Sets the criteria of this GenerateOpsEvaluatorEvaluationStepsRequestBody.

        **参数解释：** 评估标准描述，用于告知模型需要评估的维度和判断依据。  **约束限制：** - 长度必须在1到20000字符之间。 - 必须包含至少一个用双大括号{{}}包裹的变量。  **取值范围：** 符合自然语言规范的文本，支持中英文。  **示例取值：** \"评估{{actual_output}}是否准确回答了{{input}}，并与{{reference_output}}进行对比\" 

        :param criteria: The criteria of this GenerateOpsEvaluatorEvaluationStepsRequestBody.
        :type criteria: str
        """
        self._criteria = criteria

    @property
    def model_config(self):
        r"""Gets the model_config of this GenerateOpsEvaluatorEvaluationStepsRequestBody.

        :return: The model_config of this GenerateOpsEvaluatorEvaluationStepsRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.GenerateOpsEvaluatorEvaluationStepsRequestBodyModelConfig`
        """
        return self._model_config

    @model_config.setter
    def model_config(self, model_config):
        r"""Sets the model_config of this GenerateOpsEvaluatorEvaluationStepsRequestBody.

        :param model_config: The model_config of this GenerateOpsEvaluatorEvaluationStepsRequestBody.
        :type model_config: :class:`huaweicloudsdkagentarts.v1.GenerateOpsEvaluatorEvaluationStepsRequestBodyModelConfig`
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
        if not isinstance(other, GenerateOpsEvaluatorEvaluationStepsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
