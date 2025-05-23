# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryMetricDataParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metrics': 'list[MetricQueryMetricParam]',
        'period': 'int',
        'statistics': 'list[str]',
        'timerange': 'str'
    }

    attribute_map = {
        'metrics': 'metrics',
        'period': 'period',
        'statistics': 'statistics',
        'timerange': 'timerange'
    }

    def __init__(self, metrics=None, period=None, statistics=None, timerange=None):
        r"""QueryMetricDataParam

        The model defined in huaweicloud sdk

        :param metrics: 指标对象列表。 取值范围 JSON数组大小不超过20
        :type metrics: list[:class:`huaweicloudsdkaom.v2.MetricQueryMetricParam`]
        :param period: 监控数据粒度。取值范围（枚举）：60（表示粒度为1分钟），300（表示粒度为5分钟），900（表示粒度为15分钟），3600（表示粒度为1小时）。
        :type period: int
        :param statistics: 统计方式。 取值范围 maximum，minimum，sum，average，sampleCount
        :type statistics: list[str]
        :param timerange: timeRange用于指标查询时间范围，主要用于解决客户端时间和服务端时间不一致情况下，查询最近N分钟的数据。另可用于精确查询某一段时间的数据。   如：   - -1.-1.60(表示最近60分钟)，不管当前客户端是什么时间，都以服务端时间为准查询最近60分钟。   - 1650852000000.1650852300000.5(表示GMT+8 2022-04-25 10:00:00至2022-04-25 10:05:00指定的5分钟)   格式：   startTimeInMillis.endTimeInMillis.durationInMinutes   参数解释：   - startTimeInMillis: 查询的开始时间，格式为UTC毫秒，如果指定为-1，服务端将按(endTimeInMillis - durationInMinutes * 60 * 1000)计算开始时间。如-1.1650852300000.5，则相当于1650852000000.1650852300000.5   - endTimeInMillis: 查询的结束时间，格式为UTC毫秒，如果指定为-1，服务端将按(startTimeInMillis + durationInMinutes * 60 * 1000)计算结束时间，如果计算出的结束时间大于当前系统时间，则使用当前系统时间。如1650852000000.-1.5，则相当于1650852000000.1650852300000.5   - durationInMinutes：查询时间的跨度分钟数。 取值范围大于0并且大于等于(endTimeInMillis - startTimeInMillis) / (60 * 1000) - 1。当开始时间与结束时间都设置为-1时，系统会将结束时间设置为当前时间UTC毫秒值，并按(endTimeInMillis - durationInMinutes * 60 * 1000)计算开始时间。如：-1.-1.60(表示最近60分钟)   约束：   单次请求中，查询时长与周期需要满足以下条件: durationInMinutes * 60 / period &lt;&#x3D; 1440
        :type timerange: str
        """
        
        

        self._metrics = None
        self._period = None
        self._statistics = None
        self._timerange = None
        self.discriminator = None

        self.metrics = metrics
        self.period = period
        self.statistics = statistics
        self.timerange = timerange

    @property
    def metrics(self):
        r"""Gets the metrics of this QueryMetricDataParam.

        指标对象列表。 取值范围 JSON数组大小不超过20

        :return: The metrics of this QueryMetricDataParam.
        :rtype: list[:class:`huaweicloudsdkaom.v2.MetricQueryMetricParam`]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        r"""Sets the metrics of this QueryMetricDataParam.

        指标对象列表。 取值范围 JSON数组大小不超过20

        :param metrics: The metrics of this QueryMetricDataParam.
        :type metrics: list[:class:`huaweicloudsdkaom.v2.MetricQueryMetricParam`]
        """
        self._metrics = metrics

    @property
    def period(self):
        r"""Gets the period of this QueryMetricDataParam.

        监控数据粒度。取值范围（枚举）：60（表示粒度为1分钟），300（表示粒度为5分钟），900（表示粒度为15分钟），3600（表示粒度为1小时）。

        :return: The period of this QueryMetricDataParam.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this QueryMetricDataParam.

        监控数据粒度。取值范围（枚举）：60（表示粒度为1分钟），300（表示粒度为5分钟），900（表示粒度为15分钟），3600（表示粒度为1小时）。

        :param period: The period of this QueryMetricDataParam.
        :type period: int
        """
        self._period = period

    @property
    def statistics(self):
        r"""Gets the statistics of this QueryMetricDataParam.

        统计方式。 取值范围 maximum，minimum，sum，average，sampleCount

        :return: The statistics of this QueryMetricDataParam.
        :rtype: list[str]
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        r"""Sets the statistics of this QueryMetricDataParam.

        统计方式。 取值范围 maximum，minimum，sum，average，sampleCount

        :param statistics: The statistics of this QueryMetricDataParam.
        :type statistics: list[str]
        """
        self._statistics = statistics

    @property
    def timerange(self):
        r"""Gets the timerange of this QueryMetricDataParam.

        timeRange用于指标查询时间范围，主要用于解决客户端时间和服务端时间不一致情况下，查询最近N分钟的数据。另可用于精确查询某一段时间的数据。   如：   - -1.-1.60(表示最近60分钟)，不管当前客户端是什么时间，都以服务端时间为准查询最近60分钟。   - 1650852000000.1650852300000.5(表示GMT+8 2022-04-25 10:00:00至2022-04-25 10:05:00指定的5分钟)   格式：   startTimeInMillis.endTimeInMillis.durationInMinutes   参数解释：   - startTimeInMillis: 查询的开始时间，格式为UTC毫秒，如果指定为-1，服务端将按(endTimeInMillis - durationInMinutes * 60 * 1000)计算开始时间。如-1.1650852300000.5，则相当于1650852000000.1650852300000.5   - endTimeInMillis: 查询的结束时间，格式为UTC毫秒，如果指定为-1，服务端将按(startTimeInMillis + durationInMinutes * 60 * 1000)计算结束时间，如果计算出的结束时间大于当前系统时间，则使用当前系统时间。如1650852000000.-1.5，则相当于1650852000000.1650852300000.5   - durationInMinutes：查询时间的跨度分钟数。 取值范围大于0并且大于等于(endTimeInMillis - startTimeInMillis) / (60 * 1000) - 1。当开始时间与结束时间都设置为-1时，系统会将结束时间设置为当前时间UTC毫秒值，并按(endTimeInMillis - durationInMinutes * 60 * 1000)计算开始时间。如：-1.-1.60(表示最近60分钟)   约束：   单次请求中，查询时长与周期需要满足以下条件: durationInMinutes * 60 / period <= 1440

        :return: The timerange of this QueryMetricDataParam.
        :rtype: str
        """
        return self._timerange

    @timerange.setter
    def timerange(self, timerange):
        r"""Sets the timerange of this QueryMetricDataParam.

        timeRange用于指标查询时间范围，主要用于解决客户端时间和服务端时间不一致情况下，查询最近N分钟的数据。另可用于精确查询某一段时间的数据。   如：   - -1.-1.60(表示最近60分钟)，不管当前客户端是什么时间，都以服务端时间为准查询最近60分钟。   - 1650852000000.1650852300000.5(表示GMT+8 2022-04-25 10:00:00至2022-04-25 10:05:00指定的5分钟)   格式：   startTimeInMillis.endTimeInMillis.durationInMinutes   参数解释：   - startTimeInMillis: 查询的开始时间，格式为UTC毫秒，如果指定为-1，服务端将按(endTimeInMillis - durationInMinutes * 60 * 1000)计算开始时间。如-1.1650852300000.5，则相当于1650852000000.1650852300000.5   - endTimeInMillis: 查询的结束时间，格式为UTC毫秒，如果指定为-1，服务端将按(startTimeInMillis + durationInMinutes * 60 * 1000)计算结束时间，如果计算出的结束时间大于当前系统时间，则使用当前系统时间。如1650852000000.-1.5，则相当于1650852000000.1650852300000.5   - durationInMinutes：查询时间的跨度分钟数。 取值范围大于0并且大于等于(endTimeInMillis - startTimeInMillis) / (60 * 1000) - 1。当开始时间与结束时间都设置为-1时，系统会将结束时间设置为当前时间UTC毫秒值，并按(endTimeInMillis - durationInMinutes * 60 * 1000)计算开始时间。如：-1.-1.60(表示最近60分钟)   约束：   单次请求中，查询时长与周期需要满足以下条件: durationInMinutes * 60 / period <= 1440

        :param timerange: The timerange of this QueryMetricDataParam.
        :type timerange: str
        """
        self._timerange = timerange

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
        if not isinstance(other, QueryMetricDataParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
