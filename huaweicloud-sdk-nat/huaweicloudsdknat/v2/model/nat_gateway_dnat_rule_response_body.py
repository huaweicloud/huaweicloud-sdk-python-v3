# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'created_at': 'str',
        'global_eip_id': 'str',
        'global_eip_address': 'str'
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
        'created_at': 'created_at',
        'global_eip_id': 'global_eip_id',
        'global_eip_address': 'global_eip_address'
    }

    def __init__(self, id=None, tenant_id=None, description=None, port_id=None, private_ip=None, internal_service_port=None, nat_gateway_id=None, floating_ip_id=None, floating_ip_address=None, external_service_port=None, status=None, admin_state_up=None, internal_service_port_range=None, external_service_port_range=None, protocol=None, created_at=None, global_eip_id=None, global_eip_address=None):
        """NatGatewayDnatRuleResponseBody

        The model defined in huaweicloud sdk

        :param id: DNAT规则的ID。
        :type id: str
        :param tenant_id: 项目的ID。
        :type tenant_id: str
        :param description: DNAT规则的描述。长度范围小于等于255个字符，不能包含“&lt;”和“&gt;”。
        :type description: str
        :param port_id: 虚拟机或者裸机的Port ID，对应虚拟私有云场景，与private_ip参数二选一。
        :type port_id: str
        :param private_ip: 用户私有IP地址，对应专线、云连接场景，与port_id参数二选一。
        :type private_ip: str
        :param internal_service_port: 虚拟机或者裸机对外提供服务的协议端口号。 取值范围：0~65535。
        :type internal_service_port: int
        :param nat_gateway_id: 公网NAT网关实例的ID。
        :type nat_gateway_id: str
        :param floating_ip_id: 弹性公网IP的id。
        :type floating_ip_id: str
        :param floating_ip_address: 弹性公网IP的IP地址。 
        :type floating_ip_address: str
        :param external_service_port: Floatingip对外提供服务的端口号。 取值范围：0~65535。
        :type external_service_port: int
        :param status: DNAT规则的状态。 取值为： \&quot;ACTIVE\&quot;: 可用 \&quot;PENDING_CREATE\&quot;：创建中 \&quot;PENDING_UPDATE\&quot;：更新中 \&quot;PENDING_DELETE\&quot;：删除中 \&quot;EIP_FREEZED\&quot;：EIP冻结 \&quot;INACTIVE\&quot;：不可用
        :type status: str
        :param admin_state_up: 解冻/冻结状态。 取值范围： − “true”： 解冻 − “false”： 冻结 
        :type admin_state_up: bool
        :param internal_service_port_range: 虚拟机或者裸机对外提供服务的协议端口号范围。 功能说明：该端口范围与external _service_port_range按顺序实现1:1映射。 取值范围：1~65535。 约束：只能以’-’字符连接端口范围。 
        :type internal_service_port_range: str
        :param external_service_port_range: Floatingip对外提供服务的端口号范围。 功能说明：该端口范围与internal _service_port_range按顺序实现1:1映射。 取值范围：1~65535。 约束：只能以’-’字符连接端口范围 
        :type external_service_port_range: str
        :param protocol: 协议类型，目前支持TCP/tcp、UDP/udp、ANY/any。 对应协议号6、17、0。 
        :type protocol: str
        :param created_at: DNAT规则的创建时间，格式是yyyy-mm-dd hh:mm:ss.SSSSSS。
        :type created_at: str
        :param global_eip_id: 全域弹性公网IP的id。
        :type global_eip_id: str
        :param global_eip_address: 全域弹性公网IP的地址。
        :type global_eip_address: str
        """
        
        

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
        self._global_eip_id = None
        self._global_eip_address = None
        self.discriminator = None

        self.id = id
        self.tenant_id = tenant_id
        self.description = description
        if port_id is not None:
            self.port_id = port_id
        if private_ip is not None:
            self.private_ip = private_ip
        self.internal_service_port = internal_service_port
        self.nat_gateway_id = nat_gateway_id
        self.floating_ip_id = floating_ip_id
        self.floating_ip_address = floating_ip_address
        self.external_service_port = external_service_port
        self.status = status
        self.admin_state_up = admin_state_up
        if internal_service_port_range is not None:
            self.internal_service_port_range = internal_service_port_range
        if external_service_port_range is not None:
            self.external_service_port_range = external_service_port_range
        self.protocol = protocol
        self.created_at = created_at
        self.global_eip_id = global_eip_id
        self.global_eip_address = global_eip_address

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
        :type id: str
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
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def description(self):
        """Gets the description of this NatGatewayDnatRuleResponseBody.

        DNAT规则的描述。长度范围小于等于255个字符，不能包含“<”和“>”。

        :return: The description of this NatGatewayDnatRuleResponseBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NatGatewayDnatRuleResponseBody.

        DNAT规则的描述。长度范围小于等于255个字符，不能包含“<”和“>”。

        :param description: The description of this NatGatewayDnatRuleResponseBody.
        :type description: str
        """
        self._description = description

    @property
    def port_id(self):
        """Gets the port_id of this NatGatewayDnatRuleResponseBody.

        虚拟机或者裸机的Port ID，对应虚拟私有云场景，与private_ip参数二选一。

        :return: The port_id of this NatGatewayDnatRuleResponseBody.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this NatGatewayDnatRuleResponseBody.

        虚拟机或者裸机的Port ID，对应虚拟私有云场景，与private_ip参数二选一。

        :param port_id: The port_id of this NatGatewayDnatRuleResponseBody.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def private_ip(self):
        """Gets the private_ip of this NatGatewayDnatRuleResponseBody.

        用户私有IP地址，对应专线、云连接场景，与port_id参数二选一。

        :return: The private_ip of this NatGatewayDnatRuleResponseBody.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this NatGatewayDnatRuleResponseBody.

        用户私有IP地址，对应专线、云连接场景，与port_id参数二选一。

        :param private_ip: The private_ip of this NatGatewayDnatRuleResponseBody.
        :type private_ip: str
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
        :type internal_service_port: int
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
        :type nat_gateway_id: str
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
        :type floating_ip_id: str
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
        :type floating_ip_address: str
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
        :type external_service_port: int
        """
        self._external_service_port = external_service_port

    @property
    def status(self):
        """Gets the status of this NatGatewayDnatRuleResponseBody.

        DNAT规则的状态。 取值为： \"ACTIVE\": 可用 \"PENDING_CREATE\"：创建中 \"PENDING_UPDATE\"：更新中 \"PENDING_DELETE\"：删除中 \"EIP_FREEZED\"：EIP冻结 \"INACTIVE\"：不可用

        :return: The status of this NatGatewayDnatRuleResponseBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NatGatewayDnatRuleResponseBody.

        DNAT规则的状态。 取值为： \"ACTIVE\": 可用 \"PENDING_CREATE\"：创建中 \"PENDING_UPDATE\"：更新中 \"PENDING_DELETE\"：删除中 \"EIP_FREEZED\"：EIP冻结 \"INACTIVE\"：不可用

        :param status: The status of this NatGatewayDnatRuleResponseBody.
        :type status: str
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
        :type admin_state_up: bool
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
        :type internal_service_port_range: str
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
        :type external_service_port_range: str
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
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def created_at(self):
        """Gets the created_at of this NatGatewayDnatRuleResponseBody.

        DNAT规则的创建时间，格式是yyyy-mm-dd hh:mm:ss.SSSSSS。

        :return: The created_at of this NatGatewayDnatRuleResponseBody.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this NatGatewayDnatRuleResponseBody.

        DNAT规则的创建时间，格式是yyyy-mm-dd hh:mm:ss.SSSSSS。

        :param created_at: The created_at of this NatGatewayDnatRuleResponseBody.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def global_eip_id(self):
        """Gets the global_eip_id of this NatGatewayDnatRuleResponseBody.

        全域弹性公网IP的id。

        :return: The global_eip_id of this NatGatewayDnatRuleResponseBody.
        :rtype: str
        """
        return self._global_eip_id

    @global_eip_id.setter
    def global_eip_id(self, global_eip_id):
        """Sets the global_eip_id of this NatGatewayDnatRuleResponseBody.

        全域弹性公网IP的id。

        :param global_eip_id: The global_eip_id of this NatGatewayDnatRuleResponseBody.
        :type global_eip_id: str
        """
        self._global_eip_id = global_eip_id

    @property
    def global_eip_address(self):
        """Gets the global_eip_address of this NatGatewayDnatRuleResponseBody.

        全域弹性公网IP的地址。

        :return: The global_eip_address of this NatGatewayDnatRuleResponseBody.
        :rtype: str
        """
        return self._global_eip_address

    @global_eip_address.setter
    def global_eip_address(self, global_eip_address):
        """Sets the global_eip_address of this NatGatewayDnatRuleResponseBody.

        全域弹性公网IP的地址。

        :param global_eip_address: The global_eip_address of this NatGatewayDnatRuleResponseBody.
        :type global_eip_address: str
        """
        self._global_eip_address = global_eip_address

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
        if not isinstance(other, NatGatewayDnatRuleResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
