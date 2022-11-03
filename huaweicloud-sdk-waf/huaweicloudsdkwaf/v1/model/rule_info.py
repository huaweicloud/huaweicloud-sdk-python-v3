# coding: utf-8

import re
import six



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
        'rule_name': 'str',
        'policy_id': 'str',
        'policy_name': 'str'
    }

    attribute_map = {
        'rule_id': 'rule_id',
        'rule_name': 'rule_name',
        'policy_id': 'policy_id',
        'policy_name': 'policy_name'
    }

    def __init__(self, rule_id=None, rule_name=None, policy_id=None, policy_name=None):
        """RuleInfo

        The model defined in huaweicloud sdk

        :param rule_id: 规则id
        :type rule_id: str
        :param rule_name: 规则名称
        :type rule_name: str
        :param policy_id: 策略id
        :type policy_id: str
        :param policy_name: 策略名称
        :type policy_name: str
        """
        
        

        self._rule_id = None
        self._rule_name = None
        self._policy_id = None
        self._policy_name = None
        self.discriminator = None

        if rule_id is not None:
            self.rule_id = rule_id
        if rule_name is not None:
            self.rule_name = rule_name
        if policy_id is not None:
            self.policy_id = policy_id
        if policy_name is not None:
            self.policy_name = policy_name

    @property
    def rule_id(self):
        """Gets the rule_id of this RuleInfo.

        规则id

        :return: The rule_id of this RuleInfo.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this RuleInfo.

        规则id

        :param rule_id: The rule_id of this RuleInfo.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def rule_name(self):
        """Gets the rule_name of this RuleInfo.

        规则名称

        :return: The rule_name of this RuleInfo.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this RuleInfo.

        规则名称

        :param rule_name: The rule_name of this RuleInfo.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def policy_id(self):
        """Gets the policy_id of this RuleInfo.

        策略id

        :return: The policy_id of this RuleInfo.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this RuleInfo.

        策略id

        :param policy_id: The policy_id of this RuleInfo.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def policy_name(self):
        """Gets the policy_name of this RuleInfo.

        策略名称

        :return: The policy_name of this RuleInfo.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this RuleInfo.

        策略名称

        :param policy_name: The policy_name of this RuleInfo.
        :type policy_name: str
        """
        self._policy_name = policy_name

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
        if not isinstance(other, RuleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
