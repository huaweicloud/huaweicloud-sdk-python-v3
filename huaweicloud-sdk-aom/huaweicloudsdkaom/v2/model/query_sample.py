# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuerySample:

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
        'dimensions': 'list[DimensionSeries]',
        'metric_name': 'str'
    }

    attribute_map = {
        'namespace': 'namespace',
        'dimensions': 'dimensions',
        'metric_name': 'metric_name'
    }

    def __init__(self, namespace=None, dimensions=None, metric_name=None):
        """QuerySample

        The model defined in huaweicloud sdk

        :param namespace: 时间序列命名空间。 取值范围： PAAS.CONTAINER、PAAS.NODE、PAAS.SLA、PAAS.AGGR、CUSTOMMETRICS等； PAAS.CONTAINER：应用时间序列； PAAS.NODE：节点时间序列； PAAS.SLA：SLA时间序列； PAAS.AGGR：集群时间序列； CUSTOMMETRICS：自定义时间序列。
        :type namespace: str
        :param dimensions: 时间序列维度列表 可通过/v2/{project_id}/series接口中namespace+metric_name， 查询当前监控的时间序列名称的时间序列维度列表。
        :type dimensions: list[:class:`huaweicloudsdkaom.v2.DimensionSeries`]
        :param metric_name: 时间序列名称。名称长度取值范围为1~255个字符。 取值范围： AOM提供的基础时间序列名称，cpuUsage、cpuCoreUsed等， cpuUage：cpu使用率； cpuCoreUsed：cpu内核占用； 用户上报的自定义时间序列名称。
        :type metric_name: str
        """
        
        

        self._namespace = None
        self._dimensions = None
        self._metric_name = None
        self.discriminator = None

        self.namespace = namespace
        self.dimensions = dimensions
        self.metric_name = metric_name

    @property
    def namespace(self):
        """Gets the namespace of this QuerySample.

        时间序列命名空间。 取值范围： PAAS.CONTAINER、PAAS.NODE、PAAS.SLA、PAAS.AGGR、CUSTOMMETRICS等； PAAS.CONTAINER：应用时间序列； PAAS.NODE：节点时间序列； PAAS.SLA：SLA时间序列； PAAS.AGGR：集群时间序列； CUSTOMMETRICS：自定义时间序列。

        :return: The namespace of this QuerySample.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this QuerySample.

        时间序列命名空间。 取值范围： PAAS.CONTAINER、PAAS.NODE、PAAS.SLA、PAAS.AGGR、CUSTOMMETRICS等； PAAS.CONTAINER：应用时间序列； PAAS.NODE：节点时间序列； PAAS.SLA：SLA时间序列； PAAS.AGGR：集群时间序列； CUSTOMMETRICS：自定义时间序列。

        :param namespace: The namespace of this QuerySample.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def dimensions(self):
        """Gets the dimensions of this QuerySample.

        时间序列维度列表 可通过/v2/{project_id}/series接口中namespace+metric_name， 查询当前监控的时间序列名称的时间序列维度列表。

        :return: The dimensions of this QuerySample.
        :rtype: list[:class:`huaweicloudsdkaom.v2.DimensionSeries`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this QuerySample.

        时间序列维度列表 可通过/v2/{project_id}/series接口中namespace+metric_name， 查询当前监控的时间序列名称的时间序列维度列表。

        :param dimensions: The dimensions of this QuerySample.
        :type dimensions: list[:class:`huaweicloudsdkaom.v2.DimensionSeries`]
        """
        self._dimensions = dimensions

    @property
    def metric_name(self):
        """Gets the metric_name of this QuerySample.

        时间序列名称。名称长度取值范围为1~255个字符。 取值范围： AOM提供的基础时间序列名称，cpuUsage、cpuCoreUsed等， cpuUage：cpu使用率； cpuCoreUsed：cpu内核占用； 用户上报的自定义时间序列名称。

        :return: The metric_name of this QuerySample.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this QuerySample.

        时间序列名称。名称长度取值范围为1~255个字符。 取值范围： AOM提供的基础时间序列名称，cpuUsage、cpuCoreUsed等， cpuUage：cpu使用率； cpuCoreUsed：cpu内核占用； 用户上报的自定义时间序列名称。

        :param metric_name: The metric_name of this QuerySample.
        :type metric_name: str
        """
        self._metric_name = metric_name

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
        if not isinstance(other, QuerySample):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
