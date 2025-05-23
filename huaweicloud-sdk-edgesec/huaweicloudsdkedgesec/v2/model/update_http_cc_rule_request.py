# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHttpCcRuleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_id': 'str',
        'rule_id': 'str',
        'body': 'UpdateHttpCcRuleRequestBody'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'rule_id': 'rule_id',
        'body': 'body'
    }

    def __init__(self, policy_id=None, rule_id=None, body=None):
        r"""UpdateHttpCcRuleRequest

        The model defined in huaweicloud sdk

        :param policy_id: 策略id
        :type policy_id: str
        :param rule_id: cc规则id
        :type rule_id: str
        :param body: Body of the UpdateHttpCcRuleRequest
        :type body: :class:`huaweicloudsdkedgesec.v2.UpdateHttpCcRuleRequestBody`
        """
        
        

        self._policy_id = None
        self._rule_id = None
        self._body = None
        self.discriminator = None

        self.policy_id = policy_id
        self.rule_id = rule_id
        if body is not None:
            self.body = body

    @property
    def policy_id(self):
        r"""Gets the policy_id of this UpdateHttpCcRuleRequest.

        策略id

        :return: The policy_id of this UpdateHttpCcRuleRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this UpdateHttpCcRuleRequest.

        策略id

        :param policy_id: The policy_id of this UpdateHttpCcRuleRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def rule_id(self):
        r"""Gets the rule_id of this UpdateHttpCcRuleRequest.

        cc规则id

        :return: The rule_id of this UpdateHttpCcRuleRequest.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this UpdateHttpCcRuleRequest.

        cc规则id

        :param rule_id: The rule_id of this UpdateHttpCcRuleRequest.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def body(self):
        r"""Gets the body of this UpdateHttpCcRuleRequest.

        :return: The body of this UpdateHttpCcRuleRequest.
        :rtype: :class:`huaweicloudsdkedgesec.v2.UpdateHttpCcRuleRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateHttpCcRuleRequest.

        :param body: The body of this UpdateHttpCcRuleRequest.
        :type body: :class:`huaweicloudsdkedgesec.v2.UpdateHttpCcRuleRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateHttpCcRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
