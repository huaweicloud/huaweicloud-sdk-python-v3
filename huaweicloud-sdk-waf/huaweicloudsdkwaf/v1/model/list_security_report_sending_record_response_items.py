# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityReportSendingRecordResponseItems:

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
        'report_name': 'str',
        'stat_period': 'ListSecurityReportSendingRecordResponseStatPeriod',
        'report_category': 'str',
        'sending_time': 'int'
    }

    attribute_map = {
        'report_id': 'report_id',
        'subscription_id': 'subscription_id',
        'report_name': 'report_name',
        'stat_period': 'stat_period',
        'report_category': 'report_category',
        'sending_time': 'sending_time'
    }

    def __init__(self, report_id=None, subscription_id=None, report_name=None, stat_period=None, report_category=None, sending_time=None):
        r"""ListSecurityReportSendingRecordResponseItems

        The model defined in huaweicloud sdk

        :param report_id: **参数解释：** 报告ID，唯一标识该发送记录对应的安全报告。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type report_id: str
        :param subscription_id: **参数解释：** 订阅ID，关联该发送记录所属的安全报告订阅。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type subscription_id: str
        :param report_name: **参数解释：** 报告名称，该发送记录对应的安全报告名称。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type report_name: str
        :param stat_period: 
        :type stat_period: :class:`huaweicloudsdkwaf.v1.ListSecurityReportSendingRecordResponseStatPeriod`
        :param report_category: **参数解释：** 报告类别，该发送记录对应报告的类型（如日报、周报）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type report_category: str
        :param sending_time: **参数解释：** 发送时间，该报告实际发送的时间戳（毫秒级）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type sending_time: int
        """
        
        

        self._report_id = None
        self._subscription_id = None
        self._report_name = None
        self._stat_period = None
        self._report_category = None
        self._sending_time = None
        self.discriminator = None

        self.report_id = report_id
        self.subscription_id = subscription_id
        self.report_name = report_name
        self.stat_period = stat_period
        self.report_category = report_category
        self.sending_time = sending_time

    @property
    def report_id(self):
        r"""Gets the report_id of this ListSecurityReportSendingRecordResponseItems.

        **参数解释：** 报告ID，唯一标识该发送记录对应的安全报告。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The report_id of this ListSecurityReportSendingRecordResponseItems.
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        r"""Sets the report_id of this ListSecurityReportSendingRecordResponseItems.

        **参数解释：** 报告ID，唯一标识该发送记录对应的安全报告。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param report_id: The report_id of this ListSecurityReportSendingRecordResponseItems.
        :type report_id: str
        """
        self._report_id = report_id

    @property
    def subscription_id(self):
        r"""Gets the subscription_id of this ListSecurityReportSendingRecordResponseItems.

        **参数解释：** 订阅ID，关联该发送记录所属的安全报告订阅。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The subscription_id of this ListSecurityReportSendingRecordResponseItems.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        r"""Sets the subscription_id of this ListSecurityReportSendingRecordResponseItems.

        **参数解释：** 订阅ID，关联该发送记录所属的安全报告订阅。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param subscription_id: The subscription_id of this ListSecurityReportSendingRecordResponseItems.
        :type subscription_id: str
        """
        self._subscription_id = subscription_id

    @property
    def report_name(self):
        r"""Gets the report_name of this ListSecurityReportSendingRecordResponseItems.

        **参数解释：** 报告名称，该发送记录对应的安全报告名称。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The report_name of this ListSecurityReportSendingRecordResponseItems.
        :rtype: str
        """
        return self._report_name

    @report_name.setter
    def report_name(self, report_name):
        r"""Sets the report_name of this ListSecurityReportSendingRecordResponseItems.

        **参数解释：** 报告名称，该发送记录对应的安全报告名称。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param report_name: The report_name of this ListSecurityReportSendingRecordResponseItems.
        :type report_name: str
        """
        self._report_name = report_name

    @property
    def stat_period(self):
        r"""Gets the stat_period of this ListSecurityReportSendingRecordResponseItems.

        :return: The stat_period of this ListSecurityReportSendingRecordResponseItems.
        :rtype: :class:`huaweicloudsdkwaf.v1.ListSecurityReportSendingRecordResponseStatPeriod`
        """
        return self._stat_period

    @stat_period.setter
    def stat_period(self, stat_period):
        r"""Sets the stat_period of this ListSecurityReportSendingRecordResponseItems.

        :param stat_period: The stat_period of this ListSecurityReportSendingRecordResponseItems.
        :type stat_period: :class:`huaweicloudsdkwaf.v1.ListSecurityReportSendingRecordResponseStatPeriod`
        """
        self._stat_period = stat_period

    @property
    def report_category(self):
        r"""Gets the report_category of this ListSecurityReportSendingRecordResponseItems.

        **参数解释：** 报告类别，该发送记录对应报告的类型（如日报、周报）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The report_category of this ListSecurityReportSendingRecordResponseItems.
        :rtype: str
        """
        return self._report_category

    @report_category.setter
    def report_category(self, report_category):
        r"""Sets the report_category of this ListSecurityReportSendingRecordResponseItems.

        **参数解释：** 报告类别，该发送记录对应报告的类型（如日报、周报）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param report_category: The report_category of this ListSecurityReportSendingRecordResponseItems.
        :type report_category: str
        """
        self._report_category = report_category

    @property
    def sending_time(self):
        r"""Gets the sending_time of this ListSecurityReportSendingRecordResponseItems.

        **参数解释：** 发送时间，该报告实际发送的时间戳（毫秒级）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The sending_time of this ListSecurityReportSendingRecordResponseItems.
        :rtype: int
        """
        return self._sending_time

    @sending_time.setter
    def sending_time(self, sending_time):
        r"""Sets the sending_time of this ListSecurityReportSendingRecordResponseItems.

        **参数解释：** 发送时间，该报告实际发送的时间戳（毫秒级）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param sending_time: The sending_time of this ListSecurityReportSendingRecordResponseItems.
        :type sending_time: int
        """
        self._sending_time = sending_time

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
        if not isinstance(other, ListSecurityReportSendingRecordResponseItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
