# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpGetDTO:

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
        """HttpGetDTO

        The model defined in huaweicloud sdk

        :param path: 请求路径
        :type path: str
        :param port: 端口
        :type port: int
        :param host: 主机地址
        :type host: str
        :param scheme: 协议类型
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
        self.scheme = scheme

    @property
    def path(self):
        """Gets the path of this HttpGetDTO.

        请求路径

        :return: The path of this HttpGetDTO.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this HttpGetDTO.

        请求路径

        :param path: The path of this HttpGetDTO.
        :type path: str
        """
        self._path = path

    @property
    def port(self):
        """Gets the port of this HttpGetDTO.

        端口

        :return: The port of this HttpGetDTO.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this HttpGetDTO.

        端口

        :param port: The port of this HttpGetDTO.
        :type port: int
        """
        self._port = port

    @property
    def host(self):
        """Gets the host of this HttpGetDTO.

        主机地址

        :return: The host of this HttpGetDTO.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this HttpGetDTO.

        主机地址

        :param host: The host of this HttpGetDTO.
        :type host: str
        """
        self._host = host

    @property
    def scheme(self):
        """Gets the scheme of this HttpGetDTO.

        协议类型

        :return: The scheme of this HttpGetDTO.
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """Sets the scheme of this HttpGetDTO.

        协议类型

        :param scheme: The scheme of this HttpGetDTO.
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
        if not isinstance(other, HttpGetDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
