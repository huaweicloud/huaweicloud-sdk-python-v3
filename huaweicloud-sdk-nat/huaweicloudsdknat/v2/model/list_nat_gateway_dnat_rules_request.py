# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNatGatewayDnatRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'admin_state_up': 'bool',
        'external_service_port': 'int',
        'floating_ip_address': 'str',
        'status': 'list[str]',
        'floating_ip_id': 'str',
        'internal_service_port': 'int',
        'limit': 'int',
        'id': 'str',
        'description': 'str',
        'created_at': 'str',
        'nat_gateway_id': 'list[str]',
        'port_id': 'str',
        'private_ip': 'str',
        'protocol': 'list[str]'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'external_service_port': 'external_service_port',
        'floating_ip_address': 'floating_ip_address',
        'status': 'status',
        'floating_ip_id': 'floating_ip_id',
        'internal_service_port': 'internal_service_port',
        'limit': 'limit',
        'id': 'id',
        'description': 'description',
        'created_at': 'created_at',
        'nat_gateway_id': 'nat_gateway_id',
        'port_id': 'port_id',
        'private_ip': 'private_ip',
        'protocol': 'protocol'
    }

    def __init__(self, admin_state_up=None, external_service_port=None, floating_ip_address=None, status=None, floating_ip_id=None, internal_service_port=None, limit=None, id=None, description=None, created_at=None, nat_gateway_id=None, port_id=None, private_ip=None, protocol=None):
        """ListNatGatewayDnatRulesRequest

        The model defined in huaweicloud sdk

        :param admin_state_up: 解冻/冻结状态。 取值范围： \&quot;true\&quot;：解冻 \&quot;false\&quot;：冻结
        :type admin_state_up: bool
        :param external_service_port: Floatingip对外提供服务的端口号。 取值范围：0~65535。
        :type external_service_port: int
        :param floating_ip_address: 弹性公网的IP地址。
        :type floating_ip_address: str
        :param status: Dnat规则的状态。
        :type status: list[str]
        :param floating_ip_id: 弹性公网IP的id。
        :type floating_ip_id: str
        :param internal_service_port: 虚拟机或者裸机对外提供服务的协议端口号。 取值范围：0~65535。
        :type internal_service_port: int
        :param limit: 功能说明：每页返回的个数。 取值范围：0~2000。 默认值：2000。
        :type limit: int
        :param id: DNAT规则的ID。
        :type id: str
        :param description: DNAT规则的描述，长度限制为255。
        :type description: str
        :param created_at: DNAT规则的创建时间，格式是yyyy-mm-dd hh:mm:ss.SSSSSS。
        :type created_at: str
        :param nat_gateway_id: 公网NAT网关实例的ID。
        :type nat_gateway_id: list[str]
        :param port_id: 虚拟机或者裸机的Port ID，对应虚拟私有云场景，与private_ip参数二选一。
        :type port_id: str
        :param private_ip: 用户私有IP地址，对应专线、云连接场景，与port_id参数二选一。
        :type private_ip: str
        :param protocol: 协议类型，目前支持TCP/tcp、UDP/udp、ANY/any。 对应协议号6、17、0。
        :type protocol: list[str]
        """
        
        

        self._admin_state_up = None
        self._external_service_port = None
        self._floating_ip_address = None
        self._status = None
        self._floating_ip_id = None
        self._internal_service_port = None
        self._limit = None
        self._id = None
        self._description = None
        self._created_at = None
        self._nat_gateway_id = None
        self._port_id = None
        self._private_ip = None
        self._protocol = None
        self.discriminator = None

        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if external_service_port is not None:
            self.external_service_port = external_service_port
        if floating_ip_address is not None:
            self.floating_ip_address = floating_ip_address
        if status is not None:
            self.status = status
        if floating_ip_id is not None:
            self.floating_ip_id = floating_ip_id
        if internal_service_port is not None:
            self.internal_service_port = internal_service_port
        if limit is not None:
            self.limit = limit
        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if nat_gateway_id is not None:
            self.nat_gateway_id = nat_gateway_id
        if port_id is not None:
            self.port_id = port_id
        if private_ip is not None:
            self.private_ip = private_ip
        if protocol is not None:
            self.protocol = protocol

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListNatGatewayDnatRulesRequest.

        解冻/冻结状态。 取值范围： \"true\"：解冻 \"false\"：冻结

        :return: The admin_state_up of this ListNatGatewayDnatRulesRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListNatGatewayDnatRulesRequest.

        解冻/冻结状态。 取值范围： \"true\"：解冻 \"false\"：冻结

        :param admin_state_up: The admin_state_up of this ListNatGatewayDnatRulesRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def external_service_port(self):
        """Gets the external_service_port of this ListNatGatewayDnatRulesRequest.

        Floatingip对外提供服务的端口号。 取值范围：0~65535。

        :return: The external_service_port of this ListNatGatewayDnatRulesRequest.
        :rtype: int
        """
        return self._external_service_port

    @external_service_port.setter
    def external_service_port(self, external_service_port):
        """Sets the external_service_port of this ListNatGatewayDnatRulesRequest.

        Floatingip对外提供服务的端口号。 取值范围：0~65535。

        :param external_service_port: The external_service_port of this ListNatGatewayDnatRulesRequest.
        :type external_service_port: int
        """
        self._external_service_port = external_service_port

    @property
    def floating_ip_address(self):
        """Gets the floating_ip_address of this ListNatGatewayDnatRulesRequest.

        弹性公网的IP地址。

        :return: The floating_ip_address of this ListNatGatewayDnatRulesRequest.
        :rtype: str
        """
        return self._floating_ip_address

    @floating_ip_address.setter
    def floating_ip_address(self, floating_ip_address):
        """Sets the floating_ip_address of this ListNatGatewayDnatRulesRequest.

        弹性公网的IP地址。

        :param floating_ip_address: The floating_ip_address of this ListNatGatewayDnatRulesRequest.
        :type floating_ip_address: str
        """
        self._floating_ip_address = floating_ip_address

    @property
    def status(self):
        """Gets the status of this ListNatGatewayDnatRulesRequest.

        Dnat规则的状态。

        :return: The status of this ListNatGatewayDnatRulesRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListNatGatewayDnatRulesRequest.

        Dnat规则的状态。

        :param status: The status of this ListNatGatewayDnatRulesRequest.
        :type status: list[str]
        """
        self._status = status

    @property
    def floating_ip_id(self):
        """Gets the floating_ip_id of this ListNatGatewayDnatRulesRequest.

        弹性公网IP的id。

        :return: The floating_ip_id of this ListNatGatewayDnatRulesRequest.
        :rtype: str
        """
        return self._floating_ip_id

    @floating_ip_id.setter
    def floating_ip_id(self, floating_ip_id):
        """Sets the floating_ip_id of this ListNatGatewayDnatRulesRequest.

        弹性公网IP的id。

        :param floating_ip_id: The floating_ip_id of this ListNatGatewayDnatRulesRequest.
        :type floating_ip_id: str
        """
        self._floating_ip_id = floating_ip_id

    @property
    def internal_service_port(self):
        """Gets the internal_service_port of this ListNatGatewayDnatRulesRequest.

        虚拟机或者裸机对外提供服务的协议端口号。 取值范围：0~65535。

        :return: The internal_service_port of this ListNatGatewayDnatRulesRequest.
        :rtype: int
        """
        return self._internal_service_port

    @internal_service_port.setter
    def internal_service_port(self, internal_service_port):
        """Sets the internal_service_port of this ListNatGatewayDnatRulesRequest.

        虚拟机或者裸机对外提供服务的协议端口号。 取值范围：0~65535。

        :param internal_service_port: The internal_service_port of this ListNatGatewayDnatRulesRequest.
        :type internal_service_port: int
        """
        self._internal_service_port = internal_service_port

    @property
    def limit(self):
        """Gets the limit of this ListNatGatewayDnatRulesRequest.

        功能说明：每页返回的个数。 取值范围：0~2000。 默认值：2000。

        :return: The limit of this ListNatGatewayDnatRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListNatGatewayDnatRulesRequest.

        功能说明：每页返回的个数。 取值范围：0~2000。 默认值：2000。

        :param limit: The limit of this ListNatGatewayDnatRulesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def id(self):
        """Gets the id of this ListNatGatewayDnatRulesRequest.

        DNAT规则的ID。

        :return: The id of this ListNatGatewayDnatRulesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListNatGatewayDnatRulesRequest.

        DNAT规则的ID。

        :param id: The id of this ListNatGatewayDnatRulesRequest.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        """Gets the description of this ListNatGatewayDnatRulesRequest.

        DNAT规则的描述，长度限制为255。

        :return: The description of this ListNatGatewayDnatRulesRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListNatGatewayDnatRulesRequest.

        DNAT规则的描述，长度限制为255。

        :param description: The description of this ListNatGatewayDnatRulesRequest.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this ListNatGatewayDnatRulesRequest.

        DNAT规则的创建时间，格式是yyyy-mm-dd hh:mm:ss.SSSSSS。

        :return: The created_at of this ListNatGatewayDnatRulesRequest.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ListNatGatewayDnatRulesRequest.

        DNAT规则的创建时间，格式是yyyy-mm-dd hh:mm:ss.SSSSSS。

        :param created_at: The created_at of this ListNatGatewayDnatRulesRequest.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def nat_gateway_id(self):
        """Gets the nat_gateway_id of this ListNatGatewayDnatRulesRequest.

        公网NAT网关实例的ID。

        :return: The nat_gateway_id of this ListNatGatewayDnatRulesRequest.
        :rtype: list[str]
        """
        return self._nat_gateway_id

    @nat_gateway_id.setter
    def nat_gateway_id(self, nat_gateway_id):
        """Sets the nat_gateway_id of this ListNatGatewayDnatRulesRequest.

        公网NAT网关实例的ID。

        :param nat_gateway_id: The nat_gateway_id of this ListNatGatewayDnatRulesRequest.
        :type nat_gateway_id: list[str]
        """
        self._nat_gateway_id = nat_gateway_id

    @property
    def port_id(self):
        """Gets the port_id of this ListNatGatewayDnatRulesRequest.

        虚拟机或者裸机的Port ID，对应虚拟私有云场景，与private_ip参数二选一。

        :return: The port_id of this ListNatGatewayDnatRulesRequest.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this ListNatGatewayDnatRulesRequest.

        虚拟机或者裸机的Port ID，对应虚拟私有云场景，与private_ip参数二选一。

        :param port_id: The port_id of this ListNatGatewayDnatRulesRequest.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def private_ip(self):
        """Gets the private_ip of this ListNatGatewayDnatRulesRequest.

        用户私有IP地址，对应专线、云连接场景，与port_id参数二选一。

        :return: The private_ip of this ListNatGatewayDnatRulesRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this ListNatGatewayDnatRulesRequest.

        用户私有IP地址，对应专线、云连接场景，与port_id参数二选一。

        :param private_ip: The private_ip of this ListNatGatewayDnatRulesRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def protocol(self):
        """Gets the protocol of this ListNatGatewayDnatRulesRequest.

        协议类型，目前支持TCP/tcp、UDP/udp、ANY/any。 对应协议号6、17、0。

        :return: The protocol of this ListNatGatewayDnatRulesRequest.
        :rtype: list[str]
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ListNatGatewayDnatRulesRequest.

        协议类型，目前支持TCP/tcp、UDP/udp、ANY/any。 对应协议号6、17、0。

        :param protocol: The protocol of this ListNatGatewayDnatRulesRequest.
        :type protocol: list[str]
        """
        self._protocol = protocol

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
        if not isinstance(other, ListNatGatewayDnatRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
