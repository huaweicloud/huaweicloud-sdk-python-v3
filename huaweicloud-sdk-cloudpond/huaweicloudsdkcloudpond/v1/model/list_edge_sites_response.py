# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEdgeSitesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'edge_sites': 'list[EdgeSiteDetail]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'edge_sites': 'edge_sites',
        'page_info': 'page_info'
    }

    def __init__(self, edge_sites=None, page_info=None):
        r"""ListEdgeSitesResponse

        The model defined in huaweicloud sdk

        :param edge_sites: 边缘小站列表。
        :type edge_sites: list[:class:`huaweicloudsdkcloudpond.v1.EdgeSiteDetail`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkcloudpond.v1.PageInfo`
        """
        
        super(ListEdgeSitesResponse, self).__init__()

        self._edge_sites = None
        self._page_info = None
        self.discriminator = None

        if edge_sites is not None:
            self.edge_sites = edge_sites
        if page_info is not None:
            self.page_info = page_info

    @property
    def edge_sites(self):
        r"""Gets the edge_sites of this ListEdgeSitesResponse.

        边缘小站列表。

        :return: The edge_sites of this ListEdgeSitesResponse.
        :rtype: list[:class:`huaweicloudsdkcloudpond.v1.EdgeSiteDetail`]
        """
        return self._edge_sites

    @edge_sites.setter
    def edge_sites(self, edge_sites):
        r"""Sets the edge_sites of this ListEdgeSitesResponse.

        边缘小站列表。

        :param edge_sites: The edge_sites of this ListEdgeSitesResponse.
        :type edge_sites: list[:class:`huaweicloudsdkcloudpond.v1.EdgeSiteDetail`]
        """
        self._edge_sites = edge_sites

    @property
    def page_info(self):
        r"""Gets the page_info of this ListEdgeSitesResponse.

        :return: The page_info of this ListEdgeSitesResponse.
        :rtype: :class:`huaweicloudsdkcloudpond.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListEdgeSitesResponse.

        :param page_info: The page_info of this ListEdgeSitesResponse.
        :type page_info: :class:`huaweicloudsdkcloudpond.v1.PageInfo`
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
        if not isinstance(other, ListEdgeSitesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
