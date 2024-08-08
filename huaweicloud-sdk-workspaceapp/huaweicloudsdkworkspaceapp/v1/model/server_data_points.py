# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerDataPoints:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'average': 'float',
        'max': 'float',
        'min': 'float',
        'sum': 'float',
        'variance': 'float',
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
        """ServerDataPoints

        The model defined in huaweicloud sdk

        :param average: 聚合周期内指标数据的平均值。
        :type average: float
        :param max: 聚合周期内指标数据的最大值。
        :type max: float
        :param min: 聚合周期内指标数据的最小值。
        :type min: float
        :param sum: 聚合周期内指标数据的求和值。
        :type sum: float
        :param variance: 聚合周期内指标数据的方差。
        :type variance: float
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
        """Gets the average of this ServerDataPoints.

        聚合周期内指标数据的平均值。

        :return: The average of this ServerDataPoints.
        :rtype: float
        """
        return self._average

    @average.setter
    def average(self, average):
        """Sets the average of this ServerDataPoints.

        聚合周期内指标数据的平均值。

        :param average: The average of this ServerDataPoints.
        :type average: float
        """
        self._average = average

    @property
    def max(self):
        """Gets the max of this ServerDataPoints.

        聚合周期内指标数据的最大值。

        :return: The max of this ServerDataPoints.
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this ServerDataPoints.

        聚合周期内指标数据的最大值。

        :param max: The max of this ServerDataPoints.
        :type max: float
        """
        self._max = max

    @property
    def min(self):
        """Gets the min of this ServerDataPoints.

        聚合周期内指标数据的最小值。

        :return: The min of this ServerDataPoints.
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this ServerDataPoints.

        聚合周期内指标数据的最小值。

        :param min: The min of this ServerDataPoints.
        :type min: float
        """
        self._min = min

    @property
    def sum(self):
        """Gets the sum of this ServerDataPoints.

        聚合周期内指标数据的求和值。

        :return: The sum of this ServerDataPoints.
        :rtype: float
        """
        return self._sum

    @sum.setter
    def sum(self, sum):
        """Sets the sum of this ServerDataPoints.

        聚合周期内指标数据的求和值。

        :param sum: The sum of this ServerDataPoints.
        :type sum: float
        """
        self._sum = sum

    @property
    def variance(self):
        """Gets the variance of this ServerDataPoints.

        聚合周期内指标数据的方差。

        :return: The variance of this ServerDataPoints.
        :rtype: float
        """
        return self._variance

    @variance.setter
    def variance(self, variance):
        """Sets the variance of this ServerDataPoints.

        聚合周期内指标数据的方差。

        :param variance: The variance of this ServerDataPoints.
        :type variance: float
        """
        self._variance = variance

    @property
    def timestamp(self):
        """Gets the timestamp of this ServerDataPoints.

        指标采集时间，UNIX时间戳，单位毫秒。

        :return: The timestamp of this ServerDataPoints.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ServerDataPoints.

        指标采集时间，UNIX时间戳，单位毫秒。

        :param timestamp: The timestamp of this ServerDataPoints.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def unit(self):
        """Gets the unit of this ServerDataPoints.

        指标单位。

        :return: The unit of this ServerDataPoints.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ServerDataPoints.

        指标单位。

        :param unit: The unit of this ServerDataPoints.
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
        if not isinstance(other, ServerDataPoints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
