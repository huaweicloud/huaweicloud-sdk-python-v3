# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomDate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start': 'int',
        'start_unit': 'str',
        'end': 'int',
        'end_unit': 'str'
    }

    attribute_map = {
        'start': 'start',
        'start_unit': 'start_unit',
        'end': 'end',
        'end_unit': 'end_unit'
    }

    def __init__(self, start=None, start_unit=None, end=None, end_unit=None):
        r"""CustomDate

        The model defined in huaweicloud sdk

        :param start: **参数解释：** 查询起始时间相对于告警计划执行时间的偏移量数值。 **约束限制：** 根据start_unit字段的单位将有不同的取值范围，根据单位将start换算为时间不超过1天。 **取值范围：** start_unit取值为second，start取值范围为 1-86400； start_unit取值为minute，start取值范围为 1-1440； start_unit取值为hour，start取值范围为 1-24。 **默认取值：** -无。
        :type start: int
        :param start_unit: **参数解释：** 查询起始时间相对于告警计划执行时间的偏移量单位。 **约束限制：** 整点时间即is_time_range_relative为false时start_unit不支持second。 **取值范围：** - hour - minute - second **默认取值：** minute
        :type start_unit: str
        :param end: **参数解释：** 查询结束时间相对于告警计划执行时间的偏移量数值。 **约束限制：** 根据end_unit字段的单位将有不同的取值范围，根据单位将end换算为时间不超过1天； **取值范围：** end_unit取值为second，endt取值范围为 0-86399； end_unit取值为minute，end取值范围为 0-1439； end_unit取值为hour，end取值范围为 0-23。 **默认取值：** -无。
        :type end: int
        :param end_unit: **参数解释：** 查询结束时间相对于告警计划执行时间的偏移量单位。 **约束限制：** 整点时间即is_time_range_relative为false时end_unit不支持second。 **取值范围：** - hour - minute - second **默认取值：** minute
        :type end_unit: str
        """
        
        

        self._start = None
        self._start_unit = None
        self._end = None
        self._end_unit = None
        self.discriminator = None

        self.start = start
        self.start_unit = start_unit
        self.end = end
        self.end_unit = end_unit

    @property
    def start(self):
        r"""Gets the start of this CustomDate.

        **参数解释：** 查询起始时间相对于告警计划执行时间的偏移量数值。 **约束限制：** 根据start_unit字段的单位将有不同的取值范围，根据单位将start换算为时间不超过1天。 **取值范围：** start_unit取值为second，start取值范围为 1-86400； start_unit取值为minute，start取值范围为 1-1440； start_unit取值为hour，start取值范围为 1-24。 **默认取值：** -无。

        :return: The start of this CustomDate.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this CustomDate.

        **参数解释：** 查询起始时间相对于告警计划执行时间的偏移量数值。 **约束限制：** 根据start_unit字段的单位将有不同的取值范围，根据单位将start换算为时间不超过1天。 **取值范围：** start_unit取值为second，start取值范围为 1-86400； start_unit取值为minute，start取值范围为 1-1440； start_unit取值为hour，start取值范围为 1-24。 **默认取值：** -无。

        :param start: The start of this CustomDate.
        :type start: int
        """
        self._start = start

    @property
    def start_unit(self):
        r"""Gets the start_unit of this CustomDate.

        **参数解释：** 查询起始时间相对于告警计划执行时间的偏移量单位。 **约束限制：** 整点时间即is_time_range_relative为false时start_unit不支持second。 **取值范围：** - hour - minute - second **默认取值：** minute

        :return: The start_unit of this CustomDate.
        :rtype: str
        """
        return self._start_unit

    @start_unit.setter
    def start_unit(self, start_unit):
        r"""Sets the start_unit of this CustomDate.

        **参数解释：** 查询起始时间相对于告警计划执行时间的偏移量单位。 **约束限制：** 整点时间即is_time_range_relative为false时start_unit不支持second。 **取值范围：** - hour - minute - second **默认取值：** minute

        :param start_unit: The start_unit of this CustomDate.
        :type start_unit: str
        """
        self._start_unit = start_unit

    @property
    def end(self):
        r"""Gets the end of this CustomDate.

        **参数解释：** 查询结束时间相对于告警计划执行时间的偏移量数值。 **约束限制：** 根据end_unit字段的单位将有不同的取值范围，根据单位将end换算为时间不超过1天； **取值范围：** end_unit取值为second，endt取值范围为 0-86399； end_unit取值为minute，end取值范围为 0-1439； end_unit取值为hour，end取值范围为 0-23。 **默认取值：** -无。

        :return: The end of this CustomDate.
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        r"""Sets the end of this CustomDate.

        **参数解释：** 查询结束时间相对于告警计划执行时间的偏移量数值。 **约束限制：** 根据end_unit字段的单位将有不同的取值范围，根据单位将end换算为时间不超过1天； **取值范围：** end_unit取值为second，endt取值范围为 0-86399； end_unit取值为minute，end取值范围为 0-1439； end_unit取值为hour，end取值范围为 0-23。 **默认取值：** -无。

        :param end: The end of this CustomDate.
        :type end: int
        """
        self._end = end

    @property
    def end_unit(self):
        r"""Gets the end_unit of this CustomDate.

        **参数解释：** 查询结束时间相对于告警计划执行时间的偏移量单位。 **约束限制：** 整点时间即is_time_range_relative为false时end_unit不支持second。 **取值范围：** - hour - minute - second **默认取值：** minute

        :return: The end_unit of this CustomDate.
        :rtype: str
        """
        return self._end_unit

    @end_unit.setter
    def end_unit(self, end_unit):
        r"""Sets the end_unit of this CustomDate.

        **参数解释：** 查询结束时间相对于告警计划执行时间的偏移量单位。 **约束限制：** 整点时间即is_time_range_relative为false时end_unit不支持second。 **取值范围：** - hour - minute - second **默认取值：** minute

        :param end_unit: The end_unit of this CustomDate.
        :type end_unit: str
        """
        self._end_unit = end_unit

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
        if not isinstance(other, CustomDate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
