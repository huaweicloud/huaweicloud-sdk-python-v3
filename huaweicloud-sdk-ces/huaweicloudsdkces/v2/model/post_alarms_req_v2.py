# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostAlarmsReqV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'namespace': 'str',
        'resource_group_id': 'str',
        'resources': 'list[list[Dimension]]',
        'policies': 'list[Policy]',
        'type': 'str',
        'alarm_notifications': 'list[Notification]',
        'ok_notifications': 'list[Notification]',
        'notification_begin_time': 'str',
        'notification_end_time': 'str',
        'enterprise_project_id': 'str',
        'enabled': 'bool',
        'notification_enabled': 'bool',
        'alarm_template_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'namespace': 'namespace',
        'resource_group_id': 'resource_group_id',
        'resources': 'resources',
        'policies': 'policies',
        'type': 'type',
        'alarm_notifications': 'alarm_notifications',
        'ok_notifications': 'ok_notifications',
        'notification_begin_time': 'notification_begin_time',
        'notification_end_time': 'notification_end_time',
        'enterprise_project_id': 'enterprise_project_id',
        'enabled': 'enabled',
        'notification_enabled': 'notification_enabled',
        'alarm_template_id': 'alarm_template_id'
    }

    def __init__(self, name=None, description=None, namespace=None, resource_group_id=None, resources=None, policies=None, type=None, alarm_notifications=None, ok_notifications=None, notification_begin_time=None, notification_end_time=None, enterprise_project_id=None, enabled=None, notification_enabled=None, alarm_template_id=None):
        """PostAlarmsReqV2

        The model defined in huaweicloud sdk

        :param name: 告警名称, 只能包含0-9/a-z/A-Z/_/-或汉字，长度1-128
        :type name: str
        :param description: 告警描述，长度0-256
        :type description: str
        :param namespace: 查询服务的命名空间，各服务命名空间请参考[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)
        :type namespace: str
        :param resource_group_id: 资源分组ID，以rg开头，后跟22位由字母或数字组成的字符串
        :type resource_group_id: str
        :param resources: 资源列表，监控范围为指定资源时必传
        :type resources: list[list[Dimension]]
        :param policies: 告警策略
        :type policies: list[:class:`huaweicloudsdkces.v2.Policy`]
        :param type: 告警规则类型
        :type type: str
        :param alarm_notifications: 告警触发的动作
        :type alarm_notifications: list[:class:`huaweicloudsdkces.v2.Notification`]
        :param ok_notifications: 告警恢复触发的动作
        :type ok_notifications: list[:class:`huaweicloudsdkces.v2.Notification`]
        :param notification_begin_time: 告警通知开启时间
        :type notification_begin_time: str
        :param notification_end_time: 告警通知关闭时间
        :type notification_end_time: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param enabled: 告警开关
        :type enabled: bool
        :param notification_enabled: 是否开启告警通知
        :type notification_enabled: bool
        :param alarm_template_id: 告警规则关联告警模板ID，如果传了，告警规则关联的策略会和告警模板策略联动变化
        :type alarm_template_id: str
        """
        
        

        self._name = None
        self._description = None
        self._namespace = None
        self._resource_group_id = None
        self._resources = None
        self._policies = None
        self._type = None
        self._alarm_notifications = None
        self._ok_notifications = None
        self._notification_begin_time = None
        self._notification_end_time = None
        self._enterprise_project_id = None
        self._enabled = None
        self._notification_enabled = None
        self._alarm_template_id = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.namespace = namespace
        if resource_group_id is not None:
            self.resource_group_id = resource_group_id
        self.resources = resources
        self.policies = policies
        self.type = type
        if alarm_notifications is not None:
            self.alarm_notifications = alarm_notifications
        if ok_notifications is not None:
            self.ok_notifications = ok_notifications
        if notification_begin_time is not None:
            self.notification_begin_time = notification_begin_time
        if notification_end_time is not None:
            self.notification_end_time = notification_end_time
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.enabled = enabled
        self.notification_enabled = notification_enabled
        if alarm_template_id is not None:
            self.alarm_template_id = alarm_template_id

    @property
    def name(self):
        """Gets the name of this PostAlarmsReqV2.

        告警名称, 只能包含0-9/a-z/A-Z/_/-或汉字，长度1-128

        :return: The name of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostAlarmsReqV2.

        告警名称, 只能包含0-9/a-z/A-Z/_/-或汉字，长度1-128

        :param name: The name of this PostAlarmsReqV2.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this PostAlarmsReqV2.

        告警描述，长度0-256

        :return: The description of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PostAlarmsReqV2.

        告警描述，长度0-256

        :param description: The description of this PostAlarmsReqV2.
        :type description: str
        """
        self._description = description

    @property
    def namespace(self):
        """Gets the namespace of this PostAlarmsReqV2.

        查询服务的命名空间，各服务命名空间请参考[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)

        :return: The namespace of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this PostAlarmsReqV2.

        查询服务的命名空间，各服务命名空间请参考[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)

        :param namespace: The namespace of this PostAlarmsReqV2.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def resource_group_id(self):
        """Gets the resource_group_id of this PostAlarmsReqV2.

        资源分组ID，以rg开头，后跟22位由字母或数字组成的字符串

        :return: The resource_group_id of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._resource_group_id

    @resource_group_id.setter
    def resource_group_id(self, resource_group_id):
        """Sets the resource_group_id of this PostAlarmsReqV2.

        资源分组ID，以rg开头，后跟22位由字母或数字组成的字符串

        :param resource_group_id: The resource_group_id of this PostAlarmsReqV2.
        :type resource_group_id: str
        """
        self._resource_group_id = resource_group_id

    @property
    def resources(self):
        """Gets the resources of this PostAlarmsReqV2.

        资源列表，监控范围为指定资源时必传

        :return: The resources of this PostAlarmsReqV2.
        :rtype: list[list[Dimension]]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this PostAlarmsReqV2.

        资源列表，监控范围为指定资源时必传

        :param resources: The resources of this PostAlarmsReqV2.
        :type resources: list[list[Dimension]]
        """
        self._resources = resources

    @property
    def policies(self):
        """Gets the policies of this PostAlarmsReqV2.

        告警策略

        :return: The policies of this PostAlarmsReqV2.
        :rtype: list[:class:`huaweicloudsdkces.v2.Policy`]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this PostAlarmsReqV2.

        告警策略

        :param policies: The policies of this PostAlarmsReqV2.
        :type policies: list[:class:`huaweicloudsdkces.v2.Policy`]
        """
        self._policies = policies

    @property
    def type(self):
        """Gets the type of this PostAlarmsReqV2.

        告警规则类型

        :return: The type of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PostAlarmsReqV2.

        告警规则类型

        :param type: The type of this PostAlarmsReqV2.
        :type type: str
        """
        self._type = type

    @property
    def alarm_notifications(self):
        """Gets the alarm_notifications of this PostAlarmsReqV2.

        告警触发的动作

        :return: The alarm_notifications of this PostAlarmsReqV2.
        :rtype: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        return self._alarm_notifications

    @alarm_notifications.setter
    def alarm_notifications(self, alarm_notifications):
        """Sets the alarm_notifications of this PostAlarmsReqV2.

        告警触发的动作

        :param alarm_notifications: The alarm_notifications of this PostAlarmsReqV2.
        :type alarm_notifications: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        self._alarm_notifications = alarm_notifications

    @property
    def ok_notifications(self):
        """Gets the ok_notifications of this PostAlarmsReqV2.

        告警恢复触发的动作

        :return: The ok_notifications of this PostAlarmsReqV2.
        :rtype: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        return self._ok_notifications

    @ok_notifications.setter
    def ok_notifications(self, ok_notifications):
        """Sets the ok_notifications of this PostAlarmsReqV2.

        告警恢复触发的动作

        :param ok_notifications: The ok_notifications of this PostAlarmsReqV2.
        :type ok_notifications: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        self._ok_notifications = ok_notifications

    @property
    def notification_begin_time(self):
        """Gets the notification_begin_time of this PostAlarmsReqV2.

        告警通知开启时间

        :return: The notification_begin_time of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._notification_begin_time

    @notification_begin_time.setter
    def notification_begin_time(self, notification_begin_time):
        """Sets the notification_begin_time of this PostAlarmsReqV2.

        告警通知开启时间

        :param notification_begin_time: The notification_begin_time of this PostAlarmsReqV2.
        :type notification_begin_time: str
        """
        self._notification_begin_time = notification_begin_time

    @property
    def notification_end_time(self):
        """Gets the notification_end_time of this PostAlarmsReqV2.

        告警通知关闭时间

        :return: The notification_end_time of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._notification_end_time

    @notification_end_time.setter
    def notification_end_time(self, notification_end_time):
        """Sets the notification_end_time of this PostAlarmsReqV2.

        告警通知关闭时间

        :param notification_end_time: The notification_end_time of this PostAlarmsReqV2.
        :type notification_end_time: str
        """
        self._notification_end_time = notification_end_time

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this PostAlarmsReqV2.

        企业项目ID

        :return: The enterprise_project_id of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this PostAlarmsReqV2.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this PostAlarmsReqV2.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enabled(self):
        """Gets the enabled of this PostAlarmsReqV2.

        告警开关

        :return: The enabled of this PostAlarmsReqV2.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this PostAlarmsReqV2.

        告警开关

        :param enabled: The enabled of this PostAlarmsReqV2.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def notification_enabled(self):
        """Gets the notification_enabled of this PostAlarmsReqV2.

        是否开启告警通知

        :return: The notification_enabled of this PostAlarmsReqV2.
        :rtype: bool
        """
        return self._notification_enabled

    @notification_enabled.setter
    def notification_enabled(self, notification_enabled):
        """Sets the notification_enabled of this PostAlarmsReqV2.

        是否开启告警通知

        :param notification_enabled: The notification_enabled of this PostAlarmsReqV2.
        :type notification_enabled: bool
        """
        self._notification_enabled = notification_enabled

    @property
    def alarm_template_id(self):
        """Gets the alarm_template_id of this PostAlarmsReqV2.

        告警规则关联告警模板ID，如果传了，告警规则关联的策略会和告警模板策略联动变化

        :return: The alarm_template_id of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._alarm_template_id

    @alarm_template_id.setter
    def alarm_template_id(self, alarm_template_id):
        """Sets the alarm_template_id of this PostAlarmsReqV2.

        告警规则关联告警模板ID，如果传了，告警规则关联的策略会和告警模板策略联动变化

        :param alarm_template_id: The alarm_template_id of this PostAlarmsReqV2.
        :type alarm_template_id: str
        """
        self._alarm_template_id = alarm_template_id

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
        if not isinstance(other, PostAlarmsReqV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
