# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteResolveRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resolver_rules': 'list[ResolveRuleParam]'
    }

    attribute_map = {
        'resolver_rules': 'resolver_rules'
    }

    def __init__(self, resolver_rules=None):
        """DeleteResolveRuleResponse

        The model defined in huaweicloud sdk

        :param resolver_rules: 查询resolver_rule的列表响应。
        :type resolver_rules: list[:class:`huaweicloudsdkdns.v2.ResolveRuleParam`]
        """
        
        super(DeleteResolveRuleResponse, self).__init__()

        self._resolver_rules = None
        self.discriminator = None

        if resolver_rules is not None:
            self.resolver_rules = resolver_rules

    @property
    def resolver_rules(self):
        """Gets the resolver_rules of this DeleteResolveRuleResponse.

        查询resolver_rule的列表响应。

        :return: The resolver_rules of this DeleteResolveRuleResponse.
        :rtype: list[:class:`huaweicloudsdkdns.v2.ResolveRuleParam`]
        """
        return self._resolver_rules

    @resolver_rules.setter
    def resolver_rules(self, resolver_rules):
        """Sets the resolver_rules of this DeleteResolveRuleResponse.

        查询resolver_rule的列表响应。

        :param resolver_rules: The resolver_rules of this DeleteResolveRuleResponse.
        :type resolver_rules: list[:class:`huaweicloudsdkdns.v2.ResolveRuleParam`]
        """
        self._resolver_rules = resolver_rules

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
        if not isinstance(other, DeleteResolveRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
