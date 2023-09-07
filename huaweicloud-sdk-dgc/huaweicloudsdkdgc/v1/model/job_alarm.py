# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobAlarm:

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
        'topic_urn': 'str'
    }

    attribute_map = {
        'alarm_type': 'alarmType',
        'topic_urn': 'topicUrn'
    }

    def __init__(self, alarm_type=None, topic_urn=None):
        """JobAlarm

        The model defined in huaweicloud sdk

        :param alarm_type: 告警类型
        :type alarm_type: str
        :param topic_urn: 
        :type topic_urn: str
        """
        
        

        self._alarm_type = None
        self._topic_urn = None
        self.discriminator = None

        self.alarm_type = alarm_type
        self.topic_urn = topic_urn

    @property
    def alarm_type(self):
        """Gets the alarm_type of this JobAlarm.

        告警类型

        :return: The alarm_type of this JobAlarm.
        :rtype: str
        """
        return self._alarm_type

    @alarm_type.setter
    def alarm_type(self, alarm_type):
        """Sets the alarm_type of this JobAlarm.

        告警类型

        :param alarm_type: The alarm_type of this JobAlarm.
        :type alarm_type: str
        """
        self._alarm_type = alarm_type

    @property
    def topic_urn(self):
        """Gets the topic_urn of this JobAlarm.

        :return: The topic_urn of this JobAlarm.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        """Sets the topic_urn of this JobAlarm.

        :param topic_urn: The topic_urn of this JobAlarm.
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
        if not isinstance(other, JobAlarm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
