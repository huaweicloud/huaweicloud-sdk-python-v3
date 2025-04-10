# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceMultiNodesSingleMetricResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_name': 'str',
        'unit': 'str',
        'metrics': 'list[MultiNodesSingleMetricMetrics]'
    }

    attribute_map = {
        'metric_name': 'metric_name',
        'unit': 'unit',
        'metrics': 'metrics'
    }

    def __init__(self, metric_name=None, unit=None, metrics=None):
        r"""ListInstanceMultiNodesSingleMetricResponse

        The model defined in huaweicloud sdk

        :param metric_name: 指标名称
        :type metric_name: str
        :param unit: 单位
        :type unit: str
        :param metrics: 指标值
        :type metrics: list[:class:`huaweicloudsdkdas.v3.MultiNodesSingleMetricMetrics`]
        """
        
        super(ListInstanceMultiNodesSingleMetricResponse, self).__init__()

        self._metric_name = None
        self._unit = None
        self._metrics = None
        self.discriminator = None

        if metric_name is not None:
            self.metric_name = metric_name
        if unit is not None:
            self.unit = unit
        if metrics is not None:
            self.metrics = metrics

    @property
    def metric_name(self):
        r"""Gets the metric_name of this ListInstanceMultiNodesSingleMetricResponse.

        指标名称

        :return: The metric_name of this ListInstanceMultiNodesSingleMetricResponse.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this ListInstanceMultiNodesSingleMetricResponse.

        指标名称

        :param metric_name: The metric_name of this ListInstanceMultiNodesSingleMetricResponse.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def unit(self):
        r"""Gets the unit of this ListInstanceMultiNodesSingleMetricResponse.

        单位

        :return: The unit of this ListInstanceMultiNodesSingleMetricResponse.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this ListInstanceMultiNodesSingleMetricResponse.

        单位

        :param unit: The unit of this ListInstanceMultiNodesSingleMetricResponse.
        :type unit: str
        """
        self._unit = unit

    @property
    def metrics(self):
        r"""Gets the metrics of this ListInstanceMultiNodesSingleMetricResponse.

        指标值

        :return: The metrics of this ListInstanceMultiNodesSingleMetricResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.MultiNodesSingleMetricMetrics`]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        r"""Sets the metrics of this ListInstanceMultiNodesSingleMetricResponse.

        指标值

        :param metrics: The metrics of this ListInstanceMultiNodesSingleMetricResponse.
        :type metrics: list[:class:`huaweicloudsdkdas.v3.MultiNodesSingleMetricMetrics`]
        """
        self._metrics = metrics

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
        if not isinstance(other, ListInstanceMultiNodesSingleMetricResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
