# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHttpPolicyRuleStatusRequest:

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
        'rule_type': 'str',
        'rule_id': 'str',
        'body': 'UpdateHttpPolicyRuleStatusRequestBody'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'rule_type': 'rule_type',
        'rule_id': 'rule_id',
        'body': 'body'
    }

    def __init__(self, policy_id=None, rule_type=None, rule_id=None, body=None):
        r"""UpdateHttpPolicyRuleStatusRequest

        The model defined in huaweicloud sdk

        :param policy_id: 防护策略id
        :type policy_id: str
        :param rule_type: 防护策略规则 cc-rule|access-control-rule|blocktrustip-rule|privacy-rule|ignore-rule|geoip-rule|punishment-rule
        :type rule_type: str
        :param rule_id: 防护策略规则id
        :type rule_id: str
        :param body: Body of the UpdateHttpPolicyRuleStatusRequest
        :type body: :class:`huaweicloudsdkedgesec.v2.UpdateHttpPolicyRuleStatusRequestBody`
        """
        
        

        self._policy_id = None
        self._rule_type = None
        self._rule_id = None
        self._body = None
        self.discriminator = None

        self.policy_id = policy_id
        self.rule_type = rule_type
        self.rule_id = rule_id
        if body is not None:
            self.body = body

    @property
    def policy_id(self):
        r"""Gets the policy_id of this UpdateHttpPolicyRuleStatusRequest.

        防护策略id

        :return: The policy_id of this UpdateHttpPolicyRuleStatusRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this UpdateHttpPolicyRuleStatusRequest.

        防护策略id

        :param policy_id: The policy_id of this UpdateHttpPolicyRuleStatusRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def rule_type(self):
        r"""Gets the rule_type of this UpdateHttpPolicyRuleStatusRequest.

        防护策略规则 cc-rule|access-control-rule|blocktrustip-rule|privacy-rule|ignore-rule|geoip-rule|punishment-rule

        :return: The rule_type of this UpdateHttpPolicyRuleStatusRequest.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        r"""Sets the rule_type of this UpdateHttpPolicyRuleStatusRequest.

        防护策略规则 cc-rule|access-control-rule|blocktrustip-rule|privacy-rule|ignore-rule|geoip-rule|punishment-rule

        :param rule_type: The rule_type of this UpdateHttpPolicyRuleStatusRequest.
        :type rule_type: str
        """
        self._rule_type = rule_type

    @property
    def rule_id(self):
        r"""Gets the rule_id of this UpdateHttpPolicyRuleStatusRequest.

        防护策略规则id

        :return: The rule_id of this UpdateHttpPolicyRuleStatusRequest.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this UpdateHttpPolicyRuleStatusRequest.

        防护策略规则id

        :param rule_id: The rule_id of this UpdateHttpPolicyRuleStatusRequest.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def body(self):
        r"""Gets the body of this UpdateHttpPolicyRuleStatusRequest.

        :return: The body of this UpdateHttpPolicyRuleStatusRequest.
        :rtype: :class:`huaweicloudsdkedgesec.v2.UpdateHttpPolicyRuleStatusRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateHttpPolicyRuleStatusRequest.

        :param body: The body of this UpdateHttpPolicyRuleStatusRequest.
        :type body: :class:`huaweicloudsdkedgesec.v2.UpdateHttpPolicyRuleStatusRequestBody`
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
        if not isinstance(other, UpdateHttpPolicyRuleStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
