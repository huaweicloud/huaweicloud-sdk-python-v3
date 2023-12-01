# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrivateDnat:

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
        'project_id': 'str',
        'description': 'str',
        'transit_ip_id': 'str',
        'gateway_id': 'str',
        'network_interface_id': 'str',
        'type': 'str',
        'protocol': 'str',
        'private_ip_address': 'str',
        'internal_service_port': 'str',
        'transit_service_port': 'str',
        'enterprise_project_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'description': 'description',
        'transit_ip_id': 'transit_ip_id',
        'gateway_id': 'gateway_id',
        'network_interface_id': 'network_interface_id',
        'type': 'type',
        'protocol': 'protocol',
        'private_ip_address': 'private_ip_address',
        'internal_service_port': 'internal_service_port',
        'transit_service_port': 'transit_service_port',
        'enterprise_project_id': 'enterprise_project_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, project_id=None, description=None, transit_ip_id=None, gateway_id=None, network_interface_id=None, type=None, protocol=None, private_ip_address=None, internal_service_port=None, transit_service_port=None, enterprise_project_id=None, created_at=None, updated_at=None):
        """PrivateDnat

        The model defined in huaweicloud sdk

        :param id: DNAT规则的ID。
        :type id: str
        :param project_id: 项目的ID。
        :type project_id: str
        :param description: DNAT规则的描述。长度范围小于等于255个字符，不能包含“&lt;”和“&gt;”。
        :type description: str
        :param transit_ip_id: 中转IP的ID。
        :type transit_ip_id: str
        :param gateway_id: 私网NAT网关实例的ID。
        :type gateway_id: str
        :param network_interface_id: 网络接口ID，支持计算、ELB、VIP等实例的端口。
        :type network_interface_id: str
        :param type: DNAT规则后端的类型。 取值：     COMPUTE：后端为计算实例。     VIP：后端为VIP的实例。     ELB：后端为ELB的实例。     ELBv3：后端为ELBv3的实例。     CUSTOMIZE：后端为自定义IP。
        :type type: str
        :param protocol: 协议类型。 目前支持TCP/tcp、UDP/udp、ANY/any。 对应协议号6、17、0。
        :type protocol: str
        :param private_ip_address: 后端实例的私网IP地址。
        :type private_ip_address: str
        :param internal_service_port: 后端实例的端口号。
        :type internal_service_port: str
        :param transit_service_port: 中转IP的端口号。
        :type transit_service_port: str
        :param enterprise_project_id: 企业项目ID。创建DNAT规则时，关联的企业项目ID。
        :type enterprise_project_id: str
        :param created_at: DNAT规则的创建时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。
        :type created_at: datetime
        :param updated_at: DNAT规则的更新时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._project_id = None
        self._description = None
        self._transit_ip_id = None
        self._gateway_id = None
        self._network_interface_id = None
        self._type = None
        self._protocol = None
        self._private_ip_address = None
        self._internal_service_port = None
        self._transit_service_port = None
        self._enterprise_project_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if description is not None:
            self.description = description
        if transit_ip_id is not None:
            self.transit_ip_id = transit_ip_id
        if gateway_id is not None:
            self.gateway_id = gateway_id
        if network_interface_id is not None:
            self.network_interface_id = network_interface_id
        if type is not None:
            self.type = type
        if protocol is not None:
            self.protocol = protocol
        if private_ip_address is not None:
            self.private_ip_address = private_ip_address
        if internal_service_port is not None:
            self.internal_service_port = internal_service_port
        if transit_service_port is not None:
            self.transit_service_port = transit_service_port
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this PrivateDnat.

        DNAT规则的ID。

        :return: The id of this PrivateDnat.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PrivateDnat.

        DNAT规则的ID。

        :param id: The id of this PrivateDnat.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this PrivateDnat.

        项目的ID。

        :return: The project_id of this PrivateDnat.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this PrivateDnat.

        项目的ID。

        :param project_id: The project_id of this PrivateDnat.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def description(self):
        """Gets the description of this PrivateDnat.

        DNAT规则的描述。长度范围小于等于255个字符，不能包含“<”和“>”。

        :return: The description of this PrivateDnat.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PrivateDnat.

        DNAT规则的描述。长度范围小于等于255个字符，不能包含“<”和“>”。

        :param description: The description of this PrivateDnat.
        :type description: str
        """
        self._description = description

    @property
    def transit_ip_id(self):
        """Gets the transit_ip_id of this PrivateDnat.

        中转IP的ID。

        :return: The transit_ip_id of this PrivateDnat.
        :rtype: str
        """
        return self._transit_ip_id

    @transit_ip_id.setter
    def transit_ip_id(self, transit_ip_id):
        """Sets the transit_ip_id of this PrivateDnat.

        中转IP的ID。

        :param transit_ip_id: The transit_ip_id of this PrivateDnat.
        :type transit_ip_id: str
        """
        self._transit_ip_id = transit_ip_id

    @property
    def gateway_id(self):
        """Gets the gateway_id of this PrivateDnat.

        私网NAT网关实例的ID。

        :return: The gateway_id of this PrivateDnat.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """Sets the gateway_id of this PrivateDnat.

        私网NAT网关实例的ID。

        :param gateway_id: The gateway_id of this PrivateDnat.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

    @property
    def network_interface_id(self):
        """Gets the network_interface_id of this PrivateDnat.

        网络接口ID，支持计算、ELB、VIP等实例的端口。

        :return: The network_interface_id of this PrivateDnat.
        :rtype: str
        """
        return self._network_interface_id

    @network_interface_id.setter
    def network_interface_id(self, network_interface_id):
        """Sets the network_interface_id of this PrivateDnat.

        网络接口ID，支持计算、ELB、VIP等实例的端口。

        :param network_interface_id: The network_interface_id of this PrivateDnat.
        :type network_interface_id: str
        """
        self._network_interface_id = network_interface_id

    @property
    def type(self):
        """Gets the type of this PrivateDnat.

        DNAT规则后端的类型。 取值：     COMPUTE：后端为计算实例。     VIP：后端为VIP的实例。     ELB：后端为ELB的实例。     ELBv3：后端为ELBv3的实例。     CUSTOMIZE：后端为自定义IP。

        :return: The type of this PrivateDnat.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PrivateDnat.

        DNAT规则后端的类型。 取值：     COMPUTE：后端为计算实例。     VIP：后端为VIP的实例。     ELB：后端为ELB的实例。     ELBv3：后端为ELBv3的实例。     CUSTOMIZE：后端为自定义IP。

        :param type: The type of this PrivateDnat.
        :type type: str
        """
        self._type = type

    @property
    def protocol(self):
        """Gets the protocol of this PrivateDnat.

        协议类型。 目前支持TCP/tcp、UDP/udp、ANY/any。 对应协议号6、17、0。

        :return: The protocol of this PrivateDnat.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this PrivateDnat.

        协议类型。 目前支持TCP/tcp、UDP/udp、ANY/any。 对应协议号6、17、0。

        :param protocol: The protocol of this PrivateDnat.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def private_ip_address(self):
        """Gets the private_ip_address of this PrivateDnat.

        后端实例的私网IP地址。

        :return: The private_ip_address of this PrivateDnat.
        :rtype: str
        """
        return self._private_ip_address

    @private_ip_address.setter
    def private_ip_address(self, private_ip_address):
        """Sets the private_ip_address of this PrivateDnat.

        后端实例的私网IP地址。

        :param private_ip_address: The private_ip_address of this PrivateDnat.
        :type private_ip_address: str
        """
        self._private_ip_address = private_ip_address

    @property
    def internal_service_port(self):
        """Gets the internal_service_port of this PrivateDnat.

        后端实例的端口号。

        :return: The internal_service_port of this PrivateDnat.
        :rtype: str
        """
        return self._internal_service_port

    @internal_service_port.setter
    def internal_service_port(self, internal_service_port):
        """Sets the internal_service_port of this PrivateDnat.

        后端实例的端口号。

        :param internal_service_port: The internal_service_port of this PrivateDnat.
        :type internal_service_port: str
        """
        self._internal_service_port = internal_service_port

    @property
    def transit_service_port(self):
        """Gets the transit_service_port of this PrivateDnat.

        中转IP的端口号。

        :return: The transit_service_port of this PrivateDnat.
        :rtype: str
        """
        return self._transit_service_port

    @transit_service_port.setter
    def transit_service_port(self, transit_service_port):
        """Sets the transit_service_port of this PrivateDnat.

        中转IP的端口号。

        :param transit_service_port: The transit_service_port of this PrivateDnat.
        :type transit_service_port: str
        """
        self._transit_service_port = transit_service_port

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this PrivateDnat.

        企业项目ID。创建DNAT规则时，关联的企业项目ID。

        :return: The enterprise_project_id of this PrivateDnat.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this PrivateDnat.

        企业项目ID。创建DNAT规则时，关联的企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this PrivateDnat.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def created_at(self):
        """Gets the created_at of this PrivateDnat.

        DNAT规则的创建时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。

        :return: The created_at of this PrivateDnat.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PrivateDnat.

        DNAT规则的创建时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。

        :param created_at: The created_at of this PrivateDnat.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this PrivateDnat.

        DNAT规则的更新时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。

        :return: The updated_at of this PrivateDnat.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this PrivateDnat.

        DNAT规则的更新时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。

        :param updated_at: The updated_at of this PrivateDnat.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, PrivateDnat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
