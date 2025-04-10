# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SupplementDataRespSupplementDataInstanceTime:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'days': 'list[str]',
        'time_of_day': 'str'
    }

    attribute_map = {
        'days': 'days',
        'time_of_day': 'time_of_day'
    }

    def __init__(self, days=None, time_of_day=None):
        r"""SupplementDataRespSupplementDataInstanceTime

        The model defined in huaweicloud sdk

        :param days: 支持离散的天
        :type days: list[str]
        :param time_of_day: 一天中的时间段
        :type time_of_day: str
        """
        
        

        self._days = None
        self._time_of_day = None
        self.discriminator = None

        if days is not None:
            self.days = days
        if time_of_day is not None:
            self.time_of_day = time_of_day

    @property
    def days(self):
        r"""Gets the days of this SupplementDataRespSupplementDataInstanceTime.

        支持离散的天

        :return: The days of this SupplementDataRespSupplementDataInstanceTime.
        :rtype: list[str]
        """
        return self._days

    @days.setter
    def days(self, days):
        r"""Sets the days of this SupplementDataRespSupplementDataInstanceTime.

        支持离散的天

        :param days: The days of this SupplementDataRespSupplementDataInstanceTime.
        :type days: list[str]
        """
        self._days = days

    @property
    def time_of_day(self):
        r"""Gets the time_of_day of this SupplementDataRespSupplementDataInstanceTime.

        一天中的时间段

        :return: The time_of_day of this SupplementDataRespSupplementDataInstanceTime.
        :rtype: str
        """
        return self._time_of_day

    @time_of_day.setter
    def time_of_day(self, time_of_day):
        r"""Sets the time_of_day of this SupplementDataRespSupplementDataInstanceTime.

        一天中的时间段

        :param time_of_day: The time_of_day of this SupplementDataRespSupplementDataInstanceTime.
        :type time_of_day: str
        """
        self._time_of_day = time_of_day

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
        if not isinstance(other, SupplementDataRespSupplementDataInstanceTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
