# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentAffinity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kind': 'str',
        'condition': 'str',
        'weight': 'int',
        'match_expressions': 'list[ComponentAffinityMatchExpressions]'
    }

    attribute_map = {
        'kind': 'kind',
        'condition': 'condition',
        'weight': 'weight',
        'match_expressions': 'match_expressions'
    }

    def __init__(self, kind=None, condition=None, weight=None, match_expressions=None):
        """ComponentAffinity

        The model defined in huaweicloud sdk

        :param kind: 指定亲和和反亲和的类型
        :type kind: str
        :param condition: 
        :type condition: str
        :param weight: 
        :type weight: int
        :param match_expressions: 匹配的条件列表
        :type match_expressions: list[:class:`huaweicloudsdkservicestage.v3.ComponentAffinityMatchExpressions`]
        """
        
        

        self._kind = None
        self._condition = None
        self._weight = None
        self._match_expressions = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if condition is not None:
            self.condition = condition
        if weight is not None:
            self.weight = weight
        if match_expressions is not None:
            self.match_expressions = match_expressions

    @property
    def kind(self):
        """Gets the kind of this ComponentAffinity.

        指定亲和和反亲和的类型

        :return: The kind of this ComponentAffinity.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this ComponentAffinity.

        指定亲和和反亲和的类型

        :param kind: The kind of this ComponentAffinity.
        :type kind: str
        """
        self._kind = kind

    @property
    def condition(self):
        """Gets the condition of this ComponentAffinity.

        :return: The condition of this ComponentAffinity.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this ComponentAffinity.

        :param condition: The condition of this ComponentAffinity.
        :type condition: str
        """
        self._condition = condition

    @property
    def weight(self):
        """Gets the weight of this ComponentAffinity.

        :return: The weight of this ComponentAffinity.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this ComponentAffinity.

        :param weight: The weight of this ComponentAffinity.
        :type weight: int
        """
        self._weight = weight

    @property
    def match_expressions(self):
        """Gets the match_expressions of this ComponentAffinity.

        匹配的条件列表

        :return: The match_expressions of this ComponentAffinity.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.ComponentAffinityMatchExpressions`]
        """
        return self._match_expressions

    @match_expressions.setter
    def match_expressions(self, match_expressions):
        """Sets the match_expressions of this ComponentAffinity.

        匹配的条件列表

        :param match_expressions: The match_expressions of this ComponentAffinity.
        :type match_expressions: list[:class:`huaweicloudsdkservicestage.v3.ComponentAffinityMatchExpressions`]
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
        if not isinstance(other, ComponentAffinity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
