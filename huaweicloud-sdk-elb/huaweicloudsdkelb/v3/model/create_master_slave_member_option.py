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
        """CreateMasterSlaveMemberOption

        The model defined in huaweicloud sdk

        :param address: 后端服务器对应的IP地址。  使用说明： - 若subnet_cidr_id为空，表示添加跨VPC后端，此时address必须为IPv4地址。 - 若subnet_cidr_id不为空，表示是一个关联到ECS的后端服务器。 该IP地址可以是IPv4或IPv6。但必须在subnet_cidr_id对应的子网网段中。且只能指定为关联ECS的主网卡内网IP。  [不支持IPv6，请勿设置为IPv6地址。](tag:dt,dt_test)
        :type address: str
        :param admin_state_up: 后端云服务器的管理状态。  取值：true。  虽然创建、更新请求支持该字段，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。
        :type admin_state_up: bool
        :param name: 后端云服务器名称。
        :type name: str
        :param protocol_port: 后端服务器业务端口。 &gt;在开启端口透传的pool下创建member传该字段不生效，可不传该字段。
        :type protocol_port: int
        :param subnet_cidr_id: 后端云服务器所在的子网ID，可以是子网的IPv4子网ID或IPv6子网ID。  使用说明： - 该子网和关联的负载均衡器的子网必须在同一VPC下。 - 若所属LB的跨VPC后端转发特性已开启，则该字段可以不传，表示添加跨VPC的后端服务器。 此时address必须为IPv4地址，所在的pool的协议必须为TCP/HTTP/HTTPS。  [不支持IPv6，请勿设置为IPv6子网ID。](tag:dt,dt_test)
        :type subnet_cidr_id: str
        :param role: 后端服务器的主备状态。  取值范围： - master：主后端服务器。 - slave：备后端服务器。
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
        self.protocol_port = protocol_port
        if subnet_cidr_id is not None:
            self.subnet_cidr_id = subnet_cidr_id
        self.role = role

    @property
    def address(self):
        """Gets the address of this CreateMasterSlaveMemberOption.

        后端服务器对应的IP地址。  使用说明： - 若subnet_cidr_id为空，表示添加跨VPC后端，此时address必须为IPv4地址。 - 若subnet_cidr_id不为空，表示是一个关联到ECS的后端服务器。 该IP地址可以是IPv4或IPv6。但必须在subnet_cidr_id对应的子网网段中。且只能指定为关联ECS的主网卡内网IP。  [不支持IPv6，请勿设置为IPv6地址。](tag:dt,dt_test)

        :return: The address of this CreateMasterSlaveMemberOption.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CreateMasterSlaveMemberOption.

        后端服务器对应的IP地址。  使用说明： - 若subnet_cidr_id为空，表示添加跨VPC后端，此时address必须为IPv4地址。 - 若subnet_cidr_id不为空，表示是一个关联到ECS的后端服务器。 该IP地址可以是IPv4或IPv6。但必须在subnet_cidr_id对应的子网网段中。且只能指定为关联ECS的主网卡内网IP。  [不支持IPv6，请勿设置为IPv6地址。](tag:dt,dt_test)

        :param address: The address of this CreateMasterSlaveMemberOption.
        :type address: str
        """
        self._address = address

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this CreateMasterSlaveMemberOption.

        后端云服务器的管理状态。  取值：true。  虽然创建、更新请求支持该字段，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。

        :return: The admin_state_up of this CreateMasterSlaveMemberOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this CreateMasterSlaveMemberOption.

        后端云服务器的管理状态。  取值：true。  虽然创建、更新请求支持该字段，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。

        :param admin_state_up: The admin_state_up of this CreateMasterSlaveMemberOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def name(self):
        """Gets the name of this CreateMasterSlaveMemberOption.

        后端云服务器名称。

        :return: The name of this CreateMasterSlaveMemberOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateMasterSlaveMemberOption.

        后端云服务器名称。

        :param name: The name of this CreateMasterSlaveMemberOption.
        :type name: str
        """
        self._name = name

    @property
    def protocol_port(self):
        """Gets the protocol_port of this CreateMasterSlaveMemberOption.

        后端服务器业务端口。 >在开启端口透传的pool下创建member传该字段不生效，可不传该字段。

        :return: The protocol_port of this CreateMasterSlaveMemberOption.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this CreateMasterSlaveMemberOption.

        后端服务器业务端口。 >在开启端口透传的pool下创建member传该字段不生效，可不传该字段。

        :param protocol_port: The protocol_port of this CreateMasterSlaveMemberOption.
        :type protocol_port: int
        """
        self._protocol_port = protocol_port

    @property
    def subnet_cidr_id(self):
        """Gets the subnet_cidr_id of this CreateMasterSlaveMemberOption.

        后端云服务器所在的子网ID，可以是子网的IPv4子网ID或IPv6子网ID。  使用说明： - 该子网和关联的负载均衡器的子网必须在同一VPC下。 - 若所属LB的跨VPC后端转发特性已开启，则该字段可以不传，表示添加跨VPC的后端服务器。 此时address必须为IPv4地址，所在的pool的协议必须为TCP/HTTP/HTTPS。  [不支持IPv6，请勿设置为IPv6子网ID。](tag:dt,dt_test)

        :return: The subnet_cidr_id of this CreateMasterSlaveMemberOption.
        :rtype: str
        """
        return self._subnet_cidr_id

    @subnet_cidr_id.setter
    def subnet_cidr_id(self, subnet_cidr_id):
        """Sets the subnet_cidr_id of this CreateMasterSlaveMemberOption.

        后端云服务器所在的子网ID，可以是子网的IPv4子网ID或IPv6子网ID。  使用说明： - 该子网和关联的负载均衡器的子网必须在同一VPC下。 - 若所属LB的跨VPC后端转发特性已开启，则该字段可以不传，表示添加跨VPC的后端服务器。 此时address必须为IPv4地址，所在的pool的协议必须为TCP/HTTP/HTTPS。  [不支持IPv6，请勿设置为IPv6子网ID。](tag:dt,dt_test)

        :param subnet_cidr_id: The subnet_cidr_id of this CreateMasterSlaveMemberOption.
        :type subnet_cidr_id: str
        """
        self._subnet_cidr_id = subnet_cidr_id

    @property
    def role(self):
        """Gets the role of this CreateMasterSlaveMemberOption.

        后端服务器的主备状态。  取值范围： - master：主后端服务器。 - slave：备后端服务器。

        :return: The role of this CreateMasterSlaveMemberOption.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this CreateMasterSlaveMemberOption.

        后端服务器的主备状态。  取值范围： - master：主后端服务器。 - slave：备后端服务器。

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
