# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatapointForBatchMetric:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max': 'float',
        'min': 'float',
        'average': 'float',
        'sum': 'float',
        'variance': 'float',
        'timestamp': 'int'
    }

    attribute_map = {
        'max': 'max',
        'min': 'min',
        'average': 'average',
        'sum': 'sum',
        'variance': 'variance',
        'timestamp': 'timestamp'
    }

    def __init__(self, max=None, min=None, average=None, sum=None, variance=None, timestamp=None):
        """DatapointForBatchMetric

        The model defined in huaweicloud sdk

        :param max: 聚合周期内指标数据的最大值。
        :type max: float
        :param min: 聚合周期内指标数据的最小值。
        :type min: float
        :param average: 聚合周期内指标数据的平均值。
        :type average: float
        :param sum: 聚合周期内指标数据的求和值。
        :type sum: float
        :param variance: 聚合周期内指标数据的方差。
        :type variance: float
        :param timestamp: 指标采集时间，UNIX时间戳，单位毫秒。
        :type timestamp: int
        """
        
        

        self._max = None
        self._min = None
        self._average = None
        self._sum = None
        self._variance = None
        self._timestamp = None
        self.discriminator = None

        if max is not None:
            self.max = max
        if min is not None:
            self.min = min
        if average is not None:
            self.average = average
        if sum is not None:
            self.sum = sum
        if variance is not None:
            self.variance = variance
        self.timestamp = timestamp

    @property
    def max(self):
        """Gets the max of this DatapointForBatchMetric.

        聚合周期内指标数据的最大值。

        :return: The max of this DatapointForBatchMetric.
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this DatapointForBatchMetric.

        聚合周期内指标数据的最大值。

        :param max: The max of this DatapointForBatchMetric.
        :type max: float
        """
        self._max = max

    @property
    def min(self):
        """Gets the min of this DatapointForBatchMetric.

        聚合周期内指标数据的最小值。

        :return: The min of this DatapointForBatchMetric.
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this DatapointForBatchMetric.

        聚合周期内指标数据的最小值。

        :param min: The min of this DatapointForBatchMetric.
        :type min: float
        """
        self._min = min

    @property
    def average(self):
        """Gets the average of this DatapointForBatchMetric.

        聚合周期内指标数据的平均值。

        :return: The average of this DatapointForBatchMetric.
        :rtype: float
        """
        return self._average

    @average.setter
    def average(self, average):
        """Sets the average of this DatapointForBatchMetric.

        聚合周期内指标数据的平均值。

        :param average: The average of this DatapointForBatchMetric.
        :type average: float
        """
        self._average = average

    @property
    def sum(self):
        """Gets the sum of this DatapointForBatchMetric.

        聚合周期内指标数据的求和值。

        :return: The sum of this DatapointForBatchMetric.
        :rtype: float
        """
        return self._sum

    @sum.setter
    def sum(self, sum):
        """Sets the sum of this DatapointForBatchMetric.

        聚合周期内指标数据的求和值。

        :param sum: The sum of this DatapointForBatchMetric.
        :type sum: float
        """
        self._sum = sum

    @property
    def variance(self):
        """Gets the variance of this DatapointForBatchMetric.

        聚合周期内指标数据的方差。

        :return: The variance of this DatapointForBatchMetric.
        :rtype: float
        """
        return self._variance

    @variance.setter
    def variance(self, variance):
        """Sets the variance of this DatapointForBatchMetric.

        聚合周期内指标数据的方差。

        :param variance: The variance of this DatapointForBatchMetric.
        :type variance: float
        """
        self._variance = variance

    @property
    def timestamp(self):
        """Gets the timestamp of this DatapointForBatchMetric.

        指标采集时间，UNIX时间戳，单位毫秒。

        :return: The timestamp of this DatapointForBatchMetric.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this DatapointForBatchMetric.

        指标采集时间，UNIX时间戳，单位毫秒。

        :param timestamp: The timestamp of this DatapointForBatchMetric.
        :type timestamp: int
        """
        self._timestamp = timestamp

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
        if not isinstance(other, DatapointForBatchMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
