# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateOneClickAlarmNotificationsRequestBody:

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
        'alarm_notifications': 'list[Notification]',
        'ok_notifications': 'list[Notification]',
        'notification_begin_time': 'str',
        'notification_end_time': 'str',
        'notification_manner': 'str',
        'notification_policy_ids': 'list[str]'
    }

    attribute_map = {
        'notification_enabled': 'notification_enabled',
        'alarm_notifications': 'alarm_notifications',
        'ok_notifications': 'ok_notifications',
        'notification_begin_time': 'notification_begin_time',
        'notification_end_time': 'notification_end_time',
        'notification_manner': 'notification_manner',
        'notification_policy_ids': 'notification_policy_ids'
    }

    def __init__(self, notification_enabled=None, alarm_notifications=None, ok_notifications=None, notification_begin_time=None, notification_end_time=None, notification_manner=None, notification_policy_ids=None):
        r"""UpdateOneClickAlarmNotificationsRequestBody

        The model defined in huaweicloud sdk

        :param notification_enabled: 是否开启告警通知。true:开启，false:关闭。
        :type notification_enabled: bool
        :param alarm_notifications: 告警触发的动作
        :type alarm_notifications: list[:class:`huaweicloudsdkces.v2.Notification`]
        :param ok_notifications: 告警恢复触发的动作
        :type ok_notifications: list[:class:`huaweicloudsdkces.v2.Notification`]
        :param notification_begin_time: 告警通知开启时间
        :type notification_begin_time: str
        :param notification_end_time: 告警通知关闭时间
        :type notification_end_time: str
        :param notification_manner: NOTIFICATION_GROUP(通知组)/TOPIC_SUBSCRIPTION(主题订阅)/NOTIFICATION_POLICY(通知策略)
        :type notification_manner: str
        :param notification_policy_ids: 关联的通知策略ID列表
        :type notification_policy_ids: list[str]
        """
        
        

        self._notification_enabled = None
        self._alarm_notifications = None
        self._ok_notifications = None
        self._notification_begin_time = None
        self._notification_end_time = None
        self._notification_manner = None
        self._notification_policy_ids = None
        self.discriminator = None

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
    def notification_enabled(self):
        r"""Gets the notification_enabled of this UpdateOneClickAlarmNotificationsRequestBody.

        是否开启告警通知。true:开启，false:关闭。

        :return: The notification_enabled of this UpdateOneClickAlarmNotificationsRequestBody.
        :rtype: bool
        """
        return self._notification_enabled

    @notification_enabled.setter
    def notification_enabled(self, notification_enabled):
        r"""Sets the notification_enabled of this UpdateOneClickAlarmNotificationsRequestBody.

        是否开启告警通知。true:开启，false:关闭。

        :param notification_enabled: The notification_enabled of this UpdateOneClickAlarmNotificationsRequestBody.
        :type notification_enabled: bool
        """
        self._notification_enabled = notification_enabled

    @property
    def alarm_notifications(self):
        r"""Gets the alarm_notifications of this UpdateOneClickAlarmNotificationsRequestBody.

        告警触发的动作

        :return: The alarm_notifications of this UpdateOneClickAlarmNotificationsRequestBody.
        :rtype: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        return self._alarm_notifications

    @alarm_notifications.setter
    def alarm_notifications(self, alarm_notifications):
        r"""Sets the alarm_notifications of this UpdateOneClickAlarmNotificationsRequestBody.

        告警触发的动作

        :param alarm_notifications: The alarm_notifications of this UpdateOneClickAlarmNotificationsRequestBody.
        :type alarm_notifications: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        self._alarm_notifications = alarm_notifications

    @property
    def ok_notifications(self):
        r"""Gets the ok_notifications of this UpdateOneClickAlarmNotificationsRequestBody.

        告警恢复触发的动作

        :return: The ok_notifications of this UpdateOneClickAlarmNotificationsRequestBody.
        :rtype: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        return self._ok_notifications

    @ok_notifications.setter
    def ok_notifications(self, ok_notifications):
        r"""Sets the ok_notifications of this UpdateOneClickAlarmNotificationsRequestBody.

        告警恢复触发的动作

        :param ok_notifications: The ok_notifications of this UpdateOneClickAlarmNotificationsRequestBody.
        :type ok_notifications: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        self._ok_notifications = ok_notifications

    @property
    def notification_begin_time(self):
        r"""Gets the notification_begin_time of this UpdateOneClickAlarmNotificationsRequestBody.

        告警通知开启时间

        :return: The notification_begin_time of this UpdateOneClickAlarmNotificationsRequestBody.
        :rtype: str
        """
        return self._notification_begin_time

    @notification_begin_time.setter
    def notification_begin_time(self, notification_begin_time):
        r"""Sets the notification_begin_time of this UpdateOneClickAlarmNotificationsRequestBody.

        告警通知开启时间

        :param notification_begin_time: The notification_begin_time of this UpdateOneClickAlarmNotificationsRequestBody.
        :type notification_begin_time: str
        """
        self._notification_begin_time = notification_begin_time

    @property
    def notification_end_time(self):
        r"""Gets the notification_end_time of this UpdateOneClickAlarmNotificationsRequestBody.

        告警通知关闭时间

        :return: The notification_end_time of this UpdateOneClickAlarmNotificationsRequestBody.
        :rtype: str
        """
        return self._notification_end_time

    @notification_end_time.setter
    def notification_end_time(self, notification_end_time):
        r"""Sets the notification_end_time of this UpdateOneClickAlarmNotificationsRequestBody.

        告警通知关闭时间

        :param notification_end_time: The notification_end_time of this UpdateOneClickAlarmNotificationsRequestBody.
        :type notification_end_time: str
        """
        self._notification_end_time = notification_end_time

    @property
    def notification_manner(self):
        r"""Gets the notification_manner of this UpdateOneClickAlarmNotificationsRequestBody.

        NOTIFICATION_GROUP(通知组)/TOPIC_SUBSCRIPTION(主题订阅)/NOTIFICATION_POLICY(通知策略)

        :return: The notification_manner of this UpdateOneClickAlarmNotificationsRequestBody.
        :rtype: str
        """
        return self._notification_manner

    @notification_manner.setter
    def notification_manner(self, notification_manner):
        r"""Sets the notification_manner of this UpdateOneClickAlarmNotificationsRequestBody.

        NOTIFICATION_GROUP(通知组)/TOPIC_SUBSCRIPTION(主题订阅)/NOTIFICATION_POLICY(通知策略)

        :param notification_manner: The notification_manner of this UpdateOneClickAlarmNotificationsRequestBody.
        :type notification_manner: str
        """
        self._notification_manner = notification_manner

    @property
    def notification_policy_ids(self):
        r"""Gets the notification_policy_ids of this UpdateOneClickAlarmNotificationsRequestBody.

        关联的通知策略ID列表

        :return: The notification_policy_ids of this UpdateOneClickAlarmNotificationsRequestBody.
        :rtype: list[str]
        """
        return self._notification_policy_ids

    @notification_policy_ids.setter
    def notification_policy_ids(self, notification_policy_ids):
        r"""Sets the notification_policy_ids of this UpdateOneClickAlarmNotificationsRequestBody.

        关联的通知策略ID列表

        :param notification_policy_ids: The notification_policy_ids of this UpdateOneClickAlarmNotificationsRequestBody.
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
        if not isinstance(other, UpdateOneClickAlarmNotificationsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
