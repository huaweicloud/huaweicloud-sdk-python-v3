# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRepositoryStatisticalDataV2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'commit_number': 'int',
        'git_repo_cap': 'str',
        'last_commit_time': 'str',
        'code_lines': 'int',
        'branch_number': 'int',
        'detail_url': 'str',
        'download_url': 'str'
    }

    attribute_map = {
        'name': 'name',
        'commit_number': 'commit_number',
        'git_repo_cap': 'git_repo_cap',
        'last_commit_time': 'last_commit_time',
        'code_lines': 'code_lines',
        'branch_number': 'branch_number',
        'detail_url': 'detail_url',
        'download_url': 'download_url'
    }

    def __init__(self, name=None, commit_number=None, git_repo_cap=None, last_commit_time=None, code_lines=None, branch_number=None, detail_url=None, download_url=None):
        r"""ShowRepositoryStatisticalDataV2Response

        The model defined in huaweicloud sdk

        :param name: 代码仓的名称
        :type name: str
        :param commit_number: 提交数量
        :type commit_number: int
        :param git_repo_cap: Git库容量
        :type git_repo_cap: str
        :param last_commit_time: 近一次提交时间
        :type last_commit_time: str
        :param code_lines: 代码行数
        :type code_lines: int
        :param branch_number: 分支数量
        :type branch_number: int
        :param detail_url: 代码仓路径url
        :type detail_url: str
        :param download_url: 代码仓下载url
        :type download_url: str
        """
        
        super(ShowRepositoryStatisticalDataV2Response, self).__init__()

        self._name = None
        self._commit_number = None
        self._git_repo_cap = None
        self._last_commit_time = None
        self._code_lines = None
        self._branch_number = None
        self._detail_url = None
        self._download_url = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if commit_number is not None:
            self.commit_number = commit_number
        if git_repo_cap is not None:
            self.git_repo_cap = git_repo_cap
        if last_commit_time is not None:
            self.last_commit_time = last_commit_time
        if code_lines is not None:
            self.code_lines = code_lines
        if branch_number is not None:
            self.branch_number = branch_number
        if detail_url is not None:
            self.detail_url = detail_url
        if download_url is not None:
            self.download_url = download_url

    @property
    def name(self):
        r"""Gets the name of this ShowRepositoryStatisticalDataV2Response.

        代码仓的名称

        :return: The name of this ShowRepositoryStatisticalDataV2Response.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowRepositoryStatisticalDataV2Response.

        代码仓的名称

        :param name: The name of this ShowRepositoryStatisticalDataV2Response.
        :type name: str
        """
        self._name = name

    @property
    def commit_number(self):
        r"""Gets the commit_number of this ShowRepositoryStatisticalDataV2Response.

        提交数量

        :return: The commit_number of this ShowRepositoryStatisticalDataV2Response.
        :rtype: int
        """
        return self._commit_number

    @commit_number.setter
    def commit_number(self, commit_number):
        r"""Sets the commit_number of this ShowRepositoryStatisticalDataV2Response.

        提交数量

        :param commit_number: The commit_number of this ShowRepositoryStatisticalDataV2Response.
        :type commit_number: int
        """
        self._commit_number = commit_number

    @property
    def git_repo_cap(self):
        r"""Gets the git_repo_cap of this ShowRepositoryStatisticalDataV2Response.

        Git库容量

        :return: The git_repo_cap of this ShowRepositoryStatisticalDataV2Response.
        :rtype: str
        """
        return self._git_repo_cap

    @git_repo_cap.setter
    def git_repo_cap(self, git_repo_cap):
        r"""Sets the git_repo_cap of this ShowRepositoryStatisticalDataV2Response.

        Git库容量

        :param git_repo_cap: The git_repo_cap of this ShowRepositoryStatisticalDataV2Response.
        :type git_repo_cap: str
        """
        self._git_repo_cap = git_repo_cap

    @property
    def last_commit_time(self):
        r"""Gets the last_commit_time of this ShowRepositoryStatisticalDataV2Response.

        近一次提交时间

        :return: The last_commit_time of this ShowRepositoryStatisticalDataV2Response.
        :rtype: str
        """
        return self._last_commit_time

    @last_commit_time.setter
    def last_commit_time(self, last_commit_time):
        r"""Sets the last_commit_time of this ShowRepositoryStatisticalDataV2Response.

        近一次提交时间

        :param last_commit_time: The last_commit_time of this ShowRepositoryStatisticalDataV2Response.
        :type last_commit_time: str
        """
        self._last_commit_time = last_commit_time

    @property
    def code_lines(self):
        r"""Gets the code_lines of this ShowRepositoryStatisticalDataV2Response.

        代码行数

        :return: The code_lines of this ShowRepositoryStatisticalDataV2Response.
        :rtype: int
        """
        return self._code_lines

    @code_lines.setter
    def code_lines(self, code_lines):
        r"""Sets the code_lines of this ShowRepositoryStatisticalDataV2Response.

        代码行数

        :param code_lines: The code_lines of this ShowRepositoryStatisticalDataV2Response.
        :type code_lines: int
        """
        self._code_lines = code_lines

    @property
    def branch_number(self):
        r"""Gets the branch_number of this ShowRepositoryStatisticalDataV2Response.

        分支数量

        :return: The branch_number of this ShowRepositoryStatisticalDataV2Response.
        :rtype: int
        """
        return self._branch_number

    @branch_number.setter
    def branch_number(self, branch_number):
        r"""Sets the branch_number of this ShowRepositoryStatisticalDataV2Response.

        分支数量

        :param branch_number: The branch_number of this ShowRepositoryStatisticalDataV2Response.
        :type branch_number: int
        """
        self._branch_number = branch_number

    @property
    def detail_url(self):
        r"""Gets the detail_url of this ShowRepositoryStatisticalDataV2Response.

        代码仓路径url

        :return: The detail_url of this ShowRepositoryStatisticalDataV2Response.
        :rtype: str
        """
        return self._detail_url

    @detail_url.setter
    def detail_url(self, detail_url):
        r"""Sets the detail_url of this ShowRepositoryStatisticalDataV2Response.

        代码仓路径url

        :param detail_url: The detail_url of this ShowRepositoryStatisticalDataV2Response.
        :type detail_url: str
        """
        self._detail_url = detail_url

    @property
    def download_url(self):
        r"""Gets the download_url of this ShowRepositoryStatisticalDataV2Response.

        代码仓下载url

        :return: The download_url of this ShowRepositoryStatisticalDataV2Response.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        r"""Sets the download_url of this ShowRepositoryStatisticalDataV2Response.

        代码仓下载url

        :param download_url: The download_url of this ShowRepositoryStatisticalDataV2Response.
        :type download_url: str
        """
        self._download_url = download_url

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
        if not isinstance(other, ShowRepositoryStatisticalDataV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
