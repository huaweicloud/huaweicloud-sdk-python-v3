# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValiditySchedule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'end_time': 'str',
        'recurrences': 'list[ValidityRecurrence]',
        'start_time': 'str',
        'time_zone': 'str'
    }

    attribute_map = {
        'end_time': 'end_time',
        'recurrences': 'recurrences',
        'start_time': 'start_time',
        'time_zone': 'time_zone'
    }

    def __init__(self, end_time=None, recurrences=None, start_time=None, time_zone=None):
        """ValiditySchedule

        The model defined in huaweicloud sdk

        :param end_time: end时间
        :type end_time: str
        :param recurrences: 策略递归
        :type recurrences: list[:class:`huaweicloudsdklakeformation.v1.ValidityRecurrence`]
        :param start_time: 开始时间
        :type start_time: str
        :param time_zone: 时间域
        :type time_zone: str
        """
        
        

        self._end_time = None
        self._recurrences = None
        self._start_time = None
        self._time_zone = None
        self.discriminator = None

        if end_time is not None:
            self.end_time = end_time
        if recurrences is not None:
            self.recurrences = recurrences
        if start_time is not None:
            self.start_time = start_time
        if time_zone is not None:
            self.time_zone = time_zone

    @property
    def end_time(self):
        """Gets the end_time of this ValiditySchedule.

        end时间

        :return: The end_time of this ValiditySchedule.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ValiditySchedule.

        end时间

        :param end_time: The end_time of this ValiditySchedule.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def recurrences(self):
        """Gets the recurrences of this ValiditySchedule.

        策略递归

        :return: The recurrences of this ValiditySchedule.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.ValidityRecurrence`]
        """
        return self._recurrences

    @recurrences.setter
    def recurrences(self, recurrences):
        """Sets the recurrences of this ValiditySchedule.

        策略递归

        :param recurrences: The recurrences of this ValiditySchedule.
        :type recurrences: list[:class:`huaweicloudsdklakeformation.v1.ValidityRecurrence`]
        """
        self._recurrences = recurrences

    @property
    def start_time(self):
        """Gets the start_time of this ValiditySchedule.

        开始时间

        :return: The start_time of this ValiditySchedule.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ValiditySchedule.

        开始时间

        :param start_time: The start_time of this ValiditySchedule.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def time_zone(self):
        """Gets the time_zone of this ValiditySchedule.

        时间域

        :return: The time_zone of this ValiditySchedule.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this ValiditySchedule.

        时间域

        :param time_zone: The time_zone of this ValiditySchedule.
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
        if not isinstance(other, ValiditySchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
