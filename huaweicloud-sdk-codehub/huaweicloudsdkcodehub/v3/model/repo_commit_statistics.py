# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepoCommitStatistics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'all_branch_commits_count': 'int',
        'codelines': 'list[RepoDailyCodeline]',
        'count': 'int',
        'event': 'RepoStatisticsEvent',
        'statistics': 'list[RepoStatistics]',
        'total': 'int'
    }

    attribute_map = {
        'all_branch_commits_count': 'all_branch_commits_count',
        'codelines': 'codelines',
        'count': 'count',
        'event': 'event',
        'statistics': 'statistics',
        'total': 'total'
    }

    def __init__(self, all_branch_commits_count=None, codelines=None, count=None, event=None, statistics=None, total=None):
        """RepoCommitStatistics

        The model defined in huaweicloud sdk

        :param all_branch_commits_count: 仓库总提交次数
        :type all_branch_commits_count: int
        :param codelines: 近15日每日代码提交行数
        :type codelines: list[:class:`huaweicloudsdkcodehub.v3.RepoDailyCodeline`]
        :param count: 对应分支仓库总提交次数
        :type count: int
        :param event: 
        :type event: :class:`huaweicloudsdkcodehub.v3.RepoStatisticsEvent`
        :param statistics: 仓库统计列表
        :type statistics: list[:class:`huaweicloudsdkcodehub.v3.RepoStatistics`]
        :param total: 仓库统计次数
        :type total: int
        """
        
        

        self._all_branch_commits_count = None
        self._codelines = None
        self._count = None
        self._event = None
        self._statistics = None
        self._total = None
        self.discriminator = None

        if all_branch_commits_count is not None:
            self.all_branch_commits_count = all_branch_commits_count
        if codelines is not None:
            self.codelines = codelines
        if count is not None:
            self.count = count
        if event is not None:
            self.event = event
        if statistics is not None:
            self.statistics = statistics
        if total is not None:
            self.total = total

    @property
    def all_branch_commits_count(self):
        """Gets the all_branch_commits_count of this RepoCommitStatistics.

        仓库总提交次数

        :return: The all_branch_commits_count of this RepoCommitStatistics.
        :rtype: int
        """
        return self._all_branch_commits_count

    @all_branch_commits_count.setter
    def all_branch_commits_count(self, all_branch_commits_count):
        """Sets the all_branch_commits_count of this RepoCommitStatistics.

        仓库总提交次数

        :param all_branch_commits_count: The all_branch_commits_count of this RepoCommitStatistics.
        :type all_branch_commits_count: int
        """
        self._all_branch_commits_count = all_branch_commits_count

    @property
    def codelines(self):
        """Gets the codelines of this RepoCommitStatistics.

        近15日每日代码提交行数

        :return: The codelines of this RepoCommitStatistics.
        :rtype: list[:class:`huaweicloudsdkcodehub.v3.RepoDailyCodeline`]
        """
        return self._codelines

    @codelines.setter
    def codelines(self, codelines):
        """Sets the codelines of this RepoCommitStatistics.

        近15日每日代码提交行数

        :param codelines: The codelines of this RepoCommitStatistics.
        :type codelines: list[:class:`huaweicloudsdkcodehub.v3.RepoDailyCodeline`]
        """
        self._codelines = codelines

    @property
    def count(self):
        """Gets the count of this RepoCommitStatistics.

        对应分支仓库总提交次数

        :return: The count of this RepoCommitStatistics.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this RepoCommitStatistics.

        对应分支仓库总提交次数

        :param count: The count of this RepoCommitStatistics.
        :type count: int
        """
        self._count = count

    @property
    def event(self):
        """Gets the event of this RepoCommitStatistics.

        :return: The event of this RepoCommitStatistics.
        :rtype: :class:`huaweicloudsdkcodehub.v3.RepoStatisticsEvent`
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this RepoCommitStatistics.

        :param event: The event of this RepoCommitStatistics.
        :type event: :class:`huaweicloudsdkcodehub.v3.RepoStatisticsEvent`
        """
        self._event = event

    @property
    def statistics(self):
        """Gets the statistics of this RepoCommitStatistics.

        仓库统计列表

        :return: The statistics of this RepoCommitStatistics.
        :rtype: list[:class:`huaweicloudsdkcodehub.v3.RepoStatistics`]
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """Sets the statistics of this RepoCommitStatistics.

        仓库统计列表

        :param statistics: The statistics of this RepoCommitStatistics.
        :type statistics: list[:class:`huaweicloudsdkcodehub.v3.RepoStatistics`]
        """
        self._statistics = statistics

    @property
    def total(self):
        """Gets the total of this RepoCommitStatistics.

        仓库统计次数

        :return: The total of this RepoCommitStatistics.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this RepoCommitStatistics.

        仓库统计次数

        :param total: The total of this RepoCommitStatistics.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, RepoCommitStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
