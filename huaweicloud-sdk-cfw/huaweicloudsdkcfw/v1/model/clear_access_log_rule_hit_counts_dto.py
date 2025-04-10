# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClearAccessLogRuleHitCountsDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_ids': 'list[str]'
    }

    attribute_map = {
        'rule_ids': 'rule_ids'
    }

    def __init__(self, rule_ids=None):
        r"""ClearAccessLogRuleHitCountsDto

        The model defined in huaweicloud sdk

        :param rule_ids: 删除规则击中次数请求的规则列表，规则id可通过[查询防护规则接口](ListAclRules.xml)查询获得，通过返回值中的data.records.rule_id（.表示各对象之间层级的区分）获得。
        :type rule_ids: list[str]
        """
        
        

        self._rule_ids = None
        self.discriminator = None

        self.rule_ids = rule_ids

    @property
    def rule_ids(self):
        r"""Gets the rule_ids of this ClearAccessLogRuleHitCountsDto.

        删除规则击中次数请求的规则列表，规则id可通过[查询防护规则接口](ListAclRules.xml)查询获得，通过返回值中的data.records.rule_id（.表示各对象之间层级的区分）获得。

        :return: The rule_ids of this ClearAccessLogRuleHitCountsDto.
        :rtype: list[str]
        """
        return self._rule_ids

    @rule_ids.setter
    def rule_ids(self, rule_ids):
        r"""Sets the rule_ids of this ClearAccessLogRuleHitCountsDto.

        删除规则击中次数请求的规则列表，规则id可通过[查询防护规则接口](ListAclRules.xml)查询获得，通过返回值中的data.records.rule_id（.表示各对象之间层级的区分）获得。

        :param rule_ids: The rule_ids of this ClearAccessLogRuleHitCountsDto.
        :type rule_ids: list[str]
        """
        self._rule_ids = rule_ids

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
        if not isinstance(other, ClearAccessLogRuleHitCountsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
