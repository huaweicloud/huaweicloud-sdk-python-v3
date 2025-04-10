# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSqlAlarmRuleResponse(SdkResponse):

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
        'alarm_rule_alias': 'str',
        'is_css_sql': 'bool',
        'index_id': 'str',
        'project_id': 'str',
        'sql_alarm_rule_id': 'str',
        'sql_alarm_rule_description': 'str',
        'sql_requests': 'list[SqlRequest]',
        'frequency': 'FrequencyRespBody',
        'condition_expression': 'str',
        'sql_alarm_level': 'str',
        'sql_alarm_send': 'bool',
        'domain_id': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'topics': 'list[Topics]',
        'language': 'str',
        'id': 'str',
        'notification_frequency': 'int',
        'alarm_action_rule_name': 'str'
    }

    attribute_map = {
        'sql_alarm_rule_name': 'sql_alarm_rule_name',
        'alarm_rule_alias': 'alarm_rule_alias',
        'is_css_sql': 'is_css_sql',
        'index_id': 'indexId',
        'project_id': 'projectId',
        'sql_alarm_rule_id': 'sql_alarm_rule_id',
        'sql_alarm_rule_description': 'sql_alarm_rule_description',
        'sql_requests': 'sql_requests',
        'frequency': 'frequency',
        'condition_expression': 'condition_expression',
        'sql_alarm_level': 'sql_alarm_level',
        'sql_alarm_send': 'sql_alarm_send',
        'domain_id': 'domain_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'topics': 'topics',
        'language': 'language',
        'id': 'id',
        'notification_frequency': 'notification_frequency',
        'alarm_action_rule_name': 'alarm_action_rule_name'
    }

    def __init__(self, sql_alarm_rule_name=None, alarm_rule_alias=None, is_css_sql=None, index_id=None, project_id=None, sql_alarm_rule_id=None, sql_alarm_rule_description=None, sql_requests=None, frequency=None, condition_expression=None, sql_alarm_level=None, sql_alarm_send=None, domain_id=None, create_time=None, update_time=None, topics=None, language=None, id=None, notification_frequency=None, alarm_action_rule_name=None):
        r"""UpdateSqlAlarmRuleResponse

        The model defined in huaweicloud sdk

        :param sql_alarm_rule_name: SQL告警名称
        :type sql_alarm_rule_name: str
        :param alarm_rule_alias: 规则名称
        :type alarm_rule_alias: str
        :param is_css_sql: 是否管道符sql查询
        :type is_css_sql: bool
        :param index_id: 索引id
        :type index_id: str
        :param project_id: 项目id
        :type project_id: str
        :param sql_alarm_rule_id: SQL告警规则id
        :type sql_alarm_rule_id: str
        :param sql_alarm_rule_description: SQL告警信息描述
        :type sql_alarm_rule_description: str
        :param sql_requests: SQL详细信息
        :type sql_requests: list[:class:`huaweicloudsdklts.v2.SqlRequest`]
        :param frequency: 
        :type frequency: :class:`huaweicloudsdklts.v2.FrequencyRespBody`
        :param condition_expression: 条件表达式
        :type condition_expression: str
        :param sql_alarm_level: 告警级别
        :type sql_alarm_level: str
        :param sql_alarm_send: 是否发送
        :type sql_alarm_send: bool
        :param domain_id: domainId
        :type domain_id: str
        :param create_time: 创建时间（毫秒时间戳）
        :type create_time: int
        :param update_time: 更新时间（毫秒时间戳）
        :type update_time: int
        :param topics: 主题
        :type topics: list[:class:`huaweicloudsdklts.v2.Topics`]
        :param language: 邮件附加信息语言
        :type language: str
        :param id: 规则ID。
        :type id: str
        :param notification_frequency: 通知频率,单位(分钟)
        :type notification_frequency: int
        :param alarm_action_rule_name: 告警行动规则名称 &gt;alarm_action_rule_name和notification_save_rule可以选填一个，如果都填，优先选择alarm_action_rule_name
        :type alarm_action_rule_name: str
        """
        
        super(UpdateSqlAlarmRuleResponse, self).__init__()

        self._sql_alarm_rule_name = None
        self._alarm_rule_alias = None
        self._is_css_sql = None
        self._index_id = None
        self._project_id = None
        self._sql_alarm_rule_id = None
        self._sql_alarm_rule_description = None
        self._sql_requests = None
        self._frequency = None
        self._condition_expression = None
        self._sql_alarm_level = None
        self._sql_alarm_send = None
        self._domain_id = None
        self._create_time = None
        self._update_time = None
        self._topics = None
        self._language = None
        self._id = None
        self._notification_frequency = None
        self._alarm_action_rule_name = None
        self.discriminator = None

        if sql_alarm_rule_name is not None:
            self.sql_alarm_rule_name = sql_alarm_rule_name
        if alarm_rule_alias is not None:
            self.alarm_rule_alias = alarm_rule_alias
        if is_css_sql is not None:
            self.is_css_sql = is_css_sql
        if index_id is not None:
            self.index_id = index_id
        if project_id is not None:
            self.project_id = project_id
        if sql_alarm_rule_id is not None:
            self.sql_alarm_rule_id = sql_alarm_rule_id
        if sql_alarm_rule_description is not None:
            self.sql_alarm_rule_description = sql_alarm_rule_description
        if sql_requests is not None:
            self.sql_requests = sql_requests
        if frequency is not None:
            self.frequency = frequency
        if condition_expression is not None:
            self.condition_expression = condition_expression
        if sql_alarm_level is not None:
            self.sql_alarm_level = sql_alarm_level
        if sql_alarm_send is not None:
            self.sql_alarm_send = sql_alarm_send
        if domain_id is not None:
            self.domain_id = domain_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if topics is not None:
            self.topics = topics
        if language is not None:
            self.language = language
        if id is not None:
            self.id = id
        if notification_frequency is not None:
            self.notification_frequency = notification_frequency
        if alarm_action_rule_name is not None:
            self.alarm_action_rule_name = alarm_action_rule_name

    @property
    def sql_alarm_rule_name(self):
        r"""Gets the sql_alarm_rule_name of this UpdateSqlAlarmRuleResponse.

        SQL告警名称

        :return: The sql_alarm_rule_name of this UpdateSqlAlarmRuleResponse.
        :rtype: str
        """
        return self._sql_alarm_rule_name

    @sql_alarm_rule_name.setter
    def sql_alarm_rule_name(self, sql_alarm_rule_name):
        r"""Sets the sql_alarm_rule_name of this UpdateSqlAlarmRuleResponse.

        SQL告警名称

        :param sql_alarm_rule_name: The sql_alarm_rule_name of this UpdateSqlAlarmRuleResponse.
        :type sql_alarm_rule_name: str
        """
        self._sql_alarm_rule_name = sql_alarm_rule_name

    @property
    def alarm_rule_alias(self):
        r"""Gets the alarm_rule_alias of this UpdateSqlAlarmRuleResponse.

        规则名称

        :return: The alarm_rule_alias of this UpdateSqlAlarmRuleResponse.
        :rtype: str
        """
        return self._alarm_rule_alias

    @alarm_rule_alias.setter
    def alarm_rule_alias(self, alarm_rule_alias):
        r"""Sets the alarm_rule_alias of this UpdateSqlAlarmRuleResponse.

        规则名称

        :param alarm_rule_alias: The alarm_rule_alias of this UpdateSqlAlarmRuleResponse.
        :type alarm_rule_alias: str
        """
        self._alarm_rule_alias = alarm_rule_alias

    @property
    def is_css_sql(self):
        r"""Gets the is_css_sql of this UpdateSqlAlarmRuleResponse.

        是否管道符sql查询

        :return: The is_css_sql of this UpdateSqlAlarmRuleResponse.
        :rtype: bool
        """
        return self._is_css_sql

    @is_css_sql.setter
    def is_css_sql(self, is_css_sql):
        r"""Sets the is_css_sql of this UpdateSqlAlarmRuleResponse.

        是否管道符sql查询

        :param is_css_sql: The is_css_sql of this UpdateSqlAlarmRuleResponse.
        :type is_css_sql: bool
        """
        self._is_css_sql = is_css_sql

    @property
    def index_id(self):
        r"""Gets the index_id of this UpdateSqlAlarmRuleResponse.

        索引id

        :return: The index_id of this UpdateSqlAlarmRuleResponse.
        :rtype: str
        """
        return self._index_id

    @index_id.setter
    def index_id(self, index_id):
        r"""Sets the index_id of this UpdateSqlAlarmRuleResponse.

        索引id

        :param index_id: The index_id of this UpdateSqlAlarmRuleResponse.
        :type index_id: str
        """
        self._index_id = index_id

    @property
    def project_id(self):
        r"""Gets the project_id of this UpdateSqlAlarmRuleResponse.

        项目id

        :return: The project_id of this UpdateSqlAlarmRuleResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this UpdateSqlAlarmRuleResponse.

        项目id

        :param project_id: The project_id of this UpdateSqlAlarmRuleResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def sql_alarm_rule_id(self):
        r"""Gets the sql_alarm_rule_id of this UpdateSqlAlarmRuleResponse.

        SQL告警规则id

        :return: The sql_alarm_rule_id of this UpdateSqlAlarmRuleResponse.
        :rtype: str
        """
        return self._sql_alarm_rule_id

    @sql_alarm_rule_id.setter
    def sql_alarm_rule_id(self, sql_alarm_rule_id):
        r"""Sets the sql_alarm_rule_id of this UpdateSqlAlarmRuleResponse.

        SQL告警规则id

        :param sql_alarm_rule_id: The sql_alarm_rule_id of this UpdateSqlAlarmRuleResponse.
        :type sql_alarm_rule_id: str
        """
        self._sql_alarm_rule_id = sql_alarm_rule_id

    @property
    def sql_alarm_rule_description(self):
        r"""Gets the sql_alarm_rule_description of this UpdateSqlAlarmRuleResponse.

        SQL告警信息描述

        :return: The sql_alarm_rule_description of this UpdateSqlAlarmRuleResponse.
        :rtype: str
        """
        return self._sql_alarm_rule_description

    @sql_alarm_rule_description.setter
    def sql_alarm_rule_description(self, sql_alarm_rule_description):
        r"""Sets the sql_alarm_rule_description of this UpdateSqlAlarmRuleResponse.

        SQL告警信息描述

        :param sql_alarm_rule_description: The sql_alarm_rule_description of this UpdateSqlAlarmRuleResponse.
        :type sql_alarm_rule_description: str
        """
        self._sql_alarm_rule_description = sql_alarm_rule_description

    @property
    def sql_requests(self):
        r"""Gets the sql_requests of this UpdateSqlAlarmRuleResponse.

        SQL详细信息

        :return: The sql_requests of this UpdateSqlAlarmRuleResponse.
        :rtype: list[:class:`huaweicloudsdklts.v2.SqlRequest`]
        """
        return self._sql_requests

    @sql_requests.setter
    def sql_requests(self, sql_requests):
        r"""Sets the sql_requests of this UpdateSqlAlarmRuleResponse.

        SQL详细信息

        :param sql_requests: The sql_requests of this UpdateSqlAlarmRuleResponse.
        :type sql_requests: list[:class:`huaweicloudsdklts.v2.SqlRequest`]
        """
        self._sql_requests = sql_requests

    @property
    def frequency(self):
        r"""Gets the frequency of this UpdateSqlAlarmRuleResponse.

        :return: The frequency of this UpdateSqlAlarmRuleResponse.
        :rtype: :class:`huaweicloudsdklts.v2.FrequencyRespBody`
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        r"""Sets the frequency of this UpdateSqlAlarmRuleResponse.

        :param frequency: The frequency of this UpdateSqlAlarmRuleResponse.
        :type frequency: :class:`huaweicloudsdklts.v2.FrequencyRespBody`
        """
        self._frequency = frequency

    @property
    def condition_expression(self):
        r"""Gets the condition_expression of this UpdateSqlAlarmRuleResponse.

        条件表达式

        :return: The condition_expression of this UpdateSqlAlarmRuleResponse.
        :rtype: str
        """
        return self._condition_expression

    @condition_expression.setter
    def condition_expression(self, condition_expression):
        r"""Sets the condition_expression of this UpdateSqlAlarmRuleResponse.

        条件表达式

        :param condition_expression: The condition_expression of this UpdateSqlAlarmRuleResponse.
        :type condition_expression: str
        """
        self._condition_expression = condition_expression

    @property
    def sql_alarm_level(self):
        r"""Gets the sql_alarm_level of this UpdateSqlAlarmRuleResponse.

        告警级别

        :return: The sql_alarm_level of this UpdateSqlAlarmRuleResponse.
        :rtype: str
        """
        return self._sql_alarm_level

    @sql_alarm_level.setter
    def sql_alarm_level(self, sql_alarm_level):
        r"""Sets the sql_alarm_level of this UpdateSqlAlarmRuleResponse.

        告警级别

        :param sql_alarm_level: The sql_alarm_level of this UpdateSqlAlarmRuleResponse.
        :type sql_alarm_level: str
        """
        self._sql_alarm_level = sql_alarm_level

    @property
    def sql_alarm_send(self):
        r"""Gets the sql_alarm_send of this UpdateSqlAlarmRuleResponse.

        是否发送

        :return: The sql_alarm_send of this UpdateSqlAlarmRuleResponse.
        :rtype: bool
        """
        return self._sql_alarm_send

    @sql_alarm_send.setter
    def sql_alarm_send(self, sql_alarm_send):
        r"""Sets the sql_alarm_send of this UpdateSqlAlarmRuleResponse.

        是否发送

        :param sql_alarm_send: The sql_alarm_send of this UpdateSqlAlarmRuleResponse.
        :type sql_alarm_send: bool
        """
        self._sql_alarm_send = sql_alarm_send

    @property
    def domain_id(self):
        r"""Gets the domain_id of this UpdateSqlAlarmRuleResponse.

        domainId

        :return: The domain_id of this UpdateSqlAlarmRuleResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this UpdateSqlAlarmRuleResponse.

        domainId

        :param domain_id: The domain_id of this UpdateSqlAlarmRuleResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def create_time(self):
        r"""Gets the create_time of this UpdateSqlAlarmRuleResponse.

        创建时间（毫秒时间戳）

        :return: The create_time of this UpdateSqlAlarmRuleResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this UpdateSqlAlarmRuleResponse.

        创建时间（毫秒时间戳）

        :param create_time: The create_time of this UpdateSqlAlarmRuleResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this UpdateSqlAlarmRuleResponse.

        更新时间（毫秒时间戳）

        :return: The update_time of this UpdateSqlAlarmRuleResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this UpdateSqlAlarmRuleResponse.

        更新时间（毫秒时间戳）

        :param update_time: The update_time of this UpdateSqlAlarmRuleResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def topics(self):
        r"""Gets the topics of this UpdateSqlAlarmRuleResponse.

        主题

        :return: The topics of this UpdateSqlAlarmRuleResponse.
        :rtype: list[:class:`huaweicloudsdklts.v2.Topics`]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        r"""Sets the topics of this UpdateSqlAlarmRuleResponse.

        主题

        :param topics: The topics of this UpdateSqlAlarmRuleResponse.
        :type topics: list[:class:`huaweicloudsdklts.v2.Topics`]
        """
        self._topics = topics

    @property
    def language(self):
        r"""Gets the language of this UpdateSqlAlarmRuleResponse.

        邮件附加信息语言

        :return: The language of this UpdateSqlAlarmRuleResponse.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this UpdateSqlAlarmRuleResponse.

        邮件附加信息语言

        :param language: The language of this UpdateSqlAlarmRuleResponse.
        :type language: str
        """
        self._language = language

    @property
    def id(self):
        r"""Gets the id of this UpdateSqlAlarmRuleResponse.

        规则ID。

        :return: The id of this UpdateSqlAlarmRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateSqlAlarmRuleResponse.

        规则ID。

        :param id: The id of this UpdateSqlAlarmRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def notification_frequency(self):
        r"""Gets the notification_frequency of this UpdateSqlAlarmRuleResponse.

        通知频率,单位(分钟)

        :return: The notification_frequency of this UpdateSqlAlarmRuleResponse.
        :rtype: int
        """
        return self._notification_frequency

    @notification_frequency.setter
    def notification_frequency(self, notification_frequency):
        r"""Sets the notification_frequency of this UpdateSqlAlarmRuleResponse.

        通知频率,单位(分钟)

        :param notification_frequency: The notification_frequency of this UpdateSqlAlarmRuleResponse.
        :type notification_frequency: int
        """
        self._notification_frequency = notification_frequency

    @property
    def alarm_action_rule_name(self):
        r"""Gets the alarm_action_rule_name of this UpdateSqlAlarmRuleResponse.

        告警行动规则名称 >alarm_action_rule_name和notification_save_rule可以选填一个，如果都填，优先选择alarm_action_rule_name

        :return: The alarm_action_rule_name of this UpdateSqlAlarmRuleResponse.
        :rtype: str
        """
        return self._alarm_action_rule_name

    @alarm_action_rule_name.setter
    def alarm_action_rule_name(self, alarm_action_rule_name):
        r"""Sets the alarm_action_rule_name of this UpdateSqlAlarmRuleResponse.

        告警行动规则名称 >alarm_action_rule_name和notification_save_rule可以选填一个，如果都填，优先选择alarm_action_rule_name

        :param alarm_action_rule_name: The alarm_action_rule_name of this UpdateSqlAlarmRuleResponse.
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
        if not isinstance(other, UpdateSqlAlarmRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
