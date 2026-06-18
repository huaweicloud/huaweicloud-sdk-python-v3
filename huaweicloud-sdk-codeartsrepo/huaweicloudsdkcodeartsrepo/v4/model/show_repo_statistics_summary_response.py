# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRepoStatisticsSummaryResponse(SdkResponse):

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
        'branch_count': 'int'
    }

    attribute_map = {
        'repo_name': 'repo_name',
        'commit_count': 'commit_count',
        'repo_size': 'repo_size',
        'last_commit_time': 'last_commit_time',
        'code_lines': 'code_lines',
        'branch_count': 'branch_count'
    }

    def __init__(self, repo_name=None, commit_count=None, repo_size=None, last_commit_time=None, code_lines=None, branch_count=None):
        r"""ShowRepoStatisticsSummaryResponse

        The model defined in huaweicloud sdk

        :param repo_name: **参数解释：** 仓库名称。 **取值范围：** 最小1个字节，最大200字节 **默认取值：** 不涉及。
        :type repo_name: str
        :param commit_count: **参数解释：** 默认分支的提交数量。 **取值范围：** 最小0 **默认取值：** 0
        :type commit_count: int
        :param repo_size: **参数解释：** 仓库占用磁盘空间大小。 **取值范围：** 最小0 **默认取值：** 0
        :type repo_size: str
        :param last_commit_time: **参数解释：** 仓库最新的提交日期，格式yyyy-MM-dd&#39;T&#39;HH:mm:ssXXX,例：2025-10-30T08:27:43.000Z **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type last_commit_time: str
        :param code_lines: **参数解释：** 默认分支的代码行数。 **取值范围：** 最小0 **默认取值：** 0。
        :type code_lines: int
        :param branch_count: **参数解释：** 仓库分支数量 **取值范围：** 最小0 **默认取值：** 0
        :type branch_count: int
        """
        
        super().__init__()

        self._repo_name = None
        self._commit_count = None
        self._repo_size = None
        self._last_commit_time = None
        self._code_lines = None
        self._branch_count = None
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

    @property
    def repo_name(self):
        r"""Gets the repo_name of this ShowRepoStatisticsSummaryResponse.

        **参数解释：** 仓库名称。 **取值范围：** 最小1个字节，最大200字节 **默认取值：** 不涉及。

        :return: The repo_name of this ShowRepoStatisticsSummaryResponse.
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        r"""Sets the repo_name of this ShowRepoStatisticsSummaryResponse.

        **参数解释：** 仓库名称。 **取值范围：** 最小1个字节，最大200字节 **默认取值：** 不涉及。

        :param repo_name: The repo_name of this ShowRepoStatisticsSummaryResponse.
        :type repo_name: str
        """
        self._repo_name = repo_name

    @property
    def commit_count(self):
        r"""Gets the commit_count of this ShowRepoStatisticsSummaryResponse.

        **参数解释：** 默认分支的提交数量。 **取值范围：** 最小0 **默认取值：** 0

        :return: The commit_count of this ShowRepoStatisticsSummaryResponse.
        :rtype: int
        """
        return self._commit_count

    @commit_count.setter
    def commit_count(self, commit_count):
        r"""Sets the commit_count of this ShowRepoStatisticsSummaryResponse.

        **参数解释：** 默认分支的提交数量。 **取值范围：** 最小0 **默认取值：** 0

        :param commit_count: The commit_count of this ShowRepoStatisticsSummaryResponse.
        :type commit_count: int
        """
        self._commit_count = commit_count

    @property
    def repo_size(self):
        r"""Gets the repo_size of this ShowRepoStatisticsSummaryResponse.

        **参数解释：** 仓库占用磁盘空间大小。 **取值范围：** 最小0 **默认取值：** 0

        :return: The repo_size of this ShowRepoStatisticsSummaryResponse.
        :rtype: str
        """
        return self._repo_size

    @repo_size.setter
    def repo_size(self, repo_size):
        r"""Sets the repo_size of this ShowRepoStatisticsSummaryResponse.

        **参数解释：** 仓库占用磁盘空间大小。 **取值范围：** 最小0 **默认取值：** 0

        :param repo_size: The repo_size of this ShowRepoStatisticsSummaryResponse.
        :type repo_size: str
        """
        self._repo_size = repo_size

    @property
    def last_commit_time(self):
        r"""Gets the last_commit_time of this ShowRepoStatisticsSummaryResponse.

        **参数解释：** 仓库最新的提交日期，格式yyyy-MM-dd'T'HH:mm:ssXXX,例：2025-10-30T08:27:43.000Z **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The last_commit_time of this ShowRepoStatisticsSummaryResponse.
        :rtype: str
        """
        return self._last_commit_time

    @last_commit_time.setter
    def last_commit_time(self, last_commit_time):
        r"""Sets the last_commit_time of this ShowRepoStatisticsSummaryResponse.

        **参数解释：** 仓库最新的提交日期，格式yyyy-MM-dd'T'HH:mm:ssXXX,例：2025-10-30T08:27:43.000Z **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param last_commit_time: The last_commit_time of this ShowRepoStatisticsSummaryResponse.
        :type last_commit_time: str
        """
        self._last_commit_time = last_commit_time

    @property
    def code_lines(self):
        r"""Gets the code_lines of this ShowRepoStatisticsSummaryResponse.

        **参数解释：** 默认分支的代码行数。 **取值范围：** 最小0 **默认取值：** 0。

        :return: The code_lines of this ShowRepoStatisticsSummaryResponse.
        :rtype: int
        """
        return self._code_lines

    @code_lines.setter
    def code_lines(self, code_lines):
        r"""Sets the code_lines of this ShowRepoStatisticsSummaryResponse.

        **参数解释：** 默认分支的代码行数。 **取值范围：** 最小0 **默认取值：** 0。

        :param code_lines: The code_lines of this ShowRepoStatisticsSummaryResponse.
        :type code_lines: int
        """
        self._code_lines = code_lines

    @property
    def branch_count(self):
        r"""Gets the branch_count of this ShowRepoStatisticsSummaryResponse.

        **参数解释：** 仓库分支数量 **取值范围：** 最小0 **默认取值：** 0

        :return: The branch_count of this ShowRepoStatisticsSummaryResponse.
        :rtype: int
        """
        return self._branch_count

    @branch_count.setter
    def branch_count(self, branch_count):
        r"""Sets the branch_count of this ShowRepoStatisticsSummaryResponse.

        **参数解释：** 仓库分支数量 **取值范围：** 最小0 **默认取值：** 0

        :param branch_count: The branch_count of this ShowRepoStatisticsSummaryResponse.
        :type branch_count: int
        """
        self._branch_count = branch_count

    def to_dict(self):
        import warnings
        warnings.warn("ShowRepoStatisticsSummaryResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowRepoStatisticsSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
