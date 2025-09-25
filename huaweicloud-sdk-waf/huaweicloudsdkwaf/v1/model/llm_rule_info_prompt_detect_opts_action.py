# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LlmRuleInfoPromptDetectOptsAction:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'response': 'LlmRuleInfoPromptDetectOptsActionResponse'
    }

    attribute_map = {
        'category': 'category',
        'response': 'response'
    }

    def __init__(self, category=None, response=None):
        r"""LlmRuleInfoPromptDetectOptsAction

        The model defined in huaweicloud sdk

        :param category: 防护动作
        :type category: str
        :param response: 
        :type response: :class:`huaweicloudsdkwaf.v1.LlmRuleInfoPromptDetectOptsActionResponse`
        """
        
        

        self._category = None
        self._response = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if response is not None:
            self.response = response

    @property
    def category(self):
        r"""Gets the category of this LlmRuleInfoPromptDetectOptsAction.

        防护动作

        :return: The category of this LlmRuleInfoPromptDetectOptsAction.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this LlmRuleInfoPromptDetectOptsAction.

        防护动作

        :param category: The category of this LlmRuleInfoPromptDetectOptsAction.
        :type category: str
        """
        self._category = category

    @property
    def response(self):
        r"""Gets the response of this LlmRuleInfoPromptDetectOptsAction.

        :return: The response of this LlmRuleInfoPromptDetectOptsAction.
        :rtype: :class:`huaweicloudsdkwaf.v1.LlmRuleInfoPromptDetectOptsActionResponse`
        """
        return self._response

    @response.setter
    def response(self, response):
        r"""Sets the response of this LlmRuleInfoPromptDetectOptsAction.

        :param response: The response of this LlmRuleInfoPromptDetectOptsAction.
        :type response: :class:`huaweicloudsdkwaf.v1.LlmRuleInfoPromptDetectOptsActionResponse`
        """
        self._response = response

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
        if not isinstance(other, LlmRuleInfoPromptDetectOptsAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
