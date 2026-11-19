# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubNetworkInterfacesRequest:

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
        'id': 'list[str]',
        'virsubnet_id': 'list[str]',
        'private_ip_address': 'list[str]',
        'mac_address': 'list[str]',
        'vpc_id': 'list[str]',
        'description': 'list[str]',
        'parent_id': 'list[str]',
        'enable_eip': 'bool',
        'scope': 'str',
        'security_groups': 'list[str]',
        'enterprise_project_id': 'str',
        'parent_device_id': 'list[str]',
        'vlan_id': 'list[int]',
        'state': 'list[str]',
        'ipv6_ip_address': 'list[str]',
        'instance_id': 'list[str]',
        'instance_type': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'virsubnet_id': 'virsubnet_id',
        'private_ip_address': 'private_ip_address',
        'mac_address': 'mac_address',
        'vpc_id': 'vpc_id',
        'description': 'description',
        'parent_id': 'parent_id',
        'enable_eip': 'enable_eip',
        'scope': 'scope',
        'security_groups': 'security_groups',
        'enterprise_project_id': 'enterprise_project_id',
        'parent_device_id': 'parent_device_id',
        'vlan_id': 'vlan_id',
        'state': 'state',
        'ipv6_ip_address': 'ipv6_ip_address',
        'instance_id': 'instance_id',
        'instance_type': 'instance_type'
    }

    def __init__(self, limit=None, marker=None, id=None, virsubnet_id=None, private_ip_address=None, mac_address=None, vpc_id=None, description=None, parent_id=None, enable_eip=None, scope=None, security_groups=None, enterprise_project_id=None, parent_device_id=None, vlan_id=None, state=None, ipv6_ip_address=None, instance_id=None, instance_type=None):
        r"""ListSubNetworkInterfacesRequest

        The model defined in huaweicloud sdk

        :param limit: 功能说明：每页返回的个数 取值范围：0-2000
        :type limit: int
        :param marker: 分页查询起始的资源ID，为空时查询第一页
        :type marker: str
        :param id: 功能说明：辅助弹性网卡ID，支持多ID过滤 使用场景：查询需要的多个辅助弹性网卡信息
        :type id: list[str]
        :param virsubnet_id: 功能说明：辅助弹性网卡所属虚拟子网的ID，支持多个ID过滤 使用场景：过滤需要的单个或者多个虚拟子网下的辅助弹性网卡
        :type virsubnet_id: list[str]
        :param private_ip_address: 功能说明：辅助弹性网卡的私有IPv4地址，支持多个地址同时过滤 使用场景：通过单个或者多个ip地址过滤查询辅助弹性网卡
        :type private_ip_address: list[str]
        :param mac_address: 功能说明：辅助弹性网卡的mac地址，支持多个同时过滤 使用场景：使用mac地址精确过滤辅助弹性网卡
        :type mac_address: list[str]
        :param vpc_id: 功能说明：辅助弹性网卡所属的VPC_ID，支持多ID过滤 使用场景：过滤单个或多个VPC下的辅助弹性网卡信息
        :type vpc_id: list[str]
        :param description: 功能说明：辅助弹性网卡的描述信息，支持多个同时过滤 使用场景：通过描述信息过滤辅助弹性网卡
        :type description: list[str]
        :param parent_id: 功能说明：辅助弹性网卡的宿主网卡的ID，支持多ID过滤 使用场景：过滤单个或多个宿主网卡下存在的辅助弹性网卡
        :type parent_id: list[str]
        :param enable_eip: **参数解释**： 辅助弹性网卡是否关联EIP，可以通过此字段过滤辅助弹性网卡，不支持传入多个值进行过滤。 **取值范围**：   - true：辅助弹性网卡已关联EIP   - false：辅助弹性网卡未关联EIP **约束限制**： 不涉及。 **默认取值**： 不涉及。
        :type enable_eip: bool
        :param scope: **参数解释**： 辅助弹性网卡所在站点的公网出口信息，可以通过此字段过滤辅助弹性网卡。 **取值范围**： 不涉及。 **约束限制**： 不涉及。 **默认取值**： 不涉及。
        :type scope: str
        :param security_groups: **参数解释**： 辅助弹性网卡关联的安全组ID，可以通过此字段过滤辅助弹性网卡，支持传入多个安全组ID过滤。[获取方式请参见[查询安全组列表](vpc_apiv3_0011.xml)。](tag:hws,hws_hk,hws_test) **取值范围**： 不涉及。 **约束限制**： 不涉及。 **默认取值**： 不涉及。
        :type security_groups: list[str]
        :param enterprise_project_id: **参数解释**： 辅助弹性网卡所属企业项目的ID。可以使用该字段过滤某个企业项目下的辅助弹性网卡。 **取值范围**： - 最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。 - 若需要查询当前用户所有企业项目绑定的辅助弹性网卡，请传参all_granted_eps。 **约束限制**： 不涉及。 **默认取值**： 不涉及。
        :type enterprise_project_id: str
        :param parent_device_id: **参数解释**： 辅助弹性网卡的宿主网卡所属的设备ID，可以通过此字段过滤辅助弹性网卡，支持传入多个ID过滤。 **取值范围**： 不涉及。 **约束限制**： 不涉及。 **默认取值**： 不涉及。
        :type parent_device_id: list[str]
        :param vlan_id: **参数解释**： 辅助弹性网卡的VLAN ID，可以通过此字段过滤辅助弹性网卡，支持传入多个VLAN ID过滤。 **取值范围**： 1-4094。 **约束限制**： 不涉及。 **默认取值**： 不涉及。
        :type vlan_id: list[int]
        :param state: **参数解释**： 辅助弹性网卡的状态，可以通过此字段过滤辅助弹性网卡，支持传入多个状态过滤。 **取值范围**： NORMAL：过滤出已挂载在弹性网卡上的辅助弹性网卡 UNBOUND：过滤出未挂载在弹性网卡上的辅助弹性网卡 **约束限制**： 不涉及。 **默认取值**： 不涉及。
        :type state: list[str]
        :param ipv6_ip_address: **参数解释**： 辅助弹性网卡的IPv6地址，可以通过此字段过滤辅助弹性网卡，支持传入多个IP地址过滤。 **取值范围**： 不涉及。 **约束限制**： 不涉及。 **默认取值**： 不涉及。
        :type ipv6_ip_address: list[str]
        :param instance_id: **参数解释**： 辅助弹性网卡所属云服务实例的ID，例如RDS实例的ID，可以通过此字段过滤辅助弹性网卡，支持传入多个ID过滤。 **取值范围**： 不涉及。 **约束限制**： 不涉及。 **默认取值**： 不涉及。
        :type instance_id: list[str]
        :param instance_type: **参数解释**： 辅助弹性网卡所属云服务实例的类型，例如“RDS”，可以通过此字段过滤辅助弹性网卡，支持传入多个实例类型过滤。 **取值范围**： 不涉及。 **约束限制**： 不涉及。 **默认取值**： 不涉及。
        :type instance_type: list[str]
        """
        
        

        self._limit = None
        self._marker = None
        self._id = None
        self._virsubnet_id = None
        self._private_ip_address = None
        self._mac_address = None
        self._vpc_id = None
        self._description = None
        self._parent_id = None
        self._enable_eip = None
        self._scope = None
        self._security_groups = None
        self._enterprise_project_id = None
        self._parent_device_id = None
        self._vlan_id = None
        self._state = None
        self._ipv6_ip_address = None
        self._instance_id = None
        self._instance_type = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if virsubnet_id is not None:
            self.virsubnet_id = virsubnet_id
        if private_ip_address is not None:
            self.private_ip_address = private_ip_address
        if mac_address is not None:
            self.mac_address = mac_address
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if description is not None:
            self.description = description
        if parent_id is not None:
            self.parent_id = parent_id
        if enable_eip is not None:
            self.enable_eip = enable_eip
        if scope is not None:
            self.scope = scope
        if security_groups is not None:
            self.security_groups = security_groups
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if parent_device_id is not None:
            self.parent_device_id = parent_device_id
        if vlan_id is not None:
            self.vlan_id = vlan_id
        if state is not None:
            self.state = state
        if ipv6_ip_address is not None:
            self.ipv6_ip_address = ipv6_ip_address
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_type is not None:
            self.instance_type = instance_type

    @property
    def limit(self):
        r"""Gets the limit of this ListSubNetworkInterfacesRequest.

        功能说明：每页返回的个数 取值范围：0-2000

        :return: The limit of this ListSubNetworkInterfacesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSubNetworkInterfacesRequest.

        功能说明：每页返回的个数 取值范围：0-2000

        :param limit: The limit of this ListSubNetworkInterfacesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListSubNetworkInterfacesRequest.

        分页查询起始的资源ID，为空时查询第一页

        :return: The marker of this ListSubNetworkInterfacesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListSubNetworkInterfacesRequest.

        分页查询起始的资源ID，为空时查询第一页

        :param marker: The marker of this ListSubNetworkInterfacesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def id(self):
        r"""Gets the id of this ListSubNetworkInterfacesRequest.

        功能说明：辅助弹性网卡ID，支持多ID过滤 使用场景：查询需要的多个辅助弹性网卡信息

        :return: The id of this ListSubNetworkInterfacesRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListSubNetworkInterfacesRequest.

        功能说明：辅助弹性网卡ID，支持多ID过滤 使用场景：查询需要的多个辅助弹性网卡信息

        :param id: The id of this ListSubNetworkInterfacesRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def virsubnet_id(self):
        r"""Gets the virsubnet_id of this ListSubNetworkInterfacesRequest.

        功能说明：辅助弹性网卡所属虚拟子网的ID，支持多个ID过滤 使用场景：过滤需要的单个或者多个虚拟子网下的辅助弹性网卡

        :return: The virsubnet_id of this ListSubNetworkInterfacesRequest.
        :rtype: list[str]
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        r"""Sets the virsubnet_id of this ListSubNetworkInterfacesRequest.

        功能说明：辅助弹性网卡所属虚拟子网的ID，支持多个ID过滤 使用场景：过滤需要的单个或者多个虚拟子网下的辅助弹性网卡

        :param virsubnet_id: The virsubnet_id of this ListSubNetworkInterfacesRequest.
        :type virsubnet_id: list[str]
        """
        self._virsubnet_id = virsubnet_id

    @property
    def private_ip_address(self):
        r"""Gets the private_ip_address of this ListSubNetworkInterfacesRequest.

        功能说明：辅助弹性网卡的私有IPv4地址，支持多个地址同时过滤 使用场景：通过单个或者多个ip地址过滤查询辅助弹性网卡

        :return: The private_ip_address of this ListSubNetworkInterfacesRequest.
        :rtype: list[str]
        """
        return self._private_ip_address

    @private_ip_address.setter
    def private_ip_address(self, private_ip_address):
        r"""Sets the private_ip_address of this ListSubNetworkInterfacesRequest.

        功能说明：辅助弹性网卡的私有IPv4地址，支持多个地址同时过滤 使用场景：通过单个或者多个ip地址过滤查询辅助弹性网卡

        :param private_ip_address: The private_ip_address of this ListSubNetworkInterfacesRequest.
        :type private_ip_address: list[str]
        """
        self._private_ip_address = private_ip_address

    @property
    def mac_address(self):
        r"""Gets the mac_address of this ListSubNetworkInterfacesRequest.

        功能说明：辅助弹性网卡的mac地址，支持多个同时过滤 使用场景：使用mac地址精确过滤辅助弹性网卡

        :return: The mac_address of this ListSubNetworkInterfacesRequest.
        :rtype: list[str]
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        r"""Sets the mac_address of this ListSubNetworkInterfacesRequest.

        功能说明：辅助弹性网卡的mac地址，支持多个同时过滤 使用场景：使用mac地址精确过滤辅助弹性网卡

        :param mac_address: The mac_address of this ListSubNetworkInterfacesRequest.
        :type mac_address: list[str]
        """
        self._mac_address = mac_address

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ListSubNetworkInterfacesRequest.

        功能说明：辅助弹性网卡所属的VPC_ID，支持多ID过滤 使用场景：过滤单个或多个VPC下的辅助弹性网卡信息

        :return: The vpc_id of this ListSubNetworkInterfacesRequest.
        :rtype: list[str]
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ListSubNetworkInterfacesRequest.

        功能说明：辅助弹性网卡所属的VPC_ID，支持多ID过滤 使用场景：过滤单个或多个VPC下的辅助弹性网卡信息

        :param vpc_id: The vpc_id of this ListSubNetworkInterfacesRequest.
        :type vpc_id: list[str]
        """
        self._vpc_id = vpc_id

    @property
    def description(self):
        r"""Gets the description of this ListSubNetworkInterfacesRequest.

        功能说明：辅助弹性网卡的描述信息，支持多个同时过滤 使用场景：通过描述信息过滤辅助弹性网卡

        :return: The description of this ListSubNetworkInterfacesRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListSubNetworkInterfacesRequest.

        功能说明：辅助弹性网卡的描述信息，支持多个同时过滤 使用场景：通过描述信息过滤辅助弹性网卡

        :param description: The description of this ListSubNetworkInterfacesRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def parent_id(self):
        r"""Gets the parent_id of this ListSubNetworkInterfacesRequest.

        功能说明：辅助弹性网卡的宿主网卡的ID，支持多ID过滤 使用场景：过滤单个或多个宿主网卡下存在的辅助弹性网卡

        :return: The parent_id of this ListSubNetworkInterfacesRequest.
        :rtype: list[str]
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this ListSubNetworkInterfacesRequest.

        功能说明：辅助弹性网卡的宿主网卡的ID，支持多ID过滤 使用场景：过滤单个或多个宿主网卡下存在的辅助弹性网卡

        :param parent_id: The parent_id of this ListSubNetworkInterfacesRequest.
        :type parent_id: list[str]
        """
        self._parent_id = parent_id

    @property
    def enable_eip(self):
        r"""Gets the enable_eip of this ListSubNetworkInterfacesRequest.

        **参数解释**： 辅助弹性网卡是否关联EIP，可以通过此字段过滤辅助弹性网卡，不支持传入多个值进行过滤。 **取值范围**：   - true：辅助弹性网卡已关联EIP   - false：辅助弹性网卡未关联EIP **约束限制**： 不涉及。 **默认取值**： 不涉及。

        :return: The enable_eip of this ListSubNetworkInterfacesRequest.
        :rtype: bool
        """
        return self._enable_eip

    @enable_eip.setter
    def enable_eip(self, enable_eip):
        r"""Sets the enable_eip of this ListSubNetworkInterfacesRequest.

        **参数解释**： 辅助弹性网卡是否关联EIP，可以通过此字段过滤辅助弹性网卡，不支持传入多个值进行过滤。 **取值范围**：   - true：辅助弹性网卡已关联EIP   - false：辅助弹性网卡未关联EIP **约束限制**： 不涉及。 **默认取值**： 不涉及。

        :param enable_eip: The enable_eip of this ListSubNetworkInterfacesRequest.
        :type enable_eip: bool
        """
        self._enable_eip = enable_eip

    @property
    def scope(self):
        r"""Gets the scope of this ListSubNetworkInterfacesRequest.

        **参数解释**： 辅助弹性网卡所在站点的公网出口信息，可以通过此字段过滤辅助弹性网卡。 **取值范围**： 不涉及。 **约束限制**： 不涉及。 **默认取值**： 不涉及。

        :return: The scope of this ListSubNetworkInterfacesRequest.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this ListSubNetworkInterfacesRequest.

        **参数解释**： 辅助弹性网卡所在站点的公网出口信息，可以通过此字段过滤辅助弹性网卡。 **取值范围**： 不涉及。 **约束限制**： 不涉及。 **默认取值**： 不涉及。

        :param scope: The scope of this ListSubNetworkInterfacesRequest.
        :type scope: str
        """
        self._scope = scope

    @property
    def security_groups(self):
        r"""Gets the security_groups of this ListSubNetworkInterfacesRequest.

        **参数解释**： 辅助弹性网卡关联的安全组ID，可以通过此字段过滤辅助弹性网卡，支持传入多个安全组ID过滤。[获取方式请参见[查询安全组列表](vpc_apiv3_0011.xml)。](tag:hws,hws_hk,hws_test) **取值范围**： 不涉及。 **约束限制**： 不涉及。 **默认取值**： 不涉及。

        :return: The security_groups of this ListSubNetworkInterfacesRequest.
        :rtype: list[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        r"""Sets the security_groups of this ListSubNetworkInterfacesRequest.

        **参数解释**： 辅助弹性网卡关联的安全组ID，可以通过此字段过滤辅助弹性网卡，支持传入多个安全组ID过滤。[获取方式请参见[查询安全组列表](vpc_apiv3_0011.xml)。](tag:hws,hws_hk,hws_test) **取值范围**： 不涉及。 **约束限制**： 不涉及。 **默认取值**： 不涉及。

        :param security_groups: The security_groups of this ListSubNetworkInterfacesRequest.
        :type security_groups: list[str]
        """
        self._security_groups = security_groups

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListSubNetworkInterfacesRequest.

        **参数解释**： 辅助弹性网卡所属企业项目的ID。可以使用该字段过滤某个企业项目下的辅助弹性网卡。 **取值范围**： - 最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。 - 若需要查询当前用户所有企业项目绑定的辅助弹性网卡，请传参all_granted_eps。 **约束限制**： 不涉及。 **默认取值**： 不涉及。

        :return: The enterprise_project_id of this ListSubNetworkInterfacesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListSubNetworkInterfacesRequest.

        **参数解释**： 辅助弹性网卡所属企业项目的ID。可以使用该字段过滤某个企业项目下的辅助弹性网卡。 **取值范围**： - 最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。 - 若需要查询当前用户所有企业项目绑定的辅助弹性网卡，请传参all_granted_eps。 **约束限制**： 不涉及。 **默认取值**： 不涉及。

        :param enterprise_project_id: The enterprise_project_id of this ListSubNetworkInterfacesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def parent_device_id(self):
        r"""Gets the parent_device_id of this ListSubNetworkInterfacesRequest.

        **参数解释**： 辅助弹性网卡的宿主网卡所属的设备ID，可以通过此字段过滤辅助弹性网卡，支持传入多个ID过滤。 **取值范围**： 不涉及。 **约束限制**： 不涉及。 **默认取值**： 不涉及。

        :return: The parent_device_id of this ListSubNetworkInterfacesRequest.
        :rtype: list[str]
        """
        return self._parent_device_id

    @parent_device_id.setter
    def parent_device_id(self, parent_device_id):
        r"""Sets the parent_device_id of this ListSubNetworkInterfacesRequest.

        **参数解释**： 辅助弹性网卡的宿主网卡所属的设备ID，可以通过此字段过滤辅助弹性网卡，支持传入多个ID过滤。 **取值范围**： 不涉及。 **约束限制**： 不涉及。 **默认取值**： 不涉及。

        :param parent_device_id: The parent_device_id of this ListSubNetworkInterfacesRequest.
        :type parent_device_id: list[str]
        """
        self._parent_device_id = parent_device_id

    @property
    def vlan_id(self):
        r"""Gets the vlan_id of this ListSubNetworkInterfacesRequest.

        **参数解释**： 辅助弹性网卡的VLAN ID，可以通过此字段过滤辅助弹性网卡，支持传入多个VLAN ID过滤。 **取值范围**： 1-4094。 **约束限制**： 不涉及。 **默认取值**： 不涉及。

        :return: The vlan_id of this ListSubNetworkInterfacesRequest.
        :rtype: list[int]
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        r"""Sets the vlan_id of this ListSubNetworkInterfacesRequest.

        **参数解释**： 辅助弹性网卡的VLAN ID，可以通过此字段过滤辅助弹性网卡，支持传入多个VLAN ID过滤。 **取值范围**： 1-4094。 **约束限制**： 不涉及。 **默认取值**： 不涉及。

        :param vlan_id: The vlan_id of this ListSubNetworkInterfacesRequest.
        :type vlan_id: list[int]
        """
        self._vlan_id = vlan_id

    @property
    def state(self):
        r"""Gets the state of this ListSubNetworkInterfacesRequest.

        **参数解释**： 辅助弹性网卡的状态，可以通过此字段过滤辅助弹性网卡，支持传入多个状态过滤。 **取值范围**： NORMAL：过滤出已挂载在弹性网卡上的辅助弹性网卡 UNBOUND：过滤出未挂载在弹性网卡上的辅助弹性网卡 **约束限制**： 不涉及。 **默认取值**： 不涉及。

        :return: The state of this ListSubNetworkInterfacesRequest.
        :rtype: list[str]
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListSubNetworkInterfacesRequest.

        **参数解释**： 辅助弹性网卡的状态，可以通过此字段过滤辅助弹性网卡，支持传入多个状态过滤。 **取值范围**： NORMAL：过滤出已挂载在弹性网卡上的辅助弹性网卡 UNBOUND：过滤出未挂载在弹性网卡上的辅助弹性网卡 **约束限制**： 不涉及。 **默认取值**： 不涉及。

        :param state: The state of this ListSubNetworkInterfacesRequest.
        :type state: list[str]
        """
        self._state = state

    @property
    def ipv6_ip_address(self):
        r"""Gets the ipv6_ip_address of this ListSubNetworkInterfacesRequest.

        **参数解释**： 辅助弹性网卡的IPv6地址，可以通过此字段过滤辅助弹性网卡，支持传入多个IP地址过滤。 **取值范围**： 不涉及。 **约束限制**： 不涉及。 **默认取值**： 不涉及。

        :return: The ipv6_ip_address of this ListSubNetworkInterfacesRequest.
        :rtype: list[str]
        """
        return self._ipv6_ip_address

    @ipv6_ip_address.setter
    def ipv6_ip_address(self, ipv6_ip_address):
        r"""Sets the ipv6_ip_address of this ListSubNetworkInterfacesRequest.

        **参数解释**： 辅助弹性网卡的IPv6地址，可以通过此字段过滤辅助弹性网卡，支持传入多个IP地址过滤。 **取值范围**： 不涉及。 **约束限制**： 不涉及。 **默认取值**： 不涉及。

        :param ipv6_ip_address: The ipv6_ip_address of this ListSubNetworkInterfacesRequest.
        :type ipv6_ip_address: list[str]
        """
        self._ipv6_ip_address = ipv6_ip_address

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListSubNetworkInterfacesRequest.

        **参数解释**： 辅助弹性网卡所属云服务实例的ID，例如RDS实例的ID，可以通过此字段过滤辅助弹性网卡，支持传入多个ID过滤。 **取值范围**： 不涉及。 **约束限制**： 不涉及。 **默认取值**： 不涉及。

        :return: The instance_id of this ListSubNetworkInterfacesRequest.
        :rtype: list[str]
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListSubNetworkInterfacesRequest.

        **参数解释**： 辅助弹性网卡所属云服务实例的ID，例如RDS实例的ID，可以通过此字段过滤辅助弹性网卡，支持传入多个ID过滤。 **取值范围**： 不涉及。 **约束限制**： 不涉及。 **默认取值**： 不涉及。

        :param instance_id: The instance_id of this ListSubNetworkInterfacesRequest.
        :type instance_id: list[str]
        """
        self._instance_id = instance_id

    @property
    def instance_type(self):
        r"""Gets the instance_type of this ListSubNetworkInterfacesRequest.

        **参数解释**： 辅助弹性网卡所属云服务实例的类型，例如“RDS”，可以通过此字段过滤辅助弹性网卡，支持传入多个实例类型过滤。 **取值范围**： 不涉及。 **约束限制**： 不涉及。 **默认取值**： 不涉及。

        :return: The instance_type of this ListSubNetworkInterfacesRequest.
        :rtype: list[str]
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this ListSubNetworkInterfacesRequest.

        **参数解释**： 辅助弹性网卡所属云服务实例的类型，例如“RDS”，可以通过此字段过滤辅助弹性网卡，支持传入多个实例类型过滤。 **取值范围**： 不涉及。 **约束限制**： 不涉及。 **默认取值**： 不涉及。

        :param instance_type: The instance_type of this ListSubNetworkInterfacesRequest.
        :type instance_type: list[str]
        """
        self._instance_type = instance_type

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
        if not isinstance(other, ListSubNetworkInterfacesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
