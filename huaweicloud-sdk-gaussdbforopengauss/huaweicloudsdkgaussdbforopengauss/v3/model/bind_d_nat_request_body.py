# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BindDNatRequestBody:

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
        'public_ip_id': 'str',
        'nat_gateway_id': 'str',
        'external_service_port': 'int',
        'action': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'public_ip_id': 'public_ip_id',
        'nat_gateway_id': 'nat_gateway_id',
        'external_service_port': 'external_service_port',
        'action': 'action'
    }

    def __init__(self, node_id=None, public_ip_id=None, nat_gateway_id=None, external_service_port=None, action=None):
        r"""BindDNatRequestBody

        The model defined in huaweicloud sdk

        :param node_id: **参数解释**: 需要绑定或者解绑的节点ID。 **约束限制**: 分布式仅支持CN节点，集中式不支持日志节点。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type node_id: str
        :param public_ip_id: **参数解释**: 弹性公网ID。 **约束限制**: action类型为BIND时必选。 一个弹性公网IP只能绑定到一个NAT网关。 **取值范围**: UUID格式。 **默认取值**: 不涉及。
        :type public_ip_id: str
        :param nat_gateway_id: **参数解释**: 公网NAT网关的ID。 **约束限制**: action类型为BIND时必选。 NAT网关的虚拟私有云和子网需要和GaussDB数据库实例的虚拟私有云和子网保持一致。 **取值范围**: UUID格式。 **默认取值**: 不涉及。
        :type nat_gateway_id: str
        :param external_service_port: **参数解释**: 对外提供服务的端口号，可通过弹性公网IP加该端口号的方式连接数据库实例。 **约束限制**: action类型为BIND时必选。 **取值范围**: 0~65535。 **默认取值**: 不涉及。
        :type external_service_port: int
        :param action: **参数解释**: 操作标识。 **约束限制**: 不涉及。 **取值范围**: BIND，表示绑定NAT网关。 UNBIND，表示解绑NAT网关。 **默认取值**: 不涉及。
        :type action: str
        """
        
        

        self._node_id = None
        self._public_ip_id = None
        self._nat_gateway_id = None
        self._external_service_port = None
        self._action = None
        self.discriminator = None

        self.node_id = node_id
        if public_ip_id is not None:
            self.public_ip_id = public_ip_id
        if nat_gateway_id is not None:
            self.nat_gateway_id = nat_gateway_id
        if external_service_port is not None:
            self.external_service_port = external_service_port
        self.action = action

    @property
    def node_id(self):
        r"""Gets the node_id of this BindDNatRequestBody.

        **参数解释**: 需要绑定或者解绑的节点ID。 **约束限制**: 分布式仅支持CN节点，集中式不支持日志节点。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The node_id of this BindDNatRequestBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this BindDNatRequestBody.

        **参数解释**: 需要绑定或者解绑的节点ID。 **约束限制**: 分布式仅支持CN节点，集中式不支持日志节点。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param node_id: The node_id of this BindDNatRequestBody.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def public_ip_id(self):
        r"""Gets the public_ip_id of this BindDNatRequestBody.

        **参数解释**: 弹性公网ID。 **约束限制**: action类型为BIND时必选。 一个弹性公网IP只能绑定到一个NAT网关。 **取值范围**: UUID格式。 **默认取值**: 不涉及。

        :return: The public_ip_id of this BindDNatRequestBody.
        :rtype: str
        """
        return self._public_ip_id

    @public_ip_id.setter
    def public_ip_id(self, public_ip_id):
        r"""Sets the public_ip_id of this BindDNatRequestBody.

        **参数解释**: 弹性公网ID。 **约束限制**: action类型为BIND时必选。 一个弹性公网IP只能绑定到一个NAT网关。 **取值范围**: UUID格式。 **默认取值**: 不涉及。

        :param public_ip_id: The public_ip_id of this BindDNatRequestBody.
        :type public_ip_id: str
        """
        self._public_ip_id = public_ip_id

    @property
    def nat_gateway_id(self):
        r"""Gets the nat_gateway_id of this BindDNatRequestBody.

        **参数解释**: 公网NAT网关的ID。 **约束限制**: action类型为BIND时必选。 NAT网关的虚拟私有云和子网需要和GaussDB数据库实例的虚拟私有云和子网保持一致。 **取值范围**: UUID格式。 **默认取值**: 不涉及。

        :return: The nat_gateway_id of this BindDNatRequestBody.
        :rtype: str
        """
        return self._nat_gateway_id

    @nat_gateway_id.setter
    def nat_gateway_id(self, nat_gateway_id):
        r"""Sets the nat_gateway_id of this BindDNatRequestBody.

        **参数解释**: 公网NAT网关的ID。 **约束限制**: action类型为BIND时必选。 NAT网关的虚拟私有云和子网需要和GaussDB数据库实例的虚拟私有云和子网保持一致。 **取值范围**: UUID格式。 **默认取值**: 不涉及。

        :param nat_gateway_id: The nat_gateway_id of this BindDNatRequestBody.
        :type nat_gateway_id: str
        """
        self._nat_gateway_id = nat_gateway_id

    @property
    def external_service_port(self):
        r"""Gets the external_service_port of this BindDNatRequestBody.

        **参数解释**: 对外提供服务的端口号，可通过弹性公网IP加该端口号的方式连接数据库实例。 **约束限制**: action类型为BIND时必选。 **取值范围**: 0~65535。 **默认取值**: 不涉及。

        :return: The external_service_port of this BindDNatRequestBody.
        :rtype: int
        """
        return self._external_service_port

    @external_service_port.setter
    def external_service_port(self, external_service_port):
        r"""Sets the external_service_port of this BindDNatRequestBody.

        **参数解释**: 对外提供服务的端口号，可通过弹性公网IP加该端口号的方式连接数据库实例。 **约束限制**: action类型为BIND时必选。 **取值范围**: 0~65535。 **默认取值**: 不涉及。

        :param external_service_port: The external_service_port of this BindDNatRequestBody.
        :type external_service_port: int
        """
        self._external_service_port = external_service_port

    @property
    def action(self):
        r"""Gets the action of this BindDNatRequestBody.

        **参数解释**: 操作标识。 **约束限制**: 不涉及。 **取值范围**: BIND，表示绑定NAT网关。 UNBIND，表示解绑NAT网关。 **默认取值**: 不涉及。

        :return: The action of this BindDNatRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this BindDNatRequestBody.

        **参数解释**: 操作标识。 **约束限制**: 不涉及。 **取值范围**: BIND，表示绑定NAT网关。 UNBIND，表示解绑NAT网关。 **默认取值**: 不涉及。

        :param action: The action of this BindDNatRequestBody.
        :type action: str
        """
        self._action = action

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
        if not isinstance(other, BindDNatRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
