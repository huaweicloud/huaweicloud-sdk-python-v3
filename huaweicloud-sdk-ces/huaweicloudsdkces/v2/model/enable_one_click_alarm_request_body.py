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
        'notification_end_time': 'str'
    }

    attribute_map = {
        'one_click_alarm_id': 'one_click_alarm_id',
        'dimension_names': 'dimension_names',
        'notification_enabled': 'notification_enabled',
        'alarm_notifications': 'alarm_notifications',
        'ok_notifications': 'ok_notifications',
        'notification_begin_time': 'notification_begin_time',
        'notification_end_time': 'notification_end_time'
    }

    def __init__(self, one_click_alarm_id=None, dimension_names=None, notification_enabled=None, alarm_notifications=None, ok_notifications=None, notification_begin_time=None, notification_end_time=None):
        """EnableOneClickAlarmRequestBody

        The model defined in huaweicloud sdk

        :param one_click_alarm_id: 一键告警ID
        :type one_click_alarm_id: str
        :param dimension_names: 
        :type dimension_names: :class:`huaweicloudsdkces.v2.DimensionNames`
        :param notification_enabled: 是否开启告警通知
        :type notification_enabled: bool
        :param alarm_notifications: 告警触发的动作
        :type alarm_notifications: list[:class:`huaweicloudsdkces.v2.Notification`]
        :param ok_notifications: 告警恢复触发的动作
        :type ok_notifications: list[:class:`huaweicloudsdkces.v2.Notification`]
        :param notification_begin_time: 告警通知开启时间
        :type notification_begin_time: str
        :param notification_end_time: 告警通知关闭时间
        :type notification_end_time: str
        """
        
        

        self._one_click_alarm_id = None
        self._dimension_names = None
        self._notification_enabled = None
        self._alarm_notifications = None
        self._ok_notifications = None
        self._notification_begin_time = None
        self._notification_end_time = None
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

    @property
    def one_click_alarm_id(self):
        """Gets the one_click_alarm_id of this EnableOneClickAlarmRequestBody.

        一键告警ID

        :return: The one_click_alarm_id of this EnableOneClickAlarmRequestBody.
        :rtype: str
        """
        return self._one_click_alarm_id

    @one_click_alarm_id.setter
    def one_click_alarm_id(self, one_click_alarm_id):
        """Sets the one_click_alarm_id of this EnableOneClickAlarmRequestBody.

        一键告警ID

        :param one_click_alarm_id: The one_click_alarm_id of this EnableOneClickAlarmRequestBody.
        :type one_click_alarm_id: str
        """
        self._one_click_alarm_id = one_click_alarm_id

    @property
    def dimension_names(self):
        """Gets the dimension_names of this EnableOneClickAlarmRequestBody.

        :return: The dimension_names of this EnableOneClickAlarmRequestBody.
        :rtype: :class:`huaweicloudsdkces.v2.DimensionNames`
        """
        return self._dimension_names

    @dimension_names.setter
    def dimension_names(self, dimension_names):
        """Sets the dimension_names of this EnableOneClickAlarmRequestBody.

        :param dimension_names: The dimension_names of this EnableOneClickAlarmRequestBody.
        :type dimension_names: :class:`huaweicloudsdkces.v2.DimensionNames`
        """
        self._dimension_names = dimension_names

    @property
    def notification_enabled(self):
        """Gets the notification_enabled of this EnableOneClickAlarmRequestBody.

        是否开启告警通知

        :return: The notification_enabled of this EnableOneClickAlarmRequestBody.
        :rtype: bool
        """
        return self._notification_enabled

    @notification_enabled.setter
    def notification_enabled(self, notification_enabled):
        """Sets the notification_enabled of this EnableOneClickAlarmRequestBody.

        是否开启告警通知

        :param notification_enabled: The notification_enabled of this EnableOneClickAlarmRequestBody.
        :type notification_enabled: bool
        """
        self._notification_enabled = notification_enabled

    @property
    def alarm_notifications(self):
        """Gets the alarm_notifications of this EnableOneClickAlarmRequestBody.

        告警触发的动作

        :return: The alarm_notifications of this EnableOneClickAlarmRequestBody.
        :rtype: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        return self._alarm_notifications

    @alarm_notifications.setter
    def alarm_notifications(self, alarm_notifications):
        """Sets the alarm_notifications of this EnableOneClickAlarmRequestBody.

        告警触发的动作

        :param alarm_notifications: The alarm_notifications of this EnableOneClickAlarmRequestBody.
        :type alarm_notifications: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        self._alarm_notifications = alarm_notifications

    @property
    def ok_notifications(self):
        """Gets the ok_notifications of this EnableOneClickAlarmRequestBody.

        告警恢复触发的动作

        :return: The ok_notifications of this EnableOneClickAlarmRequestBody.
        :rtype: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        return self._ok_notifications

    @ok_notifications.setter
    def ok_notifications(self, ok_notifications):
        """Sets the ok_notifications of this EnableOneClickAlarmRequestBody.

        告警恢复触发的动作

        :param ok_notifications: The ok_notifications of this EnableOneClickAlarmRequestBody.
        :type ok_notifications: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        self._ok_notifications = ok_notifications

    @property
    def notification_begin_time(self):
        """Gets the notification_begin_time of this EnableOneClickAlarmRequestBody.

        告警通知开启时间

        :return: The notification_begin_time of this EnableOneClickAlarmRequestBody.
        :rtype: str
        """
        return self._notification_begin_time

    @notification_begin_time.setter
    def notification_begin_time(self, notification_begin_time):
        """Sets the notification_begin_time of this EnableOneClickAlarmRequestBody.

        告警通知开启时间

        :param notification_begin_time: The notification_begin_time of this EnableOneClickAlarmRequestBody.
        :type notification_begin_time: str
        """
        self._notification_begin_time = notification_begin_time

    @property
    def notification_end_time(self):
        """Gets the notification_end_time of this EnableOneClickAlarmRequestBody.

        告警通知关闭时间

        :return: The notification_end_time of this EnableOneClickAlarmRequestBody.
        :rtype: str
        """
        return self._notification_end_time

    @notification_end_time.setter
    def notification_end_time(self, notification_end_time):
        """Sets the notification_end_time of this EnableOneClickAlarmRequestBody.

        告警通知关闭时间

        :param notification_end_time: The notification_end_time of this EnableOneClickAlarmRequestBody.
        :type notification_end_time: str
        """
        self._notification_end_time = notification_end_time

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
