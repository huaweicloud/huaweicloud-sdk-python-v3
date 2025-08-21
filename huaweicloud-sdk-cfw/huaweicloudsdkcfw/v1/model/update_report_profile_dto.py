# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateReportProfileDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'name': 'str',
        'send_period': 'int',
        'send_week_day': 'int',
        'statistic_period': 'StatisticPeriod',
        'status': 'int',
        'topic_urn': 'str',
        'subscription_type': 'int'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'send_period': 'send_period',
        'send_week_day': 'send_week_day',
        'statistic_period': 'statistic_period',
        'status': 'status',
        'topic_urn': 'topic_urn',
        'subscription_type': 'subscription_type'
    }

    def __init__(self, description=None, name=None, send_period=None, send_week_day=None, statistic_period=None, status=None, topic_urn=None, subscription_type=None):
        r"""UpdateReportProfileDto

        The model defined in huaweicloud sdk

        :param description: **参数解释**： 模板描述 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type description: str
        :param name: **参数解释**： 模板名称 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type name: str
        :param send_period: **参数解释**： 发送时间，日报和周报需要设置 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type send_period: int
        :param send_week_day: **参数解释**： 发送星期，周报需要设置 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type send_week_day: int
        :param statistic_period: 
        :type statistic_period: :class:`huaweicloudsdkcfw.v1.StatisticPeriod`
        :param status: **参数解释**： 启用状态 **约束限制**： 不涉及 **取值范围**： 0 关闭 1 启用 **默认取值**： 不涉及
        :type status: int
        :param topic_urn: **参数解释**： 通知群组 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type topic_urn: str
        :param subscription_type: **参数解释**： 通知方式 **约束限制**： 不涉及 **取值范围**： 0 SMN通知方式 1 不需要通知 **默认取值**： 不涉及
        :type subscription_type: int
        """
        
        

        self._description = None
        self._name = None
        self._send_period = None
        self._send_week_day = None
        self._statistic_period = None
        self._status = None
        self._topic_urn = None
        self._subscription_type = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if send_period is not None:
            self.send_period = send_period
        if send_week_day is not None:
            self.send_week_day = send_week_day
        if statistic_period is not None:
            self.statistic_period = statistic_period
        if status is not None:
            self.status = status
        if topic_urn is not None:
            self.topic_urn = topic_urn
        if subscription_type is not None:
            self.subscription_type = subscription_type

    @property
    def description(self):
        r"""Gets the description of this UpdateReportProfileDto.

        **参数解释**： 模板描述 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The description of this UpdateReportProfileDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateReportProfileDto.

        **参数解释**： 模板描述 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param description: The description of this UpdateReportProfileDto.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        r"""Gets the name of this UpdateReportProfileDto.

        **参数解释**： 模板名称 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The name of this UpdateReportProfileDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateReportProfileDto.

        **参数解释**： 模板名称 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param name: The name of this UpdateReportProfileDto.
        :type name: str
        """
        self._name = name

    @property
    def send_period(self):
        r"""Gets the send_period of this UpdateReportProfileDto.

        **参数解释**： 发送时间，日报和周报需要设置 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The send_period of this UpdateReportProfileDto.
        :rtype: int
        """
        return self._send_period

    @send_period.setter
    def send_period(self, send_period):
        r"""Sets the send_period of this UpdateReportProfileDto.

        **参数解释**： 发送时间，日报和周报需要设置 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param send_period: The send_period of this UpdateReportProfileDto.
        :type send_period: int
        """
        self._send_period = send_period

    @property
    def send_week_day(self):
        r"""Gets the send_week_day of this UpdateReportProfileDto.

        **参数解释**： 发送星期，周报需要设置 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The send_week_day of this UpdateReportProfileDto.
        :rtype: int
        """
        return self._send_week_day

    @send_week_day.setter
    def send_week_day(self, send_week_day):
        r"""Sets the send_week_day of this UpdateReportProfileDto.

        **参数解释**： 发送星期，周报需要设置 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param send_week_day: The send_week_day of this UpdateReportProfileDto.
        :type send_week_day: int
        """
        self._send_week_day = send_week_day

    @property
    def statistic_period(self):
        r"""Gets the statistic_period of this UpdateReportProfileDto.

        :return: The statistic_period of this UpdateReportProfileDto.
        :rtype: :class:`huaweicloudsdkcfw.v1.StatisticPeriod`
        """
        return self._statistic_period

    @statistic_period.setter
    def statistic_period(self, statistic_period):
        r"""Sets the statistic_period of this UpdateReportProfileDto.

        :param statistic_period: The statistic_period of this UpdateReportProfileDto.
        :type statistic_period: :class:`huaweicloudsdkcfw.v1.StatisticPeriod`
        """
        self._statistic_period = statistic_period

    @property
    def status(self):
        r"""Gets the status of this UpdateReportProfileDto.

        **参数解释**： 启用状态 **约束限制**： 不涉及 **取值范围**： 0 关闭 1 启用 **默认取值**： 不涉及

        :return: The status of this UpdateReportProfileDto.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateReportProfileDto.

        **参数解释**： 启用状态 **约束限制**： 不涉及 **取值范围**： 0 关闭 1 启用 **默认取值**： 不涉及

        :param status: The status of this UpdateReportProfileDto.
        :type status: int
        """
        self._status = status

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this UpdateReportProfileDto.

        **参数解释**： 通知群组 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The topic_urn of this UpdateReportProfileDto.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this UpdateReportProfileDto.

        **参数解释**： 通知群组 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param topic_urn: The topic_urn of this UpdateReportProfileDto.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def subscription_type(self):
        r"""Gets the subscription_type of this UpdateReportProfileDto.

        **参数解释**： 通知方式 **约束限制**： 不涉及 **取值范围**： 0 SMN通知方式 1 不需要通知 **默认取值**： 不涉及

        :return: The subscription_type of this UpdateReportProfileDto.
        :rtype: int
        """
        return self._subscription_type

    @subscription_type.setter
    def subscription_type(self, subscription_type):
        r"""Sets the subscription_type of this UpdateReportProfileDto.

        **参数解释**： 通知方式 **约束限制**： 不涉及 **取值范围**： 0 SMN通知方式 1 不需要通知 **默认取值**： 不涉及

        :param subscription_type: The subscription_type of this UpdateReportProfileDto.
        :type subscription_type: int
        """
        self._subscription_type = subscription_type

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
        if not isinstance(other, UpdateReportProfileDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
