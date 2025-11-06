# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetResourceCopySummaryResponseSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'statistic_date': 'str',
        'total_copy_counts': 'int',
        'completed_copy_counts': 'int',
        'failed_copy_counts': 'int'
    }

    attribute_map = {
        'statistic_date': 'statistic_date',
        'total_copy_counts': 'total_copy_counts',
        'completed_copy_counts': 'completed_copy_counts',
        'failed_copy_counts': 'failed_copy_counts'
    }

    def __init__(self, statistic_date=None, total_copy_counts=None, completed_copy_counts=None, failed_copy_counts=None):
        r"""GetResourceCopySummaryResponseSummary

        The model defined in huaweicloud sdk

        :param statistic_date: 统计日期
        :type statistic_date: str
        :param total_copy_counts: 当前统计日期内的备份总数
        :type total_copy_counts: int
        :param completed_copy_counts: 当前统计日期内的完成备份总数, key -&gt; ResourceCopyStatisticsKeyEnum.COMPLETED.getValue()
        :type completed_copy_counts: int
        :param failed_copy_counts: 当前统计日期内的失败备份总数, key -&gt; ResourceCopyStatisticsKeyEnum.FAILED.getValue()
        :type failed_copy_counts: int
        """
        
        

        self._statistic_date = None
        self._total_copy_counts = None
        self._completed_copy_counts = None
        self._failed_copy_counts = None
        self.discriminator = None

        if statistic_date is not None:
            self.statistic_date = statistic_date
        if total_copy_counts is not None:
            self.total_copy_counts = total_copy_counts
        if completed_copy_counts is not None:
            self.completed_copy_counts = completed_copy_counts
        if failed_copy_counts is not None:
            self.failed_copy_counts = failed_copy_counts

    @property
    def statistic_date(self):
        r"""Gets the statistic_date of this GetResourceCopySummaryResponseSummary.

        统计日期

        :return: The statistic_date of this GetResourceCopySummaryResponseSummary.
        :rtype: str
        """
        return self._statistic_date

    @statistic_date.setter
    def statistic_date(self, statistic_date):
        r"""Sets the statistic_date of this GetResourceCopySummaryResponseSummary.

        统计日期

        :param statistic_date: The statistic_date of this GetResourceCopySummaryResponseSummary.
        :type statistic_date: str
        """
        self._statistic_date = statistic_date

    @property
    def total_copy_counts(self):
        r"""Gets the total_copy_counts of this GetResourceCopySummaryResponseSummary.

        当前统计日期内的备份总数

        :return: The total_copy_counts of this GetResourceCopySummaryResponseSummary.
        :rtype: int
        """
        return self._total_copy_counts

    @total_copy_counts.setter
    def total_copy_counts(self, total_copy_counts):
        r"""Sets the total_copy_counts of this GetResourceCopySummaryResponseSummary.

        当前统计日期内的备份总数

        :param total_copy_counts: The total_copy_counts of this GetResourceCopySummaryResponseSummary.
        :type total_copy_counts: int
        """
        self._total_copy_counts = total_copy_counts

    @property
    def completed_copy_counts(self):
        r"""Gets the completed_copy_counts of this GetResourceCopySummaryResponseSummary.

        当前统计日期内的完成备份总数, key -> ResourceCopyStatisticsKeyEnum.COMPLETED.getValue()

        :return: The completed_copy_counts of this GetResourceCopySummaryResponseSummary.
        :rtype: int
        """
        return self._completed_copy_counts

    @completed_copy_counts.setter
    def completed_copy_counts(self, completed_copy_counts):
        r"""Sets the completed_copy_counts of this GetResourceCopySummaryResponseSummary.

        当前统计日期内的完成备份总数, key -> ResourceCopyStatisticsKeyEnum.COMPLETED.getValue()

        :param completed_copy_counts: The completed_copy_counts of this GetResourceCopySummaryResponseSummary.
        :type completed_copy_counts: int
        """
        self._completed_copy_counts = completed_copy_counts

    @property
    def failed_copy_counts(self):
        r"""Gets the failed_copy_counts of this GetResourceCopySummaryResponseSummary.

        当前统计日期内的失败备份总数, key -> ResourceCopyStatisticsKeyEnum.FAILED.getValue()

        :return: The failed_copy_counts of this GetResourceCopySummaryResponseSummary.
        :rtype: int
        """
        return self._failed_copy_counts

    @failed_copy_counts.setter
    def failed_copy_counts(self, failed_copy_counts):
        r"""Sets the failed_copy_counts of this GetResourceCopySummaryResponseSummary.

        当前统计日期内的失败备份总数, key -> ResourceCopyStatisticsKeyEnum.FAILED.getValue()

        :param failed_copy_counts: The failed_copy_counts of this GetResourceCopySummaryResponseSummary.
        :type failed_copy_counts: int
        """
        self._failed_copy_counts = failed_copy_counts

    def to_dict(self):
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
        if not isinstance(other, GetResourceCopySummaryResponseSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
