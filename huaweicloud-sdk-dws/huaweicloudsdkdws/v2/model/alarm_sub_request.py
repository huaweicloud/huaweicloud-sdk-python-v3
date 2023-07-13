# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmSubRequest:

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
        'enable': 'int',
        'alarm_level': 'str',
        'notification_target': 'str',
        'notification_target_name': 'str',
        'notification_target_type': 'str',
        'time_zone': 'str'
    }

    attribute_map = {
        'name': 'name',
        'enable': 'enable',
        'alarm_level': 'alarm_level',
        'notification_target': 'notification_target',
        'notification_target_name': 'notification_target_name',
        'notification_target_type': 'notification_target_type',
        'time_zone': 'time_zone'
    }

    def __init__(self, name=None, enable=None, alarm_level=None, notification_target=None, notification_target_name=None, notification_target_type=None, time_zone=None):
        """AlarmSubRequest

        The model defined in huaweicloud sdk

        :param name: 告警订阅名称
        :type name: str
        :param enable: 是否开启订阅
        :type enable: int
        :param alarm_level: 告警级别
        :type alarm_level: str
        :param notification_target: 消息主题地址
        :type notification_target: str
        :param notification_target_name: 消息主题名称
        :type notification_target_name: str
        :param notification_target_type: 消息主题类型，支持SMN
        :type notification_target_type: str
        :param time_zone: 时区
        :type time_zone: str
        """
        
        

        self._name = None
        self._enable = None
        self._alarm_level = None
        self._notification_target = None
        self._notification_target_name = None
        self._notification_target_type = None
        self._time_zone = None
        self.discriminator = None

        self.name = name
        if enable is not None:
            self.enable = enable
        if alarm_level is not None:
            self.alarm_level = alarm_level
        self.notification_target = notification_target
        self.notification_target_name = notification_target_name
        self.notification_target_type = notification_target_type
        self.time_zone = time_zone

    @property
    def name(self):
        """Gets the name of this AlarmSubRequest.

        告警订阅名称

        :return: The name of this AlarmSubRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AlarmSubRequest.

        告警订阅名称

        :param name: The name of this AlarmSubRequest.
        :type name: str
        """
        self._name = name

    @property
    def enable(self):
        """Gets the enable of this AlarmSubRequest.

        是否开启订阅

        :return: The enable of this AlarmSubRequest.
        :rtype: int
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this AlarmSubRequest.

        是否开启订阅

        :param enable: The enable of this AlarmSubRequest.
        :type enable: int
        """
        self._enable = enable

    @property
    def alarm_level(self):
        """Gets the alarm_level of this AlarmSubRequest.

        告警级别

        :return: The alarm_level of this AlarmSubRequest.
        :rtype: str
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        """Sets the alarm_level of this AlarmSubRequest.

        告警级别

        :param alarm_level: The alarm_level of this AlarmSubRequest.
        :type alarm_level: str
        """
        self._alarm_level = alarm_level

    @property
    def notification_target(self):
        """Gets the notification_target of this AlarmSubRequest.

        消息主题地址

        :return: The notification_target of this AlarmSubRequest.
        :rtype: str
        """
        return self._notification_target

    @notification_target.setter
    def notification_target(self, notification_target):
        """Sets the notification_target of this AlarmSubRequest.

        消息主题地址

        :param notification_target: The notification_target of this AlarmSubRequest.
        :type notification_target: str
        """
        self._notification_target = notification_target

    @property
    def notification_target_name(self):
        """Gets the notification_target_name of this AlarmSubRequest.

        消息主题名称

        :return: The notification_target_name of this AlarmSubRequest.
        :rtype: str
        """
        return self._notification_target_name

    @notification_target_name.setter
    def notification_target_name(self, notification_target_name):
        """Sets the notification_target_name of this AlarmSubRequest.

        消息主题名称

        :param notification_target_name: The notification_target_name of this AlarmSubRequest.
        :type notification_target_name: str
        """
        self._notification_target_name = notification_target_name

    @property
    def notification_target_type(self):
        """Gets the notification_target_type of this AlarmSubRequest.

        消息主题类型，支持SMN

        :return: The notification_target_type of this AlarmSubRequest.
        :rtype: str
        """
        return self._notification_target_type

    @notification_target_type.setter
    def notification_target_type(self, notification_target_type):
        """Sets the notification_target_type of this AlarmSubRequest.

        消息主题类型，支持SMN

        :param notification_target_type: The notification_target_type of this AlarmSubRequest.
        :type notification_target_type: str
        """
        self._notification_target_type = notification_target_type

    @property
    def time_zone(self):
        """Gets the time_zone of this AlarmSubRequest.

        时区

        :return: The time_zone of this AlarmSubRequest.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this AlarmSubRequest.

        时区

        :param time_zone: The time_zone of this AlarmSubRequest.
        :type time_zone: str
        """
        self._time_zone = time_zone

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
        if not isinstance(other, AlarmSubRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
