# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPersonalRepositoryImportRecordsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'state': 'str',
        'source_type': 'str',
        'created_after': 'datetime',
        'created_before': 'datetime',
        'finished_after': 'datetime',
        'finished_before': 'datetime',
        'search': 'str',
        'order_by': 'str',
        'sort': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'state': 'state',
        'source_type': 'source_type',
        'created_after': 'created_after',
        'created_before': 'created_before',
        'finished_after': 'finished_after',
        'finished_before': 'finished_before',
        'search': 'search',
        'order_by': 'order_by',
        'sort': 'sort'
    }

    def __init__(self, offset=None, limit=None, state=None, source_type=None, created_after=None, created_before=None, finished_after=None, finished_before=None, search=None, order_by=None, sort=None):
        r"""ListPersonalRepositoryImportRecordsRequest

        The model defined in huaweicloud sdk

        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        :param state: **参数解释：** 状态 **取值范围：** - finished, 导入成功 - fail, 导入失败 - importing, 导入中
        :type state: str
        :param source_type: **参数解释：** 导入来源 **取值范围：** - gitee - self_managed_gitlab - gitlab - github - git - svn - coding - bitbucket - gerrit - codeup
        :type source_type: str
        :param created_after: **参数解释：** 筛选在该时间之后导入的
        :type created_after: datetime
        :param created_before: **参数解释：** 筛选在该时间之前导入的
        :type created_before: datetime
        :param finished_after: **参数解释：** 筛选在该时间之后导入完成的
        :type finished_after: datetime
        :param finished_before: **参数解释：** 筛选在该时间之前导入完成的
        :type finished_before: datetime
        :param search: **参数解释：** 搜索仓库
        :type search: str
        :param order_by: **参数解释：** 排序方式。 **取值范围：** - created_at, 导入时间 - source_repo_name, 源仓库路径 - size, 源仓库容量
        :type order_by: str
        :param sort: **参数解释：** 返回排序 - asc 正序返回 - desc 倒序返回
        :type sort: str
        """
        
        

        self._offset = None
        self._limit = None
        self._state = None
        self._source_type = None
        self._created_after = None
        self._created_before = None
        self._finished_after = None
        self._finished_before = None
        self._search = None
        self._order_by = None
        self._sort = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if state is not None:
            self.state = state
        if source_type is not None:
            self.source_type = source_type
        if created_after is not None:
            self.created_after = created_after
        if created_before is not None:
            self.created_before = created_before
        if finished_after is not None:
            self.finished_after = finished_after
        if finished_before is not None:
            self.finished_before = finished_before
        if search is not None:
            self.search = search
        if order_by is not None:
            self.order_by = order_by
        if sort is not None:
            self.sort = sort

    @property
    def offset(self):
        r"""Gets the offset of this ListPersonalRepositoryImportRecordsRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListPersonalRepositoryImportRecordsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPersonalRepositoryImportRecordsRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListPersonalRepositoryImportRecordsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListPersonalRepositoryImportRecordsRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListPersonalRepositoryImportRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPersonalRepositoryImportRecordsRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListPersonalRepositoryImportRecordsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def state(self):
        r"""Gets the state of this ListPersonalRepositoryImportRecordsRequest.

        **参数解释：** 状态 **取值范围：** - finished, 导入成功 - fail, 导入失败 - importing, 导入中

        :return: The state of this ListPersonalRepositoryImportRecordsRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListPersonalRepositoryImportRecordsRequest.

        **参数解释：** 状态 **取值范围：** - finished, 导入成功 - fail, 导入失败 - importing, 导入中

        :param state: The state of this ListPersonalRepositoryImportRecordsRequest.
        :type state: str
        """
        self._state = state

    @property
    def source_type(self):
        r"""Gets the source_type of this ListPersonalRepositoryImportRecordsRequest.

        **参数解释：** 导入来源 **取值范围：** - gitee - self_managed_gitlab - gitlab - github - git - svn - coding - bitbucket - gerrit - codeup

        :return: The source_type of this ListPersonalRepositoryImportRecordsRequest.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        r"""Sets the source_type of this ListPersonalRepositoryImportRecordsRequest.

        **参数解释：** 导入来源 **取值范围：** - gitee - self_managed_gitlab - gitlab - github - git - svn - coding - bitbucket - gerrit - codeup

        :param source_type: The source_type of this ListPersonalRepositoryImportRecordsRequest.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def created_after(self):
        r"""Gets the created_after of this ListPersonalRepositoryImportRecordsRequest.

        **参数解释：** 筛选在该时间之后导入的

        :return: The created_after of this ListPersonalRepositoryImportRecordsRequest.
        :rtype: datetime
        """
        return self._created_after

    @created_after.setter
    def created_after(self, created_after):
        r"""Sets the created_after of this ListPersonalRepositoryImportRecordsRequest.

        **参数解释：** 筛选在该时间之后导入的

        :param created_after: The created_after of this ListPersonalRepositoryImportRecordsRequest.
        :type created_after: datetime
        """
        self._created_after = created_after

    @property
    def created_before(self):
        r"""Gets the created_before of this ListPersonalRepositoryImportRecordsRequest.

        **参数解释：** 筛选在该时间之前导入的

        :return: The created_before of this ListPersonalRepositoryImportRecordsRequest.
        :rtype: datetime
        """
        return self._created_before

    @created_before.setter
    def created_before(self, created_before):
        r"""Sets the created_before of this ListPersonalRepositoryImportRecordsRequest.

        **参数解释：** 筛选在该时间之前导入的

        :param created_before: The created_before of this ListPersonalRepositoryImportRecordsRequest.
        :type created_before: datetime
        """
        self._created_before = created_before

    @property
    def finished_after(self):
        r"""Gets the finished_after of this ListPersonalRepositoryImportRecordsRequest.

        **参数解释：** 筛选在该时间之后导入完成的

        :return: The finished_after of this ListPersonalRepositoryImportRecordsRequest.
        :rtype: datetime
        """
        return self._finished_after

    @finished_after.setter
    def finished_after(self, finished_after):
        r"""Sets the finished_after of this ListPersonalRepositoryImportRecordsRequest.

        **参数解释：** 筛选在该时间之后导入完成的

        :param finished_after: The finished_after of this ListPersonalRepositoryImportRecordsRequest.
        :type finished_after: datetime
        """
        self._finished_after = finished_after

    @property
    def finished_before(self):
        r"""Gets the finished_before of this ListPersonalRepositoryImportRecordsRequest.

        **参数解释：** 筛选在该时间之前导入完成的

        :return: The finished_before of this ListPersonalRepositoryImportRecordsRequest.
        :rtype: datetime
        """
        return self._finished_before

    @finished_before.setter
    def finished_before(self, finished_before):
        r"""Sets the finished_before of this ListPersonalRepositoryImportRecordsRequest.

        **参数解释：** 筛选在该时间之前导入完成的

        :param finished_before: The finished_before of this ListPersonalRepositoryImportRecordsRequest.
        :type finished_before: datetime
        """
        self._finished_before = finished_before

    @property
    def search(self):
        r"""Gets the search of this ListPersonalRepositoryImportRecordsRequest.

        **参数解释：** 搜索仓库

        :return: The search of this ListPersonalRepositoryImportRecordsRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListPersonalRepositoryImportRecordsRequest.

        **参数解释：** 搜索仓库

        :param search: The search of this ListPersonalRepositoryImportRecordsRequest.
        :type search: str
        """
        self._search = search

    @property
    def order_by(self):
        r"""Gets the order_by of this ListPersonalRepositoryImportRecordsRequest.

        **参数解释：** 排序方式。 **取值范围：** - created_at, 导入时间 - source_repo_name, 源仓库路径 - size, 源仓库容量

        :return: The order_by of this ListPersonalRepositoryImportRecordsRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListPersonalRepositoryImportRecordsRequest.

        **参数解释：** 排序方式。 **取值范围：** - created_at, 导入时间 - source_repo_name, 源仓库路径 - size, 源仓库容量

        :param order_by: The order_by of this ListPersonalRepositoryImportRecordsRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def sort(self):
        r"""Gets the sort of this ListPersonalRepositoryImportRecordsRequest.

        **参数解释：** 返回排序 - asc 正序返回 - desc 倒序返回

        :return: The sort of this ListPersonalRepositoryImportRecordsRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ListPersonalRepositoryImportRecordsRequest.

        **参数解释：** 返回排序 - asc 正序返回 - desc 倒序返回

        :param sort: The sort of this ListPersonalRepositoryImportRecordsRequest.
        :type sort: str
        """
        self._sort = sort

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
        if not isinstance(other, ListPersonalRepositoryImportRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
