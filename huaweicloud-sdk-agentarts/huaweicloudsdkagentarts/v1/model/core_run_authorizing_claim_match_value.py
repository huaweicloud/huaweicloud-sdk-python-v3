# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreRunAuthorizingClaimMatchValue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'claim_match_operator': 'str',
        'claim_match_value': 'CoreRunClaimMatchValue'
    }

    attribute_map = {
        'claim_match_operator': 'claim_match_operator',
        'claim_match_value': 'claim_match_value'
    }

    def __init__(self, claim_match_operator=None, claim_match_value=None):
        r"""CoreRunAuthorizingClaimMatchValue

        The model defined in huaweicloud sdk

        :param claim_match_operator: **参数解释**：  定义声明字段值与要匹配的值之间的关系。 - EQUALS: 表示完全匹配 - CONTAINS: 表示包含匹配项 - CONTAINS_ANY: 表示包含任意匹配项。 **约束限制**: 不涉及。 **取值范围**： 长度为 1 - 12 个字符。允许的值： - EQUALS - CONTAINS - CONTAINS_ANY。 **默认取值**: 不涉及。
        :type claim_match_operator: str
        :param claim_match_value: 
        :type claim_match_value: :class:`huaweicloudsdkagentarts.v1.CoreRunClaimMatchValue`
        """
        
        

        self._claim_match_operator = None
        self._claim_match_value = None
        self.discriminator = None

        self.claim_match_operator = claim_match_operator
        self.claim_match_value = claim_match_value

    @property
    def claim_match_operator(self):
        r"""Gets the claim_match_operator of this CoreRunAuthorizingClaimMatchValue.

        **参数解释**：  定义声明字段值与要匹配的值之间的关系。 - EQUALS: 表示完全匹配 - CONTAINS: 表示包含匹配项 - CONTAINS_ANY: 表示包含任意匹配项。 **约束限制**: 不涉及。 **取值范围**： 长度为 1 - 12 个字符。允许的值： - EQUALS - CONTAINS - CONTAINS_ANY。 **默认取值**: 不涉及。

        :return: The claim_match_operator of this CoreRunAuthorizingClaimMatchValue.
        :rtype: str
        """
        return self._claim_match_operator

    @claim_match_operator.setter
    def claim_match_operator(self, claim_match_operator):
        r"""Sets the claim_match_operator of this CoreRunAuthorizingClaimMatchValue.

        **参数解释**：  定义声明字段值与要匹配的值之间的关系。 - EQUALS: 表示完全匹配 - CONTAINS: 表示包含匹配项 - CONTAINS_ANY: 表示包含任意匹配项。 **约束限制**: 不涉及。 **取值范围**： 长度为 1 - 12 个字符。允许的值： - EQUALS - CONTAINS - CONTAINS_ANY。 **默认取值**: 不涉及。

        :param claim_match_operator: The claim_match_operator of this CoreRunAuthorizingClaimMatchValue.
        :type claim_match_operator: str
        """
        self._claim_match_operator = claim_match_operator

    @property
    def claim_match_value(self):
        r"""Gets the claim_match_value of this CoreRunAuthorizingClaimMatchValue.

        :return: The claim_match_value of this CoreRunAuthorizingClaimMatchValue.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreRunClaimMatchValue`
        """
        return self._claim_match_value

    @claim_match_value.setter
    def claim_match_value(self, claim_match_value):
        r"""Sets the claim_match_value of this CoreRunAuthorizingClaimMatchValue.

        :param claim_match_value: The claim_match_value of this CoreRunAuthorizingClaimMatchValue.
        :type claim_match_value: :class:`huaweicloudsdkagentarts.v1.CoreRunClaimMatchValue`
        """
        self._claim_match_value = claim_match_value

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
        if not isinstance(other, CoreRunAuthorizingClaimMatchValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
