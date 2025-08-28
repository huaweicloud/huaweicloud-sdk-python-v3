# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePoolOption:

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
        'lb_algorithm': 'str',
        'listener_id': 'str',
        'loadbalancer_id': 'str',
        'name': 'str',
        'project_id': 'str',
        'protocol': 'str',
        'session_persistence': 'CreatePoolSessionPersistenceOption',
        'slow_start': 'CreatePoolSlowStartOption',
        'member_deletion_protection_enable': 'bool',
        'vpc_id': 'str',
        'type': 'str',
        'ip_version': 'str',
        'protection_status': 'str',
        'protection_reason': 'str',
        'any_port_enable': 'bool',
        'connection_drain': 'ConnectionDrain',
        'pool_health': 'PoolHealth',
        'public_border_group': 'str',
        'quic_cid_hash_strategy': 'QuicCidHashStrategy'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'az_affinity': 'az_affinity',
        'description': 'description',
        'lb_algorithm': 'lb_algorithm',
        'listener_id': 'listener_id',
        'loadbalancer_id': 'loadbalancer_id',
        'name': 'name',
        'project_id': 'project_id',
        'protocol': 'protocol',
        'session_persistence': 'session_persistence',
        'slow_start': 'slow_start',
        'member_deletion_protection_enable': 'member_deletion_protection_enable',
        'vpc_id': 'vpc_id',
        'type': 'type',
        'ip_version': 'ip_version',
        'protection_status': 'protection_status',
        'protection_reason': 'protection_reason',
        'any_port_enable': 'any_port_enable',
        'connection_drain': 'connection_drain',
        'pool_health': 'pool_health',
        'public_border_group': 'public_border_group',
        'quic_cid_hash_strategy': 'quic_cid_hash_strategy'
    }

    def __init__(self, admin_state_up=None, az_affinity=None, description=None, lb_algorithm=None, listener_id=None, loadbalancer_id=None, name=None, project_id=None, protocol=None, session_persistence=None, slow_start=None, member_deletion_protection_enable=None, vpc_id=None, type=None, ip_version=None, protection_status=None, protection_reason=None, any_port_enable=None, connection_drain=None, pool_health=None, public_border_group=None, quic_cid_hash_strategy=None):
        r"""CreatePoolOption

        The model defined in huaweicloud sdk

        :param admin_state_up: **参数解释**：后端服务器组的管理状态。  **约束限制**：只支持设置为true。  **取值范围**：true  **默认取值**：true  [不支持该字段，请勿使用。](tag:dt,hcso_dt)
        :type admin_state_up: bool
        :param az_affinity: 
        :type az_affinity: :class:`huaweicloudsdkelb.v3.AzAffinity`
        :param description: **参数解释**：后端服务器组的描述信息。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type description: str
        :param lb_algorithm: **参数解释**：后端服务器组的负载均衡算法。  **约束限制**： - 当该字段的取值为SOURCE_IP或QUIC_CID时，后端服务器组绑定的后端服务器的weight字段无效。 - 只有pool的protocol为QUIC时，才支持QUIC_CID算法。 [- 不支持QUIC_CID。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  **取值范围**： - ROUND_ROBIN：加权轮询算法。 - LEAST_CONNECTIONS：加权最少连接算法。 - SOURCE_IP：源IP算法。 - QUIC_CID：连接ID算法。 [- 2_TUPLE_HASH：二元组hash算法，仅IP类型的pool支持。 - 3_TUPLE_HASH：三元组hash算法，仅IP类型的pool支持。 - 5_TUPLE_HASH：五元组hash算法，仅IP类型的pool支持。 - IP型pool不指定该字段时，默认设置为5_TUPLE_HASH。](tag:hws_eu)  **默认取值**：不涉及  [荷兰region不支持QUIC_CID。](tag:dt)
        :type lb_algorithm: str
        :param listener_id: **参数解释**：后端服务器组关联的监听器的ID。  **约束限制**： - listener_id，loadbalancer_id，type至少指定一个。 [- 独享型实例的后端服务器组loadbalancer_id和listener_id可以都不指定，但共享型实例至少指定一个。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)  **取值范围**：不涉及  **默认取值**：不涉及
        :type listener_id: str
        :param loadbalancer_id: **参数解释**：后端服务器组关联的负载均衡器ID。  **约束限制**： - listener_id，loadbalancer_id，type至少指定一个。 [- 独享型实例的后端服务器组loadbalancer_id和listener_id可以都不指定，但共享型实例至少指定一个。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)  **取值范围**：不涉及  **默认取值**：不涉及
        :type loadbalancer_id: str
        :param name: **参数解释**：后端服务器组的名称。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type name: str
        :param project_id: **参数解释**：后端服务器组所属的项目ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type project_id: str
        :param protocol: **参数解释**：后端服务器组的后端协议。  **约束限制**： - listener的protocol为UDP时，pool的protocol必须为UDP或QUIC。 - listener的protocol为TCP时pool的protocol必须为TCP。 [- listener的protocol为IP时，pool的protocol必须为IP。](tag:hws_eu) - listener的protocol为HTTP时，pool的protocol必须为HTTP。 - listener的protocol为HTTPS时，pool的protocol必须为HTTP、HTTPS或GRPC。 - listener的protocol为TERMINATED_HTTPS时，pool的protocol必须为HTTP。 - listener的protocol为QUIC时，pool的protocol必须为HTTP、HTTPS或GRPC。 - listener的protocol为TLS时，pool的protocol必须为TLS或TCP（且只能使用ip_version为v4的TCP pool）。 - 若pool的protocol为QUIC，则必须开启session_persistence且type为SOURCE_IP。 - 若pool的protocol为GRPC，关联监听器的http2_enable必须为true。 [- 不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  **取值范围**：TCP、UDP、[IP、](tag:hws_eu)TLS、GRPC、HTTP、HTTPS和QUIC。  **默认取值**：不涉及  [荷兰region不支持QUIC。](tag:dt)
        :type protocol: str
        :param session_persistence: 
        :type session_persistence: :class:`huaweicloudsdkelb.v3.CreatePoolSessionPersistenceOption`
        :param slow_start: 
        :type slow_start: :class:`huaweicloudsdkelb.v3.CreatePoolSlowStartOption`
        :param member_deletion_protection_enable: **参数解释**：是否开启后端服务器移除保护。开关开启后，不允许从该ELB后端服务器组下移除后端服务器。  **约束限制**： - 开关开启后，移除member会报错拦截，涉及如下API:   + 级联删除负载均衡器（DELETE /v3/{project_id}/elb/loadbalancers/{loadbalancer_id}/force-elb）   + 级联删除负载均衡器及关联EIP（POST /v3/{project_id}/elb/loadbalancers/{loadbalancer_id}/delete-cascade）   + 级联删除监听器（DELETE /v3/{project_id}/elb/listeners/{listener_id}/force）   + 级联删除后端服务器组（DELETE /v3/{project_id}/elb/pools/{pool_id}/delete-cascade）   + 删除后端服务器（DELETE /v3/{project_id}/elb/pools/{pool_id}/members/{member_id}）   + 批量删除后端服务器（POST /v3/{project_id}/elb/pools/{pool_id}/members/batch-delete）  **取值范围**：false 不开启，true 开启。  **默认取值**：false  &gt; 退场时需要先关闭所有资源的删除保护开关。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)  [荷兰region不支持该字段，请勿使用。](tag:dt)
        :type member_deletion_protection_enable: bool
        :param vpc_id: **参数解释**：后端服务器组关联的虚拟私有云的ID。  **约束限制**： - 只能挂载到该虚拟私有云下。 - 只能添加该虚拟私有云下的后端服务器或跨VPC的后端服务器。 - type必须指定为instance。 [- pool的protocol为IP时，必须指定vpc_id，且与LB的vpc_id相同。](tag:hws_eu) - 若未指定vpc_id，则后续添加后端服务器时，vpc_id由后端服务器所在的虚拟私有云确定。  **取值范围**：不涉及  **默认取值**：不涉及
        :type vpc_id: str
        :param type: **参数解释**：后端服务器组的类型。  **约束限制**： - 不传表示允许任意类型的后端，并返回type为空字符串。 - listener_id，loadbalancer_id，type至少指定一个。 [- 独享型实例的后端服务器组loadbalancer_id和listener_id可以都不指定，但共享型实例至少指定一个。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)  **取值范围**： - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加IP类型后端，type指定为该类型时，vpc_id不允许指定。[pool的protocol为IP时，type不允许设置为ip。](tag:hws_eu)]  **默认取值**：不涉及
        :type type: str
        :param ip_version: **参数解释**：后端服务器组支持的IP版本。  **约束限制**：不涉及  [**取值范围**： - 共享型：固定为v4； - 独享型：取值dualstack、v4。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。当协议为HTTP时，ip_version为v4。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs)  [**取值范围**：dualstack、v4。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。当协议为HTTP时，ip_version为v4。](tag:hcso_dt)  **默认取值**：不涉及  [不支持IPv6，只会返回v4。](tag:dt)
        :type ip_version: str
        :param protection_status: **参数解释**：修改保护状态。  **约束限制**：不涉及  **取值范围**： - nonProtection: 不保护，默认值为nonProtection - consoleProtection: 控制台修改保护   **默认取值**：不涉及
        :type protection_status: str
        :param protection_reason: **参数解释**：设置保护的原因。作为protection_status的转态设置的原因。  **约束限制**：仅当protection_status为consoleProtection时有效。  **取值范围**：除&#39;&lt;&#39;和&#39;&gt;&#39;外通用Unicode字符集字符，最大255个字符。  **默认取值**：不涉及
        :type protection_reason: str
        :param any_port_enable: **参数解释**：后端是否开启全端口转发。开启后，后端服务器端口与前端监听器端口保持一致。关闭后，请求会转发给后端服务器protocol_port字段指定端口。  **约束限制**： - 仅QUIC,TCP,UDP的pool支持。  **取值范围**：false 不开启，true 开启。  **默认取值**：不涉及
        :type any_port_enable: bool
        :param connection_drain: 
        :type connection_drain: :class:`huaweicloudsdkelb.v3.ConnectionDrain`
        :param pool_health: 
        :type pool_health: :class:`huaweicloudsdkelb.v3.PoolHealth`
        :param public_border_group: **参数解释**：公网边界组。  **约束限制**：不涉及  **取值范围**： - center：表示中心站点的公网边界组 - 边缘站点名称：表示边缘站点的公网边界组  **默认取值**：不涉及
        :type public_border_group: str
        :param quic_cid_hash_strategy: 
        :type quic_cid_hash_strategy: :class:`huaweicloudsdkelb.v3.QuicCidHashStrategy`
        """
        
        

        self._admin_state_up = None
        self._az_affinity = None
        self._description = None
        self._lb_algorithm = None
        self._listener_id = None
        self._loadbalancer_id = None
        self._name = None
        self._project_id = None
        self._protocol = None
        self._session_persistence = None
        self._slow_start = None
        self._member_deletion_protection_enable = None
        self._vpc_id = None
        self._type = None
        self._ip_version = None
        self._protection_status = None
        self._protection_reason = None
        self._any_port_enable = None
        self._connection_drain = None
        self._pool_health = None
        self._public_border_group = None
        self._quic_cid_hash_strategy = None
        self.discriminator = None

        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if az_affinity is not None:
            self.az_affinity = az_affinity
        if description is not None:
            self.description = description
        self.lb_algorithm = lb_algorithm
        if listener_id is not None:
            self.listener_id = listener_id
        if loadbalancer_id is not None:
            self.loadbalancer_id = loadbalancer_id
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        self.protocol = protocol
        if session_persistence is not None:
            self.session_persistence = session_persistence
        if slow_start is not None:
            self.slow_start = slow_start
        if member_deletion_protection_enable is not None:
            self.member_deletion_protection_enable = member_deletion_protection_enable
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if type is not None:
            self.type = type
        if ip_version is not None:
            self.ip_version = ip_version
        if protection_status is not None:
            self.protection_status = protection_status
        if protection_reason is not None:
            self.protection_reason = protection_reason
        if any_port_enable is not None:
            self.any_port_enable = any_port_enable
        if connection_drain is not None:
            self.connection_drain = connection_drain
        if pool_health is not None:
            self.pool_health = pool_health
        if public_border_group is not None:
            self.public_border_group = public_border_group
        if quic_cid_hash_strategy is not None:
            self.quic_cid_hash_strategy = quic_cid_hash_strategy

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this CreatePoolOption.

        **参数解释**：后端服务器组的管理状态。  **约束限制**：只支持设置为true。  **取值范围**：true  **默认取值**：true  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :return: The admin_state_up of this CreatePoolOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this CreatePoolOption.

        **参数解释**：后端服务器组的管理状态。  **约束限制**：只支持设置为true。  **取值范围**：true  **默认取值**：true  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :param admin_state_up: The admin_state_up of this CreatePoolOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def az_affinity(self):
        r"""Gets the az_affinity of this CreatePoolOption.

        :return: The az_affinity of this CreatePoolOption.
        :rtype: :class:`huaweicloudsdkelb.v3.AzAffinity`
        """
        return self._az_affinity

    @az_affinity.setter
    def az_affinity(self, az_affinity):
        r"""Sets the az_affinity of this CreatePoolOption.

        :param az_affinity: The az_affinity of this CreatePoolOption.
        :type az_affinity: :class:`huaweicloudsdkelb.v3.AzAffinity`
        """
        self._az_affinity = az_affinity

    @property
    def description(self):
        r"""Gets the description of this CreatePoolOption.

        **参数解释**：后端服务器组的描述信息。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The description of this CreatePoolOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreatePoolOption.

        **参数解释**：后端服务器组的描述信息。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param description: The description of this CreatePoolOption.
        :type description: str
        """
        self._description = description

    @property
    def lb_algorithm(self):
        r"""Gets the lb_algorithm of this CreatePoolOption.

        **参数解释**：后端服务器组的负载均衡算法。  **约束限制**： - 当该字段的取值为SOURCE_IP或QUIC_CID时，后端服务器组绑定的后端服务器的weight字段无效。 - 只有pool的protocol为QUIC时，才支持QUIC_CID算法。 [- 不支持QUIC_CID。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  **取值范围**： - ROUND_ROBIN：加权轮询算法。 - LEAST_CONNECTIONS：加权最少连接算法。 - SOURCE_IP：源IP算法。 - QUIC_CID：连接ID算法。 [- 2_TUPLE_HASH：二元组hash算法，仅IP类型的pool支持。 - 3_TUPLE_HASH：三元组hash算法，仅IP类型的pool支持。 - 5_TUPLE_HASH：五元组hash算法，仅IP类型的pool支持。 - IP型pool不指定该字段时，默认设置为5_TUPLE_HASH。](tag:hws_eu)  **默认取值**：不涉及  [荷兰region不支持QUIC_CID。](tag:dt)

        :return: The lb_algorithm of this CreatePoolOption.
        :rtype: str
        """
        return self._lb_algorithm

    @lb_algorithm.setter
    def lb_algorithm(self, lb_algorithm):
        r"""Sets the lb_algorithm of this CreatePoolOption.

        **参数解释**：后端服务器组的负载均衡算法。  **约束限制**： - 当该字段的取值为SOURCE_IP或QUIC_CID时，后端服务器组绑定的后端服务器的weight字段无效。 - 只有pool的protocol为QUIC时，才支持QUIC_CID算法。 [- 不支持QUIC_CID。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  **取值范围**： - ROUND_ROBIN：加权轮询算法。 - LEAST_CONNECTIONS：加权最少连接算法。 - SOURCE_IP：源IP算法。 - QUIC_CID：连接ID算法。 [- 2_TUPLE_HASH：二元组hash算法，仅IP类型的pool支持。 - 3_TUPLE_HASH：三元组hash算法，仅IP类型的pool支持。 - 5_TUPLE_HASH：五元组hash算法，仅IP类型的pool支持。 - IP型pool不指定该字段时，默认设置为5_TUPLE_HASH。](tag:hws_eu)  **默认取值**：不涉及  [荷兰region不支持QUIC_CID。](tag:dt)

        :param lb_algorithm: The lb_algorithm of this CreatePoolOption.
        :type lb_algorithm: str
        """
        self._lb_algorithm = lb_algorithm

    @property
    def listener_id(self):
        r"""Gets the listener_id of this CreatePoolOption.

        **参数解释**：后端服务器组关联的监听器的ID。  **约束限制**： - listener_id，loadbalancer_id，type至少指定一个。 [- 独享型实例的后端服务器组loadbalancer_id和listener_id可以都不指定，但共享型实例至少指定一个。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The listener_id of this CreatePoolOption.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        r"""Sets the listener_id of this CreatePoolOption.

        **参数解释**：后端服务器组关联的监听器的ID。  **约束限制**： - listener_id，loadbalancer_id，type至少指定一个。 [- 独享型实例的后端服务器组loadbalancer_id和listener_id可以都不指定，但共享型实例至少指定一个。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)  **取值范围**：不涉及  **默认取值**：不涉及

        :param listener_id: The listener_id of this CreatePoolOption.
        :type listener_id: str
        """
        self._listener_id = listener_id

    @property
    def loadbalancer_id(self):
        r"""Gets the loadbalancer_id of this CreatePoolOption.

        **参数解释**：后端服务器组关联的负载均衡器ID。  **约束限制**： - listener_id，loadbalancer_id，type至少指定一个。 [- 独享型实例的后端服务器组loadbalancer_id和listener_id可以都不指定，但共享型实例至少指定一个。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The loadbalancer_id of this CreatePoolOption.
        :rtype: str
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        r"""Sets the loadbalancer_id of this CreatePoolOption.

        **参数解释**：后端服务器组关联的负载均衡器ID。  **约束限制**： - listener_id，loadbalancer_id，type至少指定一个。 [- 独享型实例的后端服务器组loadbalancer_id和listener_id可以都不指定，但共享型实例至少指定一个。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)  **取值范围**：不涉及  **默认取值**：不涉及

        :param loadbalancer_id: The loadbalancer_id of this CreatePoolOption.
        :type loadbalancer_id: str
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def name(self):
        r"""Gets the name of this CreatePoolOption.

        **参数解释**：后端服务器组的名称。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The name of this CreatePoolOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreatePoolOption.

        **参数解释**：后端服务器组的名称。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param name: The name of this CreatePoolOption.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this CreatePoolOption.

        **参数解释**：后端服务器组所属的项目ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The project_id of this CreatePoolOption.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreatePoolOption.

        **参数解释**：后端服务器组所属的项目ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param project_id: The project_id of this CreatePoolOption.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def protocol(self):
        r"""Gets the protocol of this CreatePoolOption.

        **参数解释**：后端服务器组的后端协议。  **约束限制**： - listener的protocol为UDP时，pool的protocol必须为UDP或QUIC。 - listener的protocol为TCP时pool的protocol必须为TCP。 [- listener的protocol为IP时，pool的protocol必须为IP。](tag:hws_eu) - listener的protocol为HTTP时，pool的protocol必须为HTTP。 - listener的protocol为HTTPS时，pool的protocol必须为HTTP、HTTPS或GRPC。 - listener的protocol为TERMINATED_HTTPS时，pool的protocol必须为HTTP。 - listener的protocol为QUIC时，pool的protocol必须为HTTP、HTTPS或GRPC。 - listener的protocol为TLS时，pool的protocol必须为TLS或TCP（且只能使用ip_version为v4的TCP pool）。 - 若pool的protocol为QUIC，则必须开启session_persistence且type为SOURCE_IP。 - 若pool的protocol为GRPC，关联监听器的http2_enable必须为true。 [- 不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  **取值范围**：TCP、UDP、[IP、](tag:hws_eu)TLS、GRPC、HTTP、HTTPS和QUIC。  **默认取值**：不涉及  [荷兰region不支持QUIC。](tag:dt)

        :return: The protocol of this CreatePoolOption.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this CreatePoolOption.

        **参数解释**：后端服务器组的后端协议。  **约束限制**： - listener的protocol为UDP时，pool的protocol必须为UDP或QUIC。 - listener的protocol为TCP时pool的protocol必须为TCP。 [- listener的protocol为IP时，pool的protocol必须为IP。](tag:hws_eu) - listener的protocol为HTTP时，pool的protocol必须为HTTP。 - listener的protocol为HTTPS时，pool的protocol必须为HTTP、HTTPS或GRPC。 - listener的protocol为TERMINATED_HTTPS时，pool的protocol必须为HTTP。 - listener的protocol为QUIC时，pool的protocol必须为HTTP、HTTPS或GRPC。 - listener的protocol为TLS时，pool的protocol必须为TLS或TCP（且只能使用ip_version为v4的TCP pool）。 - 若pool的protocol为QUIC，则必须开启session_persistence且type为SOURCE_IP。 - 若pool的protocol为GRPC，关联监听器的http2_enable必须为true。 [- 不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  **取值范围**：TCP、UDP、[IP、](tag:hws_eu)TLS、GRPC、HTTP、HTTPS和QUIC。  **默认取值**：不涉及  [荷兰region不支持QUIC。](tag:dt)

        :param protocol: The protocol of this CreatePoolOption.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def session_persistence(self):
        r"""Gets the session_persistence of this CreatePoolOption.

        :return: The session_persistence of this CreatePoolOption.
        :rtype: :class:`huaweicloudsdkelb.v3.CreatePoolSessionPersistenceOption`
        """
        return self._session_persistence

    @session_persistence.setter
    def session_persistence(self, session_persistence):
        r"""Sets the session_persistence of this CreatePoolOption.

        :param session_persistence: The session_persistence of this CreatePoolOption.
        :type session_persistence: :class:`huaweicloudsdkelb.v3.CreatePoolSessionPersistenceOption`
        """
        self._session_persistence = session_persistence

    @property
    def slow_start(self):
        r"""Gets the slow_start of this CreatePoolOption.

        :return: The slow_start of this CreatePoolOption.
        :rtype: :class:`huaweicloudsdkelb.v3.CreatePoolSlowStartOption`
        """
        return self._slow_start

    @slow_start.setter
    def slow_start(self, slow_start):
        r"""Sets the slow_start of this CreatePoolOption.

        :param slow_start: The slow_start of this CreatePoolOption.
        :type slow_start: :class:`huaweicloudsdkelb.v3.CreatePoolSlowStartOption`
        """
        self._slow_start = slow_start

    @property
    def member_deletion_protection_enable(self):
        r"""Gets the member_deletion_protection_enable of this CreatePoolOption.

        **参数解释**：是否开启后端服务器移除保护。开关开启后，不允许从该ELB后端服务器组下移除后端服务器。  **约束限制**： - 开关开启后，移除member会报错拦截，涉及如下API:   + 级联删除负载均衡器（DELETE /v3/{project_id}/elb/loadbalancers/{loadbalancer_id}/force-elb）   + 级联删除负载均衡器及关联EIP（POST /v3/{project_id}/elb/loadbalancers/{loadbalancer_id}/delete-cascade）   + 级联删除监听器（DELETE /v3/{project_id}/elb/listeners/{listener_id}/force）   + 级联删除后端服务器组（DELETE /v3/{project_id}/elb/pools/{pool_id}/delete-cascade）   + 删除后端服务器（DELETE /v3/{project_id}/elb/pools/{pool_id}/members/{member_id}）   + 批量删除后端服务器（POST /v3/{project_id}/elb/pools/{pool_id}/members/batch-delete）  **取值范围**：false 不开启，true 开启。  **默认取值**：false  > 退场时需要先关闭所有资源的删除保护开关。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :return: The member_deletion_protection_enable of this CreatePoolOption.
        :rtype: bool
        """
        return self._member_deletion_protection_enable

    @member_deletion_protection_enable.setter
    def member_deletion_protection_enable(self, member_deletion_protection_enable):
        r"""Sets the member_deletion_protection_enable of this CreatePoolOption.

        **参数解释**：是否开启后端服务器移除保护。开关开启后，不允许从该ELB后端服务器组下移除后端服务器。  **约束限制**： - 开关开启后，移除member会报错拦截，涉及如下API:   + 级联删除负载均衡器（DELETE /v3/{project_id}/elb/loadbalancers/{loadbalancer_id}/force-elb）   + 级联删除负载均衡器及关联EIP（POST /v3/{project_id}/elb/loadbalancers/{loadbalancer_id}/delete-cascade）   + 级联删除监听器（DELETE /v3/{project_id}/elb/listeners/{listener_id}/force）   + 级联删除后端服务器组（DELETE /v3/{project_id}/elb/pools/{pool_id}/delete-cascade）   + 删除后端服务器（DELETE /v3/{project_id}/elb/pools/{pool_id}/members/{member_id}）   + 批量删除后端服务器（POST /v3/{project_id}/elb/pools/{pool_id}/members/batch-delete）  **取值范围**：false 不开启，true 开启。  **默认取值**：false  > 退场时需要先关闭所有资源的删除保护开关。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :param member_deletion_protection_enable: The member_deletion_protection_enable of this CreatePoolOption.
        :type member_deletion_protection_enable: bool
        """
        self._member_deletion_protection_enable = member_deletion_protection_enable

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreatePoolOption.

        **参数解释**：后端服务器组关联的虚拟私有云的ID。  **约束限制**： - 只能挂载到该虚拟私有云下。 - 只能添加该虚拟私有云下的后端服务器或跨VPC的后端服务器。 - type必须指定为instance。 [- pool的protocol为IP时，必须指定vpc_id，且与LB的vpc_id相同。](tag:hws_eu) - 若未指定vpc_id，则后续添加后端服务器时，vpc_id由后端服务器所在的虚拟私有云确定。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The vpc_id of this CreatePoolOption.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreatePoolOption.

        **参数解释**：后端服务器组关联的虚拟私有云的ID。  **约束限制**： - 只能挂载到该虚拟私有云下。 - 只能添加该虚拟私有云下的后端服务器或跨VPC的后端服务器。 - type必须指定为instance。 [- pool的protocol为IP时，必须指定vpc_id，且与LB的vpc_id相同。](tag:hws_eu) - 若未指定vpc_id，则后续添加后端服务器时，vpc_id由后端服务器所在的虚拟私有云确定。  **取值范围**：不涉及  **默认取值**：不涉及

        :param vpc_id: The vpc_id of this CreatePoolOption.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def type(self):
        r"""Gets the type of this CreatePoolOption.

        **参数解释**：后端服务器组的类型。  **约束限制**： - 不传表示允许任意类型的后端，并返回type为空字符串。 - listener_id，loadbalancer_id，type至少指定一个。 [- 独享型实例的后端服务器组loadbalancer_id和listener_id可以都不指定，但共享型实例至少指定一个。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)  **取值范围**： - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加IP类型后端，type指定为该类型时，vpc_id不允许指定。[pool的protocol为IP时，type不允许设置为ip。](tag:hws_eu)]  **默认取值**：不涉及

        :return: The type of this CreatePoolOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreatePoolOption.

        **参数解释**：后端服务器组的类型。  **约束限制**： - 不传表示允许任意类型的后端，并返回type为空字符串。 - listener_id，loadbalancer_id，type至少指定一个。 [- 独享型实例的后端服务器组loadbalancer_id和listener_id可以都不指定，但共享型实例至少指定一个。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)  **取值范围**： - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加IP类型后端，type指定为该类型时，vpc_id不允许指定。[pool的protocol为IP时，type不允许设置为ip。](tag:hws_eu)]  **默认取值**：不涉及

        :param type: The type of this CreatePoolOption.
        :type type: str
        """
        self._type = type

    @property
    def ip_version(self):
        r"""Gets the ip_version of this CreatePoolOption.

        **参数解释**：后端服务器组支持的IP版本。  **约束限制**：不涉及  [**取值范围**： - 共享型：固定为v4； - 独享型：取值dualstack、v4。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。当协议为HTTP时，ip_version为v4。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs)  [**取值范围**：dualstack、v4。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。当协议为HTTP时，ip_version为v4。](tag:hcso_dt)  **默认取值**：不涉及  [不支持IPv6，只会返回v4。](tag:dt)

        :return: The ip_version of this CreatePoolOption.
        :rtype: str
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this CreatePoolOption.

        **参数解释**：后端服务器组支持的IP版本。  **约束限制**：不涉及  [**取值范围**： - 共享型：固定为v4； - 独享型：取值dualstack、v4。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。当协议为HTTP时，ip_version为v4。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs)  [**取值范围**：dualstack、v4。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。当协议为HTTP时，ip_version为v4。](tag:hcso_dt)  **默认取值**：不涉及  [不支持IPv6，只会返回v4。](tag:dt)

        :param ip_version: The ip_version of this CreatePoolOption.
        :type ip_version: str
        """
        self._ip_version = ip_version

    @property
    def protection_status(self):
        r"""Gets the protection_status of this CreatePoolOption.

        **参数解释**：修改保护状态。  **约束限制**：不涉及  **取值范围**： - nonProtection: 不保护，默认值为nonProtection - consoleProtection: 控制台修改保护   **默认取值**：不涉及

        :return: The protection_status of this CreatePoolOption.
        :rtype: str
        """
        return self._protection_status

    @protection_status.setter
    def protection_status(self, protection_status):
        r"""Sets the protection_status of this CreatePoolOption.

        **参数解释**：修改保护状态。  **约束限制**：不涉及  **取值范围**： - nonProtection: 不保护，默认值为nonProtection - consoleProtection: 控制台修改保护   **默认取值**：不涉及

        :param protection_status: The protection_status of this CreatePoolOption.
        :type protection_status: str
        """
        self._protection_status = protection_status

    @property
    def protection_reason(self):
        r"""Gets the protection_reason of this CreatePoolOption.

        **参数解释**：设置保护的原因。作为protection_status的转态设置的原因。  **约束限制**：仅当protection_status为consoleProtection时有效。  **取值范围**：除'<'和'>'外通用Unicode字符集字符，最大255个字符。  **默认取值**：不涉及

        :return: The protection_reason of this CreatePoolOption.
        :rtype: str
        """
        return self._protection_reason

    @protection_reason.setter
    def protection_reason(self, protection_reason):
        r"""Sets the protection_reason of this CreatePoolOption.

        **参数解释**：设置保护的原因。作为protection_status的转态设置的原因。  **约束限制**：仅当protection_status为consoleProtection时有效。  **取值范围**：除'<'和'>'外通用Unicode字符集字符，最大255个字符。  **默认取值**：不涉及

        :param protection_reason: The protection_reason of this CreatePoolOption.
        :type protection_reason: str
        """
        self._protection_reason = protection_reason

    @property
    def any_port_enable(self):
        r"""Gets the any_port_enable of this CreatePoolOption.

        **参数解释**：后端是否开启全端口转发。开启后，后端服务器端口与前端监听器端口保持一致。关闭后，请求会转发给后端服务器protocol_port字段指定端口。  **约束限制**： - 仅QUIC,TCP,UDP的pool支持。  **取值范围**：false 不开启，true 开启。  **默认取值**：不涉及

        :return: The any_port_enable of this CreatePoolOption.
        :rtype: bool
        """
        return self._any_port_enable

    @any_port_enable.setter
    def any_port_enable(self, any_port_enable):
        r"""Sets the any_port_enable of this CreatePoolOption.

        **参数解释**：后端是否开启全端口转发。开启后，后端服务器端口与前端监听器端口保持一致。关闭后，请求会转发给后端服务器protocol_port字段指定端口。  **约束限制**： - 仅QUIC,TCP,UDP的pool支持。  **取值范围**：false 不开启，true 开启。  **默认取值**：不涉及

        :param any_port_enable: The any_port_enable of this CreatePoolOption.
        :type any_port_enable: bool
        """
        self._any_port_enable = any_port_enable

    @property
    def connection_drain(self):
        r"""Gets the connection_drain of this CreatePoolOption.

        :return: The connection_drain of this CreatePoolOption.
        :rtype: :class:`huaweicloudsdkelb.v3.ConnectionDrain`
        """
        return self._connection_drain

    @connection_drain.setter
    def connection_drain(self, connection_drain):
        r"""Sets the connection_drain of this CreatePoolOption.

        :param connection_drain: The connection_drain of this CreatePoolOption.
        :type connection_drain: :class:`huaweicloudsdkelb.v3.ConnectionDrain`
        """
        self._connection_drain = connection_drain

    @property
    def pool_health(self):
        r"""Gets the pool_health of this CreatePoolOption.

        :return: The pool_health of this CreatePoolOption.
        :rtype: :class:`huaweicloudsdkelb.v3.PoolHealth`
        """
        return self._pool_health

    @pool_health.setter
    def pool_health(self, pool_health):
        r"""Sets the pool_health of this CreatePoolOption.

        :param pool_health: The pool_health of this CreatePoolOption.
        :type pool_health: :class:`huaweicloudsdkelb.v3.PoolHealth`
        """
        self._pool_health = pool_health

    @property
    def public_border_group(self):
        r"""Gets the public_border_group of this CreatePoolOption.

        **参数解释**：公网边界组。  **约束限制**：不涉及  **取值范围**： - center：表示中心站点的公网边界组 - 边缘站点名称：表示边缘站点的公网边界组  **默认取值**：不涉及

        :return: The public_border_group of this CreatePoolOption.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        r"""Sets the public_border_group of this CreatePoolOption.

        **参数解释**：公网边界组。  **约束限制**：不涉及  **取值范围**： - center：表示中心站点的公网边界组 - 边缘站点名称：表示边缘站点的公网边界组  **默认取值**：不涉及

        :param public_border_group: The public_border_group of this CreatePoolOption.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

    @property
    def quic_cid_hash_strategy(self):
        r"""Gets the quic_cid_hash_strategy of this CreatePoolOption.

        :return: The quic_cid_hash_strategy of this CreatePoolOption.
        :rtype: :class:`huaweicloudsdkelb.v3.QuicCidHashStrategy`
        """
        return self._quic_cid_hash_strategy

    @quic_cid_hash_strategy.setter
    def quic_cid_hash_strategy(self, quic_cid_hash_strategy):
        r"""Sets the quic_cid_hash_strategy of this CreatePoolOption.

        :param quic_cid_hash_strategy: The quic_cid_hash_strategy of this CreatePoolOption.
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
        if not isinstance(other, CreatePoolOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
