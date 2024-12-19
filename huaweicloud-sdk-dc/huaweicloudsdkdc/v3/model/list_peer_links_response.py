# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPeerLinksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'peer_links': 'list[PeerLinkEntry]',
        'page_info': 'PageInfo',
        'request_id': 'str'
    }

    attribute_map = {
        'peer_links': 'peer_links',
        'page_info': 'page_info',
        'request_id': 'request_id'
    }

    def __init__(self, peer_links=None, page_info=None, request_id=None):
        """ListPeerLinksResponse

        The model defined in huaweicloud sdk

        :param peer_links: 专线关联连接列表。
        :type peer_links: list[:class:`huaweicloudsdkdc.v3.PeerLinkEntry`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkdc.v3.PageInfo`
        :param request_id: 请求ID。
        :type request_id: str
        """
        
        super(ListPeerLinksResponse, self).__init__()

        self._peer_links = None
        self._page_info = None
        self._request_id = None
        self.discriminator = None

        if peer_links is not None:
            self.peer_links = peer_links
        if page_info is not None:
            self.page_info = page_info
        if request_id is not None:
            self.request_id = request_id

    @property
    def peer_links(self):
        """Gets the peer_links of this ListPeerLinksResponse.

        专线关联连接列表。

        :return: The peer_links of this ListPeerLinksResponse.
        :rtype: list[:class:`huaweicloudsdkdc.v3.PeerLinkEntry`]
        """
        return self._peer_links

    @peer_links.setter
    def peer_links(self, peer_links):
        """Sets the peer_links of this ListPeerLinksResponse.

        专线关联连接列表。

        :param peer_links: The peer_links of this ListPeerLinksResponse.
        :type peer_links: list[:class:`huaweicloudsdkdc.v3.PeerLinkEntry`]
        """
        self._peer_links = peer_links

    @property
    def page_info(self):
        """Gets the page_info of this ListPeerLinksResponse.

        :return: The page_info of this ListPeerLinksResponse.
        :rtype: :class:`huaweicloudsdkdc.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListPeerLinksResponse.

        :param page_info: The page_info of this ListPeerLinksResponse.
        :type page_info: :class:`huaweicloudsdkdc.v3.PageInfo`
        """
        self._page_info = page_info

    @property
    def request_id(self):
        """Gets the request_id of this ListPeerLinksResponse.

        请求ID。

        :return: The request_id of this ListPeerLinksResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListPeerLinksResponse.

        请求ID。

        :param request_id: The request_id of this ListPeerLinksResponse.
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
        if not isinstance(other, ListPeerLinksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
