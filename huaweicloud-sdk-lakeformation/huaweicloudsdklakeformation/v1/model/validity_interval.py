# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidityInterval:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'days': 'int',
        'hours': 'int',
        'minutes': 'int'
    }

    attribute_map = {
        'days': 'days',
        'hours': 'hours',
        'minutes': 'minutes'
    }

    def __init__(self, days=None, hours=None, minutes=None):
        """ValidityInterval

        The model defined in huaweicloud sdk

        :param days: 日
        :type days: int
        :param hours: 时
        :type hours: int
        :param minutes: 分
        :type minutes: int
        """
        
        

        self._days = None
        self._hours = None
        self._minutes = None
        self.discriminator = None

        if days is not None:
            self.days = days
        if hours is not None:
            self.hours = hours
        if minutes is not None:
            self.minutes = minutes

    @property
    def days(self):
        """Gets the days of this ValidityInterval.

        日

        :return: The days of this ValidityInterval.
        :rtype: int
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this ValidityInterval.

        日

        :param days: The days of this ValidityInterval.
        :type days: int
        """
        self._days = days

    @property
    def hours(self):
        """Gets the hours of this ValidityInterval.

        时

        :return: The hours of this ValidityInterval.
        :rtype: int
        """
        return self._hours

    @hours.setter
    def hours(self, hours):
        """Sets the hours of this ValidityInterval.

        时

        :param hours: The hours of this ValidityInterval.
        :type hours: int
        """
        self._hours = hours

    @property
    def minutes(self):
        """Gets the minutes of this ValidityInterval.

        分

        :return: The minutes of this ValidityInterval.
        :rtype: int
        """
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        """Sets the minutes of this ValidityInterval.

        分

        :param minutes: The minutes of this ValidityInterval.
        :type minutes: int
        """
        self._minutes = minutes

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
        if not isinstance(other, ValidityInterval):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
