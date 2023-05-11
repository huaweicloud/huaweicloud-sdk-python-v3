# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDownloadResourceStatDataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_statistics': 'list[ResourceStatDataRsp]'
    }

    attribute_map = {
        'metric_statistics': 'metric_statistics'
    }

    def __init__(self, metric_statistics=None):
        """BatchDownloadResourceStatDataResponse

        The model defined in huaweicloud sdk

        :param metric_statistics: 资源统计数据列表
        :type metric_statistics: list[:class:`huaweicloudsdkeihealth.v1.ResourceStatDataRsp`]
        """
        
        super(BatchDownloadResourceStatDataResponse, self).__init__()

        self._metric_statistics = None
        self.discriminator = None

        if metric_statistics is not None:
            self.metric_statistics = metric_statistics

    @property
    def metric_statistics(self):
        """Gets the metric_statistics of this BatchDownloadResourceStatDataResponse.

        资源统计数据列表

        :return: The metric_statistics of this BatchDownloadResourceStatDataResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.ResourceStatDataRsp`]
        """
        return self._metric_statistics

    @metric_statistics.setter
    def metric_statistics(self, metric_statistics):
        """Sets the metric_statistics of this BatchDownloadResourceStatDataResponse.

        资源统计数据列表

        :param metric_statistics: The metric_statistics of this BatchDownloadResourceStatDataResponse.
        :type metric_statistics: list[:class:`huaweicloudsdkeihealth.v1.ResourceStatDataRsp`]
        """
        self._metric_statistics = metric_statistics

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
        if not isinstance(other, BatchDownloadResourceStatDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
