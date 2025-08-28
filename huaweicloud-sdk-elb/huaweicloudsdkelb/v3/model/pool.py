# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Pool:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'admin_state_up': 'bool',
        'az_affinity': 'AzAffinity',
        'description': 'str',
        'healthmonitor_id': 'str',
        'id': 'str',
        'lb_algorithm': 'str',
        'listeners': 'list[ListenerRef]',
        'loadbalancers': 'list[LoadBalancerRef]',
        'members': 'list[MemberRef]',
        'name': 'str',
        'project_id': 'str',
        'protocol': 'str',
        'session_persistence': 'SessionPersistence',
        'ip_version': 'str',
        'slow_start': 'SlowStart',
        'member_deletion_protection_enable': 'bool',
        'created_at': 'str',
        'updated_at': 'str',
        'vpc_id': 'str',
        'type': 'str',
        'protection_status': 'str',
        'protection_reason': 'str',
        'any_port_enable': 'bool',
        'connection_drain': 'ConnectionDrain',
        'enterprise_project_id': 'str',
        'pool_health': 'PoolHealth',
        'public_border_group': 'str',
        'quic_cid_hash_strategy': 'QuicCidHashStrategy'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'az_affinity': 'az_affinity',
        'description': 'description',
        'healthmonitor_id': 'healthmonitor_id',
        'id': 'id',
        'lb_algorithm': 'lb_algorithm',
        'listeners': 'listeners',
        'loadbalancers': 'loadbalancers',
        'members': 'members',
        'name': 'name',
        'project_id': 'project_id',
        'protocol': 'protocol',
        'session_persistence': 'session_persistence',
        'ip_version': 'ip_version',
        'slow_start': 'slow_start',
        'member_deletion_protection_enable': 'member_deletion_protection_enable',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'vpc_id': 'vpc_id',
        'type': 'type',
        'protection_status': 'protection_status',
        'protection_reason': 'protection_reason',
        'any_port_enable': 'any_port_enable',
        'connection_drain': 'connection_drain',
        'enterprise_project_id': 'enterprise_project_id',
        'pool_health': 'pool_health',
        'public_border_group': 'public_border_group',
        'quic_cid_hash_strategy': 'quic_cid_hash_strategy'
    }

    def __init__(self, admin_state_up=None, az_affinity=None, description=None, healthmonitor_id=None, id=None, lb_algorithm=None, listeners=None, loadbalancers=None, members=None, name=None, project_id=None, protocol=None, session_persistence=None, ip_version=None, slow_start=None, member_deletion_protection_enable=None, created_at=None, updated_at=None, vpc_id=None, type=None, protection_status=None, protection_reason=None, any_port_enable=None, connection_drain=None, enterprise_project_id=None, pool_health=None, public_border_group=None, quic_cid_hash_strategy=None):
        r"""Pool

        The model defined in huaweicloud sdk

        :param admin_state_up: **参数解释**：后端服务器组的管理状态。只支持设置为true。  **取值范围**：true 启用。  [不支持该字段，请勿使用。](tag:dt,hcso_dt)
        :type admin_state_up: bool
        :param az_affinity: 
        :type az_affinity: :class:`huaweicloudsdkelb.v3.AzAffinity`
        :param description: **参数解释**：后端服务器组的描述信息。  **取值范围**：不涉及
        :type description: str
        :param healthmonitor_id: **参数解释**：后端服务器组关联的健康检查的ID。  **取值范围**：不涉及
        :type healthmonitor_id: str
        :param id: **参数解释**：后端服务器组的ID。  **取值范围**：不涉及
        :type id: str
        :param lb_algorithm: **参数解释**：后端服务器组的负载均衡算法。  **取值范围**： - ROUND_ROBIN：加权轮询算法。 - LEAST_CONNECTIONS：加权最少连接算法。 - SOURCE_IP：源IP算法。 - QUIC_CID：连接ID算法。 [- 2_TUPLE_HASH：二元组hash算法，仅IP类型的pool支持。 - 3_TUPLE_HASH：三元组hash算法，仅IP类型的pool支持。 - 5_TUPLE_HASH：五元组hash算法，仅IP类型的pool支持。 - IP型pool不指定该字段时，默认设置为5_TUPLE_HASH。](tag:hws_eu)  [不支持QUIC_CID算法。](tag:hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC_CID。](tag:dt)
        :type lb_algorithm: str
        :param listeners: **参数解释**：后端服务器组关联的监听器ID列表。
        :type listeners: list[:class:`huaweicloudsdkelb.v3.ListenerRef`]
        :param loadbalancers: **参数解释**：后端服务器组关联的负载均衡器ID列表。
        :type loadbalancers: list[:class:`huaweicloudsdkelb.v3.LoadBalancerRef`]
        :param members: **参数解释**：后端服务器组中的后端服务器ID列表。
        :type members: list[:class:`huaweicloudsdkelb.v3.MemberRef`]
        :param name: **参数解释**：后端服务器组的名称。  **取值范围**：不涉及
        :type name: str
        :param project_id: **参数解释**：后端服务器组所在的项目ID。  **取值范围**：不涉及
        :type project_id: str
        :param protocol: **参数解释**：后端服务器组的后端协议。  **取值范围**：TCP、UDP、[IP、](tag:hws_eu)TLS、GRPC、HTTP、HTTPS和QUIC。  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC。](tag:dt)
        :type protocol: str
        :param session_persistence: 
        :type session_persistence: :class:`huaweicloudsdkelb.v3.SessionPersistence`
        :param ip_version: **参数解释**：后端服务器组支持的IP版本。  [**取值范围**： - 共享型：固定为v4； - 独享型：取值dualstack、v4。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。当协议为HTTP时，ip_version为v4。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs)  [**取值范围**：dualstack、v4。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。当协议为HTTP时，ip_version为v4。](tag:hcso_dt)  [不支持IPv6，只会返回v4。](tag:dt)
        :type ip_version: str
        :param slow_start: 
        :type slow_start: :class:`huaweicloudsdkelb.v3.SlowStart`
        :param member_deletion_protection_enable: **参数解释**：是否开启后端服务器移除保护。开关开启后，不允许从该ELB后端服务器组下移除后端服务器。  **取值范围**：false 不开启，true 开启。  &gt; 退场时需要先关闭所有资源的删除保护开关。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)  [荷兰region不支持该字段，请勿使用。](tag:dt)
        :type member_deletion_protection_enable: bool
        :param created_at: **参数解释**：创建时间。  **取值范围**：格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)
        :type created_at: str
        :param updated_at: **参数解释**：更新时间。  **取值范围**：格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)
        :type updated_at: str
        :param vpc_id: **参数解释**：后端服务器组关联的虚拟私有云的ID。  **取值范围**：不涉及
        :type vpc_id: str
        :param type: **参数解释**：后端服务器组的类型。  **取值范围**： - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加IP类型后端，type指定为该类型时，vpc_id不允许指定。[pool的protocol为IP时，type不允许设置为ip。](tag:hws_eu)] - 空字符串（\&quot;\&quot;）：允许任意类型的后端
        :type type: str
        :param protection_status: **参数解释**：修改保护状态,。  **取值范围**： - nonProtection: 不保护。 - consoleProtection: 控制台修改保护。
        :type protection_status: str
        :param protection_reason: **参数解释**：设置保护的原因。作为protection_status的转态设置的原因。  **取值范围**：除&#39;&lt;&#39;和&#39;&gt;&#39;外通用Unicode字符集字符，最大255个字符。
        :type protection_reason: str
        :param any_port_enable: **参数解释**：后端是否开启全端口转发。开启后，后端服务器端口与前端监听器端口保持一致。关闭后，请求会转发给后端服务器protocol_port字段指定端口。取值：false 不开启，true 开启。  **约束限制**： - 仅QUIC,TCP,UDP的pool支持。  [不支持该字段，请勿使用。](tag:hws_eu,hws_eu_wb,hws_test,dt,hcso_dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,g42,hk_g42)
        :type any_port_enable: bool
        :param connection_drain: 
        :type connection_drain: :class:`huaweicloudsdkelb.v3.ConnectionDrain`
        :param enterprise_project_id: **参数解释**：资源所属的企业项目ID。  **取值范围**： - \&quot;0\&quot;：表示资源属于default企业项目。 - UUID格式的字符串，表示非默认企业项目。  [不支持该字段，请勿使用。](tag:dt,hcso_dt)
        :type enterprise_project_id: str
        :param pool_health: 
        :type pool_health: :class:`huaweicloudsdkelb.v3.PoolHealth`
        :param public_border_group: **参数解释**：公网边界组。  **取值范围**： - center：表示中心站点的公网边界组 - 边缘站点名称：表示边缘站点的公网边界组  [不支持该字段，请勿使用。](tag:hws_eu,hws_eu_wb,hws_test,fcs,dt,hcso_dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,g42,hk_g42)
        :type public_border_group: str
        :param quic_cid_hash_strategy: 
        :type quic_cid_hash_strategy: :class:`huaweicloudsdkelb.v3.QuicCidHashStrategy`
        """
        
        

        self._admin_state_up = None
        self._az_affinity = None
        self._description = None
        self._healthmonitor_id = None
        self._id = None
        self._lb_algorithm = None
        self._listeners = None
        self._loadbalancers = None
        self._members = None
        self._name = None
        self._project_id = None
        self._protocol = None
        self._session_persistence = None
        self._ip_version = None
        self._slow_start = None
        self._member_deletion_protection_enable = None
        self._created_at = None
        self._updated_at = None
        self._vpc_id = None
        self._type = None
        self._protection_status = None
        self._protection_reason = None
        self._any_port_enable = None
        self._connection_drain = None
        self._enterprise_project_id = None
        self._pool_health = None
        self._public_border_group = None
        self._quic_cid_hash_strategy = None
        self.discriminator = None

        self.admin_state_up = admin_state_up
        if az_affinity is not None:
            self.az_affinity = az_affinity
        self.description = description
        self.healthmonitor_id = healthmonitor_id
        self.id = id
        self.lb_algorithm = lb_algorithm
        self.listeners = listeners
        self.loadbalancers = loadbalancers
        self.members = members
        self.name = name
        self.project_id = project_id
        self.protocol = protocol
        self.session_persistence = session_persistence
        self.ip_version = ip_version
        self.slow_start = slow_start
        self.member_deletion_protection_enable = member_deletion_protection_enable
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        self.vpc_id = vpc_id
        self.type = type
        if protection_status is not None:
            self.protection_status = protection_status
        if protection_reason is not None:
            self.protection_reason = protection_reason
        if any_port_enable is not None:
            self.any_port_enable = any_port_enable
        if connection_drain is not None:
            self.connection_drain = connection_drain
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if pool_health is not None:
            self.pool_health = pool_health
        if public_border_group is not None:
            self.public_border_group = public_border_group
        if quic_cid_hash_strategy is not None:
            self.quic_cid_hash_strategy = quic_cid_hash_strategy

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this Pool.

        **参数解释**：后端服务器组的管理状态。只支持设置为true。  **取值范围**：true 启用。  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :return: The admin_state_up of this Pool.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this Pool.

        **参数解释**：后端服务器组的管理状态。只支持设置为true。  **取值范围**：true 启用。  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :param admin_state_up: The admin_state_up of this Pool.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def az_affinity(self):
        r"""Gets the az_affinity of this Pool.

        :return: The az_affinity of this Pool.
        :rtype: :class:`huaweicloudsdkelb.v3.AzAffinity`
        """
        return self._az_affinity

    @az_affinity.setter
    def az_affinity(self, az_affinity):
        r"""Sets the az_affinity of this Pool.

        :param az_affinity: The az_affinity of this Pool.
        :type az_affinity: :class:`huaweicloudsdkelb.v3.AzAffinity`
        """
        self._az_affinity = az_affinity

    @property
    def description(self):
        r"""Gets the description of this Pool.

        **参数解释**：后端服务器组的描述信息。  **取值范围**：不涉及

        :return: The description of this Pool.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Pool.

        **参数解释**：后端服务器组的描述信息。  **取值范围**：不涉及

        :param description: The description of this Pool.
        :type description: str
        """
        self._description = description

    @property
    def healthmonitor_id(self):
        r"""Gets the healthmonitor_id of this Pool.

        **参数解释**：后端服务器组关联的健康检查的ID。  **取值范围**：不涉及

        :return: The healthmonitor_id of this Pool.
        :rtype: str
        """
        return self._healthmonitor_id

    @healthmonitor_id.setter
    def healthmonitor_id(self, healthmonitor_id):
        r"""Sets the healthmonitor_id of this Pool.

        **参数解释**：后端服务器组关联的健康检查的ID。  **取值范围**：不涉及

        :param healthmonitor_id: The healthmonitor_id of this Pool.
        :type healthmonitor_id: str
        """
        self._healthmonitor_id = healthmonitor_id

    @property
    def id(self):
        r"""Gets the id of this Pool.

        **参数解释**：后端服务器组的ID。  **取值范围**：不涉及

        :return: The id of this Pool.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Pool.

        **参数解释**：后端服务器组的ID。  **取值范围**：不涉及

        :param id: The id of this Pool.
        :type id: str
        """
        self._id = id

    @property
    def lb_algorithm(self):
        r"""Gets the lb_algorithm of this Pool.

        **参数解释**：后端服务器组的负载均衡算法。  **取值范围**： - ROUND_ROBIN：加权轮询算法。 - LEAST_CONNECTIONS：加权最少连接算法。 - SOURCE_IP：源IP算法。 - QUIC_CID：连接ID算法。 [- 2_TUPLE_HASH：二元组hash算法，仅IP类型的pool支持。 - 3_TUPLE_HASH：三元组hash算法，仅IP类型的pool支持。 - 5_TUPLE_HASH：五元组hash算法，仅IP类型的pool支持。 - IP型pool不指定该字段时，默认设置为5_TUPLE_HASH。](tag:hws_eu)  [不支持QUIC_CID算法。](tag:hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC_CID。](tag:dt)

        :return: The lb_algorithm of this Pool.
        :rtype: str
        """
        return self._lb_algorithm

    @lb_algorithm.setter
    def lb_algorithm(self, lb_algorithm):
        r"""Sets the lb_algorithm of this Pool.

        **参数解释**：后端服务器组的负载均衡算法。  **取值范围**： - ROUND_ROBIN：加权轮询算法。 - LEAST_CONNECTIONS：加权最少连接算法。 - SOURCE_IP：源IP算法。 - QUIC_CID：连接ID算法。 [- 2_TUPLE_HASH：二元组hash算法，仅IP类型的pool支持。 - 3_TUPLE_HASH：三元组hash算法，仅IP类型的pool支持。 - 5_TUPLE_HASH：五元组hash算法，仅IP类型的pool支持。 - IP型pool不指定该字段时，默认设置为5_TUPLE_HASH。](tag:hws_eu)  [不支持QUIC_CID算法。](tag:hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC_CID。](tag:dt)

        :param lb_algorithm: The lb_algorithm of this Pool.
        :type lb_algorithm: str
        """
        self._lb_algorithm = lb_algorithm

    @property
    def listeners(self):
        r"""Gets the listeners of this Pool.

        **参数解释**：后端服务器组关联的监听器ID列表。

        :return: The listeners of this Pool.
        :rtype: list[:class:`huaweicloudsdkelb.v3.ListenerRef`]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        r"""Sets the listeners of this Pool.

        **参数解释**：后端服务器组关联的监听器ID列表。

        :param listeners: The listeners of this Pool.
        :type listeners: list[:class:`huaweicloudsdkelb.v3.ListenerRef`]
        """
        self._listeners = listeners

    @property
    def loadbalancers(self):
        r"""Gets the loadbalancers of this Pool.

        **参数解释**：后端服务器组关联的负载均衡器ID列表。

        :return: The loadbalancers of this Pool.
        :rtype: list[:class:`huaweicloudsdkelb.v3.LoadBalancerRef`]
        """
        return self._loadbalancers

    @loadbalancers.setter
    def loadbalancers(self, loadbalancers):
        r"""Sets the loadbalancers of this Pool.

        **参数解释**：后端服务器组关联的负载均衡器ID列表。

        :param loadbalancers: The loadbalancers of this Pool.
        :type loadbalancers: list[:class:`huaweicloudsdkelb.v3.LoadBalancerRef`]
        """
        self._loadbalancers = loadbalancers

    @property
    def members(self):
        r"""Gets the members of this Pool.

        **参数解释**：后端服务器组中的后端服务器ID列表。

        :return: The members of this Pool.
        :rtype: list[:class:`huaweicloudsdkelb.v3.MemberRef`]
        """
        return self._members

    @members.setter
    def members(self, members):
        r"""Sets the members of this Pool.

        **参数解释**：后端服务器组中的后端服务器ID列表。

        :param members: The members of this Pool.
        :type members: list[:class:`huaweicloudsdkelb.v3.MemberRef`]
        """
        self._members = members

    @property
    def name(self):
        r"""Gets the name of this Pool.

        **参数解释**：后端服务器组的名称。  **取值范围**：不涉及

        :return: The name of this Pool.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Pool.

        **参数解释**：后端服务器组的名称。  **取值范围**：不涉及

        :param name: The name of this Pool.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this Pool.

        **参数解释**：后端服务器组所在的项目ID。  **取值范围**：不涉及

        :return: The project_id of this Pool.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this Pool.

        **参数解释**：后端服务器组所在的项目ID。  **取值范围**：不涉及

        :param project_id: The project_id of this Pool.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def protocol(self):
        r"""Gets the protocol of this Pool.

        **参数解释**：后端服务器组的后端协议。  **取值范围**：TCP、UDP、[IP、](tag:hws_eu)TLS、GRPC、HTTP、HTTPS和QUIC。  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC。](tag:dt)

        :return: The protocol of this Pool.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this Pool.

        **参数解释**：后端服务器组的后端协议。  **取值范围**：TCP、UDP、[IP、](tag:hws_eu)TLS、GRPC、HTTP、HTTPS和QUIC。  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC。](tag:dt)

        :param protocol: The protocol of this Pool.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def session_persistence(self):
        r"""Gets the session_persistence of this Pool.

        :return: The session_persistence of this Pool.
        :rtype: :class:`huaweicloudsdkelb.v3.SessionPersistence`
        """
        return self._session_persistence

    @session_persistence.setter
    def session_persistence(self, session_persistence):
        r"""Sets the session_persistence of this Pool.

        :param session_persistence: The session_persistence of this Pool.
        :type session_persistence: :class:`huaweicloudsdkelb.v3.SessionPersistence`
        """
        self._session_persistence = session_persistence

    @property
    def ip_version(self):
        r"""Gets the ip_version of this Pool.

        **参数解释**：后端服务器组支持的IP版本。  [**取值范围**： - 共享型：固定为v4； - 独享型：取值dualstack、v4。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。当协议为HTTP时，ip_version为v4。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs)  [**取值范围**：dualstack、v4。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。当协议为HTTP时，ip_version为v4。](tag:hcso_dt)  [不支持IPv6，只会返回v4。](tag:dt)

        :return: The ip_version of this Pool.
        :rtype: str
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this Pool.

        **参数解释**：后端服务器组支持的IP版本。  [**取值范围**： - 共享型：固定为v4； - 独享型：取值dualstack、v4。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。当协议为HTTP时，ip_version为v4。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs)  [**取值范围**：dualstack、v4。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。当协议为HTTP时，ip_version为v4。](tag:hcso_dt)  [不支持IPv6，只会返回v4。](tag:dt)

        :param ip_version: The ip_version of this Pool.
        :type ip_version: str
        """
        self._ip_version = ip_version

    @property
    def slow_start(self):
        r"""Gets the slow_start of this Pool.

        :return: The slow_start of this Pool.
        :rtype: :class:`huaweicloudsdkelb.v3.SlowStart`
        """
        return self._slow_start

    @slow_start.setter
    def slow_start(self, slow_start):
        r"""Sets the slow_start of this Pool.

        :param slow_start: The slow_start of this Pool.
        :type slow_start: :class:`huaweicloudsdkelb.v3.SlowStart`
        """
        self._slow_start = slow_start

    @property
    def member_deletion_protection_enable(self):
        r"""Gets the member_deletion_protection_enable of this Pool.

        **参数解释**：是否开启后端服务器移除保护。开关开启后，不允许从该ELB后端服务器组下移除后端服务器。  **取值范围**：false 不开启，true 开启。  > 退场时需要先关闭所有资源的删除保护开关。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :return: The member_deletion_protection_enable of this Pool.
        :rtype: bool
        """
        return self._member_deletion_protection_enable

    @member_deletion_protection_enable.setter
    def member_deletion_protection_enable(self, member_deletion_protection_enable):
        r"""Sets the member_deletion_protection_enable of this Pool.

        **参数解释**：是否开启后端服务器移除保护。开关开启后，不允许从该ELB后端服务器组下移除后端服务器。  **取值范围**：false 不开启，true 开启。  > 退场时需要先关闭所有资源的删除保护开关。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :param member_deletion_protection_enable: The member_deletion_protection_enable of this Pool.
        :type member_deletion_protection_enable: bool
        """
        self._member_deletion_protection_enable = member_deletion_protection_enable

    @property
    def created_at(self):
        r"""Gets the created_at of this Pool.

        **参数解释**：创建时间。  **取值范围**：格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)

        :return: The created_at of this Pool.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this Pool.

        **参数解释**：创建时间。  **取值范围**：格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)

        :param created_at: The created_at of this Pool.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this Pool.

        **参数解释**：更新时间。  **取值范围**：格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)

        :return: The updated_at of this Pool.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this Pool.

        **参数解释**：更新时间。  **取值范围**：格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)

        :param updated_at: The updated_at of this Pool.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this Pool.

        **参数解释**：后端服务器组关联的虚拟私有云的ID。  **取值范围**：不涉及

        :return: The vpc_id of this Pool.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this Pool.

        **参数解释**：后端服务器组关联的虚拟私有云的ID。  **取值范围**：不涉及

        :param vpc_id: The vpc_id of this Pool.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def type(self):
        r"""Gets the type of this Pool.

        **参数解释**：后端服务器组的类型。  **取值范围**： - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加IP类型后端，type指定为该类型时，vpc_id不允许指定。[pool的protocol为IP时，type不允许设置为ip。](tag:hws_eu)] - 空字符串（\"\"）：允许任意类型的后端

        :return: The type of this Pool.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Pool.

        **参数解释**：后端服务器组的类型。  **取值范围**： - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加IP类型后端，type指定为该类型时，vpc_id不允许指定。[pool的protocol为IP时，type不允许设置为ip。](tag:hws_eu)] - 空字符串（\"\"）：允许任意类型的后端

        :param type: The type of this Pool.
        :type type: str
        """
        self._type = type

    @property
    def protection_status(self):
        r"""Gets the protection_status of this Pool.

        **参数解释**：修改保护状态,。  **取值范围**： - nonProtection: 不保护。 - consoleProtection: 控制台修改保护。

        :return: The protection_status of this Pool.
        :rtype: str
        """
        return self._protection_status

    @protection_status.setter
    def protection_status(self, protection_status):
        r"""Sets the protection_status of this Pool.

        **参数解释**：修改保护状态,。  **取值范围**： - nonProtection: 不保护。 - consoleProtection: 控制台修改保护。

        :param protection_status: The protection_status of this Pool.
        :type protection_status: str
        """
        self._protection_status = protection_status

    @property
    def protection_reason(self):
        r"""Gets the protection_reason of this Pool.

        **参数解释**：设置保护的原因。作为protection_status的转态设置的原因。  **取值范围**：除'<'和'>'外通用Unicode字符集字符，最大255个字符。

        :return: The protection_reason of this Pool.
        :rtype: str
        """
        return self._protection_reason

    @protection_reason.setter
    def protection_reason(self, protection_reason):
        r"""Sets the protection_reason of this Pool.

        **参数解释**：设置保护的原因。作为protection_status的转态设置的原因。  **取值范围**：除'<'和'>'外通用Unicode字符集字符，最大255个字符。

        :param protection_reason: The protection_reason of this Pool.
        :type protection_reason: str
        """
        self._protection_reason = protection_reason

    @property
    def any_port_enable(self):
        r"""Gets the any_port_enable of this Pool.

        **参数解释**：后端是否开启全端口转发。开启后，后端服务器端口与前端监听器端口保持一致。关闭后，请求会转发给后端服务器protocol_port字段指定端口。取值：false 不开启，true 开启。  **约束限制**： - 仅QUIC,TCP,UDP的pool支持。  [不支持该字段，请勿使用。](tag:hws_eu,hws_eu_wb,hws_test,dt,hcso_dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,g42,hk_g42)

        :return: The any_port_enable of this Pool.
        :rtype: bool
        """
        return self._any_port_enable

    @any_port_enable.setter
    def any_port_enable(self, any_port_enable):
        r"""Sets the any_port_enable of this Pool.

        **参数解释**：后端是否开启全端口转发。开启后，后端服务器端口与前端监听器端口保持一致。关闭后，请求会转发给后端服务器protocol_port字段指定端口。取值：false 不开启，true 开启。  **约束限制**： - 仅QUIC,TCP,UDP的pool支持。  [不支持该字段，请勿使用。](tag:hws_eu,hws_eu_wb,hws_test,dt,hcso_dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,g42,hk_g42)

        :param any_port_enable: The any_port_enable of this Pool.
        :type any_port_enable: bool
        """
        self._any_port_enable = any_port_enable

    @property
    def connection_drain(self):
        r"""Gets the connection_drain of this Pool.

        :return: The connection_drain of this Pool.
        :rtype: :class:`huaweicloudsdkelb.v3.ConnectionDrain`
        """
        return self._connection_drain

    @connection_drain.setter
    def connection_drain(self, connection_drain):
        r"""Sets the connection_drain of this Pool.

        :param connection_drain: The connection_drain of this Pool.
        :type connection_drain: :class:`huaweicloudsdkelb.v3.ConnectionDrain`
        """
        self._connection_drain = connection_drain

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this Pool.

        **参数解释**：资源所属的企业项目ID。  **取值范围**： - \"0\"：表示资源属于default企业项目。 - UUID格式的字符串，表示非默认企业项目。  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :return: The enterprise_project_id of this Pool.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this Pool.

        **参数解释**：资源所属的企业项目ID。  **取值范围**： - \"0\"：表示资源属于default企业项目。 - UUID格式的字符串，表示非默认企业项目。  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :param enterprise_project_id: The enterprise_project_id of this Pool.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def pool_health(self):
        r"""Gets the pool_health of this Pool.

        :return: The pool_health of this Pool.
        :rtype: :class:`huaweicloudsdkelb.v3.PoolHealth`
        """
        return self._pool_health

    @pool_health.setter
    def pool_health(self, pool_health):
        r"""Sets the pool_health of this Pool.

        :param pool_health: The pool_health of this Pool.
        :type pool_health: :class:`huaweicloudsdkelb.v3.PoolHealth`
        """
        self._pool_health = pool_health

    @property
    def public_border_group(self):
        r"""Gets the public_border_group of this Pool.

        **参数解释**：公网边界组。  **取值范围**： - center：表示中心站点的公网边界组 - 边缘站点名称：表示边缘站点的公网边界组  [不支持该字段，请勿使用。](tag:hws_eu,hws_eu_wb,hws_test,fcs,dt,hcso_dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,g42,hk_g42)

        :return: The public_border_group of this Pool.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        r"""Sets the public_border_group of this Pool.

        **参数解释**：公网边界组。  **取值范围**： - center：表示中心站点的公网边界组 - 边缘站点名称：表示边缘站点的公网边界组  [不支持该字段，请勿使用。](tag:hws_eu,hws_eu_wb,hws_test,fcs,dt,hcso_dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,g42,hk_g42)

        :param public_border_group: The public_border_group of this Pool.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

    @property
    def quic_cid_hash_strategy(self):
        r"""Gets the quic_cid_hash_strategy of this Pool.

        :return: The quic_cid_hash_strategy of this Pool.
        :rtype: :class:`huaweicloudsdkelb.v3.QuicCidHashStrategy`
        """
        return self._quic_cid_hash_strategy

    @quic_cid_hash_strategy.setter
    def quic_cid_hash_strategy(self, quic_cid_hash_strategy):
        r"""Sets the quic_cid_hash_strategy of this Pool.

        :param quic_cid_hash_strategy: The quic_cid_hash_strategy of this Pool.
        :type quic_cid_hash_strategy: :class:`huaweicloudsdkelb.v3.QuicCidHashStrategy`
        """
        self._quic_cid_hash_strategy = quic_cid_hash_strategy

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
        if not isinstance(other, Pool):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
