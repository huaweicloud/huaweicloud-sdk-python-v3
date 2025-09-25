# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LlmRuleInfoPromptDetectOpts:

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
        'inject_enable': 'bool',
        'compliance_enable': 'bool',
        'action': 'LlmRuleInfoPromptDetectOptsAction'
    }

    attribute_map = {
        'content': 'content',
        'inject_enable': 'inject_enable',
        'compliance_enable': 'compliance_enable',
        'action': 'action'
    }

    def __init__(self, content=None, inject_enable=None, compliance_enable=None, action=None):
        r"""LlmRuleInfoPromptDetectOpts

        The model defined in huaweicloud sdk

        :param content: 提示词索引
        :type content: str
        :param inject_enable: 提示词注入检测
        :type inject_enable: bool
        :param compliance_enable: 提示词合规检测
        :type compliance_enable: bool
        :param action: 
        :type action: :class:`huaweicloudsdkwaf.v1.LlmRuleInfoPromptDetectOptsAction`
        """
        
        

        self._content = None
        self._inject_enable = None
        self._compliance_enable = None
        self._action = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if inject_enable is not None:
            self.inject_enable = inject_enable
        if compliance_enable is not None:
            self.compliance_enable = compliance_enable
        if action is not None:
            self.action = action

    @property
    def content(self):
        r"""Gets the content of this LlmRuleInfoPromptDetectOpts.

        提示词索引

        :return: The content of this LlmRuleInfoPromptDetectOpts.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this LlmRuleInfoPromptDetectOpts.

        提示词索引

        :param content: The content of this LlmRuleInfoPromptDetectOpts.
        :type content: str
        """
        self._content = content

    @property
    def inject_enable(self):
        r"""Gets the inject_enable of this LlmRuleInfoPromptDetectOpts.

        提示词注入检测

        :return: The inject_enable of this LlmRuleInfoPromptDetectOpts.
        :rtype: bool
        """
        return self._inject_enable

    @inject_enable.setter
    def inject_enable(self, inject_enable):
        r"""Sets the inject_enable of this LlmRuleInfoPromptDetectOpts.

        提示词注入检测

        :param inject_enable: The inject_enable of this LlmRuleInfoPromptDetectOpts.
        :type inject_enable: bool
        """
        self._inject_enable = inject_enable

    @property
    def compliance_enable(self):
        r"""Gets the compliance_enable of this LlmRuleInfoPromptDetectOpts.

        提示词合规检测

        :return: The compliance_enable of this LlmRuleInfoPromptDetectOpts.
        :rtype: bool
        """
        return self._compliance_enable

    @compliance_enable.setter
    def compliance_enable(self, compliance_enable):
        r"""Sets the compliance_enable of this LlmRuleInfoPromptDetectOpts.

        提示词合规检测

        :param compliance_enable: The compliance_enable of this LlmRuleInfoPromptDetectOpts.
        :type compliance_enable: bool
        """
        self._compliance_enable = compliance_enable

    @property
    def action(self):
        r"""Gets the action of this LlmRuleInfoPromptDetectOpts.

        :return: The action of this LlmRuleInfoPromptDetectOpts.
        :rtype: :class:`huaweicloudsdkwaf.v1.LlmRuleInfoPromptDetectOptsAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this LlmRuleInfoPromptDetectOpts.

        :param action: The action of this LlmRuleInfoPromptDetectOpts.
        :type action: :class:`huaweicloudsdkwaf.v1.LlmRuleInfoPromptDetectOptsAction`
        """
        self._action = action

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
        if not isinstance(other, LlmRuleInfoPromptDetectOpts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
