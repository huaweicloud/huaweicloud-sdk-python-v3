# coding: utf-8

import pprint
import re

import six





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
        'description': 'str',
        'lb_algorithm': 'str',
        'listener_id': 'str',
        'loadbalancer_id': 'str',
        'name': 'str',
        'project_id': 'str',
        'protocol': 'str',
        'session_persistence': 'CreatePoolSessionPersistenceOption',
        'slow_start': 'CreatePoolSlowStartOption',
        'member_deletion_protection_enable': 'bool'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'description': 'description',
        'lb_algorithm': 'lb_algorithm',
        'listener_id': 'listener_id',
        'loadbalancer_id': 'loadbalancer_id',
        'name': 'name',
        'project_id': 'project_id',
        'protocol': 'protocol',
        'session_persistence': 'session_persistence',
        'slow_start': 'slow_start',
        'member_deletion_protection_enable': 'member_deletion_protection_enable'
    }

    def __init__(self, admin_state_up=None, description=None, lb_algorithm=None, listener_id=None, loadbalancer_id=None, name=None, project_id=None, protocol=None, session_persistence=None, slow_start=None, member_deletion_protection_enable=False):
        """CreatePoolOption - a model defined in huaweicloud sdk"""
        
        

        self._admin_state_up = None
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
        self.discriminator = None

        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
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

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this CreatePoolOption.

        后端云服务器组的管理状态；该字段为预留字段，暂未启用。只支持更新为true。

        :return: The admin_state_up of this CreatePoolOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this CreatePoolOption.

        后端云服务器组的管理状态；该字段为预留字段，暂未启用。只支持更新为true。

        :param admin_state_up: The admin_state_up of this CreatePoolOption.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def description(self):
        """Gets the description of this CreatePoolOption.

        后端云服务器组的描述信息

        :return: The description of this CreatePoolOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreatePoolOption.

        后端云服务器组的描述信息

        :param description: The description of this CreatePoolOption.
        :type: str
        """
        self._description = description

    @property
    def lb_algorithm(self):
        """Gets the lb_algorithm of this CreatePoolOption.

        描述：后端云服务器组的负载均衡算法     取值：   1、ROUND_ROBIN：加权轮询算法；   2、LEAST_CONNECTIONS：加权最少连接算法；   3、SOURCE_IP：源IP算法；   4、QUIC_CID：连接ID算法；   约束：   1、当该字段的取值为SOURCE_IP时，后端云服务器组绑定的后端云服务器的weight字段无效。   2、只有pool的protocol为QUIC时，才支持QUIC_CID算法。

        :return: The lb_algorithm of this CreatePoolOption.
        :rtype: str
        """
        return self._lb_algorithm

    @lb_algorithm.setter
    def lb_algorithm(self, lb_algorithm):
        """Sets the lb_algorithm of this CreatePoolOption.

        描述：后端云服务器组的负载均衡算法     取值：   1、ROUND_ROBIN：加权轮询算法；   2、LEAST_CONNECTIONS：加权最少连接算法；   3、SOURCE_IP：源IP算法；   4、QUIC_CID：连接ID算法；   约束：   1、当该字段的取值为SOURCE_IP时，后端云服务器组绑定的后端云服务器的weight字段无效。   2、只有pool的protocol为QUIC时，才支持QUIC_CID算法。

        :param lb_algorithm: The lb_algorithm of this CreatePoolOption.
        :type: str
        """
        self._lb_algorithm = lb_algorithm

    @property
    def listener_id(self):
        """Gets the listener_id of this CreatePoolOption.

        后端云服务器组关联的监听器的ID。listener_id和loadbalancer_id中至少指定一个。

        :return: The listener_id of this CreatePoolOption.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this CreatePoolOption.

        后端云服务器组关联的监听器的ID。listener_id和loadbalancer_id中至少指定一个。

        :param listener_id: The listener_id of this CreatePoolOption.
        :type: str
        """
        self._listener_id = listener_id

    @property
    def loadbalancer_id(self):
        """Gets the loadbalancer_id of this CreatePoolOption.

        后端云服务器组关联的负载均衡器ID。listener_id和loadbalancer_id中至少指定一个。

        :return: The loadbalancer_id of this CreatePoolOption.
        :rtype: str
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        """Sets the loadbalancer_id of this CreatePoolOption.

        后端云服务器组关联的负载均衡器ID。listener_id和loadbalancer_id中至少指定一个。

        :param loadbalancer_id: The loadbalancer_id of this CreatePoolOption.
        :type: str
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def name(self):
        """Gets the name of this CreatePoolOption.

        后端云服务器组的名称。

        :return: The name of this CreatePoolOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreatePoolOption.

        后端云服务器组的名称。

        :param name: The name of this CreatePoolOption.
        :type: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this CreatePoolOption.

        后端云服务器组所在的项目ID。

        :return: The project_id of this CreatePoolOption.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreatePoolOption.

        后端云服务器组所在的项目ID。

        :param project_id: The project_id of this CreatePoolOption.
        :type: str
        """
        self._project_id = project_id

    @property
    def protocol(self):
        """Gets the protocol of this CreatePoolOption.

        描述：后端云服务器组的后端协议。   使用说明：支持TCP、UDP、HTTP和QUIC。 约束： 1、listener的protocol为UDP时，pool的protocol必须为UDP或QUIC；   2、listener的protocol为TCP时pool的protocol必须为TCP；   3、listener的protocol为HTTP或TERMINATED_HTTPS时，pool的protocol必须为HTTP。

        :return: The protocol of this CreatePoolOption.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this CreatePoolOption.

        描述：后端云服务器组的后端协议。   使用说明：支持TCP、UDP、HTTP和QUIC。 约束： 1、listener的protocol为UDP时，pool的protocol必须为UDP或QUIC；   2、listener的protocol为TCP时pool的protocol必须为TCP；   3、listener的protocol为HTTP或TERMINATED_HTTPS时，pool的protocol必须为HTTP。

        :param protocol: The protocol of this CreatePoolOption.
        :type: str
        """
        self._protocol = protocol

    @property
    def session_persistence(self):
        """Gets the session_persistence of this CreatePoolOption.


        :return: The session_persistence of this CreatePoolOption.
        :rtype: CreatePoolSessionPersistenceOption
        """
        return self._session_persistence

    @session_persistence.setter
    def session_persistence(self, session_persistence):
        """Sets the session_persistence of this CreatePoolOption.


        :param session_persistence: The session_persistence of this CreatePoolOption.
        :type: CreatePoolSessionPersistenceOption
        """
        self._session_persistence = session_persistence

    @property
    def slow_start(self):
        """Gets the slow_start of this CreatePoolOption.


        :return: The slow_start of this CreatePoolOption.
        :rtype: CreatePoolSlowStartOption
        """
        return self._slow_start

    @slow_start.setter
    def slow_start(self, slow_start):
        """Sets the slow_start of this CreatePoolOption.


        :param slow_start: The slow_start of this CreatePoolOption.
        :type: CreatePoolSlowStartOption
        """
        self._slow_start = slow_start

    @property
    def member_deletion_protection_enable(self):
        """Gets the member_deletion_protection_enable of this CreatePoolOption.

        是否开启删除保护，默认不开启

        :return: The member_deletion_protection_enable of this CreatePoolOption.
        :rtype: bool
        """
        return self._member_deletion_protection_enable

    @member_deletion_protection_enable.setter
    def member_deletion_protection_enable(self, member_deletion_protection_enable):
        """Sets the member_deletion_protection_enable of this CreatePoolOption.

        是否开启删除保护，默认不开启

        :param member_deletion_protection_enable: The member_deletion_protection_enable of this CreatePoolOption.
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
        if not isinstance(other, CreatePoolOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
