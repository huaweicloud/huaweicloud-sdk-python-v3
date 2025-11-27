# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPrivateDnatsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'page_reverse': 'bool',
        'id': 'list[str]',
        'enterprise_project_id': 'list[str]',
        'description': 'list[str]',
        'gateway_id': 'list[str]',
        'transit_ip_id': 'list[str]',
        'network_interface_id': 'list[str]',
        'type': 'list[str]',
        'private_ip_address': 'list[str]',
        'protocol': 'list[str]',
        'internal_service_port': 'list[str]',
        'transit_service_port': 'list[str]',
        'transit_ip_address': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'id': 'id',
        'enterprise_project_id': 'enterprise_project_id',
        'description': 'description',
        'gateway_id': 'gateway_id',
        'transit_ip_id': 'transit_ip_id',
        'network_interface_id': 'network_interface_id',
        'type': 'type',
        'private_ip_address': 'private_ip_address',
        'protocol': 'protocol',
        'internal_service_port': 'internal_service_port',
        'transit_service_port': 'transit_service_port',
        'transit_ip_address': 'transit_ip_address'
    }

    def __init__(self, limit=None, marker=None, page_reverse=None, id=None, enterprise_project_id=None, description=None, gateway_id=None, transit_ip_id=None, network_interface_id=None, type=None, private_ip_address=None, protocol=None, internal_service_port=None, transit_service_port=None, transit_ip_address=None):
        r"""ListPrivateDnatsRequest

        The model defined in huaweicloud sdk

        :param limit: 功能说明：每页返回的个数。 取值范围：1~2000。 默认值：2000。
        :type limit: int
        :param marker: 功能说明：分页查询起始的资源ID，为空时查询第一页。 值从上一次查询的PageInfo中的next_marker或者previous_marker中获取。
        :type marker: str
        :param page_reverse: 是否查询前一页。
        :type page_reverse: bool
        :param id: DNAT规则的ID。
        :type id: list[str]
        :param enterprise_project_id: 企业项目ID。创建DNAT规则时，关联的企业项目ID。
        :type enterprise_project_id: list[str]
        :param description: DNAT规则的描述。长度范围小于等于255个字符，不能包含“&lt;”和“&gt;”。
        :type description: list[str]
        :param gateway_id: 私网NAT网关实例的ID。
        :type gateway_id: list[str]
        :param transit_ip_id: 中转IP的ID。
        :type transit_ip_id: list[str]
        :param network_interface_id: 计算实例、ELBV2、ELBV3、VIP等资源的端口ID。
        :type network_interface_id: list[str]
        :param type: DNAT规则后端的类型。 取值：     COMPUTE：后端为计算实例。     VIP：后端为VIP的实例。     ELB：后端为ELBv2的实例。     ELBv3：后端为ELBv3的实例。     CUSTOMIZE：后端为自定义IP。
        :type type: list[str]
        :param private_ip_address: 后端资源（计算实例、ELBV2、ELBV3、VIP等）的私网IP地址。
        :type private_ip_address: list[str]
        :param protocol: DNAT规则协议类型， 目前支持TCP/tcp/Tcp/tCp/tcP/TCp/tCP/TcP、 UDP/udp/Udp/uDp/udP/UDp/uDP/UdP、 ANY/any/Any/aNy/anY/ANy/aNY/AnY。 分别对应协议号6、17、0。
        :type protocol: list[str]
        :param internal_service_port: 后端实例的端口号（计算实例、ELBV2、ELBV3、VIP等)。
        :type internal_service_port: list[str]
        :param transit_service_port: 中转IP的端口号。
        :type transit_service_port: list[str]
        :param transit_ip_address: 中转IP的地址。
        :type transit_ip_address: list[str]
        """
        
        

        self._limit = None
        self._marker = None
        self._page_reverse = None
        self._id = None
        self._enterprise_project_id = None
        self._description = None
        self._gateway_id = None
        self._transit_ip_id = None
        self._network_interface_id = None
        self._type = None
        self._private_ip_address = None
        self._protocol = None
        self._internal_service_port = None
        self._transit_service_port = None
        self._transit_ip_address = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if id is not None:
            self.id = id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if description is not None:
            self.description = description
        if gateway_id is not None:
            self.gateway_id = gateway_id
        if transit_ip_id is not None:
            self.transit_ip_id = transit_ip_id
        if network_interface_id is not None:
            self.network_interface_id = network_interface_id
        if type is not None:
            self.type = type
        if private_ip_address is not None:
            self.private_ip_address = private_ip_address
        if protocol is not None:
            self.protocol = protocol
        if internal_service_port is not None:
            self.internal_service_port = internal_service_port
        if transit_service_port is not None:
            self.transit_service_port = transit_service_port
        if transit_ip_address is not None:
            self.transit_ip_address = transit_ip_address

    @property
    def limit(self):
        r"""Gets the limit of this ListPrivateDnatsRequest.

        功能说明：每页返回的个数。 取值范围：1~2000。 默认值：2000。

        :return: The limit of this ListPrivateDnatsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPrivateDnatsRequest.

        功能说明：每页返回的个数。 取值范围：1~2000。 默认值：2000。

        :param limit: The limit of this ListPrivateDnatsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListPrivateDnatsRequest.

        功能说明：分页查询起始的资源ID，为空时查询第一页。 值从上一次查询的PageInfo中的next_marker或者previous_marker中获取。

        :return: The marker of this ListPrivateDnatsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListPrivateDnatsRequest.

        功能说明：分页查询起始的资源ID，为空时查询第一页。 值从上一次查询的PageInfo中的next_marker或者previous_marker中获取。

        :param marker: The marker of this ListPrivateDnatsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        r"""Gets the page_reverse of this ListPrivateDnatsRequest.

        是否查询前一页。

        :return: The page_reverse of this ListPrivateDnatsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        r"""Sets the page_reverse of this ListPrivateDnatsRequest.

        是否查询前一页。

        :param page_reverse: The page_reverse of this ListPrivateDnatsRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        r"""Gets the id of this ListPrivateDnatsRequest.

        DNAT规则的ID。

        :return: The id of this ListPrivateDnatsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListPrivateDnatsRequest.

        DNAT规则的ID。

        :param id: The id of this ListPrivateDnatsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListPrivateDnatsRequest.

        企业项目ID。创建DNAT规则时，关联的企业项目ID。

        :return: The enterprise_project_id of this ListPrivateDnatsRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListPrivateDnatsRequest.

        企业项目ID。创建DNAT规则时，关联的企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ListPrivateDnatsRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def description(self):
        r"""Gets the description of this ListPrivateDnatsRequest.

        DNAT规则的描述。长度范围小于等于255个字符，不能包含“<”和“>”。

        :return: The description of this ListPrivateDnatsRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListPrivateDnatsRequest.

        DNAT规则的描述。长度范围小于等于255个字符，不能包含“<”和“>”。

        :param description: The description of this ListPrivateDnatsRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def gateway_id(self):
        r"""Gets the gateway_id of this ListPrivateDnatsRequest.

        私网NAT网关实例的ID。

        :return: The gateway_id of this ListPrivateDnatsRequest.
        :rtype: list[str]
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        r"""Sets the gateway_id of this ListPrivateDnatsRequest.

        私网NAT网关实例的ID。

        :param gateway_id: The gateway_id of this ListPrivateDnatsRequest.
        :type gateway_id: list[str]
        """
        self._gateway_id = gateway_id

    @property
    def transit_ip_id(self):
        r"""Gets the transit_ip_id of this ListPrivateDnatsRequest.

        中转IP的ID。

        :return: The transit_ip_id of this ListPrivateDnatsRequest.
        :rtype: list[str]
        """
        return self._transit_ip_id

    @transit_ip_id.setter
    def transit_ip_id(self, transit_ip_id):
        r"""Sets the transit_ip_id of this ListPrivateDnatsRequest.

        中转IP的ID。

        :param transit_ip_id: The transit_ip_id of this ListPrivateDnatsRequest.
        :type transit_ip_id: list[str]
        """
        self._transit_ip_id = transit_ip_id

    @property
    def network_interface_id(self):
        r"""Gets the network_interface_id of this ListPrivateDnatsRequest.

        计算实例、ELBV2、ELBV3、VIP等资源的端口ID。

        :return: The network_interface_id of this ListPrivateDnatsRequest.
        :rtype: list[str]
        """
        return self._network_interface_id

    @network_interface_id.setter
    def network_interface_id(self, network_interface_id):
        r"""Sets the network_interface_id of this ListPrivateDnatsRequest.

        计算实例、ELBV2、ELBV3、VIP等资源的端口ID。

        :param network_interface_id: The network_interface_id of this ListPrivateDnatsRequest.
        :type network_interface_id: list[str]
        """
        self._network_interface_id = network_interface_id

    @property
    def type(self):
        r"""Gets the type of this ListPrivateDnatsRequest.

        DNAT规则后端的类型。 取值：     COMPUTE：后端为计算实例。     VIP：后端为VIP的实例。     ELB：后端为ELBv2的实例。     ELBv3：后端为ELBv3的实例。     CUSTOMIZE：后端为自定义IP。

        :return: The type of this ListPrivateDnatsRequest.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListPrivateDnatsRequest.

        DNAT规则后端的类型。 取值：     COMPUTE：后端为计算实例。     VIP：后端为VIP的实例。     ELB：后端为ELBv2的实例。     ELBv3：后端为ELBv3的实例。     CUSTOMIZE：后端为自定义IP。

        :param type: The type of this ListPrivateDnatsRequest.
        :type type: list[str]
        """
        self._type = type

    @property
    def private_ip_address(self):
        r"""Gets the private_ip_address of this ListPrivateDnatsRequest.

        后端资源（计算实例、ELBV2、ELBV3、VIP等）的私网IP地址。

        :return: The private_ip_address of this ListPrivateDnatsRequest.
        :rtype: list[str]
        """
        return self._private_ip_address

    @private_ip_address.setter
    def private_ip_address(self, private_ip_address):
        r"""Sets the private_ip_address of this ListPrivateDnatsRequest.

        后端资源（计算实例、ELBV2、ELBV3、VIP等）的私网IP地址。

        :param private_ip_address: The private_ip_address of this ListPrivateDnatsRequest.
        :type private_ip_address: list[str]
        """
        self._private_ip_address = private_ip_address

    @property
    def protocol(self):
        r"""Gets the protocol of this ListPrivateDnatsRequest.

        DNAT规则协议类型， 目前支持TCP/tcp/Tcp/tCp/tcP/TCp/tCP/TcP、 UDP/udp/Udp/uDp/udP/UDp/uDP/UdP、 ANY/any/Any/aNy/anY/ANy/aNY/AnY。 分别对应协议号6、17、0。

        :return: The protocol of this ListPrivateDnatsRequest.
        :rtype: list[str]
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this ListPrivateDnatsRequest.

        DNAT规则协议类型， 目前支持TCP/tcp/Tcp/tCp/tcP/TCp/tCP/TcP、 UDP/udp/Udp/uDp/udP/UDp/uDP/UdP、 ANY/any/Any/aNy/anY/ANy/aNY/AnY。 分别对应协议号6、17、0。

        :param protocol: The protocol of this ListPrivateDnatsRequest.
        :type protocol: list[str]
        """
        self._protocol = protocol

    @property
    def internal_service_port(self):
        r"""Gets the internal_service_port of this ListPrivateDnatsRequest.

        后端实例的端口号（计算实例、ELBV2、ELBV3、VIP等)。

        :return: The internal_service_port of this ListPrivateDnatsRequest.
        :rtype: list[str]
        """
        return self._internal_service_port

    @internal_service_port.setter
    def internal_service_port(self, internal_service_port):
        r"""Sets the internal_service_port of this ListPrivateDnatsRequest.

        后端实例的端口号（计算实例、ELBV2、ELBV3、VIP等)。

        :param internal_service_port: The internal_service_port of this ListPrivateDnatsRequest.
        :type internal_service_port: list[str]
        """
        self._internal_service_port = internal_service_port

    @property
    def transit_service_port(self):
        r"""Gets the transit_service_port of this ListPrivateDnatsRequest.

        中转IP的端口号。

        :return: The transit_service_port of this ListPrivateDnatsRequest.
        :rtype: list[str]
        """
        return self._transit_service_port

    @transit_service_port.setter
    def transit_service_port(self, transit_service_port):
        r"""Sets the transit_service_port of this ListPrivateDnatsRequest.

        中转IP的端口号。

        :param transit_service_port: The transit_service_port of this ListPrivateDnatsRequest.
        :type transit_service_port: list[str]
        """
        self._transit_service_port = transit_service_port

    @property
    def transit_ip_address(self):
        r"""Gets the transit_ip_address of this ListPrivateDnatsRequest.

        中转IP的地址。

        :return: The transit_ip_address of this ListPrivateDnatsRequest.
        :rtype: list[str]
        """
        return self._transit_ip_address

    @transit_ip_address.setter
    def transit_ip_address(self, transit_ip_address):
        r"""Sets the transit_ip_address of this ListPrivateDnatsRequest.

        中转IP的地址。

        :param transit_ip_address: The transit_ip_address of this ListPrivateDnatsRequest.
        :type transit_ip_address: list[str]
        """
        self._transit_ip_address = transit_ip_address

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
        if not isinstance(other, ListPrivateDnatsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
