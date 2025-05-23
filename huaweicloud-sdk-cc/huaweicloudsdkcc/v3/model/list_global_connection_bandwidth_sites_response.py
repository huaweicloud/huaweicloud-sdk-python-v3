# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGlobalConnectionBandwidthSitesResponse(SdkResponse):

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
        'site_infos': 'list[GlobalConnectionBandwidthSites]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'page_info': 'page_info',
        'site_infos': 'site_infos'
    }

    def __init__(self, request_id=None, page_info=None, site_infos=None):
        r"""ListGlobalConnectionBandwidthSitesResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求ID。
        :type request_id: str
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkcc.v3.PageInfo`
        :param site_infos: 站点信息列表响应体。
        :type site_infos: list[:class:`huaweicloudsdkcc.v3.GlobalConnectionBandwidthSites`]
        """
        
        super(ListGlobalConnectionBandwidthSitesResponse, self).__init__()

        self._request_id = None
        self._page_info = None
        self._site_infos = None
        self.discriminator = None

        self.request_id = request_id
        if page_info is not None:
            self.page_info = page_info
        self.site_infos = site_infos

    @property
    def request_id(self):
        r"""Gets the request_id of this ListGlobalConnectionBandwidthSitesResponse.

        请求ID。

        :return: The request_id of this ListGlobalConnectionBandwidthSitesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListGlobalConnectionBandwidthSitesResponse.

        请求ID。

        :param request_id: The request_id of this ListGlobalConnectionBandwidthSitesResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def page_info(self):
        r"""Gets the page_info of this ListGlobalConnectionBandwidthSitesResponse.

        :return: The page_info of this ListGlobalConnectionBandwidthSitesResponse.
        :rtype: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListGlobalConnectionBandwidthSitesResponse.

        :param page_info: The page_info of this ListGlobalConnectionBandwidthSitesResponse.
        :type page_info: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        self._page_info = page_info

    @property
    def site_infos(self):
        r"""Gets the site_infos of this ListGlobalConnectionBandwidthSitesResponse.

        站点信息列表响应体。

        :return: The site_infos of this ListGlobalConnectionBandwidthSitesResponse.
        :rtype: list[:class:`huaweicloudsdkcc.v3.GlobalConnectionBandwidthSites`]
        """
        return self._site_infos

    @site_infos.setter
    def site_infos(self, site_infos):
        r"""Sets the site_infos of this ListGlobalConnectionBandwidthSitesResponse.

        站点信息列表响应体。

        :param site_infos: The site_infos of this ListGlobalConnectionBandwidthSitesResponse.
        :type site_infos: list[:class:`huaweicloudsdkcc.v3.GlobalConnectionBandwidthSites`]
        """
        self._site_infos = site_infos

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
        if not isinstance(other, ListGlobalConnectionBandwidthSitesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
