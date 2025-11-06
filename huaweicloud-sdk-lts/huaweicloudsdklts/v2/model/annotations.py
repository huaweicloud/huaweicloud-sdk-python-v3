# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Annotations:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'message': 'str',
        'log_info': 'str',
        'current_value': 'str',
        'old_annotations': 'str',
        'alarm_action_rule_name': 'str',
        'alarm_rule_alias': 'str',
        'alarm_rule_url': 'str',
        'alarm_status': 'str',
        'condition_expression': 'str',
        'condition_expression_with_value': 'str',
        'notification_frequency': 'str',
        'record_id': 'str',
        'recovery_policy': 'bool',
        'results': 'list[Results]',
        'frequency': 'str',
        'type': 'str'
    }

    attribute_map = {
        'message': 'message',
        'log_info': 'log_info',
        'current_value': 'current_value',
        'old_annotations': 'old_annotations',
        'alarm_action_rule_name': 'alarm_action_rule_name',
        'alarm_rule_alias': 'alarm_rule_alias',
        'alarm_rule_url': 'alarm_rule_url',
        'alarm_status': 'alarm_status',
        'condition_expression': 'condition_expression',
        'condition_expression_with_value': 'condition_expression_with_value',
        'notification_frequency': 'notification_frequency',
        'record_id': 'record_id',
        'recovery_policy': 'recovery_policy',
        'results': 'results',
        'frequency': 'frequency',
        'type': 'type'
    }

    def __init__(self, message=None, log_info=None, current_value=None, old_annotations=None, alarm_action_rule_name=None, alarm_rule_alias=None, alarm_rule_url=None, alarm_status=None, condition_expression=None, condition_expression_with_value=None, notification_frequency=None, record_id=None, recovery_policy=None, results=None, frequency=None, type=None):
        r"""Annotations

        The model defined in huaweicloud sdk

        :param message: 告警列表详情
        :type message: str
        :param log_info: 日志组/流id,名称
        :type log_info: str
        :param current_value: 当前值
        :type current_value: str
        :param old_annotations: (sql/关键词)告警详情原始数据
        :type old_annotations: str
        :param alarm_action_rule_name: **参数解释：** 告警行动规则名称。 **取值范围：** 不涉及。
        :type alarm_action_rule_name: str
        :param alarm_rule_alias: **参数解释：** 告警规则别名。 **取值范围：** 不涉及。
        :type alarm_rule_alias: str
        :param alarm_rule_url: **参数解释：** 告警规则url。 **取值范围：** 不涉及。
        :type alarm_rule_url: str
        :param alarm_status: **参数解释：** 告警触发状态。 **取值范围：** - 触发(firing) - 恢复(resolved)
        :type alarm_status: str
        :param condition_expression: **参数解释：** 告警触发条件表达式。 **取值范围：** 不涉及。
        :type condition_expression: str
        :param condition_expression_with_value: **参数解释：** 告警触发表达式带值。例如：条件表达式为pv &gt; 0，则condition_expression_with_value取值为：100 &gt; 0。 **取值范围：** 不涉及。
        :type condition_expression_with_value: str
        :param notification_frequency: **参数解释：** 通知频率。 **取值范围：** 不涉及。
        :type notification_frequency: str
        :param record_id: **参数解释：** 告警ID。 **取值范围：** 不涉及。
        :type record_id: str
        :param recovery_policy: **参数解释：** 是否开启告警恢复开关。 **取值范围：** - true： 开启告警恢复 - false： 关闭告警恢复
        :type recovery_policy: bool
        :param results: **参数解释：** 告警通知的详细信息。
        :type results: list[:class:`huaweicloudsdklts.v2.Results`]
        :param frequency: **参数解释：** 告警统计周期。 **取值范围：** 不涉及。
        :type frequency: str
        :param type: **参数解释：** 告警规则类型。 **取值范围：** - sql： sql告警 - keywords： 关键词告警
        :type type: str
        """
        
        

        self._message = None
        self._log_info = None
        self._current_value = None
        self._old_annotations = None
        self._alarm_action_rule_name = None
        self._alarm_rule_alias = None
        self._alarm_rule_url = None
        self._alarm_status = None
        self._condition_expression = None
        self._condition_expression_with_value = None
        self._notification_frequency = None
        self._record_id = None
        self._recovery_policy = None
        self._results = None
        self._frequency = None
        self._type = None
        self.discriminator = None

        self.message = message
        self.log_info = log_info
        self.current_value = current_value
        self.old_annotations = old_annotations
        if alarm_action_rule_name is not None:
            self.alarm_action_rule_name = alarm_action_rule_name
        if alarm_rule_alias is not None:
            self.alarm_rule_alias = alarm_rule_alias
        if alarm_rule_url is not None:
            self.alarm_rule_url = alarm_rule_url
        if alarm_status is not None:
            self.alarm_status = alarm_status
        if condition_expression is not None:
            self.condition_expression = condition_expression
        if condition_expression_with_value is not None:
            self.condition_expression_with_value = condition_expression_with_value
        if notification_frequency is not None:
            self.notification_frequency = notification_frequency
        if record_id is not None:
            self.record_id = record_id
        if recovery_policy is not None:
            self.recovery_policy = recovery_policy
        if results is not None:
            self.results = results
        if frequency is not None:
            self.frequency = frequency
        if type is not None:
            self.type = type

    @property
    def message(self):
        r"""Gets the message of this Annotations.

        告警列表详情

        :return: The message of this Annotations.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this Annotations.

        告警列表详情

        :param message: The message of this Annotations.
        :type message: str
        """
        self._message = message

    @property
    def log_info(self):
        r"""Gets the log_info of this Annotations.

        日志组/流id,名称

        :return: The log_info of this Annotations.
        :rtype: str
        """
        return self._log_info

    @log_info.setter
    def log_info(self, log_info):
        r"""Sets the log_info of this Annotations.

        日志组/流id,名称

        :param log_info: The log_info of this Annotations.
        :type log_info: str
        """
        self._log_info = log_info

    @property
    def current_value(self):
        r"""Gets the current_value of this Annotations.

        当前值

        :return: The current_value of this Annotations.
        :rtype: str
        """
        return self._current_value

    @current_value.setter
    def current_value(self, current_value):
        r"""Sets the current_value of this Annotations.

        当前值

        :param current_value: The current_value of this Annotations.
        :type current_value: str
        """
        self._current_value = current_value

    @property
    def old_annotations(self):
        r"""Gets the old_annotations of this Annotations.

        (sql/关键词)告警详情原始数据

        :return: The old_annotations of this Annotations.
        :rtype: str
        """
        return self._old_annotations

    @old_annotations.setter
    def old_annotations(self, old_annotations):
        r"""Sets the old_annotations of this Annotations.

        (sql/关键词)告警详情原始数据

        :param old_annotations: The old_annotations of this Annotations.
        :type old_annotations: str
        """
        self._old_annotations = old_annotations

    @property
    def alarm_action_rule_name(self):
        r"""Gets the alarm_action_rule_name of this Annotations.

        **参数解释：** 告警行动规则名称。 **取值范围：** 不涉及。

        :return: The alarm_action_rule_name of this Annotations.
        :rtype: str
        """
        return self._alarm_action_rule_name

    @alarm_action_rule_name.setter
    def alarm_action_rule_name(self, alarm_action_rule_name):
        r"""Sets the alarm_action_rule_name of this Annotations.

        **参数解释：** 告警行动规则名称。 **取值范围：** 不涉及。

        :param alarm_action_rule_name: The alarm_action_rule_name of this Annotations.
        :type alarm_action_rule_name: str
        """
        self._alarm_action_rule_name = alarm_action_rule_name

    @property
    def alarm_rule_alias(self):
        r"""Gets the alarm_rule_alias of this Annotations.

        **参数解释：** 告警规则别名。 **取值范围：** 不涉及。

        :return: The alarm_rule_alias of this Annotations.
        :rtype: str
        """
        return self._alarm_rule_alias

    @alarm_rule_alias.setter
    def alarm_rule_alias(self, alarm_rule_alias):
        r"""Sets the alarm_rule_alias of this Annotations.

        **参数解释：** 告警规则别名。 **取值范围：** 不涉及。

        :param alarm_rule_alias: The alarm_rule_alias of this Annotations.
        :type alarm_rule_alias: str
        """
        self._alarm_rule_alias = alarm_rule_alias

    @property
    def alarm_rule_url(self):
        r"""Gets the alarm_rule_url of this Annotations.

        **参数解释：** 告警规则url。 **取值范围：** 不涉及。

        :return: The alarm_rule_url of this Annotations.
        :rtype: str
        """
        return self._alarm_rule_url

    @alarm_rule_url.setter
    def alarm_rule_url(self, alarm_rule_url):
        r"""Sets the alarm_rule_url of this Annotations.

        **参数解释：** 告警规则url。 **取值范围：** 不涉及。

        :param alarm_rule_url: The alarm_rule_url of this Annotations.
        :type alarm_rule_url: str
        """
        self._alarm_rule_url = alarm_rule_url

    @property
    def alarm_status(self):
        r"""Gets the alarm_status of this Annotations.

        **参数解释：** 告警触发状态。 **取值范围：** - 触发(firing) - 恢复(resolved)

        :return: The alarm_status of this Annotations.
        :rtype: str
        """
        return self._alarm_status

    @alarm_status.setter
    def alarm_status(self, alarm_status):
        r"""Sets the alarm_status of this Annotations.

        **参数解释：** 告警触发状态。 **取值范围：** - 触发(firing) - 恢复(resolved)

        :param alarm_status: The alarm_status of this Annotations.
        :type alarm_status: str
        """
        self._alarm_status = alarm_status

    @property
    def condition_expression(self):
        r"""Gets the condition_expression of this Annotations.

        **参数解释：** 告警触发条件表达式。 **取值范围：** 不涉及。

        :return: The condition_expression of this Annotations.
        :rtype: str
        """
        return self._condition_expression

    @condition_expression.setter
    def condition_expression(self, condition_expression):
        r"""Sets the condition_expression of this Annotations.

        **参数解释：** 告警触发条件表达式。 **取值范围：** 不涉及。

        :param condition_expression: The condition_expression of this Annotations.
        :type condition_expression: str
        """
        self._condition_expression = condition_expression

    @property
    def condition_expression_with_value(self):
        r"""Gets the condition_expression_with_value of this Annotations.

        **参数解释：** 告警触发表达式带值。例如：条件表达式为pv > 0，则condition_expression_with_value取值为：100 > 0。 **取值范围：** 不涉及。

        :return: The condition_expression_with_value of this Annotations.
        :rtype: str
        """
        return self._condition_expression_with_value

    @condition_expression_with_value.setter
    def condition_expression_with_value(self, condition_expression_with_value):
        r"""Sets the condition_expression_with_value of this Annotations.

        **参数解释：** 告警触发表达式带值。例如：条件表达式为pv > 0，则condition_expression_with_value取值为：100 > 0。 **取值范围：** 不涉及。

        :param condition_expression_with_value: The condition_expression_with_value of this Annotations.
        :type condition_expression_with_value: str
        """
        self._condition_expression_with_value = condition_expression_with_value

    @property
    def notification_frequency(self):
        r"""Gets the notification_frequency of this Annotations.

        **参数解释：** 通知频率。 **取值范围：** 不涉及。

        :return: The notification_frequency of this Annotations.
        :rtype: str
        """
        return self._notification_frequency

    @notification_frequency.setter
    def notification_frequency(self, notification_frequency):
        r"""Sets the notification_frequency of this Annotations.

        **参数解释：** 通知频率。 **取值范围：** 不涉及。

        :param notification_frequency: The notification_frequency of this Annotations.
        :type notification_frequency: str
        """
        self._notification_frequency = notification_frequency

    @property
    def record_id(self):
        r"""Gets the record_id of this Annotations.

        **参数解释：** 告警ID。 **取值范围：** 不涉及。

        :return: The record_id of this Annotations.
        :rtype: str
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        r"""Sets the record_id of this Annotations.

        **参数解释：** 告警ID。 **取值范围：** 不涉及。

        :param record_id: The record_id of this Annotations.
        :type record_id: str
        """
        self._record_id = record_id

    @property
    def recovery_policy(self):
        r"""Gets the recovery_policy of this Annotations.

        **参数解释：** 是否开启告警恢复开关。 **取值范围：** - true： 开启告警恢复 - false： 关闭告警恢复

        :return: The recovery_policy of this Annotations.
        :rtype: bool
        """
        return self._recovery_policy

    @recovery_policy.setter
    def recovery_policy(self, recovery_policy):
        r"""Sets the recovery_policy of this Annotations.

        **参数解释：** 是否开启告警恢复开关。 **取值范围：** - true： 开启告警恢复 - false： 关闭告警恢复

        :param recovery_policy: The recovery_policy of this Annotations.
        :type recovery_policy: bool
        """
        self._recovery_policy = recovery_policy

    @property
    def results(self):
        r"""Gets the results of this Annotations.

        **参数解释：** 告警通知的详细信息。

        :return: The results of this Annotations.
        :rtype: list[:class:`huaweicloudsdklts.v2.Results`]
        """
        return self._results

    @results.setter
    def results(self, results):
        r"""Sets the results of this Annotations.

        **参数解释：** 告警通知的详细信息。

        :param results: The results of this Annotations.
        :type results: list[:class:`huaweicloudsdklts.v2.Results`]
        """
        self._results = results

    @property
    def frequency(self):
        r"""Gets the frequency of this Annotations.

        **参数解释：** 告警统计周期。 **取值范围：** 不涉及。

        :return: The frequency of this Annotations.
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        r"""Sets the frequency of this Annotations.

        **参数解释：** 告警统计周期。 **取值范围：** 不涉及。

        :param frequency: The frequency of this Annotations.
        :type frequency: str
        """
        self._frequency = frequency

    @property
    def type(self):
        r"""Gets the type of this Annotations.

        **参数解释：** 告警规则类型。 **取值范围：** - sql： sql告警 - keywords： 关键词告警

        :return: The type of this Annotations.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Annotations.

        **参数解释：** 告警规则类型。 **取值范围：** - sql： sql告警 - keywords： 关键词告警

        :param type: The type of this Annotations.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, Annotations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
