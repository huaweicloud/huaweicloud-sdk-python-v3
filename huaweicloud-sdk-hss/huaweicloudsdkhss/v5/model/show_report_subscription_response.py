# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowReportSubscriptionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'report_id': 'int',
        'report_name': 'str',
        'sending_period': 'str',
        'report_category': 'str',
        'topic_urn': 'str',
        'display_name': 'str',
        'logo_type': 'str',
        'logo_id': 'str',
        'subscription_type': 'str',
        'overview_subscriptions': 'OverviewSubscriptionRes',
        'scans_subscriptions': 'ScansSubscriptionRes',
        'intrusion_subscriptions': 'IntrusionSubscriptionRes',
        'stat_period': 'StatPeriodRes'
    }

    attribute_map = {
        'report_id': 'report_id',
        'report_name': 'report_name',
        'sending_period': 'sending_period',
        'report_category': 'report_category',
        'topic_urn': 'topic_urn',
        'display_name': 'display_name',
        'logo_type': 'logo_type',
        'logo_id': 'logo_id',
        'subscription_type': 'subscription_type',
        'overview_subscriptions': 'overview_subscriptions',
        'scans_subscriptions': 'scans_subscriptions',
        'intrusion_subscriptions': 'intrusion_subscriptions',
        'stat_period': 'stat_period'
    }

    def __init__(self, report_id=None, report_name=None, sending_period=None, report_category=None, topic_urn=None, display_name=None, logo_type=None, logo_id=None, subscription_type=None, overview_subscriptions=None, scans_subscriptions=None, intrusion_subscriptions=None, stat_period=None):
        r"""ShowReportSubscriptionResponse

        The model defined in huaweicloud sdk

        :param report_id: **参数解释**: 报告ID **取值范围**: 最小值0，最大值2147483647 
        :type report_id: int
        :param report_name: **参数解释**: 报告名称 **取值范围**: 字符长度1-32位 
        :type report_name: str
        :param sending_period: **参数解释**: 报告发送的时间段 **取值范围**: - morning：0点到6点 - noon：6点到12点 - afternoon：12点到18点 - evening：18点到24点 
        :type sending_period: str
        :param report_category: **参数解释**: 报告类别 **取值范围**: - daily_report：安全日报 - weekly_report：安全周报 - monthly_report：安全月报 - custom_report：自定义报告 
        :type report_category: str
        :param topic_urn: **参数解释**: 主题urn **取值范围**: 字符长度0-256位 
        :type topic_urn: str
        :param display_name: **参数解释**: 主题的显示名 **取值范围**: 字符长度0-256位 
        :type display_name: str
        :param logo_type: **参数解释**: 报告logo类型 **取值范围**: - default：华为logo - customize：自定义logo 
        :type logo_type: str
        :param logo_id: **参数解释**: 自定义logo的文件id **取值范围**: 字符长度0-256位 
        :type logo_id: str
        :param subscription_type: **参数解释**: 订阅的方式 **取值范围**: - smn_topic：SMN主题 - message_center：消息中心 - silent：无需发送到邮箱 
        :type subscription_type: str
        :param overview_subscriptions: 
        :type overview_subscriptions: :class:`huaweicloudsdkhss.v5.OverviewSubscriptionRes`
        :param scans_subscriptions: 
        :type scans_subscriptions: :class:`huaweicloudsdkhss.v5.ScansSubscriptionRes`
        :param intrusion_subscriptions: 
        :type intrusion_subscriptions: :class:`huaweicloudsdkhss.v5.IntrusionSubscriptionRes`
        :param stat_period: 
        :type stat_period: :class:`huaweicloudsdkhss.v5.StatPeriodRes`
        """
        
        super().__init__()

        self._report_id = None
        self._report_name = None
        self._sending_period = None
        self._report_category = None
        self._topic_urn = None
        self._display_name = None
        self._logo_type = None
        self._logo_id = None
        self._subscription_type = None
        self._overview_subscriptions = None
        self._scans_subscriptions = None
        self._intrusion_subscriptions = None
        self._stat_period = None
        self.discriminator = None

        if report_id is not None:
            self.report_id = report_id
        if report_name is not None:
            self.report_name = report_name
        if sending_period is not None:
            self.sending_period = sending_period
        if report_category is not None:
            self.report_category = report_category
        if topic_urn is not None:
            self.topic_urn = topic_urn
        if display_name is not None:
            self.display_name = display_name
        if logo_type is not None:
            self.logo_type = logo_type
        if logo_id is not None:
            self.logo_id = logo_id
        if subscription_type is not None:
            self.subscription_type = subscription_type
        if overview_subscriptions is not None:
            self.overview_subscriptions = overview_subscriptions
        if scans_subscriptions is not None:
            self.scans_subscriptions = scans_subscriptions
        if intrusion_subscriptions is not None:
            self.intrusion_subscriptions = intrusion_subscriptions
        if stat_period is not None:
            self.stat_period = stat_period

    @property
    def report_id(self):
        r"""Gets the report_id of this ShowReportSubscriptionResponse.

        **参数解释**: 报告ID **取值范围**: 最小值0，最大值2147483647 

        :return: The report_id of this ShowReportSubscriptionResponse.
        :rtype: int
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        r"""Sets the report_id of this ShowReportSubscriptionResponse.

        **参数解释**: 报告ID **取值范围**: 最小值0，最大值2147483647 

        :param report_id: The report_id of this ShowReportSubscriptionResponse.
        :type report_id: int
        """
        self._report_id = report_id

    @property
    def report_name(self):
        r"""Gets the report_name of this ShowReportSubscriptionResponse.

        **参数解释**: 报告名称 **取值范围**: 字符长度1-32位 

        :return: The report_name of this ShowReportSubscriptionResponse.
        :rtype: str
        """
        return self._report_name

    @report_name.setter
    def report_name(self, report_name):
        r"""Sets the report_name of this ShowReportSubscriptionResponse.

        **参数解释**: 报告名称 **取值范围**: 字符长度1-32位 

        :param report_name: The report_name of this ShowReportSubscriptionResponse.
        :type report_name: str
        """
        self._report_name = report_name

    @property
    def sending_period(self):
        r"""Gets the sending_period of this ShowReportSubscriptionResponse.

        **参数解释**: 报告发送的时间段 **取值范围**: - morning：0点到6点 - noon：6点到12点 - afternoon：12点到18点 - evening：18点到24点 

        :return: The sending_period of this ShowReportSubscriptionResponse.
        :rtype: str
        """
        return self._sending_period

    @sending_period.setter
    def sending_period(self, sending_period):
        r"""Sets the sending_period of this ShowReportSubscriptionResponse.

        **参数解释**: 报告发送的时间段 **取值范围**: - morning：0点到6点 - noon：6点到12点 - afternoon：12点到18点 - evening：18点到24点 

        :param sending_period: The sending_period of this ShowReportSubscriptionResponse.
        :type sending_period: str
        """
        self._sending_period = sending_period

    @property
    def report_category(self):
        r"""Gets the report_category of this ShowReportSubscriptionResponse.

        **参数解释**: 报告类别 **取值范围**: - daily_report：安全日报 - weekly_report：安全周报 - monthly_report：安全月报 - custom_report：自定义报告 

        :return: The report_category of this ShowReportSubscriptionResponse.
        :rtype: str
        """
        return self._report_category

    @report_category.setter
    def report_category(self, report_category):
        r"""Sets the report_category of this ShowReportSubscriptionResponse.

        **参数解释**: 报告类别 **取值范围**: - daily_report：安全日报 - weekly_report：安全周报 - monthly_report：安全月报 - custom_report：自定义报告 

        :param report_category: The report_category of this ShowReportSubscriptionResponse.
        :type report_category: str
        """
        self._report_category = report_category

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this ShowReportSubscriptionResponse.

        **参数解释**: 主题urn **取值范围**: 字符长度0-256位 

        :return: The topic_urn of this ShowReportSubscriptionResponse.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this ShowReportSubscriptionResponse.

        **参数解释**: 主题urn **取值范围**: 字符长度0-256位 

        :param topic_urn: The topic_urn of this ShowReportSubscriptionResponse.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def display_name(self):
        r"""Gets the display_name of this ShowReportSubscriptionResponse.

        **参数解释**: 主题的显示名 **取值范围**: 字符长度0-256位 

        :return: The display_name of this ShowReportSubscriptionResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this ShowReportSubscriptionResponse.

        **参数解释**: 主题的显示名 **取值范围**: 字符长度0-256位 

        :param display_name: The display_name of this ShowReportSubscriptionResponse.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def logo_type(self):
        r"""Gets the logo_type of this ShowReportSubscriptionResponse.

        **参数解释**: 报告logo类型 **取值范围**: - default：华为logo - customize：自定义logo 

        :return: The logo_type of this ShowReportSubscriptionResponse.
        :rtype: str
        """
        return self._logo_type

    @logo_type.setter
    def logo_type(self, logo_type):
        r"""Sets the logo_type of this ShowReportSubscriptionResponse.

        **参数解释**: 报告logo类型 **取值范围**: - default：华为logo - customize：自定义logo 

        :param logo_type: The logo_type of this ShowReportSubscriptionResponse.
        :type logo_type: str
        """
        self._logo_type = logo_type

    @property
    def logo_id(self):
        r"""Gets the logo_id of this ShowReportSubscriptionResponse.

        **参数解释**: 自定义logo的文件id **取值范围**: 字符长度0-256位 

        :return: The logo_id of this ShowReportSubscriptionResponse.
        :rtype: str
        """
        return self._logo_id

    @logo_id.setter
    def logo_id(self, logo_id):
        r"""Sets the logo_id of this ShowReportSubscriptionResponse.

        **参数解释**: 自定义logo的文件id **取值范围**: 字符长度0-256位 

        :param logo_id: The logo_id of this ShowReportSubscriptionResponse.
        :type logo_id: str
        """
        self._logo_id = logo_id

    @property
    def subscription_type(self):
        r"""Gets the subscription_type of this ShowReportSubscriptionResponse.

        **参数解释**: 订阅的方式 **取值范围**: - smn_topic：SMN主题 - message_center：消息中心 - silent：无需发送到邮箱 

        :return: The subscription_type of this ShowReportSubscriptionResponse.
        :rtype: str
        """
        return self._subscription_type

    @subscription_type.setter
    def subscription_type(self, subscription_type):
        r"""Sets the subscription_type of this ShowReportSubscriptionResponse.

        **参数解释**: 订阅的方式 **取值范围**: - smn_topic：SMN主题 - message_center：消息中心 - silent：无需发送到邮箱 

        :param subscription_type: The subscription_type of this ShowReportSubscriptionResponse.
        :type subscription_type: str
        """
        self._subscription_type = subscription_type

    @property
    def overview_subscriptions(self):
        r"""Gets the overview_subscriptions of this ShowReportSubscriptionResponse.

        :return: The overview_subscriptions of this ShowReportSubscriptionResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.OverviewSubscriptionRes`
        """
        return self._overview_subscriptions

    @overview_subscriptions.setter
    def overview_subscriptions(self, overview_subscriptions):
        r"""Sets the overview_subscriptions of this ShowReportSubscriptionResponse.

        :param overview_subscriptions: The overview_subscriptions of this ShowReportSubscriptionResponse.
        :type overview_subscriptions: :class:`huaweicloudsdkhss.v5.OverviewSubscriptionRes`
        """
        self._overview_subscriptions = overview_subscriptions

    @property
    def scans_subscriptions(self):
        r"""Gets the scans_subscriptions of this ShowReportSubscriptionResponse.

        :return: The scans_subscriptions of this ShowReportSubscriptionResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.ScansSubscriptionRes`
        """
        return self._scans_subscriptions

    @scans_subscriptions.setter
    def scans_subscriptions(self, scans_subscriptions):
        r"""Sets the scans_subscriptions of this ShowReportSubscriptionResponse.

        :param scans_subscriptions: The scans_subscriptions of this ShowReportSubscriptionResponse.
        :type scans_subscriptions: :class:`huaweicloudsdkhss.v5.ScansSubscriptionRes`
        """
        self._scans_subscriptions = scans_subscriptions

    @property
    def intrusion_subscriptions(self):
        r"""Gets the intrusion_subscriptions of this ShowReportSubscriptionResponse.

        :return: The intrusion_subscriptions of this ShowReportSubscriptionResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.IntrusionSubscriptionRes`
        """
        return self._intrusion_subscriptions

    @intrusion_subscriptions.setter
    def intrusion_subscriptions(self, intrusion_subscriptions):
        r"""Sets the intrusion_subscriptions of this ShowReportSubscriptionResponse.

        :param intrusion_subscriptions: The intrusion_subscriptions of this ShowReportSubscriptionResponse.
        :type intrusion_subscriptions: :class:`huaweicloudsdkhss.v5.IntrusionSubscriptionRes`
        """
        self._intrusion_subscriptions = intrusion_subscriptions

    @property
    def stat_period(self):
        r"""Gets the stat_period of this ShowReportSubscriptionResponse.

        :return: The stat_period of this ShowReportSubscriptionResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.StatPeriodRes`
        """
        return self._stat_period

    @stat_period.setter
    def stat_period(self, stat_period):
        r"""Sets the stat_period of this ShowReportSubscriptionResponse.

        :param stat_period: The stat_period of this ShowReportSubscriptionResponse.
        :type stat_period: :class:`huaweicloudsdkhss.v5.StatPeriodRes`
        """
        self._stat_period = stat_period

    def to_dict(self):
        import warnings
        warnings.warn("ShowReportSubscriptionResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowReportSubscriptionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
