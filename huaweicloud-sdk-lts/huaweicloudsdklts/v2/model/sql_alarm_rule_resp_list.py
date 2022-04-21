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
        'create_time': 'int',
        'update_time': 'int',
        'template_name': 'str',
        'status': 'str'
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
        'template_name': 'template_name',
        'status': 'status'
    }

    def __init__(self, sql_alarm_rule_name=None, sql_alarm_rule_id=None, sql_alarm_rule_description=None, sql_requests=None, frequency=None, condition_expression=None, topics=None, sql_alarm_level=None, sql_alarm_send=None, domain_id=None, create_time=None, update_time=None, template_name=None, status=None):
        """SqlAlarmRuleRespList

        The model defined in huaweicloud sdk

        :param sql_alarm_rule_name: SQL告警名称
        :type sql_alarm_rule_name: str
        :param sql_alarm_rule_id: SQL告警规则id
        :type sql_alarm_rule_id: str
        :param sql_alarm_rule_description: SQL告警信息描述
        :type sql_alarm_rule_description: str
        :param sql_requests: SQL详细信息
        :type sql_requests: list[:class:`huaweicloudsdklts.v2.SqlRequest`]
        :param frequency: 告警统计周期
        :type frequency: :class:`huaweicloudsdklts.v2.Frequency`
        :param condition_expression: 条件表达式
        :type condition_expression: str
        :param topics: 主题信息
        :type topics: list[:class:`huaweicloudsdklts.v2.Topics`]
        :param sql_alarm_level: 告警级别
        :type sql_alarm_level: str
        :param sql_alarm_send: 是否发送
        :type sql_alarm_send: bool
        :param domain_id: domainId
        :type domain_id: str
        :param create_time: 创建时间(毫秒时间戳)
        :type create_time: int
        :param update_time: 更新时间(毫秒时间戳)
        :type update_time: int
        :param template_name: 
        :type template_name: str
        :param status: 
        :type status: str
        """
        
        

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
        self._template_name = None
        self._status = None
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
        if template_name is not None:
            self.template_name = template_name
        if status is not None:
            self.status = status

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
        :type sql_alarm_rule_name: str
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
        :type sql_alarm_rule_id: str
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
        :type sql_alarm_rule_description: str
        """
        self._sql_alarm_rule_description = sql_alarm_rule_description

    @property
    def sql_requests(self):
        """Gets the sql_requests of this SqlAlarmRuleRespList.

        SQL详细信息

        :return: The sql_requests of this SqlAlarmRuleRespList.
        :rtype: list[:class:`huaweicloudsdklts.v2.SqlRequest`]
        """
        return self._sql_requests

    @sql_requests.setter
    def sql_requests(self, sql_requests):
        """Sets the sql_requests of this SqlAlarmRuleRespList.

        SQL详细信息

        :param sql_requests: The sql_requests of this SqlAlarmRuleRespList.
        :type sql_requests: list[:class:`huaweicloudsdklts.v2.SqlRequest`]
        """
        self._sql_requests = sql_requests

    @property
    def frequency(self):
        """Gets the frequency of this SqlAlarmRuleRespList.

        告警统计周期

        :return: The frequency of this SqlAlarmRuleRespList.
        :rtype: :class:`huaweicloudsdklts.v2.Frequency`
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this SqlAlarmRuleRespList.

        告警统计周期

        :param frequency: The frequency of this SqlAlarmRuleRespList.
        :type frequency: :class:`huaweicloudsdklts.v2.Frequency`
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
        :type condition_expression: str
        """
        self._condition_expression = condition_expression

    @property
    def topics(self):
        """Gets the topics of this SqlAlarmRuleRespList.

        主题信息

        :return: The topics of this SqlAlarmRuleRespList.
        :rtype: list[:class:`huaweicloudsdklts.v2.Topics`]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        """Sets the topics of this SqlAlarmRuleRespList.

        主题信息

        :param topics: The topics of this SqlAlarmRuleRespList.
        :type topics: list[:class:`huaweicloudsdklts.v2.Topics`]
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
        :type sql_alarm_level: str
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
        :type sql_alarm_send: bool
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
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def create_time(self):
        """Gets the create_time of this SqlAlarmRuleRespList.

        创建时间(毫秒时间戳)

        :return: The create_time of this SqlAlarmRuleRespList.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this SqlAlarmRuleRespList.

        创建时间(毫秒时间戳)

        :param create_time: The create_time of this SqlAlarmRuleRespList.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this SqlAlarmRuleRespList.

        更新时间(毫秒时间戳)

        :return: The update_time of this SqlAlarmRuleRespList.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this SqlAlarmRuleRespList.

        更新时间(毫秒时间戳)

        :param update_time: The update_time of this SqlAlarmRuleRespList.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def template_name(self):
        """Gets the template_name of this SqlAlarmRuleRespList.


        :return: The template_name of this SqlAlarmRuleRespList.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this SqlAlarmRuleRespList.


        :param template_name: The template_name of this SqlAlarmRuleRespList.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def status(self):
        """Gets the status of this SqlAlarmRuleRespList.


        :return: The status of this SqlAlarmRuleRespList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SqlAlarmRuleRespList.


        :param status: The status of this SqlAlarmRuleRespList.
        :type status: str
        """
        self._status = status

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
