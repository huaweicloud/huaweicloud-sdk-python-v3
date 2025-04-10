# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepositoryStatisticsVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repo_name': 'str',
        'commit_count': 'int',
        'repo_size': 'str',
        'last_commit_time': 'str',
        'code_lines': 'int',
        'branch_count': 'int',
        'archive_url': 'str'
    }

    attribute_map = {
        'repo_name': 'repoName',
        'commit_count': 'commitCount',
        'repo_size': 'repoSize',
        'last_commit_time': 'lastCommitTime',
        'code_lines': 'codeLines',
        'branch_count': 'branchCount',
        'archive_url': 'archiveUrl'
    }

    def __init__(self, repo_name=None, commit_count=None, repo_size=None, last_commit_time=None, code_lines=None, branch_count=None, archive_url=None):
        r"""RepositoryStatisticsVO

        The model defined in huaweicloud sdk

        :param repo_name: 仓库名称
        :type repo_name: str
        :param commit_count: 提交次数
        :type commit_count: int
        :param repo_size: 仓库容量
        :type repo_size: str
        :param last_commit_time: 最近一次提交时间
        :type last_commit_time: str
        :param code_lines: 代码行数
        :type code_lines: int
        :param branch_count: 分支数量
        :type branch_count: int
        :param archive_url: 代码仓下载地址
        :type archive_url: str
        """
        
        

        self._repo_name = None
        self._commit_count = None
        self._repo_size = None
        self._last_commit_time = None
        self._code_lines = None
        self._branch_count = None
        self._archive_url = None
        self.discriminator = None

        if repo_name is not None:
            self.repo_name = repo_name
        if commit_count is not None:
            self.commit_count = commit_count
        if repo_size is not None:
            self.repo_size = repo_size
        if last_commit_time is not None:
            self.last_commit_time = last_commit_time
        if code_lines is not None:
            self.code_lines = code_lines
        if branch_count is not None:
            self.branch_count = branch_count
        if archive_url is not None:
            self.archive_url = archive_url

    @property
    def repo_name(self):
        r"""Gets the repo_name of this RepositoryStatisticsVO.

        仓库名称

        :return: The repo_name of this RepositoryStatisticsVO.
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        r"""Sets the repo_name of this RepositoryStatisticsVO.

        仓库名称

        :param repo_name: The repo_name of this RepositoryStatisticsVO.
        :type repo_name: str
        """
        self._repo_name = repo_name

    @property
    def commit_count(self):
        r"""Gets the commit_count of this RepositoryStatisticsVO.

        提交次数

        :return: The commit_count of this RepositoryStatisticsVO.
        :rtype: int
        """
        return self._commit_count

    @commit_count.setter
    def commit_count(self, commit_count):
        r"""Sets the commit_count of this RepositoryStatisticsVO.

        提交次数

        :param commit_count: The commit_count of this RepositoryStatisticsVO.
        :type commit_count: int
        """
        self._commit_count = commit_count

    @property
    def repo_size(self):
        r"""Gets the repo_size of this RepositoryStatisticsVO.

        仓库容量

        :return: The repo_size of this RepositoryStatisticsVO.
        :rtype: str
        """
        return self._repo_size

    @repo_size.setter
    def repo_size(self, repo_size):
        r"""Sets the repo_size of this RepositoryStatisticsVO.

        仓库容量

        :param repo_size: The repo_size of this RepositoryStatisticsVO.
        :type repo_size: str
        """
        self._repo_size = repo_size

    @property
    def last_commit_time(self):
        r"""Gets the last_commit_time of this RepositoryStatisticsVO.

        最近一次提交时间

        :return: The last_commit_time of this RepositoryStatisticsVO.
        :rtype: str
        """
        return self._last_commit_time

    @last_commit_time.setter
    def last_commit_time(self, last_commit_time):
        r"""Sets the last_commit_time of this RepositoryStatisticsVO.

        最近一次提交时间

        :param last_commit_time: The last_commit_time of this RepositoryStatisticsVO.
        :type last_commit_time: str
        """
        self._last_commit_time = last_commit_time

    @property
    def code_lines(self):
        r"""Gets the code_lines of this RepositoryStatisticsVO.

        代码行数

        :return: The code_lines of this RepositoryStatisticsVO.
        :rtype: int
        """
        return self._code_lines

    @code_lines.setter
    def code_lines(self, code_lines):
        r"""Sets the code_lines of this RepositoryStatisticsVO.

        代码行数

        :param code_lines: The code_lines of this RepositoryStatisticsVO.
        :type code_lines: int
        """
        self._code_lines = code_lines

    @property
    def branch_count(self):
        r"""Gets the branch_count of this RepositoryStatisticsVO.

        分支数量

        :return: The branch_count of this RepositoryStatisticsVO.
        :rtype: int
        """
        return self._branch_count

    @branch_count.setter
    def branch_count(self, branch_count):
        r"""Sets the branch_count of this RepositoryStatisticsVO.

        分支数量

        :param branch_count: The branch_count of this RepositoryStatisticsVO.
        :type branch_count: int
        """
        self._branch_count = branch_count

    @property
    def archive_url(self):
        r"""Gets the archive_url of this RepositoryStatisticsVO.

        代码仓下载地址

        :return: The archive_url of this RepositoryStatisticsVO.
        :rtype: str
        """
        return self._archive_url

    @archive_url.setter
    def archive_url(self, archive_url):
        r"""Sets the archive_url of this RepositoryStatisticsVO.

        代码仓下载地址

        :param archive_url: The archive_url of this RepositoryStatisticsVO.
        :type archive_url: str
        """
        self._archive_url = archive_url

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
        if not isinstance(other, RepositoryStatisticsVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
