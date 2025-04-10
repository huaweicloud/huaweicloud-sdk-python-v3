# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddBlackWhiteListDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_id': 'str',
        'list_type': 'int',
        'direction': 'int',
        'address_type': 'int',
        'address': 'str',
        'protocol': 'int',
        'port': 'str',
        'description': 'str'
    }

    attribute_map = {
        'object_id': 'object_id',
        'list_type': 'list_type',
        'direction': 'direction',
        'address_type': 'address_type',
        'address': 'address',
        'protocol': 'protocol',
        'port': 'port',
        'description': 'description'
    }

    def __init__(self, object_id=None, list_type=None, direction=None, address_type=None, address=None, protocol=None, port=None, description=None):
        r"""AddBlackWhiteListDto

        The model defined in huaweicloud sdk

        :param object_id: 防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得
        :type object_id: str
        :param list_type: 黑白名单类型4：黑名单，5：白名单
        :type list_type: int
        :param direction: 地址方向0：源地址1：目的地址
        :type direction: int
        :param address_type: ip地址类型 0：ipv4，1:ipv6
        :type address_type: int
        :param address: ip地址
        :type address: str
        :param protocol: 协议类型：TCP为6，UDP为17，ICMP为1，ICMPV6为58，ANY为-1,手动类型不为空，自动类型为空
        :type protocol: int
        :param port: 目的端口
        :type port: str
        :param description: 描述
        :type description: str
        """
        
        

        self._object_id = None
        self._list_type = None
        self._direction = None
        self._address_type = None
        self._address = None
        self._protocol = None
        self._port = None
        self._description = None
        self.discriminator = None

        self.object_id = object_id
        self.list_type = list_type
        self.direction = direction
        self.address_type = address_type
        self.address = address
        self.protocol = protocol
        self.port = port
        if description is not None:
            self.description = description

    @property
    def object_id(self):
        r"""Gets the object_id of this AddBlackWhiteListDto.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得

        :return: The object_id of this AddBlackWhiteListDto.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this AddBlackWhiteListDto.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得

        :param object_id: The object_id of this AddBlackWhiteListDto.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def list_type(self):
        r"""Gets the list_type of this AddBlackWhiteListDto.

        黑白名单类型4：黑名单，5：白名单

        :return: The list_type of this AddBlackWhiteListDto.
        :rtype: int
        """
        return self._list_type

    @list_type.setter
    def list_type(self, list_type):
        r"""Sets the list_type of this AddBlackWhiteListDto.

        黑白名单类型4：黑名单，5：白名单

        :param list_type: The list_type of this AddBlackWhiteListDto.
        :type list_type: int
        """
        self._list_type = list_type

    @property
    def direction(self):
        r"""Gets the direction of this AddBlackWhiteListDto.

        地址方向0：源地址1：目的地址

        :return: The direction of this AddBlackWhiteListDto.
        :rtype: int
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        r"""Sets the direction of this AddBlackWhiteListDto.

        地址方向0：源地址1：目的地址

        :param direction: The direction of this AddBlackWhiteListDto.
        :type direction: int
        """
        self._direction = direction

    @property
    def address_type(self):
        r"""Gets the address_type of this AddBlackWhiteListDto.

        ip地址类型 0：ipv4，1:ipv6

        :return: The address_type of this AddBlackWhiteListDto.
        :rtype: int
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        r"""Sets the address_type of this AddBlackWhiteListDto.

        ip地址类型 0：ipv4，1:ipv6

        :param address_type: The address_type of this AddBlackWhiteListDto.
        :type address_type: int
        """
        self._address_type = address_type

    @property
    def address(self):
        r"""Gets the address of this AddBlackWhiteListDto.

        ip地址

        :return: The address of this AddBlackWhiteListDto.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this AddBlackWhiteListDto.

        ip地址

        :param address: The address of this AddBlackWhiteListDto.
        :type address: str
        """
        self._address = address

    @property
    def protocol(self):
        r"""Gets the protocol of this AddBlackWhiteListDto.

        协议类型：TCP为6，UDP为17，ICMP为1，ICMPV6为58，ANY为-1,手动类型不为空，自动类型为空

        :return: The protocol of this AddBlackWhiteListDto.
        :rtype: int
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this AddBlackWhiteListDto.

        协议类型：TCP为6，UDP为17，ICMP为1，ICMPV6为58，ANY为-1,手动类型不为空，自动类型为空

        :param protocol: The protocol of this AddBlackWhiteListDto.
        :type protocol: int
        """
        self._protocol = protocol

    @property
    def port(self):
        r"""Gets the port of this AddBlackWhiteListDto.

        目的端口

        :return: The port of this AddBlackWhiteListDto.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this AddBlackWhiteListDto.

        目的端口

        :param port: The port of this AddBlackWhiteListDto.
        :type port: str
        """
        self._port = port

    @property
    def description(self):
        r"""Gets the description of this AddBlackWhiteListDto.

        描述

        :return: The description of this AddBlackWhiteListDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AddBlackWhiteListDto.

        描述

        :param description: The description of this AddBlackWhiteListDto.
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
        if not isinstance(other, AddBlackWhiteListDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
