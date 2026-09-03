# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTokenVaultRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'token_vault_id': 'str',
        'body': 'UpdateTokenVaultReqBody'
    }

    attribute_map = {
        'token_vault_id': 'token_vault_id',
        'body': 'body'
    }

    def __init__(self, token_vault_id=None, body=None):
        r"""UpdateTokenVaultRequest

        The model defined in huaweicloud sdk

        :param token_vault_id: The unique identifier of the token vault.
        :type token_vault_id: str
        :param body: Body of the UpdateTokenVaultRequest
        :type body: :class:`huaweicloudsdkagentidentity.v1.UpdateTokenVaultReqBody`
        """
        
        

        self._token_vault_id = None
        self._body = None
        self.discriminator = None

        self.token_vault_id = token_vault_id
        if body is not None:
            self.body = body

    @property
    def token_vault_id(self):
        r"""Gets the token_vault_id of this UpdateTokenVaultRequest.

        The unique identifier of the token vault.

        :return: The token_vault_id of this UpdateTokenVaultRequest.
        :rtype: str
        """
        return self._token_vault_id

    @token_vault_id.setter
    def token_vault_id(self, token_vault_id):
        r"""Sets the token_vault_id of this UpdateTokenVaultRequest.

        The unique identifier of the token vault.

        :param token_vault_id: The token_vault_id of this UpdateTokenVaultRequest.
        :type token_vault_id: str
        """
        self._token_vault_id = token_vault_id

    @property
    def body(self):
        r"""Gets the body of this UpdateTokenVaultRequest.

        :return: The body of this UpdateTokenVaultRequest.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.UpdateTokenVaultReqBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateTokenVaultRequest.

        :param body: The body of this UpdateTokenVaultRequest.
        :type body: :class:`huaweicloudsdkagentidentity.v1.UpdateTokenVaultReqBody`
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
        if not isinstance(other, UpdateTokenVaultRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
