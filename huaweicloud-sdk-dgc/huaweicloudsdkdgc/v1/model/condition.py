# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Condition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pre_node_name': 'str',
        'expression': 'str'
    }

    attribute_map = {
        'pre_node_name': 'preNodeName',
        'expression': 'expression'
    }

    def __init__(self, pre_node_name=None, expression=None):
        r"""Condition

        The model defined in huaweicloud sdk

        :param pre_node_name: 本节点依赖的前一个节点名称
        :type pre_node_name: str
        :param expression: EL表达式，如果EL表达式的计算结果为true，则触发执行本节点
        :type expression: str
        """
        
        

        self._pre_node_name = None
        self._expression = None
        self.discriminator = None

        self.pre_node_name = pre_node_name
        self.expression = expression

    @property
    def pre_node_name(self):
        r"""Gets the pre_node_name of this Condition.

        本节点依赖的前一个节点名称

        :return: The pre_node_name of this Condition.
        :rtype: str
        """
        return self._pre_node_name

    @pre_node_name.setter
    def pre_node_name(self, pre_node_name):
        r"""Sets the pre_node_name of this Condition.

        本节点依赖的前一个节点名称

        :param pre_node_name: The pre_node_name of this Condition.
        :type pre_node_name: str
        """
        self._pre_node_name = pre_node_name

    @property
    def expression(self):
        r"""Gets the expression of this Condition.

        EL表达式，如果EL表达式的计算结果为true，则触发执行本节点

        :return: The expression of this Condition.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        r"""Sets the expression of this Condition.

        EL表达式，如果EL表达式的计算结果为true，则触发执行本节点

        :param expression: The expression of this Condition.
        :type expression: str
        """
        self._expression = expression

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
        if not isinstance(other, Condition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
