# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateServerRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tunnel_protocol': 'str',
        'client_cidr': 'str',
        'local_subnets': 'list[str]',
        'client_auth_type': 'str',
        'server_certificate': 'CreateServerRequestServerCertificate',
        'client_ca_certificates': 'list[CreateServerRequestClientCaCertificates]',
        'ssl_options': 'CreateServerRequestSslOptions'
    }

    attribute_map = {
        'tunnel_protocol': 'tunnel_protocol',
        'client_cidr': 'client_cidr',
        'local_subnets': 'local_subnets',
        'client_auth_type': 'client_auth_type',
        'server_certificate': 'server_certificate',
        'client_ca_certificates': 'client_ca_certificates',
        'ssl_options': 'ssl_options'
    }

    def __init__(self, tunnel_protocol=None, client_cidr=None, local_subnets=None, client_auth_type=None, server_certificate=None, client_ca_certificates=None, ssl_options=None):
        """CreateServerRequest

        The model defined in huaweicloud sdk

        :param tunnel_protocol: 隧道协议类型
        :type tunnel_protocol: str
        :param client_cidr: 客户端网段
        :type client_cidr: str
        :param local_subnets: 本端网段列表，至少有一个本端网段
        :type local_subnets: list[str]
        :param client_auth_type: 客户端认证类型
        :type client_auth_type: str
        :param server_certificate: 
        :type server_certificate: :class:`huaweicloudsdkvpn.v5.CreateServerRequestServerCertificate`
        :param client_ca_certificates: 客户端证书列表。隧道协议类型是SSL且认证方式是证书认证时，必填
        :type client_ca_certificates: list[:class:`huaweicloudsdkvpn.v5.CreateServerRequestClientCaCertificates`]
        :param ssl_options: 
        :type ssl_options: :class:`huaweicloudsdkvpn.v5.CreateServerRequestSslOptions`
        """
        
        

        self._tunnel_protocol = None
        self._client_cidr = None
        self._local_subnets = None
        self._client_auth_type = None
        self._server_certificate = None
        self._client_ca_certificates = None
        self._ssl_options = None
        self.discriminator = None

        self.tunnel_protocol = tunnel_protocol
        self.client_cidr = client_cidr
        self.local_subnets = local_subnets
        self.client_auth_type = client_auth_type
        if server_certificate is not None:
            self.server_certificate = server_certificate
        if client_ca_certificates is not None:
            self.client_ca_certificates = client_ca_certificates
        if ssl_options is not None:
            self.ssl_options = ssl_options

    @property
    def tunnel_protocol(self):
        """Gets the tunnel_protocol of this CreateServerRequest.

        隧道协议类型

        :return: The tunnel_protocol of this CreateServerRequest.
        :rtype: str
        """
        return self._tunnel_protocol

    @tunnel_protocol.setter
    def tunnel_protocol(self, tunnel_protocol):
        """Sets the tunnel_protocol of this CreateServerRequest.

        隧道协议类型

        :param tunnel_protocol: The tunnel_protocol of this CreateServerRequest.
        :type tunnel_protocol: str
        """
        self._tunnel_protocol = tunnel_protocol

    @property
    def client_cidr(self):
        """Gets the client_cidr of this CreateServerRequest.

        客户端网段

        :return: The client_cidr of this CreateServerRequest.
        :rtype: str
        """
        return self._client_cidr

    @client_cidr.setter
    def client_cidr(self, client_cidr):
        """Sets the client_cidr of this CreateServerRequest.

        客户端网段

        :param client_cidr: The client_cidr of this CreateServerRequest.
        :type client_cidr: str
        """
        self._client_cidr = client_cidr

    @property
    def local_subnets(self):
        """Gets the local_subnets of this CreateServerRequest.

        本端网段列表，至少有一个本端网段

        :return: The local_subnets of this CreateServerRequest.
        :rtype: list[str]
        """
        return self._local_subnets

    @local_subnets.setter
    def local_subnets(self, local_subnets):
        """Sets the local_subnets of this CreateServerRequest.

        本端网段列表，至少有一个本端网段

        :param local_subnets: The local_subnets of this CreateServerRequest.
        :type local_subnets: list[str]
        """
        self._local_subnets = local_subnets

    @property
    def client_auth_type(self):
        """Gets the client_auth_type of this CreateServerRequest.

        客户端认证类型

        :return: The client_auth_type of this CreateServerRequest.
        :rtype: str
        """
        return self._client_auth_type

    @client_auth_type.setter
    def client_auth_type(self, client_auth_type):
        """Sets the client_auth_type of this CreateServerRequest.

        客户端认证类型

        :param client_auth_type: The client_auth_type of this CreateServerRequest.
        :type client_auth_type: str
        """
        self._client_auth_type = client_auth_type

    @property
    def server_certificate(self):
        """Gets the server_certificate of this CreateServerRequest.

        :return: The server_certificate of this CreateServerRequest.
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateServerRequestServerCertificate`
        """
        return self._server_certificate

    @server_certificate.setter
    def server_certificate(self, server_certificate):
        """Sets the server_certificate of this CreateServerRequest.

        :param server_certificate: The server_certificate of this CreateServerRequest.
        :type server_certificate: :class:`huaweicloudsdkvpn.v5.CreateServerRequestServerCertificate`
        """
        self._server_certificate = server_certificate

    @property
    def client_ca_certificates(self):
        """Gets the client_ca_certificates of this CreateServerRequest.

        客户端证书列表。隧道协议类型是SSL且认证方式是证书认证时，必填

        :return: The client_ca_certificates of this CreateServerRequest.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.CreateServerRequestClientCaCertificates`]
        """
        return self._client_ca_certificates

    @client_ca_certificates.setter
    def client_ca_certificates(self, client_ca_certificates):
        """Sets the client_ca_certificates of this CreateServerRequest.

        客户端证书列表。隧道协议类型是SSL且认证方式是证书认证时，必填

        :param client_ca_certificates: The client_ca_certificates of this CreateServerRequest.
        :type client_ca_certificates: list[:class:`huaweicloudsdkvpn.v5.CreateServerRequestClientCaCertificates`]
        """
        self._client_ca_certificates = client_ca_certificates

    @property
    def ssl_options(self):
        """Gets the ssl_options of this CreateServerRequest.

        :return: The ssl_options of this CreateServerRequest.
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateServerRequestSslOptions`
        """
        return self._ssl_options

    @ssl_options.setter
    def ssl_options(self, ssl_options):
        """Sets the ssl_options of this CreateServerRequest.

        :param ssl_options: The ssl_options of this CreateServerRequest.
        :type ssl_options: :class:`huaweicloudsdkvpn.v5.CreateServerRequestSslOptions`
        """
        self._ssl_options = ssl_options

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
        if not isinstance(other, CreateServerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
