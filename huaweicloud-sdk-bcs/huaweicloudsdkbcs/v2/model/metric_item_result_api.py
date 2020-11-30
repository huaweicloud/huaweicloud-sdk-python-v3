# coding: utf-8

import pprint
import re

import six





class MetricItemResultAPI:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'metric': 'MetricDemision',
        'data_points': 'list[MetricDataPoints]'
    }

    attribute_map = {
        'metric': 'metric',
        'data_points': 'dataPoints'
    }

    def __init__(self, metric=None, data_points=None):
        """MetricItemResultAPI - a model defined in huaweicloud sdk"""
        
        

        self._metric = None
        self._data_points = None
        self.discriminator = None

        if metric is not None:
            self.metric = metric
        if data_points is not None:
            self.data_points = data_points

    @property
    def metric(self):
        """Gets the metric of this MetricItemResultAPI.


        :return: The metric of this MetricItemResultAPI.
        :rtype: MetricDemision
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this MetricItemResultAPI.


        :param metric: The metric of this MetricItemResultAPI.
        :type: MetricDemision
        """
        self._metric = metric

    @property
    def data_points(self):
        """Gets the data_points of this MetricItemResultAPI.

        监控数据信息

        :return: The data_points of this MetricItemResultAPI.
        :rtype: list[MetricDataPoints]
        """
        return self._data_points

    @data_points.setter
    def data_points(self, data_points):
        """Sets the data_points of this MetricItemResultAPI.

        监控数据信息

        :param data_points: The data_points of this MetricItemResultAPI.
        :type: list[MetricDataPoints]
        """
        self._data_points = data_points

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
        if not isinstance(other, MetricItemResultAPI):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
