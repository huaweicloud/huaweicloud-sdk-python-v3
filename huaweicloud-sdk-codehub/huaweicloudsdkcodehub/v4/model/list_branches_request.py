# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBranchesRequest:

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
        'branch_type': 'str',
        'creator': 'str',
        'sort': 'str',
        'query_view': 'str',
        'view': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'branch_type': 'branch_type',
        'creator': 'creator',
        'sort': 'sort',
        'query_view': 'query_view',
        'view': 'view',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, repository_id=None, branch_type=None, creator=None, sort=None, query_view=None, view=None, offset=None, limit=None):
        r"""ListBranchesRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param branch_type: **参数解释：** 分支类型，默认返回全部分支，not_protect，返回非保护分支。 **约束限制：** 不涉及。 **取值范围：** 不涉及。
        :type branch_type: str
        :param creator: **参数解释：** 创建者，用户ID或者IamId。 **取值范围：** 字符串长度不少于1，不超过100000。
        :type creator: str
        :param sort: **参数解释：** 排序方式 **约束限制：** - name，分支名倒序。 - updated_desc，更新时间倒序。 - updated_asc，更新时间正序。
        :type sort: str
        :param query_view: **参数解释：** 分支类型 **约束限制：** - my_branches，个人分支。 - active，活跃分支。 - stale，过时分支。 - all_branches，所有分支。
        :type query_view: str
        :param view: **参数解释：** 结果集属性，根据给定的参数返回不同的结果 **约束限制：** - all，返回分支的所有信息。 - basic，返回分支的基本信息。 - simple，返回分支的简单信息。
        :type view: str
        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        """
        
        

        self._repository_id = None
        self._branch_type = None
        self._creator = None
        self._sort = None
        self._query_view = None
        self._view = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.repository_id = repository_id
        if branch_type is not None:
            self.branch_type = branch_type
        if creator is not None:
            self.creator = creator
        if sort is not None:
            self.sort = sort
        if query_view is not None:
            self.query_view = query_view
        if view is not None:
            self.view = view
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ListBranchesRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this ListBranchesRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ListBranchesRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this ListBranchesRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def branch_type(self):
        r"""Gets the branch_type of this ListBranchesRequest.

        **参数解释：** 分支类型，默认返回全部分支，not_protect，返回非保护分支。 **约束限制：** 不涉及。 **取值范围：** 不涉及。

        :return: The branch_type of this ListBranchesRequest.
        :rtype: str
        """
        return self._branch_type

    @branch_type.setter
    def branch_type(self, branch_type):
        r"""Sets the branch_type of this ListBranchesRequest.

        **参数解释：** 分支类型，默认返回全部分支，not_protect，返回非保护分支。 **约束限制：** 不涉及。 **取值范围：** 不涉及。

        :param branch_type: The branch_type of this ListBranchesRequest.
        :type branch_type: str
        """
        self._branch_type = branch_type

    @property
    def creator(self):
        r"""Gets the creator of this ListBranchesRequest.

        **参数解释：** 创建者，用户ID或者IamId。 **取值范围：** 字符串长度不少于1，不超过100000。

        :return: The creator of this ListBranchesRequest.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ListBranchesRequest.

        **参数解释：** 创建者，用户ID或者IamId。 **取值范围：** 字符串长度不少于1，不超过100000。

        :param creator: The creator of this ListBranchesRequest.
        :type creator: str
        """
        self._creator = creator

    @property
    def sort(self):
        r"""Gets the sort of this ListBranchesRequest.

        **参数解释：** 排序方式 **约束限制：** - name，分支名倒序。 - updated_desc，更新时间倒序。 - updated_asc，更新时间正序。

        :return: The sort of this ListBranchesRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ListBranchesRequest.

        **参数解释：** 排序方式 **约束限制：** - name，分支名倒序。 - updated_desc，更新时间倒序。 - updated_asc，更新时间正序。

        :param sort: The sort of this ListBranchesRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def query_view(self):
        r"""Gets the query_view of this ListBranchesRequest.

        **参数解释：** 分支类型 **约束限制：** - my_branches，个人分支。 - active，活跃分支。 - stale，过时分支。 - all_branches，所有分支。

        :return: The query_view of this ListBranchesRequest.
        :rtype: str
        """
        return self._query_view

    @query_view.setter
    def query_view(self, query_view):
        r"""Sets the query_view of this ListBranchesRequest.

        **参数解释：** 分支类型 **约束限制：** - my_branches，个人分支。 - active，活跃分支。 - stale，过时分支。 - all_branches，所有分支。

        :param query_view: The query_view of this ListBranchesRequest.
        :type query_view: str
        """
        self._query_view = query_view

    @property
    def view(self):
        r"""Gets the view of this ListBranchesRequest.

        **参数解释：** 结果集属性，根据给定的参数返回不同的结果 **约束限制：** - all，返回分支的所有信息。 - basic，返回分支的基本信息。 - simple，返回分支的简单信息。

        :return: The view of this ListBranchesRequest.
        :rtype: str
        """
        return self._view

    @view.setter
    def view(self, view):
        r"""Sets the view of this ListBranchesRequest.

        **参数解释：** 结果集属性，根据给定的参数返回不同的结果 **约束限制：** - all，返回分支的所有信息。 - basic，返回分支的基本信息。 - simple，返回分支的简单信息。

        :param view: The view of this ListBranchesRequest.
        :type view: str
        """
        self._view = view

    @property
    def offset(self):
        r"""Gets the offset of this ListBranchesRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListBranchesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListBranchesRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListBranchesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListBranchesRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListBranchesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListBranchesRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListBranchesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListBranchesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
