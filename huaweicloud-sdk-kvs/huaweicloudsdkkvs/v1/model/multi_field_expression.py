# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MultiFieldExpression:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'logic': 'str',
        'expressions': 'list[SingleFieldExpression]'
    }

    attribute_map = {
        'logic': 'logic',
        'expressions': 'expressions'
    }

    def __init__(self, logic=None, expressions=None):
        r"""MultiFieldExpression

        The model defined in huaweicloud sdk

        :param logic: 多字段条件，多个相同优先级的单字段条件。
        :type logic: str
        :param expressions: 多个相同逻辑操作的单字段条件。
        :type expressions: list[:class:`huaweicloudsdkkvs.v1.SingleFieldExpression`]
        """
        
        

        self._logic = None
        self._expressions = None
        self.discriminator = None

        if logic is not None:
            self.logic = logic
        self.expressions = expressions

    @property
    def logic(self):
        r"""Gets the logic of this MultiFieldExpression.

        多字段条件，多个相同优先级的单字段条件。

        :return: The logic of this MultiFieldExpression.
        :rtype: str
        """
        return self._logic

    @logic.setter
    def logic(self, logic):
        r"""Sets the logic of this MultiFieldExpression.

        多字段条件，多个相同优先级的单字段条件。

        :param logic: The logic of this MultiFieldExpression.
        :type logic: str
        """
        self._logic = logic

    @property
    def expressions(self):
        r"""Gets the expressions of this MultiFieldExpression.

        多个相同逻辑操作的单字段条件。

        :return: The expressions of this MultiFieldExpression.
        :rtype: list[:class:`huaweicloudsdkkvs.v1.SingleFieldExpression`]
        """
        return self._expressions

    @expressions.setter
    def expressions(self, expressions):
        r"""Sets the expressions of this MultiFieldExpression.

        多个相同逻辑操作的单字段条件。

        :param expressions: The expressions of this MultiFieldExpression.
        :type expressions: list[:class:`huaweicloudsdkkvs.v1.SingleFieldExpression`]
        """
        self._expressions = expressions

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
        if not isinstance(other, MultiFieldExpression):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
