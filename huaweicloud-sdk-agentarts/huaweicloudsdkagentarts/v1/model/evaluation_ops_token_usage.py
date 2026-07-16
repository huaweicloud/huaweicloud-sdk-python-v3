# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EvaluationOpsTokenUsage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'prompt_tokens': 'int',
        'completion_tokens': 'int',
        'total_tokens': 'int'
    }

    attribute_map = {
        'prompt_tokens': 'prompt_tokens',
        'completion_tokens': 'completion_tokens',
        'total_tokens': 'total_tokens'
    }

    def __init__(self, prompt_tokens=None, completion_tokens=None, total_tokens=None):
        r"""EvaluationOpsTokenUsage

        The model defined in huaweicloud sdk

        :param prompt_tokens: **参数解释：**   输入提示词所消耗的Token数量。 **取值范围：**   0-9,999,999,999。 
        :type prompt_tokens: int
        :param completion_tokens: **参数解释：**   模型生成内容所消耗的Token数量。 **取值范围：**   0-9,999,999,999。 
        :type completion_tokens: int
        :param total_tokens: **参数解释：**   本次任务产生的Token消耗总量。 **取值范围：**   0-9,999,999,999。 
        :type total_tokens: int
        """
        
        

        self._prompt_tokens = None
        self._completion_tokens = None
        self._total_tokens = None
        self.discriminator = None

        if prompt_tokens is not None:
            self.prompt_tokens = prompt_tokens
        if completion_tokens is not None:
            self.completion_tokens = completion_tokens
        if total_tokens is not None:
            self.total_tokens = total_tokens

    @property
    def prompt_tokens(self):
        r"""Gets the prompt_tokens of this EvaluationOpsTokenUsage.

        **参数解释：**   输入提示词所消耗的Token数量。 **取值范围：**   0-9,999,999,999。 

        :return: The prompt_tokens of this EvaluationOpsTokenUsage.
        :rtype: int
        """
        return self._prompt_tokens

    @prompt_tokens.setter
    def prompt_tokens(self, prompt_tokens):
        r"""Sets the prompt_tokens of this EvaluationOpsTokenUsage.

        **参数解释：**   输入提示词所消耗的Token数量。 **取值范围：**   0-9,999,999,999。 

        :param prompt_tokens: The prompt_tokens of this EvaluationOpsTokenUsage.
        :type prompt_tokens: int
        """
        self._prompt_tokens = prompt_tokens

    @property
    def completion_tokens(self):
        r"""Gets the completion_tokens of this EvaluationOpsTokenUsage.

        **参数解释：**   模型生成内容所消耗的Token数量。 **取值范围：**   0-9,999,999,999。 

        :return: The completion_tokens of this EvaluationOpsTokenUsage.
        :rtype: int
        """
        return self._completion_tokens

    @completion_tokens.setter
    def completion_tokens(self, completion_tokens):
        r"""Sets the completion_tokens of this EvaluationOpsTokenUsage.

        **参数解释：**   模型生成内容所消耗的Token数量。 **取值范围：**   0-9,999,999,999。 

        :param completion_tokens: The completion_tokens of this EvaluationOpsTokenUsage.
        :type completion_tokens: int
        """
        self._completion_tokens = completion_tokens

    @property
    def total_tokens(self):
        r"""Gets the total_tokens of this EvaluationOpsTokenUsage.

        **参数解释：**   本次任务产生的Token消耗总量。 **取值范围：**   0-9,999,999,999。 

        :return: The total_tokens of this EvaluationOpsTokenUsage.
        :rtype: int
        """
        return self._total_tokens

    @total_tokens.setter
    def total_tokens(self, total_tokens):
        r"""Sets the total_tokens of this EvaluationOpsTokenUsage.

        **参数解释：**   本次任务产生的Token消耗总量。 **取值范围：**   0-9,999,999,999。 

        :param total_tokens: The total_tokens of this EvaluationOpsTokenUsage.
        :type total_tokens: int
        """
        self._total_tokens = total_tokens

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
        if not isinstance(other, EvaluationOpsTokenUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
