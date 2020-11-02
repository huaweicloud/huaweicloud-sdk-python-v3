# coding: utf-8

import pprint
import re

import six





class CreatePoolReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'protocol': 'str',
        'lb_algorithm': 'str',
        'loadbalancer_id': 'str',
        'listener_id': 'str',
        'tenant_id': 'str',
        'name': 'str',
        'description': 'str',
        'admin_state_up': 'bool',
        'session_persistence': 'SessionPersistence'
    }

    attribute_map = {
        'protocol': 'protocol',
        'lb_algorithm': 'lb_algorithm',
        'loadbalancer_id': 'loadbalancer_id',
        'listener_id': 'listener_id',
        'tenant_id': 'tenant_id',
        'name': 'name',
        'description': 'description',
        'admin_state_up': 'admin_state_up',
        'session_persistence': 'session_persistence'
    }

    def __init__(self, protocol=None, lb_algorithm=None, loadbalancer_id=None, listener_id=None, tenant_id=None, name=None, description=None, admin_state_up=None, session_persistence=None):
        """CreatePoolReq - a model defined in huaweicloud sdk"""
        
        

        self._protocol = None
        self._lb_algorithm = None
        self._loadbalancer_id = None
        self._listener_id = None
        self._tenant_id = None
        self._name = None
        self._description = None
        self._admin_state_up = None
        self._session_persistence = None
        self.discriminator = None

        self.protocol = protocol
        self.lb_algorithm = lb_algorithm
        if loadbalancer_id is not None:
            self.loadbalancer_id = loadbalancer_id
        if listener_id is not None:
            self.listener_id = listener_id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if session_persistence is not None:
            self.session_persistence = session_persistence

    @property
    def protocol(self):
        """Gets the protocol of this CreatePoolReq.

        后端云服务器组的后端协议。取值：UDP、TCP、HTTP。当指定istener_id创建后端云服务器组时，后端云服务器组的protocol和它关联的监听器的protocol有如下关系：监听器的protocol为TCP时，后端云服务器组的protocol必须为TCP。监听器的protocol为UDP时，后端云服务器组的protocol必须为UDP。监听器的protocol为HTTP或TERMINATED_HTTPS时，后端云服务器组的protocol必须为HTTP。

        :return: The protocol of this CreatePoolReq.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this CreatePoolReq.

        后端云服务器组的后端协议。取值：UDP、TCP、HTTP。当指定istener_id创建后端云服务器组时，后端云服务器组的protocol和它关联的监听器的protocol有如下关系：监听器的protocol为TCP时，后端云服务器组的protocol必须为TCP。监听器的protocol为UDP时，后端云服务器组的protocol必须为UDP。监听器的protocol为HTTP或TERMINATED_HTTPS时，后端云服务器组的protocol必须为HTTP。

        :param protocol: The protocol of this CreatePoolReq.
        :type: str
        """
        self._protocol = protocol

    @property
    def lb_algorithm(self):
        """Gets the lb_algorithm of this CreatePoolReq.

        后端云服务器组的负载均衡算法，取值：ROUND_ROBIN：加权轮询算法；LEAST_CONNECTIONS：加权最少连接算法；SOURCE_IP：源IP算法；当该字段的取值为SOURCE_IP时，后端云服务器组绑定的后端云服务器的weight字段无效。

        :return: The lb_algorithm of this CreatePoolReq.
        :rtype: str
        """
        return self._lb_algorithm

    @lb_algorithm.setter
    def lb_algorithm(self, lb_algorithm):
        """Sets the lb_algorithm of this CreatePoolReq.

        后端云服务器组的负载均衡算法，取值：ROUND_ROBIN：加权轮询算法；LEAST_CONNECTIONS：加权最少连接算法；SOURCE_IP：源IP算法；当该字段的取值为SOURCE_IP时，后端云服务器组绑定的后端云服务器的weight字段无效。

        :param lb_algorithm: The lb_algorithm of this CreatePoolReq.
        :type: str
        """
        self._lb_algorithm = lb_algorithm

    @property
    def loadbalancer_id(self):
        """Gets the loadbalancer_id of this CreatePoolReq.

        后端云服务器组关联的负载均衡器ID。listener_id和loadbalancer_id中至少指定一个。

        :return: The loadbalancer_id of this CreatePoolReq.
        :rtype: str
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        """Sets the loadbalancer_id of this CreatePoolReq.

        后端云服务器组关联的负载均衡器ID。listener_id和loadbalancer_id中至少指定一个。

        :param loadbalancer_id: The loadbalancer_id of this CreatePoolReq.
        :type: str
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def listener_id(self):
        """Gets the listener_id of this CreatePoolReq.

        后端云服务器组关联的监听器的ID。listener_id和loadbalancer_id中至少指定一个。

        :return: The listener_id of this CreatePoolReq.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this CreatePoolReq.

        后端云服务器组关联的监听器的ID。listener_id和loadbalancer_id中至少指定一个。

        :param listener_id: The listener_id of this CreatePoolReq.
        :type: str
        """
        self._listener_id = listener_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this CreatePoolReq.

        后端云服务器组所在的项目ID。

        :return: The tenant_id of this CreatePoolReq.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this CreatePoolReq.

        后端云服务器组所在的项目ID。

        :param tenant_id: The tenant_id of this CreatePoolReq.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def name(self):
        """Gets the name of this CreatePoolReq.

        后端云服务器组的名称。

        :return: The name of this CreatePoolReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreatePoolReq.

        后端云服务器组的名称。

        :param name: The name of this CreatePoolReq.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreatePoolReq.

        后端云服务器组的描述信息

        :return: The description of this CreatePoolReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreatePoolReq.

        后端云服务器组的描述信息

        :param description: The description of this CreatePoolReq.
        :type: str
        """
        self._description = description

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this CreatePoolReq.

        后端云服务器组的管理状态。只支持设定为true，该字段的值无实际意义。

        :return: The admin_state_up of this CreatePoolReq.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this CreatePoolReq.

        后端云服务器组的管理状态。只支持设定为true，该字段的值无实际意义。

        :param admin_state_up: The admin_state_up of this CreatePoolReq.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def session_persistence(self):
        """Gets the session_persistence of this CreatePoolReq.


        :return: The session_persistence of this CreatePoolReq.
        :rtype: SessionPersistence
        """
        return self._session_persistence

    @session_persistence.setter
    def session_persistence(self, session_persistence):
        """Sets the session_persistence of this CreatePoolReq.


        :param session_persistence: The session_persistence of this CreatePoolReq.
        :type: SessionPersistence
        """
        self._session_persistence = session_persistence

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
        if not isinstance(other, CreatePoolReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
