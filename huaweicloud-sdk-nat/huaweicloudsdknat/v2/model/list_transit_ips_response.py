# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTransitIpsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'transit_ips': 'list[TransitIp]',
        'page_info': 'PageInfo',
        'request_id': 'str'
    }

    attribute_map = {
        'transit_ips': 'transit_ips',
        'page_info': 'page_info',
        'request_id': 'request_id'
    }

    def __init__(self, transit_ips=None, page_info=None, request_id=None):
        r"""ListTransitIpsResponse

        The model defined in huaweicloud sdk

        :param transit_ips: 查询中转IP列表的响应体。
        :type transit_ips: list[:class:`huaweicloudsdknat.v2.TransitIp`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdknat.v2.PageInfo`
        :param request_id: 请求ID。
        :type request_id: str
        """
        
        super(ListTransitIpsResponse, self).__init__()

        self._transit_ips = None
        self._page_info = None
        self._request_id = None
        self.discriminator = None

        if transit_ips is not None:
            self.transit_ips = transit_ips
        if page_info is not None:
            self.page_info = page_info
        if request_id is not None:
            self.request_id = request_id

    @property
    def transit_ips(self):
        r"""Gets the transit_ips of this ListTransitIpsResponse.

        查询中转IP列表的响应体。

        :return: The transit_ips of this ListTransitIpsResponse.
        :rtype: list[:class:`huaweicloudsdknat.v2.TransitIp`]
        """
        return self._transit_ips

    @transit_ips.setter
    def transit_ips(self, transit_ips):
        r"""Sets the transit_ips of this ListTransitIpsResponse.

        查询中转IP列表的响应体。

        :param transit_ips: The transit_ips of this ListTransitIpsResponse.
        :type transit_ips: list[:class:`huaweicloudsdknat.v2.TransitIp`]
        """
        self._transit_ips = transit_ips

    @property
    def page_info(self):
        r"""Gets the page_info of this ListTransitIpsResponse.

        :return: The page_info of this ListTransitIpsResponse.
        :rtype: :class:`huaweicloudsdknat.v2.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListTransitIpsResponse.

        :param page_info: The page_info of this ListTransitIpsResponse.
        :type page_info: :class:`huaweicloudsdknat.v2.PageInfo`
        """
        self._page_info = page_info

    @property
    def request_id(self):
        r"""Gets the request_id of this ListTransitIpsResponse.

        请求ID。

        :return: The request_id of this ListTransitIpsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListTransitIpsResponse.

        请求ID。

        :param request_id: The request_id of this ListTransitIpsResponse.
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
        if not isinstance(other, ListTransitIpsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
