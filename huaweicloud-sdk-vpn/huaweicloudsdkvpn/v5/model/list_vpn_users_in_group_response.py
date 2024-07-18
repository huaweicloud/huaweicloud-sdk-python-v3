# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVpnUsersInGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'users': 'list[VpnUserInGroup]',
        'total_count': 'int',
        'page_info': 'PageInfo',
        'request_id': 'str',
        'header_response_token': 'str'
    }

    attribute_map = {
        'users': 'users',
        'total_count': 'total_count',
        'page_info': 'page_info',
        'request_id': 'request_id',
        'header_response_token': 'header-response-token'
    }

    def __init__(self, users=None, total_count=None, page_info=None, request_id=None, header_response_token=None):
        """ListVpnUsersInGroupResponse

        The model defined in huaweicloud sdk

        :param users: 用户列表信息
        :type users: list[:class:`huaweicloudsdkvpn.v5.VpnUserInGroup`]
        :param total_count: 总数
        :type total_count: int
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkvpn.v5.PageInfo`
        :param request_id: 请求ID
        :type request_id: str
        :param header_response_token: 
        :type header_response_token: str
        """
        
        super(ListVpnUsersInGroupResponse, self).__init__()

        self._users = None
        self._total_count = None
        self._page_info = None
        self._request_id = None
        self._header_response_token = None
        self.discriminator = None

        if users is not None:
            self.users = users
        if total_count is not None:
            self.total_count = total_count
        if page_info is not None:
            self.page_info = page_info
        if request_id is not None:
            self.request_id = request_id
        if header_response_token is not None:
            self.header_response_token = header_response_token

    @property
    def users(self):
        """Gets the users of this ListVpnUsersInGroupResponse.

        用户列表信息

        :return: The users of this ListVpnUsersInGroupResponse.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.VpnUserInGroup`]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this ListVpnUsersInGroupResponse.

        用户列表信息

        :param users: The users of this ListVpnUsersInGroupResponse.
        :type users: list[:class:`huaweicloudsdkvpn.v5.VpnUserInGroup`]
        """
        self._users = users

    @property
    def total_count(self):
        """Gets the total_count of this ListVpnUsersInGroupResponse.

        总数

        :return: The total_count of this ListVpnUsersInGroupResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListVpnUsersInGroupResponse.

        总数

        :param total_count: The total_count of this ListVpnUsersInGroupResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def page_info(self):
        """Gets the page_info of this ListVpnUsersInGroupResponse.

        :return: The page_info of this ListVpnUsersInGroupResponse.
        :rtype: :class:`huaweicloudsdkvpn.v5.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListVpnUsersInGroupResponse.

        :param page_info: The page_info of this ListVpnUsersInGroupResponse.
        :type page_info: :class:`huaweicloudsdkvpn.v5.PageInfo`
        """
        self._page_info = page_info

    @property
    def request_id(self):
        """Gets the request_id of this ListVpnUsersInGroupResponse.

        请求ID

        :return: The request_id of this ListVpnUsersInGroupResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListVpnUsersInGroupResponse.

        请求ID

        :param request_id: The request_id of this ListVpnUsersInGroupResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def header_response_token(self):
        """Gets the header_response_token of this ListVpnUsersInGroupResponse.

        :return: The header_response_token of this ListVpnUsersInGroupResponse.
        :rtype: str
        """
        return self._header_response_token

    @header_response_token.setter
    def header_response_token(self, header_response_token):
        """Sets the header_response_token of this ListVpnUsersInGroupResponse.

        :param header_response_token: The header_response_token of this ListVpnUsersInGroupResponse.
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
        if not isinstance(other, ListVpnUsersInGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
