# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QosDataElement:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time': 'str',
        'value': 'int',
        'alarm': 'bool',
        'threshold': 'int'
    }

    attribute_map = {
        'time': 'time',
        'value': 'value',
        'alarm': 'alarm',
        'threshold': 'threshold'
    }

    def __init__(self, time=None, value=None, alarm=None, threshold=None):
        """QosDataElement

        The model defined in huaweicloud sdk

        :param time: QoS时间点, UTC时间，格式：yyyy-MM-ddTHH:mm:ss.SSSZ。
        :type time: str
        :param value: QoS值。
        :type value: int
        :param alarm: 该时间点是否有阈值告警。 * true: 阈值告警 * false: 无阈值告警 
        :type alarm: bool
        :param threshold: 该时间点的阈值。
        :type threshold: int
        """
        
        

        self._time = None
        self._value = None
        self._alarm = None
        self._threshold = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if value is not None:
            self.value = value
        if alarm is not None:
            self.alarm = alarm
        if threshold is not None:
            self.threshold = threshold

    @property
    def time(self):
        """Gets the time of this QosDataElement.

        QoS时间点, UTC时间，格式：yyyy-MM-ddTHH:mm:ss.SSSZ。

        :return: The time of this QosDataElement.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this QosDataElement.

        QoS时间点, UTC时间，格式：yyyy-MM-ddTHH:mm:ss.SSSZ。

        :param time: The time of this QosDataElement.
        :type time: str
        """
        self._time = time

    @property
    def value(self):
        """Gets the value of this QosDataElement.

        QoS值。

        :return: The value of this QosDataElement.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this QosDataElement.

        QoS值。

        :param value: The value of this QosDataElement.
        :type value: int
        """
        self._value = value

    @property
    def alarm(self):
        """Gets the alarm of this QosDataElement.

        该时间点是否有阈值告警。 * true: 阈值告警 * false: 无阈值告警 

        :return: The alarm of this QosDataElement.
        :rtype: bool
        """
        return self._alarm

    @alarm.setter
    def alarm(self, alarm):
        """Sets the alarm of this QosDataElement.

        该时间点是否有阈值告警。 * true: 阈值告警 * false: 无阈值告警 

        :param alarm: The alarm of this QosDataElement.
        :type alarm: bool
        """
        self._alarm = alarm

    @property
    def threshold(self):
        """Gets the threshold of this QosDataElement.

        该时间点的阈值。

        :return: The threshold of this QosDataElement.
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this QosDataElement.

        该时间点的阈值。

        :param threshold: The threshold of this QosDataElement.
        :type threshold: int
        """
        self._threshold = threshold

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
        if not isinstance(other, QosDataElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
