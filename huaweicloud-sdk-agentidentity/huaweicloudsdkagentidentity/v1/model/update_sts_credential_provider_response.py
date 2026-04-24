# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateStsCredentialProviderResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'credential_provider': 'StsCredentialProvider'
    }

    attribute_map = {
        'credential_provider': 'credential_provider'
    }

    def __init__(self, credential_provider=None):
        r"""UpdateStsCredentialProviderResponse

        The model defined in huaweicloud sdk

        :param credential_provider: 
        :type credential_provider: :class:`huaweicloudsdkagentidentity.v1.StsCredentialProvider`
        """
        
        super().__init__()

        self._credential_provider = None
        self.discriminator = None

        if credential_provider is not None:
            self.credential_provider = credential_provider

    @property
    def credential_provider(self):
        r"""Gets the credential_provider of this UpdateStsCredentialProviderResponse.

        :return: The credential_provider of this UpdateStsCredentialProviderResponse.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.StsCredentialProvider`
        """
        return self._credential_provider

    @credential_provider.setter
    def credential_provider(self, credential_provider):
        r"""Sets the credential_provider of this UpdateStsCredentialProviderResponse.

        :param credential_provider: The credential_provider of this UpdateStsCredentialProviderResponse.
        :type credential_provider: :class:`huaweicloudsdkagentidentity.v1.StsCredentialProvider`
        """
        self._credential_provider = credential_provider

    def to_dict(self):
        import warnings
        warnings.warn("UpdateStsCredentialProviderResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdateStsCredentialProviderResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
