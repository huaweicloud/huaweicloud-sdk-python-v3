# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmRuleEntity:

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
        'policies': 'str',
        'resources': 'str',
        'type': 'str',
        'enabled': 'bool',
        'notification_enabled': 'bool',
        'alarm_notifications': 'str',
        'ok_notifications': 'str',
        'notification_begin_time': 'str',
        'notification_end_time': 'str',
        'region_id': 'str',
        'enterprise_project_id': 'str',
        'alarm_template_id': 'str'
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
        'region_id': 'region_id',
        'enterprise_project_id': 'enterprise_project_id',
        'alarm_template_id': 'alarm_template_id'
    }

    def __init__(self, alarm_id=None, name=None, description=None, namespace=None, policies=None, resources=None, type=None, enabled=None, notification_enabled=None, alarm_notifications=None, ok_notifications=None, notification_begin_time=None, notification_end_time=None, region_id=None, enterprise_project_id=None, alarm_template_id=None):
        r"""AlarmRuleEntity

        The model defined in huaweicloud sdk

        :param alarm_id: 告警规则ID
        :type alarm_id: str
        :param name: 告警名称
        :type name: str
        :param description: 告警描述
        :type description: str
        :param namespace: 告警命名空间，取值范围：SYS.CBR,SYS.RDS,SYS.GaussDB
        :type namespace: str
        :param policies: 告警策略
        :type policies: str
        :param resources: 资源列表
        :type resources: str
        :param type: 告警类型
        :type type: str
        :param enabled: 告警开关
        :type enabled: bool
        :param notification_enabled: 是否开启告警通知
        :type notification_enabled: bool
        :param alarm_notifications: 告警触发的动作
        :type alarm_notifications: str
        :param ok_notifications: 告警恢复触发的动作
        :type ok_notifications: str
        :param notification_begin_time: 告警通知开启时间
        :type notification_begin_time: str
        :param notification_end_time: 告警通知关闭时间
        :type notification_end_time: str
        :param region_id: RegionID
        :type region_id: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param alarm_template_id: 告警规则关联告警模板ID
        :type alarm_template_id: str
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
        self._region_id = None
        self._enterprise_project_id = None
        self._alarm_template_id = None
        self.discriminator = None

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
        if region_id is not None:
            self.region_id = region_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if alarm_template_id is not None:
            self.alarm_template_id = alarm_template_id

    @property
    def alarm_id(self):
        r"""Gets the alarm_id of this AlarmRuleEntity.

        告警规则ID

        :return: The alarm_id of this AlarmRuleEntity.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        r"""Sets the alarm_id of this AlarmRuleEntity.

        告警规则ID

        :param alarm_id: The alarm_id of this AlarmRuleEntity.
        :type alarm_id: str
        """
        self._alarm_id = alarm_id

    @property
    def name(self):
        r"""Gets the name of this AlarmRuleEntity.

        告警名称

        :return: The name of this AlarmRuleEntity.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AlarmRuleEntity.

        告警名称

        :param name: The name of this AlarmRuleEntity.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this AlarmRuleEntity.

        告警描述

        :return: The description of this AlarmRuleEntity.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AlarmRuleEntity.

        告警描述

        :param description: The description of this AlarmRuleEntity.
        :type description: str
        """
        self._description = description

    @property
    def namespace(self):
        r"""Gets the namespace of this AlarmRuleEntity.

        告警命名空间，取值范围：SYS.CBR,SYS.RDS,SYS.GaussDB

        :return: The namespace of this AlarmRuleEntity.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this AlarmRuleEntity.

        告警命名空间，取值范围：SYS.CBR,SYS.RDS,SYS.GaussDB

        :param namespace: The namespace of this AlarmRuleEntity.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def policies(self):
        r"""Gets the policies of this AlarmRuleEntity.

        告警策略

        :return: The policies of this AlarmRuleEntity.
        :rtype: str
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        r"""Sets the policies of this AlarmRuleEntity.

        告警策略

        :param policies: The policies of this AlarmRuleEntity.
        :type policies: str
        """
        self._policies = policies

    @property
    def resources(self):
        r"""Gets the resources of this AlarmRuleEntity.

        资源列表

        :return: The resources of this AlarmRuleEntity.
        :rtype: str
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this AlarmRuleEntity.

        资源列表

        :param resources: The resources of this AlarmRuleEntity.
        :type resources: str
        """
        self._resources = resources

    @property
    def type(self):
        r"""Gets the type of this AlarmRuleEntity.

        告警类型

        :return: The type of this AlarmRuleEntity.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AlarmRuleEntity.

        告警类型

        :param type: The type of this AlarmRuleEntity.
        :type type: str
        """
        self._type = type

    @property
    def enabled(self):
        r"""Gets the enabled of this AlarmRuleEntity.

        告警开关

        :return: The enabled of this AlarmRuleEntity.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this AlarmRuleEntity.

        告警开关

        :param enabled: The enabled of this AlarmRuleEntity.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def notification_enabled(self):
        r"""Gets the notification_enabled of this AlarmRuleEntity.

        是否开启告警通知

        :return: The notification_enabled of this AlarmRuleEntity.
        :rtype: bool
        """
        return self._notification_enabled

    @notification_enabled.setter
    def notification_enabled(self, notification_enabled):
        r"""Sets the notification_enabled of this AlarmRuleEntity.

        是否开启告警通知

        :param notification_enabled: The notification_enabled of this AlarmRuleEntity.
        :type notification_enabled: bool
        """
        self._notification_enabled = notification_enabled

    @property
    def alarm_notifications(self):
        r"""Gets the alarm_notifications of this AlarmRuleEntity.

        告警触发的动作

        :return: The alarm_notifications of this AlarmRuleEntity.
        :rtype: str
        """
        return self._alarm_notifications

    @alarm_notifications.setter
    def alarm_notifications(self, alarm_notifications):
        r"""Sets the alarm_notifications of this AlarmRuleEntity.

        告警触发的动作

        :param alarm_notifications: The alarm_notifications of this AlarmRuleEntity.
        :type alarm_notifications: str
        """
        self._alarm_notifications = alarm_notifications

    @property
    def ok_notifications(self):
        r"""Gets the ok_notifications of this AlarmRuleEntity.

        告警恢复触发的动作

        :return: The ok_notifications of this AlarmRuleEntity.
        :rtype: str
        """
        return self._ok_notifications

    @ok_notifications.setter
    def ok_notifications(self, ok_notifications):
        r"""Sets the ok_notifications of this AlarmRuleEntity.

        告警恢复触发的动作

        :param ok_notifications: The ok_notifications of this AlarmRuleEntity.
        :type ok_notifications: str
        """
        self._ok_notifications = ok_notifications

    @property
    def notification_begin_time(self):
        r"""Gets the notification_begin_time of this AlarmRuleEntity.

        告警通知开启时间

        :return: The notification_begin_time of this AlarmRuleEntity.
        :rtype: str
        """
        return self._notification_begin_time

    @notification_begin_time.setter
    def notification_begin_time(self, notification_begin_time):
        r"""Sets the notification_begin_time of this AlarmRuleEntity.

        告警通知开启时间

        :param notification_begin_time: The notification_begin_time of this AlarmRuleEntity.
        :type notification_begin_time: str
        """
        self._notification_begin_time = notification_begin_time

    @property
    def notification_end_time(self):
        r"""Gets the notification_end_time of this AlarmRuleEntity.

        告警通知关闭时间

        :return: The notification_end_time of this AlarmRuleEntity.
        :rtype: str
        """
        return self._notification_end_time

    @notification_end_time.setter
    def notification_end_time(self, notification_end_time):
        r"""Sets the notification_end_time of this AlarmRuleEntity.

        告警通知关闭时间

        :param notification_end_time: The notification_end_time of this AlarmRuleEntity.
        :type notification_end_time: str
        """
        self._notification_end_time = notification_end_time

    @property
    def region_id(self):
        r"""Gets the region_id of this AlarmRuleEntity.

        RegionID

        :return: The region_id of this AlarmRuleEntity.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this AlarmRuleEntity.

        RegionID

        :param region_id: The region_id of this AlarmRuleEntity.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this AlarmRuleEntity.

        企业项目ID

        :return: The enterprise_project_id of this AlarmRuleEntity.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this AlarmRuleEntity.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this AlarmRuleEntity.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def alarm_template_id(self):
        r"""Gets the alarm_template_id of this AlarmRuleEntity.

        告警规则关联告警模板ID

        :return: The alarm_template_id of this AlarmRuleEntity.
        :rtype: str
        """
        return self._alarm_template_id

    @alarm_template_id.setter
    def alarm_template_id(self, alarm_template_id):
        r"""Sets the alarm_template_id of this AlarmRuleEntity.

        告警规则关联告警模板ID

        :param alarm_template_id: The alarm_template_id of this AlarmRuleEntity.
        :type alarm_template_id: str
        """
        self._alarm_template_id = alarm_template_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AlarmRuleEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
