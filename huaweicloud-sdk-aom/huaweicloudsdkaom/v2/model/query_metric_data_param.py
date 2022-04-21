# coding: utf-8

import re
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
        'metrics': 'list[MetricQueryMeritcParam]',
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
        """QueryMetricDataParam

        The model defined in huaweicloud sdk

        :param metrics: 指标对象列表。 取值范围 JSON数组大小不超过20
        :type metrics: list[:class:`huaweicloudsdkaom.v2.MetricQueryMeritcParam`]
        :param period: 监控数据粒度。 取值范围 枚举值，取值范围： 60，1分钟粒度 300，5分钟粒度 900，15分钟粒度 3600，1小时粒度
        :type period: int
        :param statistics: 统计方式。 取值范围 maximum，minimum，sum，average，sampleCount
        :type statistics: list[str]
        :param timerange: 说明： timerange/period≤1440 计算时，timerange和period需换算为相同的单位。 取值范围 格式：开始时间UTC毫秒.结束时间UTC毫秒.时间范围分钟数。开始和结束时间为-1时，表示最近N分钟，N为时间范围分钟取值。 查询时间段，如最近五分钟可以表示为-1.-1.5，固定的时间范围（2017-08-01 08:00 :00到2017-08-02 08:00:00）可以表示为1501545600000.1501632000000.1440。
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
        """Gets the metrics of this QueryMetricDataParam.

        指标对象列表。 取值范围 JSON数组大小不超过20

        :return: The metrics of this QueryMetricDataParam.
        :rtype: list[:class:`huaweicloudsdkaom.v2.MetricQueryMeritcParam`]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this QueryMetricDataParam.

        指标对象列表。 取值范围 JSON数组大小不超过20

        :param metrics: The metrics of this QueryMetricDataParam.
        :type metrics: list[:class:`huaweicloudsdkaom.v2.MetricQueryMeritcParam`]
        """
        self._metrics = metrics

    @property
    def period(self):
        """Gets the period of this QueryMetricDataParam.

        监控数据粒度。 取值范围 枚举值，取值范围： 60，1分钟粒度 300，5分钟粒度 900，15分钟粒度 3600，1小时粒度

        :return: The period of this QueryMetricDataParam.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this QueryMetricDataParam.

        监控数据粒度。 取值范围 枚举值，取值范围： 60，1分钟粒度 300，5分钟粒度 900，15分钟粒度 3600，1小时粒度

        :param period: The period of this QueryMetricDataParam.
        :type period: int
        """
        self._period = period

    @property
    def statistics(self):
        """Gets the statistics of this QueryMetricDataParam.

        统计方式。 取值范围 maximum，minimum，sum，average，sampleCount

        :return: The statistics of this QueryMetricDataParam.
        :rtype: list[str]
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """Sets the statistics of this QueryMetricDataParam.

        统计方式。 取值范围 maximum，minimum，sum，average，sampleCount

        :param statistics: The statistics of this QueryMetricDataParam.
        :type statistics: list[str]
        """
        self._statistics = statistics

    @property
    def timerange(self):
        """Gets the timerange of this QueryMetricDataParam.

        说明： timerange/period≤1440 计算时，timerange和period需换算为相同的单位。 取值范围 格式：开始时间UTC毫秒.结束时间UTC毫秒.时间范围分钟数。开始和结束时间为-1时，表示最近N分钟，N为时间范围分钟取值。 查询时间段，如最近五分钟可以表示为-1.-1.5，固定的时间范围（2017-08-01 08:00 :00到2017-08-02 08:00:00）可以表示为1501545600000.1501632000000.1440。

        :return: The timerange of this QueryMetricDataParam.
        :rtype: str
        """
        return self._timerange

    @timerange.setter
    def timerange(self, timerange):
        """Sets the timerange of this QueryMetricDataParam.

        说明： timerange/period≤1440 计算时，timerange和period需换算为相同的单位。 取值范围 格式：开始时间UTC毫秒.结束时间UTC毫秒.时间范围分钟数。开始和结束时间为-1时，表示最近N分钟，N为时间范围分钟取值。 查询时间段，如最近五分钟可以表示为-1.-1.5，固定的时间范围（2017-08-01 08:00 :00到2017-08-02 08:00:00）可以表示为1501545600000.1501632000000.1440。

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
