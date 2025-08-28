# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPoolsRequest:

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
        'description': 'list[str]',
        'admin_state_up': 'bool',
        'healthmonitor_id': 'list[str]',
        'id': 'list[str]',
        'name': 'list[str]',
        'loadbalancer_id': 'list[str]',
        'protocol': 'list[str]',
        'lb_algorithm': 'list[str]',
        'enterprise_project_id': 'list[str]',
        'ip_version': 'list[str]',
        'member_address': 'list[str]',
        'member_device_id': 'list[str]',
        'member_deletion_protection_enable': 'bool',
        'listener_id': 'list[str]',
        'member_instance_id': 'list[str]',
        'vpc_id': 'list[str]',
        'type': 'list[str]',
        'protection_status': 'list[str]',
        'connection_drain': 'bool',
        'pool_health': 'str',
        'any_port_enable': 'bool',
        'public_border_group': 'str',
        'quic_cid_len': 'int',
        'quic_cid_offset': 'int',
        'az_affinity': 'list[str]'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'page_reverse': 'page_reverse',
        'description': 'description',
        'admin_state_up': 'admin_state_up',
        'healthmonitor_id': 'healthmonitor_id',
        'id': 'id',
        'name': 'name',
        'loadbalancer_id': 'loadbalancer_id',
        'protocol': 'protocol',
        'lb_algorithm': 'lb_algorithm',
        'enterprise_project_id': 'enterprise_project_id',
        'ip_version': 'ip_version',
        'member_address': 'member_address',
        'member_device_id': 'member_device_id',
        'member_deletion_protection_enable': 'member_deletion_protection_enable',
        'listener_id': 'listener_id',
        'member_instance_id': 'member_instance_id',
        'vpc_id': 'vpc_id',
        'type': 'type',
        'protection_status': 'protection_status',
        'connection_drain': 'connection_drain',
        'pool_health': 'pool_health',
        'any_port_enable': 'any_port_enable',
        'public_border_group': 'public_border_group',
        'quic_cid_len': 'quic_cid_len',
        'quic_cid_offset': 'quic_cid_offset',
        'az_affinity': 'az_affinity'
    }

    def __init__(self, marker=None, limit=None, page_reverse=None, description=None, admin_state_up=None, healthmonitor_id=None, id=None, name=None, loadbalancer_id=None, protocol=None, lb_algorithm=None, enterprise_project_id=None, ip_version=None, member_address=None, member_device_id=None, member_deletion_protection_enable=None, listener_id=None, member_instance_id=None, vpc_id=None, type=None, protection_status=None, connection_drain=None, pool_health=None, any_port_enable=None, public_border_group=None, quic_cid_len=None, quic_cid_offset=None, az_affinity=None):
        r"""ListPoolsRequest

        The model defined in huaweicloud sdk

        :param marker: **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及
        :type marker: str
        :param limit: **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000
        :type limit: int
        :param page_reverse: **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse&#x3D;true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false
        :type page_reverse: bool
        :param description: **参数解释**：后端服务器组的描述信息 支持多值查询，查询条件格式：*description&#x3D;xxx&amp;description&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type description: list[str]
        :param admin_state_up: **参数解释**：后端服务器组的管理状态。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)
        :type admin_state_up: bool
        :param healthmonitor_id: **参数解释**：后端服务器组关联的健康检查的ID。 支持多值查询，查询条件格式：*healthmonitor_id&#x3D;xxx&amp;healthmonitor_id&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type healthmonitor_id: list[str]
        :param id: **参数解释**：后端服务器组的ID。 支持多值查询，查询条件格式：*id&#x3D;xxx&amp;id&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type id: list[str]
        :param name: **参数解释**：后端服务器组的名称。 支持多值查询，查询条件格式：*name&#x3D;xxx&amp;name&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type name: list[str]
        :param loadbalancer_id: **参数解释**：后端服务器组绑定的负载均衡器ID。 支持多值查询，查询条件格式：*loadbalancer_id&#x3D;xxx&amp;loadbalancer_id&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type loadbalancer_id: list[str]
        :param protocol: **参数解释**：后端服务器组的后端协议。 支持多值查询，查询条件格式：*protocol&#x3D;xxx&amp;protocol&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：TCP、UDP、[IP、](tag:hws_eu)TLS、HTTP、HTTPS、QUIC和GRPC。  **默认取值**：不涉及  [荷兰region不支持QUIC。](tag:dt)
        :type protocol: list[str]
        :param lb_algorithm: **参数解释**：后端服务器组的负载均衡算法。 支持多值查询，查询条件格式：*lb_algorithm&#x3D;xxx&amp;lb_algorithm&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**： - ROUND_ROBIN：加权轮询算法。 - LEAST_CONNECTIONS：加权最少连接算法。 - SOURCE_IP：源IP算法。 - QUIC_CID：连接ID算法。 [- 2_TUPLE_HASH：二元组hash算法，仅IP类型的pool支持。 - 3_TUPLE_HASH：三元组hash算法，仅IP类型的pool支持。 - 5_TUPLE_HASH：五元组hash算法，仅IP类型的pool支持。 - IP型pool不指定该字段时，默认设置为5_TUPLE_HASH。](tag:hws_eu)  **默认取值**：不涉及
        :type lb_algorithm: list[str]
        :param enterprise_project_id: **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式： *enterprise_project_id&#x3D;xxx&amp;enterprise_project_id&#x3D;xxx*。  **约束限制**： 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:pools:list权限。 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)
        :type enterprise_project_id: list[str]
        :param ip_version: **参数解释**：后端服务器组支持的IP版本。 支持多值查询，查询条件格式：*ip_version&#x3D;xxx&amp;ip_version&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type ip_version: list[str]
        :param member_address: **参数解释**：后端服务器的IP地址。仅用于查询条件，不作为响应参数字段。 支持多值查询，查询条件格式：*member_address&#x3D;xxx&amp;member_address&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type member_address: list[str]
        :param member_device_id: **参数解释**：后端服务器对应的弹性云服务器的ID。仅用于查询条件，不作为响应参数字段。 支持多值查询，查询条件格式：*member_device_id&#x3D;xxx&amp;member_device_id&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type member_device_id: list[str]
        :param member_deletion_protection_enable: **参数解释**：是否开启删除保护。  **约束限制**：不涉及  **取值范围**：false 不开启，true 开启，不传查询全部。  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)  [荷兰region不支持该字段，请勿使用。](tag:dt)
        :type member_deletion_protection_enable: bool
        :param listener_id: **参数解释**：关联的监听器ID，包括通过l7policy关联的。 支持多值查询，查询条件格式：*listener_id&#x3D;xxx&amp;listener_id&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type listener_id: list[str]
        :param member_instance_id: **参数解释**：后端服务器ID。仅用于查询条件，不作为响应参数字段。 支持多值查询，查询条件格式：*member_instance_id&#x3D;xxx&amp;member_instance_id&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type member_instance_id: list[str]
        :param vpc_id: **参数解释**：后端服务器组关联的虚拟私有云的ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type vpc_id: list[str]
        :param type: **参数解释**：后端服务器组的类型。  **约束限制**：不涉及  **取值范围**： - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加IP类型后端，type指定为该类型时，vpc_id不允许指定。 - 空字符串（\&quot;\&quot;）：允许任意类型的后端  **默认取值**：不涉及
        :type type: list[str]
        :param protection_status: **参数解释**：修改保护状态,  **约束限制**：不涉及  **取值范围**： - nonProtection: 不保护，默认值为nonProtection - consoleProtection: 控制台修改保护  **默认取值**：不涉及
        :type protection_status: list[str]
        :param connection_drain: **参数解释**：查询是否开启延迟注销的功能，查询条件格式：*connection_drain&#x3D;true或者*connection_drain&#x3D;false  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type connection_drain: bool
        :param pool_health: **参数解释**：查询是否开启后端全下线转发功能，查询条件格式：*pool_health&#x3D;minimum_healthy_member_count&#x3D;0或者*pool_health&#x3D;minimum_healthy_member_count&#x3D;1  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type pool_health: str
        :param any_port_enable: **参数解释**：后端是否开启全端口转发。开启后，后端服务器端口与前端监听器端口保持一致。  **约束限制**：不涉及  **取值范围**：false 不开启，true 开启。  **默认取值**：不涉及
        :type any_port_enable: bool
        :param public_border_group: **参数解释**：公网边界组。 支持多值查询，查询条件格式：*public_border_group&#x3D;xxx&amp;public_border_group&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**： - center：表示中心站点的公网边界组 - 边缘站点名称：表示边缘站点的公网边界组  **默认取值**：不涉及
        :type public_border_group: str
        :param quic_cid_len: **参数解释**：查询相同QUIC CID策略配置的后端服务器组，仅用于查询条件，不作为响应参数字段。 支持多值查询，查询条件格式：*quic_cid_len&#x3D;3&amp;quic_cid_len&#x3D;5*  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type quic_cid_len: int
        :param quic_cid_offset: **参数解释**：查询相同QUIC CID策略配置的后端服务器组，仅用于查询条件，不作为响应参数字段。 支持多值查询，查询条件格式：*quic_cid_offset&#x3D;1&amp;quic_cid_offset&#x3D;3*  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type quic_cid_offset: int
        :param az_affinity: **参数解释**：查询后端服务器组可用区亲和性策略是否开启。示例如下： \&quot;az_affinity\&quot;: {             \&quot;enable\&quot;: \&quot;true\&quot;         } 支持多值查询，查询条件格式： *az_affinity&#x3D;enable&#x3D;true&amp;az_affinity&#x3D;enable&#x3D;false*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type az_affinity: list[str]
        """
        
        

        self._marker = None
        self._limit = None
        self._page_reverse = None
        self._description = None
        self._admin_state_up = None
        self._healthmonitor_id = None
        self._id = None
        self._name = None
        self._loadbalancer_id = None
        self._protocol = None
        self._lb_algorithm = None
        self._enterprise_project_id = None
        self._ip_version = None
        self._member_address = None
        self._member_device_id = None
        self._member_deletion_protection_enable = None
        self._listener_id = None
        self._member_instance_id = None
        self._vpc_id = None
        self._type = None
        self._protection_status = None
        self._connection_drain = None
        self._pool_health = None
        self._any_port_enable = None
        self._public_border_group = None
        self._quic_cid_len = None
        self._quic_cid_offset = None
        self._az_affinity = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if description is not None:
            self.description = description
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if healthmonitor_id is not None:
            self.healthmonitor_id = healthmonitor_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if loadbalancer_id is not None:
            self.loadbalancer_id = loadbalancer_id
        if protocol is not None:
            self.protocol = protocol
        if lb_algorithm is not None:
            self.lb_algorithm = lb_algorithm
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if ip_version is not None:
            self.ip_version = ip_version
        if member_address is not None:
            self.member_address = member_address
        if member_device_id is not None:
            self.member_device_id = member_device_id
        if member_deletion_protection_enable is not None:
            self.member_deletion_protection_enable = member_deletion_protection_enable
        if listener_id is not None:
            self.listener_id = listener_id
        if member_instance_id is not None:
            self.member_instance_id = member_instance_id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if type is not None:
            self.type = type
        if protection_status is not None:
            self.protection_status = protection_status
        if connection_drain is not None:
            self.connection_drain = connection_drain
        if pool_health is not None:
            self.pool_health = pool_health
        if any_port_enable is not None:
            self.any_port_enable = any_port_enable
        if public_border_group is not None:
            self.public_border_group = public_border_group
        if quic_cid_len is not None:
            self.quic_cid_len = quic_cid_len
        if quic_cid_offset is not None:
            self.quic_cid_offset = quic_cid_offset
        if az_affinity is not None:
            self.az_affinity = az_affinity

    @property
    def marker(self):
        r"""Gets the marker of this ListPoolsRequest.

        **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The marker of this ListPoolsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListPoolsRequest.

        **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及

        :param marker: The marker of this ListPoolsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListPoolsRequest.

        **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000

        :return: The limit of this ListPoolsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPoolsRequest.

        **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000

        :param limit: The limit of this ListPoolsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def page_reverse(self):
        r"""Gets the page_reverse of this ListPoolsRequest.

        **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false

        :return: The page_reverse of this ListPoolsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        r"""Sets the page_reverse of this ListPoolsRequest.

        **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false

        :param page_reverse: The page_reverse of this ListPoolsRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def description(self):
        r"""Gets the description of this ListPoolsRequest.

        **参数解释**：后端服务器组的描述信息 支持多值查询，查询条件格式：*description=xxx&description=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The description of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListPoolsRequest.

        **参数解释**：后端服务器组的描述信息 支持多值查询，查询条件格式：*description=xxx&description=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param description: The description of this ListPoolsRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this ListPoolsRequest.

        **参数解释**：后端服务器组的管理状态。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :return: The admin_state_up of this ListPoolsRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this ListPoolsRequest.

        **参数解释**：后端服务器组的管理状态。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :param admin_state_up: The admin_state_up of this ListPoolsRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def healthmonitor_id(self):
        r"""Gets the healthmonitor_id of this ListPoolsRequest.

        **参数解释**：后端服务器组关联的健康检查的ID。 支持多值查询，查询条件格式：*healthmonitor_id=xxx&healthmonitor_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The healthmonitor_id of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._healthmonitor_id

    @healthmonitor_id.setter
    def healthmonitor_id(self, healthmonitor_id):
        r"""Sets the healthmonitor_id of this ListPoolsRequest.

        **参数解释**：后端服务器组关联的健康检查的ID。 支持多值查询，查询条件格式：*healthmonitor_id=xxx&healthmonitor_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param healthmonitor_id: The healthmonitor_id of this ListPoolsRequest.
        :type healthmonitor_id: list[str]
        """
        self._healthmonitor_id = healthmonitor_id

    @property
    def id(self):
        r"""Gets the id of this ListPoolsRequest.

        **参数解释**：后端服务器组的ID。 支持多值查询，查询条件格式：*id=xxx&id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The id of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListPoolsRequest.

        **参数解释**：后端服务器组的ID。 支持多值查询，查询条件格式：*id=xxx&id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param id: The id of this ListPoolsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListPoolsRequest.

        **参数解释**：后端服务器组的名称。 支持多值查询，查询条件格式：*name=xxx&name=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The name of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListPoolsRequest.

        **参数解释**：后端服务器组的名称。 支持多值查询，查询条件格式：*name=xxx&name=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param name: The name of this ListPoolsRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def loadbalancer_id(self):
        r"""Gets the loadbalancer_id of this ListPoolsRequest.

        **参数解释**：后端服务器组绑定的负载均衡器ID。 支持多值查询，查询条件格式：*loadbalancer_id=xxx&loadbalancer_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The loadbalancer_id of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        r"""Sets the loadbalancer_id of this ListPoolsRequest.

        **参数解释**：后端服务器组绑定的负载均衡器ID。 支持多值查询，查询条件格式：*loadbalancer_id=xxx&loadbalancer_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param loadbalancer_id: The loadbalancer_id of this ListPoolsRequest.
        :type loadbalancer_id: list[str]
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def protocol(self):
        r"""Gets the protocol of this ListPoolsRequest.

        **参数解释**：后端服务器组的后端协议。 支持多值查询，查询条件格式：*protocol=xxx&protocol=xxx*。  **约束限制**：不涉及  **取值范围**：TCP、UDP、[IP、](tag:hws_eu)TLS、HTTP、HTTPS、QUIC和GRPC。  **默认取值**：不涉及  [荷兰region不支持QUIC。](tag:dt)

        :return: The protocol of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this ListPoolsRequest.

        **参数解释**：后端服务器组的后端协议。 支持多值查询，查询条件格式：*protocol=xxx&protocol=xxx*。  **约束限制**：不涉及  **取值范围**：TCP、UDP、[IP、](tag:hws_eu)TLS、HTTP、HTTPS、QUIC和GRPC。  **默认取值**：不涉及  [荷兰region不支持QUIC。](tag:dt)

        :param protocol: The protocol of this ListPoolsRequest.
        :type protocol: list[str]
        """
        self._protocol = protocol

    @property
    def lb_algorithm(self):
        r"""Gets the lb_algorithm of this ListPoolsRequest.

        **参数解释**：后端服务器组的负载均衡算法。 支持多值查询，查询条件格式：*lb_algorithm=xxx&lb_algorithm=xxx*。  **约束限制**：不涉及  **取值范围**： - ROUND_ROBIN：加权轮询算法。 - LEAST_CONNECTIONS：加权最少连接算法。 - SOURCE_IP：源IP算法。 - QUIC_CID：连接ID算法。 [- 2_TUPLE_HASH：二元组hash算法，仅IP类型的pool支持。 - 3_TUPLE_HASH：三元组hash算法，仅IP类型的pool支持。 - 5_TUPLE_HASH：五元组hash算法，仅IP类型的pool支持。 - IP型pool不指定该字段时，默认设置为5_TUPLE_HASH。](tag:hws_eu)  **默认取值**：不涉及

        :return: The lb_algorithm of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._lb_algorithm

    @lb_algorithm.setter
    def lb_algorithm(self, lb_algorithm):
        r"""Sets the lb_algorithm of this ListPoolsRequest.

        **参数解释**：后端服务器组的负载均衡算法。 支持多值查询，查询条件格式：*lb_algorithm=xxx&lb_algorithm=xxx*。  **约束限制**：不涉及  **取值范围**： - ROUND_ROBIN：加权轮询算法。 - LEAST_CONNECTIONS：加权最少连接算法。 - SOURCE_IP：源IP算法。 - QUIC_CID：连接ID算法。 [- 2_TUPLE_HASH：二元组hash算法，仅IP类型的pool支持。 - 3_TUPLE_HASH：三元组hash算法，仅IP类型的pool支持。 - 5_TUPLE_HASH：五元组hash算法，仅IP类型的pool支持。 - IP型pool不指定该字段时，默认设置为5_TUPLE_HASH。](tag:hws_eu)  **默认取值**：不涉及

        :param lb_algorithm: The lb_algorithm of this ListPoolsRequest.
        :type lb_algorithm: list[str]
        """
        self._lb_algorithm = lb_algorithm

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListPoolsRequest.

        **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式： *enterprise_project_id=xxx&enterprise_project_id=xxx*。  **约束限制**： 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:pools:list权限。 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :return: The enterprise_project_id of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListPoolsRequest.

        **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式： *enterprise_project_id=xxx&enterprise_project_id=xxx*。  **约束限制**： 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:pools:list权限。 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :param enterprise_project_id: The enterprise_project_id of this ListPoolsRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def ip_version(self):
        r"""Gets the ip_version of this ListPoolsRequest.

        **参数解释**：后端服务器组支持的IP版本。 支持多值查询，查询条件格式：*ip_version=xxx&ip_version=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The ip_version of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this ListPoolsRequest.

        **参数解释**：后端服务器组支持的IP版本。 支持多值查询，查询条件格式：*ip_version=xxx&ip_version=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param ip_version: The ip_version of this ListPoolsRequest.
        :type ip_version: list[str]
        """
        self._ip_version = ip_version

    @property
    def member_address(self):
        r"""Gets the member_address of this ListPoolsRequest.

        **参数解释**：后端服务器的IP地址。仅用于查询条件，不作为响应参数字段。 支持多值查询，查询条件格式：*member_address=xxx&member_address=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The member_address of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._member_address

    @member_address.setter
    def member_address(self, member_address):
        r"""Sets the member_address of this ListPoolsRequest.

        **参数解释**：后端服务器的IP地址。仅用于查询条件，不作为响应参数字段。 支持多值查询，查询条件格式：*member_address=xxx&member_address=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param member_address: The member_address of this ListPoolsRequest.
        :type member_address: list[str]
        """
        self._member_address = member_address

    @property
    def member_device_id(self):
        r"""Gets the member_device_id of this ListPoolsRequest.

        **参数解释**：后端服务器对应的弹性云服务器的ID。仅用于查询条件，不作为响应参数字段。 支持多值查询，查询条件格式：*member_device_id=xxx&member_device_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The member_device_id of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._member_device_id

    @member_device_id.setter
    def member_device_id(self, member_device_id):
        r"""Sets the member_device_id of this ListPoolsRequest.

        **参数解释**：后端服务器对应的弹性云服务器的ID。仅用于查询条件，不作为响应参数字段。 支持多值查询，查询条件格式：*member_device_id=xxx&member_device_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param member_device_id: The member_device_id of this ListPoolsRequest.
        :type member_device_id: list[str]
        """
        self._member_device_id = member_device_id

    @property
    def member_deletion_protection_enable(self):
        r"""Gets the member_deletion_protection_enable of this ListPoolsRequest.

        **参数解释**：是否开启删除保护。  **约束限制**：不涉及  **取值范围**：false 不开启，true 开启，不传查询全部。  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :return: The member_deletion_protection_enable of this ListPoolsRequest.
        :rtype: bool
        """
        return self._member_deletion_protection_enable

    @member_deletion_protection_enable.setter
    def member_deletion_protection_enable(self, member_deletion_protection_enable):
        r"""Sets the member_deletion_protection_enable of this ListPoolsRequest.

        **参数解释**：是否开启删除保护。  **约束限制**：不涉及  **取值范围**：false 不开启，true 开启，不传查询全部。  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :param member_deletion_protection_enable: The member_deletion_protection_enable of this ListPoolsRequest.
        :type member_deletion_protection_enable: bool
        """
        self._member_deletion_protection_enable = member_deletion_protection_enable

    @property
    def listener_id(self):
        r"""Gets the listener_id of this ListPoolsRequest.

        **参数解释**：关联的监听器ID，包括通过l7policy关联的。 支持多值查询，查询条件格式：*listener_id=xxx&listener_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The listener_id of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        r"""Sets the listener_id of this ListPoolsRequest.

        **参数解释**：关联的监听器ID，包括通过l7policy关联的。 支持多值查询，查询条件格式：*listener_id=xxx&listener_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param listener_id: The listener_id of this ListPoolsRequest.
        :type listener_id: list[str]
        """
        self._listener_id = listener_id

    @property
    def member_instance_id(self):
        r"""Gets the member_instance_id of this ListPoolsRequest.

        **参数解释**：后端服务器ID。仅用于查询条件，不作为响应参数字段。 支持多值查询，查询条件格式：*member_instance_id=xxx&member_instance_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The member_instance_id of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._member_instance_id

    @member_instance_id.setter
    def member_instance_id(self, member_instance_id):
        r"""Sets the member_instance_id of this ListPoolsRequest.

        **参数解释**：后端服务器ID。仅用于查询条件，不作为响应参数字段。 支持多值查询，查询条件格式：*member_instance_id=xxx&member_instance_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param member_instance_id: The member_instance_id of this ListPoolsRequest.
        :type member_instance_id: list[str]
        """
        self._member_instance_id = member_instance_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ListPoolsRequest.

        **参数解释**：后端服务器组关联的虚拟私有云的ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The vpc_id of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ListPoolsRequest.

        **参数解释**：后端服务器组关联的虚拟私有云的ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param vpc_id: The vpc_id of this ListPoolsRequest.
        :type vpc_id: list[str]
        """
        self._vpc_id = vpc_id

    @property
    def type(self):
        r"""Gets the type of this ListPoolsRequest.

        **参数解释**：后端服务器组的类型。  **约束限制**：不涉及  **取值范围**： - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加IP类型后端，type指定为该类型时，vpc_id不允许指定。 - 空字符串（\"\"）：允许任意类型的后端  **默认取值**：不涉及

        :return: The type of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListPoolsRequest.

        **参数解释**：后端服务器组的类型。  **约束限制**：不涉及  **取值范围**： - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加IP类型后端，type指定为该类型时，vpc_id不允许指定。 - 空字符串（\"\"）：允许任意类型的后端  **默认取值**：不涉及

        :param type: The type of this ListPoolsRequest.
        :type type: list[str]
        """
        self._type = type

    @property
    def protection_status(self):
        r"""Gets the protection_status of this ListPoolsRequest.

        **参数解释**：修改保护状态,  **约束限制**：不涉及  **取值范围**： - nonProtection: 不保护，默认值为nonProtection - consoleProtection: 控制台修改保护  **默认取值**：不涉及

        :return: The protection_status of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._protection_status

    @protection_status.setter
    def protection_status(self, protection_status):
        r"""Sets the protection_status of this ListPoolsRequest.

        **参数解释**：修改保护状态,  **约束限制**：不涉及  **取值范围**： - nonProtection: 不保护，默认值为nonProtection - consoleProtection: 控制台修改保护  **默认取值**：不涉及

        :param protection_status: The protection_status of this ListPoolsRequest.
        :type protection_status: list[str]
        """
        self._protection_status = protection_status

    @property
    def connection_drain(self):
        r"""Gets the connection_drain of this ListPoolsRequest.

        **参数解释**：查询是否开启延迟注销的功能，查询条件格式：*connection_drain=true或者*connection_drain=false  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The connection_drain of this ListPoolsRequest.
        :rtype: bool
        """
        return self._connection_drain

    @connection_drain.setter
    def connection_drain(self, connection_drain):
        r"""Sets the connection_drain of this ListPoolsRequest.

        **参数解释**：查询是否开启延迟注销的功能，查询条件格式：*connection_drain=true或者*connection_drain=false  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param connection_drain: The connection_drain of this ListPoolsRequest.
        :type connection_drain: bool
        """
        self._connection_drain = connection_drain

    @property
    def pool_health(self):
        r"""Gets the pool_health of this ListPoolsRequest.

        **参数解释**：查询是否开启后端全下线转发功能，查询条件格式：*pool_health=minimum_healthy_member_count=0或者*pool_health=minimum_healthy_member_count=1  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The pool_health of this ListPoolsRequest.
        :rtype: str
        """
        return self._pool_health

    @pool_health.setter
    def pool_health(self, pool_health):
        r"""Sets the pool_health of this ListPoolsRequest.

        **参数解释**：查询是否开启后端全下线转发功能，查询条件格式：*pool_health=minimum_healthy_member_count=0或者*pool_health=minimum_healthy_member_count=1  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param pool_health: The pool_health of this ListPoolsRequest.
        :type pool_health: str
        """
        self._pool_health = pool_health

    @property
    def any_port_enable(self):
        r"""Gets the any_port_enable of this ListPoolsRequest.

        **参数解释**：后端是否开启全端口转发。开启后，后端服务器端口与前端监听器端口保持一致。  **约束限制**：不涉及  **取值范围**：false 不开启，true 开启。  **默认取值**：不涉及

        :return: The any_port_enable of this ListPoolsRequest.
        :rtype: bool
        """
        return self._any_port_enable

    @any_port_enable.setter
    def any_port_enable(self, any_port_enable):
        r"""Sets the any_port_enable of this ListPoolsRequest.

        **参数解释**：后端是否开启全端口转发。开启后，后端服务器端口与前端监听器端口保持一致。  **约束限制**：不涉及  **取值范围**：false 不开启，true 开启。  **默认取值**：不涉及

        :param any_port_enable: The any_port_enable of this ListPoolsRequest.
        :type any_port_enable: bool
        """
        self._any_port_enable = any_port_enable

    @property
    def public_border_group(self):
        r"""Gets the public_border_group of this ListPoolsRequest.

        **参数解释**：公网边界组。 支持多值查询，查询条件格式：*public_border_group=xxx&public_border_group=xxx*。  **约束限制**：不涉及  **取值范围**： - center：表示中心站点的公网边界组 - 边缘站点名称：表示边缘站点的公网边界组  **默认取值**：不涉及

        :return: The public_border_group of this ListPoolsRequest.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        r"""Sets the public_border_group of this ListPoolsRequest.

        **参数解释**：公网边界组。 支持多值查询，查询条件格式：*public_border_group=xxx&public_border_group=xxx*。  **约束限制**：不涉及  **取值范围**： - center：表示中心站点的公网边界组 - 边缘站点名称：表示边缘站点的公网边界组  **默认取值**：不涉及

        :param public_border_group: The public_border_group of this ListPoolsRequest.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

    @property
    def quic_cid_len(self):
        r"""Gets the quic_cid_len of this ListPoolsRequest.

        **参数解释**：查询相同QUIC CID策略配置的后端服务器组，仅用于查询条件，不作为响应参数字段。 支持多值查询，查询条件格式：*quic_cid_len=3&quic_cid_len=5*  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The quic_cid_len of this ListPoolsRequest.
        :rtype: int
        """
        return self._quic_cid_len

    @quic_cid_len.setter
    def quic_cid_len(self, quic_cid_len):
        r"""Sets the quic_cid_len of this ListPoolsRequest.

        **参数解释**：查询相同QUIC CID策略配置的后端服务器组，仅用于查询条件，不作为响应参数字段。 支持多值查询，查询条件格式：*quic_cid_len=3&quic_cid_len=5*  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param quic_cid_len: The quic_cid_len of this ListPoolsRequest.
        :type quic_cid_len: int
        """
        self._quic_cid_len = quic_cid_len

    @property
    def quic_cid_offset(self):
        r"""Gets the quic_cid_offset of this ListPoolsRequest.

        **参数解释**：查询相同QUIC CID策略配置的后端服务器组，仅用于查询条件，不作为响应参数字段。 支持多值查询，查询条件格式：*quic_cid_offset=1&quic_cid_offset=3*  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The quic_cid_offset of this ListPoolsRequest.
        :rtype: int
        """
        return self._quic_cid_offset

    @quic_cid_offset.setter
    def quic_cid_offset(self, quic_cid_offset):
        r"""Sets the quic_cid_offset of this ListPoolsRequest.

        **参数解释**：查询相同QUIC CID策略配置的后端服务器组，仅用于查询条件，不作为响应参数字段。 支持多值查询，查询条件格式：*quic_cid_offset=1&quic_cid_offset=3*  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param quic_cid_offset: The quic_cid_offset of this ListPoolsRequest.
        :type quic_cid_offset: int
        """
        self._quic_cid_offset = quic_cid_offset

    @property
    def az_affinity(self):
        r"""Gets the az_affinity of this ListPoolsRequest.

        **参数解释**：查询后端服务器组可用区亲和性策略是否开启。示例如下： \"az_affinity\": {             \"enable\": \"true\"         } 支持多值查询，查询条件格式： *az_affinity=enable=true&az_affinity=enable=false*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The az_affinity of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._az_affinity

    @az_affinity.setter
    def az_affinity(self, az_affinity):
        r"""Sets the az_affinity of this ListPoolsRequest.

        **参数解释**：查询后端服务器组可用区亲和性策略是否开启。示例如下： \"az_affinity\": {             \"enable\": \"true\"         } 支持多值查询，查询条件格式： *az_affinity=enable=true&az_affinity=enable=false*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param az_affinity: The az_affinity of this ListPoolsRequest.
        :type az_affinity: list[str]
        """
        self._az_affinity = az_affinity

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
        if not isinstance(other, ListPoolsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
