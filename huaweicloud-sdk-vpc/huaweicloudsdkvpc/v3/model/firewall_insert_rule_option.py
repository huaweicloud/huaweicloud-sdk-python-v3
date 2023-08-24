# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FirewallInsertRuleOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ingress_rules': 'list[FirewallInsertRuleItemOption]',
        'egress_rules': 'list[FirewallInsertRuleItemOption]',
        'insert_after_rule': 'str'
    }

    attribute_map = {
        'ingress_rules': 'ingress_rules',
        'egress_rules': 'egress_rules',
        'insert_after_rule': 'insert_after_rule'
    }

    def __init__(self, ingress_rules=None, egress_rules=None, insert_after_rule=None):
        """FirewallInsertRuleOption

        The model defined in huaweicloud sdk

        :param ingress_rules: 功能说明：ACL添加入方向规则列表
        :type ingress_rules: list[:class:`huaweicloudsdkvpc.v3.FirewallInsertRuleItemOption`]
        :param egress_rules: 功能说明：ACL添加出方向规则列表
        :type egress_rules: list[:class:`huaweicloudsdkvpc.v3.FirewallInsertRuleItemOption`]
        :param insert_after_rule: 功能说明：插入ACL的规则在入方向或者出方向某条规则位置后，不指定则在入方向或者出方向规则列表最前面插入规则 约束：指定了insert_after_rule，ingress_rules和egress_rules只能同时设置一个，且该规则在入方向或者出方向规则中存在
        :type insert_after_rule: str
        """
        
        

        self._ingress_rules = None
        self._egress_rules = None
        self._insert_after_rule = None
        self.discriminator = None

        if ingress_rules is not None:
            self.ingress_rules = ingress_rules
        if egress_rules is not None:
            self.egress_rules = egress_rules
        if insert_after_rule is not None:
            self.insert_after_rule = insert_after_rule

    @property
    def ingress_rules(self):
        """Gets the ingress_rules of this FirewallInsertRuleOption.

        功能说明：ACL添加入方向规则列表

        :return: The ingress_rules of this FirewallInsertRuleOption.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.FirewallInsertRuleItemOption`]
        """
        return self._ingress_rules

    @ingress_rules.setter
    def ingress_rules(self, ingress_rules):
        """Sets the ingress_rules of this FirewallInsertRuleOption.

        功能说明：ACL添加入方向规则列表

        :param ingress_rules: The ingress_rules of this FirewallInsertRuleOption.
        :type ingress_rules: list[:class:`huaweicloudsdkvpc.v3.FirewallInsertRuleItemOption`]
        """
        self._ingress_rules = ingress_rules

    @property
    def egress_rules(self):
        """Gets the egress_rules of this FirewallInsertRuleOption.

        功能说明：ACL添加出方向规则列表

        :return: The egress_rules of this FirewallInsertRuleOption.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.FirewallInsertRuleItemOption`]
        """
        return self._egress_rules

    @egress_rules.setter
    def egress_rules(self, egress_rules):
        """Sets the egress_rules of this FirewallInsertRuleOption.

        功能说明：ACL添加出方向规则列表

        :param egress_rules: The egress_rules of this FirewallInsertRuleOption.
        :type egress_rules: list[:class:`huaweicloudsdkvpc.v3.FirewallInsertRuleItemOption`]
        """
        self._egress_rules = egress_rules

    @property
    def insert_after_rule(self):
        """Gets the insert_after_rule of this FirewallInsertRuleOption.

        功能说明：插入ACL的规则在入方向或者出方向某条规则位置后，不指定则在入方向或者出方向规则列表最前面插入规则 约束：指定了insert_after_rule，ingress_rules和egress_rules只能同时设置一个，且该规则在入方向或者出方向规则中存在

        :return: The insert_after_rule of this FirewallInsertRuleOption.
        :rtype: str
        """
        return self._insert_after_rule

    @insert_after_rule.setter
    def insert_after_rule(self, insert_after_rule):
        """Sets the insert_after_rule of this FirewallInsertRuleOption.

        功能说明：插入ACL的规则在入方向或者出方向某条规则位置后，不指定则在入方向或者出方向规则列表最前面插入规则 约束：指定了insert_after_rule，ingress_rules和egress_rules只能同时设置一个，且该规则在入方向或者出方向规则中存在

        :param insert_after_rule: The insert_after_rule of this FirewallInsertRuleOption.
        :type insert_after_rule: str
        """
        self._insert_after_rule = insert_after_rule

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
        if not isinstance(other, FirewallInsertRuleOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
