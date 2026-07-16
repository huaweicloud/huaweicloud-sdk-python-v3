# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreRunCustomClaimValidation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'authorizing_claim_match_value': 'CoreRunAuthorizingClaimMatchValue',
        'inbound_token_claim_name': 'str',
        'inbound_token_claim_value_type': 'str'
    }

    attribute_map = {
        'authorizing_claim_match_value': 'authorizing_claim_match_value',
        'inbound_token_claim_name': 'inbound_token_claim_name',
        'inbound_token_claim_value_type': 'inbound_token_claim_value_type'
    }

    def __init__(self, authorizing_claim_match_value=None, inbound_token_claim_name=None, inbound_token_claim_value_type=None):
        r"""CoreRunCustomClaimValidation

        The model defined in huaweicloud sdk

        :param authorizing_claim_match_value: 
        :type authorizing_claim_match_value: :class:`huaweicloudsdkagentarts.v1.CoreRunAuthorizingClaimMatchValue`
        :param inbound_token_claim_name: **参数解释**：  要检查的自定义声明字段的名称。 **约束限制**: 不涉及。 **取值范围**： 长度为 1 - 255 个字符，只包含字母数字、下划线、点号、中划线和冒号。 **默认取值**: 不涉及。
        :type inbound_token_claim_name: str
        :param inbound_token_claim_value_type: **参数解释**：  要检查的声明值的数据类型。 - STRING: 表示字符串类型。 - STRING_ARRAY: 表示字符串数组类型。 **约束限制**: 不涉及。 **取值范围**： 长度为 1 - 12 个字符。 - STRING - STRING_ARRAY **默认取值**: 不涉及。
        :type inbound_token_claim_value_type: str
        """
        
        

        self._authorizing_claim_match_value = None
        self._inbound_token_claim_name = None
        self._inbound_token_claim_value_type = None
        self.discriminator = None

        self.authorizing_claim_match_value = authorizing_claim_match_value
        self.inbound_token_claim_name = inbound_token_claim_name
        self.inbound_token_claim_value_type = inbound_token_claim_value_type

    @property
    def authorizing_claim_match_value(self):
        r"""Gets the authorizing_claim_match_value of this CoreRunCustomClaimValidation.

        :return: The authorizing_claim_match_value of this CoreRunCustomClaimValidation.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreRunAuthorizingClaimMatchValue`
        """
        return self._authorizing_claim_match_value

    @authorizing_claim_match_value.setter
    def authorizing_claim_match_value(self, authorizing_claim_match_value):
        r"""Sets the authorizing_claim_match_value of this CoreRunCustomClaimValidation.

        :param authorizing_claim_match_value: The authorizing_claim_match_value of this CoreRunCustomClaimValidation.
        :type authorizing_claim_match_value: :class:`huaweicloudsdkagentarts.v1.CoreRunAuthorizingClaimMatchValue`
        """
        self._authorizing_claim_match_value = authorizing_claim_match_value

    @property
    def inbound_token_claim_name(self):
        r"""Gets the inbound_token_claim_name of this CoreRunCustomClaimValidation.

        **参数解释**：  要检查的自定义声明字段的名称。 **约束限制**: 不涉及。 **取值范围**： 长度为 1 - 255 个字符，只包含字母数字、下划线、点号、中划线和冒号。 **默认取值**: 不涉及。

        :return: The inbound_token_claim_name of this CoreRunCustomClaimValidation.
        :rtype: str
        """
        return self._inbound_token_claim_name

    @inbound_token_claim_name.setter
    def inbound_token_claim_name(self, inbound_token_claim_name):
        r"""Sets the inbound_token_claim_name of this CoreRunCustomClaimValidation.

        **参数解释**：  要检查的自定义声明字段的名称。 **约束限制**: 不涉及。 **取值范围**： 长度为 1 - 255 个字符，只包含字母数字、下划线、点号、中划线和冒号。 **默认取值**: 不涉及。

        :param inbound_token_claim_name: The inbound_token_claim_name of this CoreRunCustomClaimValidation.
        :type inbound_token_claim_name: str
        """
        self._inbound_token_claim_name = inbound_token_claim_name

    @property
    def inbound_token_claim_value_type(self):
        r"""Gets the inbound_token_claim_value_type of this CoreRunCustomClaimValidation.

        **参数解释**：  要检查的声明值的数据类型。 - STRING: 表示字符串类型。 - STRING_ARRAY: 表示字符串数组类型。 **约束限制**: 不涉及。 **取值范围**： 长度为 1 - 12 个字符。 - STRING - STRING_ARRAY **默认取值**: 不涉及。

        :return: The inbound_token_claim_value_type of this CoreRunCustomClaimValidation.
        :rtype: str
        """
        return self._inbound_token_claim_value_type

    @inbound_token_claim_value_type.setter
    def inbound_token_claim_value_type(self, inbound_token_claim_value_type):
        r"""Sets the inbound_token_claim_value_type of this CoreRunCustomClaimValidation.

        **参数解释**：  要检查的声明值的数据类型。 - STRING: 表示字符串类型。 - STRING_ARRAY: 表示字符串数组类型。 **约束限制**: 不涉及。 **取值范围**： 长度为 1 - 12 个字符。 - STRING - STRING_ARRAY **默认取值**: 不涉及。

        :param inbound_token_claim_value_type: The inbound_token_claim_value_type of this CoreRunCustomClaimValidation.
        :type inbound_token_claim_value_type: str
        """
        self._inbound_token_claim_value_type = inbound_token_claim_value_type

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
        if not isinstance(other, CoreRunCustomClaimValidation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
