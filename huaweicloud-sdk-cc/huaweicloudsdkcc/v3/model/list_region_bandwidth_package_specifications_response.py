# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRegionBandwidthPackageSpecificationsResponse(SdkResponse):

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
        'region_specifications': 'list[RegionBandwidthPackageSpecification]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'page_info': 'page_info',
        'region_specifications': 'region_specifications'
    }

    def __init__(self, request_id=None, page_info=None, region_specifications=None):
        r"""ListRegionBandwidthPackageSpecificationsResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求ID。
        :type request_id: str
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkcc.v3.PageInfo`
        :param region_specifications: 租户带宽包城域规格列表。
        :type region_specifications: list[:class:`huaweicloudsdkcc.v3.RegionBandwidthPackageSpecification`]
        """
        
        super(ListRegionBandwidthPackageSpecificationsResponse, self).__init__()

        self._request_id = None
        self._page_info = None
        self._region_specifications = None
        self.discriminator = None

        self.request_id = request_id
        if page_info is not None:
            self.page_info = page_info
        self.region_specifications = region_specifications

    @property
    def request_id(self):
        r"""Gets the request_id of this ListRegionBandwidthPackageSpecificationsResponse.

        请求ID。

        :return: The request_id of this ListRegionBandwidthPackageSpecificationsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListRegionBandwidthPackageSpecificationsResponse.

        请求ID。

        :param request_id: The request_id of this ListRegionBandwidthPackageSpecificationsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def page_info(self):
        r"""Gets the page_info of this ListRegionBandwidthPackageSpecificationsResponse.

        :return: The page_info of this ListRegionBandwidthPackageSpecificationsResponse.
        :rtype: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListRegionBandwidthPackageSpecificationsResponse.

        :param page_info: The page_info of this ListRegionBandwidthPackageSpecificationsResponse.
        :type page_info: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        self._page_info = page_info

    @property
    def region_specifications(self):
        r"""Gets the region_specifications of this ListRegionBandwidthPackageSpecificationsResponse.

        租户带宽包城域规格列表。

        :return: The region_specifications of this ListRegionBandwidthPackageSpecificationsResponse.
        :rtype: list[:class:`huaweicloudsdkcc.v3.RegionBandwidthPackageSpecification`]
        """
        return self._region_specifications

    @region_specifications.setter
    def region_specifications(self, region_specifications):
        r"""Sets the region_specifications of this ListRegionBandwidthPackageSpecificationsResponse.

        租户带宽包城域规格列表。

        :param region_specifications: The region_specifications of this ListRegionBandwidthPackageSpecificationsResponse.
        :type region_specifications: list[:class:`huaweicloudsdkcc.v3.RegionBandwidthPackageSpecification`]
        """
        self._region_specifications = region_specifications

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
        if not isinstance(other, ListRegionBandwidthPackageSpecificationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
