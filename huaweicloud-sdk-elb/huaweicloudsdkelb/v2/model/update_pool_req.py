# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePoolReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'lb_algorithm': 'str',
        'name': 'str',
        'description': 'str',
        'admin_state_up': 'bool',
        'session_persistence': 'SessionPersistence'
    }

    attribute_map = {
        'lb_algorithm': 'lb_algorithm',
        'name': 'name',
        'description': 'description',
        'admin_state_up': 'admin_state_up',
        'session_persistence': 'session_persistence'
    }

    def __init__(self, lb_algorithm=None, name=None, description=None, admin_state_up=None, session_persistence=None):
        """UpdatePoolReq

        The model defined in huaweicloud sdk

        :param lb_algorithm: 后端云服务器组的负载均衡算法，取值：ROUND_ROBIN：加权轮询算法；LEAST_CONNECTIONS：加权最少连接算法；SOURCE_IP：源IP算法；当该字段的取值为SOURCE_IP时，后端云服务器组绑定的后端云服务器的weight字段无效。
        :type lb_algorithm: str
        :param name: 后端云服务器组的名称。
        :type name: str
        :param description: 后端云服务器组的描述信息
        :type description: str
        :param admin_state_up: 后端云服务器组的管理状态；该字段为预留字段，暂未启用。只支持更新为true。
        :type admin_state_up: bool
        :param session_persistence: 
        :type session_persistence: :class:`huaweicloudsdkelb.v2.SessionPersistence`
        """
        
        

        self._lb_algorithm = None
        self._name = None
        self._description = None
        self._admin_state_up = None
        self._session_persistence = None
        self.discriminator = None

        if lb_algorithm is not None:
            self.lb_algorithm = lb_algorithm
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if session_persistence is not None:
            self.session_persistence = session_persistence

    @property
    def lb_algorithm(self):
        """Gets the lb_algorithm of this UpdatePoolReq.

        后端云服务器组的负载均衡算法，取值：ROUND_ROBIN：加权轮询算法；LEAST_CONNECTIONS：加权最少连接算法；SOURCE_IP：源IP算法；当该字段的取值为SOURCE_IP时，后端云服务器组绑定的后端云服务器的weight字段无效。

        :return: The lb_algorithm of this UpdatePoolReq.
        :rtype: str
        """
        return self._lb_algorithm

    @lb_algorithm.setter
    def lb_algorithm(self, lb_algorithm):
        """Sets the lb_algorithm of this UpdatePoolReq.

        后端云服务器组的负载均衡算法，取值：ROUND_ROBIN：加权轮询算法；LEAST_CONNECTIONS：加权最少连接算法；SOURCE_IP：源IP算法；当该字段的取值为SOURCE_IP时，后端云服务器组绑定的后端云服务器的weight字段无效。

        :param lb_algorithm: The lb_algorithm of this UpdatePoolReq.
        :type lb_algorithm: str
        """
        self._lb_algorithm = lb_algorithm

    @property
    def name(self):
        """Gets the name of this UpdatePoolReq.

        后端云服务器组的名称。

        :return: The name of this UpdatePoolReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdatePoolReq.

        后端云服务器组的名称。

        :param name: The name of this UpdatePoolReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdatePoolReq.

        后端云服务器组的描述信息

        :return: The description of this UpdatePoolReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdatePoolReq.

        后端云服务器组的描述信息

        :param description: The description of this UpdatePoolReq.
        :type description: str
        """
        self._description = description

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this UpdatePoolReq.

        后端云服务器组的管理状态；该字段为预留字段，暂未启用。只支持更新为true。

        :return: The admin_state_up of this UpdatePoolReq.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this UpdatePoolReq.

        后端云服务器组的管理状态；该字段为预留字段，暂未启用。只支持更新为true。

        :param admin_state_up: The admin_state_up of this UpdatePoolReq.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def session_persistence(self):
        """Gets the session_persistence of this UpdatePoolReq.


        :return: The session_persistence of this UpdatePoolReq.
        :rtype: :class:`huaweicloudsdkelb.v2.SessionPersistence`
        """
        return self._session_persistence

    @session_persistence.setter
    def session_persistence(self, session_persistence):
        """Sets the session_persistence of this UpdatePoolReq.


        :param session_persistence: The session_persistence of this UpdatePoolReq.
        :type session_persistence: :class:`huaweicloudsdkelb.v2.SessionPersistence`
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
        if not isinstance(other, UpdatePoolReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
