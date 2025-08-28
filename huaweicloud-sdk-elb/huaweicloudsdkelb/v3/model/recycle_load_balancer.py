# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecycleLoadBalancer:

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
        'auto_terminate_time': 'str',
        'description': 'str',
        'provisioning_status': 'str',
        'admin_state_up': 'bool',
        'provider': 'str',
        'pools': 'list[PoolRef]',
        'listeners': 'list[ListenerRef]',
        'operating_status': 'str',
        'name': 'str',
        'project_id': 'str',
        'vip_subnet_cidr_id': 'str',
        'vip_address': 'str',
        'vip_port_id': 'str',
        'tags': 'list[Tag]',
        'created_at': 'str',
        'updated_at': 'str',
        'guaranteed': 'bool',
        'vpc_id': 'str',
        'eips': 'list[EipInfo]',
        'ipv6_vip_address': 'str',
        'ipv6_vip_virsubnet_id': 'str',
        'ipv6_vip_port_id': 'str',
        'availability_zone_list': 'list[str]',
        'enterprise_project_id': 'str',
        'billing_info': 'str',
        'l4_flavor_id': 'str',
        'l4_scale_flavor_id': 'str',
        'l7_flavor_id': 'str',
        'l7_scale_flavor_id': 'str',
        'publicips': 'list[PublicIpInfo]',
        'global_eips': 'list[GlobalEipInfo]',
        'elb_virsubnet_ids': 'list[str]',
        'elb_virsubnet_type': 'str',
        'ip_target_enable': 'bool',
        'frozen_scene': 'str',
        'ipv6_bandwidth': 'BandwidthRef',
        'deletion_protection_enable': 'bool',
        'autoscaling': 'AutoscalingRef',
        'public_border_group': 'str',
        'charge_mode': 'str',
        'waf_failure_action': 'str',
        'protection_status': 'str',
        'protection_reason': 'str',
        'log_group_id': 'str',
        'log_topic_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'auto_terminate_time': 'auto_terminate_time',
        'description': 'description',
        'provisioning_status': 'provisioning_status',
        'admin_state_up': 'admin_state_up',
        'provider': 'provider',
        'pools': 'pools',
        'listeners': 'listeners',
        'operating_status': 'operating_status',
        'name': 'name',
        'project_id': 'project_id',
        'vip_subnet_cidr_id': 'vip_subnet_cidr_id',
        'vip_address': 'vip_address',
        'vip_port_id': 'vip_port_id',
        'tags': 'tags',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'guaranteed': 'guaranteed',
        'vpc_id': 'vpc_id',
        'eips': 'eips',
        'ipv6_vip_address': 'ipv6_vip_address',
        'ipv6_vip_virsubnet_id': 'ipv6_vip_virsubnet_id',
        'ipv6_vip_port_id': 'ipv6_vip_port_id',
        'availability_zone_list': 'availability_zone_list',
        'enterprise_project_id': 'enterprise_project_id',
        'billing_info': 'billing_info',
        'l4_flavor_id': 'l4_flavor_id',
        'l4_scale_flavor_id': 'l4_scale_flavor_id',
        'l7_flavor_id': 'l7_flavor_id',
        'l7_scale_flavor_id': 'l7_scale_flavor_id',
        'publicips': 'publicips',
        'global_eips': 'global_eips',
        'elb_virsubnet_ids': 'elb_virsubnet_ids',
        'elb_virsubnet_type': 'elb_virsubnet_type',
        'ip_target_enable': 'ip_target_enable',
        'frozen_scene': 'frozen_scene',
        'ipv6_bandwidth': 'ipv6_bandwidth',
        'deletion_protection_enable': 'deletion_protection_enable',
        'autoscaling': 'autoscaling',
        'public_border_group': 'public_border_group',
        'charge_mode': 'charge_mode',
        'waf_failure_action': 'waf_failure_action',
        'protection_status': 'protection_status',
        'protection_reason': 'protection_reason',
        'log_group_id': 'log_group_id',
        'log_topic_id': 'log_topic_id'
    }

    def __init__(self, id=None, auto_terminate_time=None, description=None, provisioning_status=None, admin_state_up=None, provider=None, pools=None, listeners=None, operating_status=None, name=None, project_id=None, vip_subnet_cidr_id=None, vip_address=None, vip_port_id=None, tags=None, created_at=None, updated_at=None, guaranteed=None, vpc_id=None, eips=None, ipv6_vip_address=None, ipv6_vip_virsubnet_id=None, ipv6_vip_port_id=None, availability_zone_list=None, enterprise_project_id=None, billing_info=None, l4_flavor_id=None, l4_scale_flavor_id=None, l7_flavor_id=None, l7_scale_flavor_id=None, publicips=None, global_eips=None, elb_virsubnet_ids=None, elb_virsubnet_type=None, ip_target_enable=None, frozen_scene=None, ipv6_bandwidth=None, deletion_protection_enable=None, autoscaling=None, public_border_group=None, charge_mode=None, waf_failure_action=None, protection_status=None, protection_reason=None, log_group_id=None, log_topic_id=None):
        r"""RecycleLoadBalancer

        The model defined in huaweicloud sdk

        :param id: **参数解释**：负载均衡器ID。  **取值范围**：不涉及
        :type id: str
        :param auto_terminate_time: **参数解释**：回收站elb的自动到期销毁时间。格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;  **取值范围**：不涉及
        :type auto_terminate_time: str
        :param description: **参数解释**：负载均衡器描述信息。  **取值范围**：不涉及
        :type description: str
        :param provisioning_status: **参数解释**：负载均衡器的配置状态。  **取值范围**： - RECYCLING：处于回收站用中。
        :type provisioning_status: str
        :param admin_state_up: **参数解释**：负载均衡器的启用状态。  **取值范围**： - true ：启用。 - false：停用。  [不支持该字段，请勿使用。](tag:dt)
        :type admin_state_up: bool
        :param provider: **参数解释**：负载均衡器的生产者名称。固定为vlb。  **取值范围**：不涉及
        :type provider: str
        :param pools: **参数解释**：负载均衡器直接关联的后端服务器组的ID列表。
        :type pools: list[:class:`huaweicloudsdkelb.v3.PoolRef`]
        :param listeners: **参数解释**：负载均衡器关联的监听器的ID列表。
        :type listeners: list[:class:`huaweicloudsdkelb.v3.ListenerRef`]
        :param operating_status: **参数解释**：负载均衡器的操作状态。  **取值范围**： - ONLINE：在线。 - FROZEN：已冻结。
        :type operating_status: str
        :param name: **参数解释**：负载均衡器的名称。  **取值范围**：不涉及
        :type name: str
        :param project_id: **参数解释**：负载均衡器所属的项目ID。  **取值范围**：不涉及
        :type project_id: str
        :param vip_subnet_cidr_id: **参数解释**：负载均衡器所在子网的IPv4子网ID，也称为该负载均衡器实例的前端子网。  **取值范围**：不涉及
        :type vip_subnet_cidr_id: str
        :param vip_address: **参数解释**：负载均衡器的IPv4私网IP地址。  **取值范围**：不涉及
        :type vip_address: str
        :param vip_port_id: **参数解释**：负载均衡器的IPv4对应的port ID。 [创建弹性负载均衡时，会自动为负载均衡创建一个port并关联一个默认的安全组，这个安全组对所有流量不生效。 ](tag:dt,hcso_dt)  **取值范围**：不涉及
        :type vip_port_id: str
        :param tags: **参数解释**：负载均衡的标签列表。
        :type tags: list[:class:`huaweicloudsdkelb.v3.Tag`]
        :param created_at: **参数解释**：负载均衡器的创建时间。  **取值范围**： 格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;
        :type created_at: str
        :param updated_at: **参数解释**：负载均衡器的更新时间。  **取值范围**： 格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;
        :type updated_at: str
        :param guaranteed: **参数解释**：是否独享型LB。  **取值范围**： - false：共享型。 - true：独享型。
        :type guaranteed: bool
        :param vpc_id: **参数解释**：负载均衡器所在VPC ID。  **取值范围**：不涉及
        :type vpc_id: str
        :param eips: **参数解释**：负载均衡器绑定的EIP。 注：该字段与publicips一致。
        :type eips: list[:class:`huaweicloudsdkelb.v3.EipInfo`]
        :param ipv6_vip_address: **参数解释**：双栈类型负载均衡器的IPv6地址。  **取值范围**：不涉及  [不支持IPv6，请勿使用。](tag:dt)
        :type ipv6_vip_address: str
        :param ipv6_vip_virsubnet_id: **参数解释**：双栈类型负载均衡器所在子网的IPv6网络ID，也称为该负载均衡器实例的前端子网。  **取值范围**：不涉及  [不支持IPv6，请勿使用。](tag:dt)
        :type ipv6_vip_virsubnet_id: str
        :param ipv6_vip_port_id: **参数解释**：双栈类型负载均衡器的IPv6对应的port ID。  **取值范围**：不涉及  [不支持IPv6，请勿使用。](tag:dt)
        :type ipv6_vip_port_id: str
        :param availability_zone_list: **参数解释**：负载均衡器所在的可用区列表。  **取值范围**：不涉及
        :type availability_zone_list: list[str]
        :param enterprise_project_id: **参数解释**：资源所属的企业项目ID。  **取值范围**： - \&quot;0\&quot;：表示资源属于default企业项目。 - UUID格式的字符串，表示非默认企业项目。  [不支持该字段，请勿使用。](tag:dt,hcso_dt)
        :type enterprise_project_id: str
        :param billing_info: **参数解释**：资源账单信息。  **取值范围**： - 空：按需计费。 [- 非空：包周期计费，  包周期计费billing_info字段的格式为：order_id:product_id:region_id:project_id，如： CS2107161019CDJZZ:OFFI569702121789763584:az:057ef081eb00d2732fd1c01a9be75e6f  不支持该字段，请勿使用](tag:hws_eu,g42,hk_g42,dt,hcso_dt,hcso,hk_vdf,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b)
        :type billing_info: str
        :param l4_flavor_id: **参数解释**：网络型规格ID。 对于弹性扩缩容实例，表示上限规格。  **取值范围**：不涉及 [hsco场景下所有LB实例共享带宽，该字段无效，请勿使用。](tag:hcso,hk_vdf,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b)
        :type l4_flavor_id: str
        :param l4_scale_flavor_id: **参数解释**：四层弹性Flavor ID。  **取值范围**：不涉及  不支持该字段，请勿使用。
        :type l4_scale_flavor_id: str
        :param l7_flavor_id: **参数解释**：应用型ID。 对于弹性扩缩容实例，表示上限规格ID。  **取值范围**：不涉及  [hsco场景下所有LB实例共享带宽，该字段无效，请勿使用。](tag:hcso,hk_vdf,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b)
        :type l7_flavor_id: str
        :param l7_scale_flavor_id: **参数解释**：七层弹性Flavor ID。  **取值范围**：不涉及  不支持该字段，请勿使用。
        :type l7_scale_flavor_id: str
        :param publicips: **参数解释**：负载均衡器绑定的公网IP。只支持绑定一个公网IP。  注：该字段与eips一致。
        :type publicips: list[:class:`huaweicloudsdkelb.v3.PublicIpInfo`]
        :param global_eips: **参数解释**：负载均衡器绑定的global eip。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42,dt,hcso_dt,hk_vdf,fcs,ctc,ocb,hws_ocb)
        :type global_eips: list[:class:`huaweicloudsdkelb.v3.GlobalEipInfo`]
        :param elb_virsubnet_ids: **参数解释**：下联面子网的网络ID列表。  **取值范围**：不涉及
        :type elb_virsubnet_ids: list[str]
        :param elb_virsubnet_type: **参数解释**：下联面子网类型。  **取值范围**： - ipv4：ipv4 - dualstack：双栈
        :type elb_virsubnet_type: str
        :param ip_target_enable: **参数解释**：是否启用IP类型后端转发。 [开启IP类型后端转发后，后端服务器组不仅支持添加云上VPC内的服务器，还支持添加其他VPC、其他公有云、云下数据中心的服务器。](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,dt,hcso_dt,hws_eu) [开启IP类型后端转发后，后端服务器组不仅支持添加云上VPC内的服务器，还支持添加其他VPC、云下数据中心的服务器。](tag:fcs)  **取值范围**： - true：开启。 - false：不开启。  [荷兰region不支持该字段，请勿使用。](tag:dt)
        :type ip_target_enable: bool
        :param frozen_scene: **参数解释**：负载均衡器的冻结场景。 [若负载均衡器有多个冻结场景，用逗号分隔。  **取值范围**： - POLICE：公安冻结场景。 - ILLEGAL：违规冻结场景。 - VERIFY：客户未实名认证冻结场景。 - PARTNER：合作伙伴冻结（合作伙伴冻结子客户资源）。 - AREAR：欠费冻结场景。](tag:hws,hws_hk)  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42,dt,hcso_dt,ocb,hws_ocb)
        :type frozen_scene: str
        :param ipv6_bandwidth: 
        :type ipv6_bandwidth: :class:`huaweicloudsdkelb.v3.BandwidthRef`
        :param deletion_protection_enable: **参数解释**：是否开启删除保护。  **取值范围**： - false：不开启。 - true：开启。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)  [荷兰region不支持该字段，请勿使用。](tag:dt)
        :type deletion_protection_enable: bool
        :param autoscaling: 
        :type autoscaling: :class:`huaweicloudsdkelb.v3.AutoscalingRef`
        :param public_border_group: **参数解释**：LB所属AZ组。  **取值范围**：不涉及
        :type public_border_group: str
        :param charge_mode: **参数解释**：负载均衡器实例的计费模式。  **取值范围**： - flavor：按规格计费 - lcu：按使用量计费 - 空值：若是共享型表示免费实例。若是独享型则与flavor模式一致，都是按规格计费。
        :type charge_mode: str
        :param waf_failure_action: **参数解释**：WAF故障时的流量处理策略。  **取值范围**：discard:丢弃，forward: 转发到后端。  [不支持该字段，请勿使用。](tag:hws_eu,hws_test,hcs,hcs_sm,hcso,hk_vdf,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b,hcso_dt,dt,ocb,ctc,cmcc,tm,ct,sbc,g42,hws_ocb,hk_sbc,hk_tm,hk_g42)
        :type waf_failure_action: str
        :param protection_status: **参数解释**：修改保护状态。  **取值范围**： - nonProtection: 不保护。 - consoleProtection: 控制台修改保护。
        :type protection_status: str
        :param protection_reason: **参数解释**：设置保护的原因。作为protection_status的转态设置的原因。  **取值范围**：除&lt;和&gt;外通用Unicode字符集字符，最大255个字符。
        :type protection_reason: str
        :param log_group_id: **参数解释**：LB所绑定的logtank对应的group id。  **取值范围**：不涉及
        :type log_group_id: str
        :param log_topic_id: **参数解释**：LB所绑定的logtank对应的topic id。  **取值范围**：不涉及
        :type log_topic_id: str
        """
        
        

        self._id = None
        self._auto_terminate_time = None
        self._description = None
        self._provisioning_status = None
        self._admin_state_up = None
        self._provider = None
        self._pools = None
        self._listeners = None
        self._operating_status = None
        self._name = None
        self._project_id = None
        self._vip_subnet_cidr_id = None
        self._vip_address = None
        self._vip_port_id = None
        self._tags = None
        self._created_at = None
        self._updated_at = None
        self._guaranteed = None
        self._vpc_id = None
        self._eips = None
        self._ipv6_vip_address = None
        self._ipv6_vip_virsubnet_id = None
        self._ipv6_vip_port_id = None
        self._availability_zone_list = None
        self._enterprise_project_id = None
        self._billing_info = None
        self._l4_flavor_id = None
        self._l4_scale_flavor_id = None
        self._l7_flavor_id = None
        self._l7_scale_flavor_id = None
        self._publicips = None
        self._global_eips = None
        self._elb_virsubnet_ids = None
        self._elb_virsubnet_type = None
        self._ip_target_enable = None
        self._frozen_scene = None
        self._ipv6_bandwidth = None
        self._deletion_protection_enable = None
        self._autoscaling = None
        self._public_border_group = None
        self._charge_mode = None
        self._waf_failure_action = None
        self._protection_status = None
        self._protection_reason = None
        self._log_group_id = None
        self._log_topic_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if auto_terminate_time is not None:
            self.auto_terminate_time = auto_terminate_time
        if description is not None:
            self.description = description
        if provisioning_status is not None:
            self.provisioning_status = provisioning_status
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if provider is not None:
            self.provider = provider
        if pools is not None:
            self.pools = pools
        if listeners is not None:
            self.listeners = listeners
        if operating_status is not None:
            self.operating_status = operating_status
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if vip_subnet_cidr_id is not None:
            self.vip_subnet_cidr_id = vip_subnet_cidr_id
        if vip_address is not None:
            self.vip_address = vip_address
        if vip_port_id is not None:
            self.vip_port_id = vip_port_id
        if tags is not None:
            self.tags = tags
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if guaranteed is not None:
            self.guaranteed = guaranteed
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if eips is not None:
            self.eips = eips
        if ipv6_vip_address is not None:
            self.ipv6_vip_address = ipv6_vip_address
        if ipv6_vip_virsubnet_id is not None:
            self.ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id
        if ipv6_vip_port_id is not None:
            self.ipv6_vip_port_id = ipv6_vip_port_id
        if availability_zone_list is not None:
            self.availability_zone_list = availability_zone_list
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if billing_info is not None:
            self.billing_info = billing_info
        if l4_flavor_id is not None:
            self.l4_flavor_id = l4_flavor_id
        if l4_scale_flavor_id is not None:
            self.l4_scale_flavor_id = l4_scale_flavor_id
        if l7_flavor_id is not None:
            self.l7_flavor_id = l7_flavor_id
        if l7_scale_flavor_id is not None:
            self.l7_scale_flavor_id = l7_scale_flavor_id
        if publicips is not None:
            self.publicips = publicips
        if global_eips is not None:
            self.global_eips = global_eips
        if elb_virsubnet_ids is not None:
            self.elb_virsubnet_ids = elb_virsubnet_ids
        if elb_virsubnet_type is not None:
            self.elb_virsubnet_type = elb_virsubnet_type
        if ip_target_enable is not None:
            self.ip_target_enable = ip_target_enable
        if frozen_scene is not None:
            self.frozen_scene = frozen_scene
        if ipv6_bandwidth is not None:
            self.ipv6_bandwidth = ipv6_bandwidth
        if deletion_protection_enable is not None:
            self.deletion_protection_enable = deletion_protection_enable
        if autoscaling is not None:
            self.autoscaling = autoscaling
        if public_border_group is not None:
            self.public_border_group = public_border_group
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if waf_failure_action is not None:
            self.waf_failure_action = waf_failure_action
        if protection_status is not None:
            self.protection_status = protection_status
        if protection_reason is not None:
            self.protection_reason = protection_reason
        if log_group_id is not None:
            self.log_group_id = log_group_id
        if log_topic_id is not None:
            self.log_topic_id = log_topic_id

    @property
    def id(self):
        r"""Gets the id of this RecycleLoadBalancer.

        **参数解释**：负载均衡器ID。  **取值范围**：不涉及

        :return: The id of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RecycleLoadBalancer.

        **参数解释**：负载均衡器ID。  **取值范围**：不涉及

        :param id: The id of this RecycleLoadBalancer.
        :type id: str
        """
        self._id = id

    @property
    def auto_terminate_time(self):
        r"""Gets the auto_terminate_time of this RecycleLoadBalancer.

        **参数解释**：回收站elb的自动到期销毁时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'  **取值范围**：不涉及

        :return: The auto_terminate_time of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._auto_terminate_time

    @auto_terminate_time.setter
    def auto_terminate_time(self, auto_terminate_time):
        r"""Sets the auto_terminate_time of this RecycleLoadBalancer.

        **参数解释**：回收站elb的自动到期销毁时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'  **取值范围**：不涉及

        :param auto_terminate_time: The auto_terminate_time of this RecycleLoadBalancer.
        :type auto_terminate_time: str
        """
        self._auto_terminate_time = auto_terminate_time

    @property
    def description(self):
        r"""Gets the description of this RecycleLoadBalancer.

        **参数解释**：负载均衡器描述信息。  **取值范围**：不涉及

        :return: The description of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RecycleLoadBalancer.

        **参数解释**：负载均衡器描述信息。  **取值范围**：不涉及

        :param description: The description of this RecycleLoadBalancer.
        :type description: str
        """
        self._description = description

    @property
    def provisioning_status(self):
        r"""Gets the provisioning_status of this RecycleLoadBalancer.

        **参数解释**：负载均衡器的配置状态。  **取值范围**： - RECYCLING：处于回收站用中。

        :return: The provisioning_status of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        r"""Sets the provisioning_status of this RecycleLoadBalancer.

        **参数解释**：负载均衡器的配置状态。  **取值范围**： - RECYCLING：处于回收站用中。

        :param provisioning_status: The provisioning_status of this RecycleLoadBalancer.
        :type provisioning_status: str
        """
        self._provisioning_status = provisioning_status

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this RecycleLoadBalancer.

        **参数解释**：负载均衡器的启用状态。  **取值范围**： - true ：启用。 - false：停用。  [不支持该字段，请勿使用。](tag:dt)

        :return: The admin_state_up of this RecycleLoadBalancer.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this RecycleLoadBalancer.

        **参数解释**：负载均衡器的启用状态。  **取值范围**： - true ：启用。 - false：停用。  [不支持该字段，请勿使用。](tag:dt)

        :param admin_state_up: The admin_state_up of this RecycleLoadBalancer.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def provider(self):
        r"""Gets the provider of this RecycleLoadBalancer.

        **参数解释**：负载均衡器的生产者名称。固定为vlb。  **取值范围**：不涉及

        :return: The provider of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this RecycleLoadBalancer.

        **参数解释**：负载均衡器的生产者名称。固定为vlb。  **取值范围**：不涉及

        :param provider: The provider of this RecycleLoadBalancer.
        :type provider: str
        """
        self._provider = provider

    @property
    def pools(self):
        r"""Gets the pools of this RecycleLoadBalancer.

        **参数解释**：负载均衡器直接关联的后端服务器组的ID列表。

        :return: The pools of this RecycleLoadBalancer.
        :rtype: list[:class:`huaweicloudsdkelb.v3.PoolRef`]
        """
        return self._pools

    @pools.setter
    def pools(self, pools):
        r"""Sets the pools of this RecycleLoadBalancer.

        **参数解释**：负载均衡器直接关联的后端服务器组的ID列表。

        :param pools: The pools of this RecycleLoadBalancer.
        :type pools: list[:class:`huaweicloudsdkelb.v3.PoolRef`]
        """
        self._pools = pools

    @property
    def listeners(self):
        r"""Gets the listeners of this RecycleLoadBalancer.

        **参数解释**：负载均衡器关联的监听器的ID列表。

        :return: The listeners of this RecycleLoadBalancer.
        :rtype: list[:class:`huaweicloudsdkelb.v3.ListenerRef`]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        r"""Sets the listeners of this RecycleLoadBalancer.

        **参数解释**：负载均衡器关联的监听器的ID列表。

        :param listeners: The listeners of this RecycleLoadBalancer.
        :type listeners: list[:class:`huaweicloudsdkelb.v3.ListenerRef`]
        """
        self._listeners = listeners

    @property
    def operating_status(self):
        r"""Gets the operating_status of this RecycleLoadBalancer.

        **参数解释**：负载均衡器的操作状态。  **取值范围**： - ONLINE：在线。 - FROZEN：已冻结。

        :return: The operating_status of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        r"""Sets the operating_status of this RecycleLoadBalancer.

        **参数解释**：负载均衡器的操作状态。  **取值范围**： - ONLINE：在线。 - FROZEN：已冻结。

        :param operating_status: The operating_status of this RecycleLoadBalancer.
        :type operating_status: str
        """
        self._operating_status = operating_status

    @property
    def name(self):
        r"""Gets the name of this RecycleLoadBalancer.

        **参数解释**：负载均衡器的名称。  **取值范围**：不涉及

        :return: The name of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RecycleLoadBalancer.

        **参数解释**：负载均衡器的名称。  **取值范围**：不涉及

        :param name: The name of this RecycleLoadBalancer.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this RecycleLoadBalancer.

        **参数解释**：负载均衡器所属的项目ID。  **取值范围**：不涉及

        :return: The project_id of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this RecycleLoadBalancer.

        **参数解释**：负载均衡器所属的项目ID。  **取值范围**：不涉及

        :param project_id: The project_id of this RecycleLoadBalancer.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def vip_subnet_cidr_id(self):
        r"""Gets the vip_subnet_cidr_id of this RecycleLoadBalancer.

        **参数解释**：负载均衡器所在子网的IPv4子网ID，也称为该负载均衡器实例的前端子网。  **取值范围**：不涉及

        :return: The vip_subnet_cidr_id of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._vip_subnet_cidr_id

    @vip_subnet_cidr_id.setter
    def vip_subnet_cidr_id(self, vip_subnet_cidr_id):
        r"""Sets the vip_subnet_cidr_id of this RecycleLoadBalancer.

        **参数解释**：负载均衡器所在子网的IPv4子网ID，也称为该负载均衡器实例的前端子网。  **取值范围**：不涉及

        :param vip_subnet_cidr_id: The vip_subnet_cidr_id of this RecycleLoadBalancer.
        :type vip_subnet_cidr_id: str
        """
        self._vip_subnet_cidr_id = vip_subnet_cidr_id

    @property
    def vip_address(self):
        r"""Gets the vip_address of this RecycleLoadBalancer.

        **参数解释**：负载均衡器的IPv4私网IP地址。  **取值范围**：不涉及

        :return: The vip_address of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._vip_address

    @vip_address.setter
    def vip_address(self, vip_address):
        r"""Sets the vip_address of this RecycleLoadBalancer.

        **参数解释**：负载均衡器的IPv4私网IP地址。  **取值范围**：不涉及

        :param vip_address: The vip_address of this RecycleLoadBalancer.
        :type vip_address: str
        """
        self._vip_address = vip_address

    @property
    def vip_port_id(self):
        r"""Gets the vip_port_id of this RecycleLoadBalancer.

        **参数解释**：负载均衡器的IPv4对应的port ID。 [创建弹性负载均衡时，会自动为负载均衡创建一个port并关联一个默认的安全组，这个安全组对所有流量不生效。 ](tag:dt,hcso_dt)  **取值范围**：不涉及

        :return: The vip_port_id of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._vip_port_id

    @vip_port_id.setter
    def vip_port_id(self, vip_port_id):
        r"""Sets the vip_port_id of this RecycleLoadBalancer.

        **参数解释**：负载均衡器的IPv4对应的port ID。 [创建弹性负载均衡时，会自动为负载均衡创建一个port并关联一个默认的安全组，这个安全组对所有流量不生效。 ](tag:dt,hcso_dt)  **取值范围**：不涉及

        :param vip_port_id: The vip_port_id of this RecycleLoadBalancer.
        :type vip_port_id: str
        """
        self._vip_port_id = vip_port_id

    @property
    def tags(self):
        r"""Gets the tags of this RecycleLoadBalancer.

        **参数解释**：负载均衡的标签列表。

        :return: The tags of this RecycleLoadBalancer.
        :rtype: list[:class:`huaweicloudsdkelb.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this RecycleLoadBalancer.

        **参数解释**：负载均衡的标签列表。

        :param tags: The tags of this RecycleLoadBalancer.
        :type tags: list[:class:`huaweicloudsdkelb.v3.Tag`]
        """
        self._tags = tags

    @property
    def created_at(self):
        r"""Gets the created_at of this RecycleLoadBalancer.

        **参数解释**：负载均衡器的创建时间。  **取值范围**： 格式：yyyy-MM-dd'T'HH:mm:ss'Z'

        :return: The created_at of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this RecycleLoadBalancer.

        **参数解释**：负载均衡器的创建时间。  **取值范围**： 格式：yyyy-MM-dd'T'HH:mm:ss'Z'

        :param created_at: The created_at of this RecycleLoadBalancer.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this RecycleLoadBalancer.

        **参数解释**：负载均衡器的更新时间。  **取值范围**： 格式：yyyy-MM-dd'T'HH:mm:ss'Z'

        :return: The updated_at of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this RecycleLoadBalancer.

        **参数解释**：负载均衡器的更新时间。  **取值范围**： 格式：yyyy-MM-dd'T'HH:mm:ss'Z'

        :param updated_at: The updated_at of this RecycleLoadBalancer.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def guaranteed(self):
        r"""Gets the guaranteed of this RecycleLoadBalancer.

        **参数解释**：是否独享型LB。  **取值范围**： - false：共享型。 - true：独享型。

        :return: The guaranteed of this RecycleLoadBalancer.
        :rtype: bool
        """
        return self._guaranteed

    @guaranteed.setter
    def guaranteed(self, guaranteed):
        r"""Sets the guaranteed of this RecycleLoadBalancer.

        **参数解释**：是否独享型LB。  **取值范围**： - false：共享型。 - true：独享型。

        :param guaranteed: The guaranteed of this RecycleLoadBalancer.
        :type guaranteed: bool
        """
        self._guaranteed = guaranteed

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this RecycleLoadBalancer.

        **参数解释**：负载均衡器所在VPC ID。  **取值范围**：不涉及

        :return: The vpc_id of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this RecycleLoadBalancer.

        **参数解释**：负载均衡器所在VPC ID。  **取值范围**：不涉及

        :param vpc_id: The vpc_id of this RecycleLoadBalancer.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def eips(self):
        r"""Gets the eips of this RecycleLoadBalancer.

        **参数解释**：负载均衡器绑定的EIP。 注：该字段与publicips一致。

        :return: The eips of this RecycleLoadBalancer.
        :rtype: list[:class:`huaweicloudsdkelb.v3.EipInfo`]
        """
        return self._eips

    @eips.setter
    def eips(self, eips):
        r"""Sets the eips of this RecycleLoadBalancer.

        **参数解释**：负载均衡器绑定的EIP。 注：该字段与publicips一致。

        :param eips: The eips of this RecycleLoadBalancer.
        :type eips: list[:class:`huaweicloudsdkelb.v3.EipInfo`]
        """
        self._eips = eips

    @property
    def ipv6_vip_address(self):
        r"""Gets the ipv6_vip_address of this RecycleLoadBalancer.

        **参数解释**：双栈类型负载均衡器的IPv6地址。  **取值范围**：不涉及  [不支持IPv6，请勿使用。](tag:dt)

        :return: The ipv6_vip_address of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._ipv6_vip_address

    @ipv6_vip_address.setter
    def ipv6_vip_address(self, ipv6_vip_address):
        r"""Sets the ipv6_vip_address of this RecycleLoadBalancer.

        **参数解释**：双栈类型负载均衡器的IPv6地址。  **取值范围**：不涉及  [不支持IPv6，请勿使用。](tag:dt)

        :param ipv6_vip_address: The ipv6_vip_address of this RecycleLoadBalancer.
        :type ipv6_vip_address: str
        """
        self._ipv6_vip_address = ipv6_vip_address

    @property
    def ipv6_vip_virsubnet_id(self):
        r"""Gets the ipv6_vip_virsubnet_id of this RecycleLoadBalancer.

        **参数解释**：双栈类型负载均衡器所在子网的IPv6网络ID，也称为该负载均衡器实例的前端子网。  **取值范围**：不涉及  [不支持IPv6，请勿使用。](tag:dt)

        :return: The ipv6_vip_virsubnet_id of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._ipv6_vip_virsubnet_id

    @ipv6_vip_virsubnet_id.setter
    def ipv6_vip_virsubnet_id(self, ipv6_vip_virsubnet_id):
        r"""Sets the ipv6_vip_virsubnet_id of this RecycleLoadBalancer.

        **参数解释**：双栈类型负载均衡器所在子网的IPv6网络ID，也称为该负载均衡器实例的前端子网。  **取值范围**：不涉及  [不支持IPv6，请勿使用。](tag:dt)

        :param ipv6_vip_virsubnet_id: The ipv6_vip_virsubnet_id of this RecycleLoadBalancer.
        :type ipv6_vip_virsubnet_id: str
        """
        self._ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id

    @property
    def ipv6_vip_port_id(self):
        r"""Gets the ipv6_vip_port_id of this RecycleLoadBalancer.

        **参数解释**：双栈类型负载均衡器的IPv6对应的port ID。  **取值范围**：不涉及  [不支持IPv6，请勿使用。](tag:dt)

        :return: The ipv6_vip_port_id of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._ipv6_vip_port_id

    @ipv6_vip_port_id.setter
    def ipv6_vip_port_id(self, ipv6_vip_port_id):
        r"""Sets the ipv6_vip_port_id of this RecycleLoadBalancer.

        **参数解释**：双栈类型负载均衡器的IPv6对应的port ID。  **取值范围**：不涉及  [不支持IPv6，请勿使用。](tag:dt)

        :param ipv6_vip_port_id: The ipv6_vip_port_id of this RecycleLoadBalancer.
        :type ipv6_vip_port_id: str
        """
        self._ipv6_vip_port_id = ipv6_vip_port_id

    @property
    def availability_zone_list(self):
        r"""Gets the availability_zone_list of this RecycleLoadBalancer.

        **参数解释**：负载均衡器所在的可用区列表。  **取值范围**：不涉及

        :return: The availability_zone_list of this RecycleLoadBalancer.
        :rtype: list[str]
        """
        return self._availability_zone_list

    @availability_zone_list.setter
    def availability_zone_list(self, availability_zone_list):
        r"""Sets the availability_zone_list of this RecycleLoadBalancer.

        **参数解释**：负载均衡器所在的可用区列表。  **取值范围**：不涉及

        :param availability_zone_list: The availability_zone_list of this RecycleLoadBalancer.
        :type availability_zone_list: list[str]
        """
        self._availability_zone_list = availability_zone_list

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this RecycleLoadBalancer.

        **参数解释**：资源所属的企业项目ID。  **取值范围**： - \"0\"：表示资源属于default企业项目。 - UUID格式的字符串，表示非默认企业项目。  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :return: The enterprise_project_id of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this RecycleLoadBalancer.

        **参数解释**：资源所属的企业项目ID。  **取值范围**： - \"0\"：表示资源属于default企业项目。 - UUID格式的字符串，表示非默认企业项目。  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :param enterprise_project_id: The enterprise_project_id of this RecycleLoadBalancer.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def billing_info(self):
        r"""Gets the billing_info of this RecycleLoadBalancer.

        **参数解释**：资源账单信息。  **取值范围**： - 空：按需计费。 [- 非空：包周期计费，  包周期计费billing_info字段的格式为：order_id:product_id:region_id:project_id，如： CS2107161019CDJZZ:OFFI569702121789763584:az:057ef081eb00d2732fd1c01a9be75e6f  不支持该字段，请勿使用](tag:hws_eu,g42,hk_g42,dt,hcso_dt,hcso,hk_vdf,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b)

        :return: The billing_info of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        r"""Sets the billing_info of this RecycleLoadBalancer.

        **参数解释**：资源账单信息。  **取值范围**： - 空：按需计费。 [- 非空：包周期计费，  包周期计费billing_info字段的格式为：order_id:product_id:region_id:project_id，如： CS2107161019CDJZZ:OFFI569702121789763584:az:057ef081eb00d2732fd1c01a9be75e6f  不支持该字段，请勿使用](tag:hws_eu,g42,hk_g42,dt,hcso_dt,hcso,hk_vdf,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b)

        :param billing_info: The billing_info of this RecycleLoadBalancer.
        :type billing_info: str
        """
        self._billing_info = billing_info

    @property
    def l4_flavor_id(self):
        r"""Gets the l4_flavor_id of this RecycleLoadBalancer.

        **参数解释**：网络型规格ID。 对于弹性扩缩容实例，表示上限规格。  **取值范围**：不涉及 [hsco场景下所有LB实例共享带宽，该字段无效，请勿使用。](tag:hcso,hk_vdf,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b)

        :return: The l4_flavor_id of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._l4_flavor_id

    @l4_flavor_id.setter
    def l4_flavor_id(self, l4_flavor_id):
        r"""Sets the l4_flavor_id of this RecycleLoadBalancer.

        **参数解释**：网络型规格ID。 对于弹性扩缩容实例，表示上限规格。  **取值范围**：不涉及 [hsco场景下所有LB实例共享带宽，该字段无效，请勿使用。](tag:hcso,hk_vdf,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b)

        :param l4_flavor_id: The l4_flavor_id of this RecycleLoadBalancer.
        :type l4_flavor_id: str
        """
        self._l4_flavor_id = l4_flavor_id

    @property
    def l4_scale_flavor_id(self):
        r"""Gets the l4_scale_flavor_id of this RecycleLoadBalancer.

        **参数解释**：四层弹性Flavor ID。  **取值范围**：不涉及  不支持该字段，请勿使用。

        :return: The l4_scale_flavor_id of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._l4_scale_flavor_id

    @l4_scale_flavor_id.setter
    def l4_scale_flavor_id(self, l4_scale_flavor_id):
        r"""Sets the l4_scale_flavor_id of this RecycleLoadBalancer.

        **参数解释**：四层弹性Flavor ID。  **取值范围**：不涉及  不支持该字段，请勿使用。

        :param l4_scale_flavor_id: The l4_scale_flavor_id of this RecycleLoadBalancer.
        :type l4_scale_flavor_id: str
        """
        self._l4_scale_flavor_id = l4_scale_flavor_id

    @property
    def l7_flavor_id(self):
        r"""Gets the l7_flavor_id of this RecycleLoadBalancer.

        **参数解释**：应用型ID。 对于弹性扩缩容实例，表示上限规格ID。  **取值范围**：不涉及  [hsco场景下所有LB实例共享带宽，该字段无效，请勿使用。](tag:hcso,hk_vdf,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b)

        :return: The l7_flavor_id of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._l7_flavor_id

    @l7_flavor_id.setter
    def l7_flavor_id(self, l7_flavor_id):
        r"""Sets the l7_flavor_id of this RecycleLoadBalancer.

        **参数解释**：应用型ID。 对于弹性扩缩容实例，表示上限规格ID。  **取值范围**：不涉及  [hsco场景下所有LB实例共享带宽，该字段无效，请勿使用。](tag:hcso,hk_vdf,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b)

        :param l7_flavor_id: The l7_flavor_id of this RecycleLoadBalancer.
        :type l7_flavor_id: str
        """
        self._l7_flavor_id = l7_flavor_id

    @property
    def l7_scale_flavor_id(self):
        r"""Gets the l7_scale_flavor_id of this RecycleLoadBalancer.

        **参数解释**：七层弹性Flavor ID。  **取值范围**：不涉及  不支持该字段，请勿使用。

        :return: The l7_scale_flavor_id of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._l7_scale_flavor_id

    @l7_scale_flavor_id.setter
    def l7_scale_flavor_id(self, l7_scale_flavor_id):
        r"""Sets the l7_scale_flavor_id of this RecycleLoadBalancer.

        **参数解释**：七层弹性Flavor ID。  **取值范围**：不涉及  不支持该字段，请勿使用。

        :param l7_scale_flavor_id: The l7_scale_flavor_id of this RecycleLoadBalancer.
        :type l7_scale_flavor_id: str
        """
        self._l7_scale_flavor_id = l7_scale_flavor_id

    @property
    def publicips(self):
        r"""Gets the publicips of this RecycleLoadBalancer.

        **参数解释**：负载均衡器绑定的公网IP。只支持绑定一个公网IP。  注：该字段与eips一致。

        :return: The publicips of this RecycleLoadBalancer.
        :rtype: list[:class:`huaweicloudsdkelb.v3.PublicIpInfo`]
        """
        return self._publicips

    @publicips.setter
    def publicips(self, publicips):
        r"""Sets the publicips of this RecycleLoadBalancer.

        **参数解释**：负载均衡器绑定的公网IP。只支持绑定一个公网IP。  注：该字段与eips一致。

        :param publicips: The publicips of this RecycleLoadBalancer.
        :type publicips: list[:class:`huaweicloudsdkelb.v3.PublicIpInfo`]
        """
        self._publicips = publicips

    @property
    def global_eips(self):
        r"""Gets the global_eips of this RecycleLoadBalancer.

        **参数解释**：负载均衡器绑定的global eip。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42,dt,hcso_dt,hk_vdf,fcs,ctc,ocb,hws_ocb)

        :return: The global_eips of this RecycleLoadBalancer.
        :rtype: list[:class:`huaweicloudsdkelb.v3.GlobalEipInfo`]
        """
        return self._global_eips

    @global_eips.setter
    def global_eips(self, global_eips):
        r"""Sets the global_eips of this RecycleLoadBalancer.

        **参数解释**：负载均衡器绑定的global eip。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42,dt,hcso_dt,hk_vdf,fcs,ctc,ocb,hws_ocb)

        :param global_eips: The global_eips of this RecycleLoadBalancer.
        :type global_eips: list[:class:`huaweicloudsdkelb.v3.GlobalEipInfo`]
        """
        self._global_eips = global_eips

    @property
    def elb_virsubnet_ids(self):
        r"""Gets the elb_virsubnet_ids of this RecycleLoadBalancer.

        **参数解释**：下联面子网的网络ID列表。  **取值范围**：不涉及

        :return: The elb_virsubnet_ids of this RecycleLoadBalancer.
        :rtype: list[str]
        """
        return self._elb_virsubnet_ids

    @elb_virsubnet_ids.setter
    def elb_virsubnet_ids(self, elb_virsubnet_ids):
        r"""Sets the elb_virsubnet_ids of this RecycleLoadBalancer.

        **参数解释**：下联面子网的网络ID列表。  **取值范围**：不涉及

        :param elb_virsubnet_ids: The elb_virsubnet_ids of this RecycleLoadBalancer.
        :type elb_virsubnet_ids: list[str]
        """
        self._elb_virsubnet_ids = elb_virsubnet_ids

    @property
    def elb_virsubnet_type(self):
        r"""Gets the elb_virsubnet_type of this RecycleLoadBalancer.

        **参数解释**：下联面子网类型。  **取值范围**： - ipv4：ipv4 - dualstack：双栈

        :return: The elb_virsubnet_type of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._elb_virsubnet_type

    @elb_virsubnet_type.setter
    def elb_virsubnet_type(self, elb_virsubnet_type):
        r"""Sets the elb_virsubnet_type of this RecycleLoadBalancer.

        **参数解释**：下联面子网类型。  **取值范围**： - ipv4：ipv4 - dualstack：双栈

        :param elb_virsubnet_type: The elb_virsubnet_type of this RecycleLoadBalancer.
        :type elb_virsubnet_type: str
        """
        self._elb_virsubnet_type = elb_virsubnet_type

    @property
    def ip_target_enable(self):
        r"""Gets the ip_target_enable of this RecycleLoadBalancer.

        **参数解释**：是否启用IP类型后端转发。 [开启IP类型后端转发后，后端服务器组不仅支持添加云上VPC内的服务器，还支持添加其他VPC、其他公有云、云下数据中心的服务器。](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,dt,hcso_dt,hws_eu) [开启IP类型后端转发后，后端服务器组不仅支持添加云上VPC内的服务器，还支持添加其他VPC、云下数据中心的服务器。](tag:fcs)  **取值范围**： - true：开启。 - false：不开启。  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :return: The ip_target_enable of this RecycleLoadBalancer.
        :rtype: bool
        """
        return self._ip_target_enable

    @ip_target_enable.setter
    def ip_target_enable(self, ip_target_enable):
        r"""Sets the ip_target_enable of this RecycleLoadBalancer.

        **参数解释**：是否启用IP类型后端转发。 [开启IP类型后端转发后，后端服务器组不仅支持添加云上VPC内的服务器，还支持添加其他VPC、其他公有云、云下数据中心的服务器。](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,dt,hcso_dt,hws_eu) [开启IP类型后端转发后，后端服务器组不仅支持添加云上VPC内的服务器，还支持添加其他VPC、云下数据中心的服务器。](tag:fcs)  **取值范围**： - true：开启。 - false：不开启。  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :param ip_target_enable: The ip_target_enable of this RecycleLoadBalancer.
        :type ip_target_enable: bool
        """
        self._ip_target_enable = ip_target_enable

    @property
    def frozen_scene(self):
        r"""Gets the frozen_scene of this RecycleLoadBalancer.

        **参数解释**：负载均衡器的冻结场景。 [若负载均衡器有多个冻结场景，用逗号分隔。  **取值范围**： - POLICE：公安冻结场景。 - ILLEGAL：违规冻结场景。 - VERIFY：客户未实名认证冻结场景。 - PARTNER：合作伙伴冻结（合作伙伴冻结子客户资源）。 - AREAR：欠费冻结场景。](tag:hws,hws_hk)  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42,dt,hcso_dt,ocb,hws_ocb)

        :return: The frozen_scene of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._frozen_scene

    @frozen_scene.setter
    def frozen_scene(self, frozen_scene):
        r"""Sets the frozen_scene of this RecycleLoadBalancer.

        **参数解释**：负载均衡器的冻结场景。 [若负载均衡器有多个冻结场景，用逗号分隔。  **取值范围**： - POLICE：公安冻结场景。 - ILLEGAL：违规冻结场景。 - VERIFY：客户未实名认证冻结场景。 - PARTNER：合作伙伴冻结（合作伙伴冻结子客户资源）。 - AREAR：欠费冻结场景。](tag:hws,hws_hk)  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42,dt,hcso_dt,ocb,hws_ocb)

        :param frozen_scene: The frozen_scene of this RecycleLoadBalancer.
        :type frozen_scene: str
        """
        self._frozen_scene = frozen_scene

    @property
    def ipv6_bandwidth(self):
        r"""Gets the ipv6_bandwidth of this RecycleLoadBalancer.

        :return: The ipv6_bandwidth of this RecycleLoadBalancer.
        :rtype: :class:`huaweicloudsdkelb.v3.BandwidthRef`
        """
        return self._ipv6_bandwidth

    @ipv6_bandwidth.setter
    def ipv6_bandwidth(self, ipv6_bandwidth):
        r"""Sets the ipv6_bandwidth of this RecycleLoadBalancer.

        :param ipv6_bandwidth: The ipv6_bandwidth of this RecycleLoadBalancer.
        :type ipv6_bandwidth: :class:`huaweicloudsdkelb.v3.BandwidthRef`
        """
        self._ipv6_bandwidth = ipv6_bandwidth

    @property
    def deletion_protection_enable(self):
        r"""Gets the deletion_protection_enable of this RecycleLoadBalancer.

        **参数解释**：是否开启删除保护。  **取值范围**： - false：不开启。 - true：开启。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :return: The deletion_protection_enable of this RecycleLoadBalancer.
        :rtype: bool
        """
        return self._deletion_protection_enable

    @deletion_protection_enable.setter
    def deletion_protection_enable(self, deletion_protection_enable):
        r"""Sets the deletion_protection_enable of this RecycleLoadBalancer.

        **参数解释**：是否开启删除保护。  **取值范围**： - false：不开启。 - true：开启。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :param deletion_protection_enable: The deletion_protection_enable of this RecycleLoadBalancer.
        :type deletion_protection_enable: bool
        """
        self._deletion_protection_enable = deletion_protection_enable

    @property
    def autoscaling(self):
        r"""Gets the autoscaling of this RecycleLoadBalancer.

        :return: The autoscaling of this RecycleLoadBalancer.
        :rtype: :class:`huaweicloudsdkelb.v3.AutoscalingRef`
        """
        return self._autoscaling

    @autoscaling.setter
    def autoscaling(self, autoscaling):
        r"""Sets the autoscaling of this RecycleLoadBalancer.

        :param autoscaling: The autoscaling of this RecycleLoadBalancer.
        :type autoscaling: :class:`huaweicloudsdkelb.v3.AutoscalingRef`
        """
        self._autoscaling = autoscaling

    @property
    def public_border_group(self):
        r"""Gets the public_border_group of this RecycleLoadBalancer.

        **参数解释**：LB所属AZ组。  **取值范围**：不涉及

        :return: The public_border_group of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        r"""Sets the public_border_group of this RecycleLoadBalancer.

        **参数解释**：LB所属AZ组。  **取值范围**：不涉及

        :param public_border_group: The public_border_group of this RecycleLoadBalancer.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this RecycleLoadBalancer.

        **参数解释**：负载均衡器实例的计费模式。  **取值范围**： - flavor：按规格计费 - lcu：按使用量计费 - 空值：若是共享型表示免费实例。若是独享型则与flavor模式一致，都是按规格计费。

        :return: The charge_mode of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this RecycleLoadBalancer.

        **参数解释**：负载均衡器实例的计费模式。  **取值范围**： - flavor：按规格计费 - lcu：按使用量计费 - 空值：若是共享型表示免费实例。若是独享型则与flavor模式一致，都是按规格计费。

        :param charge_mode: The charge_mode of this RecycleLoadBalancer.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def waf_failure_action(self):
        r"""Gets the waf_failure_action of this RecycleLoadBalancer.

        **参数解释**：WAF故障时的流量处理策略。  **取值范围**：discard:丢弃，forward: 转发到后端。  [不支持该字段，请勿使用。](tag:hws_eu,hws_test,hcs,hcs_sm,hcso,hk_vdf,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b,hcso_dt,dt,ocb,ctc,cmcc,tm,ct,sbc,g42,hws_ocb,hk_sbc,hk_tm,hk_g42)

        :return: The waf_failure_action of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._waf_failure_action

    @waf_failure_action.setter
    def waf_failure_action(self, waf_failure_action):
        r"""Sets the waf_failure_action of this RecycleLoadBalancer.

        **参数解释**：WAF故障时的流量处理策略。  **取值范围**：discard:丢弃，forward: 转发到后端。  [不支持该字段，请勿使用。](tag:hws_eu,hws_test,hcs,hcs_sm,hcso,hk_vdf,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b,hcso_dt,dt,ocb,ctc,cmcc,tm,ct,sbc,g42,hws_ocb,hk_sbc,hk_tm,hk_g42)

        :param waf_failure_action: The waf_failure_action of this RecycleLoadBalancer.
        :type waf_failure_action: str
        """
        self._waf_failure_action = waf_failure_action

    @property
    def protection_status(self):
        r"""Gets the protection_status of this RecycleLoadBalancer.

        **参数解释**：修改保护状态。  **取值范围**： - nonProtection: 不保护。 - consoleProtection: 控制台修改保护。

        :return: The protection_status of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._protection_status

    @protection_status.setter
    def protection_status(self, protection_status):
        r"""Sets the protection_status of this RecycleLoadBalancer.

        **参数解释**：修改保护状态。  **取值范围**： - nonProtection: 不保护。 - consoleProtection: 控制台修改保护。

        :param protection_status: The protection_status of this RecycleLoadBalancer.
        :type protection_status: str
        """
        self._protection_status = protection_status

    @property
    def protection_reason(self):
        r"""Gets the protection_reason of this RecycleLoadBalancer.

        **参数解释**：设置保护的原因。作为protection_status的转态设置的原因。  **取值范围**：除<和>外通用Unicode字符集字符，最大255个字符。

        :return: The protection_reason of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._protection_reason

    @protection_reason.setter
    def protection_reason(self, protection_reason):
        r"""Sets the protection_reason of this RecycleLoadBalancer.

        **参数解释**：设置保护的原因。作为protection_status的转态设置的原因。  **取值范围**：除<和>外通用Unicode字符集字符，最大255个字符。

        :param protection_reason: The protection_reason of this RecycleLoadBalancer.
        :type protection_reason: str
        """
        self._protection_reason = protection_reason

    @property
    def log_group_id(self):
        r"""Gets the log_group_id of this RecycleLoadBalancer.

        **参数解释**：LB所绑定的logtank对应的group id。  **取值范围**：不涉及

        :return: The log_group_id of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        r"""Sets the log_group_id of this RecycleLoadBalancer.

        **参数解释**：LB所绑定的logtank对应的group id。  **取值范围**：不涉及

        :param log_group_id: The log_group_id of this RecycleLoadBalancer.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_topic_id(self):
        r"""Gets the log_topic_id of this RecycleLoadBalancer.

        **参数解释**：LB所绑定的logtank对应的topic id。  **取值范围**：不涉及

        :return: The log_topic_id of this RecycleLoadBalancer.
        :rtype: str
        """
        return self._log_topic_id

    @log_topic_id.setter
    def log_topic_id(self, log_topic_id):
        r"""Sets the log_topic_id of this RecycleLoadBalancer.

        **参数解释**：LB所绑定的logtank对应的topic id。  **取值范围**：不涉及

        :param log_topic_id: The log_topic_id of this RecycleLoadBalancer.
        :type log_topic_id: str
        """
        self._log_topic_id = log_topic_id

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
        if not isinstance(other, RecycleLoadBalancer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
