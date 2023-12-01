# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMasterSlavePoolOption:

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
        'lb_algorithm': 'str',
        'loadbalancer_id': 'str',
        'listener_id': 'str',
        'name': 'str',
        'project_id': 'str',
        'protocol': 'str',
        'session_persistence': 'CreatePoolSessionPersistenceOption',
        'vpc_id': 'str',
        'type': 'str',
        'ip_version': 'str',
        'members': 'list[CreateMasterSlaveMemberOption]',
        'healthmonitor': 'CreateMasterSlaveHealthMonitorOption',
        'any_port_enable': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'lb_algorithm': 'lb_algorithm',
        'loadbalancer_id': 'loadbalancer_id',
        'listener_id': 'listener_id',
        'name': 'name',
        'project_id': 'project_id',
        'protocol': 'protocol',
        'session_persistence': 'session_persistence',
        'vpc_id': 'vpc_id',
        'type': 'type',
        'ip_version': 'ip_version',
        'members': 'members',
        'healthmonitor': 'healthmonitor',
        'any_port_enable': 'any_port_enable'
    }

    def __init__(self, description=None, lb_algorithm=None, loadbalancer_id=None, listener_id=None, name=None, project_id=None, protocol=None, session_persistence=None, vpc_id=None, type=None, ip_version=None, members=None, healthmonitor=None, any_port_enable=None):
        """CreateMasterSlavePoolOption

        The model defined in huaweicloud sdk

        :param description: 后端云服务器组的描述信息。
        :type description: str
        :param lb_algorithm: 后端云服务器组的负载均衡算法。  取值： - ROUND_ROBIN：加权轮询算法。 - LEAST_CONNECTIONS：加权最少连接算法。 - SOURCE_IP：源IP算法。 - QUIC_CID：连接ID算法。  [不支持QUIC_CID。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC_CID。](tag:dt,dt_test)
        :type lb_algorithm: str
        :param loadbalancer_id: 后端云服务器组关联的LB的ID。  使用说明：listener_id，loadbalancer_id，type至少指定一个。
        :type loadbalancer_id: str
        :param listener_id: 后端云服务器组关联的监听器的ID。  使用说明：listener_id，loadbalancer_id，type至少指定一个。
        :type listener_id: str
        :param name: 后端云服务器组的名称。
        :type name: str
        :param project_id: 后端云服务器组所属的项目ID。
        :type project_id: str
        :param protocol: 后端云服务器组的后端协议。  取值：TCP、UDP、QUIC。  使用说明： - listener的protocol为UDP时，pool的protocol必须为UDP或QUIC。 - listener的protocol为TCP时pool的protocol必须为TCP。  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC。](tag:dt,dt_test)
        :type protocol: str
        :param session_persistence: 
        :type session_persistence: :class:`huaweicloudsdkelb.v3.CreatePoolSessionPersistenceOption`
        :param vpc_id: 后端云服务器组关联的虚拟私有云的ID。  指定了vpc_id的约束： - 只能挂载到该虚拟私有云下。 - 只能添加该虚拟私有云下的后端服务器或跨VPC的后端服务器。 - type必须指定为instance。  没有指定vpc_id的约束： - 后续添加后端服务器时，vpc_id由后端服务器所在的虚拟私有云确定。
        :type vpc_id: str
        :param type: 后端服务器组的类型。  取值： - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加跨VPC后端，type指定为该类型时，vpc_id不允许指定。
        :type type: str
        :param ip_version: 后端云服务器组支持的IP版本。  [取值： - 共享型：固定为v4； -  独享型：取值dualstack、v4、v6。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。  当协议为HTTP时，ip_version为v4。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,fcs)  [取值：dualstack、v4、v6。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。 当协议为HTTP时，ip_version为v4。](tag:hcso_dt)  [不支持IPv6，只会返回v4。](tag:dt,dt_test)
        :type ip_version: str
        :param members: 主备主机组的后端服务器。 只能添加2个后端云服务器，必须有一个为主，一个为备。
        :type members: list[:class:`huaweicloudsdkelb.v3.CreateMasterSlaveMemberOption`]
        :param healthmonitor: 
        :type healthmonitor: :class:`huaweicloudsdkelb.v3.CreateMasterSlaveHealthMonitorOption`
        :param any_port_enable: 后端是否开启端口透传，开启后，后端服务器端口与前端监听器端口保持一致。取值：false不开启，true开启，默认false。 &gt; 关闭端口透传后，请求会转发给后端服务器protocol_port字段指定端口。
        :type any_port_enable: bool
        """
        
        

        self._description = None
        self._lb_algorithm = None
        self._loadbalancer_id = None
        self._listener_id = None
        self._name = None
        self._project_id = None
        self._protocol = None
        self._session_persistence = None
        self._vpc_id = None
        self._type = None
        self._ip_version = None
        self._members = None
        self._healthmonitor = None
        self._any_port_enable = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.lb_algorithm = lb_algorithm
        if loadbalancer_id is not None:
            self.loadbalancer_id = loadbalancer_id
        if listener_id is not None:
            self.listener_id = listener_id
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        self.protocol = protocol
        if session_persistence is not None:
            self.session_persistence = session_persistence
        if vpc_id is not None:
            self.vpc_id = vpc_id
        self.type = type
        if ip_version is not None:
            self.ip_version = ip_version
        self.members = members
        self.healthmonitor = healthmonitor
        if any_port_enable is not None:
            self.any_port_enable = any_port_enable

    @property
    def description(self):
        """Gets the description of this CreateMasterSlavePoolOption.

        后端云服务器组的描述信息。

        :return: The description of this CreateMasterSlavePoolOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateMasterSlavePoolOption.

        后端云服务器组的描述信息。

        :param description: The description of this CreateMasterSlavePoolOption.
        :type description: str
        """
        self._description = description

    @property
    def lb_algorithm(self):
        """Gets the lb_algorithm of this CreateMasterSlavePoolOption.

        后端云服务器组的负载均衡算法。  取值： - ROUND_ROBIN：加权轮询算法。 - LEAST_CONNECTIONS：加权最少连接算法。 - SOURCE_IP：源IP算法。 - QUIC_CID：连接ID算法。  [不支持QUIC_CID。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC_CID。](tag:dt,dt_test)

        :return: The lb_algorithm of this CreateMasterSlavePoolOption.
        :rtype: str
        """
        return self._lb_algorithm

    @lb_algorithm.setter
    def lb_algorithm(self, lb_algorithm):
        """Sets the lb_algorithm of this CreateMasterSlavePoolOption.

        后端云服务器组的负载均衡算法。  取值： - ROUND_ROBIN：加权轮询算法。 - LEAST_CONNECTIONS：加权最少连接算法。 - SOURCE_IP：源IP算法。 - QUIC_CID：连接ID算法。  [不支持QUIC_CID。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC_CID。](tag:dt,dt_test)

        :param lb_algorithm: The lb_algorithm of this CreateMasterSlavePoolOption.
        :type lb_algorithm: str
        """
        self._lb_algorithm = lb_algorithm

    @property
    def loadbalancer_id(self):
        """Gets the loadbalancer_id of this CreateMasterSlavePoolOption.

        后端云服务器组关联的LB的ID。  使用说明：listener_id，loadbalancer_id，type至少指定一个。

        :return: The loadbalancer_id of this CreateMasterSlavePoolOption.
        :rtype: str
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        """Sets the loadbalancer_id of this CreateMasterSlavePoolOption.

        后端云服务器组关联的LB的ID。  使用说明：listener_id，loadbalancer_id，type至少指定一个。

        :param loadbalancer_id: The loadbalancer_id of this CreateMasterSlavePoolOption.
        :type loadbalancer_id: str
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def listener_id(self):
        """Gets the listener_id of this CreateMasterSlavePoolOption.

        后端云服务器组关联的监听器的ID。  使用说明：listener_id，loadbalancer_id，type至少指定一个。

        :return: The listener_id of this CreateMasterSlavePoolOption.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this CreateMasterSlavePoolOption.

        后端云服务器组关联的监听器的ID。  使用说明：listener_id，loadbalancer_id，type至少指定一个。

        :param listener_id: The listener_id of this CreateMasterSlavePoolOption.
        :type listener_id: str
        """
        self._listener_id = listener_id

    @property
    def name(self):
        """Gets the name of this CreateMasterSlavePoolOption.

        后端云服务器组的名称。

        :return: The name of this CreateMasterSlavePoolOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateMasterSlavePoolOption.

        后端云服务器组的名称。

        :param name: The name of this CreateMasterSlavePoolOption.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this CreateMasterSlavePoolOption.

        后端云服务器组所属的项目ID。

        :return: The project_id of this CreateMasterSlavePoolOption.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateMasterSlavePoolOption.

        后端云服务器组所属的项目ID。

        :param project_id: The project_id of this CreateMasterSlavePoolOption.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def protocol(self):
        """Gets the protocol of this CreateMasterSlavePoolOption.

        后端云服务器组的后端协议。  取值：TCP、UDP、QUIC。  使用说明： - listener的protocol为UDP时，pool的protocol必须为UDP或QUIC。 - listener的protocol为TCP时pool的protocol必须为TCP。  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC。](tag:dt,dt_test)

        :return: The protocol of this CreateMasterSlavePoolOption.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this CreateMasterSlavePoolOption.

        后端云服务器组的后端协议。  取值：TCP、UDP、QUIC。  使用说明： - listener的protocol为UDP时，pool的protocol必须为UDP或QUIC。 - listener的protocol为TCP时pool的protocol必须为TCP。  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC。](tag:dt,dt_test)

        :param protocol: The protocol of this CreateMasterSlavePoolOption.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def session_persistence(self):
        """Gets the session_persistence of this CreateMasterSlavePoolOption.

        :return: The session_persistence of this CreateMasterSlavePoolOption.
        :rtype: :class:`huaweicloudsdkelb.v3.CreatePoolSessionPersistenceOption`
        """
        return self._session_persistence

    @session_persistence.setter
    def session_persistence(self, session_persistence):
        """Sets the session_persistence of this CreateMasterSlavePoolOption.

        :param session_persistence: The session_persistence of this CreateMasterSlavePoolOption.
        :type session_persistence: :class:`huaweicloudsdkelb.v3.CreatePoolSessionPersistenceOption`
        """
        self._session_persistence = session_persistence

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateMasterSlavePoolOption.

        后端云服务器组关联的虚拟私有云的ID。  指定了vpc_id的约束： - 只能挂载到该虚拟私有云下。 - 只能添加该虚拟私有云下的后端服务器或跨VPC的后端服务器。 - type必须指定为instance。  没有指定vpc_id的约束： - 后续添加后端服务器时，vpc_id由后端服务器所在的虚拟私有云确定。

        :return: The vpc_id of this CreateMasterSlavePoolOption.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateMasterSlavePoolOption.

        后端云服务器组关联的虚拟私有云的ID。  指定了vpc_id的约束： - 只能挂载到该虚拟私有云下。 - 只能添加该虚拟私有云下的后端服务器或跨VPC的后端服务器。 - type必须指定为instance。  没有指定vpc_id的约束： - 后续添加后端服务器时，vpc_id由后端服务器所在的虚拟私有云确定。

        :param vpc_id: The vpc_id of this CreateMasterSlavePoolOption.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def type(self):
        """Gets the type of this CreateMasterSlavePoolOption.

        后端服务器组的类型。  取值： - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加跨VPC后端，type指定为该类型时，vpc_id不允许指定。

        :return: The type of this CreateMasterSlavePoolOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateMasterSlavePoolOption.

        后端服务器组的类型。  取值： - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加跨VPC后端，type指定为该类型时，vpc_id不允许指定。

        :param type: The type of this CreateMasterSlavePoolOption.
        :type type: str
        """
        self._type = type

    @property
    def ip_version(self):
        """Gets the ip_version of this CreateMasterSlavePoolOption.

        后端云服务器组支持的IP版本。  [取值： - 共享型：固定为v4； -  独享型：取值dualstack、v4、v6。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。  当协议为HTTP时，ip_version为v4。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,fcs)  [取值：dualstack、v4、v6。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。 当协议为HTTP时，ip_version为v4。](tag:hcso_dt)  [不支持IPv6，只会返回v4。](tag:dt,dt_test)

        :return: The ip_version of this CreateMasterSlavePoolOption.
        :rtype: str
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this CreateMasterSlavePoolOption.

        后端云服务器组支持的IP版本。  [取值： - 共享型：固定为v4； -  独享型：取值dualstack、v4、v6。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。  当协议为HTTP时，ip_version为v4。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,fcs)  [取值：dualstack、v4、v6。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。 当协议为HTTP时，ip_version为v4。](tag:hcso_dt)  [不支持IPv6，只会返回v4。](tag:dt,dt_test)

        :param ip_version: The ip_version of this CreateMasterSlavePoolOption.
        :type ip_version: str
        """
        self._ip_version = ip_version

    @property
    def members(self):
        """Gets the members of this CreateMasterSlavePoolOption.

        主备主机组的后端服务器。 只能添加2个后端云服务器，必须有一个为主，一个为备。

        :return: The members of this CreateMasterSlavePoolOption.
        :rtype: list[:class:`huaweicloudsdkelb.v3.CreateMasterSlaveMemberOption`]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this CreateMasterSlavePoolOption.

        主备主机组的后端服务器。 只能添加2个后端云服务器，必须有一个为主，一个为备。

        :param members: The members of this CreateMasterSlavePoolOption.
        :type members: list[:class:`huaweicloudsdkelb.v3.CreateMasterSlaveMemberOption`]
        """
        self._members = members

    @property
    def healthmonitor(self):
        """Gets the healthmonitor of this CreateMasterSlavePoolOption.

        :return: The healthmonitor of this CreateMasterSlavePoolOption.
        :rtype: :class:`huaweicloudsdkelb.v3.CreateMasterSlaveHealthMonitorOption`
        """
        return self._healthmonitor

    @healthmonitor.setter
    def healthmonitor(self, healthmonitor):
        """Sets the healthmonitor of this CreateMasterSlavePoolOption.

        :param healthmonitor: The healthmonitor of this CreateMasterSlavePoolOption.
        :type healthmonitor: :class:`huaweicloudsdkelb.v3.CreateMasterSlaveHealthMonitorOption`
        """
        self._healthmonitor = healthmonitor

    @property
    def any_port_enable(self):
        """Gets the any_port_enable of this CreateMasterSlavePoolOption.

        后端是否开启端口透传，开启后，后端服务器端口与前端监听器端口保持一致。取值：false不开启，true开启，默认false。 > 关闭端口透传后，请求会转发给后端服务器protocol_port字段指定端口。

        :return: The any_port_enable of this CreateMasterSlavePoolOption.
        :rtype: bool
        """
        return self._any_port_enable

    @any_port_enable.setter
    def any_port_enable(self, any_port_enable):
        """Sets the any_port_enable of this CreateMasterSlavePoolOption.

        后端是否开启端口透传，开启后，后端服务器端口与前端监听器端口保持一致。取值：false不开启，true开启，默认false。 > 关闭端口透传后，请求会转发给后端服务器protocol_port字段指定端口。

        :param any_port_enable: The any_port_enable of this CreateMasterSlavePoolOption.
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
        if not isinstance(other, CreateMasterSlavePoolOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
