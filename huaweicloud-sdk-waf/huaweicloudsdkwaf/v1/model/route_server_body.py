# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RouteServerBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'back_protocol': 'str',
        'address': 'str',
        'port': 'int'
    }

    attribute_map = {
        'back_protocol': 'back_protocol',
        'address': 'address',
        'port': 'port'
    }

    def __init__(self, back_protocol=None, address=None, port=None):
        """RouteServerBody

        The model defined in huaweicloud sdk

        :param back_protocol: WAF转发客户端请求到防护域名源站服务器的协议
        :type back_protocol: str
        :param address: 客户端访问的源站服务器的IP地址
        :type address: str
        :param port: WAF转发客户端请求到源站服务的业务端口
        :type port: int
        """
        
        

        self._back_protocol = None
        self._address = None
        self._port = None
        self.discriminator = None

        if back_protocol is not None:
            self.back_protocol = back_protocol
        if address is not None:
            self.address = address
        if port is not None:
            self.port = port

    @property
    def back_protocol(self):
        """Gets the back_protocol of this RouteServerBody.

        WAF转发客户端请求到防护域名源站服务器的协议

        :return: The back_protocol of this RouteServerBody.
        :rtype: str
        """
        return self._back_protocol

    @back_protocol.setter
    def back_protocol(self, back_protocol):
        """Sets the back_protocol of this RouteServerBody.

        WAF转发客户端请求到防护域名源站服务器的协议

        :param back_protocol: The back_protocol of this RouteServerBody.
        :type back_protocol: str
        """
        self._back_protocol = back_protocol

    @property
    def address(self):
        """Gets the address of this RouteServerBody.

        客户端访问的源站服务器的IP地址

        :return: The address of this RouteServerBody.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this RouteServerBody.

        客户端访问的源站服务器的IP地址

        :param address: The address of this RouteServerBody.
        :type address: str
        """
        self._address = address

    @property
    def port(self):
        """Gets the port of this RouteServerBody.

        WAF转发客户端请求到源站服务的业务端口

        :return: The port of this RouteServerBody.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this RouteServerBody.

        WAF转发客户端请求到源站服务的业务端口

        :param port: The port of this RouteServerBody.
        :type port: int
        """
        self._port = port

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
        if not isinstance(other, RouteServerBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
