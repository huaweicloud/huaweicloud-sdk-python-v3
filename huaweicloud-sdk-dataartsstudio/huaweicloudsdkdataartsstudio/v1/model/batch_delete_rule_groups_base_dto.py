# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteRuleGroupsBaseDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_group_ids': 'list[str]'
    }

    attribute_map = {
        'rule_group_ids': 'rule_group_ids'
    }

    def __init__(self, rule_group_ids=None):
        r"""BatchDeleteRuleGroupsBaseDTO

        The model defined in huaweicloud sdk

        :param rule_group_ids: 识别规则组id列表
        :type rule_group_ids: list[str]
        """
        
        

        self._rule_group_ids = None
        self.discriminator = None

        self.rule_group_ids = rule_group_ids

    @property
    def rule_group_ids(self):
        r"""Gets the rule_group_ids of this BatchDeleteRuleGroupsBaseDTO.

        识别规则组id列表

        :return: The rule_group_ids of this BatchDeleteRuleGroupsBaseDTO.
        :rtype: list[str]
        """
        return self._rule_group_ids

    @rule_group_ids.setter
    def rule_group_ids(self, rule_group_ids):
        r"""Sets the rule_group_ids of this BatchDeleteRuleGroupsBaseDTO.

        识别规则组id列表

        :param rule_group_ids: The rule_group_ids of this BatchDeleteRuleGroupsBaseDTO.
        :type rule_group_ids: list[str]
        """
        self._rule_group_ids = rule_group_ids

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
        if not isinstance(other, BatchDeleteRuleGroupsBaseDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
