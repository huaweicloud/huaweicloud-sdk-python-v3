# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Rule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_name': 'str',
        'rule_ratio': 'int',
        'priority': 'int'
    }

    attribute_map = {
        'table_name': 'table_name',
        'rule_ratio': 'rule_ratio',
        'priority': 'priority'
    }

    def __init__(self, table_name=None, rule_ratio=None, priority=None):
        """Rule

        The model defined in huaweicloud sdk

        :param table_name: 候选集表名。
        :type table_name: str
        :param rule_ratio: 规则占比。
        :type rule_ratio: int
        :param priority: 优先级。
        :type priority: int
        """
        
        

        self._table_name = None
        self._rule_ratio = None
        self._priority = None
        self.discriminator = None

        self.table_name = table_name
        self.rule_ratio = rule_ratio
        self.priority = priority

    @property
    def table_name(self):
        """Gets the table_name of this Rule.

        候选集表名。

        :return: The table_name of this Rule.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this Rule.

        候选集表名。

        :param table_name: The table_name of this Rule.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def rule_ratio(self):
        """Gets the rule_ratio of this Rule.

        规则占比。

        :return: The rule_ratio of this Rule.
        :rtype: int
        """
        return self._rule_ratio

    @rule_ratio.setter
    def rule_ratio(self, rule_ratio):
        """Sets the rule_ratio of this Rule.

        规则占比。

        :param rule_ratio: The rule_ratio of this Rule.
        :type rule_ratio: int
        """
        self._rule_ratio = rule_ratio

    @property
    def priority(self):
        """Gets the priority of this Rule.

        优先级。

        :return: The priority of this Rule.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this Rule.

        优先级。

        :param priority: The priority of this Rule.
        :type priority: int
        """
        self._priority = priority

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
        if not isinstance(other, Rule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
