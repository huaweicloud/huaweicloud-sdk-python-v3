# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGroupProtectedRefsUserGroupsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'int',
        'offset': 'int',
        'limit': 'int',
        'search': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'offset': 'offset',
        'limit': 'limit',
        'search': 'search'
    }

    def __init__(self, group_id=None, offset=None, limit=None, search=None):
        r"""ListGroupProtectedRefsUserGroupsRequest

        The model defined in huaweicloud sdk

        :param group_id: **参数解释：** 代码组id，代码组首页，Group ID后的数字Id
        :type group_id: int
        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        :param search: **参数解释：** 查询关键字，可模糊匹配用户名称、用户昵称、租户名称。
        :type search: str
        """
        
        

        self._group_id = None
        self._offset = None
        self._limit = None
        self._search = None
        self.discriminator = None

        self.group_id = group_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if search is not None:
            self.search = search

    @property
    def group_id(self):
        r"""Gets the group_id of this ListGroupProtectedRefsUserGroupsRequest.

        **参数解释：** 代码组id，代码组首页，Group ID后的数字Id

        :return: The group_id of this ListGroupProtectedRefsUserGroupsRequest.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListGroupProtectedRefsUserGroupsRequest.

        **参数解释：** 代码组id，代码组首页，Group ID后的数字Id

        :param group_id: The group_id of this ListGroupProtectedRefsUserGroupsRequest.
        :type group_id: int
        """
        self._group_id = group_id

    @property
    def offset(self):
        r"""Gets the offset of this ListGroupProtectedRefsUserGroupsRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListGroupProtectedRefsUserGroupsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListGroupProtectedRefsUserGroupsRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListGroupProtectedRefsUserGroupsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListGroupProtectedRefsUserGroupsRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListGroupProtectedRefsUserGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListGroupProtectedRefsUserGroupsRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListGroupProtectedRefsUserGroupsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def search(self):
        r"""Gets the search of this ListGroupProtectedRefsUserGroupsRequest.

        **参数解释：** 查询关键字，可模糊匹配用户名称、用户昵称、租户名称。

        :return: The search of this ListGroupProtectedRefsUserGroupsRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListGroupProtectedRefsUserGroupsRequest.

        **参数解释：** 查询关键字，可模糊匹配用户名称、用户昵称、租户名称。

        :param search: The search of this ListGroupProtectedRefsUserGroupsRequest.
        :type search: str
        """
        self._search = search

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListGroupProtectedRefsUserGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
