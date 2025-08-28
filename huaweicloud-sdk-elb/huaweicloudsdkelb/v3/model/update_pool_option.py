# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePoolOption:

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
        'description': 'str',
        'lb_algorithm': 'str',
        'name': 'str',
        'session_persistence': 'UpdatePoolSessionPersistenceOption',
        'slow_start': 'UpdatePoolSlowStartOption',
        'member_deletion_protection_enable': 'bool',
        'vpc_id': 'str',
        'type': 'str',
        'protection_status': 'str',
        'protection_reason': 'str',
        'any_port_enable': 'bool',
        'connection_drain': 'ConnectionDrain',
        'pool_health': 'PoolHealth',
        'quic_cid_hash_strategy': 'QuicCidHashStrategy',
        'az_affinity': 'UpdateAzAffinity'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'description': 'description',
        'lb_algorithm': 'lb_algorithm',
        'name': 'name',
        'session_persistence': 'session_persistence',
        'slow_start': 'slow_start',
        'member_deletion_protection_enable': 'member_deletion_protection_enable',
        'vpc_id': 'vpc_id',
        'type': 'type',
        'protection_status': 'protection_status',
        'protection_reason': 'protection_reason',
        'any_port_enable': 'any_port_enable',
        'connection_drain': 'connection_drain',
        'pool_health': 'pool_health',
        'quic_cid_hash_strategy': 'quic_cid_hash_strategy',
        'az_affinity': 'az_affinity'
    }

    def __init__(self, admin_state_up=None, description=None, lb_algorithm=None, name=None, session_persistence=None, slow_start=None, member_deletion_protection_enable=None, vpc_id=None, type=None, protection_status=None, protection_reason=None, any_port_enable=None, connection_drain=None, pool_health=None, quic_cid_hash_strategy=None, az_affinity=None):
        r"""UpdatePoolOption

        The model defined in huaweicloud sdk

        :param admin_state_up: **参数解释**：后端服务器组的管理状态。  **约束限制**：只支持更新为true。  **取值范围**：true 启用。  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)
        :type admin_state_up: bool
        :param description: **参数解释**：后端服务器组的描述信息。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type description: str
        :param lb_algorithm: **参数解释**：后端服务器组的负载均衡算法。  **约束限制**： - 当该字段的取值为SOURCE_IP或QUIC_CID时，后端服务器组绑定的后端服务器的weight字段无效。 - 只有pool的protocol为QUIC时，才支持QUIC_CID算法。  **取值范围**： - ROUND_ROBIN：加权轮询算法。 - LEAST_CONNECTIONS：加权最少连接算法。 - SOURCE_IP：源IP算法。 - QUIC_CID：连接ID算法。 [- 2_TUPLE_HASH：二元组hash算法，仅IP类型的pool支持。 - 3_TUPLE_HASH：三元组hash算法，仅IP类型的pool支持。 - 5_TUPLE_HASH：五元组hash算法，仅IP类型的pool支持。 - IP型pool不指定该字段时，默认设置为5_TUPLE_HASH。](tag:hws_eu)  **默认取值**：不涉及  [不支持QUIC_CID。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC_CID。](tag:dt)
        :type lb_algorithm: str
        :param name: **参数解释**：后端服务器组的名称。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type name: str
        :param session_persistence: 
        :type session_persistence: :class:`huaweicloudsdkelb.v3.UpdatePoolSessionPersistenceOption`
        :param slow_start: 
        :type slow_start: :class:`huaweicloudsdkelb.v3.UpdatePoolSlowStartOption`
        :param member_deletion_protection_enable: **参数解释**：是否开启后端服务器移除保护。开关开启后，不允许从该ELB后端服务器组下移除后端服务器。  **约束限制**： - 开关开启后，移除member会报错拦截，涉及如下API:   + 级联删除负载均衡器（DELETE /v3/{project_id}/elb/loadbalancers/{loadbalancer_id}/force-elb）   + 级联删除负载均衡器及关联EIP（POST /v3/{project_id}/elb/loadbalancers/{loadbalancer_id}/delete-cascade）   + 级联删除监听器（DELETE /v3/{project_id}/elb/listeners/{listener_id}/force）   + 级联删除后端服务器组（DELETE /v3/{project_id}/elb/pools/{pool_id}/delete-cascade）   + 删除后端服务器（DELETE /v3/{project_id}/elb/pools/{pool_id}/members/{member_id}）   + 批量删除后端服务器（POST /v3/{project_id}/elb/pools/{pool_id}/members/batch-delete）   **取值范围**：false 不开启，true 开启。  **默认取值**：false  &gt; 退场时需要先关闭所有资源的删除保护开关。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)  [荷兰region不支持该字段，请勿使用。](tag:dt)
        :type member_deletion_protection_enable: bool
        :param vpc_id: **参数解释**：后端服务器组关联的虚拟私有云的ID。  **约束限制**：只有vpc_id为空时允许更新。  **取值范围**：不涉及  **默认取值**：不涉及
        :type vpc_id: str
        :param type: **参数解释**：后端服务器组的类型。  **约束限制**： - 只有type为空时允许更新，不允许从非空更新为空。 - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加IP类型后端，type指定为该类型时，vpc_id不允许指定。[pool的protocol为IP时，type不允许设置为ip。](tag:hws_eu)] - 空字符串（\&quot;\&quot;）：允许任意类型的后端  **取值范围**：不涉及  **默认取值**：不涉及
        :type type: str
        :param protection_status: **参数解释**：修改保护状态。  **约束限制**：不涉及  **取值范围**： - nonProtection: 不保护 - consoleProtection: 控制台修改保护  **默认取值**：不涉及
        :type protection_status: str
        :param protection_reason: **参数解释**：设置保护的原因。作为protection_status的转态设置的原因。  **约束限制**：仅当protection_status为consoleProtection时有效。  **取值范围**：除&#39;&lt;&#39;和&#39;&gt;&#39;外通用Unicode字符集字符，最大255个字符。  **默认取值**：不涉及
        :type protection_reason: str
        :param any_port_enable: **参数解释**：后端是否开启全端口转发。开启后，后端服务器端口与前端监听器端口保持一致。关闭后，请求会转发给后端服务器protocol_port字段指定端口。  **约束限制**：仅QUIC,TCP,UDP的pool支持。  **取值范围**：false 不开启，true 开启。  **默认取值**：false
        :type any_port_enable: bool
        :param connection_drain: 
        :type connection_drain: :class:`huaweicloudsdkelb.v3.ConnectionDrain`
        :param pool_health: 
        :type pool_health: :class:`huaweicloudsdkelb.v3.PoolHealth`
        :param quic_cid_hash_strategy: 
        :type quic_cid_hash_strategy: :class:`huaweicloudsdkelb.v3.QuicCidHashStrategy`
        :param az_affinity: 
        :type az_affinity: :class:`huaweicloudsdkelb.v3.UpdateAzAffinity`
        """
        
        

        self._admin_state_up = None
        self._description = None
        self._lb_algorithm = None
        self._name = None
        self._session_persistence = None
        self._slow_start = None
        self._member_deletion_protection_enable = None
        self._vpc_id = None
        self._type = None
        self._protection_status = None
        self._protection_reason = None
        self._any_port_enable = None
        self._connection_drain = None
        self._pool_health = None
        self._quic_cid_hash_strategy = None
        self._az_affinity = None
        self.discriminator = None

        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if description is not None:
            self.description = description
        if lb_algorithm is not None:
            self.lb_algorithm = lb_algorithm
        if name is not None:
            self.name = name
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
        if quic_cid_hash_strategy is not None:
            self.quic_cid_hash_strategy = quic_cid_hash_strategy
        if az_affinity is not None:
            self.az_affinity = az_affinity

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this UpdatePoolOption.

        **参数解释**：后端服务器组的管理状态。  **约束限制**：只支持更新为true。  **取值范围**：true 启用。  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :return: The admin_state_up of this UpdatePoolOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this UpdatePoolOption.

        **参数解释**：后端服务器组的管理状态。  **约束限制**：只支持更新为true。  **取值范围**：true 启用。  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :param admin_state_up: The admin_state_up of this UpdatePoolOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def description(self):
        r"""Gets the description of this UpdatePoolOption.

        **参数解释**：后端服务器组的描述信息。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The description of this UpdatePoolOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdatePoolOption.

        **参数解释**：后端服务器组的描述信息。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param description: The description of this UpdatePoolOption.
        :type description: str
        """
        self._description = description

    @property
    def lb_algorithm(self):
        r"""Gets the lb_algorithm of this UpdatePoolOption.

        **参数解释**：后端服务器组的负载均衡算法。  **约束限制**： - 当该字段的取值为SOURCE_IP或QUIC_CID时，后端服务器组绑定的后端服务器的weight字段无效。 - 只有pool的protocol为QUIC时，才支持QUIC_CID算法。  **取值范围**： - ROUND_ROBIN：加权轮询算法。 - LEAST_CONNECTIONS：加权最少连接算法。 - SOURCE_IP：源IP算法。 - QUIC_CID：连接ID算法。 [- 2_TUPLE_HASH：二元组hash算法，仅IP类型的pool支持。 - 3_TUPLE_HASH：三元组hash算法，仅IP类型的pool支持。 - 5_TUPLE_HASH：五元组hash算法，仅IP类型的pool支持。 - IP型pool不指定该字段时，默认设置为5_TUPLE_HASH。](tag:hws_eu)  **默认取值**：不涉及  [不支持QUIC_CID。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC_CID。](tag:dt)

        :return: The lb_algorithm of this UpdatePoolOption.
        :rtype: str
        """
        return self._lb_algorithm

    @lb_algorithm.setter
    def lb_algorithm(self, lb_algorithm):
        r"""Sets the lb_algorithm of this UpdatePoolOption.

        **参数解释**：后端服务器组的负载均衡算法。  **约束限制**： - 当该字段的取值为SOURCE_IP或QUIC_CID时，后端服务器组绑定的后端服务器的weight字段无效。 - 只有pool的protocol为QUIC时，才支持QUIC_CID算法。  **取值范围**： - ROUND_ROBIN：加权轮询算法。 - LEAST_CONNECTIONS：加权最少连接算法。 - SOURCE_IP：源IP算法。 - QUIC_CID：连接ID算法。 [- 2_TUPLE_HASH：二元组hash算法，仅IP类型的pool支持。 - 3_TUPLE_HASH：三元组hash算法，仅IP类型的pool支持。 - 5_TUPLE_HASH：五元组hash算法，仅IP类型的pool支持。 - IP型pool不指定该字段时，默认设置为5_TUPLE_HASH。](tag:hws_eu)  **默认取值**：不涉及  [不支持QUIC_CID。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC_CID。](tag:dt)

        :param lb_algorithm: The lb_algorithm of this UpdatePoolOption.
        :type lb_algorithm: str
        """
        self._lb_algorithm = lb_algorithm

    @property
    def name(self):
        r"""Gets the name of this UpdatePoolOption.

        **参数解释**：后端服务器组的名称。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The name of this UpdatePoolOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdatePoolOption.

        **参数解释**：后端服务器组的名称。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param name: The name of this UpdatePoolOption.
        :type name: str
        """
        self._name = name

    @property
    def session_persistence(self):
        r"""Gets the session_persistence of this UpdatePoolOption.

        :return: The session_persistence of this UpdatePoolOption.
        :rtype: :class:`huaweicloudsdkelb.v3.UpdatePoolSessionPersistenceOption`
        """
        return self._session_persistence

    @session_persistence.setter
    def session_persistence(self, session_persistence):
        r"""Sets the session_persistence of this UpdatePoolOption.

        :param session_persistence: The session_persistence of this UpdatePoolOption.
        :type session_persistence: :class:`huaweicloudsdkelb.v3.UpdatePoolSessionPersistenceOption`
        """
        self._session_persistence = session_persistence

    @property
    def slow_start(self):
        r"""Gets the slow_start of this UpdatePoolOption.

        :return: The slow_start of this UpdatePoolOption.
        :rtype: :class:`huaweicloudsdkelb.v3.UpdatePoolSlowStartOption`
        """
        return self._slow_start

    @slow_start.setter
    def slow_start(self, slow_start):
        r"""Sets the slow_start of this UpdatePoolOption.

        :param slow_start: The slow_start of this UpdatePoolOption.
        :type slow_start: :class:`huaweicloudsdkelb.v3.UpdatePoolSlowStartOption`
        """
        self._slow_start = slow_start

    @property
    def member_deletion_protection_enable(self):
        r"""Gets the member_deletion_protection_enable of this UpdatePoolOption.

        **参数解释**：是否开启后端服务器移除保护。开关开启后，不允许从该ELB后端服务器组下移除后端服务器。  **约束限制**： - 开关开启后，移除member会报错拦截，涉及如下API:   + 级联删除负载均衡器（DELETE /v3/{project_id}/elb/loadbalancers/{loadbalancer_id}/force-elb）   + 级联删除负载均衡器及关联EIP（POST /v3/{project_id}/elb/loadbalancers/{loadbalancer_id}/delete-cascade）   + 级联删除监听器（DELETE /v3/{project_id}/elb/listeners/{listener_id}/force）   + 级联删除后端服务器组（DELETE /v3/{project_id}/elb/pools/{pool_id}/delete-cascade）   + 删除后端服务器（DELETE /v3/{project_id}/elb/pools/{pool_id}/members/{member_id}）   + 批量删除后端服务器（POST /v3/{project_id}/elb/pools/{pool_id}/members/batch-delete）   **取值范围**：false 不开启，true 开启。  **默认取值**：false  > 退场时需要先关闭所有资源的删除保护开关。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :return: The member_deletion_protection_enable of this UpdatePoolOption.
        :rtype: bool
        """
        return self._member_deletion_protection_enable

    @member_deletion_protection_enable.setter
    def member_deletion_protection_enable(self, member_deletion_protection_enable):
        r"""Sets the member_deletion_protection_enable of this UpdatePoolOption.

        **参数解释**：是否开启后端服务器移除保护。开关开启后，不允许从该ELB后端服务器组下移除后端服务器。  **约束限制**： - 开关开启后，移除member会报错拦截，涉及如下API:   + 级联删除负载均衡器（DELETE /v3/{project_id}/elb/loadbalancers/{loadbalancer_id}/force-elb）   + 级联删除负载均衡器及关联EIP（POST /v3/{project_id}/elb/loadbalancers/{loadbalancer_id}/delete-cascade）   + 级联删除监听器（DELETE /v3/{project_id}/elb/listeners/{listener_id}/force）   + 级联删除后端服务器组（DELETE /v3/{project_id}/elb/pools/{pool_id}/delete-cascade）   + 删除后端服务器（DELETE /v3/{project_id}/elb/pools/{pool_id}/members/{member_id}）   + 批量删除后端服务器（POST /v3/{project_id}/elb/pools/{pool_id}/members/batch-delete）   **取值范围**：false 不开启，true 开启。  **默认取值**：false  > 退场时需要先关闭所有资源的删除保护开关。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :param member_deletion_protection_enable: The member_deletion_protection_enable of this UpdatePoolOption.
        :type member_deletion_protection_enable: bool
        """
        self._member_deletion_protection_enable = member_deletion_protection_enable

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this UpdatePoolOption.

        **参数解释**：后端服务器组关联的虚拟私有云的ID。  **约束限制**：只有vpc_id为空时允许更新。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The vpc_id of this UpdatePoolOption.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this UpdatePoolOption.

        **参数解释**：后端服务器组关联的虚拟私有云的ID。  **约束限制**：只有vpc_id为空时允许更新。  **取值范围**：不涉及  **默认取值**：不涉及

        :param vpc_id: The vpc_id of this UpdatePoolOption.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def type(self):
        r"""Gets the type of this UpdatePoolOption.

        **参数解释**：后端服务器组的类型。  **约束限制**： - 只有type为空时允许更新，不允许从非空更新为空。 - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加IP类型后端，type指定为该类型时，vpc_id不允许指定。[pool的protocol为IP时，type不允许设置为ip。](tag:hws_eu)] - 空字符串（\"\"）：允许任意类型的后端  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The type of this UpdatePoolOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UpdatePoolOption.

        **参数解释**：后端服务器组的类型。  **约束限制**： - 只有type为空时允许更新，不允许从非空更新为空。 - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加IP类型后端，type指定为该类型时，vpc_id不允许指定。[pool的protocol为IP时，type不允许设置为ip。](tag:hws_eu)] - 空字符串（\"\"）：允许任意类型的后端  **取值范围**：不涉及  **默认取值**：不涉及

        :param type: The type of this UpdatePoolOption.
        :type type: str
        """
        self._type = type

    @property
    def protection_status(self):
        r"""Gets the protection_status of this UpdatePoolOption.

        **参数解释**：修改保护状态。  **约束限制**：不涉及  **取值范围**： - nonProtection: 不保护 - consoleProtection: 控制台修改保护  **默认取值**：不涉及

        :return: The protection_status of this UpdatePoolOption.
        :rtype: str
        """
        return self._protection_status

    @protection_status.setter
    def protection_status(self, protection_status):
        r"""Sets the protection_status of this UpdatePoolOption.

        **参数解释**：修改保护状态。  **约束限制**：不涉及  **取值范围**： - nonProtection: 不保护 - consoleProtection: 控制台修改保护  **默认取值**：不涉及

        :param protection_status: The protection_status of this UpdatePoolOption.
        :type protection_status: str
        """
        self._protection_status = protection_status

    @property
    def protection_reason(self):
        r"""Gets the protection_reason of this UpdatePoolOption.

        **参数解释**：设置保护的原因。作为protection_status的转态设置的原因。  **约束限制**：仅当protection_status为consoleProtection时有效。  **取值范围**：除'<'和'>'外通用Unicode字符集字符，最大255个字符。  **默认取值**：不涉及

        :return: The protection_reason of this UpdatePoolOption.
        :rtype: str
        """
        return self._protection_reason

    @protection_reason.setter
    def protection_reason(self, protection_reason):
        r"""Sets the protection_reason of this UpdatePoolOption.

        **参数解释**：设置保护的原因。作为protection_status的转态设置的原因。  **约束限制**：仅当protection_status为consoleProtection时有效。  **取值范围**：除'<'和'>'外通用Unicode字符集字符，最大255个字符。  **默认取值**：不涉及

        :param protection_reason: The protection_reason of this UpdatePoolOption.
        :type protection_reason: str
        """
        self._protection_reason = protection_reason

    @property
    def any_port_enable(self):
        r"""Gets the any_port_enable of this UpdatePoolOption.

        **参数解释**：后端是否开启全端口转发。开启后，后端服务器端口与前端监听器端口保持一致。关闭后，请求会转发给后端服务器protocol_port字段指定端口。  **约束限制**：仅QUIC,TCP,UDP的pool支持。  **取值范围**：false 不开启，true 开启。  **默认取值**：false

        :return: The any_port_enable of this UpdatePoolOption.
        :rtype: bool
        """
        return self._any_port_enable

    @any_port_enable.setter
    def any_port_enable(self, any_port_enable):
        r"""Sets the any_port_enable of this UpdatePoolOption.

        **参数解释**：后端是否开启全端口转发。开启后，后端服务器端口与前端监听器端口保持一致。关闭后，请求会转发给后端服务器protocol_port字段指定端口。  **约束限制**：仅QUIC,TCP,UDP的pool支持。  **取值范围**：false 不开启，true 开启。  **默认取值**：false

        :param any_port_enable: The any_port_enable of this UpdatePoolOption.
        :type any_port_enable: bool
        """
        self._any_port_enable = any_port_enable

    @property
    def connection_drain(self):
        r"""Gets the connection_drain of this UpdatePoolOption.

        :return: The connection_drain of this UpdatePoolOption.
        :rtype: :class:`huaweicloudsdkelb.v3.ConnectionDrain`
        """
        return self._connection_drain

    @connection_drain.setter
    def connection_drain(self, connection_drain):
        r"""Sets the connection_drain of this UpdatePoolOption.

        :param connection_drain: The connection_drain of this UpdatePoolOption.
        :type connection_drain: :class:`huaweicloudsdkelb.v3.ConnectionDrain`
        """
        self._connection_drain = connection_drain

    @property
    def pool_health(self):
        r"""Gets the pool_health of this UpdatePoolOption.

        :return: The pool_health of this UpdatePoolOption.
        :rtype: :class:`huaweicloudsdkelb.v3.PoolHealth`
        """
        return self._pool_health

    @pool_health.setter
    def pool_health(self, pool_health):
        r"""Sets the pool_health of this UpdatePoolOption.

        :param pool_health: The pool_health of this UpdatePoolOption.
        :type pool_health: :class:`huaweicloudsdkelb.v3.PoolHealth`
        """
        self._pool_health = pool_health

    @property
    def quic_cid_hash_strategy(self):
        r"""Gets the quic_cid_hash_strategy of this UpdatePoolOption.

        :return: The quic_cid_hash_strategy of this UpdatePoolOption.
        :rtype: :class:`huaweicloudsdkelb.v3.QuicCidHashStrategy`
        """
        return self._quic_cid_hash_strategy

    @quic_cid_hash_strategy.setter
    def quic_cid_hash_strategy(self, quic_cid_hash_strategy):
        r"""Sets the quic_cid_hash_strategy of this UpdatePoolOption.

        :param quic_cid_hash_strategy: The quic_cid_hash_strategy of this UpdatePoolOption.
        :type quic_cid_hash_strategy: :class:`huaweicloudsdkelb.v3.QuicCidHashStrategy`
        """
        self._quic_cid_hash_strategy = quic_cid_hash_strategy

    @property
    def az_affinity(self):
        r"""Gets the az_affinity of this UpdatePoolOption.

        :return: The az_affinity of this UpdatePoolOption.
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateAzAffinity`
        """
        return self._az_affinity

    @az_affinity.setter
    def az_affinity(self, az_affinity):
        r"""Sets the az_affinity of this UpdatePoolOption.

        :param az_affinity: The az_affinity of this UpdatePoolOption.
        :type az_affinity: :class:`huaweicloudsdkelb.v3.UpdateAzAffinity`
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
        if not isinstance(other, UpdatePoolOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
