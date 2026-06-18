# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGroupProtectedBranchesRequest:

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
        'search': 'str',
        'user_actions': 'bool'
    }

    attribute_map = {
        'group_id': 'group_id',
        'offset': 'offset',
        'limit': 'limit',
        'search': 'search',
        'user_actions': 'user_actions'
    }

    def __init__(self, group_id=None, offset=None, limit=None, search=None, user_actions=None):
        r"""ListGroupProtectedBranchesRequest

        The model defined in huaweicloud sdk

        :param group_id: **参数解释：** 代码组id，代码组首页，Group ID后的数字Id **默认取值：** 不涉及。
        :type group_id: int
        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        :param search: **参数解释：** 检索内容 **约束限制：** 保护分支名称 **取值范围：** 保护分支名称 **默认取值：** 不涉及
        :type search: str
        :param user_actions: **参数解释：** 是否返回带有user_action结构的数据，user_action结构的数据为最新的结构，推荐传参为true **约束限制：** true,false **取值范围：** true,false **默认取值：** 默认不传参
        :type user_actions: bool
        """
        
        

        self._group_id = None
        self._offset = None
        self._limit = None
        self._search = None
        self._user_actions = None
        self.discriminator = None

        self.group_id = group_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if search is not None:
            self.search = search
        self.user_actions = user_actions

    @property
    def group_id(self):
        r"""Gets the group_id of this ListGroupProtectedBranchesRequest.

        **参数解释：** 代码组id，代码组首页，Group ID后的数字Id **默认取值：** 不涉及。

        :return: The group_id of this ListGroupProtectedBranchesRequest.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListGroupProtectedBranchesRequest.

        **参数解释：** 代码组id，代码组首页，Group ID后的数字Id **默认取值：** 不涉及。

        :param group_id: The group_id of this ListGroupProtectedBranchesRequest.
        :type group_id: int
        """
        self._group_id = group_id

    @property
    def offset(self):
        r"""Gets the offset of this ListGroupProtectedBranchesRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListGroupProtectedBranchesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListGroupProtectedBranchesRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListGroupProtectedBranchesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListGroupProtectedBranchesRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListGroupProtectedBranchesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListGroupProtectedBranchesRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListGroupProtectedBranchesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def search(self):
        r"""Gets the search of this ListGroupProtectedBranchesRequest.

        **参数解释：** 检索内容 **约束限制：** 保护分支名称 **取值范围：** 保护分支名称 **默认取值：** 不涉及

        :return: The search of this ListGroupProtectedBranchesRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListGroupProtectedBranchesRequest.

        **参数解释：** 检索内容 **约束限制：** 保护分支名称 **取值范围：** 保护分支名称 **默认取值：** 不涉及

        :param search: The search of this ListGroupProtectedBranchesRequest.
        :type search: str
        """
        self._search = search

    @property
    def user_actions(self):
        r"""Gets the user_actions of this ListGroupProtectedBranchesRequest.

        **参数解释：** 是否返回带有user_action结构的数据，user_action结构的数据为最新的结构，推荐传参为true **约束限制：** true,false **取值范围：** true,false **默认取值：** 默认不传参

        :return: The user_actions of this ListGroupProtectedBranchesRequest.
        :rtype: bool
        """
        return self._user_actions

    @user_actions.setter
    def user_actions(self, user_actions):
        r"""Sets the user_actions of this ListGroupProtectedBranchesRequest.

        **参数解释：** 是否返回带有user_action结构的数据，user_action结构的数据为最新的结构，推荐传参为true **约束限制：** true,false **取值范围：** true,false **默认取值：** 默认不传参

        :param user_actions: The user_actions of this ListGroupProtectedBranchesRequest.
        :type user_actions: bool
        """
        self._user_actions = user_actions

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
        if not isinstance(other, ListGroupProtectedBranchesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
