# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DailyTimerType:

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
        'days_of_week': 'str'
    }

    attribute_map = {
        'time': 'time',
        'days_of_week': 'days_of_week'
    }

    def __init__(self, time=None, days_of_week=None):
        """DailyTimerType

        The model defined in huaweicloud sdk

        :param time: **参数说明**：规则触发的时间，格式：HH:MM。
        :type time: str
        :param days_of_week: **参数说明**：星期列表，以逗号分隔。1代表周日，2代表周一，依次类推，默认为每天。 **取值范围**：只允许数字和逗号的组合，数字不小于1不大于7，数量不超过7个，以逗号隔开
        :type days_of_week: str
        """
        
        

        self._time = None
        self._days_of_week = None
        self.discriminator = None

        self.time = time
        if days_of_week is not None:
            self.days_of_week = days_of_week

    @property
    def time(self):
        """Gets the time of this DailyTimerType.

        **参数说明**：规则触发的时间，格式：HH:MM。

        :return: The time of this DailyTimerType.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this DailyTimerType.

        **参数说明**：规则触发的时间，格式：HH:MM。

        :param time: The time of this DailyTimerType.
        :type time: str
        """
        self._time = time

    @property
    def days_of_week(self):
        """Gets the days_of_week of this DailyTimerType.

        **参数说明**：星期列表，以逗号分隔。1代表周日，2代表周一，依次类推，默认为每天。 **取值范围**：只允许数字和逗号的组合，数字不小于1不大于7，数量不超过7个，以逗号隔开

        :return: The days_of_week of this DailyTimerType.
        :rtype: str
        """
        return self._days_of_week

    @days_of_week.setter
    def days_of_week(self, days_of_week):
        """Sets the days_of_week of this DailyTimerType.

        **参数说明**：星期列表，以逗号分隔。1代表周日，2代表周一，依次类推，默认为每天。 **取值范围**：只允许数字和逗号的组合，数字不小于1不大于7，数量不超过7个，以逗号隔开

        :param days_of_week: The days_of_week of this DailyTimerType.
        :type days_of_week: str
        """
        self._days_of_week = days_of_week

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
        if not isinstance(other, DailyTimerType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
