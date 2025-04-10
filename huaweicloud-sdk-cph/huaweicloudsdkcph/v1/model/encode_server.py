# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EncodeServer:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'encode_server_name': 'str',
        'encode_server_id': 'str',
        'encode_server_ip': 'str',
        'server_id': 'str',
        'keypair_name': 'str',
        'type': 'int',
        'status': 'int',
        'access_infos': 'list[EncodeServerAccessInfo]',
        'encode_server_ipv6': 'str'
    }

    attribute_map = {
        'encode_server_name': 'encode_server_name',
        'encode_server_id': 'encode_server_id',
        'encode_server_ip': 'encode_server_ip',
        'server_id': 'server_id',
        'keypair_name': 'keypair_name',
        'type': 'type',
        'status': 'status',
        'access_infos': 'access_infos',
        'encode_server_ipv6': 'encode_server_ipv6'
    }

    def __init__(self, encode_server_name=None, encode_server_id=None, encode_server_ip=None, server_id=None, keypair_name=None, type=None, status=None, access_infos=None, encode_server_ipv6=None):
        r"""EncodeServer

        The model defined in huaweicloud sdk

        :param encode_server_name: 编码服务的名称，不大于64个字节。
        :type encode_server_name: str
        :param encode_server_id: 编码服务的唯一标识ID，不大于32个字节。
        :type encode_server_id: str
        :param encode_server_ip: 编码服务IP地址。
        :type encode_server_ip: str
        :param server_id: 云手机服务器ID，不大于32个字节。
        :type server_id: str
        :param keypair_name: 编码服务登录密钥名称。
        :type keypair_name: str
        :param type: 编码服务类型。 - 0：服务器 - 1：容器
        :type type: int
        :param status: 编码服务状态。 - 1：运行中 - 2：异常 - 3：重启中 - 0、4、5：创建中
        :type status: int
        :param access_infos: 编码服务的访问信息。
        :type access_infos: list[:class:`huaweicloudsdkcph.v1.EncodeServerAccessInfo`]
        :param encode_server_ipv6: 编码服务IPv6地址。
        :type encode_server_ipv6: str
        """
        
        

        self._encode_server_name = None
        self._encode_server_id = None
        self._encode_server_ip = None
        self._server_id = None
        self._keypair_name = None
        self._type = None
        self._status = None
        self._access_infos = None
        self._encode_server_ipv6 = None
        self.discriminator = None

        if encode_server_name is not None:
            self.encode_server_name = encode_server_name
        if encode_server_id is not None:
            self.encode_server_id = encode_server_id
        if encode_server_ip is not None:
            self.encode_server_ip = encode_server_ip
        if server_id is not None:
            self.server_id = server_id
        if keypair_name is not None:
            self.keypair_name = keypair_name
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if access_infos is not None:
            self.access_infos = access_infos
        if encode_server_ipv6 is not None:
            self.encode_server_ipv6 = encode_server_ipv6

    @property
    def encode_server_name(self):
        r"""Gets the encode_server_name of this EncodeServer.

        编码服务的名称，不大于64个字节。

        :return: The encode_server_name of this EncodeServer.
        :rtype: str
        """
        return self._encode_server_name

    @encode_server_name.setter
    def encode_server_name(self, encode_server_name):
        r"""Sets the encode_server_name of this EncodeServer.

        编码服务的名称，不大于64个字节。

        :param encode_server_name: The encode_server_name of this EncodeServer.
        :type encode_server_name: str
        """
        self._encode_server_name = encode_server_name

    @property
    def encode_server_id(self):
        r"""Gets the encode_server_id of this EncodeServer.

        编码服务的唯一标识ID，不大于32个字节。

        :return: The encode_server_id of this EncodeServer.
        :rtype: str
        """
        return self._encode_server_id

    @encode_server_id.setter
    def encode_server_id(self, encode_server_id):
        r"""Sets the encode_server_id of this EncodeServer.

        编码服务的唯一标识ID，不大于32个字节。

        :param encode_server_id: The encode_server_id of this EncodeServer.
        :type encode_server_id: str
        """
        self._encode_server_id = encode_server_id

    @property
    def encode_server_ip(self):
        r"""Gets the encode_server_ip of this EncodeServer.

        编码服务IP地址。

        :return: The encode_server_ip of this EncodeServer.
        :rtype: str
        """
        return self._encode_server_ip

    @encode_server_ip.setter
    def encode_server_ip(self, encode_server_ip):
        r"""Sets the encode_server_ip of this EncodeServer.

        编码服务IP地址。

        :param encode_server_ip: The encode_server_ip of this EncodeServer.
        :type encode_server_ip: str
        """
        self._encode_server_ip = encode_server_ip

    @property
    def server_id(self):
        r"""Gets the server_id of this EncodeServer.

        云手机服务器ID，不大于32个字节。

        :return: The server_id of this EncodeServer.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this EncodeServer.

        云手机服务器ID，不大于32个字节。

        :param server_id: The server_id of this EncodeServer.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def keypair_name(self):
        r"""Gets the keypair_name of this EncodeServer.

        编码服务登录密钥名称。

        :return: The keypair_name of this EncodeServer.
        :rtype: str
        """
        return self._keypair_name

    @keypair_name.setter
    def keypair_name(self, keypair_name):
        r"""Sets the keypair_name of this EncodeServer.

        编码服务登录密钥名称。

        :param keypair_name: The keypair_name of this EncodeServer.
        :type keypair_name: str
        """
        self._keypair_name = keypair_name

    @property
    def type(self):
        r"""Gets the type of this EncodeServer.

        编码服务类型。 - 0：服务器 - 1：容器

        :return: The type of this EncodeServer.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this EncodeServer.

        编码服务类型。 - 0：服务器 - 1：容器

        :param type: The type of this EncodeServer.
        :type type: int
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this EncodeServer.

        编码服务状态。 - 1：运行中 - 2：异常 - 3：重启中 - 0、4、5：创建中

        :return: The status of this EncodeServer.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this EncodeServer.

        编码服务状态。 - 1：运行中 - 2：异常 - 3：重启中 - 0、4、5：创建中

        :param status: The status of this EncodeServer.
        :type status: int
        """
        self._status = status

    @property
    def access_infos(self):
        r"""Gets the access_infos of this EncodeServer.

        编码服务的访问信息。

        :return: The access_infos of this EncodeServer.
        :rtype: list[:class:`huaweicloudsdkcph.v1.EncodeServerAccessInfo`]
        """
        return self._access_infos

    @access_infos.setter
    def access_infos(self, access_infos):
        r"""Sets the access_infos of this EncodeServer.

        编码服务的访问信息。

        :param access_infos: The access_infos of this EncodeServer.
        :type access_infos: list[:class:`huaweicloudsdkcph.v1.EncodeServerAccessInfo`]
        """
        self._access_infos = access_infos

    @property
    def encode_server_ipv6(self):
        r"""Gets the encode_server_ipv6 of this EncodeServer.

        编码服务IPv6地址。

        :return: The encode_server_ipv6 of this EncodeServer.
        :rtype: str
        """
        return self._encode_server_ipv6

    @encode_server_ipv6.setter
    def encode_server_ipv6(self, encode_server_ipv6):
        r"""Sets the encode_server_ipv6 of this EncodeServer.

        编码服务IPv6地址。

        :param encode_server_ipv6: The encode_server_ipv6 of this EncodeServer.
        :type encode_server_ipv6: str
        """
        self._encode_server_ipv6 = encode_server_ipv6

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
        if not isinstance(other, EncodeServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
