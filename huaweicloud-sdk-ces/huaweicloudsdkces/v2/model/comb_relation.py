# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CombRelation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'logical_operator': 'str',
        'conditions': 'list[Condition]'
    }

    attribute_map = {
        'logical_operator': 'logical_operator',
        'conditions': 'conditions'
    }

    def __init__(self, logical_operator=None, conditions=None):
        r"""CombRelation

        The model defined in huaweicloud sdk

        :param logical_operator: 逻辑运算符  ALL 所有条件匹配成功  ANY 任意条件匹配成功 
        :type logical_operator: str
        :param conditions: 组合匹配资源分组的匹配条件
        :type conditions: list[:class:`huaweicloudsdkces.v2.Condition`]
        """
        
        

        self._logical_operator = None
        self._conditions = None
        self.discriminator = None

        self.logical_operator = logical_operator
        self.conditions = conditions

    @property
    def logical_operator(self):
        r"""Gets the logical_operator of this CombRelation.

        逻辑运算符  ALL 所有条件匹配成功  ANY 任意条件匹配成功 

        :return: The logical_operator of this CombRelation.
        :rtype: str
        """
        return self._logical_operator

    @logical_operator.setter
    def logical_operator(self, logical_operator):
        r"""Sets the logical_operator of this CombRelation.

        逻辑运算符  ALL 所有条件匹配成功  ANY 任意条件匹配成功 

        :param logical_operator: The logical_operator of this CombRelation.
        :type logical_operator: str
        """
        self._logical_operator = logical_operator

    @property
    def conditions(self):
        r"""Gets the conditions of this CombRelation.

        组合匹配资源分组的匹配条件

        :return: The conditions of this CombRelation.
        :rtype: list[:class:`huaweicloudsdkces.v2.Condition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this CombRelation.

        组合匹配资源分组的匹配条件

        :param conditions: The conditions of this CombRelation.
        :type conditions: list[:class:`huaweicloudsdkces.v2.Condition`]
        """
        self._conditions = conditions

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
        if not isinstance(other, CombRelation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
