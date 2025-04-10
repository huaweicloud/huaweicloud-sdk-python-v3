# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        r"""MetricItemResultAPI

        The model defined in huaweicloud sdk

        :param metric: 
        :type metric: :class:`huaweicloudsdkbcs.v2.MetricDemision`
        :param data_points: 监控数据信息
        :type data_points: list[:class:`huaweicloudsdkbcs.v2.MetricDataPoints`]
        """
        
        

        self._metric = None
        self._data_points = None
        self.discriminator = None

        if metric is not None:
            self.metric = metric
        if data_points is not None:
            self.data_points = data_points

    @property
    def metric(self):
        r"""Gets the metric of this MetricItemResultAPI.

        :return: The metric of this MetricItemResultAPI.
        :rtype: :class:`huaweicloudsdkbcs.v2.MetricDemision`
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        r"""Sets the metric of this MetricItemResultAPI.

        :param metric: The metric of this MetricItemResultAPI.
        :type metric: :class:`huaweicloudsdkbcs.v2.MetricDemision`
        """
        self._metric = metric

    @property
    def data_points(self):
        r"""Gets the data_points of this MetricItemResultAPI.

        监控数据信息

        :return: The data_points of this MetricItemResultAPI.
        :rtype: list[:class:`huaweicloudsdkbcs.v2.MetricDataPoints`]
        """
        return self._data_points

    @data_points.setter
    def data_points(self, data_points):
        r"""Sets the data_points of this MetricItemResultAPI.

        监控数据信息

        :param data_points: The data_points of this MetricItemResultAPI.
        :type data_points: list[:class:`huaweicloudsdkbcs.v2.MetricDataPoints`]
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
        if not isinstance(other, MetricItemResultAPI):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
