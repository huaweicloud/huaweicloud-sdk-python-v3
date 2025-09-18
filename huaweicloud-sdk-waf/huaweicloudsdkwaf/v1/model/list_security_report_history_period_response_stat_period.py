# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityReportHistoryPeriodResponseStatPeriod:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'begin_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'begin_time': 'begin_time',
        'end_time': 'end_time'
    }

    def __init__(self, begin_time=None, end_time=None):
        r"""ListSecurityReportHistoryPeriodResponseStatPeriod

        The model defined in huaweicloud sdk

        :param begin_time: **参数解释：** 开始时间，统计周期的起始时间戳（毫秒级）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type begin_time: int
        :param end_time: **参数解释：** 结束时间，统计周期的终止时间戳（毫秒级）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type end_time: int
        """
        
        

        self._begin_time = None
        self._end_time = None
        self.discriminator = None

        self.begin_time = begin_time
        self.end_time = end_time

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ListSecurityReportHistoryPeriodResponseStatPeriod.

        **参数解释：** 开始时间，统计周期的起始时间戳（毫秒级）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The begin_time of this ListSecurityReportHistoryPeriodResponseStatPeriod.
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ListSecurityReportHistoryPeriodResponseStatPeriod.

        **参数解释：** 开始时间，统计周期的起始时间戳（毫秒级）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param begin_time: The begin_time of this ListSecurityReportHistoryPeriodResponseStatPeriod.
        :type begin_time: int
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListSecurityReportHistoryPeriodResponseStatPeriod.

        **参数解释：** 结束时间，统计周期的终止时间戳（毫秒级）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The end_time of this ListSecurityReportHistoryPeriodResponseStatPeriod.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListSecurityReportHistoryPeriodResponseStatPeriod.

        **参数解释：** 结束时间，统计周期的终止时间戳（毫秒级）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param end_time: The end_time of this ListSecurityReportHistoryPeriodResponseStatPeriod.
        :type end_time: int
        """
        self._end_time = end_time

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
        if not isinstance(other, ListSecurityReportHistoryPeriodResponseStatPeriod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
