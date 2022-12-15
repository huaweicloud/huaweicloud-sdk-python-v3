# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSqlAlarmRuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_alarm_rule_id': 'str',
        'sql_alarm_rule_name': 'str',
        'sql_alarm_rule_description': 'str',
        'sql_requests': 'list[SqlRequest]',
        'frequency': 'Frequency',
        'condition_expression': 'str',
        'sql_alarm_level': 'str',
        'sql_alarm_send': 'bool',
        'sql_alarm_send_code': 'int',
        'domain_id': 'str',
        'notification_save_rule': 'NotificationSaveRule',
        'trigger_condition_count': 'int',
        'trigger_condition_frequency': 'int',
        'whether_recovery_policy': 'bool',
        'recovery_policy': 'int'
    }

    attribute_map = {
        'sql_alarm_rule_id': 'sql_alarm_rule_id',
        'sql_alarm_rule_name': 'sql_alarm_rule_name',
        'sql_alarm_rule_description': 'sql_alarm_rule_description',
        'sql_requests': 'sql_requests',
        'frequency': 'frequency',
        'condition_expression': 'condition_expression',
        'sql_alarm_level': 'sql_alarm_level',
        'sql_alarm_send': 'sql_alarm_send',
        'sql_alarm_send_code': 'sql_alarm_send_code',
        'domain_id': 'domain_id',
        'notification_save_rule': 'notification_save_rule',
        'trigger_condition_count': 'trigger_condition_count',
        'trigger_condition_frequency': 'trigger_condition_frequency',
        'whether_recovery_policy': 'whether_recovery_policy',
        'recovery_policy': 'recovery_policy'
    }

    def __init__(self, sql_alarm_rule_id=None, sql_alarm_rule_name=None, sql_alarm_rule_description=None, sql_requests=None, frequency=None, condition_expression=None, sql_alarm_level=None, sql_alarm_send=None, sql_alarm_send_code=None, domain_id=None, notification_save_rule=None, trigger_condition_count=None, trigger_condition_frequency=None, whether_recovery_policy=None, recovery_policy=None):
        """UpdateSqlAlarmRuleRequestBody

        The model defined in huaweicloud sdk

        :param sql_alarm_rule_id: SQL告警id
        :type sql_alarm_rule_id: str
        :param sql_alarm_rule_name: SQL告警名称
        :type sql_alarm_rule_name: str
        :param sql_alarm_rule_description: SQL告警信息描述
        :type sql_alarm_rule_description: str
        :param sql_requests: SQL详细信息
        :type sql_requests: list[:class:`huaweicloudsdklts.v2.SqlRequest`]
        :param frequency: 告警统计周期
        :type frequency: :class:`huaweicloudsdklts.v2.Frequency`
        :param condition_expression: 条件表达式
        :type condition_expression: str
        :param sql_alarm_level: 告警级别
        :type sql_alarm_level: str
        :param sql_alarm_send: 是否发送
        :type sql_alarm_send: bool
        :param sql_alarm_send_code: 发送主题 0:不变 1:新增 2:修改 3:删除
        :type sql_alarm_send_code: int
        :param domain_id: domainId
        :type domain_id: str
        :param notification_save_rule: 通知主题
        :type notification_save_rule: :class:`huaweicloudsdklts.v2.NotificationSaveRule`
        :param trigger_condition_count: 触发条件：触发次数;默认为1
        :type trigger_condition_count: int
        :param trigger_condition_frequency: 触发条件：触发周期;默认为1
        :type trigger_condition_frequency: int
        :param whether_recovery_policy: 是否打开恢复通知;默认false
        :type whether_recovery_policy: bool
        :param recovery_policy: 恢复策略周期;默认为3
        :type recovery_policy: int
        """
        
        

        self._sql_alarm_rule_id = None
        self._sql_alarm_rule_name = None
        self._sql_alarm_rule_description = None
        self._sql_requests = None
        self._frequency = None
        self._condition_expression = None
        self._sql_alarm_level = None
        self._sql_alarm_send = None
        self._sql_alarm_send_code = None
        self._domain_id = None
        self._notification_save_rule = None
        self._trigger_condition_count = None
        self._trigger_condition_frequency = None
        self._whether_recovery_policy = None
        self._recovery_policy = None
        self.discriminator = None

        self.sql_alarm_rule_id = sql_alarm_rule_id
        self.sql_alarm_rule_name = sql_alarm_rule_name
        if sql_alarm_rule_description is not None:
            self.sql_alarm_rule_description = sql_alarm_rule_description
        self.sql_requests = sql_requests
        self.frequency = frequency
        self.condition_expression = condition_expression
        self.sql_alarm_level = sql_alarm_level
        self.sql_alarm_send = sql_alarm_send
        self.sql_alarm_send_code = sql_alarm_send_code
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

    @property
    def sql_alarm_rule_id(self):
        """Gets the sql_alarm_rule_id of this UpdateSqlAlarmRuleRequestBody.

        SQL告警id

        :return: The sql_alarm_rule_id of this UpdateSqlAlarmRuleRequestBody.
        :rtype: str
        """
        return self._sql_alarm_rule_id

    @sql_alarm_rule_id.setter
    def sql_alarm_rule_id(self, sql_alarm_rule_id):
        """Sets the sql_alarm_rule_id of this UpdateSqlAlarmRuleRequestBody.

        SQL告警id

        :param sql_alarm_rule_id: The sql_alarm_rule_id of this UpdateSqlAlarmRuleRequestBody.
        :type sql_alarm_rule_id: str
        """
        self._sql_alarm_rule_id = sql_alarm_rule_id

    @property
    def sql_alarm_rule_name(self):
        """Gets the sql_alarm_rule_name of this UpdateSqlAlarmRuleRequestBody.

        SQL告警名称

        :return: The sql_alarm_rule_name of this UpdateSqlAlarmRuleRequestBody.
        :rtype: str
        """
        return self._sql_alarm_rule_name

    @sql_alarm_rule_name.setter
    def sql_alarm_rule_name(self, sql_alarm_rule_name):
        """Sets the sql_alarm_rule_name of this UpdateSqlAlarmRuleRequestBody.

        SQL告警名称

        :param sql_alarm_rule_name: The sql_alarm_rule_name of this UpdateSqlAlarmRuleRequestBody.
        :type sql_alarm_rule_name: str
        """
        self._sql_alarm_rule_name = sql_alarm_rule_name

    @property
    def sql_alarm_rule_description(self):
        """Gets the sql_alarm_rule_description of this UpdateSqlAlarmRuleRequestBody.

        SQL告警信息描述

        :return: The sql_alarm_rule_description of this UpdateSqlAlarmRuleRequestBody.
        :rtype: str
        """
        return self._sql_alarm_rule_description

    @sql_alarm_rule_description.setter
    def sql_alarm_rule_description(self, sql_alarm_rule_description):
        """Sets the sql_alarm_rule_description of this UpdateSqlAlarmRuleRequestBody.

        SQL告警信息描述

        :param sql_alarm_rule_description: The sql_alarm_rule_description of this UpdateSqlAlarmRuleRequestBody.
        :type sql_alarm_rule_description: str
        """
        self._sql_alarm_rule_description = sql_alarm_rule_description

    @property
    def sql_requests(self):
        """Gets the sql_requests of this UpdateSqlAlarmRuleRequestBody.

        SQL详细信息

        :return: The sql_requests of this UpdateSqlAlarmRuleRequestBody.
        :rtype: list[:class:`huaweicloudsdklts.v2.SqlRequest`]
        """
        return self._sql_requests

    @sql_requests.setter
    def sql_requests(self, sql_requests):
        """Sets the sql_requests of this UpdateSqlAlarmRuleRequestBody.

        SQL详细信息

        :param sql_requests: The sql_requests of this UpdateSqlAlarmRuleRequestBody.
        :type sql_requests: list[:class:`huaweicloudsdklts.v2.SqlRequest`]
        """
        self._sql_requests = sql_requests

    @property
    def frequency(self):
        """Gets the frequency of this UpdateSqlAlarmRuleRequestBody.

        告警统计周期

        :return: The frequency of this UpdateSqlAlarmRuleRequestBody.
        :rtype: :class:`huaweicloudsdklts.v2.Frequency`
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this UpdateSqlAlarmRuleRequestBody.

        告警统计周期

        :param frequency: The frequency of this UpdateSqlAlarmRuleRequestBody.
        :type frequency: :class:`huaweicloudsdklts.v2.Frequency`
        """
        self._frequency = frequency

    @property
    def condition_expression(self):
        """Gets the condition_expression of this UpdateSqlAlarmRuleRequestBody.

        条件表达式

        :return: The condition_expression of this UpdateSqlAlarmRuleRequestBody.
        :rtype: str
        """
        return self._condition_expression

    @condition_expression.setter
    def condition_expression(self, condition_expression):
        """Sets the condition_expression of this UpdateSqlAlarmRuleRequestBody.

        条件表达式

        :param condition_expression: The condition_expression of this UpdateSqlAlarmRuleRequestBody.
        :type condition_expression: str
        """
        self._condition_expression = condition_expression

    @property
    def sql_alarm_level(self):
        """Gets the sql_alarm_level of this UpdateSqlAlarmRuleRequestBody.

        告警级别

        :return: The sql_alarm_level of this UpdateSqlAlarmRuleRequestBody.
        :rtype: str
        """
        return self._sql_alarm_level

    @sql_alarm_level.setter
    def sql_alarm_level(self, sql_alarm_level):
        """Sets the sql_alarm_level of this UpdateSqlAlarmRuleRequestBody.

        告警级别

        :param sql_alarm_level: The sql_alarm_level of this UpdateSqlAlarmRuleRequestBody.
        :type sql_alarm_level: str
        """
        self._sql_alarm_level = sql_alarm_level

    @property
    def sql_alarm_send(self):
        """Gets the sql_alarm_send of this UpdateSqlAlarmRuleRequestBody.

        是否发送

        :return: The sql_alarm_send of this UpdateSqlAlarmRuleRequestBody.
        :rtype: bool
        """
        return self._sql_alarm_send

    @sql_alarm_send.setter
    def sql_alarm_send(self, sql_alarm_send):
        """Sets the sql_alarm_send of this UpdateSqlAlarmRuleRequestBody.

        是否发送

        :param sql_alarm_send: The sql_alarm_send of this UpdateSqlAlarmRuleRequestBody.
        :type sql_alarm_send: bool
        """
        self._sql_alarm_send = sql_alarm_send

    @property
    def sql_alarm_send_code(self):
        """Gets the sql_alarm_send_code of this UpdateSqlAlarmRuleRequestBody.

        发送主题 0:不变 1:新增 2:修改 3:删除

        :return: The sql_alarm_send_code of this UpdateSqlAlarmRuleRequestBody.
        :rtype: int
        """
        return self._sql_alarm_send_code

    @sql_alarm_send_code.setter
    def sql_alarm_send_code(self, sql_alarm_send_code):
        """Sets the sql_alarm_send_code of this UpdateSqlAlarmRuleRequestBody.

        发送主题 0:不变 1:新增 2:修改 3:删除

        :param sql_alarm_send_code: The sql_alarm_send_code of this UpdateSqlAlarmRuleRequestBody.
        :type sql_alarm_send_code: int
        """
        self._sql_alarm_send_code = sql_alarm_send_code

    @property
    def domain_id(self):
        """Gets the domain_id of this UpdateSqlAlarmRuleRequestBody.

        domainId

        :return: The domain_id of this UpdateSqlAlarmRuleRequestBody.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this UpdateSqlAlarmRuleRequestBody.

        domainId

        :param domain_id: The domain_id of this UpdateSqlAlarmRuleRequestBody.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def notification_save_rule(self):
        """Gets the notification_save_rule of this UpdateSqlAlarmRuleRequestBody.

        通知主题

        :return: The notification_save_rule of this UpdateSqlAlarmRuleRequestBody.
        :rtype: :class:`huaweicloudsdklts.v2.NotificationSaveRule`
        """
        return self._notification_save_rule

    @notification_save_rule.setter
    def notification_save_rule(self, notification_save_rule):
        """Sets the notification_save_rule of this UpdateSqlAlarmRuleRequestBody.

        通知主题

        :param notification_save_rule: The notification_save_rule of this UpdateSqlAlarmRuleRequestBody.
        :type notification_save_rule: :class:`huaweicloudsdklts.v2.NotificationSaveRule`
        """
        self._notification_save_rule = notification_save_rule

    @property
    def trigger_condition_count(self):
        """Gets the trigger_condition_count of this UpdateSqlAlarmRuleRequestBody.

        触发条件：触发次数;默认为1

        :return: The trigger_condition_count of this UpdateSqlAlarmRuleRequestBody.
        :rtype: int
        """
        return self._trigger_condition_count

    @trigger_condition_count.setter
    def trigger_condition_count(self, trigger_condition_count):
        """Sets the trigger_condition_count of this UpdateSqlAlarmRuleRequestBody.

        触发条件：触发次数;默认为1

        :param trigger_condition_count: The trigger_condition_count of this UpdateSqlAlarmRuleRequestBody.
        :type trigger_condition_count: int
        """
        self._trigger_condition_count = trigger_condition_count

    @property
    def trigger_condition_frequency(self):
        """Gets the trigger_condition_frequency of this UpdateSqlAlarmRuleRequestBody.

        触发条件：触发周期;默认为1

        :return: The trigger_condition_frequency of this UpdateSqlAlarmRuleRequestBody.
        :rtype: int
        """
        return self._trigger_condition_frequency

    @trigger_condition_frequency.setter
    def trigger_condition_frequency(self, trigger_condition_frequency):
        """Sets the trigger_condition_frequency of this UpdateSqlAlarmRuleRequestBody.

        触发条件：触发周期;默认为1

        :param trigger_condition_frequency: The trigger_condition_frequency of this UpdateSqlAlarmRuleRequestBody.
        :type trigger_condition_frequency: int
        """
        self._trigger_condition_frequency = trigger_condition_frequency

    @property
    def whether_recovery_policy(self):
        """Gets the whether_recovery_policy of this UpdateSqlAlarmRuleRequestBody.

        是否打开恢复通知;默认false

        :return: The whether_recovery_policy of this UpdateSqlAlarmRuleRequestBody.
        :rtype: bool
        """
        return self._whether_recovery_policy

    @whether_recovery_policy.setter
    def whether_recovery_policy(self, whether_recovery_policy):
        """Sets the whether_recovery_policy of this UpdateSqlAlarmRuleRequestBody.

        是否打开恢复通知;默认false

        :param whether_recovery_policy: The whether_recovery_policy of this UpdateSqlAlarmRuleRequestBody.
        :type whether_recovery_policy: bool
        """
        self._whether_recovery_policy = whether_recovery_policy

    @property
    def recovery_policy(self):
        """Gets the recovery_policy of this UpdateSqlAlarmRuleRequestBody.

        恢复策略周期;默认为3

        :return: The recovery_policy of this UpdateSqlAlarmRuleRequestBody.
        :rtype: int
        """
        return self._recovery_policy

    @recovery_policy.setter
    def recovery_policy(self, recovery_policy):
        """Sets the recovery_policy of this UpdateSqlAlarmRuleRequestBody.

        恢复策略周期;默认为3

        :param recovery_policy: The recovery_policy of this UpdateSqlAlarmRuleRequestBody.
        :type recovery_policy: int
        """
        self._recovery_policy = recovery_policy

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
        if not isinstance(other, UpdateSqlAlarmRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
