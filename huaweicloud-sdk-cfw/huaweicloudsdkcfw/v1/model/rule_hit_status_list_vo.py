# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleHitStatusListVO:

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
        'rule_hit_count': 'int',
        'rule_last_hit_time': 'int'
    }

    attribute_map = {
        'rule_id': 'rule_id',
        'rule_hit_count': 'rule_hit_count',
        'rule_last_hit_time': 'rule_last_hit_time'
    }

    def __init__(self, rule_id=None, rule_hit_count=None, rule_last_hit_time=None):
        r"""RuleHitStatusListVO

        The model defined in huaweicloud sdk

        :param rule_id: **参数解释**： 规则ID **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type rule_id: str
        :param rule_hit_count: **参数解释**： 规则命中次数 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type rule_hit_count: int
        :param rule_last_hit_time: **参数解释**： 命中时间 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type rule_last_hit_time: int
        """
        
        

        self._rule_id = None
        self._rule_hit_count = None
        self._rule_last_hit_time = None
        self.discriminator = None

        if rule_id is not None:
            self.rule_id = rule_id
        if rule_hit_count is not None:
            self.rule_hit_count = rule_hit_count
        if rule_last_hit_time is not None:
            self.rule_last_hit_time = rule_last_hit_time

    @property
    def rule_id(self):
        r"""Gets the rule_id of this RuleHitStatusListVO.

        **参数解释**： 规则ID **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The rule_id of this RuleHitStatusListVO.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this RuleHitStatusListVO.

        **参数解释**： 规则ID **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param rule_id: The rule_id of this RuleHitStatusListVO.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def rule_hit_count(self):
        r"""Gets the rule_hit_count of this RuleHitStatusListVO.

        **参数解释**： 规则命中次数 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The rule_hit_count of this RuleHitStatusListVO.
        :rtype: int
        """
        return self._rule_hit_count

    @rule_hit_count.setter
    def rule_hit_count(self, rule_hit_count):
        r"""Sets the rule_hit_count of this RuleHitStatusListVO.

        **参数解释**： 规则命中次数 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param rule_hit_count: The rule_hit_count of this RuleHitStatusListVO.
        :type rule_hit_count: int
        """
        self._rule_hit_count = rule_hit_count

    @property
    def rule_last_hit_time(self):
        r"""Gets the rule_last_hit_time of this RuleHitStatusListVO.

        **参数解释**： 命中时间 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The rule_last_hit_time of this RuleHitStatusListVO.
        :rtype: int
        """
        return self._rule_last_hit_time

    @rule_last_hit_time.setter
    def rule_last_hit_time(self, rule_last_hit_time):
        r"""Sets the rule_last_hit_time of this RuleHitStatusListVO.

        **参数解释**： 命中时间 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param rule_last_hit_time: The rule_last_hit_time of this RuleHitStatusListVO.
        :type rule_last_hit_time: int
        """
        self._rule_last_hit_time = rule_last_hit_time

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
        if not isinstance(other, RuleHitStatusListVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
