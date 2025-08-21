# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMergeRequestReviewersRequest:

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
        'target_branch': 'str',
        'source_branch': 'str',
        'merge_request_iid': 'int',
        'target_repository_id': 'str',
        'search': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'target_branch': 'target_branch',
        'source_branch': 'source_branch',
        'merge_request_iid': 'merge_request_iid',
        'target_repository_id': 'target_repository_id',
        'search': 'search',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, repository_id=None, target_branch=None, source_branch=None, merge_request_iid=None, target_repository_id=None, search=None, offset=None, limit=None):
        r"""ListMergeRequestReviewersRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param target_branch: **参数解释：** 目标分支。创建MR时，代码将要合入的分支。
        :type target_branch: str
        :param source_branch: **参数解释：** 目标分支。创建MR时，变更代码所属的分支。
        :type source_branch: str
        :param merge_request_iid: **参数解释：**  合并请求 iid。
        :type merge_request_iid: int
        :param target_repository_id: **参数解释：** 目标仓库id。创建MR时，代码将要合入的仓库。
        :type target_repository_id: str
        :param search: **参数解释：** 查询关键字，可模糊匹配用户名称、用户昵称、租户名称。
        :type search: str
        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        """
        
        

        self._repository_id = None
        self._target_branch = None
        self._source_branch = None
        self._merge_request_iid = None
        self._target_repository_id = None
        self._search = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.repository_id = repository_id
        if target_branch is not None:
            self.target_branch = target_branch
        if source_branch is not None:
            self.source_branch = source_branch
        if merge_request_iid is not None:
            self.merge_request_iid = merge_request_iid
        if target_repository_id is not None:
            self.target_repository_id = target_repository_id
        if search is not None:
            self.search = search
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ListMergeRequestReviewersRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this ListMergeRequestReviewersRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ListMergeRequestReviewersRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this ListMergeRequestReviewersRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def target_branch(self):
        r"""Gets the target_branch of this ListMergeRequestReviewersRequest.

        **参数解释：** 目标分支。创建MR时，代码将要合入的分支。

        :return: The target_branch of this ListMergeRequestReviewersRequest.
        :rtype: str
        """
        return self._target_branch

    @target_branch.setter
    def target_branch(self, target_branch):
        r"""Sets the target_branch of this ListMergeRequestReviewersRequest.

        **参数解释：** 目标分支。创建MR时，代码将要合入的分支。

        :param target_branch: The target_branch of this ListMergeRequestReviewersRequest.
        :type target_branch: str
        """
        self._target_branch = target_branch

    @property
    def source_branch(self):
        r"""Gets the source_branch of this ListMergeRequestReviewersRequest.

        **参数解释：** 目标分支。创建MR时，变更代码所属的分支。

        :return: The source_branch of this ListMergeRequestReviewersRequest.
        :rtype: str
        """
        return self._source_branch

    @source_branch.setter
    def source_branch(self, source_branch):
        r"""Sets the source_branch of this ListMergeRequestReviewersRequest.

        **参数解释：** 目标分支。创建MR时，变更代码所属的分支。

        :param source_branch: The source_branch of this ListMergeRequestReviewersRequest.
        :type source_branch: str
        """
        self._source_branch = source_branch

    @property
    def merge_request_iid(self):
        r"""Gets the merge_request_iid of this ListMergeRequestReviewersRequest.

        **参数解释：**  合并请求 iid。

        :return: The merge_request_iid of this ListMergeRequestReviewersRequest.
        :rtype: int
        """
        return self._merge_request_iid

    @merge_request_iid.setter
    def merge_request_iid(self, merge_request_iid):
        r"""Sets the merge_request_iid of this ListMergeRequestReviewersRequest.

        **参数解释：**  合并请求 iid。

        :param merge_request_iid: The merge_request_iid of this ListMergeRequestReviewersRequest.
        :type merge_request_iid: int
        """
        self._merge_request_iid = merge_request_iid

    @property
    def target_repository_id(self):
        r"""Gets the target_repository_id of this ListMergeRequestReviewersRequest.

        **参数解释：** 目标仓库id。创建MR时，代码将要合入的仓库。

        :return: The target_repository_id of this ListMergeRequestReviewersRequest.
        :rtype: str
        """
        return self._target_repository_id

    @target_repository_id.setter
    def target_repository_id(self, target_repository_id):
        r"""Sets the target_repository_id of this ListMergeRequestReviewersRequest.

        **参数解释：** 目标仓库id。创建MR时，代码将要合入的仓库。

        :param target_repository_id: The target_repository_id of this ListMergeRequestReviewersRequest.
        :type target_repository_id: str
        """
        self._target_repository_id = target_repository_id

    @property
    def search(self):
        r"""Gets the search of this ListMergeRequestReviewersRequest.

        **参数解释：** 查询关键字，可模糊匹配用户名称、用户昵称、租户名称。

        :return: The search of this ListMergeRequestReviewersRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListMergeRequestReviewersRequest.

        **参数解释：** 查询关键字，可模糊匹配用户名称、用户昵称、租户名称。

        :param search: The search of this ListMergeRequestReviewersRequest.
        :type search: str
        """
        self._search = search

    @property
    def offset(self):
        r"""Gets the offset of this ListMergeRequestReviewersRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListMergeRequestReviewersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListMergeRequestReviewersRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListMergeRequestReviewersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListMergeRequestReviewersRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListMergeRequestReviewersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListMergeRequestReviewersRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListMergeRequestReviewersRequest.
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
        if not isinstance(other, ListMergeRequestReviewersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
