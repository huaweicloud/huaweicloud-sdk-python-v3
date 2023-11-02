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
        'any_port_enable': 'bool'
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
        'any_port_enable': 'any_port_enable'
    }

    def __init__(self, admin_state_up=None, description=None, lb_algorithm=None, name=None, session_persistence=None, slow_start=None, member_deletion_protection_enable=None, vpc_id=None, type=None, protection_status=None, protection_reason=None, any_port_enable=None):
        """UpdatePoolOption

        The model defined in huaweicloud sdk

        :param admin_state_up: 后端云服务器组的管理状态，只支持更新为true。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)
        :type admin_state_up: bool
        :param description: 后端云服务器组的描述信息。
        :type description: str
        :param lb_algorithm: 后端云服务器组的负载均衡算法。  取值： - ROUND_ROBIN：加权轮询算法。 - LEAST_CONNECTIONS：加权最少连接算法。 - SOURCE_IP：源IP算法。 - QUIC_CID：连接ID算法。  使用说明： - 当该字段的取值为SOURCE_IP时，后端云服务器组绑定的后端云服务器的weight字段无效。 - 只有pool的protocol为QUIC时，才支持QUIC_CID算法。  [不支持QUIC_CID。](tag:hws_eu,g42,hk_g42,hcso_dt,tm)
        :type lb_algorithm: str
        :param name: 后端云服务器组的名称。
        :type name: str
        :param session_persistence: 
        :type session_persistence: :class:`huaweicloudsdkelb.v3.UpdatePoolSessionPersistenceOption`
        :param slow_start: 
        :type slow_start: :class:`huaweicloudsdkelb.v3.UpdatePoolSlowStartOption`
        :param member_deletion_protection_enable: 是否开启删除保护。  取值：false不开启，true开启。  &gt; 退场时需要先关闭所有资源的删除保护开关。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)
        :type member_deletion_protection_enable: bool
        :param vpc_id: 后端云服务器组关联的虚拟私有云的ID。  只有vpc_id为空时允许更新。
        :type vpc_id: str
        :param type: 后端服务器组的类型。  取值： - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加跨VPC后端，type指定为该类型时，vpc_id不允许指定。 - 空字符串（\&quot;\&quot;）：允许任意类型的后端  使用说明： - 只有type为空时允许更新，不允许从非空更新为空。
        :type type: str
        :param protection_status: 修改保护状态, 取值： - nonProtection: 不保护 - consoleProtection: 控制台修改保护
        :type protection_status: str
        :param protection_reason: 设置保护的原因 &gt;仅当protection_status为consoleProtection时有效。
        :type protection_reason: str
        :param any_port_enable: 后端是否开启端口透传，开启后，后端服务器端口与前端监听器端口保持一致。  使用说明： - 仅QUIC,TCP,UDP的pool支持。  &gt; 关闭端口透传后，请求会转发给后端服务器protocol_port字段指定端口。
        :type any_port_enable: bool
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

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this UpdatePoolOption.

        后端云服务器组的管理状态，只支持更新为true。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)

        :return: The admin_state_up of this UpdatePoolOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this UpdatePoolOption.

        后端云服务器组的管理状态，只支持更新为true。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)

        :param admin_state_up: The admin_state_up of this UpdatePoolOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def description(self):
        """Gets the description of this UpdatePoolOption.

        后端云服务器组的描述信息。

        :return: The description of this UpdatePoolOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdatePoolOption.

        后端云服务器组的描述信息。

        :param description: The description of this UpdatePoolOption.
        :type description: str
        """
        self._description = description

    @property
    def lb_algorithm(self):
        """Gets the lb_algorithm of this UpdatePoolOption.

        后端云服务器组的负载均衡算法。  取值： - ROUND_ROBIN：加权轮询算法。 - LEAST_CONNECTIONS：加权最少连接算法。 - SOURCE_IP：源IP算法。 - QUIC_CID：连接ID算法。  使用说明： - 当该字段的取值为SOURCE_IP时，后端云服务器组绑定的后端云服务器的weight字段无效。 - 只有pool的protocol为QUIC时，才支持QUIC_CID算法。  [不支持QUIC_CID。](tag:hws_eu,g42,hk_g42,hcso_dt,tm)

        :return: The lb_algorithm of this UpdatePoolOption.
        :rtype: str
        """
        return self._lb_algorithm

    @lb_algorithm.setter
    def lb_algorithm(self, lb_algorithm):
        """Sets the lb_algorithm of this UpdatePoolOption.

        后端云服务器组的负载均衡算法。  取值： - ROUND_ROBIN：加权轮询算法。 - LEAST_CONNECTIONS：加权最少连接算法。 - SOURCE_IP：源IP算法。 - QUIC_CID：连接ID算法。  使用说明： - 当该字段的取值为SOURCE_IP时，后端云服务器组绑定的后端云服务器的weight字段无效。 - 只有pool的protocol为QUIC时，才支持QUIC_CID算法。  [不支持QUIC_CID。](tag:hws_eu,g42,hk_g42,hcso_dt,tm)

        :param lb_algorithm: The lb_algorithm of this UpdatePoolOption.
        :type lb_algorithm: str
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
        :type name: str
        """
        self._name = name

    @property
    def session_persistence(self):
        """Gets the session_persistence of this UpdatePoolOption.

        :return: The session_persistence of this UpdatePoolOption.
        :rtype: :class:`huaweicloudsdkelb.v3.UpdatePoolSessionPersistenceOption`
        """
        return self._session_persistence

    @session_persistence.setter
    def session_persistence(self, session_persistence):
        """Sets the session_persistence of this UpdatePoolOption.

        :param session_persistence: The session_persistence of this UpdatePoolOption.
        :type session_persistence: :class:`huaweicloudsdkelb.v3.UpdatePoolSessionPersistenceOption`
        """
        self._session_persistence = session_persistence

    @property
    def slow_start(self):
        """Gets the slow_start of this UpdatePoolOption.

        :return: The slow_start of this UpdatePoolOption.
        :rtype: :class:`huaweicloudsdkelb.v3.UpdatePoolSlowStartOption`
        """
        return self._slow_start

    @slow_start.setter
    def slow_start(self, slow_start):
        """Sets the slow_start of this UpdatePoolOption.

        :param slow_start: The slow_start of this UpdatePoolOption.
        :type slow_start: :class:`huaweicloudsdkelb.v3.UpdatePoolSlowStartOption`
        """
        self._slow_start = slow_start

    @property
    def member_deletion_protection_enable(self):
        """Gets the member_deletion_protection_enable of this UpdatePoolOption.

        是否开启删除保护。  取值：false不开启，true开启。  > 退场时需要先关闭所有资源的删除保护开关。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)

        :return: The member_deletion_protection_enable of this UpdatePoolOption.
        :rtype: bool
        """
        return self._member_deletion_protection_enable

    @member_deletion_protection_enable.setter
    def member_deletion_protection_enable(self, member_deletion_protection_enable):
        """Sets the member_deletion_protection_enable of this UpdatePoolOption.

        是否开启删除保护。  取值：false不开启，true开启。  > 退场时需要先关闭所有资源的删除保护开关。  [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)

        :param member_deletion_protection_enable: The member_deletion_protection_enable of this UpdatePoolOption.
        :type member_deletion_protection_enable: bool
        """
        self._member_deletion_protection_enable = member_deletion_protection_enable

    @property
    def vpc_id(self):
        """Gets the vpc_id of this UpdatePoolOption.

        后端云服务器组关联的虚拟私有云的ID。  只有vpc_id为空时允许更新。

        :return: The vpc_id of this UpdatePoolOption.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this UpdatePoolOption.

        后端云服务器组关联的虚拟私有云的ID。  只有vpc_id为空时允许更新。

        :param vpc_id: The vpc_id of this UpdatePoolOption.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def type(self):
        """Gets the type of this UpdatePoolOption.

        后端服务器组的类型。  取值： - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加跨VPC后端，type指定为该类型时，vpc_id不允许指定。 - 空字符串（\"\"）：允许任意类型的后端  使用说明： - 只有type为空时允许更新，不允许从非空更新为空。

        :return: The type of this UpdatePoolOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdatePoolOption.

        后端服务器组的类型。  取值： - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加跨VPC后端，type指定为该类型时，vpc_id不允许指定。 - 空字符串（\"\"）：允许任意类型的后端  使用说明： - 只有type为空时允许更新，不允许从非空更新为空。

        :param type: The type of this UpdatePoolOption.
        :type type: str
        """
        self._type = type

    @property
    def protection_status(self):
        """Gets the protection_status of this UpdatePoolOption.

        修改保护状态, 取值： - nonProtection: 不保护 - consoleProtection: 控制台修改保护

        :return: The protection_status of this UpdatePoolOption.
        :rtype: str
        """
        return self._protection_status

    @protection_status.setter
    def protection_status(self, protection_status):
        """Sets the protection_status of this UpdatePoolOption.

        修改保护状态, 取值： - nonProtection: 不保护 - consoleProtection: 控制台修改保护

        :param protection_status: The protection_status of this UpdatePoolOption.
        :type protection_status: str
        """
        self._protection_status = protection_status

    @property
    def protection_reason(self):
        """Gets the protection_reason of this UpdatePoolOption.

        设置保护的原因 >仅当protection_status为consoleProtection时有效。

        :return: The protection_reason of this UpdatePoolOption.
        :rtype: str
        """
        return self._protection_reason

    @protection_reason.setter
    def protection_reason(self, protection_reason):
        """Sets the protection_reason of this UpdatePoolOption.

        设置保护的原因 >仅当protection_status为consoleProtection时有效。

        :param protection_reason: The protection_reason of this UpdatePoolOption.
        :type protection_reason: str
        """
        self._protection_reason = protection_reason

    @property
    def any_port_enable(self):
        """Gets the any_port_enable of this UpdatePoolOption.

        后端是否开启端口透传，开启后，后端服务器端口与前端监听器端口保持一致。  使用说明： - 仅QUIC,TCP,UDP的pool支持。  > 关闭端口透传后，请求会转发给后端服务器protocol_port字段指定端口。

        :return: The any_port_enable of this UpdatePoolOption.
        :rtype: bool
        """
        return self._any_port_enable

    @any_port_enable.setter
    def any_port_enable(self, any_port_enable):
        """Sets the any_port_enable of this UpdatePoolOption.

        后端是否开启端口透传，开启后，后端服务器端口与前端监听器端口保持一致。  使用说明： - 仅QUIC,TCP,UDP的pool支持。  > 关闭端口透传后，请求会转发给后端服务器protocol_port字段指定端口。

        :param any_port_enable: The any_port_enable of this UpdatePoolOption.
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
        if not isinstance(other, UpdatePoolOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
