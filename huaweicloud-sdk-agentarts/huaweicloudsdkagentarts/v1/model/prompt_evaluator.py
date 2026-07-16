# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PromptEvaluator:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'message_list': 'list[object]',
        'model_config': 'EvaluationOpsModelConfig',
        'prompt_source_type': 'int',
        'prompt_template_key': 'str',
        'prompt_template_name': 'str'
    }

    attribute_map = {
        'message_list': 'message_list',
        'model_config': 'model_config',
        'prompt_source_type': 'prompt_source_type',
        'prompt_template_key': 'prompt_template_key',
        'prompt_template_name': 'prompt_template_name'
    }

    def __init__(self, message_list=None, model_config=None, prompt_source_type=None, prompt_template_key=None, prompt_template_name=None):
        r"""PromptEvaluator

        The model defined in huaweicloud sdk

        :param message_list: **参数解释：** 消息列表，包含评估过程中的对话记录或消息对象。 
        :type message_list: list[object]
        :param model_config: 
        :type model_config: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsModelConfig`
        :param prompt_source_type: **参数解释：** 提示词（Prompt）的来源类型。 
        :type prompt_source_type: int
        :param prompt_template_key: **参数解释：** 提示词模板的唯一关键字（Key）。 
        :type prompt_template_key: str
        :param prompt_template_name: **参数解释：** 提示词模板的显示名称。 
        :type prompt_template_name: str
        """
        
        

        self._message_list = None
        self._model_config = None
        self._prompt_source_type = None
        self._prompt_template_key = None
        self._prompt_template_name = None
        self.discriminator = None

        if message_list is not None:
            self.message_list = message_list
        if model_config is not None:
            self.model_config = model_config
        if prompt_source_type is not None:
            self.prompt_source_type = prompt_source_type
        if prompt_template_key is not None:
            self.prompt_template_key = prompt_template_key
        if prompt_template_name is not None:
            self.prompt_template_name = prompt_template_name

    @property
    def message_list(self):
        r"""Gets the message_list of this PromptEvaluator.

        **参数解释：** 消息列表，包含评估过程中的对话记录或消息对象。 

        :return: The message_list of this PromptEvaluator.
        :rtype: list[object]
        """
        return self._message_list

    @message_list.setter
    def message_list(self, message_list):
        r"""Sets the message_list of this PromptEvaluator.

        **参数解释：** 消息列表，包含评估过程中的对话记录或消息对象。 

        :param message_list: The message_list of this PromptEvaluator.
        :type message_list: list[object]
        """
        self._message_list = message_list

    @property
    def model_config(self):
        r"""Gets the model_config of this PromptEvaluator.

        :return: The model_config of this PromptEvaluator.
        :rtype: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsModelConfig`
        """
        return self._model_config

    @model_config.setter
    def model_config(self, model_config):
        r"""Sets the model_config of this PromptEvaluator.

        :param model_config: The model_config of this PromptEvaluator.
        :type model_config: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsModelConfig`
        """
        self._model_config = model_config

    @property
    def prompt_source_type(self):
        r"""Gets the prompt_source_type of this PromptEvaluator.

        **参数解释：** 提示词（Prompt）的来源类型。 

        :return: The prompt_source_type of this PromptEvaluator.
        :rtype: int
        """
        return self._prompt_source_type

    @prompt_source_type.setter
    def prompt_source_type(self, prompt_source_type):
        r"""Sets the prompt_source_type of this PromptEvaluator.

        **参数解释：** 提示词（Prompt）的来源类型。 

        :param prompt_source_type: The prompt_source_type of this PromptEvaluator.
        :type prompt_source_type: int
        """
        self._prompt_source_type = prompt_source_type

    @property
    def prompt_template_key(self):
        r"""Gets the prompt_template_key of this PromptEvaluator.

        **参数解释：** 提示词模板的唯一关键字（Key）。 

        :return: The prompt_template_key of this PromptEvaluator.
        :rtype: str
        """
        return self._prompt_template_key

    @prompt_template_key.setter
    def prompt_template_key(self, prompt_template_key):
        r"""Sets the prompt_template_key of this PromptEvaluator.

        **参数解释：** 提示词模板的唯一关键字（Key）。 

        :param prompt_template_key: The prompt_template_key of this PromptEvaluator.
        :type prompt_template_key: str
        """
        self._prompt_template_key = prompt_template_key

    @property
    def prompt_template_name(self):
        r"""Gets the prompt_template_name of this PromptEvaluator.

        **参数解释：** 提示词模板的显示名称。 

        :return: The prompt_template_name of this PromptEvaluator.
        :rtype: str
        """
        return self._prompt_template_name

    @prompt_template_name.setter
    def prompt_template_name(self, prompt_template_name):
        r"""Sets the prompt_template_name of this PromptEvaluator.

        **参数解释：** 提示词模板的显示名称。 

        :param prompt_template_name: The prompt_template_name of this PromptEvaluator.
        :type prompt_template_name: str
        """
        self._prompt_template_name = prompt_template_name

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
        if not isinstance(other, PromptEvaluator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
