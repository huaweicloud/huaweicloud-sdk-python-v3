# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSAMLProviderV5Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'saml_provider': 'InlineResponse201SamlProvider'
    }

    attribute_map = {
        'saml_provider': 'saml_provider'
    }

    def __init__(self, saml_provider=None):
        r"""CreateSAMLProviderV5Response

        The model defined in huaweicloud sdk

        :param saml_provider: 
        :type saml_provider: :class:`huaweicloudsdkiam.v5.InlineResponse201SamlProvider`
        """
        
        super().__init__()

        self._saml_provider = None
        self.discriminator = None

        if saml_provider is not None:
            self.saml_provider = saml_provider

    @property
    def saml_provider(self):
        r"""Gets the saml_provider of this CreateSAMLProviderV5Response.

        :return: The saml_provider of this CreateSAMLProviderV5Response.
        :rtype: :class:`huaweicloudsdkiam.v5.InlineResponse201SamlProvider`
        """
        return self._saml_provider

    @saml_provider.setter
    def saml_provider(self, saml_provider):
        r"""Sets the saml_provider of this CreateSAMLProviderV5Response.

        :param saml_provider: The saml_provider of this CreateSAMLProviderV5Response.
        :type saml_provider: :class:`huaweicloudsdkiam.v5.InlineResponse201SamlProvider`
        """
        self._saml_provider = saml_provider

    def to_dict(self):
        import warnings
        warnings.warn("CreateSAMLProviderV5Response.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateSAMLProviderV5Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
