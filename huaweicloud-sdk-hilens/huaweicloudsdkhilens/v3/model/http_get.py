# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpGet:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host': 'str',
        'path': 'str',
        'port': 'int',
        'scheme': 'str'
    }

    attribute_map = {
        'host': 'host',
        'path': 'path',
        'port': 'port',
        'scheme': 'scheme'
    }

    def __init__(self, host=None, path=None, port=None, scheme=None):
        """HttpGet

        The model defined in huaweicloud sdk

        :param host: 请求的主机地址，默认为容器IP
        :type host: str
        :param path: 必须要以/开头，构造结果为：协议类型://主机地址:端口路径
        :type path: str
        :param port: 探测的http端口，1到65535之间的整数
        :type port: int
        :param scheme: 协议类型，HTTP或HTTPS，默认HTTP
        :type scheme: str
        """
        
        

        self._host = None
        self._path = None
        self._port = None
        self._scheme = None
        self.discriminator = None

        if host is not None:
            self.host = host
        self.path = path
        self.port = port
        if scheme is not None:
            self.scheme = scheme

    @property
    def host(self):
        """Gets the host of this HttpGet.

        请求的主机地址，默认为容器IP

        :return: The host of this HttpGet.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this HttpGet.

        请求的主机地址，默认为容器IP

        :param host: The host of this HttpGet.
        :type host: str
        """
        self._host = host

    @property
    def path(self):
        """Gets the path of this HttpGet.

        必须要以/开头，构造结果为：协议类型://主机地址:端口路径

        :return: The path of this HttpGet.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this HttpGet.

        必须要以/开头，构造结果为：协议类型://主机地址:端口路径

        :param path: The path of this HttpGet.
        :type path: str
        """
        self._path = path

    @property
    def port(self):
        """Gets the port of this HttpGet.

        探测的http端口，1到65535之间的整数

        :return: The port of this HttpGet.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this HttpGet.

        探测的http端口，1到65535之间的整数

        :param port: The port of this HttpGet.
        :type port: int
        """
        self._port = port

    @property
    def scheme(self):
        """Gets the scheme of this HttpGet.

        协议类型，HTTP或HTTPS，默认HTTP

        :return: The scheme of this HttpGet.
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """Sets the scheme of this HttpGet.

        协议类型，HTTP或HTTPS，默认HTTP

        :param scheme: The scheme of this HttpGet.
        :type scheme: str
        """
        self._scheme = scheme

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
        if not isinstance(other, HttpGet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
