# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBandwidthPackageLevelsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidth_package_levels': 'list[BandwidthPackageLevel]',
        'request_id': 'str',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'bandwidth_package_levels': 'bandwidth_package_levels',
        'request_id': 'request_id',
        'page_info': 'page_info'
    }

    def __init__(self, bandwidth_package_levels=None, request_id=None, page_info=None):
        r"""ListBandwidthPackageLevelsResponse

        The model defined in huaweicloud sdk

        :param bandwidth_package_levels: 带宽包等级列表。
        :type bandwidth_package_levels: list[:class:`huaweicloudsdkcc.v3.BandwidthPackageLevel`]
        :param request_id: 请求ID。
        :type request_id: str
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        
        super(ListBandwidthPackageLevelsResponse, self).__init__()

        self._bandwidth_package_levels = None
        self._request_id = None
        self._page_info = None
        self.discriminator = None

        if bandwidth_package_levels is not None:
            self.bandwidth_package_levels = bandwidth_package_levels
        if request_id is not None:
            self.request_id = request_id
        if page_info is not None:
            self.page_info = page_info

    @property
    def bandwidth_package_levels(self):
        r"""Gets the bandwidth_package_levels of this ListBandwidthPackageLevelsResponse.

        带宽包等级列表。

        :return: The bandwidth_package_levels of this ListBandwidthPackageLevelsResponse.
        :rtype: list[:class:`huaweicloudsdkcc.v3.BandwidthPackageLevel`]
        """
        return self._bandwidth_package_levels

    @bandwidth_package_levels.setter
    def bandwidth_package_levels(self, bandwidth_package_levels):
        r"""Sets the bandwidth_package_levels of this ListBandwidthPackageLevelsResponse.

        带宽包等级列表。

        :param bandwidth_package_levels: The bandwidth_package_levels of this ListBandwidthPackageLevelsResponse.
        :type bandwidth_package_levels: list[:class:`huaweicloudsdkcc.v3.BandwidthPackageLevel`]
        """
        self._bandwidth_package_levels = bandwidth_package_levels

    @property
    def request_id(self):
        r"""Gets the request_id of this ListBandwidthPackageLevelsResponse.

        请求ID。

        :return: The request_id of this ListBandwidthPackageLevelsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListBandwidthPackageLevelsResponse.

        请求ID。

        :param request_id: The request_id of this ListBandwidthPackageLevelsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def page_info(self):
        r"""Gets the page_info of this ListBandwidthPackageLevelsResponse.

        :return: The page_info of this ListBandwidthPackageLevelsResponse.
        :rtype: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListBandwidthPackageLevelsResponse.

        :param page_info: The page_info of this ListBandwidthPackageLevelsResponse.
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
        if not isinstance(other, ListBandwidthPackageLevelsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
