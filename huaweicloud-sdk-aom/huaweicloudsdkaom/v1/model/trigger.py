# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Trigger:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'information': 'str',
        'scheduled_time': 'str',
        'time_zone': 'str',
        'topic_urn': 'str',
        'alarm_name': 'str'
    }

    attribute_map = {
        'information': 'information',
        'scheduled_time': 'scheduled_time',
        'time_zone': 'time_zone',
        'topic_urn': 'topic_urn',
        'alarm_name': 'alarm_name'
    }

    def __init__(self, information=None, scheduled_time=None, time_zone=None, topic_urn=None, alarm_name=None):
        """Trigger

        The model defined in huaweicloud sdk

        :param information: 定时任务的必填信息。
        :type information: str
        :param scheduled_time: 触发器执行时间。
        :type scheduled_time: str
        :param time_zone: 时区。
        :type time_zone: str
        :param topic_urn: smn主题urn。
        :type topic_urn: str
        :param alarm_name: aom告警名字。
        :type alarm_name: str
        """
        
        

        self._information = None
        self._scheduled_time = None
        self._time_zone = None
        self._topic_urn = None
        self._alarm_name = None
        self.discriminator = None

        self.information = information
        self.scheduled_time = scheduled_time
        self.time_zone = time_zone
        self.topic_urn = topic_urn
        self.alarm_name = alarm_name

    @property
    def information(self):
        """Gets the information of this Trigger.

        定时任务的必填信息。

        :return: The information of this Trigger.
        :rtype: str
        """
        return self._information

    @information.setter
    def information(self, information):
        """Sets the information of this Trigger.

        定时任务的必填信息。

        :param information: The information of this Trigger.
        :type information: str
        """
        self._information = information

    @property
    def scheduled_time(self):
        """Gets the scheduled_time of this Trigger.

        触发器执行时间。

        :return: The scheduled_time of this Trigger.
        :rtype: str
        """
        return self._scheduled_time

    @scheduled_time.setter
    def scheduled_time(self, scheduled_time):
        """Sets the scheduled_time of this Trigger.

        触发器执行时间。

        :param scheduled_time: The scheduled_time of this Trigger.
        :type scheduled_time: str
        """
        self._scheduled_time = scheduled_time

    @property
    def time_zone(self):
        """Gets the time_zone of this Trigger.

        时区。

        :return: The time_zone of this Trigger.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this Trigger.

        时区。

        :param time_zone: The time_zone of this Trigger.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def topic_urn(self):
        """Gets the topic_urn of this Trigger.

        smn主题urn。

        :return: The topic_urn of this Trigger.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        """Sets the topic_urn of this Trigger.

        smn主题urn。

        :param topic_urn: The topic_urn of this Trigger.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def alarm_name(self):
        """Gets the alarm_name of this Trigger.

        aom告警名字。

        :return: The alarm_name of this Trigger.
        :rtype: str
        """
        return self._alarm_name

    @alarm_name.setter
    def alarm_name(self, alarm_name):
        """Sets the alarm_name of this Trigger.

        aom告警名字。

        :param alarm_name: The alarm_name of this Trigger.
        :type alarm_name: str
        """
        self._alarm_name = alarm_name

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
        if not isinstance(other, Trigger):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
