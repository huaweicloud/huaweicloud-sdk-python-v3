# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmNotification:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'notification_type': 'str',
        'route_group_enable': 'bool',
        'route_group_rule': 'str',
        'notification_enable': 'bool',
        'bind_notification_rule_id': 'str',
        'notify_resolved': 'bool',
        'notify_triggered': 'bool',
        'notify_frequency': 'int'
    }

    attribute_map = {
        'notification_type': 'notification_type',
        'route_group_enable': 'route_group_enable',
        'route_group_rule': 'route_group_rule',
        'notification_enable': 'notification_enable',
        'bind_notification_rule_id': 'bind_notification_rule_id',
        'notify_resolved': 'notify_resolved',
        'notify_triggered': 'notify_triggered',
        'notify_frequency': 'notify_frequency'
    }

    def __init__(self, notification_type=None, route_group_enable=None, route_group_rule=None, notification_enable=None, bind_notification_rule_id=None, notify_resolved=None, notify_triggered=None, notify_frequency=None):
        """AlarmNotification

        The model defined in huaweicloud sdk

        :param notification_type: 通知类型。 - “direct”：直接告警 - “alarm_policy”：告警降噪
        :type notification_type: str
        :param route_group_enable: 启用分组规则。 - 当通知类型为“alarm_policy”时：true - 当通知类型为“direct”时：false
        :type route_group_enable: bool
        :param route_group_rule: 分组规则名称。 - 当route_group_enable 为true时，填分组规则名称 - 当route_group_enable 为false时，填“”
        :type route_group_rule: str
        :param notification_enable: 是否启用告警行动规则。 - 当通知类型为“direct”时，填true - 当通知类型为“alarm_policy”时，填false
        :type notification_enable: bool
        :param bind_notification_rule_id: 告警行动策略id。 - 当notification_enable为true时，填告警行动策略id - 当notification_enable为false时，填“”
        :type bind_notification_rule_id: str
        :param notify_resolved: 告警解决是否通知。 - true：通知 - false：不通知
        :type notify_resolved: bool
        :param notify_triggered: 告警触发是否通知。 - true：通知 - false：不通知
        :type notify_triggered: bool
        :param notify_frequency: 通知频率 - 当通知类型为“alarm_policy”时，填“-1” - 当通知类型为“direct”时，    - “0”：只告警一次    - “300”：每5分钟    - “600”：每10分钟    - “900”：每15分钟    - “1800”：每30分钟    - “3600”：每1小时    - “10800”：每3小时    - “21600”：每6小时    - “43200”：每12小时    - “86400”：每天
        :type notify_frequency: int
        """
        
        

        self._notification_type = None
        self._route_group_enable = None
        self._route_group_rule = None
        self._notification_enable = None
        self._bind_notification_rule_id = None
        self._notify_resolved = None
        self._notify_triggered = None
        self._notify_frequency = None
        self.discriminator = None

        self.notification_type = notification_type
        self.route_group_enable = route_group_enable
        self.route_group_rule = route_group_rule
        if notification_enable is not None:
            self.notification_enable = notification_enable
        if bind_notification_rule_id is not None:
            self.bind_notification_rule_id = bind_notification_rule_id
        if notify_resolved is not None:
            self.notify_resolved = notify_resolved
        if notify_triggered is not None:
            self.notify_triggered = notify_triggered
        if notify_frequency is not None:
            self.notify_frequency = notify_frequency

    @property
    def notification_type(self):
        """Gets the notification_type of this AlarmNotification.

        通知类型。 - “direct”：直接告警 - “alarm_policy”：告警降噪

        :return: The notification_type of this AlarmNotification.
        :rtype: str
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type):
        """Sets the notification_type of this AlarmNotification.

        通知类型。 - “direct”：直接告警 - “alarm_policy”：告警降噪

        :param notification_type: The notification_type of this AlarmNotification.
        :type notification_type: str
        """
        self._notification_type = notification_type

    @property
    def route_group_enable(self):
        """Gets the route_group_enable of this AlarmNotification.

        启用分组规则。 - 当通知类型为“alarm_policy”时：true - 当通知类型为“direct”时：false

        :return: The route_group_enable of this AlarmNotification.
        :rtype: bool
        """
        return self._route_group_enable

    @route_group_enable.setter
    def route_group_enable(self, route_group_enable):
        """Sets the route_group_enable of this AlarmNotification.

        启用分组规则。 - 当通知类型为“alarm_policy”时：true - 当通知类型为“direct”时：false

        :param route_group_enable: The route_group_enable of this AlarmNotification.
        :type route_group_enable: bool
        """
        self._route_group_enable = route_group_enable

    @property
    def route_group_rule(self):
        """Gets the route_group_rule of this AlarmNotification.

        分组规则名称。 - 当route_group_enable 为true时，填分组规则名称 - 当route_group_enable 为false时，填“”

        :return: The route_group_rule of this AlarmNotification.
        :rtype: str
        """
        return self._route_group_rule

    @route_group_rule.setter
    def route_group_rule(self, route_group_rule):
        """Sets the route_group_rule of this AlarmNotification.

        分组规则名称。 - 当route_group_enable 为true时，填分组规则名称 - 当route_group_enable 为false时，填“”

        :param route_group_rule: The route_group_rule of this AlarmNotification.
        :type route_group_rule: str
        """
        self._route_group_rule = route_group_rule

    @property
    def notification_enable(self):
        """Gets the notification_enable of this AlarmNotification.

        是否启用告警行动规则。 - 当通知类型为“direct”时，填true - 当通知类型为“alarm_policy”时，填false

        :return: The notification_enable of this AlarmNotification.
        :rtype: bool
        """
        return self._notification_enable

    @notification_enable.setter
    def notification_enable(self, notification_enable):
        """Sets the notification_enable of this AlarmNotification.

        是否启用告警行动规则。 - 当通知类型为“direct”时，填true - 当通知类型为“alarm_policy”时，填false

        :param notification_enable: The notification_enable of this AlarmNotification.
        :type notification_enable: bool
        """
        self._notification_enable = notification_enable

    @property
    def bind_notification_rule_id(self):
        """Gets the bind_notification_rule_id of this AlarmNotification.

        告警行动策略id。 - 当notification_enable为true时，填告警行动策略id - 当notification_enable为false时，填“”

        :return: The bind_notification_rule_id of this AlarmNotification.
        :rtype: str
        """
        return self._bind_notification_rule_id

    @bind_notification_rule_id.setter
    def bind_notification_rule_id(self, bind_notification_rule_id):
        """Sets the bind_notification_rule_id of this AlarmNotification.

        告警行动策略id。 - 当notification_enable为true时，填告警行动策略id - 当notification_enable为false时，填“”

        :param bind_notification_rule_id: The bind_notification_rule_id of this AlarmNotification.
        :type bind_notification_rule_id: str
        """
        self._bind_notification_rule_id = bind_notification_rule_id

    @property
    def notify_resolved(self):
        """Gets the notify_resolved of this AlarmNotification.

        告警解决是否通知。 - true：通知 - false：不通知

        :return: The notify_resolved of this AlarmNotification.
        :rtype: bool
        """
        return self._notify_resolved

    @notify_resolved.setter
    def notify_resolved(self, notify_resolved):
        """Sets the notify_resolved of this AlarmNotification.

        告警解决是否通知。 - true：通知 - false：不通知

        :param notify_resolved: The notify_resolved of this AlarmNotification.
        :type notify_resolved: bool
        """
        self._notify_resolved = notify_resolved

    @property
    def notify_triggered(self):
        """Gets the notify_triggered of this AlarmNotification.

        告警触发是否通知。 - true：通知 - false：不通知

        :return: The notify_triggered of this AlarmNotification.
        :rtype: bool
        """
        return self._notify_triggered

    @notify_triggered.setter
    def notify_triggered(self, notify_triggered):
        """Sets the notify_triggered of this AlarmNotification.

        告警触发是否通知。 - true：通知 - false：不通知

        :param notify_triggered: The notify_triggered of this AlarmNotification.
        :type notify_triggered: bool
        """
        self._notify_triggered = notify_triggered

    @property
    def notify_frequency(self):
        """Gets the notify_frequency of this AlarmNotification.

        通知频率 - 当通知类型为“alarm_policy”时，填“-1” - 当通知类型为“direct”时，    - “0”：只告警一次    - “300”：每5分钟    - “600”：每10分钟    - “900”：每15分钟    - “1800”：每30分钟    - “3600”：每1小时    - “10800”：每3小时    - “21600”：每6小时    - “43200”：每12小时    - “86400”：每天

        :return: The notify_frequency of this AlarmNotification.
        :rtype: int
        """
        return self._notify_frequency

    @notify_frequency.setter
    def notify_frequency(self, notify_frequency):
        """Sets the notify_frequency of this AlarmNotification.

        通知频率 - 当通知类型为“alarm_policy”时，填“-1” - 当通知类型为“direct”时，    - “0”：只告警一次    - “300”：每5分钟    - “600”：每10分钟    - “900”：每15分钟    - “1800”：每30分钟    - “3600”：每1小时    - “10800”：每3小时    - “21600”：每6小时    - “43200”：每12小时    - “86400”：每天

        :param notify_frequency: The notify_frequency of this AlarmNotification.
        :type notify_frequency: int
        """
        self._notify_frequency = notify_frequency

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
        if not isinstance(other, AlarmNotification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
