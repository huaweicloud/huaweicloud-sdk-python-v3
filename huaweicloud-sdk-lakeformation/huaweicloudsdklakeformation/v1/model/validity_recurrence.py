# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidityRecurrence:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'interval': 'ValidityInterval',
        'schedule': 'RecurrenceSchedule'
    }

    attribute_map = {
        'interval': 'interval',
        'schedule': 'schedule'
    }

    def __init__(self, interval=None, schedule=None):
        """ValidityRecurrence

        The model defined in huaweicloud sdk

        :param interval: 
        :type interval: :class:`huaweicloudsdklakeformation.v1.ValidityInterval`
        :param schedule: 
        :type schedule: :class:`huaweicloudsdklakeformation.v1.RecurrenceSchedule`
        """
        
        

        self._interval = None
        self._schedule = None
        self.discriminator = None

        if interval is not None:
            self.interval = interval
        if schedule is not None:
            self.schedule = schedule

    @property
    def interval(self):
        """Gets the interval of this ValidityRecurrence.

        :return: The interval of this ValidityRecurrence.
        :rtype: :class:`huaweicloudsdklakeformation.v1.ValidityInterval`
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this ValidityRecurrence.

        :param interval: The interval of this ValidityRecurrence.
        :type interval: :class:`huaweicloudsdklakeformation.v1.ValidityInterval`
        """
        self._interval = interval

    @property
    def schedule(self):
        """Gets the schedule of this ValidityRecurrence.

        :return: The schedule of this ValidityRecurrence.
        :rtype: :class:`huaweicloudsdklakeformation.v1.RecurrenceSchedule`
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this ValidityRecurrence.

        :param schedule: The schedule of this ValidityRecurrence.
        :type schedule: :class:`huaweicloudsdklakeformation.v1.RecurrenceSchedule`
        """
        self._schedule = schedule

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
        if not isinstance(other, ValidityRecurrence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
