# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVpnServersByVgwResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpn_servers': 'list[ShowServerResponse]',
        'total_count': 'int',
        'page_info': 'PageInfo',
        'request_id': 'str',
        'header_response_token': 'str'
    }

    attribute_map = {
        'vpn_servers': 'vpn_servers',
        'total_count': 'total_count',
        'page_info': 'page_info',
        'request_id': 'request_id',
        'header_response_token': 'header-response-token'
    }

    def __init__(self, vpn_servers=None, total_count=None, page_info=None, request_id=None, header_response_token=None):
        r"""ListVpnServersByVgwResponse

        The model defined in huaweicloud sdk

        :param vpn_servers: 服务端列表
        :type vpn_servers: list[:class:`huaweicloudsdkvpn.v5.ShowServerResponse`]
        :param total_count: 总数
        :type total_count: int
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkvpn.v5.PageInfo`
        :param request_id: 请求id
        :type request_id: str
        :param header_response_token: 
        :type header_response_token: str
        """
        
        super(ListVpnServersByVgwResponse, self).__init__()

        self._vpn_servers = None
        self._total_count = None
        self._page_info = None
        self._request_id = None
        self._header_response_token = None
        self.discriminator = None

        if vpn_servers is not None:
            self.vpn_servers = vpn_servers
        if total_count is not None:
            self.total_count = total_count
        if page_info is not None:
            self.page_info = page_info
        if request_id is not None:
            self.request_id = request_id
        if header_response_token is not None:
            self.header_response_token = header_response_token

    @property
    def vpn_servers(self):
        r"""Gets the vpn_servers of this ListVpnServersByVgwResponse.

        服务端列表

        :return: The vpn_servers of this ListVpnServersByVgwResponse.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.ShowServerResponse`]
        """
        return self._vpn_servers

    @vpn_servers.setter
    def vpn_servers(self, vpn_servers):
        r"""Sets the vpn_servers of this ListVpnServersByVgwResponse.

        服务端列表

        :param vpn_servers: The vpn_servers of this ListVpnServersByVgwResponse.
        :type vpn_servers: list[:class:`huaweicloudsdkvpn.v5.ShowServerResponse`]
        """
        self._vpn_servers = vpn_servers

    @property
    def total_count(self):
        r"""Gets the total_count of this ListVpnServersByVgwResponse.

        总数

        :return: The total_count of this ListVpnServersByVgwResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListVpnServersByVgwResponse.

        总数

        :param total_count: The total_count of this ListVpnServersByVgwResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def page_info(self):
        r"""Gets the page_info of this ListVpnServersByVgwResponse.

        :return: The page_info of this ListVpnServersByVgwResponse.
        :rtype: :class:`huaweicloudsdkvpn.v5.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListVpnServersByVgwResponse.

        :param page_info: The page_info of this ListVpnServersByVgwResponse.
        :type page_info: :class:`huaweicloudsdkvpn.v5.PageInfo`
        """
        self._page_info = page_info

    @property
    def request_id(self):
        r"""Gets the request_id of this ListVpnServersByVgwResponse.

        请求id

        :return: The request_id of this ListVpnServersByVgwResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListVpnServersByVgwResponse.

        请求id

        :param request_id: The request_id of this ListVpnServersByVgwResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def header_response_token(self):
        r"""Gets the header_response_token of this ListVpnServersByVgwResponse.

        :return: The header_response_token of this ListVpnServersByVgwResponse.
        :rtype: str
        """
        return self._header_response_token

    @header_response_token.setter
    def header_response_token(self, header_response_token):
        r"""Sets the header_response_token of this ListVpnServersByVgwResponse.

        :param header_response_token: The header_response_token of this ListVpnServersByVgwResponse.
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
        if not isinstance(other, ListVpnServersByVgwResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
