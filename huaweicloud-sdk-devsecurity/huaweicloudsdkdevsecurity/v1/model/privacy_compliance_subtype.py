# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrivacyComplianceSubtype:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'desc': 'str',
        'checker_rules': 'list[CheckerRule]'
    }

    attribute_map = {
        'desc': 'desc',
        'checker_rules': 'checker_rules'
    }

    def __init__(self, desc=None, checker_rules=None):
        """PrivacyComplianceSubtype

        The model defined in huaweicloud sdk

        :param desc: 隐私合规子类型描述
        :type desc: str
        :param checker_rules: 检测项列表
        :type checker_rules: list[:class:`huaweicloudsdkdevsecurity.v1.CheckerRule`]
        """
        
        

        self._desc = None
        self._checker_rules = None
        self.discriminator = None

        if desc is not None:
            self.desc = desc
        if checker_rules is not None:
            self.checker_rules = checker_rules

    @property
    def desc(self):
        """Gets the desc of this PrivacyComplianceSubtype.

        隐私合规子类型描述

        :return: The desc of this PrivacyComplianceSubtype.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this PrivacyComplianceSubtype.

        隐私合规子类型描述

        :param desc: The desc of this PrivacyComplianceSubtype.
        :type desc: str
        """
        self._desc = desc

    @property
    def checker_rules(self):
        """Gets the checker_rules of this PrivacyComplianceSubtype.

        检测项列表

        :return: The checker_rules of this PrivacyComplianceSubtype.
        :rtype: list[:class:`huaweicloudsdkdevsecurity.v1.CheckerRule`]
        """
        return self._checker_rules

    @checker_rules.setter
    def checker_rules(self, checker_rules):
        """Sets the checker_rules of this PrivacyComplianceSubtype.

        检测项列表

        :param checker_rules: The checker_rules of this PrivacyComplianceSubtype.
        :type checker_rules: list[:class:`huaweicloudsdkdevsecurity.v1.CheckerRule`]
        """
        self._checker_rules = checker_rules

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
        if not isinstance(other, PrivacyComplianceSubtype):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
