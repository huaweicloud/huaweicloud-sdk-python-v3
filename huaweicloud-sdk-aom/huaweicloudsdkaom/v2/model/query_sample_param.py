# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuerySampleParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'samples': 'list[QuerySample]',
        'statistics': 'list[str]',
        'period': 'int',
        'time_range': 'str'
    }

    attribute_map = {
        'samples': 'samples',
        'statistics': 'statistics',
        'period': 'period',
        'time_range': 'time_range'
    }

    def __init__(self, samples=None, statistics=None, period=None, time_range=None):
        """QuerySampleParam

        The model defined in huaweicloud sdk

        :param samples: 时序数据对象列表。  取值范围：JSON数组大小不超过20。
        :type samples: list[:class:`huaweicloudsdkaom.v2.QuerySample`]
        :param statistics: 统计方式。 取值范围： maximum，minimum，sum，average，sampleCount。
        :type statistics: list[str]
        :param period: 监控数据粒度。 取值范围 枚举值，取值范围： 60，1分钟粒度； 300，5分钟粒度； 900，15分钟粒度； 3600，1小时粒度。
        :type period: int
        :param time_range: 说明： time_range/period≤1440 计算时，time_range和period需换算为相同的单位。 取值范围 格式：开始时间UTC毫秒.结束时间UTC毫秒.时间范围分钟数。开始和结束时间为-1时，表示最近N分钟，N为时间范围分钟取值。 查询时间段，如最近五分钟可以表示为-1.-1.5，固定的时间范围（2017-08-01 08:00 :00到2017-08-02 08:00:00）可以表示为1501545600000.1501632000000.1440。
        :type time_range: str
        """
        
        

        self._samples = None
        self._statistics = None
        self._period = None
        self._time_range = None
        self.discriminator = None

        self.samples = samples
        self.statistics = statistics
        self.period = period
        self.time_range = time_range

    @property
    def samples(self):
        """Gets the samples of this QuerySampleParam.

        时序数据对象列表。  取值范围：JSON数组大小不超过20。

        :return: The samples of this QuerySampleParam.
        :rtype: list[:class:`huaweicloudsdkaom.v2.QuerySample`]
        """
        return self._samples

    @samples.setter
    def samples(self, samples):
        """Sets the samples of this QuerySampleParam.

        时序数据对象列表。  取值范围：JSON数组大小不超过20。

        :param samples: The samples of this QuerySampleParam.
        :type samples: list[:class:`huaweicloudsdkaom.v2.QuerySample`]
        """
        self._samples = samples

    @property
    def statistics(self):
        """Gets the statistics of this QuerySampleParam.

        统计方式。 取值范围： maximum，minimum，sum，average，sampleCount。

        :return: The statistics of this QuerySampleParam.
        :rtype: list[str]
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """Sets the statistics of this QuerySampleParam.

        统计方式。 取值范围： maximum，minimum，sum，average，sampleCount。

        :param statistics: The statistics of this QuerySampleParam.
        :type statistics: list[str]
        """
        self._statistics = statistics

    @property
    def period(self):
        """Gets the period of this QuerySampleParam.

        监控数据粒度。 取值范围 枚举值，取值范围： 60，1分钟粒度； 300，5分钟粒度； 900，15分钟粒度； 3600，1小时粒度。

        :return: The period of this QuerySampleParam.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this QuerySampleParam.

        监控数据粒度。 取值范围 枚举值，取值范围： 60，1分钟粒度； 300，5分钟粒度； 900，15分钟粒度； 3600，1小时粒度。

        :param period: The period of this QuerySampleParam.
        :type period: int
        """
        self._period = period

    @property
    def time_range(self):
        """Gets the time_range of this QuerySampleParam.

        说明： time_range/period≤1440 计算时，time_range和period需换算为相同的单位。 取值范围 格式：开始时间UTC毫秒.结束时间UTC毫秒.时间范围分钟数。开始和结束时间为-1时，表示最近N分钟，N为时间范围分钟取值。 查询时间段，如最近五分钟可以表示为-1.-1.5，固定的时间范围（2017-08-01 08:00 :00到2017-08-02 08:00:00）可以表示为1501545600000.1501632000000.1440。

        :return: The time_range of this QuerySampleParam.
        :rtype: str
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """Sets the time_range of this QuerySampleParam.

        说明： time_range/period≤1440 计算时，time_range和period需换算为相同的单位。 取值范围 格式：开始时间UTC毫秒.结束时间UTC毫秒.时间范围分钟数。开始和结束时间为-1时，表示最近N分钟，N为时间范围分钟取值。 查询时间段，如最近五分钟可以表示为-1.-1.5，固定的时间范围（2017-08-01 08:00 :00到2017-08-02 08:00:00）可以表示为1501545600000.1501632000000.1440。

        :param time_range: The time_range of this QuerySampleParam.
        :type time_range: str
        """
        self._time_range = time_range

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
        if not isinstance(other, QuerySampleParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
