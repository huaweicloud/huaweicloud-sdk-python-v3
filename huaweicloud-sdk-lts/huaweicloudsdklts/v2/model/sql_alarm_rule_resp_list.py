# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlAlarmRuleRespList:


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
        'sql_alarm_rule_id': 'str',
        'sql_alarm_rule_description': 'str',
        'sql_requests': 'list[SqlRequest]',
        'frequency': 'Frequency',
        'condition_expression': 'str',
        'topics': 'list[Topics]',
        'sql_alarm_level': 'str',
        'sql_alarm_send': 'bool',
        'domain_id': 'str',
        'create_time': 'object',
        'update_time': 'object',
        'whether_english': 'bool'
    }

    attribute_map = {
        'sql_alarm_rule_name': 'sql_alarm_rule_name',
        'sql_alarm_rule_id': 'sql_alarm_rule_id',
        'sql_alarm_rule_description': 'sql_alarm_rule_description',
        'sql_requests': 'sql_requests',
        'frequency': 'frequency',
        'condition_expression': 'condition_expression',
        'topics': 'topics',
        'sql_alarm_level': 'sql_alarm_level',
        'sql_alarm_send': 'sql_alarm_send',
        'domain_id': 'domain_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'whether_english': 'whether_english'
    }

    def __init__(self, sql_alarm_rule_name=None, sql_alarm_rule_id=None, sql_alarm_rule_description=None, sql_requests=None, frequency=None, condition_expression=None, topics=None, sql_alarm_level=None, sql_alarm_send=None, domain_id=None, create_time=None, update_time=None, whether_english=None):
        """SqlAlarmRuleRespList - a model defined in huaweicloud sdk"""
        
        

        self._sql_alarm_rule_name = None
        self._sql_alarm_rule_id = None
        self._sql_alarm_rule_description = None
        self._sql_requests = None
        self._frequency = None
        self._condition_expression = None
        self._topics = None
        self._sql_alarm_level = None
        self._sql_alarm_send = None
        self._domain_id = None
        self._create_time = None
        self._update_time = None
        self._whether_english = None
        self.discriminator = None

        self.sql_alarm_rule_name = sql_alarm_rule_name
        self.sql_alarm_rule_id = sql_alarm_rule_id
        self.sql_alarm_rule_description = sql_alarm_rule_description
        self.sql_requests = sql_requests
        self.frequency = frequency
        self.condition_expression = condition_expression
        self.topics = topics
        self.sql_alarm_level = sql_alarm_level
        self.sql_alarm_send = sql_alarm_send
        self.domain_id = domain_id
        self.create_time = create_time
        self.update_time = update_time
        self.whether_english = whether_english

    @property
    def sql_alarm_rule_name(self):
        """Gets the sql_alarm_rule_name of this SqlAlarmRuleRespList.

        SQL告警名称

        :return: The sql_alarm_rule_name of this SqlAlarmRuleRespList.
        :rtype: str
        """
        return self._sql_alarm_rule_name

    @sql_alarm_rule_name.setter
    def sql_alarm_rule_name(self, sql_alarm_rule_name):
        """Sets the sql_alarm_rule_name of this SqlAlarmRuleRespList.

        SQL告警名称

        :param sql_alarm_rule_name: The sql_alarm_rule_name of this SqlAlarmRuleRespList.
        :type: str
        """
        self._sql_alarm_rule_name = sql_alarm_rule_name

    @property
    def sql_alarm_rule_id(self):
        """Gets the sql_alarm_rule_id of this SqlAlarmRuleRespList.

        SQL告警规则id

        :return: The sql_alarm_rule_id of this SqlAlarmRuleRespList.
        :rtype: str
        """
        return self._sql_alarm_rule_id

    @sql_alarm_rule_id.setter
    def sql_alarm_rule_id(self, sql_alarm_rule_id):
        """Sets the sql_alarm_rule_id of this SqlAlarmRuleRespList.

        SQL告警规则id

        :param sql_alarm_rule_id: The sql_alarm_rule_id of this SqlAlarmRuleRespList.
        :type: str
        """
        self._sql_alarm_rule_id = sql_alarm_rule_id

    @property
    def sql_alarm_rule_description(self):
        """Gets the sql_alarm_rule_description of this SqlAlarmRuleRespList.

        SQL告警信息描述

        :return: The sql_alarm_rule_description of this SqlAlarmRuleRespList.
        :rtype: str
        """
        return self._sql_alarm_rule_description

    @sql_alarm_rule_description.setter
    def sql_alarm_rule_description(self, sql_alarm_rule_description):
        """Sets the sql_alarm_rule_description of this SqlAlarmRuleRespList.

        SQL告警信息描述

        :param sql_alarm_rule_description: The sql_alarm_rule_description of this SqlAlarmRuleRespList.
        :type: str
        """
        self._sql_alarm_rule_description = sql_alarm_rule_description

    @property
    def sql_requests(self):
        """Gets the sql_requests of this SqlAlarmRuleRespList.

        SQL详细信息

        :return: The sql_requests of this SqlAlarmRuleRespList.
        :rtype: list[SqlRequest]
        """
        return self._sql_requests

    @sql_requests.setter
    def sql_requests(self, sql_requests):
        """Sets the sql_requests of this SqlAlarmRuleRespList.

        SQL详细信息

        :param sql_requests: The sql_requests of this SqlAlarmRuleRespList.
        :type: list[SqlRequest]
        """
        self._sql_requests = sql_requests

    @property
    def frequency(self):
        """Gets the frequency of this SqlAlarmRuleRespList.

        告警统计周期

        :return: The frequency of this SqlAlarmRuleRespList.
        :rtype: Frequency
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this SqlAlarmRuleRespList.

        告警统计周期

        :param frequency: The frequency of this SqlAlarmRuleRespList.
        :type: Frequency
        """
        self._frequency = frequency

    @property
    def condition_expression(self):
        """Gets the condition_expression of this SqlAlarmRuleRespList.

        条件表达式

        :return: The condition_expression of this SqlAlarmRuleRespList.
        :rtype: str
        """
        return self._condition_expression

    @condition_expression.setter
    def condition_expression(self, condition_expression):
        """Sets the condition_expression of this SqlAlarmRuleRespList.

        条件表达式

        :param condition_expression: The condition_expression of this SqlAlarmRuleRespList.
        :type: str
        """
        self._condition_expression = condition_expression

    @property
    def topics(self):
        """Gets the topics of this SqlAlarmRuleRespList.

        主题信息

        :return: The topics of this SqlAlarmRuleRespList.
        :rtype: list[Topics]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        """Sets the topics of this SqlAlarmRuleRespList.

        主题信息

        :param topics: The topics of this SqlAlarmRuleRespList.
        :type: list[Topics]
        """
        self._topics = topics

    @property
    def sql_alarm_level(self):
        """Gets the sql_alarm_level of this SqlAlarmRuleRespList.

        告警级别

        :return: The sql_alarm_level of this SqlAlarmRuleRespList.
        :rtype: str
        """
        return self._sql_alarm_level

    @sql_alarm_level.setter
    def sql_alarm_level(self, sql_alarm_level):
        """Sets the sql_alarm_level of this SqlAlarmRuleRespList.

        告警级别

        :param sql_alarm_level: The sql_alarm_level of this SqlAlarmRuleRespList.
        :type: str
        """
        self._sql_alarm_level = sql_alarm_level

    @property
    def sql_alarm_send(self):
        """Gets the sql_alarm_send of this SqlAlarmRuleRespList.

        是否发送

        :return: The sql_alarm_send of this SqlAlarmRuleRespList.
        :rtype: bool
        """
        return self._sql_alarm_send

    @sql_alarm_send.setter
    def sql_alarm_send(self, sql_alarm_send):
        """Sets the sql_alarm_send of this SqlAlarmRuleRespList.

        是否发送

        :param sql_alarm_send: The sql_alarm_send of this SqlAlarmRuleRespList.
        :type: bool
        """
        self._sql_alarm_send = sql_alarm_send

    @property
    def domain_id(self):
        """Gets the domain_id of this SqlAlarmRuleRespList.

        domainId

        :return: The domain_id of this SqlAlarmRuleRespList.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this SqlAlarmRuleRespList.

        domainId

        :param domain_id: The domain_id of this SqlAlarmRuleRespList.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def create_time(self):
        """Gets the create_time of this SqlAlarmRuleRespList.

        创建时间(毫秒时间戳)

        :return: The create_time of this SqlAlarmRuleRespList.
        :rtype: object
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this SqlAlarmRuleRespList.

        创建时间(毫秒时间戳)

        :param create_time: The create_time of this SqlAlarmRuleRespList.
        :type: object
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this SqlAlarmRuleRespList.

        更新时间(毫秒时间戳)

        :return: The update_time of this SqlAlarmRuleRespList.
        :rtype: object
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this SqlAlarmRuleRespList.

        更新时间(毫秒时间戳)

        :param update_time: The update_time of this SqlAlarmRuleRespList.
        :type: object
        """
        self._update_time = update_time

    @property
    def whether_english(self):
        """Gets the whether_english of this SqlAlarmRuleRespList.

        邮件附加信息是否英文

        :return: The whether_english of this SqlAlarmRuleRespList.
        :rtype: bool
        """
        return self._whether_english

    @whether_english.setter
    def whether_english(self, whether_english):
        """Sets the whether_english of this SqlAlarmRuleRespList.

        邮件附加信息是否英文

        :param whether_english: The whether_english of this SqlAlarmRuleRespList.
        :type: bool
        """
        self._whether_english = whether_english

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
        if not isinstance(other, SqlAlarmRuleRespList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
