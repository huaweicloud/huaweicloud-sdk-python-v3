# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfoPeakInfoList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'timeline': 'list[SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfoTimeline1]'
    }

    attribute_map = {
        'key': 'key',
        'timeline': 'timeline'
    }

    def __init__(self, key=None, timeline=None):
        r"""SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfoPeakInfoList

        The model defined in huaweicloud sdk

        :param key: **参数解释：** 统计维度标识（如BANDWIDTH表示带宽类统计）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type key: str
        :param timeline: **参数解释：** 时间线数据，按时间顺序排列的峰值带宽值。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type timeline: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfoTimeline1`]
        """
        
        

        self._key = None
        self._timeline = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if timeline is not None:
            self.timeline = timeline

    @property
    def key(self):
        r"""Gets the key of this SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfoPeakInfoList.

        **参数解释：** 统计维度标识（如BANDWIDTH表示带宽类统计）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The key of this SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfoPeakInfoList.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfoPeakInfoList.

        **参数解释：** 统计维度标识（如BANDWIDTH表示带宽类统计）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param key: The key of this SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfoPeakInfoList.
        :type key: str
        """
        self._key = key

    @property
    def timeline(self):
        r"""Gets the timeline of this SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfoPeakInfoList.

        **参数解释：** 时间线数据，按时间顺序排列的峰值带宽值。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The timeline of this SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfoPeakInfoList.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfoTimeline1`]
        """
        return self._timeline

    @timeline.setter
    def timeline(self, timeline):
        r"""Sets the timeline of this SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfoPeakInfoList.

        **参数解释：** 时间线数据，按时间顺序排列的峰值带宽值。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param timeline: The timeline of this SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfoPeakInfoList.
        :type timeline: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfoTimeline1`]
        """
        self._timeline = timeline

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
        if not isinstance(other, SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfoPeakInfoList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
