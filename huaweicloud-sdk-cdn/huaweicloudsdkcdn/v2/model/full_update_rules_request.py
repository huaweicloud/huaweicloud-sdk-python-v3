# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FullUpdateRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rules': 'list[CreateRuleRequest]'
    }

    attribute_map = {
        'rules': 'rules'
    }

    def __init__(self, rules=None):
        r"""FullUpdateRulesRequest

        The model defined in huaweicloud sdk

        :param rules: **参数解释：** 规则配置内容，可以配置多个规则 **约束限制：** 不涉及
        :type rules: list[:class:`huaweicloudsdkcdn.v2.CreateRuleRequest`]
        """
        
        

        self._rules = None
        self.discriminator = None

        self.rules = rules

    @property
    def rules(self):
        r"""Gets the rules of this FullUpdateRulesRequest.

        **参数解释：** 规则配置内容，可以配置多个规则 **约束限制：** 不涉及

        :return: The rules of this FullUpdateRulesRequest.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.CreateRuleRequest`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        r"""Sets the rules of this FullUpdateRulesRequest.

        **参数解释：** 规则配置内容，可以配置多个规则 **约束限制：** 不涉及

        :param rules: The rules of this FullUpdateRulesRequest.
        :type rules: list[:class:`huaweicloudsdkcdn.v2.CreateRuleRequest`]
        """
        self._rules = rules

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
        if not isinstance(other, FullUpdateRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
