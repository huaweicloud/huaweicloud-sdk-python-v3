# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBandwidthPackageLinesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidth_package_lines': 'list[BandwidthPackageLine]',
        'request_id': 'str',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'bandwidth_package_lines': 'bandwidth_package_lines',
        'request_id': 'request_id',
        'page_info': 'page_info'
    }

    def __init__(self, bandwidth_package_lines=None, request_id=None, page_info=None):
        r"""ListBandwidthPackageLinesResponse

        The model defined in huaweicloud sdk

        :param bandwidth_package_lines: 带宽包线路列表。
        :type bandwidth_package_lines: list[:class:`huaweicloudsdkcc.v3.BandwidthPackageLine`]
        :param request_id: 请求ID。
        :type request_id: str
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        
        super(ListBandwidthPackageLinesResponse, self).__init__()

        self._bandwidth_package_lines = None
        self._request_id = None
        self._page_info = None
        self.discriminator = None

        if bandwidth_package_lines is not None:
            self.bandwidth_package_lines = bandwidth_package_lines
        if request_id is not None:
            self.request_id = request_id
        if page_info is not None:
            self.page_info = page_info

    @property
    def bandwidth_package_lines(self):
        r"""Gets the bandwidth_package_lines of this ListBandwidthPackageLinesResponse.

        带宽包线路列表。

        :return: The bandwidth_package_lines of this ListBandwidthPackageLinesResponse.
        :rtype: list[:class:`huaweicloudsdkcc.v3.BandwidthPackageLine`]
        """
        return self._bandwidth_package_lines

    @bandwidth_package_lines.setter
    def bandwidth_package_lines(self, bandwidth_package_lines):
        r"""Sets the bandwidth_package_lines of this ListBandwidthPackageLinesResponse.

        带宽包线路列表。

        :param bandwidth_package_lines: The bandwidth_package_lines of this ListBandwidthPackageLinesResponse.
        :type bandwidth_package_lines: list[:class:`huaweicloudsdkcc.v3.BandwidthPackageLine`]
        """
        self._bandwidth_package_lines = bandwidth_package_lines

    @property
    def request_id(self):
        r"""Gets the request_id of this ListBandwidthPackageLinesResponse.

        请求ID。

        :return: The request_id of this ListBandwidthPackageLinesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListBandwidthPackageLinesResponse.

        请求ID。

        :param request_id: The request_id of this ListBandwidthPackageLinesResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def page_info(self):
        r"""Gets the page_info of this ListBandwidthPackageLinesResponse.

        :return: The page_info of this ListBandwidthPackageLinesResponse.
        :rtype: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListBandwidthPackageLinesResponse.

        :param page_info: The page_info of this ListBandwidthPackageLinesResponse.
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
        if not isinstance(other, ListBandwidthPackageLinesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
