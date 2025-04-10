# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlaTriggeringRuleInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'day': 'int',
        'hour': 'int',
        'minute': 'int',
        'protocol': 'str',
        'is_ongoing_notification': 'bool',
        'notification_interval': 'int',
        'notification_obj_configuration': 'list[NotificationObjConfiguration]'
    }

    attribute_map = {
        'day': 'day',
        'hour': 'hour',
        'minute': 'minute',
        'protocol': 'protocol',
        'is_ongoing_notification': 'is_ongoing_notification',
        'notification_interval': 'notification_interval',
        'notification_obj_configuration': 'notification_obj_configuration'
    }

    def __init__(self, day=None, hour=None, minute=None, protocol=None, is_ongoing_notification=None, notification_interval=None, notification_obj_configuration=None):
        r"""SlaTriggeringRuleInfo

        The model defined in huaweicloud sdk

        :param day: 天
        :type day: int
        :param hour: 小时
        :type hour: int
        :param minute: 分钟
        :type minute: int
        :param protocol: 通知类型
        :type protocol: str
        :param is_ongoing_notification: 是否持续通知
        :type is_ongoing_notification: bool
        :param notification_interval: 通知间隔
        :type notification_interval: int
        :param notification_obj_configuration: 通知配置
        :type notification_obj_configuration: list[:class:`huaweicloudsdkcoc.v1.NotificationObjConfiguration`]
        """
        
        

        self._day = None
        self._hour = None
        self._minute = None
        self._protocol = None
        self._is_ongoing_notification = None
        self._notification_interval = None
        self._notification_obj_configuration = None
        self.discriminator = None

        if day is not None:
            self.day = day
        if hour is not None:
            self.hour = hour
        if minute is not None:
            self.minute = minute
        if protocol is not None:
            self.protocol = protocol
        if is_ongoing_notification is not None:
            self.is_ongoing_notification = is_ongoing_notification
        if notification_interval is not None:
            self.notification_interval = notification_interval
        if notification_obj_configuration is not None:
            self.notification_obj_configuration = notification_obj_configuration

    @property
    def day(self):
        r"""Gets the day of this SlaTriggeringRuleInfo.

        天

        :return: The day of this SlaTriggeringRuleInfo.
        :rtype: int
        """
        return self._day

    @day.setter
    def day(self, day):
        r"""Sets the day of this SlaTriggeringRuleInfo.

        天

        :param day: The day of this SlaTriggeringRuleInfo.
        :type day: int
        """
        self._day = day

    @property
    def hour(self):
        r"""Gets the hour of this SlaTriggeringRuleInfo.

        小时

        :return: The hour of this SlaTriggeringRuleInfo.
        :rtype: int
        """
        return self._hour

    @hour.setter
    def hour(self, hour):
        r"""Sets the hour of this SlaTriggeringRuleInfo.

        小时

        :param hour: The hour of this SlaTriggeringRuleInfo.
        :type hour: int
        """
        self._hour = hour

    @property
    def minute(self):
        r"""Gets the minute of this SlaTriggeringRuleInfo.

        分钟

        :return: The minute of this SlaTriggeringRuleInfo.
        :rtype: int
        """
        return self._minute

    @minute.setter
    def minute(self, minute):
        r"""Sets the minute of this SlaTriggeringRuleInfo.

        分钟

        :param minute: The minute of this SlaTriggeringRuleInfo.
        :type minute: int
        """
        self._minute = minute

    @property
    def protocol(self):
        r"""Gets the protocol of this SlaTriggeringRuleInfo.

        通知类型

        :return: The protocol of this SlaTriggeringRuleInfo.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this SlaTriggeringRuleInfo.

        通知类型

        :param protocol: The protocol of this SlaTriggeringRuleInfo.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def is_ongoing_notification(self):
        r"""Gets the is_ongoing_notification of this SlaTriggeringRuleInfo.

        是否持续通知

        :return: The is_ongoing_notification of this SlaTriggeringRuleInfo.
        :rtype: bool
        """
        return self._is_ongoing_notification

    @is_ongoing_notification.setter
    def is_ongoing_notification(self, is_ongoing_notification):
        r"""Sets the is_ongoing_notification of this SlaTriggeringRuleInfo.

        是否持续通知

        :param is_ongoing_notification: The is_ongoing_notification of this SlaTriggeringRuleInfo.
        :type is_ongoing_notification: bool
        """
        self._is_ongoing_notification = is_ongoing_notification

    @property
    def notification_interval(self):
        r"""Gets the notification_interval of this SlaTriggeringRuleInfo.

        通知间隔

        :return: The notification_interval of this SlaTriggeringRuleInfo.
        :rtype: int
        """
        return self._notification_interval

    @notification_interval.setter
    def notification_interval(self, notification_interval):
        r"""Sets the notification_interval of this SlaTriggeringRuleInfo.

        通知间隔

        :param notification_interval: The notification_interval of this SlaTriggeringRuleInfo.
        :type notification_interval: int
        """
        self._notification_interval = notification_interval

    @property
    def notification_obj_configuration(self):
        r"""Gets the notification_obj_configuration of this SlaTriggeringRuleInfo.

        通知配置

        :return: The notification_obj_configuration of this SlaTriggeringRuleInfo.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.NotificationObjConfiguration`]
        """
        return self._notification_obj_configuration

    @notification_obj_configuration.setter
    def notification_obj_configuration(self, notification_obj_configuration):
        r"""Sets the notification_obj_configuration of this SlaTriggeringRuleInfo.

        通知配置

        :param notification_obj_configuration: The notification_obj_configuration of this SlaTriggeringRuleInfo.
        :type notification_obj_configuration: list[:class:`huaweicloudsdkcoc.v1.NotificationObjConfiguration`]
        """
        self._notification_obj_configuration = notification_obj_configuration

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
        if not isinstance(other, SlaTriggeringRuleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
