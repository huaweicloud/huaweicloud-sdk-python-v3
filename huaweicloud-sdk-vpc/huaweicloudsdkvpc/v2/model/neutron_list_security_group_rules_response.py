# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronListSecurityGroupRulesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'security_group_rules': 'list[NeutronSecurityGroupRule]',
        'security_group_rules_links': 'list[NeutronPageLink]'
    }

    attribute_map = {
        'security_group_rules': 'security_group_rules',
        'security_group_rules_links': 'security_group_rules_links'
    }

    def __init__(self, security_group_rules=None, security_group_rules_links=None):
        """NeutronListSecurityGroupRulesResponse

        The model defined in huaweicloud sdk

        :param security_group_rules: 安全组规则对象列表
        :type security_group_rules: list[:class:`huaweicloudsdkvpc.v2.NeutronSecurityGroupRule`]
        :param security_group_rules_links: 分页信息
        :type security_group_rules_links: list[:class:`huaweicloudsdkvpc.v2.NeutronPageLink`]
        """
        
        super(NeutronListSecurityGroupRulesResponse, self).__init__()

        self._security_group_rules = None
        self._security_group_rules_links = None
        self.discriminator = None

        if security_group_rules is not None:
            self.security_group_rules = security_group_rules
        if security_group_rules_links is not None:
            self.security_group_rules_links = security_group_rules_links

    @property
    def security_group_rules(self):
        """Gets the security_group_rules of this NeutronListSecurityGroupRulesResponse.

        安全组规则对象列表

        :return: The security_group_rules of this NeutronListSecurityGroupRulesResponse.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.NeutronSecurityGroupRule`]
        """
        return self._security_group_rules

    @security_group_rules.setter
    def security_group_rules(self, security_group_rules):
        """Sets the security_group_rules of this NeutronListSecurityGroupRulesResponse.

        安全组规则对象列表

        :param security_group_rules: The security_group_rules of this NeutronListSecurityGroupRulesResponse.
        :type security_group_rules: list[:class:`huaweicloudsdkvpc.v2.NeutronSecurityGroupRule`]
        """
        self._security_group_rules = security_group_rules

    @property
    def security_group_rules_links(self):
        """Gets the security_group_rules_links of this NeutronListSecurityGroupRulesResponse.

        分页信息

        :return: The security_group_rules_links of this NeutronListSecurityGroupRulesResponse.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.NeutronPageLink`]
        """
        return self._security_group_rules_links

    @security_group_rules_links.setter
    def security_group_rules_links(self, security_group_rules_links):
        """Sets the security_group_rules_links of this NeutronListSecurityGroupRulesResponse.

        分页信息

        :param security_group_rules_links: The security_group_rules_links of this NeutronListSecurityGroupRulesResponse.
        :type security_group_rules_links: list[:class:`huaweicloudsdkvpc.v2.NeutronPageLink`]
        """
        self._security_group_rules_links = security_group_rules_links

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
        if not isinstance(other, NeutronListSecurityGroupRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
