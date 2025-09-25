# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSecurityReportContentResponse(SdkResponse):

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
        'sending_period': 'str',
        'report_name': 'str',
        'report_category': 'str',
        'topic_urn': 'str',
        'subscription_type': 'str',
        'report_content_info': 'SecurityReportContentResponseReportContentInfo',
        'create_time': 'int',
        'stat_period': 'SecurityReportContentResponseStatPeriod'
    }

    attribute_map = {
        'report_id': 'report_id',
        'subscription_id': 'subscription_id',
        'sending_period': 'sending_period',
        'report_name': 'report_name',
        'report_category': 'report_category',
        'topic_urn': 'topic_urn',
        'subscription_type': 'subscription_type',
        'report_content_info': 'report_content_info',
        'create_time': 'create_time',
        'stat_period': 'stat_period'
    }

    def __init__(self, report_id=None, subscription_id=None, sending_period=None, report_name=None, report_category=None, topic_urn=None, subscription_type=None, report_content_info=None, create_time=None, stat_period=None):
        r"""ShowSecurityReportContentResponse

        The model defined in huaweicloud sdk

        :param report_id: **参数解释：** 报告ID，唯一标识当前查询的安全报告。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type report_id: str
        :param subscription_id: **参数解释：** 订阅ID，关联当前报告所属的安全报告订阅记录。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type subscription_id: str
        :param sending_period: **参数解释：** 发送时间段，标识报告的预设发送时间（如morning表示早晨时段）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type sending_period: str
        :param report_name: **参数解释：** 报告名称，用于标识当前安全报告的名称。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type report_name: str
        :param report_category: **参数解释：** 报告类别，标识报告类型（如daily_report表示安全日报）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type report_category: str
        :param topic_urn: **参数解释：** 主题urn，关联报告发送的SMN主题唯一标识。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type topic_urn: str
        :param subscription_type: **参数解释：** 订阅类型，标识安全报告的订阅方式（如slient表示静默订阅）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type subscription_type: str
        :param report_content_info: 
        :type report_content_info: :class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfo`
        :param create_time: **参数解释：** 创建时间，报告的创建时间。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type create_time: int
        :param stat_period: 
        :type stat_period: :class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseStatPeriod`
        """
        
        super(ShowSecurityReportContentResponse, self).__init__()

        self._report_id = None
        self._subscription_id = None
        self._sending_period = None
        self._report_name = None
        self._report_category = None
        self._topic_urn = None
        self._subscription_type = None
        self._report_content_info = None
        self._create_time = None
        self._stat_period = None
        self.discriminator = None

        if report_id is not None:
            self.report_id = report_id
        if subscription_id is not None:
            self.subscription_id = subscription_id
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
        if report_content_info is not None:
            self.report_content_info = report_content_info
        if create_time is not None:
            self.create_time = create_time
        if stat_period is not None:
            self.stat_period = stat_period

    @property
    def report_id(self):
        r"""Gets the report_id of this ShowSecurityReportContentResponse.

        **参数解释：** 报告ID，唯一标识当前查询的安全报告。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The report_id of this ShowSecurityReportContentResponse.
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        r"""Sets the report_id of this ShowSecurityReportContentResponse.

        **参数解释：** 报告ID，唯一标识当前查询的安全报告。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param report_id: The report_id of this ShowSecurityReportContentResponse.
        :type report_id: str
        """
        self._report_id = report_id

    @property
    def subscription_id(self):
        r"""Gets the subscription_id of this ShowSecurityReportContentResponse.

        **参数解释：** 订阅ID，关联当前报告所属的安全报告订阅记录。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The subscription_id of this ShowSecurityReportContentResponse.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        r"""Sets the subscription_id of this ShowSecurityReportContentResponse.

        **参数解释：** 订阅ID，关联当前报告所属的安全报告订阅记录。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param subscription_id: The subscription_id of this ShowSecurityReportContentResponse.
        :type subscription_id: str
        """
        self._subscription_id = subscription_id

    @property
    def sending_period(self):
        r"""Gets the sending_period of this ShowSecurityReportContentResponse.

        **参数解释：** 发送时间段，标识报告的预设发送时间（如morning表示早晨时段）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The sending_period of this ShowSecurityReportContentResponse.
        :rtype: str
        """
        return self._sending_period

    @sending_period.setter
    def sending_period(self, sending_period):
        r"""Sets the sending_period of this ShowSecurityReportContentResponse.

        **参数解释：** 发送时间段，标识报告的预设发送时间（如morning表示早晨时段）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param sending_period: The sending_period of this ShowSecurityReportContentResponse.
        :type sending_period: str
        """
        self._sending_period = sending_period

    @property
    def report_name(self):
        r"""Gets the report_name of this ShowSecurityReportContentResponse.

        **参数解释：** 报告名称，用于标识当前安全报告的名称。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The report_name of this ShowSecurityReportContentResponse.
        :rtype: str
        """
        return self._report_name

    @report_name.setter
    def report_name(self, report_name):
        r"""Sets the report_name of this ShowSecurityReportContentResponse.

        **参数解释：** 报告名称，用于标识当前安全报告的名称。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param report_name: The report_name of this ShowSecurityReportContentResponse.
        :type report_name: str
        """
        self._report_name = report_name

    @property
    def report_category(self):
        r"""Gets the report_category of this ShowSecurityReportContentResponse.

        **参数解释：** 报告类别，标识报告类型（如daily_report表示安全日报）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The report_category of this ShowSecurityReportContentResponse.
        :rtype: str
        """
        return self._report_category

    @report_category.setter
    def report_category(self, report_category):
        r"""Sets the report_category of this ShowSecurityReportContentResponse.

        **参数解释：** 报告类别，标识报告类型（如daily_report表示安全日报）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param report_category: The report_category of this ShowSecurityReportContentResponse.
        :type report_category: str
        """
        self._report_category = report_category

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this ShowSecurityReportContentResponse.

        **参数解释：** 主题urn，关联报告发送的SMN主题唯一标识。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The topic_urn of this ShowSecurityReportContentResponse.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this ShowSecurityReportContentResponse.

        **参数解释：** 主题urn，关联报告发送的SMN主题唯一标识。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param topic_urn: The topic_urn of this ShowSecurityReportContentResponse.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def subscription_type(self):
        r"""Gets the subscription_type of this ShowSecurityReportContentResponse.

        **参数解释：** 订阅类型，标识安全报告的订阅方式（如slient表示静默订阅）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The subscription_type of this ShowSecurityReportContentResponse.
        :rtype: str
        """
        return self._subscription_type

    @subscription_type.setter
    def subscription_type(self, subscription_type):
        r"""Sets the subscription_type of this ShowSecurityReportContentResponse.

        **参数解释：** 订阅类型，标识安全报告的订阅方式（如slient表示静默订阅）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param subscription_type: The subscription_type of this ShowSecurityReportContentResponse.
        :type subscription_type: str
        """
        self._subscription_type = subscription_type

    @property
    def report_content_info(self):
        r"""Gets the report_content_info of this ShowSecurityReportContentResponse.

        :return: The report_content_info of this ShowSecurityReportContentResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfo`
        """
        return self._report_content_info

    @report_content_info.setter
    def report_content_info(self, report_content_info):
        r"""Sets the report_content_info of this ShowSecurityReportContentResponse.

        :param report_content_info: The report_content_info of this ShowSecurityReportContentResponse.
        :type report_content_info: :class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfo`
        """
        self._report_content_info = report_content_info

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowSecurityReportContentResponse.

        **参数解释：** 创建时间，报告的创建时间。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The create_time of this ShowSecurityReportContentResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowSecurityReportContentResponse.

        **参数解释：** 创建时间，报告的创建时间。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param create_time: The create_time of this ShowSecurityReportContentResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def stat_period(self):
        r"""Gets the stat_period of this ShowSecurityReportContentResponse.

        :return: The stat_period of this ShowSecurityReportContentResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseStatPeriod`
        """
        return self._stat_period

    @stat_period.setter
    def stat_period(self, stat_period):
        r"""Sets the stat_period of this ShowSecurityReportContentResponse.

        :param stat_period: The stat_period of this ShowSecurityReportContentResponse.
        :type stat_period: :class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseStatPeriod`
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
        if not isinstance(other, ShowSecurityReportContentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
