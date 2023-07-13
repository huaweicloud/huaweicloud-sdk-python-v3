# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CostUnitPair:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cost_unit_name': 'str',
        'cost_unit_rule_value': 'str'
    }

    attribute_map = {
        'cost_unit_name': 'cost_unit_name',
        'cost_unit_rule_value': 'cost_unit_rule_value'
    }

    def __init__(self, cost_unit_name=None, cost_unit_rule_value=None):
        """CostUnitPair

        The model defined in huaweicloud sdk

        :param cost_unit_name: 成本单元名称。
        :type cost_unit_name: str
        :param cost_unit_rule_value: 成本单元规则值。
        :type cost_unit_rule_value: str
        """
        
        

        self._cost_unit_name = None
        self._cost_unit_rule_value = None
        self.discriminator = None

        if cost_unit_name is not None:
            self.cost_unit_name = cost_unit_name
        if cost_unit_rule_value is not None:
            self.cost_unit_rule_value = cost_unit_rule_value

    @property
    def cost_unit_name(self):
        """Gets the cost_unit_name of this CostUnitPair.

        成本单元名称。

        :return: The cost_unit_name of this CostUnitPair.
        :rtype: str
        """
        return self._cost_unit_name

    @cost_unit_name.setter
    def cost_unit_name(self, cost_unit_name):
        """Sets the cost_unit_name of this CostUnitPair.

        成本单元名称。

        :param cost_unit_name: The cost_unit_name of this CostUnitPair.
        :type cost_unit_name: str
        """
        self._cost_unit_name = cost_unit_name

    @property
    def cost_unit_rule_value(self):
        """Gets the cost_unit_rule_value of this CostUnitPair.

        成本单元规则值。

        :return: The cost_unit_rule_value of this CostUnitPair.
        :rtype: str
        """
        return self._cost_unit_rule_value

    @cost_unit_rule_value.setter
    def cost_unit_rule_value(self, cost_unit_rule_value):
        """Sets the cost_unit_rule_value of this CostUnitPair.

        成本单元规则值。

        :param cost_unit_rule_value: The cost_unit_rule_value of this CostUnitPair.
        :type cost_unit_rule_value: str
        """
        self._cost_unit_rule_value = cost_unit_rule_value

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
        if not isinstance(other, CostUnitPair):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
