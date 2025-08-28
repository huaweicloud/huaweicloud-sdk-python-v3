# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLoadBalancerOption:

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
        'admin_state_up': 'bool',
        'description': 'str',
        'ipv6_vip_virsubnet_id': 'str',
        'vip_subnet_cidr_id': 'str',
        'vip_address': 'str',
        'l4_flavor_id': 'str',
        'l7_flavor_id': 'str',
        'ipv6_bandwidth': 'BandwidthRef',
        'ip_target_enable': 'bool',
        'elb_virsubnet_ids': 'list[str]',
        'deletion_protection_enable': 'bool',
        'prepaid_options': 'PrepaidUpdateOption',
        'autoscaling': 'UpdateLoadbalancerAutoscalingOption',
        'charge_mode': 'str',
        'waf_failure_action': 'str',
        'protection_status': 'str',
        'protection_reason': 'str',
        'ipv6_vip_address': 'str'
    }

    attribute_map = {
        'name': 'name',
        'admin_state_up': 'admin_state_up',
        'description': 'description',
        'ipv6_vip_virsubnet_id': 'ipv6_vip_virsubnet_id',
        'vip_subnet_cidr_id': 'vip_subnet_cidr_id',
        'vip_address': 'vip_address',
        'l4_flavor_id': 'l4_flavor_id',
        'l7_flavor_id': 'l7_flavor_id',
        'ipv6_bandwidth': 'ipv6_bandwidth',
        'ip_target_enable': 'ip_target_enable',
        'elb_virsubnet_ids': 'elb_virsubnet_ids',
        'deletion_protection_enable': 'deletion_protection_enable',
        'prepaid_options': 'prepaid_options',
        'autoscaling': 'autoscaling',
        'charge_mode': 'charge_mode',
        'waf_failure_action': 'waf_failure_action',
        'protection_status': 'protection_status',
        'protection_reason': 'protection_reason',
        'ipv6_vip_address': 'ipv6_vip_address'
    }

    def __init__(self, name=None, admin_state_up=None, description=None, ipv6_vip_virsubnet_id=None, vip_subnet_cidr_id=None, vip_address=None, l4_flavor_id=None, l7_flavor_id=None, ipv6_bandwidth=None, ip_target_enable=None, elb_virsubnet_ids=None, deletion_protection_enable=None, prepaid_options=None, autoscaling=None, charge_mode=None, waf_failure_action=None, protection_status=None, protection_reason=None, ipv6_vip_address=None):
        r"""UpdateLoadBalancerOption

        The model defined in huaweicloud sdk

        :param name: **参数解释**：负载均衡器的名称。  **约束限制**：不涉及  **取值范围**：支持中文字符、英文字符等unicode字符，且长度为[0-255]个字符。可以为空。  **默认取值**：不涉及
        :type name: str
        :param admin_state_up: **参数解释**：负载均衡器的启用状态。  **取值范围**： - true ：启用。 - false：停用。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt)
        :type admin_state_up: bool
        :param description: **参数解释**：负载均衡器的描述。  **约束限制**：不涉及  **取值范围**：支持中文字符、英文字符等unicode字符，且长度为[0-255]个字符。可以为空。  **默认取值**：不涉及
        :type description: str
        :param ipv6_vip_virsubnet_id: **参数解释**：双栈类型负载均衡器所在子网的IPv6网络ID，也称为该负载均衡器实例的前端子网。 可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_network_id得到。 更新ipv6_vip_virsubnet_id可以更新负载均衡器所在IPv6子网，且负载均衡器的内网IPv6地址将发生变化，但不会导致IPv4子网发生变化。  **约束限制**： - ipv6_vip_virsubnet_id 对应的子网必须属于当前负载均衡器所在VPC，且子网需开启支持IPv6。 - 只有guaranteed是true的负载均衡器才支持更新ipv6_vip_virsubnet_id。  **取值范围**：标准的UUID格式，长度为36个字符。  **默认取值**：不涉及  [不支持IPv6，请勿使用。](tag:dt) &gt; *传入为null表示解绑IPv6子网。不变更IPv6子网，请勿传入该字段。*
        :type ipv6_vip_virsubnet_id: str
        :param vip_subnet_cidr_id: **参数解释**：负载均衡器所在的IPv4子网ID，也称为该负载均衡器实例的前端子网。 可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_subnet_id得到。 更新vip_subnet_cidr_id可以更新负载均衡器所在IPv4子网，并且负载均衡器的**私网IPv4**地址将发生变化，但不会导致IPv6子网发生变化。  **约束限制**： - 若同时设置了vip_address，则必须保证vip_address对应的IP在vip_subnet_cidr_id的子网网段中。 - vip_subnet_cidr_id对应的子网必须属于当前负载均衡器vpc_id对应的VPC。 - 只有guaranteed是true的负载均衡器才支持更新vip_subnet_cidr_id。  **取值范围**：标准的UUID格式，长度为36个字符。  **默认取值**：不涉及  &gt;*传入null表示解绑IPv4子网。不变更IPv4子网，请勿传入该字段。*
        :type vip_subnet_cidr_id: str
        :param vip_address: **参数解释**：负载均衡器的IPv4私网IP。  **约束限制**：该地址必须包含在所在子网的IPv4网段内，且未被占用。  **取值范围**：满足IPv4的地址格式，[0-255].[0-255].[0-255].[0-255]. 如192.168.1.1。  **默认取值**：不涉及  注：仅当guaranteed是true的场合，才支持更新。
        :type vip_address: str
        :param l4_flavor_id: **参数解释**：网络型规格ID。 可以通过GET https://{ELB_Endpoint}/v3/{project_id}/elb/flavors?type&#x3D;L4 响应参数中的id得到。  **约束限制**： - 仅当guaranteed是true的场合，才支持更新。 - 可以支持规格改大改小，注意改小过程中可能会造成部分长连接中断，影响部分连接的新建。 - autoscaling.enable&#x3D;true时，修改无意义，不生效。 - 当传入的规格类型为L4，表示该实例为固定规格实例，按规格计费。 - 当传入的规格类型为L4_elastic_max，表示该实例为弹性实例，按LCU计费。  **取值范围**：不涉及  **默认取值**：不涉及  [网关型LB不支持指定l4_flavor_id。](tag:hws_eu) [只支持设置为l4_flavor.elb.shared。](tag:hcso_dt) [当前场景下所有LB实例共享带宽，该字段无效，请勿使用。](tag:hk_vdf,srg,fcs)
        :type l4_flavor_id: str
        :param l7_flavor_id: **参数解释**：应用型ID。 可以通过GET https://{ELB_Endpoint}/v3/{project_id}/elb/flavors?type&#x3D;L7 响应参数中的id得到。  **约束限制**： - 仅当guaranteed是true的场合，才支持更新。 - 可以支持规格改大改小，注意改小过程中可能会造成部分长连接中断，影响部分连接的新建， - autoscaling.enable&#x3D;true时，修改无意义，不生效。 - 当传入的规格类型为L7，表示该实例为固定规格实例，按规格计费。 - 当传入的规格类型为L7_elastic_max，表示该实例为弹性实例，按LCU计费。  **取值范围**：不涉及  **默认取值**：不涉及  [网关型LB不支持指定l7_flavor_id。](tag:hws_eu) [只支持设置为l7_flavor.elb.shared。](tag:hcso_dt) [所有LB实例共享带宽，该字段无效，请勿使用。](tag:hk_vdf,srg,fcs)
        :type l7_flavor_id: str
        :param ipv6_bandwidth: 
        :type ipv6_bandwidth: :class:`huaweicloudsdkelb.v3.BandwidthRef`
        :param ip_target_enable: **参数解释**：是否启用IP类型后端转发。 [开启IP类型后端转发后，后端服务器组不仅支持添加云上VPC内的服务器，还支持添加其他VPC、其他公有云、云下数据中心的服务器。](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,dt,hcso_dt,hws_eu) [开启IP类型后端转发后，后端服务器组不仅支持添加云上VPC内的服务器，还支持添加其他VPC、云下数据中心的服务器。](tag:srg,fcs)  **约束限制**： - 开启后不能关闭。 - 使用共享VPC的实例使用此特性时，需确保共享资源所有者已开通VPC对等连接，否则通信异常。 [- 仅独享型负载均衡器支持该特性。](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt) [- 网关型LB不支持该特性。](tag:hws_eu)  **取值范围**： - true：开启。 - false：不开启。  **默认取值**：不涉及  [荷兰region不支持该字段，请勿使用。](tag:dt)
        :type ip_target_enable: bool
        :param elb_virsubnet_ids: **参数解释**：下联面子网的网络ID列表。 可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_network_id得到。  **约束限制**： - 已绑定的下联面子网也在传参elb_virsubnet_ids列表中，则绑定关系保留。 - 已绑定的下联面子网若不在传参elb_virsubnet_ids列表中，则将移除LB与该下联面子网的关联关系。但不允许移除已被ELB使用的子网，否则将报错，不做任何修改。 - 在传参elb_virsubnet_ids列表中但不在已绑定的下联面子网列表中，则将新增LB与下联面的绑定关系。 - 所有elb_virsubnet_ids中的ID同属于该LB所在的VPC。 - 不支持边缘云子网。  **取值范围**：不涉及  **默认取值**：不涉及
        :type elb_virsubnet_ids: list[str]
        :param deletion_protection_enable: **参数解释**：是否开启删除保护。  **约束限制**：退场时需要先关闭所有资源的删除保护开关。  **取值范围**：false 不开启，true 开启。  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42) [荷兰region不支持该字段，请勿使用。](tag:dt)
        :type deletion_protection_enable: bool
        :param prepaid_options: 
        :type prepaid_options: :class:`huaweicloudsdkelb.v3.PrepaidUpdateOption`
        :param autoscaling: 
        :type autoscaling: :class:`huaweicloudsdkelb.v3.UpdateLoadbalancerAutoscalingOption`
        :param charge_mode: **参数解释**：计费模式。  **约束限制**：不涉及  **取值范围**： - flavor：按规格计费  **默认取值**：不涉及
        :type charge_mode: str
        :param waf_failure_action: **参数解释**：WAF故障时的流量处理策略。  **约束限制**：只有绑定了waf的LB实例，该字段才会生效。  **取值范围**：discard:丢弃，forward: 转发到后端。  **默认取值**：forward  [不支持该字段，请勿使用。](tag:hws_eu,hws_test,hcs,hcs_sm,hcso,hk_vdf,srg,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b,hcso_dt,dt,ocb,ctc,cmcc,tm,ct,sbc,g42,hws_ocb,hk_sbc,hk_tm,hk_g42)
        :type waf_failure_action: str
        :param protection_status: **参数解释**：修改保护状态。  **约束限制**：不涉及  **取值范围**： - nonProtection: 不保护 - consoleProtection: 控制台修改保护。  **默认取值**：不涉及
        :type protection_status: str
        :param protection_reason: **参数解释**：设置保护的原因。作为protection_status的转态设置的原因。  **约束限制**：仅当protection_status为consoleProtection时有效。  **取值范围**：除&#39;&lt;&#39;和&#39;&gt;&#39;外通用Unicode字符集字符，最大255个字符。  **默认取值**：不涉及
        :type protection_reason: str
        :param ipv6_vip_address: **参数解释**：双栈类型负载均衡器的IPv6地址。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  [不支持IPv6，请勿使用。](tag:dt)
        :type ipv6_vip_address: str
        """
        
        

        self._name = None
        self._admin_state_up = None
        self._description = None
        self._ipv6_vip_virsubnet_id = None
        self._vip_subnet_cidr_id = None
        self._vip_address = None
        self._l4_flavor_id = None
        self._l7_flavor_id = None
        self._ipv6_bandwidth = None
        self._ip_target_enable = None
        self._elb_virsubnet_ids = None
        self._deletion_protection_enable = None
        self._prepaid_options = None
        self._autoscaling = None
        self._charge_mode = None
        self._waf_failure_action = None
        self._protection_status = None
        self._protection_reason = None
        self._ipv6_vip_address = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if description is not None:
            self.description = description
        if ipv6_vip_virsubnet_id is not None:
            self.ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id
        if vip_subnet_cidr_id is not None:
            self.vip_subnet_cidr_id = vip_subnet_cidr_id
        if vip_address is not None:
            self.vip_address = vip_address
        if l4_flavor_id is not None:
            self.l4_flavor_id = l4_flavor_id
        if l7_flavor_id is not None:
            self.l7_flavor_id = l7_flavor_id
        if ipv6_bandwidth is not None:
            self.ipv6_bandwidth = ipv6_bandwidth
        if ip_target_enable is not None:
            self.ip_target_enable = ip_target_enable
        if elb_virsubnet_ids is not None:
            self.elb_virsubnet_ids = elb_virsubnet_ids
        if deletion_protection_enable is not None:
            self.deletion_protection_enable = deletion_protection_enable
        if prepaid_options is not None:
            self.prepaid_options = prepaid_options
        if autoscaling is not None:
            self.autoscaling = autoscaling
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if waf_failure_action is not None:
            self.waf_failure_action = waf_failure_action
        if protection_status is not None:
            self.protection_status = protection_status
        if protection_reason is not None:
            self.protection_reason = protection_reason
        if ipv6_vip_address is not None:
            self.ipv6_vip_address = ipv6_vip_address

    @property
    def name(self):
        r"""Gets the name of this UpdateLoadBalancerOption.

        **参数解释**：负载均衡器的名称。  **约束限制**：不涉及  **取值范围**：支持中文字符、英文字符等unicode字符，且长度为[0-255]个字符。可以为空。  **默认取值**：不涉及

        :return: The name of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateLoadBalancerOption.

        **参数解释**：负载均衡器的名称。  **约束限制**：不涉及  **取值范围**：支持中文字符、英文字符等unicode字符，且长度为[0-255]个字符。可以为空。  **默认取值**：不涉及

        :param name: The name of this UpdateLoadBalancerOption.
        :type name: str
        """
        self._name = name

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this UpdateLoadBalancerOption.

        **参数解释**：负载均衡器的启用状态。  **取值范围**： - true ：启用。 - false：停用。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt)

        :return: The admin_state_up of this UpdateLoadBalancerOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this UpdateLoadBalancerOption.

        **参数解释**：负载均衡器的启用状态。  **取值范围**： - true ：启用。 - false：停用。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt)

        :param admin_state_up: The admin_state_up of this UpdateLoadBalancerOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def description(self):
        r"""Gets the description of this UpdateLoadBalancerOption.

        **参数解释**：负载均衡器的描述。  **约束限制**：不涉及  **取值范围**：支持中文字符、英文字符等unicode字符，且长度为[0-255]个字符。可以为空。  **默认取值**：不涉及

        :return: The description of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateLoadBalancerOption.

        **参数解释**：负载均衡器的描述。  **约束限制**：不涉及  **取值范围**：支持中文字符、英文字符等unicode字符，且长度为[0-255]个字符。可以为空。  **默认取值**：不涉及

        :param description: The description of this UpdateLoadBalancerOption.
        :type description: str
        """
        self._description = description

    @property
    def ipv6_vip_virsubnet_id(self):
        r"""Gets the ipv6_vip_virsubnet_id of this UpdateLoadBalancerOption.

        **参数解释**：双栈类型负载均衡器所在子网的IPv6网络ID，也称为该负载均衡器实例的前端子网。 可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_network_id得到。 更新ipv6_vip_virsubnet_id可以更新负载均衡器所在IPv6子网，且负载均衡器的内网IPv6地址将发生变化，但不会导致IPv4子网发生变化。  **约束限制**： - ipv6_vip_virsubnet_id 对应的子网必须属于当前负载均衡器所在VPC，且子网需开启支持IPv6。 - 只有guaranteed是true的负载均衡器才支持更新ipv6_vip_virsubnet_id。  **取值范围**：标准的UUID格式，长度为36个字符。  **默认取值**：不涉及  [不支持IPv6，请勿使用。](tag:dt) > *传入为null表示解绑IPv6子网。不变更IPv6子网，请勿传入该字段。*

        :return: The ipv6_vip_virsubnet_id of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._ipv6_vip_virsubnet_id

    @ipv6_vip_virsubnet_id.setter
    def ipv6_vip_virsubnet_id(self, ipv6_vip_virsubnet_id):
        r"""Sets the ipv6_vip_virsubnet_id of this UpdateLoadBalancerOption.

        **参数解释**：双栈类型负载均衡器所在子网的IPv6网络ID，也称为该负载均衡器实例的前端子网。 可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_network_id得到。 更新ipv6_vip_virsubnet_id可以更新负载均衡器所在IPv6子网，且负载均衡器的内网IPv6地址将发生变化，但不会导致IPv4子网发生变化。  **约束限制**： - ipv6_vip_virsubnet_id 对应的子网必须属于当前负载均衡器所在VPC，且子网需开启支持IPv6。 - 只有guaranteed是true的负载均衡器才支持更新ipv6_vip_virsubnet_id。  **取值范围**：标准的UUID格式，长度为36个字符。  **默认取值**：不涉及  [不支持IPv6，请勿使用。](tag:dt) > *传入为null表示解绑IPv6子网。不变更IPv6子网，请勿传入该字段。*

        :param ipv6_vip_virsubnet_id: The ipv6_vip_virsubnet_id of this UpdateLoadBalancerOption.
        :type ipv6_vip_virsubnet_id: str
        """
        self._ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id

    @property
    def vip_subnet_cidr_id(self):
        r"""Gets the vip_subnet_cidr_id of this UpdateLoadBalancerOption.

        **参数解释**：负载均衡器所在的IPv4子网ID，也称为该负载均衡器实例的前端子网。 可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_subnet_id得到。 更新vip_subnet_cidr_id可以更新负载均衡器所在IPv4子网，并且负载均衡器的**私网IPv4**地址将发生变化，但不会导致IPv6子网发生变化。  **约束限制**： - 若同时设置了vip_address，则必须保证vip_address对应的IP在vip_subnet_cidr_id的子网网段中。 - vip_subnet_cidr_id对应的子网必须属于当前负载均衡器vpc_id对应的VPC。 - 只有guaranteed是true的负载均衡器才支持更新vip_subnet_cidr_id。  **取值范围**：标准的UUID格式，长度为36个字符。  **默认取值**：不涉及  >*传入null表示解绑IPv4子网。不变更IPv4子网，请勿传入该字段。*

        :return: The vip_subnet_cidr_id of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._vip_subnet_cidr_id

    @vip_subnet_cidr_id.setter
    def vip_subnet_cidr_id(self, vip_subnet_cidr_id):
        r"""Sets the vip_subnet_cidr_id of this UpdateLoadBalancerOption.

        **参数解释**：负载均衡器所在的IPv4子网ID，也称为该负载均衡器实例的前端子网。 可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_subnet_id得到。 更新vip_subnet_cidr_id可以更新负载均衡器所在IPv4子网，并且负载均衡器的**私网IPv4**地址将发生变化，但不会导致IPv6子网发生变化。  **约束限制**： - 若同时设置了vip_address，则必须保证vip_address对应的IP在vip_subnet_cidr_id的子网网段中。 - vip_subnet_cidr_id对应的子网必须属于当前负载均衡器vpc_id对应的VPC。 - 只有guaranteed是true的负载均衡器才支持更新vip_subnet_cidr_id。  **取值范围**：标准的UUID格式，长度为36个字符。  **默认取值**：不涉及  >*传入null表示解绑IPv4子网。不变更IPv4子网，请勿传入该字段。*

        :param vip_subnet_cidr_id: The vip_subnet_cidr_id of this UpdateLoadBalancerOption.
        :type vip_subnet_cidr_id: str
        """
        self._vip_subnet_cidr_id = vip_subnet_cidr_id

    @property
    def vip_address(self):
        r"""Gets the vip_address of this UpdateLoadBalancerOption.

        **参数解释**：负载均衡器的IPv4私网IP。  **约束限制**：该地址必须包含在所在子网的IPv4网段内，且未被占用。  **取值范围**：满足IPv4的地址格式，[0-255].[0-255].[0-255].[0-255]. 如192.168.1.1。  **默认取值**：不涉及  注：仅当guaranteed是true的场合，才支持更新。

        :return: The vip_address of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._vip_address

    @vip_address.setter
    def vip_address(self, vip_address):
        r"""Sets the vip_address of this UpdateLoadBalancerOption.

        **参数解释**：负载均衡器的IPv4私网IP。  **约束限制**：该地址必须包含在所在子网的IPv4网段内，且未被占用。  **取值范围**：满足IPv4的地址格式，[0-255].[0-255].[0-255].[0-255]. 如192.168.1.1。  **默认取值**：不涉及  注：仅当guaranteed是true的场合，才支持更新。

        :param vip_address: The vip_address of this UpdateLoadBalancerOption.
        :type vip_address: str
        """
        self._vip_address = vip_address

    @property
    def l4_flavor_id(self):
        r"""Gets the l4_flavor_id of this UpdateLoadBalancerOption.

        **参数解释**：网络型规格ID。 可以通过GET https://{ELB_Endpoint}/v3/{project_id}/elb/flavors?type=L4 响应参数中的id得到。  **约束限制**： - 仅当guaranteed是true的场合，才支持更新。 - 可以支持规格改大改小，注意改小过程中可能会造成部分长连接中断，影响部分连接的新建。 - autoscaling.enable=true时，修改无意义，不生效。 - 当传入的规格类型为L4，表示该实例为固定规格实例，按规格计费。 - 当传入的规格类型为L4_elastic_max，表示该实例为弹性实例，按LCU计费。  **取值范围**：不涉及  **默认取值**：不涉及  [网关型LB不支持指定l4_flavor_id。](tag:hws_eu) [只支持设置为l4_flavor.elb.shared。](tag:hcso_dt) [当前场景下所有LB实例共享带宽，该字段无效，请勿使用。](tag:hk_vdf,srg,fcs)

        :return: The l4_flavor_id of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._l4_flavor_id

    @l4_flavor_id.setter
    def l4_flavor_id(self, l4_flavor_id):
        r"""Sets the l4_flavor_id of this UpdateLoadBalancerOption.

        **参数解释**：网络型规格ID。 可以通过GET https://{ELB_Endpoint}/v3/{project_id}/elb/flavors?type=L4 响应参数中的id得到。  **约束限制**： - 仅当guaranteed是true的场合，才支持更新。 - 可以支持规格改大改小，注意改小过程中可能会造成部分长连接中断，影响部分连接的新建。 - autoscaling.enable=true时，修改无意义，不生效。 - 当传入的规格类型为L4，表示该实例为固定规格实例，按规格计费。 - 当传入的规格类型为L4_elastic_max，表示该实例为弹性实例，按LCU计费。  **取值范围**：不涉及  **默认取值**：不涉及  [网关型LB不支持指定l4_flavor_id。](tag:hws_eu) [只支持设置为l4_flavor.elb.shared。](tag:hcso_dt) [当前场景下所有LB实例共享带宽，该字段无效，请勿使用。](tag:hk_vdf,srg,fcs)

        :param l4_flavor_id: The l4_flavor_id of this UpdateLoadBalancerOption.
        :type l4_flavor_id: str
        """
        self._l4_flavor_id = l4_flavor_id

    @property
    def l7_flavor_id(self):
        r"""Gets the l7_flavor_id of this UpdateLoadBalancerOption.

        **参数解释**：应用型ID。 可以通过GET https://{ELB_Endpoint}/v3/{project_id}/elb/flavors?type=L7 响应参数中的id得到。  **约束限制**： - 仅当guaranteed是true的场合，才支持更新。 - 可以支持规格改大改小，注意改小过程中可能会造成部分长连接中断，影响部分连接的新建， - autoscaling.enable=true时，修改无意义，不生效。 - 当传入的规格类型为L7，表示该实例为固定规格实例，按规格计费。 - 当传入的规格类型为L7_elastic_max，表示该实例为弹性实例，按LCU计费。  **取值范围**：不涉及  **默认取值**：不涉及  [网关型LB不支持指定l7_flavor_id。](tag:hws_eu) [只支持设置为l7_flavor.elb.shared。](tag:hcso_dt) [所有LB实例共享带宽，该字段无效，请勿使用。](tag:hk_vdf,srg,fcs)

        :return: The l7_flavor_id of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._l7_flavor_id

    @l7_flavor_id.setter
    def l7_flavor_id(self, l7_flavor_id):
        r"""Sets the l7_flavor_id of this UpdateLoadBalancerOption.

        **参数解释**：应用型ID。 可以通过GET https://{ELB_Endpoint}/v3/{project_id}/elb/flavors?type=L7 响应参数中的id得到。  **约束限制**： - 仅当guaranteed是true的场合，才支持更新。 - 可以支持规格改大改小，注意改小过程中可能会造成部分长连接中断，影响部分连接的新建， - autoscaling.enable=true时，修改无意义，不生效。 - 当传入的规格类型为L7，表示该实例为固定规格实例，按规格计费。 - 当传入的规格类型为L7_elastic_max，表示该实例为弹性实例，按LCU计费。  **取值范围**：不涉及  **默认取值**：不涉及  [网关型LB不支持指定l7_flavor_id。](tag:hws_eu) [只支持设置为l7_flavor.elb.shared。](tag:hcso_dt) [所有LB实例共享带宽，该字段无效，请勿使用。](tag:hk_vdf,srg,fcs)

        :param l7_flavor_id: The l7_flavor_id of this UpdateLoadBalancerOption.
        :type l7_flavor_id: str
        """
        self._l7_flavor_id = l7_flavor_id

    @property
    def ipv6_bandwidth(self):
        r"""Gets the ipv6_bandwidth of this UpdateLoadBalancerOption.

        :return: The ipv6_bandwidth of this UpdateLoadBalancerOption.
        :rtype: :class:`huaweicloudsdkelb.v3.BandwidthRef`
        """
        return self._ipv6_bandwidth

    @ipv6_bandwidth.setter
    def ipv6_bandwidth(self, ipv6_bandwidth):
        r"""Sets the ipv6_bandwidth of this UpdateLoadBalancerOption.

        :param ipv6_bandwidth: The ipv6_bandwidth of this UpdateLoadBalancerOption.
        :type ipv6_bandwidth: :class:`huaweicloudsdkelb.v3.BandwidthRef`
        """
        self._ipv6_bandwidth = ipv6_bandwidth

    @property
    def ip_target_enable(self):
        r"""Gets the ip_target_enable of this UpdateLoadBalancerOption.

        **参数解释**：是否启用IP类型后端转发。 [开启IP类型后端转发后，后端服务器组不仅支持添加云上VPC内的服务器，还支持添加其他VPC、其他公有云、云下数据中心的服务器。](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,dt,hcso_dt,hws_eu) [开启IP类型后端转发后，后端服务器组不仅支持添加云上VPC内的服务器，还支持添加其他VPC、云下数据中心的服务器。](tag:srg,fcs)  **约束限制**： - 开启后不能关闭。 - 使用共享VPC的实例使用此特性时，需确保共享资源所有者已开通VPC对等连接，否则通信异常。 [- 仅独享型负载均衡器支持该特性。](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt) [- 网关型LB不支持该特性。](tag:hws_eu)  **取值范围**： - true：开启。 - false：不开启。  **默认取值**：不涉及  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :return: The ip_target_enable of this UpdateLoadBalancerOption.
        :rtype: bool
        """
        return self._ip_target_enable

    @ip_target_enable.setter
    def ip_target_enable(self, ip_target_enable):
        r"""Sets the ip_target_enable of this UpdateLoadBalancerOption.

        **参数解释**：是否启用IP类型后端转发。 [开启IP类型后端转发后，后端服务器组不仅支持添加云上VPC内的服务器，还支持添加其他VPC、其他公有云、云下数据中心的服务器。](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,dt,hcso_dt,hws_eu) [开启IP类型后端转发后，后端服务器组不仅支持添加云上VPC内的服务器，还支持添加其他VPC、云下数据中心的服务器。](tag:srg,fcs)  **约束限制**： - 开启后不能关闭。 - 使用共享VPC的实例使用此特性时，需确保共享资源所有者已开通VPC对等连接，否则通信异常。 [- 仅独享型负载均衡器支持该特性。](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt) [- 网关型LB不支持该特性。](tag:hws_eu)  **取值范围**： - true：开启。 - false：不开启。  **默认取值**：不涉及  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :param ip_target_enable: The ip_target_enable of this UpdateLoadBalancerOption.
        :type ip_target_enable: bool
        """
        self._ip_target_enable = ip_target_enable

    @property
    def elb_virsubnet_ids(self):
        r"""Gets the elb_virsubnet_ids of this UpdateLoadBalancerOption.

        **参数解释**：下联面子网的网络ID列表。 可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_network_id得到。  **约束限制**： - 已绑定的下联面子网也在传参elb_virsubnet_ids列表中，则绑定关系保留。 - 已绑定的下联面子网若不在传参elb_virsubnet_ids列表中，则将移除LB与该下联面子网的关联关系。但不允许移除已被ELB使用的子网，否则将报错，不做任何修改。 - 在传参elb_virsubnet_ids列表中但不在已绑定的下联面子网列表中，则将新增LB与下联面的绑定关系。 - 所有elb_virsubnet_ids中的ID同属于该LB所在的VPC。 - 不支持边缘云子网。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The elb_virsubnet_ids of this UpdateLoadBalancerOption.
        :rtype: list[str]
        """
        return self._elb_virsubnet_ids

    @elb_virsubnet_ids.setter
    def elb_virsubnet_ids(self, elb_virsubnet_ids):
        r"""Sets the elb_virsubnet_ids of this UpdateLoadBalancerOption.

        **参数解释**：下联面子网的网络ID列表。 可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_network_id得到。  **约束限制**： - 已绑定的下联面子网也在传参elb_virsubnet_ids列表中，则绑定关系保留。 - 已绑定的下联面子网若不在传参elb_virsubnet_ids列表中，则将移除LB与该下联面子网的关联关系。但不允许移除已被ELB使用的子网，否则将报错，不做任何修改。 - 在传参elb_virsubnet_ids列表中但不在已绑定的下联面子网列表中，则将新增LB与下联面的绑定关系。 - 所有elb_virsubnet_ids中的ID同属于该LB所在的VPC。 - 不支持边缘云子网。  **取值范围**：不涉及  **默认取值**：不涉及

        :param elb_virsubnet_ids: The elb_virsubnet_ids of this UpdateLoadBalancerOption.
        :type elb_virsubnet_ids: list[str]
        """
        self._elb_virsubnet_ids = elb_virsubnet_ids

    @property
    def deletion_protection_enable(self):
        r"""Gets the deletion_protection_enable of this UpdateLoadBalancerOption.

        **参数解释**：是否开启删除保护。  **约束限制**：退场时需要先关闭所有资源的删除保护开关。  **取值范围**：false 不开启，true 开启。  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42) [荷兰region不支持该字段，请勿使用。](tag:dt)

        :return: The deletion_protection_enable of this UpdateLoadBalancerOption.
        :rtype: bool
        """
        return self._deletion_protection_enable

    @deletion_protection_enable.setter
    def deletion_protection_enable(self, deletion_protection_enable):
        r"""Sets the deletion_protection_enable of this UpdateLoadBalancerOption.

        **参数解释**：是否开启删除保护。  **约束限制**：退场时需要先关闭所有资源的删除保护开关。  **取值范围**：false 不开启，true 开启。  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42) [荷兰region不支持该字段，请勿使用。](tag:dt)

        :param deletion_protection_enable: The deletion_protection_enable of this UpdateLoadBalancerOption.
        :type deletion_protection_enable: bool
        """
        self._deletion_protection_enable = deletion_protection_enable

    @property
    def prepaid_options(self):
        r"""Gets the prepaid_options of this UpdateLoadBalancerOption.

        :return: The prepaid_options of this UpdateLoadBalancerOption.
        :rtype: :class:`huaweicloudsdkelb.v3.PrepaidUpdateOption`
        """
        return self._prepaid_options

    @prepaid_options.setter
    def prepaid_options(self, prepaid_options):
        r"""Sets the prepaid_options of this UpdateLoadBalancerOption.

        :param prepaid_options: The prepaid_options of this UpdateLoadBalancerOption.
        :type prepaid_options: :class:`huaweicloudsdkelb.v3.PrepaidUpdateOption`
        """
        self._prepaid_options = prepaid_options

    @property
    def autoscaling(self):
        r"""Gets the autoscaling of this UpdateLoadBalancerOption.

        :return: The autoscaling of this UpdateLoadBalancerOption.
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateLoadbalancerAutoscalingOption`
        """
        return self._autoscaling

    @autoscaling.setter
    def autoscaling(self, autoscaling):
        r"""Sets the autoscaling of this UpdateLoadBalancerOption.

        :param autoscaling: The autoscaling of this UpdateLoadBalancerOption.
        :type autoscaling: :class:`huaweicloudsdkelb.v3.UpdateLoadbalancerAutoscalingOption`
        """
        self._autoscaling = autoscaling

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this UpdateLoadBalancerOption.

        **参数解释**：计费模式。  **约束限制**：不涉及  **取值范围**： - flavor：按规格计费  **默认取值**：不涉及

        :return: The charge_mode of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this UpdateLoadBalancerOption.

        **参数解释**：计费模式。  **约束限制**：不涉及  **取值范围**： - flavor：按规格计费  **默认取值**：不涉及

        :param charge_mode: The charge_mode of this UpdateLoadBalancerOption.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def waf_failure_action(self):
        r"""Gets the waf_failure_action of this UpdateLoadBalancerOption.

        **参数解释**：WAF故障时的流量处理策略。  **约束限制**：只有绑定了waf的LB实例，该字段才会生效。  **取值范围**：discard:丢弃，forward: 转发到后端。  **默认取值**：forward  [不支持该字段，请勿使用。](tag:hws_eu,hws_test,hcs,hcs_sm,hcso,hk_vdf,srg,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b,hcso_dt,dt,ocb,ctc,cmcc,tm,ct,sbc,g42,hws_ocb,hk_sbc,hk_tm,hk_g42)

        :return: The waf_failure_action of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._waf_failure_action

    @waf_failure_action.setter
    def waf_failure_action(self, waf_failure_action):
        r"""Sets the waf_failure_action of this UpdateLoadBalancerOption.

        **参数解释**：WAF故障时的流量处理策略。  **约束限制**：只有绑定了waf的LB实例，该字段才会生效。  **取值范围**：discard:丢弃，forward: 转发到后端。  **默认取值**：forward  [不支持该字段，请勿使用。](tag:hws_eu,hws_test,hcs,hcs_sm,hcso,hk_vdf,srg,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b,hcso_dt,dt,ocb,ctc,cmcc,tm,ct,sbc,g42,hws_ocb,hk_sbc,hk_tm,hk_g42)

        :param waf_failure_action: The waf_failure_action of this UpdateLoadBalancerOption.
        :type waf_failure_action: str
        """
        self._waf_failure_action = waf_failure_action

    @property
    def protection_status(self):
        r"""Gets the protection_status of this UpdateLoadBalancerOption.

        **参数解释**：修改保护状态。  **约束限制**：不涉及  **取值范围**： - nonProtection: 不保护 - consoleProtection: 控制台修改保护。  **默认取值**：不涉及

        :return: The protection_status of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._protection_status

    @protection_status.setter
    def protection_status(self, protection_status):
        r"""Sets the protection_status of this UpdateLoadBalancerOption.

        **参数解释**：修改保护状态。  **约束限制**：不涉及  **取值范围**： - nonProtection: 不保护 - consoleProtection: 控制台修改保护。  **默认取值**：不涉及

        :param protection_status: The protection_status of this UpdateLoadBalancerOption.
        :type protection_status: str
        """
        self._protection_status = protection_status

    @property
    def protection_reason(self):
        r"""Gets the protection_reason of this UpdateLoadBalancerOption.

        **参数解释**：设置保护的原因。作为protection_status的转态设置的原因。  **约束限制**：仅当protection_status为consoleProtection时有效。  **取值范围**：除'<'和'>'外通用Unicode字符集字符，最大255个字符。  **默认取值**：不涉及

        :return: The protection_reason of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._protection_reason

    @protection_reason.setter
    def protection_reason(self, protection_reason):
        r"""Sets the protection_reason of this UpdateLoadBalancerOption.

        **参数解释**：设置保护的原因。作为protection_status的转态设置的原因。  **约束限制**：仅当protection_status为consoleProtection时有效。  **取值范围**：除'<'和'>'外通用Unicode字符集字符，最大255个字符。  **默认取值**：不涉及

        :param protection_reason: The protection_reason of this UpdateLoadBalancerOption.
        :type protection_reason: str
        """
        self._protection_reason = protection_reason

    @property
    def ipv6_vip_address(self):
        r"""Gets the ipv6_vip_address of this UpdateLoadBalancerOption.

        **参数解释**：双栈类型负载均衡器的IPv6地址。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  [不支持IPv6，请勿使用。](tag:dt)

        :return: The ipv6_vip_address of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._ipv6_vip_address

    @ipv6_vip_address.setter
    def ipv6_vip_address(self, ipv6_vip_address):
        r"""Sets the ipv6_vip_address of this UpdateLoadBalancerOption.

        **参数解释**：双栈类型负载均衡器的IPv6地址。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  [不支持IPv6，请勿使用。](tag:dt)

        :param ipv6_vip_address: The ipv6_vip_address of this UpdateLoadBalancerOption.
        :type ipv6_vip_address: str
        """
        self._ipv6_vip_address = ipv6_vip_address

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
        if not isinstance(other, UpdateLoadBalancerOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
