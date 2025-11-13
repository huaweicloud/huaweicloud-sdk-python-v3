# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeywordsAlarmRuleRespList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'keywords_alarm_rule_id': 'str',
        'keywords_alarm_rule_name': 'str',
        'keywords_alarm_rule_description': 'str',
        'condition_expression': 'str',
        'keywords_requests': 'list[KeywordsRequestResponse]',
        'frequency': 'Frequency',
        'keywords_alarm_level': 'str',
        'domain_id': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'status': 'str',
        'trigger_condition_count': 'int',
        'trigger_condition_frequency': 'int',
        'whether_recovery_policy': 'bool',
        'recovery_policy': 'int',
        'notification_frequency': 'int',
        'alarm_action_rule_name': 'str',
        'tags': 'list[TagsResBody]'
    }

    attribute_map = {
        'project_id': 'projectId',
        'keywords_alarm_rule_id': 'keywords_alarm_rule_id',
        'keywords_alarm_rule_name': 'keywords_alarm_rule_name',
        'keywords_alarm_rule_description': 'keywords_alarm_rule_description',
        'condition_expression': 'condition_expression',
        'keywords_requests': 'keywords_requests',
        'frequency': 'frequency',
        'keywords_alarm_level': 'keywords_alarm_level',
        'domain_id': 'domain_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'status': 'status',
        'trigger_condition_count': 'trigger_condition_count',
        'trigger_condition_frequency': 'trigger_condition_frequency',
        'whether_recovery_policy': 'whether_recovery_policy',
        'recovery_policy': 'recovery_policy',
        'notification_frequency': 'notification_frequency',
        'alarm_action_rule_name': 'alarm_action_rule_name',
        'tags': 'tags'
    }

    def __init__(self, project_id=None, keywords_alarm_rule_id=None, keywords_alarm_rule_name=None, keywords_alarm_rule_description=None, condition_expression=None, keywords_requests=None, frequency=None, keywords_alarm_level=None, domain_id=None, create_time=None, update_time=None, status=None, trigger_condition_count=None, trigger_condition_frequency=None, whether_recovery_policy=None, recovery_policy=None, notification_frequency=None, alarm_action_rule_name=None, tags=None):
        r"""KeywordsAlarmRuleRespList

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param keywords_alarm_rule_id: 关键词告警id
        :type keywords_alarm_rule_id: str
        :param keywords_alarm_rule_name: 关键词告警名称
        :type keywords_alarm_rule_name: str
        :param keywords_alarm_rule_description: 关键词告警信息描述
        :type keywords_alarm_rule_description: str
        :param condition_expression: 条件
        :type condition_expression: str
        :param keywords_requests: 关键词详细信息
        :type keywords_requests: list[:class:`huaweicloudsdklts.v2.KeywordsRequestResponse`]
        :param frequency: 
        :type frequency: :class:`huaweicloudsdklts.v2.Frequency`
        :param keywords_alarm_level: 告警级别
        :type keywords_alarm_level: str
        :param domain_id: domainId
        :type domain_id: str
        :param create_time: 创建时间（毫秒时间戳）
        :type create_time: int
        :param update_time: 更新时间（毫秒时间戳）
        :type update_time: int
        :param status: 告警状态
        :type status: str
        :param trigger_condition_count: 触发条件：触发周期;默认为1
        :type trigger_condition_count: int
        :param trigger_condition_frequency: 触发条件：触发次数;默认为1
        :type trigger_condition_frequency: int
        :param whether_recovery_policy: 是否打开恢复通知;默认false
        :type whether_recovery_policy: bool
        :param recovery_policy: 恢复策略周期;默认为3
        :type recovery_policy: int
        :param notification_frequency: 通知频率,单位(分钟)
        :type notification_frequency: int
        :param alarm_action_rule_name: 告警行动规则名称 &gt;alarm_action_rule_name和notification_save_rule可以选填一个，如果都填，优先选择alarm_action_rule_name
        :type alarm_action_rule_name: str
        :param tags: **参数解释：** 告警标签信息。标签是以键值对（key-value）的形式表示，key和value为一一对应关系。
        :type tags: list[:class:`huaweicloudsdklts.v2.TagsResBody`]
        """
        
        

        self._project_id = None
        self._keywords_alarm_rule_id = None
        self._keywords_alarm_rule_name = None
        self._keywords_alarm_rule_description = None
        self._condition_expression = None
        self._keywords_requests = None
        self._frequency = None
        self._keywords_alarm_level = None
        self._domain_id = None
        self._create_time = None
        self._update_time = None
        self._status = None
        self._trigger_condition_count = None
        self._trigger_condition_frequency = None
        self._whether_recovery_policy = None
        self._recovery_policy = None
        self._notification_frequency = None
        self._alarm_action_rule_name = None
        self._tags = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        self.keywords_alarm_rule_id = keywords_alarm_rule_id
        self.keywords_alarm_rule_name = keywords_alarm_rule_name
        self.keywords_alarm_rule_description = keywords_alarm_rule_description
        self.condition_expression = condition_expression
        self.keywords_requests = keywords_requests
        self.frequency = frequency
        self.keywords_alarm_level = keywords_alarm_level
        self.domain_id = domain_id
        self.create_time = create_time
        self.update_time = update_time
        if status is not None:
            self.status = status
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
        if tags is not None:
            self.tags = tags

    @property
    def project_id(self):
        r"""Gets the project_id of this KeywordsAlarmRuleRespList.

        项目id

        :return: The project_id of this KeywordsAlarmRuleRespList.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this KeywordsAlarmRuleRespList.

        项目id

        :param project_id: The project_id of this KeywordsAlarmRuleRespList.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def keywords_alarm_rule_id(self):
        r"""Gets the keywords_alarm_rule_id of this KeywordsAlarmRuleRespList.

        关键词告警id

        :return: The keywords_alarm_rule_id of this KeywordsAlarmRuleRespList.
        :rtype: str
        """
        return self._keywords_alarm_rule_id

    @keywords_alarm_rule_id.setter
    def keywords_alarm_rule_id(self, keywords_alarm_rule_id):
        r"""Sets the keywords_alarm_rule_id of this KeywordsAlarmRuleRespList.

        关键词告警id

        :param keywords_alarm_rule_id: The keywords_alarm_rule_id of this KeywordsAlarmRuleRespList.
        :type keywords_alarm_rule_id: str
        """
        self._keywords_alarm_rule_id = keywords_alarm_rule_id

    @property
    def keywords_alarm_rule_name(self):
        r"""Gets the keywords_alarm_rule_name of this KeywordsAlarmRuleRespList.

        关键词告警名称

        :return: The keywords_alarm_rule_name of this KeywordsAlarmRuleRespList.
        :rtype: str
        """
        return self._keywords_alarm_rule_name

    @keywords_alarm_rule_name.setter
    def keywords_alarm_rule_name(self, keywords_alarm_rule_name):
        r"""Sets the keywords_alarm_rule_name of this KeywordsAlarmRuleRespList.

        关键词告警名称

        :param keywords_alarm_rule_name: The keywords_alarm_rule_name of this KeywordsAlarmRuleRespList.
        :type keywords_alarm_rule_name: str
        """
        self._keywords_alarm_rule_name = keywords_alarm_rule_name

    @property
    def keywords_alarm_rule_description(self):
        r"""Gets the keywords_alarm_rule_description of this KeywordsAlarmRuleRespList.

        关键词告警信息描述

        :return: The keywords_alarm_rule_description of this KeywordsAlarmRuleRespList.
        :rtype: str
        """
        return self._keywords_alarm_rule_description

    @keywords_alarm_rule_description.setter
    def keywords_alarm_rule_description(self, keywords_alarm_rule_description):
        r"""Sets the keywords_alarm_rule_description of this KeywordsAlarmRuleRespList.

        关键词告警信息描述

        :param keywords_alarm_rule_description: The keywords_alarm_rule_description of this KeywordsAlarmRuleRespList.
        :type keywords_alarm_rule_description: str
        """
        self._keywords_alarm_rule_description = keywords_alarm_rule_description

    @property
    def condition_expression(self):
        r"""Gets the condition_expression of this KeywordsAlarmRuleRespList.

        条件

        :return: The condition_expression of this KeywordsAlarmRuleRespList.
        :rtype: str
        """
        return self._condition_expression

    @condition_expression.setter
    def condition_expression(self, condition_expression):
        r"""Sets the condition_expression of this KeywordsAlarmRuleRespList.

        条件

        :param condition_expression: The condition_expression of this KeywordsAlarmRuleRespList.
        :type condition_expression: str
        """
        self._condition_expression = condition_expression

    @property
    def keywords_requests(self):
        r"""Gets the keywords_requests of this KeywordsAlarmRuleRespList.

        关键词详细信息

        :return: The keywords_requests of this KeywordsAlarmRuleRespList.
        :rtype: list[:class:`huaweicloudsdklts.v2.KeywordsRequestResponse`]
        """
        return self._keywords_requests

    @keywords_requests.setter
    def keywords_requests(self, keywords_requests):
        r"""Sets the keywords_requests of this KeywordsAlarmRuleRespList.

        关键词详细信息

        :param keywords_requests: The keywords_requests of this KeywordsAlarmRuleRespList.
        :type keywords_requests: list[:class:`huaweicloudsdklts.v2.KeywordsRequestResponse`]
        """
        self._keywords_requests = keywords_requests

    @property
    def frequency(self):
        r"""Gets the frequency of this KeywordsAlarmRuleRespList.

        :return: The frequency of this KeywordsAlarmRuleRespList.
        :rtype: :class:`huaweicloudsdklts.v2.Frequency`
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        r"""Sets the frequency of this KeywordsAlarmRuleRespList.

        :param frequency: The frequency of this KeywordsAlarmRuleRespList.
        :type frequency: :class:`huaweicloudsdklts.v2.Frequency`
        """
        self._frequency = frequency

    @property
    def keywords_alarm_level(self):
        r"""Gets the keywords_alarm_level of this KeywordsAlarmRuleRespList.

        告警级别

        :return: The keywords_alarm_level of this KeywordsAlarmRuleRespList.
        :rtype: str
        """
        return self._keywords_alarm_level

    @keywords_alarm_level.setter
    def keywords_alarm_level(self, keywords_alarm_level):
        r"""Sets the keywords_alarm_level of this KeywordsAlarmRuleRespList.

        告警级别

        :param keywords_alarm_level: The keywords_alarm_level of this KeywordsAlarmRuleRespList.
        :type keywords_alarm_level: str
        """
        self._keywords_alarm_level = keywords_alarm_level

    @property
    def domain_id(self):
        r"""Gets the domain_id of this KeywordsAlarmRuleRespList.

        domainId

        :return: The domain_id of this KeywordsAlarmRuleRespList.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this KeywordsAlarmRuleRespList.

        domainId

        :param domain_id: The domain_id of this KeywordsAlarmRuleRespList.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def create_time(self):
        r"""Gets the create_time of this KeywordsAlarmRuleRespList.

        创建时间（毫秒时间戳）

        :return: The create_time of this KeywordsAlarmRuleRespList.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this KeywordsAlarmRuleRespList.

        创建时间（毫秒时间戳）

        :param create_time: The create_time of this KeywordsAlarmRuleRespList.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this KeywordsAlarmRuleRespList.

        更新时间（毫秒时间戳）

        :return: The update_time of this KeywordsAlarmRuleRespList.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this KeywordsAlarmRuleRespList.

        更新时间（毫秒时间戳）

        :param update_time: The update_time of this KeywordsAlarmRuleRespList.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def status(self):
        r"""Gets the status of this KeywordsAlarmRuleRespList.

        告警状态

        :return: The status of this KeywordsAlarmRuleRespList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this KeywordsAlarmRuleRespList.

        告警状态

        :param status: The status of this KeywordsAlarmRuleRespList.
        :type status: str
        """
        self._status = status

    @property
    def trigger_condition_count(self):
        r"""Gets the trigger_condition_count of this KeywordsAlarmRuleRespList.

        触发条件：触发周期;默认为1

        :return: The trigger_condition_count of this KeywordsAlarmRuleRespList.
        :rtype: int
        """
        return self._trigger_condition_count

    @trigger_condition_count.setter
    def trigger_condition_count(self, trigger_condition_count):
        r"""Sets the trigger_condition_count of this KeywordsAlarmRuleRespList.

        触发条件：触发周期;默认为1

        :param trigger_condition_count: The trigger_condition_count of this KeywordsAlarmRuleRespList.
        :type trigger_condition_count: int
        """
        self._trigger_condition_count = trigger_condition_count

    @property
    def trigger_condition_frequency(self):
        r"""Gets the trigger_condition_frequency of this KeywordsAlarmRuleRespList.

        触发条件：触发次数;默认为1

        :return: The trigger_condition_frequency of this KeywordsAlarmRuleRespList.
        :rtype: int
        """
        return self._trigger_condition_frequency

    @trigger_condition_frequency.setter
    def trigger_condition_frequency(self, trigger_condition_frequency):
        r"""Sets the trigger_condition_frequency of this KeywordsAlarmRuleRespList.

        触发条件：触发次数;默认为1

        :param trigger_condition_frequency: The trigger_condition_frequency of this KeywordsAlarmRuleRespList.
        :type trigger_condition_frequency: int
        """
        self._trigger_condition_frequency = trigger_condition_frequency

    @property
    def whether_recovery_policy(self):
        r"""Gets the whether_recovery_policy of this KeywordsAlarmRuleRespList.

        是否打开恢复通知;默认false

        :return: The whether_recovery_policy of this KeywordsAlarmRuleRespList.
        :rtype: bool
        """
        return self._whether_recovery_policy

    @whether_recovery_policy.setter
    def whether_recovery_policy(self, whether_recovery_policy):
        r"""Sets the whether_recovery_policy of this KeywordsAlarmRuleRespList.

        是否打开恢复通知;默认false

        :param whether_recovery_policy: The whether_recovery_policy of this KeywordsAlarmRuleRespList.
        :type whether_recovery_policy: bool
        """
        self._whether_recovery_policy = whether_recovery_policy

    @property
    def recovery_policy(self):
        r"""Gets the recovery_policy of this KeywordsAlarmRuleRespList.

        恢复策略周期;默认为3

        :return: The recovery_policy of this KeywordsAlarmRuleRespList.
        :rtype: int
        """
        return self._recovery_policy

    @recovery_policy.setter
    def recovery_policy(self, recovery_policy):
        r"""Sets the recovery_policy of this KeywordsAlarmRuleRespList.

        恢复策略周期;默认为3

        :param recovery_policy: The recovery_policy of this KeywordsAlarmRuleRespList.
        :type recovery_policy: int
        """
        self._recovery_policy = recovery_policy

    @property
    def notification_frequency(self):
        r"""Gets the notification_frequency of this KeywordsAlarmRuleRespList.

        通知频率,单位(分钟)

        :return: The notification_frequency of this KeywordsAlarmRuleRespList.
        :rtype: int
        """
        return self._notification_frequency

    @notification_frequency.setter
    def notification_frequency(self, notification_frequency):
        r"""Sets the notification_frequency of this KeywordsAlarmRuleRespList.

        通知频率,单位(分钟)

        :param notification_frequency: The notification_frequency of this KeywordsAlarmRuleRespList.
        :type notification_frequency: int
        """
        self._notification_frequency = notification_frequency

    @property
    def alarm_action_rule_name(self):
        r"""Gets the alarm_action_rule_name of this KeywordsAlarmRuleRespList.

        告警行动规则名称 >alarm_action_rule_name和notification_save_rule可以选填一个，如果都填，优先选择alarm_action_rule_name

        :return: The alarm_action_rule_name of this KeywordsAlarmRuleRespList.
        :rtype: str
        """
        return self._alarm_action_rule_name

    @alarm_action_rule_name.setter
    def alarm_action_rule_name(self, alarm_action_rule_name):
        r"""Sets the alarm_action_rule_name of this KeywordsAlarmRuleRespList.

        告警行动规则名称 >alarm_action_rule_name和notification_save_rule可以选填一个，如果都填，优先选择alarm_action_rule_name

        :param alarm_action_rule_name: The alarm_action_rule_name of this KeywordsAlarmRuleRespList.
        :type alarm_action_rule_name: str
        """
        self._alarm_action_rule_name = alarm_action_rule_name

    @property
    def tags(self):
        r"""Gets the tags of this KeywordsAlarmRuleRespList.

        **参数解释：** 告警标签信息。标签是以键值对（key-value）的形式表示，key和value为一一对应关系。

        :return: The tags of this KeywordsAlarmRuleRespList.
        :rtype: list[:class:`huaweicloudsdklts.v2.TagsResBody`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this KeywordsAlarmRuleRespList.

        **参数解释：** 告警标签信息。标签是以键值对（key-value）的形式表示，key和value为一一对应关系。

        :param tags: The tags of this KeywordsAlarmRuleRespList.
        :type tags: list[:class:`huaweicloudsdklts.v2.TagsResBody`]
        """
        self._tags = tags

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
        if not isinstance(other, KeywordsAlarmRuleRespList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
