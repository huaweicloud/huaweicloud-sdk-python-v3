# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatisticsPVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'start_time': 'startTime',
        'end_time': 'endTime'
    }

    def __init__(self, start_time=None, end_time=None):
        r"""StatisticsPVO

        The model defined in huaweicloud sdk

        :param start_time: **参数解释：**  统计区间的开始时间，用于指定统计时间区间的起始点。  **约束限制：**  不能为空，且必须早于或等于endTime。  **取值范围：**  UTC标准时间格式，格式为yyyy-MM-ddTHH:mm:ss.SSSZ。  **默认取值：**  不涉及。
        :type start_time: str
        :param end_time: **参数解释：**  统计区间的结束时间，用于指定统计时间区间的结束点。  **约束限制：**  不能为空，且必须晚于或等于startTime。  **取值范围：**  UTC标准时间格式，格式为yyyy-MM-ddTHH:mm:ss.SSSZ。  **默认取值：**  不涉及。
        :type end_time: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time

    @property
    def start_time(self):
        r"""Gets the start_time of this StatisticsPVO.

        **参数解释：**  统计区间的开始时间，用于指定统计时间区间的起始点。  **约束限制：**  不能为空，且必须早于或等于endTime。  **取值范围：**  UTC标准时间格式，格式为yyyy-MM-ddTHH:mm:ss.SSSZ。  **默认取值：**  不涉及。

        :return: The start_time of this StatisticsPVO.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this StatisticsPVO.

        **参数解释：**  统计区间的开始时间，用于指定统计时间区间的起始点。  **约束限制：**  不能为空，且必须早于或等于endTime。  **取值范围：**  UTC标准时间格式，格式为yyyy-MM-ddTHH:mm:ss.SSSZ。  **默认取值：**  不涉及。

        :param start_time: The start_time of this StatisticsPVO.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this StatisticsPVO.

        **参数解释：**  统计区间的结束时间，用于指定统计时间区间的结束点。  **约束限制：**  不能为空，且必须晚于或等于startTime。  **取值范围：**  UTC标准时间格式，格式为yyyy-MM-ddTHH:mm:ss.SSSZ。  **默认取值：**  不涉及。

        :return: The end_time of this StatisticsPVO.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this StatisticsPVO.

        **参数解释：**  统计区间的结束时间，用于指定统计时间区间的结束点。  **约束限制：**  不能为空，且必须晚于或等于startTime。  **取值范围：**  UTC标准时间格式，格式为yyyy-MM-ddTHH:mm:ss.SSSZ。  **默认取值：**  不涉及。

        :param end_time: The end_time of this StatisticsPVO.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, StatisticsPVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
