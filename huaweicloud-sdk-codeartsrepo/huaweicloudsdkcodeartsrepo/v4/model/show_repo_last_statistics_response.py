# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRepoLastStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event': 'StatisticEventsDto',
        'total': 'int',
        'statistics': 'list[StatisticDto]',
        'codelines': 'list[CodelineDto]',
        'count': 'int',
        'all_branch_commits_count': 'int'
    }

    attribute_map = {
        'event': 'event',
        'total': 'total',
        'statistics': 'statistics',
        'codelines': 'codelines',
        'count': 'count',
        'all_branch_commits_count': 'all_branch_commits_count'
    }

    def __init__(self, event=None, total=None, statistics=None, codelines=None, count=None, all_branch_commits_count=None):
        r"""ShowRepoLastStatisticsResponse

        The model defined in huaweicloud sdk

        :param event: 
        :type event: :class:`huaweicloudsdkcodeartsrepo.v4.StatisticEventsDto`
        :param total: **参数解释：** 统计信息数量 **取值范围：** 最小0 **默认取值：** 0
        :type total: int
        :param statistics: 统计信息
        :type statistics: list[:class:`huaweicloudsdkcodeartsrepo.v4.StatisticDto`]
        :param codelines: 仓库近15日每日代码提交增减行数信息。
        :type codelines: list[:class:`huaweicloudsdkcodeartsrepo.v4.CodelineDto`]
        :param count: **参数解释：** 分支提交总数。 **取值范围：** 最小0 **默认取值：** 0
        :type count: int
        :param all_branch_commits_count: **参数解释：** 仓库提交总数。 **取值范围：** 最小0 **默认取值：** 0
        :type all_branch_commits_count: int
        """
        
        super().__init__()

        self._event = None
        self._total = None
        self._statistics = None
        self._codelines = None
        self._count = None
        self._all_branch_commits_count = None
        self.discriminator = None

        if event is not None:
            self.event = event
        if total is not None:
            self.total = total
        if statistics is not None:
            self.statistics = statistics
        if codelines is not None:
            self.codelines = codelines
        if count is not None:
            self.count = count
        if all_branch_commits_count is not None:
            self.all_branch_commits_count = all_branch_commits_count

    @property
    def event(self):
        r"""Gets the event of this ShowRepoLastStatisticsResponse.

        :return: The event of this ShowRepoLastStatisticsResponse.
        :rtype: :class:`huaweicloudsdkcodeartsrepo.v4.StatisticEventsDto`
        """
        return self._event

    @event.setter
    def event(self, event):
        r"""Sets the event of this ShowRepoLastStatisticsResponse.

        :param event: The event of this ShowRepoLastStatisticsResponse.
        :type event: :class:`huaweicloudsdkcodeartsrepo.v4.StatisticEventsDto`
        """
        self._event = event

    @property
    def total(self):
        r"""Gets the total of this ShowRepoLastStatisticsResponse.

        **参数解释：** 统计信息数量 **取值范围：** 最小0 **默认取值：** 0

        :return: The total of this ShowRepoLastStatisticsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowRepoLastStatisticsResponse.

        **参数解释：** 统计信息数量 **取值范围：** 最小0 **默认取值：** 0

        :param total: The total of this ShowRepoLastStatisticsResponse.
        :type total: int
        """
        self._total = total

    @property
    def statistics(self):
        r"""Gets the statistics of this ShowRepoLastStatisticsResponse.

        统计信息

        :return: The statistics of this ShowRepoLastStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartsrepo.v4.StatisticDto`]
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        r"""Sets the statistics of this ShowRepoLastStatisticsResponse.

        统计信息

        :param statistics: The statistics of this ShowRepoLastStatisticsResponse.
        :type statistics: list[:class:`huaweicloudsdkcodeartsrepo.v4.StatisticDto`]
        """
        self._statistics = statistics

    @property
    def codelines(self):
        r"""Gets the codelines of this ShowRepoLastStatisticsResponse.

        仓库近15日每日代码提交增减行数信息。

        :return: The codelines of this ShowRepoLastStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartsrepo.v4.CodelineDto`]
        """
        return self._codelines

    @codelines.setter
    def codelines(self, codelines):
        r"""Sets the codelines of this ShowRepoLastStatisticsResponse.

        仓库近15日每日代码提交增减行数信息。

        :param codelines: The codelines of this ShowRepoLastStatisticsResponse.
        :type codelines: list[:class:`huaweicloudsdkcodeartsrepo.v4.CodelineDto`]
        """
        self._codelines = codelines

    @property
    def count(self):
        r"""Gets the count of this ShowRepoLastStatisticsResponse.

        **参数解释：** 分支提交总数。 **取值范围：** 最小0 **默认取值：** 0

        :return: The count of this ShowRepoLastStatisticsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowRepoLastStatisticsResponse.

        **参数解释：** 分支提交总数。 **取值范围：** 最小0 **默认取值：** 0

        :param count: The count of this ShowRepoLastStatisticsResponse.
        :type count: int
        """
        self._count = count

    @property
    def all_branch_commits_count(self):
        r"""Gets the all_branch_commits_count of this ShowRepoLastStatisticsResponse.

        **参数解释：** 仓库提交总数。 **取值范围：** 最小0 **默认取值：** 0

        :return: The all_branch_commits_count of this ShowRepoLastStatisticsResponse.
        :rtype: int
        """
        return self._all_branch_commits_count

    @all_branch_commits_count.setter
    def all_branch_commits_count(self, all_branch_commits_count):
        r"""Sets the all_branch_commits_count of this ShowRepoLastStatisticsResponse.

        **参数解释：** 仓库提交总数。 **取值范围：** 最小0 **默认取值：** 0

        :param all_branch_commits_count: The all_branch_commits_count of this ShowRepoLastStatisticsResponse.
        :type all_branch_commits_count: int
        """
        self._all_branch_commits_count = all_branch_commits_count

    def to_dict(self):
        import warnings
        warnings.warn("ShowRepoLastStatisticsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowRepoLastStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
