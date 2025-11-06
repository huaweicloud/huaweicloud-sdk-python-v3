# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmPeriod:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'complete_time': 'str',
        'period': 'int'
    }

    attribute_map = {
        'complete_time': 'complete_time',
        'period': 'period'
    }

    def __init__(self, complete_time=None, period=None):
        r"""AlarmPeriod

        The model defined in huaweicloud sdk

        :param complete_time: 任务完成时间。
        :type complete_time: str
        :param period: 周期。
        :type period: int
        """
        
        

        self._complete_time = None
        self._period = None
        self.discriminator = None

        if complete_time is not None:
            self.complete_time = complete_time
        if period is not None:
            self.period = period

    @property
    def complete_time(self):
        r"""Gets the complete_time of this AlarmPeriod.

        任务完成时间。

        :return: The complete_time of this AlarmPeriod.
        :rtype: str
        """
        return self._complete_time

    @complete_time.setter
    def complete_time(self, complete_time):
        r"""Sets the complete_time of this AlarmPeriod.

        任务完成时间。

        :param complete_time: The complete_time of this AlarmPeriod.
        :type complete_time: str
        """
        self._complete_time = complete_time

    @property
    def period(self):
        r"""Gets the period of this AlarmPeriod.

        周期。

        :return: The period of this AlarmPeriod.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this AlarmPeriod.

        周期。

        :param period: The period of this AlarmPeriod.
        :type period: int
        """
        self._period = period

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AlarmPeriod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
