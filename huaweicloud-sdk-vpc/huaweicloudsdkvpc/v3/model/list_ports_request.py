# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPortsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'list[str]',
        'name': 'list[str]',
        'admin_state_up': 'bool',
        'status': 'str',
        'virsubnet_id': 'list[str]',
        'device_id': 'list[str]',
        'mac_address': 'list[str]',
        'device_owner': 'list[str]',
        'device_owner_prefixlike': 'str',
        'description': 'list[str]',
        'bindinghost_id': 'list[str]',
        'private_ips': 'list[str]',
        'security_groups': 'list[str]',
        'vpc_id': 'list[str]',
        'allowed_address_pairs': 'list[str]',
        'instance_id': 'str',
        'instance_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'admin_state_up': 'admin_state_up',
        'status': 'status',
        'virsubnet_id': 'virsubnet_id',
        'device_id': 'device_id',
        'mac_address': 'mac_address',
        'device_owner': 'device_owner',
        'device_owner_prefixlike': 'device_owner_prefixlike',
        'description': 'description',
        'bindinghost_id': 'binding:host_id',
        'private_ips': 'private_ips',
        'security_groups': 'security_groups',
        'vpc_id': 'vpc_id',
        'allowed_address_pairs': 'allowed_address_pairs',
        'instance_id': 'instance_id',
        'instance_type': 'instance_type'
    }

    def __init__(self, id=None, name=None, admin_state_up=None, status=None, virsubnet_id=None, device_id=None, mac_address=None, device_owner=None, device_owner_prefixlike=None, description=None, bindinghost_id=None, private_ips=None, security_groups=None, vpc_id=None, allowed_address_pairs=None, instance_id=None, instance_type=None):
        r"""ListPortsRequest

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 端口的资源ID。 **取值范围**： 带“-”的标准UUID格式。
        :type id: list[str]
        :param name: **参数解释**： 端口的名称。 **取值范围**： 默认为空，最大长度不超过255。
        :type name: list[str]
        :param admin_state_up: **参数解释**： 端口的管理状态。 **取值范围**： true，false，默认值true。
        :type admin_state_up: bool
        :param status: **参数解释**： 端口的状态。 **取值范围**： - ACTIVE：端口处- 于活动状态，可以正常进行网络通信。 - BUILD：端口正在创建或配置中。 - DOWN：端口处于非活动状态，不能进行网络通信。Hana 硬直通虚拟机端口状态总为DOWN。
        :type status: str
        :param virsubnet_id: **参数解释**： 端口所在的虚拟子网ID。 **取值范围**： 带“-”的标准UUID格式。
        :type virsubnet_id: list[str]
        :param device_id: **参数解释**： 端口所属的设备ID。 **取值范围**： 带“-”的标准UUID格式。
        :type device_id: list[str]
        :param mac_address: **参数解释**： 端口的MAC地址。 **取值范围**： 不涉及
        :type mac_address: list[str]
        :param device_owner: **参数解释**： 端口所属的设备名称。 **取值范围**： - network:dhcp, 表示DHCP服务 - network:router_interface_distributed, 表示子网网关地址 - compute:xxx, 表示云服务器网卡私有IP地址，其中XXX对应具体的可用区名称，例如compute:aa-bb-cc表示私有IP地址被可用区aa-bb-cc内的云服务器使用 - neutron:VIP_PORT, 表示虚拟IP地址 - neutron:LOADBALANCERV2, 表示共享型ELB - neutron:LOADBALANCERV3, 表示独享型ELB - network:endpoint_interface, 表示VPC终端节点 - network:nat_gateway, 表示NAT网关 - network:ucmp, 表示UCMP端口，为企业路由器服务所用
        :type device_owner: list[str]
        :param device_owner_prefixlike: **参数解释**： 端口所属的设备名称前缀。 **取值范围**： - network：过滤出device_owner前缀是network的端口，如DHCP端口。 - compute：过滤出device_owner前缀是compute的端口，如云服务器网卡。 - neutron：过滤出device_owner前缀是compute的端口，如虚拟IP地址。
        :type device_owner_prefixlike: str
        :param description: **参数解释**： 端口的描述信息。 **取值范围**： 0-255个字符，不能包含“&lt;”和“&gt;”。
        :type description: list[str]
        :param bindinghost_id: **参数解释**： 端口所在的主机ID。 **取值范围**： 不涉及。
        :type bindinghost_id: list[str]
        :param private_ips: **参数解释**： 端口的私有IP地址。 **取值范围**： - private_ips&#x3D;ip_address&#x3D;{ip_address}，其中{ip_address}填IP地址，如192.168.21.22。 - private_ips&#x3D;subnet_cidr_id&#x3D;{subnet_id}，其中{subnet_id}填IPv4子网或IPv6子网的ID，如011fc878-5521-4654-a1ad-f5b0b5820302。
        :type private_ips: list[str]
        :param security_groups: **参数解释**： 端口绑定的安全组列表。 **取值范围**： 不涉及。
        :type security_groups: list[str]
        :param vpc_id: **参数解释**： 端口所在的VPC的ID。 **取值范围**： 带“-”的标准UUID格式。
        :type vpc_id: list[str]
        :param allowed_address_pairs: **参数解释**： 端口的IP/Mac对列表。 **取值范围**： - allowed_address_pairs&#x3D;ip_address&#x3D;{ip_address}，其中{ip_address}填IP地址，如192.168.21.22。 - allowed_address_pairs&#x3D;mac_address&#x3D;{mac_address}，其中{mac_address}填MAC地址，如fa:16:3e:b1:da:62。
        :type allowed_address_pairs: list[str]
        :param instance_id: **参数解释**： 端口所属的云服务实例ID，例如RDS实例ID。 **取值范围**： 不涉及。
        :type instance_id: str
        :param instance_type: **参数解释**： 端口所属的云服务实例类型，例如“RDS”。 **取值范围**： 不涉及。
        :type instance_type: str
        """
        
        

        self._id = None
        self._name = None
        self._admin_state_up = None
        self._status = None
        self._virsubnet_id = None
        self._device_id = None
        self._mac_address = None
        self._device_owner = None
        self._device_owner_prefixlike = None
        self._description = None
        self._bindinghost_id = None
        self._private_ips = None
        self._security_groups = None
        self._vpc_id = None
        self._allowed_address_pairs = None
        self._instance_id = None
        self._instance_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if status is not None:
            self.status = status
        if virsubnet_id is not None:
            self.virsubnet_id = virsubnet_id
        if device_id is not None:
            self.device_id = device_id
        if mac_address is not None:
            self.mac_address = mac_address
        if device_owner is not None:
            self.device_owner = device_owner
        if device_owner_prefixlike is not None:
            self.device_owner_prefixlike = device_owner_prefixlike
        if description is not None:
            self.description = description
        if bindinghost_id is not None:
            self.bindinghost_id = bindinghost_id
        if private_ips is not None:
            self.private_ips = private_ips
        if security_groups is not None:
            self.security_groups = security_groups
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if allowed_address_pairs is not None:
            self.allowed_address_pairs = allowed_address_pairs
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_type is not None:
            self.instance_type = instance_type

    @property
    def id(self):
        r"""Gets the id of this ListPortsRequest.

        **参数解释**： 端口的资源ID。 **取值范围**： 带“-”的标准UUID格式。

        :return: The id of this ListPortsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListPortsRequest.

        **参数解释**： 端口的资源ID。 **取值范围**： 带“-”的标准UUID格式。

        :param id: The id of this ListPortsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListPortsRequest.

        **参数解释**： 端口的名称。 **取值范围**： 默认为空，最大长度不超过255。

        :return: The name of this ListPortsRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListPortsRequest.

        **参数解释**： 端口的名称。 **取值范围**： 默认为空，最大长度不超过255。

        :param name: The name of this ListPortsRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this ListPortsRequest.

        **参数解释**： 端口的管理状态。 **取值范围**： true，false，默认值true。

        :return: The admin_state_up of this ListPortsRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this ListPortsRequest.

        **参数解释**： 端口的管理状态。 **取值范围**： true，false，默认值true。

        :param admin_state_up: The admin_state_up of this ListPortsRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def status(self):
        r"""Gets the status of this ListPortsRequest.

        **参数解释**： 端口的状态。 **取值范围**： - ACTIVE：端口处- 于活动状态，可以正常进行网络通信。 - BUILD：端口正在创建或配置中。 - DOWN：端口处于非活动状态，不能进行网络通信。Hana 硬直通虚拟机端口状态总为DOWN。

        :return: The status of this ListPortsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListPortsRequest.

        **参数解释**： 端口的状态。 **取值范围**： - ACTIVE：端口处- 于活动状态，可以正常进行网络通信。 - BUILD：端口正在创建或配置中。 - DOWN：端口处于非活动状态，不能进行网络通信。Hana 硬直通虚拟机端口状态总为DOWN。

        :param status: The status of this ListPortsRequest.
        :type status: str
        """
        self._status = status

    @property
    def virsubnet_id(self):
        r"""Gets the virsubnet_id of this ListPortsRequest.

        **参数解释**： 端口所在的虚拟子网ID。 **取值范围**： 带“-”的标准UUID格式。

        :return: The virsubnet_id of this ListPortsRequest.
        :rtype: list[str]
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        r"""Sets the virsubnet_id of this ListPortsRequest.

        **参数解释**： 端口所在的虚拟子网ID。 **取值范围**： 带“-”的标准UUID格式。

        :param virsubnet_id: The virsubnet_id of this ListPortsRequest.
        :type virsubnet_id: list[str]
        """
        self._virsubnet_id = virsubnet_id

    @property
    def device_id(self):
        r"""Gets the device_id of this ListPortsRequest.

        **参数解释**： 端口所属的设备ID。 **取值范围**： 带“-”的标准UUID格式。

        :return: The device_id of this ListPortsRequest.
        :rtype: list[str]
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        r"""Sets the device_id of this ListPortsRequest.

        **参数解释**： 端口所属的设备ID。 **取值范围**： 带“-”的标准UUID格式。

        :param device_id: The device_id of this ListPortsRequest.
        :type device_id: list[str]
        """
        self._device_id = device_id

    @property
    def mac_address(self):
        r"""Gets the mac_address of this ListPortsRequest.

        **参数解释**： 端口的MAC地址。 **取值范围**： 不涉及

        :return: The mac_address of this ListPortsRequest.
        :rtype: list[str]
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        r"""Sets the mac_address of this ListPortsRequest.

        **参数解释**： 端口的MAC地址。 **取值范围**： 不涉及

        :param mac_address: The mac_address of this ListPortsRequest.
        :type mac_address: list[str]
        """
        self._mac_address = mac_address

    @property
    def device_owner(self):
        r"""Gets the device_owner of this ListPortsRequest.

        **参数解释**： 端口所属的设备名称。 **取值范围**： - network:dhcp, 表示DHCP服务 - network:router_interface_distributed, 表示子网网关地址 - compute:xxx, 表示云服务器网卡私有IP地址，其中XXX对应具体的可用区名称，例如compute:aa-bb-cc表示私有IP地址被可用区aa-bb-cc内的云服务器使用 - neutron:VIP_PORT, 表示虚拟IP地址 - neutron:LOADBALANCERV2, 表示共享型ELB - neutron:LOADBALANCERV3, 表示独享型ELB - network:endpoint_interface, 表示VPC终端节点 - network:nat_gateway, 表示NAT网关 - network:ucmp, 表示UCMP端口，为企业路由器服务所用

        :return: The device_owner of this ListPortsRequest.
        :rtype: list[str]
        """
        return self._device_owner

    @device_owner.setter
    def device_owner(self, device_owner):
        r"""Sets the device_owner of this ListPortsRequest.

        **参数解释**： 端口所属的设备名称。 **取值范围**： - network:dhcp, 表示DHCP服务 - network:router_interface_distributed, 表示子网网关地址 - compute:xxx, 表示云服务器网卡私有IP地址，其中XXX对应具体的可用区名称，例如compute:aa-bb-cc表示私有IP地址被可用区aa-bb-cc内的云服务器使用 - neutron:VIP_PORT, 表示虚拟IP地址 - neutron:LOADBALANCERV2, 表示共享型ELB - neutron:LOADBALANCERV3, 表示独享型ELB - network:endpoint_interface, 表示VPC终端节点 - network:nat_gateway, 表示NAT网关 - network:ucmp, 表示UCMP端口，为企业路由器服务所用

        :param device_owner: The device_owner of this ListPortsRequest.
        :type device_owner: list[str]
        """
        self._device_owner = device_owner

    @property
    def device_owner_prefixlike(self):
        r"""Gets the device_owner_prefixlike of this ListPortsRequest.

        **参数解释**： 端口所属的设备名称前缀。 **取值范围**： - network：过滤出device_owner前缀是network的端口，如DHCP端口。 - compute：过滤出device_owner前缀是compute的端口，如云服务器网卡。 - neutron：过滤出device_owner前缀是compute的端口，如虚拟IP地址。

        :return: The device_owner_prefixlike of this ListPortsRequest.
        :rtype: str
        """
        return self._device_owner_prefixlike

    @device_owner_prefixlike.setter
    def device_owner_prefixlike(self, device_owner_prefixlike):
        r"""Sets the device_owner_prefixlike of this ListPortsRequest.

        **参数解释**： 端口所属的设备名称前缀。 **取值范围**： - network：过滤出device_owner前缀是network的端口，如DHCP端口。 - compute：过滤出device_owner前缀是compute的端口，如云服务器网卡。 - neutron：过滤出device_owner前缀是compute的端口，如虚拟IP地址。

        :param device_owner_prefixlike: The device_owner_prefixlike of this ListPortsRequest.
        :type device_owner_prefixlike: str
        """
        self._device_owner_prefixlike = device_owner_prefixlike

    @property
    def description(self):
        r"""Gets the description of this ListPortsRequest.

        **参数解释**： 端口的描述信息。 **取值范围**： 0-255个字符，不能包含“<”和“>”。

        :return: The description of this ListPortsRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListPortsRequest.

        **参数解释**： 端口的描述信息。 **取值范围**： 0-255个字符，不能包含“<”和“>”。

        :param description: The description of this ListPortsRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def bindinghost_id(self):
        r"""Gets the bindinghost_id of this ListPortsRequest.

        **参数解释**： 端口所在的主机ID。 **取值范围**： 不涉及。

        :return: The bindinghost_id of this ListPortsRequest.
        :rtype: list[str]
        """
        return self._bindinghost_id

    @bindinghost_id.setter
    def bindinghost_id(self, bindinghost_id):
        r"""Sets the bindinghost_id of this ListPortsRequest.

        **参数解释**： 端口所在的主机ID。 **取值范围**： 不涉及。

        :param bindinghost_id: The bindinghost_id of this ListPortsRequest.
        :type bindinghost_id: list[str]
        """
        self._bindinghost_id = bindinghost_id

    @property
    def private_ips(self):
        r"""Gets the private_ips of this ListPortsRequest.

        **参数解释**： 端口的私有IP地址。 **取值范围**： - private_ips=ip_address={ip_address}，其中{ip_address}填IP地址，如192.168.21.22。 - private_ips=subnet_cidr_id={subnet_id}，其中{subnet_id}填IPv4子网或IPv6子网的ID，如011fc878-5521-4654-a1ad-f5b0b5820302。

        :return: The private_ips of this ListPortsRequest.
        :rtype: list[str]
        """
        return self._private_ips

    @private_ips.setter
    def private_ips(self, private_ips):
        r"""Sets the private_ips of this ListPortsRequest.

        **参数解释**： 端口的私有IP地址。 **取值范围**： - private_ips=ip_address={ip_address}，其中{ip_address}填IP地址，如192.168.21.22。 - private_ips=subnet_cidr_id={subnet_id}，其中{subnet_id}填IPv4子网或IPv6子网的ID，如011fc878-5521-4654-a1ad-f5b0b5820302。

        :param private_ips: The private_ips of this ListPortsRequest.
        :type private_ips: list[str]
        """
        self._private_ips = private_ips

    @property
    def security_groups(self):
        r"""Gets the security_groups of this ListPortsRequest.

        **参数解释**： 端口绑定的安全组列表。 **取值范围**： 不涉及。

        :return: The security_groups of this ListPortsRequest.
        :rtype: list[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        r"""Sets the security_groups of this ListPortsRequest.

        **参数解释**： 端口绑定的安全组列表。 **取值范围**： 不涉及。

        :param security_groups: The security_groups of this ListPortsRequest.
        :type security_groups: list[str]
        """
        self._security_groups = security_groups

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ListPortsRequest.

        **参数解释**： 端口所在的VPC的ID。 **取值范围**： 带“-”的标准UUID格式。

        :return: The vpc_id of this ListPortsRequest.
        :rtype: list[str]
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ListPortsRequest.

        **参数解释**： 端口所在的VPC的ID。 **取值范围**： 带“-”的标准UUID格式。

        :param vpc_id: The vpc_id of this ListPortsRequest.
        :type vpc_id: list[str]
        """
        self._vpc_id = vpc_id

    @property
    def allowed_address_pairs(self):
        r"""Gets the allowed_address_pairs of this ListPortsRequest.

        **参数解释**： 端口的IP/Mac对列表。 **取值范围**： - allowed_address_pairs=ip_address={ip_address}，其中{ip_address}填IP地址，如192.168.21.22。 - allowed_address_pairs=mac_address={mac_address}，其中{mac_address}填MAC地址，如fa:16:3e:b1:da:62。

        :return: The allowed_address_pairs of this ListPortsRequest.
        :rtype: list[str]
        """
        return self._allowed_address_pairs

    @allowed_address_pairs.setter
    def allowed_address_pairs(self, allowed_address_pairs):
        r"""Sets the allowed_address_pairs of this ListPortsRequest.

        **参数解释**： 端口的IP/Mac对列表。 **取值范围**： - allowed_address_pairs=ip_address={ip_address}，其中{ip_address}填IP地址，如192.168.21.22。 - allowed_address_pairs=mac_address={mac_address}，其中{mac_address}填MAC地址，如fa:16:3e:b1:da:62。

        :param allowed_address_pairs: The allowed_address_pairs of this ListPortsRequest.
        :type allowed_address_pairs: list[str]
        """
        self._allowed_address_pairs = allowed_address_pairs

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListPortsRequest.

        **参数解释**： 端口所属的云服务实例ID，例如RDS实例ID。 **取值范围**： 不涉及。

        :return: The instance_id of this ListPortsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListPortsRequest.

        **参数解释**： 端口所属的云服务实例ID，例如RDS实例ID。 **取值范围**： 不涉及。

        :param instance_id: The instance_id of this ListPortsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_type(self):
        r"""Gets the instance_type of this ListPortsRequest.

        **参数解释**： 端口所属的云服务实例类型，例如“RDS”。 **取值范围**： 不涉及。

        :return: The instance_type of this ListPortsRequest.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this ListPortsRequest.

        **参数解释**： 端口所属的云服务实例类型，例如“RDS”。 **取值范围**： 不涉及。

        :param instance_type: The instance_type of this ListPortsRequest.
        :type instance_type: str
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
        if not isinstance(other, ListPortsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
