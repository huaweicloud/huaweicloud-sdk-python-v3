# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorMessageList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content': 'ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorContent',
        'role': 'int'
    }

    attribute_map = {
        'content': 'content',
        'role': 'role'
    }

    def __init__(self, content=None, role=None):
        r"""ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorMessageList

        The model defined in huaweicloud sdk

        :param content: 
        :type content: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorContent`
        :param role: **参数解释：** 角色标识消息发送者的身份。 **取值范围：** 1 (系统), 2 (用户)。 
        :type role: int
        """
        
        

        self._content = None
        self._role = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if role is not None:
            self.role = role

    @property
    def content(self):
        r"""Gets the content of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorMessageList.

        :return: The content of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorMessageList.
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorContent`
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorMessageList.

        :param content: The content of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorMessageList.
        :type content: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorContent`
        """
        self._content = content

    @property
    def role(self):
        r"""Gets the role of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorMessageList.

        **参数解释：** 角色标识消息发送者的身份。 **取值范围：** 1 (系统), 2 (用户)。 

        :return: The role of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorMessageList.
        :rtype: int
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorMessageList.

        **参数解释：** 角色标识消息发送者的身份。 **取值范围：** 1 (系统), 2 (用户)。 

        :param role: The role of this ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorMessageList.
        :type role: int
        """
        self._role = role

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
        if not isinstance(other, ShowOpsEvaluatorTemplateResponseBodyTemplateEvaluatorContentPromptEvaluatorMessageList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
