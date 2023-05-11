# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpGetDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'path': 'str',
        'port': 'int',
        'host': 'str',
        'scheme': 'str'
    }

    attribute_map = {
        'path': 'path',
        'port': 'port',
        'host': 'host',
        'scheme': 'scheme'
    }

    def __init__(self, path=None, port=None, host=None, scheme=None):
        """HttpGetDetail

        The model defined in huaweicloud sdk

        :param path: 必须要以/开头，构造结果为：协议类型://主机地址:端口路径
        :type path: str
        :param port: 探测的http端口，1到65535之间的整数
        :type port: int
        :param host: 请求的主机地址，默认为容器IP
        :type host: str
        :param scheme: 协议类型，HTTP或HTTPS，默认HTTP
        :type scheme: str
        """
        
        

        self._path = None
        self._port = None
        self._host = None
        self._scheme = None
        self.discriminator = None

        self.path = path
        self.port = port
        if host is not None:
            self.host = host
        if scheme is not None:
            self.scheme = scheme

    @property
    def path(self):
        """Gets the path of this HttpGetDetail.

        必须要以/开头，构造结果为：协议类型://主机地址:端口路径

        :return: The path of this HttpGetDetail.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this HttpGetDetail.

        必须要以/开头，构造结果为：协议类型://主机地址:端口路径

        :param path: The path of this HttpGetDetail.
        :type path: str
        """
        self._path = path

    @property
    def port(self):
        """Gets the port of this HttpGetDetail.

        探测的http端口，1到65535之间的整数

        :return: The port of this HttpGetDetail.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this HttpGetDetail.

        探测的http端口，1到65535之间的整数

        :param port: The port of this HttpGetDetail.
        :type port: int
        """
        self._port = port

    @property
    def host(self):
        """Gets the host of this HttpGetDetail.

        请求的主机地址，默认为容器IP

        :return: The host of this HttpGetDetail.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this HttpGetDetail.

        请求的主机地址，默认为容器IP

        :param host: The host of this HttpGetDetail.
        :type host: str
        """
        self._host = host

    @property
    def scheme(self):
        """Gets the scheme of this HttpGetDetail.

        协议类型，HTTP或HTTPS，默认HTTP

        :return: The scheme of this HttpGetDetail.
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """Sets the scheme of this HttpGetDetail.

        协议类型，HTTP或HTTPS，默认HTTP

        :param scheme: The scheme of this HttpGetDetail.
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
        if not isinstance(other, HttpGetDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
