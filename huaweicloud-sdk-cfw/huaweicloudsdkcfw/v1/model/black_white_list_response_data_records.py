# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BlackWhiteListResponseDataRecords:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'list_id': 'str',
        'direction': 'int',
        'address_type': 'int',
        'address': 'str',
        'protocol': 'int',
        'port': 'str',
        'description': 'str'
    }

    attribute_map = {
        'list_id': 'list_id',
        'direction': 'direction',
        'address_type': 'address_type',
        'address': 'address',
        'protocol': 'protocol',
        'port': 'port',
        'description': 'description'
    }

    def __init__(self, list_id=None, direction=None, address_type=None, address=None, protocol=None, port=None, description=None):
        """BlackWhiteListResponseDataRecords

        The model defined in huaweicloud sdk

        :param list_id: 黑白名单列表id
        :type list_id: str
        :param direction: 黑白地址方向0：源地址1：目的地址
        :type direction: int
        :param address_type: IP地址类型0：ipv4,1:ipv6,2:domain
        :type address_type: int
        :param address: ip地址
        :type address: str
        :param protocol: 协议类型:TCP为6,UDP为17,ICMP为1,ICMPV6为58,ANY为-1,手动类型不为空，自动类型为空
        :type protocol: int
        :param port: 端口
        :type port: str
        :param description: 描述
        :type description: str
        """
        
        

        self._list_id = None
        self._direction = None
        self._address_type = None
        self._address = None
        self._protocol = None
        self._port = None
        self._description = None
        self.discriminator = None

        if list_id is not None:
            self.list_id = list_id
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
        if description is not None:
            self.description = description

    @property
    def list_id(self):
        """Gets the list_id of this BlackWhiteListResponseDataRecords.

        黑白名单列表id

        :return: The list_id of this BlackWhiteListResponseDataRecords.
        :rtype: str
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this BlackWhiteListResponseDataRecords.

        黑白名单列表id

        :param list_id: The list_id of this BlackWhiteListResponseDataRecords.
        :type list_id: str
        """
        self._list_id = list_id

    @property
    def direction(self):
        """Gets the direction of this BlackWhiteListResponseDataRecords.

        黑白地址方向0：源地址1：目的地址

        :return: The direction of this BlackWhiteListResponseDataRecords.
        :rtype: int
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this BlackWhiteListResponseDataRecords.

        黑白地址方向0：源地址1：目的地址

        :param direction: The direction of this BlackWhiteListResponseDataRecords.
        :type direction: int
        """
        self._direction = direction

    @property
    def address_type(self):
        """Gets the address_type of this BlackWhiteListResponseDataRecords.

        IP地址类型0：ipv4,1:ipv6,2:domain

        :return: The address_type of this BlackWhiteListResponseDataRecords.
        :rtype: int
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """Sets the address_type of this BlackWhiteListResponseDataRecords.

        IP地址类型0：ipv4,1:ipv6,2:domain

        :param address_type: The address_type of this BlackWhiteListResponseDataRecords.
        :type address_type: int
        """
        self._address_type = address_type

    @property
    def address(self):
        """Gets the address of this BlackWhiteListResponseDataRecords.

        ip地址

        :return: The address of this BlackWhiteListResponseDataRecords.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this BlackWhiteListResponseDataRecords.

        ip地址

        :param address: The address of this BlackWhiteListResponseDataRecords.
        :type address: str
        """
        self._address = address

    @property
    def protocol(self):
        """Gets the protocol of this BlackWhiteListResponseDataRecords.

        协议类型:TCP为6,UDP为17,ICMP为1,ICMPV6为58,ANY为-1,手动类型不为空，自动类型为空

        :return: The protocol of this BlackWhiteListResponseDataRecords.
        :rtype: int
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this BlackWhiteListResponseDataRecords.

        协议类型:TCP为6,UDP为17,ICMP为1,ICMPV6为58,ANY为-1,手动类型不为空，自动类型为空

        :param protocol: The protocol of this BlackWhiteListResponseDataRecords.
        :type protocol: int
        """
        self._protocol = protocol

    @property
    def port(self):
        """Gets the port of this BlackWhiteListResponseDataRecords.

        端口

        :return: The port of this BlackWhiteListResponseDataRecords.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this BlackWhiteListResponseDataRecords.

        端口

        :param port: The port of this BlackWhiteListResponseDataRecords.
        :type port: str
        """
        self._port = port

    @property
    def description(self):
        """Gets the description of this BlackWhiteListResponseDataRecords.

        描述

        :return: The description of this BlackWhiteListResponseDataRecords.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BlackWhiteListResponseDataRecords.

        描述

        :param description: The description of this BlackWhiteListResponseDataRecords.
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
        if not isinstance(other, BlackWhiteListResponseDataRecords):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
