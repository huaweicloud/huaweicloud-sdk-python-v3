# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateKeywordsAlarmRuleResponse(SdkResponse):

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
        'keywords_requests': 'list[KeywordsResBody]',
        'frequency': 'FrequencyRespBody',
        'keywords_alarm_level': 'str',
        'keywords_alarm_send': 'bool',
        'domain_id': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'language': 'str',
        'project_id': 'str',
        'topics': 'list[Topics]',
        'condition_expression': 'str',
        'index_id': 'str',
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
        'domain_id': 'domain_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'language': 'language',
        'project_id': 'projectId',
        'topics': 'topics',
        'condition_expression': 'condition_expression',
        'index_id': 'indexId',
        'notification_frequency': 'notification_frequency',
        'alarm_action_rule_name': 'alarm_action_rule_name'
    }

    def __init__(self, keywords_alarm_rule_id=None, keywords_alarm_rule_name=None, alarm_rule_alias=None, keywords_alarm_rule_description=None, keywords_requests=None, frequency=None, keywords_alarm_level=None, keywords_alarm_send=None, domain_id=None, create_time=None, update_time=None, language=None, project_id=None, topics=None, condition_expression=None, index_id=None, notification_frequency=None, alarm_action_rule_name=None):
        r"""UpdateKeywordsAlarmRuleResponse

        The model defined in huaweicloud sdk

        :param keywords_alarm_rule_id: 关键词告警id
        :type keywords_alarm_rule_id: str
        :param keywords_alarm_rule_name: 关键词告警名称
        :type keywords_alarm_rule_name: str
        :param alarm_rule_alias: 规则名称
        :type alarm_rule_alias: str
        :param keywords_alarm_rule_description: 关键词告警信息描述
        :type keywords_alarm_rule_description: str
        :param keywords_requests: 关键词详细信息
        :type keywords_requests: list[:class:`huaweicloudsdklts.v2.KeywordsResBody`]
        :param frequency: 
        :type frequency: :class:`huaweicloudsdklts.v2.FrequencyRespBody`
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
        :param language: 邮件附加信息语言
        :type language: str
        :param project_id: 项目id
        :type project_id: str
        :param topics: 通知主题
        :type topics: list[:class:`huaweicloudsdklts.v2.Topics`]
        :param condition_expression: 情况表述
        :type condition_expression: str
        :param index_id: 索引id
        :type index_id: str
        :param notification_frequency: 通知频率,单位(分钟)
        :type notification_frequency: int
        :param alarm_action_rule_name: 告警行动规则名称 &gt;alarm_action_rule_name和notification_save_rule可以选填一个，如果都填，优先选择alarm_action_rule_name
        :type alarm_action_rule_name: str
        """
        
        super(UpdateKeywordsAlarmRuleResponse, self).__init__()

        self._keywords_alarm_rule_id = None
        self._keywords_alarm_rule_name = None
        self._alarm_rule_alias = None
        self._keywords_alarm_rule_description = None
        self._keywords_requests = None
        self._frequency = None
        self._keywords_alarm_level = None
        self._keywords_alarm_send = None
        self._domain_id = None
        self._create_time = None
        self._update_time = None
        self._language = None
        self._project_id = None
        self._topics = None
        self._condition_expression = None
        self._index_id = None
        self._notification_frequency = None
        self._alarm_action_rule_name = None
        self.discriminator = None

        if keywords_alarm_rule_id is not None:
            self.keywords_alarm_rule_id = keywords_alarm_rule_id
        if keywords_alarm_rule_name is not None:
            self.keywords_alarm_rule_name = keywords_alarm_rule_name
        if alarm_rule_alias is not None:
            self.alarm_rule_alias = alarm_rule_alias
        if keywords_alarm_rule_description is not None:
            self.keywords_alarm_rule_description = keywords_alarm_rule_description
        if keywords_requests is not None:
            self.keywords_requests = keywords_requests
        if frequency is not None:
            self.frequency = frequency
        if keywords_alarm_level is not None:
            self.keywords_alarm_level = keywords_alarm_level
        if keywords_alarm_send is not None:
            self.keywords_alarm_send = keywords_alarm_send
        if domain_id is not None:
            self.domain_id = domain_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if language is not None:
            self.language = language
        if project_id is not None:
            self.project_id = project_id
        if topics is not None:
            self.topics = topics
        if condition_expression is not None:
            self.condition_expression = condition_expression
        if index_id is not None:
            self.index_id = index_id
        if notification_frequency is not None:
            self.notification_frequency = notification_frequency
        if alarm_action_rule_name is not None:
            self.alarm_action_rule_name = alarm_action_rule_name

    @property
    def keywords_alarm_rule_id(self):
        r"""Gets the keywords_alarm_rule_id of this UpdateKeywordsAlarmRuleResponse.

        关键词告警id

        :return: The keywords_alarm_rule_id of this UpdateKeywordsAlarmRuleResponse.
        :rtype: str
        """
        return self._keywords_alarm_rule_id

    @keywords_alarm_rule_id.setter
    def keywords_alarm_rule_id(self, keywords_alarm_rule_id):
        r"""Sets the keywords_alarm_rule_id of this UpdateKeywordsAlarmRuleResponse.

        关键词告警id

        :param keywords_alarm_rule_id: The keywords_alarm_rule_id of this UpdateKeywordsAlarmRuleResponse.
        :type keywords_alarm_rule_id: str
        """
        self._keywords_alarm_rule_id = keywords_alarm_rule_id

    @property
    def keywords_alarm_rule_name(self):
        r"""Gets the keywords_alarm_rule_name of this UpdateKeywordsAlarmRuleResponse.

        关键词告警名称

        :return: The keywords_alarm_rule_name of this UpdateKeywordsAlarmRuleResponse.
        :rtype: str
        """
        return self._keywords_alarm_rule_name

    @keywords_alarm_rule_name.setter
    def keywords_alarm_rule_name(self, keywords_alarm_rule_name):
        r"""Sets the keywords_alarm_rule_name of this UpdateKeywordsAlarmRuleResponse.

        关键词告警名称

        :param keywords_alarm_rule_name: The keywords_alarm_rule_name of this UpdateKeywordsAlarmRuleResponse.
        :type keywords_alarm_rule_name: str
        """
        self._keywords_alarm_rule_name = keywords_alarm_rule_name

    @property
    def alarm_rule_alias(self):
        r"""Gets the alarm_rule_alias of this UpdateKeywordsAlarmRuleResponse.

        规则名称

        :return: The alarm_rule_alias of this UpdateKeywordsAlarmRuleResponse.
        :rtype: str
        """
        return self._alarm_rule_alias

    @alarm_rule_alias.setter
    def alarm_rule_alias(self, alarm_rule_alias):
        r"""Sets the alarm_rule_alias of this UpdateKeywordsAlarmRuleResponse.

        规则名称

        :param alarm_rule_alias: The alarm_rule_alias of this UpdateKeywordsAlarmRuleResponse.
        :type alarm_rule_alias: str
        """
        self._alarm_rule_alias = alarm_rule_alias

    @property
    def keywords_alarm_rule_description(self):
        r"""Gets the keywords_alarm_rule_description of this UpdateKeywordsAlarmRuleResponse.

        关键词告警信息描述

        :return: The keywords_alarm_rule_description of this UpdateKeywordsAlarmRuleResponse.
        :rtype: str
        """
        return self._keywords_alarm_rule_description

    @keywords_alarm_rule_description.setter
    def keywords_alarm_rule_description(self, keywords_alarm_rule_description):
        r"""Sets the keywords_alarm_rule_description of this UpdateKeywordsAlarmRuleResponse.

        关键词告警信息描述

        :param keywords_alarm_rule_description: The keywords_alarm_rule_description of this UpdateKeywordsAlarmRuleResponse.
        :type keywords_alarm_rule_description: str
        """
        self._keywords_alarm_rule_description = keywords_alarm_rule_description

    @property
    def keywords_requests(self):
        r"""Gets the keywords_requests of this UpdateKeywordsAlarmRuleResponse.

        关键词详细信息

        :return: The keywords_requests of this UpdateKeywordsAlarmRuleResponse.
        :rtype: list[:class:`huaweicloudsdklts.v2.KeywordsResBody`]
        """
        return self._keywords_requests

    @keywords_requests.setter
    def keywords_requests(self, keywords_requests):
        r"""Sets the keywords_requests of this UpdateKeywordsAlarmRuleResponse.

        关键词详细信息

        :param keywords_requests: The keywords_requests of this UpdateKeywordsAlarmRuleResponse.
        :type keywords_requests: list[:class:`huaweicloudsdklts.v2.KeywordsResBody`]
        """
        self._keywords_requests = keywords_requests

    @property
    def frequency(self):
        r"""Gets the frequency of this UpdateKeywordsAlarmRuleResponse.

        :return: The frequency of this UpdateKeywordsAlarmRuleResponse.
        :rtype: :class:`huaweicloudsdklts.v2.FrequencyRespBody`
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        r"""Sets the frequency of this UpdateKeywordsAlarmRuleResponse.

        :param frequency: The frequency of this UpdateKeywordsAlarmRuleResponse.
        :type frequency: :class:`huaweicloudsdklts.v2.FrequencyRespBody`
        """
        self._frequency = frequency

    @property
    def keywords_alarm_level(self):
        r"""Gets the keywords_alarm_level of this UpdateKeywordsAlarmRuleResponse.

        告警级别

        :return: The keywords_alarm_level of this UpdateKeywordsAlarmRuleResponse.
        :rtype: str
        """
        return self._keywords_alarm_level

    @keywords_alarm_level.setter
    def keywords_alarm_level(self, keywords_alarm_level):
        r"""Sets the keywords_alarm_level of this UpdateKeywordsAlarmRuleResponse.

        告警级别

        :param keywords_alarm_level: The keywords_alarm_level of this UpdateKeywordsAlarmRuleResponse.
        :type keywords_alarm_level: str
        """
        self._keywords_alarm_level = keywords_alarm_level

    @property
    def keywords_alarm_send(self):
        r"""Gets the keywords_alarm_send of this UpdateKeywordsAlarmRuleResponse.

        是否发送

        :return: The keywords_alarm_send of this UpdateKeywordsAlarmRuleResponse.
        :rtype: bool
        """
        return self._keywords_alarm_send

    @keywords_alarm_send.setter
    def keywords_alarm_send(self, keywords_alarm_send):
        r"""Sets the keywords_alarm_send of this UpdateKeywordsAlarmRuleResponse.

        是否发送

        :param keywords_alarm_send: The keywords_alarm_send of this UpdateKeywordsAlarmRuleResponse.
        :type keywords_alarm_send: bool
        """
        self._keywords_alarm_send = keywords_alarm_send

    @property
    def domain_id(self):
        r"""Gets the domain_id of this UpdateKeywordsAlarmRuleResponse.

        domainId

        :return: The domain_id of this UpdateKeywordsAlarmRuleResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this UpdateKeywordsAlarmRuleResponse.

        domainId

        :param domain_id: The domain_id of this UpdateKeywordsAlarmRuleResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def create_time(self):
        r"""Gets the create_time of this UpdateKeywordsAlarmRuleResponse.

        创建时间(毫秒时间戳)

        :return: The create_time of this UpdateKeywordsAlarmRuleResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this UpdateKeywordsAlarmRuleResponse.

        创建时间(毫秒时间戳)

        :param create_time: The create_time of this UpdateKeywordsAlarmRuleResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this UpdateKeywordsAlarmRuleResponse.

        更新时间(毫秒时间戳)

        :return: The update_time of this UpdateKeywordsAlarmRuleResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this UpdateKeywordsAlarmRuleResponse.

        更新时间(毫秒时间戳)

        :param update_time: The update_time of this UpdateKeywordsAlarmRuleResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def language(self):
        r"""Gets the language of this UpdateKeywordsAlarmRuleResponse.

        邮件附加信息语言

        :return: The language of this UpdateKeywordsAlarmRuleResponse.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this UpdateKeywordsAlarmRuleResponse.

        邮件附加信息语言

        :param language: The language of this UpdateKeywordsAlarmRuleResponse.
        :type language: str
        """
        self._language = language

    @property
    def project_id(self):
        r"""Gets the project_id of this UpdateKeywordsAlarmRuleResponse.

        项目id

        :return: The project_id of this UpdateKeywordsAlarmRuleResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this UpdateKeywordsAlarmRuleResponse.

        项目id

        :param project_id: The project_id of this UpdateKeywordsAlarmRuleResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def topics(self):
        r"""Gets the topics of this UpdateKeywordsAlarmRuleResponse.

        通知主题

        :return: The topics of this UpdateKeywordsAlarmRuleResponse.
        :rtype: list[:class:`huaweicloudsdklts.v2.Topics`]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        r"""Sets the topics of this UpdateKeywordsAlarmRuleResponse.

        通知主题

        :param topics: The topics of this UpdateKeywordsAlarmRuleResponse.
        :type topics: list[:class:`huaweicloudsdklts.v2.Topics`]
        """
        self._topics = topics

    @property
    def condition_expression(self):
        r"""Gets the condition_expression of this UpdateKeywordsAlarmRuleResponse.

        情况表述

        :return: The condition_expression of this UpdateKeywordsAlarmRuleResponse.
        :rtype: str
        """
        return self._condition_expression

    @condition_expression.setter
    def condition_expression(self, condition_expression):
        r"""Sets the condition_expression of this UpdateKeywordsAlarmRuleResponse.

        情况表述

        :param condition_expression: The condition_expression of this UpdateKeywordsAlarmRuleResponse.
        :type condition_expression: str
        """
        self._condition_expression = condition_expression

    @property
    def index_id(self):
        r"""Gets the index_id of this UpdateKeywordsAlarmRuleResponse.

        索引id

        :return: The index_id of this UpdateKeywordsAlarmRuleResponse.
        :rtype: str
        """
        return self._index_id

    @index_id.setter
    def index_id(self, index_id):
        r"""Sets the index_id of this UpdateKeywordsAlarmRuleResponse.

        索引id

        :param index_id: The index_id of this UpdateKeywordsAlarmRuleResponse.
        :type index_id: str
        """
        self._index_id = index_id

    @property
    def notification_frequency(self):
        r"""Gets the notification_frequency of this UpdateKeywordsAlarmRuleResponse.

        通知频率,单位(分钟)

        :return: The notification_frequency of this UpdateKeywordsAlarmRuleResponse.
        :rtype: int
        """
        return self._notification_frequency

    @notification_frequency.setter
    def notification_frequency(self, notification_frequency):
        r"""Sets the notification_frequency of this UpdateKeywordsAlarmRuleResponse.

        通知频率,单位(分钟)

        :param notification_frequency: The notification_frequency of this UpdateKeywordsAlarmRuleResponse.
        :type notification_frequency: int
        """
        self._notification_frequency = notification_frequency

    @property
    def alarm_action_rule_name(self):
        r"""Gets the alarm_action_rule_name of this UpdateKeywordsAlarmRuleResponse.

        告警行动规则名称 >alarm_action_rule_name和notification_save_rule可以选填一个，如果都填，优先选择alarm_action_rule_name

        :return: The alarm_action_rule_name of this UpdateKeywordsAlarmRuleResponse.
        :rtype: str
        """
        return self._alarm_action_rule_name

    @alarm_action_rule_name.setter
    def alarm_action_rule_name(self, alarm_action_rule_name):
        r"""Sets the alarm_action_rule_name of this UpdateKeywordsAlarmRuleResponse.

        告警行动规则名称 >alarm_action_rule_name和notification_save_rule可以选填一个，如果都填，优先选择alarm_action_rule_name

        :param alarm_action_rule_name: The alarm_action_rule_name of this UpdateKeywordsAlarmRuleResponse.
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
        if not isinstance(other, UpdateKeywordsAlarmRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
