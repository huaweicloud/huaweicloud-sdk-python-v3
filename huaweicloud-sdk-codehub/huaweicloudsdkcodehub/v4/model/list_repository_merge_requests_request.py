# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRepositoryMergeRequestsRequest:

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
        'offset': 'int',
        'limit': 'int',
        'state': 'str',
        'order_by': 'str',
        'sort': 'str',
        'author_id': 'str',
        'source_branch': 'str',
        'target_branch': 'str',
        'search': 'str',
        'source_repository_id': 'int',
        'only_count': 'bool',
        'labels': 'str'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'offset': 'offset',
        'limit': 'limit',
        'state': 'state',
        'order_by': 'order_by',
        'sort': 'sort',
        'author_id': 'author_id',
        'source_branch': 'source_branch',
        'target_branch': 'target_branch',
        'search': 'search',
        'source_repository_id': 'source_repository_id',
        'only_count': 'only_count',
        'labels': 'labels'
    }

    def __init__(self, repository_id=None, offset=None, limit=None, state=None, order_by=None, sort=None, author_id=None, source_branch=None, target_branch=None, search=None, source_repository_id=None, only_count=None, labels=None):
        r"""ListRepositoryMergeRequestsRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        :param state: **参数解释：** 返回指定状态的合并请求。 **约束限制：** - all，表示所有状态。 - opened，表示开启中状态 - closed，表示已关闭状态 - merged，表示已合并状态
        :type state: str
        :param order_by: **参数解释：** 排序方式。 **取值范围：** - created_at，创建时间。 - updated_at，更新时间。
        :type order_by: str
        :param sort: **参数解释：** 排序方式。 **约束限制：** - asc，升序。 - desc，降序。
        :type sort: str
        :param author_id: **参数解释：** 返回由指定ID用户创建的合并请求。 多个ID以逗号&#39;,&#39;分隔，返回满足条件的合并请求并集。
        :type author_id: str
        :param source_branch: **参数解释：** 返回指定源分支的合并请求。
        :type source_branch: str
        :param target_branch: **参数解释：** 返回指定目标分支的合并请求。
        :type target_branch: str
        :param search: **参数解释：** 合并请求关键字搜索。 返回标题或者描述包含对应关键字的合并请求。
        :type search: str
        :param source_repository_id: **参数解释：** 查询指定源仓库的数据。
        :type source_repository_id: int
        :param only_count: **参数解释：** 是否仅返回合并请求计数。 **取值范围：** - true，仅返回合并请求计数。 - false，返回合并请求详细信息。
        :type only_count: bool
        :param labels: **参数解释：** 查询包含指定labels的合并请求。
        :type labels: str
        """
        
        

        self._repository_id = None
        self._offset = None
        self._limit = None
        self._state = None
        self._order_by = None
        self._sort = None
        self._author_id = None
        self._source_branch = None
        self._target_branch = None
        self._search = None
        self._source_repository_id = None
        self._only_count = None
        self._labels = None
        self.discriminator = None

        self.repository_id = repository_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if state is not None:
            self.state = state
        if order_by is not None:
            self.order_by = order_by
        if sort is not None:
            self.sort = sort
        if author_id is not None:
            self.author_id = author_id
        if source_branch is not None:
            self.source_branch = source_branch
        if target_branch is not None:
            self.target_branch = target_branch
        if search is not None:
            self.search = search
        if source_repository_id is not None:
            self.source_repository_id = source_repository_id
        if only_count is not None:
            self.only_count = only_count
        if labels is not None:
            self.labels = labels

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ListRepositoryMergeRequestsRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this ListRepositoryMergeRequestsRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ListRepositoryMergeRequestsRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this ListRepositoryMergeRequestsRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def offset(self):
        r"""Gets the offset of this ListRepositoryMergeRequestsRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListRepositoryMergeRequestsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListRepositoryMergeRequestsRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListRepositoryMergeRequestsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListRepositoryMergeRequestsRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListRepositoryMergeRequestsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRepositoryMergeRequestsRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListRepositoryMergeRequestsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def state(self):
        r"""Gets the state of this ListRepositoryMergeRequestsRequest.

        **参数解释：** 返回指定状态的合并请求。 **约束限制：** - all，表示所有状态。 - opened，表示开启中状态 - closed，表示已关闭状态 - merged，表示已合并状态

        :return: The state of this ListRepositoryMergeRequestsRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListRepositoryMergeRequestsRequest.

        **参数解释：** 返回指定状态的合并请求。 **约束限制：** - all，表示所有状态。 - opened，表示开启中状态 - closed，表示已关闭状态 - merged，表示已合并状态

        :param state: The state of this ListRepositoryMergeRequestsRequest.
        :type state: str
        """
        self._state = state

    @property
    def order_by(self):
        r"""Gets the order_by of this ListRepositoryMergeRequestsRequest.

        **参数解释：** 排序方式。 **取值范围：** - created_at，创建时间。 - updated_at，更新时间。

        :return: The order_by of this ListRepositoryMergeRequestsRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListRepositoryMergeRequestsRequest.

        **参数解释：** 排序方式。 **取值范围：** - created_at，创建时间。 - updated_at，更新时间。

        :param order_by: The order_by of this ListRepositoryMergeRequestsRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def sort(self):
        r"""Gets the sort of this ListRepositoryMergeRequestsRequest.

        **参数解释：** 排序方式。 **约束限制：** - asc，升序。 - desc，降序。

        :return: The sort of this ListRepositoryMergeRequestsRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ListRepositoryMergeRequestsRequest.

        **参数解释：** 排序方式。 **约束限制：** - asc，升序。 - desc，降序。

        :param sort: The sort of this ListRepositoryMergeRequestsRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def author_id(self):
        r"""Gets the author_id of this ListRepositoryMergeRequestsRequest.

        **参数解释：** 返回由指定ID用户创建的合并请求。 多个ID以逗号','分隔，返回满足条件的合并请求并集。

        :return: The author_id of this ListRepositoryMergeRequestsRequest.
        :rtype: str
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        r"""Sets the author_id of this ListRepositoryMergeRequestsRequest.

        **参数解释：** 返回由指定ID用户创建的合并请求。 多个ID以逗号','分隔，返回满足条件的合并请求并集。

        :param author_id: The author_id of this ListRepositoryMergeRequestsRequest.
        :type author_id: str
        """
        self._author_id = author_id

    @property
    def source_branch(self):
        r"""Gets the source_branch of this ListRepositoryMergeRequestsRequest.

        **参数解释：** 返回指定源分支的合并请求。

        :return: The source_branch of this ListRepositoryMergeRequestsRequest.
        :rtype: str
        """
        return self._source_branch

    @source_branch.setter
    def source_branch(self, source_branch):
        r"""Sets the source_branch of this ListRepositoryMergeRequestsRequest.

        **参数解释：** 返回指定源分支的合并请求。

        :param source_branch: The source_branch of this ListRepositoryMergeRequestsRequest.
        :type source_branch: str
        """
        self._source_branch = source_branch

    @property
    def target_branch(self):
        r"""Gets the target_branch of this ListRepositoryMergeRequestsRequest.

        **参数解释：** 返回指定目标分支的合并请求。

        :return: The target_branch of this ListRepositoryMergeRequestsRequest.
        :rtype: str
        """
        return self._target_branch

    @target_branch.setter
    def target_branch(self, target_branch):
        r"""Sets the target_branch of this ListRepositoryMergeRequestsRequest.

        **参数解释：** 返回指定目标分支的合并请求。

        :param target_branch: The target_branch of this ListRepositoryMergeRequestsRequest.
        :type target_branch: str
        """
        self._target_branch = target_branch

    @property
    def search(self):
        r"""Gets the search of this ListRepositoryMergeRequestsRequest.

        **参数解释：** 合并请求关键字搜索。 返回标题或者描述包含对应关键字的合并请求。

        :return: The search of this ListRepositoryMergeRequestsRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListRepositoryMergeRequestsRequest.

        **参数解释：** 合并请求关键字搜索。 返回标题或者描述包含对应关键字的合并请求。

        :param search: The search of this ListRepositoryMergeRequestsRequest.
        :type search: str
        """
        self._search = search

    @property
    def source_repository_id(self):
        r"""Gets the source_repository_id of this ListRepositoryMergeRequestsRequest.

        **参数解释：** 查询指定源仓库的数据。

        :return: The source_repository_id of this ListRepositoryMergeRequestsRequest.
        :rtype: int
        """
        return self._source_repository_id

    @source_repository_id.setter
    def source_repository_id(self, source_repository_id):
        r"""Sets the source_repository_id of this ListRepositoryMergeRequestsRequest.

        **参数解释：** 查询指定源仓库的数据。

        :param source_repository_id: The source_repository_id of this ListRepositoryMergeRequestsRequest.
        :type source_repository_id: int
        """
        self._source_repository_id = source_repository_id

    @property
    def only_count(self):
        r"""Gets the only_count of this ListRepositoryMergeRequestsRequest.

        **参数解释：** 是否仅返回合并请求计数。 **取值范围：** - true，仅返回合并请求计数。 - false，返回合并请求详细信息。

        :return: The only_count of this ListRepositoryMergeRequestsRequest.
        :rtype: bool
        """
        return self._only_count

    @only_count.setter
    def only_count(self, only_count):
        r"""Sets the only_count of this ListRepositoryMergeRequestsRequest.

        **参数解释：** 是否仅返回合并请求计数。 **取值范围：** - true，仅返回合并请求计数。 - false，返回合并请求详细信息。

        :param only_count: The only_count of this ListRepositoryMergeRequestsRequest.
        :type only_count: bool
        """
        self._only_count = only_count

    @property
    def labels(self):
        r"""Gets the labels of this ListRepositoryMergeRequestsRequest.

        **参数解释：** 查询包含指定labels的合并请求。

        :return: The labels of this ListRepositoryMergeRequestsRequest.
        :rtype: str
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ListRepositoryMergeRequestsRequest.

        **参数解释：** 查询包含指定labels的合并请求。

        :param labels: The labels of this ListRepositoryMergeRequestsRequest.
        :type labels: str
        """
        self._labels = labels

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
        if not isinstance(other, ListRepositoryMergeRequestsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
