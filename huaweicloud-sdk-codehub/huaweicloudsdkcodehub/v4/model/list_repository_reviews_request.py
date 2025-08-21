# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRepositoryReviewsRequest:

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
        'noteable_type': 'str',
        'search': 'str',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'only_count': 'bool',
        'review_categories': 'str',
        'review_modules': 'str',
        'severity': 'str',
        'assignee_id': 'int',
        'proposer_id': 'int',
        'target_branch': 'str',
        'include_reply': 'bool',
        'order_by': 'str',
        'sort': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'noteable_type': 'noteable_type',
        'search': 'search',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'only_count': 'only_count',
        'review_categories': 'review_categories',
        'review_modules': 'review_modules',
        'severity': 'severity',
        'assignee_id': 'assignee_id',
        'proposer_id': 'proposer_id',
        'target_branch': 'target_branch',
        'include_reply': 'include_reply',
        'order_by': 'order_by',
        'sort': 'sort',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, repository_id=None, noteable_type=None, search=None, start_date=None, end_date=None, only_count=None, review_categories=None, review_modules=None, severity=None, assignee_id=None, proposer_id=None, target_branch=None, include_reply=None, order_by=None, sort=None, offset=None, limit=None):
        r"""ListRepositoryReviewsRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param noteable_type: **参数解释：** 意见类型。 **取值范围：** - Commit，提交。 - MergeRequest，合并请求。  
        :type noteable_type: str
        :param search: **参数解释：** 查询评论内容。
        :type search: str
        :param start_date: **参数解释：** 开始日期。
        :type start_date: datetime
        :param end_date: **参数解释：** 结束日期。
        :type end_date: datetime
        :param only_count: **参数解释：** 是否仅返回todo。 **取值范围：** - true，仅返回带有提交计数和diffs计数的结果。 - false，按照compare_view参数返回结果信息。
        :type only_count: bool
        :param review_categories: **参数解释：** 搜索的检视意见分类。 **取值范围：** 字符串长度不少于1，不超过200。
        :type review_categories: str
        :param review_modules: **参数解释：** 搜索的检视意见模块。 **取值范围：** 字符串长度不少于1，不超过200。
        :type review_modules: str
        :param severity: **参数解释：** 检视意见严重程度
        :type severity: str
        :param assignee_id: **参数解释：** 检视意见指派人id。
        :type assignee_id: int
        :param proposer_id: **参数解释：** 检视意见检视人id。
        :type proposer_id: int
        :param target_branch: **参数解释：** 目标分支名称。 **取值范围：** 字符串长度不少于1，不超过2000。
        :type target_branch: str
        :param include_reply: **参数解释：** 是否包含回复。 **取值范围：** - true，包含。 - false，不包含。
        :type include_reply: bool
        :param order_by: **参数解释：** 排序方式。 **取值范围：** - created，创建时间。 - updated，更新时间。
        :type order_by: str
        :param sort: **参数解释：** 检视意见返回排序 - asc 按创建时间正序返回 - desc 按创建时间倒序返回
        :type sort: str
        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        """
        
        

        self._repository_id = None
        self._noteable_type = None
        self._search = None
        self._start_date = None
        self._end_date = None
        self._only_count = None
        self._review_categories = None
        self._review_modules = None
        self._severity = None
        self._assignee_id = None
        self._proposer_id = None
        self._target_branch = None
        self._include_reply = None
        self._order_by = None
        self._sort = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.repository_id = repository_id
        self.noteable_type = noteable_type
        if search is not None:
            self.search = search
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if only_count is not None:
            self.only_count = only_count
        if review_categories is not None:
            self.review_categories = review_categories
        if review_modules is not None:
            self.review_modules = review_modules
        if severity is not None:
            self.severity = severity
        if assignee_id is not None:
            self.assignee_id = assignee_id
        if proposer_id is not None:
            self.proposer_id = proposer_id
        if target_branch is not None:
            self.target_branch = target_branch
        if include_reply is not None:
            self.include_reply = include_reply
        if order_by is not None:
            self.order_by = order_by
        if sort is not None:
            self.sort = sort
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ListRepositoryReviewsRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this ListRepositoryReviewsRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ListRepositoryReviewsRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this ListRepositoryReviewsRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def noteable_type(self):
        r"""Gets the noteable_type of this ListRepositoryReviewsRequest.

        **参数解释：** 意见类型。 **取值范围：** - Commit，提交。 - MergeRequest，合并请求。  

        :return: The noteable_type of this ListRepositoryReviewsRequest.
        :rtype: str
        """
        return self._noteable_type

    @noteable_type.setter
    def noteable_type(self, noteable_type):
        r"""Sets the noteable_type of this ListRepositoryReviewsRequest.

        **参数解释：** 意见类型。 **取值范围：** - Commit，提交。 - MergeRequest，合并请求。  

        :param noteable_type: The noteable_type of this ListRepositoryReviewsRequest.
        :type noteable_type: str
        """
        self._noteable_type = noteable_type

    @property
    def search(self):
        r"""Gets the search of this ListRepositoryReviewsRequest.

        **参数解释：** 查询评论内容。

        :return: The search of this ListRepositoryReviewsRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListRepositoryReviewsRequest.

        **参数解释：** 查询评论内容。

        :param search: The search of this ListRepositoryReviewsRequest.
        :type search: str
        """
        self._search = search

    @property
    def start_date(self):
        r"""Gets the start_date of this ListRepositoryReviewsRequest.

        **参数解释：** 开始日期。

        :return: The start_date of this ListRepositoryReviewsRequest.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        r"""Sets the start_date of this ListRepositoryReviewsRequest.

        **参数解释：** 开始日期。

        :param start_date: The start_date of this ListRepositoryReviewsRequest.
        :type start_date: datetime
        """
        self._start_date = start_date

    @property
    def end_date(self):
        r"""Gets the end_date of this ListRepositoryReviewsRequest.

        **参数解释：** 结束日期。

        :return: The end_date of this ListRepositoryReviewsRequest.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        r"""Sets the end_date of this ListRepositoryReviewsRequest.

        **参数解释：** 结束日期。

        :param end_date: The end_date of this ListRepositoryReviewsRequest.
        :type end_date: datetime
        """
        self._end_date = end_date

    @property
    def only_count(self):
        r"""Gets the only_count of this ListRepositoryReviewsRequest.

        **参数解释：** 是否仅返回todo。 **取值范围：** - true，仅返回带有提交计数和diffs计数的结果。 - false，按照compare_view参数返回结果信息。

        :return: The only_count of this ListRepositoryReviewsRequest.
        :rtype: bool
        """
        return self._only_count

    @only_count.setter
    def only_count(self, only_count):
        r"""Sets the only_count of this ListRepositoryReviewsRequest.

        **参数解释：** 是否仅返回todo。 **取值范围：** - true，仅返回带有提交计数和diffs计数的结果。 - false，按照compare_view参数返回结果信息。

        :param only_count: The only_count of this ListRepositoryReviewsRequest.
        :type only_count: bool
        """
        self._only_count = only_count

    @property
    def review_categories(self):
        r"""Gets the review_categories of this ListRepositoryReviewsRequest.

        **参数解释：** 搜索的检视意见分类。 **取值范围：** 字符串长度不少于1，不超过200。

        :return: The review_categories of this ListRepositoryReviewsRequest.
        :rtype: str
        """
        return self._review_categories

    @review_categories.setter
    def review_categories(self, review_categories):
        r"""Sets the review_categories of this ListRepositoryReviewsRequest.

        **参数解释：** 搜索的检视意见分类。 **取值范围：** 字符串长度不少于1，不超过200。

        :param review_categories: The review_categories of this ListRepositoryReviewsRequest.
        :type review_categories: str
        """
        self._review_categories = review_categories

    @property
    def review_modules(self):
        r"""Gets the review_modules of this ListRepositoryReviewsRequest.

        **参数解释：** 搜索的检视意见模块。 **取值范围：** 字符串长度不少于1，不超过200。

        :return: The review_modules of this ListRepositoryReviewsRequest.
        :rtype: str
        """
        return self._review_modules

    @review_modules.setter
    def review_modules(self, review_modules):
        r"""Sets the review_modules of this ListRepositoryReviewsRequest.

        **参数解释：** 搜索的检视意见模块。 **取值范围：** 字符串长度不少于1，不超过200。

        :param review_modules: The review_modules of this ListRepositoryReviewsRequest.
        :type review_modules: str
        """
        self._review_modules = review_modules

    @property
    def severity(self):
        r"""Gets the severity of this ListRepositoryReviewsRequest.

        **参数解释：** 检视意见严重程度

        :return: The severity of this ListRepositoryReviewsRequest.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ListRepositoryReviewsRequest.

        **参数解释：** 检视意见严重程度

        :param severity: The severity of this ListRepositoryReviewsRequest.
        :type severity: str
        """
        self._severity = severity

    @property
    def assignee_id(self):
        r"""Gets the assignee_id of this ListRepositoryReviewsRequest.

        **参数解释：** 检视意见指派人id。

        :return: The assignee_id of this ListRepositoryReviewsRequest.
        :rtype: int
        """
        return self._assignee_id

    @assignee_id.setter
    def assignee_id(self, assignee_id):
        r"""Sets the assignee_id of this ListRepositoryReviewsRequest.

        **参数解释：** 检视意见指派人id。

        :param assignee_id: The assignee_id of this ListRepositoryReviewsRequest.
        :type assignee_id: int
        """
        self._assignee_id = assignee_id

    @property
    def proposer_id(self):
        r"""Gets the proposer_id of this ListRepositoryReviewsRequest.

        **参数解释：** 检视意见检视人id。

        :return: The proposer_id of this ListRepositoryReviewsRequest.
        :rtype: int
        """
        return self._proposer_id

    @proposer_id.setter
    def proposer_id(self, proposer_id):
        r"""Sets the proposer_id of this ListRepositoryReviewsRequest.

        **参数解释：** 检视意见检视人id。

        :param proposer_id: The proposer_id of this ListRepositoryReviewsRequest.
        :type proposer_id: int
        """
        self._proposer_id = proposer_id

    @property
    def target_branch(self):
        r"""Gets the target_branch of this ListRepositoryReviewsRequest.

        **参数解释：** 目标分支名称。 **取值范围：** 字符串长度不少于1，不超过2000。

        :return: The target_branch of this ListRepositoryReviewsRequest.
        :rtype: str
        """
        return self._target_branch

    @target_branch.setter
    def target_branch(self, target_branch):
        r"""Sets the target_branch of this ListRepositoryReviewsRequest.

        **参数解释：** 目标分支名称。 **取值范围：** 字符串长度不少于1，不超过2000。

        :param target_branch: The target_branch of this ListRepositoryReviewsRequest.
        :type target_branch: str
        """
        self._target_branch = target_branch

    @property
    def include_reply(self):
        r"""Gets the include_reply of this ListRepositoryReviewsRequest.

        **参数解释：** 是否包含回复。 **取值范围：** - true，包含。 - false，不包含。

        :return: The include_reply of this ListRepositoryReviewsRequest.
        :rtype: bool
        """
        return self._include_reply

    @include_reply.setter
    def include_reply(self, include_reply):
        r"""Sets the include_reply of this ListRepositoryReviewsRequest.

        **参数解释：** 是否包含回复。 **取值范围：** - true，包含。 - false，不包含。

        :param include_reply: The include_reply of this ListRepositoryReviewsRequest.
        :type include_reply: bool
        """
        self._include_reply = include_reply

    @property
    def order_by(self):
        r"""Gets the order_by of this ListRepositoryReviewsRequest.

        **参数解释：** 排序方式。 **取值范围：** - created，创建时间。 - updated，更新时间。

        :return: The order_by of this ListRepositoryReviewsRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListRepositoryReviewsRequest.

        **参数解释：** 排序方式。 **取值范围：** - created，创建时间。 - updated，更新时间。

        :param order_by: The order_by of this ListRepositoryReviewsRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def sort(self):
        r"""Gets the sort of this ListRepositoryReviewsRequest.

        **参数解释：** 检视意见返回排序 - asc 按创建时间正序返回 - desc 按创建时间倒序返回

        :return: The sort of this ListRepositoryReviewsRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ListRepositoryReviewsRequest.

        **参数解释：** 检视意见返回排序 - asc 按创建时间正序返回 - desc 按创建时间倒序返回

        :param sort: The sort of this ListRepositoryReviewsRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def offset(self):
        r"""Gets the offset of this ListRepositoryReviewsRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListRepositoryReviewsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListRepositoryReviewsRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListRepositoryReviewsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListRepositoryReviewsRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListRepositoryReviewsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRepositoryReviewsRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListRepositoryReviewsRequest.
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
        if not isinstance(other, ListRepositoryReviewsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
