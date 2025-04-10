# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PatchRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'patch_filters': 'list[PatchFilter]',
        'rule_name': 'str',
        'compliance_level': 'str',
        'approve_after_days': 'int',
        'approve_until_date': 'int',
        'enable_non_security': 'bool'
    }

    attribute_map = {
        'patch_filters': 'patch_filters',
        'rule_name': 'rule_name',
        'compliance_level': 'compliance_level',
        'approve_after_days': 'approve_after_days',
        'approve_until_date': 'approve_until_date',
        'enable_non_security': 'enable_non_security'
    }

    def __init__(self, patch_filters=None, rule_name=None, compliance_level=None, approve_after_days=None, approve_until_date=None, enable_non_security=None):
        r"""PatchRule

        The model defined in huaweicloud sdk

        :param patch_filters: 批准规则过滤
        :type patch_filters: list[:class:`huaweicloudsdkcoc.v1.PatchFilter`]
        :param rule_name: 规则名称
        :type rule_name: str
        :param compliance_level: 合规性报告级别
        :type compliance_level: str
        :param approve_after_days: 指定天数后批准补丁，指定的天数
        :type approve_after_days: int
        :param approve_until_date: 批准指定日期之前发布的补丁,指定的日期时间戳
        :type approve_until_date: int
        :param enable_non_security: 是否包括非安全性更新
        :type enable_non_security: bool
        """
        
        

        self._patch_filters = None
        self._rule_name = None
        self._compliance_level = None
        self._approve_after_days = None
        self._approve_until_date = None
        self._enable_non_security = None
        self.discriminator = None

        self.patch_filters = patch_filters
        if rule_name is not None:
            self.rule_name = rule_name
        self.compliance_level = compliance_level
        if approve_after_days is not None:
            self.approve_after_days = approve_after_days
        if approve_until_date is not None:
            self.approve_until_date = approve_until_date
        self.enable_non_security = enable_non_security

    @property
    def patch_filters(self):
        r"""Gets the patch_filters of this PatchRule.

        批准规则过滤

        :return: The patch_filters of this PatchRule.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.PatchFilter`]
        """
        return self._patch_filters

    @patch_filters.setter
    def patch_filters(self, patch_filters):
        r"""Sets the patch_filters of this PatchRule.

        批准规则过滤

        :param patch_filters: The patch_filters of this PatchRule.
        :type patch_filters: list[:class:`huaweicloudsdkcoc.v1.PatchFilter`]
        """
        self._patch_filters = patch_filters

    @property
    def rule_name(self):
        r"""Gets the rule_name of this PatchRule.

        规则名称

        :return: The rule_name of this PatchRule.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this PatchRule.

        规则名称

        :param rule_name: The rule_name of this PatchRule.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def compliance_level(self):
        r"""Gets the compliance_level of this PatchRule.

        合规性报告级别

        :return: The compliance_level of this PatchRule.
        :rtype: str
        """
        return self._compliance_level

    @compliance_level.setter
    def compliance_level(self, compliance_level):
        r"""Sets the compliance_level of this PatchRule.

        合规性报告级别

        :param compliance_level: The compliance_level of this PatchRule.
        :type compliance_level: str
        """
        self._compliance_level = compliance_level

    @property
    def approve_after_days(self):
        r"""Gets the approve_after_days of this PatchRule.

        指定天数后批准补丁，指定的天数

        :return: The approve_after_days of this PatchRule.
        :rtype: int
        """
        return self._approve_after_days

    @approve_after_days.setter
    def approve_after_days(self, approve_after_days):
        r"""Sets the approve_after_days of this PatchRule.

        指定天数后批准补丁，指定的天数

        :param approve_after_days: The approve_after_days of this PatchRule.
        :type approve_after_days: int
        """
        self._approve_after_days = approve_after_days

    @property
    def approve_until_date(self):
        r"""Gets the approve_until_date of this PatchRule.

        批准指定日期之前发布的补丁,指定的日期时间戳

        :return: The approve_until_date of this PatchRule.
        :rtype: int
        """
        return self._approve_until_date

    @approve_until_date.setter
    def approve_until_date(self, approve_until_date):
        r"""Sets the approve_until_date of this PatchRule.

        批准指定日期之前发布的补丁,指定的日期时间戳

        :param approve_until_date: The approve_until_date of this PatchRule.
        :type approve_until_date: int
        """
        self._approve_until_date = approve_until_date

    @property
    def enable_non_security(self):
        r"""Gets the enable_non_security of this PatchRule.

        是否包括非安全性更新

        :return: The enable_non_security of this PatchRule.
        :rtype: bool
        """
        return self._enable_non_security

    @enable_non_security.setter
    def enable_non_security(self, enable_non_security):
        r"""Sets the enable_non_security of this PatchRule.

        是否包括非安全性更新

        :param enable_non_security: The enable_non_security of this PatchRule.
        :type enable_non_security: bool
        """
        self._enable_non_security = enable_non_security

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
        if not isinstance(other, PatchRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
