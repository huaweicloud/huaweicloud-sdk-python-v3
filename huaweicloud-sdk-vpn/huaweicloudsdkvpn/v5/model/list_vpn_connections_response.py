# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVpnConnectionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpn_connections': 'list[ResponseVpnConnection]',
        'page_info': 'PageInfo',
        'request_id': 'str',
        'total_count': 'int',
        'header_response_token': 'str'
    }

    attribute_map = {
        'vpn_connections': 'vpn_connections',
        'page_info': 'page_info',
        'request_id': 'request_id',
        'total_count': 'total_count',
        'header_response_token': 'header-response-token'
    }

    def __init__(self, vpn_connections=None, page_info=None, request_id=None, total_count=None, header_response_token=None):
        """ListVpnConnectionsResponse

        The model defined in huaweicloud sdk

        :param vpn_connections: 
        :type vpn_connections: list[:class:`huaweicloudsdkvpn.v5.ResponseVpnConnection`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkvpn.v5.PageInfo`
        :param request_id: 请求ID
        :type request_id: str
        :param total_count: 租户下连接总数
        :type total_count: int
        :param header_response_token: 
        :type header_response_token: str
        """
        
        super(ListVpnConnectionsResponse, self).__init__()

        self._vpn_connections = None
        self._page_info = None
        self._request_id = None
        self._total_count = None
        self._header_response_token = None
        self.discriminator = None

        if vpn_connections is not None:
            self.vpn_connections = vpn_connections
        if page_info is not None:
            self.page_info = page_info
        if request_id is not None:
            self.request_id = request_id
        if total_count is not None:
            self.total_count = total_count
        if header_response_token is not None:
            self.header_response_token = header_response_token

    @property
    def vpn_connections(self):
        """Gets the vpn_connections of this ListVpnConnectionsResponse.

        :return: The vpn_connections of this ListVpnConnectionsResponse.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.ResponseVpnConnection`]
        """
        return self._vpn_connections

    @vpn_connections.setter
    def vpn_connections(self, vpn_connections):
        """Sets the vpn_connections of this ListVpnConnectionsResponse.

        :param vpn_connections: The vpn_connections of this ListVpnConnectionsResponse.
        :type vpn_connections: list[:class:`huaweicloudsdkvpn.v5.ResponseVpnConnection`]
        """
        self._vpn_connections = vpn_connections

    @property
    def page_info(self):
        """Gets the page_info of this ListVpnConnectionsResponse.

        :return: The page_info of this ListVpnConnectionsResponse.
        :rtype: :class:`huaweicloudsdkvpn.v5.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListVpnConnectionsResponse.

        :param page_info: The page_info of this ListVpnConnectionsResponse.
        :type page_info: :class:`huaweicloudsdkvpn.v5.PageInfo`
        """
        self._page_info = page_info

    @property
    def request_id(self):
        """Gets the request_id of this ListVpnConnectionsResponse.

        请求ID

        :return: The request_id of this ListVpnConnectionsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListVpnConnectionsResponse.

        请求ID

        :param request_id: The request_id of this ListVpnConnectionsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def total_count(self):
        """Gets the total_count of this ListVpnConnectionsResponse.

        租户下连接总数

        :return: The total_count of this ListVpnConnectionsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListVpnConnectionsResponse.

        租户下连接总数

        :param total_count: The total_count of this ListVpnConnectionsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def header_response_token(self):
        """Gets the header_response_token of this ListVpnConnectionsResponse.

        :return: The header_response_token of this ListVpnConnectionsResponse.
        :rtype: str
        """
        return self._header_response_token

    @header_response_token.setter
    def header_response_token(self, header_response_token):
        """Sets the header_response_token of this ListVpnConnectionsResponse.

        :param header_response_token: The header_response_token of this ListVpnConnectionsResponse.
        :type header_response_token: str
        """
        self._header_response_token = header_response_token

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
        if not isinstance(other, ListVpnConnectionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
