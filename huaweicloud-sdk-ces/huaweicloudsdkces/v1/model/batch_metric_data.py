# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchMetricData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'unit': 'str',
        'datapoints': 'list[DatapointForBatchMetric]',
        'namespace': 'str',
        'metric_name': 'str',
        'dimensions': 'list[MetricsDimension]'
    }

    attribute_map = {
        'unit': 'unit',
        'datapoints': 'datapoints',
        'namespace': 'namespace',
        'metric_name': 'metric_name',
        'dimensions': 'dimensions'
    }

    def __init__(self, unit=None, datapoints=None, namespace=None, metric_name=None, dimensions=None):
        r"""BatchMetricData

        The model defined in huaweicloud sdk

        :param unit: 指标单位。
        :type unit: str
        :param datapoints: 指标数据列表。由于查询数据时，云监控会根据所选择的聚合粒度向前取整from参数，所以datapoints中包含的数据点有可能会多于预期。
        :type datapoints: list[:class:`huaweicloudsdkces.v1.DatapointForBatchMetric`]
        :param namespace: 指标命名空间，格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_，总长度最短为3，最大为32；各服务的命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。
        :type namespace: str
        :param metric_name: 指标名称，例如弹性云服务器监控指标中的cpu_util；各服务的指标名称可查看：“[服务指标名称](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。
        :type metric_name: str
        :param dimensions: 指标维度列表。
        :type dimensions: list[:class:`huaweicloudsdkces.v1.MetricsDimension`]
        """
        
        

        self._unit = None
        self._datapoints = None
        self._namespace = None
        self._metric_name = None
        self._dimensions = None
        self.discriminator = None

        if unit is not None:
            self.unit = unit
        self.datapoints = datapoints
        if namespace is not None:
            self.namespace = namespace
        self.metric_name = metric_name
        if dimensions is not None:
            self.dimensions = dimensions

    @property
    def unit(self):
        r"""Gets the unit of this BatchMetricData.

        指标单位。

        :return: The unit of this BatchMetricData.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this BatchMetricData.

        指标单位。

        :param unit: The unit of this BatchMetricData.
        :type unit: str
        """
        self._unit = unit

    @property
    def datapoints(self):
        r"""Gets the datapoints of this BatchMetricData.

        指标数据列表。由于查询数据时，云监控会根据所选择的聚合粒度向前取整from参数，所以datapoints中包含的数据点有可能会多于预期。

        :return: The datapoints of this BatchMetricData.
        :rtype: list[:class:`huaweicloudsdkces.v1.DatapointForBatchMetric`]
        """
        return self._datapoints

    @datapoints.setter
    def datapoints(self, datapoints):
        r"""Sets the datapoints of this BatchMetricData.

        指标数据列表。由于查询数据时，云监控会根据所选择的聚合粒度向前取整from参数，所以datapoints中包含的数据点有可能会多于预期。

        :param datapoints: The datapoints of this BatchMetricData.
        :type datapoints: list[:class:`huaweicloudsdkces.v1.DatapointForBatchMetric`]
        """
        self._datapoints = datapoints

    @property
    def namespace(self):
        r"""Gets the namespace of this BatchMetricData.

        指标命名空间，格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_，总长度最短为3，最大为32；各服务的命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The namespace of this BatchMetricData.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this BatchMetricData.

        指标命名空间，格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_，总长度最短为3，最大为32；各服务的命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param namespace: The namespace of this BatchMetricData.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def metric_name(self):
        r"""Gets the metric_name of this BatchMetricData.

        指标名称，例如弹性云服务器监控指标中的cpu_util；各服务的指标名称可查看：“[服务指标名称](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The metric_name of this BatchMetricData.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this BatchMetricData.

        指标名称，例如弹性云服务器监控指标中的cpu_util；各服务的指标名称可查看：“[服务指标名称](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param metric_name: The metric_name of this BatchMetricData.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def dimensions(self):
        r"""Gets the dimensions of this BatchMetricData.

        指标维度列表。

        :return: The dimensions of this BatchMetricData.
        :rtype: list[:class:`huaweicloudsdkces.v1.MetricsDimension`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        r"""Sets the dimensions of this BatchMetricData.

        指标维度列表。

        :param dimensions: The dimensions of this BatchMetricData.
        :type dimensions: list[:class:`huaweicloudsdkces.v1.MetricsDimension`]
        """
        self._dimensions = dimensions

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
        if not isinstance(other, BatchMetricData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
