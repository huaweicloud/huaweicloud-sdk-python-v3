# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBandwidthPackageSitesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidth_package_sites': 'list[BandwidthPackageSite]',
        'request_id': 'str',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'bandwidth_package_sites': 'bandwidth_package_sites',
        'request_id': 'request_id',
        'page_info': 'page_info'
    }

    def __init__(self, bandwidth_package_sites=None, request_id=None, page_info=None):
        r"""ListBandwidthPackageSitesResponse

        The model defined in huaweicloud sdk

        :param bandwidth_package_sites: 站点列表表。
        :type bandwidth_package_sites: list[:class:`huaweicloudsdkcc.v3.BandwidthPackageSite`]
        :param request_id: 请求ID。
        :type request_id: str
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        
        super(ListBandwidthPackageSitesResponse, self).__init__()

        self._bandwidth_package_sites = None
        self._request_id = None
        self._page_info = None
        self.discriminator = None

        if bandwidth_package_sites is not None:
            self.bandwidth_package_sites = bandwidth_package_sites
        if request_id is not None:
            self.request_id = request_id
        if page_info is not None:
            self.page_info = page_info

    @property
    def bandwidth_package_sites(self):
        r"""Gets the bandwidth_package_sites of this ListBandwidthPackageSitesResponse.

        站点列表表。

        :return: The bandwidth_package_sites of this ListBandwidthPackageSitesResponse.
        :rtype: list[:class:`huaweicloudsdkcc.v3.BandwidthPackageSite`]
        """
        return self._bandwidth_package_sites

    @bandwidth_package_sites.setter
    def bandwidth_package_sites(self, bandwidth_package_sites):
        r"""Sets the bandwidth_package_sites of this ListBandwidthPackageSitesResponse.

        站点列表表。

        :param bandwidth_package_sites: The bandwidth_package_sites of this ListBandwidthPackageSitesResponse.
        :type bandwidth_package_sites: list[:class:`huaweicloudsdkcc.v3.BandwidthPackageSite`]
        """
        self._bandwidth_package_sites = bandwidth_package_sites

    @property
    def request_id(self):
        r"""Gets the request_id of this ListBandwidthPackageSitesResponse.

        请求ID。

        :return: The request_id of this ListBandwidthPackageSitesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListBandwidthPackageSitesResponse.

        请求ID。

        :param request_id: The request_id of this ListBandwidthPackageSitesResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def page_info(self):
        r"""Gets the page_info of this ListBandwidthPackageSitesResponse.

        :return: The page_info of this ListBandwidthPackageSitesResponse.
        :rtype: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListBandwidthPackageSitesResponse.

        :param page_info: The page_info of this ListBandwidthPackageSitesResponse.
        :type page_info: :class:`huaweicloudsdkcc.v3.PageInfo`
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
        if not isinstance(other, ListBandwidthPackageSitesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
