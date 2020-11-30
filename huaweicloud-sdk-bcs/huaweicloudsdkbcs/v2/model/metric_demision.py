# coding: utf-8

import pprint
import re

import six





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
        """MetricDemision - a model defined in huaweicloud sdk"""
        
        

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
        :type: str
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
        :type: str
        """
        self._metric_name = metric_name

    @property
    def dimensions(self):
        """Gets the dimensions of this MetricDemision.

        维度列表

        :return: The dimensions of this MetricDemision.
        :rtype: list[Dimension]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this MetricDemision.

        维度列表

        :param dimensions: The dimensions of this MetricDemision.
        :type: list[Dimension]
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MetricDemision):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
