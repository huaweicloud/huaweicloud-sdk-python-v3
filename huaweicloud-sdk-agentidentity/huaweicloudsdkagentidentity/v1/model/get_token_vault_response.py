# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetTokenVaultResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'token_vault': 'TokenVault'
    }

    attribute_map = {
        'token_vault': 'token_vault'
    }

    def __init__(self, token_vault=None):
        r"""GetTokenVaultResponse

        The model defined in huaweicloud sdk

        :param token_vault: 
        :type token_vault: :class:`huaweicloudsdkagentidentity.v1.TokenVault`
        """
        
        super().__init__()

        self._token_vault = None
        self.discriminator = None

        if token_vault is not None:
            self.token_vault = token_vault

    @property
    def token_vault(self):
        r"""Gets the token_vault of this GetTokenVaultResponse.

        :return: The token_vault of this GetTokenVaultResponse.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.TokenVault`
        """
        return self._token_vault

    @token_vault.setter
    def token_vault(self, token_vault):
        r"""Sets the token_vault of this GetTokenVaultResponse.

        :param token_vault: The token_vault of this GetTokenVaultResponse.
        :type token_vault: :class:`huaweicloudsdkagentidentity.v1.TokenVault`
        """
        self._token_vault = token_vault

    def to_dict(self):
        import warnings
        warnings.warn("GetTokenVaultResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, GetTokenVaultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
