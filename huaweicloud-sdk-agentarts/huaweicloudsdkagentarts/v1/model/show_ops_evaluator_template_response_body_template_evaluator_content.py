# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'input_schemas': 'list[ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentInputSchemas]',
        'output_schemas': 'list[ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentOutputSchemas]',
        'prompt_evaluator': 'ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluator',
        'receive_chat_history': 'bool'
    }

    attribute_map = {
        'input_schemas': 'input_schemas',
        'output_schemas': 'output_schemas',
        'prompt_evaluator': 'prompt_evaluator',
        'receive_chat_history': 'receive_chat_history'
    }

    def __init__(self, input_schemas=None, output_schemas=None, prompt_evaluator=None, receive_chat_history=None):
        r"""ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContent

        The model defined in huaweicloud sdk

        :param input_schemas: **参数解释：** 输入参数定义列表。 **取值范围：** 不涉及。 
        :type input_schemas: list[:class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentInputSchemas`]
        :param output_schemas: **参数解释：** 输出参数定义评估器返回值的格式和结构。 **取值范围：** 不涉及。 
        :type output_schemas: list[:class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentOutputSchemas`]
        :param prompt_evaluator: 
        :type prompt_evaluator: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluator`
        :param receive_chat_history: **参数解释：** 标识是否需要接收对话历史。 **取值范围：** true (是), false (否)。 
        :type receive_chat_history: bool
        """
        
        

        self._input_schemas = None
        self._output_schemas = None
        self._prompt_evaluator = None
        self._receive_chat_history = None
        self.discriminator = None

        self.input_schemas = input_schemas
        self.output_schemas = output_schemas
        self.prompt_evaluator = prompt_evaluator
        if receive_chat_history is not None:
            self.receive_chat_history = receive_chat_history

    @property
    def input_schemas(self):
        r"""Gets the input_schemas of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContent.

        **参数解释：** 输入参数定义列表。 **取值范围：** 不涉及。 

        :return: The input_schemas of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContent.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentInputSchemas`]
        """
        return self._input_schemas

    @input_schemas.setter
    def input_schemas(self, input_schemas):
        r"""Sets the input_schemas of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContent.

        **参数解释：** 输入参数定义列表。 **取值范围：** 不涉及。 

        :param input_schemas: The input_schemas of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContent.
        :type input_schemas: list[:class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentInputSchemas`]
        """
        self._input_schemas = input_schemas

    @property
    def output_schemas(self):
        r"""Gets the output_schemas of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContent.

        **参数解释：** 输出参数定义评估器返回值的格式和结构。 **取值范围：** 不涉及。 

        :return: The output_schemas of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContent.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentOutputSchemas`]
        """
        return self._output_schemas

    @output_schemas.setter
    def output_schemas(self, output_schemas):
        r"""Sets the output_schemas of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContent.

        **参数解释：** 输出参数定义评估器返回值的格式和结构。 **取值范围：** 不涉及。 

        :param output_schemas: The output_schemas of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContent.
        :type output_schemas: list[:class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentOutputSchemas`]
        """
        self._output_schemas = output_schemas

    @property
    def prompt_evaluator(self):
        r"""Gets the prompt_evaluator of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContent.

        :return: The prompt_evaluator of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContent.
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluator`
        """
        return self._prompt_evaluator

    @prompt_evaluator.setter
    def prompt_evaluator(self, prompt_evaluator):
        r"""Sets the prompt_evaluator of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContent.

        :param prompt_evaluator: The prompt_evaluator of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContent.
        :type prompt_evaluator: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluator`
        """
        self._prompt_evaluator = prompt_evaluator

    @property
    def receive_chat_history(self):
        r"""Gets the receive_chat_history of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContent.

        **参数解释：** 标识是否需要接收对话历史。 **取值范围：** true (是), false (否)。 

        :return: The receive_chat_history of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContent.
        :rtype: bool
        """
        return self._receive_chat_history

    @receive_chat_history.setter
    def receive_chat_history(self, receive_chat_history):
        r"""Sets the receive_chat_history of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContent.

        **参数解释：** 标识是否需要接收对话历史。 **取值范围：** true (是), false (否)。 

        :param receive_chat_history: The receive_chat_history of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContent.
        :type receive_chat_history: bool
        """
        self._receive_chat_history = receive_chat_history

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
        if not isinstance(other, ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
