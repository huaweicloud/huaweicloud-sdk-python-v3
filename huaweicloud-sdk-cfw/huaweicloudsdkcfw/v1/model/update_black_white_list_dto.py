# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateBlackWhiteListDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'direction': 'int',
        'address_type': 'int',
        'address': 'str',
        'protocol': 'int',
        'port': 'str',
        'description': 'str'
    }

    attribute_map = {
        'direction': 'direction',
        'address_type': 'address_type',
        'address': 'address',
        'protocol': 'protocol',
        'port': 'port',
        'description': 'description'
    }

    def __init__(self, direction=None, address_type=None, address=None, protocol=None, port=None, description=None):
        r"""UpdateBlackWhiteListDto

        The model defined in huaweicloud sdk

        :param direction: 地址方向0：源地址1：目的地址
        :type direction: int
        :param address_type: 地址类型0：ipv4，1:ipv6
        :type address_type: int
        :param address: ip地址
        :type address: str
        :param protocol: 协议类型：TCP为6，UDP为17，ICMP为1，ICMPV6为58，ANY为-1
        :type protocol: int
        :param port: 端口
        :type port: str
        :param description: 描述
        :type description: str
        """
        
        

        self._direction = None
        self._address_type = None
        self._address = None
        self._protocol = None
        self._port = None
        self._description = None
        self.discriminator = None

        if direction is not None:
            self.direction = direction
        if address_type is not None:
            self.address_type = address_type
        self.address = address
        if protocol is not None:
            self.protocol = protocol
        if port is not None:
            self.port = port
        if description is not None:
            self.description = description

    @property
    def direction(self):
        r"""Gets the direction of this UpdateBlackWhiteListDto.

        地址方向0：源地址1：目的地址

        :return: The direction of this UpdateBlackWhiteListDto.
        :rtype: int
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        r"""Sets the direction of this UpdateBlackWhiteListDto.

        地址方向0：源地址1：目的地址

        :param direction: The direction of this UpdateBlackWhiteListDto.
        :type direction: int
        """
        self._direction = direction

    @property
    def address_type(self):
        r"""Gets the address_type of this UpdateBlackWhiteListDto.

        地址类型0：ipv4，1:ipv6

        :return: The address_type of this UpdateBlackWhiteListDto.
        :rtype: int
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        r"""Sets the address_type of this UpdateBlackWhiteListDto.

        地址类型0：ipv4，1:ipv6

        :param address_type: The address_type of this UpdateBlackWhiteListDto.
        :type address_type: int
        """
        self._address_type = address_type

    @property
    def address(self):
        r"""Gets the address of this UpdateBlackWhiteListDto.

        ip地址

        :return: The address of this UpdateBlackWhiteListDto.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this UpdateBlackWhiteListDto.

        ip地址

        :param address: The address of this UpdateBlackWhiteListDto.
        :type address: str
        """
        self._address = address

    @property
    def protocol(self):
        r"""Gets the protocol of this UpdateBlackWhiteListDto.

        协议类型：TCP为6，UDP为17，ICMP为1，ICMPV6为58，ANY为-1

        :return: The protocol of this UpdateBlackWhiteListDto.
        :rtype: int
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this UpdateBlackWhiteListDto.

        协议类型：TCP为6，UDP为17，ICMP为1，ICMPV6为58，ANY为-1

        :param protocol: The protocol of this UpdateBlackWhiteListDto.
        :type protocol: int
        """
        self._protocol = protocol

    @property
    def port(self):
        r"""Gets the port of this UpdateBlackWhiteListDto.

        端口

        :return: The port of this UpdateBlackWhiteListDto.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this UpdateBlackWhiteListDto.

        端口

        :param port: The port of this UpdateBlackWhiteListDto.
        :type port: str
        """
        self._port = port

    @property
    def description(self):
        r"""Gets the description of this UpdateBlackWhiteListDto.

        描述

        :return: The description of this UpdateBlackWhiteListDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateBlackWhiteListDto.

        描述

        :param description: The description of this UpdateBlackWhiteListDto.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, UpdateBlackWhiteListDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
