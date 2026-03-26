# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EndpointConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ray_service_config': 'RayServiceConfig'
    }

    attribute_map = {
        'ray_service_config': 'ray_service_config'
    }

    def __init__(self, ray_service_config=None):
        r"""EndpointConfig

        The model defined in huaweicloud sdk

        :param ray_service_config: 
        :type ray_service_config: :class:`huaweicloudsdkdataartsfabric.v1.RayServiceConfig`
        """
        
        

        self._ray_service_config = None
        self.discriminator = None

        if ray_service_config is not None:
            self.ray_service_config = ray_service_config

    @property
    def ray_service_config(self):
        r"""Gets the ray_service_config of this EndpointConfig.

        :return: The ray_service_config of this EndpointConfig.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.RayServiceConfig`
        """
        return self._ray_service_config

    @ray_service_config.setter
    def ray_service_config(self, ray_service_config):
        r"""Sets the ray_service_config of this EndpointConfig.

        :param ray_service_config: The ray_service_config of this EndpointConfig.
        :type ray_service_config: :class:`huaweicloudsdkdataartsfabric.v1.RayServiceConfig`
        """
        self._ray_service_config = ray_service_config

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
        if not isinstance(other, EndpointConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
