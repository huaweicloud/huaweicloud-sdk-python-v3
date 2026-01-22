# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BlackWhiteInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'address': 'str',
        'address_type': 'int',
        'description': 'str',
        'direction': 'int',
        'port': 'str',
        'protocol': 'int'
    }

    attribute_map = {
        'address': 'address',
        'address_type': 'address_type',
        'description': 'description',
        'direction': 'direction',
        'port': 'port',
        'protocol': 'protocol'
    }

    def __init__(self, address=None, address_type=None, description=None, direction=None, port=None, protocol=None):
        r"""BlackWhiteInfo

        The model defined in huaweicloud sdk

        :param address: **参数解释**： IP地址 **约束限制**： 不涉及  **取值范围**： 不涉及 **默认取值**： 不涉及
        :type address: str
        :param address_type: **参数解释**： IP地址类型 **约束限制**： 不涉及  **取值范围**：  0：IPV4  1：IPV6 **默认取值**： 不涉及
        :type address_type: int
        :param description: **参数解释**： 描述 **约束限制**： 不涉及  **取值范围**： 不涉及 **默认取值**： 不涉及
        :type description: str
        :param direction: **参数解释**： 地址方向 **约束限制**： 不涉及  **取值范围**： 0：源地址 1：目的地址 **默认取值**： 不涉及
        :type direction: int
        :param port: **参数解释**： 端口 **约束限制**： 不涉及  **取值范围**： 不涉及 **默认取值**： 不涉及
        :type port: str
        :param protocol: **参数解释**： 协议类型 **约束限制**： 不涉及  **取值范围**： -1：ANY 1：ICMP 6：TCP 17：UDP 58：ICMPV6 132：SCTP 手动类型不为空，自动类型为空 **默认取值**： 不涉及
        :type protocol: int
        """
        
        

        self._address = None
        self._address_type = None
        self._description = None
        self._direction = None
        self._port = None
        self._protocol = None
        self.discriminator = None

        self.address = address
        if address_type is not None:
            self.address_type = address_type
        if description is not None:
            self.description = description
        self.direction = direction
        if port is not None:
            self.port = port
        self.protocol = protocol

    @property
    def address(self):
        r"""Gets the address of this BlackWhiteInfo.

        **参数解释**： IP地址 **约束限制**： 不涉及  **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The address of this BlackWhiteInfo.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this BlackWhiteInfo.

        **参数解释**： IP地址 **约束限制**： 不涉及  **取值范围**： 不涉及 **默认取值**： 不涉及

        :param address: The address of this BlackWhiteInfo.
        :type address: str
        """
        self._address = address

    @property
    def address_type(self):
        r"""Gets the address_type of this BlackWhiteInfo.

        **参数解释**： IP地址类型 **约束限制**： 不涉及  **取值范围**：  0：IPV4  1：IPV6 **默认取值**： 不涉及

        :return: The address_type of this BlackWhiteInfo.
        :rtype: int
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        r"""Sets the address_type of this BlackWhiteInfo.

        **参数解释**： IP地址类型 **约束限制**： 不涉及  **取值范围**：  0：IPV4  1：IPV6 **默认取值**： 不涉及

        :param address_type: The address_type of this BlackWhiteInfo.
        :type address_type: int
        """
        self._address_type = address_type

    @property
    def description(self):
        r"""Gets the description of this BlackWhiteInfo.

        **参数解释**： 描述 **约束限制**： 不涉及  **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The description of this BlackWhiteInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BlackWhiteInfo.

        **参数解释**： 描述 **约束限制**： 不涉及  **取值范围**： 不涉及 **默认取值**： 不涉及

        :param description: The description of this BlackWhiteInfo.
        :type description: str
        """
        self._description = description

    @property
    def direction(self):
        r"""Gets the direction of this BlackWhiteInfo.

        **参数解释**： 地址方向 **约束限制**： 不涉及  **取值范围**： 0：源地址 1：目的地址 **默认取值**： 不涉及

        :return: The direction of this BlackWhiteInfo.
        :rtype: int
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        r"""Sets the direction of this BlackWhiteInfo.

        **参数解释**： 地址方向 **约束限制**： 不涉及  **取值范围**： 0：源地址 1：目的地址 **默认取值**： 不涉及

        :param direction: The direction of this BlackWhiteInfo.
        :type direction: int
        """
        self._direction = direction

    @property
    def port(self):
        r"""Gets the port of this BlackWhiteInfo.

        **参数解释**： 端口 **约束限制**： 不涉及  **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The port of this BlackWhiteInfo.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this BlackWhiteInfo.

        **参数解释**： 端口 **约束限制**： 不涉及  **取值范围**： 不涉及 **默认取值**： 不涉及

        :param port: The port of this BlackWhiteInfo.
        :type port: str
        """
        self._port = port

    @property
    def protocol(self):
        r"""Gets the protocol of this BlackWhiteInfo.

        **参数解释**： 协议类型 **约束限制**： 不涉及  **取值范围**： -1：ANY 1：ICMP 6：TCP 17：UDP 58：ICMPV6 132：SCTP 手动类型不为空，自动类型为空 **默认取值**： 不涉及

        :return: The protocol of this BlackWhiteInfo.
        :rtype: int
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this BlackWhiteInfo.

        **参数解释**： 协议类型 **约束限制**： 不涉及  **取值范围**： -1：ANY 1：ICMP 6：TCP 17：UDP 58：ICMPV6 132：SCTP 手动类型不为空，自动类型为空 **默认取值**： 不涉及

        :param protocol: The protocol of this BlackWhiteInfo.
        :type protocol: int
        """
        self._protocol = protocol

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BlackWhiteInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
