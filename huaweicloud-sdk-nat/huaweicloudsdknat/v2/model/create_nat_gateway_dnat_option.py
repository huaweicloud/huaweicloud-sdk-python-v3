# coding: utf-8

import pprint
import re

import six





class CreateNatGatewayDnatOption:


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
        'port_id': 'str',
        'private_ip': 'str',
        'nat_gateway_id': 'str',
        'internal_service_port': 'int',
        'floating_ip_id': 'str',
        'external_service_port': 'int',
        'protocol': 'str',
        'internal_service_port_range': 'str',
        'external_service_port_range': 'str'
    }

    attribute_map = {
        'description': 'description',
        'port_id': 'port_id',
        'private_ip': 'private_ip',
        'nat_gateway_id': 'nat_gateway_id',
        'internal_service_port': 'internal_service_port',
        'floating_ip_id': 'floating_ip_id',
        'external_service_port': 'external_service_port',
        'protocol': 'protocol',
        'internal_service_port_range': 'internal_service_port_range',
        'external_service_port_range': 'external_service_port_range'
    }

    def __init__(self, description=None, port_id=None, private_ip=None, nat_gateway_id=None, internal_service_port=None, floating_ip_id=None, external_service_port=None, protocol=None, internal_service_port_range=None, external_service_port_range=None):
        """CreateNatGatewayDnatOption - a model defined in huaweicloud sdk"""
        
        

        self._description = None
        self._port_id = None
        self._private_ip = None
        self._nat_gateway_id = None
        self._internal_service_port = None
        self._floating_ip_id = None
        self._external_service_port = None
        self._protocol = None
        self._internal_service_port_range = None
        self._external_service_port_range = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if port_id is not None:
            self.port_id = port_id
        if private_ip is not None:
            self.private_ip = private_ip
        if nat_gateway_id is not None:
            self.nat_gateway_id = nat_gateway_id
        if internal_service_port is not None:
            self.internal_service_port = internal_service_port
        if floating_ip_id is not None:
            self.floating_ip_id = floating_ip_id
        if external_service_port is not None:
            self.external_service_port = external_service_port
        if protocol is not None:
            self.protocol = protocol
        if internal_service_port_range is not None:
            self.internal_service_port_range = internal_service_port_range
        if external_service_port_range is not None:
            self.external_service_port_range = external_service_port_range

    @property
    def description(self):
        """Gets the description of this CreateNatGatewayDnatOption.

        DNAT规则的描述。

        :return: The description of this CreateNatGatewayDnatOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateNatGatewayDnatOption.

        DNAT规则的描述。

        :param description: The description of this CreateNatGatewayDnatOption.
        :type: str
        """
        self._description = description

    @property
    def port_id(self):
        """Gets the port_id of this CreateNatGatewayDnatOption.

        虚拟机或者裸机的Port ID，与private_ip参数二选一。

        :return: The port_id of this CreateNatGatewayDnatOption.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this CreateNatGatewayDnatOption.

        虚拟机或者裸机的Port ID，与private_ip参数二选一。

        :param port_id: The port_id of this CreateNatGatewayDnatOption.
        :type: str
        """
        self._port_id = port_id

    @property
    def private_ip(self):
        """Gets the private_ip of this CreateNatGatewayDnatOption.

        用户私有IP地址，例如专线连接的私有云地址，与port_id参数二选一。

        :return: The private_ip of this CreateNatGatewayDnatOption.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this CreateNatGatewayDnatOption.

        用户私有IP地址，例如专线连接的私有云地址，与port_id参数二选一。

        :param private_ip: The private_ip of this CreateNatGatewayDnatOption.
        :type: str
        """
        self._private_ip = private_ip

    @property
    def nat_gateway_id(self):
        """Gets the nat_gateway_id of this CreateNatGatewayDnatOption.

        公网NAT网关实例的ID。

        :return: The nat_gateway_id of this CreateNatGatewayDnatOption.
        :rtype: str
        """
        return self._nat_gateway_id

    @nat_gateway_id.setter
    def nat_gateway_id(self, nat_gateway_id):
        """Sets the nat_gateway_id of this CreateNatGatewayDnatOption.

        公网NAT网关实例的ID。

        :param nat_gateway_id: The nat_gateway_id of this CreateNatGatewayDnatOption.
        :type: str
        """
        self._nat_gateway_id = nat_gateway_id

    @property
    def internal_service_port(self):
        """Gets the internal_service_port of this CreateNatGatewayDnatOption.

        虚拟机或者裸机对外提供服务的协议端口号。 取值范围：0~65535。

        :return: The internal_service_port of this CreateNatGatewayDnatOption.
        :rtype: int
        """
        return self._internal_service_port

    @internal_service_port.setter
    def internal_service_port(self, internal_service_port):
        """Sets the internal_service_port of this CreateNatGatewayDnatOption.

        虚拟机或者裸机对外提供服务的协议端口号。 取值范围：0~65535。

        :param internal_service_port: The internal_service_port of this CreateNatGatewayDnatOption.
        :type: int
        """
        self._internal_service_port = internal_service_port

    @property
    def floating_ip_id(self):
        """Gets the floating_ip_id of this CreateNatGatewayDnatOption.

        弹性公网IP的id。

        :return: The floating_ip_id of this CreateNatGatewayDnatOption.
        :rtype: str
        """
        return self._floating_ip_id

    @floating_ip_id.setter
    def floating_ip_id(self, floating_ip_id):
        """Sets the floating_ip_id of this CreateNatGatewayDnatOption.

        弹性公网IP的id。

        :param floating_ip_id: The floating_ip_id of this CreateNatGatewayDnatOption.
        :type: str
        """
        self._floating_ip_id = floating_ip_id

    @property
    def external_service_port(self):
        """Gets the external_service_port of this CreateNatGatewayDnatOption.

        Floatingip对外提供服务的端口号。 取值范围：0~65535。

        :return: The external_service_port of this CreateNatGatewayDnatOption.
        :rtype: int
        """
        return self._external_service_port

    @external_service_port.setter
    def external_service_port(self, external_service_port):
        """Sets the external_service_port of this CreateNatGatewayDnatOption.

        Floatingip对外提供服务的端口号。 取值范围：0~65535。

        :param external_service_port: The external_service_port of this CreateNatGatewayDnatOption.
        :type: int
        """
        self._external_service_port = external_service_port

    @property
    def protocol(self):
        """Gets the protocol of this CreateNatGatewayDnatOption.

        协议类型，目前支持TCP/tcp、UDP/udp、ANY/any。 对应协议号6、17、0。

        :return: The protocol of this CreateNatGatewayDnatOption.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this CreateNatGatewayDnatOption.

        协议类型，目前支持TCP/tcp、UDP/udp、ANY/any。 对应协议号6、17、0。

        :param protocol: The protocol of this CreateNatGatewayDnatOption.
        :type: str
        """
        self._protocol = protocol

    @property
    def internal_service_port_range(self):
        """Gets the internal_service_port_range of this CreateNatGatewayDnatOption.

        虚拟机或者裸机对外提供服务的协议端口号范围。 功能说明：该端口范围与external _service_port_range按顺序实现1:1映射。 取值范围：1~65535。 约束：只能以’-’字符连接端口范围。 

        :return: The internal_service_port_range of this CreateNatGatewayDnatOption.
        :rtype: str
        """
        return self._internal_service_port_range

    @internal_service_port_range.setter
    def internal_service_port_range(self, internal_service_port_range):
        """Sets the internal_service_port_range of this CreateNatGatewayDnatOption.

        虚拟机或者裸机对外提供服务的协议端口号范围。 功能说明：该端口范围与external _service_port_range按顺序实现1:1映射。 取值范围：1~65535。 约束：只能以’-’字符连接端口范围。 

        :param internal_service_port_range: The internal_service_port_range of this CreateNatGatewayDnatOption.
        :type: str
        """
        self._internal_service_port_range = internal_service_port_range

    @property
    def external_service_port_range(self):
        """Gets the external_service_port_range of this CreateNatGatewayDnatOption.

        Floatingip对外提供服务的端口号范围。 功能说明：该端口范围与internal _service_port_range按顺序实现1:1映射。 取值范围：1~65535。 约束：只能以’-’字符连接端口范围。 

        :return: The external_service_port_range of this CreateNatGatewayDnatOption.
        :rtype: str
        """
        return self._external_service_port_range

    @external_service_port_range.setter
    def external_service_port_range(self, external_service_port_range):
        """Sets the external_service_port_range of this CreateNatGatewayDnatOption.

        Floatingip对外提供服务的端口号范围。 功能说明：该端口范围与internal _service_port_range按顺序实现1:1映射。 取值范围：1~65535。 约束：只能以’-’字符连接端口范围。 

        :param external_service_port_range: The external_service_port_range of this CreateNatGatewayDnatOption.
        :type: str
        """
        self._external_service_port_range = external_service_port_range

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateNatGatewayDnatOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
