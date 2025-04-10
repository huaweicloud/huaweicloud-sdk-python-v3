# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSqlAlarmRuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_alarm_rule_name': 'str',
        'is_css_sql': 'bool',
        'sql_alarm_rule_description': 'str',
        'sql_requests': 'list[SqlRequest]',
        'frequency': 'CreateSqlAlarmRuleFrequency',
        'condition_expression': 'str',
        'sql_alarm_level': 'str',
        'sql_alarm_send': 'bool',
        'domain_id': 'str',
        'notification_save_rule': 'SqlNotificationSaveRule',
        'trigger_condition_count': 'int',
        'trigger_condition_frequency': 'int',
        'whether_recovery_policy': 'bool',
        'recovery_policy': 'int',
        'notification_frequency': 'int',
        'alarm_action_rule_name': 'str'
    }

    attribute_map = {
        'sql_alarm_rule_name': 'sql_alarm_rule_name',
        'is_css_sql': 'is_css_sql',
        'sql_alarm_rule_description': 'sql_alarm_rule_description',
        'sql_requests': 'sql_requests',
        'frequency': 'frequency',
        'condition_expression': 'condition_expression',
        'sql_alarm_level': 'sql_alarm_level',
        'sql_alarm_send': 'sql_alarm_send',
        'domain_id': 'domain_id',
        'notification_save_rule': 'notification_save_rule',
        'trigger_condition_count': 'trigger_condition_count',
        'trigger_condition_frequency': 'trigger_condition_frequency',
        'whether_recovery_policy': 'whether_recovery_policy',
        'recovery_policy': 'recovery_policy',
        'notification_frequency': 'notification_frequency',
        'alarm_action_rule_name': 'alarm_action_rule_name'
    }

    def __init__(self, sql_alarm_rule_name=None, is_css_sql=None, sql_alarm_rule_description=None, sql_requests=None, frequency=None, condition_expression=None, sql_alarm_level=None, sql_alarm_send=None, domain_id=None, notification_save_rule=None, trigger_condition_count=None, trigger_condition_frequency=None, whether_recovery_policy=None, recovery_policy=None, notification_frequency=None, alarm_action_rule_name=None):
        r"""CreateSqlAlarmRuleRequestBody

        The model defined in huaweicloud sdk

        :param sql_alarm_rule_name: SQL告警名称
        :type sql_alarm_rule_name: str
        :param is_css_sql: 是否管道符sql查询
        :type is_css_sql: bool
        :param sql_alarm_rule_description: SQL告警信息描述
        :type sql_alarm_rule_description: str
        :param sql_requests: SQL详细信息
        :type sql_requests: list[:class:`huaweicloudsdklts.v2.SqlRequest`]
        :param frequency: 
        :type frequency: :class:`huaweicloudsdklts.v2.CreateSqlAlarmRuleFrequency`
        :param condition_expression: 条件表达式
        :type condition_expression: str
        :param sql_alarm_level: 告警级别
        :type sql_alarm_level: str
        :param sql_alarm_send: 是否发送
        :type sql_alarm_send: bool
        :param domain_id: domainId
        :type domain_id: str
        :param notification_save_rule: 
        :type notification_save_rule: :class:`huaweicloudsdklts.v2.SqlNotificationSaveRule`
        :param trigger_condition_count: 触发条件：触发次数;默认为1
        :type trigger_condition_count: int
        :param trigger_condition_frequency: 触发条件：触发周期;默认为1
        :type trigger_condition_frequency: int
        :param whether_recovery_policy: 是否打开恢复通知;默认false
        :type whether_recovery_policy: bool
        :param recovery_policy: 恢复策略周期;默认为3
        :type recovery_policy: int
        :param notification_frequency: 通知频率,单位(分钟)
        :type notification_frequency: int
        :param alarm_action_rule_name: 告警行动规则名称 &gt;alarm_action_rule_name和notification_save_rule可以选填一个，如果都填，优先选择alarm_action_rule_name
        :type alarm_action_rule_name: str
        """
        
        

        self._sql_alarm_rule_name = None
        self._is_css_sql = None
        self._sql_alarm_rule_description = None
        self._sql_requests = None
        self._frequency = None
        self._condition_expression = None
        self._sql_alarm_level = None
        self._sql_alarm_send = None
        self._domain_id = None
        self._notification_save_rule = None
        self._trigger_condition_count = None
        self._trigger_condition_frequency = None
        self._whether_recovery_policy = None
        self._recovery_policy = None
        self._notification_frequency = None
        self._alarm_action_rule_name = None
        self.discriminator = None

        self.sql_alarm_rule_name = sql_alarm_rule_name
        if is_css_sql is not None:
            self.is_css_sql = is_css_sql
        if sql_alarm_rule_description is not None:
            self.sql_alarm_rule_description = sql_alarm_rule_description
        self.sql_requests = sql_requests
        self.frequency = frequency
        self.condition_expression = condition_expression
        self.sql_alarm_level = sql_alarm_level
        self.sql_alarm_send = sql_alarm_send
        self.domain_id = domain_id
        if notification_save_rule is not None:
            self.notification_save_rule = notification_save_rule
        if trigger_condition_count is not None:
            self.trigger_condition_count = trigger_condition_count
        if trigger_condition_frequency is not None:
            self.trigger_condition_frequency = trigger_condition_frequency
        if whether_recovery_policy is not None:
            self.whether_recovery_policy = whether_recovery_policy
        if recovery_policy is not None:
            self.recovery_policy = recovery_policy
        self.notification_frequency = notification_frequency
        if alarm_action_rule_name is not None:
            self.alarm_action_rule_name = alarm_action_rule_name

    @property
    def sql_alarm_rule_name(self):
        r"""Gets the sql_alarm_rule_name of this CreateSqlAlarmRuleRequestBody.

        SQL告警名称

        :return: The sql_alarm_rule_name of this CreateSqlAlarmRuleRequestBody.
        :rtype: str
        """
        return self._sql_alarm_rule_name

    @sql_alarm_rule_name.setter
    def sql_alarm_rule_name(self, sql_alarm_rule_name):
        r"""Sets the sql_alarm_rule_name of this CreateSqlAlarmRuleRequestBody.

        SQL告警名称

        :param sql_alarm_rule_name: The sql_alarm_rule_name of this CreateSqlAlarmRuleRequestBody.
        :type sql_alarm_rule_name: str
        """
        self._sql_alarm_rule_name = sql_alarm_rule_name

    @property
    def is_css_sql(self):
        r"""Gets the is_css_sql of this CreateSqlAlarmRuleRequestBody.

        是否管道符sql查询

        :return: The is_css_sql of this CreateSqlAlarmRuleRequestBody.
        :rtype: bool
        """
        return self._is_css_sql

    @is_css_sql.setter
    def is_css_sql(self, is_css_sql):
        r"""Sets the is_css_sql of this CreateSqlAlarmRuleRequestBody.

        是否管道符sql查询

        :param is_css_sql: The is_css_sql of this CreateSqlAlarmRuleRequestBody.
        :type is_css_sql: bool
        """
        self._is_css_sql = is_css_sql

    @property
    def sql_alarm_rule_description(self):
        r"""Gets the sql_alarm_rule_description of this CreateSqlAlarmRuleRequestBody.

        SQL告警信息描述

        :return: The sql_alarm_rule_description of this CreateSqlAlarmRuleRequestBody.
        :rtype: str
        """
        return self._sql_alarm_rule_description

    @sql_alarm_rule_description.setter
    def sql_alarm_rule_description(self, sql_alarm_rule_description):
        r"""Sets the sql_alarm_rule_description of this CreateSqlAlarmRuleRequestBody.

        SQL告警信息描述

        :param sql_alarm_rule_description: The sql_alarm_rule_description of this CreateSqlAlarmRuleRequestBody.
        :type sql_alarm_rule_description: str
        """
        self._sql_alarm_rule_description = sql_alarm_rule_description

    @property
    def sql_requests(self):
        r"""Gets the sql_requests of this CreateSqlAlarmRuleRequestBody.

        SQL详细信息

        :return: The sql_requests of this CreateSqlAlarmRuleRequestBody.
        :rtype: list[:class:`huaweicloudsdklts.v2.SqlRequest`]
        """
        return self._sql_requests

    @sql_requests.setter
    def sql_requests(self, sql_requests):
        r"""Sets the sql_requests of this CreateSqlAlarmRuleRequestBody.

        SQL详细信息

        :param sql_requests: The sql_requests of this CreateSqlAlarmRuleRequestBody.
        :type sql_requests: list[:class:`huaweicloudsdklts.v2.SqlRequest`]
        """
        self._sql_requests = sql_requests

    @property
    def frequency(self):
        r"""Gets the frequency of this CreateSqlAlarmRuleRequestBody.

        :return: The frequency of this CreateSqlAlarmRuleRequestBody.
        :rtype: :class:`huaweicloudsdklts.v2.CreateSqlAlarmRuleFrequency`
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        r"""Sets the frequency of this CreateSqlAlarmRuleRequestBody.

        :param frequency: The frequency of this CreateSqlAlarmRuleRequestBody.
        :type frequency: :class:`huaweicloudsdklts.v2.CreateSqlAlarmRuleFrequency`
        """
        self._frequency = frequency

    @property
    def condition_expression(self):
        r"""Gets the condition_expression of this CreateSqlAlarmRuleRequestBody.

        条件表达式

        :return: The condition_expression of this CreateSqlAlarmRuleRequestBody.
        :rtype: str
        """
        return self._condition_expression

    @condition_expression.setter
    def condition_expression(self, condition_expression):
        r"""Sets the condition_expression of this CreateSqlAlarmRuleRequestBody.

        条件表达式

        :param condition_expression: The condition_expression of this CreateSqlAlarmRuleRequestBody.
        :type condition_expression: str
        """
        self._condition_expression = condition_expression

    @property
    def sql_alarm_level(self):
        r"""Gets the sql_alarm_level of this CreateSqlAlarmRuleRequestBody.

        告警级别

        :return: The sql_alarm_level of this CreateSqlAlarmRuleRequestBody.
        :rtype: str
        """
        return self._sql_alarm_level

    @sql_alarm_level.setter
    def sql_alarm_level(self, sql_alarm_level):
        r"""Sets the sql_alarm_level of this CreateSqlAlarmRuleRequestBody.

        告警级别

        :param sql_alarm_level: The sql_alarm_level of this CreateSqlAlarmRuleRequestBody.
        :type sql_alarm_level: str
        """
        self._sql_alarm_level = sql_alarm_level

    @property
    def sql_alarm_send(self):
        r"""Gets the sql_alarm_send of this CreateSqlAlarmRuleRequestBody.

        是否发送

        :return: The sql_alarm_send of this CreateSqlAlarmRuleRequestBody.
        :rtype: bool
        """
        return self._sql_alarm_send

    @sql_alarm_send.setter
    def sql_alarm_send(self, sql_alarm_send):
        r"""Sets the sql_alarm_send of this CreateSqlAlarmRuleRequestBody.

        是否发送

        :param sql_alarm_send: The sql_alarm_send of this CreateSqlAlarmRuleRequestBody.
        :type sql_alarm_send: bool
        """
        self._sql_alarm_send = sql_alarm_send

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CreateSqlAlarmRuleRequestBody.

        domainId

        :return: The domain_id of this CreateSqlAlarmRuleRequestBody.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CreateSqlAlarmRuleRequestBody.

        domainId

        :param domain_id: The domain_id of this CreateSqlAlarmRuleRequestBody.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def notification_save_rule(self):
        r"""Gets the notification_save_rule of this CreateSqlAlarmRuleRequestBody.

        :return: The notification_save_rule of this CreateSqlAlarmRuleRequestBody.
        :rtype: :class:`huaweicloudsdklts.v2.SqlNotificationSaveRule`
        """
        return self._notification_save_rule

    @notification_save_rule.setter
    def notification_save_rule(self, notification_save_rule):
        r"""Sets the notification_save_rule of this CreateSqlAlarmRuleRequestBody.

        :param notification_save_rule: The notification_save_rule of this CreateSqlAlarmRuleRequestBody.
        :type notification_save_rule: :class:`huaweicloudsdklts.v2.SqlNotificationSaveRule`
        """
        self._notification_save_rule = notification_save_rule

    @property
    def trigger_condition_count(self):
        r"""Gets the trigger_condition_count of this CreateSqlAlarmRuleRequestBody.

        触发条件：触发次数;默认为1

        :return: The trigger_condition_count of this CreateSqlAlarmRuleRequestBody.
        :rtype: int
        """
        return self._trigger_condition_count

    @trigger_condition_count.setter
    def trigger_condition_count(self, trigger_condition_count):
        r"""Sets the trigger_condition_count of this CreateSqlAlarmRuleRequestBody.

        触发条件：触发次数;默认为1

        :param trigger_condition_count: The trigger_condition_count of this CreateSqlAlarmRuleRequestBody.
        :type trigger_condition_count: int
        """
        self._trigger_condition_count = trigger_condition_count

    @property
    def trigger_condition_frequency(self):
        r"""Gets the trigger_condition_frequency of this CreateSqlAlarmRuleRequestBody.

        触发条件：触发周期;默认为1

        :return: The trigger_condition_frequency of this CreateSqlAlarmRuleRequestBody.
        :rtype: int
        """
        return self._trigger_condition_frequency

    @trigger_condition_frequency.setter
    def trigger_condition_frequency(self, trigger_condition_frequency):
        r"""Sets the trigger_condition_frequency of this CreateSqlAlarmRuleRequestBody.

        触发条件：触发周期;默认为1

        :param trigger_condition_frequency: The trigger_condition_frequency of this CreateSqlAlarmRuleRequestBody.
        :type trigger_condition_frequency: int
        """
        self._trigger_condition_frequency = trigger_condition_frequency

    @property
    def whether_recovery_policy(self):
        r"""Gets the whether_recovery_policy of this CreateSqlAlarmRuleRequestBody.

        是否打开恢复通知;默认false

        :return: The whether_recovery_policy of this CreateSqlAlarmRuleRequestBody.
        :rtype: bool
        """
        return self._whether_recovery_policy

    @whether_recovery_policy.setter
    def whether_recovery_policy(self, whether_recovery_policy):
        r"""Sets the whether_recovery_policy of this CreateSqlAlarmRuleRequestBody.

        是否打开恢复通知;默认false

        :param whether_recovery_policy: The whether_recovery_policy of this CreateSqlAlarmRuleRequestBody.
        :type whether_recovery_policy: bool
        """
        self._whether_recovery_policy = whether_recovery_policy

    @property
    def recovery_policy(self):
        r"""Gets the recovery_policy of this CreateSqlAlarmRuleRequestBody.

        恢复策略周期;默认为3

        :return: The recovery_policy of this CreateSqlAlarmRuleRequestBody.
        :rtype: int
        """
        return self._recovery_policy

    @recovery_policy.setter
    def recovery_policy(self, recovery_policy):
        r"""Sets the recovery_policy of this CreateSqlAlarmRuleRequestBody.

        恢复策略周期;默认为3

        :param recovery_policy: The recovery_policy of this CreateSqlAlarmRuleRequestBody.
        :type recovery_policy: int
        """
        self._recovery_policy = recovery_policy

    @property
    def notification_frequency(self):
        r"""Gets the notification_frequency of this CreateSqlAlarmRuleRequestBody.

        通知频率,单位(分钟)

        :return: The notification_frequency of this CreateSqlAlarmRuleRequestBody.
        :rtype: int
        """
        return self._notification_frequency

    @notification_frequency.setter
    def notification_frequency(self, notification_frequency):
        r"""Sets the notification_frequency of this CreateSqlAlarmRuleRequestBody.

        通知频率,单位(分钟)

        :param notification_frequency: The notification_frequency of this CreateSqlAlarmRuleRequestBody.
        :type notification_frequency: int
        """
        self._notification_frequency = notification_frequency

    @property
    def alarm_action_rule_name(self):
        r"""Gets the alarm_action_rule_name of this CreateSqlAlarmRuleRequestBody.

        告警行动规则名称 >alarm_action_rule_name和notification_save_rule可以选填一个，如果都填，优先选择alarm_action_rule_name

        :return: The alarm_action_rule_name of this CreateSqlAlarmRuleRequestBody.
        :rtype: str
        """
        return self._alarm_action_rule_name

    @alarm_action_rule_name.setter
    def alarm_action_rule_name(self, alarm_action_rule_name):
        r"""Sets the alarm_action_rule_name of this CreateSqlAlarmRuleRequestBody.

        告警行动规则名称 >alarm_action_rule_name和notification_save_rule可以选填一个，如果都填，优先选择alarm_action_rule_name

        :param alarm_action_rule_name: The alarm_action_rule_name of this CreateSqlAlarmRuleRequestBody.
        :type alarm_action_rule_name: str
        """
        self._alarm_action_rule_name = alarm_action_rule_name

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
        if not isinstance(other, CreateSqlAlarmRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
