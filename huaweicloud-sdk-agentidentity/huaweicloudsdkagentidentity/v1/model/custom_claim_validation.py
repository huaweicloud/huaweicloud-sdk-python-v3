# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomClaimValidation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'authorizing_claim_match_value': 'AuthorizingClaimMatchValue',
        'inbound_token_claim_name': 'str',
        'inbound_token_claim_value_type': 'str'
    }

    attribute_map = {
        'authorizing_claim_match_value': 'authorizing_claim_match_value',
        'inbound_token_claim_name': 'inbound_token_claim_name',
        'inbound_token_claim_value_type': 'inbound_token_claim_value_type'
    }

    def __init__(self, authorizing_claim_match_value=None, inbound_token_claim_name=None, inbound_token_claim_value_type=None):
        r"""CustomClaimValidation

        The model defined in huaweicloud sdk

        :param authorizing_claim_match_value: 
        :type authorizing_claim_match_value: :class:`huaweicloudsdkagentidentity.v1.AuthorizingClaimMatchValue`
        :param inbound_token_claim_name: The name of the custom claim field to check.
        :type inbound_token_claim_name: str
        :param inbound_token_claim_value_type: The data type of the claim value to check for.
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
        r"""Gets the authorizing_claim_match_value of this CustomClaimValidation.

        :return: The authorizing_claim_match_value of this CustomClaimValidation.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.AuthorizingClaimMatchValue`
        """
        return self._authorizing_claim_match_value

    @authorizing_claim_match_value.setter
    def authorizing_claim_match_value(self, authorizing_claim_match_value):
        r"""Sets the authorizing_claim_match_value of this CustomClaimValidation.

        :param authorizing_claim_match_value: The authorizing_claim_match_value of this CustomClaimValidation.
        :type authorizing_claim_match_value: :class:`huaweicloudsdkagentidentity.v1.AuthorizingClaimMatchValue`
        """
        self._authorizing_claim_match_value = authorizing_claim_match_value

    @property
    def inbound_token_claim_name(self):
        r"""Gets the inbound_token_claim_name of this CustomClaimValidation.

        The name of the custom claim field to check.

        :return: The inbound_token_claim_name of this CustomClaimValidation.
        :rtype: str
        """
        return self._inbound_token_claim_name

    @inbound_token_claim_name.setter
    def inbound_token_claim_name(self, inbound_token_claim_name):
        r"""Sets the inbound_token_claim_name of this CustomClaimValidation.

        The name of the custom claim field to check.

        :param inbound_token_claim_name: The inbound_token_claim_name of this CustomClaimValidation.
        :type inbound_token_claim_name: str
        """
        self._inbound_token_claim_name = inbound_token_claim_name

    @property
    def inbound_token_claim_value_type(self):
        r"""Gets the inbound_token_claim_value_type of this CustomClaimValidation.

        The data type of the claim value to check for.

        :return: The inbound_token_claim_value_type of this CustomClaimValidation.
        :rtype: str
        """
        return self._inbound_token_claim_value_type

    @inbound_token_claim_value_type.setter
    def inbound_token_claim_value_type(self, inbound_token_claim_value_type):
        r"""Sets the inbound_token_claim_value_type of this CustomClaimValidation.

        The data type of the claim value to check for.

        :param inbound_token_claim_value_type: The inbound_token_claim_value_type of this CustomClaimValidation.
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
        if not isinstance(other, CustomClaimValidation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
