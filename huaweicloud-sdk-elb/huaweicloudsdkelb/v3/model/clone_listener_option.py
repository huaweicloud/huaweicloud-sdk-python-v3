# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloneListenerOption:

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
        'loadbalancer_id': 'str',
        'protocol_port': 'int',
        'port_ranges': 'list[PortRange]',
        'reuse_pool': 'bool',
        'subnet_mapping_list': 'list[SubnetMappingList]'
    }

    attribute_map = {
        'name': 'name',
        'loadbalancer_id': 'loadbalancer_id',
        'protocol_port': 'protocol_port',
        'port_ranges': 'port_ranges',
        'reuse_pool': 'reuse_pool',
        'subnet_mapping_list': 'subnet_mapping_list'
    }

    def __init__(self, name=None, loadbalancer_id=None, protocol_port=None, port_ranges=None, reuse_pool=None, subnet_mapping_list=None):
        r"""CloneListenerOption

        The model defined in huaweicloud sdk

        :param name: **参数解释**：新监听器的名称。 **约束限制**：不涉及 **取值范围**：[0-255]个字符，传入空字符串则取默认值。 **默认取值**：原监听器名称+ “-copy”。
        :type name: str
        :param loadbalancer_id: **参数解释**：新监听器所在的负载均衡器ID（UUID）。 **约束限制**： - 不支持复制到网关型负载均衡器。 - 目的负载均衡器类型需要支持源监听器协议。源监听器协议为HTTP、HTTPS，目的负载均衡器需要为应用型负载均衡器；源监听器协议为TCP、UDP、TLS，目的负载均衡器需要为网络型负载均衡器。 - 只支持共享型负载均衡器复制到共享型负载均衡器，独享型负载均衡器复制到独享型负载均衡器。 - 源监听器的负载均衡器启用IP类型后端转发，目的负载均衡器也需要启动IP类型后端转发功能。 - 源监听器协议为TLS，目的负载均衡器需要支持创建TLS协议监听器。 **取值范围**：标准的UUID格式，长度为36个字符。 **默认取值**：不涉及
        :type loadbalancer_id: str
        :param protocol_port: **参数解释**：新监听器的监听端口。 **约束限制**： - 不能与目的负载均衡器下已有监听器监听端口重复。 - 0表示开启监听端口范围的能力，此时port_ranges为必填字段。 - 共享型负载均衡器上的HTTP和TERMINATED_HTTPS监听器不支持设置21端口。 **取值范围**：0-65535 **默认取值**：不涉及
        :type protocol_port: int
        :param port_ranges: **参数解释**：端口监听范围（闭区间)，最多指定10个端口组，每个组范围不可有重叠部分。 **约束限制**： - 仅当protocol_port为0或未传入protocol_port时可以传入该字段。 - 仅TCP, UDP，TLS监听器支持该字段。 - 不能与目的负载均衡器下已有端口冲突
        :type port_ranges: list[:class:`huaweicloudsdkelb.v3.PortRange`]
        :param reuse_pool: **参数解释**：新监听器是否复用或复制源监听器的后端服务器组和后端服务器的标识。 - 复用：目的负载均衡器将会直接使用源负载均衡器的后端服务器组。 - 复制：系统将会根据原有配置创建新的后端服务器组，然后将其关联到目的负载均衡器使用。 **约束限制**： - 配置为true时，需要开启后端服务器组多挂实例功能。 - 只在独享型场景复制、同VPC场景可配。 **取值范围**： - true：复用源监听器的后端服务器组。 - false：复制源监听器的后端服务器组。 **默认取值**：false
        :type reuse_pool: bool
        :param subnet_mapping_list: **参数解释**：源监听器下后端服务器子网信息和新监听器下后端服务器子网信息一一对应关系。 **约束限制**： - 将监听器复制到不同VPC下的负载均衡器时，该字段必填。复制到同一个VPC下的负载均衡器时不填。 - 若源监听器所在负载均衡器已开启ip_target_enable（该功能默认不开启），则不允许跨VPC复制，即该字段不允许填。 - 每一组subnet_cidr_id都需要是新监听器下后端服务器的VPC子网ID，每一组dst_subnet_cidr_id都需要为源监听器下后端服务器的的VPC子网ID，不允许少填多填、或重复对应关系。 - 每一组的subnet_cidr_id和dst_subnet_cidr_id的两个子网必须存在且网段相同。
        :type subnet_mapping_list: list[:class:`huaweicloudsdkelb.v3.SubnetMappingList`]
        """
        
        

        self._name = None
        self._loadbalancer_id = None
        self._protocol_port = None
        self._port_ranges = None
        self._reuse_pool = None
        self._subnet_mapping_list = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.loadbalancer_id = loadbalancer_id
        if protocol_port is not None:
            self.protocol_port = protocol_port
        if port_ranges is not None:
            self.port_ranges = port_ranges
        if reuse_pool is not None:
            self.reuse_pool = reuse_pool
        if subnet_mapping_list is not None:
            self.subnet_mapping_list = subnet_mapping_list

    @property
    def name(self):
        r"""Gets the name of this CloneListenerOption.

        **参数解释**：新监听器的名称。 **约束限制**：不涉及 **取值范围**：[0-255]个字符，传入空字符串则取默认值。 **默认取值**：原监听器名称+ “-copy”。

        :return: The name of this CloneListenerOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CloneListenerOption.

        **参数解释**：新监听器的名称。 **约束限制**：不涉及 **取值范围**：[0-255]个字符，传入空字符串则取默认值。 **默认取值**：原监听器名称+ “-copy”。

        :param name: The name of this CloneListenerOption.
        :type name: str
        """
        self._name = name

    @property
    def loadbalancer_id(self):
        r"""Gets the loadbalancer_id of this CloneListenerOption.

        **参数解释**：新监听器所在的负载均衡器ID（UUID）。 **约束限制**： - 不支持复制到网关型负载均衡器。 - 目的负载均衡器类型需要支持源监听器协议。源监听器协议为HTTP、HTTPS，目的负载均衡器需要为应用型负载均衡器；源监听器协议为TCP、UDP、TLS，目的负载均衡器需要为网络型负载均衡器。 - 只支持共享型负载均衡器复制到共享型负载均衡器，独享型负载均衡器复制到独享型负载均衡器。 - 源监听器的负载均衡器启用IP类型后端转发，目的负载均衡器也需要启动IP类型后端转发功能。 - 源监听器协议为TLS，目的负载均衡器需要支持创建TLS协议监听器。 **取值范围**：标准的UUID格式，长度为36个字符。 **默认取值**：不涉及

        :return: The loadbalancer_id of this CloneListenerOption.
        :rtype: str
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        r"""Sets the loadbalancer_id of this CloneListenerOption.

        **参数解释**：新监听器所在的负载均衡器ID（UUID）。 **约束限制**： - 不支持复制到网关型负载均衡器。 - 目的负载均衡器类型需要支持源监听器协议。源监听器协议为HTTP、HTTPS，目的负载均衡器需要为应用型负载均衡器；源监听器协议为TCP、UDP、TLS，目的负载均衡器需要为网络型负载均衡器。 - 只支持共享型负载均衡器复制到共享型负载均衡器，独享型负载均衡器复制到独享型负载均衡器。 - 源监听器的负载均衡器启用IP类型后端转发，目的负载均衡器也需要启动IP类型后端转发功能。 - 源监听器协议为TLS，目的负载均衡器需要支持创建TLS协议监听器。 **取值范围**：标准的UUID格式，长度为36个字符。 **默认取值**：不涉及

        :param loadbalancer_id: The loadbalancer_id of this CloneListenerOption.
        :type loadbalancer_id: str
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def protocol_port(self):
        r"""Gets the protocol_port of this CloneListenerOption.

        **参数解释**：新监听器的监听端口。 **约束限制**： - 不能与目的负载均衡器下已有监听器监听端口重复。 - 0表示开启监听端口范围的能力，此时port_ranges为必填字段。 - 共享型负载均衡器上的HTTP和TERMINATED_HTTPS监听器不支持设置21端口。 **取值范围**：0-65535 **默认取值**：不涉及

        :return: The protocol_port of this CloneListenerOption.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        r"""Sets the protocol_port of this CloneListenerOption.

        **参数解释**：新监听器的监听端口。 **约束限制**： - 不能与目的负载均衡器下已有监听器监听端口重复。 - 0表示开启监听端口范围的能力，此时port_ranges为必填字段。 - 共享型负载均衡器上的HTTP和TERMINATED_HTTPS监听器不支持设置21端口。 **取值范围**：0-65535 **默认取值**：不涉及

        :param protocol_port: The protocol_port of this CloneListenerOption.
        :type protocol_port: int
        """
        self._protocol_port = protocol_port

    @property
    def port_ranges(self):
        r"""Gets the port_ranges of this CloneListenerOption.

        **参数解释**：端口监听范围（闭区间)，最多指定10个端口组，每个组范围不可有重叠部分。 **约束限制**： - 仅当protocol_port为0或未传入protocol_port时可以传入该字段。 - 仅TCP, UDP，TLS监听器支持该字段。 - 不能与目的负载均衡器下已有端口冲突

        :return: The port_ranges of this CloneListenerOption.
        :rtype: list[:class:`huaweicloudsdkelb.v3.PortRange`]
        """
        return self._port_ranges

    @port_ranges.setter
    def port_ranges(self, port_ranges):
        r"""Sets the port_ranges of this CloneListenerOption.

        **参数解释**：端口监听范围（闭区间)，最多指定10个端口组，每个组范围不可有重叠部分。 **约束限制**： - 仅当protocol_port为0或未传入protocol_port时可以传入该字段。 - 仅TCP, UDP，TLS监听器支持该字段。 - 不能与目的负载均衡器下已有端口冲突

        :param port_ranges: The port_ranges of this CloneListenerOption.
        :type port_ranges: list[:class:`huaweicloudsdkelb.v3.PortRange`]
        """
        self._port_ranges = port_ranges

    @property
    def reuse_pool(self):
        r"""Gets the reuse_pool of this CloneListenerOption.

        **参数解释**：新监听器是否复用或复制源监听器的后端服务器组和后端服务器的标识。 - 复用：目的负载均衡器将会直接使用源负载均衡器的后端服务器组。 - 复制：系统将会根据原有配置创建新的后端服务器组，然后将其关联到目的负载均衡器使用。 **约束限制**： - 配置为true时，需要开启后端服务器组多挂实例功能。 - 只在独享型场景复制、同VPC场景可配。 **取值范围**： - true：复用源监听器的后端服务器组。 - false：复制源监听器的后端服务器组。 **默认取值**：false

        :return: The reuse_pool of this CloneListenerOption.
        :rtype: bool
        """
        return self._reuse_pool

    @reuse_pool.setter
    def reuse_pool(self, reuse_pool):
        r"""Sets the reuse_pool of this CloneListenerOption.

        **参数解释**：新监听器是否复用或复制源监听器的后端服务器组和后端服务器的标识。 - 复用：目的负载均衡器将会直接使用源负载均衡器的后端服务器组。 - 复制：系统将会根据原有配置创建新的后端服务器组，然后将其关联到目的负载均衡器使用。 **约束限制**： - 配置为true时，需要开启后端服务器组多挂实例功能。 - 只在独享型场景复制、同VPC场景可配。 **取值范围**： - true：复用源监听器的后端服务器组。 - false：复制源监听器的后端服务器组。 **默认取值**：false

        :param reuse_pool: The reuse_pool of this CloneListenerOption.
        :type reuse_pool: bool
        """
        self._reuse_pool = reuse_pool

    @property
    def subnet_mapping_list(self):
        r"""Gets the subnet_mapping_list of this CloneListenerOption.

        **参数解释**：源监听器下后端服务器子网信息和新监听器下后端服务器子网信息一一对应关系。 **约束限制**： - 将监听器复制到不同VPC下的负载均衡器时，该字段必填。复制到同一个VPC下的负载均衡器时不填。 - 若源监听器所在负载均衡器已开启ip_target_enable（该功能默认不开启），则不允许跨VPC复制，即该字段不允许填。 - 每一组subnet_cidr_id都需要是新监听器下后端服务器的VPC子网ID，每一组dst_subnet_cidr_id都需要为源监听器下后端服务器的的VPC子网ID，不允许少填多填、或重复对应关系。 - 每一组的subnet_cidr_id和dst_subnet_cidr_id的两个子网必须存在且网段相同。

        :return: The subnet_mapping_list of this CloneListenerOption.
        :rtype: list[:class:`huaweicloudsdkelb.v3.SubnetMappingList`]
        """
        return self._subnet_mapping_list

    @subnet_mapping_list.setter
    def subnet_mapping_list(self, subnet_mapping_list):
        r"""Sets the subnet_mapping_list of this CloneListenerOption.

        **参数解释**：源监听器下后端服务器子网信息和新监听器下后端服务器子网信息一一对应关系。 **约束限制**： - 将监听器复制到不同VPC下的负载均衡器时，该字段必填。复制到同一个VPC下的负载均衡器时不填。 - 若源监听器所在负载均衡器已开启ip_target_enable（该功能默认不开启），则不允许跨VPC复制，即该字段不允许填。 - 每一组subnet_cidr_id都需要是新监听器下后端服务器的VPC子网ID，每一组dst_subnet_cidr_id都需要为源监听器下后端服务器的的VPC子网ID，不允许少填多填、或重复对应关系。 - 每一组的subnet_cidr_id和dst_subnet_cidr_id的两个子网必须存在且网段相同。

        :param subnet_mapping_list: The subnet_mapping_list of this CloneListenerOption.
        :type subnet_mapping_list: list[:class:`huaweicloudsdkelb.v3.SubnetMappingList`]
        """
        self._subnet_mapping_list = subnet_mapping_list

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
        if not isinstance(other, CloneListenerOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
