# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRefCompareResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'commit': 'CommitDto',
        'commits': 'list[CommitDto]',
        'diffs': 'list[DiffDto]',
        'diffs_files': 'list[DiffDto]',
        'compare_timeout': 'bool',
        'compare_same_ref': 'bool',
        'conflict_files': 'list[ConflictFileDto]',
        'added_lines': 'int',
        'removed_lines': 'int',
        'commits_count': 'int',
        'diffs_count': 'int',
        'x_total': 'str'
    }

    attribute_map = {
        'commit': 'commit',
        'commits': 'commits',
        'diffs': 'diffs',
        'diffs_files': 'diffs_files',
        'compare_timeout': 'compare_timeout',
        'compare_same_ref': 'compare_same_ref',
        'conflict_files': 'conflict_files',
        'added_lines': 'added_lines',
        'removed_lines': 'removed_lines',
        'commits_count': 'commits_count',
        'diffs_count': 'diffs_count',
        'x_total': 'X-Total'
    }

    def __init__(self, commit=None, commits=None, diffs=None, diffs_files=None, compare_timeout=None, compare_same_ref=None, conflict_files=None, added_lines=None, removed_lines=None, commits_count=None, diffs_count=None, x_total=None):
        r"""ShowRefCompareResponse

        The model defined in huaweicloud sdk

        :param commit: 
        :type commit: :class:`huaweicloudsdkcodehub.v4.CommitDto`
        :param commits: commit相关信息列表
        :type commits: list[:class:`huaweicloudsdkcodehub.v4.CommitDto`]
        :param diffs: 变更文件信息
        :type diffs: list[:class:`huaweicloudsdkcodehub.v4.DiffDto`]
        :param diffs_files: 变更文件信息
        :type diffs_files: list[:class:`huaweicloudsdkcodehub.v4.DiffDto`]
        :param compare_timeout: 是否超时
        :type compare_timeout: bool
        :param compare_same_ref: 是否相同
        :type compare_same_ref: bool
        :param conflict_files: 冲突文件
        :type conflict_files: list[:class:`huaweicloudsdkcodehub.v4.ConflictFileDto`]
        :param added_lines: 增加行数
        :type added_lines: int
        :param removed_lines: 删除行数
        :type removed_lines: int
        :param commits_count: 提交数量
        :type commits_count: int
        :param diffs_count: 文件变更数量
        :type diffs_count: int
        :param x_total: 
        :type x_total: str
        """
        
        super(ShowRefCompareResponse, self).__init__()

        self._commit = None
        self._commits = None
        self._diffs = None
        self._diffs_files = None
        self._compare_timeout = None
        self._compare_same_ref = None
        self._conflict_files = None
        self._added_lines = None
        self._removed_lines = None
        self._commits_count = None
        self._diffs_count = None
        self._x_total = None
        self.discriminator = None

        if commit is not None:
            self.commit = commit
        if commits is not None:
            self.commits = commits
        if diffs is not None:
            self.diffs = diffs
        if diffs_files is not None:
            self.diffs_files = diffs_files
        if compare_timeout is not None:
            self.compare_timeout = compare_timeout
        if compare_same_ref is not None:
            self.compare_same_ref = compare_same_ref
        if conflict_files is not None:
            self.conflict_files = conflict_files
        if added_lines is not None:
            self.added_lines = added_lines
        if removed_lines is not None:
            self.removed_lines = removed_lines
        if commits_count is not None:
            self.commits_count = commits_count
        if diffs_count is not None:
            self.diffs_count = diffs_count
        if x_total is not None:
            self.x_total = x_total

    @property
    def commit(self):
        r"""Gets the commit of this ShowRefCompareResponse.

        :return: The commit of this ShowRefCompareResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.CommitDto`
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        r"""Sets the commit of this ShowRefCompareResponse.

        :param commit: The commit of this ShowRefCompareResponse.
        :type commit: :class:`huaweicloudsdkcodehub.v4.CommitDto`
        """
        self._commit = commit

    @property
    def commits(self):
        r"""Gets the commits of this ShowRefCompareResponse.

        commit相关信息列表

        :return: The commits of this ShowRefCompareResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.CommitDto`]
        """
        return self._commits

    @commits.setter
    def commits(self, commits):
        r"""Sets the commits of this ShowRefCompareResponse.

        commit相关信息列表

        :param commits: The commits of this ShowRefCompareResponse.
        :type commits: list[:class:`huaweicloudsdkcodehub.v4.CommitDto`]
        """
        self._commits = commits

    @property
    def diffs(self):
        r"""Gets the diffs of this ShowRefCompareResponse.

        变更文件信息

        :return: The diffs of this ShowRefCompareResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.DiffDto`]
        """
        return self._diffs

    @diffs.setter
    def diffs(self, diffs):
        r"""Sets the diffs of this ShowRefCompareResponse.

        变更文件信息

        :param diffs: The diffs of this ShowRefCompareResponse.
        :type diffs: list[:class:`huaweicloudsdkcodehub.v4.DiffDto`]
        """
        self._diffs = diffs

    @property
    def diffs_files(self):
        r"""Gets the diffs_files of this ShowRefCompareResponse.

        变更文件信息

        :return: The diffs_files of this ShowRefCompareResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.DiffDto`]
        """
        return self._diffs_files

    @diffs_files.setter
    def diffs_files(self, diffs_files):
        r"""Sets the diffs_files of this ShowRefCompareResponse.

        变更文件信息

        :param diffs_files: The diffs_files of this ShowRefCompareResponse.
        :type diffs_files: list[:class:`huaweicloudsdkcodehub.v4.DiffDto`]
        """
        self._diffs_files = diffs_files

    @property
    def compare_timeout(self):
        r"""Gets the compare_timeout of this ShowRefCompareResponse.

        是否超时

        :return: The compare_timeout of this ShowRefCompareResponse.
        :rtype: bool
        """
        return self._compare_timeout

    @compare_timeout.setter
    def compare_timeout(self, compare_timeout):
        r"""Sets the compare_timeout of this ShowRefCompareResponse.

        是否超时

        :param compare_timeout: The compare_timeout of this ShowRefCompareResponse.
        :type compare_timeout: bool
        """
        self._compare_timeout = compare_timeout

    @property
    def compare_same_ref(self):
        r"""Gets the compare_same_ref of this ShowRefCompareResponse.

        是否相同

        :return: The compare_same_ref of this ShowRefCompareResponse.
        :rtype: bool
        """
        return self._compare_same_ref

    @compare_same_ref.setter
    def compare_same_ref(self, compare_same_ref):
        r"""Sets the compare_same_ref of this ShowRefCompareResponse.

        是否相同

        :param compare_same_ref: The compare_same_ref of this ShowRefCompareResponse.
        :type compare_same_ref: bool
        """
        self._compare_same_ref = compare_same_ref

    @property
    def conflict_files(self):
        r"""Gets the conflict_files of this ShowRefCompareResponse.

        冲突文件

        :return: The conflict_files of this ShowRefCompareResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.ConflictFileDto`]
        """
        return self._conflict_files

    @conflict_files.setter
    def conflict_files(self, conflict_files):
        r"""Sets the conflict_files of this ShowRefCompareResponse.

        冲突文件

        :param conflict_files: The conflict_files of this ShowRefCompareResponse.
        :type conflict_files: list[:class:`huaweicloudsdkcodehub.v4.ConflictFileDto`]
        """
        self._conflict_files = conflict_files

    @property
    def added_lines(self):
        r"""Gets the added_lines of this ShowRefCompareResponse.

        增加行数

        :return: The added_lines of this ShowRefCompareResponse.
        :rtype: int
        """
        return self._added_lines

    @added_lines.setter
    def added_lines(self, added_lines):
        r"""Sets the added_lines of this ShowRefCompareResponse.

        增加行数

        :param added_lines: The added_lines of this ShowRefCompareResponse.
        :type added_lines: int
        """
        self._added_lines = added_lines

    @property
    def removed_lines(self):
        r"""Gets the removed_lines of this ShowRefCompareResponse.

        删除行数

        :return: The removed_lines of this ShowRefCompareResponse.
        :rtype: int
        """
        return self._removed_lines

    @removed_lines.setter
    def removed_lines(self, removed_lines):
        r"""Sets the removed_lines of this ShowRefCompareResponse.

        删除行数

        :param removed_lines: The removed_lines of this ShowRefCompareResponse.
        :type removed_lines: int
        """
        self._removed_lines = removed_lines

    @property
    def commits_count(self):
        r"""Gets the commits_count of this ShowRefCompareResponse.

        提交数量

        :return: The commits_count of this ShowRefCompareResponse.
        :rtype: int
        """
        return self._commits_count

    @commits_count.setter
    def commits_count(self, commits_count):
        r"""Sets the commits_count of this ShowRefCompareResponse.

        提交数量

        :param commits_count: The commits_count of this ShowRefCompareResponse.
        :type commits_count: int
        """
        self._commits_count = commits_count

    @property
    def diffs_count(self):
        r"""Gets the diffs_count of this ShowRefCompareResponse.

        文件变更数量

        :return: The diffs_count of this ShowRefCompareResponse.
        :rtype: int
        """
        return self._diffs_count

    @diffs_count.setter
    def diffs_count(self, diffs_count):
        r"""Sets the diffs_count of this ShowRefCompareResponse.

        文件变更数量

        :param diffs_count: The diffs_count of this ShowRefCompareResponse.
        :type diffs_count: int
        """
        self._diffs_count = diffs_count

    @property
    def x_total(self):
        r"""Gets the x_total of this ShowRefCompareResponse.

        :return: The x_total of this ShowRefCompareResponse.
        :rtype: str
        """
        return self._x_total

    @x_total.setter
    def x_total(self, x_total):
        r"""Sets the x_total of this ShowRefCompareResponse.

        :param x_total: The x_total of this ShowRefCompareResponse.
        :type x_total: str
        """
        self._x_total = x_total

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
        if not isinstance(other, ShowRefCompareResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
