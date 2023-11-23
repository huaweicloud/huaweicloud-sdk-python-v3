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
        'any_port_enable': 'bool'
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
        'any_port_enable': 'any_port_enable'
    }

    def __init__(self, description=None, id=None, lb_algorithm=None, listeners=None, loadbalancers=None, members=None, name=None, project_id=None, protocol=None, session_persistence=None, ip_version=None, created_at=None, updated_at=None, vpc_id=None, type=None, enterprise_project_id=None, healthmonitor=None, any_port_enable=None):
        """MasterSlavePool

        The model defined in huaweicloud sdk

        :param description: 后端云服务器组的描述信息。
        :type description: str
        :param id: 后端云服务器组的ID。
        :type id: str
        :param lb_algorithm: 后端云服务器组的负载均衡算法。  取值： - ROUND_ROBIN：加权轮询算法。 - LEAST_CONNECTIONS：加权最少连接算法。 - SOURCE_IP：源IP算法。 - QUIC_CID：连接ID算法。  使用说明： - 当该字段的取值为SOURCE_IP时，后端云服务器组绑定的后端云服务器的weight字段无效。 - 只有pool的protocol为QUIC时，才支持QUIC_CID算法。  [不支持QUIC_CID。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC_CID。](tag:dt,dt_test)
        :type lb_algorithm: str
        :param listeners: 后端云服务器组关联的监听器ID列表。
        :type listeners: list[:class:`huaweicloudsdkelb.v3.ListenerRef`]
        :param loadbalancers: 后端云服务器组关联的负载均衡器ID列表。
        :type loadbalancers: list[:class:`huaweicloudsdkelb.v3.LoadBalancerRef`]
        :param members: 后端云服务器组中的后端云服务器列表。
        :type members: list[:class:`huaweicloudsdkelb.v3.MasterSlaveMember`]
        :param name: 后端云服务器组的名称。
        :type name: str
        :param project_id: 后端云服务器组所在的项目ID。
        :type project_id: str
        :param protocol: 后端云服务器组的后端协议。  取值：TCP、UDP、HTTP、HTTPS和QUIC。  使用说明： - listener的protocol为UDP时，pool的protocol必须为UDP或QUIC； - listener的protocol为TCP时pool的protocol必须为TCP； - listener的protocol为HTTP时，pool的protocol必须为HTTP。 - listener的protocol为HTTPS时，pool的protocol必须为HTTP或HTTPS。 - listener的protocol为TERMINATED_HTTPS时，pool的protocol必须为HTTP。  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC。](tag:dt,dt_test)
        :type protocol: str
        :param session_persistence: 
        :type session_persistence: :class:`huaweicloudsdkelb.v3.SessionPersistence`
        :param ip_version: 后端云服务器组支持的IP版本。  [取值： - 共享型：固定为v4； -  独享型：取值dualstack、v4、v6。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。  当协议为HTTP时，ip_version为v4。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,fcs)  [取值：dualstack、v4、v6。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。 当协议为HTTP时，ip_version为v4。](tag:hcso_dt)  [不支持IPv6，只会返回v4。](tag:dt,dt_test)
        :type ip_version: str
        :param created_at: 创建时间。格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt,hk_tm)
        :type created_at: str
        :param updated_at: 更新时间。格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt,hk_tm)
        :type updated_at: str
        :param vpc_id: 后端云服务器组关联的虚拟私有云的ID。
        :type vpc_id: str
        :param type: 后端服务器组的类型。  取值： - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加跨VPC后端，type指定为该类型时，vpc_id不允许指定。 - 空字符串（\&quot;\&quot;）：允许任意类型的后端
        :type type: str
        :param enterprise_project_id: 后端服务器组的企业项目ID。无论创建什么企业项目，都在默认企业项目下。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)
        :type enterprise_project_id: str
        :param healthmonitor: 
        :type healthmonitor: :class:`huaweicloudsdkelb.v3.MasterSlaveHealthMonitor`
        :param any_port_enable: 后端是否开启端口透传，开启后，后端服务器端口与前端监听器端口保持一致。取值：false不开启，true开启，默认false。 &gt; 关闭端口透传后，请求会转发给后端服务器protocol_port字段指定端口。
        :type any_port_enable: bool
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

    @property
    def description(self):
        """Gets the description of this MasterSlavePool.

        后端云服务器组的描述信息。

        :return: The description of this MasterSlavePool.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MasterSlavePool.

        后端云服务器组的描述信息。

        :param description: The description of this MasterSlavePool.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this MasterSlavePool.

        后端云服务器组的ID。

        :return: The id of this MasterSlavePool.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MasterSlavePool.

        后端云服务器组的ID。

        :param id: The id of this MasterSlavePool.
        :type id: str
        """
        self._id = id

    @property
    def lb_algorithm(self):
        """Gets the lb_algorithm of this MasterSlavePool.

        后端云服务器组的负载均衡算法。  取值： - ROUND_ROBIN：加权轮询算法。 - LEAST_CONNECTIONS：加权最少连接算法。 - SOURCE_IP：源IP算法。 - QUIC_CID：连接ID算法。  使用说明： - 当该字段的取值为SOURCE_IP时，后端云服务器组绑定的后端云服务器的weight字段无效。 - 只有pool的protocol为QUIC时，才支持QUIC_CID算法。  [不支持QUIC_CID。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC_CID。](tag:dt,dt_test)

        :return: The lb_algorithm of this MasterSlavePool.
        :rtype: str
        """
        return self._lb_algorithm

    @lb_algorithm.setter
    def lb_algorithm(self, lb_algorithm):
        """Sets the lb_algorithm of this MasterSlavePool.

        后端云服务器组的负载均衡算法。  取值： - ROUND_ROBIN：加权轮询算法。 - LEAST_CONNECTIONS：加权最少连接算法。 - SOURCE_IP：源IP算法。 - QUIC_CID：连接ID算法。  使用说明： - 当该字段的取值为SOURCE_IP时，后端云服务器组绑定的后端云服务器的weight字段无效。 - 只有pool的protocol为QUIC时，才支持QUIC_CID算法。  [不支持QUIC_CID。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC_CID。](tag:dt,dt_test)

        :param lb_algorithm: The lb_algorithm of this MasterSlavePool.
        :type lb_algorithm: str
        """
        self._lb_algorithm = lb_algorithm

    @property
    def listeners(self):
        """Gets the listeners of this MasterSlavePool.

        后端云服务器组关联的监听器ID列表。

        :return: The listeners of this MasterSlavePool.
        :rtype: list[:class:`huaweicloudsdkelb.v3.ListenerRef`]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        """Sets the listeners of this MasterSlavePool.

        后端云服务器组关联的监听器ID列表。

        :param listeners: The listeners of this MasterSlavePool.
        :type listeners: list[:class:`huaweicloudsdkelb.v3.ListenerRef`]
        """
        self._listeners = listeners

    @property
    def loadbalancers(self):
        """Gets the loadbalancers of this MasterSlavePool.

        后端云服务器组关联的负载均衡器ID列表。

        :return: The loadbalancers of this MasterSlavePool.
        :rtype: list[:class:`huaweicloudsdkelb.v3.LoadBalancerRef`]
        """
        return self._loadbalancers

    @loadbalancers.setter
    def loadbalancers(self, loadbalancers):
        """Sets the loadbalancers of this MasterSlavePool.

        后端云服务器组关联的负载均衡器ID列表。

        :param loadbalancers: The loadbalancers of this MasterSlavePool.
        :type loadbalancers: list[:class:`huaweicloudsdkelb.v3.LoadBalancerRef`]
        """
        self._loadbalancers = loadbalancers

    @property
    def members(self):
        """Gets the members of this MasterSlavePool.

        后端云服务器组中的后端云服务器列表。

        :return: The members of this MasterSlavePool.
        :rtype: list[:class:`huaweicloudsdkelb.v3.MasterSlaveMember`]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this MasterSlavePool.

        后端云服务器组中的后端云服务器列表。

        :param members: The members of this MasterSlavePool.
        :type members: list[:class:`huaweicloudsdkelb.v3.MasterSlaveMember`]
        """
        self._members = members

    @property
    def name(self):
        """Gets the name of this MasterSlavePool.

        后端云服务器组的名称。

        :return: The name of this MasterSlavePool.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MasterSlavePool.

        后端云服务器组的名称。

        :param name: The name of this MasterSlavePool.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this MasterSlavePool.

        后端云服务器组所在的项目ID。

        :return: The project_id of this MasterSlavePool.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this MasterSlavePool.

        后端云服务器组所在的项目ID。

        :param project_id: The project_id of this MasterSlavePool.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def protocol(self):
        """Gets the protocol of this MasterSlavePool.

        后端云服务器组的后端协议。  取值：TCP、UDP、HTTP、HTTPS和QUIC。  使用说明： - listener的protocol为UDP时，pool的protocol必须为UDP或QUIC； - listener的protocol为TCP时pool的protocol必须为TCP； - listener的protocol为HTTP时，pool的protocol必须为HTTP。 - listener的protocol为HTTPS时，pool的protocol必须为HTTP或HTTPS。 - listener的protocol为TERMINATED_HTTPS时，pool的protocol必须为HTTP。  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC。](tag:dt,dt_test)

        :return: The protocol of this MasterSlavePool.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this MasterSlavePool.

        后端云服务器组的后端协议。  取值：TCP、UDP、HTTP、HTTPS和QUIC。  使用说明： - listener的protocol为UDP时，pool的protocol必须为UDP或QUIC； - listener的protocol为TCP时pool的protocol必须为TCP； - listener的protocol为HTTP时，pool的protocol必须为HTTP。 - listener的protocol为HTTPS时，pool的protocol必须为HTTP或HTTPS。 - listener的protocol为TERMINATED_HTTPS时，pool的protocol必须为HTTP。  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC。](tag:dt,dt_test)

        :param protocol: The protocol of this MasterSlavePool.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def session_persistence(self):
        """Gets the session_persistence of this MasterSlavePool.

        :return: The session_persistence of this MasterSlavePool.
        :rtype: :class:`huaweicloudsdkelb.v3.SessionPersistence`
        """
        return self._session_persistence

    @session_persistence.setter
    def session_persistence(self, session_persistence):
        """Sets the session_persistence of this MasterSlavePool.

        :param session_persistence: The session_persistence of this MasterSlavePool.
        :type session_persistence: :class:`huaweicloudsdkelb.v3.SessionPersistence`
        """
        self._session_persistence = session_persistence

    @property
    def ip_version(self):
        """Gets the ip_version of this MasterSlavePool.

        后端云服务器组支持的IP版本。  [取值： - 共享型：固定为v4； -  独享型：取值dualstack、v4、v6。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。  当协议为HTTP时，ip_version为v4。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,fcs)  [取值：dualstack、v4、v6。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。 当协议为HTTP时，ip_version为v4。](tag:hcso_dt)  [不支持IPv6，只会返回v4。](tag:dt,dt_test)

        :return: The ip_version of this MasterSlavePool.
        :rtype: str
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this MasterSlavePool.

        后端云服务器组支持的IP版本。  [取值： - 共享型：固定为v4； -  独享型：取值dualstack、v4、v6。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。  当协议为HTTP时，ip_version为v4。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,fcs)  [取值：dualstack、v4、v6。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。 当协议为HTTP时，ip_version为v4。](tag:hcso_dt)  [不支持IPv6，只会返回v4。](tag:dt,dt_test)

        :param ip_version: The ip_version of this MasterSlavePool.
        :type ip_version: str
        """
        self._ip_version = ip_version

    @property
    def created_at(self):
        """Gets the created_at of this MasterSlavePool.

        创建时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt,hk_tm)

        :return: The created_at of this MasterSlavePool.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this MasterSlavePool.

        创建时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt,hk_tm)

        :param created_at: The created_at of this MasterSlavePool.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this MasterSlavePool.

        更新时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt,hk_tm)

        :return: The updated_at of this MasterSlavePool.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this MasterSlavePool.

        更新时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt,hk_tm)

        :param updated_at: The updated_at of this MasterSlavePool.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def vpc_id(self):
        """Gets the vpc_id of this MasterSlavePool.

        后端云服务器组关联的虚拟私有云的ID。

        :return: The vpc_id of this MasterSlavePool.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this MasterSlavePool.

        后端云服务器组关联的虚拟私有云的ID。

        :param vpc_id: The vpc_id of this MasterSlavePool.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def type(self):
        """Gets the type of this MasterSlavePool.

        后端服务器组的类型。  取值： - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加跨VPC后端，type指定为该类型时，vpc_id不允许指定。 - 空字符串（\"\"）：允许任意类型的后端

        :return: The type of this MasterSlavePool.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MasterSlavePool.

        后端服务器组的类型。  取值： - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加跨VPC后端，type指定为该类型时，vpc_id不允许指定。 - 空字符串（\"\"）：允许任意类型的后端

        :param type: The type of this MasterSlavePool.
        :type type: str
        """
        self._type = type

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this MasterSlavePool.

        后端服务器组的企业项目ID。无论创建什么企业项目，都在默认企业项目下。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)

        :return: The enterprise_project_id of this MasterSlavePool.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this MasterSlavePool.

        后端服务器组的企业项目ID。无论创建什么企业项目，都在默认企业项目下。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)

        :param enterprise_project_id: The enterprise_project_id of this MasterSlavePool.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def healthmonitor(self):
        """Gets the healthmonitor of this MasterSlavePool.

        :return: The healthmonitor of this MasterSlavePool.
        :rtype: :class:`huaweicloudsdkelb.v3.MasterSlaveHealthMonitor`
        """
        return self._healthmonitor

    @healthmonitor.setter
    def healthmonitor(self, healthmonitor):
        """Sets the healthmonitor of this MasterSlavePool.

        :param healthmonitor: The healthmonitor of this MasterSlavePool.
        :type healthmonitor: :class:`huaweicloudsdkelb.v3.MasterSlaveHealthMonitor`
        """
        self._healthmonitor = healthmonitor

    @property
    def any_port_enable(self):
        """Gets the any_port_enable of this MasterSlavePool.

        后端是否开启端口透传，开启后，后端服务器端口与前端监听器端口保持一致。取值：false不开启，true开启，默认false。 > 关闭端口透传后，请求会转发给后端服务器protocol_port字段指定端口。

        :return: The any_port_enable of this MasterSlavePool.
        :rtype: bool
        """
        return self._any_port_enable

    @any_port_enable.setter
    def any_port_enable(self, any_port_enable):
        """Sets the any_port_enable of this MasterSlavePool.

        后端是否开启端口透传，开启后，后端服务器端口与前端监听器端口保持一致。取值：false不开启，true开启，默认false。 > 关闭端口透传后，请求会转发给后端服务器protocol_port字段指定端口。

        :param any_port_enable: The any_port_enable of this MasterSlavePool.
        :type any_port_enable: bool
        """
        self._any_port_enable = any_port_enable

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
