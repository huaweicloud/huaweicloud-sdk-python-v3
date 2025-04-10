# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetAddress:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ip': 'str',
        'port': 'int',
        'domain': 'str'
    }

    attribute_map = {
        'ip': 'ip',
        'port': 'port',
        'domain': 'domain'
    }

    def __init__(self, ip=None, port=None, domain=None):
        r"""NetAddress

        The model defined in huaweicloud sdk

        :param ip: **参数说明**：服务的对应IP
        :type ip: str
        :param port: **参数说明**：服务对应端口
        :type port: int
        :param domain: **参数说明**：服务对应的域名
        :type domain: str
        """
        
        

        self._ip = None
        self._port = None
        self._domain = None
        self.discriminator = None

        if ip is not None:
            self.ip = ip
        if port is not None:
            self.port = port
        if domain is not None:
            self.domain = domain

    @property
    def ip(self):
        r"""Gets the ip of this NetAddress.

        **参数说明**：服务的对应IP

        :return: The ip of this NetAddress.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this NetAddress.

        **参数说明**：服务的对应IP

        :param ip: The ip of this NetAddress.
        :type ip: str
        """
        self._ip = ip

    @property
    def port(self):
        r"""Gets the port of this NetAddress.

        **参数说明**：服务对应端口

        :return: The port of this NetAddress.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this NetAddress.

        **参数说明**：服务对应端口

        :param port: The port of this NetAddress.
        :type port: int
        """
        self._port = port

    @property
    def domain(self):
        r"""Gets the domain of this NetAddress.

        **参数说明**：服务对应的域名

        :return: The domain of this NetAddress.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this NetAddress.

        **参数说明**：服务对应的域名

        :param domain: The domain of this NetAddress.
        :type domain: str
        """
        self._domain = domain

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
        if not isinstance(other, NetAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
