# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GenerateOpsEvaluatorEvaluationStepsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'evaluation_steps': 'list[str]'
    }

    attribute_map = {
        'evaluation_steps': 'evaluation_steps'
    }

    def __init__(self, evaluation_steps=None):
        r"""GenerateOpsEvaluatorEvaluationStepsResponse

        The model defined in huaweicloud sdk

        :param evaluation_steps: **参数解释：** 生成的评估步骤列表，每个元素是一个独立的评估步骤描述。  **约束限制：** 列表不为空，最多返回10条评估步骤；每个步骤长度为1到200个字符。  **取值范围：** 符合评估任务要求的自然语言步骤。  **默认取值：** 不涉及。 
        :type evaluation_steps: list[str]
        """
        
        super().__init__()

        self._evaluation_steps = None
        self.discriminator = None

        if evaluation_steps is not None:
            self.evaluation_steps = evaluation_steps

    @property
    def evaluation_steps(self):
        r"""Gets the evaluation_steps of this GenerateOpsEvaluatorEvaluationStepsResponse.

        **参数解释：** 生成的评估步骤列表，每个元素是一个独立的评估步骤描述。  **约束限制：** 列表不为空，最多返回10条评估步骤；每个步骤长度为1到200个字符。  **取值范围：** 符合评估任务要求的自然语言步骤。  **默认取值：** 不涉及。 

        :return: The evaluation_steps of this GenerateOpsEvaluatorEvaluationStepsResponse.
        :rtype: list[str]
        """
        return self._evaluation_steps

    @evaluation_steps.setter
    def evaluation_steps(self, evaluation_steps):
        r"""Sets the evaluation_steps of this GenerateOpsEvaluatorEvaluationStepsResponse.

        **参数解释：** 生成的评估步骤列表，每个元素是一个独立的评估步骤描述。  **约束限制：** 列表不为空，最多返回10条评估步骤；每个步骤长度为1到200个字符。  **取值范围：** 符合评估任务要求的自然语言步骤。  **默认取值：** 不涉及。 

        :param evaluation_steps: The evaluation_steps of this GenerateOpsEvaluatorEvaluationStepsResponse.
        :type evaluation_steps: list[str]
        """
        self._evaluation_steps = evaluation_steps

    def to_dict(self):
        import warnings
        warnings.warn("GenerateOpsEvaluatorEvaluationStepsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, GenerateOpsEvaluatorEvaluationStepsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
