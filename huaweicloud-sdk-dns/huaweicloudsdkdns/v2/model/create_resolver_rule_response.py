# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateResolverRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resolver_rule': 'ResolverRuleParam'
    }

    attribute_map = {
        'resolver_rule': 'resolver_rule'
    }

    def __init__(self, resolver_rule=None):
        r"""CreateResolverRuleResponse

        The model defined in huaweicloud sdk

        :param resolver_rule: 
        :type resolver_rule: :class:`huaweicloudsdkdns.v2.ResolverRuleParam`
        """
        
        super(CreateResolverRuleResponse, self).__init__()

        self._resolver_rule = None
        self.discriminator = None

        if resolver_rule is not None:
            self.resolver_rule = resolver_rule

    @property
    def resolver_rule(self):
        r"""Gets the resolver_rule of this CreateResolverRuleResponse.

        :return: The resolver_rule of this CreateResolverRuleResponse.
        :rtype: :class:`huaweicloudsdkdns.v2.ResolverRuleParam`
        """
        return self._resolver_rule

    @resolver_rule.setter
    def resolver_rule(self, resolver_rule):
        r"""Sets the resolver_rule of this CreateResolverRuleResponse.

        :param resolver_rule: The resolver_rule of this CreateResolverRuleResponse.
        :type resolver_rule: :class:`huaweicloudsdkdns.v2.ResolverRuleParam`
        """
        self._resolver_rule = resolver_rule

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
        if not isinstance(other, CreateResolverRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
