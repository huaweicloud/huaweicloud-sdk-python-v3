# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMergeRequestChangesTreesRequest:

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
        'approval_user_id': 'int',
        'commit_id': 'str',
        'from_diff_id': 'int',
        'to_diff_id': 'int',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'merge_request_iid': 'merge_request_iid',
        'approval_user_id': 'approval_user_id',
        'commit_id': 'commit_id',
        'from_diff_id': 'from_diff_id',
        'to_diff_id': 'to_diff_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, repository_id=None, merge_request_iid=None, approval_user_id=None, commit_id=None, from_diff_id=None, to_diff_id=None, offset=None, limit=None):
        r"""ListMergeRequestChangesTreesRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param merge_request_iid: **参数解释：**  合并请求 iid。
        :type merge_request_iid: int
        :param approval_user_id: **参数解释：** 审核人ID。
        :type approval_user_id: int
        :param commit_id: **参数解释：** commit ID。 **取值范围：** 字符串长度不少于1，不超过40。
        :type commit_id: str
        :param from_diff_id: **参数解释：** 文件变更对比源版本id
        :type from_diff_id: int
        :param to_diff_id: **参数解释：** 文件变更对比目标版本id
        :type to_diff_id: int
        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        """
        
        

        self._repository_id = None
        self._merge_request_iid = None
        self._approval_user_id = None
        self._commit_id = None
        self._from_diff_id = None
        self._to_diff_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.repository_id = repository_id
        self.merge_request_iid = merge_request_iid
        if approval_user_id is not None:
            self.approval_user_id = approval_user_id
        self.commit_id = commit_id
        if from_diff_id is not None:
            self.from_diff_id = from_diff_id
        if to_diff_id is not None:
            self.to_diff_id = to_diff_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ListMergeRequestChangesTreesRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this ListMergeRequestChangesTreesRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ListMergeRequestChangesTreesRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this ListMergeRequestChangesTreesRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def merge_request_iid(self):
        r"""Gets the merge_request_iid of this ListMergeRequestChangesTreesRequest.

        **参数解释：**  合并请求 iid。

        :return: The merge_request_iid of this ListMergeRequestChangesTreesRequest.
        :rtype: int
        """
        return self._merge_request_iid

    @merge_request_iid.setter
    def merge_request_iid(self, merge_request_iid):
        r"""Sets the merge_request_iid of this ListMergeRequestChangesTreesRequest.

        **参数解释：**  合并请求 iid。

        :param merge_request_iid: The merge_request_iid of this ListMergeRequestChangesTreesRequest.
        :type merge_request_iid: int
        """
        self._merge_request_iid = merge_request_iid

    @property
    def approval_user_id(self):
        r"""Gets the approval_user_id of this ListMergeRequestChangesTreesRequest.

        **参数解释：** 审核人ID。

        :return: The approval_user_id of this ListMergeRequestChangesTreesRequest.
        :rtype: int
        """
        return self._approval_user_id

    @approval_user_id.setter
    def approval_user_id(self, approval_user_id):
        r"""Sets the approval_user_id of this ListMergeRequestChangesTreesRequest.

        **参数解释：** 审核人ID。

        :param approval_user_id: The approval_user_id of this ListMergeRequestChangesTreesRequest.
        :type approval_user_id: int
        """
        self._approval_user_id = approval_user_id

    @property
    def commit_id(self):
        r"""Gets the commit_id of this ListMergeRequestChangesTreesRequest.

        **参数解释：** commit ID。 **取值范围：** 字符串长度不少于1，不超过40。

        :return: The commit_id of this ListMergeRequestChangesTreesRequest.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        r"""Sets the commit_id of this ListMergeRequestChangesTreesRequest.

        **参数解释：** commit ID。 **取值范围：** 字符串长度不少于1，不超过40。

        :param commit_id: The commit_id of this ListMergeRequestChangesTreesRequest.
        :type commit_id: str
        """
        self._commit_id = commit_id

    @property
    def from_diff_id(self):
        r"""Gets the from_diff_id of this ListMergeRequestChangesTreesRequest.

        **参数解释：** 文件变更对比源版本id

        :return: The from_diff_id of this ListMergeRequestChangesTreesRequest.
        :rtype: int
        """
        return self._from_diff_id

    @from_diff_id.setter
    def from_diff_id(self, from_diff_id):
        r"""Sets the from_diff_id of this ListMergeRequestChangesTreesRequest.

        **参数解释：** 文件变更对比源版本id

        :param from_diff_id: The from_diff_id of this ListMergeRequestChangesTreesRequest.
        :type from_diff_id: int
        """
        self._from_diff_id = from_diff_id

    @property
    def to_diff_id(self):
        r"""Gets the to_diff_id of this ListMergeRequestChangesTreesRequest.

        **参数解释：** 文件变更对比目标版本id

        :return: The to_diff_id of this ListMergeRequestChangesTreesRequest.
        :rtype: int
        """
        return self._to_diff_id

    @to_diff_id.setter
    def to_diff_id(self, to_diff_id):
        r"""Sets the to_diff_id of this ListMergeRequestChangesTreesRequest.

        **参数解释：** 文件变更对比目标版本id

        :param to_diff_id: The to_diff_id of this ListMergeRequestChangesTreesRequest.
        :type to_diff_id: int
        """
        self._to_diff_id = to_diff_id

    @property
    def offset(self):
        r"""Gets the offset of this ListMergeRequestChangesTreesRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListMergeRequestChangesTreesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListMergeRequestChangesTreesRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListMergeRequestChangesTreesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListMergeRequestChangesTreesRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListMergeRequestChangesTreesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListMergeRequestChangesTreesRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListMergeRequestChangesTreesRequest.
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
        if not isinstance(other, ListMergeRequestChangesTreesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
