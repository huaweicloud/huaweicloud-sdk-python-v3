# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDomainConfigurationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configuration_id': 'str',
        'domain_name': 'str',
        'access_protocol': 'str',
        'server_certificate_id': 'str',
        'server_certificate_config': 'ServerCertificateConfig'
    }

    attribute_map = {
        'configuration_id': 'configuration_id',
        'domain_name': 'domain_name',
        'access_protocol': 'access_protocol',
        'server_certificate_id': 'server_certificate_id',
        'server_certificate_config': 'server_certificate_config'
    }

    def __init__(self, configuration_id=None, domain_name=None, access_protocol=None, server_certificate_id=None, server_certificate_config=None):
        r"""UpdateDomainConfigurationResponse

        The model defined in huaweicloud sdk

        :param configuration_id: 域配置唯一标识ID
        :type configuration_id: str
        :param domain_name: **参数说明**：自定义域名
        :type domain_name: str
        :param access_protocol: **参数说明**：应用协议场景，当前仅支持Device-MQTTS：设备接入MQTTS场景
        :type access_protocol: str
        :param server_certificate_id: **参数说明**：自定义服务端证书ID
        :type server_certificate_id: str
        :param server_certificate_config: 
        :type server_certificate_config: :class:`huaweicloudsdkiotda.v5.ServerCertificateConfig`
        """
        
        super().__init__()

        self._configuration_id = None
        self._domain_name = None
        self._access_protocol = None
        self._server_certificate_id = None
        self._server_certificate_config = None
        self.discriminator = None

        if configuration_id is not None:
            self.configuration_id = configuration_id
        if domain_name is not None:
            self.domain_name = domain_name
        if access_protocol is not None:
            self.access_protocol = access_protocol
        if server_certificate_id is not None:
            self.server_certificate_id = server_certificate_id
        if server_certificate_config is not None:
            self.server_certificate_config = server_certificate_config

    @property
    def configuration_id(self):
        r"""Gets the configuration_id of this UpdateDomainConfigurationResponse.

        域配置唯一标识ID

        :return: The configuration_id of this UpdateDomainConfigurationResponse.
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        r"""Sets the configuration_id of this UpdateDomainConfigurationResponse.

        域配置唯一标识ID

        :param configuration_id: The configuration_id of this UpdateDomainConfigurationResponse.
        :type configuration_id: str
        """
        self._configuration_id = configuration_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this UpdateDomainConfigurationResponse.

        **参数说明**：自定义域名

        :return: The domain_name of this UpdateDomainConfigurationResponse.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this UpdateDomainConfigurationResponse.

        **参数说明**：自定义域名

        :param domain_name: The domain_name of this UpdateDomainConfigurationResponse.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def access_protocol(self):
        r"""Gets the access_protocol of this UpdateDomainConfigurationResponse.

        **参数说明**：应用协议场景，当前仅支持Device-MQTTS：设备接入MQTTS场景

        :return: The access_protocol of this UpdateDomainConfigurationResponse.
        :rtype: str
        """
        return self._access_protocol

    @access_protocol.setter
    def access_protocol(self, access_protocol):
        r"""Sets the access_protocol of this UpdateDomainConfigurationResponse.

        **参数说明**：应用协议场景，当前仅支持Device-MQTTS：设备接入MQTTS场景

        :param access_protocol: The access_protocol of this UpdateDomainConfigurationResponse.
        :type access_protocol: str
        """
        self._access_protocol = access_protocol

    @property
    def server_certificate_id(self):
        r"""Gets the server_certificate_id of this UpdateDomainConfigurationResponse.

        **参数说明**：自定义服务端证书ID

        :return: The server_certificate_id of this UpdateDomainConfigurationResponse.
        :rtype: str
        """
        return self._server_certificate_id

    @server_certificate_id.setter
    def server_certificate_id(self, server_certificate_id):
        r"""Sets the server_certificate_id of this UpdateDomainConfigurationResponse.

        **参数说明**：自定义服务端证书ID

        :param server_certificate_id: The server_certificate_id of this UpdateDomainConfigurationResponse.
        :type server_certificate_id: str
        """
        self._server_certificate_id = server_certificate_id

    @property
    def server_certificate_config(self):
        r"""Gets the server_certificate_config of this UpdateDomainConfigurationResponse.

        :return: The server_certificate_config of this UpdateDomainConfigurationResponse.
        :rtype: :class:`huaweicloudsdkiotda.v5.ServerCertificateConfig`
        """
        return self._server_certificate_config

    @server_certificate_config.setter
    def server_certificate_config(self, server_certificate_config):
        r"""Sets the server_certificate_config of this UpdateDomainConfigurationResponse.

        :param server_certificate_config: The server_certificate_config of this UpdateDomainConfigurationResponse.
        :type server_certificate_config: :class:`huaweicloudsdkiotda.v5.ServerCertificateConfig`
        """
        self._server_certificate_config = server_certificate_config

    def to_dict(self):
        import warnings
        warnings.warn("UpdateDomainConfigurationResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdateDomainConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
