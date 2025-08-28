# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMasterSlaveMemberOption:

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
        'admin_state_up': 'bool',
        'name': 'str',
        'protocol_port': 'int',
        'subnet_cidr_id': 'str',
        'role': 'str'
    }

    attribute_map = {
        'address': 'address',
        'admin_state_up': 'admin_state_up',
        'name': 'name',
        'protocol_port': 'protocol_port',
        'subnet_cidr_id': 'subnet_cidr_id',
        'role': 'role'
    }

    def __init__(self, address=None, admin_state_up=None, name=None, protocol_port=None, subnet_cidr_id=None, role=None):
        r"""CreateMasterSlaveMemberOption

        The model defined in huaweicloud sdk

        :param address: **参数解释**：后端服务器对应的IP地址。  **约束限制**： - 若subnet_cidr_id为空，表示添加IP类型后端，此时address必须为**私网IPv4**地址。 - 若subnet_cidr_id不为空，表示是一个关联到ECS的后端服务器。该IP地址必须在subnet_cidr_id对应的子网网段中，可以是**私网IPv4**或IPv6。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持IPv6，请勿设置为IPv6地址。](tag:dt)
        :type address: str
        :param admin_state_up: **参数解释**：后端服务器的管理状态。  **约束限制**：虽然创建、更新请求支持该字段，但实际取值决定于后端服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。  **取值范围**：true 弹性云服务器存在，false 弹性云服务器不存在。  **默认取值**：不涉及
        :type admin_state_up: bool
        :param name: **参数解释**：后端服务器名称。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type name: str
        :param protocol_port: **参数解释**：后端服务器业务端口  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  &gt;在开启端口透传的pool下创建member传该字段不生效，可不传该字段。
        :type protocol_port: int
        :param subnet_cidr_id: **参数解释**：后端服务器所在的子网ID，可以是子网的IPv4子网ID或IPv6子网ID。  **约束限制**： - 该子网和关联的负载均衡器的子网必须在同一VPC下。 - 若所属LB的IP类型后端转发特性已开启，则该字段可以不传，表示添加跨VPC的后端服务器。此时address必须为**私网IPv4**地址，所在的pool的协议必须为UDP/TCP/TLS/HTTP/HTTPS/QUIC/GRPC。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持IPv6，请勿设置为IPv6子网ID。](tag:dt)
        :type subnet_cidr_id: str
        :param role: **参数解释**：后端服务器的主备状态。  **约束限制**：不涉及  **取值范围**： - master：主后端服务器。 - slave：备后端服务器。  **默认取值**：不涉及
        :type role: str
        """
        
        

        self._address = None
        self._admin_state_up = None
        self._name = None
        self._protocol_port = None
        self._subnet_cidr_id = None
        self._role = None
        self.discriminator = None

        self.address = address
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if name is not None:
            self.name = name
        if protocol_port is not None:
            self.protocol_port = protocol_port
        if subnet_cidr_id is not None:
            self.subnet_cidr_id = subnet_cidr_id
        self.role = role

    @property
    def address(self):
        r"""Gets the address of this CreateMasterSlaveMemberOption.

        **参数解释**：后端服务器对应的IP地址。  **约束限制**： - 若subnet_cidr_id为空，表示添加IP类型后端，此时address必须为**私网IPv4**地址。 - 若subnet_cidr_id不为空，表示是一个关联到ECS的后端服务器。该IP地址必须在subnet_cidr_id对应的子网网段中，可以是**私网IPv4**或IPv6。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持IPv6，请勿设置为IPv6地址。](tag:dt)

        :return: The address of this CreateMasterSlaveMemberOption.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this CreateMasterSlaveMemberOption.

        **参数解释**：后端服务器对应的IP地址。  **约束限制**： - 若subnet_cidr_id为空，表示添加IP类型后端，此时address必须为**私网IPv4**地址。 - 若subnet_cidr_id不为空，表示是一个关联到ECS的后端服务器。该IP地址必须在subnet_cidr_id对应的子网网段中，可以是**私网IPv4**或IPv6。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持IPv6，请勿设置为IPv6地址。](tag:dt)

        :param address: The address of this CreateMasterSlaveMemberOption.
        :type address: str
        """
        self._address = address

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this CreateMasterSlaveMemberOption.

        **参数解释**：后端服务器的管理状态。  **约束限制**：虽然创建、更新请求支持该字段，但实际取值决定于后端服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。  **取值范围**：true 弹性云服务器存在，false 弹性云服务器不存在。  **默认取值**：不涉及

        :return: The admin_state_up of this CreateMasterSlaveMemberOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this CreateMasterSlaveMemberOption.

        **参数解释**：后端服务器的管理状态。  **约束限制**：虽然创建、更新请求支持该字段，但实际取值决定于后端服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。  **取值范围**：true 弹性云服务器存在，false 弹性云服务器不存在。  **默认取值**：不涉及

        :param admin_state_up: The admin_state_up of this CreateMasterSlaveMemberOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def name(self):
        r"""Gets the name of this CreateMasterSlaveMemberOption.

        **参数解释**：后端服务器名称。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The name of this CreateMasterSlaveMemberOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateMasterSlaveMemberOption.

        **参数解释**：后端服务器名称。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param name: The name of this CreateMasterSlaveMemberOption.
        :type name: str
        """
        self._name = name

    @property
    def protocol_port(self):
        r"""Gets the protocol_port of this CreateMasterSlaveMemberOption.

        **参数解释**：后端服务器业务端口  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  >在开启端口透传的pool下创建member传该字段不生效，可不传该字段。

        :return: The protocol_port of this CreateMasterSlaveMemberOption.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        r"""Sets the protocol_port of this CreateMasterSlaveMemberOption.

        **参数解释**：后端服务器业务端口  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  >在开启端口透传的pool下创建member传该字段不生效，可不传该字段。

        :param protocol_port: The protocol_port of this CreateMasterSlaveMemberOption.
        :type protocol_port: int
        """
        self._protocol_port = protocol_port

    @property
    def subnet_cidr_id(self):
        r"""Gets the subnet_cidr_id of this CreateMasterSlaveMemberOption.

        **参数解释**：后端服务器所在的子网ID，可以是子网的IPv4子网ID或IPv6子网ID。  **约束限制**： - 该子网和关联的负载均衡器的子网必须在同一VPC下。 - 若所属LB的IP类型后端转发特性已开启，则该字段可以不传，表示添加跨VPC的后端服务器。此时address必须为**私网IPv4**地址，所在的pool的协议必须为UDP/TCP/TLS/HTTP/HTTPS/QUIC/GRPC。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持IPv6，请勿设置为IPv6子网ID。](tag:dt)

        :return: The subnet_cidr_id of this CreateMasterSlaveMemberOption.
        :rtype: str
        """
        return self._subnet_cidr_id

    @subnet_cidr_id.setter
    def subnet_cidr_id(self, subnet_cidr_id):
        r"""Sets the subnet_cidr_id of this CreateMasterSlaveMemberOption.

        **参数解释**：后端服务器所在的子网ID，可以是子网的IPv4子网ID或IPv6子网ID。  **约束限制**： - 该子网和关联的负载均衡器的子网必须在同一VPC下。 - 若所属LB的IP类型后端转发特性已开启，则该字段可以不传，表示添加跨VPC的后端服务器。此时address必须为**私网IPv4**地址，所在的pool的协议必须为UDP/TCP/TLS/HTTP/HTTPS/QUIC/GRPC。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持IPv6，请勿设置为IPv6子网ID。](tag:dt)

        :param subnet_cidr_id: The subnet_cidr_id of this CreateMasterSlaveMemberOption.
        :type subnet_cidr_id: str
        """
        self._subnet_cidr_id = subnet_cidr_id

    @property
    def role(self):
        r"""Gets the role of this CreateMasterSlaveMemberOption.

        **参数解释**：后端服务器的主备状态。  **约束限制**：不涉及  **取值范围**： - master：主后端服务器。 - slave：备后端服务器。  **默认取值**：不涉及

        :return: The role of this CreateMasterSlaveMemberOption.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this CreateMasterSlaveMemberOption.

        **参数解释**：后端服务器的主备状态。  **约束限制**：不涉及  **取值范围**： - master：主后端服务器。 - slave：备后端服务器。  **默认取值**：不涉及

        :param role: The role of this CreateMasterSlaveMemberOption.
        :type role: str
        """
        self._role = role

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
        if not isinstance(other, CreateMasterSlaveMemberOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
