# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateServerRequestSslOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protocol': 'str',
        'port': 'int',
        'encryption_algorithm': 'str',
        'is_compressed': 'bool'
    }

    attribute_map = {
        'protocol': 'protocol',
        'port': 'port',
        'encryption_algorithm': 'encryption_algorithm',
        'is_compressed': 'is_compressed'
    }

    def __init__(self, protocol=None, port=None, encryption_algorithm=None, is_compressed=None):
        """CreateServerRequestSslOptions

        The model defined in huaweicloud sdk

        :param protocol: 协议
        :type protocol: str
        :param port: 端口
        :type port: int
        :param encryption_algorithm: 加密算法
        :type encryption_algorithm: str
        :param is_compressed: 是否压缩
        :type is_compressed: bool
        """
        
        

        self._protocol = None
        self._port = None
        self._encryption_algorithm = None
        self._is_compressed = None
        self.discriminator = None

        if protocol is not None:
            self.protocol = protocol
        if port is not None:
            self.port = port
        if encryption_algorithm is not None:
            self.encryption_algorithm = encryption_algorithm
        if is_compressed is not None:
            self.is_compressed = is_compressed

    @property
    def protocol(self):
        """Gets the protocol of this CreateServerRequestSslOptions.

        协议

        :return: The protocol of this CreateServerRequestSslOptions.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this CreateServerRequestSslOptions.

        协议

        :param protocol: The protocol of this CreateServerRequestSslOptions.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def port(self):
        """Gets the port of this CreateServerRequestSslOptions.

        端口

        :return: The port of this CreateServerRequestSslOptions.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this CreateServerRequestSslOptions.

        端口

        :param port: The port of this CreateServerRequestSslOptions.
        :type port: int
        """
        self._port = port

    @property
    def encryption_algorithm(self):
        """Gets the encryption_algorithm of this CreateServerRequestSslOptions.

        加密算法

        :return: The encryption_algorithm of this CreateServerRequestSslOptions.
        :rtype: str
        """
        return self._encryption_algorithm

    @encryption_algorithm.setter
    def encryption_algorithm(self, encryption_algorithm):
        """Sets the encryption_algorithm of this CreateServerRequestSslOptions.

        加密算法

        :param encryption_algorithm: The encryption_algorithm of this CreateServerRequestSslOptions.
        :type encryption_algorithm: str
        """
        self._encryption_algorithm = encryption_algorithm

    @property
    def is_compressed(self):
        """Gets the is_compressed of this CreateServerRequestSslOptions.

        是否压缩

        :return: The is_compressed of this CreateServerRequestSslOptions.
        :rtype: bool
        """
        return self._is_compressed

    @is_compressed.setter
    def is_compressed(self, is_compressed):
        """Sets the is_compressed of this CreateServerRequestSslOptions.

        是否压缩

        :param is_compressed: The is_compressed of this CreateServerRequestSslOptions.
        :type is_compressed: bool
        """
        self._is_compressed = is_compressed

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
        if not isinstance(other, CreateServerRequestSslOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
