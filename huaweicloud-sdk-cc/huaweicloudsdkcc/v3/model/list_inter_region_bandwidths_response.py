# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInterRegionBandwidthsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'inter_region_bandwidths': 'list[InterRegionBandwidth]',
        'page_info': 'PageInfo',
        'request_id': 'str'
    }

    attribute_map = {
        'inter_region_bandwidths': 'inter_region_bandwidths',
        'page_info': 'page_info',
        'request_id': 'request_id'
    }

    def __init__(self, inter_region_bandwidths=None, page_info=None, request_id=None):
        """ListInterRegionBandwidthsResponse

        The model defined in huaweicloud sdk

        :param inter_region_bandwidths: 域间带宽实例列表。
        :type inter_region_bandwidths: list[:class:`huaweicloudsdkcc.v3.InterRegionBandwidth`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkcc.v3.PageInfo`
        :param request_id: 请求ID。
        :type request_id: str
        """
        
        super(ListInterRegionBandwidthsResponse, self).__init__()

        self._inter_region_bandwidths = None
        self._page_info = None
        self._request_id = None
        self.discriminator = None

        if inter_region_bandwidths is not None:
            self.inter_region_bandwidths = inter_region_bandwidths
        if page_info is not None:
            self.page_info = page_info
        if request_id is not None:
            self.request_id = request_id

    @property
    def inter_region_bandwidths(self):
        """Gets the inter_region_bandwidths of this ListInterRegionBandwidthsResponse.

        域间带宽实例列表。

        :return: The inter_region_bandwidths of this ListInterRegionBandwidthsResponse.
        :rtype: list[:class:`huaweicloudsdkcc.v3.InterRegionBandwidth`]
        """
        return self._inter_region_bandwidths

    @inter_region_bandwidths.setter
    def inter_region_bandwidths(self, inter_region_bandwidths):
        """Sets the inter_region_bandwidths of this ListInterRegionBandwidthsResponse.

        域间带宽实例列表。

        :param inter_region_bandwidths: The inter_region_bandwidths of this ListInterRegionBandwidthsResponse.
        :type inter_region_bandwidths: list[:class:`huaweicloudsdkcc.v3.InterRegionBandwidth`]
        """
        self._inter_region_bandwidths = inter_region_bandwidths

    @property
    def page_info(self):
        """Gets the page_info of this ListInterRegionBandwidthsResponse.

        :return: The page_info of this ListInterRegionBandwidthsResponse.
        :rtype: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListInterRegionBandwidthsResponse.

        :param page_info: The page_info of this ListInterRegionBandwidthsResponse.
        :type page_info: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        self._page_info = page_info

    @property
    def request_id(self):
        """Gets the request_id of this ListInterRegionBandwidthsResponse.

        请求ID。

        :return: The request_id of this ListInterRegionBandwidthsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListInterRegionBandwidthsResponse.

        请求ID。

        :param request_id: The request_id of this ListInterRegionBandwidthsResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, ListInterRegionBandwidthsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
