# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuerySeriesOptionParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'metric_name': 'str',
        'dimensions': 'list[DimensionSeries]'
    }

    attribute_map = {
        'namespace': 'namespace',
        'metric_name': 'metric_name',
        'dimensions': 'dimensions'
    }

    def __init__(self, namespace=None, metric_name=None, dimensions=None):
        r"""QuerySeriesOptionParam

        The model defined in huaweicloud sdk

        :param namespace: 时间序列命名空间。取值范围：PAAS.CONTAINER、PAAS.NODE、PAAS.SLA、PAAS.AGGR、CUSTOMMETRICS等。PAAS.CONTAINER：应用时间序列命名空间；PAAS.NODE：节点时间序列命名空间；PAAS.SLA：SLA时间序列命名空间；PAAS.AGGR：集群时间序列命名空间；CUSTOMMETRICS：自定义时间序列命名空间。
        :type namespace: str
        :param metric_name: 时间序列名称，名称长度取值范围为1~255个字符。取值范围：AOM提供的基础时间序列名称，cpuUsage、cpuCoreUsed等：cpuUsage：cpu使用率；cpuCoreUsed：cpu内核占用；用户上报的自定义时间序列名称。
        :type metric_name: str
        :param dimensions: 时间序列维度列表。可通过/v2/{project_id}/series接口中namespace+metric_name，查询当前监控的时间序列名称的时间序列维度列表。
        :type dimensions: list[:class:`huaweicloudsdkaom.v2.DimensionSeries`]
        """
        
        

        self._namespace = None
        self._metric_name = None
        self._dimensions = None
        self.discriminator = None

        self.namespace = namespace
        if metric_name is not None:
            self.metric_name = metric_name
        if dimensions is not None:
            self.dimensions = dimensions

    @property
    def namespace(self):
        r"""Gets the namespace of this QuerySeriesOptionParam.

        时间序列命名空间。取值范围：PAAS.CONTAINER、PAAS.NODE、PAAS.SLA、PAAS.AGGR、CUSTOMMETRICS等。PAAS.CONTAINER：应用时间序列命名空间；PAAS.NODE：节点时间序列命名空间；PAAS.SLA：SLA时间序列命名空间；PAAS.AGGR：集群时间序列命名空间；CUSTOMMETRICS：自定义时间序列命名空间。

        :return: The namespace of this QuerySeriesOptionParam.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this QuerySeriesOptionParam.

        时间序列命名空间。取值范围：PAAS.CONTAINER、PAAS.NODE、PAAS.SLA、PAAS.AGGR、CUSTOMMETRICS等。PAAS.CONTAINER：应用时间序列命名空间；PAAS.NODE：节点时间序列命名空间；PAAS.SLA：SLA时间序列命名空间；PAAS.AGGR：集群时间序列命名空间；CUSTOMMETRICS：自定义时间序列命名空间。

        :param namespace: The namespace of this QuerySeriesOptionParam.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def metric_name(self):
        r"""Gets the metric_name of this QuerySeriesOptionParam.

        时间序列名称，名称长度取值范围为1~255个字符。取值范围：AOM提供的基础时间序列名称，cpuUsage、cpuCoreUsed等：cpuUsage：cpu使用率；cpuCoreUsed：cpu内核占用；用户上报的自定义时间序列名称。

        :return: The metric_name of this QuerySeriesOptionParam.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this QuerySeriesOptionParam.

        时间序列名称，名称长度取值范围为1~255个字符。取值范围：AOM提供的基础时间序列名称，cpuUsage、cpuCoreUsed等：cpuUsage：cpu使用率；cpuCoreUsed：cpu内核占用；用户上报的自定义时间序列名称。

        :param metric_name: The metric_name of this QuerySeriesOptionParam.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def dimensions(self):
        r"""Gets the dimensions of this QuerySeriesOptionParam.

        时间序列维度列表。可通过/v2/{project_id}/series接口中namespace+metric_name，查询当前监控的时间序列名称的时间序列维度列表。

        :return: The dimensions of this QuerySeriesOptionParam.
        :rtype: list[:class:`huaweicloudsdkaom.v2.DimensionSeries`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        r"""Sets the dimensions of this QuerySeriesOptionParam.

        时间序列维度列表。可通过/v2/{project_id}/series接口中namespace+metric_name，查询当前监控的时间序列名称的时间序列维度列表。

        :param dimensions: The dimensions of this QuerySeriesOptionParam.
        :type dimensions: list[:class:`huaweicloudsdkaom.v2.DimensionSeries`]
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
        if not isinstance(other, QuerySeriesOptionParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
