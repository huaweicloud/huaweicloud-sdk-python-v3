# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsExecutionStrategy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'int',
        'end_time': 'int',
        'repeat': 'bool',
        'repeat_type': 'str',
        'repeat_interval': 'int',
        'day_of_week': 'int'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'repeat': 'repeat',
        'repeat_type': 'repeat_type',
        'repeat_interval': 'repeat_interval',
        'day_of_week': 'day_of_week'
    }

    def __init__(self, start_time=None, end_time=None, repeat=None, repeat_type=None, repeat_interval=None, day_of_week=None):
        r"""OpsExecutionStrategy

        The model defined in huaweicloud sdk

        :param start_time: **参数解释：** 开始时间（单位：毫秒数）  **约束限制：** 不超过当前时间的前31天。  **取值范围：** 13位毫秒级时间戳。  **默认取值：** 无。
        :type start_time: int
        :param end_time: **参数解释：** 结束时间（单位：毫秒数）  **约束限制：** 无。  **取值范围：** 13位毫秒级时间戳。  **默认取值：** 无。
        :type end_time: int
        :param repeat: **参数解释：** 是否重复执行。  **约束限制：** 无。  **取值范围：** ture或者false。  **默认取值：** false。
        :type repeat: bool
        :param repeat_type: **参数解释：** 重复周期类型。  **约束限制：** 无。  **取值范围：** daily：天重复，weekly：周重复。  **默认取值：** 无。
        :type repeat_type: str
        :param repeat_interval: **参数解释：** 重复周期。  **约束限制：** 无。  **取值范围：** 1到6之间的数字。  **默认取值：** 无。
        :type repeat_interval: int
        :param day_of_week: **参数解释：** 周重复时，每周几执行。  **约束限制：** 仅 repeat_type&#x3D;weekly 时必填且非 null；repeat_type&#x3D;daily 时必须为 null（或不上送）。无语义即 null。  **取值范围：** 1到7之间的数字，分别代表周一到周日；daily 场景为 null。  **默认取值：** 无。
        :type day_of_week: int
        """
        
        

        self._start_time = None
        self._end_time = None
        self._repeat = None
        self._repeat_type = None
        self._repeat_interval = None
        self._day_of_week = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        self.repeat = repeat
        if repeat_type is not None:
            self.repeat_type = repeat_type
        if repeat_interval is not None:
            self.repeat_interval = repeat_interval
        if day_of_week is not None:
            self.day_of_week = day_of_week

    @property
    def start_time(self):
        r"""Gets the start_time of this OpsExecutionStrategy.

        **参数解释：** 开始时间（单位：毫秒数）  **约束限制：** 不超过当前时间的前31天。  **取值范围：** 13位毫秒级时间戳。  **默认取值：** 无。

        :return: The start_time of this OpsExecutionStrategy.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this OpsExecutionStrategy.

        **参数解释：** 开始时间（单位：毫秒数）  **约束限制：** 不超过当前时间的前31天。  **取值范围：** 13位毫秒级时间戳。  **默认取值：** 无。

        :param start_time: The start_time of this OpsExecutionStrategy.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this OpsExecutionStrategy.

        **参数解释：** 结束时间（单位：毫秒数）  **约束限制：** 无。  **取值范围：** 13位毫秒级时间戳。  **默认取值：** 无。

        :return: The end_time of this OpsExecutionStrategy.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this OpsExecutionStrategy.

        **参数解释：** 结束时间（单位：毫秒数）  **约束限制：** 无。  **取值范围：** 13位毫秒级时间戳。  **默认取值：** 无。

        :param end_time: The end_time of this OpsExecutionStrategy.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def repeat(self):
        r"""Gets the repeat of this OpsExecutionStrategy.

        **参数解释：** 是否重复执行。  **约束限制：** 无。  **取值范围：** ture或者false。  **默认取值：** false。

        :return: The repeat of this OpsExecutionStrategy.
        :rtype: bool
        """
        return self._repeat

    @repeat.setter
    def repeat(self, repeat):
        r"""Sets the repeat of this OpsExecutionStrategy.

        **参数解释：** 是否重复执行。  **约束限制：** 无。  **取值范围：** ture或者false。  **默认取值：** false。

        :param repeat: The repeat of this OpsExecutionStrategy.
        :type repeat: bool
        """
        self._repeat = repeat

    @property
    def repeat_type(self):
        r"""Gets the repeat_type of this OpsExecutionStrategy.

        **参数解释：** 重复周期类型。  **约束限制：** 无。  **取值范围：** daily：天重复，weekly：周重复。  **默认取值：** 无。

        :return: The repeat_type of this OpsExecutionStrategy.
        :rtype: str
        """
        return self._repeat_type

    @repeat_type.setter
    def repeat_type(self, repeat_type):
        r"""Sets the repeat_type of this OpsExecutionStrategy.

        **参数解释：** 重复周期类型。  **约束限制：** 无。  **取值范围：** daily：天重复，weekly：周重复。  **默认取值：** 无。

        :param repeat_type: The repeat_type of this OpsExecutionStrategy.
        :type repeat_type: str
        """
        self._repeat_type = repeat_type

    @property
    def repeat_interval(self):
        r"""Gets the repeat_interval of this OpsExecutionStrategy.

        **参数解释：** 重复周期。  **约束限制：** 无。  **取值范围：** 1到6之间的数字。  **默认取值：** 无。

        :return: The repeat_interval of this OpsExecutionStrategy.
        :rtype: int
        """
        return self._repeat_interval

    @repeat_interval.setter
    def repeat_interval(self, repeat_interval):
        r"""Sets the repeat_interval of this OpsExecutionStrategy.

        **参数解释：** 重复周期。  **约束限制：** 无。  **取值范围：** 1到6之间的数字。  **默认取值：** 无。

        :param repeat_interval: The repeat_interval of this OpsExecutionStrategy.
        :type repeat_interval: int
        """
        self._repeat_interval = repeat_interval

    @property
    def day_of_week(self):
        r"""Gets the day_of_week of this OpsExecutionStrategy.

        **参数解释：** 周重复时，每周几执行。  **约束限制：** 仅 repeat_type=weekly 时必填且非 null；repeat_type=daily 时必须为 null（或不上送）。无语义即 null。  **取值范围：** 1到7之间的数字，分别代表周一到周日；daily 场景为 null。  **默认取值：** 无。

        :return: The day_of_week of this OpsExecutionStrategy.
        :rtype: int
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        r"""Sets the day_of_week of this OpsExecutionStrategy.

        **参数解释：** 周重复时，每周几执行。  **约束限制：** 仅 repeat_type=weekly 时必填且非 null；repeat_type=daily 时必须为 null（或不上送）。无语义即 null。  **取值范围：** 1到7之间的数字，分别代表周一到周日；daily 场景为 null。  **默认取值：** 无。

        :param day_of_week: The day_of_week of this OpsExecutionStrategy.
        :type day_of_week: int
        """
        self._day_of_week = day_of_week

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
        if not isinstance(other, OpsExecutionStrategy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
