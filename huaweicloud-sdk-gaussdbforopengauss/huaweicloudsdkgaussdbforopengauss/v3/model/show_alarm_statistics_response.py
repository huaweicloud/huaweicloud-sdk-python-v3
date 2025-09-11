# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAlarmStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_alarm_count': 'int',
        'ring_percentage': 'float',
        'instance_alarm_level_statistics': 'list[InstanceAlarmLevelStatisticResult]',
        'total_alarm_level_statistics': 'list[AlarmLevelStatisticsResult]'
    }

    attribute_map = {
        'total_alarm_count': 'total_alarm_count',
        'ring_percentage': 'ring_percentage',
        'instance_alarm_level_statistics': 'instance_alarm_level_statistics',
        'total_alarm_level_statistics': 'total_alarm_level_statistics'
    }

    def __init__(self, total_alarm_count=None, ring_percentage=None, instance_alarm_level_statistics=None, total_alarm_level_statistics=None):
        r"""ShowAlarmStatisticsResponse

        The model defined in huaweicloud sdk

        :param total_alarm_count: **参数解释**: 告警总数。 **取值范围**: 不涉及。
        :type total_alarm_count: int
        :param ring_percentage: **参数解释**: 环比比率。 **取值范围**: 值为0表示环比没有变化，值为空表示上一周期没有告警。
        :type ring_percentage: float
        :param instance_alarm_level_statistics: **参数解释**: 实例级别的告警统计。
        :type instance_alarm_level_statistics: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.InstanceAlarmLevelStatisticResult`]
        :param total_alarm_level_statistics: **参数解释**: 全量告警统计。
        :type total_alarm_level_statistics: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.AlarmLevelStatisticsResult`]
        """
        
        super(ShowAlarmStatisticsResponse, self).__init__()

        self._total_alarm_count = None
        self._ring_percentage = None
        self._instance_alarm_level_statistics = None
        self._total_alarm_level_statistics = None
        self.discriminator = None

        if total_alarm_count is not None:
            self.total_alarm_count = total_alarm_count
        if ring_percentage is not None:
            self.ring_percentage = ring_percentage
        if instance_alarm_level_statistics is not None:
            self.instance_alarm_level_statistics = instance_alarm_level_statistics
        if total_alarm_level_statistics is not None:
            self.total_alarm_level_statistics = total_alarm_level_statistics

    @property
    def total_alarm_count(self):
        r"""Gets the total_alarm_count of this ShowAlarmStatisticsResponse.

        **参数解释**: 告警总数。 **取值范围**: 不涉及。

        :return: The total_alarm_count of this ShowAlarmStatisticsResponse.
        :rtype: int
        """
        return self._total_alarm_count

    @total_alarm_count.setter
    def total_alarm_count(self, total_alarm_count):
        r"""Sets the total_alarm_count of this ShowAlarmStatisticsResponse.

        **参数解释**: 告警总数。 **取值范围**: 不涉及。

        :param total_alarm_count: The total_alarm_count of this ShowAlarmStatisticsResponse.
        :type total_alarm_count: int
        """
        self._total_alarm_count = total_alarm_count

    @property
    def ring_percentage(self):
        r"""Gets the ring_percentage of this ShowAlarmStatisticsResponse.

        **参数解释**: 环比比率。 **取值范围**: 值为0表示环比没有变化，值为空表示上一周期没有告警。

        :return: The ring_percentage of this ShowAlarmStatisticsResponse.
        :rtype: float
        """
        return self._ring_percentage

    @ring_percentage.setter
    def ring_percentage(self, ring_percentage):
        r"""Sets the ring_percentage of this ShowAlarmStatisticsResponse.

        **参数解释**: 环比比率。 **取值范围**: 值为0表示环比没有变化，值为空表示上一周期没有告警。

        :param ring_percentage: The ring_percentage of this ShowAlarmStatisticsResponse.
        :type ring_percentage: float
        """
        self._ring_percentage = ring_percentage

    @property
    def instance_alarm_level_statistics(self):
        r"""Gets the instance_alarm_level_statistics of this ShowAlarmStatisticsResponse.

        **参数解释**: 实例级别的告警统计。

        :return: The instance_alarm_level_statistics of this ShowAlarmStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.InstanceAlarmLevelStatisticResult`]
        """
        return self._instance_alarm_level_statistics

    @instance_alarm_level_statistics.setter
    def instance_alarm_level_statistics(self, instance_alarm_level_statistics):
        r"""Sets the instance_alarm_level_statistics of this ShowAlarmStatisticsResponse.

        **参数解释**: 实例级别的告警统计。

        :param instance_alarm_level_statistics: The instance_alarm_level_statistics of this ShowAlarmStatisticsResponse.
        :type instance_alarm_level_statistics: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.InstanceAlarmLevelStatisticResult`]
        """
        self._instance_alarm_level_statistics = instance_alarm_level_statistics

    @property
    def total_alarm_level_statistics(self):
        r"""Gets the total_alarm_level_statistics of this ShowAlarmStatisticsResponse.

        **参数解释**: 全量告警统计。

        :return: The total_alarm_level_statistics of this ShowAlarmStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.AlarmLevelStatisticsResult`]
        """
        return self._total_alarm_level_statistics

    @total_alarm_level_statistics.setter
    def total_alarm_level_statistics(self, total_alarm_level_statistics):
        r"""Sets the total_alarm_level_statistics of this ShowAlarmStatisticsResponse.

        **参数解释**: 全量告警统计。

        :param total_alarm_level_statistics: The total_alarm_level_statistics of this ShowAlarmStatisticsResponse.
        :type total_alarm_level_statistics: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.AlarmLevelStatisticsResult`]
        """
        self._total_alarm_level_statistics = total_alarm_level_statistics

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
        if not isinstance(other, ShowAlarmStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
