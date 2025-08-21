# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRepositoryLabelsRequest:

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
        'search': 'str',
        'sort': 'str',
        'include_expired': 'bool',
        'view': 'str'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'offset': 'offset',
        'limit': 'limit',
        'search': 'search',
        'sort': 'sort',
        'include_expired': 'include_expired',
        'view': 'view'
    }

    def __init__(self, repository_id=None, offset=None, limit=None, search=None, sort=None, include_expired=None, view=None):
        r"""ListRepositoryLabelsRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        :param search: **参数解释：** 查询关键字，可模糊匹配标签名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type search: str
        :param sort: **参数解释：**  排序。 **约束限制：** 不涉及。 **取值范围：** - name_asc，按标签名升序。 - name_desc，按标签名降序。 - created_asc，按标创建时间升序。 - created_desc，按标创建时间降序。 - updated_asc，按标更新时间升序。 - updated_desc，按标更新时间降序。 **默认取值：** name_asc
        :type sort: str
        :param include_expired: **参数解释：** 是否包含失效的标签。 **约束限制：** 不涉及。 **取值范围：** - true，包含。 - false，不包含。 **默认取值：** true
        :type include_expired: bool
        :param view: **参数解释：** 结果集属性，根据给定的参数返回不同的结果。 **约束限制：** 不涉及。 **取值范围：** - simple，返回简略信息。 - basic，返回基本信息。 - detail，返回详细信息。 **默认取值：** basic
        :type view: str
        """
        
        

        self._repository_id = None
        self._offset = None
        self._limit = None
        self._search = None
        self._sort = None
        self._include_expired = None
        self._view = None
        self.discriminator = None

        self.repository_id = repository_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if search is not None:
            self.search = search
        if sort is not None:
            self.sort = sort
        if include_expired is not None:
            self.include_expired = include_expired
        if view is not None:
            self.view = view

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ListRepositoryLabelsRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this ListRepositoryLabelsRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ListRepositoryLabelsRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this ListRepositoryLabelsRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def offset(self):
        r"""Gets the offset of this ListRepositoryLabelsRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListRepositoryLabelsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListRepositoryLabelsRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListRepositoryLabelsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListRepositoryLabelsRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListRepositoryLabelsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRepositoryLabelsRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListRepositoryLabelsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def search(self):
        r"""Gets the search of this ListRepositoryLabelsRequest.

        **参数解释：** 查询关键字，可模糊匹配标签名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The search of this ListRepositoryLabelsRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListRepositoryLabelsRequest.

        **参数解释：** 查询关键字，可模糊匹配标签名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param search: The search of this ListRepositoryLabelsRequest.
        :type search: str
        """
        self._search = search

    @property
    def sort(self):
        r"""Gets the sort of this ListRepositoryLabelsRequest.

        **参数解释：**  排序。 **约束限制：** 不涉及。 **取值范围：** - name_asc，按标签名升序。 - name_desc，按标签名降序。 - created_asc，按标创建时间升序。 - created_desc，按标创建时间降序。 - updated_asc，按标更新时间升序。 - updated_desc，按标更新时间降序。 **默认取值：** name_asc

        :return: The sort of this ListRepositoryLabelsRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ListRepositoryLabelsRequest.

        **参数解释：**  排序。 **约束限制：** 不涉及。 **取值范围：** - name_asc，按标签名升序。 - name_desc，按标签名降序。 - created_asc，按标创建时间升序。 - created_desc，按标创建时间降序。 - updated_asc，按标更新时间升序。 - updated_desc，按标更新时间降序。 **默认取值：** name_asc

        :param sort: The sort of this ListRepositoryLabelsRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def include_expired(self):
        r"""Gets the include_expired of this ListRepositoryLabelsRequest.

        **参数解释：** 是否包含失效的标签。 **约束限制：** 不涉及。 **取值范围：** - true，包含。 - false，不包含。 **默认取值：** true

        :return: The include_expired of this ListRepositoryLabelsRequest.
        :rtype: bool
        """
        return self._include_expired

    @include_expired.setter
    def include_expired(self, include_expired):
        r"""Sets the include_expired of this ListRepositoryLabelsRequest.

        **参数解释：** 是否包含失效的标签。 **约束限制：** 不涉及。 **取值范围：** - true，包含。 - false，不包含。 **默认取值：** true

        :param include_expired: The include_expired of this ListRepositoryLabelsRequest.
        :type include_expired: bool
        """
        self._include_expired = include_expired

    @property
    def view(self):
        r"""Gets the view of this ListRepositoryLabelsRequest.

        **参数解释：** 结果集属性，根据给定的参数返回不同的结果。 **约束限制：** 不涉及。 **取值范围：** - simple，返回简略信息。 - basic，返回基本信息。 - detail，返回详细信息。 **默认取值：** basic

        :return: The view of this ListRepositoryLabelsRequest.
        :rtype: str
        """
        return self._view

    @view.setter
    def view(self, view):
        r"""Sets the view of this ListRepositoryLabelsRequest.

        **参数解释：** 结果集属性，根据给定的参数返回不同的结果。 **约束限制：** 不涉及。 **取值范围：** - simple，返回简略信息。 - basic，返回基本信息。 - detail，返回详细信息。 **默认取值：** basic

        :param view: The view of this ListRepositoryLabelsRequest.
        :type view: str
        """
        self._view = view

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
        if not isinstance(other, ListRepositoryLabelsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
