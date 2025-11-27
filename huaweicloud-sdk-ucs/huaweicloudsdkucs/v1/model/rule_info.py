# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleInfo:

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
        'rule_name': 'str'
    }

    attribute_map = {
        'rule_id': 'ruleID',
        'rule_name': 'ruleName'
    }

    def __init__(self, rule_id=None, rule_name=None):
        r"""RuleInfo

        The model defined in huaweicloud sdk

        :param rule_id: 权限策略id
        :type rule_id: str
        :param rule_name: 权限策略名字
        :type rule_name: str
        """
        
        

        self._rule_id = None
        self._rule_name = None
        self.discriminator = None

        if rule_id is not None:
            self.rule_id = rule_id
        if rule_name is not None:
            self.rule_name = rule_name

    @property
    def rule_id(self):
        r"""Gets the rule_id of this RuleInfo.

        权限策略id

        :return: The rule_id of this RuleInfo.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this RuleInfo.

        权限策略id

        :param rule_id: The rule_id of this RuleInfo.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def rule_name(self):
        r"""Gets the rule_name of this RuleInfo.

        权限策略名字

        :return: The rule_name of this RuleInfo.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this RuleInfo.

        权限策略名字

        :param rule_name: The rule_name of this RuleInfo.
        :type rule_name: str
        """
        self._rule_name = rule_name

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RuleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
