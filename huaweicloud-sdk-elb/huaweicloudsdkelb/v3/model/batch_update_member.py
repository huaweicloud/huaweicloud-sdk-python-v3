# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateMember:

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
        'project_id': 'str',
        'admin_state_up': 'bool',
        'subnet_cidr_id': 'str',
        'protocol_port': 'int',
        'weight': 'int',
        'address': 'str',
        'operating_status': 'str',
        'status': 'list[MemberStatus]',
        'member_type': 'str',
        'instance_id': 'str',
        'port_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'project_id': 'project_id',
        'admin_state_up': 'admin_state_up',
        'subnet_cidr_id': 'subnet_cidr_id',
        'protocol_port': 'protocol_port',
        'weight': 'weight',
        'address': 'address',
        'operating_status': 'operating_status',
        'status': 'status',
        'member_type': 'member_type',
        'instance_id': 'instance_id',
        'port_id': 'port_id'
    }

    def __init__(self, id=None, name=None, project_id=None, admin_state_up=None, subnet_cidr_id=None, protocol_port=None, weight=None, address=None, operating_status=None, status=None, member_type=None, instance_id=None, port_id=None):
        """BatchUpdateMember

        The model defined in huaweicloud sdk

        :param id: 后端服务器ID。 &gt;说明： 此处并非ECS服务器的ID，而是ELB为绑定的后端服务器自动生成的member ID。
        :type id: str
        :param name: 后端服务器名称。
        :type name: str
        :param project_id: 后端服务器所在的项目ID。
        :type project_id: str
        :param admin_state_up: 后端云服务器的管理状态。取值：true、false。  虽然创建、更新请求支持该字段，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。
        :type admin_state_up: bool
        :param subnet_cidr_id: 后端云服务器所在子网的IPv4子网ID或IPv6子网ID。    若所属的LB的跨VPC后端转发特性已开启，则该字段可以不传，表示添加跨VPC的后端服务器。此时address必须为IPv4地址，所在的pool的协议必须为TCP/HTTP/HTTPS。    使用说明：   - 该子网和关联的负载均衡器的子网必须在同一VPC下。   [不支持IPv6，请勿设置为IPv6子网ID。](tag:dt,dt_test)
        :type subnet_cidr_id: str
        :param protocol_port: 后端服务器业务端口号。 &gt;在开启端口透传的pool下的member，该字段不支持更新
        :type protocol_port: int
        :param weight: 后端云服务器的权重，请求将根据pool配置的负载均衡算法和后端云服务器的权重进行负载分发。权重值越大，分发的请求越多。权重为0的后端不再接受新的请求。   取值：0-100，默认1。   使用说明：    - 若所在pool的lb_algorithm取值为SOURCE_IP，该字段无效。
        :type weight: int
        :param address: 后端服务器对应的IP地址。   使用说明：   - 若subnet_cidr_id为空，表示添加跨VPC后端，此时address必须为IPv4地址。   - 若subnet_cidr_id不为空，表示是一个关联到ECS的后端服务器。该IP地址可以是IPv4或IPv6。但必须在subnet_cidr_id对应的子网网段中。且只能指定为关联ECS的主网卡内网IP。   [不支持IPv6，请勿设置为IPv6地址。](tag:dt,dt_test)
        :type address: str
        :param operating_status: 后端云服务器的健康状态。取值： - ONLINE：后端云服务器正常。 - NO_MONITOR：后端云服务器所在的服务器组没有健康检查器。 - OFFLINE：后端云服务器关联的ECS服务器不存在或已关机。
        :type operating_status: str
        :param status: 后端云服务器监听器粒度的的健康状态。 若绑定的监听器在该字段中，则以该字段中监听器对应的operating_stauts为准。 若绑定的监听器不在该字段中，则以外层的operating_status为准。
        :type status: list[:class:`huaweicloudsdkelb.v3.MemberStatus`]
        :param member_type: 后端云服务器的类型。取值： - ip：跨VPC的member。 - instance：关联到ECS的member。
        :type member_type: str
        :param instance_id: member关联的实例ID，空表示跨VPC场景的member。
        :type instance_id: str
        :param port_id: IP地址对应的VPC port ID
        :type port_id: str
        """
        
        

        self._id = None
        self._name = None
        self._project_id = None
        self._admin_state_up = None
        self._subnet_cidr_id = None
        self._protocol_port = None
        self._weight = None
        self._address = None
        self._operating_status = None
        self._status = None
        self._member_type = None
        self._instance_id = None
        self._port_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.project_id = project_id
        self.admin_state_up = admin_state_up
        if subnet_cidr_id is not None:
            self.subnet_cidr_id = subnet_cidr_id
        self.protocol_port = protocol_port
        self.weight = weight
        self.address = address
        self.operating_status = operating_status
        if status is not None:
            self.status = status
        if member_type is not None:
            self.member_type = member_type
        if instance_id is not None:
            self.instance_id = instance_id
        self.port_id = port_id

    @property
    def id(self):
        """Gets the id of this BatchUpdateMember.

        后端服务器ID。 >说明： 此处并非ECS服务器的ID，而是ELB为绑定的后端服务器自动生成的member ID。

        :return: The id of this BatchUpdateMember.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BatchUpdateMember.

        后端服务器ID。 >说明： 此处并非ECS服务器的ID，而是ELB为绑定的后端服务器自动生成的member ID。

        :param id: The id of this BatchUpdateMember.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this BatchUpdateMember.

        后端服务器名称。

        :return: The name of this BatchUpdateMember.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BatchUpdateMember.

        后端服务器名称。

        :param name: The name of this BatchUpdateMember.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this BatchUpdateMember.

        后端服务器所在的项目ID。

        :return: The project_id of this BatchUpdateMember.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this BatchUpdateMember.

        后端服务器所在的项目ID。

        :param project_id: The project_id of this BatchUpdateMember.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this BatchUpdateMember.

        后端云服务器的管理状态。取值：true、false。  虽然创建、更新请求支持该字段，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。

        :return: The admin_state_up of this BatchUpdateMember.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this BatchUpdateMember.

        后端云服务器的管理状态。取值：true、false。  虽然创建、更新请求支持该字段，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。

        :param admin_state_up: The admin_state_up of this BatchUpdateMember.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def subnet_cidr_id(self):
        """Gets the subnet_cidr_id of this BatchUpdateMember.

        后端云服务器所在子网的IPv4子网ID或IPv6子网ID。    若所属的LB的跨VPC后端转发特性已开启，则该字段可以不传，表示添加跨VPC的后端服务器。此时address必须为IPv4地址，所在的pool的协议必须为TCP/HTTP/HTTPS。    使用说明：   - 该子网和关联的负载均衡器的子网必须在同一VPC下。   [不支持IPv6，请勿设置为IPv6子网ID。](tag:dt,dt_test)

        :return: The subnet_cidr_id of this BatchUpdateMember.
        :rtype: str
        """
        return self._subnet_cidr_id

    @subnet_cidr_id.setter
    def subnet_cidr_id(self, subnet_cidr_id):
        """Sets the subnet_cidr_id of this BatchUpdateMember.

        后端云服务器所在子网的IPv4子网ID或IPv6子网ID。    若所属的LB的跨VPC后端转发特性已开启，则该字段可以不传，表示添加跨VPC的后端服务器。此时address必须为IPv4地址，所在的pool的协议必须为TCP/HTTP/HTTPS。    使用说明：   - 该子网和关联的负载均衡器的子网必须在同一VPC下。   [不支持IPv6，请勿设置为IPv6子网ID。](tag:dt,dt_test)

        :param subnet_cidr_id: The subnet_cidr_id of this BatchUpdateMember.
        :type subnet_cidr_id: str
        """
        self._subnet_cidr_id = subnet_cidr_id

    @property
    def protocol_port(self):
        """Gets the protocol_port of this BatchUpdateMember.

        后端服务器业务端口号。 >在开启端口透传的pool下的member，该字段不支持更新

        :return: The protocol_port of this BatchUpdateMember.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this BatchUpdateMember.

        后端服务器业务端口号。 >在开启端口透传的pool下的member，该字段不支持更新

        :param protocol_port: The protocol_port of this BatchUpdateMember.
        :type protocol_port: int
        """
        self._protocol_port = protocol_port

    @property
    def weight(self):
        """Gets the weight of this BatchUpdateMember.

        后端云服务器的权重，请求将根据pool配置的负载均衡算法和后端云服务器的权重进行负载分发。权重值越大，分发的请求越多。权重为0的后端不再接受新的请求。   取值：0-100，默认1。   使用说明：    - 若所在pool的lb_algorithm取值为SOURCE_IP，该字段无效。

        :return: The weight of this BatchUpdateMember.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this BatchUpdateMember.

        后端云服务器的权重，请求将根据pool配置的负载均衡算法和后端云服务器的权重进行负载分发。权重值越大，分发的请求越多。权重为0的后端不再接受新的请求。   取值：0-100，默认1。   使用说明：    - 若所在pool的lb_algorithm取值为SOURCE_IP，该字段无效。

        :param weight: The weight of this BatchUpdateMember.
        :type weight: int
        """
        self._weight = weight

    @property
    def address(self):
        """Gets the address of this BatchUpdateMember.

        后端服务器对应的IP地址。   使用说明：   - 若subnet_cidr_id为空，表示添加跨VPC后端，此时address必须为IPv4地址。   - 若subnet_cidr_id不为空，表示是一个关联到ECS的后端服务器。该IP地址可以是IPv4或IPv6。但必须在subnet_cidr_id对应的子网网段中。且只能指定为关联ECS的主网卡内网IP。   [不支持IPv6，请勿设置为IPv6地址。](tag:dt,dt_test)

        :return: The address of this BatchUpdateMember.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this BatchUpdateMember.

        后端服务器对应的IP地址。   使用说明：   - 若subnet_cidr_id为空，表示添加跨VPC后端，此时address必须为IPv4地址。   - 若subnet_cidr_id不为空，表示是一个关联到ECS的后端服务器。该IP地址可以是IPv4或IPv6。但必须在subnet_cidr_id对应的子网网段中。且只能指定为关联ECS的主网卡内网IP。   [不支持IPv6，请勿设置为IPv6地址。](tag:dt,dt_test)

        :param address: The address of this BatchUpdateMember.
        :type address: str
        """
        self._address = address

    @property
    def operating_status(self):
        """Gets the operating_status of this BatchUpdateMember.

        后端云服务器的健康状态。取值： - ONLINE：后端云服务器正常。 - NO_MONITOR：后端云服务器所在的服务器组没有健康检查器。 - OFFLINE：后端云服务器关联的ECS服务器不存在或已关机。

        :return: The operating_status of this BatchUpdateMember.
        :rtype: str
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        """Sets the operating_status of this BatchUpdateMember.

        后端云服务器的健康状态。取值： - ONLINE：后端云服务器正常。 - NO_MONITOR：后端云服务器所在的服务器组没有健康检查器。 - OFFLINE：后端云服务器关联的ECS服务器不存在或已关机。

        :param operating_status: The operating_status of this BatchUpdateMember.
        :type operating_status: str
        """
        self._operating_status = operating_status

    @property
    def status(self):
        """Gets the status of this BatchUpdateMember.

        后端云服务器监听器粒度的的健康状态。 若绑定的监听器在该字段中，则以该字段中监听器对应的operating_stauts为准。 若绑定的监听器不在该字段中，则以外层的operating_status为准。

        :return: The status of this BatchUpdateMember.
        :rtype: list[:class:`huaweicloudsdkelb.v3.MemberStatus`]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BatchUpdateMember.

        后端云服务器监听器粒度的的健康状态。 若绑定的监听器在该字段中，则以该字段中监听器对应的operating_stauts为准。 若绑定的监听器不在该字段中，则以外层的operating_status为准。

        :param status: The status of this BatchUpdateMember.
        :type status: list[:class:`huaweicloudsdkelb.v3.MemberStatus`]
        """
        self._status = status

    @property
    def member_type(self):
        """Gets the member_type of this BatchUpdateMember.

        后端云服务器的类型。取值： - ip：跨VPC的member。 - instance：关联到ECS的member。

        :return: The member_type of this BatchUpdateMember.
        :rtype: str
        """
        return self._member_type

    @member_type.setter
    def member_type(self, member_type):
        """Sets the member_type of this BatchUpdateMember.

        后端云服务器的类型。取值： - ip：跨VPC的member。 - instance：关联到ECS的member。

        :param member_type: The member_type of this BatchUpdateMember.
        :type member_type: str
        """
        self._member_type = member_type

    @property
    def instance_id(self):
        """Gets the instance_id of this BatchUpdateMember.

        member关联的实例ID，空表示跨VPC场景的member。

        :return: The instance_id of this BatchUpdateMember.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this BatchUpdateMember.

        member关联的实例ID，空表示跨VPC场景的member。

        :param instance_id: The instance_id of this BatchUpdateMember.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def port_id(self):
        """Gets the port_id of this BatchUpdateMember.

        IP地址对应的VPC port ID

        :return: The port_id of this BatchUpdateMember.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this BatchUpdateMember.

        IP地址对应的VPC port ID

        :param port_id: The port_id of this BatchUpdateMember.
        :type port_id: str
        """
        self._port_id = port_id

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
        if not isinstance(other, BatchUpdateMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
