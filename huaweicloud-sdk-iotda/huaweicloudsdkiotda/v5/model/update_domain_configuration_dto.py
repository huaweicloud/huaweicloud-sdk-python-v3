# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDomainConfigurationDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_certificate_id': 'str',
        'server_certificate_config': 'ServerCertificateConfig'
    }

    attribute_map = {
        'server_certificate_id': 'server_certificate_id',
        'server_certificate_config': 'server_certificate_config'
    }

    def __init__(self, server_certificate_id=None, server_certificate_config=None):
        r"""UpdateDomainConfigurationDTO

        The model defined in huaweicloud sdk

        :param server_certificate_id: **参数说明**：自定义服务端证书ID
        :type server_certificate_id: str
        :param server_certificate_config: 
        :type server_certificate_config: :class:`huaweicloudsdkiotda.v5.ServerCertificateConfig`
        """
        
        

        self._server_certificate_id = None
        self._server_certificate_config = None
        self.discriminator = None

        if server_certificate_id is not None:
            self.server_certificate_id = server_certificate_id
        if server_certificate_config is not None:
            self.server_certificate_config = server_certificate_config

    @property
    def server_certificate_id(self):
        r"""Gets the server_certificate_id of this UpdateDomainConfigurationDTO.

        **参数说明**：自定义服务端证书ID

        :return: The server_certificate_id of this UpdateDomainConfigurationDTO.
        :rtype: str
        """
        return self._server_certificate_id

    @server_certificate_id.setter
    def server_certificate_id(self, server_certificate_id):
        r"""Sets the server_certificate_id of this UpdateDomainConfigurationDTO.

        **参数说明**：自定义服务端证书ID

        :param server_certificate_id: The server_certificate_id of this UpdateDomainConfigurationDTO.
        :type server_certificate_id: str
        """
        self._server_certificate_id = server_certificate_id

    @property
    def server_certificate_config(self):
        r"""Gets the server_certificate_config of this UpdateDomainConfigurationDTO.

        :return: The server_certificate_config of this UpdateDomainConfigurationDTO.
        :rtype: :class:`huaweicloudsdkiotda.v5.ServerCertificateConfig`
        """
        return self._server_certificate_config

    @server_certificate_config.setter
    def server_certificate_config(self, server_certificate_config):
        r"""Sets the server_certificate_config of this UpdateDomainConfigurationDTO.

        :param server_certificate_config: The server_certificate_config of this UpdateDomainConfigurationDTO.
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
        if not isinstance(other, UpdateDomainConfigurationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
