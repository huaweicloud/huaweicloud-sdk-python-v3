# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchListMetricDataRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metrics': 'list[MetricInfo]',
        'period': 'str',
        'filter': 'str',
        '_from': 'int',
        'to': 'int'
    }

    attribute_map = {
        'metrics': 'metrics',
        'period': 'period',
        'filter': 'filter',
        '_from': 'from',
        'to': 'to'
    }

    def __init__(self, metrics=None, period=None, filter=None, _from=None, to=None):
        r"""BatchListMetricDataRequestBody

        The model defined in huaweicloud sdk

        :param metrics: 指标数据。数组长度最大500
        :type metrics: list[:class:`huaweicloudsdkces.v1.MetricInfo`]
        :param period: 指标监控数据的聚合粒度，取值范围：1，300，1200，3600，14400，86400；1为监控资源的实时数据；300为聚合5分钟粒度数据，表示5分钟一个数据点；1200为聚合20分钟粒度数据，表示20分钟一个数据点；3600为聚合1小时粒度数据，表示1小时一个数据点；14400为聚合4小时粒度数据，表示4小时一个数据点；86400为聚合1天粒度数据，表示1天一个数据点；聚合解释可查看：“[聚合含义](https://support.huaweicloud.com/ces_faq/ces_faq_0009.html)”。 
        :type period: str
        :param filter: **参数解释**： 数据聚合的方式。 **约束限制**： period为1（原始值）时，filter字段不生效，参数值默认为average。period大于1时filter才起作用。 **取值范围**： 支持 average、variance、min、max、sum。 - average： 平均值 - variance：方差 - min：最小值 - max：最大值 - sum：求和 **默认取值**： 不涉及。 
        :type filter: str
        :param _from: 
        :type _from: int
        :param to: 
        :type to: int
        """
        
        

        self._metrics = None
        self._period = None
        self._filter = None
        self.__from = None
        self._to = None
        self.discriminator = None

        self.metrics = metrics
        self.period = period
        self.filter = filter
        self._from = _from
        self.to = to

    @property
    def metrics(self):
        r"""Gets the metrics of this BatchListMetricDataRequestBody.

        指标数据。数组长度最大500

        :return: The metrics of this BatchListMetricDataRequestBody.
        :rtype: list[:class:`huaweicloudsdkces.v1.MetricInfo`]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        r"""Sets the metrics of this BatchListMetricDataRequestBody.

        指标数据。数组长度最大500

        :param metrics: The metrics of this BatchListMetricDataRequestBody.
        :type metrics: list[:class:`huaweicloudsdkces.v1.MetricInfo`]
        """
        self._metrics = metrics

    @property
    def period(self):
        r"""Gets the period of this BatchListMetricDataRequestBody.

        指标监控数据的聚合粒度，取值范围：1，300，1200，3600，14400，86400；1为监控资源的实时数据；300为聚合5分钟粒度数据，表示5分钟一个数据点；1200为聚合20分钟粒度数据，表示20分钟一个数据点；3600为聚合1小时粒度数据，表示1小时一个数据点；14400为聚合4小时粒度数据，表示4小时一个数据点；86400为聚合1天粒度数据，表示1天一个数据点；聚合解释可查看：“[聚合含义](https://support.huaweicloud.com/ces_faq/ces_faq_0009.html)”。 

        :return: The period of this BatchListMetricDataRequestBody.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this BatchListMetricDataRequestBody.

        指标监控数据的聚合粒度，取值范围：1，300，1200，3600，14400，86400；1为监控资源的实时数据；300为聚合5分钟粒度数据，表示5分钟一个数据点；1200为聚合20分钟粒度数据，表示20分钟一个数据点；3600为聚合1小时粒度数据，表示1小时一个数据点；14400为聚合4小时粒度数据，表示4小时一个数据点；86400为聚合1天粒度数据，表示1天一个数据点；聚合解释可查看：“[聚合含义](https://support.huaweicloud.com/ces_faq/ces_faq_0009.html)”。 

        :param period: The period of this BatchListMetricDataRequestBody.
        :type period: str
        """
        self._period = period

    @property
    def filter(self):
        r"""Gets the filter of this BatchListMetricDataRequestBody.

        **参数解释**： 数据聚合的方式。 **约束限制**： period为1（原始值）时，filter字段不生效，参数值默认为average。period大于1时filter才起作用。 **取值范围**： 支持 average、variance、min、max、sum。 - average： 平均值 - variance：方差 - min：最小值 - max：最大值 - sum：求和 **默认取值**： 不涉及。 

        :return: The filter of this BatchListMetricDataRequestBody.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this BatchListMetricDataRequestBody.

        **参数解释**： 数据聚合的方式。 **约束限制**： period为1（原始值）时，filter字段不生效，参数值默认为average。period大于1时filter才起作用。 **取值范围**： 支持 average、variance、min、max、sum。 - average： 平均值 - variance：方差 - min：最小值 - max：最大值 - sum：求和 **默认取值**： 不涉及。 

        :param filter: The filter of this BatchListMetricDataRequestBody.
        :type filter: str
        """
        self._filter = filter

    @property
    def _from(self):
        r"""Gets the _from of this BatchListMetricDataRequestBody.

        :return: The _from of this BatchListMetricDataRequestBody.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this BatchListMetricDataRequestBody.

        :param _from: The _from of this BatchListMetricDataRequestBody.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this BatchListMetricDataRequestBody.

        :return: The to of this BatchListMetricDataRequestBody.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this BatchListMetricDataRequestBody.

        :param to: The to of this BatchListMetricDataRequestBody.
        :type to: int
        """
        self._to = to

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
        if not isinstance(other, BatchListMetricDataRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
