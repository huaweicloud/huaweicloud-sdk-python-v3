# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowServerResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'p2c_vgw_id': 'str',
        'client_cidr': 'str',
        'local_subnets': 'list[str]',
        'client_auth_type': 'str',
        'tunnel_protocol': 'str',
        'server_certificate': 'ShowServerResponseServerCertificate',
        'client_ca_certificates': 'list[QueryClientCaCertificateBody]',
        'ssl_options': 'ShowServerResponseSslOptions',
        'status': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'p2c_vgw_id': 'p2c_vgw_id',
        'client_cidr': 'client_cidr',
        'local_subnets': 'local_subnets',
        'client_auth_type': 'client_auth_type',
        'tunnel_protocol': 'tunnel_protocol',
        'server_certificate': 'server_certificate',
        'client_ca_certificates': 'client_ca_certificates',
        'ssl_options': 'ssl_options',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, p2c_vgw_id=None, client_cidr=None, local_subnets=None, client_auth_type=None, tunnel_protocol=None, server_certificate=None, client_ca_certificates=None, ssl_options=None, status=None, created_at=None, updated_at=None):
        """ShowServerResponse

        The model defined in huaweicloud sdk

        :param id: 服务端 ID
        :type id: str
        :param p2c_vgw_id: P2C VPN 网关 ID
        :type p2c_vgw_id: str
        :param client_cidr: 客户端网段
        :type client_cidr: str
        :param local_subnets: 本端网段列表
        :type local_subnets: list[str]
        :param client_auth_type: 客户端认证类型
        :type client_auth_type: str
        :param tunnel_protocol: 隧道协议类型
        :type tunnel_protocol: str
        :param server_certificate: 
        :type server_certificate: :class:`huaweicloudsdkvpn.v5.ShowServerResponseServerCertificate`
        :param client_ca_certificates: 
        :type client_ca_certificates: list[:class:`huaweicloudsdkvpn.v5.QueryClientCaCertificateBody`]
        :param ssl_options: 
        :type ssl_options: :class:`huaweicloudsdkvpn.v5.ShowServerResponseSslOptions`
        :param status: 服务端状态
        :type status: str
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._p2c_vgw_id = None
        self._client_cidr = None
        self._local_subnets = None
        self._client_auth_type = None
        self._tunnel_protocol = None
        self._server_certificate = None
        self._client_ca_certificates = None
        self._ssl_options = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if p2c_vgw_id is not None:
            self.p2c_vgw_id = p2c_vgw_id
        if client_cidr is not None:
            self.client_cidr = client_cidr
        if local_subnets is not None:
            self.local_subnets = local_subnets
        if client_auth_type is not None:
            self.client_auth_type = client_auth_type
        if tunnel_protocol is not None:
            self.tunnel_protocol = tunnel_protocol
        if server_certificate is not None:
            self.server_certificate = server_certificate
        if client_ca_certificates is not None:
            self.client_ca_certificates = client_ca_certificates
        if ssl_options is not None:
            self.ssl_options = ssl_options
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this ShowServerResponse.

        服务端 ID

        :return: The id of this ShowServerResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowServerResponse.

        服务端 ID

        :param id: The id of this ShowServerResponse.
        :type id: str
        """
        self._id = id

    @property
    def p2c_vgw_id(self):
        """Gets the p2c_vgw_id of this ShowServerResponse.

        P2C VPN 网关 ID

        :return: The p2c_vgw_id of this ShowServerResponse.
        :rtype: str
        """
        return self._p2c_vgw_id

    @p2c_vgw_id.setter
    def p2c_vgw_id(self, p2c_vgw_id):
        """Sets the p2c_vgw_id of this ShowServerResponse.

        P2C VPN 网关 ID

        :param p2c_vgw_id: The p2c_vgw_id of this ShowServerResponse.
        :type p2c_vgw_id: str
        """
        self._p2c_vgw_id = p2c_vgw_id

    @property
    def client_cidr(self):
        """Gets the client_cidr of this ShowServerResponse.

        客户端网段

        :return: The client_cidr of this ShowServerResponse.
        :rtype: str
        """
        return self._client_cidr

    @client_cidr.setter
    def client_cidr(self, client_cidr):
        """Sets the client_cidr of this ShowServerResponse.

        客户端网段

        :param client_cidr: The client_cidr of this ShowServerResponse.
        :type client_cidr: str
        """
        self._client_cidr = client_cidr

    @property
    def local_subnets(self):
        """Gets the local_subnets of this ShowServerResponse.

        本端网段列表

        :return: The local_subnets of this ShowServerResponse.
        :rtype: list[str]
        """
        return self._local_subnets

    @local_subnets.setter
    def local_subnets(self, local_subnets):
        """Sets the local_subnets of this ShowServerResponse.

        本端网段列表

        :param local_subnets: The local_subnets of this ShowServerResponse.
        :type local_subnets: list[str]
        """
        self._local_subnets = local_subnets

    @property
    def client_auth_type(self):
        """Gets the client_auth_type of this ShowServerResponse.

        客户端认证类型

        :return: The client_auth_type of this ShowServerResponse.
        :rtype: str
        """
        return self._client_auth_type

    @client_auth_type.setter
    def client_auth_type(self, client_auth_type):
        """Sets the client_auth_type of this ShowServerResponse.

        客户端认证类型

        :param client_auth_type: The client_auth_type of this ShowServerResponse.
        :type client_auth_type: str
        """
        self._client_auth_type = client_auth_type

    @property
    def tunnel_protocol(self):
        """Gets the tunnel_protocol of this ShowServerResponse.

        隧道协议类型

        :return: The tunnel_protocol of this ShowServerResponse.
        :rtype: str
        """
        return self._tunnel_protocol

    @tunnel_protocol.setter
    def tunnel_protocol(self, tunnel_protocol):
        """Sets the tunnel_protocol of this ShowServerResponse.

        隧道协议类型

        :param tunnel_protocol: The tunnel_protocol of this ShowServerResponse.
        :type tunnel_protocol: str
        """
        self._tunnel_protocol = tunnel_protocol

    @property
    def server_certificate(self):
        """Gets the server_certificate of this ShowServerResponse.

        :return: The server_certificate of this ShowServerResponse.
        :rtype: :class:`huaweicloudsdkvpn.v5.ShowServerResponseServerCertificate`
        """
        return self._server_certificate

    @server_certificate.setter
    def server_certificate(self, server_certificate):
        """Sets the server_certificate of this ShowServerResponse.

        :param server_certificate: The server_certificate of this ShowServerResponse.
        :type server_certificate: :class:`huaweicloudsdkvpn.v5.ShowServerResponseServerCertificate`
        """
        self._server_certificate = server_certificate

    @property
    def client_ca_certificates(self):
        """Gets the client_ca_certificates of this ShowServerResponse.

        :return: The client_ca_certificates of this ShowServerResponse.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.QueryClientCaCertificateBody`]
        """
        return self._client_ca_certificates

    @client_ca_certificates.setter
    def client_ca_certificates(self, client_ca_certificates):
        """Sets the client_ca_certificates of this ShowServerResponse.

        :param client_ca_certificates: The client_ca_certificates of this ShowServerResponse.
        :type client_ca_certificates: list[:class:`huaweicloudsdkvpn.v5.QueryClientCaCertificateBody`]
        """
        self._client_ca_certificates = client_ca_certificates

    @property
    def ssl_options(self):
        """Gets the ssl_options of this ShowServerResponse.

        :return: The ssl_options of this ShowServerResponse.
        :rtype: :class:`huaweicloudsdkvpn.v5.ShowServerResponseSslOptions`
        """
        return self._ssl_options

    @ssl_options.setter
    def ssl_options(self, ssl_options):
        """Sets the ssl_options of this ShowServerResponse.

        :param ssl_options: The ssl_options of this ShowServerResponse.
        :type ssl_options: :class:`huaweicloudsdkvpn.v5.ShowServerResponseSslOptions`
        """
        self._ssl_options = ssl_options

    @property
    def status(self):
        """Gets the status of this ShowServerResponse.

        服务端状态

        :return: The status of this ShowServerResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowServerResponse.

        服务端状态

        :param status: The status of this ShowServerResponse.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this ShowServerResponse.

        创建时间

        :return: The created_at of this ShowServerResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ShowServerResponse.

        创建时间

        :param created_at: The created_at of this ShowServerResponse.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ShowServerResponse.

        更新时间

        :return: The updated_at of this ShowServerResponse.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ShowServerResponse.

        更新时间

        :param updated_at: The updated_at of this ShowServerResponse.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, ShowServerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
