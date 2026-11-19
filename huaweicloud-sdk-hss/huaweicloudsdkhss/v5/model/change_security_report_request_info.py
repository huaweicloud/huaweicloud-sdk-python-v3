# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeSecurityReportRequestInfo:

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
        'sending_period': 'str',
        'report_name': 'str',
        'topic_urn': 'str',
        'display_name': 'str',
        'subscription_type': 'str',
        'overview_subscriptions': 'OverviewSubscriptionReq',
        'scans_subscriptions': 'ScansSubscriptionReq',
        'intrusion_subscriptions': 'IntrusionSubscriptionReq',
        'logo_type': 'str',
        'logo_id': 'str'
    }

    attribute_map = {
        'report_id': 'report_id',
        'sending_period': 'sending_period',
        'report_name': 'report_name',
        'topic_urn': 'topic_urn',
        'display_name': 'display_name',
        'subscription_type': 'subscription_type',
        'overview_subscriptions': 'overview_subscriptions',
        'scans_subscriptions': 'scans_subscriptions',
        'intrusion_subscriptions': 'intrusion_subscriptions',
        'logo_type': 'logo_type',
        'logo_id': 'logo_id'
    }

    def __init__(self, report_id=None, sending_period=None, report_name=None, topic_urn=None, display_name=None, subscription_type=None, overview_subscriptions=None, scans_subscriptions=None, intrusion_subscriptions=None, logo_type=None, logo_id=None):
        r"""ChangeSecurityReportRequestInfo

        The model defined in huaweicloud sdk

        :param report_id: **参数解释**: 报告ID **约束限制**: 必填 **取值范围**: 最小值0，最大值2147483647 **默认取值**: 不涉及 
        :type report_id: int
        :param sending_period: **参数解释**: 报告发送的时间段 **约束限制**: 不涉及 **取值范围**: - morning：0点到6点 - noon：6点到12点 - afternoon：12点到18点 - evening：18点到24点  **默认取值**: 不涉及 
        :type sending_period: str
        :param report_name: **参数解释**: 报告名称 **约束限制**: 必填 **取值范围**: 字符长度1-32位 **默认取值**: 不涉及 
        :type report_name: str
        :param topic_urn: **参数解释**: 主题urn **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type topic_urn: str
        :param display_name: **参数解释**: 主题的显示名 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type display_name: str
        :param subscription_type: **参数解释**: 订阅的方式 **约束限制**: 不涉及 **取值范围**: - smn_topic：SMN主题 - message_center：消息中心 - silent：无需发送到邮箱  **默认取值**: 不涉及 
        :type subscription_type: str
        :param overview_subscriptions: 
        :type overview_subscriptions: :class:`huaweicloudsdkhss.v5.OverviewSubscriptionReq`
        :param scans_subscriptions: 
        :type scans_subscriptions: :class:`huaweicloudsdkhss.v5.ScansSubscriptionReq`
        :param intrusion_subscriptions: 
        :type intrusion_subscriptions: :class:`huaweicloudsdkhss.v5.IntrusionSubscriptionReq`
        :param logo_type: **参数解释**: 报告logo类型 **约束限制**: 不涉及 **取值范围**: - default：华为logo - customize：自定义logo  **默认取值**: 不涉及 
        :type logo_type: str
        :param logo_id: **参数解释**: 自定义logo的文件id **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type logo_id: str
        """
        
        

        self._report_id = None
        self._sending_period = None
        self._report_name = None
        self._topic_urn = None
        self._display_name = None
        self._subscription_type = None
        self._overview_subscriptions = None
        self._scans_subscriptions = None
        self._intrusion_subscriptions = None
        self._logo_type = None
        self._logo_id = None
        self.discriminator = None

        self.report_id = report_id
        if sending_period is not None:
            self.sending_period = sending_period
        self.report_name = report_name
        if topic_urn is not None:
            self.topic_urn = topic_urn
        if display_name is not None:
            self.display_name = display_name
        if subscription_type is not None:
            self.subscription_type = subscription_type
        if overview_subscriptions is not None:
            self.overview_subscriptions = overview_subscriptions
        if scans_subscriptions is not None:
            self.scans_subscriptions = scans_subscriptions
        if intrusion_subscriptions is not None:
            self.intrusion_subscriptions = intrusion_subscriptions
        if logo_type is not None:
            self.logo_type = logo_type
        if logo_id is not None:
            self.logo_id = logo_id

    @property
    def report_id(self):
        r"""Gets the report_id of this ChangeSecurityReportRequestInfo.

        **参数解释**: 报告ID **约束限制**: 必填 **取值范围**: 最小值0，最大值2147483647 **默认取值**: 不涉及 

        :return: The report_id of this ChangeSecurityReportRequestInfo.
        :rtype: int
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        r"""Sets the report_id of this ChangeSecurityReportRequestInfo.

        **参数解释**: 报告ID **约束限制**: 必填 **取值范围**: 最小值0，最大值2147483647 **默认取值**: 不涉及 

        :param report_id: The report_id of this ChangeSecurityReportRequestInfo.
        :type report_id: int
        """
        self._report_id = report_id

    @property
    def sending_period(self):
        r"""Gets the sending_period of this ChangeSecurityReportRequestInfo.

        **参数解释**: 报告发送的时间段 **约束限制**: 不涉及 **取值范围**: - morning：0点到6点 - noon：6点到12点 - afternoon：12点到18点 - evening：18点到24点  **默认取值**: 不涉及 

        :return: The sending_period of this ChangeSecurityReportRequestInfo.
        :rtype: str
        """
        return self._sending_period

    @sending_period.setter
    def sending_period(self, sending_period):
        r"""Sets the sending_period of this ChangeSecurityReportRequestInfo.

        **参数解释**: 报告发送的时间段 **约束限制**: 不涉及 **取值范围**: - morning：0点到6点 - noon：6点到12点 - afternoon：12点到18点 - evening：18点到24点  **默认取值**: 不涉及 

        :param sending_period: The sending_period of this ChangeSecurityReportRequestInfo.
        :type sending_period: str
        """
        self._sending_period = sending_period

    @property
    def report_name(self):
        r"""Gets the report_name of this ChangeSecurityReportRequestInfo.

        **参数解释**: 报告名称 **约束限制**: 必填 **取值范围**: 字符长度1-32位 **默认取值**: 不涉及 

        :return: The report_name of this ChangeSecurityReportRequestInfo.
        :rtype: str
        """
        return self._report_name

    @report_name.setter
    def report_name(self, report_name):
        r"""Sets the report_name of this ChangeSecurityReportRequestInfo.

        **参数解释**: 报告名称 **约束限制**: 必填 **取值范围**: 字符长度1-32位 **默认取值**: 不涉及 

        :param report_name: The report_name of this ChangeSecurityReportRequestInfo.
        :type report_name: str
        """
        self._report_name = report_name

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this ChangeSecurityReportRequestInfo.

        **参数解释**: 主题urn **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The topic_urn of this ChangeSecurityReportRequestInfo.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this ChangeSecurityReportRequestInfo.

        **参数解释**: 主题urn **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param topic_urn: The topic_urn of this ChangeSecurityReportRequestInfo.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def display_name(self):
        r"""Gets the display_name of this ChangeSecurityReportRequestInfo.

        **参数解释**: 主题的显示名 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The display_name of this ChangeSecurityReportRequestInfo.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this ChangeSecurityReportRequestInfo.

        **参数解释**: 主题的显示名 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param display_name: The display_name of this ChangeSecurityReportRequestInfo.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def subscription_type(self):
        r"""Gets the subscription_type of this ChangeSecurityReportRequestInfo.

        **参数解释**: 订阅的方式 **约束限制**: 不涉及 **取值范围**: - smn_topic：SMN主题 - message_center：消息中心 - silent：无需发送到邮箱  **默认取值**: 不涉及 

        :return: The subscription_type of this ChangeSecurityReportRequestInfo.
        :rtype: str
        """
        return self._subscription_type

    @subscription_type.setter
    def subscription_type(self, subscription_type):
        r"""Sets the subscription_type of this ChangeSecurityReportRequestInfo.

        **参数解释**: 订阅的方式 **约束限制**: 不涉及 **取值范围**: - smn_topic：SMN主题 - message_center：消息中心 - silent：无需发送到邮箱  **默认取值**: 不涉及 

        :param subscription_type: The subscription_type of this ChangeSecurityReportRequestInfo.
        :type subscription_type: str
        """
        self._subscription_type = subscription_type

    @property
    def overview_subscriptions(self):
        r"""Gets the overview_subscriptions of this ChangeSecurityReportRequestInfo.

        :return: The overview_subscriptions of this ChangeSecurityReportRequestInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.OverviewSubscriptionReq`
        """
        return self._overview_subscriptions

    @overview_subscriptions.setter
    def overview_subscriptions(self, overview_subscriptions):
        r"""Sets the overview_subscriptions of this ChangeSecurityReportRequestInfo.

        :param overview_subscriptions: The overview_subscriptions of this ChangeSecurityReportRequestInfo.
        :type overview_subscriptions: :class:`huaweicloudsdkhss.v5.OverviewSubscriptionReq`
        """
        self._overview_subscriptions = overview_subscriptions

    @property
    def scans_subscriptions(self):
        r"""Gets the scans_subscriptions of this ChangeSecurityReportRequestInfo.

        :return: The scans_subscriptions of this ChangeSecurityReportRequestInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.ScansSubscriptionReq`
        """
        return self._scans_subscriptions

    @scans_subscriptions.setter
    def scans_subscriptions(self, scans_subscriptions):
        r"""Sets the scans_subscriptions of this ChangeSecurityReportRequestInfo.

        :param scans_subscriptions: The scans_subscriptions of this ChangeSecurityReportRequestInfo.
        :type scans_subscriptions: :class:`huaweicloudsdkhss.v5.ScansSubscriptionReq`
        """
        self._scans_subscriptions = scans_subscriptions

    @property
    def intrusion_subscriptions(self):
        r"""Gets the intrusion_subscriptions of this ChangeSecurityReportRequestInfo.

        :return: The intrusion_subscriptions of this ChangeSecurityReportRequestInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.IntrusionSubscriptionReq`
        """
        return self._intrusion_subscriptions

    @intrusion_subscriptions.setter
    def intrusion_subscriptions(self, intrusion_subscriptions):
        r"""Sets the intrusion_subscriptions of this ChangeSecurityReportRequestInfo.

        :param intrusion_subscriptions: The intrusion_subscriptions of this ChangeSecurityReportRequestInfo.
        :type intrusion_subscriptions: :class:`huaweicloudsdkhss.v5.IntrusionSubscriptionReq`
        """
        self._intrusion_subscriptions = intrusion_subscriptions

    @property
    def logo_type(self):
        r"""Gets the logo_type of this ChangeSecurityReportRequestInfo.

        **参数解释**: 报告logo类型 **约束限制**: 不涉及 **取值范围**: - default：华为logo - customize：自定义logo  **默认取值**: 不涉及 

        :return: The logo_type of this ChangeSecurityReportRequestInfo.
        :rtype: str
        """
        return self._logo_type

    @logo_type.setter
    def logo_type(self, logo_type):
        r"""Sets the logo_type of this ChangeSecurityReportRequestInfo.

        **参数解释**: 报告logo类型 **约束限制**: 不涉及 **取值范围**: - default：华为logo - customize：自定义logo  **默认取值**: 不涉及 

        :param logo_type: The logo_type of this ChangeSecurityReportRequestInfo.
        :type logo_type: str
        """
        self._logo_type = logo_type

    @property
    def logo_id(self):
        r"""Gets the logo_id of this ChangeSecurityReportRequestInfo.

        **参数解释**: 自定义logo的文件id **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The logo_id of this ChangeSecurityReportRequestInfo.
        :rtype: str
        """
        return self._logo_id

    @logo_id.setter
    def logo_id(self, logo_id):
        r"""Sets the logo_id of this ChangeSecurityReportRequestInfo.

        **参数解释**: 自定义logo的文件id **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param logo_id: The logo_id of this ChangeSecurityReportRequestInfo.
        :type logo_id: str
        """
        self._logo_id = logo_id

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
        if not isinstance(other, ChangeSecurityReportRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
