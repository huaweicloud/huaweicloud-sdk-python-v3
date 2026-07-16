# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsEvaluatorTemplatesResponseBodyEvaluatorContentPromptEvaluatorMessageList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role': 'int',
        'content': 'ListOpsEvaluatorTemplatesResponseBodyEvaluatorContentPromptEvaluatorContent'
    }

    attribute_map = {
        'role': 'role',
        'content': 'content'
    }

    def __init__(self, role=None, content=None):
        r"""ListOpsEvaluatorTemplatesResponseBodyEvaluatorContentPromptEvaluatorMessageList

        The model defined in huaweicloud sdk

        :param role: **参数解释：** 消息角色。 **取值范围：** 1: System, 2: User 等。 
        :type role: int
        :param content: 
        :type content: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorTemplatesResponseBodyEvaluatorContentPromptEvaluatorContent`
        """
        
        

        self._role = None
        self._content = None
        self.discriminator = None

        if role is not None:
            self.role = role
        if content is not None:
            self.content = content

    @property
    def role(self):
        r"""Gets the role of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorContentPromptEvaluatorMessageList.

        **参数解释：** 消息角色。 **取值范围：** 1: System, 2: User 等。 

        :return: The role of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorContentPromptEvaluatorMessageList.
        :rtype: int
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorContentPromptEvaluatorMessageList.

        **参数解释：** 消息角色。 **取值范围：** 1: System, 2: User 等。 

        :param role: The role of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorContentPromptEvaluatorMessageList.
        :type role: int
        """
        self._role = role

    @property
    def content(self):
        r"""Gets the content of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorContentPromptEvaluatorMessageList.

        :return: The content of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorContentPromptEvaluatorMessageList.
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorTemplatesResponseBodyEvaluatorContentPromptEvaluatorContent`
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorContentPromptEvaluatorMessageList.

        :param content: The content of this ListOpsEvaluatorTemplatesResponseBodyEvaluatorContentPromptEvaluatorMessageList.
        :type content: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorTemplatesResponseBodyEvaluatorContentPromptEvaluatorContent`
        """
        self._content = content

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
        if not isinstance(other, ListOpsEvaluatorTemplatesResponseBodyEvaluatorContentPromptEvaluatorMessageList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
