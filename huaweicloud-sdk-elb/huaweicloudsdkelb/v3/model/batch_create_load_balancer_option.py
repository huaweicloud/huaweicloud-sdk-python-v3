# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateLoadBalancerOption:

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
        'ids': 'list[str]',
        'project_id': 'str',
        'number': 'int',
        'name': 'str',
        'description': 'str',
        'vip_address': 'str',
        'vip_subnet_cidr_id': 'str',
        'ipv6_vip_virsubnet_id': 'str',
        'provider': 'str',
        'l4_flavor_id': 'str',
        'l7_flavor_id': 'str',
        'guaranteed': 'bool',
        'vpc_id': 'str',
        'availability_zone_list': 'list[str]',
        'enterprise_project_id': 'str',
        'tags': 'list[Tag]',
        'admin_state_up': 'bool',
        'billing_info': 'str',
        'ipv6_bandwidth': 'BandwidthRef',
        'bandwidth': 'BandwidthRef',
        'publicip_ids': 'list[str]',
        'publicip': 'CreateLoadBalancerPublicIpOption',
        'elb_virsubnet_ids': 'list[str]',
        'ip_target_enable': 'bool',
        'deletion_protection_enable': 'bool',
        'prepaid_options': 'PrepaidCreateOption',
        'autoscaling': 'CreateLoadbalancerAutoscalingOption',
        'waf_failure_action': 'str',
        'protection_status': 'str',
        'protection_reason': 'str',
        'charge_mode': 'str',
        'ipv6_vip_address': 'str'
    }

    attribute_map = {
        'id': 'id',
        'ids': 'ids',
        'project_id': 'project_id',
        'number': 'number',
        'name': 'name',
        'description': 'description',
        'vip_address': 'vip_address',
        'vip_subnet_cidr_id': 'vip_subnet_cidr_id',
        'ipv6_vip_virsubnet_id': 'ipv6_vip_virsubnet_id',
        'provider': 'provider',
        'l4_flavor_id': 'l4_flavor_id',
        'l7_flavor_id': 'l7_flavor_id',
        'guaranteed': 'guaranteed',
        'vpc_id': 'vpc_id',
        'availability_zone_list': 'availability_zone_list',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'admin_state_up': 'admin_state_up',
        'billing_info': 'billing_info',
        'ipv6_bandwidth': 'ipv6_bandwidth',
        'bandwidth': 'bandwidth',
        'publicip_ids': 'publicip_ids',
        'publicip': 'publicip',
        'elb_virsubnet_ids': 'elb_virsubnet_ids',
        'ip_target_enable': 'ip_target_enable',
        'deletion_protection_enable': 'deletion_protection_enable',
        'prepaid_options': 'prepaid_options',
        'autoscaling': 'autoscaling',
        'waf_failure_action': 'waf_failure_action',
        'protection_status': 'protection_status',
        'protection_reason': 'protection_reason',
        'charge_mode': 'charge_mode',
        'ipv6_vip_address': 'ipv6_vip_address'
    }

    def __init__(self, id=None, ids=None, project_id=None, number=None, name=None, description=None, vip_address=None, vip_subnet_cidr_id=None, ipv6_vip_virsubnet_id=None, provider=None, l4_flavor_id=None, l7_flavor_id=None, guaranteed=None, vpc_id=None, availability_zone_list=None, enterprise_project_id=None, tags=None, admin_state_up=None, billing_info=None, ipv6_bandwidth=None, bandwidth=None, publicip_ids=None, publicip=None, elb_virsubnet_ids=None, ip_target_enable=None, deletion_protection_enable=None, prepaid_options=None, autoscaling=None, waf_failure_action=None, protection_status=None, protection_reason=None, charge_mode=None, ipv6_vip_address=None):
        r"""BatchCreateLoadBalancerOption

        The model defined in huaweicloud sdk

        :param id: 负载均衡器ID（UUID）。不支持该字段，请勿使用。
        :type id: str
        :param ids: 批创负载均衡器ID的列表（UUID）。不支持该字段，请勿使用。
        :type ids: list[str]
        :param project_id: 负载均衡器所在的项目ID。
        :type project_id: str
        :param number: 批量创建负载均衡器的数量
        :type number: int
        :param name: 负载均衡器的名称。 使用说明： - 当批创负载均衡器数量为1时，负载均衡器的名字即为该传入的值。 - 当批创负载均衡器数量大于1时，负载均衡器的名字在传入的name后加上4位后缀。  例如：批量创建3个负载均衡器，传入name为\&quot;elb-test\&quot;，则三个负载均衡器名字分别为： \&quot;elb-test-0001\&quot;，\&quot;elb-test-0002\&quot;，\&quot;elb-test-0003\&quot;
        :type name: str
        :param description: 负载均衡器的描述。
        :type description: str
        :param vip_address: 负载均衡器的IPv4虚拟IP。该地址必须包含在所在子网的IPv4网段内，且未被占用。  使用说明： - 传入vip_address时必须传入vip_subnet_cidr_id。 - 不传入vip_address，但传入vip_subnet_cidr_id，则自动分配IPv4虚拟IP。 - 不传入vip_address，且不传vip_subnet_cidr_id，则不分配虚拟IP，vip_address&#x3D;null。 - 当批量创建的number数量大于1时不支持传入该字段，返回400。
        :type vip_address: str
        :param vip_subnet_cidr_id: 负载均衡器所在子网的IPv4子网ID。若需要创建带IPv4虚拟IP的LB，该字段必须传入。 可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_subnet_id得到。  使用说明： - vpc_id, vip_subnet_cidr_id, ipv6_vip_virsubnet_id不能同时为空，且需要在同一个vpc下。 - 若同时传入vpc_id和vip_subnet_cidr_id， 则vip_subnet_cidr_id对应的子网必须属于vpc_id对应的VPC。
        :type vip_subnet_cidr_id: str
        :param ipv6_vip_virsubnet_id: 双栈类型负载均衡器所在子网的IPv6网络ID。可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_network_id得到。  使用说明： - vpc_id，vip_subnet_cidr_id，ipv6_vip_virsubnet_id不能同时为空，且需要在同一个vpc下。 - 需要对应的子网开启IPv6。 - 批量创建共享型实例时，该字段不允许指定。  [不支持IPv6，请勿使用。](tag:dt)
        :type ipv6_vip_virsubnet_id: str
        :param provider: 负载均衡器的生产者名称。固定为vlb。批量创建共享型实例时，该字段不允许指定。
        :type provider: str
        :param l4_flavor_id: 网络型规格ID。  [使用说明： - 可以通过GET https://{ELB_Endpoint}/v3/{project_id}/elb/flavors?type&#x3D;L4 响应参数中的id得到。 - 当l4_flavor_id和l7_flavor_id都不传的时，会使用默认flavor （默认flavor根据不同局点有所不同，具体以实际值为准）。 - 当传入的规格类型为L4，表示该实例为固定规格实例，按规格计费。 - 当传入的规格类型为L4_elastic_max，表示该实例为弹性实例，按LCU计费。 - 批量创建共享型实例时，该字段不允许指定。  ](tag:hws,hws_hk,hws_eu,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb)   [网关型LB不支持指定l4_flavor_id。](tag:hws_eu) [只支持设置为l4_flavor.elb.shared。](tag:hcso_dt) [所有LB实例共享带宽，该字段无效，请勿使用。](tag:hcso,srg,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b)
        :type l4_flavor_id: str
        :param l7_flavor_id: 应用型规格ID。  [使用说明： - 可以通过GET https://{ELB_Endpoint}/v3/{project_id}/elb/flavors?type&#x3D;L7 响应参数中的id得到。 - 当l4_flavor_id和l7_flavor_id都不传的时，会使用默认flavor （默认flavor根据不同局点有所不同，具体以实际值为准）。 - 当传入的规格类型为L7，表示该实例为固定规格实例，按规格计费。 - 当传入的规格类型为L7_elastic_max，表示该实例为弹性实例，按LCU计费。 - 批量创建共享型实例时，该字段不允许指定。 ](tag:hws,hws_hk,hws_eu,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb)   [网关型LB不支持指定l7_flavor_id。](tag:hws_eu) [只支持设置为l7_flavor.elb.shared。](tag:hcso_dt) [所有LB实例共享带宽，该字段无效，请勿使用。](tag:hcso,srg,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b)
        :type l7_flavor_id: str
        :param guaranteed: 批量创建的是否是独享型负载均衡器。  取值： - true：独享型。 - false：共享型。  默认：true。
        :type guaranteed: bool
        :param vpc_id: 负载均衡器所在的VPC ID。可以通过GET https://{VPC_Endpoint}/v1/{project_id}/vpcs 响应参数中的id得到。  使用说明： - vpc_id，vip_subnet_cidr_id，ipv6_vip_virsubnet_id不能同时为空，且需要在同一个vpc下。 - 批量创建共享型实例时，该字段不允许指定。
        :type vpc_id: str
        :param availability_zone_list: 可用区列表。可通过GET https://{ELB_Endpoint}/v3/{project_id}/elb/availability-zones 接口来查询可用区集合列表。创建负载均衡器时，从查询结果选择某一个可用区集合，并从中选择一个或多个可用区。  使用说明： - 批量创建共享型实例时，该字段不允许指定。
        :type availability_zone_list: list[str]
        :param enterprise_project_id: 负载均衡器所属的企业项目ID。创建时传入\&quot;\&quot;、\&quot;0\&quot;或不存在的企业项目ID，或者不传则资源属于default企业项目，默认返回\&quot;0\&quot;。  [不支持该字段，请勿使用。](tag:dt,hcso_dt)
        :type enterprise_project_id: str
        :param tags: 负载均衡的标签列表。示例：\&quot;tags\&quot;:[{\&quot;key\&quot;:\&quot;my_tag\&quot;,\&quot;value\&quot;:\&quot;my_tag_value\&quot;}]
        :type tags: list[:class:`huaweicloudsdkelb.v3.Tag`]
        :param admin_state_up: 参数解释：负载均衡器的启用状态。  取值范围： - true ：启用。 - false：停用。  默认取值：true。  [不支持该字段，请勿使用。](tag:dt)
        :type admin_state_up: bool
        :param billing_info: 资源账单信息。  取值范围： - 空：按需计费。 [- 非空：包周期计费，格式为：order_id:product_id:region_id:project_id。如：CS2107161019CDJZZ:OFFI569702121789763584:az1:057ef081eb00d2732fd1c01a9be75e6f](tag:hws)  [不支持该字段，请勿使用。](tag:hws_hk,hws_eu,hws_eu_wb,hws_test,srg,fcs,fcs_vm,dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf)
        :type billing_info: str
        :param ipv6_bandwidth: 
        :type ipv6_bandwidth: :class:`huaweicloudsdkelb.v3.BandwidthRef`
        :param bandwidth: 
        :type bandwidth: :class:`huaweicloudsdkelb.v3.BandwidthRef`
        :param publicip_ids: 负载均衡器绑定的公网IP ID。只支持绑定数组中的第一个EIP，其他将被忽略。 当批量创建的number数量大于1时不支持传入该字段，返回400。
        :type publicip_ids: list[str]
        :param publicip: 
        :type publicip: :class:`huaweicloudsdkelb.v3.CreateLoadBalancerPublicIpOption`
        :param elb_virsubnet_ids: 下联面子网的网络ID列表。可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_network_id得到。  若不指定该字段，则按如下规则选择下联面网络： 1. 如果ELB实例开启ipv6，则选择ipv6_vip_virsubnet_id子网对应的网络ID。 2. 如果ELB实例没有开启ipv6，开启ipv4，则选择vip_subnet_cidr_id子网对应的网络ID。 3. 如果ELB实例没有选择私网，只开启公网，则会在当前负载均衡器所在的VPC中任意选一个子网，优选可用IP多的网络。 4. 批量创建共享型实例的场景，该字段不允许指定。  若指定多个下联面子网，则按顺序优先使用第一个子网来为负载均衡器下联面端口分配ip地址。  下联面子网必须属于该LB所在的VPC。
        :type elb_virsubnet_ids: list[str]
        :param ip_target_enable: 参数解释：是否启用跨VPC后端转发。 开启跨VPC后端转发后，后端服务器组不仅支持添加云上VPC内的服务器，还支持添加其他VPC、其他公有云、云下数据中心的服务器。  约束限制： - 开启后不能关闭。 - 使用共享VPC的实例使用此特性时，需确保共享资源所有者已开通VPC对等连接，否则通信异常。 [- 仅独享型负载均衡器支持该特性。](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt) [- 网关型LB不支持该特性。](tag:hws_eu)  取值范围： - true：开启。 - false：不开启。  [荷兰region不支持该字段，请勿使用。](tag:dt)
        :type ip_target_enable: bool
        :param deletion_protection_enable: 是否开启删除保护。 批量创建共享型实例的场景，该字段不允许指定。  取值：false不开启，true开启。默认false不开启。  &gt; 退场时需要先关闭所有资源的删除保护开关。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)  [荷兰region不支持该字段，请勿使用。](tag:dt)
        :type deletion_protection_enable: bool
        :param prepaid_options: 
        :type prepaid_options: :class:`huaweicloudsdkelb.v3.PrepaidCreateOption`
        :param autoscaling: 
        :type autoscaling: :class:`huaweicloudsdkelb.v3.CreateLoadbalancerAutoscalingOption`
        :param waf_failure_action: WAF故障时的流量处理策略。discard:丢弃，forward: 转发到后端（默认）  使用说明：只有绑定了waf的LB实例，该字段才会生效。  [不支持该字段，请勿使用。](tag:hws_eu,hws_test,hcs,hcs_sm,hcso,srg,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b,hcso_dt,dt,ocb,ctc,cmcc,tm,ct,sbc,g42,hws_ocb,hk_sbc,hk_tm,hk_g42)
        :type waf_failure_action: str
        :param protection_status: 修改保护状态, 取值： - nonProtection: 不保护，默认值为nonProtection - consoleProtection: 控制台修改保护
        :type protection_status: str
        :param protection_reason: 参数解释：设置保护的原因。作为protection_status的转态设置的原因。  约束限制：仅当protection_status为consoleProtection时有效。  取值范围：除&lt;和&gt;外通用Unicode字符集字符，最大255个字符。
        :type protection_reason: str
        :param charge_mode: 创建实例采用的计费模式。flavor: 按实例规格收费，默认值。lcu: 按使用量收费。 批量创建共享型实例时，该字段不允许指定。
        :type charge_mode: str
        :param ipv6_vip_address: 双栈类型负载均衡器的IPv6地址。 当批量创建的number数量大于1时不支持传入该字段，返回400。 批量创建共享型实例的场景，该字段不允许指定。 [不支持IPv6，请勿使用。](tag:dt)
        :type ipv6_vip_address: str
        """
        
        

        self._id = None
        self._ids = None
        self._project_id = None
        self._number = None
        self._name = None
        self._description = None
        self._vip_address = None
        self._vip_subnet_cidr_id = None
        self._ipv6_vip_virsubnet_id = None
        self._provider = None
        self._l4_flavor_id = None
        self._l7_flavor_id = None
        self._guaranteed = None
        self._vpc_id = None
        self._availability_zone_list = None
        self._enterprise_project_id = None
        self._tags = None
        self._admin_state_up = None
        self._billing_info = None
        self._ipv6_bandwidth = None
        self._bandwidth = None
        self._publicip_ids = None
        self._publicip = None
        self._elb_virsubnet_ids = None
        self._ip_target_enable = None
        self._deletion_protection_enable = None
        self._prepaid_options = None
        self._autoscaling = None
        self._waf_failure_action = None
        self._protection_status = None
        self._protection_reason = None
        self._charge_mode = None
        self._ipv6_vip_address = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if ids is not None:
            self.ids = ids
        if project_id is not None:
            self.project_id = project_id
        if number is not None:
            self.number = number
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if vip_address is not None:
            self.vip_address = vip_address
        if vip_subnet_cidr_id is not None:
            self.vip_subnet_cidr_id = vip_subnet_cidr_id
        if ipv6_vip_virsubnet_id is not None:
            self.ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id
        if provider is not None:
            self.provider = provider
        if l4_flavor_id is not None:
            self.l4_flavor_id = l4_flavor_id
        if l7_flavor_id is not None:
            self.l7_flavor_id = l7_flavor_id
        if guaranteed is not None:
            self.guaranteed = guaranteed
        if vpc_id is not None:
            self.vpc_id = vpc_id
        self.availability_zone_list = availability_zone_list
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if billing_info is not None:
            self.billing_info = billing_info
        if ipv6_bandwidth is not None:
            self.ipv6_bandwidth = ipv6_bandwidth
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if publicip_ids is not None:
            self.publicip_ids = publicip_ids
        if publicip is not None:
            self.publicip = publicip
        if elb_virsubnet_ids is not None:
            self.elb_virsubnet_ids = elb_virsubnet_ids
        if ip_target_enable is not None:
            self.ip_target_enable = ip_target_enable
        if deletion_protection_enable is not None:
            self.deletion_protection_enable = deletion_protection_enable
        if prepaid_options is not None:
            self.prepaid_options = prepaid_options
        if autoscaling is not None:
            self.autoscaling = autoscaling
        if waf_failure_action is not None:
            self.waf_failure_action = waf_failure_action
        if protection_status is not None:
            self.protection_status = protection_status
        if protection_reason is not None:
            self.protection_reason = protection_reason
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if ipv6_vip_address is not None:
            self.ipv6_vip_address = ipv6_vip_address

    @property
    def id(self):
        r"""Gets the id of this BatchCreateLoadBalancerOption.

        负载均衡器ID（UUID）。不支持该字段，请勿使用。

        :return: The id of this BatchCreateLoadBalancerOption.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BatchCreateLoadBalancerOption.

        负载均衡器ID（UUID）。不支持该字段，请勿使用。

        :param id: The id of this BatchCreateLoadBalancerOption.
        :type id: str
        """
        self._id = id

    @property
    def ids(self):
        r"""Gets the ids of this BatchCreateLoadBalancerOption.

        批创负载均衡器ID的列表（UUID）。不支持该字段，请勿使用。

        :return: The ids of this BatchCreateLoadBalancerOption.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this BatchCreateLoadBalancerOption.

        批创负载均衡器ID的列表（UUID）。不支持该字段，请勿使用。

        :param ids: The ids of this BatchCreateLoadBalancerOption.
        :type ids: list[str]
        """
        self._ids = ids

    @property
    def project_id(self):
        r"""Gets the project_id of this BatchCreateLoadBalancerOption.

        负载均衡器所在的项目ID。

        :return: The project_id of this BatchCreateLoadBalancerOption.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this BatchCreateLoadBalancerOption.

        负载均衡器所在的项目ID。

        :param project_id: The project_id of this BatchCreateLoadBalancerOption.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def number(self):
        r"""Gets the number of this BatchCreateLoadBalancerOption.

        批量创建负载均衡器的数量

        :return: The number of this BatchCreateLoadBalancerOption.
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this BatchCreateLoadBalancerOption.

        批量创建负载均衡器的数量

        :param number: The number of this BatchCreateLoadBalancerOption.
        :type number: int
        """
        self._number = number

    @property
    def name(self):
        r"""Gets the name of this BatchCreateLoadBalancerOption.

        负载均衡器的名称。 使用说明： - 当批创负载均衡器数量为1时，负载均衡器的名字即为该传入的值。 - 当批创负载均衡器数量大于1时，负载均衡器的名字在传入的name后加上4位后缀。  例如：批量创建3个负载均衡器，传入name为\"elb-test\"，则三个负载均衡器名字分别为： \"elb-test-0001\"，\"elb-test-0002\"，\"elb-test-0003\"

        :return: The name of this BatchCreateLoadBalancerOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BatchCreateLoadBalancerOption.

        负载均衡器的名称。 使用说明： - 当批创负载均衡器数量为1时，负载均衡器的名字即为该传入的值。 - 当批创负载均衡器数量大于1时，负载均衡器的名字在传入的name后加上4位后缀。  例如：批量创建3个负载均衡器，传入name为\"elb-test\"，则三个负载均衡器名字分别为： \"elb-test-0001\"，\"elb-test-0002\"，\"elb-test-0003\"

        :param name: The name of this BatchCreateLoadBalancerOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this BatchCreateLoadBalancerOption.

        负载均衡器的描述。

        :return: The description of this BatchCreateLoadBalancerOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BatchCreateLoadBalancerOption.

        负载均衡器的描述。

        :param description: The description of this BatchCreateLoadBalancerOption.
        :type description: str
        """
        self._description = description

    @property
    def vip_address(self):
        r"""Gets the vip_address of this BatchCreateLoadBalancerOption.

        负载均衡器的IPv4虚拟IP。该地址必须包含在所在子网的IPv4网段内，且未被占用。  使用说明： - 传入vip_address时必须传入vip_subnet_cidr_id。 - 不传入vip_address，但传入vip_subnet_cidr_id，则自动分配IPv4虚拟IP。 - 不传入vip_address，且不传vip_subnet_cidr_id，则不分配虚拟IP，vip_address=null。 - 当批量创建的number数量大于1时不支持传入该字段，返回400。

        :return: The vip_address of this BatchCreateLoadBalancerOption.
        :rtype: str
        """
        return self._vip_address

    @vip_address.setter
    def vip_address(self, vip_address):
        r"""Sets the vip_address of this BatchCreateLoadBalancerOption.

        负载均衡器的IPv4虚拟IP。该地址必须包含在所在子网的IPv4网段内，且未被占用。  使用说明： - 传入vip_address时必须传入vip_subnet_cidr_id。 - 不传入vip_address，但传入vip_subnet_cidr_id，则自动分配IPv4虚拟IP。 - 不传入vip_address，且不传vip_subnet_cidr_id，则不分配虚拟IP，vip_address=null。 - 当批量创建的number数量大于1时不支持传入该字段，返回400。

        :param vip_address: The vip_address of this BatchCreateLoadBalancerOption.
        :type vip_address: str
        """
        self._vip_address = vip_address

    @property
    def vip_subnet_cidr_id(self):
        r"""Gets the vip_subnet_cidr_id of this BatchCreateLoadBalancerOption.

        负载均衡器所在子网的IPv4子网ID。若需要创建带IPv4虚拟IP的LB，该字段必须传入。 可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_subnet_id得到。  使用说明： - vpc_id, vip_subnet_cidr_id, ipv6_vip_virsubnet_id不能同时为空，且需要在同一个vpc下。 - 若同时传入vpc_id和vip_subnet_cidr_id， 则vip_subnet_cidr_id对应的子网必须属于vpc_id对应的VPC。

        :return: The vip_subnet_cidr_id of this BatchCreateLoadBalancerOption.
        :rtype: str
        """
        return self._vip_subnet_cidr_id

    @vip_subnet_cidr_id.setter
    def vip_subnet_cidr_id(self, vip_subnet_cidr_id):
        r"""Sets the vip_subnet_cidr_id of this BatchCreateLoadBalancerOption.

        负载均衡器所在子网的IPv4子网ID。若需要创建带IPv4虚拟IP的LB，该字段必须传入。 可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_subnet_id得到。  使用说明： - vpc_id, vip_subnet_cidr_id, ipv6_vip_virsubnet_id不能同时为空，且需要在同一个vpc下。 - 若同时传入vpc_id和vip_subnet_cidr_id， 则vip_subnet_cidr_id对应的子网必须属于vpc_id对应的VPC。

        :param vip_subnet_cidr_id: The vip_subnet_cidr_id of this BatchCreateLoadBalancerOption.
        :type vip_subnet_cidr_id: str
        """
        self._vip_subnet_cidr_id = vip_subnet_cidr_id

    @property
    def ipv6_vip_virsubnet_id(self):
        r"""Gets the ipv6_vip_virsubnet_id of this BatchCreateLoadBalancerOption.

        双栈类型负载均衡器所在子网的IPv6网络ID。可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_network_id得到。  使用说明： - vpc_id，vip_subnet_cidr_id，ipv6_vip_virsubnet_id不能同时为空，且需要在同一个vpc下。 - 需要对应的子网开启IPv6。 - 批量创建共享型实例时，该字段不允许指定。  [不支持IPv6，请勿使用。](tag:dt)

        :return: The ipv6_vip_virsubnet_id of this BatchCreateLoadBalancerOption.
        :rtype: str
        """
        return self._ipv6_vip_virsubnet_id

    @ipv6_vip_virsubnet_id.setter
    def ipv6_vip_virsubnet_id(self, ipv6_vip_virsubnet_id):
        r"""Sets the ipv6_vip_virsubnet_id of this BatchCreateLoadBalancerOption.

        双栈类型负载均衡器所在子网的IPv6网络ID。可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_network_id得到。  使用说明： - vpc_id，vip_subnet_cidr_id，ipv6_vip_virsubnet_id不能同时为空，且需要在同一个vpc下。 - 需要对应的子网开启IPv6。 - 批量创建共享型实例时，该字段不允许指定。  [不支持IPv6，请勿使用。](tag:dt)

        :param ipv6_vip_virsubnet_id: The ipv6_vip_virsubnet_id of this BatchCreateLoadBalancerOption.
        :type ipv6_vip_virsubnet_id: str
        """
        self._ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id

    @property
    def provider(self):
        r"""Gets the provider of this BatchCreateLoadBalancerOption.

        负载均衡器的生产者名称。固定为vlb。批量创建共享型实例时，该字段不允许指定。

        :return: The provider of this BatchCreateLoadBalancerOption.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this BatchCreateLoadBalancerOption.

        负载均衡器的生产者名称。固定为vlb。批量创建共享型实例时，该字段不允许指定。

        :param provider: The provider of this BatchCreateLoadBalancerOption.
        :type provider: str
        """
        self._provider = provider

    @property
    def l4_flavor_id(self):
        r"""Gets the l4_flavor_id of this BatchCreateLoadBalancerOption.

        网络型规格ID。  [使用说明： - 可以通过GET https://{ELB_Endpoint}/v3/{project_id}/elb/flavors?type=L4 响应参数中的id得到。 - 当l4_flavor_id和l7_flavor_id都不传的时，会使用默认flavor （默认flavor根据不同局点有所不同，具体以实际值为准）。 - 当传入的规格类型为L4，表示该实例为固定规格实例，按规格计费。 - 当传入的规格类型为L4_elastic_max，表示该实例为弹性实例，按LCU计费。 - 批量创建共享型实例时，该字段不允许指定。  ](tag:hws,hws_hk,hws_eu,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb)   [网关型LB不支持指定l4_flavor_id。](tag:hws_eu) [只支持设置为l4_flavor.elb.shared。](tag:hcso_dt) [所有LB实例共享带宽，该字段无效，请勿使用。](tag:hcso,srg,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b)

        :return: The l4_flavor_id of this BatchCreateLoadBalancerOption.
        :rtype: str
        """
        return self._l4_flavor_id

    @l4_flavor_id.setter
    def l4_flavor_id(self, l4_flavor_id):
        r"""Sets the l4_flavor_id of this BatchCreateLoadBalancerOption.

        网络型规格ID。  [使用说明： - 可以通过GET https://{ELB_Endpoint}/v3/{project_id}/elb/flavors?type=L4 响应参数中的id得到。 - 当l4_flavor_id和l7_flavor_id都不传的时，会使用默认flavor （默认flavor根据不同局点有所不同，具体以实际值为准）。 - 当传入的规格类型为L4，表示该实例为固定规格实例，按规格计费。 - 当传入的规格类型为L4_elastic_max，表示该实例为弹性实例，按LCU计费。 - 批量创建共享型实例时，该字段不允许指定。  ](tag:hws,hws_hk,hws_eu,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb)   [网关型LB不支持指定l4_flavor_id。](tag:hws_eu) [只支持设置为l4_flavor.elb.shared。](tag:hcso_dt) [所有LB实例共享带宽，该字段无效，请勿使用。](tag:hcso,srg,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b)

        :param l4_flavor_id: The l4_flavor_id of this BatchCreateLoadBalancerOption.
        :type l4_flavor_id: str
        """
        self._l4_flavor_id = l4_flavor_id

    @property
    def l7_flavor_id(self):
        r"""Gets the l7_flavor_id of this BatchCreateLoadBalancerOption.

        应用型规格ID。  [使用说明： - 可以通过GET https://{ELB_Endpoint}/v3/{project_id}/elb/flavors?type=L7 响应参数中的id得到。 - 当l4_flavor_id和l7_flavor_id都不传的时，会使用默认flavor （默认flavor根据不同局点有所不同，具体以实际值为准）。 - 当传入的规格类型为L7，表示该实例为固定规格实例，按规格计费。 - 当传入的规格类型为L7_elastic_max，表示该实例为弹性实例，按LCU计费。 - 批量创建共享型实例时，该字段不允许指定。 ](tag:hws,hws_hk,hws_eu,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb)   [网关型LB不支持指定l7_flavor_id。](tag:hws_eu) [只支持设置为l7_flavor.elb.shared。](tag:hcso_dt) [所有LB实例共享带宽，该字段无效，请勿使用。](tag:hcso,srg,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b)

        :return: The l7_flavor_id of this BatchCreateLoadBalancerOption.
        :rtype: str
        """
        return self._l7_flavor_id

    @l7_flavor_id.setter
    def l7_flavor_id(self, l7_flavor_id):
        r"""Sets the l7_flavor_id of this BatchCreateLoadBalancerOption.

        应用型规格ID。  [使用说明： - 可以通过GET https://{ELB_Endpoint}/v3/{project_id}/elb/flavors?type=L7 响应参数中的id得到。 - 当l4_flavor_id和l7_flavor_id都不传的时，会使用默认flavor （默认flavor根据不同局点有所不同，具体以实际值为准）。 - 当传入的规格类型为L7，表示该实例为固定规格实例，按规格计费。 - 当传入的规格类型为L7_elastic_max，表示该实例为弹性实例，按LCU计费。 - 批量创建共享型实例时，该字段不允许指定。 ](tag:hws,hws_hk,hws_eu,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb)   [网关型LB不支持指定l7_flavor_id。](tag:hws_eu) [只支持设置为l7_flavor.elb.shared。](tag:hcso_dt) [所有LB实例共享带宽，该字段无效，请勿使用。](tag:hcso,srg,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b)

        :param l7_flavor_id: The l7_flavor_id of this BatchCreateLoadBalancerOption.
        :type l7_flavor_id: str
        """
        self._l7_flavor_id = l7_flavor_id

    @property
    def guaranteed(self):
        r"""Gets the guaranteed of this BatchCreateLoadBalancerOption.

        批量创建的是否是独享型负载均衡器。  取值： - true：独享型。 - false：共享型。  默认：true。

        :return: The guaranteed of this BatchCreateLoadBalancerOption.
        :rtype: bool
        """
        return self._guaranteed

    @guaranteed.setter
    def guaranteed(self, guaranteed):
        r"""Sets the guaranteed of this BatchCreateLoadBalancerOption.

        批量创建的是否是独享型负载均衡器。  取值： - true：独享型。 - false：共享型。  默认：true。

        :param guaranteed: The guaranteed of this BatchCreateLoadBalancerOption.
        :type guaranteed: bool
        """
        self._guaranteed = guaranteed

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this BatchCreateLoadBalancerOption.

        负载均衡器所在的VPC ID。可以通过GET https://{VPC_Endpoint}/v1/{project_id}/vpcs 响应参数中的id得到。  使用说明： - vpc_id，vip_subnet_cidr_id，ipv6_vip_virsubnet_id不能同时为空，且需要在同一个vpc下。 - 批量创建共享型实例时，该字段不允许指定。

        :return: The vpc_id of this BatchCreateLoadBalancerOption.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this BatchCreateLoadBalancerOption.

        负载均衡器所在的VPC ID。可以通过GET https://{VPC_Endpoint}/v1/{project_id}/vpcs 响应参数中的id得到。  使用说明： - vpc_id，vip_subnet_cidr_id，ipv6_vip_virsubnet_id不能同时为空，且需要在同一个vpc下。 - 批量创建共享型实例时，该字段不允许指定。

        :param vpc_id: The vpc_id of this BatchCreateLoadBalancerOption.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def availability_zone_list(self):
        r"""Gets the availability_zone_list of this BatchCreateLoadBalancerOption.

        可用区列表。可通过GET https://{ELB_Endpoint}/v3/{project_id}/elb/availability-zones 接口来查询可用区集合列表。创建负载均衡器时，从查询结果选择某一个可用区集合，并从中选择一个或多个可用区。  使用说明： - 批量创建共享型实例时，该字段不允许指定。

        :return: The availability_zone_list of this BatchCreateLoadBalancerOption.
        :rtype: list[str]
        """
        return self._availability_zone_list

    @availability_zone_list.setter
    def availability_zone_list(self, availability_zone_list):
        r"""Sets the availability_zone_list of this BatchCreateLoadBalancerOption.

        可用区列表。可通过GET https://{ELB_Endpoint}/v3/{project_id}/elb/availability-zones 接口来查询可用区集合列表。创建负载均衡器时，从查询结果选择某一个可用区集合，并从中选择一个或多个可用区。  使用说明： - 批量创建共享型实例时，该字段不允许指定。

        :param availability_zone_list: The availability_zone_list of this BatchCreateLoadBalancerOption.
        :type availability_zone_list: list[str]
        """
        self._availability_zone_list = availability_zone_list

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this BatchCreateLoadBalancerOption.

        负载均衡器所属的企业项目ID。创建时传入\"\"、\"0\"或不存在的企业项目ID，或者不传则资源属于default企业项目，默认返回\"0\"。  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :return: The enterprise_project_id of this BatchCreateLoadBalancerOption.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this BatchCreateLoadBalancerOption.

        负载均衡器所属的企业项目ID。创建时传入\"\"、\"0\"或不存在的企业项目ID，或者不传则资源属于default企业项目，默认返回\"0\"。  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :param enterprise_project_id: The enterprise_project_id of this BatchCreateLoadBalancerOption.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this BatchCreateLoadBalancerOption.

        负载均衡的标签列表。示例：\"tags\":[{\"key\":\"my_tag\",\"value\":\"my_tag_value\"}]

        :return: The tags of this BatchCreateLoadBalancerOption.
        :rtype: list[:class:`huaweicloudsdkelb.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this BatchCreateLoadBalancerOption.

        负载均衡的标签列表。示例：\"tags\":[{\"key\":\"my_tag\",\"value\":\"my_tag_value\"}]

        :param tags: The tags of this BatchCreateLoadBalancerOption.
        :type tags: list[:class:`huaweicloudsdkelb.v3.Tag`]
        """
        self._tags = tags

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this BatchCreateLoadBalancerOption.

        参数解释：负载均衡器的启用状态。  取值范围： - true ：启用。 - false：停用。  默认取值：true。  [不支持该字段，请勿使用。](tag:dt)

        :return: The admin_state_up of this BatchCreateLoadBalancerOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this BatchCreateLoadBalancerOption.

        参数解释：负载均衡器的启用状态。  取值范围： - true ：启用。 - false：停用。  默认取值：true。  [不支持该字段，请勿使用。](tag:dt)

        :param admin_state_up: The admin_state_up of this BatchCreateLoadBalancerOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def billing_info(self):
        r"""Gets the billing_info of this BatchCreateLoadBalancerOption.

        资源账单信息。  取值范围： - 空：按需计费。 [- 非空：包周期计费，格式为：order_id:product_id:region_id:project_id。如：CS2107161019CDJZZ:OFFI569702121789763584:az1:057ef081eb00d2732fd1c01a9be75e6f](tag:hws)  [不支持该字段，请勿使用。](tag:hws_hk,hws_eu,hws_eu_wb,hws_test,srg,fcs,fcs_vm,dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf)

        :return: The billing_info of this BatchCreateLoadBalancerOption.
        :rtype: str
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        r"""Sets the billing_info of this BatchCreateLoadBalancerOption.

        资源账单信息。  取值范围： - 空：按需计费。 [- 非空：包周期计费，格式为：order_id:product_id:region_id:project_id。如：CS2107161019CDJZZ:OFFI569702121789763584:az1:057ef081eb00d2732fd1c01a9be75e6f](tag:hws)  [不支持该字段，请勿使用。](tag:hws_hk,hws_eu,hws_eu_wb,hws_test,srg,fcs,fcs_vm,dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf)

        :param billing_info: The billing_info of this BatchCreateLoadBalancerOption.
        :type billing_info: str
        """
        self._billing_info = billing_info

    @property
    def ipv6_bandwidth(self):
        r"""Gets the ipv6_bandwidth of this BatchCreateLoadBalancerOption.

        :return: The ipv6_bandwidth of this BatchCreateLoadBalancerOption.
        :rtype: :class:`huaweicloudsdkelb.v3.BandwidthRef`
        """
        return self._ipv6_bandwidth

    @ipv6_bandwidth.setter
    def ipv6_bandwidth(self, ipv6_bandwidth):
        r"""Sets the ipv6_bandwidth of this BatchCreateLoadBalancerOption.

        :param ipv6_bandwidth: The ipv6_bandwidth of this BatchCreateLoadBalancerOption.
        :type ipv6_bandwidth: :class:`huaweicloudsdkelb.v3.BandwidthRef`
        """
        self._ipv6_bandwidth = ipv6_bandwidth

    @property
    def bandwidth(self):
        r"""Gets the bandwidth of this BatchCreateLoadBalancerOption.

        :return: The bandwidth of this BatchCreateLoadBalancerOption.
        :rtype: :class:`huaweicloudsdkelb.v3.BandwidthRef`
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        r"""Sets the bandwidth of this BatchCreateLoadBalancerOption.

        :param bandwidth: The bandwidth of this BatchCreateLoadBalancerOption.
        :type bandwidth: :class:`huaweicloudsdkelb.v3.BandwidthRef`
        """
        self._bandwidth = bandwidth

    @property
    def publicip_ids(self):
        r"""Gets the publicip_ids of this BatchCreateLoadBalancerOption.

        负载均衡器绑定的公网IP ID。只支持绑定数组中的第一个EIP，其他将被忽略。 当批量创建的number数量大于1时不支持传入该字段，返回400。

        :return: The publicip_ids of this BatchCreateLoadBalancerOption.
        :rtype: list[str]
        """
        return self._publicip_ids

    @publicip_ids.setter
    def publicip_ids(self, publicip_ids):
        r"""Sets the publicip_ids of this BatchCreateLoadBalancerOption.

        负载均衡器绑定的公网IP ID。只支持绑定数组中的第一个EIP，其他将被忽略。 当批量创建的number数量大于1时不支持传入该字段，返回400。

        :param publicip_ids: The publicip_ids of this BatchCreateLoadBalancerOption.
        :type publicip_ids: list[str]
        """
        self._publicip_ids = publicip_ids

    @property
    def publicip(self):
        r"""Gets the publicip of this BatchCreateLoadBalancerOption.

        :return: The publicip of this BatchCreateLoadBalancerOption.
        :rtype: :class:`huaweicloudsdkelb.v3.CreateLoadBalancerPublicIpOption`
        """
        return self._publicip

    @publicip.setter
    def publicip(self, publicip):
        r"""Sets the publicip of this BatchCreateLoadBalancerOption.

        :param publicip: The publicip of this BatchCreateLoadBalancerOption.
        :type publicip: :class:`huaweicloudsdkelb.v3.CreateLoadBalancerPublicIpOption`
        """
        self._publicip = publicip

    @property
    def elb_virsubnet_ids(self):
        r"""Gets the elb_virsubnet_ids of this BatchCreateLoadBalancerOption.

        下联面子网的网络ID列表。可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_network_id得到。  若不指定该字段，则按如下规则选择下联面网络： 1. 如果ELB实例开启ipv6，则选择ipv6_vip_virsubnet_id子网对应的网络ID。 2. 如果ELB实例没有开启ipv6，开启ipv4，则选择vip_subnet_cidr_id子网对应的网络ID。 3. 如果ELB实例没有选择私网，只开启公网，则会在当前负载均衡器所在的VPC中任意选一个子网，优选可用IP多的网络。 4. 批量创建共享型实例的场景，该字段不允许指定。  若指定多个下联面子网，则按顺序优先使用第一个子网来为负载均衡器下联面端口分配ip地址。  下联面子网必须属于该LB所在的VPC。

        :return: The elb_virsubnet_ids of this BatchCreateLoadBalancerOption.
        :rtype: list[str]
        """
        return self._elb_virsubnet_ids

    @elb_virsubnet_ids.setter
    def elb_virsubnet_ids(self, elb_virsubnet_ids):
        r"""Sets the elb_virsubnet_ids of this BatchCreateLoadBalancerOption.

        下联面子网的网络ID列表。可以通过GET https://{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_network_id得到。  若不指定该字段，则按如下规则选择下联面网络： 1. 如果ELB实例开启ipv6，则选择ipv6_vip_virsubnet_id子网对应的网络ID。 2. 如果ELB实例没有开启ipv6，开启ipv4，则选择vip_subnet_cidr_id子网对应的网络ID。 3. 如果ELB实例没有选择私网，只开启公网，则会在当前负载均衡器所在的VPC中任意选一个子网，优选可用IP多的网络。 4. 批量创建共享型实例的场景，该字段不允许指定。  若指定多个下联面子网，则按顺序优先使用第一个子网来为负载均衡器下联面端口分配ip地址。  下联面子网必须属于该LB所在的VPC。

        :param elb_virsubnet_ids: The elb_virsubnet_ids of this BatchCreateLoadBalancerOption.
        :type elb_virsubnet_ids: list[str]
        """
        self._elb_virsubnet_ids = elb_virsubnet_ids

    @property
    def ip_target_enable(self):
        r"""Gets the ip_target_enable of this BatchCreateLoadBalancerOption.

        参数解释：是否启用跨VPC后端转发。 开启跨VPC后端转发后，后端服务器组不仅支持添加云上VPC内的服务器，还支持添加其他VPC、其他公有云、云下数据中心的服务器。  约束限制： - 开启后不能关闭。 - 使用共享VPC的实例使用此特性时，需确保共享资源所有者已开通VPC对等连接，否则通信异常。 [- 仅独享型负载均衡器支持该特性。](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt) [- 网关型LB不支持该特性。](tag:hws_eu)  取值范围： - true：开启。 - false：不开启。  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :return: The ip_target_enable of this BatchCreateLoadBalancerOption.
        :rtype: bool
        """
        return self._ip_target_enable

    @ip_target_enable.setter
    def ip_target_enable(self, ip_target_enable):
        r"""Sets the ip_target_enable of this BatchCreateLoadBalancerOption.

        参数解释：是否启用跨VPC后端转发。 开启跨VPC后端转发后，后端服务器组不仅支持添加云上VPC内的服务器，还支持添加其他VPC、其他公有云、云下数据中心的服务器。  约束限制： - 开启后不能关闭。 - 使用共享VPC的实例使用此特性时，需确保共享资源所有者已开通VPC对等连接，否则通信异常。 [- 仅独享型负载均衡器支持该特性。](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt) [- 网关型LB不支持该特性。](tag:hws_eu)  取值范围： - true：开启。 - false：不开启。  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :param ip_target_enable: The ip_target_enable of this BatchCreateLoadBalancerOption.
        :type ip_target_enable: bool
        """
        self._ip_target_enable = ip_target_enable

    @property
    def deletion_protection_enable(self):
        r"""Gets the deletion_protection_enable of this BatchCreateLoadBalancerOption.

        是否开启删除保护。 批量创建共享型实例的场景，该字段不允许指定。  取值：false不开启，true开启。默认false不开启。  > 退场时需要先关闭所有资源的删除保护开关。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :return: The deletion_protection_enable of this BatchCreateLoadBalancerOption.
        :rtype: bool
        """
        return self._deletion_protection_enable

    @deletion_protection_enable.setter
    def deletion_protection_enable(self, deletion_protection_enable):
        r"""Sets the deletion_protection_enable of this BatchCreateLoadBalancerOption.

        是否开启删除保护。 批量创建共享型实例的场景，该字段不允许指定。  取值：false不开启，true开启。默认false不开启。  > 退场时需要先关闭所有资源的删除保护开关。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :param deletion_protection_enable: The deletion_protection_enable of this BatchCreateLoadBalancerOption.
        :type deletion_protection_enable: bool
        """
        self._deletion_protection_enable = deletion_protection_enable

    @property
    def prepaid_options(self):
        r"""Gets the prepaid_options of this BatchCreateLoadBalancerOption.

        :return: The prepaid_options of this BatchCreateLoadBalancerOption.
        :rtype: :class:`huaweicloudsdkelb.v3.PrepaidCreateOption`
        """
        return self._prepaid_options

    @prepaid_options.setter
    def prepaid_options(self, prepaid_options):
        r"""Sets the prepaid_options of this BatchCreateLoadBalancerOption.

        :param prepaid_options: The prepaid_options of this BatchCreateLoadBalancerOption.
        :type prepaid_options: :class:`huaweicloudsdkelb.v3.PrepaidCreateOption`
        """
        self._prepaid_options = prepaid_options

    @property
    def autoscaling(self):
        r"""Gets the autoscaling of this BatchCreateLoadBalancerOption.

        :return: The autoscaling of this BatchCreateLoadBalancerOption.
        :rtype: :class:`huaweicloudsdkelb.v3.CreateLoadbalancerAutoscalingOption`
        """
        return self._autoscaling

    @autoscaling.setter
    def autoscaling(self, autoscaling):
        r"""Sets the autoscaling of this BatchCreateLoadBalancerOption.

        :param autoscaling: The autoscaling of this BatchCreateLoadBalancerOption.
        :type autoscaling: :class:`huaweicloudsdkelb.v3.CreateLoadbalancerAutoscalingOption`
        """
        self._autoscaling = autoscaling

    @property
    def waf_failure_action(self):
        r"""Gets the waf_failure_action of this BatchCreateLoadBalancerOption.

        WAF故障时的流量处理策略。discard:丢弃，forward: 转发到后端（默认）  使用说明：只有绑定了waf的LB实例，该字段才会生效。  [不支持该字段，请勿使用。](tag:hws_eu,hws_test,hcs,hcs_sm,hcso,srg,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b,hcso_dt,dt,ocb,ctc,cmcc,tm,ct,sbc,g42,hws_ocb,hk_sbc,hk_tm,hk_g42)

        :return: The waf_failure_action of this BatchCreateLoadBalancerOption.
        :rtype: str
        """
        return self._waf_failure_action

    @waf_failure_action.setter
    def waf_failure_action(self, waf_failure_action):
        r"""Sets the waf_failure_action of this BatchCreateLoadBalancerOption.

        WAF故障时的流量处理策略。discard:丢弃，forward: 转发到后端（默认）  使用说明：只有绑定了waf的LB实例，该字段才会生效。  [不支持该字段，请勿使用。](tag:hws_eu,hws_test,hcs,hcs_sm,hcso,srg,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b,hcso_dt,dt,ocb,ctc,cmcc,tm,ct,sbc,g42,hws_ocb,hk_sbc,hk_tm,hk_g42)

        :param waf_failure_action: The waf_failure_action of this BatchCreateLoadBalancerOption.
        :type waf_failure_action: str
        """
        self._waf_failure_action = waf_failure_action

    @property
    def protection_status(self):
        r"""Gets the protection_status of this BatchCreateLoadBalancerOption.

        修改保护状态, 取值： - nonProtection: 不保护，默认值为nonProtection - consoleProtection: 控制台修改保护

        :return: The protection_status of this BatchCreateLoadBalancerOption.
        :rtype: str
        """
        return self._protection_status

    @protection_status.setter
    def protection_status(self, protection_status):
        r"""Sets the protection_status of this BatchCreateLoadBalancerOption.

        修改保护状态, 取值： - nonProtection: 不保护，默认值为nonProtection - consoleProtection: 控制台修改保护

        :param protection_status: The protection_status of this BatchCreateLoadBalancerOption.
        :type protection_status: str
        """
        self._protection_status = protection_status

    @property
    def protection_reason(self):
        r"""Gets the protection_reason of this BatchCreateLoadBalancerOption.

        参数解释：设置保护的原因。作为protection_status的转态设置的原因。  约束限制：仅当protection_status为consoleProtection时有效。  取值范围：除<和>外通用Unicode字符集字符，最大255个字符。

        :return: The protection_reason of this BatchCreateLoadBalancerOption.
        :rtype: str
        """
        return self._protection_reason

    @protection_reason.setter
    def protection_reason(self, protection_reason):
        r"""Sets the protection_reason of this BatchCreateLoadBalancerOption.

        参数解释：设置保护的原因。作为protection_status的转态设置的原因。  约束限制：仅当protection_status为consoleProtection时有效。  取值范围：除<和>外通用Unicode字符集字符，最大255个字符。

        :param protection_reason: The protection_reason of this BatchCreateLoadBalancerOption.
        :type protection_reason: str
        """
        self._protection_reason = protection_reason

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this BatchCreateLoadBalancerOption.

        创建实例采用的计费模式。flavor: 按实例规格收费，默认值。lcu: 按使用量收费。 批量创建共享型实例时，该字段不允许指定。

        :return: The charge_mode of this BatchCreateLoadBalancerOption.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this BatchCreateLoadBalancerOption.

        创建实例采用的计费模式。flavor: 按实例规格收费，默认值。lcu: 按使用量收费。 批量创建共享型实例时，该字段不允许指定。

        :param charge_mode: The charge_mode of this BatchCreateLoadBalancerOption.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def ipv6_vip_address(self):
        r"""Gets the ipv6_vip_address of this BatchCreateLoadBalancerOption.

        双栈类型负载均衡器的IPv6地址。 当批量创建的number数量大于1时不支持传入该字段，返回400。 批量创建共享型实例的场景，该字段不允许指定。 [不支持IPv6，请勿使用。](tag:dt)

        :return: The ipv6_vip_address of this BatchCreateLoadBalancerOption.
        :rtype: str
        """
        return self._ipv6_vip_address

    @ipv6_vip_address.setter
    def ipv6_vip_address(self, ipv6_vip_address):
        r"""Sets the ipv6_vip_address of this BatchCreateLoadBalancerOption.

        双栈类型负载均衡器的IPv6地址。 当批量创建的number数量大于1时不支持传入该字段，返回400。 批量创建共享型实例的场景，该字段不允许指定。 [不支持IPv6，请勿使用。](tag:dt)

        :param ipv6_vip_address: The ipv6_vip_address of this BatchCreateLoadBalancerOption.
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
        if not isinstance(other, BatchCreateLoadBalancerOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
