# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMetricsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'timestamps': 'list[str]',
        'metrics': 'list[MetricList]'
    }

    attribute_map = {
        'timestamps': 'timestamps',
        'metrics': 'metrics'
    }

    def __init__(self, timestamps=None, metrics=None):
        """ListMetricsResponse

        The model defined in huaweicloud sdk

        :param timestamps: 时间序列
        :type timestamps: list[str]
        :param metrics: 查询的测量指标列表
        :type metrics: list[:class:`huaweicloudsdkiotanalytics.v1.MetricList`]
        """
        
        super(ListMetricsResponse, self).__init__()

        self._timestamps = None
        self._metrics = None
        self.discriminator = None

        if timestamps is not None:
            self.timestamps = timestamps
        if metrics is not None:
            self.metrics = metrics

    @property
    def timestamps(self):
        """Gets the timestamps of this ListMetricsResponse.

        时间序列

        :return: The timestamps of this ListMetricsResponse.
        :rtype: list[str]
        """
        return self._timestamps

    @timestamps.setter
    def timestamps(self, timestamps):
        """Sets the timestamps of this ListMetricsResponse.

        时间序列

        :param timestamps: The timestamps of this ListMetricsResponse.
        :type timestamps: list[str]
        """
        self._timestamps = timestamps

    @property
    def metrics(self):
        """Gets the metrics of this ListMetricsResponse.

        查询的测量指标列表

        :return: The metrics of this ListMetricsResponse.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.MetricList`]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this ListMetricsResponse.

        查询的测量指标列表

        :param metrics: The metrics of this ListMetricsResponse.
        :type metrics: list[:class:`huaweicloudsdkiotanalytics.v1.MetricList`]
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
        if not isinstance(other, ListMetricsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
