# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'average': 'int',
        'max': 'int',
        'min': 'int',
        'sum': 'int',
        'variance': 'int',
        'timestamp': 'int',
        'unit': 'str'
    }

    attribute_map = {
        'average': 'average',
        'max': 'max',
        'min': 'min',
        'sum': 'sum',
        'variance': 'variance',
        'timestamp': 'timestamp',
        'unit': 'unit'
    }

    def __init__(self, average=None, max=None, min=None, sum=None, variance=None, timestamp=None, unit=None):
        """MetricData

        The model defined in huaweicloud sdk

        :param average: 聚合周期内指标数据的平均值，仅当请求参数filter字段值为average时支持。
        :type average: int
        :param max: 聚合周期内指标数据的最大值，仅当请求参数filter字段值为max时支持。
        :type max: int
        :param min: 聚合周期内指标数据的最小值，仅当请求参数filter字段值为min时支持。
        :type min: int
        :param sum: 聚合周期内指标数据的求和值，仅当请求参数filter字段值为sum时支持。
        :type sum: int
        :param variance: 聚合周期内指标数据的方差，仅当请求参数filter字段值为variance时支持。
        :type variance: int
        :param timestamp: 指标采集时间，UNIX时间戳，单位毫秒。
        :type timestamp: int
        :param unit: 指标单位。
        :type unit: str
        """
        
        

        self._average = None
        self._max = None
        self._min = None
        self._sum = None
        self._variance = None
        self._timestamp = None
        self._unit = None
        self.discriminator = None

        if average is not None:
            self.average = average
        if max is not None:
            self.max = max
        if min is not None:
            self.min = min
        if sum is not None:
            self.sum = sum
        if variance is not None:
            self.variance = variance
        if timestamp is not None:
            self.timestamp = timestamp
        if unit is not None:
            self.unit = unit

    @property
    def average(self):
        """Gets the average of this MetricData.

        聚合周期内指标数据的平均值，仅当请求参数filter字段值为average时支持。

        :return: The average of this MetricData.
        :rtype: int
        """
        return self._average

    @average.setter
    def average(self, average):
        """Sets the average of this MetricData.

        聚合周期内指标数据的平均值，仅当请求参数filter字段值为average时支持。

        :param average: The average of this MetricData.
        :type average: int
        """
        self._average = average

    @property
    def max(self):
        """Gets the max of this MetricData.

        聚合周期内指标数据的最大值，仅当请求参数filter字段值为max时支持。

        :return: The max of this MetricData.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this MetricData.

        聚合周期内指标数据的最大值，仅当请求参数filter字段值为max时支持。

        :param max: The max of this MetricData.
        :type max: int
        """
        self._max = max

    @property
    def min(self):
        """Gets the min of this MetricData.

        聚合周期内指标数据的最小值，仅当请求参数filter字段值为min时支持。

        :return: The min of this MetricData.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this MetricData.

        聚合周期内指标数据的最小值，仅当请求参数filter字段值为min时支持。

        :param min: The min of this MetricData.
        :type min: int
        """
        self._min = min

    @property
    def sum(self):
        """Gets the sum of this MetricData.

        聚合周期内指标数据的求和值，仅当请求参数filter字段值为sum时支持。

        :return: The sum of this MetricData.
        :rtype: int
        """
        return self._sum

    @sum.setter
    def sum(self, sum):
        """Sets the sum of this MetricData.

        聚合周期内指标数据的求和值，仅当请求参数filter字段值为sum时支持。

        :param sum: The sum of this MetricData.
        :type sum: int
        """
        self._sum = sum

    @property
    def variance(self):
        """Gets the variance of this MetricData.

        聚合周期内指标数据的方差，仅当请求参数filter字段值为variance时支持。

        :return: The variance of this MetricData.
        :rtype: int
        """
        return self._variance

    @variance.setter
    def variance(self, variance):
        """Sets the variance of this MetricData.

        聚合周期内指标数据的方差，仅当请求参数filter字段值为variance时支持。

        :param variance: The variance of this MetricData.
        :type variance: int
        """
        self._variance = variance

    @property
    def timestamp(self):
        """Gets the timestamp of this MetricData.

        指标采集时间，UNIX时间戳，单位毫秒。

        :return: The timestamp of this MetricData.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this MetricData.

        指标采集时间，UNIX时间戳，单位毫秒。

        :param timestamp: The timestamp of this MetricData.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def unit(self):
        """Gets the unit of this MetricData.

        指标单位。

        :return: The unit of this MetricData.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this MetricData.

        指标单位。

        :param unit: The unit of this MetricData.
        :type unit: str
        """
        self._unit = unit

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
        if not isinstance(other, MetricData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
