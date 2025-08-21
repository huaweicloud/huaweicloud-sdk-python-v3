# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRepositoryContributorsRequest:

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
        'order_by': 'str',
        'sort': 'str',
        'ref_name': 'str',
        'skip_merge': 'bool',
        'author': 'str'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'offset': 'offset',
        'limit': 'limit',
        'order_by': 'order_by',
        'sort': 'sort',
        'ref_name': 'ref_name',
        'skip_merge': 'skip_merge',
        'author': 'author'
    }

    def __init__(self, repository_id=None, offset=None, limit=None, order_by=None, sort=None, ref_name=None, skip_merge=None, author=None):
        r"""ListRepositoryContributorsRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        :param order_by: **参数解释：** 排序方式。 **取值范围：** - name，名字。 - email，邮箱。 - commits，提交数量。
        :type order_by: str
        :param sort: **参数解释：** 返回排序 - asc 按提交数量正序返回 - desc 按提交数量倒序返回
        :type sort: str
        :param ref_name: **参数解释：** 分支或者tag名称。 **约束限制：** 不支持以 - . refs/heads/ refs/remotes/ 开头，不支持空格 [ \\ &lt; ~ ^ : ? * ! ( ) &#39; \&quot; | 等特殊字符，不支持以. / .lock结尾。 **取值范围：** 字符串长度不少于1，不超过200。 **默认取值：** 仓库默认分支。
        :type ref_name: str
        :param skip_merge: **参数解释：** 是否跳过合并。 **约束限制：** 不涉及。 **取值范围：** - false, 跳过合并 - true, 不跳过合并
        :type skip_merge: bool
        :param author: **参数解释：** 提交者。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type author: str
        """
        
        

        self._repository_id = None
        self._offset = None
        self._limit = None
        self._order_by = None
        self._sort = None
        self._ref_name = None
        self._skip_merge = None
        self._author = None
        self.discriminator = None

        self.repository_id = repository_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if order_by is not None:
            self.order_by = order_by
        if sort is not None:
            self.sort = sort
        if ref_name is not None:
            self.ref_name = ref_name
        if skip_merge is not None:
            self.skip_merge = skip_merge
        if author is not None:
            self.author = author

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ListRepositoryContributorsRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this ListRepositoryContributorsRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ListRepositoryContributorsRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this ListRepositoryContributorsRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def offset(self):
        r"""Gets the offset of this ListRepositoryContributorsRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListRepositoryContributorsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListRepositoryContributorsRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListRepositoryContributorsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListRepositoryContributorsRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListRepositoryContributorsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRepositoryContributorsRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListRepositoryContributorsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def order_by(self):
        r"""Gets the order_by of this ListRepositoryContributorsRequest.

        **参数解释：** 排序方式。 **取值范围：** - name，名字。 - email，邮箱。 - commits，提交数量。

        :return: The order_by of this ListRepositoryContributorsRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListRepositoryContributorsRequest.

        **参数解释：** 排序方式。 **取值范围：** - name，名字。 - email，邮箱。 - commits，提交数量。

        :param order_by: The order_by of this ListRepositoryContributorsRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def sort(self):
        r"""Gets the sort of this ListRepositoryContributorsRequest.

        **参数解释：** 返回排序 - asc 按提交数量正序返回 - desc 按提交数量倒序返回

        :return: The sort of this ListRepositoryContributorsRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ListRepositoryContributorsRequest.

        **参数解释：** 返回排序 - asc 按提交数量正序返回 - desc 按提交数量倒序返回

        :param sort: The sort of this ListRepositoryContributorsRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def ref_name(self):
        r"""Gets the ref_name of this ListRepositoryContributorsRequest.

        **参数解释：** 分支或者tag名称。 **约束限制：** 不支持以 - . refs/heads/ refs/remotes/ 开头，不支持空格 [ \\ < ~ ^ : ? * ! ( ) ' \" | 等特殊字符，不支持以. / .lock结尾。 **取值范围：** 字符串长度不少于1，不超过200。 **默认取值：** 仓库默认分支。

        :return: The ref_name of this ListRepositoryContributorsRequest.
        :rtype: str
        """
        return self._ref_name

    @ref_name.setter
    def ref_name(self, ref_name):
        r"""Sets the ref_name of this ListRepositoryContributorsRequest.

        **参数解释：** 分支或者tag名称。 **约束限制：** 不支持以 - . refs/heads/ refs/remotes/ 开头，不支持空格 [ \\ < ~ ^ : ? * ! ( ) ' \" | 等特殊字符，不支持以. / .lock结尾。 **取值范围：** 字符串长度不少于1，不超过200。 **默认取值：** 仓库默认分支。

        :param ref_name: The ref_name of this ListRepositoryContributorsRequest.
        :type ref_name: str
        """
        self._ref_name = ref_name

    @property
    def skip_merge(self):
        r"""Gets the skip_merge of this ListRepositoryContributorsRequest.

        **参数解释：** 是否跳过合并。 **约束限制：** 不涉及。 **取值范围：** - false, 跳过合并 - true, 不跳过合并

        :return: The skip_merge of this ListRepositoryContributorsRequest.
        :rtype: bool
        """
        return self._skip_merge

    @skip_merge.setter
    def skip_merge(self, skip_merge):
        r"""Sets the skip_merge of this ListRepositoryContributorsRequest.

        **参数解释：** 是否跳过合并。 **约束限制：** 不涉及。 **取值范围：** - false, 跳过合并 - true, 不跳过合并

        :param skip_merge: The skip_merge of this ListRepositoryContributorsRequest.
        :type skip_merge: bool
        """
        self._skip_merge = skip_merge

    @property
    def author(self):
        r"""Gets the author of this ListRepositoryContributorsRequest.

        **参数解释：** 提交者。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The author of this ListRepositoryContributorsRequest.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        r"""Sets the author of this ListRepositoryContributorsRequest.

        **参数解释：** 提交者。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param author: The author of this ListRepositoryContributorsRequest.
        :type author: str
        """
        self._author = author

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
        if not isinstance(other, ListRepositoryContributorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
