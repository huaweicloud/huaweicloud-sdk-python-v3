# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPersonalMergeRequestsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'state': 'str',
        'order_by': 'str',
        'sort': 'str',
        'labels': 'str',
        'created_before': 'datetime',
        'created_after': 'datetime',
        'updated_after': 'datetime',
        'updated_before': 'datetime',
        'view': 'str',
        'author_id': 'str',
        'scope': 'str',
        'source_branch': 'str',
        'target_branch': 'str',
        'search': 'str',
        'wip': 'str',
        'merged_by': 'str',
        'merged_after': 'datetime',
        'merged_before': 'datetime',
        'offset': 'int',
        'limit': 'int',
        'only_count': 'bool'
    }

    attribute_map = {
        'state': 'state',
        'order_by': 'order_by',
        'sort': 'sort',
        'labels': 'labels',
        'created_before': 'created_before',
        'created_after': 'created_after',
        'updated_after': 'updated_after',
        'updated_before': 'updated_before',
        'view': 'view',
        'author_id': 'author_id',
        'scope': 'scope',
        'source_branch': 'source_branch',
        'target_branch': 'target_branch',
        'search': 'search',
        'wip': 'wip',
        'merged_by': 'merged_by',
        'merged_after': 'merged_after',
        'merged_before': 'merged_before',
        'offset': 'offset',
        'limit': 'limit',
        'only_count': 'only_count'
    }

    def __init__(self, state=None, order_by=None, sort=None, labels=None, created_before=None, created_after=None, updated_after=None, updated_before=None, view=None, author_id=None, scope=None, source_branch=None, target_branch=None, search=None, wip=None, merged_by=None, merged_after=None, merged_before=None, offset=None, limit=None, only_count=None):
        r"""ListPersonalMergeRequestsRequest

        The model defined in huaweicloud sdk

        :param state: **参数解释：** 合并请求状态 **约束限制：** - all，返回所有状态的合并请求。 - opened，返回开启中的合并请求。 - closed，返回关闭的合并请求。 - locked，返回锁定的合并请求。 - merged，返回已合并的合并请求。
        :type state: str
        :param order_by: **参数解释：** 排序方式 **约束限制：** - created_at，根据创建时间排序。 - updated_at，根据更新时间排序。 - merged_at，根据合并时间排序。
        :type order_by: str
        :param sort: **参数解释：** 排序顺序 **约束限制：**   - asc，正序排序。   - desc，倒序排序。
        :type sort: str
        :param labels: **参数解释：** 合并请求关联标签
        :type labels: str
        :param created_before: **参数解释：** 指定时间前创建
        :type created_before: datetime
        :param created_after: **参数解释：** 指定时间后创建
        :type created_after: datetime
        :param updated_after: **参数解释：** 指定时间后更新
        :type updated_after: datetime
        :param updated_before: **参数解释：** 指定时间前更新
        :type updated_before: datetime
        :param view: **参数解释：** 结果集属性，根据给定的参数返回不同的结果， simple，返回简单数据，basic返回基本数据。
        :type view: str
        :param author_id: **参数解释：** 合并请求创建人
        :type author_id: str
        :param scope: **参数解释：**   - created_by_me 我创建的合并请求   - assigned_to_me 待我合并的合并请求   - need_my_review 待我检视的合并请求   - need_my_approve 待我审核的合并请求   - all 所有有权限访问的合并请求
        :type scope: str
        :param source_branch: **参数解释：** 合并请求原分支
        :type source_branch: str
        :param target_branch: **参数解释：** 合并请求目标分支
        :type target_branch: str
        :param search: **参数解释：** 根据合并请求标题、描述信息过滤关键字
        :type search: str
        :param wip: **参数解释：** 合并请求标题是否有WIP关键字
        :type wip: str
        :param merged_by: **参数解释：** 合并请求合并人
        :type merged_by: str
        :param merged_after: **参数解释：** 指定时间后合入
        :type merged_after: datetime
        :param merged_before: **参数解释：** 指定时间前合入
        :type merged_before: datetime
        :param offset: **参数解释：** 分页参数偏移量
        :type offset: int
        :param limit: **参数解释：** 分页参数结果数量限制
        :type limit: int
        :param only_count: **参数解释：** 是否只返回合并请求总数
        :type only_count: bool
        """
        
        

        self._state = None
        self._order_by = None
        self._sort = None
        self._labels = None
        self._created_before = None
        self._created_after = None
        self._updated_after = None
        self._updated_before = None
        self._view = None
        self._author_id = None
        self._scope = None
        self._source_branch = None
        self._target_branch = None
        self._search = None
        self._wip = None
        self._merged_by = None
        self._merged_after = None
        self._merged_before = None
        self._offset = None
        self._limit = None
        self._only_count = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if order_by is not None:
            self.order_by = order_by
        if sort is not None:
            self.sort = sort
        if labels is not None:
            self.labels = labels
        if created_before is not None:
            self.created_before = created_before
        if created_after is not None:
            self.created_after = created_after
        if updated_after is not None:
            self.updated_after = updated_after
        if updated_before is not None:
            self.updated_before = updated_before
        if view is not None:
            self.view = view
        if author_id is not None:
            self.author_id = author_id
        if scope is not None:
            self.scope = scope
        if source_branch is not None:
            self.source_branch = source_branch
        if target_branch is not None:
            self.target_branch = target_branch
        if search is not None:
            self.search = search
        if wip is not None:
            self.wip = wip
        if merged_by is not None:
            self.merged_by = merged_by
        if merged_after is not None:
            self.merged_after = merged_after
        if merged_before is not None:
            self.merged_before = merged_before
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if only_count is not None:
            self.only_count = only_count

    @property
    def state(self):
        r"""Gets the state of this ListPersonalMergeRequestsRequest.

        **参数解释：** 合并请求状态 **约束限制：** - all，返回所有状态的合并请求。 - opened，返回开启中的合并请求。 - closed，返回关闭的合并请求。 - locked，返回锁定的合并请求。 - merged，返回已合并的合并请求。

        :return: The state of this ListPersonalMergeRequestsRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListPersonalMergeRequestsRequest.

        **参数解释：** 合并请求状态 **约束限制：** - all，返回所有状态的合并请求。 - opened，返回开启中的合并请求。 - closed，返回关闭的合并请求。 - locked，返回锁定的合并请求。 - merged，返回已合并的合并请求。

        :param state: The state of this ListPersonalMergeRequestsRequest.
        :type state: str
        """
        self._state = state

    @property
    def order_by(self):
        r"""Gets the order_by of this ListPersonalMergeRequestsRequest.

        **参数解释：** 排序方式 **约束限制：** - created_at，根据创建时间排序。 - updated_at，根据更新时间排序。 - merged_at，根据合并时间排序。

        :return: The order_by of this ListPersonalMergeRequestsRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListPersonalMergeRequestsRequest.

        **参数解释：** 排序方式 **约束限制：** - created_at，根据创建时间排序。 - updated_at，根据更新时间排序。 - merged_at，根据合并时间排序。

        :param order_by: The order_by of this ListPersonalMergeRequestsRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def sort(self):
        r"""Gets the sort of this ListPersonalMergeRequestsRequest.

        **参数解释：** 排序顺序 **约束限制：**   - asc，正序排序。   - desc，倒序排序。

        :return: The sort of this ListPersonalMergeRequestsRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ListPersonalMergeRequestsRequest.

        **参数解释：** 排序顺序 **约束限制：**   - asc，正序排序。   - desc，倒序排序。

        :param sort: The sort of this ListPersonalMergeRequestsRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def labels(self):
        r"""Gets the labels of this ListPersonalMergeRequestsRequest.

        **参数解释：** 合并请求关联标签

        :return: The labels of this ListPersonalMergeRequestsRequest.
        :rtype: str
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ListPersonalMergeRequestsRequest.

        **参数解释：** 合并请求关联标签

        :param labels: The labels of this ListPersonalMergeRequestsRequest.
        :type labels: str
        """
        self._labels = labels

    @property
    def created_before(self):
        r"""Gets the created_before of this ListPersonalMergeRequestsRequest.

        **参数解释：** 指定时间前创建

        :return: The created_before of this ListPersonalMergeRequestsRequest.
        :rtype: datetime
        """
        return self._created_before

    @created_before.setter
    def created_before(self, created_before):
        r"""Sets the created_before of this ListPersonalMergeRequestsRequest.

        **参数解释：** 指定时间前创建

        :param created_before: The created_before of this ListPersonalMergeRequestsRequest.
        :type created_before: datetime
        """
        self._created_before = created_before

    @property
    def created_after(self):
        r"""Gets the created_after of this ListPersonalMergeRequestsRequest.

        **参数解释：** 指定时间后创建

        :return: The created_after of this ListPersonalMergeRequestsRequest.
        :rtype: datetime
        """
        return self._created_after

    @created_after.setter
    def created_after(self, created_after):
        r"""Sets the created_after of this ListPersonalMergeRequestsRequest.

        **参数解释：** 指定时间后创建

        :param created_after: The created_after of this ListPersonalMergeRequestsRequest.
        :type created_after: datetime
        """
        self._created_after = created_after

    @property
    def updated_after(self):
        r"""Gets the updated_after of this ListPersonalMergeRequestsRequest.

        **参数解释：** 指定时间后更新

        :return: The updated_after of this ListPersonalMergeRequestsRequest.
        :rtype: datetime
        """
        return self._updated_after

    @updated_after.setter
    def updated_after(self, updated_after):
        r"""Sets the updated_after of this ListPersonalMergeRequestsRequest.

        **参数解释：** 指定时间后更新

        :param updated_after: The updated_after of this ListPersonalMergeRequestsRequest.
        :type updated_after: datetime
        """
        self._updated_after = updated_after

    @property
    def updated_before(self):
        r"""Gets the updated_before of this ListPersonalMergeRequestsRequest.

        **参数解释：** 指定时间前更新

        :return: The updated_before of this ListPersonalMergeRequestsRequest.
        :rtype: datetime
        """
        return self._updated_before

    @updated_before.setter
    def updated_before(self, updated_before):
        r"""Sets the updated_before of this ListPersonalMergeRequestsRequest.

        **参数解释：** 指定时间前更新

        :param updated_before: The updated_before of this ListPersonalMergeRequestsRequest.
        :type updated_before: datetime
        """
        self._updated_before = updated_before

    @property
    def view(self):
        r"""Gets the view of this ListPersonalMergeRequestsRequest.

        **参数解释：** 结果集属性，根据给定的参数返回不同的结果， simple，返回简单数据，basic返回基本数据。

        :return: The view of this ListPersonalMergeRequestsRequest.
        :rtype: str
        """
        return self._view

    @view.setter
    def view(self, view):
        r"""Sets the view of this ListPersonalMergeRequestsRequest.

        **参数解释：** 结果集属性，根据给定的参数返回不同的结果， simple，返回简单数据，basic返回基本数据。

        :param view: The view of this ListPersonalMergeRequestsRequest.
        :type view: str
        """
        self._view = view

    @property
    def author_id(self):
        r"""Gets the author_id of this ListPersonalMergeRequestsRequest.

        **参数解释：** 合并请求创建人

        :return: The author_id of this ListPersonalMergeRequestsRequest.
        :rtype: str
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        r"""Sets the author_id of this ListPersonalMergeRequestsRequest.

        **参数解释：** 合并请求创建人

        :param author_id: The author_id of this ListPersonalMergeRequestsRequest.
        :type author_id: str
        """
        self._author_id = author_id

    @property
    def scope(self):
        r"""Gets the scope of this ListPersonalMergeRequestsRequest.

        **参数解释：**   - created_by_me 我创建的合并请求   - assigned_to_me 待我合并的合并请求   - need_my_review 待我检视的合并请求   - need_my_approve 待我审核的合并请求   - all 所有有权限访问的合并请求

        :return: The scope of this ListPersonalMergeRequestsRequest.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this ListPersonalMergeRequestsRequest.

        **参数解释：**   - created_by_me 我创建的合并请求   - assigned_to_me 待我合并的合并请求   - need_my_review 待我检视的合并请求   - need_my_approve 待我审核的合并请求   - all 所有有权限访问的合并请求

        :param scope: The scope of this ListPersonalMergeRequestsRequest.
        :type scope: str
        """
        self._scope = scope

    @property
    def source_branch(self):
        r"""Gets the source_branch of this ListPersonalMergeRequestsRequest.

        **参数解释：** 合并请求原分支

        :return: The source_branch of this ListPersonalMergeRequestsRequest.
        :rtype: str
        """
        return self._source_branch

    @source_branch.setter
    def source_branch(self, source_branch):
        r"""Sets the source_branch of this ListPersonalMergeRequestsRequest.

        **参数解释：** 合并请求原分支

        :param source_branch: The source_branch of this ListPersonalMergeRequestsRequest.
        :type source_branch: str
        """
        self._source_branch = source_branch

    @property
    def target_branch(self):
        r"""Gets the target_branch of this ListPersonalMergeRequestsRequest.

        **参数解释：** 合并请求目标分支

        :return: The target_branch of this ListPersonalMergeRequestsRequest.
        :rtype: str
        """
        return self._target_branch

    @target_branch.setter
    def target_branch(self, target_branch):
        r"""Sets the target_branch of this ListPersonalMergeRequestsRequest.

        **参数解释：** 合并请求目标分支

        :param target_branch: The target_branch of this ListPersonalMergeRequestsRequest.
        :type target_branch: str
        """
        self._target_branch = target_branch

    @property
    def search(self):
        r"""Gets the search of this ListPersonalMergeRequestsRequest.

        **参数解释：** 根据合并请求标题、描述信息过滤关键字

        :return: The search of this ListPersonalMergeRequestsRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListPersonalMergeRequestsRequest.

        **参数解释：** 根据合并请求标题、描述信息过滤关键字

        :param search: The search of this ListPersonalMergeRequestsRequest.
        :type search: str
        """
        self._search = search

    @property
    def wip(self):
        r"""Gets the wip of this ListPersonalMergeRequestsRequest.

        **参数解释：** 合并请求标题是否有WIP关键字

        :return: The wip of this ListPersonalMergeRequestsRequest.
        :rtype: str
        """
        return self._wip

    @wip.setter
    def wip(self, wip):
        r"""Sets the wip of this ListPersonalMergeRequestsRequest.

        **参数解释：** 合并请求标题是否有WIP关键字

        :param wip: The wip of this ListPersonalMergeRequestsRequest.
        :type wip: str
        """
        self._wip = wip

    @property
    def merged_by(self):
        r"""Gets the merged_by of this ListPersonalMergeRequestsRequest.

        **参数解释：** 合并请求合并人

        :return: The merged_by of this ListPersonalMergeRequestsRequest.
        :rtype: str
        """
        return self._merged_by

    @merged_by.setter
    def merged_by(self, merged_by):
        r"""Sets the merged_by of this ListPersonalMergeRequestsRequest.

        **参数解释：** 合并请求合并人

        :param merged_by: The merged_by of this ListPersonalMergeRequestsRequest.
        :type merged_by: str
        """
        self._merged_by = merged_by

    @property
    def merged_after(self):
        r"""Gets the merged_after of this ListPersonalMergeRequestsRequest.

        **参数解释：** 指定时间后合入

        :return: The merged_after of this ListPersonalMergeRequestsRequest.
        :rtype: datetime
        """
        return self._merged_after

    @merged_after.setter
    def merged_after(self, merged_after):
        r"""Sets the merged_after of this ListPersonalMergeRequestsRequest.

        **参数解释：** 指定时间后合入

        :param merged_after: The merged_after of this ListPersonalMergeRequestsRequest.
        :type merged_after: datetime
        """
        self._merged_after = merged_after

    @property
    def merged_before(self):
        r"""Gets the merged_before of this ListPersonalMergeRequestsRequest.

        **参数解释：** 指定时间前合入

        :return: The merged_before of this ListPersonalMergeRequestsRequest.
        :rtype: datetime
        """
        return self._merged_before

    @merged_before.setter
    def merged_before(self, merged_before):
        r"""Sets the merged_before of this ListPersonalMergeRequestsRequest.

        **参数解释：** 指定时间前合入

        :param merged_before: The merged_before of this ListPersonalMergeRequestsRequest.
        :type merged_before: datetime
        """
        self._merged_before = merged_before

    @property
    def offset(self):
        r"""Gets the offset of this ListPersonalMergeRequestsRequest.

        **参数解释：** 分页参数偏移量

        :return: The offset of this ListPersonalMergeRequestsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPersonalMergeRequestsRequest.

        **参数解释：** 分页参数偏移量

        :param offset: The offset of this ListPersonalMergeRequestsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListPersonalMergeRequestsRequest.

        **参数解释：** 分页参数结果数量限制

        :return: The limit of this ListPersonalMergeRequestsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPersonalMergeRequestsRequest.

        **参数解释：** 分页参数结果数量限制

        :param limit: The limit of this ListPersonalMergeRequestsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def only_count(self):
        r"""Gets the only_count of this ListPersonalMergeRequestsRequest.

        **参数解释：** 是否只返回合并请求总数

        :return: The only_count of this ListPersonalMergeRequestsRequest.
        :rtype: bool
        """
        return self._only_count

    @only_count.setter
    def only_count(self, only_count):
        r"""Sets the only_count of this ListPersonalMergeRequestsRequest.

        **参数解释：** 是否只返回合并请求总数

        :param only_count: The only_count of this ListPersonalMergeRequestsRequest.
        :type only_count: bool
        """
        self._only_count = only_count

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
        if not isinstance(other, ListPersonalMergeRequestsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
