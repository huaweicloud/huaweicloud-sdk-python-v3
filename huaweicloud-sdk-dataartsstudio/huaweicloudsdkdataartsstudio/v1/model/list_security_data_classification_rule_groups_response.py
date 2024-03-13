# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityDataClassificationRuleGroupsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_groups': 'list[DataClassificationGroupQueryDTO]',
        'total': 'int'
    }

    attribute_map = {
        'rule_groups': 'rule_groups',
        'total': 'total'
    }

    def __init__(self, rule_groups=None, total=None):
        """ListSecurityDataClassificationRuleGroupsResponse

        The model defined in huaweicloud sdk

        :param rule_groups: 规则组列表
        :type rule_groups: list[:class:`huaweicloudsdkdataartsstudio.v1.DataClassificationGroupQueryDTO`]
        :param total: 规则组总数
        :type total: int
        """
        
        super(ListSecurityDataClassificationRuleGroupsResponse, self).__init__()

        self._rule_groups = None
        self._total = None
        self.discriminator = None

        if rule_groups is not None:
            self.rule_groups = rule_groups
        if total is not None:
            self.total = total

    @property
    def rule_groups(self):
        """Gets the rule_groups of this ListSecurityDataClassificationRuleGroupsResponse.

        规则组列表

        :return: The rule_groups of this ListSecurityDataClassificationRuleGroupsResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.DataClassificationGroupQueryDTO`]
        """
        return self._rule_groups

    @rule_groups.setter
    def rule_groups(self, rule_groups):
        """Sets the rule_groups of this ListSecurityDataClassificationRuleGroupsResponse.

        规则组列表

        :param rule_groups: The rule_groups of this ListSecurityDataClassificationRuleGroupsResponse.
        :type rule_groups: list[:class:`huaweicloudsdkdataartsstudio.v1.DataClassificationGroupQueryDTO`]
        """
        self._rule_groups = rule_groups

    @property
    def total(self):
        """Gets the total of this ListSecurityDataClassificationRuleGroupsResponse.

        规则组总数

        :return: The total of this ListSecurityDataClassificationRuleGroupsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListSecurityDataClassificationRuleGroupsResponse.

        规则组总数

        :param total: The total of this ListSecurityDataClassificationRuleGroupsResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListSecurityDataClassificationRuleGroupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
