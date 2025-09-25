# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChatMessage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content': 'str',
        'reasoning_content': 'str',
        'tool_calls': 'list[ToolCall]'
    }

    attribute_map = {
        'content': 'content',
        'reasoning_content': 'reasoning_content',
        'tool_calls': 'tool_calls'
    }

    def __init__(self, content=None, reasoning_content=None, tool_calls=None):
        r"""ChatMessage

        The model defined in huaweicloud sdk

        :param content: **参数解释**： 对话内容。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type content: str
        :param reasoning_content: **参数解释**： 深度搜索思维链内容。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type reasoning_content: str
        :param tool_calls: **参数解释**： 工具调用列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type tool_calls: list[:class:`huaweicloudsdkeihealth.v1.ToolCall`]
        """
        
        

        self._content = None
        self._reasoning_content = None
        self._tool_calls = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if reasoning_content is not None:
            self.reasoning_content = reasoning_content
        if tool_calls is not None:
            self.tool_calls = tool_calls

    @property
    def content(self):
        r"""Gets the content of this ChatMessage.

        **参数解释**： 对话内容。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The content of this ChatMessage.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this ChatMessage.

        **参数解释**： 对话内容。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param content: The content of this ChatMessage.
        :type content: str
        """
        self._content = content

    @property
    def reasoning_content(self):
        r"""Gets the reasoning_content of this ChatMessage.

        **参数解释**： 深度搜索思维链内容。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The reasoning_content of this ChatMessage.
        :rtype: str
        """
        return self._reasoning_content

    @reasoning_content.setter
    def reasoning_content(self, reasoning_content):
        r"""Sets the reasoning_content of this ChatMessage.

        **参数解释**： 深度搜索思维链内容。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param reasoning_content: The reasoning_content of this ChatMessage.
        :type reasoning_content: str
        """
        self._reasoning_content = reasoning_content

    @property
    def tool_calls(self):
        r"""Gets the tool_calls of this ChatMessage.

        **参数解释**： 工具调用列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The tool_calls of this ChatMessage.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.ToolCall`]
        """
        return self._tool_calls

    @tool_calls.setter
    def tool_calls(self, tool_calls):
        r"""Sets the tool_calls of this ChatMessage.

        **参数解释**： 工具调用列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param tool_calls: The tool_calls of this ChatMessage.
        :type tool_calls: list[:class:`huaweicloudsdkeihealth.v1.ToolCall`]
        """
        self._tool_calls = tool_calls

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ChatMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
