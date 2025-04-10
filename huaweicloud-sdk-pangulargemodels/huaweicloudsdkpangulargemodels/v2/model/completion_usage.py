# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompletionUsage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'completion_tokens': 'float',
        'prompt_tokens': 'float',
        'total_tokens': 'float'
    }

    attribute_map = {
        'completion_tokens': 'completion_tokens',
        'prompt_tokens': 'prompt_tokens',
        'total_tokens': 'total_tokens'
    }

    def __init__(self, completion_tokens=None, prompt_tokens=None, total_tokens=None):
        r"""CompletionUsage

        The model defined in huaweicloud sdk

        :param completion_tokens: 表示模型生成的答案中包含的tokens的数量。
        :type completion_tokens: float
        :param prompt_tokens: 表示生成结果时使用的提示文本的tokens的数量。
        :type prompt_tokens: float
        :param total_tokens: 对话过程中使用的tokens总数。
        :type total_tokens: float
        """
        
        

        self._completion_tokens = None
        self._prompt_tokens = None
        self._total_tokens = None
        self.discriminator = None

        self.completion_tokens = completion_tokens
        self.prompt_tokens = prompt_tokens
        self.total_tokens = total_tokens

    @property
    def completion_tokens(self):
        r"""Gets the completion_tokens of this CompletionUsage.

        表示模型生成的答案中包含的tokens的数量。

        :return: The completion_tokens of this CompletionUsage.
        :rtype: float
        """
        return self._completion_tokens

    @completion_tokens.setter
    def completion_tokens(self, completion_tokens):
        r"""Sets the completion_tokens of this CompletionUsage.

        表示模型生成的答案中包含的tokens的数量。

        :param completion_tokens: The completion_tokens of this CompletionUsage.
        :type completion_tokens: float
        """
        self._completion_tokens = completion_tokens

    @property
    def prompt_tokens(self):
        r"""Gets the prompt_tokens of this CompletionUsage.

        表示生成结果时使用的提示文本的tokens的数量。

        :return: The prompt_tokens of this CompletionUsage.
        :rtype: float
        """
        return self._prompt_tokens

    @prompt_tokens.setter
    def prompt_tokens(self, prompt_tokens):
        r"""Sets the prompt_tokens of this CompletionUsage.

        表示生成结果时使用的提示文本的tokens的数量。

        :param prompt_tokens: The prompt_tokens of this CompletionUsage.
        :type prompt_tokens: float
        """
        self._prompt_tokens = prompt_tokens

    @property
    def total_tokens(self):
        r"""Gets the total_tokens of this CompletionUsage.

        对话过程中使用的tokens总数。

        :return: The total_tokens of this CompletionUsage.
        :rtype: float
        """
        return self._total_tokens

    @total_tokens.setter
    def total_tokens(self, total_tokens):
        r"""Sets the total_tokens of this CompletionUsage.

        对话过程中使用的tokens总数。

        :param total_tokens: The total_tokens of this CompletionUsage.
        :type total_tokens: float
        """
        self._total_tokens = total_tokens

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
        if not isinstance(other, CompletionUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
