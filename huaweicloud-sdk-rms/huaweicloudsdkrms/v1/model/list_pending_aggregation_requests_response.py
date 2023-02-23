# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPendingAggregationRequestsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pending_aggregation_requests': 'list[PendingAggregationRequest]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'pending_aggregation_requests': 'pending_aggregation_requests',
        'page_info': 'page_info'
    }

    def __init__(self, pending_aggregation_requests=None, page_info=None):
        """ListPendingAggregationRequestsResponse

        The model defined in huaweicloud sdk

        :param pending_aggregation_requests: 挂起的聚合请求列表。
        :type pending_aggregation_requests: list[:class:`huaweicloudsdkrms.v1.PendingAggregationRequest`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkrms.v1.PageInfo`
        """
        
        super(ListPendingAggregationRequestsResponse, self).__init__()

        self._pending_aggregation_requests = None
        self._page_info = None
        self.discriminator = None

        if pending_aggregation_requests is not None:
            self.pending_aggregation_requests = pending_aggregation_requests
        if page_info is not None:
            self.page_info = page_info

    @property
    def pending_aggregation_requests(self):
        """Gets the pending_aggregation_requests of this ListPendingAggregationRequestsResponse.

        挂起的聚合请求列表。

        :return: The pending_aggregation_requests of this ListPendingAggregationRequestsResponse.
        :rtype: list[:class:`huaweicloudsdkrms.v1.PendingAggregationRequest`]
        """
        return self._pending_aggregation_requests

    @pending_aggregation_requests.setter
    def pending_aggregation_requests(self, pending_aggregation_requests):
        """Sets the pending_aggregation_requests of this ListPendingAggregationRequestsResponse.

        挂起的聚合请求列表。

        :param pending_aggregation_requests: The pending_aggregation_requests of this ListPendingAggregationRequestsResponse.
        :type pending_aggregation_requests: list[:class:`huaweicloudsdkrms.v1.PendingAggregationRequest`]
        """
        self._pending_aggregation_requests = pending_aggregation_requests

    @property
    def page_info(self):
        """Gets the page_info of this ListPendingAggregationRequestsResponse.

        :return: The page_info of this ListPendingAggregationRequestsResponse.
        :rtype: :class:`huaweicloudsdkrms.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListPendingAggregationRequestsResponse.

        :param page_info: The page_info of this ListPendingAggregationRequestsResponse.
        :type page_info: :class:`huaweicloudsdkrms.v1.PageInfo`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListPendingAggregationRequestsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
