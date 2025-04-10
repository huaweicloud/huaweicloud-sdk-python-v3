# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Metric:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sources': 'list[FlinkJobMetricInfo]',
        'sinks': 'list[FlinkJobMetricInfo]',
        'total_read_rate': 'float',
        'total_write_rate': 'float'
    }

    attribute_map = {
        'sources': 'sources',
        'sinks': 'sinks',
        'total_read_rate': 'total_read_rate',
        'total_write_rate': 'total_write_rate'
    }

    def __init__(self, sources=None, sinks=None, total_read_rate=None, total_write_rate=None):
        r"""Metric

        The model defined in huaweicloud sdk

        :param sources: 所有输入流。
        :type sources: list[:class:`huaweicloudsdkdli.v1.FlinkJobMetricInfo`]
        :param sinks: 所有输出流。
        :type sinks: list[:class:`huaweicloudsdkdli.v1.FlinkJobMetricInfo`]
        :param total_read_rate: 总输入速率
        :type total_read_rate: float
        :param total_write_rate: 总输出速率
        :type total_write_rate: float
        """
        
        

        self._sources = None
        self._sinks = None
        self._total_read_rate = None
        self._total_write_rate = None
        self.discriminator = None

        if sources is not None:
            self.sources = sources
        if sinks is not None:
            self.sinks = sinks
        if total_read_rate is not None:
            self.total_read_rate = total_read_rate
        if total_write_rate is not None:
            self.total_write_rate = total_write_rate

    @property
    def sources(self):
        r"""Gets the sources of this Metric.

        所有输入流。

        :return: The sources of this Metric.
        :rtype: list[:class:`huaweicloudsdkdli.v1.FlinkJobMetricInfo`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        r"""Sets the sources of this Metric.

        所有输入流。

        :param sources: The sources of this Metric.
        :type sources: list[:class:`huaweicloudsdkdli.v1.FlinkJobMetricInfo`]
        """
        self._sources = sources

    @property
    def sinks(self):
        r"""Gets the sinks of this Metric.

        所有输出流。

        :return: The sinks of this Metric.
        :rtype: list[:class:`huaweicloudsdkdli.v1.FlinkJobMetricInfo`]
        """
        return self._sinks

    @sinks.setter
    def sinks(self, sinks):
        r"""Sets the sinks of this Metric.

        所有输出流。

        :param sinks: The sinks of this Metric.
        :type sinks: list[:class:`huaweicloudsdkdli.v1.FlinkJobMetricInfo`]
        """
        self._sinks = sinks

    @property
    def total_read_rate(self):
        r"""Gets the total_read_rate of this Metric.

        总输入速率

        :return: The total_read_rate of this Metric.
        :rtype: float
        """
        return self._total_read_rate

    @total_read_rate.setter
    def total_read_rate(self, total_read_rate):
        r"""Sets the total_read_rate of this Metric.

        总输入速率

        :param total_read_rate: The total_read_rate of this Metric.
        :type total_read_rate: float
        """
        self._total_read_rate = total_read_rate

    @property
    def total_write_rate(self):
        r"""Gets the total_write_rate of this Metric.

        总输出速率

        :return: The total_write_rate of this Metric.
        :rtype: float
        """
        return self._total_write_rate

    @total_write_rate.setter
    def total_write_rate(self, total_write_rate):
        r"""Sets the total_write_rate of this Metric.

        总输出速率

        :param total_write_rate: The total_write_rate of this Metric.
        :type total_write_rate: float
        """
        self._total_write_rate = total_write_rate

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
        if not isinstance(other, Metric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
