# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NacosServerConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ip_address': 'str',
        'port': 'int',
        'grpc_port': 'int'
    }

    attribute_map = {
        'ip_address': 'ip_address',
        'port': 'port',
        'grpc_port': 'grpc_port'
    }

    def __init__(self, ip_address=None, port=None, grpc_port=None):
        r"""NacosServerConfig

        The model defined in huaweicloud sdk

        :param ip_address: nacos服务端IP地址。不包含中文字符。
        :type ip_address: str
        :param port: nacos服务端端口号。取值范围1 ~ 65535。
        :type port: int
        :param grpc_port: nacos服务端gRPC端口号，默认为port+1000。取值范围1 ~ 65535。
        :type grpc_port: int
        """
        
        

        self._ip_address = None
        self._port = None
        self._grpc_port = None
        self.discriminator = None

        self.ip_address = ip_address
        self.port = port
        if grpc_port is not None:
            self.grpc_port = grpc_port

    @property
    def ip_address(self):
        r"""Gets the ip_address of this NacosServerConfig.

        nacos服务端IP地址。不包含中文字符。

        :return: The ip_address of this NacosServerConfig.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this NacosServerConfig.

        nacos服务端IP地址。不包含中文字符。

        :param ip_address: The ip_address of this NacosServerConfig.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def port(self):
        r"""Gets the port of this NacosServerConfig.

        nacos服务端端口号。取值范围1 ~ 65535。

        :return: The port of this NacosServerConfig.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this NacosServerConfig.

        nacos服务端端口号。取值范围1 ~ 65535。

        :param port: The port of this NacosServerConfig.
        :type port: int
        """
        self._port = port

    @property
    def grpc_port(self):
        r"""Gets the grpc_port of this NacosServerConfig.

        nacos服务端gRPC端口号，默认为port+1000。取值范围1 ~ 65535。

        :return: The grpc_port of this NacosServerConfig.
        :rtype: int
        """
        return self._grpc_port

    @grpc_port.setter
    def grpc_port(self, grpc_port):
        r"""Sets the grpc_port of this NacosServerConfig.

        nacos服务端gRPC端口号，默认为port+1000。取值范围1 ~ 65535。

        :param grpc_port: The grpc_port of this NacosServerConfig.
        :type grpc_port: int
        """
        self._grpc_port = grpc_port

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
        if not isinstance(other, NacosServerConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
