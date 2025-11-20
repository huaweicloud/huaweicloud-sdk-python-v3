# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerCertificateConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ocsp_stapling_enable': 'bool',
        'ocsp_server_ca_id': 'str',
        'ocsp_ssl_enable': 'bool'
    }

    attribute_map = {
        'ocsp_stapling_enable': 'ocsp_stapling_enable',
        'ocsp_server_ca_id': 'ocsp_server_ca_id',
        'ocsp_ssl_enable': 'ocsp_ssl_enable'
    }

    def __init__(self, ocsp_stapling_enable=None, ocsp_server_ca_id=None, ocsp_ssl_enable=None):
        r"""ServerCertificateConfig

        The model defined in huaweicloud sdk

        :param ocsp_stapling_enable: 是否开启服务端OCSP装订
        :type ocsp_stapling_enable: bool
        :param ocsp_server_ca_id: ocsp服务器端CA证书id，仅当ocsp服务器为https协议时支持配置。
        :type ocsp_server_ca_id: str
        :param ocsp_ssl_enable: 访问ocsp服务器是否开启SSL
        :type ocsp_ssl_enable: bool
        """
        
        

        self._ocsp_stapling_enable = None
        self._ocsp_server_ca_id = None
        self._ocsp_ssl_enable = None
        self.discriminator = None

        if ocsp_stapling_enable is not None:
            self.ocsp_stapling_enable = ocsp_stapling_enable
        if ocsp_server_ca_id is not None:
            self.ocsp_server_ca_id = ocsp_server_ca_id
        if ocsp_ssl_enable is not None:
            self.ocsp_ssl_enable = ocsp_ssl_enable

    @property
    def ocsp_stapling_enable(self):
        r"""Gets the ocsp_stapling_enable of this ServerCertificateConfig.

        是否开启服务端OCSP装订

        :return: The ocsp_stapling_enable of this ServerCertificateConfig.
        :rtype: bool
        """
        return self._ocsp_stapling_enable

    @ocsp_stapling_enable.setter
    def ocsp_stapling_enable(self, ocsp_stapling_enable):
        r"""Sets the ocsp_stapling_enable of this ServerCertificateConfig.

        是否开启服务端OCSP装订

        :param ocsp_stapling_enable: The ocsp_stapling_enable of this ServerCertificateConfig.
        :type ocsp_stapling_enable: bool
        """
        self._ocsp_stapling_enable = ocsp_stapling_enable

    @property
    def ocsp_server_ca_id(self):
        r"""Gets the ocsp_server_ca_id of this ServerCertificateConfig.

        ocsp服务器端CA证书id，仅当ocsp服务器为https协议时支持配置。

        :return: The ocsp_server_ca_id of this ServerCertificateConfig.
        :rtype: str
        """
        return self._ocsp_server_ca_id

    @ocsp_server_ca_id.setter
    def ocsp_server_ca_id(self, ocsp_server_ca_id):
        r"""Sets the ocsp_server_ca_id of this ServerCertificateConfig.

        ocsp服务器端CA证书id，仅当ocsp服务器为https协议时支持配置。

        :param ocsp_server_ca_id: The ocsp_server_ca_id of this ServerCertificateConfig.
        :type ocsp_server_ca_id: str
        """
        self._ocsp_server_ca_id = ocsp_server_ca_id

    @property
    def ocsp_ssl_enable(self):
        r"""Gets the ocsp_ssl_enable of this ServerCertificateConfig.

        访问ocsp服务器是否开启SSL

        :return: The ocsp_ssl_enable of this ServerCertificateConfig.
        :rtype: bool
        """
        return self._ocsp_ssl_enable

    @ocsp_ssl_enable.setter
    def ocsp_ssl_enable(self, ocsp_ssl_enable):
        r"""Sets the ocsp_ssl_enable of this ServerCertificateConfig.

        访问ocsp服务器是否开启SSL

        :param ocsp_ssl_enable: The ocsp_ssl_enable of this ServerCertificateConfig.
        :type ocsp_ssl_enable: bool
        """
        self._ocsp_ssl_enable = ocsp_ssl_enable

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
        if not isinstance(other, ServerCertificateConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
