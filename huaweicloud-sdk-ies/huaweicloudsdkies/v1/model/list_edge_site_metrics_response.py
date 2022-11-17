# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEdgeSiteMetricsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_data': 'list[MetricDataDetail]'
    }

    attribute_map = {
        'metric_data': 'metric_data'
    }

    def __init__(self, metric_data=None):
        """ListEdgeSiteMetricsResponse

        The model defined in huaweicloud sdk

        :param metric_data: 监控数据
        :type metric_data: list[:class:`huaweicloudsdkies.v1.MetricDataDetail`]
        """
        
        super(ListEdgeSiteMetricsResponse, self).__init__()

        self._metric_data = None
        self.discriminator = None

        if metric_data is not None:
            self.metric_data = metric_data

    @property
    def metric_data(self):
        """Gets the metric_data of this ListEdgeSiteMetricsResponse.

        监控数据

        :return: The metric_data of this ListEdgeSiteMetricsResponse.
        :rtype: list[:class:`huaweicloudsdkies.v1.MetricDataDetail`]
        """
        return self._metric_data

    @metric_data.setter
    def metric_data(self, metric_data):
        """Sets the metric_data of this ListEdgeSiteMetricsResponse.

        监控数据

        :param metric_data: The metric_data of this ListEdgeSiteMetricsResponse.
        :type metric_data: list[:class:`huaweicloudsdkies.v1.MetricDataDetail`]
        """
        self._metric_data = metric_data

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
        if not isinstance(other, ListEdgeSiteMetricsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
