# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric': 'str',
        'value': 'list[float]'
    }

    attribute_map = {
        'metric': 'metric',
        'value': 'value'
    }

    def __init__(self, metric=None, value=None):
        r"""MetricObject

        The model defined in huaweicloud sdk

        :param metric: 运行指标，可选值如下： - cpuUsage：CPU使用率 - memUsage：物理内存使用率 - gpuUtil：GPU使用率 - gpuMemUsage：显存使用率 - npuUtil：NPU使用率 - npuMemUsage：NPU显存使用率
        :type metric: str
        :param value: 运行指标对应数值，1min统计一个平均值。
        :type value: list[float]
        """
        
        

        self._metric = None
        self._value = None
        self.discriminator = None

        if metric is not None:
            self.metric = metric
        if value is not None:
            self.value = value

    @property
    def metric(self):
        r"""Gets the metric of this MetricObject.

        运行指标，可选值如下： - cpuUsage：CPU使用率 - memUsage：物理内存使用率 - gpuUtil：GPU使用率 - gpuMemUsage：显存使用率 - npuUtil：NPU使用率 - npuMemUsage：NPU显存使用率

        :return: The metric of this MetricObject.
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        r"""Sets the metric of this MetricObject.

        运行指标，可选值如下： - cpuUsage：CPU使用率 - memUsage：物理内存使用率 - gpuUtil：GPU使用率 - gpuMemUsage：显存使用率 - npuUtil：NPU使用率 - npuMemUsage：NPU显存使用率

        :param metric: The metric of this MetricObject.
        :type metric: str
        """
        self._metric = metric

    @property
    def value(self):
        r"""Gets the value of this MetricObject.

        运行指标对应数值，1min统计一个平均值。

        :return: The value of this MetricObject.
        :rtype: list[float]
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this MetricObject.

        运行指标对应数值，1min统计一个平均值。

        :param value: The value of this MetricObject.
        :type value: list[float]
        """
        self._value = value

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
        if not isinstance(other, MetricObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
