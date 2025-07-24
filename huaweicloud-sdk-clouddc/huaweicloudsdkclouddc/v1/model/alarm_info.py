# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_device': 'str',
        'alarm_number': 'int',
        'alarm_duration': 'int'
    }

    attribute_map = {
        'alarm_device': 'alarm_device',
        'alarm_number': 'alarm_number',
        'alarm_duration': 'alarm_duration'
    }

    def __init__(self, alarm_device=None, alarm_number=None, alarm_duration=None):
        r"""AlarmInfo

        The model defined in huaweicloud sdk

        :param alarm_device: 告警设备
        :type alarm_device: str
        :param alarm_number: 告警数量
        :type alarm_number: int
        :param alarm_duration: 告警时间
        :type alarm_duration: int
        """
        
        

        self._alarm_device = None
        self._alarm_number = None
        self._alarm_duration = None
        self.discriminator = None

        if alarm_device is not None:
            self.alarm_device = alarm_device
        if alarm_number is not None:
            self.alarm_number = alarm_number
        if alarm_duration is not None:
            self.alarm_duration = alarm_duration

    @property
    def alarm_device(self):
        r"""Gets the alarm_device of this AlarmInfo.

        告警设备

        :return: The alarm_device of this AlarmInfo.
        :rtype: str
        """
        return self._alarm_device

    @alarm_device.setter
    def alarm_device(self, alarm_device):
        r"""Sets the alarm_device of this AlarmInfo.

        告警设备

        :param alarm_device: The alarm_device of this AlarmInfo.
        :type alarm_device: str
        """
        self._alarm_device = alarm_device

    @property
    def alarm_number(self):
        r"""Gets the alarm_number of this AlarmInfo.

        告警数量

        :return: The alarm_number of this AlarmInfo.
        :rtype: int
        """
        return self._alarm_number

    @alarm_number.setter
    def alarm_number(self, alarm_number):
        r"""Sets the alarm_number of this AlarmInfo.

        告警数量

        :param alarm_number: The alarm_number of this AlarmInfo.
        :type alarm_number: int
        """
        self._alarm_number = alarm_number

    @property
    def alarm_duration(self):
        r"""Gets the alarm_duration of this AlarmInfo.

        告警时间

        :return: The alarm_duration of this AlarmInfo.
        :rtype: int
        """
        return self._alarm_duration

    @alarm_duration.setter
    def alarm_duration(self, alarm_duration):
        r"""Sets the alarm_duration of this AlarmInfo.

        告警时间

        :param alarm_duration: The alarm_duration of this AlarmInfo.
        :type alarm_duration: int
        """
        self._alarm_duration = alarm_duration

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
        if not isinstance(other, AlarmInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
