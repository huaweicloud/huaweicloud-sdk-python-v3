# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoTimeline:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time': 'int',
        'num': 'int',
        'doc_count_items': 'list[SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoDocCountItems]'
    }

    attribute_map = {
        'time': 'time',
        'num': 'num',
        'doc_count_items': 'docCountItems'
    }

    def __init__(self, time=None, num=None, doc_count_items=None):
        r"""SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoTimeline

        The model defined in huaweicloud sdk

        :param time: **参数解释：** 时间戳（毫秒级），标识统计数据对应的时间点。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type time: int
        :param num: **参数解释：** 该时间点WAF返回该响应码的数量。 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0
        :type num: int
        :param doc_count_items: **参数解释：** 该时间点各响应码的详细统计项。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type doc_count_items: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoDocCountItems`]
        """
        
        

        self._time = None
        self._num = None
        self._doc_count_items = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if num is not None:
            self.num = num
        if doc_count_items is not None:
            self.doc_count_items = doc_count_items

    @property
    def time(self):
        r"""Gets the time of this SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoTimeline.

        **参数解释：** 时间戳（毫秒级），标识统计数据对应的时间点。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The time of this SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoTimeline.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoTimeline.

        **参数解释：** 时间戳（毫秒级），标识统计数据对应的时间点。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param time: The time of this SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoTimeline.
        :type time: int
        """
        self._time = time

    @property
    def num(self):
        r"""Gets the num of this SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoTimeline.

        **参数解释：** 该时间点WAF返回该响应码的数量。 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0

        :return: The num of this SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoTimeline.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        r"""Sets the num of this SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoTimeline.

        **参数解释：** 该时间点WAF返回该响应码的数量。 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0

        :param num: The num of this SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoTimeline.
        :type num: int
        """
        self._num = num

    @property
    def doc_count_items(self):
        r"""Gets the doc_count_items of this SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoTimeline.

        **参数解释：** 该时间点各响应码的详细统计项。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The doc_count_items of this SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoTimeline.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoDocCountItems`]
        """
        return self._doc_count_items

    @doc_count_items.setter
    def doc_count_items(self, doc_count_items):
        r"""Sets the doc_count_items of this SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoTimeline.

        **参数解释：** 该时间点各响应码的详细统计项。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param doc_count_items: The doc_count_items of this SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoTimeline.
        :type doc_count_items: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoDocCountItems`]
        """
        self._doc_count_items = doc_count_items

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
        if not isinstance(other, SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfoTimeline):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
