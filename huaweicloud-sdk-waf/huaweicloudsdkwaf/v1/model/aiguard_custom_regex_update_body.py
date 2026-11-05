# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AiguardCustomRegexUpdateBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'regex_expression': 'str'
    }

    attribute_map = {
        'name': 'name',
        'regex_expression': 'regex_expression'
    }

    def __init__(self, name=None, regex_expression=None):
        r"""AiguardCustomRegexUpdateBody

        The model defined in huaweicloud sdk

        :param name: 正则名称
        :type name: str
        :param regex_expression: 正则表达式
        :type regex_expression: str
        """
        
        

        self._name = None
        self._regex_expression = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if regex_expression is not None:
            self.regex_expression = regex_expression

    @property
    def name(self):
        r"""Gets the name of this AiguardCustomRegexUpdateBody.

        正则名称

        :return: The name of this AiguardCustomRegexUpdateBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AiguardCustomRegexUpdateBody.

        正则名称

        :param name: The name of this AiguardCustomRegexUpdateBody.
        :type name: str
        """
        self._name = name

    @property
    def regex_expression(self):
        r"""Gets the regex_expression of this AiguardCustomRegexUpdateBody.

        正则表达式

        :return: The regex_expression of this AiguardCustomRegexUpdateBody.
        :rtype: str
        """
        return self._regex_expression

    @regex_expression.setter
    def regex_expression(self, regex_expression):
        r"""Sets the regex_expression of this AiguardCustomRegexUpdateBody.

        正则表达式

        :param regex_expression: The regex_expression of this AiguardCustomRegexUpdateBody.
        :type regex_expression: str
        """
        self._regex_expression = regex_expression

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
        if not isinstance(other, AiguardCustomRegexUpdateBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
