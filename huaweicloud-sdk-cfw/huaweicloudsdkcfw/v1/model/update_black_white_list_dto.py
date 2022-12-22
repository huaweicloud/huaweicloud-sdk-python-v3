# coding: utf-8

import re
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
        'list_type': 'int',
        'object_id': 'str'
    }

    attribute_map = {
        'direction': 'direction',
        'address_type': 'address_type',
        'address': 'address',
        'protocol': 'protocol',
        'port': 'port',
        'list_type': 'list_type',
        'object_id': 'object_id'
    }

    def __init__(self, direction=None, address_type=None, address=None, protocol=None, port=None, list_type=None, object_id=None):
        """UpdateBlackWhiteListDto

        The model defined in huaweicloud sdk

        :param direction: 地址方向0：源地址1：目的地址
        :type direction: int
        :param address_type: 地址类型0：ipv4,1:ipv6,2:domain
        :type address_type: int
        :param address: ip地址
        :type address: str
        :param protocol: 协议类型:TCP为6, UDP为17,ICMP为1,ICMPV6为58,ANY为-1
        :type protocol: int
        :param port: 端口
        :type port: str
        :param list_type: 黑白名单类型4：黑名单，5：白名单
        :type list_type: int
        :param object_id: 防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用查询防火墙实例接口获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。具体可参考APIExlorer和帮助中心FAQ。
        :type object_id: str
        """
        
        

        self._direction = None
        self._address_type = None
        self._address = None
        self._protocol = None
        self._port = None
        self._list_type = None
        self._object_id = None
        self.discriminator = None

        if direction is not None:
            self.direction = direction
        if address_type is not None:
            self.address_type = address_type
        if address is not None:
            self.address = address
        if protocol is not None:
            self.protocol = protocol
        if port is not None:
            self.port = port
        if list_type is not None:
            self.list_type = list_type
        if object_id is not None:
            self.object_id = object_id

    @property
    def direction(self):
        """Gets the direction of this UpdateBlackWhiteListDto.

        地址方向0：源地址1：目的地址

        :return: The direction of this UpdateBlackWhiteListDto.
        :rtype: int
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this UpdateBlackWhiteListDto.

        地址方向0：源地址1：目的地址

        :param direction: The direction of this UpdateBlackWhiteListDto.
        :type direction: int
        """
        self._direction = direction

    @property
    def address_type(self):
        """Gets the address_type of this UpdateBlackWhiteListDto.

        地址类型0：ipv4,1:ipv6,2:domain

        :return: The address_type of this UpdateBlackWhiteListDto.
        :rtype: int
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """Sets the address_type of this UpdateBlackWhiteListDto.

        地址类型0：ipv4,1:ipv6,2:domain

        :param address_type: The address_type of this UpdateBlackWhiteListDto.
        :type address_type: int
        """
        self._address_type = address_type

    @property
    def address(self):
        """Gets the address of this UpdateBlackWhiteListDto.

        ip地址

        :return: The address of this UpdateBlackWhiteListDto.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this UpdateBlackWhiteListDto.

        ip地址

        :param address: The address of this UpdateBlackWhiteListDto.
        :type address: str
        """
        self._address = address

    @property
    def protocol(self):
        """Gets the protocol of this UpdateBlackWhiteListDto.

        协议类型:TCP为6, UDP为17,ICMP为1,ICMPV6为58,ANY为-1

        :return: The protocol of this UpdateBlackWhiteListDto.
        :rtype: int
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this UpdateBlackWhiteListDto.

        协议类型:TCP为6, UDP为17,ICMP为1,ICMPV6为58,ANY为-1

        :param protocol: The protocol of this UpdateBlackWhiteListDto.
        :type protocol: int
        """
        self._protocol = protocol

    @property
    def port(self):
        """Gets the port of this UpdateBlackWhiteListDto.

        端口

        :return: The port of this UpdateBlackWhiteListDto.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this UpdateBlackWhiteListDto.

        端口

        :param port: The port of this UpdateBlackWhiteListDto.
        :type port: str
        """
        self._port = port

    @property
    def list_type(self):
        """Gets the list_type of this UpdateBlackWhiteListDto.

        黑白名单类型4：黑名单，5：白名单

        :return: The list_type of this UpdateBlackWhiteListDto.
        :rtype: int
        """
        return self._list_type

    @list_type.setter
    def list_type(self, list_type):
        """Sets the list_type of this UpdateBlackWhiteListDto.

        黑白名单类型4：黑名单，5：白名单

        :param list_type: The list_type of this UpdateBlackWhiteListDto.
        :type list_type: int
        """
        self._list_type = list_type

    @property
    def object_id(self):
        """Gets the object_id of this UpdateBlackWhiteListDto.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用查询防火墙实例接口获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。具体可参考APIExlorer和帮助中心FAQ。

        :return: The object_id of this UpdateBlackWhiteListDto.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this UpdateBlackWhiteListDto.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用查询防火墙实例接口获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。具体可参考APIExlorer和帮助中心FAQ。

        :param object_id: The object_id of this UpdateBlackWhiteListDto.
        :type object_id: str
        """
        self._object_id = object_id

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
