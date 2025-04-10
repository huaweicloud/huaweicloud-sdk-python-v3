# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteRuleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'rule_id': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'rule_id': 'rule_id'
    }

    def __init__(self, domain_id=None, rule_id=None):
        r"""DeleteRuleRequest

        The model defined in huaweicloud sdk

        :param domain_id: 租户ID
        :type domain_id: str
        :param rule_id: 规则ID
        :type rule_id: str
        """
        
        

        self._domain_id = None
        self._rule_id = None
        self.discriminator = None

        self.domain_id = domain_id
        self.rule_id = rule_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this DeleteRuleRequest.

        租户ID

        :return: The domain_id of this DeleteRuleRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this DeleteRuleRequest.

        租户ID

        :param domain_id: The domain_id of this DeleteRuleRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def rule_id(self):
        r"""Gets the rule_id of this DeleteRuleRequest.

        规则ID

        :return: The rule_id of this DeleteRuleRequest.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this DeleteRuleRequest.

        规则ID

        :param rule_id: The rule_id of this DeleteRuleRequest.
        :type rule_id: str
        """
        self._rule_id = rule_id

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
        if not isinstance(other, DeleteRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
