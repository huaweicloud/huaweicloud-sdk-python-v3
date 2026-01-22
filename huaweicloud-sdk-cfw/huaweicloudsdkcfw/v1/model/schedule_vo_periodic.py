# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduleVOPeriodic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'int',
        'start_time': 'str',
        'end_time': 'str',
        'week_mask': 'list[int]',
        'start_week': 'int',
        'end_week': 'int'
    }

    attribute_map = {
        'type': 'type',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'week_mask': 'week_mask',
        'start_week': 'start_week',
        'end_week': 'end_week'
    }

    def __init__(self, type=None, start_time=None, end_time=None, week_mask=None, start_week=None, end_week=None):
        r"""ScheduleVOPeriodic

        The model defined in huaweicloud sdk

        :param type: **参数解释**： 周期计划类型 **取值范围**： 0：每天 1：每周的某几天 2：每周的一段时间
        :type type: int
        :param start_time: **参数解释**： 周期计划开始时间 **取值范围**： 不涉及
        :type start_time: str
        :param end_time: **参数解释**： 周期计划结束时间 **取值范围**： 不涉及
        :type end_time: str
        :param week_mask: **参数解释**： 每周的某几天 **取值范围**： 不涉及
        :type week_mask: list[int]
        :param start_week: **参数解释**： 每周周期计划开始日 **取值范围**： 不涉及
        :type start_week: int
        :param end_week: **参数解释**： 每周周期计划结束日 **取值范围**： 不涉及
        :type end_week: int
        """
        
        

        self._type = None
        self._start_time = None
        self._end_time = None
        self._week_mask = None
        self._start_week = None
        self._end_week = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if week_mask is not None:
            self.week_mask = week_mask
        if start_week is not None:
            self.start_week = start_week
        if end_week is not None:
            self.end_week = end_week

    @property
    def type(self):
        r"""Gets the type of this ScheduleVOPeriodic.

        **参数解释**： 周期计划类型 **取值范围**： 0：每天 1：每周的某几天 2：每周的一段时间

        :return: The type of this ScheduleVOPeriodic.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ScheduleVOPeriodic.

        **参数解释**： 周期计划类型 **取值范围**： 0：每天 1：每周的某几天 2：每周的一段时间

        :param type: The type of this ScheduleVOPeriodic.
        :type type: int
        """
        self._type = type

    @property
    def start_time(self):
        r"""Gets the start_time of this ScheduleVOPeriodic.

        **参数解释**： 周期计划开始时间 **取值范围**： 不涉及

        :return: The start_time of this ScheduleVOPeriodic.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ScheduleVOPeriodic.

        **参数解释**： 周期计划开始时间 **取值范围**： 不涉及

        :param start_time: The start_time of this ScheduleVOPeriodic.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ScheduleVOPeriodic.

        **参数解释**： 周期计划结束时间 **取值范围**： 不涉及

        :return: The end_time of this ScheduleVOPeriodic.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ScheduleVOPeriodic.

        **参数解释**： 周期计划结束时间 **取值范围**： 不涉及

        :param end_time: The end_time of this ScheduleVOPeriodic.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def week_mask(self):
        r"""Gets the week_mask of this ScheduleVOPeriodic.

        **参数解释**： 每周的某几天 **取值范围**： 不涉及

        :return: The week_mask of this ScheduleVOPeriodic.
        :rtype: list[int]
        """
        return self._week_mask

    @week_mask.setter
    def week_mask(self, week_mask):
        r"""Sets the week_mask of this ScheduleVOPeriodic.

        **参数解释**： 每周的某几天 **取值范围**： 不涉及

        :param week_mask: The week_mask of this ScheduleVOPeriodic.
        :type week_mask: list[int]
        """
        self._week_mask = week_mask

    @property
    def start_week(self):
        r"""Gets the start_week of this ScheduleVOPeriodic.

        **参数解释**： 每周周期计划开始日 **取值范围**： 不涉及

        :return: The start_week of this ScheduleVOPeriodic.
        :rtype: int
        """
        return self._start_week

    @start_week.setter
    def start_week(self, start_week):
        r"""Sets the start_week of this ScheduleVOPeriodic.

        **参数解释**： 每周周期计划开始日 **取值范围**： 不涉及

        :param start_week: The start_week of this ScheduleVOPeriodic.
        :type start_week: int
        """
        self._start_week = start_week

    @property
    def end_week(self):
        r"""Gets the end_week of this ScheduleVOPeriodic.

        **参数解释**： 每周周期计划结束日 **取值范围**： 不涉及

        :return: The end_week of this ScheduleVOPeriodic.
        :rtype: int
        """
        return self._end_week

    @end_week.setter
    def end_week(self, end_week):
        r"""Sets the end_week of this ScheduleVOPeriodic.

        **参数解释**： 每周周期计划结束日 **取值范围**： 不涉及

        :param end_week: The end_week of this ScheduleVOPeriodic.
        :type end_week: int
        """
        self._end_week = end_week

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
        if not isinstance(other, ScheduleVOPeriodic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
