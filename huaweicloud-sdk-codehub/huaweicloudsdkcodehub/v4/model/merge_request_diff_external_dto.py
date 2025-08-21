# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MergeRequestDiffExternalDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'state': 'str',
        'merge_request_id': 'int',
        'created_at': 'str',
        'updated_at': 'str',
        'base_commit_sha': 'str',
        'real_size': 'str',
        'head_commit_sha': 'str',
        'start_commit_sha': 'str',
        'commits_count': 'int',
        'external_diff': 'str',
        'external_diff_store': 'int',
        'stored_externally': 'bool',
        'added_lines': 'int',
        'removed_lines': 'int'
    }

    attribute_map = {
        'id': 'id',
        'state': 'state',
        'merge_request_id': 'merge_request_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'base_commit_sha': 'base_commit_sha',
        'real_size': 'real_size',
        'head_commit_sha': 'head_commit_sha',
        'start_commit_sha': 'start_commit_sha',
        'commits_count': 'commits_count',
        'external_diff': 'external_diff',
        'external_diff_store': 'external_diff_store',
        'stored_externally': 'stored_externally',
        'added_lines': 'added_lines',
        'removed_lines': 'removed_lines'
    }

    def __init__(self, id=None, state=None, merge_request_id=None, created_at=None, updated_at=None, base_commit_sha=None, real_size=None, head_commit_sha=None, start_commit_sha=None, commits_count=None, external_diff=None, external_diff_store=None, stored_externally=None, added_lines=None, removed_lines=None):
        r"""MergeRequestDiffExternalDto

        The model defined in huaweicloud sdk

        :param id: 合并请求diff id
        :type id: int
        :param state: 状态
        :type state: str
        :param merge_request_id: 合并请求id
        :type merge_request_id: int
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        :param base_commit_sha: base commit节点
        :type base_commit_sha: str
        :param real_size: diff文件数量
        :type real_size: str
        :param head_commit_sha: head commit节点
        :type head_commit_sha: str
        :param start_commit_sha: start commit节点
        :type start_commit_sha: str
        :param commits_count: commit数量
        :type commits_count: int
        :param external_diff: 外部diff文件
        :type external_diff: str
        :param external_diff_store: 外部差异存储
        :type external_diff_store: int
        :param stored_externally: 是否外部存储
        :type stored_externally: bool
        :param added_lines: 新增行数
        :type added_lines: int
        :param removed_lines: 删除行数
        :type removed_lines: int
        """
        
        

        self._id = None
        self._state = None
        self._merge_request_id = None
        self._created_at = None
        self._updated_at = None
        self._base_commit_sha = None
        self._real_size = None
        self._head_commit_sha = None
        self._start_commit_sha = None
        self._commits_count = None
        self._external_diff = None
        self._external_diff_store = None
        self._stored_externally = None
        self._added_lines = None
        self._removed_lines = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if state is not None:
            self.state = state
        if merge_request_id is not None:
            self.merge_request_id = merge_request_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if base_commit_sha is not None:
            self.base_commit_sha = base_commit_sha
        if real_size is not None:
            self.real_size = real_size
        if head_commit_sha is not None:
            self.head_commit_sha = head_commit_sha
        if start_commit_sha is not None:
            self.start_commit_sha = start_commit_sha
        if commits_count is not None:
            self.commits_count = commits_count
        if external_diff is not None:
            self.external_diff = external_diff
        if external_diff_store is not None:
            self.external_diff_store = external_diff_store
        if stored_externally is not None:
            self.stored_externally = stored_externally
        if added_lines is not None:
            self.added_lines = added_lines
        if removed_lines is not None:
            self.removed_lines = removed_lines

    @property
    def id(self):
        r"""Gets the id of this MergeRequestDiffExternalDto.

        合并请求diff id

        :return: The id of this MergeRequestDiffExternalDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MergeRequestDiffExternalDto.

        合并请求diff id

        :param id: The id of this MergeRequestDiffExternalDto.
        :type id: int
        """
        self._id = id

    @property
    def state(self):
        r"""Gets the state of this MergeRequestDiffExternalDto.

        状态

        :return: The state of this MergeRequestDiffExternalDto.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this MergeRequestDiffExternalDto.

        状态

        :param state: The state of this MergeRequestDiffExternalDto.
        :type state: str
        """
        self._state = state

    @property
    def merge_request_id(self):
        r"""Gets the merge_request_id of this MergeRequestDiffExternalDto.

        合并请求id

        :return: The merge_request_id of this MergeRequestDiffExternalDto.
        :rtype: int
        """
        return self._merge_request_id

    @merge_request_id.setter
    def merge_request_id(self, merge_request_id):
        r"""Sets the merge_request_id of this MergeRequestDiffExternalDto.

        合并请求id

        :param merge_request_id: The merge_request_id of this MergeRequestDiffExternalDto.
        :type merge_request_id: int
        """
        self._merge_request_id = merge_request_id

    @property
    def created_at(self):
        r"""Gets the created_at of this MergeRequestDiffExternalDto.

        创建时间

        :return: The created_at of this MergeRequestDiffExternalDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this MergeRequestDiffExternalDto.

        创建时间

        :param created_at: The created_at of this MergeRequestDiffExternalDto.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this MergeRequestDiffExternalDto.

        更新时间

        :return: The updated_at of this MergeRequestDiffExternalDto.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this MergeRequestDiffExternalDto.

        更新时间

        :param updated_at: The updated_at of this MergeRequestDiffExternalDto.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def base_commit_sha(self):
        r"""Gets the base_commit_sha of this MergeRequestDiffExternalDto.

        base commit节点

        :return: The base_commit_sha of this MergeRequestDiffExternalDto.
        :rtype: str
        """
        return self._base_commit_sha

    @base_commit_sha.setter
    def base_commit_sha(self, base_commit_sha):
        r"""Sets the base_commit_sha of this MergeRequestDiffExternalDto.

        base commit节点

        :param base_commit_sha: The base_commit_sha of this MergeRequestDiffExternalDto.
        :type base_commit_sha: str
        """
        self._base_commit_sha = base_commit_sha

    @property
    def real_size(self):
        r"""Gets the real_size of this MergeRequestDiffExternalDto.

        diff文件数量

        :return: The real_size of this MergeRequestDiffExternalDto.
        :rtype: str
        """
        return self._real_size

    @real_size.setter
    def real_size(self, real_size):
        r"""Sets the real_size of this MergeRequestDiffExternalDto.

        diff文件数量

        :param real_size: The real_size of this MergeRequestDiffExternalDto.
        :type real_size: str
        """
        self._real_size = real_size

    @property
    def head_commit_sha(self):
        r"""Gets the head_commit_sha of this MergeRequestDiffExternalDto.

        head commit节点

        :return: The head_commit_sha of this MergeRequestDiffExternalDto.
        :rtype: str
        """
        return self._head_commit_sha

    @head_commit_sha.setter
    def head_commit_sha(self, head_commit_sha):
        r"""Sets the head_commit_sha of this MergeRequestDiffExternalDto.

        head commit节点

        :param head_commit_sha: The head_commit_sha of this MergeRequestDiffExternalDto.
        :type head_commit_sha: str
        """
        self._head_commit_sha = head_commit_sha

    @property
    def start_commit_sha(self):
        r"""Gets the start_commit_sha of this MergeRequestDiffExternalDto.

        start commit节点

        :return: The start_commit_sha of this MergeRequestDiffExternalDto.
        :rtype: str
        """
        return self._start_commit_sha

    @start_commit_sha.setter
    def start_commit_sha(self, start_commit_sha):
        r"""Sets the start_commit_sha of this MergeRequestDiffExternalDto.

        start commit节点

        :param start_commit_sha: The start_commit_sha of this MergeRequestDiffExternalDto.
        :type start_commit_sha: str
        """
        self._start_commit_sha = start_commit_sha

    @property
    def commits_count(self):
        r"""Gets the commits_count of this MergeRequestDiffExternalDto.

        commit数量

        :return: The commits_count of this MergeRequestDiffExternalDto.
        :rtype: int
        """
        return self._commits_count

    @commits_count.setter
    def commits_count(self, commits_count):
        r"""Sets the commits_count of this MergeRequestDiffExternalDto.

        commit数量

        :param commits_count: The commits_count of this MergeRequestDiffExternalDto.
        :type commits_count: int
        """
        self._commits_count = commits_count

    @property
    def external_diff(self):
        r"""Gets the external_diff of this MergeRequestDiffExternalDto.

        外部diff文件

        :return: The external_diff of this MergeRequestDiffExternalDto.
        :rtype: str
        """
        return self._external_diff

    @external_diff.setter
    def external_diff(self, external_diff):
        r"""Sets the external_diff of this MergeRequestDiffExternalDto.

        外部diff文件

        :param external_diff: The external_diff of this MergeRequestDiffExternalDto.
        :type external_diff: str
        """
        self._external_diff = external_diff

    @property
    def external_diff_store(self):
        r"""Gets the external_diff_store of this MergeRequestDiffExternalDto.

        外部差异存储

        :return: The external_diff_store of this MergeRequestDiffExternalDto.
        :rtype: int
        """
        return self._external_diff_store

    @external_diff_store.setter
    def external_diff_store(self, external_diff_store):
        r"""Sets the external_diff_store of this MergeRequestDiffExternalDto.

        外部差异存储

        :param external_diff_store: The external_diff_store of this MergeRequestDiffExternalDto.
        :type external_diff_store: int
        """
        self._external_diff_store = external_diff_store

    @property
    def stored_externally(self):
        r"""Gets the stored_externally of this MergeRequestDiffExternalDto.

        是否外部存储

        :return: The stored_externally of this MergeRequestDiffExternalDto.
        :rtype: bool
        """
        return self._stored_externally

    @stored_externally.setter
    def stored_externally(self, stored_externally):
        r"""Sets the stored_externally of this MergeRequestDiffExternalDto.

        是否外部存储

        :param stored_externally: The stored_externally of this MergeRequestDiffExternalDto.
        :type stored_externally: bool
        """
        self._stored_externally = stored_externally

    @property
    def added_lines(self):
        r"""Gets the added_lines of this MergeRequestDiffExternalDto.

        新增行数

        :return: The added_lines of this MergeRequestDiffExternalDto.
        :rtype: int
        """
        return self._added_lines

    @added_lines.setter
    def added_lines(self, added_lines):
        r"""Sets the added_lines of this MergeRequestDiffExternalDto.

        新增行数

        :param added_lines: The added_lines of this MergeRequestDiffExternalDto.
        :type added_lines: int
        """
        self._added_lines = added_lines

    @property
    def removed_lines(self):
        r"""Gets the removed_lines of this MergeRequestDiffExternalDto.

        删除行数

        :return: The removed_lines of this MergeRequestDiffExternalDto.
        :rtype: int
        """
        return self._removed_lines

    @removed_lines.setter
    def removed_lines(self, removed_lines):
        r"""Sets the removed_lines of this MergeRequestDiffExternalDto.

        删除行数

        :param removed_lines: The removed_lines of this MergeRequestDiffExternalDto.
        :type removed_lines: int
        """
        self._removed_lines = removed_lines

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
        if not isinstance(other, MergeRequestDiffExternalDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
