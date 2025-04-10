# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EncodeServerAccessInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'listen_port': 'int',
        'access_ip': 'str',
        'intranet_ip': 'str',
        'public_ip': 'str',
        'server_ip': 'str',
        'access_port': 'int',
        'type': 'str',
        'server_ipv6': 'str'
    }

    attribute_map = {
        'listen_port': 'listen_port',
        'access_ip': 'access_ip',
        'intranet_ip': 'intranet_ip',
        'public_ip': 'public_ip',
        'server_ip': 'server_ip',
        'access_port': 'access_port',
        'type': 'type',
        'server_ipv6': 'server_ipv6'
    }

    def __init__(self, listen_port=None, access_ip=None, intranet_ip=None, public_ip=None, server_ip=None, access_port=None, type=None, server_ipv6=None):
        r"""EncodeServerAccessInfo

        The model defined in huaweicloud sdk

        :param listen_port: 编码服务监听端口。
        :type listen_port: int
        :param access_ip: 编码服务访问的公网IP（过期）。
        :type access_ip: str
        :param intranet_ip: 编码服务访问的内网IP（过期）。
        :type intranet_ip: str
        :param public_ip: 编码服务访问的公网IP（新增）。
        :type public_ip: str
        :param server_ip: 编码服务访问的内网IP（新增）。
        :type server_ip: str
        :param access_port: 编码服务公网的访问端口。
        :type access_port: int
        :param type: 编码服务的端口类型，取值如下： - adb：云手机的ADB端口 - vnc：云手机的VNC端口 - cph_app_server：云游戏客户端接入端 - cph_h5_server：云游戏H5 web网页接入端口 - 其他值：用户自定义端口
        :type type: str
        :param server_ipv6: 编码服务访问的内网IPv6 IP（新增）。
        :type server_ipv6: str
        """
        
        

        self._listen_port = None
        self._access_ip = None
        self._intranet_ip = None
        self._public_ip = None
        self._server_ip = None
        self._access_port = None
        self._type = None
        self._server_ipv6 = None
        self.discriminator = None

        if listen_port is not None:
            self.listen_port = listen_port
        if access_ip is not None:
            self.access_ip = access_ip
        if intranet_ip is not None:
            self.intranet_ip = intranet_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if server_ip is not None:
            self.server_ip = server_ip
        if access_port is not None:
            self.access_port = access_port
        if type is not None:
            self.type = type
        if server_ipv6 is not None:
            self.server_ipv6 = server_ipv6

    @property
    def listen_port(self):
        r"""Gets the listen_port of this EncodeServerAccessInfo.

        编码服务监听端口。

        :return: The listen_port of this EncodeServerAccessInfo.
        :rtype: int
        """
        return self._listen_port

    @listen_port.setter
    def listen_port(self, listen_port):
        r"""Sets the listen_port of this EncodeServerAccessInfo.

        编码服务监听端口。

        :param listen_port: The listen_port of this EncodeServerAccessInfo.
        :type listen_port: int
        """
        self._listen_port = listen_port

    @property
    def access_ip(self):
        r"""Gets the access_ip of this EncodeServerAccessInfo.

        编码服务访问的公网IP（过期）。

        :return: The access_ip of this EncodeServerAccessInfo.
        :rtype: str
        """
        return self._access_ip

    @access_ip.setter
    def access_ip(self, access_ip):
        r"""Sets the access_ip of this EncodeServerAccessInfo.

        编码服务访问的公网IP（过期）。

        :param access_ip: The access_ip of this EncodeServerAccessInfo.
        :type access_ip: str
        """
        self._access_ip = access_ip

    @property
    def intranet_ip(self):
        r"""Gets the intranet_ip of this EncodeServerAccessInfo.

        编码服务访问的内网IP（过期）。

        :return: The intranet_ip of this EncodeServerAccessInfo.
        :rtype: str
        """
        return self._intranet_ip

    @intranet_ip.setter
    def intranet_ip(self, intranet_ip):
        r"""Sets the intranet_ip of this EncodeServerAccessInfo.

        编码服务访问的内网IP（过期）。

        :param intranet_ip: The intranet_ip of this EncodeServerAccessInfo.
        :type intranet_ip: str
        """
        self._intranet_ip = intranet_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this EncodeServerAccessInfo.

        编码服务访问的公网IP（新增）。

        :return: The public_ip of this EncodeServerAccessInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this EncodeServerAccessInfo.

        编码服务访问的公网IP（新增）。

        :param public_ip: The public_ip of this EncodeServerAccessInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def server_ip(self):
        r"""Gets the server_ip of this EncodeServerAccessInfo.

        编码服务访问的内网IP（新增）。

        :return: The server_ip of this EncodeServerAccessInfo.
        :rtype: str
        """
        return self._server_ip

    @server_ip.setter
    def server_ip(self, server_ip):
        r"""Sets the server_ip of this EncodeServerAccessInfo.

        编码服务访问的内网IP（新增）。

        :param server_ip: The server_ip of this EncodeServerAccessInfo.
        :type server_ip: str
        """
        self._server_ip = server_ip

    @property
    def access_port(self):
        r"""Gets the access_port of this EncodeServerAccessInfo.

        编码服务公网的访问端口。

        :return: The access_port of this EncodeServerAccessInfo.
        :rtype: int
        """
        return self._access_port

    @access_port.setter
    def access_port(self, access_port):
        r"""Sets the access_port of this EncodeServerAccessInfo.

        编码服务公网的访问端口。

        :param access_port: The access_port of this EncodeServerAccessInfo.
        :type access_port: int
        """
        self._access_port = access_port

    @property
    def type(self):
        r"""Gets the type of this EncodeServerAccessInfo.

        编码服务的端口类型，取值如下： - adb：云手机的ADB端口 - vnc：云手机的VNC端口 - cph_app_server：云游戏客户端接入端 - cph_h5_server：云游戏H5 web网页接入端口 - 其他值：用户自定义端口

        :return: The type of this EncodeServerAccessInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this EncodeServerAccessInfo.

        编码服务的端口类型，取值如下： - adb：云手机的ADB端口 - vnc：云手机的VNC端口 - cph_app_server：云游戏客户端接入端 - cph_h5_server：云游戏H5 web网页接入端口 - 其他值：用户自定义端口

        :param type: The type of this EncodeServerAccessInfo.
        :type type: str
        """
        self._type = type

    @property
    def server_ipv6(self):
        r"""Gets the server_ipv6 of this EncodeServerAccessInfo.

        编码服务访问的内网IPv6 IP（新增）。

        :return: The server_ipv6 of this EncodeServerAccessInfo.
        :rtype: str
        """
        return self._server_ipv6

    @server_ipv6.setter
    def server_ipv6(self, server_ipv6):
        r"""Sets the server_ipv6 of this EncodeServerAccessInfo.

        编码服务访问的内网IPv6 IP（新增）。

        :param server_ipv6: The server_ipv6 of this EncodeServerAccessInfo.
        :type server_ipv6: str
        """
        self._server_ipv6 = server_ipv6

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
        if not isinstance(other, EncodeServerAccessInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
