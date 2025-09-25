# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAlarmConfigRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_type': 'str',
        'display_name': 'str',
        'topic_urn': 'str',
        'daily_alarm': 'bool',
        'realtime_alarm': 'bool',
        'alarm_level': 'str',
        'ignored_event_class_list': 'list[str]'
    }

    attribute_map = {
        'alarm_type': 'alarm_type',
        'display_name': 'display_name',
        'topic_urn': 'topic_urn',
        'daily_alarm': 'daily_alarm',
        'realtime_alarm': 'realtime_alarm',
        'alarm_level': 'alarm_level',
        'ignored_event_class_list': 'ignored_event_class_list'
    }

    def __init__(self, alarm_type=None, display_name=None, topic_urn=None, daily_alarm=None, realtime_alarm=None, alarm_level=None, ignored_event_class_list=None):
        r"""UpdateAlarmConfigRequestInfo

        The model defined in huaweicloud sdk

        :param alarm_type: 告警类型
        :type alarm_type: str
        :param display_name: 显示名称
        :type display_name: str
        :param topic_urn: 是否发送短信
        :type topic_urn: str
        :param daily_alarm: 是否开启每日告警
        :type daily_alarm: bool
        :param realtime_alarm: 是否开启实时告警
        :type realtime_alarm: bool
        :param alarm_level: 告警等级
        :type alarm_level: str
        :param ignored_event_class_list: 忽略事件列表
        :type ignored_event_class_list: list[str]
        """
        
        

        self._alarm_type = None
        self._display_name = None
        self._topic_urn = None
        self._daily_alarm = None
        self._realtime_alarm = None
        self._alarm_level = None
        self._ignored_event_class_list = None
        self.discriminator = None

        if alarm_type is not None:
            self.alarm_type = alarm_type
        if display_name is not None:
            self.display_name = display_name
        if topic_urn is not None:
            self.topic_urn = topic_urn
        if daily_alarm is not None:
            self.daily_alarm = daily_alarm
        if realtime_alarm is not None:
            self.realtime_alarm = realtime_alarm
        if alarm_level is not None:
            self.alarm_level = alarm_level
        if ignored_event_class_list is not None:
            self.ignored_event_class_list = ignored_event_class_list

    @property
    def alarm_type(self):
        r"""Gets the alarm_type of this UpdateAlarmConfigRequestInfo.

        告警类型

        :return: The alarm_type of this UpdateAlarmConfigRequestInfo.
        :rtype: str
        """
        return self._alarm_type

    @alarm_type.setter
    def alarm_type(self, alarm_type):
        r"""Sets the alarm_type of this UpdateAlarmConfigRequestInfo.

        告警类型

        :param alarm_type: The alarm_type of this UpdateAlarmConfigRequestInfo.
        :type alarm_type: str
        """
        self._alarm_type = alarm_type

    @property
    def display_name(self):
        r"""Gets the display_name of this UpdateAlarmConfigRequestInfo.

        显示名称

        :return: The display_name of this UpdateAlarmConfigRequestInfo.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this UpdateAlarmConfigRequestInfo.

        显示名称

        :param display_name: The display_name of this UpdateAlarmConfigRequestInfo.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this UpdateAlarmConfigRequestInfo.

        是否发送短信

        :return: The topic_urn of this UpdateAlarmConfigRequestInfo.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this UpdateAlarmConfigRequestInfo.

        是否发送短信

        :param topic_urn: The topic_urn of this UpdateAlarmConfigRequestInfo.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def daily_alarm(self):
        r"""Gets the daily_alarm of this UpdateAlarmConfigRequestInfo.

        是否开启每日告警

        :return: The daily_alarm of this UpdateAlarmConfigRequestInfo.
        :rtype: bool
        """
        return self._daily_alarm

    @daily_alarm.setter
    def daily_alarm(self, daily_alarm):
        r"""Sets the daily_alarm of this UpdateAlarmConfigRequestInfo.

        是否开启每日告警

        :param daily_alarm: The daily_alarm of this UpdateAlarmConfigRequestInfo.
        :type daily_alarm: bool
        """
        self._daily_alarm = daily_alarm

    @property
    def realtime_alarm(self):
        r"""Gets the realtime_alarm of this UpdateAlarmConfigRequestInfo.

        是否开启实时告警

        :return: The realtime_alarm of this UpdateAlarmConfigRequestInfo.
        :rtype: bool
        """
        return self._realtime_alarm

    @realtime_alarm.setter
    def realtime_alarm(self, realtime_alarm):
        r"""Sets the realtime_alarm of this UpdateAlarmConfigRequestInfo.

        是否开启实时告警

        :param realtime_alarm: The realtime_alarm of this UpdateAlarmConfigRequestInfo.
        :type realtime_alarm: bool
        """
        self._realtime_alarm = realtime_alarm

    @property
    def alarm_level(self):
        r"""Gets the alarm_level of this UpdateAlarmConfigRequestInfo.

        告警等级

        :return: The alarm_level of this UpdateAlarmConfigRequestInfo.
        :rtype: str
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        r"""Sets the alarm_level of this UpdateAlarmConfigRequestInfo.

        告警等级

        :param alarm_level: The alarm_level of this UpdateAlarmConfigRequestInfo.
        :type alarm_level: str
        """
        self._alarm_level = alarm_level

    @property
    def ignored_event_class_list(self):
        r"""Gets the ignored_event_class_list of this UpdateAlarmConfigRequestInfo.

        忽略事件列表

        :return: The ignored_event_class_list of this UpdateAlarmConfigRequestInfo.
        :rtype: list[str]
        """
        return self._ignored_event_class_list

    @ignored_event_class_list.setter
    def ignored_event_class_list(self, ignored_event_class_list):
        r"""Sets the ignored_event_class_list of this UpdateAlarmConfigRequestInfo.

        忽略事件列表

        :param ignored_event_class_list: The ignored_event_class_list of this UpdateAlarmConfigRequestInfo.
        :type ignored_event_class_list: list[str]
        """
        self._ignored_event_class_list = ignored_event_class_list

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
        if not isinstance(other, UpdateAlarmConfigRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
