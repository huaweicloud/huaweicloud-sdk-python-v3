# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMergeRequestDiscussionsRequest:

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
        'merge_request_iid': 'int',
        'unresolved': 'str',
        'author_id': 'int',
        'sort': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'merge_request_iid': 'merge_request_iid',
        'unresolved': 'unresolved',
        'author_id': 'author_id',
        'sort': 'sort',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, repository_id=None, merge_request_iid=None, unresolved=None, author_id=None, sort=None, offset=None, limit=None):
        r"""ListMergeRequestDiscussionsRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param merge_request_iid: **参数解释：**  合并请求 iid。
        :type merge_request_iid: int
        :param unresolved: **参数解释：** 是否筛选解决的检视意见 - true 筛选所有未解决的检视意见 - false 筛选所有已解决的检视意见 - &#39;&#39; 不传此值时默认查询所有检视意见
        :type unresolved: str
        :param author_id: **参数解释：** 操作者id。
        :type author_id: int
        :param sort: **参数解释：** 检视意见返回排序 - asc 按创建时间正序返回 - desc 按创建时间倒序返回
        :type sort: str
        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        """
        
        

        self._repository_id = None
        self._merge_request_iid = None
        self._unresolved = None
        self._author_id = None
        self._sort = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.repository_id = repository_id
        self.merge_request_iid = merge_request_iid
        if unresolved is not None:
            self.unresolved = unresolved
        if author_id is not None:
            self.author_id = author_id
        if sort is not None:
            self.sort = sort
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ListMergeRequestDiscussionsRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this ListMergeRequestDiscussionsRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ListMergeRequestDiscussionsRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this ListMergeRequestDiscussionsRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def merge_request_iid(self):
        r"""Gets the merge_request_iid of this ListMergeRequestDiscussionsRequest.

        **参数解释：**  合并请求 iid。

        :return: The merge_request_iid of this ListMergeRequestDiscussionsRequest.
        :rtype: int
        """
        return self._merge_request_iid

    @merge_request_iid.setter
    def merge_request_iid(self, merge_request_iid):
        r"""Sets the merge_request_iid of this ListMergeRequestDiscussionsRequest.

        **参数解释：**  合并请求 iid。

        :param merge_request_iid: The merge_request_iid of this ListMergeRequestDiscussionsRequest.
        :type merge_request_iid: int
        """
        self._merge_request_iid = merge_request_iid

    @property
    def unresolved(self):
        r"""Gets the unresolved of this ListMergeRequestDiscussionsRequest.

        **参数解释：** 是否筛选解决的检视意见 - true 筛选所有未解决的检视意见 - false 筛选所有已解决的检视意见 - '' 不传此值时默认查询所有检视意见

        :return: The unresolved of this ListMergeRequestDiscussionsRequest.
        :rtype: str
        """
        return self._unresolved

    @unresolved.setter
    def unresolved(self, unresolved):
        r"""Sets the unresolved of this ListMergeRequestDiscussionsRequest.

        **参数解释：** 是否筛选解决的检视意见 - true 筛选所有未解决的检视意见 - false 筛选所有已解决的检视意见 - '' 不传此值时默认查询所有检视意见

        :param unresolved: The unresolved of this ListMergeRequestDiscussionsRequest.
        :type unresolved: str
        """
        self._unresolved = unresolved

    @property
    def author_id(self):
        r"""Gets the author_id of this ListMergeRequestDiscussionsRequest.

        **参数解释：** 操作者id。

        :return: The author_id of this ListMergeRequestDiscussionsRequest.
        :rtype: int
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        r"""Sets the author_id of this ListMergeRequestDiscussionsRequest.

        **参数解释：** 操作者id。

        :param author_id: The author_id of this ListMergeRequestDiscussionsRequest.
        :type author_id: int
        """
        self._author_id = author_id

    @property
    def sort(self):
        r"""Gets the sort of this ListMergeRequestDiscussionsRequest.

        **参数解释：** 检视意见返回排序 - asc 按创建时间正序返回 - desc 按创建时间倒序返回

        :return: The sort of this ListMergeRequestDiscussionsRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ListMergeRequestDiscussionsRequest.

        **参数解释：** 检视意见返回排序 - asc 按创建时间正序返回 - desc 按创建时间倒序返回

        :param sort: The sort of this ListMergeRequestDiscussionsRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def offset(self):
        r"""Gets the offset of this ListMergeRequestDiscussionsRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListMergeRequestDiscussionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListMergeRequestDiscussionsRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListMergeRequestDiscussionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListMergeRequestDiscussionsRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListMergeRequestDiscussionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListMergeRequestDiscussionsRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListMergeRequestDiscussionsRequest.
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
        if not isinstance(other, ListMergeRequestDiscussionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
