# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityCheckTaskCondition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'day_of_week': 'list[str]',
        'hour': 'int',
        'minute': 'int',
        'random_offset': 'int'
    }

    attribute_map = {
        'type': 'type',
        'day_of_week': 'day_of_week',
        'hour': 'hour',
        'minute': 'minute',
        'random_offset': 'random_offset'
    }

    def __init__(self, type=None, day_of_week=None, hour=None, minute=None, random_offset=None):
        r"""SecurityCheckTaskCondition

        The model defined in huaweicloud sdk

        :param type: 定时任务，包含如下:   - fixed_weekday : 固定工作日
        :type type: str
        :param day_of_week: 周几触发，可选0或多个
        :type day_of_week: list[str]
        :param hour: 在此参数表示的小时触发定时任务
        :type hour: int
        :param minute: 在此参数表示的分钟触发定时任务
        :type minute: int
        :param random_offset: 随机偏移时间
        :type random_offset: int
        """
        
        

        self._type = None
        self._day_of_week = None
        self._hour = None
        self._minute = None
        self._random_offset = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if day_of_week is not None:
            self.day_of_week = day_of_week
        if hour is not None:
            self.hour = hour
        if minute is not None:
            self.minute = minute
        if random_offset is not None:
            self.random_offset = random_offset

    @property
    def type(self):
        r"""Gets the type of this SecurityCheckTaskCondition.

        定时任务，包含如下:   - fixed_weekday : 固定工作日

        :return: The type of this SecurityCheckTaskCondition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SecurityCheckTaskCondition.

        定时任务，包含如下:   - fixed_weekday : 固定工作日

        :param type: The type of this SecurityCheckTaskCondition.
        :type type: str
        """
        self._type = type

    @property
    def day_of_week(self):
        r"""Gets the day_of_week of this SecurityCheckTaskCondition.

        周几触发，可选0或多个

        :return: The day_of_week of this SecurityCheckTaskCondition.
        :rtype: list[str]
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        r"""Sets the day_of_week of this SecurityCheckTaskCondition.

        周几触发，可选0或多个

        :param day_of_week: The day_of_week of this SecurityCheckTaskCondition.
        :type day_of_week: list[str]
        """
        self._day_of_week = day_of_week

    @property
    def hour(self):
        r"""Gets the hour of this SecurityCheckTaskCondition.

        在此参数表示的小时触发定时任务

        :return: The hour of this SecurityCheckTaskCondition.
        :rtype: int
        """
        return self._hour

    @hour.setter
    def hour(self, hour):
        r"""Sets the hour of this SecurityCheckTaskCondition.

        在此参数表示的小时触发定时任务

        :param hour: The hour of this SecurityCheckTaskCondition.
        :type hour: int
        """
        self._hour = hour

    @property
    def minute(self):
        r"""Gets the minute of this SecurityCheckTaskCondition.

        在此参数表示的分钟触发定时任务

        :return: The minute of this SecurityCheckTaskCondition.
        :rtype: int
        """
        return self._minute

    @minute.setter
    def minute(self, minute):
        r"""Sets the minute of this SecurityCheckTaskCondition.

        在此参数表示的分钟触发定时任务

        :param minute: The minute of this SecurityCheckTaskCondition.
        :type minute: int
        """
        self._minute = minute

    @property
    def random_offset(self):
        r"""Gets the random_offset of this SecurityCheckTaskCondition.

        随机偏移时间

        :return: The random_offset of this SecurityCheckTaskCondition.
        :rtype: int
        """
        return self._random_offset

    @random_offset.setter
    def random_offset(self, random_offset):
        r"""Sets the random_offset of this SecurityCheckTaskCondition.

        随机偏移时间

        :param random_offset: The random_offset of this SecurityCheckTaskCondition.
        :type random_offset: int
        """
        self._random_offset = random_offset

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
        if not isinstance(other, SecurityCheckTaskCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
