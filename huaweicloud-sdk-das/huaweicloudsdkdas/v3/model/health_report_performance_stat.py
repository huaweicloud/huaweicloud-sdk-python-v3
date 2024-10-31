# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthReportPerformanceStat:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'peak_stats': 'list[HealthReportSingleValueStat]',
        'ratio_stats': 'list[HealthReportRatioStat]'
    }

    attribute_map = {
        'peak_stats': 'peak_stats',
        'ratio_stats': 'ratio_stats'
    }

    def __init__(self, peak_stats=None, ratio_stats=None):
        """HealthReportPerformanceStat

        The model defined in huaweicloud sdk

        :param peak_stats: 峰值统计信息列表。
        :type peak_stats: list[:class:`huaweicloudsdkdas.v3.HealthReportSingleValueStat`]
        :param ratio_stats: 比率值数据列表。
        :type ratio_stats: list[:class:`huaweicloudsdkdas.v3.HealthReportRatioStat`]
        """
        
        

        self._peak_stats = None
        self._ratio_stats = None
        self.discriminator = None

        self.peak_stats = peak_stats
        self.ratio_stats = ratio_stats

    @property
    def peak_stats(self):
        """Gets the peak_stats of this HealthReportPerformanceStat.

        峰值统计信息列表。

        :return: The peak_stats of this HealthReportPerformanceStat.
        :rtype: list[:class:`huaweicloudsdkdas.v3.HealthReportSingleValueStat`]
        """
        return self._peak_stats

    @peak_stats.setter
    def peak_stats(self, peak_stats):
        """Sets the peak_stats of this HealthReportPerformanceStat.

        峰值统计信息列表。

        :param peak_stats: The peak_stats of this HealthReportPerformanceStat.
        :type peak_stats: list[:class:`huaweicloudsdkdas.v3.HealthReportSingleValueStat`]
        """
        self._peak_stats = peak_stats

    @property
    def ratio_stats(self):
        """Gets the ratio_stats of this HealthReportPerformanceStat.

        比率值数据列表。

        :return: The ratio_stats of this HealthReportPerformanceStat.
        :rtype: list[:class:`huaweicloudsdkdas.v3.HealthReportRatioStat`]
        """
        return self._ratio_stats

    @ratio_stats.setter
    def ratio_stats(self, ratio_stats):
        """Sets the ratio_stats of this HealthReportPerformanceStat.

        比率值数据列表。

        :param ratio_stats: The ratio_stats of this HealthReportPerformanceStat.
        :type ratio_stats: list[:class:`huaweicloudsdkdas.v3.HealthReportRatioStat`]
        """
        self._ratio_stats = ratio_stats

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
        if not isinstance(other, HealthReportPerformanceStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
