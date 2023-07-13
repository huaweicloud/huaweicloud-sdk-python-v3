# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyRuleInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_type': 'str',
        'rule': 'str'
    }

    attribute_map = {
        'rule_type': 'rule_type',
        'rule': 'rule'
    }

    def __init__(self, rule_type=None, rule=None):
        """ApplyRuleInfo

        The model defined in huaweicloud sdk

        :param rule_type: 认证应用对象类型。 - ACCESS_MODE：接入类型
        :type rule_type: str
        :param rule: 认证应用对象。 - INTERNET：互联网接入，rule_type为ACCESS_MODE时可选该值 - PRIVATE：专线接入，rule_type为ACCESS_MODE时可选该值
        :type rule: str
        """
        
        

        self._rule_type = None
        self._rule = None
        self.discriminator = None

        if rule_type is not None:
            self.rule_type = rule_type
        if rule is not None:
            self.rule = rule

    @property
    def rule_type(self):
        """Gets the rule_type of this ApplyRuleInfo.

        认证应用对象类型。 - ACCESS_MODE：接入类型

        :return: The rule_type of this ApplyRuleInfo.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """Sets the rule_type of this ApplyRuleInfo.

        认证应用对象类型。 - ACCESS_MODE：接入类型

        :param rule_type: The rule_type of this ApplyRuleInfo.
        :type rule_type: str
        """
        self._rule_type = rule_type

    @property
    def rule(self):
        """Gets the rule of this ApplyRuleInfo.

        认证应用对象。 - INTERNET：互联网接入，rule_type为ACCESS_MODE时可选该值 - PRIVATE：专线接入，rule_type为ACCESS_MODE时可选该值

        :return: The rule of this ApplyRuleInfo.
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this ApplyRuleInfo.

        认证应用对象。 - INTERNET：互联网接入，rule_type为ACCESS_MODE时可选该值 - PRIVATE：专线接入，rule_type为ACCESS_MODE时可选该值

        :param rule: The rule of this ApplyRuleInfo.
        :type rule: str
        """
        self._rule = rule

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
        if not isinstance(other, ApplyRuleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
