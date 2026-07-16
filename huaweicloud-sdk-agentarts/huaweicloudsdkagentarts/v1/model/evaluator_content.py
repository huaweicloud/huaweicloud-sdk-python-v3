# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EvaluatorContent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'prompt_evaluator': 'PromptEvaluator',
        'input_schemas': 'list[object]'
    }

    attribute_map = {
        'prompt_evaluator': 'prompt_evaluator',
        'input_schemas': 'input_schemas'
    }

    def __init__(self, prompt_evaluator=None, input_schemas=None):
        r"""EvaluatorContent

        The model defined in huaweicloud sdk

        :param prompt_evaluator: 
        :type prompt_evaluator: :class:`huaweicloudsdkagentarts.v1.PromptEvaluator`
        :param input_schemas: **参数解释：** 评估器输入参数的Schema定义列表。 
        :type input_schemas: list[object]
        """
        
        

        self._prompt_evaluator = None
        self._input_schemas = None
        self.discriminator = None

        if prompt_evaluator is not None:
            self.prompt_evaluator = prompt_evaluator
        if input_schemas is not None:
            self.input_schemas = input_schemas

    @property
    def prompt_evaluator(self):
        r"""Gets the prompt_evaluator of this EvaluatorContent.

        :return: The prompt_evaluator of this EvaluatorContent.
        :rtype: :class:`huaweicloudsdkagentarts.v1.PromptEvaluator`
        """
        return self._prompt_evaluator

    @prompt_evaluator.setter
    def prompt_evaluator(self, prompt_evaluator):
        r"""Sets the prompt_evaluator of this EvaluatorContent.

        :param prompt_evaluator: The prompt_evaluator of this EvaluatorContent.
        :type prompt_evaluator: :class:`huaweicloudsdkagentarts.v1.PromptEvaluator`
        """
        self._prompt_evaluator = prompt_evaluator

    @property
    def input_schemas(self):
        r"""Gets the input_schemas of this EvaluatorContent.

        **参数解释：** 评估器输入参数的Schema定义列表。 

        :return: The input_schemas of this EvaluatorContent.
        :rtype: list[object]
        """
        return self._input_schemas

    @input_schemas.setter
    def input_schemas(self, input_schemas):
        r"""Sets the input_schemas of this EvaluatorContent.

        **参数解释：** 评估器输入参数的Schema定义列表。 

        :param input_schemas: The input_schemas of this EvaluatorContent.
        :type input_schemas: list[object]
        """
        self._input_schemas = input_schemas

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
        if not isinstance(other, EvaluatorContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
