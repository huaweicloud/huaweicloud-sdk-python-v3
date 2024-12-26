# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAttackLogAlarmConfigDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_name': 'str',
        'alarm_id': 'str',
        'alarm_time_period': 'int',
        'alarm_type': 'int',
        'enable_status': 'int',
        'frequency_count': 'int',
        'frequency_time': 'int',
        'language': 'str',
        'severity': 'str',
        'topic_urn': 'str',
        'username': 'str'
    }

    attribute_map = {
        'account_name': 'account_name',
        'alarm_id': 'alarm_id',
        'alarm_time_period': 'alarm_time_period',
        'alarm_type': 'alarm_type',
        'enable_status': 'enable_status',
        'frequency_count': 'frequency_count',
        'frequency_time': 'frequency_time',
        'language': 'language',
        'severity': 'severity',
        'topic_urn': 'topic_urn',
        'username': 'username'
    }

    def __init__(self, account_name=None, alarm_id=None, alarm_time_period=None, alarm_type=None, enable_status=None, frequency_count=None, frequency_time=None, language=None, severity=None, topic_urn=None, username=None):
        """UpdateAttackLogAlarmConfigDto

        The model defined in huaweicloud sdk

        :param account_name: 账号名称
        :type account_name: str
        :param alarm_id: 告警id
        :type alarm_id: str
        :param alarm_time_period: 告警周期，0：全天，1：8时到22时
        :type alarm_time_period: int
        :param alarm_type: 告警类型 0:攻击告警; 1:流量超额预警; 2:EIP未防护告警; 3:威胁情报告警
        :type alarm_type: int
        :param enable_status: 告警状态 0:失效; 1:生效
        :type enable_status: int
        :param frequency_count: 告警触发频次
        :type frequency_count: int
        :param frequency_time: 告警频次时间范围
        :type frequency_time: int
        :param language: 告警语言
        :type language: str
        :param severity: 告警等级
        :type severity: str
        :param topic_urn: 告警urn
        :type topic_urn: str
        :param username: 用户名称
        :type username: str
        """
        
        

        self._account_name = None
        self._alarm_id = None
        self._alarm_time_period = None
        self._alarm_type = None
        self._enable_status = None
        self._frequency_count = None
        self._frequency_time = None
        self._language = None
        self._severity = None
        self._topic_urn = None
        self._username = None
        self.discriminator = None

        if account_name is not None:
            self.account_name = account_name
        if alarm_id is not None:
            self.alarm_id = alarm_id
        if alarm_time_period is not None:
            self.alarm_time_period = alarm_time_period
        if alarm_type is not None:
            self.alarm_type = alarm_type
        if enable_status is not None:
            self.enable_status = enable_status
        if frequency_count is not None:
            self.frequency_count = frequency_count
        if frequency_time is not None:
            self.frequency_time = frequency_time
        if language is not None:
            self.language = language
        if severity is not None:
            self.severity = severity
        if topic_urn is not None:
            self.topic_urn = topic_urn
        if username is not None:
            self.username = username

    @property
    def account_name(self):
        """Gets the account_name of this UpdateAttackLogAlarmConfigDto.

        账号名称

        :return: The account_name of this UpdateAttackLogAlarmConfigDto.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this UpdateAttackLogAlarmConfigDto.

        账号名称

        :param account_name: The account_name of this UpdateAttackLogAlarmConfigDto.
        :type account_name: str
        """
        self._account_name = account_name

    @property
    def alarm_id(self):
        """Gets the alarm_id of this UpdateAttackLogAlarmConfigDto.

        告警id

        :return: The alarm_id of this UpdateAttackLogAlarmConfigDto.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        """Sets the alarm_id of this UpdateAttackLogAlarmConfigDto.

        告警id

        :param alarm_id: The alarm_id of this UpdateAttackLogAlarmConfigDto.
        :type alarm_id: str
        """
        self._alarm_id = alarm_id

    @property
    def alarm_time_period(self):
        """Gets the alarm_time_period of this UpdateAttackLogAlarmConfigDto.

        告警周期，0：全天，1：8时到22时

        :return: The alarm_time_period of this UpdateAttackLogAlarmConfigDto.
        :rtype: int
        """
        return self._alarm_time_period

    @alarm_time_period.setter
    def alarm_time_period(self, alarm_time_period):
        """Sets the alarm_time_period of this UpdateAttackLogAlarmConfigDto.

        告警周期，0：全天，1：8时到22时

        :param alarm_time_period: The alarm_time_period of this UpdateAttackLogAlarmConfigDto.
        :type alarm_time_period: int
        """
        self._alarm_time_period = alarm_time_period

    @property
    def alarm_type(self):
        """Gets the alarm_type of this UpdateAttackLogAlarmConfigDto.

        告警类型 0:攻击告警; 1:流量超额预警; 2:EIP未防护告警; 3:威胁情报告警

        :return: The alarm_type of this UpdateAttackLogAlarmConfigDto.
        :rtype: int
        """
        return self._alarm_type

    @alarm_type.setter
    def alarm_type(self, alarm_type):
        """Sets the alarm_type of this UpdateAttackLogAlarmConfigDto.

        告警类型 0:攻击告警; 1:流量超额预警; 2:EIP未防护告警; 3:威胁情报告警

        :param alarm_type: The alarm_type of this UpdateAttackLogAlarmConfigDto.
        :type alarm_type: int
        """
        self._alarm_type = alarm_type

    @property
    def enable_status(self):
        """Gets the enable_status of this UpdateAttackLogAlarmConfigDto.

        告警状态 0:失效; 1:生效

        :return: The enable_status of this UpdateAttackLogAlarmConfigDto.
        :rtype: int
        """
        return self._enable_status

    @enable_status.setter
    def enable_status(self, enable_status):
        """Sets the enable_status of this UpdateAttackLogAlarmConfigDto.

        告警状态 0:失效; 1:生效

        :param enable_status: The enable_status of this UpdateAttackLogAlarmConfigDto.
        :type enable_status: int
        """
        self._enable_status = enable_status

    @property
    def frequency_count(self):
        """Gets the frequency_count of this UpdateAttackLogAlarmConfigDto.

        告警触发频次

        :return: The frequency_count of this UpdateAttackLogAlarmConfigDto.
        :rtype: int
        """
        return self._frequency_count

    @frequency_count.setter
    def frequency_count(self, frequency_count):
        """Sets the frequency_count of this UpdateAttackLogAlarmConfigDto.

        告警触发频次

        :param frequency_count: The frequency_count of this UpdateAttackLogAlarmConfigDto.
        :type frequency_count: int
        """
        self._frequency_count = frequency_count

    @property
    def frequency_time(self):
        """Gets the frequency_time of this UpdateAttackLogAlarmConfigDto.

        告警频次时间范围

        :return: The frequency_time of this UpdateAttackLogAlarmConfigDto.
        :rtype: int
        """
        return self._frequency_time

    @frequency_time.setter
    def frequency_time(self, frequency_time):
        """Sets the frequency_time of this UpdateAttackLogAlarmConfigDto.

        告警频次时间范围

        :param frequency_time: The frequency_time of this UpdateAttackLogAlarmConfigDto.
        :type frequency_time: int
        """
        self._frequency_time = frequency_time

    @property
    def language(self):
        """Gets the language of this UpdateAttackLogAlarmConfigDto.

        告警语言

        :return: The language of this UpdateAttackLogAlarmConfigDto.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this UpdateAttackLogAlarmConfigDto.

        告警语言

        :param language: The language of this UpdateAttackLogAlarmConfigDto.
        :type language: str
        """
        self._language = language

    @property
    def severity(self):
        """Gets the severity of this UpdateAttackLogAlarmConfigDto.

        告警等级

        :return: The severity of this UpdateAttackLogAlarmConfigDto.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this UpdateAttackLogAlarmConfigDto.

        告警等级

        :param severity: The severity of this UpdateAttackLogAlarmConfigDto.
        :type severity: str
        """
        self._severity = severity

    @property
    def topic_urn(self):
        """Gets the topic_urn of this UpdateAttackLogAlarmConfigDto.

        告警urn

        :return: The topic_urn of this UpdateAttackLogAlarmConfigDto.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        """Sets the topic_urn of this UpdateAttackLogAlarmConfigDto.

        告警urn

        :param topic_urn: The topic_urn of this UpdateAttackLogAlarmConfigDto.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def username(self):
        """Gets the username of this UpdateAttackLogAlarmConfigDto.

        用户名称

        :return: The username of this UpdateAttackLogAlarmConfigDto.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UpdateAttackLogAlarmConfigDto.

        用户名称

        :param username: The username of this UpdateAttackLogAlarmConfigDto.
        :type username: str
        """
        self._username = username

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
        if not isinstance(other, UpdateAttackLogAlarmConfigDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
