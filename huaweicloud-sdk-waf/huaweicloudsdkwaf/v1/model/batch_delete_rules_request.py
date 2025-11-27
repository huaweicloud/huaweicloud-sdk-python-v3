# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_type': 'str',
        'body': 'PolicyRuleIdRequestBody'
    }

    attribute_map = {
        'rule_type': 'rule_type',
        'body': 'body'
    }

    def __init__(self, rule_type=None, body=None):
        r"""BatchDeleteRulesRequest

        The model defined in huaweicloud sdk

        :param rule_type: **参数解释：** 需要删除的规则类型,目前支持cc,custom,whiteblackip,geoip,ip-reputation,antitamper,antileakage,ignore,privacy **约束限制：** 不涉及 **取值范围：** - cc - custom - whiteblackip - geoip - ip-reputation - antitamper - antileakage - ignore - privacy  **默认取值：** 不涉及
        :type rule_type: str
        :param body: Body of the BatchDeleteRulesRequest
        :type body: :class:`huaweicloudsdkwaf.v1.PolicyRuleIdRequestBody`
        """
        
        

        self._rule_type = None
        self._body = None
        self.discriminator = None

        self.rule_type = rule_type
        if body is not None:
            self.body = body

    @property
    def rule_type(self):
        r"""Gets the rule_type of this BatchDeleteRulesRequest.

        **参数解释：** 需要删除的规则类型,目前支持cc,custom,whiteblackip,geoip,ip-reputation,antitamper,antileakage,ignore,privacy **约束限制：** 不涉及 **取值范围：** - cc - custom - whiteblackip - geoip - ip-reputation - antitamper - antileakage - ignore - privacy  **默认取值：** 不涉及

        :return: The rule_type of this BatchDeleteRulesRequest.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        r"""Sets the rule_type of this BatchDeleteRulesRequest.

        **参数解释：** 需要删除的规则类型,目前支持cc,custom,whiteblackip,geoip,ip-reputation,antitamper,antileakage,ignore,privacy **约束限制：** 不涉及 **取值范围：** - cc - custom - whiteblackip - geoip - ip-reputation - antitamper - antileakage - ignore - privacy  **默认取值：** 不涉及

        :param rule_type: The rule_type of this BatchDeleteRulesRequest.
        :type rule_type: str
        """
        self._rule_type = rule_type

    @property
    def body(self):
        r"""Gets the body of this BatchDeleteRulesRequest.

        :return: The body of this BatchDeleteRulesRequest.
        :rtype: :class:`huaweicloudsdkwaf.v1.PolicyRuleIdRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchDeleteRulesRequest.

        :param body: The body of this BatchDeleteRulesRequest.
        :type body: :class:`huaweicloudsdkwaf.v1.PolicyRuleIdRequestBody`
        """
        self._body = body

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchDeleteRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
