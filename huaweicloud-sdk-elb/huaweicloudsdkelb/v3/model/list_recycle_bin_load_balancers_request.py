# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRecycleBinLoadBalancersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'limit': 'int',
        'page_reverse': 'bool',
        'id': 'list[str]',
        'name': 'list[str]',
        'description': 'list[str]',
        'admin_state_up': 'bool',
        'operating_status': 'list[str]',
        'guaranteed': 'bool',
        'vpc_id': 'list[str]',
        'vip_port_id': 'list[str]',
        'vip_address': 'list[str]',
        'vip_subnet_cidr_id': 'list[str]',
        'ipv6_vip_port_id': 'list[str]',
        'ipv6_vip_address': 'list[str]',
        'ipv6_vip_virsubnet_id': 'list[str]',
        'eips': 'list[str]',
        'publicips': 'list[str]',
        'availability_zone_list': 'list[str]',
        'l4_flavor_id': 'list[str]',
        'l7_flavor_id': 'list[str]',
        'billing_info': 'list[str]',
        'member_device_id': 'list[str]',
        'member_address': 'list[str]',
        'enterprise_project_id': 'list[str]',
        'ip_version': 'list[int]',
        'deletion_protection_enable': 'bool',
        'elb_virsubnet_type': 'list[str]',
        'autoscaling': 'list[str]',
        'protection_status': 'list[str]',
        'global_eips': 'list[str]',
        'log_topic_id': 'str',
        'log_group_id': 'str'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'page_reverse': 'page_reverse',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'admin_state_up': 'admin_state_up',
        'operating_status': 'operating_status',
        'guaranteed': 'guaranteed',
        'vpc_id': 'vpc_id',
        'vip_port_id': 'vip_port_id',
        'vip_address': 'vip_address',
        'vip_subnet_cidr_id': 'vip_subnet_cidr_id',
        'ipv6_vip_port_id': 'ipv6_vip_port_id',
        'ipv6_vip_address': 'ipv6_vip_address',
        'ipv6_vip_virsubnet_id': 'ipv6_vip_virsubnet_id',
        'eips': 'eips',
        'publicips': 'publicips',
        'availability_zone_list': 'availability_zone_list',
        'l4_flavor_id': 'l4_flavor_id',
        'l7_flavor_id': 'l7_flavor_id',
        'billing_info': 'billing_info',
        'member_device_id': 'member_device_id',
        'member_address': 'member_address',
        'enterprise_project_id': 'enterprise_project_id',
        'ip_version': 'ip_version',
        'deletion_protection_enable': 'deletion_protection_enable',
        'elb_virsubnet_type': 'elb_virsubnet_type',
        'autoscaling': 'autoscaling',
        'protection_status': 'protection_status',
        'global_eips': 'global_eips',
        'log_topic_id': 'log_topic_id',
        'log_group_id': 'log_group_id'
    }

    def __init__(self, marker=None, limit=None, page_reverse=None, id=None, name=None, description=None, admin_state_up=None, operating_status=None, guaranteed=None, vpc_id=None, vip_port_id=None, vip_address=None, vip_subnet_cidr_id=None, ipv6_vip_port_id=None, ipv6_vip_address=None, ipv6_vip_virsubnet_id=None, eips=None, publicips=None, availability_zone_list=None, l4_flavor_id=None, l7_flavor_id=None, billing_info=None, member_device_id=None, member_address=None, enterprise_project_id=None, ip_version=None, deletion_protection_enable=None, elb_virsubnet_type=None, autoscaling=None, protection_status=None, global_eips=None, log_topic_id=None, log_group_id=None):
        r"""ListRecycleBinLoadBalancersRequest

        The model defined in huaweicloud sdk

        :param marker: **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及
        :type marker: str
        :param limit: **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000
        :type limit: int
        :param page_reverse: **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse&#x3D;true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false
        :type page_reverse: bool
        :param id: 负载均衡器ID。  支持多值查询，查询条件格式：*id&#x3D;xxx&amp;id&#x3D;xxx*。
        :type id: list[str]
        :param name: 负载均衡器名称。  支持多值查询，查询条件格式：*name&#x3D;xxx&amp;name&#x3D;xxx*。
        :type name: list[str]
        :param description: 负载均衡器的描述信息。  支持多值查询，查询条件格式：*description&#x3D;xxx&amp;description&#x3D;xxx*。
        :type description: list[str]
        :param admin_state_up: **参数解释**：负载均衡器的启用状态。  **取值范围**： - true ：启用。 - false：停用。  [不支持该字段，请勿使用。](tag:dt)
        :type admin_state_up: bool
        :param operating_status: 负载均衡器的操作状态。  取值： - ONLINE：正常运行。 - FROZEN：已冻结。  支持多值查询，查询条件格式：*operating_status&#x3D;xxx&amp;operating_status&#x3D;xxx*。
        :type operating_status: list[str]
        :param guaranteed: 是否独享型LB。  取值： - false：共享型 - true：独享型  [仅支持独享型，固定为true。](tag:hws_eu,hcso_dt)
        :type guaranteed: bool
        :param vpc_id: 负载均衡器所在的VPC ID。  支持多值查询，查询条件格式：*vpc_id&#x3D;xxx&amp;vpc_id&#x3D;xxx*。
        :type vpc_id: list[str]
        :param vip_port_id: 负载均衡器的IPv4对应的port ID。  支持多值查询，查询条件格式：*vip_port_id&#x3D;xxx&amp;vip_port_id&#x3D;xxx*。
        :type vip_port_id: list[str]
        :param vip_address: 负载均衡器的IPv4私网IP地址。  支持多值查询，查询条件格式：*vip_address&#x3D;xxx&amp;vip_address&#x3D;xxx*。
        :type vip_address: list[str]
        :param vip_subnet_cidr_id: 负载均衡器所在子网的IPv4子网ID，也称为该负载均衡器实例的前端子网。  支持多值查询，查询条件格式：*vip_subnet_cidr_id&#x3D;xxx&amp;vip_subnet_cidr_id&#x3D;xxx*。
        :type vip_subnet_cidr_id: list[str]
        :param ipv6_vip_port_id: 双栈类型负载均衡器的IPv6对应的port ID。  支持多值查询，查询条件格式：*ipv6_vip_port_id&#x3D;xxx&amp;ipv6_vip_port_id&#x3D;xxx*。  [不支持IPv6，请勿使用。](tag:dt)
        :type ipv6_vip_port_id: list[str]
        :param ipv6_vip_address: 双栈类型负载均衡器的IPv6地址。  支持多值查询，查询条件格式：*ipv6_vip_address&#x3D;xxx&amp;ipv6_vip_address&#x3D;xxx*。  [不支持IPv6，请勿使用。](tag:dt)
        :type ipv6_vip_address: list[str]
        :param ipv6_vip_virsubnet_id: 双栈类型负载均衡器所在的子网IPv6网络ID，也称为该负载均衡器实例的前端子网。  支持多值查询，查询条件格式：*ipv6_vip_virsubnet_id&#x3D;xxx&amp;ipv6_vip_virsubnet_id&#x3D;xxx*。  [不支持IPv6，请勿使用。](tag:dt)
        :type ipv6_vip_virsubnet_id: list[str]
        :param eips: 负载均衡器绑定的EIP。例如要查询绑定以下EIP的LB： \&quot;eips\&quot;: [     {         \&quot;eip_id\&quot;: \&quot;e9b72a9d-4275-455e-a724-853504e4d9c6\&quot;,         \&quot;eip_address\&quot;: \&quot;88.88.14.122\&quot;,         \&quot;ip_version\&quot;: 4     } ] 可以通如下查询： eips&#x3D;ip_version%3D4&amp;eips&#x3D;eip_address%3D88.88.14.122&amp;eips&#x3D;eip_id%3De9b72a9d-4275-455e-a724-853504e4d9c6  支持多值查询，查询条件格式： - eip_id作为查询条件：*eips&#x3D;eip_id&#x3D;xxx&amp;eips&#x3D;eip_id&#x3D;xxx*。 - eip_address作为查询条件：*eips&#x3D;eip_address&#x3D;xxx&amp;eips&#x3D;eip_address&#x3D;xxx*。 - ip_version作为查询条件：*eips&#x3D;ip_version&#x3D;xxx&amp;eips&#x3D;ip_version&#x3D;xxx*。  注：该字段与publicips字段一致。
        :type eips: list[str]
        :param publicips: 负载均衡器绑定的公网IP。例如要查询绑定以下公网IP的LB： \&quot;publicips&#x3D;\&quot;: [     {         \&quot;public_id\&quot;: \&quot;e9b72a9d-4275-455e-a724-853504e4d9c6\&quot;,         \&quot;public_address\&quot;: \&quot;88.88.14.122\&quot;,         \&quot;ip_version\&quot;: 4     } ] 可以通如下查询： publicips&#x3D;ip_version%3D4&amp;publicips&#x3D;public_address%3D88.88.14.122&amp;publicips&#x3D;public_id%3De9b72a9d-4275-455e-a724-853504e4d9c6  支持多值查询，查询条件格式： - publicip_id作为查询条件： *publicips&#x3D;publicip_id&#x3D;xxx&amp;publicips&#x3D;publicip_id&#x3D;xxx* - publicip_address作为查询条件： *publicips&#x3D;publicip_address&#x3D;xxx&amp;publicips&#x3D;publicip_address&#x3D;xxx* - ip_version作为查询条件： *publicips&#x3D;ip_version&#x3D;xxx&amp;publicips&#x3D;ip_version&#x3D;xxx*  注：该字段与eips字段一致。
        :type publicips: list[str]
        :param availability_zone_list: 负载均衡器所在可用区列表。  支持多值查询，查询条件格式： *availability_zone_list&#x3D;xxx&amp;availability_zone_list&#x3D;xxx*。
        :type availability_zone_list: list[str]
        :param l4_flavor_id: 网络型规格ID。  支持多值查询，查询条件格式：*l4_flavor_id&#x3D;xxx&amp;l4_flavor_id&#x3D;xxx*。  [不支持该字段，请勿使用。](tag:hcso,hk_vdf,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b)
        :type l4_flavor_id: list[str]
        :param l7_flavor_id: 应用型规格ID。  支持多值查询，查询条件格式：*l7_flavor_id&#x3D;xxx&amp;l7_flavor_id&#x3D;xxx*。  [不支持该字段，请勿使用。](tag:hcso,hk_vdf,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b)
        :type l7_flavor_id: list[str]
        :param billing_info: 资源账单信息。  支持多值查询，查询条件格式：*billing_info&#x3D;xxx&amp;billing_info&#x3D;xxx*。  [不支持该字段，请勿使用。](tag:hws_hk,hws_eu,hws_test,hcs,hcs_sm,hcso,hk_vdf,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b,hcso_dt,dt,ocb,ctc,cmcc,tm,sbc,g42,hws_ocb,hk_sbc,hk_tm,hk_g42)
        :type billing_info: list[str]
        :param member_device_id: 负载均衡器中的后端服务器对应的弹性云服务器的ID。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_device_id&#x3D;xxx&amp;member_device_id&#x3D;xxx*。
        :type member_device_id: list[str]
        :param member_address: 负载均衡器中的后端服务器对应的弹性云服务器的IP地址。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_address&#x3D;xxx&amp;member_address&#x3D;xxx*。
        :type member_address: list[str]
        :param enterprise_project_id: **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式： *enterprise_project_id&#x3D;xxx&amp;enterprise_project_id&#x3D;xxx*。  **约束限制**： 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:loadbalancers:list权限。 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)
        :type enterprise_project_id: list[str]
        :param ip_version: IP版本信息。  取值：4代表IPv4，6代表IPv6。  支持多值查询，查询条件格式：*ip_version&#x3D;xxx&amp;ip_version&#x3D;xxx*。  [不支持IPv6，请勿设置为6。](tag:dt)
        :type ip_version: list[int]
        :param deletion_protection_enable: 是否开启删除保护，false 不开启，true 开启。[不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)  [荷兰region不支持该字段，请勿使用。](tag:dt)
        :type deletion_protection_enable: bool
        :param elb_virsubnet_type: 下联面子网类型。  取值： - ipv4：ipv4。 - dualstack：双栈。  支持多值查询，查询条件格式： *elb_virsubnet_type&#x3D;ipv4&amp;elb_virsubnet_type&#x3D;dualstack*。
        :type elb_virsubnet_type: list[str]
        :param autoscaling: 是否开启弹性扩缩容。示例如下： \&quot;autoscaling\&quot;: {             \&quot;enable\&quot;: \&quot;true\&quot;         }  支持多值查询，查询条件格式：  *autoscaling&#x3D;enable&#x3D;true&amp;autoscaling&#x3D;enable&#x3D;false*。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42,hcso,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b)
        :type autoscaling: list[str]
        :param protection_status: 修改保护状态, 取值： - nonProtection: 不保护，默认值为nonProtection - consoleProtection: 控制台修改保护
        :type protection_status: list[str]
        :param global_eips: 负载均衡器绑定的公网IP。示例如下：  {     \&quot;global_eips\&quot;: [         {             \&quot;global_eip_id\&quot;: \&quot;24000000-0000-0000-0000-100000000001\&quot;,             \&quot;global_eip_address\&quot;: \&quot;10.10.10.10\&quot;,             \&quot;ip_version\&quot;: 4         }     ] }  支持多值查询，查询条件格式：  - global_eip_id作为查询条件：*global_eips&#x3D;global_eip_id&#x3D;xxx&amp;global_eips&#x3D;global_eip_id&#x3D;xxx*。  - global_eip_address作为查询条件：*global_eips&#x3D;global_eip_address&#x3D;xxx&amp;global_eips&#x3D;global_eip_address&#x3D;xxx*。  - ip_version作为查询条件：*global_eips&#x3D;ip_version&#x3D;xxx&amp;global_eips&#x3D;ip_version&#x3D;xxx*。
        :type global_eips: list[str]
        :param log_topic_id: LB实例绑定的logtank的topic id信息，支持多值查询，查询条件格式：*log_topic_id&#x3D;xxx&amp;log_topic_id&#x3D;xxx*。
        :type log_topic_id: str
        :param log_group_id: LB实例绑定的logtank的group id信息，支持多值查询，查询条件格式：*log_group_id&#x3D;xxx&amp;log_group_id&#x3D;xxx*。
        :type log_group_id: str
        """
        
        

        self._marker = None
        self._limit = None
        self._page_reverse = None
        self._id = None
        self._name = None
        self._description = None
        self._admin_state_up = None
        self._operating_status = None
        self._guaranteed = None
        self._vpc_id = None
        self._vip_port_id = None
        self._vip_address = None
        self._vip_subnet_cidr_id = None
        self._ipv6_vip_port_id = None
        self._ipv6_vip_address = None
        self._ipv6_vip_virsubnet_id = None
        self._eips = None
        self._publicips = None
        self._availability_zone_list = None
        self._l4_flavor_id = None
        self._l7_flavor_id = None
        self._billing_info = None
        self._member_device_id = None
        self._member_address = None
        self._enterprise_project_id = None
        self._ip_version = None
        self._deletion_protection_enable = None
        self._elb_virsubnet_type = None
        self._autoscaling = None
        self._protection_status = None
        self._global_eips = None
        self._log_topic_id = None
        self._log_group_id = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if operating_status is not None:
            self.operating_status = operating_status
        if guaranteed is not None:
            self.guaranteed = guaranteed
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if vip_port_id is not None:
            self.vip_port_id = vip_port_id
        if vip_address is not None:
            self.vip_address = vip_address
        if vip_subnet_cidr_id is not None:
            self.vip_subnet_cidr_id = vip_subnet_cidr_id
        if ipv6_vip_port_id is not None:
            self.ipv6_vip_port_id = ipv6_vip_port_id
        if ipv6_vip_address is not None:
            self.ipv6_vip_address = ipv6_vip_address
        if ipv6_vip_virsubnet_id is not None:
            self.ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id
        if eips is not None:
            self.eips = eips
        if publicips is not None:
            self.publicips = publicips
        if availability_zone_list is not None:
            self.availability_zone_list = availability_zone_list
        if l4_flavor_id is not None:
            self.l4_flavor_id = l4_flavor_id
        if l7_flavor_id is not None:
            self.l7_flavor_id = l7_flavor_id
        if billing_info is not None:
            self.billing_info = billing_info
        if member_device_id is not None:
            self.member_device_id = member_device_id
        if member_address is not None:
            self.member_address = member_address
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if ip_version is not None:
            self.ip_version = ip_version
        if deletion_protection_enable is not None:
            self.deletion_protection_enable = deletion_protection_enable
        if elb_virsubnet_type is not None:
            self.elb_virsubnet_type = elb_virsubnet_type
        if autoscaling is not None:
            self.autoscaling = autoscaling
        if protection_status is not None:
            self.protection_status = protection_status
        if global_eips is not None:
            self.global_eips = global_eips
        if log_topic_id is not None:
            self.log_topic_id = log_topic_id
        if log_group_id is not None:
            self.log_group_id = log_group_id

    @property
    def marker(self):
        r"""Gets the marker of this ListRecycleBinLoadBalancersRequest.

        **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The marker of this ListRecycleBinLoadBalancersRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListRecycleBinLoadBalancersRequest.

        **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及

        :param marker: The marker of this ListRecycleBinLoadBalancersRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListRecycleBinLoadBalancersRequest.

        **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000

        :return: The limit of this ListRecycleBinLoadBalancersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRecycleBinLoadBalancersRequest.

        **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000

        :param limit: The limit of this ListRecycleBinLoadBalancersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def page_reverse(self):
        r"""Gets the page_reverse of this ListRecycleBinLoadBalancersRequest.

        **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false

        :return: The page_reverse of this ListRecycleBinLoadBalancersRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        r"""Sets the page_reverse of this ListRecycleBinLoadBalancersRequest.

        **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false

        :param page_reverse: The page_reverse of this ListRecycleBinLoadBalancersRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        r"""Gets the id of this ListRecycleBinLoadBalancersRequest.

        负载均衡器ID。  支持多值查询，查询条件格式：*id=xxx&id=xxx*。

        :return: The id of this ListRecycleBinLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListRecycleBinLoadBalancersRequest.

        负载均衡器ID。  支持多值查询，查询条件格式：*id=xxx&id=xxx*。

        :param id: The id of this ListRecycleBinLoadBalancersRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListRecycleBinLoadBalancersRequest.

        负载均衡器名称。  支持多值查询，查询条件格式：*name=xxx&name=xxx*。

        :return: The name of this ListRecycleBinLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListRecycleBinLoadBalancersRequest.

        负载均衡器名称。  支持多值查询，查询条件格式：*name=xxx&name=xxx*。

        :param name: The name of this ListRecycleBinLoadBalancersRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ListRecycleBinLoadBalancersRequest.

        负载均衡器的描述信息。  支持多值查询，查询条件格式：*description=xxx&description=xxx*。

        :return: The description of this ListRecycleBinLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListRecycleBinLoadBalancersRequest.

        负载均衡器的描述信息。  支持多值查询，查询条件格式：*description=xxx&description=xxx*。

        :param description: The description of this ListRecycleBinLoadBalancersRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this ListRecycleBinLoadBalancersRequest.

        **参数解释**：负载均衡器的启用状态。  **取值范围**： - true ：启用。 - false：停用。  [不支持该字段，请勿使用。](tag:dt)

        :return: The admin_state_up of this ListRecycleBinLoadBalancersRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this ListRecycleBinLoadBalancersRequest.

        **参数解释**：负载均衡器的启用状态。  **取值范围**： - true ：启用。 - false：停用。  [不支持该字段，请勿使用。](tag:dt)

        :param admin_state_up: The admin_state_up of this ListRecycleBinLoadBalancersRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def operating_status(self):
        r"""Gets the operating_status of this ListRecycleBinLoadBalancersRequest.

        负载均衡器的操作状态。  取值： - ONLINE：正常运行。 - FROZEN：已冻结。  支持多值查询，查询条件格式：*operating_status=xxx&operating_status=xxx*。

        :return: The operating_status of this ListRecycleBinLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        r"""Sets the operating_status of this ListRecycleBinLoadBalancersRequest.

        负载均衡器的操作状态。  取值： - ONLINE：正常运行。 - FROZEN：已冻结。  支持多值查询，查询条件格式：*operating_status=xxx&operating_status=xxx*。

        :param operating_status: The operating_status of this ListRecycleBinLoadBalancersRequest.
        :type operating_status: list[str]
        """
        self._operating_status = operating_status

    @property
    def guaranteed(self):
        r"""Gets the guaranteed of this ListRecycleBinLoadBalancersRequest.

        是否独享型LB。  取值： - false：共享型 - true：独享型  [仅支持独享型，固定为true。](tag:hws_eu,hcso_dt)

        :return: The guaranteed of this ListRecycleBinLoadBalancersRequest.
        :rtype: bool
        """
        return self._guaranteed

    @guaranteed.setter
    def guaranteed(self, guaranteed):
        r"""Sets the guaranteed of this ListRecycleBinLoadBalancersRequest.

        是否独享型LB。  取值： - false：共享型 - true：独享型  [仅支持独享型，固定为true。](tag:hws_eu,hcso_dt)

        :param guaranteed: The guaranteed of this ListRecycleBinLoadBalancersRequest.
        :type guaranteed: bool
        """
        self._guaranteed = guaranteed

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ListRecycleBinLoadBalancersRequest.

        负载均衡器所在的VPC ID。  支持多值查询，查询条件格式：*vpc_id=xxx&vpc_id=xxx*。

        :return: The vpc_id of this ListRecycleBinLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ListRecycleBinLoadBalancersRequest.

        负载均衡器所在的VPC ID。  支持多值查询，查询条件格式：*vpc_id=xxx&vpc_id=xxx*。

        :param vpc_id: The vpc_id of this ListRecycleBinLoadBalancersRequest.
        :type vpc_id: list[str]
        """
        self._vpc_id = vpc_id

    @property
    def vip_port_id(self):
        r"""Gets the vip_port_id of this ListRecycleBinLoadBalancersRequest.

        负载均衡器的IPv4对应的port ID。  支持多值查询，查询条件格式：*vip_port_id=xxx&vip_port_id=xxx*。

        :return: The vip_port_id of this ListRecycleBinLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._vip_port_id

    @vip_port_id.setter
    def vip_port_id(self, vip_port_id):
        r"""Sets the vip_port_id of this ListRecycleBinLoadBalancersRequest.

        负载均衡器的IPv4对应的port ID。  支持多值查询，查询条件格式：*vip_port_id=xxx&vip_port_id=xxx*。

        :param vip_port_id: The vip_port_id of this ListRecycleBinLoadBalancersRequest.
        :type vip_port_id: list[str]
        """
        self._vip_port_id = vip_port_id

    @property
    def vip_address(self):
        r"""Gets the vip_address of this ListRecycleBinLoadBalancersRequest.

        负载均衡器的IPv4私网IP地址。  支持多值查询，查询条件格式：*vip_address=xxx&vip_address=xxx*。

        :return: The vip_address of this ListRecycleBinLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._vip_address

    @vip_address.setter
    def vip_address(self, vip_address):
        r"""Sets the vip_address of this ListRecycleBinLoadBalancersRequest.

        负载均衡器的IPv4私网IP地址。  支持多值查询，查询条件格式：*vip_address=xxx&vip_address=xxx*。

        :param vip_address: The vip_address of this ListRecycleBinLoadBalancersRequest.
        :type vip_address: list[str]
        """
        self._vip_address = vip_address

    @property
    def vip_subnet_cidr_id(self):
        r"""Gets the vip_subnet_cidr_id of this ListRecycleBinLoadBalancersRequest.

        负载均衡器所在子网的IPv4子网ID，也称为该负载均衡器实例的前端子网。  支持多值查询，查询条件格式：*vip_subnet_cidr_id=xxx&vip_subnet_cidr_id=xxx*。

        :return: The vip_subnet_cidr_id of this ListRecycleBinLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._vip_subnet_cidr_id

    @vip_subnet_cidr_id.setter
    def vip_subnet_cidr_id(self, vip_subnet_cidr_id):
        r"""Sets the vip_subnet_cidr_id of this ListRecycleBinLoadBalancersRequest.

        负载均衡器所在子网的IPv4子网ID，也称为该负载均衡器实例的前端子网。  支持多值查询，查询条件格式：*vip_subnet_cidr_id=xxx&vip_subnet_cidr_id=xxx*。

        :param vip_subnet_cidr_id: The vip_subnet_cidr_id of this ListRecycleBinLoadBalancersRequest.
        :type vip_subnet_cidr_id: list[str]
        """
        self._vip_subnet_cidr_id = vip_subnet_cidr_id

    @property
    def ipv6_vip_port_id(self):
        r"""Gets the ipv6_vip_port_id of this ListRecycleBinLoadBalancersRequest.

        双栈类型负载均衡器的IPv6对应的port ID。  支持多值查询，查询条件格式：*ipv6_vip_port_id=xxx&ipv6_vip_port_id=xxx*。  [不支持IPv6，请勿使用。](tag:dt)

        :return: The ipv6_vip_port_id of this ListRecycleBinLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._ipv6_vip_port_id

    @ipv6_vip_port_id.setter
    def ipv6_vip_port_id(self, ipv6_vip_port_id):
        r"""Sets the ipv6_vip_port_id of this ListRecycleBinLoadBalancersRequest.

        双栈类型负载均衡器的IPv6对应的port ID。  支持多值查询，查询条件格式：*ipv6_vip_port_id=xxx&ipv6_vip_port_id=xxx*。  [不支持IPv6，请勿使用。](tag:dt)

        :param ipv6_vip_port_id: The ipv6_vip_port_id of this ListRecycleBinLoadBalancersRequest.
        :type ipv6_vip_port_id: list[str]
        """
        self._ipv6_vip_port_id = ipv6_vip_port_id

    @property
    def ipv6_vip_address(self):
        r"""Gets the ipv6_vip_address of this ListRecycleBinLoadBalancersRequest.

        双栈类型负载均衡器的IPv6地址。  支持多值查询，查询条件格式：*ipv6_vip_address=xxx&ipv6_vip_address=xxx*。  [不支持IPv6，请勿使用。](tag:dt)

        :return: The ipv6_vip_address of this ListRecycleBinLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._ipv6_vip_address

    @ipv6_vip_address.setter
    def ipv6_vip_address(self, ipv6_vip_address):
        r"""Sets the ipv6_vip_address of this ListRecycleBinLoadBalancersRequest.

        双栈类型负载均衡器的IPv6地址。  支持多值查询，查询条件格式：*ipv6_vip_address=xxx&ipv6_vip_address=xxx*。  [不支持IPv6，请勿使用。](tag:dt)

        :param ipv6_vip_address: The ipv6_vip_address of this ListRecycleBinLoadBalancersRequest.
        :type ipv6_vip_address: list[str]
        """
        self._ipv6_vip_address = ipv6_vip_address

    @property
    def ipv6_vip_virsubnet_id(self):
        r"""Gets the ipv6_vip_virsubnet_id of this ListRecycleBinLoadBalancersRequest.

        双栈类型负载均衡器所在的子网IPv6网络ID，也称为该负载均衡器实例的前端子网。  支持多值查询，查询条件格式：*ipv6_vip_virsubnet_id=xxx&ipv6_vip_virsubnet_id=xxx*。  [不支持IPv6，请勿使用。](tag:dt)

        :return: The ipv6_vip_virsubnet_id of this ListRecycleBinLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._ipv6_vip_virsubnet_id

    @ipv6_vip_virsubnet_id.setter
    def ipv6_vip_virsubnet_id(self, ipv6_vip_virsubnet_id):
        r"""Sets the ipv6_vip_virsubnet_id of this ListRecycleBinLoadBalancersRequest.

        双栈类型负载均衡器所在的子网IPv6网络ID，也称为该负载均衡器实例的前端子网。  支持多值查询，查询条件格式：*ipv6_vip_virsubnet_id=xxx&ipv6_vip_virsubnet_id=xxx*。  [不支持IPv6，请勿使用。](tag:dt)

        :param ipv6_vip_virsubnet_id: The ipv6_vip_virsubnet_id of this ListRecycleBinLoadBalancersRequest.
        :type ipv6_vip_virsubnet_id: list[str]
        """
        self._ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id

    @property
    def eips(self):
        r"""Gets the eips of this ListRecycleBinLoadBalancersRequest.

        负载均衡器绑定的EIP。例如要查询绑定以下EIP的LB： \"eips\": [     {         \"eip_id\": \"e9b72a9d-4275-455e-a724-853504e4d9c6\",         \"eip_address\": \"88.88.14.122\",         \"ip_version\": 4     } ] 可以通如下查询： eips=ip_version%3D4&eips=eip_address%3D88.88.14.122&eips=eip_id%3De9b72a9d-4275-455e-a724-853504e4d9c6  支持多值查询，查询条件格式： - eip_id作为查询条件：*eips=eip_id=xxx&eips=eip_id=xxx*。 - eip_address作为查询条件：*eips=eip_address=xxx&eips=eip_address=xxx*。 - ip_version作为查询条件：*eips=ip_version=xxx&eips=ip_version=xxx*。  注：该字段与publicips字段一致。

        :return: The eips of this ListRecycleBinLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._eips

    @eips.setter
    def eips(self, eips):
        r"""Sets the eips of this ListRecycleBinLoadBalancersRequest.

        负载均衡器绑定的EIP。例如要查询绑定以下EIP的LB： \"eips\": [     {         \"eip_id\": \"e9b72a9d-4275-455e-a724-853504e4d9c6\",         \"eip_address\": \"88.88.14.122\",         \"ip_version\": 4     } ] 可以通如下查询： eips=ip_version%3D4&eips=eip_address%3D88.88.14.122&eips=eip_id%3De9b72a9d-4275-455e-a724-853504e4d9c6  支持多值查询，查询条件格式： - eip_id作为查询条件：*eips=eip_id=xxx&eips=eip_id=xxx*。 - eip_address作为查询条件：*eips=eip_address=xxx&eips=eip_address=xxx*。 - ip_version作为查询条件：*eips=ip_version=xxx&eips=ip_version=xxx*。  注：该字段与publicips字段一致。

        :param eips: The eips of this ListRecycleBinLoadBalancersRequest.
        :type eips: list[str]
        """
        self._eips = eips

    @property
    def publicips(self):
        r"""Gets the publicips of this ListRecycleBinLoadBalancersRequest.

        负载均衡器绑定的公网IP。例如要查询绑定以下公网IP的LB： \"publicips=\": [     {         \"public_id\": \"e9b72a9d-4275-455e-a724-853504e4d9c6\",         \"public_address\": \"88.88.14.122\",         \"ip_version\": 4     } ] 可以通如下查询： publicips=ip_version%3D4&publicips=public_address%3D88.88.14.122&publicips=public_id%3De9b72a9d-4275-455e-a724-853504e4d9c6  支持多值查询，查询条件格式： - publicip_id作为查询条件： *publicips=publicip_id=xxx&publicips=publicip_id=xxx* - publicip_address作为查询条件： *publicips=publicip_address=xxx&publicips=publicip_address=xxx* - ip_version作为查询条件： *publicips=ip_version=xxx&publicips=ip_version=xxx*  注：该字段与eips字段一致。

        :return: The publicips of this ListRecycleBinLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._publicips

    @publicips.setter
    def publicips(self, publicips):
        r"""Sets the publicips of this ListRecycleBinLoadBalancersRequest.

        负载均衡器绑定的公网IP。例如要查询绑定以下公网IP的LB： \"publicips=\": [     {         \"public_id\": \"e9b72a9d-4275-455e-a724-853504e4d9c6\",         \"public_address\": \"88.88.14.122\",         \"ip_version\": 4     } ] 可以通如下查询： publicips=ip_version%3D4&publicips=public_address%3D88.88.14.122&publicips=public_id%3De9b72a9d-4275-455e-a724-853504e4d9c6  支持多值查询，查询条件格式： - publicip_id作为查询条件： *publicips=publicip_id=xxx&publicips=publicip_id=xxx* - publicip_address作为查询条件： *publicips=publicip_address=xxx&publicips=publicip_address=xxx* - ip_version作为查询条件： *publicips=ip_version=xxx&publicips=ip_version=xxx*  注：该字段与eips字段一致。

        :param publicips: The publicips of this ListRecycleBinLoadBalancersRequest.
        :type publicips: list[str]
        """
        self._publicips = publicips

    @property
    def availability_zone_list(self):
        r"""Gets the availability_zone_list of this ListRecycleBinLoadBalancersRequest.

        负载均衡器所在可用区列表。  支持多值查询，查询条件格式： *availability_zone_list=xxx&availability_zone_list=xxx*。

        :return: The availability_zone_list of this ListRecycleBinLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._availability_zone_list

    @availability_zone_list.setter
    def availability_zone_list(self, availability_zone_list):
        r"""Sets the availability_zone_list of this ListRecycleBinLoadBalancersRequest.

        负载均衡器所在可用区列表。  支持多值查询，查询条件格式： *availability_zone_list=xxx&availability_zone_list=xxx*。

        :param availability_zone_list: The availability_zone_list of this ListRecycleBinLoadBalancersRequest.
        :type availability_zone_list: list[str]
        """
        self._availability_zone_list = availability_zone_list

    @property
    def l4_flavor_id(self):
        r"""Gets the l4_flavor_id of this ListRecycleBinLoadBalancersRequest.

        网络型规格ID。  支持多值查询，查询条件格式：*l4_flavor_id=xxx&l4_flavor_id=xxx*。  [不支持该字段，请勿使用。](tag:hcso,hk_vdf,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b)

        :return: The l4_flavor_id of this ListRecycleBinLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._l4_flavor_id

    @l4_flavor_id.setter
    def l4_flavor_id(self, l4_flavor_id):
        r"""Sets the l4_flavor_id of this ListRecycleBinLoadBalancersRequest.

        网络型规格ID。  支持多值查询，查询条件格式：*l4_flavor_id=xxx&l4_flavor_id=xxx*。  [不支持该字段，请勿使用。](tag:hcso,hk_vdf,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b)

        :param l4_flavor_id: The l4_flavor_id of this ListRecycleBinLoadBalancersRequest.
        :type l4_flavor_id: list[str]
        """
        self._l4_flavor_id = l4_flavor_id

    @property
    def l7_flavor_id(self):
        r"""Gets the l7_flavor_id of this ListRecycleBinLoadBalancersRequest.

        应用型规格ID。  支持多值查询，查询条件格式：*l7_flavor_id=xxx&l7_flavor_id=xxx*。  [不支持该字段，请勿使用。](tag:hcso,hk_vdf,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b)

        :return: The l7_flavor_id of this ListRecycleBinLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._l7_flavor_id

    @l7_flavor_id.setter
    def l7_flavor_id(self, l7_flavor_id):
        r"""Sets the l7_flavor_id of this ListRecycleBinLoadBalancersRequest.

        应用型规格ID。  支持多值查询，查询条件格式：*l7_flavor_id=xxx&l7_flavor_id=xxx*。  [不支持该字段，请勿使用。](tag:hcso,hk_vdf,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b)

        :param l7_flavor_id: The l7_flavor_id of this ListRecycleBinLoadBalancersRequest.
        :type l7_flavor_id: list[str]
        """
        self._l7_flavor_id = l7_flavor_id

    @property
    def billing_info(self):
        r"""Gets the billing_info of this ListRecycleBinLoadBalancersRequest.

        资源账单信息。  支持多值查询，查询条件格式：*billing_info=xxx&billing_info=xxx*。  [不支持该字段，请勿使用。](tag:hws_hk,hws_eu,hws_test,hcs,hcs_sm,hcso,hk_vdf,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b,hcso_dt,dt,ocb,ctc,cmcc,tm,sbc,g42,hws_ocb,hk_sbc,hk_tm,hk_g42)

        :return: The billing_info of this ListRecycleBinLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        r"""Sets the billing_info of this ListRecycleBinLoadBalancersRequest.

        资源账单信息。  支持多值查询，查询条件格式：*billing_info=xxx&billing_info=xxx*。  [不支持该字段，请勿使用。](tag:hws_hk,hws_eu,hws_test,hcs,hcs_sm,hcso,hk_vdf,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b,hcso_dt,dt,ocb,ctc,cmcc,tm,sbc,g42,hws_ocb,hk_sbc,hk_tm,hk_g42)

        :param billing_info: The billing_info of this ListRecycleBinLoadBalancersRequest.
        :type billing_info: list[str]
        """
        self._billing_info = billing_info

    @property
    def member_device_id(self):
        r"""Gets the member_device_id of this ListRecycleBinLoadBalancersRequest.

        负载均衡器中的后端服务器对应的弹性云服务器的ID。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_device_id=xxx&member_device_id=xxx*。

        :return: The member_device_id of this ListRecycleBinLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._member_device_id

    @member_device_id.setter
    def member_device_id(self, member_device_id):
        r"""Sets the member_device_id of this ListRecycleBinLoadBalancersRequest.

        负载均衡器中的后端服务器对应的弹性云服务器的ID。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_device_id=xxx&member_device_id=xxx*。

        :param member_device_id: The member_device_id of this ListRecycleBinLoadBalancersRequest.
        :type member_device_id: list[str]
        """
        self._member_device_id = member_device_id

    @property
    def member_address(self):
        r"""Gets the member_address of this ListRecycleBinLoadBalancersRequest.

        负载均衡器中的后端服务器对应的弹性云服务器的IP地址。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_address=xxx&member_address=xxx*。

        :return: The member_address of this ListRecycleBinLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._member_address

    @member_address.setter
    def member_address(self, member_address):
        r"""Sets the member_address of this ListRecycleBinLoadBalancersRequest.

        负载均衡器中的后端服务器对应的弹性云服务器的IP地址。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_address=xxx&member_address=xxx*。

        :param member_address: The member_address of this ListRecycleBinLoadBalancersRequest.
        :type member_address: list[str]
        """
        self._member_address = member_address

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListRecycleBinLoadBalancersRequest.

        **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式： *enterprise_project_id=xxx&enterprise_project_id=xxx*。  **约束限制**： 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:loadbalancers:list权限。 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :return: The enterprise_project_id of this ListRecycleBinLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListRecycleBinLoadBalancersRequest.

        **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式： *enterprise_project_id=xxx&enterprise_project_id=xxx*。  **约束限制**： 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:loadbalancers:list权限。 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :param enterprise_project_id: The enterprise_project_id of this ListRecycleBinLoadBalancersRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def ip_version(self):
        r"""Gets the ip_version of this ListRecycleBinLoadBalancersRequest.

        IP版本信息。  取值：4代表IPv4，6代表IPv6。  支持多值查询，查询条件格式：*ip_version=xxx&ip_version=xxx*。  [不支持IPv6，请勿设置为6。](tag:dt)

        :return: The ip_version of this ListRecycleBinLoadBalancersRequest.
        :rtype: list[int]
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this ListRecycleBinLoadBalancersRequest.

        IP版本信息。  取值：4代表IPv4，6代表IPv6。  支持多值查询，查询条件格式：*ip_version=xxx&ip_version=xxx*。  [不支持IPv6，请勿设置为6。](tag:dt)

        :param ip_version: The ip_version of this ListRecycleBinLoadBalancersRequest.
        :type ip_version: list[int]
        """
        self._ip_version = ip_version

    @property
    def deletion_protection_enable(self):
        r"""Gets the deletion_protection_enable of this ListRecycleBinLoadBalancersRequest.

        是否开启删除保护，false 不开启，true 开启。[不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :return: The deletion_protection_enable of this ListRecycleBinLoadBalancersRequest.
        :rtype: bool
        """
        return self._deletion_protection_enable

    @deletion_protection_enable.setter
    def deletion_protection_enable(self, deletion_protection_enable):
        r"""Sets the deletion_protection_enable of this ListRecycleBinLoadBalancersRequest.

        是否开启删除保护，false 不开启，true 开启。[不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :param deletion_protection_enable: The deletion_protection_enable of this ListRecycleBinLoadBalancersRequest.
        :type deletion_protection_enable: bool
        """
        self._deletion_protection_enable = deletion_protection_enable

    @property
    def elb_virsubnet_type(self):
        r"""Gets the elb_virsubnet_type of this ListRecycleBinLoadBalancersRequest.

        下联面子网类型。  取值： - ipv4：ipv4。 - dualstack：双栈。  支持多值查询，查询条件格式： *elb_virsubnet_type=ipv4&elb_virsubnet_type=dualstack*。

        :return: The elb_virsubnet_type of this ListRecycleBinLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._elb_virsubnet_type

    @elb_virsubnet_type.setter
    def elb_virsubnet_type(self, elb_virsubnet_type):
        r"""Sets the elb_virsubnet_type of this ListRecycleBinLoadBalancersRequest.

        下联面子网类型。  取值： - ipv4：ipv4。 - dualstack：双栈。  支持多值查询，查询条件格式： *elb_virsubnet_type=ipv4&elb_virsubnet_type=dualstack*。

        :param elb_virsubnet_type: The elb_virsubnet_type of this ListRecycleBinLoadBalancersRequest.
        :type elb_virsubnet_type: list[str]
        """
        self._elb_virsubnet_type = elb_virsubnet_type

    @property
    def autoscaling(self):
        r"""Gets the autoscaling of this ListRecycleBinLoadBalancersRequest.

        是否开启弹性扩缩容。示例如下： \"autoscaling\": {             \"enable\": \"true\"         }  支持多值查询，查询条件格式：  *autoscaling=enable=true&autoscaling=enable=false*。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42,hcso,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b)

        :return: The autoscaling of this ListRecycleBinLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._autoscaling

    @autoscaling.setter
    def autoscaling(self, autoscaling):
        r"""Sets the autoscaling of this ListRecycleBinLoadBalancersRequest.

        是否开启弹性扩缩容。示例如下： \"autoscaling\": {             \"enable\": \"true\"         }  支持多值查询，查询条件格式：  *autoscaling=enable=true&autoscaling=enable=false*。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42,hcso,fcs,fcs_vm,mix,hcso_g42,hcso_g42_b)

        :param autoscaling: The autoscaling of this ListRecycleBinLoadBalancersRequest.
        :type autoscaling: list[str]
        """
        self._autoscaling = autoscaling

    @property
    def protection_status(self):
        r"""Gets the protection_status of this ListRecycleBinLoadBalancersRequest.

        修改保护状态, 取值： - nonProtection: 不保护，默认值为nonProtection - consoleProtection: 控制台修改保护

        :return: The protection_status of this ListRecycleBinLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._protection_status

    @protection_status.setter
    def protection_status(self, protection_status):
        r"""Sets the protection_status of this ListRecycleBinLoadBalancersRequest.

        修改保护状态, 取值： - nonProtection: 不保护，默认值为nonProtection - consoleProtection: 控制台修改保护

        :param protection_status: The protection_status of this ListRecycleBinLoadBalancersRequest.
        :type protection_status: list[str]
        """
        self._protection_status = protection_status

    @property
    def global_eips(self):
        r"""Gets the global_eips of this ListRecycleBinLoadBalancersRequest.

        负载均衡器绑定的公网IP。示例如下：  {     \"global_eips\": [         {             \"global_eip_id\": \"24000000-0000-0000-0000-100000000001\",             \"global_eip_address\": \"10.10.10.10\",             \"ip_version\": 4         }     ] }  支持多值查询，查询条件格式：  - global_eip_id作为查询条件：*global_eips=global_eip_id=xxx&global_eips=global_eip_id=xxx*。  - global_eip_address作为查询条件：*global_eips=global_eip_address=xxx&global_eips=global_eip_address=xxx*。  - ip_version作为查询条件：*global_eips=ip_version=xxx&global_eips=ip_version=xxx*。

        :return: The global_eips of this ListRecycleBinLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._global_eips

    @global_eips.setter
    def global_eips(self, global_eips):
        r"""Sets the global_eips of this ListRecycleBinLoadBalancersRequest.

        负载均衡器绑定的公网IP。示例如下：  {     \"global_eips\": [         {             \"global_eip_id\": \"24000000-0000-0000-0000-100000000001\",             \"global_eip_address\": \"10.10.10.10\",             \"ip_version\": 4         }     ] }  支持多值查询，查询条件格式：  - global_eip_id作为查询条件：*global_eips=global_eip_id=xxx&global_eips=global_eip_id=xxx*。  - global_eip_address作为查询条件：*global_eips=global_eip_address=xxx&global_eips=global_eip_address=xxx*。  - ip_version作为查询条件：*global_eips=ip_version=xxx&global_eips=ip_version=xxx*。

        :param global_eips: The global_eips of this ListRecycleBinLoadBalancersRequest.
        :type global_eips: list[str]
        """
        self._global_eips = global_eips

    @property
    def log_topic_id(self):
        r"""Gets the log_topic_id of this ListRecycleBinLoadBalancersRequest.

        LB实例绑定的logtank的topic id信息，支持多值查询，查询条件格式：*log_topic_id=xxx&log_topic_id=xxx*。

        :return: The log_topic_id of this ListRecycleBinLoadBalancersRequest.
        :rtype: str
        """
        return self._log_topic_id

    @log_topic_id.setter
    def log_topic_id(self, log_topic_id):
        r"""Sets the log_topic_id of this ListRecycleBinLoadBalancersRequest.

        LB实例绑定的logtank的topic id信息，支持多值查询，查询条件格式：*log_topic_id=xxx&log_topic_id=xxx*。

        :param log_topic_id: The log_topic_id of this ListRecycleBinLoadBalancersRequest.
        :type log_topic_id: str
        """
        self._log_topic_id = log_topic_id

    @property
    def log_group_id(self):
        r"""Gets the log_group_id of this ListRecycleBinLoadBalancersRequest.

        LB实例绑定的logtank的group id信息，支持多值查询，查询条件格式：*log_group_id=xxx&log_group_id=xxx*。

        :return: The log_group_id of this ListRecycleBinLoadBalancersRequest.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        r"""Sets the log_group_id of this ListRecycleBinLoadBalancersRequest.

        LB实例绑定的logtank的group id信息，支持多值查询，查询条件格式：*log_group_id=xxx&log_group_id=xxx*。

        :param log_group_id: The log_group_id of this ListRecycleBinLoadBalancersRequest.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

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
        if not isinstance(other, ListRecycleBinLoadBalancersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
