# coding: utf-8

import pprint
import re

import six





class NatGatewayDnatRuleResponseBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'tenant_id': 'str',
        'description': 'str',
        'port_id': 'str',
        'private_ip': 'str',
        'internal_service_port': 'int',
        'nat_gateway_id': 'str',
        'floating_ip_id': 'str',
        'floating_ip_address': 'str',
        'external_service_port': 'int',
        'status': 'str',
        'admin_state_up': 'bool',
        'internal_service_port_range': 'str',
        'external_service_port_range': 'str',
        'protocol': 'str',
        'created_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'tenant_id': 'tenant_id',
        'description': 'description',
        'port_id': 'port_id',
        'private_ip': 'private_ip',
        'internal_service_port': 'internal_service_port',
        'nat_gateway_id': 'nat_gateway_id',
        'floating_ip_id': 'floating_ip_id',
        'floating_ip_address': 'floating_ip_address',
        'external_service_port': 'external_service_port',
        'status': 'status',
        'admin_state_up': 'admin_state_up',
        'internal_service_port_range': 'internal_service_port_range',
        'external_service_port_range': 'external_service_port_range',
        'protocol': 'protocol',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, tenant_id=None, description=None, port_id=None, private_ip=None, internal_service_port=None, nat_gateway_id=None, floating_ip_id=None, floating_ip_address=None, external_service_port=None, status=None, admin_state_up=None, internal_service_port_range=None, external_service_port_range=None, protocol=None, created_at=None):
        """NatGatewayDnatRuleResponseBody - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._tenant_id = None
        self._description = None
        self._port_id = None
        self._private_ip = None
        self._internal_service_port = None
        self._nat_gateway_id = None
        self._floating_ip_id = None
        self._floating_ip_address = None
        self._external_service_port = None
        self._status = None
        self._admin_state_up = None
        self._internal_service_port_range = None
        self._external_service_port_range = None
        self._protocol = None
        self._created_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if description is not None:
            self.description = description
        if port_id is not None:
            self.port_id = port_id
        if private_ip is not None:
            self.private_ip = private_ip
        if internal_service_port is not None:
            self.internal_service_port = internal_service_port
        if nat_gateway_id is not None:
            self.nat_gateway_id = nat_gateway_id
        if floating_ip_id is not None:
            self.floating_ip_id = floating_ip_id
        if floating_ip_address is not None:
            self.floating_ip_address = floating_ip_address
        if external_service_port is not None:
            self.external_service_port = external_service_port
        if status is not None:
            self.status = status
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if internal_service_port_range is not None:
            self.internal_service_port_range = internal_service_port_range
        if external_service_port_range is not None:
            self.external_service_port_range = external_service_port_range
        if protocol is not None:
            self.protocol = protocol
        if created_at is not None:
            self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this NatGatewayDnatRuleResponseBody.

        DNAT规则的ID。

        :return: The id of this NatGatewayDnatRuleResponseBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NatGatewayDnatRuleResponseBody.

        DNAT规则的ID。

        :param id: The id of this NatGatewayDnatRuleResponseBody.
        :type: str
        """
        self._id = id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NatGatewayDnatRuleResponseBody.

        项目的ID。

        :return: The tenant_id of this NatGatewayDnatRuleResponseBody.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NatGatewayDnatRuleResponseBody.

        项目的ID。

        :param tenant_id: The tenant_id of this NatGatewayDnatRuleResponseBody.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def description(self):
        """Gets the description of this NatGatewayDnatRuleResponseBody.

        DNAT规则的描述。

        :return: The description of this NatGatewayDnatRuleResponseBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NatGatewayDnatRuleResponseBody.

        DNAT规则的描述。

        :param description: The description of this NatGatewayDnatRuleResponseBody.
        :type: str
        """
        self._description = description

    @property
    def port_id(self):
        """Gets the port_id of this NatGatewayDnatRuleResponseBody.

        虚拟机或者裸机的Port ID，与private_ip参数二选一。

        :return: The port_id of this NatGatewayDnatRuleResponseBody.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this NatGatewayDnatRuleResponseBody.

        虚拟机或者裸机的Port ID，与private_ip参数二选一。

        :param port_id: The port_id of this NatGatewayDnatRuleResponseBody.
        :type: str
        """
        self._port_id = port_id

    @property
    def private_ip(self):
        """Gets the private_ip of this NatGatewayDnatRuleResponseBody.

        用户私有IP地址，例如专线连接的私有云地址，与port_id参数二选一。

        :return: The private_ip of this NatGatewayDnatRuleResponseBody.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this NatGatewayDnatRuleResponseBody.

        用户私有IP地址，例如专线连接的私有云地址，与port_id参数二选一。

        :param private_ip: The private_ip of this NatGatewayDnatRuleResponseBody.
        :type: str
        """
        self._private_ip = private_ip

    @property
    def internal_service_port(self):
        """Gets the internal_service_port of this NatGatewayDnatRuleResponseBody.

        虚拟机或者裸机对外提供服务的协议端口号。 取值范围：0~65535。

        :return: The internal_service_port of this NatGatewayDnatRuleResponseBody.
        :rtype: int
        """
        return self._internal_service_port

    @internal_service_port.setter
    def internal_service_port(self, internal_service_port):
        """Sets the internal_service_port of this NatGatewayDnatRuleResponseBody.

        虚拟机或者裸机对外提供服务的协议端口号。 取值范围：0~65535。

        :param internal_service_port: The internal_service_port of this NatGatewayDnatRuleResponseBody.
        :type: int
        """
        self._internal_service_port = internal_service_port

    @property
    def nat_gateway_id(self):
        """Gets the nat_gateway_id of this NatGatewayDnatRuleResponseBody.

        公网NAT网关实例的ID。

        :return: The nat_gateway_id of this NatGatewayDnatRuleResponseBody.
        :rtype: str
        """
        return self._nat_gateway_id

    @nat_gateway_id.setter
    def nat_gateway_id(self, nat_gateway_id):
        """Sets the nat_gateway_id of this NatGatewayDnatRuleResponseBody.

        公网NAT网关实例的ID。

        :param nat_gateway_id: The nat_gateway_id of this NatGatewayDnatRuleResponseBody.
        :type: str
        """
        self._nat_gateway_id = nat_gateway_id

    @property
    def floating_ip_id(self):
        """Gets the floating_ip_id of this NatGatewayDnatRuleResponseBody.

        弹性公网IP的id。

        :return: The floating_ip_id of this NatGatewayDnatRuleResponseBody.
        :rtype: str
        """
        return self._floating_ip_id

    @floating_ip_id.setter
    def floating_ip_id(self, floating_ip_id):
        """Sets the floating_ip_id of this NatGatewayDnatRuleResponseBody.

        弹性公网IP的id。

        :param floating_ip_id: The floating_ip_id of this NatGatewayDnatRuleResponseBody.
        :type: str
        """
        self._floating_ip_id = floating_ip_id

    @property
    def floating_ip_address(self):
        """Gets the floating_ip_address of this NatGatewayDnatRuleResponseBody.

        弹性公网IP的IP地址。 

        :return: The floating_ip_address of this NatGatewayDnatRuleResponseBody.
        :rtype: str
        """
        return self._floating_ip_address

    @floating_ip_address.setter
    def floating_ip_address(self, floating_ip_address):
        """Sets the floating_ip_address of this NatGatewayDnatRuleResponseBody.

        弹性公网IP的IP地址。 

        :param floating_ip_address: The floating_ip_address of this NatGatewayDnatRuleResponseBody.
        :type: str
        """
        self._floating_ip_address = floating_ip_address

    @property
    def external_service_port(self):
        """Gets the external_service_port of this NatGatewayDnatRuleResponseBody.

        Floatingip对外提供服务的端口号。 取值范围：0~65535。

        :return: The external_service_port of this NatGatewayDnatRuleResponseBody.
        :rtype: int
        """
        return self._external_service_port

    @external_service_port.setter
    def external_service_port(self, external_service_port):
        """Sets the external_service_port of this NatGatewayDnatRuleResponseBody.

        Floatingip对外提供服务的端口号。 取值范围：0~65535。

        :param external_service_port: The external_service_port of this NatGatewayDnatRuleResponseBody.
        :type: int
        """
        self._external_service_port = external_service_port

    @property
    def status(self):
        """Gets the status of this NatGatewayDnatRuleResponseBody.

        功能说明：DNAT规则的状态。

        :return: The status of this NatGatewayDnatRuleResponseBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NatGatewayDnatRuleResponseBody.

        功能说明：DNAT规则的状态。

        :param status: The status of this NatGatewayDnatRuleResponseBody.
        :type: str
        """
        self._status = status

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this NatGatewayDnatRuleResponseBody.

        解冻/冻结状态。 取值范围： − “true”： 解冻 − “false”： 冻结 

        :return: The admin_state_up of this NatGatewayDnatRuleResponseBody.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this NatGatewayDnatRuleResponseBody.

        解冻/冻结状态。 取值范围： − “true”： 解冻 − “false”： 冻结 

        :param admin_state_up: The admin_state_up of this NatGatewayDnatRuleResponseBody.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def internal_service_port_range(self):
        """Gets the internal_service_port_range of this NatGatewayDnatRuleResponseBody.

        虚拟机或者裸机对外提供服务的协议端口号范围。 功能说明：该端口范围与external _service_port_range按顺序实现1:1映射。 取值范围：1~65535。 约束：只能以’-’字符连接端口范围。 

        :return: The internal_service_port_range of this NatGatewayDnatRuleResponseBody.
        :rtype: str
        """
        return self._internal_service_port_range

    @internal_service_port_range.setter
    def internal_service_port_range(self, internal_service_port_range):
        """Sets the internal_service_port_range of this NatGatewayDnatRuleResponseBody.

        虚拟机或者裸机对外提供服务的协议端口号范围。 功能说明：该端口范围与external _service_port_range按顺序实现1:1映射。 取值范围：1~65535。 约束：只能以’-’字符连接端口范围。 

        :param internal_service_port_range: The internal_service_port_range of this NatGatewayDnatRuleResponseBody.
        :type: str
        """
        self._internal_service_port_range = internal_service_port_range

    @property
    def external_service_port_range(self):
        """Gets the external_service_port_range of this NatGatewayDnatRuleResponseBody.

        Floatingip对外提供服务的端口号范围。 功能说明：该端口范围与internal _service_port_range按顺序实现1:1映射。 取值范围：1~65535。 约束：只能以’-’字符连接端口范围 

        :return: The external_service_port_range of this NatGatewayDnatRuleResponseBody.
        :rtype: str
        """
        return self._external_service_port_range

    @external_service_port_range.setter
    def external_service_port_range(self, external_service_port_range):
        """Sets the external_service_port_range of this NatGatewayDnatRuleResponseBody.

        Floatingip对外提供服务的端口号范围。 功能说明：该端口范围与internal _service_port_range按顺序实现1:1映射。 取值范围：1~65535。 约束：只能以’-’字符连接端口范围 

        :param external_service_port_range: The external_service_port_range of this NatGatewayDnatRuleResponseBody.
        :type: str
        """
        self._external_service_port_range = external_service_port_range

    @property
    def protocol(self):
        """Gets the protocol of this NatGatewayDnatRuleResponseBody.

        协议类型，目前支持TCP/tcp、UDP/udp、ANY/any。 对应协议号6、17、0。 

        :return: The protocol of this NatGatewayDnatRuleResponseBody.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this NatGatewayDnatRuleResponseBody.

        协议类型，目前支持TCP/tcp、UDP/udp、ANY/any。 对应协议号6、17、0。 

        :param protocol: The protocol of this NatGatewayDnatRuleResponseBody.
        :type: str
        """
        self._protocol = protocol

    @property
    def created_at(self):
        """Gets the created_at of this NatGatewayDnatRuleResponseBody.

        DNAT规则的创建时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。

        :return: The created_at of this NatGatewayDnatRuleResponseBody.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this NatGatewayDnatRuleResponseBody.

        DNAT规则的创建时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。

        :param created_at: The created_at of this NatGatewayDnatRuleResponseBody.
        :type: datetime
        """
        self._created_at = created_at

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
        if not isinstance(other, NatGatewayDnatRuleResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
