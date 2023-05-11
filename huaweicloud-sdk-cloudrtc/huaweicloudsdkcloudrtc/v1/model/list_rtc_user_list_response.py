# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRtcUserListResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'limit': 'int',
        'offset': 'int',
        'users': 'list[RtcUser]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'total': 'total',
        'limit': 'limit',
        'offset': 'offset',
        'users': 'users',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, total=None, limit=None, offset=None, users=None, x_request_id=None):
        """ListRtcUserListResponse

        The model defined in huaweicloud sdk

        :param total: 总数
        :type total: int
        :param limit: 查询结果限制
        :type limit: int
        :param offset: 查询偏移量
        :type offset: int
        :param users: 用户列表
        :type users: list[:class:`huaweicloudsdkcloudrtc.v1.RtcUser`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListRtcUserListResponse, self).__init__()

        self._total = None
        self._limit = None
        self._offset = None
        self._users = None
        self._x_request_id = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if users is not None:
            self.users = users
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def total(self):
        """Gets the total of this ListRtcUserListResponse.

        总数

        :return: The total of this ListRtcUserListResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListRtcUserListResponse.

        总数

        :param total: The total of this ListRtcUserListResponse.
        :type total: int
        """
        self._total = total

    @property
    def limit(self):
        """Gets the limit of this ListRtcUserListResponse.

        查询结果限制

        :return: The limit of this ListRtcUserListResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRtcUserListResponse.

        查询结果限制

        :param limit: The limit of this ListRtcUserListResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListRtcUserListResponse.

        查询偏移量

        :return: The offset of this ListRtcUserListResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListRtcUserListResponse.

        查询偏移量

        :param offset: The offset of this ListRtcUserListResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def users(self):
        """Gets the users of this ListRtcUserListResponse.

        用户列表

        :return: The users of this ListRtcUserListResponse.
        :rtype: list[:class:`huaweicloudsdkcloudrtc.v1.RtcUser`]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this ListRtcUserListResponse.

        用户列表

        :param users: The users of this ListRtcUserListResponse.
        :type users: list[:class:`huaweicloudsdkcloudrtc.v1.RtcUser`]
        """
        self._users = users

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListRtcUserListResponse.

        :return: The x_request_id of this ListRtcUserListResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListRtcUserListResponse.

        :param x_request_id: The x_request_id of this ListRtcUserListResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListRtcUserListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
