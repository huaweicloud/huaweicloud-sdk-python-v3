# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTagsRequest:

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
        'creator': 'str',
        'sort': 'str',
        'search': 'str',
        'order_by': 'str',
        'view': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'creator': 'creator',
        'sort': 'sort',
        'search': 'search',
        'order_by': 'order_by',
        'view': 'view',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, repository_id=None, creator=None, sort=None, search=None, order_by=None, view=None, offset=None, limit=None):
        r"""ListTagsRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param creator: **参数解释：** 创建者，用户ID或者IamId。 **取值范围：** 字符串长度不少于1，不超过100000。
        :type creator: str
        :param sort: **参数解释：** 排序方式。 **约束限制：** - asc，升序。 - desc，降序。
        :type sort: str
        :param search: **参数解释：** 搜索条件，按标签名称搜索。 **取值范围：** 字符串长度不少于1，不超过2000。
        :type search: str
        :param order_by: **参数解释：** 排序方式。 **取值范围：** - name，名字。 - created，创建时间。 - updated，更新时间。
        :type order_by: str
        :param view: **参数解释：** 结果集展示内容。 **取值范围：** - detail，返回标签的所有信息。 - basic，返回标签的基本信息。 - simple，返回标签的简单信息。
        :type view: str
        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        """
        
        

        self._repository_id = None
        self._creator = None
        self._sort = None
        self._search = None
        self._order_by = None
        self._view = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.repository_id = repository_id
        if creator is not None:
            self.creator = creator
        if sort is not None:
            self.sort = sort
        if search is not None:
            self.search = search
        if order_by is not None:
            self.order_by = order_by
        if view is not None:
            self.view = view
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ListTagsRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this ListTagsRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ListTagsRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this ListTagsRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def creator(self):
        r"""Gets the creator of this ListTagsRequest.

        **参数解释：** 创建者，用户ID或者IamId。 **取值范围：** 字符串长度不少于1，不超过100000。

        :return: The creator of this ListTagsRequest.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ListTagsRequest.

        **参数解释：** 创建者，用户ID或者IamId。 **取值范围：** 字符串长度不少于1，不超过100000。

        :param creator: The creator of this ListTagsRequest.
        :type creator: str
        """
        self._creator = creator

    @property
    def sort(self):
        r"""Gets the sort of this ListTagsRequest.

        **参数解释：** 排序方式。 **约束限制：** - asc，升序。 - desc，降序。

        :return: The sort of this ListTagsRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ListTagsRequest.

        **参数解释：** 排序方式。 **约束限制：** - asc，升序。 - desc，降序。

        :param sort: The sort of this ListTagsRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def search(self):
        r"""Gets the search of this ListTagsRequest.

        **参数解释：** 搜索条件，按标签名称搜索。 **取值范围：** 字符串长度不少于1，不超过2000。

        :return: The search of this ListTagsRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListTagsRequest.

        **参数解释：** 搜索条件，按标签名称搜索。 **取值范围：** 字符串长度不少于1，不超过2000。

        :param search: The search of this ListTagsRequest.
        :type search: str
        """
        self._search = search

    @property
    def order_by(self):
        r"""Gets the order_by of this ListTagsRequest.

        **参数解释：** 排序方式。 **取值范围：** - name，名字。 - created，创建时间。 - updated，更新时间。

        :return: The order_by of this ListTagsRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListTagsRequest.

        **参数解释：** 排序方式。 **取值范围：** - name，名字。 - created，创建时间。 - updated，更新时间。

        :param order_by: The order_by of this ListTagsRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def view(self):
        r"""Gets the view of this ListTagsRequest.

        **参数解释：** 结果集展示内容。 **取值范围：** - detail，返回标签的所有信息。 - basic，返回标签的基本信息。 - simple，返回标签的简单信息。

        :return: The view of this ListTagsRequest.
        :rtype: str
        """
        return self._view

    @view.setter
    def view(self, view):
        r"""Sets the view of this ListTagsRequest.

        **参数解释：** 结果集展示内容。 **取值范围：** - detail，返回标签的所有信息。 - basic，返回标签的基本信息。 - simple，返回标签的简单信息。

        :param view: The view of this ListTagsRequest.
        :type view: str
        """
        self._view = view

    @property
    def offset(self):
        r"""Gets the offset of this ListTagsRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListTagsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTagsRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListTagsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListTagsRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListTagsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTagsRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListTagsRequest.
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
        if not isinstance(other, ListTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
