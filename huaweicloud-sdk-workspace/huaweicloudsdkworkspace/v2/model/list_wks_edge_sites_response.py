# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWksEdgeSitesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'wks_edge_sites': 'list[WksEdgeSiteDetail]',
        'total_count': 'int'
    }

    attribute_map = {
        'wks_edge_sites': 'wks_edge_sites',
        'total_count': 'total_count'
    }

    def __init__(self, wks_edge_sites=None, total_count=None):
        r"""ListWksEdgeSitesResponse

        The model defined in huaweicloud sdk

        :param wks_edge_sites: 边缘小站列表。
        :type wks_edge_sites: list[:class:`huaweicloudsdkworkspace.v2.WksEdgeSiteDetail`]
        :param total_count: 站点总数。
        :type total_count: int
        """
        
        super(ListWksEdgeSitesResponse, self).__init__()

        self._wks_edge_sites = None
        self._total_count = None
        self.discriminator = None

        if wks_edge_sites is not None:
            self.wks_edge_sites = wks_edge_sites
        if total_count is not None:
            self.total_count = total_count

    @property
    def wks_edge_sites(self):
        r"""Gets the wks_edge_sites of this ListWksEdgeSitesResponse.

        边缘小站列表。

        :return: The wks_edge_sites of this ListWksEdgeSitesResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.WksEdgeSiteDetail`]
        """
        return self._wks_edge_sites

    @wks_edge_sites.setter
    def wks_edge_sites(self, wks_edge_sites):
        r"""Sets the wks_edge_sites of this ListWksEdgeSitesResponse.

        边缘小站列表。

        :param wks_edge_sites: The wks_edge_sites of this ListWksEdgeSitesResponse.
        :type wks_edge_sites: list[:class:`huaweicloudsdkworkspace.v2.WksEdgeSiteDetail`]
        """
        self._wks_edge_sites = wks_edge_sites

    @property
    def total_count(self):
        r"""Gets the total_count of this ListWksEdgeSitesResponse.

        站点总数。

        :return: The total_count of this ListWksEdgeSitesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListWksEdgeSitesResponse.

        站点总数。

        :param total_count: The total_count of this ListWksEdgeSitesResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListWksEdgeSitesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
