# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduleConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'duration': 'int',
        'time_unit': 'str',
        'type': 'str'
    }

    attribute_map = {
        'duration': 'duration',
        'time_unit': 'time_unit',
        'type': 'type'
    }

    def __init__(self, duration=None, time_unit=None, type=None):
        r"""ScheduleConfig

        The model defined in huaweicloud sdk

        :param duration: **参数解释：** 对应的时间单位的数值。 **约束限制：** 与time_unit共同确认时间设置的范围是1分钟~7天之间。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type duration: int
        :param time_unit: **参数解释：** 时间的单位。 **约束限制：** 与duration共同确认时间设置的范围是1分钟~7天之间。 **取值范围：** - MINUTES：分钟。 - HOURS：小时。 - DAYS：天。 **默认取值：** 不涉及。
        :type time_unit: str
        :param type: **参数解释：** 调度类型，当前仅支持取值为STOP。 **约束限制：** 不涉及。 **取值范围：** - STOP：停止。 **默认取值：** 不涉及。
        :type type: str
        """
        
        

        self._duration = None
        self._time_unit = None
        self._type = None
        self.discriminator = None

        if duration is not None:
            self.duration = duration
        if time_unit is not None:
            self.time_unit = time_unit
        if type is not None:
            self.type = type

    @property
    def duration(self):
        r"""Gets the duration of this ScheduleConfig.

        **参数解释：** 对应的时间单位的数值。 **约束限制：** 与time_unit共同确认时间设置的范围是1分钟~7天之间。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The duration of this ScheduleConfig.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this ScheduleConfig.

        **参数解释：** 对应的时间单位的数值。 **约束限制：** 与time_unit共同确认时间设置的范围是1分钟~7天之间。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param duration: The duration of this ScheduleConfig.
        :type duration: int
        """
        self._duration = duration

    @property
    def time_unit(self):
        r"""Gets the time_unit of this ScheduleConfig.

        **参数解释：** 时间的单位。 **约束限制：** 与duration共同确认时间设置的范围是1分钟~7天之间。 **取值范围：** - MINUTES：分钟。 - HOURS：小时。 - DAYS：天。 **默认取值：** 不涉及。

        :return: The time_unit of this ScheduleConfig.
        :rtype: str
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        r"""Sets the time_unit of this ScheduleConfig.

        **参数解释：** 时间的单位。 **约束限制：** 与duration共同确认时间设置的范围是1分钟~7天之间。 **取值范围：** - MINUTES：分钟。 - HOURS：小时。 - DAYS：天。 **默认取值：** 不涉及。

        :param time_unit: The time_unit of this ScheduleConfig.
        :type time_unit: str
        """
        self._time_unit = time_unit

    @property
    def type(self):
        r"""Gets the type of this ScheduleConfig.

        **参数解释：** 调度类型，当前仅支持取值为STOP。 **约束限制：** 不涉及。 **取值范围：** - STOP：停止。 **默认取值：** 不涉及。

        :return: The type of this ScheduleConfig.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ScheduleConfig.

        **参数解释：** 调度类型，当前仅支持取值为STOP。 **约束限制：** 不涉及。 **取值范围：** - STOP：停止。 **默认取值：** 不涉及。

        :param type: The type of this ScheduleConfig.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ScheduleConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
