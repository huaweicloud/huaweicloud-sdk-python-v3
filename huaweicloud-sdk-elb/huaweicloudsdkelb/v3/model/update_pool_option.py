# coding: utf-8

import pprint
import re

import six





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
        'member_deletion_protection_enable': 'bool'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'description': 'description',
        'lb_algorithm': 'lb_algorithm',
        'name': 'name',
        'session_persistence': 'session_persistence',
        'slow_start': 'slow_start',
        'member_deletion_protection_enable': 'member_deletion_protection_enable'
    }

    def __init__(self, admin_state_up=None, description=None, lb_algorithm=None, name=None, session_persistence=None, slow_start=None, member_deletion_protection_enable=False):
        """UpdatePoolOption - a model defined in huaweicloud sdk"""
        
        

        self._admin_state_up = None
        self._description = None
        self._lb_algorithm = None
        self._name = None
        self._session_persistence = None
        self._slow_start = None
        self._member_deletion_protection_enable = None
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

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this UpdatePoolOption.

        后端云服务器组的管理状态；该字段为预留字段，暂未启用。只支持更新为true。

        :return: The admin_state_up of this UpdatePoolOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this UpdatePoolOption.

        后端云服务器组的管理状态；该字段为预留字段，暂未启用。只支持更新为true。

        :param admin_state_up: The admin_state_up of this UpdatePoolOption.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def description(self):
        """Gets the description of this UpdatePoolOption.

        后端云服务器组的描述信息

        :return: The description of this UpdatePoolOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdatePoolOption.

        后端云服务器组的描述信息

        :param description: The description of this UpdatePoolOption.
        :type: str
        """
        self._description = description

    @property
    def lb_algorithm(self):
        """Gets the lb_algorithm of this UpdatePoolOption.

        描述：后端云服务器组的负载均衡算法     取值：   1、ROUND_ROBIN：加权轮询算法；   2、LEAST_CONNECTIONS：加权最少连接算法；   3、SOURCE_IP：源IP算法；   4、QUIC_CID：连接ID算法；   约束：   1、当该字段的取值为SOURCE_IP时，后端云服务器组绑定的后端云服务器的weight字段无效。   2、只有pool的protocol为QUIC时，才支持QUIC_CID算法。

        :return: The lb_algorithm of this UpdatePoolOption.
        :rtype: str
        """
        return self._lb_algorithm

    @lb_algorithm.setter
    def lb_algorithm(self, lb_algorithm):
        """Sets the lb_algorithm of this UpdatePoolOption.

        描述：后端云服务器组的负载均衡算法     取值：   1、ROUND_ROBIN：加权轮询算法；   2、LEAST_CONNECTIONS：加权最少连接算法；   3、SOURCE_IP：源IP算法；   4、QUIC_CID：连接ID算法；   约束：   1、当该字段的取值为SOURCE_IP时，后端云服务器组绑定的后端云服务器的weight字段无效。   2、只有pool的protocol为QUIC时，才支持QUIC_CID算法。

        :param lb_algorithm: The lb_algorithm of this UpdatePoolOption.
        :type: str
        """
        self._lb_algorithm = lb_algorithm

    @property
    def name(self):
        """Gets the name of this UpdatePoolOption.

        后端云服务器组的名称。

        :return: The name of this UpdatePoolOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdatePoolOption.

        后端云服务器组的名称。

        :param name: The name of this UpdatePoolOption.
        :type: str
        """
        self._name = name

    @property
    def session_persistence(self):
        """Gets the session_persistence of this UpdatePoolOption.


        :return: The session_persistence of this UpdatePoolOption.
        :rtype: UpdatePoolSessionPersistenceOption
        """
        return self._session_persistence

    @session_persistence.setter
    def session_persistence(self, session_persistence):
        """Sets the session_persistence of this UpdatePoolOption.


        :param session_persistence: The session_persistence of this UpdatePoolOption.
        :type: UpdatePoolSessionPersistenceOption
        """
        self._session_persistence = session_persistence

    @property
    def slow_start(self):
        """Gets the slow_start of this UpdatePoolOption.


        :return: The slow_start of this UpdatePoolOption.
        :rtype: UpdatePoolSlowStartOption
        """
        return self._slow_start

    @slow_start.setter
    def slow_start(self, slow_start):
        """Sets the slow_start of this UpdatePoolOption.


        :param slow_start: The slow_start of this UpdatePoolOption.
        :type: UpdatePoolSlowStartOption
        """
        self._slow_start = slow_start

    @property
    def member_deletion_protection_enable(self):
        """Gets the member_deletion_protection_enable of this UpdatePoolOption.

        是否开启删除保护，默认不开启

        :return: The member_deletion_protection_enable of this UpdatePoolOption.
        :rtype: bool
        """
        return self._member_deletion_protection_enable

    @member_deletion_protection_enable.setter
    def member_deletion_protection_enable(self, member_deletion_protection_enable):
        """Sets the member_deletion_protection_enable of this UpdatePoolOption.

        是否开启删除保护，默认不开启

        :param member_deletion_protection_enable: The member_deletion_protection_enable of this UpdatePoolOption.
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
        if not isinstance(other, UpdatePoolOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
