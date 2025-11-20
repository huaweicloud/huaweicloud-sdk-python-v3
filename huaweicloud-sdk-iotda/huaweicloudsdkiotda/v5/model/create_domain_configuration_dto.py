# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDomainConfigurationDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'access_protocol': 'str',
        'server_certificate_id': 'str',
        'server_certificate_config': 'ServerCertificateConfig'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'access_protocol': 'access_protocol',
        'server_certificate_id': 'server_certificate_id',
        'server_certificate_config': 'server_certificate_config'
    }

    def __init__(self, domain_name=None, access_protocol=None, server_certificate_id=None, server_certificate_config=None):
        r"""CreateDomainConfigurationDTO

        The model defined in huaweicloud sdk

        :param domain_name: **参数说明**：自定义域名
        :type domain_name: str
        :param access_protocol: **参数说明**：接入协议，当前仅支持Device-MQTTS：设备接入MQTTS场景
        :type access_protocol: str
        :param server_certificate_id: **参数说明**：自定义服务端证书ID
        :type server_certificate_id: str
        :param server_certificate_config: 
        :type server_certificate_config: :class:`huaweicloudsdkiotda.v5.ServerCertificateConfig`
        """
        
        

        self._domain_name = None
        self._access_protocol = None
        self._server_certificate_id = None
        self._server_certificate_config = None
        self.discriminator = None

        self.domain_name = domain_name
        self.access_protocol = access_protocol
        self.server_certificate_id = server_certificate_id
        if server_certificate_config is not None:
            self.server_certificate_config = server_certificate_config

    @property
    def domain_name(self):
        r"""Gets the domain_name of this CreateDomainConfigurationDTO.

        **参数说明**：自定义域名

        :return: The domain_name of this CreateDomainConfigurationDTO.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this CreateDomainConfigurationDTO.

        **参数说明**：自定义域名

        :param domain_name: The domain_name of this CreateDomainConfigurationDTO.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def access_protocol(self):
        r"""Gets the access_protocol of this CreateDomainConfigurationDTO.

        **参数说明**：接入协议，当前仅支持Device-MQTTS：设备接入MQTTS场景

        :return: The access_protocol of this CreateDomainConfigurationDTO.
        :rtype: str
        """
        return self._access_protocol

    @access_protocol.setter
    def access_protocol(self, access_protocol):
        r"""Sets the access_protocol of this CreateDomainConfigurationDTO.

        **参数说明**：接入协议，当前仅支持Device-MQTTS：设备接入MQTTS场景

        :param access_protocol: The access_protocol of this CreateDomainConfigurationDTO.
        :type access_protocol: str
        """
        self._access_protocol = access_protocol

    @property
    def server_certificate_id(self):
        r"""Gets the server_certificate_id of this CreateDomainConfigurationDTO.

        **参数说明**：自定义服务端证书ID

        :return: The server_certificate_id of this CreateDomainConfigurationDTO.
        :rtype: str
        """
        return self._server_certificate_id

    @server_certificate_id.setter
    def server_certificate_id(self, server_certificate_id):
        r"""Sets the server_certificate_id of this CreateDomainConfigurationDTO.

        **参数说明**：自定义服务端证书ID

        :param server_certificate_id: The server_certificate_id of this CreateDomainConfigurationDTO.
        :type server_certificate_id: str
        """
        self._server_certificate_id = server_certificate_id

    @property
    def server_certificate_config(self):
        r"""Gets the server_certificate_config of this CreateDomainConfigurationDTO.

        :return: The server_certificate_config of this CreateDomainConfigurationDTO.
        :rtype: :class:`huaweicloudsdkiotda.v5.ServerCertificateConfig`
        """
        return self._server_certificate_config

    @server_certificate_config.setter
    def server_certificate_config(self, server_certificate_config):
        r"""Sets the server_certificate_config of this CreateDomainConfigurationDTO.

        :param server_certificate_config: The server_certificate_config of this CreateDomainConfigurationDTO.
        :type server_certificate_config: :class:`huaweicloudsdkiotda.v5.ServerCertificateConfig`
        """
        self._server_certificate_config = server_certificate_config

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
        if not isinstance(other, CreateDomainConfigurationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
