# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSecurityReportSubscriptionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sending_period': 'str',
        'report_name': 'str',
        'report_category': 'str',
        'topic_urn': 'str',
        'subscription_type': 'str',
        'report_content_subscription': 'CreateSecurityReportSubscriptionRequestBodyReportContentSubscription',
        'stat_period': 'CreateSecurityReportSubscriptionRequestBodyStatPeriod',
        'console_url_prefix': 'str'
    }

    attribute_map = {
        'sending_period': 'sending_period',
        'report_name': 'report_name',
        'report_category': 'report_category',
        'topic_urn': 'topic_urn',
        'subscription_type': 'subscription_type',
        'report_content_subscription': 'report_content_subscription',
        'stat_period': 'stat_period',
        'console_url_prefix': 'console_url_prefix'
    }

    def __init__(self, sending_period=None, report_name=None, report_category=None, topic_urn=None, subscription_type=None, report_content_subscription=None, stat_period=None, console_url_prefix=None):
        r"""CreateSecurityReportSubscriptionRequestBody

        The model defined in huaweicloud sdk

        :param sending_period: **参数解释：** 发送时间段，设置报告的预设发送时间（如morning表示早晨时段）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type sending_period: str
        :param report_name: **参数解释：** 报告名称，设置订阅报告的名称。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type report_name: str
        :param report_category: **参数解释：** 报告类别，设置订阅的报告类型（如daily_report表示安全日报）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type report_category: str
        :param topic_urn: **参数解释：** 主题urn，设置报告发送的SMN主题唯一标识。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type topic_urn: str
        :param subscription_type: **参数解释：** 订阅类型，设置报告的订阅方式（如smn_topic表示SMN主题订阅）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type subscription_type: str
        :param report_content_subscription: 
        :type report_content_subscription: :class:`huaweicloudsdkwaf.v1.CreateSecurityReportSubscriptionRequestBodyReportContentSubscription`
        :param stat_period: 
        :type stat_period: :class:`huaweicloudsdkwaf.v1.CreateSecurityReportSubscriptionRequestBodyStatPeriod`
        :param console_url_prefix: **参数解释：** 控制台URL前缀，用于拼接生成报告中相关资源的控制台访问链接 **格式要求：** 必须以http://或https://开头的有效URL格式 **约束限制：** 仅支持华为云控制台域名及路径 **默认取值：** https://console.huaweicloud.com/console/
        :type console_url_prefix: str
        """
        
        

        self._sending_period = None
        self._report_name = None
        self._report_category = None
        self._topic_urn = None
        self._subscription_type = None
        self._report_content_subscription = None
        self._stat_period = None
        self._console_url_prefix = None
        self.discriminator = None

        if sending_period is not None:
            self.sending_period = sending_period
        if report_name is not None:
            self.report_name = report_name
        if report_category is not None:
            self.report_category = report_category
        if topic_urn is not None:
            self.topic_urn = topic_urn
        if subscription_type is not None:
            self.subscription_type = subscription_type
        if report_content_subscription is not None:
            self.report_content_subscription = report_content_subscription
        if stat_period is not None:
            self.stat_period = stat_period
        if console_url_prefix is not None:
            self.console_url_prefix = console_url_prefix

    @property
    def sending_period(self):
        r"""Gets the sending_period of this CreateSecurityReportSubscriptionRequestBody.

        **参数解释：** 发送时间段，设置报告的预设发送时间（如morning表示早晨时段）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The sending_period of this CreateSecurityReportSubscriptionRequestBody.
        :rtype: str
        """
        return self._sending_period

    @sending_period.setter
    def sending_period(self, sending_period):
        r"""Sets the sending_period of this CreateSecurityReportSubscriptionRequestBody.

        **参数解释：** 发送时间段，设置报告的预设发送时间（如morning表示早晨时段）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param sending_period: The sending_period of this CreateSecurityReportSubscriptionRequestBody.
        :type sending_period: str
        """
        self._sending_period = sending_period

    @property
    def report_name(self):
        r"""Gets the report_name of this CreateSecurityReportSubscriptionRequestBody.

        **参数解释：** 报告名称，设置订阅报告的名称。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The report_name of this CreateSecurityReportSubscriptionRequestBody.
        :rtype: str
        """
        return self._report_name

    @report_name.setter
    def report_name(self, report_name):
        r"""Sets the report_name of this CreateSecurityReportSubscriptionRequestBody.

        **参数解释：** 报告名称，设置订阅报告的名称。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param report_name: The report_name of this CreateSecurityReportSubscriptionRequestBody.
        :type report_name: str
        """
        self._report_name = report_name

    @property
    def report_category(self):
        r"""Gets the report_category of this CreateSecurityReportSubscriptionRequestBody.

        **参数解释：** 报告类别，设置订阅的报告类型（如daily_report表示安全日报）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The report_category of this CreateSecurityReportSubscriptionRequestBody.
        :rtype: str
        """
        return self._report_category

    @report_category.setter
    def report_category(self, report_category):
        r"""Sets the report_category of this CreateSecurityReportSubscriptionRequestBody.

        **参数解释：** 报告类别，设置订阅的报告类型（如daily_report表示安全日报）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param report_category: The report_category of this CreateSecurityReportSubscriptionRequestBody.
        :type report_category: str
        """
        self._report_category = report_category

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this CreateSecurityReportSubscriptionRequestBody.

        **参数解释：** 主题urn，设置报告发送的SMN主题唯一标识。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The topic_urn of this CreateSecurityReportSubscriptionRequestBody.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this CreateSecurityReportSubscriptionRequestBody.

        **参数解释：** 主题urn，设置报告发送的SMN主题唯一标识。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param topic_urn: The topic_urn of this CreateSecurityReportSubscriptionRequestBody.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def subscription_type(self):
        r"""Gets the subscription_type of this CreateSecurityReportSubscriptionRequestBody.

        **参数解释：** 订阅类型，设置报告的订阅方式（如smn_topic表示SMN主题订阅）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The subscription_type of this CreateSecurityReportSubscriptionRequestBody.
        :rtype: str
        """
        return self._subscription_type

    @subscription_type.setter
    def subscription_type(self, subscription_type):
        r"""Sets the subscription_type of this CreateSecurityReportSubscriptionRequestBody.

        **参数解释：** 订阅类型，设置报告的订阅方式（如smn_topic表示SMN主题订阅）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param subscription_type: The subscription_type of this CreateSecurityReportSubscriptionRequestBody.
        :type subscription_type: str
        """
        self._subscription_type = subscription_type

    @property
    def report_content_subscription(self):
        r"""Gets the report_content_subscription of this CreateSecurityReportSubscriptionRequestBody.

        :return: The report_content_subscription of this CreateSecurityReportSubscriptionRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateSecurityReportSubscriptionRequestBodyReportContentSubscription`
        """
        return self._report_content_subscription

    @report_content_subscription.setter
    def report_content_subscription(self, report_content_subscription):
        r"""Sets the report_content_subscription of this CreateSecurityReportSubscriptionRequestBody.

        :param report_content_subscription: The report_content_subscription of this CreateSecurityReportSubscriptionRequestBody.
        :type report_content_subscription: :class:`huaweicloudsdkwaf.v1.CreateSecurityReportSubscriptionRequestBodyReportContentSubscription`
        """
        self._report_content_subscription = report_content_subscription

    @property
    def stat_period(self):
        r"""Gets the stat_period of this CreateSecurityReportSubscriptionRequestBody.

        :return: The stat_period of this CreateSecurityReportSubscriptionRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateSecurityReportSubscriptionRequestBodyStatPeriod`
        """
        return self._stat_period

    @stat_period.setter
    def stat_period(self, stat_period):
        r"""Sets the stat_period of this CreateSecurityReportSubscriptionRequestBody.

        :param stat_period: The stat_period of this CreateSecurityReportSubscriptionRequestBody.
        :type stat_period: :class:`huaweicloudsdkwaf.v1.CreateSecurityReportSubscriptionRequestBodyStatPeriod`
        """
        self._stat_period = stat_period

    @property
    def console_url_prefix(self):
        r"""Gets the console_url_prefix of this CreateSecurityReportSubscriptionRequestBody.

        **参数解释：** 控制台URL前缀，用于拼接生成报告中相关资源的控制台访问链接 **格式要求：** 必须以http://或https://开头的有效URL格式 **约束限制：** 仅支持华为云控制台域名及路径 **默认取值：** https://console.huaweicloud.com/console/

        :return: The console_url_prefix of this CreateSecurityReportSubscriptionRequestBody.
        :rtype: str
        """
        return self._console_url_prefix

    @console_url_prefix.setter
    def console_url_prefix(self, console_url_prefix):
        r"""Sets the console_url_prefix of this CreateSecurityReportSubscriptionRequestBody.

        **参数解释：** 控制台URL前缀，用于拼接生成报告中相关资源的控制台访问链接 **格式要求：** 必须以http://或https://开头的有效URL格式 **约束限制：** 仅支持华为云控制台域名及路径 **默认取值：** https://console.huaweicloud.com/console/

        :param console_url_prefix: The console_url_prefix of this CreateSecurityReportSubscriptionRequestBody.
        :type console_url_prefix: str
        """
        self._console_url_prefix = console_url_prefix

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
        if not isinstance(other, CreateSecurityReportSubscriptionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
