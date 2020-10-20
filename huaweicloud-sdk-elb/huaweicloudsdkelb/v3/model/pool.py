# coding: utf-8

import pprint
import re

import six





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
        'member_deletion_protection_enable': 'bool'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
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
        'member_deletion_protection_enable': 'member_deletion_protection_enable'
    }

    def __init__(self, admin_state_up=True, description=None, healthmonitor_id=None, id=None, lb_algorithm=None, listeners=None, loadbalancers=None, members=None, name=None, project_id=None, protocol=None, session_persistence=None, ip_version='dualstack', slow_start=None, member_deletion_protection_enable=False):
        """Pool - a model defined in huaweicloud sdk"""
        
        

        self._admin_state_up = None
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
        self.discriminator = None

        self.admin_state_up = admin_state_up
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
        if member_deletion_protection_enable is not None:
            self.member_deletion_protection_enable = member_deletion_protection_enable

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this Pool.

        后端云服务器组的管理状态；该字段为预留字段，暂未启用。只支持更新为true。

        :return: The admin_state_up of this Pool.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this Pool.

        后端云服务器组的管理状态；该字段为预留字段，暂未启用。只支持更新为true。

        :param admin_state_up: The admin_state_up of this Pool.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def description(self):
        """Gets the description of this Pool.

        后端云服务器组的描述信息

        :return: The description of this Pool.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Pool.

        后端云服务器组的描述信息

        :param description: The description of this Pool.
        :type: str
        """
        self._description = description

    @property
    def healthmonitor_id(self):
        """Gets the healthmonitor_id of this Pool.

        后端云服务器组关联的健康检查的ID。

        :return: The healthmonitor_id of this Pool.
        :rtype: str
        """
        return self._healthmonitor_id

    @healthmonitor_id.setter
    def healthmonitor_id(self, healthmonitor_id):
        """Sets the healthmonitor_id of this Pool.

        后端云服务器组关联的健康检查的ID。

        :param healthmonitor_id: The healthmonitor_id of this Pool.
        :type: str
        """
        self._healthmonitor_id = healthmonitor_id

    @property
    def id(self):
        """Gets the id of this Pool.

        后端云服务器组的ID。

        :return: The id of this Pool.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Pool.

        后端云服务器组的ID。

        :param id: The id of this Pool.
        :type: str
        """
        self._id = id

    @property
    def lb_algorithm(self):
        """Gets the lb_algorithm of this Pool.

        后端云服务器组的负载均衡算法，取值：ROUND_ROBIN：加权轮询算法；LEAST_CONNECTIONS：加权最少连接算法；SOURCE_IP：源IP算法；当该字段的取值为SOURCE_IP时，后端云服务器组绑定的后端云服务器的weight字段无效。

        :return: The lb_algorithm of this Pool.
        :rtype: str
        """
        return self._lb_algorithm

    @lb_algorithm.setter
    def lb_algorithm(self, lb_algorithm):
        """Sets the lb_algorithm of this Pool.

        后端云服务器组的负载均衡算法，取值：ROUND_ROBIN：加权轮询算法；LEAST_CONNECTIONS：加权最少连接算法；SOURCE_IP：源IP算法；当该字段的取值为SOURCE_IP时，后端云服务器组绑定的后端云服务器的weight字段无效。

        :param lb_algorithm: The lb_algorithm of this Pool.
        :type: str
        """
        self._lb_algorithm = lb_algorithm

    @property
    def listeners(self):
        """Gets the listeners of this Pool.

        后端云服务器组关联的监听器ID的列表。

        :return: The listeners of this Pool.
        :rtype: list[ListenerRef]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        """Sets the listeners of this Pool.

        后端云服务器组关联的监听器ID的列表。

        :param listeners: The listeners of this Pool.
        :type: list[ListenerRef]
        """
        self._listeners = listeners

    @property
    def loadbalancers(self):
        """Gets the loadbalancers of this Pool.

        后端云服务器组绑定的负载均衡器ID的列表。

        :return: The loadbalancers of this Pool.
        :rtype: list[LoadBalancerRef]
        """
        return self._loadbalancers

    @loadbalancers.setter
    def loadbalancers(self, loadbalancers):
        """Sets the loadbalancers of this Pool.

        后端云服务器组绑定的负载均衡器ID的列表。

        :param loadbalancers: The loadbalancers of this Pool.
        :type: list[LoadBalancerRef]
        """
        self._loadbalancers = loadbalancers

    @property
    def members(self):
        """Gets the members of this Pool.

        后端云服务器组关联的后端云服务器ID的列表。

        :return: The members of this Pool.
        :rtype: list[MemberRef]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this Pool.

        后端云服务器组关联的后端云服务器ID的列表。

        :param members: The members of this Pool.
        :type: list[MemberRef]
        """
        self._members = members

    @property
    def name(self):
        """Gets the name of this Pool.

        后端云服务器组的名称。

        :return: The name of this Pool.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Pool.

        后端云服务器组的名称。

        :param name: The name of this Pool.
        :type: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this Pool.

        后端云服务器组所在的项目ID。

        :return: The project_id of this Pool.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Pool.

        后端云服务器组所在的项目ID。

        :param project_id: The project_id of this Pool.
        :type: str
        """
        self._project_id = project_id

    @property
    def protocol(self):
        """Gets the protocol of this Pool.

        后端云服务器组的后端协议。 使用说明：支持TCP、UDP和HTTP。listener的protocol为UDP时pool的protocol必须为UDP；listener的protocol为TCP时pool的protocol必须为TCP；listener的protocol为HTTP或TERMINATED_HTTPS时pool的protocol必须为HTTP。

        :return: The protocol of this Pool.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this Pool.

        后端云服务器组的后端协议。 使用说明：支持TCP、UDP和HTTP。listener的protocol为UDP时pool的protocol必须为UDP；listener的protocol为TCP时pool的protocol必须为TCP；listener的protocol为HTTP或TERMINATED_HTTPS时pool的protocol必须为HTTP。

        :param protocol: The protocol of this Pool.
        :type: str
        """
        self._protocol = protocol

    @property
    def session_persistence(self):
        """Gets the session_persistence of this Pool.


        :return: The session_persistence of this Pool.
        :rtype: SessionPersistence
        """
        return self._session_persistence

    @session_persistence.setter
    def session_persistence(self, session_persistence):
        """Sets the session_persistence of this Pool.


        :param session_persistence: The session_persistence of this Pool.
        :type: SessionPersistence
        """
        self._session_persistence = session_persistence

    @property
    def ip_version(self):
        """Gets the ip_version of this Pool.

        后端云服务器组支持的IP版本， 共享型：默认为v4； 性能保障型：取值范围(dualstack、v4、v6)。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。当协议为HTTP时，ip_version为v4。

        :return: The ip_version of this Pool.
        :rtype: str
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this Pool.

        后端云服务器组支持的IP版本， 共享型：默认为v4； 性能保障型：取值范围(dualstack、v4、v6)。当协议为TCP/UDP时，ip_version为dualstack，表示双栈。当协议为HTTP时，ip_version为v4。

        :param ip_version: The ip_version of this Pool.
        :type: str
        """
        self._ip_version = ip_version

    @property
    def slow_start(self):
        """Gets the slow_start of this Pool.


        :return: The slow_start of this Pool.
        :rtype: SlowStart
        """
        return self._slow_start

    @slow_start.setter
    def slow_start(self, slow_start):
        """Sets the slow_start of this Pool.


        :param slow_start: The slow_start of this Pool.
        :type: SlowStart
        """
        self._slow_start = slow_start

    @property
    def member_deletion_protection_enable(self):
        """Gets the member_deletion_protection_enable of this Pool.

        是否开启误删保护，默认false不开启

        :return: The member_deletion_protection_enable of this Pool.
        :rtype: bool
        """
        return self._member_deletion_protection_enable

    @member_deletion_protection_enable.setter
    def member_deletion_protection_enable(self, member_deletion_protection_enable):
        """Sets the member_deletion_protection_enable of this Pool.

        是否开启误删保护，默认false不开启

        :param member_deletion_protection_enable: The member_deletion_protection_enable of this Pool.
        :type: bool
        """
        self._member_deletion_protection_enable = member_deletion_protection_enable

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Pool):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
