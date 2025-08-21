# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRepositoryEventsRequest:

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
        'author_id': 'int',
        'filter': 'str',
        'before': 'datetime',
        'after': 'datetime',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'author_id': 'author_id',
        'filter': 'filter',
        'before': 'before',
        'after': 'after',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, repository_id=None, author_id=None, filter=None, before=None, after=None, offset=None, limit=None):
        r"""ListRepositoryEventsRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param author_id: **参数解释：** 操作者id。
        :type author_id: int
        :param filter: **参数解释：** 动态类型。 **约束限制：** - all，表示全部。 - push，表示推送。
        :type filter: str
        :param before: **参数解释：** 开始日期。
        :type before: datetime
        :param after: **参数解释：** 结束日期。
        :type after: datetime
        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        """
        
        

        self._repository_id = None
        self._author_id = None
        self._filter = None
        self._before = None
        self._after = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.repository_id = repository_id
        if author_id is not None:
            self.author_id = author_id
        if filter is not None:
            self.filter = filter
        if before is not None:
            self.before = before
        if after is not None:
            self.after = after
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ListRepositoryEventsRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this ListRepositoryEventsRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ListRepositoryEventsRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this ListRepositoryEventsRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def author_id(self):
        r"""Gets the author_id of this ListRepositoryEventsRequest.

        **参数解释：** 操作者id。

        :return: The author_id of this ListRepositoryEventsRequest.
        :rtype: int
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        r"""Sets the author_id of this ListRepositoryEventsRequest.

        **参数解释：** 操作者id。

        :param author_id: The author_id of this ListRepositoryEventsRequest.
        :type author_id: int
        """
        self._author_id = author_id

    @property
    def filter(self):
        r"""Gets the filter of this ListRepositoryEventsRequest.

        **参数解释：** 动态类型。 **约束限制：** - all，表示全部。 - push，表示推送。

        :return: The filter of this ListRepositoryEventsRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this ListRepositoryEventsRequest.

        **参数解释：** 动态类型。 **约束限制：** - all，表示全部。 - push，表示推送。

        :param filter: The filter of this ListRepositoryEventsRequest.
        :type filter: str
        """
        self._filter = filter

    @property
    def before(self):
        r"""Gets the before of this ListRepositoryEventsRequest.

        **参数解释：** 开始日期。

        :return: The before of this ListRepositoryEventsRequest.
        :rtype: datetime
        """
        return self._before

    @before.setter
    def before(self, before):
        r"""Sets the before of this ListRepositoryEventsRequest.

        **参数解释：** 开始日期。

        :param before: The before of this ListRepositoryEventsRequest.
        :type before: datetime
        """
        self._before = before

    @property
    def after(self):
        r"""Gets the after of this ListRepositoryEventsRequest.

        **参数解释：** 结束日期。

        :return: The after of this ListRepositoryEventsRequest.
        :rtype: datetime
        """
        return self._after

    @after.setter
    def after(self, after):
        r"""Sets the after of this ListRepositoryEventsRequest.

        **参数解释：** 结束日期。

        :param after: The after of this ListRepositoryEventsRequest.
        :type after: datetime
        """
        self._after = after

    @property
    def offset(self):
        r"""Gets the offset of this ListRepositoryEventsRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListRepositoryEventsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListRepositoryEventsRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListRepositoryEventsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListRepositoryEventsRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListRepositoryEventsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRepositoryEventsRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListRepositoryEventsRequest.
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
        if not isinstance(other, ListRepositoryEventsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
