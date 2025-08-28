# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MasterSlavePool:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'id': 'str',
        'lb_algorithm': 'str',
        'listeners': 'list[ListenerRef]',
        'loadbalancers': 'list[LoadBalancerRef]',
        'members': 'list[MasterSlaveMember]',
        'name': 'str',
        'project_id': 'str',
        'protocol': 'str',
        'session_persistence': 'SessionPersistence',
        'ip_version': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'vpc_id': 'str',
        'type': 'str',
        'enterprise_project_id': 'str',
        'healthmonitor': 'MasterSlaveHealthMonitor',
        'any_port_enable': 'bool',
        'connection_drain': 'ConnectionDrain',
        'quic_cid_hash_strategy': 'QuicCidHashStrategy'
    }

    attribute_map = {
        'description': 'description',
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
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'vpc_id': 'vpc_id',
        'type': 'type',
        'enterprise_project_id': 'enterprise_project_id',
        'healthmonitor': 'healthmonitor',
        'any_port_enable': 'any_port_enable',
        'connection_drain': 'connection_drain',
        'quic_cid_hash_strategy': 'quic_cid_hash_strategy'
    }

    def __init__(self, description=None, id=None, lb_algorithm=None, listeners=None, loadbalancers=None, members=None, name=None, project_id=None, protocol=None, session_persistence=None, ip_version=None, created_at=None, updated_at=None, vpc_id=None, type=None, enterprise_project_id=None, healthmonitor=None, any_port_enable=None, connection_drain=None, quic_cid_hash_strategy=None):
        r"""MasterSlavePool

        The model defined in huaweicloud sdk

        :param description: **参数解释**：后端服务器组的描述信息。  **取值范围**：不涉及
        :type description: str
        :param id: **参数解释**：后端服务器组的ID。  **取值范围**：不涉及
        :type id: str
        :param lb_algorithm: **参数解释**：后端服务器组的负载均衡算法。  **取值范围**：不涉及 - ROUND_ROBIN：加权轮询算法。 - LEAST_CONNECTIONS：加权最少连接算法。 - SOURCE_IP：源IP算法。 - QUIC_CID：连接ID算法。  [不支持QUIC_CID。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC_CID。](tag:dt)
        :type lb_algorithm: str
        :param listeners: **参数解释**：后端服务器组关联的监听器ID列表。
        :type listeners: list[:class:`huaweicloudsdkelb.v3.ListenerRef`]
        :param loadbalancers: **参数解释**：后端服务器组关联的负载均衡器ID列表。
        :type loadbalancers: list[:class:`huaweicloudsdkelb.v3.LoadBalancerRef`]
        :param members: **参数解释**：后端服务器组中的后端服务器列表。
        :type members: list[:class:`huaweicloudsdkelb.v3.MasterSlaveMember`]
        :param name: **参数解释**：后端服务器组的名称。  **取值范围**：不涉及
        :type name: str
        :param project_id: **参数解释**：后端服务器组所在的项目ID。  **取值范围**：不涉及
        :type project_id: str
        :param protocol: **参数解释**：后端服务器组的后端协议。  **取值范围**：不涉及TCP、UDP、QUIC、TLS。  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC。](tag:dt)
        :type protocol: str
        :param session_persistence: 
        :type session_persistence: :class:`huaweicloudsdkelb.v3.SessionPersistence`
        :param ip_version: **参数解释**：后端服务器组支持的IP版本。  [**取值范围**： - 共享型：固定为v4； - 独享型：取值dualstack、v4。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。当协议为HTTP时，ip_version为v4。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs)  [**取值范围**：dualstack、v4。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。当协议为HTTP时，ip_version为v4。](tag:hcso_dt)  [不支持IPv6，只会返回v4。](tag:dt)
        :type ip_version: str
        :param created_at: **参数解释**：创建时间。格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，UTC时区。  **取值范围**：不涉及  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)
        :type created_at: str
        :param updated_at: **参数解释**：更新时间。格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，UTC时区。  **取值范围**：不涉及  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)
        :type updated_at: str
        :param vpc_id: **参数解释**：后端服务器组关联的虚拟私有云的ID。  **取值范围**：不涉及
        :type vpc_id: str
        :param type: **参数解释**：后端服务器组的类型。  **取值范围**：不涉及 - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加IP类型后端，type指定为该类型时，vpc_id不允许指定。 - 空字符串（\&quot;\&quot;）：允许任意类型的后端
        :type type: str
        :param enterprise_project_id: **参数解释**：资源所属的企业项目ID。  **取值范围**： - \&quot;0\&quot;：表示资源属于default企业项目。 - UUID格式的字符串，表示非默认企业项目。  [不支持该字段，请勿使用。](tag:dt,hcso_dt)
        :type enterprise_project_id: str
        :param healthmonitor: 
        :type healthmonitor: :class:`huaweicloudsdkelb.v3.MasterSlaveHealthMonitor`
        :param any_port_enable: **参数解释**：后端是否开启全端口转发。开启后，后端服务器端口与前端监听器端口保持一致。关闭后，请求会转发给后端服务器protocol_port字段指定端口。取值：false 不开启，true 开启。  **取值范围**：不涉及
        :type any_port_enable: bool
        :param connection_drain: 
        :type connection_drain: :class:`huaweicloudsdkelb.v3.ConnectionDrain`
        :param quic_cid_hash_strategy: 
        :type quic_cid_hash_strategy: :class:`huaweicloudsdkelb.v3.QuicCidHashStrategy`
        """
        
        

        self._description = None
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
        self._created_at = None
        self._updated_at = None
        self._vpc_id = None
        self._type = None
        self._enterprise_project_id = None
        self._healthmonitor = None
        self._any_port_enable = None
        self._connection_drain = None
        self._quic_cid_hash_strategy = None
        self.discriminator = None

        self.description = description
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
        self.created_at = created_at
        self.updated_at = updated_at
        self.vpc_id = vpc_id
        self.type = type
        self.enterprise_project_id = enterprise_project_id
        self.healthmonitor = healthmonitor
        if any_port_enable is not None:
            self.any_port_enable = any_port_enable
        if connection_drain is not None:
            self.connection_drain = connection_drain
        if quic_cid_hash_strategy is not None:
            self.quic_cid_hash_strategy = quic_cid_hash_strategy

    @property
    def description(self):
        r"""Gets the description of this MasterSlavePool.

        **参数解释**：后端服务器组的描述信息。  **取值范围**：不涉及

        :return: The description of this MasterSlavePool.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this MasterSlavePool.

        **参数解释**：后端服务器组的描述信息。  **取值范围**：不涉及

        :param description: The description of this MasterSlavePool.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        r"""Gets the id of this MasterSlavePool.

        **参数解释**：后端服务器组的ID。  **取值范围**：不涉及

        :return: The id of this MasterSlavePool.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MasterSlavePool.

        **参数解释**：后端服务器组的ID。  **取值范围**：不涉及

        :param id: The id of this MasterSlavePool.
        :type id: str
        """
        self._id = id

    @property
    def lb_algorithm(self):
        r"""Gets the lb_algorithm of this MasterSlavePool.

        **参数解释**：后端服务器组的负载均衡算法。  **取值范围**：不涉及 - ROUND_ROBIN：加权轮询算法。 - LEAST_CONNECTIONS：加权最少连接算法。 - SOURCE_IP：源IP算法。 - QUIC_CID：连接ID算法。  [不支持QUIC_CID。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC_CID。](tag:dt)

        :return: The lb_algorithm of this MasterSlavePool.
        :rtype: str
        """
        return self._lb_algorithm

    @lb_algorithm.setter
    def lb_algorithm(self, lb_algorithm):
        r"""Sets the lb_algorithm of this MasterSlavePool.

        **参数解释**：后端服务器组的负载均衡算法。  **取值范围**：不涉及 - ROUND_ROBIN：加权轮询算法。 - LEAST_CONNECTIONS：加权最少连接算法。 - SOURCE_IP：源IP算法。 - QUIC_CID：连接ID算法。  [不支持QUIC_CID。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC_CID。](tag:dt)

        :param lb_algorithm: The lb_algorithm of this MasterSlavePool.
        :type lb_algorithm: str
        """
        self._lb_algorithm = lb_algorithm

    @property
    def listeners(self):
        r"""Gets the listeners of this MasterSlavePool.

        **参数解释**：后端服务器组关联的监听器ID列表。

        :return: The listeners of this MasterSlavePool.
        :rtype: list[:class:`huaweicloudsdkelb.v3.ListenerRef`]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        r"""Sets the listeners of this MasterSlavePool.

        **参数解释**：后端服务器组关联的监听器ID列表。

        :param listeners: The listeners of this MasterSlavePool.
        :type listeners: list[:class:`huaweicloudsdkelb.v3.ListenerRef`]
        """
        self._listeners = listeners

    @property
    def loadbalancers(self):
        r"""Gets the loadbalancers of this MasterSlavePool.

        **参数解释**：后端服务器组关联的负载均衡器ID列表。

        :return: The loadbalancers of this MasterSlavePool.
        :rtype: list[:class:`huaweicloudsdkelb.v3.LoadBalancerRef`]
        """
        return self._loadbalancers

    @loadbalancers.setter
    def loadbalancers(self, loadbalancers):
        r"""Sets the loadbalancers of this MasterSlavePool.

        **参数解释**：后端服务器组关联的负载均衡器ID列表。

        :param loadbalancers: The loadbalancers of this MasterSlavePool.
        :type loadbalancers: list[:class:`huaweicloudsdkelb.v3.LoadBalancerRef`]
        """
        self._loadbalancers = loadbalancers

    @property
    def members(self):
        r"""Gets the members of this MasterSlavePool.

        **参数解释**：后端服务器组中的后端服务器列表。

        :return: The members of this MasterSlavePool.
        :rtype: list[:class:`huaweicloudsdkelb.v3.MasterSlaveMember`]
        """
        return self._members

    @members.setter
    def members(self, members):
        r"""Sets the members of this MasterSlavePool.

        **参数解释**：后端服务器组中的后端服务器列表。

        :param members: The members of this MasterSlavePool.
        :type members: list[:class:`huaweicloudsdkelb.v3.MasterSlaveMember`]
        """
        self._members = members

    @property
    def name(self):
        r"""Gets the name of this MasterSlavePool.

        **参数解释**：后端服务器组的名称。  **取值范围**：不涉及

        :return: The name of this MasterSlavePool.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this MasterSlavePool.

        **参数解释**：后端服务器组的名称。  **取值范围**：不涉及

        :param name: The name of this MasterSlavePool.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this MasterSlavePool.

        **参数解释**：后端服务器组所在的项目ID。  **取值范围**：不涉及

        :return: The project_id of this MasterSlavePool.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this MasterSlavePool.

        **参数解释**：后端服务器组所在的项目ID。  **取值范围**：不涉及

        :param project_id: The project_id of this MasterSlavePool.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def protocol(self):
        r"""Gets the protocol of this MasterSlavePool.

        **参数解释**：后端服务器组的后端协议。  **取值范围**：不涉及TCP、UDP、QUIC、TLS。  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC。](tag:dt)

        :return: The protocol of this MasterSlavePool.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this MasterSlavePool.

        **参数解释**：后端服务器组的后端协议。  **取值范围**：不涉及TCP、UDP、QUIC、TLS。  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC。](tag:dt)

        :param protocol: The protocol of this MasterSlavePool.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def session_persistence(self):
        r"""Gets the session_persistence of this MasterSlavePool.

        :return: The session_persistence of this MasterSlavePool.
        :rtype: :class:`huaweicloudsdkelb.v3.SessionPersistence`
        """
        return self._session_persistence

    @session_persistence.setter
    def session_persistence(self, session_persistence):
        r"""Sets the session_persistence of this MasterSlavePool.

        :param session_persistence: The session_persistence of this MasterSlavePool.
        :type session_persistence: :class:`huaweicloudsdkelb.v3.SessionPersistence`
        """
        self._session_persistence = session_persistence

    @property
    def ip_version(self):
        r"""Gets the ip_version of this MasterSlavePool.

        **参数解释**：后端服务器组支持的IP版本。  [**取值范围**： - 共享型：固定为v4； - 独享型：取值dualstack、v4。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。当协议为HTTP时，ip_version为v4。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs)  [**取值范围**：dualstack、v4。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。当协议为HTTP时，ip_version为v4。](tag:hcso_dt)  [不支持IPv6，只会返回v4。](tag:dt)

        :return: The ip_version of this MasterSlavePool.
        :rtype: str
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this MasterSlavePool.

        **参数解释**：后端服务器组支持的IP版本。  [**取值范围**： - 共享型：固定为v4； - 独享型：取值dualstack、v4。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。当协议为HTTP时，ip_version为v4。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs)  [**取值范围**：dualstack、v4。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。当协议为HTTP时，ip_version为v4。](tag:hcso_dt)  [不支持IPv6，只会返回v4。](tag:dt)

        :param ip_version: The ip_version of this MasterSlavePool.
        :type ip_version: str
        """
        self._ip_version = ip_version

    @property
    def created_at(self):
        r"""Gets the created_at of this MasterSlavePool.

        **参数解释**：创建时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  **取值范围**：不涉及  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)

        :return: The created_at of this MasterSlavePool.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this MasterSlavePool.

        **参数解释**：创建时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  **取值范围**：不涉及  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)

        :param created_at: The created_at of this MasterSlavePool.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this MasterSlavePool.

        **参数解释**：更新时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  **取值范围**：不涉及  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)

        :return: The updated_at of this MasterSlavePool.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this MasterSlavePool.

        **参数解释**：更新时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  **取值范围**：不涉及  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)

        :param updated_at: The updated_at of this MasterSlavePool.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this MasterSlavePool.

        **参数解释**：后端服务器组关联的虚拟私有云的ID。  **取值范围**：不涉及

        :return: The vpc_id of this MasterSlavePool.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this MasterSlavePool.

        **参数解释**：后端服务器组关联的虚拟私有云的ID。  **取值范围**：不涉及

        :param vpc_id: The vpc_id of this MasterSlavePool.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def type(self):
        r"""Gets the type of this MasterSlavePool.

        **参数解释**：后端服务器组的类型。  **取值范围**：不涉及 - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加IP类型后端，type指定为该类型时，vpc_id不允许指定。 - 空字符串（\"\"）：允许任意类型的后端

        :return: The type of this MasterSlavePool.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this MasterSlavePool.

        **参数解释**：后端服务器组的类型。  **取值范围**：不涉及 - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加IP类型后端，type指定为该类型时，vpc_id不允许指定。 - 空字符串（\"\"）：允许任意类型的后端

        :param type: The type of this MasterSlavePool.
        :type type: str
        """
        self._type = type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this MasterSlavePool.

        **参数解释**：资源所属的企业项目ID。  **取值范围**： - \"0\"：表示资源属于default企业项目。 - UUID格式的字符串，表示非默认企业项目。  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :return: The enterprise_project_id of this MasterSlavePool.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this MasterSlavePool.

        **参数解释**：资源所属的企业项目ID。  **取值范围**： - \"0\"：表示资源属于default企业项目。 - UUID格式的字符串，表示非默认企业项目。  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :param enterprise_project_id: The enterprise_project_id of this MasterSlavePool.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def healthmonitor(self):
        r"""Gets the healthmonitor of this MasterSlavePool.

        :return: The healthmonitor of this MasterSlavePool.
        :rtype: :class:`huaweicloudsdkelb.v3.MasterSlaveHealthMonitor`
        """
        return self._healthmonitor

    @healthmonitor.setter
    def healthmonitor(self, healthmonitor):
        r"""Sets the healthmonitor of this MasterSlavePool.

        :param healthmonitor: The healthmonitor of this MasterSlavePool.
        :type healthmonitor: :class:`huaweicloudsdkelb.v3.MasterSlaveHealthMonitor`
        """
        self._healthmonitor = healthmonitor

    @property
    def any_port_enable(self):
        r"""Gets the any_port_enable of this MasterSlavePool.

        **参数解释**：后端是否开启全端口转发。开启后，后端服务器端口与前端监听器端口保持一致。关闭后，请求会转发给后端服务器protocol_port字段指定端口。取值：false 不开启，true 开启。  **取值范围**：不涉及

        :return: The any_port_enable of this MasterSlavePool.
        :rtype: bool
        """
        return self._any_port_enable

    @any_port_enable.setter
    def any_port_enable(self, any_port_enable):
        r"""Sets the any_port_enable of this MasterSlavePool.

        **参数解释**：后端是否开启全端口转发。开启后，后端服务器端口与前端监听器端口保持一致。关闭后，请求会转发给后端服务器protocol_port字段指定端口。取值：false 不开启，true 开启。  **取值范围**：不涉及

        :param any_port_enable: The any_port_enable of this MasterSlavePool.
        :type any_port_enable: bool
        """
        self._any_port_enable = any_port_enable

    @property
    def connection_drain(self):
        r"""Gets the connection_drain of this MasterSlavePool.

        :return: The connection_drain of this MasterSlavePool.
        :rtype: :class:`huaweicloudsdkelb.v3.ConnectionDrain`
        """
        return self._connection_drain

    @connection_drain.setter
    def connection_drain(self, connection_drain):
        r"""Sets the connection_drain of this MasterSlavePool.

        :param connection_drain: The connection_drain of this MasterSlavePool.
        :type connection_drain: :class:`huaweicloudsdkelb.v3.ConnectionDrain`
        """
        self._connection_drain = connection_drain

    @property
    def quic_cid_hash_strategy(self):
        r"""Gets the quic_cid_hash_strategy of this MasterSlavePool.

        :return: The quic_cid_hash_strategy of this MasterSlavePool.
        :rtype: :class:`huaweicloudsdkelb.v3.QuicCidHashStrategy`
        """
        return self._quic_cid_hash_strategy

    @quic_cid_hash_strategy.setter
    def quic_cid_hash_strategy(self, quic_cid_hash_strategy):
        r"""Sets the quic_cid_hash_strategy of this MasterSlavePool.

        :param quic_cid_hash_strategy: The quic_cid_hash_strategy of this MasterSlavePool.
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
        if not isinstance(other, MasterSlavePool):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
