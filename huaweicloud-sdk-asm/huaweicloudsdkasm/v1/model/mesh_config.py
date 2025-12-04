# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MeshConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'proxy_config': 'ProxyConfig',
        'telemetry_config': 'TelemetryConfig'
    }

    attribute_map = {
        'proxy_config': 'proxyConfig',
        'telemetry_config': 'telemetryConfig'
    }

    def __init__(self, proxy_config=None, telemetry_config=None):
        r"""MeshConfig

        The model defined in huaweicloud sdk

        :param proxy_config: 
        :type proxy_config: :class:`huaweicloudsdkasm.v1.ProxyConfig`
        :param telemetry_config: 
        :type telemetry_config: :class:`huaweicloudsdkasm.v1.TelemetryConfig`
        """
        
        

        self._proxy_config = None
        self._telemetry_config = None
        self.discriminator = None

        if proxy_config is not None:
            self.proxy_config = proxy_config
        if telemetry_config is not None:
            self.telemetry_config = telemetry_config

    @property
    def proxy_config(self):
        r"""Gets the proxy_config of this MeshConfig.

        :return: The proxy_config of this MeshConfig.
        :rtype: :class:`huaweicloudsdkasm.v1.ProxyConfig`
        """
        return self._proxy_config

    @proxy_config.setter
    def proxy_config(self, proxy_config):
        r"""Sets the proxy_config of this MeshConfig.

        :param proxy_config: The proxy_config of this MeshConfig.
        :type proxy_config: :class:`huaweicloudsdkasm.v1.ProxyConfig`
        """
        self._proxy_config = proxy_config

    @property
    def telemetry_config(self):
        r"""Gets the telemetry_config of this MeshConfig.

        :return: The telemetry_config of this MeshConfig.
        :rtype: :class:`huaweicloudsdkasm.v1.TelemetryConfig`
        """
        return self._telemetry_config

    @telemetry_config.setter
    def telemetry_config(self, telemetry_config):
        r"""Sets the telemetry_config of this MeshConfig.

        :param telemetry_config: The telemetry_config of this MeshConfig.
        :type telemetry_config: :class:`huaweicloudsdkasm.v1.TelemetryConfig`
        """
        self._telemetry_config = telemetry_config

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
        if not isinstance(other, MeshConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
