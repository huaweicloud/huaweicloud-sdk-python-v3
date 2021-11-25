# coding: utf-8

import re
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
        'keywords_alarm_rule_description': 'str',
        'keywords_requests': 'list[KeywordsRequest]',
        'frequency': 'Frequency',
        'keywords_alarm_level': 'str',
        'keywords_alarm_send': 'bool',
        'domain_id': 'str',
        'create_time': 'object',
        'update_time': 'object',
        'notification_save_rule': 'NotificationSaveRule',
        'whether_english': 'bool',
        'language': 'str',
        'project_id': 'str',
        'topics': 'list[Topics]',
        'condition_expression': 'str',
        'id': 'str',
        'index_id': 'str',
        'key': 'str'
    }

    attribute_map = {
        'keywords_alarm_rule_id': 'keywords_alarm_rule_id',
        'keywords_alarm_rule_name': 'keywords_alarm_rule_name',
        'keywords_alarm_rule_description': 'keywords_alarm_rule_description',
        'keywords_requests': 'keywords_requests',
        'frequency': 'frequency',
        'keywords_alarm_level': 'keywords_alarm_level',
        'keywords_alarm_send': 'keywords_alarm_send',
        'domain_id': 'domain_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'notification_save_rule': 'notification_save_rule',
        'whether_english': 'whether_english',
        'language': 'language',
        'project_id': 'projectId',
        'topics': 'topics',
        'condition_expression': 'condition_expression',
        'id': 'id',
        'index_id': 'indexId',
        'key': 'key'
    }

    def __init__(self, keywords_alarm_rule_id=None, keywords_alarm_rule_name=None, keywords_alarm_rule_description=None, keywords_requests=None, frequency=None, keywords_alarm_level=None, keywords_alarm_send=None, domain_id=None, create_time=None, update_time=None, notification_save_rule=None, whether_english=None, language=None, project_id=None, topics=None, condition_expression=None, id=None, index_id=None, key=None):
        """UpdateKeywordsAlarmRuleResponse - a model defined in huaweicloud sdk"""
        
        super(UpdateKeywordsAlarmRuleResponse, self).__init__()

        self._keywords_alarm_rule_id = None
        self._keywords_alarm_rule_name = None
        self._keywords_alarm_rule_description = None
        self._keywords_requests = None
        self._frequency = None
        self._keywords_alarm_level = None
        self._keywords_alarm_send = None
        self._domain_id = None
        self._create_time = None
        self._update_time = None
        self._notification_save_rule = None
        self._whether_english = None
        self._language = None
        self._project_id = None
        self._topics = None
        self._condition_expression = None
        self._id = None
        self._index_id = None
        self._key = None
        self.discriminator = None

        if keywords_alarm_rule_id is not None:
            self.keywords_alarm_rule_id = keywords_alarm_rule_id
        if keywords_alarm_rule_name is not None:
            self.keywords_alarm_rule_name = keywords_alarm_rule_name
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
        if notification_save_rule is not None:
            self.notification_save_rule = notification_save_rule
        if whether_english is not None:
            self.whether_english = whether_english
        if language is not None:
            self.language = language
        if project_id is not None:
            self.project_id = project_id
        if topics is not None:
            self.topics = topics
        if condition_expression is not None:
            self.condition_expression = condition_expression
        if id is not None:
            self.id = id
        if index_id is not None:
            self.index_id = index_id
        if key is not None:
            self.key = key

    @property
    def keywords_alarm_rule_id(self):
        """Gets the keywords_alarm_rule_id of this UpdateKeywordsAlarmRuleResponse.

        关键词告警id

        :return: The keywords_alarm_rule_id of this UpdateKeywordsAlarmRuleResponse.
        :rtype: str
        """
        return self._keywords_alarm_rule_id

    @keywords_alarm_rule_id.setter
    def keywords_alarm_rule_id(self, keywords_alarm_rule_id):
        """Sets the keywords_alarm_rule_id of this UpdateKeywordsAlarmRuleResponse.

        关键词告警id

        :param keywords_alarm_rule_id: The keywords_alarm_rule_id of this UpdateKeywordsAlarmRuleResponse.
        :type: str
        """
        self._keywords_alarm_rule_id = keywords_alarm_rule_id

    @property
    def keywords_alarm_rule_name(self):
        """Gets the keywords_alarm_rule_name of this UpdateKeywordsAlarmRuleResponse.

        关键词告警名称

        :return: The keywords_alarm_rule_name of this UpdateKeywordsAlarmRuleResponse.
        :rtype: str
        """
        return self._keywords_alarm_rule_name

    @keywords_alarm_rule_name.setter
    def keywords_alarm_rule_name(self, keywords_alarm_rule_name):
        """Sets the keywords_alarm_rule_name of this UpdateKeywordsAlarmRuleResponse.

        关键词告警名称

        :param keywords_alarm_rule_name: The keywords_alarm_rule_name of this UpdateKeywordsAlarmRuleResponse.
        :type: str
        """
        self._keywords_alarm_rule_name = keywords_alarm_rule_name

    @property
    def keywords_alarm_rule_description(self):
        """Gets the keywords_alarm_rule_description of this UpdateKeywordsAlarmRuleResponse.

        关键词告警信息描述

        :return: The keywords_alarm_rule_description of this UpdateKeywordsAlarmRuleResponse.
        :rtype: str
        """
        return self._keywords_alarm_rule_description

    @keywords_alarm_rule_description.setter
    def keywords_alarm_rule_description(self, keywords_alarm_rule_description):
        """Sets the keywords_alarm_rule_description of this UpdateKeywordsAlarmRuleResponse.

        关键词告警信息描述

        :param keywords_alarm_rule_description: The keywords_alarm_rule_description of this UpdateKeywordsAlarmRuleResponse.
        :type: str
        """
        self._keywords_alarm_rule_description = keywords_alarm_rule_description

    @property
    def keywords_requests(self):
        """Gets the keywords_requests of this UpdateKeywordsAlarmRuleResponse.

        关键词详细信息

        :return: The keywords_requests of this UpdateKeywordsAlarmRuleResponse.
        :rtype: list[KeywordsRequest]
        """
        return self._keywords_requests

    @keywords_requests.setter
    def keywords_requests(self, keywords_requests):
        """Sets the keywords_requests of this UpdateKeywordsAlarmRuleResponse.

        关键词详细信息

        :param keywords_requests: The keywords_requests of this UpdateKeywordsAlarmRuleResponse.
        :type: list[KeywordsRequest]
        """
        self._keywords_requests = keywords_requests

    @property
    def frequency(self):
        """Gets the frequency of this UpdateKeywordsAlarmRuleResponse.

        告警统计周期

        :return: The frequency of this UpdateKeywordsAlarmRuleResponse.
        :rtype: Frequency
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this UpdateKeywordsAlarmRuleResponse.

        告警统计周期

        :param frequency: The frequency of this UpdateKeywordsAlarmRuleResponse.
        :type: Frequency
        """
        self._frequency = frequency

    @property
    def keywords_alarm_level(self):
        """Gets the keywords_alarm_level of this UpdateKeywordsAlarmRuleResponse.

        告警级别

        :return: The keywords_alarm_level of this UpdateKeywordsAlarmRuleResponse.
        :rtype: str
        """
        return self._keywords_alarm_level

    @keywords_alarm_level.setter
    def keywords_alarm_level(self, keywords_alarm_level):
        """Sets the keywords_alarm_level of this UpdateKeywordsAlarmRuleResponse.

        告警级别

        :param keywords_alarm_level: The keywords_alarm_level of this UpdateKeywordsAlarmRuleResponse.
        :type: str
        """
        self._keywords_alarm_level = keywords_alarm_level

    @property
    def keywords_alarm_send(self):
        """Gets the keywords_alarm_send of this UpdateKeywordsAlarmRuleResponse.

        是否发送

        :return: The keywords_alarm_send of this UpdateKeywordsAlarmRuleResponse.
        :rtype: bool
        """
        return self._keywords_alarm_send

    @keywords_alarm_send.setter
    def keywords_alarm_send(self, keywords_alarm_send):
        """Sets the keywords_alarm_send of this UpdateKeywordsAlarmRuleResponse.

        是否发送

        :param keywords_alarm_send: The keywords_alarm_send of this UpdateKeywordsAlarmRuleResponse.
        :type: bool
        """
        self._keywords_alarm_send = keywords_alarm_send

    @property
    def domain_id(self):
        """Gets the domain_id of this UpdateKeywordsAlarmRuleResponse.

        domainId

        :return: The domain_id of this UpdateKeywordsAlarmRuleResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this UpdateKeywordsAlarmRuleResponse.

        domainId

        :param domain_id: The domain_id of this UpdateKeywordsAlarmRuleResponse.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def create_time(self):
        """Gets the create_time of this UpdateKeywordsAlarmRuleResponse.

        创建时间(毫秒时间戳)

        :return: The create_time of this UpdateKeywordsAlarmRuleResponse.
        :rtype: object
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this UpdateKeywordsAlarmRuleResponse.

        创建时间(毫秒时间戳)

        :param create_time: The create_time of this UpdateKeywordsAlarmRuleResponse.
        :type: object
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this UpdateKeywordsAlarmRuleResponse.

        更新时间(毫秒时间戳)

        :return: The update_time of this UpdateKeywordsAlarmRuleResponse.
        :rtype: object
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this UpdateKeywordsAlarmRuleResponse.

        更新时间(毫秒时间戳)

        :param update_time: The update_time of this UpdateKeywordsAlarmRuleResponse.
        :type: object
        """
        self._update_time = update_time

    @property
    def notification_save_rule(self):
        """Gets the notification_save_rule of this UpdateKeywordsAlarmRuleResponse.

        通知主题

        :return: The notification_save_rule of this UpdateKeywordsAlarmRuleResponse.
        :rtype: NotificationSaveRule
        """
        return self._notification_save_rule

    @notification_save_rule.setter
    def notification_save_rule(self, notification_save_rule):
        """Sets the notification_save_rule of this UpdateKeywordsAlarmRuleResponse.

        通知主题

        :param notification_save_rule: The notification_save_rule of this UpdateKeywordsAlarmRuleResponse.
        :type: NotificationSaveRule
        """
        self._notification_save_rule = notification_save_rule

    @property
    def whether_english(self):
        """Gets the whether_english of this UpdateKeywordsAlarmRuleResponse.

        邮件附加信息是否英文

        :return: The whether_english of this UpdateKeywordsAlarmRuleResponse.
        :rtype: bool
        """
        return self._whether_english

    @whether_english.setter
    def whether_english(self, whether_english):
        """Sets the whether_english of this UpdateKeywordsAlarmRuleResponse.

        邮件附加信息是否英文

        :param whether_english: The whether_english of this UpdateKeywordsAlarmRuleResponse.
        :type: bool
        """
        self._whether_english = whether_english

    @property
    def language(self):
        """Gets the language of this UpdateKeywordsAlarmRuleResponse.

        语言

        :return: The language of this UpdateKeywordsAlarmRuleResponse.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this UpdateKeywordsAlarmRuleResponse.

        语言

        :param language: The language of this UpdateKeywordsAlarmRuleResponse.
        :type: str
        """
        self._language = language

    @property
    def project_id(self):
        """Gets the project_id of this UpdateKeywordsAlarmRuleResponse.

        项目id

        :return: The project_id of this UpdateKeywordsAlarmRuleResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this UpdateKeywordsAlarmRuleResponse.

        项目id

        :param project_id: The project_id of this UpdateKeywordsAlarmRuleResponse.
        :type: str
        """
        self._project_id = project_id

    @property
    def topics(self):
        """Gets the topics of this UpdateKeywordsAlarmRuleResponse.

        主题信息

        :return: The topics of this UpdateKeywordsAlarmRuleResponse.
        :rtype: list[Topics]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        """Sets the topics of this UpdateKeywordsAlarmRuleResponse.

        主题信息

        :param topics: The topics of this UpdateKeywordsAlarmRuleResponse.
        :type: list[Topics]
        """
        self._topics = topics

    @property
    def condition_expression(self):
        """Gets the condition_expression of this UpdateKeywordsAlarmRuleResponse.

        暂无

        :return: The condition_expression of this UpdateKeywordsAlarmRuleResponse.
        :rtype: str
        """
        return self._condition_expression

    @condition_expression.setter
    def condition_expression(self, condition_expression):
        """Sets the condition_expression of this UpdateKeywordsAlarmRuleResponse.

        暂无

        :param condition_expression: The condition_expression of this UpdateKeywordsAlarmRuleResponse.
        :type: str
        """
        self._condition_expression = condition_expression

    @property
    def id(self):
        """Gets the id of this UpdateKeywordsAlarmRuleResponse.

        暂无

        :return: The id of this UpdateKeywordsAlarmRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateKeywordsAlarmRuleResponse.

        暂无

        :param id: The id of this UpdateKeywordsAlarmRuleResponse.
        :type: str
        """
        self._id = id

    @property
    def index_id(self):
        """Gets the index_id of this UpdateKeywordsAlarmRuleResponse.

        暂无

        :return: The index_id of this UpdateKeywordsAlarmRuleResponse.
        :rtype: str
        """
        return self._index_id

    @index_id.setter
    def index_id(self, index_id):
        """Sets the index_id of this UpdateKeywordsAlarmRuleResponse.

        暂无

        :param index_id: The index_id of this UpdateKeywordsAlarmRuleResponse.
        :type: str
        """
        self._index_id = index_id

    @property
    def key(self):
        """Gets the key of this UpdateKeywordsAlarmRuleResponse.

        暂无

        :return: The key of this UpdateKeywordsAlarmRuleResponse.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this UpdateKeywordsAlarmRuleResponse.

        暂无

        :param key: The key of this UpdateKeywordsAlarmRuleResponse.
        :type: str
        """
        self._key = key

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