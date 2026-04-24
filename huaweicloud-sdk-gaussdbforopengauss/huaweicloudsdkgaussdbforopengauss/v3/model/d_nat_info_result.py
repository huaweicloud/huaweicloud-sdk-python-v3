# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DNatInfoResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'nat_gateway_id': 'str',
        'port_id': 'str',
        'public_ip_id': 'str',
        'public_ip': 'str',
        'external_service_port': 'int',
        'internal_service_port': 'int',
        'private_ip': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'nat_gateway_id': 'nat_gateway_id',
        'port_id': 'port_id',
        'public_ip_id': 'public_ip_id',
        'public_ip': 'public_ip',
        'external_service_port': 'external_service_port',
        'internal_service_port': 'internal_service_port',
        'private_ip': 'private_ip'
    }

    def __init__(self, node_id=None, nat_gateway_id=None, port_id=None, public_ip_id=None, public_ip=None, external_service_port=None, internal_service_port=None, private_ip=None):
        r"""DNatInfoResult

        The model defined in huaweicloud sdk

        :param node_id: **参数解释**: 已经绑定NAT网关的节点ID。 **取值范围**: 不涉及。
        :type node_id: str
        :param nat_gateway_id: **参数解释**: NAT网关实例的ID。 **取值范围**: 不涉及。
        :type nat_gateway_id: str
        :param port_id: **参数解释**: 端口ID。 **取值范围**: 不涉及。
        :type port_id: str
        :param public_ip_id: **参数解释**: 弹性公网ID。 **取值范围**: 不涉及。
        :type public_ip_id: str
        :param public_ip: **参数解释**: 弹性公网IP。 **取值范围**: 不涉及。
        :type public_ip: str
        :param external_service_port: **参数解释**: 对外提供服务的端口号，可通过弹性公网IP加该端口号的方式连接数据库实例。 **取值范围**: 不涉及。
        :type external_service_port: int
        :param internal_service_port: **参数解释**: GaussDB数据库端口号。 **取值范围**: 不涉及。
        :type internal_service_port: int
        :param private_ip: **参数解释**: 内网地址。 **取值范围**: 不涉及。
        :type private_ip: str
        """
        
        

        self._node_id = None
        self._nat_gateway_id = None
        self._port_id = None
        self._public_ip_id = None
        self._public_ip = None
        self._external_service_port = None
        self._internal_service_port = None
        self._private_ip = None
        self.discriminator = None

        if node_id is not None:
            self.node_id = node_id
        if nat_gateway_id is not None:
            self.nat_gateway_id = nat_gateway_id
        if port_id is not None:
            self.port_id = port_id
        if public_ip_id is not None:
            self.public_ip_id = public_ip_id
        if public_ip is not None:
            self.public_ip = public_ip
        if external_service_port is not None:
            self.external_service_port = external_service_port
        if internal_service_port is not None:
            self.internal_service_port = internal_service_port
        if private_ip is not None:
            self.private_ip = private_ip

    @property
    def node_id(self):
        r"""Gets the node_id of this DNatInfoResult.

        **参数解释**: 已经绑定NAT网关的节点ID。 **取值范围**: 不涉及。

        :return: The node_id of this DNatInfoResult.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this DNatInfoResult.

        **参数解释**: 已经绑定NAT网关的节点ID。 **取值范围**: 不涉及。

        :param node_id: The node_id of this DNatInfoResult.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def nat_gateway_id(self):
        r"""Gets the nat_gateway_id of this DNatInfoResult.

        **参数解释**: NAT网关实例的ID。 **取值范围**: 不涉及。

        :return: The nat_gateway_id of this DNatInfoResult.
        :rtype: str
        """
        return self._nat_gateway_id

    @nat_gateway_id.setter
    def nat_gateway_id(self, nat_gateway_id):
        r"""Sets the nat_gateway_id of this DNatInfoResult.

        **参数解释**: NAT网关实例的ID。 **取值范围**: 不涉及。

        :param nat_gateway_id: The nat_gateway_id of this DNatInfoResult.
        :type nat_gateway_id: str
        """
        self._nat_gateway_id = nat_gateway_id

    @property
    def port_id(self):
        r"""Gets the port_id of this DNatInfoResult.

        **参数解释**: 端口ID。 **取值范围**: 不涉及。

        :return: The port_id of this DNatInfoResult.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        r"""Sets the port_id of this DNatInfoResult.

        **参数解释**: 端口ID。 **取值范围**: 不涉及。

        :param port_id: The port_id of this DNatInfoResult.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def public_ip_id(self):
        r"""Gets the public_ip_id of this DNatInfoResult.

        **参数解释**: 弹性公网ID。 **取值范围**: 不涉及。

        :return: The public_ip_id of this DNatInfoResult.
        :rtype: str
        """
        return self._public_ip_id

    @public_ip_id.setter
    def public_ip_id(self, public_ip_id):
        r"""Sets the public_ip_id of this DNatInfoResult.

        **参数解释**: 弹性公网ID。 **取值范围**: 不涉及。

        :param public_ip_id: The public_ip_id of this DNatInfoResult.
        :type public_ip_id: str
        """
        self._public_ip_id = public_ip_id

    @property
    def public_ip(self):
        r"""Gets the public_ip of this DNatInfoResult.

        **参数解释**: 弹性公网IP。 **取值范围**: 不涉及。

        :return: The public_ip of this DNatInfoResult.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this DNatInfoResult.

        **参数解释**: 弹性公网IP。 **取值范围**: 不涉及。

        :param public_ip: The public_ip of this DNatInfoResult.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def external_service_port(self):
        r"""Gets the external_service_port of this DNatInfoResult.

        **参数解释**: 对外提供服务的端口号，可通过弹性公网IP加该端口号的方式连接数据库实例。 **取值范围**: 不涉及。

        :return: The external_service_port of this DNatInfoResult.
        :rtype: int
        """
        return self._external_service_port

    @external_service_port.setter
    def external_service_port(self, external_service_port):
        r"""Sets the external_service_port of this DNatInfoResult.

        **参数解释**: 对外提供服务的端口号，可通过弹性公网IP加该端口号的方式连接数据库实例。 **取值范围**: 不涉及。

        :param external_service_port: The external_service_port of this DNatInfoResult.
        :type external_service_port: int
        """
        self._external_service_port = external_service_port

    @property
    def internal_service_port(self):
        r"""Gets the internal_service_port of this DNatInfoResult.

        **参数解释**: GaussDB数据库端口号。 **取值范围**: 不涉及。

        :return: The internal_service_port of this DNatInfoResult.
        :rtype: int
        """
        return self._internal_service_port

    @internal_service_port.setter
    def internal_service_port(self, internal_service_port):
        r"""Sets the internal_service_port of this DNatInfoResult.

        **参数解释**: GaussDB数据库端口号。 **取值范围**: 不涉及。

        :param internal_service_port: The internal_service_port of this DNatInfoResult.
        :type internal_service_port: int
        """
        self._internal_service_port = internal_service_port

    @property
    def private_ip(self):
        r"""Gets the private_ip of this DNatInfoResult.

        **参数解释**: 内网地址。 **取值范围**: 不涉及。

        :return: The private_ip of this DNatInfoResult.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this DNatInfoResult.

        **参数解释**: 内网地址。 **取值范围**: 不涉及。

        :param private_ip: The private_ip of this DNatInfoResult.
        :type private_ip: str
        """
        self._private_ip = private_ip

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
        if not isinstance(other, DNatInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
