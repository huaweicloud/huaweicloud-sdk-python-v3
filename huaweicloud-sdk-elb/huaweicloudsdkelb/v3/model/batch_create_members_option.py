# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateMembersOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'availability_zone': 'str',
        'address': 'str',
        'protocol_port': 'int',
        'subnet_cidr_id': 'str',
        'weight': 'int'
    }

    attribute_map = {
        'name': 'name',
        'availability_zone': 'availability_zone',
        'address': 'address',
        'protocol_port': 'protocol_port',
        'subnet_cidr_id': 'subnet_cidr_id',
        'weight': 'weight'
    }

    def __init__(self, name=None, availability_zone=None, address=None, protocol_port=None, subnet_cidr_id=None, weight=None):
        r"""BatchCreateMembersOption

        The model defined in huaweicloud sdk

        :param name: **参数解释**：后端服务器名称。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type name: str
        :param availability_zone: **参数解释**：后端服务器的可用区。  **约束限制**：仅支持IP类型后端服务器设置该字段。且后端服务器组开启可用区亲和时，IP类型后端服务器必须配置该字段为有效非空值。  **取值范围**：本region中ECS可选择的可用区。  **默认取值**：不涉及
        :type availability_zone: str
        :param address: **参数解释**：后端服务器的对应的IP地址，这个IP必须在subnet_cidr_id字段的子网网段中。例如：192.168.3.11。  **约束限制**：subnet_cidr_id为空代表添加IP类型后端，此时address必须为**私网IPv4**地址。  **取值范围**：不涉及  **默认取值**：不涉及
        :type address: str
        :param protocol_port: **参数解释**：后端服务器业务端口。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  [网关型LB，即pool协议为IP时，protocol_port必须设置为0。](tag:hws_eu) &gt;在开启端口透传的pool下创建member传该字段不生效，可不传该字段。
        :type protocol_port: int
        :param subnet_cidr_id: **参数解释**：后端服务器所在的子网，可以是IPv4或IPv6子网。若是IPv4子网，使用对应子网的子网ID（neutron_subnet_id）；若是IPv6子网，使用对应子网的网络ID（neutron_network_id）。 ipv4子网的子网ID可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_subnet_id得到 ipv6子网的网络ID可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_network_id得到  **约束限制**： - 该子网和关联的负载均衡器的子网必须在同一VPC下。 - 若所属LB的IP类型后端转发已开启（ip_target_enable&#x3D;true），则该字段可以不传，表示添加跨VPC的后端服务器。此时address必须为**私网IPv4**地址，所在的pool的协议必须为UDP/TCP/TLS/HTTP/HTTPS/QUIC/GRPC。 - 若所属LB未开启IP类型后端转发，该参数必填。 [- 网关型LB，即pool协议为IP时，必须指定该子网，且必须和负载均衡器的子网在同一个VPC下，但不能相同。](tag:hws_eu)  **取值范围**：不涉及  **默认取值**：不涉及  [不支持IPv6，请勿设置为IPv6子网ID。](tag:dt)
        :type subnet_cidr_id: str
        :param weight: **参数解释**：后端服务器的权重，请求将根据pool配置的负载均衡算法和后端服务器的权重进行负载分发。权重值越大，分发的请求越多。权重为0的后端不再接受新的请求。  **约束限制**：若所在pool的lb_algorithm取值为SOURCE_IP或QUIC_CID，该字段无效。  **取值范围**：0-100  **默认取值**：1
        :type weight: int
        """
        
        

        self._name = None
        self._availability_zone = None
        self._address = None
        self._protocol_port = None
        self._subnet_cidr_id = None
        self._weight = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if availability_zone is not None:
            self.availability_zone = availability_zone
        self.address = address
        self.protocol_port = protocol_port
        if subnet_cidr_id is not None:
            self.subnet_cidr_id = subnet_cidr_id
        if weight is not None:
            self.weight = weight

    @property
    def name(self):
        r"""Gets the name of this BatchCreateMembersOption.

        **参数解释**：后端服务器名称。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The name of this BatchCreateMembersOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BatchCreateMembersOption.

        **参数解释**：后端服务器名称。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param name: The name of this BatchCreateMembersOption.
        :type name: str
        """
        self._name = name

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this BatchCreateMembersOption.

        **参数解释**：后端服务器的可用区。  **约束限制**：仅支持IP类型后端服务器设置该字段。且后端服务器组开启可用区亲和时，IP类型后端服务器必须配置该字段为有效非空值。  **取值范围**：本region中ECS可选择的可用区。  **默认取值**：不涉及

        :return: The availability_zone of this BatchCreateMembersOption.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this BatchCreateMembersOption.

        **参数解释**：后端服务器的可用区。  **约束限制**：仅支持IP类型后端服务器设置该字段。且后端服务器组开启可用区亲和时，IP类型后端服务器必须配置该字段为有效非空值。  **取值范围**：本region中ECS可选择的可用区。  **默认取值**：不涉及

        :param availability_zone: The availability_zone of this BatchCreateMembersOption.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def address(self):
        r"""Gets the address of this BatchCreateMembersOption.

        **参数解释**：后端服务器的对应的IP地址，这个IP必须在subnet_cidr_id字段的子网网段中。例如：192.168.3.11。  **约束限制**：subnet_cidr_id为空代表添加IP类型后端，此时address必须为**私网IPv4**地址。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The address of this BatchCreateMembersOption.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this BatchCreateMembersOption.

        **参数解释**：后端服务器的对应的IP地址，这个IP必须在subnet_cidr_id字段的子网网段中。例如：192.168.3.11。  **约束限制**：subnet_cidr_id为空代表添加IP类型后端，此时address必须为**私网IPv4**地址。  **取值范围**：不涉及  **默认取值**：不涉及

        :param address: The address of this BatchCreateMembersOption.
        :type address: str
        """
        self._address = address

    @property
    def protocol_port(self):
        r"""Gets the protocol_port of this BatchCreateMembersOption.

        **参数解释**：后端服务器业务端口。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  [网关型LB，即pool协议为IP时，protocol_port必须设置为0。](tag:hws_eu) >在开启端口透传的pool下创建member传该字段不生效，可不传该字段。

        :return: The protocol_port of this BatchCreateMembersOption.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        r"""Sets the protocol_port of this BatchCreateMembersOption.

        **参数解释**：后端服务器业务端口。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  [网关型LB，即pool协议为IP时，protocol_port必须设置为0。](tag:hws_eu) >在开启端口透传的pool下创建member传该字段不生效，可不传该字段。

        :param protocol_port: The protocol_port of this BatchCreateMembersOption.
        :type protocol_port: int
        """
        self._protocol_port = protocol_port

    @property
    def subnet_cidr_id(self):
        r"""Gets the subnet_cidr_id of this BatchCreateMembersOption.

        **参数解释**：后端服务器所在的子网，可以是IPv4或IPv6子网。若是IPv4子网，使用对应子网的子网ID（neutron_subnet_id）；若是IPv6子网，使用对应子网的网络ID（neutron_network_id）。 ipv4子网的子网ID可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_subnet_id得到 ipv6子网的网络ID可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_network_id得到  **约束限制**： - 该子网和关联的负载均衡器的子网必须在同一VPC下。 - 若所属LB的IP类型后端转发已开启（ip_target_enable=true），则该字段可以不传，表示添加跨VPC的后端服务器。此时address必须为**私网IPv4**地址，所在的pool的协议必须为UDP/TCP/TLS/HTTP/HTTPS/QUIC/GRPC。 - 若所属LB未开启IP类型后端转发，该参数必填。 [- 网关型LB，即pool协议为IP时，必须指定该子网，且必须和负载均衡器的子网在同一个VPC下，但不能相同。](tag:hws_eu)  **取值范围**：不涉及  **默认取值**：不涉及  [不支持IPv6，请勿设置为IPv6子网ID。](tag:dt)

        :return: The subnet_cidr_id of this BatchCreateMembersOption.
        :rtype: str
        """
        return self._subnet_cidr_id

    @subnet_cidr_id.setter
    def subnet_cidr_id(self, subnet_cidr_id):
        r"""Sets the subnet_cidr_id of this BatchCreateMembersOption.

        **参数解释**：后端服务器所在的子网，可以是IPv4或IPv6子网。若是IPv4子网，使用对应子网的子网ID（neutron_subnet_id）；若是IPv6子网，使用对应子网的网络ID（neutron_network_id）。 ipv4子网的子网ID可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_subnet_id得到 ipv6子网的网络ID可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_network_id得到  **约束限制**： - 该子网和关联的负载均衡器的子网必须在同一VPC下。 - 若所属LB的IP类型后端转发已开启（ip_target_enable=true），则该字段可以不传，表示添加跨VPC的后端服务器。此时address必须为**私网IPv4**地址，所在的pool的协议必须为UDP/TCP/TLS/HTTP/HTTPS/QUIC/GRPC。 - 若所属LB未开启IP类型后端转发，该参数必填。 [- 网关型LB，即pool协议为IP时，必须指定该子网，且必须和负载均衡器的子网在同一个VPC下，但不能相同。](tag:hws_eu)  **取值范围**：不涉及  **默认取值**：不涉及  [不支持IPv6，请勿设置为IPv6子网ID。](tag:dt)

        :param subnet_cidr_id: The subnet_cidr_id of this BatchCreateMembersOption.
        :type subnet_cidr_id: str
        """
        self._subnet_cidr_id = subnet_cidr_id

    @property
    def weight(self):
        r"""Gets the weight of this BatchCreateMembersOption.

        **参数解释**：后端服务器的权重，请求将根据pool配置的负载均衡算法和后端服务器的权重进行负载分发。权重值越大，分发的请求越多。权重为0的后端不再接受新的请求。  **约束限制**：若所在pool的lb_algorithm取值为SOURCE_IP或QUIC_CID，该字段无效。  **取值范围**：0-100  **默认取值**：1

        :return: The weight of this BatchCreateMembersOption.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this BatchCreateMembersOption.

        **参数解释**：后端服务器的权重，请求将根据pool配置的负载均衡算法和后端服务器的权重进行负载分发。权重值越大，分发的请求越多。权重为0的后端不再接受新的请求。  **约束限制**：若所在pool的lb_algorithm取值为SOURCE_IP或QUIC_CID，该字段无效。  **取值范围**：0-100  **默认取值**：1

        :param weight: The weight of this BatchCreateMembersOption.
        :type weight: int
        """
        self._weight = weight

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
        if not isinstance(other, BatchCreateMembersOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
