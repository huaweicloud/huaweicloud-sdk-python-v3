# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluator:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'message_list': 'list[ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorMessageList]',
        'model_config': 'ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorModelConfig'
    }

    attribute_map = {
        'message_list': 'message_list',
        'model_config': 'model_config'
    }

    def __init__(self, message_list=None, model_config=None):
        r"""ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluator

        The model defined in huaweicloud sdk

        :param message_list: **参数解释：** prompt 信息列表包含各种角色提示词。 **取值范围：** 不涉及。 
        :type message_list: list[:class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorMessageList`]
        :param model_config: 
        :type model_config: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorModelConfig`
        """
        
        

        self._message_list = None
        self._model_config = None
        self.discriminator = None

        if message_list is not None:
            self.message_list = message_list
        if model_config is not None:
            self.model_config = model_config

    @property
    def message_list(self):
        r"""Gets the message_list of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluator.

        **参数解释：** prompt 信息列表包含各种角色提示词。 **取值范围：** 不涉及。 

        :return: The message_list of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluator.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorMessageList`]
        """
        return self._message_list

    @message_list.setter
    def message_list(self, message_list):
        r"""Sets the message_list of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluator.

        **参数解释：** prompt 信息列表包含各种角色提示词。 **取值范围：** 不涉及。 

        :param message_list: The message_list of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluator.
        :type message_list: list[:class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorMessageList`]
        """
        self._message_list = message_list

    @property
    def model_config(self):
        r"""Gets the model_config of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluator.

        :return: The model_config of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluator.
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorModelConfig`
        """
        return self._model_config

    @model_config.setter
    def model_config(self, model_config):
        r"""Sets the model_config of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluator.

        :param model_config: The model_config of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluator.
        :type model_config: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorModelConfig`
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
        if not isinstance(other, ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
