# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulnItem:

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
        'risk_level': 'str',
        'vuln_rules': 'list[VulnRule]'
    }

    attribute_map = {
        'desc': 'desc',
        'risk_level': 'risk_level',
        'vuln_rules': 'vuln_rules'
    }

    def __init__(self, desc=None, risk_level=None, vuln_rules=None):
        """VulnItem

        The model defined in huaweicloud sdk

        :param desc: 漏洞项描述
        :type desc: str
        :param risk_level: 风险等级
        :type risk_level: str
        :param vuln_rules: 漏洞问题列表
        :type vuln_rules: list[:class:`huaweicloudsdkdevsecurity.v1.VulnRule`]
        """
        
        

        self._desc = None
        self._risk_level = None
        self._vuln_rules = None
        self.discriminator = None

        if desc is not None:
            self.desc = desc
        if risk_level is not None:
            self.risk_level = risk_level
        if vuln_rules is not None:
            self.vuln_rules = vuln_rules

    @property
    def desc(self):
        """Gets the desc of this VulnItem.

        漏洞项描述

        :return: The desc of this VulnItem.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this VulnItem.

        漏洞项描述

        :param desc: The desc of this VulnItem.
        :type desc: str
        """
        self._desc = desc

    @property
    def risk_level(self):
        """Gets the risk_level of this VulnItem.

        风险等级

        :return: The risk_level of this VulnItem.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        """Sets the risk_level of this VulnItem.

        风险等级

        :param risk_level: The risk_level of this VulnItem.
        :type risk_level: str
        """
        self._risk_level = risk_level

    @property
    def vuln_rules(self):
        """Gets the vuln_rules of this VulnItem.

        漏洞问题列表

        :return: The vuln_rules of this VulnItem.
        :rtype: list[:class:`huaweicloudsdkdevsecurity.v1.VulnRule`]
        """
        return self._vuln_rules

    @vuln_rules.setter
    def vuln_rules(self, vuln_rules):
        """Sets the vuln_rules of this VulnItem.

        漏洞问题列表

        :param vuln_rules: The vuln_rules of this VulnItem.
        :type vuln_rules: list[:class:`huaweicloudsdkdevsecurity.v1.VulnRule`]
        """
        self._vuln_rules = vuln_rules

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
        if not isinstance(other, VulnItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
