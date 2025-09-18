# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityReportHistoryPeriodResponseItems:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'report_id': 'str',
        'subscription_id': 'str',
        'stat_period': 'ListSecurityReportHistoryPeriodResponseStatPeriod'
    }

    attribute_map = {
        'report_id': 'report_id',
        'subscription_id': 'subscription_id',
        'stat_period': 'stat_period'
    }

    def __init__(self, report_id=None, subscription_id=None, stat_period=None):
        r"""ListSecurityReportHistoryPeriodResponseItems

        The model defined in huaweicloud sdk

        :param report_id: **参数解释：** 报告ID，唯一标识历史统计周期对应的安全报告。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type report_id: str
        :param subscription_id: **参数解释：** 订阅ID，关联历史统计周期所属的安全报告订阅。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type subscription_id: str
        :param stat_period: 
        :type stat_period: :class:`huaweicloudsdkwaf.v1.ListSecurityReportHistoryPeriodResponseStatPeriod`
        """
        
        

        self._report_id = None
        self._subscription_id = None
        self._stat_period = None
        self.discriminator = None

        self.report_id = report_id
        self.subscription_id = subscription_id
        self.stat_period = stat_period

    @property
    def report_id(self):
        r"""Gets the report_id of this ListSecurityReportHistoryPeriodResponseItems.

        **参数解释：** 报告ID，唯一标识历史统计周期对应的安全报告。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The report_id of this ListSecurityReportHistoryPeriodResponseItems.
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        r"""Sets the report_id of this ListSecurityReportHistoryPeriodResponseItems.

        **参数解释：** 报告ID，唯一标识历史统计周期对应的安全报告。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param report_id: The report_id of this ListSecurityReportHistoryPeriodResponseItems.
        :type report_id: str
        """
        self._report_id = report_id

    @property
    def subscription_id(self):
        r"""Gets the subscription_id of this ListSecurityReportHistoryPeriodResponseItems.

        **参数解释：** 订阅ID，关联历史统计周期所属的安全报告订阅。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The subscription_id of this ListSecurityReportHistoryPeriodResponseItems.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        r"""Sets the subscription_id of this ListSecurityReportHistoryPeriodResponseItems.

        **参数解释：** 订阅ID，关联历史统计周期所属的安全报告订阅。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param subscription_id: The subscription_id of this ListSecurityReportHistoryPeriodResponseItems.
        :type subscription_id: str
        """
        self._subscription_id = subscription_id

    @property
    def stat_period(self):
        r"""Gets the stat_period of this ListSecurityReportHistoryPeriodResponseItems.

        :return: The stat_period of this ListSecurityReportHistoryPeriodResponseItems.
        :rtype: :class:`huaweicloudsdkwaf.v1.ListSecurityReportHistoryPeriodResponseStatPeriod`
        """
        return self._stat_period

    @stat_period.setter
    def stat_period(self, stat_period):
        r"""Sets the stat_period of this ListSecurityReportHistoryPeriodResponseItems.

        :param stat_period: The stat_period of this ListSecurityReportHistoryPeriodResponseItems.
        :type stat_period: :class:`huaweicloudsdkwaf.v1.ListSecurityReportHistoryPeriodResponseStatPeriod`
        """
        self._stat_period = stat_period

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
        if not isinstance(other, ListSecurityReportHistoryPeriodResponseItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
