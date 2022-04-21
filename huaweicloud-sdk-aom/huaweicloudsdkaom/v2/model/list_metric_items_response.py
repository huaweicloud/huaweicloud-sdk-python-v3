# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMetricItemsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'meta_data': 'MetaData',
        'metrics': 'list[MetricItemResultAPI]'
    }

    attribute_map = {
        'meta_data': 'metaData',
        'metrics': 'metrics'
    }

    def __init__(self, meta_data=None, metrics=None):
        """ListMetricItemsResponse

        The model defined in huaweicloud sdk

        :param meta_data: 
        :type meta_data: :class:`huaweicloudsdkaom.v2.MetaData`
        :param metrics: 指标对象列表。
        :type metrics: list[:class:`huaweicloudsdkaom.v2.MetricItemResultAPI`]
        """
        
        super(ListMetricItemsResponse, self).__init__()

        self._meta_data = None
        self._metrics = None
        self.discriminator = None

        if meta_data is not None:
            self.meta_data = meta_data
        if metrics is not None:
            self.metrics = metrics

    @property
    def meta_data(self):
        """Gets the meta_data of this ListMetricItemsResponse.


        :return: The meta_data of this ListMetricItemsResponse.
        :rtype: :class:`huaweicloudsdkaom.v2.MetaData`
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this ListMetricItemsResponse.


        :param meta_data: The meta_data of this ListMetricItemsResponse.
        :type meta_data: :class:`huaweicloudsdkaom.v2.MetaData`
        """
        self._meta_data = meta_data

    @property
    def metrics(self):
        """Gets the metrics of this ListMetricItemsResponse.

        指标对象列表。

        :return: The metrics of this ListMetricItemsResponse.
        :rtype: list[:class:`huaweicloudsdkaom.v2.MetricItemResultAPI`]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this ListMetricItemsResponse.

        指标对象列表。

        :param metrics: The metrics of this ListMetricItemsResponse.
        :type metrics: list[:class:`huaweicloudsdkaom.v2.MetricItemResultAPI`]
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
        if not isinstance(other, ListMetricItemsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
