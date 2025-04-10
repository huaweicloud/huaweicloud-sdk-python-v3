# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVpnUsersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'users': 'list[VpnUser]',
        'total_count': 'int',
        'page_info': 'PageInfo',
        'request_id': 'str'
    }

    attribute_map = {
        'users': 'users',
        'total_count': 'total_count',
        'page_info': 'page_info',
        'request_id': 'request_id'
    }

    def __init__(self, users=None, total_count=None, page_info=None, request_id=None):
        r"""ListVpnUsersResponse

        The model defined in huaweicloud sdk

        :param users: 用户列表信息
        :type users: list[:class:`huaweicloudsdkvpn.v5.VpnUser`]
        :param total_count: 总数
        :type total_count: int
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkvpn.v5.PageInfo`
        :param request_id: 请求ID
        :type request_id: str
        """
        
        super(ListVpnUsersResponse, self).__init__()

        self._users = None
        self._total_count = None
        self._page_info = None
        self._request_id = None
        self.discriminator = None

        if users is not None:
            self.users = users
        if total_count is not None:
            self.total_count = total_count
        if page_info is not None:
            self.page_info = page_info
        if request_id is not None:
            self.request_id = request_id

    @property
    def users(self):
        r"""Gets the users of this ListVpnUsersResponse.

        用户列表信息

        :return: The users of this ListVpnUsersResponse.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.VpnUser`]
        """
        return self._users

    @users.setter
    def users(self, users):
        r"""Sets the users of this ListVpnUsersResponse.

        用户列表信息

        :param users: The users of this ListVpnUsersResponse.
        :type users: list[:class:`huaweicloudsdkvpn.v5.VpnUser`]
        """
        self._users = users

    @property
    def total_count(self):
        r"""Gets the total_count of this ListVpnUsersResponse.

        总数

        :return: The total_count of this ListVpnUsersResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListVpnUsersResponse.

        总数

        :param total_count: The total_count of this ListVpnUsersResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def page_info(self):
        r"""Gets the page_info of this ListVpnUsersResponse.

        :return: The page_info of this ListVpnUsersResponse.
        :rtype: :class:`huaweicloudsdkvpn.v5.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListVpnUsersResponse.

        :param page_info: The page_info of this ListVpnUsersResponse.
        :type page_info: :class:`huaweicloudsdkvpn.v5.PageInfo`
        """
        self._page_info = page_info

    @property
    def request_id(self):
        r"""Gets the request_id of this ListVpnUsersResponse.

        请求ID

        :return: The request_id of this ListVpnUsersResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListVpnUsersResponse.

        请求ID

        :param request_id: The request_id of this ListVpnUsersResponse.
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
        if not isinstance(other, ListVpnUsersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
