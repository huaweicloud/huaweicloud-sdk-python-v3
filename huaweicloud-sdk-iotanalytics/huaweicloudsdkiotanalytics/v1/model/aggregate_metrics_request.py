# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AggregateMetricsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time_span': 'TimeSpanDT',
        'interval': 'str',
        'offset': 'str',
        'tags': 'dict(str, object)',
        'property_filter': 'list[PropertyFilter]',
        'metrics': 'list[DTAggregateMetrics]',
        'limit': 'int'
    }

    attribute_map = {
        'time_span': 'time_span',
        'interval': 'interval',
        'offset': 'offset',
        'tags': 'tags',
        'property_filter': 'property_filter',
        'metrics': 'metrics',
        'limit': 'limit'
    }

    def __init__(self, time_span=None, interval=None, offset=None, tags=None, property_filter=None, metrics=None, limit=None):
        r"""AggregateMetricsRequest

        The model defined in huaweicloud sdk

        :param time_span: 
        :type time_span: :class:`huaweicloudsdkiotanalytics.v1.TimeSpanDT`
        :param interval: 聚合时间间隔，正则：\&quot;^[1-9][0-9]*[dhms]$\&quot;，示例：\&quot;1d|1h|10m|10s\&quot;
        :type interval: str
        :param offset: 聚合时间偏移量，需要小于interval，正则： \&quot;^[1-9][0-9]*[hms]$\&quot;，示例： \&quot;1h|10m|10s\&quot;
        :type offset: str
        :param tags: 对property按指定tags标签进行过滤查询，填入资产标签属性的属性名与属性值，不可为空，例如 {\&quot;tagPropertyA\&quot;: \&quot;id0001\&quot;}；注意，标签过滤只对打上标签时刻之后的数据生效，打标签之前的数据不能通过标签过滤
        :type tags: dict(str, object)
        :param property_filter: 属性过滤器，最多5个
        :type property_filter: list[:class:`huaweicloudsdkiotanalytics.v1.PropertyFilter`]
        :param metrics: 聚合查询指标列表，对资产属性进行聚合查询得到指标
        :type metrics: list[:class:`huaweicloudsdkiotanalytics.v1.DTAggregateMetrics`]
        :param limit: 返回值个数限制，最多2000个
        :type limit: int
        """
        
        

        self._time_span = None
        self._interval = None
        self._offset = None
        self._tags = None
        self._property_filter = None
        self._metrics = None
        self._limit = None
        self.discriminator = None

        if time_span is not None:
            self.time_span = time_span
        self.interval = interval
        if offset is not None:
            self.offset = offset
        if tags is not None:
            self.tags = tags
        if property_filter is not None:
            self.property_filter = property_filter
        self.metrics = metrics
        if limit is not None:
            self.limit = limit

    @property
    def time_span(self):
        r"""Gets the time_span of this AggregateMetricsRequest.

        :return: The time_span of this AggregateMetricsRequest.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.TimeSpanDT`
        """
        return self._time_span

    @time_span.setter
    def time_span(self, time_span):
        r"""Sets the time_span of this AggregateMetricsRequest.

        :param time_span: The time_span of this AggregateMetricsRequest.
        :type time_span: :class:`huaweicloudsdkiotanalytics.v1.TimeSpanDT`
        """
        self._time_span = time_span

    @property
    def interval(self):
        r"""Gets the interval of this AggregateMetricsRequest.

        聚合时间间隔，正则：\"^[1-9][0-9]*[dhms]$\"，示例：\"1d|1h|10m|10s\"

        :return: The interval of this AggregateMetricsRequest.
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this AggregateMetricsRequest.

        聚合时间间隔，正则：\"^[1-9][0-9]*[dhms]$\"，示例：\"1d|1h|10m|10s\"

        :param interval: The interval of this AggregateMetricsRequest.
        :type interval: str
        """
        self._interval = interval

    @property
    def offset(self):
        r"""Gets the offset of this AggregateMetricsRequest.

        聚合时间偏移量，需要小于interval，正则： \"^[1-9][0-9]*[hms]$\"，示例： \"1h|10m|10s\"

        :return: The offset of this AggregateMetricsRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this AggregateMetricsRequest.

        聚合时间偏移量，需要小于interval，正则： \"^[1-9][0-9]*[hms]$\"，示例： \"1h|10m|10s\"

        :param offset: The offset of this AggregateMetricsRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def tags(self):
        r"""Gets the tags of this AggregateMetricsRequest.

        对property按指定tags标签进行过滤查询，填入资产标签属性的属性名与属性值，不可为空，例如 {\"tagPropertyA\": \"id0001\"}；注意，标签过滤只对打上标签时刻之后的数据生效，打标签之前的数据不能通过标签过滤

        :return: The tags of this AggregateMetricsRequest.
        :rtype: dict(str, object)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this AggregateMetricsRequest.

        对property按指定tags标签进行过滤查询，填入资产标签属性的属性名与属性值，不可为空，例如 {\"tagPropertyA\": \"id0001\"}；注意，标签过滤只对打上标签时刻之后的数据生效，打标签之前的数据不能通过标签过滤

        :param tags: The tags of this AggregateMetricsRequest.
        :type tags: dict(str, object)
        """
        self._tags = tags

    @property
    def property_filter(self):
        r"""Gets the property_filter of this AggregateMetricsRequest.

        属性过滤器，最多5个

        :return: The property_filter of this AggregateMetricsRequest.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.PropertyFilter`]
        """
        return self._property_filter

    @property_filter.setter
    def property_filter(self, property_filter):
        r"""Sets the property_filter of this AggregateMetricsRequest.

        属性过滤器，最多5个

        :param property_filter: The property_filter of this AggregateMetricsRequest.
        :type property_filter: list[:class:`huaweicloudsdkiotanalytics.v1.PropertyFilter`]
        """
        self._property_filter = property_filter

    @property
    def metrics(self):
        r"""Gets the metrics of this AggregateMetricsRequest.

        聚合查询指标列表，对资产属性进行聚合查询得到指标

        :return: The metrics of this AggregateMetricsRequest.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.DTAggregateMetrics`]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        r"""Sets the metrics of this AggregateMetricsRequest.

        聚合查询指标列表，对资产属性进行聚合查询得到指标

        :param metrics: The metrics of this AggregateMetricsRequest.
        :type metrics: list[:class:`huaweicloudsdkiotanalytics.v1.DTAggregateMetrics`]
        """
        self._metrics = metrics

    @property
    def limit(self):
        r"""Gets the limit of this AggregateMetricsRequest.

        返回值个数限制，最多2000个

        :return: The limit of this AggregateMetricsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this AggregateMetricsRequest.

        返回值个数限制，最多2000个

        :param limit: The limit of this AggregateMetricsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, AggregateMetricsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
