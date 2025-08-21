# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnableOneClickAlarmRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'one_click_alarm_id': 'str',
        'dimension_names': 'DimensionNames',
        'notification_enabled': 'bool',
        'alarm_notifications': 'list[Notification]',
        'ok_notifications': 'list[Notification]',
        'notification_begin_time': 'str',
        'notification_end_time': 'str',
        'effective_timezone': 'str',
        'notification_manner': 'str',
        'notification_policy_ids': 'list[str]',
        'is_reset': 'bool',
        'one_click_update_alarms': 'list[EnableOneClickAlarmRequestBodyOneClickUpdateAlarms]'
    }

    attribute_map = {
        'one_click_alarm_id': 'one_click_alarm_id',
        'dimension_names': 'dimension_names',
        'notification_enabled': 'notification_enabled',
        'alarm_notifications': 'alarm_notifications',
        'ok_notifications': 'ok_notifications',
        'notification_begin_time': 'notification_begin_time',
        'notification_end_time': 'notification_end_time',
        'effective_timezone': 'effective_timezone',
        'notification_manner': 'notification_manner',
        'notification_policy_ids': 'notification_policy_ids',
        'is_reset': 'is_reset',
        'one_click_update_alarms': 'one_click_update_alarms'
    }

    def __init__(self, one_click_alarm_id=None, dimension_names=None, notification_enabled=None, alarm_notifications=None, ok_notifications=None, notification_begin_time=None, notification_end_time=None, effective_timezone=None, notification_manner=None, notification_policy_ids=None, is_reset=None, one_click_update_alarms=None):
        r"""EnableOneClickAlarmRequestBody

        The model defined in huaweicloud sdk

        :param one_click_alarm_id: 一键告警ID
        :type one_click_alarm_id: str
        :param dimension_names: 
        :type dimension_names: :class:`huaweicloudsdkces.v2.DimensionNames`
        :param notification_enabled: 是否开启告警通知。true:开启，false:关闭。
        :type notification_enabled: bool
        :param alarm_notifications: **参数解释**： 触发告警时，通知组/主题订阅的信息。 **约束限制**： 不涉及。 **取值范围**： 告警触发的动作数量最多为10个。 **默认取值**： 不涉及。 
        :type alarm_notifications: list[:class:`huaweicloudsdkces.v2.Notification`]
        :param ok_notifications: **参数解释**： 告警恢复时，通知组/主题订阅的信息。 **约束限制**： 不涉及。 **取值范围**： 告警恢复触发的动作数量最多为10个。 **默认取值**： 不涉及。 
        :type ok_notifications: list[:class:`huaweicloudsdkces.v2.Notification`]
        :param notification_begin_time: **参数解释**： 每天告警通知的开始时间。 **约束限制**： 不涉及。 **取值范围**： 长度为[1,64]个字符。 **默认取值**： 不涉及。 
        :type notification_begin_time: str
        :param notification_end_time: **参数解释**： 每天告警通知的结束时间。 **约束限制**： 不涉及。 **取值范围**： 长度为[1,64]个字符。 **默认取值**： 不涉及。 
        :type notification_end_time: str
        :param effective_timezone: 时区，形如：\&quot;GMT-08:00\&quot;、\&quot;GMT+08:00\&quot;、\&quot;GMT+0:00\&quot;
        :type effective_timezone: str
        :param notification_manner: NOTIFICATION_GROUP(通知组)/TOPIC_SUBSCRIPTION(主题订阅)/NOTIFICATION_POLICY(通知策略)
        :type notification_manner: str
        :param notification_policy_ids: 关联的通知策略ID列表
        :type notification_policy_ids: list[str]
        :param is_reset: 是否以默认一键告警规则重置创建
        :type is_reset: bool
        :param one_click_update_alarms: 打开一键告警需要同时修改告警策略及通知(当前仅支持通知策略修改)时传递的参数
        :type one_click_update_alarms: list[:class:`huaweicloudsdkces.v2.EnableOneClickAlarmRequestBodyOneClickUpdateAlarms`]
        """
        
        

        self._one_click_alarm_id = None
        self._dimension_names = None
        self._notification_enabled = None
        self._alarm_notifications = None
        self._ok_notifications = None
        self._notification_begin_time = None
        self._notification_end_time = None
        self._effective_timezone = None
        self._notification_manner = None
        self._notification_policy_ids = None
        self._is_reset = None
        self._one_click_update_alarms = None
        self.discriminator = None

        self.one_click_alarm_id = one_click_alarm_id
        self.dimension_names = dimension_names
        self.notification_enabled = notification_enabled
        if alarm_notifications is not None:
            self.alarm_notifications = alarm_notifications
        if ok_notifications is not None:
            self.ok_notifications = ok_notifications
        if notification_begin_time is not None:
            self.notification_begin_time = notification_begin_time
        if notification_end_time is not None:
            self.notification_end_time = notification_end_time
        if effective_timezone is not None:
            self.effective_timezone = effective_timezone
        if notification_manner is not None:
            self.notification_manner = notification_manner
        if notification_policy_ids is not None:
            self.notification_policy_ids = notification_policy_ids
        if is_reset is not None:
            self.is_reset = is_reset
        if one_click_update_alarms is not None:
            self.one_click_update_alarms = one_click_update_alarms

    @property
    def one_click_alarm_id(self):
        r"""Gets the one_click_alarm_id of this EnableOneClickAlarmRequestBody.

        一键告警ID

        :return: The one_click_alarm_id of this EnableOneClickAlarmRequestBody.
        :rtype: str
        """
        return self._one_click_alarm_id

    @one_click_alarm_id.setter
    def one_click_alarm_id(self, one_click_alarm_id):
        r"""Sets the one_click_alarm_id of this EnableOneClickAlarmRequestBody.

        一键告警ID

        :param one_click_alarm_id: The one_click_alarm_id of this EnableOneClickAlarmRequestBody.
        :type one_click_alarm_id: str
        """
        self._one_click_alarm_id = one_click_alarm_id

    @property
    def dimension_names(self):
        r"""Gets the dimension_names of this EnableOneClickAlarmRequestBody.

        :return: The dimension_names of this EnableOneClickAlarmRequestBody.
        :rtype: :class:`huaweicloudsdkces.v2.DimensionNames`
        """
        return self._dimension_names

    @dimension_names.setter
    def dimension_names(self, dimension_names):
        r"""Sets the dimension_names of this EnableOneClickAlarmRequestBody.

        :param dimension_names: The dimension_names of this EnableOneClickAlarmRequestBody.
        :type dimension_names: :class:`huaweicloudsdkces.v2.DimensionNames`
        """
        self._dimension_names = dimension_names

    @property
    def notification_enabled(self):
        r"""Gets the notification_enabled of this EnableOneClickAlarmRequestBody.

        是否开启告警通知。true:开启，false:关闭。

        :return: The notification_enabled of this EnableOneClickAlarmRequestBody.
        :rtype: bool
        """
        return self._notification_enabled

    @notification_enabled.setter
    def notification_enabled(self, notification_enabled):
        r"""Sets the notification_enabled of this EnableOneClickAlarmRequestBody.

        是否开启告警通知。true:开启，false:关闭。

        :param notification_enabled: The notification_enabled of this EnableOneClickAlarmRequestBody.
        :type notification_enabled: bool
        """
        self._notification_enabled = notification_enabled

    @property
    def alarm_notifications(self):
        r"""Gets the alarm_notifications of this EnableOneClickAlarmRequestBody.

        **参数解释**： 触发告警时，通知组/主题订阅的信息。 **约束限制**： 不涉及。 **取值范围**： 告警触发的动作数量最多为10个。 **默认取值**： 不涉及。 

        :return: The alarm_notifications of this EnableOneClickAlarmRequestBody.
        :rtype: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        return self._alarm_notifications

    @alarm_notifications.setter
    def alarm_notifications(self, alarm_notifications):
        r"""Sets the alarm_notifications of this EnableOneClickAlarmRequestBody.

        **参数解释**： 触发告警时，通知组/主题订阅的信息。 **约束限制**： 不涉及。 **取值范围**： 告警触发的动作数量最多为10个。 **默认取值**： 不涉及。 

        :param alarm_notifications: The alarm_notifications of this EnableOneClickAlarmRequestBody.
        :type alarm_notifications: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        self._alarm_notifications = alarm_notifications

    @property
    def ok_notifications(self):
        r"""Gets the ok_notifications of this EnableOneClickAlarmRequestBody.

        **参数解释**： 告警恢复时，通知组/主题订阅的信息。 **约束限制**： 不涉及。 **取值范围**： 告警恢复触发的动作数量最多为10个。 **默认取值**： 不涉及。 

        :return: The ok_notifications of this EnableOneClickAlarmRequestBody.
        :rtype: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        return self._ok_notifications

    @ok_notifications.setter
    def ok_notifications(self, ok_notifications):
        r"""Sets the ok_notifications of this EnableOneClickAlarmRequestBody.

        **参数解释**： 告警恢复时，通知组/主题订阅的信息。 **约束限制**： 不涉及。 **取值范围**： 告警恢复触发的动作数量最多为10个。 **默认取值**： 不涉及。 

        :param ok_notifications: The ok_notifications of this EnableOneClickAlarmRequestBody.
        :type ok_notifications: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        self._ok_notifications = ok_notifications

    @property
    def notification_begin_time(self):
        r"""Gets the notification_begin_time of this EnableOneClickAlarmRequestBody.

        **参数解释**： 每天告警通知的开始时间。 **约束限制**： 不涉及。 **取值范围**： 长度为[1,64]个字符。 **默认取值**： 不涉及。 

        :return: The notification_begin_time of this EnableOneClickAlarmRequestBody.
        :rtype: str
        """
        return self._notification_begin_time

    @notification_begin_time.setter
    def notification_begin_time(self, notification_begin_time):
        r"""Sets the notification_begin_time of this EnableOneClickAlarmRequestBody.

        **参数解释**： 每天告警通知的开始时间。 **约束限制**： 不涉及。 **取值范围**： 长度为[1,64]个字符。 **默认取值**： 不涉及。 

        :param notification_begin_time: The notification_begin_time of this EnableOneClickAlarmRequestBody.
        :type notification_begin_time: str
        """
        self._notification_begin_time = notification_begin_time

    @property
    def notification_end_time(self):
        r"""Gets the notification_end_time of this EnableOneClickAlarmRequestBody.

        **参数解释**： 每天告警通知的结束时间。 **约束限制**： 不涉及。 **取值范围**： 长度为[1,64]个字符。 **默认取值**： 不涉及。 

        :return: The notification_end_time of this EnableOneClickAlarmRequestBody.
        :rtype: str
        """
        return self._notification_end_time

    @notification_end_time.setter
    def notification_end_time(self, notification_end_time):
        r"""Sets the notification_end_time of this EnableOneClickAlarmRequestBody.

        **参数解释**： 每天告警通知的结束时间。 **约束限制**： 不涉及。 **取值范围**： 长度为[1,64]个字符。 **默认取值**： 不涉及。 

        :param notification_end_time: The notification_end_time of this EnableOneClickAlarmRequestBody.
        :type notification_end_time: str
        """
        self._notification_end_time = notification_end_time

    @property
    def effective_timezone(self):
        r"""Gets the effective_timezone of this EnableOneClickAlarmRequestBody.

        时区，形如：\"GMT-08:00\"、\"GMT+08:00\"、\"GMT+0:00\"

        :return: The effective_timezone of this EnableOneClickAlarmRequestBody.
        :rtype: str
        """
        return self._effective_timezone

    @effective_timezone.setter
    def effective_timezone(self, effective_timezone):
        r"""Sets the effective_timezone of this EnableOneClickAlarmRequestBody.

        时区，形如：\"GMT-08:00\"、\"GMT+08:00\"、\"GMT+0:00\"

        :param effective_timezone: The effective_timezone of this EnableOneClickAlarmRequestBody.
        :type effective_timezone: str
        """
        self._effective_timezone = effective_timezone

    @property
    def notification_manner(self):
        r"""Gets the notification_manner of this EnableOneClickAlarmRequestBody.

        NOTIFICATION_GROUP(通知组)/TOPIC_SUBSCRIPTION(主题订阅)/NOTIFICATION_POLICY(通知策略)

        :return: The notification_manner of this EnableOneClickAlarmRequestBody.
        :rtype: str
        """
        return self._notification_manner

    @notification_manner.setter
    def notification_manner(self, notification_manner):
        r"""Sets the notification_manner of this EnableOneClickAlarmRequestBody.

        NOTIFICATION_GROUP(通知组)/TOPIC_SUBSCRIPTION(主题订阅)/NOTIFICATION_POLICY(通知策略)

        :param notification_manner: The notification_manner of this EnableOneClickAlarmRequestBody.
        :type notification_manner: str
        """
        self._notification_manner = notification_manner

    @property
    def notification_policy_ids(self):
        r"""Gets the notification_policy_ids of this EnableOneClickAlarmRequestBody.

        关联的通知策略ID列表

        :return: The notification_policy_ids of this EnableOneClickAlarmRequestBody.
        :rtype: list[str]
        """
        return self._notification_policy_ids

    @notification_policy_ids.setter
    def notification_policy_ids(self, notification_policy_ids):
        r"""Sets the notification_policy_ids of this EnableOneClickAlarmRequestBody.

        关联的通知策略ID列表

        :param notification_policy_ids: The notification_policy_ids of this EnableOneClickAlarmRequestBody.
        :type notification_policy_ids: list[str]
        """
        self._notification_policy_ids = notification_policy_ids

    @property
    def is_reset(self):
        r"""Gets the is_reset of this EnableOneClickAlarmRequestBody.

        是否以默认一键告警规则重置创建

        :return: The is_reset of this EnableOneClickAlarmRequestBody.
        :rtype: bool
        """
        return self._is_reset

    @is_reset.setter
    def is_reset(self, is_reset):
        r"""Sets the is_reset of this EnableOneClickAlarmRequestBody.

        是否以默认一键告警规则重置创建

        :param is_reset: The is_reset of this EnableOneClickAlarmRequestBody.
        :type is_reset: bool
        """
        self._is_reset = is_reset

    @property
    def one_click_update_alarms(self):
        r"""Gets the one_click_update_alarms of this EnableOneClickAlarmRequestBody.

        打开一键告警需要同时修改告警策略及通知(当前仅支持通知策略修改)时传递的参数

        :return: The one_click_update_alarms of this EnableOneClickAlarmRequestBody.
        :rtype: list[:class:`huaweicloudsdkces.v2.EnableOneClickAlarmRequestBodyOneClickUpdateAlarms`]
        """
        return self._one_click_update_alarms

    @one_click_update_alarms.setter
    def one_click_update_alarms(self, one_click_update_alarms):
        r"""Sets the one_click_update_alarms of this EnableOneClickAlarmRequestBody.

        打开一键告警需要同时修改告警策略及通知(当前仅支持通知策略修改)时传递的参数

        :param one_click_update_alarms: The one_click_update_alarms of this EnableOneClickAlarmRequestBody.
        :type one_click_update_alarms: list[:class:`huaweicloudsdkces.v2.EnableOneClickAlarmRequestBodyOneClickUpdateAlarms`]
        """
        self._one_click_update_alarms = one_click_update_alarms

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
        if not isinstance(other, EnableOneClickAlarmRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
