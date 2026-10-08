# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreGatewayTargetInferenceConfigurationModelMapping:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provider_prefix': 'CoreGatewayTargetInferenceConfigurationModelMappingProviderPrefix'
    }

    attribute_map = {
        'provider_prefix': 'provider_prefix'
    }

    def __init__(self, provider_prefix=None):
        r"""CoreGatewayTargetInferenceConfigurationModelMapping

        The model defined in huaweicloud sdk

        :param provider_prefix: 
        :type provider_prefix: :class:`huaweicloudsdkagentarts.v1.CoreGatewayTargetInferenceConfigurationModelMappingProviderPrefix`
        """
        
        

        self._provider_prefix = None
        self.discriminator = None

        if provider_prefix is not None:
            self.provider_prefix = provider_prefix

    @property
    def provider_prefix(self):
        r"""Gets the provider_prefix of this CoreGatewayTargetInferenceConfigurationModelMapping.

        :return: The provider_prefix of this CoreGatewayTargetInferenceConfigurationModelMapping.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayTargetInferenceConfigurationModelMappingProviderPrefix`
        """
        return self._provider_prefix

    @provider_prefix.setter
    def provider_prefix(self, provider_prefix):
        r"""Sets the provider_prefix of this CoreGatewayTargetInferenceConfigurationModelMapping.

        :param provider_prefix: The provider_prefix of this CoreGatewayTargetInferenceConfigurationModelMapping.
        :type provider_prefix: :class:`huaweicloudsdkagentarts.v1.CoreGatewayTargetInferenceConfigurationModelMappingProviderPrefix`
        """
        self._provider_prefix = provider_prefix

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
        if not isinstance(other, CoreGatewayTargetInferenceConfigurationModelMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
