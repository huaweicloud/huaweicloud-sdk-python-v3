# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricDemision:

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
        'dimensions': 'list[Dimension]'
    }

    attribute_map = {
        'namespace': 'namespace',
        'metric_name': 'metricName',
        'dimensions': 'dimensions'
    }

    def __init__(self, namespace=None, metric_name=None, dimensions=None):
        """MetricDemision

        The model defined in huaweicloud sdk

        :param namespace: 命名空间
        :type namespace: str
        :param metric_name: 指标名称
        :type metric_name: str
        :param dimensions: 维度列表
        :type dimensions: list[:class:`huaweicloudsdkbcs.v2.Dimension`]
        """
        
        

        self._namespace = None
        self._metric_name = None
        self._dimensions = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if metric_name is not None:
            self.metric_name = metric_name
        if dimensions is not None:
            self.dimensions = dimensions

    @property
    def namespace(self):
        """Gets the namespace of this MetricDemision.

        命名空间

        :return: The namespace of this MetricDemision.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this MetricDemision.

        命名空间

        :param namespace: The namespace of this MetricDemision.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def metric_name(self):
        """Gets the metric_name of this MetricDemision.

        指标名称

        :return: The metric_name of this MetricDemision.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this MetricDemision.

        指标名称

        :param metric_name: The metric_name of this MetricDemision.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def dimensions(self):
        """Gets the dimensions of this MetricDemision.

        维度列表

        :return: The dimensions of this MetricDemision.
        :rtype: list[:class:`huaweicloudsdkbcs.v2.Dimension`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this MetricDemision.

        维度列表

        :param dimensions: The dimensions of this MetricDemision.
        :type dimensions: list[:class:`huaweicloudsdkbcs.v2.Dimension`]
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
        if not isinstance(other, MetricDemision):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
