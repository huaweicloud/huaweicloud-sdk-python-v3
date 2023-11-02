# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlertNetworkList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'direction': 'str',
        'protocol': 'str',
        'src_ip': 'str',
        'src_port': 'int',
        'src_domain': 'str',
        'src_geo': 'AlertSrcGeo',
        'dest_ip': 'str',
        'dest_port': 'str',
        'dest_domain': 'str',
        'dest_geo': 'AlertDestGeo'
    }

    attribute_map = {
        'direction': 'direction',
        'protocol': 'protocol',
        'src_ip': 'src_ip',
        'src_port': 'src_port',
        'src_domain': 'src_domain',
        'src_geo': 'src_geo',
        'dest_ip': 'dest_ip',
        'dest_port': 'dest_port',
        'dest_domain': 'dest_domain',
        'dest_geo': 'dest_geo'
    }

    def __init__(self, direction=None, protocol=None, src_ip=None, src_port=None, src_domain=None, src_geo=None, dest_ip=None, dest_port=None, dest_domain=None, dest_geo=None):
        """AlertNetworkList

        The model defined in huaweicloud sdk

        :param direction: 方向，取值范围：IN | OUT
        :type direction: str
        :param protocol: 协议，包含7层和4层的协议 参考：IANA registered name https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml
        :type protocol: str
        :param src_ip: 源IP地址
        :type src_ip: str
        :param src_port: 源端口，0–65535
        :type src_port: int
        :param src_domain: 源域名
        :type src_domain: str
        :param src_geo: 
        :type src_geo: :class:`huaweicloudsdksecmaster.v2.AlertSrcGeo`
        :param dest_ip: 目的IP地址
        :type dest_ip: str
        :param dest_port: 目的端口，0–65535
        :type dest_port: str
        :param dest_domain: 目的域名
        :type dest_domain: str
        :param dest_geo: 
        :type dest_geo: :class:`huaweicloudsdksecmaster.v2.AlertDestGeo`
        """
        
        

        self._direction = None
        self._protocol = None
        self._src_ip = None
        self._src_port = None
        self._src_domain = None
        self._src_geo = None
        self._dest_ip = None
        self._dest_port = None
        self._dest_domain = None
        self._dest_geo = None
        self.discriminator = None

        if direction is not None:
            self.direction = direction
        if protocol is not None:
            self.protocol = protocol
        if src_ip is not None:
            self.src_ip = src_ip
        if src_port is not None:
            self.src_port = src_port
        if src_domain is not None:
            self.src_domain = src_domain
        if src_geo is not None:
            self.src_geo = src_geo
        if dest_ip is not None:
            self.dest_ip = dest_ip
        if dest_port is not None:
            self.dest_port = dest_port
        if dest_domain is not None:
            self.dest_domain = dest_domain
        if dest_geo is not None:
            self.dest_geo = dest_geo

    @property
    def direction(self):
        """Gets the direction of this AlertNetworkList.

        方向，取值范围：IN | OUT

        :return: The direction of this AlertNetworkList.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this AlertNetworkList.

        方向，取值范围：IN | OUT

        :param direction: The direction of this AlertNetworkList.
        :type direction: str
        """
        self._direction = direction

    @property
    def protocol(self):
        """Gets the protocol of this AlertNetworkList.

        协议，包含7层和4层的协议 参考：IANA registered name https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml

        :return: The protocol of this AlertNetworkList.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this AlertNetworkList.

        协议，包含7层和4层的协议 参考：IANA registered name https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml

        :param protocol: The protocol of this AlertNetworkList.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def src_ip(self):
        """Gets the src_ip of this AlertNetworkList.

        源IP地址

        :return: The src_ip of this AlertNetworkList.
        :rtype: str
        """
        return self._src_ip

    @src_ip.setter
    def src_ip(self, src_ip):
        """Sets the src_ip of this AlertNetworkList.

        源IP地址

        :param src_ip: The src_ip of this AlertNetworkList.
        :type src_ip: str
        """
        self._src_ip = src_ip

    @property
    def src_port(self):
        """Gets the src_port of this AlertNetworkList.

        源端口，0–65535

        :return: The src_port of this AlertNetworkList.
        :rtype: int
        """
        return self._src_port

    @src_port.setter
    def src_port(self, src_port):
        """Sets the src_port of this AlertNetworkList.

        源端口，0–65535

        :param src_port: The src_port of this AlertNetworkList.
        :type src_port: int
        """
        self._src_port = src_port

    @property
    def src_domain(self):
        """Gets the src_domain of this AlertNetworkList.

        源域名

        :return: The src_domain of this AlertNetworkList.
        :rtype: str
        """
        return self._src_domain

    @src_domain.setter
    def src_domain(self, src_domain):
        """Sets the src_domain of this AlertNetworkList.

        源域名

        :param src_domain: The src_domain of this AlertNetworkList.
        :type src_domain: str
        """
        self._src_domain = src_domain

    @property
    def src_geo(self):
        """Gets the src_geo of this AlertNetworkList.

        :return: The src_geo of this AlertNetworkList.
        :rtype: :class:`huaweicloudsdksecmaster.v2.AlertSrcGeo`
        """
        return self._src_geo

    @src_geo.setter
    def src_geo(self, src_geo):
        """Sets the src_geo of this AlertNetworkList.

        :param src_geo: The src_geo of this AlertNetworkList.
        :type src_geo: :class:`huaweicloudsdksecmaster.v2.AlertSrcGeo`
        """
        self._src_geo = src_geo

    @property
    def dest_ip(self):
        """Gets the dest_ip of this AlertNetworkList.

        目的IP地址

        :return: The dest_ip of this AlertNetworkList.
        :rtype: str
        """
        return self._dest_ip

    @dest_ip.setter
    def dest_ip(self, dest_ip):
        """Sets the dest_ip of this AlertNetworkList.

        目的IP地址

        :param dest_ip: The dest_ip of this AlertNetworkList.
        :type dest_ip: str
        """
        self._dest_ip = dest_ip

    @property
    def dest_port(self):
        """Gets the dest_port of this AlertNetworkList.

        目的端口，0–65535

        :return: The dest_port of this AlertNetworkList.
        :rtype: str
        """
        return self._dest_port

    @dest_port.setter
    def dest_port(self, dest_port):
        """Sets the dest_port of this AlertNetworkList.

        目的端口，0–65535

        :param dest_port: The dest_port of this AlertNetworkList.
        :type dest_port: str
        """
        self._dest_port = dest_port

    @property
    def dest_domain(self):
        """Gets the dest_domain of this AlertNetworkList.

        目的域名

        :return: The dest_domain of this AlertNetworkList.
        :rtype: str
        """
        return self._dest_domain

    @dest_domain.setter
    def dest_domain(self, dest_domain):
        """Sets the dest_domain of this AlertNetworkList.

        目的域名

        :param dest_domain: The dest_domain of this AlertNetworkList.
        :type dest_domain: str
        """
        self._dest_domain = dest_domain

    @property
    def dest_geo(self):
        """Gets the dest_geo of this AlertNetworkList.

        :return: The dest_geo of this AlertNetworkList.
        :rtype: :class:`huaweicloudsdksecmaster.v2.AlertDestGeo`
        """
        return self._dest_geo

    @dest_geo.setter
    def dest_geo(self, dest_geo):
        """Sets the dest_geo of this AlertNetworkList.

        :param dest_geo: The dest_geo of this AlertNetworkList.
        :type dest_geo: :class:`huaweicloudsdksecmaster.v2.AlertDestGeo`
        """
        self._dest_geo = dest_geo

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
        if not isinstance(other, AlertNetworkList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
