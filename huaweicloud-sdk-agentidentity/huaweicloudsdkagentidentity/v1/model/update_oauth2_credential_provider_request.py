# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateOauth2CredentialProviderRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'credential_provider_name': 'str',
        'body': 'UpdateOauth2CredentialProviderReqBody'
    }

    attribute_map = {
        'credential_provider_name': 'credential_provider_name',
        'body': 'body'
    }

    def __init__(self, credential_provider_name=None, body=None):
        r"""UpdateOauth2CredentialProviderRequest

        The model defined in huaweicloud sdk

        :param credential_provider_name: The name of the credential provider.
        :type credential_provider_name: str
        :param body: Body of the UpdateOauth2CredentialProviderRequest
        :type body: :class:`huaweicloudsdkagentidentity.v1.UpdateOauth2CredentialProviderReqBody`
        """
        
        

        self._credential_provider_name = None
        self._body = None
        self.discriminator = None

        self.credential_provider_name = credential_provider_name
        if body is not None:
            self.body = body

    @property
    def credential_provider_name(self):
        r"""Gets the credential_provider_name of this UpdateOauth2CredentialProviderRequest.

        The name of the credential provider.

        :return: The credential_provider_name of this UpdateOauth2CredentialProviderRequest.
        :rtype: str
        """
        return self._credential_provider_name

    @credential_provider_name.setter
    def credential_provider_name(self, credential_provider_name):
        r"""Sets the credential_provider_name of this UpdateOauth2CredentialProviderRequest.

        The name of the credential provider.

        :param credential_provider_name: The credential_provider_name of this UpdateOauth2CredentialProviderRequest.
        :type credential_provider_name: str
        """
        self._credential_provider_name = credential_provider_name

    @property
    def body(self):
        r"""Gets the body of this UpdateOauth2CredentialProviderRequest.

        :return: The body of this UpdateOauth2CredentialProviderRequest.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.UpdateOauth2CredentialProviderReqBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateOauth2CredentialProviderRequest.

        :param body: The body of this UpdateOauth2CredentialProviderRequest.
        :type body: :class:`huaweicloudsdkagentidentity.v1.UpdateOauth2CredentialProviderReqBody`
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
        if not isinstance(other, UpdateOauth2CredentialProviderRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
