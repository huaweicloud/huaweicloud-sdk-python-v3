# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDirectConnectLocationsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'direct_connect_locations': 'list[DirectConnectLocationEntry]',
        'page_info': 'PageInfo',
        'request_id': 'str'
    }

    attribute_map = {
        'direct_connect_locations': 'direct_connect_locations',
        'page_info': 'page_info',
        'request_id': 'request_id'
    }

    def __init__(self, direct_connect_locations=None, page_info=None, request_id=None):
        r"""ListDirectConnectLocationsResponse

        The model defined in huaweicloud sdk

        :param direct_connect_locations: 专线接入点列表
        :type direct_connect_locations: list[:class:`huaweicloudsdkdc.v3.DirectConnectLocationEntry`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkdc.v3.PageInfo`
        :param request_id: 请求ID。
        :type request_id: str
        """
        
        super(ListDirectConnectLocationsResponse, self).__init__()

        self._direct_connect_locations = None
        self._page_info = None
        self._request_id = None
        self.discriminator = None

        if direct_connect_locations is not None:
            self.direct_connect_locations = direct_connect_locations
        if page_info is not None:
            self.page_info = page_info
        if request_id is not None:
            self.request_id = request_id

    @property
    def direct_connect_locations(self):
        r"""Gets the direct_connect_locations of this ListDirectConnectLocationsResponse.

        专线接入点列表

        :return: The direct_connect_locations of this ListDirectConnectLocationsResponse.
        :rtype: list[:class:`huaweicloudsdkdc.v3.DirectConnectLocationEntry`]
        """
        return self._direct_connect_locations

    @direct_connect_locations.setter
    def direct_connect_locations(self, direct_connect_locations):
        r"""Sets the direct_connect_locations of this ListDirectConnectLocationsResponse.

        专线接入点列表

        :param direct_connect_locations: The direct_connect_locations of this ListDirectConnectLocationsResponse.
        :type direct_connect_locations: list[:class:`huaweicloudsdkdc.v3.DirectConnectLocationEntry`]
        """
        self._direct_connect_locations = direct_connect_locations

    @property
    def page_info(self):
        r"""Gets the page_info of this ListDirectConnectLocationsResponse.

        :return: The page_info of this ListDirectConnectLocationsResponse.
        :rtype: :class:`huaweicloudsdkdc.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListDirectConnectLocationsResponse.

        :param page_info: The page_info of this ListDirectConnectLocationsResponse.
        :type page_info: :class:`huaweicloudsdkdc.v3.PageInfo`
        """
        self._page_info = page_info

    @property
    def request_id(self):
        r"""Gets the request_id of this ListDirectConnectLocationsResponse.

        请求ID。

        :return: The request_id of this ListDirectConnectLocationsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListDirectConnectLocationsResponse.

        请求ID。

        :param request_id: The request_id of this ListDirectConnectLocationsResponse.
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
        if not isinstance(other, ListDirectConnectLocationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
