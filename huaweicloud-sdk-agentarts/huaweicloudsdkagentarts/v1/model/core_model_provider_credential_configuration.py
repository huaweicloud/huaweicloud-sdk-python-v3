# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreModelProviderCredentialConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provider_configuration': 'CoreModelProviderCredentialProviderConfiguration'
    }

    attribute_map = {
        'provider_configuration': 'provider_configuration'
    }

    def __init__(self, provider_configuration=None):
        r"""CoreModelProviderCredentialConfiguration

        The model defined in huaweicloud sdk

        :param provider_configuration: 
        :type provider_configuration: :class:`huaweicloudsdkagentarts.v1.CoreModelProviderCredentialProviderConfiguration`
        """
        
        

        self._provider_configuration = None
        self.discriminator = None

        if provider_configuration is not None:
            self.provider_configuration = provider_configuration

    @property
    def provider_configuration(self):
        r"""Gets the provider_configuration of this CoreModelProviderCredentialConfiguration.

        :return: The provider_configuration of this CoreModelProviderCredentialConfiguration.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreModelProviderCredentialProviderConfiguration`
        """
        return self._provider_configuration

    @provider_configuration.setter
    def provider_configuration(self, provider_configuration):
        r"""Sets the provider_configuration of this CoreModelProviderCredentialConfiguration.

        :param provider_configuration: The provider_configuration of this CoreModelProviderCredentialConfiguration.
        :type provider_configuration: :class:`huaweicloudsdkagentarts.v1.CoreModelProviderCredentialProviderConfiguration`
        """
        self._provider_configuration = provider_configuration

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
        if not isinstance(other, CoreModelProviderCredentialConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
