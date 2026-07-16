# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolMonitorMetric:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dimensions': 'list[PoolMonitorMetricDimensions]',
        'metric_name': 'str',
        'namespace': 'str'
    }

    attribute_map = {
        'dimensions': 'dimensions',
        'metric_name': 'metricName',
        'namespace': 'namespace'
    }

    def __init__(self, dimensions=None, metric_name=None, namespace=None):
        r"""PoolMonitorMetric

        The model defined in huaweicloud sdk

        :param dimensions: **参数解释**：指标维度信息。
        :type dimensions: list[:class:`huaweicloudsdkmodelarts.v1.PoolMonitorMetricDimensions`]
        :param metric_name: **参数解释**：指标名称。 **取值范围**：可选值如下： - cpuUsage：CPU使用量。 - memUsedRate：内存利用率。 - gpuUtil：GPU显卡使用量。 - gpuMemUsage：GPU显存使用量。 - npuUtil：NPU显卡使用量。 - npuMemUsage：NPU显存使用量。 - diskCapacity：磁盘容量。 - diskAvailableCapacity：磁盘可用容量。 - diskUsedRate：磁盘利用率。
        :type metric_name: str
        :param namespace: **参数解释**：指标命名空间。 **取值范围**：可选值如下： -  PAAS.CONTAINER：组件指标、实例指标、进程指标和容器指标的命名空间 - PAAS.NODE： 主机指标、网络指标、磁盘指标和文件系统指标的命名空间 -  PAAS.SLA：SLA指标的命名空间 - PAAS.AGGR：集群指标的命名空间 - CUSTOMMETRICS：默认的自定义指标的命名空间
        :type namespace: str
        """
        
        

        self._dimensions = None
        self._metric_name = None
        self._namespace = None
        self.discriminator = None

        if dimensions is not None:
            self.dimensions = dimensions
        if metric_name is not None:
            self.metric_name = metric_name
        if namespace is not None:
            self.namespace = namespace

    @property
    def dimensions(self):
        r"""Gets the dimensions of this PoolMonitorMetric.

        **参数解释**：指标维度信息。

        :return: The dimensions of this PoolMonitorMetric.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.PoolMonitorMetricDimensions`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        r"""Sets the dimensions of this PoolMonitorMetric.

        **参数解释**：指标维度信息。

        :param dimensions: The dimensions of this PoolMonitorMetric.
        :type dimensions: list[:class:`huaweicloudsdkmodelarts.v1.PoolMonitorMetricDimensions`]
        """
        self._dimensions = dimensions

    @property
    def metric_name(self):
        r"""Gets the metric_name of this PoolMonitorMetric.

        **参数解释**：指标名称。 **取值范围**：可选值如下： - cpuUsage：CPU使用量。 - memUsedRate：内存利用率。 - gpuUtil：GPU显卡使用量。 - gpuMemUsage：GPU显存使用量。 - npuUtil：NPU显卡使用量。 - npuMemUsage：NPU显存使用量。 - diskCapacity：磁盘容量。 - diskAvailableCapacity：磁盘可用容量。 - diskUsedRate：磁盘利用率。

        :return: The metric_name of this PoolMonitorMetric.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this PoolMonitorMetric.

        **参数解释**：指标名称。 **取值范围**：可选值如下： - cpuUsage：CPU使用量。 - memUsedRate：内存利用率。 - gpuUtil：GPU显卡使用量。 - gpuMemUsage：GPU显存使用量。 - npuUtil：NPU显卡使用量。 - npuMemUsage：NPU显存使用量。 - diskCapacity：磁盘容量。 - diskAvailableCapacity：磁盘可用容量。 - diskUsedRate：磁盘利用率。

        :param metric_name: The metric_name of this PoolMonitorMetric.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def namespace(self):
        r"""Gets the namespace of this PoolMonitorMetric.

        **参数解释**：指标命名空间。 **取值范围**：可选值如下： -  PAAS.CONTAINER：组件指标、实例指标、进程指标和容器指标的命名空间 - PAAS.NODE： 主机指标、网络指标、磁盘指标和文件系统指标的命名空间 -  PAAS.SLA：SLA指标的命名空间 - PAAS.AGGR：集群指标的命名空间 - CUSTOMMETRICS：默认的自定义指标的命名空间

        :return: The namespace of this PoolMonitorMetric.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this PoolMonitorMetric.

        **参数解释**：指标命名空间。 **取值范围**：可选值如下： -  PAAS.CONTAINER：组件指标、实例指标、进程指标和容器指标的命名空间 - PAAS.NODE： 主机指标、网络指标、磁盘指标和文件系统指标的命名空间 -  PAAS.SLA：SLA指标的命名空间 - PAAS.AGGR：集群指标的命名空间 - CUSTOMMETRICS：默认的自定义指标的命名空间

        :param namespace: The namespace of this PoolMonitorMetric.
        :type namespace: str
        """
        self._namespace = namespace

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
        if not isinstance(other, PoolMonitorMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
