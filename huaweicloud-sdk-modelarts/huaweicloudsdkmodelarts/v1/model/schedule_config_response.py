# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduleConfigResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'due_time': 'int',
        'duration': 'int',
        'time_unit': 'str',
        'type': 'str',
        'processed': 'bool'
    }

    attribute_map = {
        'due_time': 'due_time',
        'duration': 'duration',
        'time_unit': 'time_unit',
        'type': 'type',
        'processed': 'processed'
    }

    def __init__(self, due_time=None, duration=None, time_unit=None, type=None, processed=None):
        r"""ScheduleConfigResponse

        The model defined in huaweicloud sdk

        :param due_time: **参数解释：** 触发时间，UTC毫秒，13位时间戳。 **取值范围：** 不涉及。
        :type due_time: int
        :param duration: **参数解释：** 对应的时间单位的数值。 **取值范围：** 不涉及。
        :type duration: int
        :param time_unit: **参数解释：** 调度时间单位。 **取值范围：** - MINUTES：分钟。 - HOURS：小时。 - DAYS：天。
        :type time_unit: str
        :param type: **参数解释：** 调度类型，当前仅支持取值为STOP。 **取值范围：** - STOP：停止。
        :type type: str
        :param processed: **参数解释：** 表示是否处理完成。 **取值范围：** - true：该定时任务已经执行过。 - false：该定时任务尚未执行。
        :type processed: bool
        """
        
        

        self._due_time = None
        self._duration = None
        self._time_unit = None
        self._type = None
        self._processed = None
        self.discriminator = None

        if due_time is not None:
            self.due_time = due_time
        if duration is not None:
            self.duration = duration
        if time_unit is not None:
            self.time_unit = time_unit
        if type is not None:
            self.type = type
        if processed is not None:
            self.processed = processed

    @property
    def due_time(self):
        r"""Gets the due_time of this ScheduleConfigResponse.

        **参数解释：** 触发时间，UTC毫秒，13位时间戳。 **取值范围：** 不涉及。

        :return: The due_time of this ScheduleConfigResponse.
        :rtype: int
        """
        return self._due_time

    @due_time.setter
    def due_time(self, due_time):
        r"""Sets the due_time of this ScheduleConfigResponse.

        **参数解释：** 触发时间，UTC毫秒，13位时间戳。 **取值范围：** 不涉及。

        :param due_time: The due_time of this ScheduleConfigResponse.
        :type due_time: int
        """
        self._due_time = due_time

    @property
    def duration(self):
        r"""Gets the duration of this ScheduleConfigResponse.

        **参数解释：** 对应的时间单位的数值。 **取值范围：** 不涉及。

        :return: The duration of this ScheduleConfigResponse.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this ScheduleConfigResponse.

        **参数解释：** 对应的时间单位的数值。 **取值范围：** 不涉及。

        :param duration: The duration of this ScheduleConfigResponse.
        :type duration: int
        """
        self._duration = duration

    @property
    def time_unit(self):
        r"""Gets the time_unit of this ScheduleConfigResponse.

        **参数解释：** 调度时间单位。 **取值范围：** - MINUTES：分钟。 - HOURS：小时。 - DAYS：天。

        :return: The time_unit of this ScheduleConfigResponse.
        :rtype: str
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        r"""Sets the time_unit of this ScheduleConfigResponse.

        **参数解释：** 调度时间单位。 **取值范围：** - MINUTES：分钟。 - HOURS：小时。 - DAYS：天。

        :param time_unit: The time_unit of this ScheduleConfigResponse.
        :type time_unit: str
        """
        self._time_unit = time_unit

    @property
    def type(self):
        r"""Gets the type of this ScheduleConfigResponse.

        **参数解释：** 调度类型，当前仅支持取值为STOP。 **取值范围：** - STOP：停止。

        :return: The type of this ScheduleConfigResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ScheduleConfigResponse.

        **参数解释：** 调度类型，当前仅支持取值为STOP。 **取值范围：** - STOP：停止。

        :param type: The type of this ScheduleConfigResponse.
        :type type: str
        """
        self._type = type

    @property
    def processed(self):
        r"""Gets the processed of this ScheduleConfigResponse.

        **参数解释：** 表示是否处理完成。 **取值范围：** - true：该定时任务已经执行过。 - false：该定时任务尚未执行。

        :return: The processed of this ScheduleConfigResponse.
        :rtype: bool
        """
        return self._processed

    @processed.setter
    def processed(self, processed):
        r"""Sets the processed of this ScheduleConfigResponse.

        **参数解释：** 表示是否处理完成。 **取值范围：** - true：该定时任务已经执行过。 - false：该定时任务尚未执行。

        :param processed: The processed of this ScheduleConfigResponse.
        :type processed: bool
        """
        self._processed = processed

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
        if not isinstance(other, ScheduleConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
