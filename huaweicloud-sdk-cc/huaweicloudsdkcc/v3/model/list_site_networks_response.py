# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSiteNetworksResponse(SdkResponse):

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
        'site_networks': 'list[SiteNetworkEntry]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'page_info': 'page_info',
        'site_networks': 'site_networks'
    }

    def __init__(self, request_id=None, page_info=None, site_networks=None):
        r"""ListSiteNetworksResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求ID。
        :type request_id: str
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkcc.v3.PageInfo`
        :param site_networks: 分支网络列表。
        :type site_networks: list[:class:`huaweicloudsdkcc.v3.SiteNetworkEntry`]
        """
        
        super(ListSiteNetworksResponse, self).__init__()

        self._request_id = None
        self._page_info = None
        self._site_networks = None
        self.discriminator = None

        self.request_id = request_id
        if page_info is not None:
            self.page_info = page_info
        self.site_networks = site_networks

    @property
    def request_id(self):
        r"""Gets the request_id of this ListSiteNetworksResponse.

        请求ID。

        :return: The request_id of this ListSiteNetworksResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListSiteNetworksResponse.

        请求ID。

        :param request_id: The request_id of this ListSiteNetworksResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def page_info(self):
        r"""Gets the page_info of this ListSiteNetworksResponse.

        :return: The page_info of this ListSiteNetworksResponse.
        :rtype: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListSiteNetworksResponse.

        :param page_info: The page_info of this ListSiteNetworksResponse.
        :type page_info: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        self._page_info = page_info

    @property
    def site_networks(self):
        r"""Gets the site_networks of this ListSiteNetworksResponse.

        分支网络列表。

        :return: The site_networks of this ListSiteNetworksResponse.
        :rtype: list[:class:`huaweicloudsdkcc.v3.SiteNetworkEntry`]
        """
        return self._site_networks

    @site_networks.setter
    def site_networks(self, site_networks):
        r"""Sets the site_networks of this ListSiteNetworksResponse.

        分支网络列表。

        :param site_networks: The site_networks of this ListSiteNetworksResponse.
        :type site_networks: list[:class:`huaweicloudsdkcc.v3.SiteNetworkEntry`]
        """
        self._site_networks = site_networks

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
        if not isinstance(other, ListSiteNetworksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
