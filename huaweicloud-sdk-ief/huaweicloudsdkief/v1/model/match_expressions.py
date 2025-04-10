# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MatchExpressions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'match_expressions': 'list[MatchExpression]'
    }

    attribute_map = {
        'match_expressions': 'matchExpressions'
    }

    def __init__(self, match_expressions=None):
        r"""MatchExpressions

        The model defined in huaweicloud sdk

        :param match_expressions: 匹配规则表达式
        :type match_expressions: list[:class:`huaweicloudsdkief.v1.MatchExpression`]
        """
        
        

        self._match_expressions = None
        self.discriminator = None

        if match_expressions is not None:
            self.match_expressions = match_expressions

    @property
    def match_expressions(self):
        r"""Gets the match_expressions of this MatchExpressions.

        匹配规则表达式

        :return: The match_expressions of this MatchExpressions.
        :rtype: list[:class:`huaweicloudsdkief.v1.MatchExpression`]
        """
        return self._match_expressions

    @match_expressions.setter
    def match_expressions(self, match_expressions):
        r"""Sets the match_expressions of this MatchExpressions.

        匹配规则表达式

        :param match_expressions: The match_expressions of this MatchExpressions.
        :type match_expressions: list[:class:`huaweicloudsdkief.v1.MatchExpression`]
        """
        self._match_expressions = match_expressions

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
        if not isinstance(other, MatchExpressions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
