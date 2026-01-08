# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VpcQuotas:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'acl_policy_contain_rules': 'int',
        'address_group': 'int',
        'address_group_contain_ipset': 'int',
        'clouddcn_firewall_group': 'int',
        'clouddcn_acl_policy_contain_rules': 'int',
        'edge_gateway': 'int',
        'eni_contain_secgroup': 'int',
        'firewall_policy_contain_ipv4_composite_rules': 'int',
        'firewall_policy_contain_ipv6_composite_rules': 'int',
        'forward_policy': 'int',
        'forward_policy_contain_ports': 'int',
        'forward_rule': 'int',
        'peering': 'int',
        'roce_cluster_contain_networks': 'int',
        'rtb_allow_sys_cidr_routes': 'int',
        'shared_bandwidth': 'int',
        'shared_bandwidth_contain_publicip': 'int',
        'secgroup_contain_rules': 'int',
        'secgroup_referred_by_nic': 'int',
        'security_group': 'int',
        'security_group_contain_egress_ipv4_composite_rules': 'int',
        'security_group_contain_egress_ipv6_composite_rules': 'int',
        'security_group_contain_ingress_ipv4_composite_rules': 'int',
        'security_group_contain_ingress_ipv6_composite_rules': 'int',
        'security_group_rule': 'int',
        'subnet_contain_eni': 'int',
        'traffic_mirror_filter': 'int',
        'traffic_mirror_filter_referred_by_session': 'int',
        'traffic_mirror_filter_contain_rules_each_direction': 'int',
        'traffic_mirror_session': 'int',
        'traffic_mirror_session_contain_sources': 'int',
        'traffic_mirror_source_referred_by_session': 'int',
        'traffic_mirror_target_elb_referred_by_session': 'int',
        'traffic_mirror_target_eni_referred_by_session': 'int',
        'vip': 'int',
        'virsubnet': 'int',
        'virsubnet_contain_ipv4_cidr_reservations': 'int',
        'virsubnet_contain_ipv6_cidr_reservations': 'int',
        'vpc': 'int',
        'vpc_contain_eni': 'int',
        'vpc_contain_vip': 'int',
        'vpc_contain_virsubnet': 'int'
    }

    attribute_map = {
        'acl_policy_contain_rules': 'acl_policy_contain_rules',
        'address_group': 'address_group',
        'address_group_contain_ipset': 'address_group_contain_ipset',
        'clouddcn_firewall_group': 'clouddcn_firewall_group',
        'clouddcn_acl_policy_contain_rules': 'clouddcn_acl_policy_contain_rules',
        'edge_gateway': 'edge_gateway',
        'eni_contain_secgroup': 'eni_contain_secgroup',
        'firewall_policy_contain_ipv4_composite_rules': 'firewall_policy_contain_ipv4_composite_rules',
        'firewall_policy_contain_ipv6_composite_rules': 'firewall_policy_contain_ipv6_composite_rules',
        'forward_policy': 'forward_policy',
        'forward_policy_contain_ports': 'forward_policy_contain_ports',
        'forward_rule': 'forward_rule',
        'peering': 'peering',
        'roce_cluster_contain_networks': 'roce_cluster_contain_networks',
        'rtb_allow_sys_cidr_routes': 'rtb_allow_sys_cidr_routes',
        'shared_bandwidth': 'shared_bandwidth',
        'shared_bandwidth_contain_publicip': 'shared_bandwidth_contain_publicip',
        'secgroup_contain_rules': 'secgroup_contain_rules',
        'secgroup_referred_by_nic': 'secgroup_referred_by_nic',
        'security_group': 'security_group',
        'security_group_contain_egress_ipv4_composite_rules': 'security_group_contain_egress_ipv4_composite_rules',
        'security_group_contain_egress_ipv6_composite_rules': 'security_group_contain_egress_ipv6_composite_rules',
        'security_group_contain_ingress_ipv4_composite_rules': 'security_group_contain_ingress_ipv4_composite_rules',
        'security_group_contain_ingress_ipv6_composite_rules': 'security_group_contain_ingress_ipv6_composite_rules',
        'security_group_rule': 'security_group_rule',
        'subnet_contain_eni': 'subnet_contain_eni',
        'traffic_mirror_filter': 'traffic_mirror_filter',
        'traffic_mirror_filter_referred_by_session': 'traffic_mirror_filter_referred_by_session',
        'traffic_mirror_filter_contain_rules_each_direction': 'traffic_mirror_filter_contain_rules_each_direction',
        'traffic_mirror_session': 'traffic_mirror_session',
        'traffic_mirror_session_contain_sources': 'traffic_mirror_session_contain_sources',
        'traffic_mirror_source_referred_by_session': 'traffic_mirror_source_referred_by_session',
        'traffic_mirror_target_elb_referred_by_session': 'traffic_mirror_target_elb_referred_by_session',
        'traffic_mirror_target_eni_referred_by_session': 'traffic_mirror_target_eni_referred_by_session',
        'vip': 'vip',
        'virsubnet': 'virsubnet',
        'virsubnet_contain_ipv4_cidr_reservations': 'virsubnet_contain_ipv4_cidr_reservations',
        'virsubnet_contain_ipv6_cidr_reservations': 'virsubnet_contain_ipv6_cidr_reservations',
        'vpc': 'vpc',
        'vpc_contain_eni': 'vpc_contain_eni',
        'vpc_contain_vip': 'vpc_contain_vip',
        'vpc_contain_virsubnet': 'vpc_contain_virsubnet'
    }

    def __init__(self, acl_policy_contain_rules=None, address_group=None, address_group_contain_ipset=None, clouddcn_firewall_group=None, clouddcn_acl_policy_contain_rules=None, edge_gateway=None, eni_contain_secgroup=None, firewall_policy_contain_ipv4_composite_rules=None, firewall_policy_contain_ipv6_composite_rules=None, forward_policy=None, forward_policy_contain_ports=None, forward_rule=None, peering=None, roce_cluster_contain_networks=None, rtb_allow_sys_cidr_routes=None, shared_bandwidth=None, shared_bandwidth_contain_publicip=None, secgroup_contain_rules=None, secgroup_referred_by_nic=None, security_group=None, security_group_contain_egress_ipv4_composite_rules=None, security_group_contain_egress_ipv6_composite_rules=None, security_group_contain_ingress_ipv4_composite_rules=None, security_group_contain_ingress_ipv6_composite_rules=None, security_group_rule=None, subnet_contain_eni=None, traffic_mirror_filter=None, traffic_mirror_filter_referred_by_session=None, traffic_mirror_filter_contain_rules_each_direction=None, traffic_mirror_session=None, traffic_mirror_session_contain_sources=None, traffic_mirror_source_referred_by_session=None, traffic_mirror_target_elb_referred_by_session=None, traffic_mirror_target_eni_referred_by_session=None, vip=None, virsubnet=None, virsubnet_contain_ipv4_cidr_reservations=None, virsubnet_contain_ipv6_cidr_reservations=None, vpc=None, vpc_contain_eni=None, vpc_contain_vip=None, vpc_contain_virsubnet=None):
        r"""VpcQuotas

        The model defined in huaweicloud sdk

        :param acl_policy_contain_rules: **参数解释**： 网络ACL单方向规则数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type acl_policy_contain_rules: int
        :param address_group: **参数解释**： IP地址组数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type address_group: int
        :param address_group_contain_ipset: **参数解释**： IP地址组包含的IP地址集数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type address_group_contain_ipset: int
        :param clouddcn_firewall_group: **参数解释**： CloudDCN场景的网络ACL数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type clouddcn_firewall_group: int
        :param clouddcn_acl_policy_contain_rules: **参数解释**： CloudDCN场景的网络ACL单方向规则数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type clouddcn_acl_policy_contain_rules: int
        :param edge_gateway: **参数解释**： 边缘网关数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type edge_gateway: int
        :param eni_contain_secgroup: **参数解释**： 弹性网卡关联的安全组数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type eni_contain_secgroup: int
        :param firewall_policy_contain_ipv4_composite_rules: **参数解释**： 网络ACL中配置了IP地址组或不连续端口的IPv4规则数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type firewall_policy_contain_ipv4_composite_rules: int
        :param firewall_policy_contain_ipv6_composite_rules: **参数解释**： 网络ACL中配置了IP地址组或不连续端口的IPv6规则数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type firewall_policy_contain_ipv6_composite_rules: int
        :param forward_policy: **参数解释**： 云转发策略数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type forward_policy: int
        :param forward_policy_contain_ports: **参数解释**： 云转发策略关联端口数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type forward_policy_contain_ports: int
        :param forward_rule: **参数解释**： 云转发规则数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type forward_rule: int
        :param peering: **参数解释**： 对等连接数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type peering: int
        :param roce_cluster_contain_networks: **参数解释**： 一个physical_network下支持创建的roce网络数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type roce_cluster_contain_networks: int
        :param rtb_allow_sys_cidr_routes: **参数解释**： 路由表支持系统路由数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type rtb_allow_sys_cidr_routes: int
        :param shared_bandwidth: **参数解释**： 共享带宽组数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type shared_bandwidth: int
        :param shared_bandwidth_contain_publicip: **参数解释**： 单个共享带宽关联的弹性公网IP数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type shared_bandwidth_contain_publicip: int
        :param secgroup_contain_rules: **参数解释**： 单个安全组包含的规则数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type secgroup_contain_rules: int
        :param secgroup_referred_by_nic: **参数解释**： 单个安全组关联的网卡数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type secgroup_referred_by_nic: int
        :param security_group: **参数解释**： 安全组数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type security_group: int
        :param security_group_contain_egress_ipv4_composite_rules: **参数解释**： 安全组中配置了IP地址组、不连续端口或远端安全组的IPv4出方向规则数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type security_group_contain_egress_ipv4_composite_rules: int
        :param security_group_contain_egress_ipv6_composite_rules: **参数解释**： 安全组中配置了IP地址组、不连续端口或远端安全组的IPv6出方向规则数配。 **取值范围**： 整数，-1表示此配额未上线。
        :type security_group_contain_egress_ipv6_composite_rules: int
        :param security_group_contain_ingress_ipv4_composite_rules: **参数解释**： 安全组中配置了IP地址组、不连续端口或远端安全组的IPv4入方向规则数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type security_group_contain_ingress_ipv4_composite_rules: int
        :param security_group_contain_ingress_ipv6_composite_rules: **参数解释**： 安全组中配置了IP地址组、不连续端口或远端安全组的IPv6入方向规则数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type security_group_contain_ingress_ipv6_composite_rules: int
        :param security_group_rule: **参数解释**： 安全组规则数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type security_group_rule: int
        :param subnet_contain_eni: **参数解释**： 单个子网包含的弹性网卡数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type subnet_contain_eni: int
        :param traffic_mirror_filter: **参数解释**： 流量镜像筛选条件数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type traffic_mirror_filter: int
        :param traffic_mirror_filter_referred_by_session: **参数解释**： 单个流量镜像筛选条件被镜像会话引用数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type traffic_mirror_filter_referred_by_session: int
        :param traffic_mirror_filter_contain_rules_each_direction: **参数解释**： 流量镜像筛选条件单方向规则数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type traffic_mirror_filter_contain_rules_each_direction: int
        :param traffic_mirror_session: **参数解释**： 流量镜像会话数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type traffic_mirror_session: int
        :param traffic_mirror_session_contain_sources: **参数解释**： 单个流量镜像会话关联的镜像源数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type traffic_mirror_session_contain_sources: int
        :param traffic_mirror_source_referred_by_session: **参数解释**： 单个镜像源被流量镜像会话引用次数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type traffic_mirror_source_referred_by_session: int
        :param traffic_mirror_target_elb_referred_by_session: **参数解释**： 私网弹性负载均衡类型的镜像目的被会话引用次数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type traffic_mirror_target_elb_referred_by_session: int
        :param traffic_mirror_target_eni_referred_by_session: **参数解释**： 弹性网卡类型的镜像目的被会话引用次数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type traffic_mirror_target_eni_referred_by_session: int
        :param vip: **参数解释**： 虚拟IP数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type vip: int
        :param virsubnet: **参数解释**： 子网数配额。 **取值范围**： 整数，-1表示此配额未上线，请通过[v1查询配额接口](vpc_quota_0001.xml)。
        :type virsubnet: int
        :param virsubnet_contain_ipv4_cidr_reservations: **参数解释**： 单子网包含IPv4子网预留网段数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type virsubnet_contain_ipv4_cidr_reservations: int
        :param virsubnet_contain_ipv6_cidr_reservations: **参数解释**： 单子网包含IPv6子网预留网段数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type virsubnet_contain_ipv6_cidr_reservations: int
        :param vpc: **参数解释**： VPC数配额。 **取值范围**： 整数，-1表示此配额未上线，请通过[v1查询配额接口](vpc_quota_0001.xml)。
        :type vpc: int
        :param vpc_contain_eni: **参数解释**： 单个VPC包含弹性网卡数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type vpc_contain_eni: int
        :param vpc_contain_vip: **参数解释**： 单个VPC包含虚拟IP数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type vpc_contain_vip: int
        :param vpc_contain_virsubnet: **参数解释**： 单个VPC包含子网数配额。 **取值范围**： 整数，-1表示此配额未上线。
        :type vpc_contain_virsubnet: int
        """
        
        

        self._acl_policy_contain_rules = None
        self._address_group = None
        self._address_group_contain_ipset = None
        self._clouddcn_firewall_group = None
        self._clouddcn_acl_policy_contain_rules = None
        self._edge_gateway = None
        self._eni_contain_secgroup = None
        self._firewall_policy_contain_ipv4_composite_rules = None
        self._firewall_policy_contain_ipv6_composite_rules = None
        self._forward_policy = None
        self._forward_policy_contain_ports = None
        self._forward_rule = None
        self._peering = None
        self._roce_cluster_contain_networks = None
        self._rtb_allow_sys_cidr_routes = None
        self._shared_bandwidth = None
        self._shared_bandwidth_contain_publicip = None
        self._secgroup_contain_rules = None
        self._secgroup_referred_by_nic = None
        self._security_group = None
        self._security_group_contain_egress_ipv4_composite_rules = None
        self._security_group_contain_egress_ipv6_composite_rules = None
        self._security_group_contain_ingress_ipv4_composite_rules = None
        self._security_group_contain_ingress_ipv6_composite_rules = None
        self._security_group_rule = None
        self._subnet_contain_eni = None
        self._traffic_mirror_filter = None
        self._traffic_mirror_filter_referred_by_session = None
        self._traffic_mirror_filter_contain_rules_each_direction = None
        self._traffic_mirror_session = None
        self._traffic_mirror_session_contain_sources = None
        self._traffic_mirror_source_referred_by_session = None
        self._traffic_mirror_target_elb_referred_by_session = None
        self._traffic_mirror_target_eni_referred_by_session = None
        self._vip = None
        self._virsubnet = None
        self._virsubnet_contain_ipv4_cidr_reservations = None
        self._virsubnet_contain_ipv6_cidr_reservations = None
        self._vpc = None
        self._vpc_contain_eni = None
        self._vpc_contain_vip = None
        self._vpc_contain_virsubnet = None
        self.discriminator = None

        if acl_policy_contain_rules is not None:
            self.acl_policy_contain_rules = acl_policy_contain_rules
        if address_group is not None:
            self.address_group = address_group
        if address_group_contain_ipset is not None:
            self.address_group_contain_ipset = address_group_contain_ipset
        if clouddcn_firewall_group is not None:
            self.clouddcn_firewall_group = clouddcn_firewall_group
        if clouddcn_acl_policy_contain_rules is not None:
            self.clouddcn_acl_policy_contain_rules = clouddcn_acl_policy_contain_rules
        if edge_gateway is not None:
            self.edge_gateway = edge_gateway
        if eni_contain_secgroup is not None:
            self.eni_contain_secgroup = eni_contain_secgroup
        if firewall_policy_contain_ipv4_composite_rules is not None:
            self.firewall_policy_contain_ipv4_composite_rules = firewall_policy_contain_ipv4_composite_rules
        if firewall_policy_contain_ipv6_composite_rules is not None:
            self.firewall_policy_contain_ipv6_composite_rules = firewall_policy_contain_ipv6_composite_rules
        if forward_policy is not None:
            self.forward_policy = forward_policy
        if forward_policy_contain_ports is not None:
            self.forward_policy_contain_ports = forward_policy_contain_ports
        if forward_rule is not None:
            self.forward_rule = forward_rule
        if peering is not None:
            self.peering = peering
        if roce_cluster_contain_networks is not None:
            self.roce_cluster_contain_networks = roce_cluster_contain_networks
        if rtb_allow_sys_cidr_routes is not None:
            self.rtb_allow_sys_cidr_routes = rtb_allow_sys_cidr_routes
        if shared_bandwidth is not None:
            self.shared_bandwidth = shared_bandwidth
        if shared_bandwidth_contain_publicip is not None:
            self.shared_bandwidth_contain_publicip = shared_bandwidth_contain_publicip
        if secgroup_contain_rules is not None:
            self.secgroup_contain_rules = secgroup_contain_rules
        if secgroup_referred_by_nic is not None:
            self.secgroup_referred_by_nic = secgroup_referred_by_nic
        if security_group is not None:
            self.security_group = security_group
        if security_group_contain_egress_ipv4_composite_rules is not None:
            self.security_group_contain_egress_ipv4_composite_rules = security_group_contain_egress_ipv4_composite_rules
        if security_group_contain_egress_ipv6_composite_rules is not None:
            self.security_group_contain_egress_ipv6_composite_rules = security_group_contain_egress_ipv6_composite_rules
        if security_group_contain_ingress_ipv4_composite_rules is not None:
            self.security_group_contain_ingress_ipv4_composite_rules = security_group_contain_ingress_ipv4_composite_rules
        if security_group_contain_ingress_ipv6_composite_rules is not None:
            self.security_group_contain_ingress_ipv6_composite_rules = security_group_contain_ingress_ipv6_composite_rules
        if security_group_rule is not None:
            self.security_group_rule = security_group_rule
        if subnet_contain_eni is not None:
            self.subnet_contain_eni = subnet_contain_eni
        if traffic_mirror_filter is not None:
            self.traffic_mirror_filter = traffic_mirror_filter
        if traffic_mirror_filter_referred_by_session is not None:
            self.traffic_mirror_filter_referred_by_session = traffic_mirror_filter_referred_by_session
        if traffic_mirror_filter_contain_rules_each_direction is not None:
            self.traffic_mirror_filter_contain_rules_each_direction = traffic_mirror_filter_contain_rules_each_direction
        if traffic_mirror_session is not None:
            self.traffic_mirror_session = traffic_mirror_session
        if traffic_mirror_session_contain_sources is not None:
            self.traffic_mirror_session_contain_sources = traffic_mirror_session_contain_sources
        if traffic_mirror_source_referred_by_session is not None:
            self.traffic_mirror_source_referred_by_session = traffic_mirror_source_referred_by_session
        if traffic_mirror_target_elb_referred_by_session is not None:
            self.traffic_mirror_target_elb_referred_by_session = traffic_mirror_target_elb_referred_by_session
        if traffic_mirror_target_eni_referred_by_session is not None:
            self.traffic_mirror_target_eni_referred_by_session = traffic_mirror_target_eni_referred_by_session
        if vip is not None:
            self.vip = vip
        if virsubnet is not None:
            self.virsubnet = virsubnet
        if virsubnet_contain_ipv4_cidr_reservations is not None:
            self.virsubnet_contain_ipv4_cidr_reservations = virsubnet_contain_ipv4_cidr_reservations
        if virsubnet_contain_ipv6_cidr_reservations is not None:
            self.virsubnet_contain_ipv6_cidr_reservations = virsubnet_contain_ipv6_cidr_reservations
        if vpc is not None:
            self.vpc = vpc
        if vpc_contain_eni is not None:
            self.vpc_contain_eni = vpc_contain_eni
        if vpc_contain_vip is not None:
            self.vpc_contain_vip = vpc_contain_vip
        if vpc_contain_virsubnet is not None:
            self.vpc_contain_virsubnet = vpc_contain_virsubnet

    @property
    def acl_policy_contain_rules(self):
        r"""Gets the acl_policy_contain_rules of this VpcQuotas.

        **参数解释**： 网络ACL单方向规则数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The acl_policy_contain_rules of this VpcQuotas.
        :rtype: int
        """
        return self._acl_policy_contain_rules

    @acl_policy_contain_rules.setter
    def acl_policy_contain_rules(self, acl_policy_contain_rules):
        r"""Sets the acl_policy_contain_rules of this VpcQuotas.

        **参数解释**： 网络ACL单方向规则数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param acl_policy_contain_rules: The acl_policy_contain_rules of this VpcQuotas.
        :type acl_policy_contain_rules: int
        """
        self._acl_policy_contain_rules = acl_policy_contain_rules

    @property
    def address_group(self):
        r"""Gets the address_group of this VpcQuotas.

        **参数解释**： IP地址组数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The address_group of this VpcQuotas.
        :rtype: int
        """
        return self._address_group

    @address_group.setter
    def address_group(self, address_group):
        r"""Sets the address_group of this VpcQuotas.

        **参数解释**： IP地址组数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param address_group: The address_group of this VpcQuotas.
        :type address_group: int
        """
        self._address_group = address_group

    @property
    def address_group_contain_ipset(self):
        r"""Gets the address_group_contain_ipset of this VpcQuotas.

        **参数解释**： IP地址组包含的IP地址集数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The address_group_contain_ipset of this VpcQuotas.
        :rtype: int
        """
        return self._address_group_contain_ipset

    @address_group_contain_ipset.setter
    def address_group_contain_ipset(self, address_group_contain_ipset):
        r"""Sets the address_group_contain_ipset of this VpcQuotas.

        **参数解释**： IP地址组包含的IP地址集数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param address_group_contain_ipset: The address_group_contain_ipset of this VpcQuotas.
        :type address_group_contain_ipset: int
        """
        self._address_group_contain_ipset = address_group_contain_ipset

    @property
    def clouddcn_firewall_group(self):
        r"""Gets the clouddcn_firewall_group of this VpcQuotas.

        **参数解释**： CloudDCN场景的网络ACL数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The clouddcn_firewall_group of this VpcQuotas.
        :rtype: int
        """
        return self._clouddcn_firewall_group

    @clouddcn_firewall_group.setter
    def clouddcn_firewall_group(self, clouddcn_firewall_group):
        r"""Sets the clouddcn_firewall_group of this VpcQuotas.

        **参数解释**： CloudDCN场景的网络ACL数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param clouddcn_firewall_group: The clouddcn_firewall_group of this VpcQuotas.
        :type clouddcn_firewall_group: int
        """
        self._clouddcn_firewall_group = clouddcn_firewall_group

    @property
    def clouddcn_acl_policy_contain_rules(self):
        r"""Gets the clouddcn_acl_policy_contain_rules of this VpcQuotas.

        **参数解释**： CloudDCN场景的网络ACL单方向规则数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The clouddcn_acl_policy_contain_rules of this VpcQuotas.
        :rtype: int
        """
        return self._clouddcn_acl_policy_contain_rules

    @clouddcn_acl_policy_contain_rules.setter
    def clouddcn_acl_policy_contain_rules(self, clouddcn_acl_policy_contain_rules):
        r"""Sets the clouddcn_acl_policy_contain_rules of this VpcQuotas.

        **参数解释**： CloudDCN场景的网络ACL单方向规则数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param clouddcn_acl_policy_contain_rules: The clouddcn_acl_policy_contain_rules of this VpcQuotas.
        :type clouddcn_acl_policy_contain_rules: int
        """
        self._clouddcn_acl_policy_contain_rules = clouddcn_acl_policy_contain_rules

    @property
    def edge_gateway(self):
        r"""Gets the edge_gateway of this VpcQuotas.

        **参数解释**： 边缘网关数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The edge_gateway of this VpcQuotas.
        :rtype: int
        """
        return self._edge_gateway

    @edge_gateway.setter
    def edge_gateway(self, edge_gateway):
        r"""Sets the edge_gateway of this VpcQuotas.

        **参数解释**： 边缘网关数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param edge_gateway: The edge_gateway of this VpcQuotas.
        :type edge_gateway: int
        """
        self._edge_gateway = edge_gateway

    @property
    def eni_contain_secgroup(self):
        r"""Gets the eni_contain_secgroup of this VpcQuotas.

        **参数解释**： 弹性网卡关联的安全组数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The eni_contain_secgroup of this VpcQuotas.
        :rtype: int
        """
        return self._eni_contain_secgroup

    @eni_contain_secgroup.setter
    def eni_contain_secgroup(self, eni_contain_secgroup):
        r"""Sets the eni_contain_secgroup of this VpcQuotas.

        **参数解释**： 弹性网卡关联的安全组数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param eni_contain_secgroup: The eni_contain_secgroup of this VpcQuotas.
        :type eni_contain_secgroup: int
        """
        self._eni_contain_secgroup = eni_contain_secgroup

    @property
    def firewall_policy_contain_ipv4_composite_rules(self):
        r"""Gets the firewall_policy_contain_ipv4_composite_rules of this VpcQuotas.

        **参数解释**： 网络ACL中配置了IP地址组或不连续端口的IPv4规则数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The firewall_policy_contain_ipv4_composite_rules of this VpcQuotas.
        :rtype: int
        """
        return self._firewall_policy_contain_ipv4_composite_rules

    @firewall_policy_contain_ipv4_composite_rules.setter
    def firewall_policy_contain_ipv4_composite_rules(self, firewall_policy_contain_ipv4_composite_rules):
        r"""Sets the firewall_policy_contain_ipv4_composite_rules of this VpcQuotas.

        **参数解释**： 网络ACL中配置了IP地址组或不连续端口的IPv4规则数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param firewall_policy_contain_ipv4_composite_rules: The firewall_policy_contain_ipv4_composite_rules of this VpcQuotas.
        :type firewall_policy_contain_ipv4_composite_rules: int
        """
        self._firewall_policy_contain_ipv4_composite_rules = firewall_policy_contain_ipv4_composite_rules

    @property
    def firewall_policy_contain_ipv6_composite_rules(self):
        r"""Gets the firewall_policy_contain_ipv6_composite_rules of this VpcQuotas.

        **参数解释**： 网络ACL中配置了IP地址组或不连续端口的IPv6规则数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The firewall_policy_contain_ipv6_composite_rules of this VpcQuotas.
        :rtype: int
        """
        return self._firewall_policy_contain_ipv6_composite_rules

    @firewall_policy_contain_ipv6_composite_rules.setter
    def firewall_policy_contain_ipv6_composite_rules(self, firewall_policy_contain_ipv6_composite_rules):
        r"""Sets the firewall_policy_contain_ipv6_composite_rules of this VpcQuotas.

        **参数解释**： 网络ACL中配置了IP地址组或不连续端口的IPv6规则数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param firewall_policy_contain_ipv6_composite_rules: The firewall_policy_contain_ipv6_composite_rules of this VpcQuotas.
        :type firewall_policy_contain_ipv6_composite_rules: int
        """
        self._firewall_policy_contain_ipv6_composite_rules = firewall_policy_contain_ipv6_composite_rules

    @property
    def forward_policy(self):
        r"""Gets the forward_policy of this VpcQuotas.

        **参数解释**： 云转发策略数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The forward_policy of this VpcQuotas.
        :rtype: int
        """
        return self._forward_policy

    @forward_policy.setter
    def forward_policy(self, forward_policy):
        r"""Sets the forward_policy of this VpcQuotas.

        **参数解释**： 云转发策略数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param forward_policy: The forward_policy of this VpcQuotas.
        :type forward_policy: int
        """
        self._forward_policy = forward_policy

    @property
    def forward_policy_contain_ports(self):
        r"""Gets the forward_policy_contain_ports of this VpcQuotas.

        **参数解释**： 云转发策略关联端口数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The forward_policy_contain_ports of this VpcQuotas.
        :rtype: int
        """
        return self._forward_policy_contain_ports

    @forward_policy_contain_ports.setter
    def forward_policy_contain_ports(self, forward_policy_contain_ports):
        r"""Sets the forward_policy_contain_ports of this VpcQuotas.

        **参数解释**： 云转发策略关联端口数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param forward_policy_contain_ports: The forward_policy_contain_ports of this VpcQuotas.
        :type forward_policy_contain_ports: int
        """
        self._forward_policy_contain_ports = forward_policy_contain_ports

    @property
    def forward_rule(self):
        r"""Gets the forward_rule of this VpcQuotas.

        **参数解释**： 云转发规则数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The forward_rule of this VpcQuotas.
        :rtype: int
        """
        return self._forward_rule

    @forward_rule.setter
    def forward_rule(self, forward_rule):
        r"""Sets the forward_rule of this VpcQuotas.

        **参数解释**： 云转发规则数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param forward_rule: The forward_rule of this VpcQuotas.
        :type forward_rule: int
        """
        self._forward_rule = forward_rule

    @property
    def peering(self):
        r"""Gets the peering of this VpcQuotas.

        **参数解释**： 对等连接数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The peering of this VpcQuotas.
        :rtype: int
        """
        return self._peering

    @peering.setter
    def peering(self, peering):
        r"""Sets the peering of this VpcQuotas.

        **参数解释**： 对等连接数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param peering: The peering of this VpcQuotas.
        :type peering: int
        """
        self._peering = peering

    @property
    def roce_cluster_contain_networks(self):
        r"""Gets the roce_cluster_contain_networks of this VpcQuotas.

        **参数解释**： 一个physical_network下支持创建的roce网络数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The roce_cluster_contain_networks of this VpcQuotas.
        :rtype: int
        """
        return self._roce_cluster_contain_networks

    @roce_cluster_contain_networks.setter
    def roce_cluster_contain_networks(self, roce_cluster_contain_networks):
        r"""Sets the roce_cluster_contain_networks of this VpcQuotas.

        **参数解释**： 一个physical_network下支持创建的roce网络数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param roce_cluster_contain_networks: The roce_cluster_contain_networks of this VpcQuotas.
        :type roce_cluster_contain_networks: int
        """
        self._roce_cluster_contain_networks = roce_cluster_contain_networks

    @property
    def rtb_allow_sys_cidr_routes(self):
        r"""Gets the rtb_allow_sys_cidr_routes of this VpcQuotas.

        **参数解释**： 路由表支持系统路由数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The rtb_allow_sys_cidr_routes of this VpcQuotas.
        :rtype: int
        """
        return self._rtb_allow_sys_cidr_routes

    @rtb_allow_sys_cidr_routes.setter
    def rtb_allow_sys_cidr_routes(self, rtb_allow_sys_cidr_routes):
        r"""Sets the rtb_allow_sys_cidr_routes of this VpcQuotas.

        **参数解释**： 路由表支持系统路由数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param rtb_allow_sys_cidr_routes: The rtb_allow_sys_cidr_routes of this VpcQuotas.
        :type rtb_allow_sys_cidr_routes: int
        """
        self._rtb_allow_sys_cidr_routes = rtb_allow_sys_cidr_routes

    @property
    def shared_bandwidth(self):
        r"""Gets the shared_bandwidth of this VpcQuotas.

        **参数解释**： 共享带宽组数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The shared_bandwidth of this VpcQuotas.
        :rtype: int
        """
        return self._shared_bandwidth

    @shared_bandwidth.setter
    def shared_bandwidth(self, shared_bandwidth):
        r"""Sets the shared_bandwidth of this VpcQuotas.

        **参数解释**： 共享带宽组数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param shared_bandwidth: The shared_bandwidth of this VpcQuotas.
        :type shared_bandwidth: int
        """
        self._shared_bandwidth = shared_bandwidth

    @property
    def shared_bandwidth_contain_publicip(self):
        r"""Gets the shared_bandwidth_contain_publicip of this VpcQuotas.

        **参数解释**： 单个共享带宽关联的弹性公网IP数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The shared_bandwidth_contain_publicip of this VpcQuotas.
        :rtype: int
        """
        return self._shared_bandwidth_contain_publicip

    @shared_bandwidth_contain_publicip.setter
    def shared_bandwidth_contain_publicip(self, shared_bandwidth_contain_publicip):
        r"""Sets the shared_bandwidth_contain_publicip of this VpcQuotas.

        **参数解释**： 单个共享带宽关联的弹性公网IP数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param shared_bandwidth_contain_publicip: The shared_bandwidth_contain_publicip of this VpcQuotas.
        :type shared_bandwidth_contain_publicip: int
        """
        self._shared_bandwidth_contain_publicip = shared_bandwidth_contain_publicip

    @property
    def secgroup_contain_rules(self):
        r"""Gets the secgroup_contain_rules of this VpcQuotas.

        **参数解释**： 单个安全组包含的规则数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The secgroup_contain_rules of this VpcQuotas.
        :rtype: int
        """
        return self._secgroup_contain_rules

    @secgroup_contain_rules.setter
    def secgroup_contain_rules(self, secgroup_contain_rules):
        r"""Sets the secgroup_contain_rules of this VpcQuotas.

        **参数解释**： 单个安全组包含的规则数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param secgroup_contain_rules: The secgroup_contain_rules of this VpcQuotas.
        :type secgroup_contain_rules: int
        """
        self._secgroup_contain_rules = secgroup_contain_rules

    @property
    def secgroup_referred_by_nic(self):
        r"""Gets the secgroup_referred_by_nic of this VpcQuotas.

        **参数解释**： 单个安全组关联的网卡数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The secgroup_referred_by_nic of this VpcQuotas.
        :rtype: int
        """
        return self._secgroup_referred_by_nic

    @secgroup_referred_by_nic.setter
    def secgroup_referred_by_nic(self, secgroup_referred_by_nic):
        r"""Sets the secgroup_referred_by_nic of this VpcQuotas.

        **参数解释**： 单个安全组关联的网卡数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param secgroup_referred_by_nic: The secgroup_referred_by_nic of this VpcQuotas.
        :type secgroup_referred_by_nic: int
        """
        self._secgroup_referred_by_nic = secgroup_referred_by_nic

    @property
    def security_group(self):
        r"""Gets the security_group of this VpcQuotas.

        **参数解释**： 安全组数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The security_group of this VpcQuotas.
        :rtype: int
        """
        return self._security_group

    @security_group.setter
    def security_group(self, security_group):
        r"""Sets the security_group of this VpcQuotas.

        **参数解释**： 安全组数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param security_group: The security_group of this VpcQuotas.
        :type security_group: int
        """
        self._security_group = security_group

    @property
    def security_group_contain_egress_ipv4_composite_rules(self):
        r"""Gets the security_group_contain_egress_ipv4_composite_rules of this VpcQuotas.

        **参数解释**： 安全组中配置了IP地址组、不连续端口或远端安全组的IPv4出方向规则数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The security_group_contain_egress_ipv4_composite_rules of this VpcQuotas.
        :rtype: int
        """
        return self._security_group_contain_egress_ipv4_composite_rules

    @security_group_contain_egress_ipv4_composite_rules.setter
    def security_group_contain_egress_ipv4_composite_rules(self, security_group_contain_egress_ipv4_composite_rules):
        r"""Sets the security_group_contain_egress_ipv4_composite_rules of this VpcQuotas.

        **参数解释**： 安全组中配置了IP地址组、不连续端口或远端安全组的IPv4出方向规则数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param security_group_contain_egress_ipv4_composite_rules: The security_group_contain_egress_ipv4_composite_rules of this VpcQuotas.
        :type security_group_contain_egress_ipv4_composite_rules: int
        """
        self._security_group_contain_egress_ipv4_composite_rules = security_group_contain_egress_ipv4_composite_rules

    @property
    def security_group_contain_egress_ipv6_composite_rules(self):
        r"""Gets the security_group_contain_egress_ipv6_composite_rules of this VpcQuotas.

        **参数解释**： 安全组中配置了IP地址组、不连续端口或远端安全组的IPv6出方向规则数配。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The security_group_contain_egress_ipv6_composite_rules of this VpcQuotas.
        :rtype: int
        """
        return self._security_group_contain_egress_ipv6_composite_rules

    @security_group_contain_egress_ipv6_composite_rules.setter
    def security_group_contain_egress_ipv6_composite_rules(self, security_group_contain_egress_ipv6_composite_rules):
        r"""Sets the security_group_contain_egress_ipv6_composite_rules of this VpcQuotas.

        **参数解释**： 安全组中配置了IP地址组、不连续端口或远端安全组的IPv6出方向规则数配。 **取值范围**： 整数，-1表示此配额未上线。

        :param security_group_contain_egress_ipv6_composite_rules: The security_group_contain_egress_ipv6_composite_rules of this VpcQuotas.
        :type security_group_contain_egress_ipv6_composite_rules: int
        """
        self._security_group_contain_egress_ipv6_composite_rules = security_group_contain_egress_ipv6_composite_rules

    @property
    def security_group_contain_ingress_ipv4_composite_rules(self):
        r"""Gets the security_group_contain_ingress_ipv4_composite_rules of this VpcQuotas.

        **参数解释**： 安全组中配置了IP地址组、不连续端口或远端安全组的IPv4入方向规则数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The security_group_contain_ingress_ipv4_composite_rules of this VpcQuotas.
        :rtype: int
        """
        return self._security_group_contain_ingress_ipv4_composite_rules

    @security_group_contain_ingress_ipv4_composite_rules.setter
    def security_group_contain_ingress_ipv4_composite_rules(self, security_group_contain_ingress_ipv4_composite_rules):
        r"""Sets the security_group_contain_ingress_ipv4_composite_rules of this VpcQuotas.

        **参数解释**： 安全组中配置了IP地址组、不连续端口或远端安全组的IPv4入方向规则数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param security_group_contain_ingress_ipv4_composite_rules: The security_group_contain_ingress_ipv4_composite_rules of this VpcQuotas.
        :type security_group_contain_ingress_ipv4_composite_rules: int
        """
        self._security_group_contain_ingress_ipv4_composite_rules = security_group_contain_ingress_ipv4_composite_rules

    @property
    def security_group_contain_ingress_ipv6_composite_rules(self):
        r"""Gets the security_group_contain_ingress_ipv6_composite_rules of this VpcQuotas.

        **参数解释**： 安全组中配置了IP地址组、不连续端口或远端安全组的IPv6入方向规则数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The security_group_contain_ingress_ipv6_composite_rules of this VpcQuotas.
        :rtype: int
        """
        return self._security_group_contain_ingress_ipv6_composite_rules

    @security_group_contain_ingress_ipv6_composite_rules.setter
    def security_group_contain_ingress_ipv6_composite_rules(self, security_group_contain_ingress_ipv6_composite_rules):
        r"""Sets the security_group_contain_ingress_ipv6_composite_rules of this VpcQuotas.

        **参数解释**： 安全组中配置了IP地址组、不连续端口或远端安全组的IPv6入方向规则数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param security_group_contain_ingress_ipv6_composite_rules: The security_group_contain_ingress_ipv6_composite_rules of this VpcQuotas.
        :type security_group_contain_ingress_ipv6_composite_rules: int
        """
        self._security_group_contain_ingress_ipv6_composite_rules = security_group_contain_ingress_ipv6_composite_rules

    @property
    def security_group_rule(self):
        r"""Gets the security_group_rule of this VpcQuotas.

        **参数解释**： 安全组规则数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The security_group_rule of this VpcQuotas.
        :rtype: int
        """
        return self._security_group_rule

    @security_group_rule.setter
    def security_group_rule(self, security_group_rule):
        r"""Sets the security_group_rule of this VpcQuotas.

        **参数解释**： 安全组规则数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param security_group_rule: The security_group_rule of this VpcQuotas.
        :type security_group_rule: int
        """
        self._security_group_rule = security_group_rule

    @property
    def subnet_contain_eni(self):
        r"""Gets the subnet_contain_eni of this VpcQuotas.

        **参数解释**： 单个子网包含的弹性网卡数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The subnet_contain_eni of this VpcQuotas.
        :rtype: int
        """
        return self._subnet_contain_eni

    @subnet_contain_eni.setter
    def subnet_contain_eni(self, subnet_contain_eni):
        r"""Sets the subnet_contain_eni of this VpcQuotas.

        **参数解释**： 单个子网包含的弹性网卡数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param subnet_contain_eni: The subnet_contain_eni of this VpcQuotas.
        :type subnet_contain_eni: int
        """
        self._subnet_contain_eni = subnet_contain_eni

    @property
    def traffic_mirror_filter(self):
        r"""Gets the traffic_mirror_filter of this VpcQuotas.

        **参数解释**： 流量镜像筛选条件数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The traffic_mirror_filter of this VpcQuotas.
        :rtype: int
        """
        return self._traffic_mirror_filter

    @traffic_mirror_filter.setter
    def traffic_mirror_filter(self, traffic_mirror_filter):
        r"""Sets the traffic_mirror_filter of this VpcQuotas.

        **参数解释**： 流量镜像筛选条件数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param traffic_mirror_filter: The traffic_mirror_filter of this VpcQuotas.
        :type traffic_mirror_filter: int
        """
        self._traffic_mirror_filter = traffic_mirror_filter

    @property
    def traffic_mirror_filter_referred_by_session(self):
        r"""Gets the traffic_mirror_filter_referred_by_session of this VpcQuotas.

        **参数解释**： 单个流量镜像筛选条件被镜像会话引用数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The traffic_mirror_filter_referred_by_session of this VpcQuotas.
        :rtype: int
        """
        return self._traffic_mirror_filter_referred_by_session

    @traffic_mirror_filter_referred_by_session.setter
    def traffic_mirror_filter_referred_by_session(self, traffic_mirror_filter_referred_by_session):
        r"""Sets the traffic_mirror_filter_referred_by_session of this VpcQuotas.

        **参数解释**： 单个流量镜像筛选条件被镜像会话引用数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param traffic_mirror_filter_referred_by_session: The traffic_mirror_filter_referred_by_session of this VpcQuotas.
        :type traffic_mirror_filter_referred_by_session: int
        """
        self._traffic_mirror_filter_referred_by_session = traffic_mirror_filter_referred_by_session

    @property
    def traffic_mirror_filter_contain_rules_each_direction(self):
        r"""Gets the traffic_mirror_filter_contain_rules_each_direction of this VpcQuotas.

        **参数解释**： 流量镜像筛选条件单方向规则数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The traffic_mirror_filter_contain_rules_each_direction of this VpcQuotas.
        :rtype: int
        """
        return self._traffic_mirror_filter_contain_rules_each_direction

    @traffic_mirror_filter_contain_rules_each_direction.setter
    def traffic_mirror_filter_contain_rules_each_direction(self, traffic_mirror_filter_contain_rules_each_direction):
        r"""Sets the traffic_mirror_filter_contain_rules_each_direction of this VpcQuotas.

        **参数解释**： 流量镜像筛选条件单方向规则数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param traffic_mirror_filter_contain_rules_each_direction: The traffic_mirror_filter_contain_rules_each_direction of this VpcQuotas.
        :type traffic_mirror_filter_contain_rules_each_direction: int
        """
        self._traffic_mirror_filter_contain_rules_each_direction = traffic_mirror_filter_contain_rules_each_direction

    @property
    def traffic_mirror_session(self):
        r"""Gets the traffic_mirror_session of this VpcQuotas.

        **参数解释**： 流量镜像会话数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The traffic_mirror_session of this VpcQuotas.
        :rtype: int
        """
        return self._traffic_mirror_session

    @traffic_mirror_session.setter
    def traffic_mirror_session(self, traffic_mirror_session):
        r"""Sets the traffic_mirror_session of this VpcQuotas.

        **参数解释**： 流量镜像会话数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param traffic_mirror_session: The traffic_mirror_session of this VpcQuotas.
        :type traffic_mirror_session: int
        """
        self._traffic_mirror_session = traffic_mirror_session

    @property
    def traffic_mirror_session_contain_sources(self):
        r"""Gets the traffic_mirror_session_contain_sources of this VpcQuotas.

        **参数解释**： 单个流量镜像会话关联的镜像源数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The traffic_mirror_session_contain_sources of this VpcQuotas.
        :rtype: int
        """
        return self._traffic_mirror_session_contain_sources

    @traffic_mirror_session_contain_sources.setter
    def traffic_mirror_session_contain_sources(self, traffic_mirror_session_contain_sources):
        r"""Sets the traffic_mirror_session_contain_sources of this VpcQuotas.

        **参数解释**： 单个流量镜像会话关联的镜像源数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param traffic_mirror_session_contain_sources: The traffic_mirror_session_contain_sources of this VpcQuotas.
        :type traffic_mirror_session_contain_sources: int
        """
        self._traffic_mirror_session_contain_sources = traffic_mirror_session_contain_sources

    @property
    def traffic_mirror_source_referred_by_session(self):
        r"""Gets the traffic_mirror_source_referred_by_session of this VpcQuotas.

        **参数解释**： 单个镜像源被流量镜像会话引用次数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The traffic_mirror_source_referred_by_session of this VpcQuotas.
        :rtype: int
        """
        return self._traffic_mirror_source_referred_by_session

    @traffic_mirror_source_referred_by_session.setter
    def traffic_mirror_source_referred_by_session(self, traffic_mirror_source_referred_by_session):
        r"""Sets the traffic_mirror_source_referred_by_session of this VpcQuotas.

        **参数解释**： 单个镜像源被流量镜像会话引用次数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param traffic_mirror_source_referred_by_session: The traffic_mirror_source_referred_by_session of this VpcQuotas.
        :type traffic_mirror_source_referred_by_session: int
        """
        self._traffic_mirror_source_referred_by_session = traffic_mirror_source_referred_by_session

    @property
    def traffic_mirror_target_elb_referred_by_session(self):
        r"""Gets the traffic_mirror_target_elb_referred_by_session of this VpcQuotas.

        **参数解释**： 私网弹性负载均衡类型的镜像目的被会话引用次数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The traffic_mirror_target_elb_referred_by_session of this VpcQuotas.
        :rtype: int
        """
        return self._traffic_mirror_target_elb_referred_by_session

    @traffic_mirror_target_elb_referred_by_session.setter
    def traffic_mirror_target_elb_referred_by_session(self, traffic_mirror_target_elb_referred_by_session):
        r"""Sets the traffic_mirror_target_elb_referred_by_session of this VpcQuotas.

        **参数解释**： 私网弹性负载均衡类型的镜像目的被会话引用次数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param traffic_mirror_target_elb_referred_by_session: The traffic_mirror_target_elb_referred_by_session of this VpcQuotas.
        :type traffic_mirror_target_elb_referred_by_session: int
        """
        self._traffic_mirror_target_elb_referred_by_session = traffic_mirror_target_elb_referred_by_session

    @property
    def traffic_mirror_target_eni_referred_by_session(self):
        r"""Gets the traffic_mirror_target_eni_referred_by_session of this VpcQuotas.

        **参数解释**： 弹性网卡类型的镜像目的被会话引用次数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The traffic_mirror_target_eni_referred_by_session of this VpcQuotas.
        :rtype: int
        """
        return self._traffic_mirror_target_eni_referred_by_session

    @traffic_mirror_target_eni_referred_by_session.setter
    def traffic_mirror_target_eni_referred_by_session(self, traffic_mirror_target_eni_referred_by_session):
        r"""Sets the traffic_mirror_target_eni_referred_by_session of this VpcQuotas.

        **参数解释**： 弹性网卡类型的镜像目的被会话引用次数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param traffic_mirror_target_eni_referred_by_session: The traffic_mirror_target_eni_referred_by_session of this VpcQuotas.
        :type traffic_mirror_target_eni_referred_by_session: int
        """
        self._traffic_mirror_target_eni_referred_by_session = traffic_mirror_target_eni_referred_by_session

    @property
    def vip(self):
        r"""Gets the vip of this VpcQuotas.

        **参数解释**： 虚拟IP数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The vip of this VpcQuotas.
        :rtype: int
        """
        return self._vip

    @vip.setter
    def vip(self, vip):
        r"""Sets the vip of this VpcQuotas.

        **参数解释**： 虚拟IP数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param vip: The vip of this VpcQuotas.
        :type vip: int
        """
        self._vip = vip

    @property
    def virsubnet(self):
        r"""Gets the virsubnet of this VpcQuotas.

        **参数解释**： 子网数配额。 **取值范围**： 整数，-1表示此配额未上线，请通过[v1查询配额接口](vpc_quota_0001.xml)。

        :return: The virsubnet of this VpcQuotas.
        :rtype: int
        """
        return self._virsubnet

    @virsubnet.setter
    def virsubnet(self, virsubnet):
        r"""Sets the virsubnet of this VpcQuotas.

        **参数解释**： 子网数配额。 **取值范围**： 整数，-1表示此配额未上线，请通过[v1查询配额接口](vpc_quota_0001.xml)。

        :param virsubnet: The virsubnet of this VpcQuotas.
        :type virsubnet: int
        """
        self._virsubnet = virsubnet

    @property
    def virsubnet_contain_ipv4_cidr_reservations(self):
        r"""Gets the virsubnet_contain_ipv4_cidr_reservations of this VpcQuotas.

        **参数解释**： 单子网包含IPv4子网预留网段数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The virsubnet_contain_ipv4_cidr_reservations of this VpcQuotas.
        :rtype: int
        """
        return self._virsubnet_contain_ipv4_cidr_reservations

    @virsubnet_contain_ipv4_cidr_reservations.setter
    def virsubnet_contain_ipv4_cidr_reservations(self, virsubnet_contain_ipv4_cidr_reservations):
        r"""Sets the virsubnet_contain_ipv4_cidr_reservations of this VpcQuotas.

        **参数解释**： 单子网包含IPv4子网预留网段数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param virsubnet_contain_ipv4_cidr_reservations: The virsubnet_contain_ipv4_cidr_reservations of this VpcQuotas.
        :type virsubnet_contain_ipv4_cidr_reservations: int
        """
        self._virsubnet_contain_ipv4_cidr_reservations = virsubnet_contain_ipv4_cidr_reservations

    @property
    def virsubnet_contain_ipv6_cidr_reservations(self):
        r"""Gets the virsubnet_contain_ipv6_cidr_reservations of this VpcQuotas.

        **参数解释**： 单子网包含IPv6子网预留网段数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The virsubnet_contain_ipv6_cidr_reservations of this VpcQuotas.
        :rtype: int
        """
        return self._virsubnet_contain_ipv6_cidr_reservations

    @virsubnet_contain_ipv6_cidr_reservations.setter
    def virsubnet_contain_ipv6_cidr_reservations(self, virsubnet_contain_ipv6_cidr_reservations):
        r"""Sets the virsubnet_contain_ipv6_cidr_reservations of this VpcQuotas.

        **参数解释**： 单子网包含IPv6子网预留网段数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param virsubnet_contain_ipv6_cidr_reservations: The virsubnet_contain_ipv6_cidr_reservations of this VpcQuotas.
        :type virsubnet_contain_ipv6_cidr_reservations: int
        """
        self._virsubnet_contain_ipv6_cidr_reservations = virsubnet_contain_ipv6_cidr_reservations

    @property
    def vpc(self):
        r"""Gets the vpc of this VpcQuotas.

        **参数解释**： VPC数配额。 **取值范围**： 整数，-1表示此配额未上线，请通过[v1查询配额接口](vpc_quota_0001.xml)。

        :return: The vpc of this VpcQuotas.
        :rtype: int
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        r"""Sets the vpc of this VpcQuotas.

        **参数解释**： VPC数配额。 **取值范围**： 整数，-1表示此配额未上线，请通过[v1查询配额接口](vpc_quota_0001.xml)。

        :param vpc: The vpc of this VpcQuotas.
        :type vpc: int
        """
        self._vpc = vpc

    @property
    def vpc_contain_eni(self):
        r"""Gets the vpc_contain_eni of this VpcQuotas.

        **参数解释**： 单个VPC包含弹性网卡数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The vpc_contain_eni of this VpcQuotas.
        :rtype: int
        """
        return self._vpc_contain_eni

    @vpc_contain_eni.setter
    def vpc_contain_eni(self, vpc_contain_eni):
        r"""Sets the vpc_contain_eni of this VpcQuotas.

        **参数解释**： 单个VPC包含弹性网卡数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param vpc_contain_eni: The vpc_contain_eni of this VpcQuotas.
        :type vpc_contain_eni: int
        """
        self._vpc_contain_eni = vpc_contain_eni

    @property
    def vpc_contain_vip(self):
        r"""Gets the vpc_contain_vip of this VpcQuotas.

        **参数解释**： 单个VPC包含虚拟IP数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The vpc_contain_vip of this VpcQuotas.
        :rtype: int
        """
        return self._vpc_contain_vip

    @vpc_contain_vip.setter
    def vpc_contain_vip(self, vpc_contain_vip):
        r"""Sets the vpc_contain_vip of this VpcQuotas.

        **参数解释**： 单个VPC包含虚拟IP数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param vpc_contain_vip: The vpc_contain_vip of this VpcQuotas.
        :type vpc_contain_vip: int
        """
        self._vpc_contain_vip = vpc_contain_vip

    @property
    def vpc_contain_virsubnet(self):
        r"""Gets the vpc_contain_virsubnet of this VpcQuotas.

        **参数解释**： 单个VPC包含子网数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :return: The vpc_contain_virsubnet of this VpcQuotas.
        :rtype: int
        """
        return self._vpc_contain_virsubnet

    @vpc_contain_virsubnet.setter
    def vpc_contain_virsubnet(self, vpc_contain_virsubnet):
        r"""Sets the vpc_contain_virsubnet of this VpcQuotas.

        **参数解释**： 单个VPC包含子网数配额。 **取值范围**： 整数，-1表示此配额未上线。

        :param vpc_contain_virsubnet: The vpc_contain_virsubnet of this VpcQuotas.
        :type vpc_contain_virsubnet: int
        """
        self._vpc_contain_virsubnet = vpc_contain_virsubnet

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
        if not isinstance(other, VpcQuotas):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
