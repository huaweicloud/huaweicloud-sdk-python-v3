# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServerMetricDataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_metrics': 'list[ServerMetricData]'
    }

    attribute_map = {
        'server_metrics': 'server_metrics'
    }

    def __init__(self, server_metrics=None):
        r"""ListServerMetricDataResponse

        The model defined in huaweicloud sdk

        :param server_metrics: 监控数据。
        :type server_metrics: list[:class:`huaweicloudsdkworkspaceapp.v1.ServerMetricData`]
        """
        
        super(ListServerMetricDataResponse, self).__init__()

        self._server_metrics = None
        self.discriminator = None

        if server_metrics is not None:
            self.server_metrics = server_metrics

    @property
    def server_metrics(self):
        r"""Gets the server_metrics of this ListServerMetricDataResponse.

        监控数据。

        :return: The server_metrics of this ListServerMetricDataResponse.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.ServerMetricData`]
        """
        return self._server_metrics

    @server_metrics.setter
    def server_metrics(self, server_metrics):
        r"""Sets the server_metrics of this ListServerMetricDataResponse.

        监控数据。

        :param server_metrics: The server_metrics of this ListServerMetricDataResponse.
        :type server_metrics: list[:class:`huaweicloudsdkworkspaceapp.v1.ServerMetricData`]
        """
        self._server_metrics = server_metrics

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
        if not isinstance(other, ListServerMetricDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
