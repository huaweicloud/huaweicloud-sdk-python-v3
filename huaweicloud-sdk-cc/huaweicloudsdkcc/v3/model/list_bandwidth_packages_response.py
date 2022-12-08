# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBandwidthPackagesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidth_packages': 'list[BandwidthPackage]',
        'page_info': 'PageInfo',
        'request_id': 'str'
    }

    attribute_map = {
        'bandwidth_packages': 'bandwidth_packages',
        'page_info': 'page_info',
        'request_id': 'request_id'
    }

    def __init__(self, bandwidth_packages=None, page_info=None, request_id=None):
        """ListBandwidthPackagesResponse

        The model defined in huaweicloud sdk

        :param bandwidth_packages: 带宽包实例列表。
        :type bandwidth_packages: list[:class:`huaweicloudsdkcc.v3.BandwidthPackage`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkcc.v3.PageInfo`
        :param request_id: 请求ID。
        :type request_id: str
        """
        
        super(ListBandwidthPackagesResponse, self).__init__()

        self._bandwidth_packages = None
        self._page_info = None
        self._request_id = None
        self.discriminator = None

        if bandwidth_packages is not None:
            self.bandwidth_packages = bandwidth_packages
        if page_info is not None:
            self.page_info = page_info
        if request_id is not None:
            self.request_id = request_id

    @property
    def bandwidth_packages(self):
        """Gets the bandwidth_packages of this ListBandwidthPackagesResponse.

        带宽包实例列表。

        :return: The bandwidth_packages of this ListBandwidthPackagesResponse.
        :rtype: list[:class:`huaweicloudsdkcc.v3.BandwidthPackage`]
        """
        return self._bandwidth_packages

    @bandwidth_packages.setter
    def bandwidth_packages(self, bandwidth_packages):
        """Sets the bandwidth_packages of this ListBandwidthPackagesResponse.

        带宽包实例列表。

        :param bandwidth_packages: The bandwidth_packages of this ListBandwidthPackagesResponse.
        :type bandwidth_packages: list[:class:`huaweicloudsdkcc.v3.BandwidthPackage`]
        """
        self._bandwidth_packages = bandwidth_packages

    @property
    def page_info(self):
        """Gets the page_info of this ListBandwidthPackagesResponse.

        :return: The page_info of this ListBandwidthPackagesResponse.
        :rtype: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListBandwidthPackagesResponse.

        :param page_info: The page_info of this ListBandwidthPackagesResponse.
        :type page_info: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        self._page_info = page_info

    @property
    def request_id(self):
        """Gets the request_id of this ListBandwidthPackagesResponse.

        请求ID。

        :return: The request_id of this ListBandwidthPackagesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListBandwidthPackagesResponse.

        请求ID。

        :param request_id: The request_id of this ListBandwidthPackagesResponse.
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
        if not isinstance(other, ListBandwidthPackagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
