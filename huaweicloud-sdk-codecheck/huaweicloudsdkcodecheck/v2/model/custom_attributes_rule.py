# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomAttributesRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_id': 'str',
        'value': 'str',
        'rule_config_list': 'list[RuleConfig]'
    }

    attribute_map = {
        'rule_id': 'rule_id',
        'value': 'value',
        'rule_config_list': 'rule_config_list'
    }

    def __init__(self, rule_id=None, value=None, rule_config_list=None):
        """CustomAttributesRule

        The model defined in huaweicloud sdk

        :param rule_id: 规则ID
        :type rule_id: str
        :param value: attribute的问题级别，0致命，1严重，2一般，3提示
        :type value: str
        :param rule_config_list: 规则阈值详细
        :type rule_config_list: list[:class:`huaweicloudsdkcodecheck.v2.RuleConfig`]
        """
        
        

        self._rule_id = None
        self._value = None
        self._rule_config_list = None
        self.discriminator = None

        if rule_id is not None:
            self.rule_id = rule_id
        if value is not None:
            self.value = value
        if rule_config_list is not None:
            self.rule_config_list = rule_config_list

    @property
    def rule_id(self):
        """Gets the rule_id of this CustomAttributesRule.

        规则ID

        :return: The rule_id of this CustomAttributesRule.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this CustomAttributesRule.

        规则ID

        :param rule_id: The rule_id of this CustomAttributesRule.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def value(self):
        """Gets the value of this CustomAttributesRule.

        attribute的问题级别，0致命，1严重，2一般，3提示

        :return: The value of this CustomAttributesRule.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CustomAttributesRule.

        attribute的问题级别，0致命，1严重，2一般，3提示

        :param value: The value of this CustomAttributesRule.
        :type value: str
        """
        self._value = value

    @property
    def rule_config_list(self):
        """Gets the rule_config_list of this CustomAttributesRule.

        规则阈值详细

        :return: The rule_config_list of this CustomAttributesRule.
        :rtype: list[:class:`huaweicloudsdkcodecheck.v2.RuleConfig`]
        """
        return self._rule_config_list

    @rule_config_list.setter
    def rule_config_list(self, rule_config_list):
        """Sets the rule_config_list of this CustomAttributesRule.

        规则阈值详细

        :param rule_config_list: The rule_config_list of this CustomAttributesRule.
        :type rule_config_list: list[:class:`huaweicloudsdkcodecheck.v2.RuleConfig`]
        """
        self._rule_config_list = rule_config_list

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
        if not isinstance(other, CustomAttributesRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
