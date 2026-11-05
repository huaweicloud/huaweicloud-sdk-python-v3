# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegexTestRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pattern': 'str',
        'text': 'str'
    }

    attribute_map = {
        'pattern': 'pattern',
        'text': 'text'
    }

    def __init__(self, pattern=None, text=None):
        r"""RegexTestRequest

        The model defined in huaweicloud sdk

        :param pattern: 待测试的正则表达式
        :type pattern: str
        :param text: 待匹配的文本内容
        :type text: str
        """
        
        

        self._pattern = None
        self._text = None
        self.discriminator = None

        self.pattern = pattern
        if text is not None:
            self.text = text

    @property
    def pattern(self):
        r"""Gets the pattern of this RegexTestRequest.

        待测试的正则表达式

        :return: The pattern of this RegexTestRequest.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        r"""Sets the pattern of this RegexTestRequest.

        待测试的正则表达式

        :param pattern: The pattern of this RegexTestRequest.
        :type pattern: str
        """
        self._pattern = pattern

    @property
    def text(self):
        r"""Gets the text of this RegexTestRequest.

        待匹配的文本内容

        :return: The text of this RegexTestRequest.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        r"""Sets the text of this RegexTestRequest.

        待匹配的文本内容

        :param text: The text of this RegexTestRequest.
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
        if not isinstance(other, RegexTestRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
