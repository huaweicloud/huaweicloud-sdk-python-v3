# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnableOneClickAlarmRequestBodyOneClickUpdateAlarms:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_id': 'str',
        'name': 'str',
        'description': 'str',
        'namespace': 'str',
        'policies': 'list[Policy]',
        'resources': 'list[list[Dimension]]',
        'type': 'str',
        'enabled': 'bool',
        'notification_enabled': 'bool',
        'alarm_notifications': 'list[Notification]',
        'ok_notifications': 'list[Notification]',
        'notification_begin_time': 'str',
        'notification_end_time': 'str',
        'notification_manner': 'str',
        'notification_policy_ids': 'list[str]'
    }

    attribute_map = {
        'alarm_id': 'alarm_id',
        'name': 'name',
        'description': 'description',
        'namespace': 'namespace',
        'policies': 'policies',
        'resources': 'resources',
        'type': 'type',
        'enabled': 'enabled',
        'notification_enabled': 'notification_enabled',
        'alarm_notifications': 'alarm_notifications',
        'ok_notifications': 'ok_notifications',
        'notification_begin_time': 'notification_begin_time',
        'notification_end_time': 'notification_end_time',
        'notification_manner': 'notification_manner',
        'notification_policy_ids': 'notification_policy_ids'
    }

    def __init__(self, alarm_id=None, name=None, description=None, namespace=None, policies=None, resources=None, type=None, enabled=None, notification_enabled=None, alarm_notifications=None, ok_notifications=None, notification_begin_time=None, notification_end_time=None, notification_manner=None, notification_policy_ids=None):
        r"""EnableOneClickAlarmRequestBodyOneClickUpdateAlarms

        The model defined in huaweicloud sdk

        :param alarm_id: 告警规则id，以al开头，包含22个数字或字母
        :type alarm_id: str
        :param name: 此字段已废弃。告警名称, 只能包含0-9/a-z/A-Z/_/-或汉字，长度1-128
        :type name: str
        :param description: 此字段已废弃。告警描述，长度0-256
        :type description: str
        :param namespace: 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”
        :type namespace: str
        :param policies: 告警策略
        :type policies: list[:class:`huaweicloudsdkces.v2.Policy`]
        :param resources: 此字段已废弃。资源列表，关联资源需要使用查询告警规则资源接口获取
        :type resources: list[list[Dimension]]
        :param type: 此字段已废弃。 **参数解释**： 告警规则类型 **约束限制**： 不涉及。 **取值范围**： 枚举值。ALL_INSTANCE为全部资源指标告警，RESOURCE_GROUP为资源分组指标告警，MULTI_INSTANCE为指定资源指标告警，EVENT.SYS为系统事件告警，EVENT.CUSTOM自定义事件告警，DNSHealthCheck为健康检查告警； **默认取值**： 不涉及。 
        :type type: str
        :param enabled: 是否开启告警规则。true:开启，false:关闭。
        :type enabled: bool
        :param notification_enabled: 此字段已废弃。是否开启告警通知。true:开启，false:关闭。
        :type notification_enabled: bool
        :param alarm_notifications: 此字段已废弃。告警触发的动作
        :type alarm_notifications: list[:class:`huaweicloudsdkces.v2.Notification`]
        :param ok_notifications: 此字段已废弃。告警恢复触发的动作
        :type ok_notifications: list[:class:`huaweicloudsdkces.v2.Notification`]
        :param notification_begin_time: 此字段已废弃。告警通知开启时间
        :type notification_begin_time: str
        :param notification_end_time: 此字段已废弃。告警通知关闭时间
        :type notification_end_time: str
        :param notification_manner: 此字段已废弃。通知方式。NOTIFICATION_POLICY表示通知策略，NOTIFICATION_GROUP表示通知组，TOPIC_SUBSCRIPTION表示主题订阅。
        :type notification_manner: str
        :param notification_policy_ids: 此字段已废弃。关联的通知策略ID列表
        :type notification_policy_ids: list[str]
        """
        
        

        self._alarm_id = None
        self._name = None
        self._description = None
        self._namespace = None
        self._policies = None
        self._resources = None
        self._type = None
        self._enabled = None
        self._notification_enabled = None
        self._alarm_notifications = None
        self._ok_notifications = None
        self._notification_begin_time = None
        self._notification_end_time = None
        self._notification_manner = None
        self._notification_policy_ids = None
        self.discriminator = None

        if alarm_id is not None:
            self.alarm_id = alarm_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if namespace is not None:
            self.namespace = namespace
        if policies is not None:
            self.policies = policies
        if resources is not None:
            self.resources = resources
        if type is not None:
            self.type = type
        if enabled is not None:
            self.enabled = enabled
        if notification_enabled is not None:
            self.notification_enabled = notification_enabled
        if alarm_notifications is not None:
            self.alarm_notifications = alarm_notifications
        if ok_notifications is not None:
            self.ok_notifications = ok_notifications
        if notification_begin_time is not None:
            self.notification_begin_time = notification_begin_time
        if notification_end_time is not None:
            self.notification_end_time = notification_end_time
        if notification_manner is not None:
            self.notification_manner = notification_manner
        if notification_policy_ids is not None:
            self.notification_policy_ids = notification_policy_ids

    @property
    def alarm_id(self):
        r"""Gets the alarm_id of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        告警规则id，以al开头，包含22个数字或字母

        :return: The alarm_id of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        r"""Sets the alarm_id of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        告警规则id，以al开头，包含22个数字或字母

        :param alarm_id: The alarm_id of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :type alarm_id: str
        """
        self._alarm_id = alarm_id

    @property
    def name(self):
        r"""Gets the name of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        此字段已废弃。告警名称, 只能包含0-9/a-z/A-Z/_/-或汉字，长度1-128

        :return: The name of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        此字段已废弃。告警名称, 只能包含0-9/a-z/A-Z/_/-或汉字，长度1-128

        :param name: The name of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        此字段已废弃。告警描述，长度0-256

        :return: The description of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        此字段已废弃。告警描述，长度0-256

        :param description: The description of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :type description: str
        """
        self._description = description

    @property
    def namespace(self):
        r"""Gets the namespace of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”

        :return: The namespace of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”

        :param namespace: The namespace of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def policies(self):
        r"""Gets the policies of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        告警策略

        :return: The policies of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :rtype: list[:class:`huaweicloudsdkces.v2.Policy`]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        r"""Sets the policies of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        告警策略

        :param policies: The policies of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :type policies: list[:class:`huaweicloudsdkces.v2.Policy`]
        """
        self._policies = policies

    @property
    def resources(self):
        r"""Gets the resources of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        此字段已废弃。资源列表，关联资源需要使用查询告警规则资源接口获取

        :return: The resources of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :rtype: list[list[Dimension]]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        此字段已废弃。资源列表，关联资源需要使用查询告警规则资源接口获取

        :param resources: The resources of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :type resources: list[list[Dimension]]
        """
        self._resources = resources

    @property
    def type(self):
        r"""Gets the type of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        此字段已废弃。 **参数解释**： 告警规则类型 **约束限制**： 不涉及。 **取值范围**： 枚举值。ALL_INSTANCE为全部资源指标告警，RESOURCE_GROUP为资源分组指标告警，MULTI_INSTANCE为指定资源指标告警，EVENT.SYS为系统事件告警，EVENT.CUSTOM自定义事件告警，DNSHealthCheck为健康检查告警； **默认取值**： 不涉及。 

        :return: The type of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        此字段已废弃。 **参数解释**： 告警规则类型 **约束限制**： 不涉及。 **取值范围**： 枚举值。ALL_INSTANCE为全部资源指标告警，RESOURCE_GROUP为资源分组指标告警，MULTI_INSTANCE为指定资源指标告警，EVENT.SYS为系统事件告警，EVENT.CUSTOM自定义事件告警，DNSHealthCheck为健康检查告警； **默认取值**： 不涉及。 

        :param type: The type of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :type type: str
        """
        self._type = type

    @property
    def enabled(self):
        r"""Gets the enabled of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        是否开启告警规则。true:开启，false:关闭。

        :return: The enabled of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        是否开启告警规则。true:开启，false:关闭。

        :param enabled: The enabled of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def notification_enabled(self):
        r"""Gets the notification_enabled of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        此字段已废弃。是否开启告警通知。true:开启，false:关闭。

        :return: The notification_enabled of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :rtype: bool
        """
        return self._notification_enabled

    @notification_enabled.setter
    def notification_enabled(self, notification_enabled):
        r"""Sets the notification_enabled of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        此字段已废弃。是否开启告警通知。true:开启，false:关闭。

        :param notification_enabled: The notification_enabled of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :type notification_enabled: bool
        """
        self._notification_enabled = notification_enabled

    @property
    def alarm_notifications(self):
        r"""Gets the alarm_notifications of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        此字段已废弃。告警触发的动作

        :return: The alarm_notifications of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :rtype: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        return self._alarm_notifications

    @alarm_notifications.setter
    def alarm_notifications(self, alarm_notifications):
        r"""Sets the alarm_notifications of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        此字段已废弃。告警触发的动作

        :param alarm_notifications: The alarm_notifications of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :type alarm_notifications: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        self._alarm_notifications = alarm_notifications

    @property
    def ok_notifications(self):
        r"""Gets the ok_notifications of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        此字段已废弃。告警恢复触发的动作

        :return: The ok_notifications of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :rtype: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        return self._ok_notifications

    @ok_notifications.setter
    def ok_notifications(self, ok_notifications):
        r"""Sets the ok_notifications of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        此字段已废弃。告警恢复触发的动作

        :param ok_notifications: The ok_notifications of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :type ok_notifications: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        self._ok_notifications = ok_notifications

    @property
    def notification_begin_time(self):
        r"""Gets the notification_begin_time of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        此字段已废弃。告警通知开启时间

        :return: The notification_begin_time of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :rtype: str
        """
        return self._notification_begin_time

    @notification_begin_time.setter
    def notification_begin_time(self, notification_begin_time):
        r"""Sets the notification_begin_time of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        此字段已废弃。告警通知开启时间

        :param notification_begin_time: The notification_begin_time of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :type notification_begin_time: str
        """
        self._notification_begin_time = notification_begin_time

    @property
    def notification_end_time(self):
        r"""Gets the notification_end_time of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        此字段已废弃。告警通知关闭时间

        :return: The notification_end_time of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :rtype: str
        """
        return self._notification_end_time

    @notification_end_time.setter
    def notification_end_time(self, notification_end_time):
        r"""Sets the notification_end_time of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        此字段已废弃。告警通知关闭时间

        :param notification_end_time: The notification_end_time of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :type notification_end_time: str
        """
        self._notification_end_time = notification_end_time

    @property
    def notification_manner(self):
        r"""Gets the notification_manner of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        此字段已废弃。通知方式。NOTIFICATION_POLICY表示通知策略，NOTIFICATION_GROUP表示通知组，TOPIC_SUBSCRIPTION表示主题订阅。

        :return: The notification_manner of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :rtype: str
        """
        return self._notification_manner

    @notification_manner.setter
    def notification_manner(self, notification_manner):
        r"""Sets the notification_manner of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        此字段已废弃。通知方式。NOTIFICATION_POLICY表示通知策略，NOTIFICATION_GROUP表示通知组，TOPIC_SUBSCRIPTION表示主题订阅。

        :param notification_manner: The notification_manner of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :type notification_manner: str
        """
        self._notification_manner = notification_manner

    @property
    def notification_policy_ids(self):
        r"""Gets the notification_policy_ids of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        此字段已废弃。关联的通知策略ID列表

        :return: The notification_policy_ids of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :rtype: list[str]
        """
        return self._notification_policy_ids

    @notification_policy_ids.setter
    def notification_policy_ids(self, notification_policy_ids):
        r"""Sets the notification_policy_ids of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.

        此字段已废弃。关联的通知策略ID列表

        :param notification_policy_ids: The notification_policy_ids of this EnableOneClickAlarmRequestBodyOneClickUpdateAlarms.
        :type notification_policy_ids: list[str]
        """
        self._notification_policy_ids = notification_policy_ids

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
        if not isinstance(other, EnableOneClickAlarmRequestBodyOneClickUpdateAlarms):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
