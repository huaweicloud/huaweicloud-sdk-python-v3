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
        'policy': 'str',
        'scheduled_time': 'str',
        'time_zone': 'str',
        'topic_urn': 'str'
    }

    attribute_map = {
        'policy': 'policy',
        'scheduled_time': 'scheduled_time',
        'time_zone': 'time_zone',
        'topic_urn': 'topic_urn'
    }

    def __init__(self, policy=None, scheduled_time=None, time_zone=None, topic_urn=None):
        """Trigger

        The model defined in huaweicloud sdk

        :param policy: 定时策略。once、corn、periodic
        :type policy: str
        :param scheduled_time: 触发器执行时间。单次执行为UTC毫秒数、简单周期为\&quot;[\\\&quot;7\\\&quot;]\&quot;、corn为corn表达式\&quot;0 23 * * *\&quot;
        :type scheduled_time: str
        :param time_zone: 时区。
        :type time_zone: str
        :param topic_urn: smn主题urn。
        :type topic_urn: str
        """
        
        

        self._policy = None
        self._scheduled_time = None
        self._time_zone = None
        self._topic_urn = None
        self.discriminator = None

        self.policy = policy
        self.scheduled_time = scheduled_time
        self.time_zone = time_zone
        self.topic_urn = topic_urn

    @property
    def policy(self):
        """Gets the policy of this Trigger.

        定时策略。once、corn、periodic

        :return: The policy of this Trigger.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this Trigger.

        定时策略。once、corn、periodic

        :param policy: The policy of this Trigger.
        :type policy: str
        """
        self._policy = policy

    @property
    def scheduled_time(self):
        """Gets the scheduled_time of this Trigger.

        触发器执行时间。单次执行为UTC毫秒数、简单周期为\"[\\\"7\\\"]\"、corn为corn表达式\"0 23 * * *\"

        :return: The scheduled_time of this Trigger.
        :rtype: str
        """
        return self._scheduled_time

    @scheduled_time.setter
    def scheduled_time(self, scheduled_time):
        """Sets the scheduled_time of this Trigger.

        触发器执行时间。单次执行为UTC毫秒数、简单周期为\"[\\\"7\\\"]\"、corn为corn表达式\"0 23 * * *\"

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
