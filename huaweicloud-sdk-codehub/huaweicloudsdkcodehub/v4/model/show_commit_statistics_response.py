# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCommitStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'commits': 'list[CommitStatisticsResultCommitDto]',
        'statistics': 'list[StatisticDto]',
        'total': 'int',
        'x_total': 'str'
    }

    attribute_map = {
        'commits': 'commits',
        'statistics': 'statistics',
        'total': 'total',
        'x_total': 'X-Total'
    }

    def __init__(self, commits=None, statistics=None, total=None, x_total=None):
        r"""ShowCommitStatisticsResponse

        The model defined in huaweicloud sdk

        :param commits: **参数解释：** 提交统计。
        :type commits: list[:class:`huaweicloudsdkcodehub.v4.CommitStatisticsResultCommitDto`]
        :param statistics: **参数解释：** 提交人员统计。
        :type statistics: list[:class:`huaweicloudsdkcodehub.v4.StatisticDto`]
        :param total: **参数解释：** 总数。
        :type total: int
        :param x_total: 
        :type x_total: str
        """
        
        super(ShowCommitStatisticsResponse, self).__init__()

        self._commits = None
        self._statistics = None
        self._total = None
        self._x_total = None
        self.discriminator = None

        if commits is not None:
            self.commits = commits
        if statistics is not None:
            self.statistics = statistics
        if total is not None:
            self.total = total
        if x_total is not None:
            self.x_total = x_total

    @property
    def commits(self):
        r"""Gets the commits of this ShowCommitStatisticsResponse.

        **参数解释：** 提交统计。

        :return: The commits of this ShowCommitStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.CommitStatisticsResultCommitDto`]
        """
        return self._commits

    @commits.setter
    def commits(self, commits):
        r"""Sets the commits of this ShowCommitStatisticsResponse.

        **参数解释：** 提交统计。

        :param commits: The commits of this ShowCommitStatisticsResponse.
        :type commits: list[:class:`huaweicloudsdkcodehub.v4.CommitStatisticsResultCommitDto`]
        """
        self._commits = commits

    @property
    def statistics(self):
        r"""Gets the statistics of this ShowCommitStatisticsResponse.

        **参数解释：** 提交人员统计。

        :return: The statistics of this ShowCommitStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.StatisticDto`]
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        r"""Sets the statistics of this ShowCommitStatisticsResponse.

        **参数解释：** 提交人员统计。

        :param statistics: The statistics of this ShowCommitStatisticsResponse.
        :type statistics: list[:class:`huaweicloudsdkcodehub.v4.StatisticDto`]
        """
        self._statistics = statistics

    @property
    def total(self):
        r"""Gets the total of this ShowCommitStatisticsResponse.

        **参数解释：** 总数。

        :return: The total of this ShowCommitStatisticsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowCommitStatisticsResponse.

        **参数解释：** 总数。

        :param total: The total of this ShowCommitStatisticsResponse.
        :type total: int
        """
        self._total = total

    @property
    def x_total(self):
        r"""Gets the x_total of this ShowCommitStatisticsResponse.

        :return: The x_total of this ShowCommitStatisticsResponse.
        :rtype: str
        """
        return self._x_total

    @x_total.setter
    def x_total(self, x_total):
        r"""Sets the x_total of this ShowCommitStatisticsResponse.

        :param x_total: The x_total of this ShowCommitStatisticsResponse.
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
        if not isinstance(other, ShowCommitStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
