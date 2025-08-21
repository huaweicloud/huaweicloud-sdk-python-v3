# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMembersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_id': 'int',
        'search': 'str',
        'offset': 'int',
        'limit': 'int',
        'permission': 'str',
        'action': 'str'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'search': 'search',
        'offset': 'offset',
        'limit': 'limit',
        'permission': 'permission',
        'action': 'action'
    }

    def __init__(self, repository_id=None, search=None, offset=None, limit=None, permission=None, action=None):
        r"""ListMembersRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param search: **参数解释：** 查询关键字，可模糊匹配用户名称、用户昵称、租户名称。
        :type search: str
        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        :param permission: **参数解释：** 权限点。 **约束限制：** - repository，仓库。 - code，代码。 - member，成员。 - branch，分支。 - tag，Tag。 - mr，MR。 - label，标签。
        :type permission: str
        :param action: **参数解释：** 权限动作点, 不同权限点有不同的动作。 **约束限制：** - repository：create,fork,delete,setting - code：push,download - member：create,update,delete - branch：create,delete - tag：create,delete - mr：create,update,comment,review,approve,merge,close,reopen - label：create,delete,update
        :type action: str
        """
        
        

        self._repository_id = None
        self._search = None
        self._offset = None
        self._limit = None
        self._permission = None
        self._action = None
        self.discriminator = None

        self.repository_id = repository_id
        if search is not None:
            self.search = search
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if permission is not None:
            self.permission = permission
        if action is not None:
            self.action = action

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ListMembersRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this ListMembersRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ListMembersRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this ListMembersRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def search(self):
        r"""Gets the search of this ListMembersRequest.

        **参数解释：** 查询关键字，可模糊匹配用户名称、用户昵称、租户名称。

        :return: The search of this ListMembersRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListMembersRequest.

        **参数解释：** 查询关键字，可模糊匹配用户名称、用户昵称、租户名称。

        :param search: The search of this ListMembersRequest.
        :type search: str
        """
        self._search = search

    @property
    def offset(self):
        r"""Gets the offset of this ListMembersRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListMembersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListMembersRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListMembersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListMembersRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListMembersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListMembersRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListMembersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def permission(self):
        r"""Gets the permission of this ListMembersRequest.

        **参数解释：** 权限点。 **约束限制：** - repository，仓库。 - code，代码。 - member，成员。 - branch，分支。 - tag，Tag。 - mr，MR。 - label，标签。

        :return: The permission of this ListMembersRequest.
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        r"""Sets the permission of this ListMembersRequest.

        **参数解释：** 权限点。 **约束限制：** - repository，仓库。 - code，代码。 - member，成员。 - branch，分支。 - tag，Tag。 - mr，MR。 - label，标签。

        :param permission: The permission of this ListMembersRequest.
        :type permission: str
        """
        self._permission = permission

    @property
    def action(self):
        r"""Gets the action of this ListMembersRequest.

        **参数解释：** 权限动作点, 不同权限点有不同的动作。 **约束限制：** - repository：create,fork,delete,setting - code：push,download - member：create,update,delete - branch：create,delete - tag：create,delete - mr：create,update,comment,review,approve,merge,close,reopen - label：create,delete,update

        :return: The action of this ListMembersRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ListMembersRequest.

        **参数解释：** 权限动作点, 不同权限点有不同的动作。 **约束限制：** - repository：create,fork,delete,setting - code：push,download - member：create,update,delete - branch：create,delete - tag：create,delete - mr：create,update,comment,review,approve,merge,close,reopen - label：create,delete,update

        :param action: The action of this ListMembersRequest.
        :type action: str
        """
        self._action = action

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
        if not isinstance(other, ListMembersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
