# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DnsDomain:

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
        'domain': 'str',
        'servers': 'list[Server]',
        'protect_port': 'str'
    }

    attribute_map = {
        'id': 'id',
        'domain': 'domain',
        'servers': 'servers',
        'protect_port': 'protect_port'
    }

    def __init__(self, id=None, domain=None, servers=None, protect_port=None):
        r"""DnsDomain

        The model defined in huaweicloud sdk

        :param id: dns-id
        :type id: str
        :param domain: 域名
        :type domain: str
        :param servers: dns服务信息
        :type servers: list[:class:`huaweicloudsdkwaf.v1.Server`]
        :param protect_port: 防护端口
        :type protect_port: str
        """
        
        

        self._id = None
        self._domain = None
        self._servers = None
        self._protect_port = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if domain is not None:
            self.domain = domain
        if servers is not None:
            self.servers = servers
        if protect_port is not None:
            self.protect_port = protect_port

    @property
    def id(self):
        r"""Gets the id of this DnsDomain.

        dns-id

        :return: The id of this DnsDomain.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DnsDomain.

        dns-id

        :param id: The id of this DnsDomain.
        :type id: str
        """
        self._id = id

    @property
    def domain(self):
        r"""Gets the domain of this DnsDomain.

        域名

        :return: The domain of this DnsDomain.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this DnsDomain.

        域名

        :param domain: The domain of this DnsDomain.
        :type domain: str
        """
        self._domain = domain

    @property
    def servers(self):
        r"""Gets the servers of this DnsDomain.

        dns服务信息

        :return: The servers of this DnsDomain.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.Server`]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        r"""Sets the servers of this DnsDomain.

        dns服务信息

        :param servers: The servers of this DnsDomain.
        :type servers: list[:class:`huaweicloudsdkwaf.v1.Server`]
        """
        self._servers = servers

    @property
    def protect_port(self):
        r"""Gets the protect_port of this DnsDomain.

        防护端口

        :return: The protect_port of this DnsDomain.
        :rtype: str
        """
        return self._protect_port

    @protect_port.setter
    def protect_port(self, protect_port):
        r"""Sets the protect_port of this DnsDomain.

        防护端口

        :param protect_port: The protect_port of this DnsDomain.
        :type protect_port: str
        """
        self._protect_port = protect_port

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
        if not isinstance(other, DnsDomain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
