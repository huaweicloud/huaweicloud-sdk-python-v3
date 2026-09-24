# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyAdvancedRetentionRules:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'weekly_retention_rules': 'PolicyWeeklyRetentionRules',
        'monthly_retention_rules': 'PolicyMonthlyRetentionRules',
        'yearly_retention_rules': 'PolicyYearlyRetentionRules'
    }

    attribute_map = {
        'weekly_retention_rules': 'weekly_retention_rules',
        'monthly_retention_rules': 'monthly_retention_rules',
        'yearly_retention_rules': 'yearly_retention_rules'
    }

    def __init__(self, weekly_retention_rules=None, monthly_retention_rules=None, yearly_retention_rules=None):
        r"""PolicyAdvancedRetentionRules

        The model defined in huaweicloud sdk

        :param weekly_retention_rules: 
        :type weekly_retention_rules: :class:`huaweicloudsdkcbr.v1.PolicyWeeklyRetentionRules`
        :param monthly_retention_rules: 
        :type monthly_retention_rules: :class:`huaweicloudsdkcbr.v1.PolicyMonthlyRetentionRules`
        :param yearly_retention_rules: 
        :type yearly_retention_rules: :class:`huaweicloudsdkcbr.v1.PolicyYearlyRetentionRules`
        """
        
        

        self._weekly_retention_rules = None
        self._monthly_retention_rules = None
        self._yearly_retention_rules = None
        self.discriminator = None

        if weekly_retention_rules is not None:
            self.weekly_retention_rules = weekly_retention_rules
        if monthly_retention_rules is not None:
            self.monthly_retention_rules = monthly_retention_rules
        if yearly_retention_rules is not None:
            self.yearly_retention_rules = yearly_retention_rules

    @property
    def weekly_retention_rules(self):
        r"""Gets the weekly_retention_rules of this PolicyAdvancedRetentionRules.

        :return: The weekly_retention_rules of this PolicyAdvancedRetentionRules.
        :rtype: :class:`huaweicloudsdkcbr.v1.PolicyWeeklyRetentionRules`
        """
        return self._weekly_retention_rules

    @weekly_retention_rules.setter
    def weekly_retention_rules(self, weekly_retention_rules):
        r"""Sets the weekly_retention_rules of this PolicyAdvancedRetentionRules.

        :param weekly_retention_rules: The weekly_retention_rules of this PolicyAdvancedRetentionRules.
        :type weekly_retention_rules: :class:`huaweicloudsdkcbr.v1.PolicyWeeklyRetentionRules`
        """
        self._weekly_retention_rules = weekly_retention_rules

    @property
    def monthly_retention_rules(self):
        r"""Gets the monthly_retention_rules of this PolicyAdvancedRetentionRules.

        :return: The monthly_retention_rules of this PolicyAdvancedRetentionRules.
        :rtype: :class:`huaweicloudsdkcbr.v1.PolicyMonthlyRetentionRules`
        """
        return self._monthly_retention_rules

    @monthly_retention_rules.setter
    def monthly_retention_rules(self, monthly_retention_rules):
        r"""Sets the monthly_retention_rules of this PolicyAdvancedRetentionRules.

        :param monthly_retention_rules: The monthly_retention_rules of this PolicyAdvancedRetentionRules.
        :type monthly_retention_rules: :class:`huaweicloudsdkcbr.v1.PolicyMonthlyRetentionRules`
        """
        self._monthly_retention_rules = monthly_retention_rules

    @property
    def yearly_retention_rules(self):
        r"""Gets the yearly_retention_rules of this PolicyAdvancedRetentionRules.

        :return: The yearly_retention_rules of this PolicyAdvancedRetentionRules.
        :rtype: :class:`huaweicloudsdkcbr.v1.PolicyYearlyRetentionRules`
        """
        return self._yearly_retention_rules

    @yearly_retention_rules.setter
    def yearly_retention_rules(self, yearly_retention_rules):
        r"""Sets the yearly_retention_rules of this PolicyAdvancedRetentionRules.

        :param yearly_retention_rules: The yearly_retention_rules of this PolicyAdvancedRetentionRules.
        :type yearly_retention_rules: :class:`huaweicloudsdkcbr.v1.PolicyYearlyRetentionRules`
        """
        self._yearly_retention_rules = yearly_retention_rules

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
        if not isinstance(other, PolicyAdvancedRetentionRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
