# coding: utf-8

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
        'request_id': 'str',
        'page_info': 'PageInfo',
        'inter_region_bandwidths': 'list[InterRegionBandwidth]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'page_info': 'page_info',
        'inter_region_bandwidths': 'inter_region_bandwidths'
    }

    def __init__(self, request_id=None, page_info=None, inter_region_bandwidths=None):
        """ListInterRegionBandwidthsResponse

        The model defined in huaweicloud sdk

        :param request_id: 资源ID标识符。
        :type request_id: str
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkcc.v3.PageInfo`
        :param inter_region_bandwidths: 域间带宽实例列表。
        :type inter_region_bandwidths: list[:class:`huaweicloudsdkcc.v3.InterRegionBandwidth`]
        """
        
        super(ListInterRegionBandwidthsResponse, self).__init__()

        self._request_id = None
        self._page_info = None
        self._inter_region_bandwidths = None
        self.discriminator = None

        self.request_id = request_id
        if page_info is not None:
            self.page_info = page_info
        self.inter_region_bandwidths = inter_region_bandwidths

    @property
    def request_id(self):
        """Gets the request_id of this ListInterRegionBandwidthsResponse.

        资源ID标识符。

        :return: The request_id of this ListInterRegionBandwidthsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListInterRegionBandwidthsResponse.

        资源ID标识符。

        :param request_id: The request_id of this ListInterRegionBandwidthsResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
