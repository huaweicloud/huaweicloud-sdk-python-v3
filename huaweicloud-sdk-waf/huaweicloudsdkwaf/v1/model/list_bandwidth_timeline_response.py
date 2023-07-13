# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBandwidthTimelineResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'body': 'list[BandwidthStatisticsTimelineItem]'
    }

    attribute_map = {
        'body': 'body'
    }

    def __init__(self, body=None):
        """ListBandwidthTimelineResponse

        The model defined in huaweicloud sdk

        :param body: 带宽时间线统计数据，包括带宽（BANDWIDTH）、入带宽（IN_BANDWIDTH）以及出带宽（OUT_BANDWIDTH）统计数据。
        :type body: list[:class:`huaweicloudsdkwaf.v1.BandwidthStatisticsTimelineItem`]
        """
        
        super(ListBandwidthTimelineResponse, self).__init__()

        self._body = None
        self.discriminator = None

        if body is not None:
            self.body = body

    @property
    def body(self):
        """Gets the body of this ListBandwidthTimelineResponse.

        带宽时间线统计数据，包括带宽（BANDWIDTH）、入带宽（IN_BANDWIDTH）以及出带宽（OUT_BANDWIDTH）统计数据。

        :return: The body of this ListBandwidthTimelineResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.BandwidthStatisticsTimelineItem`]
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ListBandwidthTimelineResponse.

        带宽时间线统计数据，包括带宽（BANDWIDTH）、入带宽（IN_BANDWIDTH）以及出带宽（OUT_BANDWIDTH）统计数据。

        :param body: The body of this ListBandwidthTimelineResponse.
        :type body: list[:class:`huaweicloudsdkwaf.v1.BandwidthStatisticsTimelineItem`]
        """
        self._body = body

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
        if not isinstance(other, ListBandwidthTimelineResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
