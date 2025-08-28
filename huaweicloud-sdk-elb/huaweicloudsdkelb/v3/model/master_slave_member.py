# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MasterSlaveMember:

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
        'name': 'str',
        'admin_state_up': 'bool',
        'subnet_cidr_id': 'str',
        'protocol_port': 'int',
        'address': 'str',
        'ip_version': 'str',
        'device_owner': 'str',
        'device_id': 'str',
        'operating_status': 'str',
        'reason': 'MemberHealthCheckFailedReason',
        'member_type': 'str',
        'instance_id': 'str',
        'role': 'str',
        'status': 'list[ListenerMemberInfo]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'admin_state_up': 'admin_state_up',
        'subnet_cidr_id': 'subnet_cidr_id',
        'protocol_port': 'protocol_port',
        'address': 'address',
        'ip_version': 'ip_version',
        'device_owner': 'device_owner',
        'device_id': 'device_id',
        'operating_status': 'operating_status',
        'reason': 'reason',
        'member_type': 'member_type',
        'instance_id': 'instance_id',
        'role': 'role',
        'status': 'status'
    }

    def __init__(self, id=None, name=None, admin_state_up=None, subnet_cidr_id=None, protocol_port=None, address=None, ip_version=None, device_owner=None, device_id=None, operating_status=None, reason=None, member_type=None, instance_id=None, role=None, status=None):
        r"""MasterSlaveMember

        The model defined in huaweicloud sdk

        :param id: **参数解释**：后端服务器ID。  **取值范围**：不涉及
        :type id: str
        :param name: **参数解释**：后端服务器名称。  **取值范围**：不涉及
        :type name: str
        :param admin_state_up: **参数解释**：后端服务器的管理状态。 虽然创建、更新请求支持该字段，但实际取值决定于后端服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。  **取值范围**：true、false。
        :type admin_state_up: bool
        :param subnet_cidr_id: **参数解释**：后端服务器所在子网的IPv4子网ID或IPv6子网ID。 若所属的LB的IP类型后端转发特性已开启，则该字段可以不传，表示添加跨VPC的后端服务器。此时address必须为**私网IPv4**地址，所在的pool的协议必须为UDP/TCP/TLS/HTTP/HTTPS/QUIC/GRPC。  **取值范围**：不涉及  [不支持IPv6，请勿设置为IPv6子网ID。](tag:dt)
        :type subnet_cidr_id: str
        :param protocol_port: **参数解释**：后端服务器业务端口。  &gt;在开启端口透传的pool下创建member传该字段不生效，可不传该字段。
        :type protocol_port: int
        :param address: **参数解释**：后端服务器对应的IP地址。  **取值范围**：不涉及  [不支持IPv6，请勿设置为IPv6地址。](tag:dt)
        :type address: str
        :param ip_version: **参数解释**：当前后端服务器的IP地址版本，由后端系统自动根据传入的address字段确定。  **取值范围**：v4、v6
        :type ip_version: str
        :param device_owner: **参数解释**：设备所有者。  **取值范围**：不涉及 - 空，表示后端服务器未关联到ECS。 - compute:{az_name}，表示关联到ECS，其中{az_name}表示ECS所在可用区名。 - compute:subeni，表示辅助弹性网卡。  不支持该字段，请勿使用。
        :type device_owner: str
        :param device_id: **参数解释**：关联的ECS ID，为空表示后端服务器未关联到ECS。  **取值范围**：不涉及  不支持该字段，请勿使用。
        :type device_id: str
        :param operating_status: **参数解释**：后端服务器的健康状态。  **取值范围**：不涉及 - ONLINE：后端服务器正常。 - NO_MONITOR：后端服务器所在的服务器组没有健康检查器。 - OFFLINE：后端服务器关联的ECS服务器不存在或已关机。
        :type operating_status: str
        :param reason: 
        :type reason: :class:`huaweicloudsdkelb.v3.MemberHealthCheckFailedReason`
        :param member_type: **参数解释**：后端服务器的类型。  **取值范围**： - ip：跨VPC的member。 - instance：关联到ECS的member。
        :type member_type: str
        :param instance_id: **参数解释**：member关联的实例ID。空表示member关联的实例为非真实设备 （如：跨VPC场景）。  **取值范围**：不涉及
        :type instance_id: str
        :param role: **参数解释**：后端服务器的主备状态。  **取值范围**：不涉及
        :type role: str
        :param status: **参数解释**：后端服务器监听器粒度的的健康状态。 若绑定的监听器在该字段中，则以该字段中监听器对应的operating_status为准。 若绑定的监听器不在该字段中，则以外层的operating_status为准。  **取值范围**：不涉及
        :type status: list[:class:`huaweicloudsdkelb.v3.ListenerMemberInfo`]
        """
        
        

        self._id = None
        self._name = None
        self._admin_state_up = None
        self._subnet_cidr_id = None
        self._protocol_port = None
        self._address = None
        self._ip_version = None
        self._device_owner = None
        self._device_id = None
        self._operating_status = None
        self._reason = None
        self._member_type = None
        self._instance_id = None
        self._role = None
        self._status = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.admin_state_up = admin_state_up
        self.subnet_cidr_id = subnet_cidr_id
        self.protocol_port = protocol_port
        self.address = address
        self.ip_version = ip_version
        self.device_owner = device_owner
        self.device_id = device_id
        self.operating_status = operating_status
        if reason is not None:
            self.reason = reason
        self.member_type = member_type
        self.instance_id = instance_id
        self.role = role
        self.status = status

    @property
    def id(self):
        r"""Gets the id of this MasterSlaveMember.

        **参数解释**：后端服务器ID。  **取值范围**：不涉及

        :return: The id of this MasterSlaveMember.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MasterSlaveMember.

        **参数解释**：后端服务器ID。  **取值范围**：不涉及

        :param id: The id of this MasterSlaveMember.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this MasterSlaveMember.

        **参数解释**：后端服务器名称。  **取值范围**：不涉及

        :return: The name of this MasterSlaveMember.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this MasterSlaveMember.

        **参数解释**：后端服务器名称。  **取值范围**：不涉及

        :param name: The name of this MasterSlaveMember.
        :type name: str
        """
        self._name = name

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this MasterSlaveMember.

        **参数解释**：后端服务器的管理状态。 虽然创建、更新请求支持该字段，但实际取值决定于后端服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。  **取值范围**：true、false。

        :return: The admin_state_up of this MasterSlaveMember.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this MasterSlaveMember.

        **参数解释**：后端服务器的管理状态。 虽然创建、更新请求支持该字段，但实际取值决定于后端服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。  **取值范围**：true、false。

        :param admin_state_up: The admin_state_up of this MasterSlaveMember.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def subnet_cidr_id(self):
        r"""Gets the subnet_cidr_id of this MasterSlaveMember.

        **参数解释**：后端服务器所在子网的IPv4子网ID或IPv6子网ID。 若所属的LB的IP类型后端转发特性已开启，则该字段可以不传，表示添加跨VPC的后端服务器。此时address必须为**私网IPv4**地址，所在的pool的协议必须为UDP/TCP/TLS/HTTP/HTTPS/QUIC/GRPC。  **取值范围**：不涉及  [不支持IPv6，请勿设置为IPv6子网ID。](tag:dt)

        :return: The subnet_cidr_id of this MasterSlaveMember.
        :rtype: str
        """
        return self._subnet_cidr_id

    @subnet_cidr_id.setter
    def subnet_cidr_id(self, subnet_cidr_id):
        r"""Sets the subnet_cidr_id of this MasterSlaveMember.

        **参数解释**：后端服务器所在子网的IPv4子网ID或IPv6子网ID。 若所属的LB的IP类型后端转发特性已开启，则该字段可以不传，表示添加跨VPC的后端服务器。此时address必须为**私网IPv4**地址，所在的pool的协议必须为UDP/TCP/TLS/HTTP/HTTPS/QUIC/GRPC。  **取值范围**：不涉及  [不支持IPv6，请勿设置为IPv6子网ID。](tag:dt)

        :param subnet_cidr_id: The subnet_cidr_id of this MasterSlaveMember.
        :type subnet_cidr_id: str
        """
        self._subnet_cidr_id = subnet_cidr_id

    @property
    def protocol_port(self):
        r"""Gets the protocol_port of this MasterSlaveMember.

        **参数解释**：后端服务器业务端口。  >在开启端口透传的pool下创建member传该字段不生效，可不传该字段。

        :return: The protocol_port of this MasterSlaveMember.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        r"""Sets the protocol_port of this MasterSlaveMember.

        **参数解释**：后端服务器业务端口。  >在开启端口透传的pool下创建member传该字段不生效，可不传该字段。

        :param protocol_port: The protocol_port of this MasterSlaveMember.
        :type protocol_port: int
        """
        self._protocol_port = protocol_port

    @property
    def address(self):
        r"""Gets the address of this MasterSlaveMember.

        **参数解释**：后端服务器对应的IP地址。  **取值范围**：不涉及  [不支持IPv6，请勿设置为IPv6地址。](tag:dt)

        :return: The address of this MasterSlaveMember.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this MasterSlaveMember.

        **参数解释**：后端服务器对应的IP地址。  **取值范围**：不涉及  [不支持IPv6，请勿设置为IPv6地址。](tag:dt)

        :param address: The address of this MasterSlaveMember.
        :type address: str
        """
        self._address = address

    @property
    def ip_version(self):
        r"""Gets the ip_version of this MasterSlaveMember.

        **参数解释**：当前后端服务器的IP地址版本，由后端系统自动根据传入的address字段确定。  **取值范围**：v4、v6

        :return: The ip_version of this MasterSlaveMember.
        :rtype: str
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this MasterSlaveMember.

        **参数解释**：当前后端服务器的IP地址版本，由后端系统自动根据传入的address字段确定。  **取值范围**：v4、v6

        :param ip_version: The ip_version of this MasterSlaveMember.
        :type ip_version: str
        """
        self._ip_version = ip_version

    @property
    def device_owner(self):
        r"""Gets the device_owner of this MasterSlaveMember.

        **参数解释**：设备所有者。  **取值范围**：不涉及 - 空，表示后端服务器未关联到ECS。 - compute:{az_name}，表示关联到ECS，其中{az_name}表示ECS所在可用区名。 - compute:subeni，表示辅助弹性网卡。  不支持该字段，请勿使用。

        :return: The device_owner of this MasterSlaveMember.
        :rtype: str
        """
        return self._device_owner

    @device_owner.setter
    def device_owner(self, device_owner):
        r"""Sets the device_owner of this MasterSlaveMember.

        **参数解释**：设备所有者。  **取值范围**：不涉及 - 空，表示后端服务器未关联到ECS。 - compute:{az_name}，表示关联到ECS，其中{az_name}表示ECS所在可用区名。 - compute:subeni，表示辅助弹性网卡。  不支持该字段，请勿使用。

        :param device_owner: The device_owner of this MasterSlaveMember.
        :type device_owner: str
        """
        self._device_owner = device_owner

    @property
    def device_id(self):
        r"""Gets the device_id of this MasterSlaveMember.

        **参数解释**：关联的ECS ID，为空表示后端服务器未关联到ECS。  **取值范围**：不涉及  不支持该字段，请勿使用。

        :return: The device_id of this MasterSlaveMember.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        r"""Sets the device_id of this MasterSlaveMember.

        **参数解释**：关联的ECS ID，为空表示后端服务器未关联到ECS。  **取值范围**：不涉及  不支持该字段，请勿使用。

        :param device_id: The device_id of this MasterSlaveMember.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def operating_status(self):
        r"""Gets the operating_status of this MasterSlaveMember.

        **参数解释**：后端服务器的健康状态。  **取值范围**：不涉及 - ONLINE：后端服务器正常。 - NO_MONITOR：后端服务器所在的服务器组没有健康检查器。 - OFFLINE：后端服务器关联的ECS服务器不存在或已关机。

        :return: The operating_status of this MasterSlaveMember.
        :rtype: str
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        r"""Sets the operating_status of this MasterSlaveMember.

        **参数解释**：后端服务器的健康状态。  **取值范围**：不涉及 - ONLINE：后端服务器正常。 - NO_MONITOR：后端服务器所在的服务器组没有健康检查器。 - OFFLINE：后端服务器关联的ECS服务器不存在或已关机。

        :param operating_status: The operating_status of this MasterSlaveMember.
        :type operating_status: str
        """
        self._operating_status = operating_status

    @property
    def reason(self):
        r"""Gets the reason of this MasterSlaveMember.

        :return: The reason of this MasterSlaveMember.
        :rtype: :class:`huaweicloudsdkelb.v3.MemberHealthCheckFailedReason`
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this MasterSlaveMember.

        :param reason: The reason of this MasterSlaveMember.
        :type reason: :class:`huaweicloudsdkelb.v3.MemberHealthCheckFailedReason`
        """
        self._reason = reason

    @property
    def member_type(self):
        r"""Gets the member_type of this MasterSlaveMember.

        **参数解释**：后端服务器的类型。  **取值范围**： - ip：跨VPC的member。 - instance：关联到ECS的member。

        :return: The member_type of this MasterSlaveMember.
        :rtype: str
        """
        return self._member_type

    @member_type.setter
    def member_type(self, member_type):
        r"""Sets the member_type of this MasterSlaveMember.

        **参数解释**：后端服务器的类型。  **取值范围**： - ip：跨VPC的member。 - instance：关联到ECS的member。

        :param member_type: The member_type of this MasterSlaveMember.
        :type member_type: str
        """
        self._member_type = member_type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this MasterSlaveMember.

        **参数解释**：member关联的实例ID。空表示member关联的实例为非真实设备 （如：跨VPC场景）。  **取值范围**：不涉及

        :return: The instance_id of this MasterSlaveMember.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this MasterSlaveMember.

        **参数解释**：member关联的实例ID。空表示member关联的实例为非真实设备 （如：跨VPC场景）。  **取值范围**：不涉及

        :param instance_id: The instance_id of this MasterSlaveMember.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def role(self):
        r"""Gets the role of this MasterSlaveMember.

        **参数解释**：后端服务器的主备状态。  **取值范围**：不涉及

        :return: The role of this MasterSlaveMember.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this MasterSlaveMember.

        **参数解释**：后端服务器的主备状态。  **取值范围**：不涉及

        :param role: The role of this MasterSlaveMember.
        :type role: str
        """
        self._role = role

    @property
    def status(self):
        r"""Gets the status of this MasterSlaveMember.

        **参数解释**：后端服务器监听器粒度的的健康状态。 若绑定的监听器在该字段中，则以该字段中监听器对应的operating_status为准。 若绑定的监听器不在该字段中，则以外层的operating_status为准。  **取值范围**：不涉及

        :return: The status of this MasterSlaveMember.
        :rtype: list[:class:`huaweicloudsdkelb.v3.ListenerMemberInfo`]
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this MasterSlaveMember.

        **参数解释**：后端服务器监听器粒度的的健康状态。 若绑定的监听器在该字段中，则以该字段中监听器对应的operating_status为准。 若绑定的监听器不在该字段中，则以外层的operating_status为准。  **取值范围**：不涉及

        :param status: The status of this MasterSlaveMember.
        :type status: list[:class:`huaweicloudsdkelb.v3.ListenerMemberInfo`]
        """
        self._status = status

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
        if not isinstance(other, MasterSlaveMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
