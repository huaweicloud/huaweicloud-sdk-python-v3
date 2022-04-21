# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryMetricItemOptionParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'dimensions': 'list[Dimension]',
        'metric_name': 'str',
        'namespace': 'str'
    }

    attribute_map = {
        'dimensions': 'dimensions',
        'metric_name': 'metricName',
        'namespace': 'namespace'
    }

    def __init__(self, dimensions=None, metric_name=None, namespace=None):
        """QueryMetricItemOptionParam

        The model defined in huaweicloud sdk

        :param dimensions: 指标维度列表。
        :type dimensions: list[:class:`huaweicloudsdkaom.v2.Dimension`]
        :param metric_name: 指标名称。名称长度取值范围为1~255个字符。 取值范围： AOM提供的基础指标， cpuUsage、cpuCoreUsed等 cpuUage：cpu使用率； cpuCoreUsed：cpu内核占用； 用户上报的自定义指标名称。
        :type metric_name: str
        :param namespace: 指标命名空间。 取值范围 PAAS.CONTAINER：组件指标、实例指标、进程指标和容器指标的命名空间， PAAS.NODE： 主机指标、网络指标、磁盘指标和文件系统指标的命名空间， PAAS.SLA：SLA指标的命名空间， PAAS.AGGR：集群指标的命名空间， CUSTOMMETRICS：默认的自定义指标的命名空间。
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
        self.namespace = namespace

    @property
    def dimensions(self):
        """Gets the dimensions of this QueryMetricItemOptionParam.

        指标维度列表。

        :return: The dimensions of this QueryMetricItemOptionParam.
        :rtype: list[:class:`huaweicloudsdkaom.v2.Dimension`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this QueryMetricItemOptionParam.

        指标维度列表。

        :param dimensions: The dimensions of this QueryMetricItemOptionParam.
        :type dimensions: list[:class:`huaweicloudsdkaom.v2.Dimension`]
        """
        self._dimensions = dimensions

    @property
    def metric_name(self):
        """Gets the metric_name of this QueryMetricItemOptionParam.

        指标名称。名称长度取值范围为1~255个字符。 取值范围： AOM提供的基础指标， cpuUsage、cpuCoreUsed等 cpuUage：cpu使用率； cpuCoreUsed：cpu内核占用； 用户上报的自定义指标名称。

        :return: The metric_name of this QueryMetricItemOptionParam.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this QueryMetricItemOptionParam.

        指标名称。名称长度取值范围为1~255个字符。 取值范围： AOM提供的基础指标， cpuUsage、cpuCoreUsed等 cpuUage：cpu使用率； cpuCoreUsed：cpu内核占用； 用户上报的自定义指标名称。

        :param metric_name: The metric_name of this QueryMetricItemOptionParam.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def namespace(self):
        """Gets the namespace of this QueryMetricItemOptionParam.

        指标命名空间。 取值范围 PAAS.CONTAINER：组件指标、实例指标、进程指标和容器指标的命名空间， PAAS.NODE： 主机指标、网络指标、磁盘指标和文件系统指标的命名空间， PAAS.SLA：SLA指标的命名空间， PAAS.AGGR：集群指标的命名空间， CUSTOMMETRICS：默认的自定义指标的命名空间。

        :return: The namespace of this QueryMetricItemOptionParam.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this QueryMetricItemOptionParam.

        指标命名空间。 取值范围 PAAS.CONTAINER：组件指标、实例指标、进程指标和容器指标的命名空间， PAAS.NODE： 主机指标、网络指标、磁盘指标和文件系统指标的命名空间， PAAS.SLA：SLA指标的命名空间， PAAS.AGGR：集群指标的命名空间， CUSTOMMETRICS：默认的自定义指标的命名空间。

        :param namespace: The namespace of this QueryMetricItemOptionParam.
        :type namespace: str
        """
        self._namespace = namespace

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
        if not isinstance(other, QueryMetricItemOptionParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
