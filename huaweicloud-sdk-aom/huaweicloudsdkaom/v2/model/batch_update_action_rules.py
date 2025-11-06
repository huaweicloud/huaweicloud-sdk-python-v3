# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateActionRules:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_rule_id': 'int',
        'alarm_rule_name': 'str',
        'alarm_rule_type': 'str',
        'bind_notification_rule_id': 'str',
        'frequency': 'str',
        'notification_enable': 'bool',
        'notification_type': 'str',
        'notify_resolved': 'bool',
        'notify_triggered': 'bool',
        'route_group_enable': 'bool',
        'route_group_rule': 'str'
    }

    attribute_map = {
        'alarm_rule_id': 'alarm_rule_id',
        'alarm_rule_name': 'alarm_rule_name',
        'alarm_rule_type': 'alarm_rule_type',
        'bind_notification_rule_id': 'bind_notification_rule_id',
        'frequency': 'frequency',
        'notification_enable': 'notification_enable',
        'notification_type': 'notification_type',
        'notify_resolved': 'notify_resolved',
        'notify_triggered': 'notify_triggered',
        'route_group_enable': 'route_group_enable',
        'route_group_rule': 'route_group_rule'
    }

    def __init__(self, alarm_rule_id=None, alarm_rule_name=None, alarm_rule_type=None, bind_notification_rule_id=None, frequency=None, notification_enable=None, notification_type=None, notify_resolved=None, notify_triggered=None, route_group_enable=None, route_group_rule=None):
        r"""BatchUpdateActionRules

        The model defined in huaweicloud sdk

        :param alarm_rule_id: 告警规则id。
        :type alarm_rule_id: int
        :param alarm_rule_name: 告警规则名称。
        :type alarm_rule_name: str
        :param alarm_rule_type: 告警规则类型。
        :type alarm_rule_type: str
        :param bind_notification_rule_id: 待绑定的告警行动规则名称。
        :type bind_notification_rule_id: str
        :param frequency: 通知频率 - 当通知类型为“alarm_policy”时，填“-1” - 当通知类型为“direct”时，    - “0”：只告警一次    - “300”：每5分钟    - “600”：每10分钟    - “900”：每15分钟    - “1800”：每30分钟    - “3600”：每1小时    - “10800”：每3小时    - “21600”：每6小时    - “43200”：每12小时    - “86400”：每天
        :type frequency: str
        :param notification_enable: 是否启用告警通知规则。 - 当通知类型为“direct”时，填true - 当通知类型为“alarm_policy”时，填false 如果告警触发“notify_triggered”或告警恢复“notify_resolved”都设置为false（即都不进行告警通知），则notification_enable需设置为false。
        :type notification_enable: bool
        :param notification_type: 通知类型。 - “direct”：直接告警 - “alarm_policy”：告警降噪
        :type notification_type: str
        :param notify_resolved: 告警解决是否通知。 - true：通知 - false：不通知
        :type notify_resolved: bool
        :param notify_triggered: 告警触发是否通知。 - true：通知 - false：不通知
        :type notify_triggered: bool
        :param route_group_enable: 启用告警分组规则。 - 当通知类型为“alarm_policy”时：true - 当通知类型为“direct”时：false 如果告警触发“notify_triggered”或告警恢复“notify_resolved”都设置为false（即都不进行告警通知），则route_group_enable需设置为false。
        :type route_group_enable: bool
        :param route_group_rule: 告警分组规则名称。 - 当route_group_enable 为true时，填告警分组规则名称 - 当route_group_enable 为false时，填“”
        :type route_group_rule: str
        """
        
        

        self._alarm_rule_id = None
        self._alarm_rule_name = None
        self._alarm_rule_type = None
        self._bind_notification_rule_id = None
        self._frequency = None
        self._notification_enable = None
        self._notification_type = None
        self._notify_resolved = None
        self._notify_triggered = None
        self._route_group_enable = None
        self._route_group_rule = None
        self.discriminator = None

        self.alarm_rule_id = alarm_rule_id
        self.alarm_rule_name = alarm_rule_name
        self.alarm_rule_type = alarm_rule_type
        if bind_notification_rule_id is not None:
            self.bind_notification_rule_id = bind_notification_rule_id
        self.frequency = frequency
        if notification_enable is not None:
            self.notification_enable = notification_enable
        if notification_type is not None:
            self.notification_type = notification_type
        self.notify_resolved = notify_resolved
        self.notify_triggered = notify_triggered
        if route_group_enable is not None:
            self.route_group_enable = route_group_enable
        if route_group_rule is not None:
            self.route_group_rule = route_group_rule

    @property
    def alarm_rule_id(self):
        r"""Gets the alarm_rule_id of this BatchUpdateActionRules.

        告警规则id。

        :return: The alarm_rule_id of this BatchUpdateActionRules.
        :rtype: int
        """
        return self._alarm_rule_id

    @alarm_rule_id.setter
    def alarm_rule_id(self, alarm_rule_id):
        r"""Sets the alarm_rule_id of this BatchUpdateActionRules.

        告警规则id。

        :param alarm_rule_id: The alarm_rule_id of this BatchUpdateActionRules.
        :type alarm_rule_id: int
        """
        self._alarm_rule_id = alarm_rule_id

    @property
    def alarm_rule_name(self):
        r"""Gets the alarm_rule_name of this BatchUpdateActionRules.

        告警规则名称。

        :return: The alarm_rule_name of this BatchUpdateActionRules.
        :rtype: str
        """
        return self._alarm_rule_name

    @alarm_rule_name.setter
    def alarm_rule_name(self, alarm_rule_name):
        r"""Sets the alarm_rule_name of this BatchUpdateActionRules.

        告警规则名称。

        :param alarm_rule_name: The alarm_rule_name of this BatchUpdateActionRules.
        :type alarm_rule_name: str
        """
        self._alarm_rule_name = alarm_rule_name

    @property
    def alarm_rule_type(self):
        r"""Gets the alarm_rule_type of this BatchUpdateActionRules.

        告警规则类型。

        :return: The alarm_rule_type of this BatchUpdateActionRules.
        :rtype: str
        """
        return self._alarm_rule_type

    @alarm_rule_type.setter
    def alarm_rule_type(self, alarm_rule_type):
        r"""Sets the alarm_rule_type of this BatchUpdateActionRules.

        告警规则类型。

        :param alarm_rule_type: The alarm_rule_type of this BatchUpdateActionRules.
        :type alarm_rule_type: str
        """
        self._alarm_rule_type = alarm_rule_type

    @property
    def bind_notification_rule_id(self):
        r"""Gets the bind_notification_rule_id of this BatchUpdateActionRules.

        待绑定的告警行动规则名称。

        :return: The bind_notification_rule_id of this BatchUpdateActionRules.
        :rtype: str
        """
        return self._bind_notification_rule_id

    @bind_notification_rule_id.setter
    def bind_notification_rule_id(self, bind_notification_rule_id):
        r"""Sets the bind_notification_rule_id of this BatchUpdateActionRules.

        待绑定的告警行动规则名称。

        :param bind_notification_rule_id: The bind_notification_rule_id of this BatchUpdateActionRules.
        :type bind_notification_rule_id: str
        """
        self._bind_notification_rule_id = bind_notification_rule_id

    @property
    def frequency(self):
        r"""Gets the frequency of this BatchUpdateActionRules.

        通知频率 - 当通知类型为“alarm_policy”时，填“-1” - 当通知类型为“direct”时，    - “0”：只告警一次    - “300”：每5分钟    - “600”：每10分钟    - “900”：每15分钟    - “1800”：每30分钟    - “3600”：每1小时    - “10800”：每3小时    - “21600”：每6小时    - “43200”：每12小时    - “86400”：每天

        :return: The frequency of this BatchUpdateActionRules.
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        r"""Sets the frequency of this BatchUpdateActionRules.

        通知频率 - 当通知类型为“alarm_policy”时，填“-1” - 当通知类型为“direct”时，    - “0”：只告警一次    - “300”：每5分钟    - “600”：每10分钟    - “900”：每15分钟    - “1800”：每30分钟    - “3600”：每1小时    - “10800”：每3小时    - “21600”：每6小时    - “43200”：每12小时    - “86400”：每天

        :param frequency: The frequency of this BatchUpdateActionRules.
        :type frequency: str
        """
        self._frequency = frequency

    @property
    def notification_enable(self):
        r"""Gets the notification_enable of this BatchUpdateActionRules.

        是否启用告警通知规则。 - 当通知类型为“direct”时，填true - 当通知类型为“alarm_policy”时，填false 如果告警触发“notify_triggered”或告警恢复“notify_resolved”都设置为false（即都不进行告警通知），则notification_enable需设置为false。

        :return: The notification_enable of this BatchUpdateActionRules.
        :rtype: bool
        """
        return self._notification_enable

    @notification_enable.setter
    def notification_enable(self, notification_enable):
        r"""Sets the notification_enable of this BatchUpdateActionRules.

        是否启用告警通知规则。 - 当通知类型为“direct”时，填true - 当通知类型为“alarm_policy”时，填false 如果告警触发“notify_triggered”或告警恢复“notify_resolved”都设置为false（即都不进行告警通知），则notification_enable需设置为false。

        :param notification_enable: The notification_enable of this BatchUpdateActionRules.
        :type notification_enable: bool
        """
        self._notification_enable = notification_enable

    @property
    def notification_type(self):
        r"""Gets the notification_type of this BatchUpdateActionRules.

        通知类型。 - “direct”：直接告警 - “alarm_policy”：告警降噪

        :return: The notification_type of this BatchUpdateActionRules.
        :rtype: str
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type):
        r"""Sets the notification_type of this BatchUpdateActionRules.

        通知类型。 - “direct”：直接告警 - “alarm_policy”：告警降噪

        :param notification_type: The notification_type of this BatchUpdateActionRules.
        :type notification_type: str
        """
        self._notification_type = notification_type

    @property
    def notify_resolved(self):
        r"""Gets the notify_resolved of this BatchUpdateActionRules.

        告警解决是否通知。 - true：通知 - false：不通知

        :return: The notify_resolved of this BatchUpdateActionRules.
        :rtype: bool
        """
        return self._notify_resolved

    @notify_resolved.setter
    def notify_resolved(self, notify_resolved):
        r"""Sets the notify_resolved of this BatchUpdateActionRules.

        告警解决是否通知。 - true：通知 - false：不通知

        :param notify_resolved: The notify_resolved of this BatchUpdateActionRules.
        :type notify_resolved: bool
        """
        self._notify_resolved = notify_resolved

    @property
    def notify_triggered(self):
        r"""Gets the notify_triggered of this BatchUpdateActionRules.

        告警触发是否通知。 - true：通知 - false：不通知

        :return: The notify_triggered of this BatchUpdateActionRules.
        :rtype: bool
        """
        return self._notify_triggered

    @notify_triggered.setter
    def notify_triggered(self, notify_triggered):
        r"""Sets the notify_triggered of this BatchUpdateActionRules.

        告警触发是否通知。 - true：通知 - false：不通知

        :param notify_triggered: The notify_triggered of this BatchUpdateActionRules.
        :type notify_triggered: bool
        """
        self._notify_triggered = notify_triggered

    @property
    def route_group_enable(self):
        r"""Gets the route_group_enable of this BatchUpdateActionRules.

        启用告警分组规则。 - 当通知类型为“alarm_policy”时：true - 当通知类型为“direct”时：false 如果告警触发“notify_triggered”或告警恢复“notify_resolved”都设置为false（即都不进行告警通知），则route_group_enable需设置为false。

        :return: The route_group_enable of this BatchUpdateActionRules.
        :rtype: bool
        """
        return self._route_group_enable

    @route_group_enable.setter
    def route_group_enable(self, route_group_enable):
        r"""Sets the route_group_enable of this BatchUpdateActionRules.

        启用告警分组规则。 - 当通知类型为“alarm_policy”时：true - 当通知类型为“direct”时：false 如果告警触发“notify_triggered”或告警恢复“notify_resolved”都设置为false（即都不进行告警通知），则route_group_enable需设置为false。

        :param route_group_enable: The route_group_enable of this BatchUpdateActionRules.
        :type route_group_enable: bool
        """
        self._route_group_enable = route_group_enable

    @property
    def route_group_rule(self):
        r"""Gets the route_group_rule of this BatchUpdateActionRules.

        告警分组规则名称。 - 当route_group_enable 为true时，填告警分组规则名称 - 当route_group_enable 为false时，填“”

        :return: The route_group_rule of this BatchUpdateActionRules.
        :rtype: str
        """
        return self._route_group_rule

    @route_group_rule.setter
    def route_group_rule(self, route_group_rule):
        r"""Sets the route_group_rule of this BatchUpdateActionRules.

        告警分组规则名称。 - 当route_group_enable 为true时，填告警分组规则名称 - 当route_group_enable 为false时，填“”

        :param route_group_rule: The route_group_rule of this BatchUpdateActionRules.
        :type route_group_rule: str
        """
        self._route_group_rule = route_group_rule

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
        if not isinstance(other, BatchUpdateActionRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
