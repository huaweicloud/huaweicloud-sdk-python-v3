# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityGroupRulesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'security_group_rules': 'list[SecurityGroupRule]',
        'count': 'int'
    }

    attribute_map = {
        'security_group_rules': 'security_group_rules',
        'count': 'count'
    }

    def __init__(self, security_group_rules=None, count=None):
        """ListSecurityGroupRulesResponse

        The model defined in huaweicloud sdk

        :param security_group_rules: 安全组规则列表对象。
        :type security_group_rules: list[:class:`huaweicloudsdkiec.v1.SecurityGroupRule`]
        :param count: 安全组规则数目。
        :type count: int
        """
        
        super(ListSecurityGroupRulesResponse, self).__init__()

        self._security_group_rules = None
        self._count = None
        self.discriminator = None

        if security_group_rules is not None:
            self.security_group_rules = security_group_rules
        if count is not None:
            self.count = count

    @property
    def security_group_rules(self):
        """Gets the security_group_rules of this ListSecurityGroupRulesResponse.

        安全组规则列表对象。

        :return: The security_group_rules of this ListSecurityGroupRulesResponse.
        :rtype: list[:class:`huaweicloudsdkiec.v1.SecurityGroupRule`]
        """
        return self._security_group_rules

    @security_group_rules.setter
    def security_group_rules(self, security_group_rules):
        """Sets the security_group_rules of this ListSecurityGroupRulesResponse.

        安全组规则列表对象。

        :param security_group_rules: The security_group_rules of this ListSecurityGroupRulesResponse.
        :type security_group_rules: list[:class:`huaweicloudsdkiec.v1.SecurityGroupRule`]
        """
        self._security_group_rules = security_group_rules

    @property
    def count(self):
        """Gets the count of this ListSecurityGroupRulesResponse.

        安全组规则数目。

        :return: The count of this ListSecurityGroupRulesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListSecurityGroupRulesResponse.

        安全组规则数目。

        :param count: The count of this ListSecurityGroupRulesResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListSecurityGroupRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
