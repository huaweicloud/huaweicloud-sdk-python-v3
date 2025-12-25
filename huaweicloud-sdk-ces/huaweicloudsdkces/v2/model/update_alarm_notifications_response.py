# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAlarmNotificationsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'notification_enabled': 'bool',
        'alarm_notifications': 'list[NotificationResp]',
        'ok_notifications': 'list[NotificationResp]',
        'notification_begin_time': 'str',
        'notification_end_time': 'str',
        'effective_timezone': 'str',
        'notification_manner': 'str',
        'notification_policy_ids': 'list[str]'
    }

    attribute_map = {
        'notification_enabled': 'notification_enabled',
        'alarm_notifications': 'alarm_notifications',
        'ok_notifications': 'ok_notifications',
        'notification_begin_time': 'notification_begin_time',
        'notification_end_time': 'notification_end_time',
        'effective_timezone': 'effective_timezone',
        'notification_manner': 'notification_manner',
        'notification_policy_ids': 'notification_policy_ids'
    }

    def __init__(self, notification_enabled=None, alarm_notifications=None, ok_notifications=None, notification_begin_time=None, notification_end_time=None, effective_timezone=None, notification_manner=None, notification_policy_ids=None):
        r"""UpdateAlarmNotificationsResponse

        The model defined in huaweicloud sdk

        :param notification_enabled: **参数解释**： 是否开启告警通知。     **取值范围**： 布尔值。 - true:开启。 - false:关闭。 
        :type notification_enabled: bool
        :param alarm_notifications: **参数解释**： 触发告警时，通知组/主题订阅的信息。 
        :type alarm_notifications: list[:class:`huaweicloudsdkces.v2.NotificationResp`]
        :param ok_notifications: **参数解释**： 告警恢复时，通知组/主题订阅的信息。 
        :type ok_notifications: list[:class:`huaweicloudsdkces.v2.NotificationResp`]
        :param notification_begin_time: **参数解释**： 告警通知开启时间。如 00:00    **取值范围**： 只能包含数字、“:”，长度为[1,64]个字符。 
        :type notification_begin_time: str
        :param notification_end_time: **参数解释**： 告警通知关闭时间。如 08:00   **取值范围**： 只能包含数字、“:”，长度为[1,64]个字符。 
        :type notification_end_time: str
        :param effective_timezone: **参数解释**： 时区，形如：\&quot;GMT-08:00\&quot;、\&quot;GMT+08:00\&quot;、\&quot;GMT+0:00\&quot;。    **取值范围**： 长度为[1,16]个字符。 
        :type effective_timezone: str
        :param notification_manner: **参数解释**： 告警的通知方式 **取值范围**： - NOTIFICATION_GROUP: 通知组 - TOPIC_SUBSCRIPTION: 主题订阅 - NOTIFICATION_POLICY：通知策略 
        :type notification_manner: str
        :param notification_policy_ids: **参数解释**： 关联的通知策略ID列表 
        :type notification_policy_ids: list[str]
        """
        
        super().__init__()

        self._notification_enabled = None
        self._alarm_notifications = None
        self._ok_notifications = None
        self._notification_begin_time = None
        self._notification_end_time = None
        self._effective_timezone = None
        self._notification_manner = None
        self._notification_policy_ids = None
        self.discriminator = None

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
        if effective_timezone is not None:
            self.effective_timezone = effective_timezone
        if notification_manner is not None:
            self.notification_manner = notification_manner
        if notification_policy_ids is not None:
            self.notification_policy_ids = notification_policy_ids

    @property
    def notification_enabled(self):
        r"""Gets the notification_enabled of this UpdateAlarmNotificationsResponse.

        **参数解释**： 是否开启告警通知。     **取值范围**： 布尔值。 - true:开启。 - false:关闭。 

        :return: The notification_enabled of this UpdateAlarmNotificationsResponse.
        :rtype: bool
        """
        return self._notification_enabled

    @notification_enabled.setter
    def notification_enabled(self, notification_enabled):
        r"""Sets the notification_enabled of this UpdateAlarmNotificationsResponse.

        **参数解释**： 是否开启告警通知。     **取值范围**： 布尔值。 - true:开启。 - false:关闭。 

        :param notification_enabled: The notification_enabled of this UpdateAlarmNotificationsResponse.
        :type notification_enabled: bool
        """
        self._notification_enabled = notification_enabled

    @property
    def alarm_notifications(self):
        r"""Gets the alarm_notifications of this UpdateAlarmNotificationsResponse.

        **参数解释**： 触发告警时，通知组/主题订阅的信息。 

        :return: The alarm_notifications of this UpdateAlarmNotificationsResponse.
        :rtype: list[:class:`huaweicloudsdkces.v2.NotificationResp`]
        """
        return self._alarm_notifications

    @alarm_notifications.setter
    def alarm_notifications(self, alarm_notifications):
        r"""Sets the alarm_notifications of this UpdateAlarmNotificationsResponse.

        **参数解释**： 触发告警时，通知组/主题订阅的信息。 

        :param alarm_notifications: The alarm_notifications of this UpdateAlarmNotificationsResponse.
        :type alarm_notifications: list[:class:`huaweicloudsdkces.v2.NotificationResp`]
        """
        self._alarm_notifications = alarm_notifications

    @property
    def ok_notifications(self):
        r"""Gets the ok_notifications of this UpdateAlarmNotificationsResponse.

        **参数解释**： 告警恢复时，通知组/主题订阅的信息。 

        :return: The ok_notifications of this UpdateAlarmNotificationsResponse.
        :rtype: list[:class:`huaweicloudsdkces.v2.NotificationResp`]
        """
        return self._ok_notifications

    @ok_notifications.setter
    def ok_notifications(self, ok_notifications):
        r"""Sets the ok_notifications of this UpdateAlarmNotificationsResponse.

        **参数解释**： 告警恢复时，通知组/主题订阅的信息。 

        :param ok_notifications: The ok_notifications of this UpdateAlarmNotificationsResponse.
        :type ok_notifications: list[:class:`huaweicloudsdkces.v2.NotificationResp`]
        """
        self._ok_notifications = ok_notifications

    @property
    def notification_begin_time(self):
        r"""Gets the notification_begin_time of this UpdateAlarmNotificationsResponse.

        **参数解释**： 告警通知开启时间。如 00:00    **取值范围**： 只能包含数字、“:”，长度为[1,64]个字符。 

        :return: The notification_begin_time of this UpdateAlarmNotificationsResponse.
        :rtype: str
        """
        return self._notification_begin_time

    @notification_begin_time.setter
    def notification_begin_time(self, notification_begin_time):
        r"""Sets the notification_begin_time of this UpdateAlarmNotificationsResponse.

        **参数解释**： 告警通知开启时间。如 00:00    **取值范围**： 只能包含数字、“:”，长度为[1,64]个字符。 

        :param notification_begin_time: The notification_begin_time of this UpdateAlarmNotificationsResponse.
        :type notification_begin_time: str
        """
        self._notification_begin_time = notification_begin_time

    @property
    def notification_end_time(self):
        r"""Gets the notification_end_time of this UpdateAlarmNotificationsResponse.

        **参数解释**： 告警通知关闭时间。如 08:00   **取值范围**： 只能包含数字、“:”，长度为[1,64]个字符。 

        :return: The notification_end_time of this UpdateAlarmNotificationsResponse.
        :rtype: str
        """
        return self._notification_end_time

    @notification_end_time.setter
    def notification_end_time(self, notification_end_time):
        r"""Sets the notification_end_time of this UpdateAlarmNotificationsResponse.

        **参数解释**： 告警通知关闭时间。如 08:00   **取值范围**： 只能包含数字、“:”，长度为[1,64]个字符。 

        :param notification_end_time: The notification_end_time of this UpdateAlarmNotificationsResponse.
        :type notification_end_time: str
        """
        self._notification_end_time = notification_end_time

    @property
    def effective_timezone(self):
        r"""Gets the effective_timezone of this UpdateAlarmNotificationsResponse.

        **参数解释**： 时区，形如：\"GMT-08:00\"、\"GMT+08:00\"、\"GMT+0:00\"。    **取值范围**： 长度为[1,16]个字符。 

        :return: The effective_timezone of this UpdateAlarmNotificationsResponse.
        :rtype: str
        """
        return self._effective_timezone

    @effective_timezone.setter
    def effective_timezone(self, effective_timezone):
        r"""Sets the effective_timezone of this UpdateAlarmNotificationsResponse.

        **参数解释**： 时区，形如：\"GMT-08:00\"、\"GMT+08:00\"、\"GMT+0:00\"。    **取值范围**： 长度为[1,16]个字符。 

        :param effective_timezone: The effective_timezone of this UpdateAlarmNotificationsResponse.
        :type effective_timezone: str
        """
        self._effective_timezone = effective_timezone

    @property
    def notification_manner(self):
        r"""Gets the notification_manner of this UpdateAlarmNotificationsResponse.

        **参数解释**： 告警的通知方式 **取值范围**： - NOTIFICATION_GROUP: 通知组 - TOPIC_SUBSCRIPTION: 主题订阅 - NOTIFICATION_POLICY：通知策略 

        :return: The notification_manner of this UpdateAlarmNotificationsResponse.
        :rtype: str
        """
        return self._notification_manner

    @notification_manner.setter
    def notification_manner(self, notification_manner):
        r"""Sets the notification_manner of this UpdateAlarmNotificationsResponse.

        **参数解释**： 告警的通知方式 **取值范围**： - NOTIFICATION_GROUP: 通知组 - TOPIC_SUBSCRIPTION: 主题订阅 - NOTIFICATION_POLICY：通知策略 

        :param notification_manner: The notification_manner of this UpdateAlarmNotificationsResponse.
        :type notification_manner: str
        """
        self._notification_manner = notification_manner

    @property
    def notification_policy_ids(self):
        r"""Gets the notification_policy_ids of this UpdateAlarmNotificationsResponse.

        **参数解释**： 关联的通知策略ID列表 

        :return: The notification_policy_ids of this UpdateAlarmNotificationsResponse.
        :rtype: list[str]
        """
        return self._notification_policy_ids

    @notification_policy_ids.setter
    def notification_policy_ids(self, notification_policy_ids):
        r"""Sets the notification_policy_ids of this UpdateAlarmNotificationsResponse.

        **参数解释**： 关联的通知策略ID列表 

        :param notification_policy_ids: The notification_policy_ids of this UpdateAlarmNotificationsResponse.
        :type notification_policy_ids: list[str]
        """
        self._notification_policy_ids = notification_policy_ids

    def to_dict(self):
        import warnings
        warnings.warn("UpdateAlarmNotificationsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, UpdateAlarmNotificationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
