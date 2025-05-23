# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricDataPoints:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'statistics': 'list[StatisticValue]',
        'timestamp': 'int',
        'unit': 'str'
    }

    attribute_map = {
        'statistics': 'statistics',
        'timestamp': 'timestamp',
        'unit': 'unit'
    }

    def __init__(self, statistics=None, timestamp=None, unit=None):
        r"""MetricDataPoints

        The model defined in huaweicloud sdk

        :param statistics: 统计方式。
        :type statistics: list[:class:`huaweicloudsdkaom.v2.StatisticValue`]
        :param timestamp: 时间戳。
        :type timestamp: int
        :param unit: 时间序列单位。
        :type unit: str
        """
        
        

        self._statistics = None
        self._timestamp = None
        self._unit = None
        self.discriminator = None

        if statistics is not None:
            self.statistics = statistics
        if timestamp is not None:
            self.timestamp = timestamp
        if unit is not None:
            self.unit = unit

    @property
    def statistics(self):
        r"""Gets the statistics of this MetricDataPoints.

        统计方式。

        :return: The statistics of this MetricDataPoints.
        :rtype: list[:class:`huaweicloudsdkaom.v2.StatisticValue`]
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        r"""Sets the statistics of this MetricDataPoints.

        统计方式。

        :param statistics: The statistics of this MetricDataPoints.
        :type statistics: list[:class:`huaweicloudsdkaom.v2.StatisticValue`]
        """
        self._statistics = statistics

    @property
    def timestamp(self):
        r"""Gets the timestamp of this MetricDataPoints.

        时间戳。

        :return: The timestamp of this MetricDataPoints.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this MetricDataPoints.

        时间戳。

        :param timestamp: The timestamp of this MetricDataPoints.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def unit(self):
        r"""Gets the unit of this MetricDataPoints.

        时间序列单位。

        :return: The unit of this MetricDataPoints.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this MetricDataPoints.

        时间序列单位。

        :param unit: The unit of this MetricDataPoints.
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
        if not isinstance(other, MetricDataPoints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
