# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnhanceFullSqlStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'statistics': 'list[FullSqlStatisticInfoResult]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'statistics': 'statistics'
    }

    def __init__(self, total_count=None, statistics=None):
        r"""ListEnhanceFullSqlStatisticsResponse

        The model defined in huaweicloud sdk

        :param total_count: **参数解释**: 全量SQL聚合统计列表总数。 **取值范围**: 不涉及。
        :type total_count: int
        :param statistics: **参数解释**: 全量SQL聚合统计列表。
        :type statistics: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.FullSqlStatisticInfoResult`]
        """
        
        super(ListEnhanceFullSqlStatisticsResponse, self).__init__()

        self._total_count = None
        self._statistics = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if statistics is not None:
            self.statistics = statistics

    @property
    def total_count(self):
        r"""Gets the total_count of this ListEnhanceFullSqlStatisticsResponse.

        **参数解释**: 全量SQL聚合统计列表总数。 **取值范围**: 不涉及。

        :return: The total_count of this ListEnhanceFullSqlStatisticsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListEnhanceFullSqlStatisticsResponse.

        **参数解释**: 全量SQL聚合统计列表总数。 **取值范围**: 不涉及。

        :param total_count: The total_count of this ListEnhanceFullSqlStatisticsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def statistics(self):
        r"""Gets the statistics of this ListEnhanceFullSqlStatisticsResponse.

        **参数解释**: 全量SQL聚合统计列表。

        :return: The statistics of this ListEnhanceFullSqlStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.FullSqlStatisticInfoResult`]
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        r"""Sets the statistics of this ListEnhanceFullSqlStatisticsResponse.

        **参数解释**: 全量SQL聚合统计列表。

        :param statistics: The statistics of this ListEnhanceFullSqlStatisticsResponse.
        :type statistics: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.FullSqlStatisticInfoResult`]
        """
        self._statistics = statistics

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
        if not isinstance(other, ListEnhanceFullSqlStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
