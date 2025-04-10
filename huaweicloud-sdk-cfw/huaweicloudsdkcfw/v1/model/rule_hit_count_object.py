# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleHitCountObject:

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
        'rule_hit_count': 'int'
    }

    attribute_map = {
        'rule_id': 'rule_id',
        'rule_hit_count': 'rule_hit_count'
    }

    def __init__(self, rule_id=None, rule_hit_count=None):
        r"""RuleHitCountObject

        The model defined in huaweicloud sdk

        :param rule_id: 规则id
        :type rule_id: str
        :param rule_hit_count: 规则击中次数，当acl规则被触发时，对应规则id的击中次数会添加一次。
        :type rule_hit_count: int
        """
        
        

        self._rule_id = None
        self._rule_hit_count = None
        self.discriminator = None

        if rule_id is not None:
            self.rule_id = rule_id
        if rule_hit_count is not None:
            self.rule_hit_count = rule_hit_count

    @property
    def rule_id(self):
        r"""Gets the rule_id of this RuleHitCountObject.

        规则id

        :return: The rule_id of this RuleHitCountObject.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this RuleHitCountObject.

        规则id

        :param rule_id: The rule_id of this RuleHitCountObject.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def rule_hit_count(self):
        r"""Gets the rule_hit_count of this RuleHitCountObject.

        规则击中次数，当acl规则被触发时，对应规则id的击中次数会添加一次。

        :return: The rule_hit_count of this RuleHitCountObject.
        :rtype: int
        """
        return self._rule_hit_count

    @rule_hit_count.setter
    def rule_hit_count(self, rule_hit_count):
        r"""Sets the rule_hit_count of this RuleHitCountObject.

        规则击中次数，当acl规则被触发时，对应规则id的击中次数会添加一次。

        :param rule_hit_count: The rule_hit_count of this RuleHitCountObject.
        :type rule_hit_count: int
        """
        self._rule_hit_count = rule_hit_count

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
        if not isinstance(other, RuleHitCountObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
