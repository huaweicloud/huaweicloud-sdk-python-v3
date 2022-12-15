# coding: utf-8

import re
import six



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
        'keywords_requests': 'list[KeywordsRequest]',
        'frequency': 'Frequency',
        'keywords_alarm_level': 'str',
        'keywords_alarm_send': 'bool',
        'domain_id': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'topics': 'list[Topics]',
        'template_name': 'str',
        'status': 'str',
        'trigger_condition_count': 'int',
        'trigger_condition_frequency': 'int',
        'whether_recovery_policy': 'bool',
        'recovery_policy': 'int'
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
        'keywords_alarm_send': 'keywords_alarm_send',
        'domain_id': 'domain_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'topics': 'topics',
        'template_name': 'template_name',
        'status': 'status',
        'trigger_condition_count': 'trigger_condition_count',
        'trigger_condition_frequency': 'trigger_condition_frequency',
        'whether_recovery_policy': 'whether_recovery_policy',
        'recovery_policy': 'recovery_policy'
    }

    def __init__(self, project_id=None, keywords_alarm_rule_id=None, keywords_alarm_rule_name=None, keywords_alarm_rule_description=None, condition_expression=None, keywords_requests=None, frequency=None, keywords_alarm_level=None, keywords_alarm_send=None, domain_id=None, create_time=None, update_time=None, topics=None, template_name=None, status=None, trigger_condition_count=None, trigger_condition_frequency=None, whether_recovery_policy=None, recovery_policy=None):
        """KeywordsAlarmRuleRespList

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
        :type keywords_requests: list[:class:`huaweicloudsdklts.v2.KeywordsRequest`]
        :param frequency: 告警统计周期
        :type frequency: :class:`huaweicloudsdklts.v2.Frequency`
        :param keywords_alarm_level: 告警级别
        :type keywords_alarm_level: str
        :param keywords_alarm_send: 是否发送
        :type keywords_alarm_send: bool
        :param domain_id: domainId
        :type domain_id: str
        :param create_time: 创建时间(毫秒时间戳)
        :type create_time: int
        :param update_time: 更新时间(毫秒时间戳)
        :type update_time: int
        :param topics: 主题
        :type topics: list[:class:`huaweicloudsdklts.v2.Topics`]
        :param template_name: 
        :type template_name: str
        :param status: 
        :type status: str
        :param trigger_condition_count: 触发条件：触发次数;默认为1
        :type trigger_condition_count: int
        :param trigger_condition_frequency: 触发条件：触发周期;默认为1
        :type trigger_condition_frequency: int
        :param whether_recovery_policy: 是否打开恢复通知;默认false
        :type whether_recovery_policy: bool
        :param recovery_policy: 恢复策略周期;默认为3
        :type recovery_policy: int
        """
        
        

        self._project_id = None
        self._keywords_alarm_rule_id = None
        self._keywords_alarm_rule_name = None
        self._keywords_alarm_rule_description = None
        self._condition_expression = None
        self._keywords_requests = None
        self._frequency = None
        self._keywords_alarm_level = None
        self._keywords_alarm_send = None
        self._domain_id = None
        self._create_time = None
        self._update_time = None
        self._topics = None
        self._template_name = None
        self._status = None
        self._trigger_condition_count = None
        self._trigger_condition_frequency = None
        self._whether_recovery_policy = None
        self._recovery_policy = None
        self.discriminator = None

        self.project_id = project_id
        self.keywords_alarm_rule_id = keywords_alarm_rule_id
        self.keywords_alarm_rule_name = keywords_alarm_rule_name
        self.keywords_alarm_rule_description = keywords_alarm_rule_description
        self.condition_expression = condition_expression
        self.keywords_requests = keywords_requests
        self.frequency = frequency
        self.keywords_alarm_level = keywords_alarm_level
        self.keywords_alarm_send = keywords_alarm_send
        self.domain_id = domain_id
        self.create_time = create_time
        self.update_time = update_time
        self.topics = topics
        if template_name is not None:
            self.template_name = template_name
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

    @property
    def project_id(self):
        """Gets the project_id of this KeywordsAlarmRuleRespList.

        项目id

        :return: The project_id of this KeywordsAlarmRuleRespList.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this KeywordsAlarmRuleRespList.

        项目id

        :param project_id: The project_id of this KeywordsAlarmRuleRespList.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def keywords_alarm_rule_id(self):
        """Gets the keywords_alarm_rule_id of this KeywordsAlarmRuleRespList.

        关键词告警id

        :return: The keywords_alarm_rule_id of this KeywordsAlarmRuleRespList.
        :rtype: str
        """
        return self._keywords_alarm_rule_id

    @keywords_alarm_rule_id.setter
    def keywords_alarm_rule_id(self, keywords_alarm_rule_id):
        """Sets the keywords_alarm_rule_id of this KeywordsAlarmRuleRespList.

        关键词告警id

        :param keywords_alarm_rule_id: The keywords_alarm_rule_id of this KeywordsAlarmRuleRespList.
        :type keywords_alarm_rule_id: str
        """
        self._keywords_alarm_rule_id = keywords_alarm_rule_id

    @property
    def keywords_alarm_rule_name(self):
        """Gets the keywords_alarm_rule_name of this KeywordsAlarmRuleRespList.

        关键词告警名称

        :return: The keywords_alarm_rule_name of this KeywordsAlarmRuleRespList.
        :rtype: str
        """
        return self._keywords_alarm_rule_name

    @keywords_alarm_rule_name.setter
    def keywords_alarm_rule_name(self, keywords_alarm_rule_name):
        """Sets the keywords_alarm_rule_name of this KeywordsAlarmRuleRespList.

        关键词告警名称

        :param keywords_alarm_rule_name: The keywords_alarm_rule_name of this KeywordsAlarmRuleRespList.
        :type keywords_alarm_rule_name: str
        """
        self._keywords_alarm_rule_name = keywords_alarm_rule_name

    @property
    def keywords_alarm_rule_description(self):
        """Gets the keywords_alarm_rule_description of this KeywordsAlarmRuleRespList.

        关键词告警信息描述

        :return: The keywords_alarm_rule_description of this KeywordsAlarmRuleRespList.
        :rtype: str
        """
        return self._keywords_alarm_rule_description

    @keywords_alarm_rule_description.setter
    def keywords_alarm_rule_description(self, keywords_alarm_rule_description):
        """Sets the keywords_alarm_rule_description of this KeywordsAlarmRuleRespList.

        关键词告警信息描述

        :param keywords_alarm_rule_description: The keywords_alarm_rule_description of this KeywordsAlarmRuleRespList.
        :type keywords_alarm_rule_description: str
        """
        self._keywords_alarm_rule_description = keywords_alarm_rule_description

    @property
    def condition_expression(self):
        """Gets the condition_expression of this KeywordsAlarmRuleRespList.

        条件

        :return: The condition_expression of this KeywordsAlarmRuleRespList.
        :rtype: str
        """
        return self._condition_expression

    @condition_expression.setter
    def condition_expression(self, condition_expression):
        """Sets the condition_expression of this KeywordsAlarmRuleRespList.

        条件

        :param condition_expression: The condition_expression of this KeywordsAlarmRuleRespList.
        :type condition_expression: str
        """
        self._condition_expression = condition_expression

    @property
    def keywords_requests(self):
        """Gets the keywords_requests of this KeywordsAlarmRuleRespList.

        关键词详细信息

        :return: The keywords_requests of this KeywordsAlarmRuleRespList.
        :rtype: list[:class:`huaweicloudsdklts.v2.KeywordsRequest`]
        """
        return self._keywords_requests

    @keywords_requests.setter
    def keywords_requests(self, keywords_requests):
        """Sets the keywords_requests of this KeywordsAlarmRuleRespList.

        关键词详细信息

        :param keywords_requests: The keywords_requests of this KeywordsAlarmRuleRespList.
        :type keywords_requests: list[:class:`huaweicloudsdklts.v2.KeywordsRequest`]
        """
        self._keywords_requests = keywords_requests

    @property
    def frequency(self):
        """Gets the frequency of this KeywordsAlarmRuleRespList.

        告警统计周期

        :return: The frequency of this KeywordsAlarmRuleRespList.
        :rtype: :class:`huaweicloudsdklts.v2.Frequency`
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this KeywordsAlarmRuleRespList.

        告警统计周期

        :param frequency: The frequency of this KeywordsAlarmRuleRespList.
        :type frequency: :class:`huaweicloudsdklts.v2.Frequency`
        """
        self._frequency = frequency

    @property
    def keywords_alarm_level(self):
        """Gets the keywords_alarm_level of this KeywordsAlarmRuleRespList.

        告警级别

        :return: The keywords_alarm_level of this KeywordsAlarmRuleRespList.
        :rtype: str
        """
        return self._keywords_alarm_level

    @keywords_alarm_level.setter
    def keywords_alarm_level(self, keywords_alarm_level):
        """Sets the keywords_alarm_level of this KeywordsAlarmRuleRespList.

        告警级别

        :param keywords_alarm_level: The keywords_alarm_level of this KeywordsAlarmRuleRespList.
        :type keywords_alarm_level: str
        """
        self._keywords_alarm_level = keywords_alarm_level

    @property
    def keywords_alarm_send(self):
        """Gets the keywords_alarm_send of this KeywordsAlarmRuleRespList.

        是否发送

        :return: The keywords_alarm_send of this KeywordsAlarmRuleRespList.
        :rtype: bool
        """
        return self._keywords_alarm_send

    @keywords_alarm_send.setter
    def keywords_alarm_send(self, keywords_alarm_send):
        """Sets the keywords_alarm_send of this KeywordsAlarmRuleRespList.

        是否发送

        :param keywords_alarm_send: The keywords_alarm_send of this KeywordsAlarmRuleRespList.
        :type keywords_alarm_send: bool
        """
        self._keywords_alarm_send = keywords_alarm_send

    @property
    def domain_id(self):
        """Gets the domain_id of this KeywordsAlarmRuleRespList.

        domainId

        :return: The domain_id of this KeywordsAlarmRuleRespList.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this KeywordsAlarmRuleRespList.

        domainId

        :param domain_id: The domain_id of this KeywordsAlarmRuleRespList.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def create_time(self):
        """Gets the create_time of this KeywordsAlarmRuleRespList.

        创建时间(毫秒时间戳)

        :return: The create_time of this KeywordsAlarmRuleRespList.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this KeywordsAlarmRuleRespList.

        创建时间(毫秒时间戳)

        :param create_time: The create_time of this KeywordsAlarmRuleRespList.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this KeywordsAlarmRuleRespList.

        更新时间(毫秒时间戳)

        :return: The update_time of this KeywordsAlarmRuleRespList.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this KeywordsAlarmRuleRespList.

        更新时间(毫秒时间戳)

        :param update_time: The update_time of this KeywordsAlarmRuleRespList.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def topics(self):
        """Gets the topics of this KeywordsAlarmRuleRespList.

        主题

        :return: The topics of this KeywordsAlarmRuleRespList.
        :rtype: list[:class:`huaweicloudsdklts.v2.Topics`]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        """Sets the topics of this KeywordsAlarmRuleRespList.

        主题

        :param topics: The topics of this KeywordsAlarmRuleRespList.
        :type topics: list[:class:`huaweicloudsdklts.v2.Topics`]
        """
        self._topics = topics

    @property
    def template_name(self):
        """Gets the template_name of this KeywordsAlarmRuleRespList.

        :return: The template_name of this KeywordsAlarmRuleRespList.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this KeywordsAlarmRuleRespList.

        :param template_name: The template_name of this KeywordsAlarmRuleRespList.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def status(self):
        """Gets the status of this KeywordsAlarmRuleRespList.

        :return: The status of this KeywordsAlarmRuleRespList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this KeywordsAlarmRuleRespList.

        :param status: The status of this KeywordsAlarmRuleRespList.
        :type status: str
        """
        self._status = status

    @property
    def trigger_condition_count(self):
        """Gets the trigger_condition_count of this KeywordsAlarmRuleRespList.

        触发条件：触发次数;默认为1

        :return: The trigger_condition_count of this KeywordsAlarmRuleRespList.
        :rtype: int
        """
        return self._trigger_condition_count

    @trigger_condition_count.setter
    def trigger_condition_count(self, trigger_condition_count):
        """Sets the trigger_condition_count of this KeywordsAlarmRuleRespList.

        触发条件：触发次数;默认为1

        :param trigger_condition_count: The trigger_condition_count of this KeywordsAlarmRuleRespList.
        :type trigger_condition_count: int
        """
        self._trigger_condition_count = trigger_condition_count

    @property
    def trigger_condition_frequency(self):
        """Gets the trigger_condition_frequency of this KeywordsAlarmRuleRespList.

        触发条件：触发周期;默认为1

        :return: The trigger_condition_frequency of this KeywordsAlarmRuleRespList.
        :rtype: int
        """
        return self._trigger_condition_frequency

    @trigger_condition_frequency.setter
    def trigger_condition_frequency(self, trigger_condition_frequency):
        """Sets the trigger_condition_frequency of this KeywordsAlarmRuleRespList.

        触发条件：触发周期;默认为1

        :param trigger_condition_frequency: The trigger_condition_frequency of this KeywordsAlarmRuleRespList.
        :type trigger_condition_frequency: int
        """
        self._trigger_condition_frequency = trigger_condition_frequency

    @property
    def whether_recovery_policy(self):
        """Gets the whether_recovery_policy of this KeywordsAlarmRuleRespList.

        是否打开恢复通知;默认false

        :return: The whether_recovery_policy of this KeywordsAlarmRuleRespList.
        :rtype: bool
        """
        return self._whether_recovery_policy

    @whether_recovery_policy.setter
    def whether_recovery_policy(self, whether_recovery_policy):
        """Sets the whether_recovery_policy of this KeywordsAlarmRuleRespList.

        是否打开恢复通知;默认false

        :param whether_recovery_policy: The whether_recovery_policy of this KeywordsAlarmRuleRespList.
        :type whether_recovery_policy: bool
        """
        self._whether_recovery_policy = whether_recovery_policy

    @property
    def recovery_policy(self):
        """Gets the recovery_policy of this KeywordsAlarmRuleRespList.

        恢复策略周期;默认为3

        :return: The recovery_policy of this KeywordsAlarmRuleRespList.
        :rtype: int
        """
        return self._recovery_policy

    @recovery_policy.setter
    def recovery_policy(self, recovery_policy):
        """Sets the recovery_policy of this KeywordsAlarmRuleRespList.

        恢复策略周期;默认为3

        :param recovery_policy: The recovery_policy of this KeywordsAlarmRuleRespList.
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
        if not isinstance(other, KeywordsAlarmRuleRespList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
