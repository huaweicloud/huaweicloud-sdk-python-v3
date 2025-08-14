# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateApplicationInstanceServiceProviderConfigurationReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_provider_config': 'ServiceProviderConfigDto'
    }

    attribute_map = {
        'service_provider_config': 'service_provider_config'
    }

    def __init__(self, service_provider_config=None):
        r"""UpdateApplicationInstanceServiceProviderConfigurationReqBody

        The model defined in huaweicloud sdk

        :param service_provider_config: 
        :type service_provider_config: :class:`huaweicloudsdkidentitycenter.v1.ServiceProviderConfigDto`
        """
        
        

        self._service_provider_config = None
        self.discriminator = None

        self.service_provider_config = service_provider_config

    @property
    def service_provider_config(self):
        r"""Gets the service_provider_config of this UpdateApplicationInstanceServiceProviderConfigurationReqBody.

        :return: The service_provider_config of this UpdateApplicationInstanceServiceProviderConfigurationReqBody.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ServiceProviderConfigDto`
        """
        return self._service_provider_config

    @service_provider_config.setter
    def service_provider_config(self, service_provider_config):
        r"""Sets the service_provider_config of this UpdateApplicationInstanceServiceProviderConfigurationReqBody.

        :param service_provider_config: The service_provider_config of this UpdateApplicationInstanceServiceProviderConfigurationReqBody.
        :type service_provider_config: :class:`huaweicloudsdkidentitycenter.v1.ServiceProviderConfigDto`
        """
        self._service_provider_config = service_provider_config

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateApplicationInstanceServiceProviderConfigurationReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
