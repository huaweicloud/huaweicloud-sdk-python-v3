# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePrivateDnatOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'transit_ip_id': 'str',
        'network_interface_id': 'str',
        'gateway_id': 'str',
        'protocol': 'str',
        'private_ip_address': 'str',
        'internal_service_port': 'str',
        'transit_service_port': 'str'
    }

    attribute_map = {
        'description': 'description',
        'transit_ip_id': 'transit_ip_id',
        'network_interface_id': 'network_interface_id',
        'gateway_id': 'gateway_id',
        'protocol': 'protocol',
        'private_ip_address': 'private_ip_address',
        'internal_service_port': 'internal_service_port',
        'transit_service_port': 'transit_service_port'
    }

    def __init__(self, description=None, transit_ip_id=None, network_interface_id=None, gateway_id=None, protocol=None, private_ip_address=None, internal_service_port=None, transit_service_port=None):
        """CreatePrivateDnatOption

        The model defined in huaweicloud sdk

        :param description: DNAT规则的描述。长度范围小于等于255个字符，不能包含“&lt;”和“&gt;”。
        :type description: str
        :param transit_ip_id: 中转IP的ID。
        :type transit_ip_id: str
        :param network_interface_id: 网络接口ID，支持计算、ELB、VIP等实例的网络接口。
        :type network_interface_id: str
        :param gateway_id: 私网NAT网关实例的ID。
        :type gateway_id: str
        :param protocol: 协议类型。 目前支持TCP/tcp、UDP/udp、ANY/any。 对应协议号6、17、0。
        :type protocol: str
        :param private_ip_address: 后端实例的私网IP地址。
        :type private_ip_address: str
        :param internal_service_port: 后端实例的端口号。
        :type internal_service_port: str
        :param transit_service_port: 中转IP的端口号。
        :type transit_service_port: str
        """
        
        

        self._description = None
        self._transit_ip_id = None
        self._network_interface_id = None
        self._gateway_id = None
        self._protocol = None
        self._private_ip_address = None
        self._internal_service_port = None
        self._transit_service_port = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.transit_ip_id = transit_ip_id
        if network_interface_id is not None:
            self.network_interface_id = network_interface_id
        self.gateway_id = gateway_id
        if protocol is not None:
            self.protocol = protocol
        if private_ip_address is not None:
            self.private_ip_address = private_ip_address
        if internal_service_port is not None:
            self.internal_service_port = internal_service_port
        if transit_service_port is not None:
            self.transit_service_port = transit_service_port

    @property
    def description(self):
        """Gets the description of this CreatePrivateDnatOption.

        DNAT规则的描述。长度范围小于等于255个字符，不能包含“<”和“>”。

        :return: The description of this CreatePrivateDnatOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreatePrivateDnatOption.

        DNAT规则的描述。长度范围小于等于255个字符，不能包含“<”和“>”。

        :param description: The description of this CreatePrivateDnatOption.
        :type description: str
        """
        self._description = description

    @property
    def transit_ip_id(self):
        """Gets the transit_ip_id of this CreatePrivateDnatOption.

        中转IP的ID。

        :return: The transit_ip_id of this CreatePrivateDnatOption.
        :rtype: str
        """
        return self._transit_ip_id

    @transit_ip_id.setter
    def transit_ip_id(self, transit_ip_id):
        """Sets the transit_ip_id of this CreatePrivateDnatOption.

        中转IP的ID。

        :param transit_ip_id: The transit_ip_id of this CreatePrivateDnatOption.
        :type transit_ip_id: str
        """
        self._transit_ip_id = transit_ip_id

    @property
    def network_interface_id(self):
        """Gets the network_interface_id of this CreatePrivateDnatOption.

        网络接口ID，支持计算、ELB、VIP等实例的网络接口。

        :return: The network_interface_id of this CreatePrivateDnatOption.
        :rtype: str
        """
        return self._network_interface_id

    @network_interface_id.setter
    def network_interface_id(self, network_interface_id):
        """Sets the network_interface_id of this CreatePrivateDnatOption.

        网络接口ID，支持计算、ELB、VIP等实例的网络接口。

        :param network_interface_id: The network_interface_id of this CreatePrivateDnatOption.
        :type network_interface_id: str
        """
        self._network_interface_id = network_interface_id

    @property
    def gateway_id(self):
        """Gets the gateway_id of this CreatePrivateDnatOption.

        私网NAT网关实例的ID。

        :return: The gateway_id of this CreatePrivateDnatOption.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """Sets the gateway_id of this CreatePrivateDnatOption.

        私网NAT网关实例的ID。

        :param gateway_id: The gateway_id of this CreatePrivateDnatOption.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

    @property
    def protocol(self):
        """Gets the protocol of this CreatePrivateDnatOption.

        协议类型。 目前支持TCP/tcp、UDP/udp、ANY/any。 对应协议号6、17、0。

        :return: The protocol of this CreatePrivateDnatOption.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this CreatePrivateDnatOption.

        协议类型。 目前支持TCP/tcp、UDP/udp、ANY/any。 对应协议号6、17、0。

        :param protocol: The protocol of this CreatePrivateDnatOption.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def private_ip_address(self):
        """Gets the private_ip_address of this CreatePrivateDnatOption.

        后端实例的私网IP地址。

        :return: The private_ip_address of this CreatePrivateDnatOption.
        :rtype: str
        """
        return self._private_ip_address

    @private_ip_address.setter
    def private_ip_address(self, private_ip_address):
        """Sets the private_ip_address of this CreatePrivateDnatOption.

        后端实例的私网IP地址。

        :param private_ip_address: The private_ip_address of this CreatePrivateDnatOption.
        :type private_ip_address: str
        """
        self._private_ip_address = private_ip_address

    @property
    def internal_service_port(self):
        """Gets the internal_service_port of this CreatePrivateDnatOption.

        后端实例的端口号。

        :return: The internal_service_port of this CreatePrivateDnatOption.
        :rtype: str
        """
        return self._internal_service_port

    @internal_service_port.setter
    def internal_service_port(self, internal_service_port):
        """Sets the internal_service_port of this CreatePrivateDnatOption.

        后端实例的端口号。

        :param internal_service_port: The internal_service_port of this CreatePrivateDnatOption.
        :type internal_service_port: str
        """
        self._internal_service_port = internal_service_port

    @property
    def transit_service_port(self):
        """Gets the transit_service_port of this CreatePrivateDnatOption.

        中转IP的端口号。

        :return: The transit_service_port of this CreatePrivateDnatOption.
        :rtype: str
        """
        return self._transit_service_port

    @transit_service_port.setter
    def transit_service_port(self, transit_service_port):
        """Sets the transit_service_port of this CreatePrivateDnatOption.

        中转IP的端口号。

        :param transit_service_port: The transit_service_port of this CreatePrivateDnatOption.
        :type transit_service_port: str
        """
        self._transit_service_port = transit_service_port

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
        if not isinstance(other, CreatePrivateDnatOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
