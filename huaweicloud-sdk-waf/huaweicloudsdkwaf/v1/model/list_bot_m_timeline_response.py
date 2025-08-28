# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBotMTimelineResponse(SdkResponse):

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
        'time_span': 'int',
        'timelines': 'list[BotRequestTimeline]'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'time_span': 'time_span',
        'timelines': 'timelines'
    }

    def __init__(self, start_time=None, end_time=None, time_span=None, timelines=None):
        r"""ListBotMTimelineResponse

        The model defined in huaweicloud sdk

        :param start_time: **参数解释：** 统计开始时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type start_time: int
        :param end_time: **参数解释：** 统计结束时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type end_time: int
        :param time_span: **参数解释：** 时间间隔（如1h表示每小时） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type time_span: int
        :param timelines: 
        :type timelines: list[:class:`huaweicloudsdkwaf.v1.BotRequestTimeline`]
        """
        
        super(ListBotMTimelineResponse, self).__init__()

        self._start_time = None
        self._end_time = None
        self._time_span = None
        self._timelines = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if time_span is not None:
            self.time_span = time_span
        if timelines is not None:
            self.timelines = timelines

    @property
    def start_time(self):
        r"""Gets the start_time of this ListBotMTimelineResponse.

        **参数解释：** 统计开始时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The start_time of this ListBotMTimelineResponse.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListBotMTimelineResponse.

        **参数解释：** 统计开始时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param start_time: The start_time of this ListBotMTimelineResponse.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListBotMTimelineResponse.

        **参数解释：** 统计结束时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The end_time of this ListBotMTimelineResponse.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListBotMTimelineResponse.

        **参数解释：** 统计结束时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param end_time: The end_time of this ListBotMTimelineResponse.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def time_span(self):
        r"""Gets the time_span of this ListBotMTimelineResponse.

        **参数解释：** 时间间隔（如1h表示每小时） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The time_span of this ListBotMTimelineResponse.
        :rtype: int
        """
        return self._time_span

    @time_span.setter
    def time_span(self, time_span):
        r"""Sets the time_span of this ListBotMTimelineResponse.

        **参数解释：** 时间间隔（如1h表示每小时） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param time_span: The time_span of this ListBotMTimelineResponse.
        :type time_span: int
        """
        self._time_span = time_span

    @property
    def timelines(self):
        r"""Gets the timelines of this ListBotMTimelineResponse.

        :return: The timelines of this ListBotMTimelineResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.BotRequestTimeline`]
        """
        return self._timelines

    @timelines.setter
    def timelines(self, timelines):
        r"""Sets the timelines of this ListBotMTimelineResponse.

        :param timelines: The timelines of this ListBotMTimelineResponse.
        :type timelines: list[:class:`huaweicloudsdkwaf.v1.BotRequestTimeline`]
        """
        self._timelines = timelines

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
        if not isinstance(other, ListBotMTimelineResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
