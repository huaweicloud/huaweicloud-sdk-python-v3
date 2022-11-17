# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricDataValue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_points': 'list[MetricDataPoints]',
        'metric': 'MetricQueryMeritcParam'
    }

    attribute_map = {
        'data_points': 'dataPoints',
        'metric': 'metric'
    }

    def __init__(self, data_points=None, metric=None):
        """MetricDataValue

        The model defined in huaweicloud sdk

        :param data_points: 重点指标。
        :type data_points: list[:class:`huaweicloudsdkaom.v2.MetricDataPoints`]
        :param metric: 
        :type metric: :class:`huaweicloudsdkaom.v2.MetricQueryMeritcParam`
        """
        
        

        self._data_points = None
        self._metric = None
        self.discriminator = None

        if data_points is not None:
            self.data_points = data_points
        if metric is not None:
            self.metric = metric

    @property
    def data_points(self):
        """Gets the data_points of this MetricDataValue.

        重点指标。

        :return: The data_points of this MetricDataValue.
        :rtype: list[:class:`huaweicloudsdkaom.v2.MetricDataPoints`]
        """
        return self._data_points

    @data_points.setter
    def data_points(self, data_points):
        """Sets the data_points of this MetricDataValue.

        重点指标。

        :param data_points: The data_points of this MetricDataValue.
        :type data_points: list[:class:`huaweicloudsdkaom.v2.MetricDataPoints`]
        """
        self._data_points = data_points

    @property
    def metric(self):
        """Gets the metric of this MetricDataValue.

        :return: The metric of this MetricDataValue.
        :rtype: :class:`huaweicloudsdkaom.v2.MetricQueryMeritcParam`
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this MetricDataValue.

        :param metric: The metric of this MetricDataValue.
        :type metric: :class:`huaweicloudsdkaom.v2.MetricQueryMeritcParam`
        """
        self._metric = metric

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
        if not isinstance(other, MetricDataValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
