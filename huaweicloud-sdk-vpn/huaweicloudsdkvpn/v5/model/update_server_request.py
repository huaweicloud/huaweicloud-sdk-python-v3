# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateServerRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'client_cidr': 'str',
        'local_subnets': 'list[str]',
        'server_certificate': 'UpdateServerRequestServerCertificate',
        'ssl_options': 'UpdateServerRequestSslOptions',
        'client_auth_type': 'str'
    }

    attribute_map = {
        'client_cidr': 'client_cidr',
        'local_subnets': 'local_subnets',
        'server_certificate': 'server_certificate',
        'ssl_options': 'ssl_options',
        'client_auth_type': 'client_auth_type'
    }

    def __init__(self, client_cidr=None, local_subnets=None, server_certificate=None, ssl_options=None, client_auth_type=None):
        """UpdateServerRequest

        The model defined in huaweicloud sdk

        :param client_cidr: 客户端网段
        :type client_cidr: str
        :param local_subnets: 本端网段列表,至少有一个本端网段
        :type local_subnets: list[str]
        :param server_certificate: 
        :type server_certificate: :class:`huaweicloudsdkvpn.v5.UpdateServerRequestServerCertificate`
        :param ssl_options: 
        :type ssl_options: :class:`huaweicloudsdkvpn.v5.UpdateServerRequestSslOptions`
        :param client_auth_type: 客户端认证类型
        :type client_auth_type: str
        """
        
        

        self._client_cidr = None
        self._local_subnets = None
        self._server_certificate = None
        self._ssl_options = None
        self._client_auth_type = None
        self.discriminator = None

        if client_cidr is not None:
            self.client_cidr = client_cidr
        if local_subnets is not None:
            self.local_subnets = local_subnets
        if server_certificate is not None:
            self.server_certificate = server_certificate
        if ssl_options is not None:
            self.ssl_options = ssl_options
        if client_auth_type is not None:
            self.client_auth_type = client_auth_type

    @property
    def client_cidr(self):
        """Gets the client_cidr of this UpdateServerRequest.

        客户端网段

        :return: The client_cidr of this UpdateServerRequest.
        :rtype: str
        """
        return self._client_cidr

    @client_cidr.setter
    def client_cidr(self, client_cidr):
        """Sets the client_cidr of this UpdateServerRequest.

        客户端网段

        :param client_cidr: The client_cidr of this UpdateServerRequest.
        :type client_cidr: str
        """
        self._client_cidr = client_cidr

    @property
    def local_subnets(self):
        """Gets the local_subnets of this UpdateServerRequest.

        本端网段列表,至少有一个本端网段

        :return: The local_subnets of this UpdateServerRequest.
        :rtype: list[str]
        """
        return self._local_subnets

    @local_subnets.setter
    def local_subnets(self, local_subnets):
        """Sets the local_subnets of this UpdateServerRequest.

        本端网段列表,至少有一个本端网段

        :param local_subnets: The local_subnets of this UpdateServerRequest.
        :type local_subnets: list[str]
        """
        self._local_subnets = local_subnets

    @property
    def server_certificate(self):
        """Gets the server_certificate of this UpdateServerRequest.

        :return: The server_certificate of this UpdateServerRequest.
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateServerRequestServerCertificate`
        """
        return self._server_certificate

    @server_certificate.setter
    def server_certificate(self, server_certificate):
        """Sets the server_certificate of this UpdateServerRequest.

        :param server_certificate: The server_certificate of this UpdateServerRequest.
        :type server_certificate: :class:`huaweicloudsdkvpn.v5.UpdateServerRequestServerCertificate`
        """
        self._server_certificate = server_certificate

    @property
    def ssl_options(self):
        """Gets the ssl_options of this UpdateServerRequest.

        :return: The ssl_options of this UpdateServerRequest.
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateServerRequestSslOptions`
        """
        return self._ssl_options

    @ssl_options.setter
    def ssl_options(self, ssl_options):
        """Sets the ssl_options of this UpdateServerRequest.

        :param ssl_options: The ssl_options of this UpdateServerRequest.
        :type ssl_options: :class:`huaweicloudsdkvpn.v5.UpdateServerRequestSslOptions`
        """
        self._ssl_options = ssl_options

    @property
    def client_auth_type(self):
        """Gets the client_auth_type of this UpdateServerRequest.

        客户端认证类型

        :return: The client_auth_type of this UpdateServerRequest.
        :rtype: str
        """
        return self._client_auth_type

    @client_auth_type.setter
    def client_auth_type(self, client_auth_type):
        """Sets the client_auth_type of this UpdateServerRequest.

        客户端认证类型

        :param client_auth_type: The client_auth_type of this UpdateServerRequest.
        :type client_auth_type: str
        """
        self._client_auth_type = client_auth_type

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
        if not isinstance(other, UpdateServerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
