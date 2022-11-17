# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLoadBalancersRequest:

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
        'provisioning_status': 'list[str]',
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
        'l4_scale_flavor_id': 'list[str]',
        'l7_flavor_id': 'list[str]',
        'l7_scale_flavor_id': 'list[str]',
        'billing_info': 'list[str]',
        'member_device_id': 'list[str]',
        'member_address': 'list[str]',
        'enterprise_project_id': 'list[str]',
        'ip_version': 'list[int]',
        'deletion_protection_enable': 'bool',
        'elb_virsubnet_type': 'list[str]',
        'autoscaling': 'list[str]'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'page_reverse': 'page_reverse',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'admin_state_up': 'admin_state_up',
        'provisioning_status': 'provisioning_status',
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
        'l4_scale_flavor_id': 'l4_scale_flavor_id',
        'l7_flavor_id': 'l7_flavor_id',
        'l7_scale_flavor_id': 'l7_scale_flavor_id',
        'billing_info': 'billing_info',
        'member_device_id': 'member_device_id',
        'member_address': 'member_address',
        'enterprise_project_id': 'enterprise_project_id',
        'ip_version': 'ip_version',
        'deletion_protection_enable': 'deletion_protection_enable',
        'elb_virsubnet_type': 'elb_virsubnet_type',
        'autoscaling': 'autoscaling'
    }

    def __init__(self, marker=None, limit=None, page_reverse=None, id=None, name=None, description=None, admin_state_up=None, provisioning_status=None, operating_status=None, guaranteed=None, vpc_id=None, vip_port_id=None, vip_address=None, vip_subnet_cidr_id=None, ipv6_vip_port_id=None, ipv6_vip_address=None, ipv6_vip_virsubnet_id=None, eips=None, publicips=None, availability_zone_list=None, l4_flavor_id=None, l4_scale_flavor_id=None, l7_flavor_id=None, l7_scale_flavor_id=None, billing_info=None, member_device_id=None, member_address=None, enterprise_project_id=None, ip_version=None, deletion_protection_enable=None, elb_virsubnet_type=None, autoscaling=None):
        """ListLoadBalancersRequest

        The model defined in huaweicloud sdk

        :param marker: 上一页最后一条记录的ID。  使用说明： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。
        :type marker: str
        :param limit: 每页返回的个数。
        :type limit: int
        :param page_reverse: 是否反向查询。  取值： - true：查询上一页。 - false：查询下一页，默认。  使用说明： - 必须与limit一起使用。 - 当page_reverse&#x3D;true时，若要查询上一页，marker取值为当前页返回值的previous_marker。
        :type page_reverse: bool
        :param id: 负载均衡器ID。  支持多值查询，查询条件格式：*id&#x3D;xxx&amp;id&#x3D;xxx*。
        :type id: list[str]
        :param name: 负载均衡器名称。  支持多值查询，查询条件格式：*name&#x3D;xxx&amp;name&#x3D;xxx*。
        :type name: list[str]
        :param description: 负载均衡器的描述信息。  支持多值查询，查询条件格式：*description&#x3D;xxx&amp;description&#x3D;xxx*。
        :type description: list[str]
        :param admin_state_up: 负载均衡器的管理状态。  不支持该字段，请勿使用。
        :type admin_state_up: bool
        :param provisioning_status: 负载均衡器的配置状态。  取值： - ACTIVE：使用中。 - PENDING_DELETE：删除中。  支持多值查询，查询条件格式：*provisioning_status&#x3D;xxx&amp;provisioning_status&#x3D;xxx*。
        :type provisioning_status: list[str]
        :param operating_status: 负载均衡器的操作状态。  取值： - ONLINE：正常运行。 - FROZEN：已冻结。  支持多值查询，查询条件格式：*operating_status&#x3D;xxx&amp;operating_status&#x3D;xxx*。
        :type operating_status: list[str]
        :param guaranteed: 是否独享型LB。  取值： - false：共享型 - true：独享型  [仅支持独享型，固定为true。](tag:hws_eu,hcso_dt)
        :type guaranteed: bool
        :param vpc_id: 负载均衡器所在的VPC ID。  支持多值查询，查询条件格式：*vpc_id&#x3D;xxx&amp;vpc_id&#x3D;xxx*。
        :type vpc_id: list[str]
        :param vip_port_id: 负载均衡器的IPv4对应的port ID。  支持多值查询，查询条件格式：*vip_port_id&#x3D;xxx&amp;vip_port_id&#x3D;xxx*。
        :type vip_port_id: list[str]
        :param vip_address: 负载均衡器的IPv4虚拟IP地址。  支持多值查询，查询条件格式：*vip_address&#x3D;xxx&amp;vip_address&#x3D;xxx*。
        :type vip_address: list[str]
        :param vip_subnet_cidr_id: 负载均衡器所在子网的IPv4子网ID。  支持多值查询，查询条件格式：*vip_subnet_cidr_id&#x3D;xxx&amp;vip_subnet_cidr_id&#x3D;xxx*。
        :type vip_subnet_cidr_id: list[str]
        :param ipv6_vip_port_id: 双栈类型负载均衡器的IPv6对应的port ID。  支持多值查询，查询条件格式：*ipv6_vip_port_id&#x3D;xxx&amp;ipv6_vip_port_id&#x3D;xxx*。  [不支持IPv6，请勿使用。](tag:dt,dt_test)
        :type ipv6_vip_port_id: list[str]
        :param ipv6_vip_address: 双栈类型负载均衡器的IPv6地址。  支持多值查询，查询条件格式：*ipv6_vip_address&#x3D;xxx&amp;ipv6_vip_address&#x3D;xxx*。  [不支持IPv6，请勿使用。](tag:dt,dt_test)
        :type ipv6_vip_address: list[str]
        :param ipv6_vip_virsubnet_id: 双栈类型负载均衡器所在的子网IPv6网络ID。  支持多值查询，查询条件格式：*ipv6_vip_virsubnet_id&#x3D;xxx&amp;ipv6_vip_virsubnet_id&#x3D;xxx*。  [不支持IPv6，请勿使用。](tag:dt,dt_test)
        :type ipv6_vip_virsubnet_id: list[str]
        :param eips: 负载均衡器绑定的EIP。示例如下： \&quot;eips\&quot;: [             {                 \&quot;eip_id\&quot;: \&quot;e9b72a9d-4275-455e-a724-853504e4d9c6\&quot;,                 \&quot;eip_address\&quot;: \&quot;88.88.14.122\&quot;,                 \&quot;ip_version\&quot;: 4             }         ]  支持多值查询，查询条件格式： - eip_id作为查询条件：*eips&#x3D;eip_id&#x3D;xxx&amp;eips&#x3D;eip_id&#x3D;xxx*。 - eip_address作为查询条件：*eips&#x3D;eip_address&#x3D;xxx&amp;eips&#x3D;eip_address&#x3D;xxx*。 - ip_version作为查询条件：*eips&#x3D;ip_version&#x3D;xxx&amp;eips&#x3D;ip_version&#x3D;xxx*。  注：该字段与publicips字段一致。
        :type eips: list[str]
        :param publicips: 负载均衡器绑定的公网IP。示例如下：  \&quot;publicips\&quot;: [                 {                     \&quot;publicip_id\&quot;: \&quot;e9b72a9d-4275-455e-a724-853504e4d9c6\&quot;,                     \&quot;publicip_address\&quot;: \&quot;88.88.14.122\&quot;,                     \&quot;ip_version\&quot;: 4                 }             ]  支持多值查询，查询条件格式： - publicip_id作为查询条件： *publicips&#x3D;publicip_id&#x3D;xxx&amp;publicips&#x3D;publicip_id&#x3D;xxx* - publicip_address作为查询条件： *publicips&#x3D;publicip_address&#x3D;xxx&amp;publicips&#x3D;publicip_address&#x3D;xxx* - ip_version作为查询条件： *publicips&#x3D;ip_version&#x3D;xxx&amp;publicips&#x3D;ip_version&#x3D;xxx*  注：该字段与eips字段一致。
        :type publicips: list[str]
        :param availability_zone_list: 负载均衡器所在可用区列表。  支持多值查询，查询条件格式： *availability_zone_list&#x3D;xxx&amp;availability_zone_list&#x3D;xxx*。
        :type availability_zone_list: list[str]
        :param l4_flavor_id: 四层Flavor ID。  支持多值查询，查询条件格式：*l4_flavor_id&#x3D;xxx&amp;l4_flavor_id&#x3D;xxx*。
        :type l4_flavor_id: list[str]
        :param l4_scale_flavor_id: 四层弹性Flavor ID。  支持多值查询，查询条件格式：*l4_scale_flavor_id&#x3D;xxx&amp;l4_scale_flavor_id&#x3D;xxx*。  不支持该字段，请勿使用。
        :type l4_scale_flavor_id: list[str]
        :param l7_flavor_id: 七层Flavor ID。  支持多值查询，查询条件格式：*l7_flavor_id&#x3D;xxx&amp;l7_flavor_id&#x3D;xxx*。
        :type l7_flavor_id: list[str]
        :param l7_scale_flavor_id: 七层弹性Flavor ID。  支持多值查询，查询条件格式：*l7_scale_flavor_id&#x3D;xxx&amp;l7_scale_flavor_id&#x3D;xxx*。  不支持该字段，请勿使用。
        :type l7_scale_flavor_id: list[str]
        :param billing_info: 资源账单信息。  支持多值查询，查询条件格式：*billing_info&#x3D;xxx&amp;billing_info&#x3D;xxx*。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42,dt,dt_test,hcso_dt)
        :type billing_info: list[str]
        :param member_device_id: 负载均衡器中的后端云服务器对应的弹性云服务器的ID。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_device_id&#x3D;xxx&amp;member_device_id&#x3D;xxx*。
        :type member_device_id: list[str]
        :param member_address: 负载均衡器中的后端云服务器对应的弹性云服务器的IP地址。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_address&#x3D;xxx&amp;member_address&#x3D;xxx*。
        :type member_address: list[str]
        :param enterprise_project_id: 负载均衡器所属的企业项目ID。 查询时若不传，则查询default企业项目下的资源，鉴权按照default企业项目鉴权。 如果传值，则必须传已存在的企业项目ID（不可为\&quot;0\&quot;）或传all_granted_eps表示查询所有企业项目。  支持多值查询，查询条件格式： *enterprise_project_id&#x3D;xxx&amp;enterprise_project_id&#x3D;xxx*。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)
        :type enterprise_project_id: list[str]
        :param ip_version: IP版本信息。  取值：4代表IPv4，6代表IPv6。  支持多值查询，查询条件格式：*ip_version&#x3D;xxx&amp;ip_version&#x3D;xxx*。  [不支持IPv6，请勿设置为6。](tag:dt,dt_test)
        :type ip_version: list[int]
        :param deletion_protection_enable: 是否开启删除保护，false不开启，true开启。[不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)
        :type deletion_protection_enable: bool
        :param elb_virsubnet_type: 下联面子网类型。  取值： - ipv4：ipv4。 - dualstack：双栈。  支持多值查询，查询条件格式： *elb_virsubnet_type&#x3D;ipv4&amp;elb_virsubnet_type&#x3D;dualstack*。
        :type elb_virsubnet_type: list[str]
        :param autoscaling: 是否开启弹性扩缩容。示例如下： \&quot;autoscaling\&quot;: {             \&quot;enable\&quot;: \&quot;true\&quot;         }  支持多值查询，查询条件格式：  *autoscaling&#x3D;enable&#x3D;true&amp;autoscaling&#x3D;enable&#x3D;false*。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)
        :type autoscaling: list[str]
        """
        
        

        self._marker = None
        self._limit = None
        self._page_reverse = None
        self._id = None
        self._name = None
        self._description = None
        self._admin_state_up = None
        self._provisioning_status = None
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
        self._l4_scale_flavor_id = None
        self._l7_flavor_id = None
        self._l7_scale_flavor_id = None
        self._billing_info = None
        self._member_device_id = None
        self._member_address = None
        self._enterprise_project_id = None
        self._ip_version = None
        self._deletion_protection_enable = None
        self._elb_virsubnet_type = None
        self._autoscaling = None
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
        if provisioning_status is not None:
            self.provisioning_status = provisioning_status
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
        if l4_scale_flavor_id is not None:
            self.l4_scale_flavor_id = l4_scale_flavor_id
        if l7_flavor_id is not None:
            self.l7_flavor_id = l7_flavor_id
        if l7_scale_flavor_id is not None:
            self.l7_scale_flavor_id = l7_scale_flavor_id
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

    @property
    def marker(self):
        """Gets the marker of this ListLoadBalancersRequest.

        上一页最后一条记录的ID。  使用说明： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。

        :return: The marker of this ListLoadBalancersRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListLoadBalancersRequest.

        上一页最后一条记录的ID。  使用说明： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。

        :param marker: The marker of this ListLoadBalancersRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        """Gets the limit of this ListLoadBalancersRequest.

        每页返回的个数。

        :return: The limit of this ListLoadBalancersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListLoadBalancersRequest.

        每页返回的个数。

        :param limit: The limit of this ListLoadBalancersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListLoadBalancersRequest.

        是否反向查询。  取值： - true：查询上一页。 - false：查询下一页，默认。  使用说明： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。

        :return: The page_reverse of this ListLoadBalancersRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListLoadBalancersRequest.

        是否反向查询。  取值： - true：查询上一页。 - false：查询下一页，默认。  使用说明： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。

        :param page_reverse: The page_reverse of this ListLoadBalancersRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        """Gets the id of this ListLoadBalancersRequest.

        负载均衡器ID。  支持多值查询，查询条件格式：*id=xxx&id=xxx*。

        :return: The id of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListLoadBalancersRequest.

        负载均衡器ID。  支持多值查询，查询条件格式：*id=xxx&id=xxx*。

        :param id: The id of this ListLoadBalancersRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListLoadBalancersRequest.

        负载均衡器名称。  支持多值查询，查询条件格式：*name=xxx&name=xxx*。

        :return: The name of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListLoadBalancersRequest.

        负载均衡器名称。  支持多值查询，查询条件格式：*name=xxx&name=xxx*。

        :param name: The name of this ListLoadBalancersRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ListLoadBalancersRequest.

        负载均衡器的描述信息。  支持多值查询，查询条件格式：*description=xxx&description=xxx*。

        :return: The description of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListLoadBalancersRequest.

        负载均衡器的描述信息。  支持多值查询，查询条件格式：*description=xxx&description=xxx*。

        :param description: The description of this ListLoadBalancersRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListLoadBalancersRequest.

        负载均衡器的管理状态。  不支持该字段，请勿使用。

        :return: The admin_state_up of this ListLoadBalancersRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListLoadBalancersRequest.

        负载均衡器的管理状态。  不支持该字段，请勿使用。

        :param admin_state_up: The admin_state_up of this ListLoadBalancersRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this ListLoadBalancersRequest.

        负载均衡器的配置状态。  取值： - ACTIVE：使用中。 - PENDING_DELETE：删除中。  支持多值查询，查询条件格式：*provisioning_status=xxx&provisioning_status=xxx*。

        :return: The provisioning_status of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this ListLoadBalancersRequest.

        负载均衡器的配置状态。  取值： - ACTIVE：使用中。 - PENDING_DELETE：删除中。  支持多值查询，查询条件格式：*provisioning_status=xxx&provisioning_status=xxx*。

        :param provisioning_status: The provisioning_status of this ListLoadBalancersRequest.
        :type provisioning_status: list[str]
        """
        self._provisioning_status = provisioning_status

    @property
    def operating_status(self):
        """Gets the operating_status of this ListLoadBalancersRequest.

        负载均衡器的操作状态。  取值： - ONLINE：正常运行。 - FROZEN：已冻结。  支持多值查询，查询条件格式：*operating_status=xxx&operating_status=xxx*。

        :return: The operating_status of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        """Sets the operating_status of this ListLoadBalancersRequest.

        负载均衡器的操作状态。  取值： - ONLINE：正常运行。 - FROZEN：已冻结。  支持多值查询，查询条件格式：*operating_status=xxx&operating_status=xxx*。

        :param operating_status: The operating_status of this ListLoadBalancersRequest.
        :type operating_status: list[str]
        """
        self._operating_status = operating_status

    @property
    def guaranteed(self):
        """Gets the guaranteed of this ListLoadBalancersRequest.

        是否独享型LB。  取值： - false：共享型 - true：独享型  [仅支持独享型，固定为true。](tag:hws_eu,hcso_dt)

        :return: The guaranteed of this ListLoadBalancersRequest.
        :rtype: bool
        """
        return self._guaranteed

    @guaranteed.setter
    def guaranteed(self, guaranteed):
        """Sets the guaranteed of this ListLoadBalancersRequest.

        是否独享型LB。  取值： - false：共享型 - true：独享型  [仅支持独享型，固定为true。](tag:hws_eu,hcso_dt)

        :param guaranteed: The guaranteed of this ListLoadBalancersRequest.
        :type guaranteed: bool
        """
        self._guaranteed = guaranteed

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ListLoadBalancersRequest.

        负载均衡器所在的VPC ID。  支持多值查询，查询条件格式：*vpc_id=xxx&vpc_id=xxx*。

        :return: The vpc_id of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ListLoadBalancersRequest.

        负载均衡器所在的VPC ID。  支持多值查询，查询条件格式：*vpc_id=xxx&vpc_id=xxx*。

        :param vpc_id: The vpc_id of this ListLoadBalancersRequest.
        :type vpc_id: list[str]
        """
        self._vpc_id = vpc_id

    @property
    def vip_port_id(self):
        """Gets the vip_port_id of this ListLoadBalancersRequest.

        负载均衡器的IPv4对应的port ID。  支持多值查询，查询条件格式：*vip_port_id=xxx&vip_port_id=xxx*。

        :return: The vip_port_id of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._vip_port_id

    @vip_port_id.setter
    def vip_port_id(self, vip_port_id):
        """Sets the vip_port_id of this ListLoadBalancersRequest.

        负载均衡器的IPv4对应的port ID。  支持多值查询，查询条件格式：*vip_port_id=xxx&vip_port_id=xxx*。

        :param vip_port_id: The vip_port_id of this ListLoadBalancersRequest.
        :type vip_port_id: list[str]
        """
        self._vip_port_id = vip_port_id

    @property
    def vip_address(self):
        """Gets the vip_address of this ListLoadBalancersRequest.

        负载均衡器的IPv4虚拟IP地址。  支持多值查询，查询条件格式：*vip_address=xxx&vip_address=xxx*。

        :return: The vip_address of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._vip_address

    @vip_address.setter
    def vip_address(self, vip_address):
        """Sets the vip_address of this ListLoadBalancersRequest.

        负载均衡器的IPv4虚拟IP地址。  支持多值查询，查询条件格式：*vip_address=xxx&vip_address=xxx*。

        :param vip_address: The vip_address of this ListLoadBalancersRequest.
        :type vip_address: list[str]
        """
        self._vip_address = vip_address

    @property
    def vip_subnet_cidr_id(self):
        """Gets the vip_subnet_cidr_id of this ListLoadBalancersRequest.

        负载均衡器所在子网的IPv4子网ID。  支持多值查询，查询条件格式：*vip_subnet_cidr_id=xxx&vip_subnet_cidr_id=xxx*。

        :return: The vip_subnet_cidr_id of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._vip_subnet_cidr_id

    @vip_subnet_cidr_id.setter
    def vip_subnet_cidr_id(self, vip_subnet_cidr_id):
        """Sets the vip_subnet_cidr_id of this ListLoadBalancersRequest.

        负载均衡器所在子网的IPv4子网ID。  支持多值查询，查询条件格式：*vip_subnet_cidr_id=xxx&vip_subnet_cidr_id=xxx*。

        :param vip_subnet_cidr_id: The vip_subnet_cidr_id of this ListLoadBalancersRequest.
        :type vip_subnet_cidr_id: list[str]
        """
        self._vip_subnet_cidr_id = vip_subnet_cidr_id

    @property
    def ipv6_vip_port_id(self):
        """Gets the ipv6_vip_port_id of this ListLoadBalancersRequest.

        双栈类型负载均衡器的IPv6对应的port ID。  支持多值查询，查询条件格式：*ipv6_vip_port_id=xxx&ipv6_vip_port_id=xxx*。  [不支持IPv6，请勿使用。](tag:dt,dt_test)

        :return: The ipv6_vip_port_id of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._ipv6_vip_port_id

    @ipv6_vip_port_id.setter
    def ipv6_vip_port_id(self, ipv6_vip_port_id):
        """Sets the ipv6_vip_port_id of this ListLoadBalancersRequest.

        双栈类型负载均衡器的IPv6对应的port ID。  支持多值查询，查询条件格式：*ipv6_vip_port_id=xxx&ipv6_vip_port_id=xxx*。  [不支持IPv6，请勿使用。](tag:dt,dt_test)

        :param ipv6_vip_port_id: The ipv6_vip_port_id of this ListLoadBalancersRequest.
        :type ipv6_vip_port_id: list[str]
        """
        self._ipv6_vip_port_id = ipv6_vip_port_id

    @property
    def ipv6_vip_address(self):
        """Gets the ipv6_vip_address of this ListLoadBalancersRequest.

        双栈类型负载均衡器的IPv6地址。  支持多值查询，查询条件格式：*ipv6_vip_address=xxx&ipv6_vip_address=xxx*。  [不支持IPv6，请勿使用。](tag:dt,dt_test)

        :return: The ipv6_vip_address of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._ipv6_vip_address

    @ipv6_vip_address.setter
    def ipv6_vip_address(self, ipv6_vip_address):
        """Sets the ipv6_vip_address of this ListLoadBalancersRequest.

        双栈类型负载均衡器的IPv6地址。  支持多值查询，查询条件格式：*ipv6_vip_address=xxx&ipv6_vip_address=xxx*。  [不支持IPv6，请勿使用。](tag:dt,dt_test)

        :param ipv6_vip_address: The ipv6_vip_address of this ListLoadBalancersRequest.
        :type ipv6_vip_address: list[str]
        """
        self._ipv6_vip_address = ipv6_vip_address

    @property
    def ipv6_vip_virsubnet_id(self):
        """Gets the ipv6_vip_virsubnet_id of this ListLoadBalancersRequest.

        双栈类型负载均衡器所在的子网IPv6网络ID。  支持多值查询，查询条件格式：*ipv6_vip_virsubnet_id=xxx&ipv6_vip_virsubnet_id=xxx*。  [不支持IPv6，请勿使用。](tag:dt,dt_test)

        :return: The ipv6_vip_virsubnet_id of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._ipv6_vip_virsubnet_id

    @ipv6_vip_virsubnet_id.setter
    def ipv6_vip_virsubnet_id(self, ipv6_vip_virsubnet_id):
        """Sets the ipv6_vip_virsubnet_id of this ListLoadBalancersRequest.

        双栈类型负载均衡器所在的子网IPv6网络ID。  支持多值查询，查询条件格式：*ipv6_vip_virsubnet_id=xxx&ipv6_vip_virsubnet_id=xxx*。  [不支持IPv6，请勿使用。](tag:dt,dt_test)

        :param ipv6_vip_virsubnet_id: The ipv6_vip_virsubnet_id of this ListLoadBalancersRequest.
        :type ipv6_vip_virsubnet_id: list[str]
        """
        self._ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id

    @property
    def eips(self):
        """Gets the eips of this ListLoadBalancersRequest.

        负载均衡器绑定的EIP。示例如下： \"eips\": [             {                 \"eip_id\": \"e9b72a9d-4275-455e-a724-853504e4d9c6\",                 \"eip_address\": \"88.88.14.122\",                 \"ip_version\": 4             }         ]  支持多值查询，查询条件格式： - eip_id作为查询条件：*eips=eip_id=xxx&eips=eip_id=xxx*。 - eip_address作为查询条件：*eips=eip_address=xxx&eips=eip_address=xxx*。 - ip_version作为查询条件：*eips=ip_version=xxx&eips=ip_version=xxx*。  注：该字段与publicips字段一致。

        :return: The eips of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._eips

    @eips.setter
    def eips(self, eips):
        """Sets the eips of this ListLoadBalancersRequest.

        负载均衡器绑定的EIP。示例如下： \"eips\": [             {                 \"eip_id\": \"e9b72a9d-4275-455e-a724-853504e4d9c6\",                 \"eip_address\": \"88.88.14.122\",                 \"ip_version\": 4             }         ]  支持多值查询，查询条件格式： - eip_id作为查询条件：*eips=eip_id=xxx&eips=eip_id=xxx*。 - eip_address作为查询条件：*eips=eip_address=xxx&eips=eip_address=xxx*。 - ip_version作为查询条件：*eips=ip_version=xxx&eips=ip_version=xxx*。  注：该字段与publicips字段一致。

        :param eips: The eips of this ListLoadBalancersRequest.
        :type eips: list[str]
        """
        self._eips = eips

    @property
    def publicips(self):
        """Gets the publicips of this ListLoadBalancersRequest.

        负载均衡器绑定的公网IP。示例如下：  \"publicips\": [                 {                     \"publicip_id\": \"e9b72a9d-4275-455e-a724-853504e4d9c6\",                     \"publicip_address\": \"88.88.14.122\",                     \"ip_version\": 4                 }             ]  支持多值查询，查询条件格式： - publicip_id作为查询条件： *publicips=publicip_id=xxx&publicips=publicip_id=xxx* - publicip_address作为查询条件： *publicips=publicip_address=xxx&publicips=publicip_address=xxx* - ip_version作为查询条件： *publicips=ip_version=xxx&publicips=ip_version=xxx*  注：该字段与eips字段一致。

        :return: The publicips of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._publicips

    @publicips.setter
    def publicips(self, publicips):
        """Sets the publicips of this ListLoadBalancersRequest.

        负载均衡器绑定的公网IP。示例如下：  \"publicips\": [                 {                     \"publicip_id\": \"e9b72a9d-4275-455e-a724-853504e4d9c6\",                     \"publicip_address\": \"88.88.14.122\",                     \"ip_version\": 4                 }             ]  支持多值查询，查询条件格式： - publicip_id作为查询条件： *publicips=publicip_id=xxx&publicips=publicip_id=xxx* - publicip_address作为查询条件： *publicips=publicip_address=xxx&publicips=publicip_address=xxx* - ip_version作为查询条件： *publicips=ip_version=xxx&publicips=ip_version=xxx*  注：该字段与eips字段一致。

        :param publicips: The publicips of this ListLoadBalancersRequest.
        :type publicips: list[str]
        """
        self._publicips = publicips

    @property
    def availability_zone_list(self):
        """Gets the availability_zone_list of this ListLoadBalancersRequest.

        负载均衡器所在可用区列表。  支持多值查询，查询条件格式： *availability_zone_list=xxx&availability_zone_list=xxx*。

        :return: The availability_zone_list of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._availability_zone_list

    @availability_zone_list.setter
    def availability_zone_list(self, availability_zone_list):
        """Sets the availability_zone_list of this ListLoadBalancersRequest.

        负载均衡器所在可用区列表。  支持多值查询，查询条件格式： *availability_zone_list=xxx&availability_zone_list=xxx*。

        :param availability_zone_list: The availability_zone_list of this ListLoadBalancersRequest.
        :type availability_zone_list: list[str]
        """
        self._availability_zone_list = availability_zone_list

    @property
    def l4_flavor_id(self):
        """Gets the l4_flavor_id of this ListLoadBalancersRequest.

        四层Flavor ID。  支持多值查询，查询条件格式：*l4_flavor_id=xxx&l4_flavor_id=xxx*。

        :return: The l4_flavor_id of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._l4_flavor_id

    @l4_flavor_id.setter
    def l4_flavor_id(self, l4_flavor_id):
        """Sets the l4_flavor_id of this ListLoadBalancersRequest.

        四层Flavor ID。  支持多值查询，查询条件格式：*l4_flavor_id=xxx&l4_flavor_id=xxx*。

        :param l4_flavor_id: The l4_flavor_id of this ListLoadBalancersRequest.
        :type l4_flavor_id: list[str]
        """
        self._l4_flavor_id = l4_flavor_id

    @property
    def l4_scale_flavor_id(self):
        """Gets the l4_scale_flavor_id of this ListLoadBalancersRequest.

        四层弹性Flavor ID。  支持多值查询，查询条件格式：*l4_scale_flavor_id=xxx&l4_scale_flavor_id=xxx*。  不支持该字段，请勿使用。

        :return: The l4_scale_flavor_id of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._l4_scale_flavor_id

    @l4_scale_flavor_id.setter
    def l4_scale_flavor_id(self, l4_scale_flavor_id):
        """Sets the l4_scale_flavor_id of this ListLoadBalancersRequest.

        四层弹性Flavor ID。  支持多值查询，查询条件格式：*l4_scale_flavor_id=xxx&l4_scale_flavor_id=xxx*。  不支持该字段，请勿使用。

        :param l4_scale_flavor_id: The l4_scale_flavor_id of this ListLoadBalancersRequest.
        :type l4_scale_flavor_id: list[str]
        """
        self._l4_scale_flavor_id = l4_scale_flavor_id

    @property
    def l7_flavor_id(self):
        """Gets the l7_flavor_id of this ListLoadBalancersRequest.

        七层Flavor ID。  支持多值查询，查询条件格式：*l7_flavor_id=xxx&l7_flavor_id=xxx*。

        :return: The l7_flavor_id of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._l7_flavor_id

    @l7_flavor_id.setter
    def l7_flavor_id(self, l7_flavor_id):
        """Sets the l7_flavor_id of this ListLoadBalancersRequest.

        七层Flavor ID。  支持多值查询，查询条件格式：*l7_flavor_id=xxx&l7_flavor_id=xxx*。

        :param l7_flavor_id: The l7_flavor_id of this ListLoadBalancersRequest.
        :type l7_flavor_id: list[str]
        """
        self._l7_flavor_id = l7_flavor_id

    @property
    def l7_scale_flavor_id(self):
        """Gets the l7_scale_flavor_id of this ListLoadBalancersRequest.

        七层弹性Flavor ID。  支持多值查询，查询条件格式：*l7_scale_flavor_id=xxx&l7_scale_flavor_id=xxx*。  不支持该字段，请勿使用。

        :return: The l7_scale_flavor_id of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._l7_scale_flavor_id

    @l7_scale_flavor_id.setter
    def l7_scale_flavor_id(self, l7_scale_flavor_id):
        """Sets the l7_scale_flavor_id of this ListLoadBalancersRequest.

        七层弹性Flavor ID。  支持多值查询，查询条件格式：*l7_scale_flavor_id=xxx&l7_scale_flavor_id=xxx*。  不支持该字段，请勿使用。

        :param l7_scale_flavor_id: The l7_scale_flavor_id of this ListLoadBalancersRequest.
        :type l7_scale_flavor_id: list[str]
        """
        self._l7_scale_flavor_id = l7_scale_flavor_id

    @property
    def billing_info(self):
        """Gets the billing_info of this ListLoadBalancersRequest.

        资源账单信息。  支持多值查询，查询条件格式：*billing_info=xxx&billing_info=xxx*。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42,dt,dt_test,hcso_dt)

        :return: The billing_info of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        """Sets the billing_info of this ListLoadBalancersRequest.

        资源账单信息。  支持多值查询，查询条件格式：*billing_info=xxx&billing_info=xxx*。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42,dt,dt_test,hcso_dt)

        :param billing_info: The billing_info of this ListLoadBalancersRequest.
        :type billing_info: list[str]
        """
        self._billing_info = billing_info

    @property
    def member_device_id(self):
        """Gets the member_device_id of this ListLoadBalancersRequest.

        负载均衡器中的后端云服务器对应的弹性云服务器的ID。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_device_id=xxx&member_device_id=xxx*。

        :return: The member_device_id of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._member_device_id

    @member_device_id.setter
    def member_device_id(self, member_device_id):
        """Sets the member_device_id of this ListLoadBalancersRequest.

        负载均衡器中的后端云服务器对应的弹性云服务器的ID。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_device_id=xxx&member_device_id=xxx*。

        :param member_device_id: The member_device_id of this ListLoadBalancersRequest.
        :type member_device_id: list[str]
        """
        self._member_device_id = member_device_id

    @property
    def member_address(self):
        """Gets the member_address of this ListLoadBalancersRequest.

        负载均衡器中的后端云服务器对应的弹性云服务器的IP地址。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_address=xxx&member_address=xxx*。

        :return: The member_address of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._member_address

    @member_address.setter
    def member_address(self, member_address):
        """Sets the member_address of this ListLoadBalancersRequest.

        负载均衡器中的后端云服务器对应的弹性云服务器的IP地址。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_address=xxx&member_address=xxx*。

        :param member_address: The member_address of this ListLoadBalancersRequest.
        :type member_address: list[str]
        """
        self._member_address = member_address

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListLoadBalancersRequest.

        负载均衡器所属的企业项目ID。 查询时若不传，则查询default企业项目下的资源，鉴权按照default企业项目鉴权。 如果传值，则必须传已存在的企业项目ID（不可为\"0\"）或传all_granted_eps表示查询所有企业项目。  支持多值查询，查询条件格式： *enterprise_project_id=xxx&enterprise_project_id=xxx*。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)

        :return: The enterprise_project_id of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListLoadBalancersRequest.

        负载均衡器所属的企业项目ID。 查询时若不传，则查询default企业项目下的资源，鉴权按照default企业项目鉴权。 如果传值，则必须传已存在的企业项目ID（不可为\"0\"）或传all_granted_eps表示查询所有企业项目。  支持多值查询，查询条件格式： *enterprise_project_id=xxx&enterprise_project_id=xxx*。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)

        :param enterprise_project_id: The enterprise_project_id of this ListLoadBalancersRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def ip_version(self):
        """Gets the ip_version of this ListLoadBalancersRequest.

        IP版本信息。  取值：4代表IPv4，6代表IPv6。  支持多值查询，查询条件格式：*ip_version=xxx&ip_version=xxx*。  [不支持IPv6，请勿设置为6。](tag:dt,dt_test)

        :return: The ip_version of this ListLoadBalancersRequest.
        :rtype: list[int]
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this ListLoadBalancersRequest.

        IP版本信息。  取值：4代表IPv4，6代表IPv6。  支持多值查询，查询条件格式：*ip_version=xxx&ip_version=xxx*。  [不支持IPv6，请勿设置为6。](tag:dt,dt_test)

        :param ip_version: The ip_version of this ListLoadBalancersRequest.
        :type ip_version: list[int]
        """
        self._ip_version = ip_version

    @property
    def deletion_protection_enable(self):
        """Gets the deletion_protection_enable of this ListLoadBalancersRequest.

        是否开启删除保护，false不开启，true开启。[不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)

        :return: The deletion_protection_enable of this ListLoadBalancersRequest.
        :rtype: bool
        """
        return self._deletion_protection_enable

    @deletion_protection_enable.setter
    def deletion_protection_enable(self, deletion_protection_enable):
        """Sets the deletion_protection_enable of this ListLoadBalancersRequest.

        是否开启删除保护，false不开启，true开启。[不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)

        :param deletion_protection_enable: The deletion_protection_enable of this ListLoadBalancersRequest.
        :type deletion_protection_enable: bool
        """
        self._deletion_protection_enable = deletion_protection_enable

    @property
    def elb_virsubnet_type(self):
        """Gets the elb_virsubnet_type of this ListLoadBalancersRequest.

        下联面子网类型。  取值： - ipv4：ipv4。 - dualstack：双栈。  支持多值查询，查询条件格式： *elb_virsubnet_type=ipv4&elb_virsubnet_type=dualstack*。

        :return: The elb_virsubnet_type of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._elb_virsubnet_type

    @elb_virsubnet_type.setter
    def elb_virsubnet_type(self, elb_virsubnet_type):
        """Sets the elb_virsubnet_type of this ListLoadBalancersRequest.

        下联面子网类型。  取值： - ipv4：ipv4。 - dualstack：双栈。  支持多值查询，查询条件格式： *elb_virsubnet_type=ipv4&elb_virsubnet_type=dualstack*。

        :param elb_virsubnet_type: The elb_virsubnet_type of this ListLoadBalancersRequest.
        :type elb_virsubnet_type: list[str]
        """
        self._elb_virsubnet_type = elb_virsubnet_type

    @property
    def autoscaling(self):
        """Gets the autoscaling of this ListLoadBalancersRequest.

        是否开启弹性扩缩容。示例如下： \"autoscaling\": {             \"enable\": \"true\"         }  支持多值查询，查询条件格式：  *autoscaling=enable=true&autoscaling=enable=false*。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)

        :return: The autoscaling of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._autoscaling

    @autoscaling.setter
    def autoscaling(self, autoscaling):
        """Sets the autoscaling of this ListLoadBalancersRequest.

        是否开启弹性扩缩容。示例如下： \"autoscaling\": {             \"enable\": \"true\"         }  支持多值查询，查询条件格式：  *autoscaling=enable=true&autoscaling=enable=false*。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)

        :param autoscaling: The autoscaling of this ListLoadBalancersRequest.
        :type autoscaling: list[str]
        """
        self._autoscaling = autoscaling

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
        if not isinstance(other, ListLoadBalancersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
