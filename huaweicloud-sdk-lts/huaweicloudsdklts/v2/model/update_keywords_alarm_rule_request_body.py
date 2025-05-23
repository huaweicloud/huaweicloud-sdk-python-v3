# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateKeywordsAlarmRuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keywords_alarm_rule_id': 'str',
        'keywords_alarm_rule_name': 'str',
        'alarm_rule_alias': 'str',
        'keywords_alarm_rule_description': 'str',
        'keywords_requests': 'list[KeywordsRequest]',
        'frequency': 'Frequency',
        'keywords_alarm_level': 'str',
        'keywords_alarm_send': 'bool',
        'keywords_alarm_send_code': 'int',
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
        'keywords_alarm_rule_id': 'keywords_alarm_rule_id',
        'keywords_alarm_rule_name': 'keywords_alarm_rule_name',
        'alarm_rule_alias': 'alarm_rule_alias',
        'keywords_alarm_rule_description': 'keywords_alarm_rule_description',
        'keywords_requests': 'keywords_requests',
        'frequency': 'frequency',
        'keywords_alarm_level': 'keywords_alarm_level',
        'keywords_alarm_send': 'keywords_alarm_send',
        'keywords_alarm_send_code': 'keywords_alarm_send_code',
        'domain_id': 'domain_id',
        'notification_save_rule': 'notification_save_rule',
        'trigger_condition_count': 'trigger_condition_count',
        'trigger_condition_frequency': 'trigger_condition_frequency',
        'whether_recovery_policy': 'whether_recovery_policy',
        'recovery_policy': 'recovery_policy',
        'notification_frequency': 'notification_frequency',
        'alarm_action_rule_name': 'alarm_action_rule_name'
    }

    def __init__(self, keywords_alarm_rule_id=None, keywords_alarm_rule_name=None, alarm_rule_alias=None, keywords_alarm_rule_description=None, keywords_requests=None, frequency=None, keywords_alarm_level=None, keywords_alarm_send=None, keywords_alarm_send_code=None, domain_id=None, notification_save_rule=None, trigger_condition_count=None, trigger_condition_frequency=None, whether_recovery_policy=None, recovery_policy=None, notification_frequency=None, alarm_action_rule_name=None):
        r"""UpdateKeywordsAlarmRuleRequestBody

        The model defined in huaweicloud sdk

        :param keywords_alarm_rule_id: 关键词告警规则id
        :type keywords_alarm_rule_id: str
        :param keywords_alarm_rule_name: 关键词告警名称
        :type keywords_alarm_rule_name: str
        :param alarm_rule_alias: 规则名称
        :type alarm_rule_alias: str
        :param keywords_alarm_rule_description: 关键词告警信息描述
        :type keywords_alarm_rule_description: str
        :param keywords_requests: 关键词详细信息
        :type keywords_requests: list[:class:`huaweicloudsdklts.v2.KeywordsRequest`]
        :param frequency: 
        :type frequency: :class:`huaweicloudsdklts.v2.Frequency`
        :param keywords_alarm_level: 告警级别
        :type keywords_alarm_level: str
        :param keywords_alarm_send: 是否发送
        :type keywords_alarm_send: bool
        :param keywords_alarm_send_code: 发送主题 0:不变 1:新增 2:修改 3:删除
        :type keywords_alarm_send_code: int
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
        
        

        self._keywords_alarm_rule_id = None
        self._keywords_alarm_rule_name = None
        self._alarm_rule_alias = None
        self._keywords_alarm_rule_description = None
        self._keywords_requests = None
        self._frequency = None
        self._keywords_alarm_level = None
        self._keywords_alarm_send = None
        self._keywords_alarm_send_code = None
        self._domain_id = None
        self._notification_save_rule = None
        self._trigger_condition_count = None
        self._trigger_condition_frequency = None
        self._whether_recovery_policy = None
        self._recovery_policy = None
        self._notification_frequency = None
        self._alarm_action_rule_name = None
        self.discriminator = None

        self.keywords_alarm_rule_id = keywords_alarm_rule_id
        self.keywords_alarm_rule_name = keywords_alarm_rule_name
        if alarm_rule_alias is not None:
            self.alarm_rule_alias = alarm_rule_alias
        if keywords_alarm_rule_description is not None:
            self.keywords_alarm_rule_description = keywords_alarm_rule_description
        self.keywords_requests = keywords_requests
        self.frequency = frequency
        self.keywords_alarm_level = keywords_alarm_level
        self.keywords_alarm_send = keywords_alarm_send
        self.keywords_alarm_send_code = keywords_alarm_send_code
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
    def keywords_alarm_rule_id(self):
        r"""Gets the keywords_alarm_rule_id of this UpdateKeywordsAlarmRuleRequestBody.

        关键词告警规则id

        :return: The keywords_alarm_rule_id of this UpdateKeywordsAlarmRuleRequestBody.
        :rtype: str
        """
        return self._keywords_alarm_rule_id

    @keywords_alarm_rule_id.setter
    def keywords_alarm_rule_id(self, keywords_alarm_rule_id):
        r"""Sets the keywords_alarm_rule_id of this UpdateKeywordsAlarmRuleRequestBody.

        关键词告警规则id

        :param keywords_alarm_rule_id: The keywords_alarm_rule_id of this UpdateKeywordsAlarmRuleRequestBody.
        :type keywords_alarm_rule_id: str
        """
        self._keywords_alarm_rule_id = keywords_alarm_rule_id

    @property
    def keywords_alarm_rule_name(self):
        r"""Gets the keywords_alarm_rule_name of this UpdateKeywordsAlarmRuleRequestBody.

        关键词告警名称

        :return: The keywords_alarm_rule_name of this UpdateKeywordsAlarmRuleRequestBody.
        :rtype: str
        """
        return self._keywords_alarm_rule_name

    @keywords_alarm_rule_name.setter
    def keywords_alarm_rule_name(self, keywords_alarm_rule_name):
        r"""Sets the keywords_alarm_rule_name of this UpdateKeywordsAlarmRuleRequestBody.

        关键词告警名称

        :param keywords_alarm_rule_name: The keywords_alarm_rule_name of this UpdateKeywordsAlarmRuleRequestBody.
        :type keywords_alarm_rule_name: str
        """
        self._keywords_alarm_rule_name = keywords_alarm_rule_name

    @property
    def alarm_rule_alias(self):
        r"""Gets the alarm_rule_alias of this UpdateKeywordsAlarmRuleRequestBody.

        规则名称

        :return: The alarm_rule_alias of this UpdateKeywordsAlarmRuleRequestBody.
        :rtype: str
        """
        return self._alarm_rule_alias

    @alarm_rule_alias.setter
    def alarm_rule_alias(self, alarm_rule_alias):
        r"""Sets the alarm_rule_alias of this UpdateKeywordsAlarmRuleRequestBody.

        规则名称

        :param alarm_rule_alias: The alarm_rule_alias of this UpdateKeywordsAlarmRuleRequestBody.
        :type alarm_rule_alias: str
        """
        self._alarm_rule_alias = alarm_rule_alias

    @property
    def keywords_alarm_rule_description(self):
        r"""Gets the keywords_alarm_rule_description of this UpdateKeywordsAlarmRuleRequestBody.

        关键词告警信息描述

        :return: The keywords_alarm_rule_description of this UpdateKeywordsAlarmRuleRequestBody.
        :rtype: str
        """
        return self._keywords_alarm_rule_description

    @keywords_alarm_rule_description.setter
    def keywords_alarm_rule_description(self, keywords_alarm_rule_description):
        r"""Sets the keywords_alarm_rule_description of this UpdateKeywordsAlarmRuleRequestBody.

        关键词告警信息描述

        :param keywords_alarm_rule_description: The keywords_alarm_rule_description of this UpdateKeywordsAlarmRuleRequestBody.
        :type keywords_alarm_rule_description: str
        """
        self._keywords_alarm_rule_description = keywords_alarm_rule_description

    @property
    def keywords_requests(self):
        r"""Gets the keywords_requests of this UpdateKeywordsAlarmRuleRequestBody.

        关键词详细信息

        :return: The keywords_requests of this UpdateKeywordsAlarmRuleRequestBody.
        :rtype: list[:class:`huaweicloudsdklts.v2.KeywordsRequest`]
        """
        return self._keywords_requests

    @keywords_requests.setter
    def keywords_requests(self, keywords_requests):
        r"""Sets the keywords_requests of this UpdateKeywordsAlarmRuleRequestBody.

        关键词详细信息

        :param keywords_requests: The keywords_requests of this UpdateKeywordsAlarmRuleRequestBody.
        :type keywords_requests: list[:class:`huaweicloudsdklts.v2.KeywordsRequest`]
        """
        self._keywords_requests = keywords_requests

    @property
    def frequency(self):
        r"""Gets the frequency of this UpdateKeywordsAlarmRuleRequestBody.

        :return: The frequency of this UpdateKeywordsAlarmRuleRequestBody.
        :rtype: :class:`huaweicloudsdklts.v2.Frequency`
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        r"""Sets the frequency of this UpdateKeywordsAlarmRuleRequestBody.

        :param frequency: The frequency of this UpdateKeywordsAlarmRuleRequestBody.
        :type frequency: :class:`huaweicloudsdklts.v2.Frequency`
        """
        self._frequency = frequency

    @property
    def keywords_alarm_level(self):
        r"""Gets the keywords_alarm_level of this UpdateKeywordsAlarmRuleRequestBody.

        告警级别

        :return: The keywords_alarm_level of this UpdateKeywordsAlarmRuleRequestBody.
        :rtype: str
        """
        return self._keywords_alarm_level

    @keywords_alarm_level.setter
    def keywords_alarm_level(self, keywords_alarm_level):
        r"""Sets the keywords_alarm_level of this UpdateKeywordsAlarmRuleRequestBody.

        告警级别

        :param keywords_alarm_level: The keywords_alarm_level of this UpdateKeywordsAlarmRuleRequestBody.
        :type keywords_alarm_level: str
        """
        self._keywords_alarm_level = keywords_alarm_level

    @property
    def keywords_alarm_send(self):
        r"""Gets the keywords_alarm_send of this UpdateKeywordsAlarmRuleRequestBody.

        是否发送

        :return: The keywords_alarm_send of this UpdateKeywordsAlarmRuleRequestBody.
        :rtype: bool
        """
        return self._keywords_alarm_send

    @keywords_alarm_send.setter
    def keywords_alarm_send(self, keywords_alarm_send):
        r"""Sets the keywords_alarm_send of this UpdateKeywordsAlarmRuleRequestBody.

        是否发送

        :param keywords_alarm_send: The keywords_alarm_send of this UpdateKeywordsAlarmRuleRequestBody.
        :type keywords_alarm_send: bool
        """
        self._keywords_alarm_send = keywords_alarm_send

    @property
    def keywords_alarm_send_code(self):
        r"""Gets the keywords_alarm_send_code of this UpdateKeywordsAlarmRuleRequestBody.

        发送主题 0:不变 1:新增 2:修改 3:删除

        :return: The keywords_alarm_send_code of this UpdateKeywordsAlarmRuleRequestBody.
        :rtype: int
        """
        return self._keywords_alarm_send_code

    @keywords_alarm_send_code.setter
    def keywords_alarm_send_code(self, keywords_alarm_send_code):
        r"""Sets the keywords_alarm_send_code of this UpdateKeywordsAlarmRuleRequestBody.

        发送主题 0:不变 1:新增 2:修改 3:删除

        :param keywords_alarm_send_code: The keywords_alarm_send_code of this UpdateKeywordsAlarmRuleRequestBody.
        :type keywords_alarm_send_code: int
        """
        self._keywords_alarm_send_code = keywords_alarm_send_code

    @property
    def domain_id(self):
        r"""Gets the domain_id of this UpdateKeywordsAlarmRuleRequestBody.

        domainId

        :return: The domain_id of this UpdateKeywordsAlarmRuleRequestBody.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this UpdateKeywordsAlarmRuleRequestBody.

        domainId

        :param domain_id: The domain_id of this UpdateKeywordsAlarmRuleRequestBody.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def notification_save_rule(self):
        r"""Gets the notification_save_rule of this UpdateKeywordsAlarmRuleRequestBody.

        :return: The notification_save_rule of this UpdateKeywordsAlarmRuleRequestBody.
        :rtype: :class:`huaweicloudsdklts.v2.SqlNotificationSaveRule`
        """
        return self._notification_save_rule

    @notification_save_rule.setter
    def notification_save_rule(self, notification_save_rule):
        r"""Sets the notification_save_rule of this UpdateKeywordsAlarmRuleRequestBody.

        :param notification_save_rule: The notification_save_rule of this UpdateKeywordsAlarmRuleRequestBody.
        :type notification_save_rule: :class:`huaweicloudsdklts.v2.SqlNotificationSaveRule`
        """
        self._notification_save_rule = notification_save_rule

    @property
    def trigger_condition_count(self):
        r"""Gets the trigger_condition_count of this UpdateKeywordsAlarmRuleRequestBody.

        触发条件：触发次数;默认为1

        :return: The trigger_condition_count of this UpdateKeywordsAlarmRuleRequestBody.
        :rtype: int
        """
        return self._trigger_condition_count

    @trigger_condition_count.setter
    def trigger_condition_count(self, trigger_condition_count):
        r"""Sets the trigger_condition_count of this UpdateKeywordsAlarmRuleRequestBody.

        触发条件：触发次数;默认为1

        :param trigger_condition_count: The trigger_condition_count of this UpdateKeywordsAlarmRuleRequestBody.
        :type trigger_condition_count: int
        """
        self._trigger_condition_count = trigger_condition_count

    @property
    def trigger_condition_frequency(self):
        r"""Gets the trigger_condition_frequency of this UpdateKeywordsAlarmRuleRequestBody.

        触发条件：触发周期;默认为1

        :return: The trigger_condition_frequency of this UpdateKeywordsAlarmRuleRequestBody.
        :rtype: int
        """
        return self._trigger_condition_frequency

    @trigger_condition_frequency.setter
    def trigger_condition_frequency(self, trigger_condition_frequency):
        r"""Sets the trigger_condition_frequency of this UpdateKeywordsAlarmRuleRequestBody.

        触发条件：触发周期;默认为1

        :param trigger_condition_frequency: The trigger_condition_frequency of this UpdateKeywordsAlarmRuleRequestBody.
        :type trigger_condition_frequency: int
        """
        self._trigger_condition_frequency = trigger_condition_frequency

    @property
    def whether_recovery_policy(self):
        r"""Gets the whether_recovery_policy of this UpdateKeywordsAlarmRuleRequestBody.

        是否打开恢复通知;默认false

        :return: The whether_recovery_policy of this UpdateKeywordsAlarmRuleRequestBody.
        :rtype: bool
        """
        return self._whether_recovery_policy

    @whether_recovery_policy.setter
    def whether_recovery_policy(self, whether_recovery_policy):
        r"""Sets the whether_recovery_policy of this UpdateKeywordsAlarmRuleRequestBody.

        是否打开恢复通知;默认false

        :param whether_recovery_policy: The whether_recovery_policy of this UpdateKeywordsAlarmRuleRequestBody.
        :type whether_recovery_policy: bool
        """
        self._whether_recovery_policy = whether_recovery_policy

    @property
    def recovery_policy(self):
        r"""Gets the recovery_policy of this UpdateKeywordsAlarmRuleRequestBody.

        恢复策略周期;默认为3

        :return: The recovery_policy of this UpdateKeywordsAlarmRuleRequestBody.
        :rtype: int
        """
        return self._recovery_policy

    @recovery_policy.setter
    def recovery_policy(self, recovery_policy):
        r"""Sets the recovery_policy of this UpdateKeywordsAlarmRuleRequestBody.

        恢复策略周期;默认为3

        :param recovery_policy: The recovery_policy of this UpdateKeywordsAlarmRuleRequestBody.
        :type recovery_policy: int
        """
        self._recovery_policy = recovery_policy

    @property
    def notification_frequency(self):
        r"""Gets the notification_frequency of this UpdateKeywordsAlarmRuleRequestBody.

        通知频率,单位(分钟)

        :return: The notification_frequency of this UpdateKeywordsAlarmRuleRequestBody.
        :rtype: int
        """
        return self._notification_frequency

    @notification_frequency.setter
    def notification_frequency(self, notification_frequency):
        r"""Sets the notification_frequency of this UpdateKeywordsAlarmRuleRequestBody.

        通知频率,单位(分钟)

        :param notification_frequency: The notification_frequency of this UpdateKeywordsAlarmRuleRequestBody.
        :type notification_frequency: int
        """
        self._notification_frequency = notification_frequency

    @property
    def alarm_action_rule_name(self):
        r"""Gets the alarm_action_rule_name of this UpdateKeywordsAlarmRuleRequestBody.

        告警行动规则名称 >alarm_action_rule_name和notification_save_rule可以选填一个，如果都填，优先选择alarm_action_rule_name

        :return: The alarm_action_rule_name of this UpdateKeywordsAlarmRuleRequestBody.
        :rtype: str
        """
        return self._alarm_action_rule_name

    @alarm_action_rule_name.setter
    def alarm_action_rule_name(self, alarm_action_rule_name):
        r"""Sets the alarm_action_rule_name of this UpdateKeywordsAlarmRuleRequestBody.

        告警行动规则名称 >alarm_action_rule_name和notification_save_rule可以选填一个，如果都填，优先选择alarm_action_rule_name

        :param alarm_action_rule_name: The alarm_action_rule_name of this UpdateKeywordsAlarmRuleRequestBody.
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
        if not isinstance(other, UpdateKeywordsAlarmRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
