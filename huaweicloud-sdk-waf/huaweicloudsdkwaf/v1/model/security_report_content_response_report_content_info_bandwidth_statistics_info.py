# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'average_info_list': 'list[SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfoAverageInfoList]',
        'peak_info_list': 'list[SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfoPeakInfoList]'
    }

    attribute_map = {
        'average_info_list': 'average_info_list',
        'peak_info_list': 'peak_info_list'
    }

    def __init__(self, average_info_list=None, peak_info_list=None):
        r"""SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfo

        The model defined in huaweicloud sdk

        :param average_info_list: **参数解释：** 平均带宽统计列表，包含各维度按时间线的平均带宽数据。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type average_info_list: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfoAverageInfoList`]
        :param peak_info_list: **参数解释：** 峰值带宽统计列表，包含各维度按时间线的峰值带宽数据。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type peak_info_list: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfoPeakInfoList`]
        """
        
        

        self._average_info_list = None
        self._peak_info_list = None
        self.discriminator = None

        if average_info_list is not None:
            self.average_info_list = average_info_list
        if peak_info_list is not None:
            self.peak_info_list = peak_info_list

    @property
    def average_info_list(self):
        r"""Gets the average_info_list of this SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfo.

        **参数解释：** 平均带宽统计列表，包含各维度按时间线的平均带宽数据。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The average_info_list of this SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfo.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfoAverageInfoList`]
        """
        return self._average_info_list

    @average_info_list.setter
    def average_info_list(self, average_info_list):
        r"""Sets the average_info_list of this SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfo.

        **参数解释：** 平均带宽统计列表，包含各维度按时间线的平均带宽数据。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param average_info_list: The average_info_list of this SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfo.
        :type average_info_list: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfoAverageInfoList`]
        """
        self._average_info_list = average_info_list

    @property
    def peak_info_list(self):
        r"""Gets the peak_info_list of this SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfo.

        **参数解释：** 峰值带宽统计列表，包含各维度按时间线的峰值带宽数据。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The peak_info_list of this SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfo.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfoPeakInfoList`]
        """
        return self._peak_info_list

    @peak_info_list.setter
    def peak_info_list(self, peak_info_list):
        r"""Sets the peak_info_list of this SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfo.

        **参数解释：** 峰值带宽统计列表，包含各维度按时间线的峰值带宽数据。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param peak_info_list: The peak_info_list of this SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfo.
        :type peak_info_list: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfoPeakInfoList`]
        """
        self._peak_info_list = peak_info_list

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
        if not isinstance(other, SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
