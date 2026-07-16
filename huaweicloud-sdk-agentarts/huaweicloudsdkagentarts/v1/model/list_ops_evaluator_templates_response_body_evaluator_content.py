# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsEvaluatorTemplatesResponseBodyEvaluatorContent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'input_schemas': 'list[ListOpsEvaluatorTemplatesResponseBodyEvaluatorContentInputSchemas]',
        'output_schemas': 'list[ListOpsEvaluatorTemplatesResponseBodyEvaluatorContentOutputSchemas]',
        'prompt_evaluator': 'ListOpsEvaluatorTemplatesResponseBodyEvaluatorContentPromptEvaluator',
        'receive_chat_history': 'bool'
    }

    attribute_map = {
        'input_schemas': 'input_schemas',
        'output_schemas': 'output_schemas',
        'prompt_evaluator': 'prompt_evaluator',
        'receive_chat_history': 'receive_chat_history'
    }

    def __init__(self, input_schemas=None, output_schemas=None, prompt_evaluator=None, receive_chat_history=None):
        r"""ListOpsEvaluatorTemplatesResponseBodyEvaluatorContent

        The model defined in huaweicloud sdk

        :param input_schemas: **参数解释：** 输入参数定义评估器接收的数据格式。 **取值范围：** 包含json_schema、key等的对象。 
        :type input_schemas: list[:class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorTemplatesResponseBodyEvaluatorContentInputSchemas`]
        :param output_schemas: **参数解释：** 输出参数定义。 **取值范围：** 不涉及。 
        :type output_schemas: list[:class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorTemplatesResponseBodyEvaluatorContentOutputSchemas`]
        :param prompt_evaluator: 
        :type prompt_evaluator: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorTemplatesResponseBodyEvaluatorContentPromptEvaluator`
        :param receive_chat_history: **参数解释：** 是否接收聊天记录上下文。 **取值范围：** true: 接收, false: 不接收。 
        :type receive_chat_history: bool
        """
        
        

        self._input_schemas = None
        self._output_schemas = None
        self._prompt_evaluator = None
        self._receive_chat_history = None
        self.discriminator = None

        if input_schemas is not None:
            self.input_schemas = input_schemas
        if output_schemas is not None:
            self.output_schemas = output_schemas
        if prompt_evaluator is not None:
            self.prompt_evaluator = prompt_evaluator
        if receive_chat_history is not None:
            self.receive_chat_history = receive_chat_history

    @property
    def input_schemas(self):
        r"""Gets the input_schemas of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorContent.

        **参数解释：** 输入参数定义评估器接收的数据格式。 **取值范围：** 包含json_schema、key等的对象。 

        :return: The input_schemas of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorContent.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorTemplatesResponseBodyEvaluatorContentInputSchemas`]
        """
        return self._input_schemas

    @input_schemas.setter
    def input_schemas(self, input_schemas):
        r"""Sets the input_schemas of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorContent.

        **参数解释：** 输入参数定义评估器接收的数据格式。 **取值范围：** 包含json_schema、key等的对象。 

        :param input_schemas: The input_schemas of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorContent.
        :type input_schemas: list[:class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorTemplatesResponseBodyEvaluatorContentInputSchemas`]
        """
        self._input_schemas = input_schemas

    @property
    def output_schemas(self):
        r"""Gets the output_schemas of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorContent.

        **参数解释：** 输出参数定义。 **取值范围：** 不涉及。 

        :return: The output_schemas of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorContent.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorTemplatesResponseBodyEvaluatorContentOutputSchemas`]
        """
        return self._output_schemas

    @output_schemas.setter
    def output_schemas(self, output_schemas):
        r"""Sets the output_schemas of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorContent.

        **参数解释：** 输出参数定义。 **取值范围：** 不涉及。 

        :param output_schemas: The output_schemas of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorContent.
        :type output_schemas: list[:class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorTemplatesResponseBodyEvaluatorContentOutputSchemas`]
        """
        self._output_schemas = output_schemas

    @property
    def prompt_evaluator(self):
        r"""Gets the prompt_evaluator of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorContent.

        :return: The prompt_evaluator of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorContent.
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorTemplatesResponseBodyEvaluatorContentPromptEvaluator`
        """
        return self._prompt_evaluator

    @prompt_evaluator.setter
    def prompt_evaluator(self, prompt_evaluator):
        r"""Sets the prompt_evaluator of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorContent.

        :param prompt_evaluator: The prompt_evaluator of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorContent.
        :type prompt_evaluator: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorTemplatesResponseBodyEvaluatorContentPromptEvaluator`
        """
        self._prompt_evaluator = prompt_evaluator

    @property
    def receive_chat_history(self):
        r"""Gets the receive_chat_history of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorContent.

        **参数解释：** 是否接收聊天记录上下文。 **取值范围：** true: 接收, false: 不接收。 

        :return: The receive_chat_history of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorContent.
        :rtype: bool
        """
        return self._receive_chat_history

    @receive_chat_history.setter
    def receive_chat_history(self, receive_chat_history):
        r"""Sets the receive_chat_history of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorContent.

        **参数解释：** 是否接收聊天记录上下文。 **取值范围：** true: 接收, false: 不接收。 

        :param receive_chat_history: The receive_chat_history of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorContent.
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
        if not isinstance(other, ListOpsEvaluatorTemplatesResponseBodyEvaluatorContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
