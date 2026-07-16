# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorContent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content_type': 'str',
        'format': 'int',
        'text': 'str'
    }

    attribute_map = {
        'content_type': 'content_type',
        'format': 'format',
        'text': 'text'
    }

    def __init__(self, content_type=None, format=None, text=None):
        r"""ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorContent

        The model defined in huaweicloud sdk

        :param content_type: **参数解释：** 类型标识提示词内容的表现形式。 **取值范围：** Text。 
        :type content_type: str
        :param format: **参数解释：** 格式标识提示词内容的结构化形式。 **取值范围：** 不涉及。 
        :type format: int
        :param text: **参数解释：** 提示词的具体文本信息。 **取值范围：** 不涉及。 
        :type text: str
        """
        
        

        self._content_type = None
        self._format = None
        self._text = None
        self.discriminator = None

        if content_type is not None:
            self.content_type = content_type
        if format is not None:
            self.format = format
        if text is not None:
            self.text = text

    @property
    def content_type(self):
        r"""Gets the content_type of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorContent.

        **参数解释：** 类型标识提示词内容的表现形式。 **取值范围：** Text。 

        :return: The content_type of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorContent.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        r"""Sets the content_type of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorContent.

        **参数解释：** 类型标识提示词内容的表现形式。 **取值范围：** Text。 

        :param content_type: The content_type of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorContent.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def format(self):
        r"""Gets the format of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorContent.

        **参数解释：** 格式标识提示词内容的结构化形式。 **取值范围：** 不涉及。 

        :return: The format of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorContent.
        :rtype: int
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorContent.

        **参数解释：** 格式标识提示词内容的结构化形式。 **取值范围：** 不涉及。 

        :param format: The format of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorContent.
        :type format: int
        """
        self._format = format

    @property
    def text(self):
        r"""Gets the text of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorContent.

        **参数解释：** 提示词的具体文本信息。 **取值范围：** 不涉及。 

        :return: The text of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorContent.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        r"""Sets the text of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorContent.

        **参数解释：** 提示词的具体文本信息。 **取值范围：** 不涉及。 

        :param text: The text of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorContent.
        :type text: str
        """
        self._text = text

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
        if not isinstance(other, ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
