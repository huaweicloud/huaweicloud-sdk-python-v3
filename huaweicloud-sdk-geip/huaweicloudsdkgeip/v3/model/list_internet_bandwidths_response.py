# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInternetBandwidthsResponse(SdkResponse):

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
        'internet_bandwidths': 'list[ListInternetBandwidths]',
        'page_info': 'ListGlobalEipsResponseBodyPageInfo',
        'x_request_id': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'internet_bandwidths': 'internet_bandwidths',
        'page_info': 'page_info',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, request_id=None, internet_bandwidths=None, page_info=None, x_request_id=None):
        """ListInternetBandwidthsResponse

        The model defined in huaweicloud sdk

        :param request_id: 本次请求的编号
        :type request_id: str
        :param internet_bandwidths: 全域公网带宽列表
        :type internet_bandwidths: list[:class:`huaweicloudsdkgeip.v3.ListInternetBandwidths`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkgeip.v3.ListGlobalEipsResponseBodyPageInfo`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListInternetBandwidthsResponse, self).__init__()

        self._request_id = None
        self._internet_bandwidths = None
        self._page_info = None
        self._x_request_id = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if internet_bandwidths is not None:
            self.internet_bandwidths = internet_bandwidths
        if page_info is not None:
            self.page_info = page_info
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def request_id(self):
        """Gets the request_id of this ListInternetBandwidthsResponse.

        本次请求的编号

        :return: The request_id of this ListInternetBandwidthsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListInternetBandwidthsResponse.

        本次请求的编号

        :param request_id: The request_id of this ListInternetBandwidthsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def internet_bandwidths(self):
        """Gets the internet_bandwidths of this ListInternetBandwidthsResponse.

        全域公网带宽列表

        :return: The internet_bandwidths of this ListInternetBandwidthsResponse.
        :rtype: list[:class:`huaweicloudsdkgeip.v3.ListInternetBandwidths`]
        """
        return self._internet_bandwidths

    @internet_bandwidths.setter
    def internet_bandwidths(self, internet_bandwidths):
        """Sets the internet_bandwidths of this ListInternetBandwidthsResponse.

        全域公网带宽列表

        :param internet_bandwidths: The internet_bandwidths of this ListInternetBandwidthsResponse.
        :type internet_bandwidths: list[:class:`huaweicloudsdkgeip.v3.ListInternetBandwidths`]
        """
        self._internet_bandwidths = internet_bandwidths

    @property
    def page_info(self):
        """Gets the page_info of this ListInternetBandwidthsResponse.

        :return: The page_info of this ListInternetBandwidthsResponse.
        :rtype: :class:`huaweicloudsdkgeip.v3.ListGlobalEipsResponseBodyPageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListInternetBandwidthsResponse.

        :param page_info: The page_info of this ListInternetBandwidthsResponse.
        :type page_info: :class:`huaweicloudsdkgeip.v3.ListGlobalEipsResponseBodyPageInfo`
        """
        self._page_info = page_info

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListInternetBandwidthsResponse.

        :return: The x_request_id of this ListInternetBandwidthsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListInternetBandwidthsResponse.

        :param x_request_id: The x_request_id of this ListInternetBandwidthsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListInternetBandwidthsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
