# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AdvancedIpsRuleListVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'advanced_ips_rules': 'list[AdvancedIpsRuleVo]',
        'total': 'int'
    }

    attribute_map = {
        'advanced_ips_rules': 'advanced_ips_rules',
        'total': 'total'
    }

    def __init__(self, advanced_ips_rules=None, total=None):
        r"""AdvancedIpsRuleListVo

        The model defined in huaweicloud sdk

        :param advanced_ips_rules: 
        :type advanced_ips_rules: list[:class:`huaweicloudsdkcfw.v1.AdvancedIpsRuleVo`]
        :param total: 
        :type total: int
        """
        
        

        self._advanced_ips_rules = None
        self._total = None
        self.discriminator = None

        if advanced_ips_rules is not None:
            self.advanced_ips_rules = advanced_ips_rules
        if total is not None:
            self.total = total

    @property
    def advanced_ips_rules(self):
        r"""Gets the advanced_ips_rules of this AdvancedIpsRuleListVo.

        :return: The advanced_ips_rules of this AdvancedIpsRuleListVo.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.AdvancedIpsRuleVo`]
        """
        return self._advanced_ips_rules

    @advanced_ips_rules.setter
    def advanced_ips_rules(self, advanced_ips_rules):
        r"""Sets the advanced_ips_rules of this AdvancedIpsRuleListVo.

        :param advanced_ips_rules: The advanced_ips_rules of this AdvancedIpsRuleListVo.
        :type advanced_ips_rules: list[:class:`huaweicloudsdkcfw.v1.AdvancedIpsRuleVo`]
        """
        self._advanced_ips_rules = advanced_ips_rules

    @property
    def total(self):
        r"""Gets the total of this AdvancedIpsRuleListVo.

        :return: The total of this AdvancedIpsRuleListVo.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this AdvancedIpsRuleListVo.

        :param total: The total of this AdvancedIpsRuleListVo.
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
        if not isinstance(other, AdvancedIpsRuleListVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
