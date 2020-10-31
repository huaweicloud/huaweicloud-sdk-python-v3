# coding: utf-8

import pprint
import re

import six





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
        '_from': 'int',
        'to': 'int',
        'period': 'str',
        'filter': 'str'
    }

    attribute_map = {
        'metrics': 'metrics',
        '_from': 'from',
        'to': 'to',
        'period': 'period',
        'filter': 'filter'
    }

    def __init__(self, metrics=None, _from=None, to=None, period=None, filter=None):
        """BatchListMetricDataRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._metrics = None
        self.__from = None
        self._to = None
        self._period = None
        self._filter = None
        self.discriminator = None

        self.metrics = metrics
        self._from = _from
        self.to = to
        self.period = period
        self.filter = filter

    @property
    def metrics(self):
        """Gets the metrics of this BatchListMetricDataRequestBody.

        指标数据。数组长度最大10

        :return: The metrics of this BatchListMetricDataRequestBody.
        :rtype: list[MetricInfo]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this BatchListMetricDataRequestBody.

        指标数据。数组长度最大10

        :param metrics: The metrics of this BatchListMetricDataRequestBody.
        :type: list[MetricInfo]
        """
        self._metrics = metrics

    @property
    def _from(self):
        """Gets the _from of this BatchListMetricDataRequestBody.

        查询数据起始时间，UNIX时间戳，单位毫秒。建议from的值相对于当前时间向前偏移至少1个周期。由于聚合运算的过程是将一个聚合周期范围内的数据点聚合到周期起始边界上，如果将from和to的范围设置在聚合周期内，会因为聚合未完成而造成查询数据为空，所以建议from参数相对于当前时间向前偏移至少1个周期。以5分钟聚合周期为例：假设当前时间点为10:35，10:30~10:35之间的原始数据会被聚合到10:30这个点上，所以查询5分钟数据点时from参数应为10:30或之前。 说明： 云监控会根据所选择的聚合粒度向前取整from参数。

        :return: The _from of this BatchListMetricDataRequestBody.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this BatchListMetricDataRequestBody.

        查询数据起始时间，UNIX时间戳，单位毫秒。建议from的值相对于当前时间向前偏移至少1个周期。由于聚合运算的过程是将一个聚合周期范围内的数据点聚合到周期起始边界上，如果将from和to的范围设置在聚合周期内，会因为聚合未完成而造成查询数据为空，所以建议from参数相对于当前时间向前偏移至少1个周期。以5分钟聚合周期为例：假设当前时间点为10:35，10:30~10:35之间的原始数据会被聚合到10:30这个点上，所以查询5分钟数据点时from参数应为10:30或之前。 说明： 云监控会根据所选择的聚合粒度向前取整from参数。

        :param _from: The _from of this BatchListMetricDataRequestBody.
        :type: int
        """
        self.__from = _from

    @property
    def to(self):
        """Gets the to of this BatchListMetricDataRequestBody.

        查询数据截止时间UNIX时间戳，单位毫秒。from必须小于to。

        :return: The to of this BatchListMetricDataRequestBody.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this BatchListMetricDataRequestBody.

        查询数据截止时间UNIX时间戳，单位毫秒。from必须小于to。

        :param to: The to of this BatchListMetricDataRequestBody.
        :type: int
        """
        self._to = to

    @property
    def period(self):
        """Gets the period of this BatchListMetricDataRequestBody.

        监控数据粒度。  取值范围：  \"1\"，原始数据 \"300\"，5分钟粒度 \"1200\"，20分钟粒度 \"3600\"，1小时粒度 \"14400\"，4小时粒度 \"86400\"，1天粒度

        :return: The period of this BatchListMetricDataRequestBody.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this BatchListMetricDataRequestBody.

        监控数据粒度。  取值范围：  \"1\"，原始数据 \"300\"，5分钟粒度 \"1200\"，20分钟粒度 \"3600\"，1小时粒度 \"14400\"，4小时粒度 \"86400\"，1天粒度

        :param period: The period of this BatchListMetricDataRequestBody.
        :type: str
        """
        self._period = period

    @property
    def filter(self):
        """Gets the filter of this BatchListMetricDataRequestBody.

        数据聚合方式。  支持的值为max, min, average, sum, variance。 filter参数的值不会影响原始数据（period为1）的查询结果。

        :return: The filter of this BatchListMetricDataRequestBody.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this BatchListMetricDataRequestBody.

        数据聚合方式。  支持的值为max, min, average, sum, variance。 filter参数的值不会影响原始数据（period为1）的查询结果。

        :param filter: The filter of this BatchListMetricDataRequestBody.
        :type: str
        """
        self._filter = filter

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchListMetricDataRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
