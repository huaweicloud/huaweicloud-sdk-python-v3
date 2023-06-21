# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowQualityTaskDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'description': 'str',
        'category_id': 'int',
        'level': 'str',
        'alarm_condition': 'str',
        'alarm_notify': 'bool',
        'alarm_notify_type': 'str',
        'alarm_notify_topic': 'str',
        'schedule_type': 'str',
        'schedule_start_date': 'str',
        'schedule_end_date': 'str',
        'schedule_period': 'str',
        'schedule_interval': 'str',
        'schedule_start_time': 'str',
        'schedule_end_time': 'str',
        'create_time': 'int',
        'last_run_time': 'int',
        'sub_rules': 'list[QualityTaskRuleDetailForOpenApi]',
        'schedule_cron': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'category_id': 'category_id',
        'level': 'level',
        'alarm_condition': 'alarm_condition',
        'alarm_notify': 'alarm_notify',
        'alarm_notify_type': 'alarm_notify_type',
        'alarm_notify_topic': 'alarm_notify_topic',
        'schedule_type': 'schedule_type',
        'schedule_start_date': 'schedule_start_date',
        'schedule_end_date': 'schedule_end_date',
        'schedule_period': 'schedule_period',
        'schedule_interval': 'schedule_interval',
        'schedule_start_time': 'schedule_start_time',
        'schedule_end_time': 'schedule_end_time',
        'create_time': 'create_time',
        'last_run_time': 'last_run_time',
        'sub_rules': 'sub_rules',
        'schedule_cron': 'schedule_cron'
    }

    def __init__(self, id=None, name=None, description=None, category_id=None, level=None, alarm_condition=None, alarm_notify=None, alarm_notify_type=None, alarm_notify_topic=None, schedule_type=None, schedule_start_date=None, schedule_end_date=None, schedule_period=None, schedule_interval=None, schedule_start_time=None, schedule_end_time=None, create_time=None, last_run_time=None, sub_rules=None, schedule_cron=None):
        """ShowQualityTaskDetailResponse

        The model defined in huaweicloud sdk

        :param id: ID
        :type id: int
        :param name: 作业名称
        :type name: str
        :param description: 作业描述
        :type description: str
        :param category_id: 所属目录ID
        :type category_id: int
        :param level: SUGGEST:提示, MINOR:一般, MAJOR:严重, FATAL:致命
        :type level: str
        :param alarm_condition: 统一告警条件
        :type alarm_condition: str
        :param alarm_notify: 是否开启通知告警
        :type alarm_notify: bool
        :param alarm_notify_type: TRIGGER_ALARM:触发告警, RUN_SUCCESS:运行成功, TRIGGER_ALARM_AND_RUNNING_SUCCESS:触发告警和运行成功
        :type alarm_notify_type: str
        :param alarm_notify_topic: 通知主题名
        :type alarm_notify_topic: str
        :param schedule_type: 调度类型，ONCE：单次调度，PERIODIC：周期性调度
        :type schedule_type: str
        :param schedule_start_date: 调度开始日期
        :type schedule_start_date: str
        :param schedule_end_date: 调度结束日期
        :type schedule_end_date: str
        :param schedule_period: 调度周期，MINUTE:按分钟调度，HOUR:按小时调度，DAY:按天调度，WEEK:按周调度
        :type schedule_period: str
        :param schedule_interval: 调度间隔，注意：当调度周期为分钟、小时、天时，间隔时间为数字；而当调度周期为周时，调度间隔为星期的英文，如：每周一、周二调度时，schedule_interval为\&quot;MONDAY,TUESDAY\&quot;
        :type schedule_interval: str
        :param schedule_start_time: 调度开始时间
        :type schedule_start_time: str
        :param schedule_end_time: 调度结束时间
        :type schedule_end_time: str
        :param create_time: 最近运行时间,13位时间戳(精确到毫秒)
        :type create_time: int
        :param last_run_time: 最近运行时间,13位时间戳(精确到毫秒)
        :type last_run_time: int
        :param sub_rules: 子规则
        :type sub_rules: list[:class:`huaweicloudsdkdataartsstudio.v1.QualityTaskRuleDetailForOpenApi`]
        :param schedule_cron: 调度cron表达式
        :type schedule_cron: str
        """
        
        super(ShowQualityTaskDetailResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._category_id = None
        self._level = None
        self._alarm_condition = None
        self._alarm_notify = None
        self._alarm_notify_type = None
        self._alarm_notify_topic = None
        self._schedule_type = None
        self._schedule_start_date = None
        self._schedule_end_date = None
        self._schedule_period = None
        self._schedule_interval = None
        self._schedule_start_time = None
        self._schedule_end_time = None
        self._create_time = None
        self._last_run_time = None
        self._sub_rules = None
        self._schedule_cron = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if category_id is not None:
            self.category_id = category_id
        if level is not None:
            self.level = level
        if alarm_condition is not None:
            self.alarm_condition = alarm_condition
        if alarm_notify is not None:
            self.alarm_notify = alarm_notify
        if alarm_notify_type is not None:
            self.alarm_notify_type = alarm_notify_type
        if alarm_notify_topic is not None:
            self.alarm_notify_topic = alarm_notify_topic
        if schedule_type is not None:
            self.schedule_type = schedule_type
        if schedule_start_date is not None:
            self.schedule_start_date = schedule_start_date
        if schedule_end_date is not None:
            self.schedule_end_date = schedule_end_date
        if schedule_period is not None:
            self.schedule_period = schedule_period
        if schedule_interval is not None:
            self.schedule_interval = schedule_interval
        if schedule_start_time is not None:
            self.schedule_start_time = schedule_start_time
        if schedule_end_time is not None:
            self.schedule_end_time = schedule_end_time
        if create_time is not None:
            self.create_time = create_time
        if last_run_time is not None:
            self.last_run_time = last_run_time
        if sub_rules is not None:
            self.sub_rules = sub_rules
        if schedule_cron is not None:
            self.schedule_cron = schedule_cron

    @property
    def id(self):
        """Gets the id of this ShowQualityTaskDetailResponse.

        ID

        :return: The id of this ShowQualityTaskDetailResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowQualityTaskDetailResponse.

        ID

        :param id: The id of this ShowQualityTaskDetailResponse.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowQualityTaskDetailResponse.

        作业名称

        :return: The name of this ShowQualityTaskDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowQualityTaskDetailResponse.

        作业名称

        :param name: The name of this ShowQualityTaskDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ShowQualityTaskDetailResponse.

        作业描述

        :return: The description of this ShowQualityTaskDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowQualityTaskDetailResponse.

        作业描述

        :param description: The description of this ShowQualityTaskDetailResponse.
        :type description: str
        """
        self._description = description

    @property
    def category_id(self):
        """Gets the category_id of this ShowQualityTaskDetailResponse.

        所属目录ID

        :return: The category_id of this ShowQualityTaskDetailResponse.
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this ShowQualityTaskDetailResponse.

        所属目录ID

        :param category_id: The category_id of this ShowQualityTaskDetailResponse.
        :type category_id: int
        """
        self._category_id = category_id

    @property
    def level(self):
        """Gets the level of this ShowQualityTaskDetailResponse.

        SUGGEST:提示, MINOR:一般, MAJOR:严重, FATAL:致命

        :return: The level of this ShowQualityTaskDetailResponse.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this ShowQualityTaskDetailResponse.

        SUGGEST:提示, MINOR:一般, MAJOR:严重, FATAL:致命

        :param level: The level of this ShowQualityTaskDetailResponse.
        :type level: str
        """
        self._level = level

    @property
    def alarm_condition(self):
        """Gets the alarm_condition of this ShowQualityTaskDetailResponse.

        统一告警条件

        :return: The alarm_condition of this ShowQualityTaskDetailResponse.
        :rtype: str
        """
        return self._alarm_condition

    @alarm_condition.setter
    def alarm_condition(self, alarm_condition):
        """Sets the alarm_condition of this ShowQualityTaskDetailResponse.

        统一告警条件

        :param alarm_condition: The alarm_condition of this ShowQualityTaskDetailResponse.
        :type alarm_condition: str
        """
        self._alarm_condition = alarm_condition

    @property
    def alarm_notify(self):
        """Gets the alarm_notify of this ShowQualityTaskDetailResponse.

        是否开启通知告警

        :return: The alarm_notify of this ShowQualityTaskDetailResponse.
        :rtype: bool
        """
        return self._alarm_notify

    @alarm_notify.setter
    def alarm_notify(self, alarm_notify):
        """Sets the alarm_notify of this ShowQualityTaskDetailResponse.

        是否开启通知告警

        :param alarm_notify: The alarm_notify of this ShowQualityTaskDetailResponse.
        :type alarm_notify: bool
        """
        self._alarm_notify = alarm_notify

    @property
    def alarm_notify_type(self):
        """Gets the alarm_notify_type of this ShowQualityTaskDetailResponse.

        TRIGGER_ALARM:触发告警, RUN_SUCCESS:运行成功, TRIGGER_ALARM_AND_RUNNING_SUCCESS:触发告警和运行成功

        :return: The alarm_notify_type of this ShowQualityTaskDetailResponse.
        :rtype: str
        """
        return self._alarm_notify_type

    @alarm_notify_type.setter
    def alarm_notify_type(self, alarm_notify_type):
        """Sets the alarm_notify_type of this ShowQualityTaskDetailResponse.

        TRIGGER_ALARM:触发告警, RUN_SUCCESS:运行成功, TRIGGER_ALARM_AND_RUNNING_SUCCESS:触发告警和运行成功

        :param alarm_notify_type: The alarm_notify_type of this ShowQualityTaskDetailResponse.
        :type alarm_notify_type: str
        """
        self._alarm_notify_type = alarm_notify_type

    @property
    def alarm_notify_topic(self):
        """Gets the alarm_notify_topic of this ShowQualityTaskDetailResponse.

        通知主题名

        :return: The alarm_notify_topic of this ShowQualityTaskDetailResponse.
        :rtype: str
        """
        return self._alarm_notify_topic

    @alarm_notify_topic.setter
    def alarm_notify_topic(self, alarm_notify_topic):
        """Sets the alarm_notify_topic of this ShowQualityTaskDetailResponse.

        通知主题名

        :param alarm_notify_topic: The alarm_notify_topic of this ShowQualityTaskDetailResponse.
        :type alarm_notify_topic: str
        """
        self._alarm_notify_topic = alarm_notify_topic

    @property
    def schedule_type(self):
        """Gets the schedule_type of this ShowQualityTaskDetailResponse.

        调度类型，ONCE：单次调度，PERIODIC：周期性调度

        :return: The schedule_type of this ShowQualityTaskDetailResponse.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """Sets the schedule_type of this ShowQualityTaskDetailResponse.

        调度类型，ONCE：单次调度，PERIODIC：周期性调度

        :param schedule_type: The schedule_type of this ShowQualityTaskDetailResponse.
        :type schedule_type: str
        """
        self._schedule_type = schedule_type

    @property
    def schedule_start_date(self):
        """Gets the schedule_start_date of this ShowQualityTaskDetailResponse.

        调度开始日期

        :return: The schedule_start_date of this ShowQualityTaskDetailResponse.
        :rtype: str
        """
        return self._schedule_start_date

    @schedule_start_date.setter
    def schedule_start_date(self, schedule_start_date):
        """Sets the schedule_start_date of this ShowQualityTaskDetailResponse.

        调度开始日期

        :param schedule_start_date: The schedule_start_date of this ShowQualityTaskDetailResponse.
        :type schedule_start_date: str
        """
        self._schedule_start_date = schedule_start_date

    @property
    def schedule_end_date(self):
        """Gets the schedule_end_date of this ShowQualityTaskDetailResponse.

        调度结束日期

        :return: The schedule_end_date of this ShowQualityTaskDetailResponse.
        :rtype: str
        """
        return self._schedule_end_date

    @schedule_end_date.setter
    def schedule_end_date(self, schedule_end_date):
        """Sets the schedule_end_date of this ShowQualityTaskDetailResponse.

        调度结束日期

        :param schedule_end_date: The schedule_end_date of this ShowQualityTaskDetailResponse.
        :type schedule_end_date: str
        """
        self._schedule_end_date = schedule_end_date

    @property
    def schedule_period(self):
        """Gets the schedule_period of this ShowQualityTaskDetailResponse.

        调度周期，MINUTE:按分钟调度，HOUR:按小时调度，DAY:按天调度，WEEK:按周调度

        :return: The schedule_period of this ShowQualityTaskDetailResponse.
        :rtype: str
        """
        return self._schedule_period

    @schedule_period.setter
    def schedule_period(self, schedule_period):
        """Sets the schedule_period of this ShowQualityTaskDetailResponse.

        调度周期，MINUTE:按分钟调度，HOUR:按小时调度，DAY:按天调度，WEEK:按周调度

        :param schedule_period: The schedule_period of this ShowQualityTaskDetailResponse.
        :type schedule_period: str
        """
        self._schedule_period = schedule_period

    @property
    def schedule_interval(self):
        """Gets the schedule_interval of this ShowQualityTaskDetailResponse.

        调度间隔，注意：当调度周期为分钟、小时、天时，间隔时间为数字；而当调度周期为周时，调度间隔为星期的英文，如：每周一、周二调度时，schedule_interval为\"MONDAY,TUESDAY\"

        :return: The schedule_interval of this ShowQualityTaskDetailResponse.
        :rtype: str
        """
        return self._schedule_interval

    @schedule_interval.setter
    def schedule_interval(self, schedule_interval):
        """Sets the schedule_interval of this ShowQualityTaskDetailResponse.

        调度间隔，注意：当调度周期为分钟、小时、天时，间隔时间为数字；而当调度周期为周时，调度间隔为星期的英文，如：每周一、周二调度时，schedule_interval为\"MONDAY,TUESDAY\"

        :param schedule_interval: The schedule_interval of this ShowQualityTaskDetailResponse.
        :type schedule_interval: str
        """
        self._schedule_interval = schedule_interval

    @property
    def schedule_start_time(self):
        """Gets the schedule_start_time of this ShowQualityTaskDetailResponse.

        调度开始时间

        :return: The schedule_start_time of this ShowQualityTaskDetailResponse.
        :rtype: str
        """
        return self._schedule_start_time

    @schedule_start_time.setter
    def schedule_start_time(self, schedule_start_time):
        """Sets the schedule_start_time of this ShowQualityTaskDetailResponse.

        调度开始时间

        :param schedule_start_time: The schedule_start_time of this ShowQualityTaskDetailResponse.
        :type schedule_start_time: str
        """
        self._schedule_start_time = schedule_start_time

    @property
    def schedule_end_time(self):
        """Gets the schedule_end_time of this ShowQualityTaskDetailResponse.

        调度结束时间

        :return: The schedule_end_time of this ShowQualityTaskDetailResponse.
        :rtype: str
        """
        return self._schedule_end_time

    @schedule_end_time.setter
    def schedule_end_time(self, schedule_end_time):
        """Sets the schedule_end_time of this ShowQualityTaskDetailResponse.

        调度结束时间

        :param schedule_end_time: The schedule_end_time of this ShowQualityTaskDetailResponse.
        :type schedule_end_time: str
        """
        self._schedule_end_time = schedule_end_time

    @property
    def create_time(self):
        """Gets the create_time of this ShowQualityTaskDetailResponse.

        最近运行时间,13位时间戳(精确到毫秒)

        :return: The create_time of this ShowQualityTaskDetailResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowQualityTaskDetailResponse.

        最近运行时间,13位时间戳(精确到毫秒)

        :param create_time: The create_time of this ShowQualityTaskDetailResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def last_run_time(self):
        """Gets the last_run_time of this ShowQualityTaskDetailResponse.

        最近运行时间,13位时间戳(精确到毫秒)

        :return: The last_run_time of this ShowQualityTaskDetailResponse.
        :rtype: int
        """
        return self._last_run_time

    @last_run_time.setter
    def last_run_time(self, last_run_time):
        """Sets the last_run_time of this ShowQualityTaskDetailResponse.

        最近运行时间,13位时间戳(精确到毫秒)

        :param last_run_time: The last_run_time of this ShowQualityTaskDetailResponse.
        :type last_run_time: int
        """
        self._last_run_time = last_run_time

    @property
    def sub_rules(self):
        """Gets the sub_rules of this ShowQualityTaskDetailResponse.

        子规则

        :return: The sub_rules of this ShowQualityTaskDetailResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.QualityTaskRuleDetailForOpenApi`]
        """
        return self._sub_rules

    @sub_rules.setter
    def sub_rules(self, sub_rules):
        """Sets the sub_rules of this ShowQualityTaskDetailResponse.

        子规则

        :param sub_rules: The sub_rules of this ShowQualityTaskDetailResponse.
        :type sub_rules: list[:class:`huaweicloudsdkdataartsstudio.v1.QualityTaskRuleDetailForOpenApi`]
        """
        self._sub_rules = sub_rules

    @property
    def schedule_cron(self):
        """Gets the schedule_cron of this ShowQualityTaskDetailResponse.

        调度cron表达式

        :return: The schedule_cron of this ShowQualityTaskDetailResponse.
        :rtype: str
        """
        return self._schedule_cron

    @schedule_cron.setter
    def schedule_cron(self, schedule_cron):
        """Sets the schedule_cron of this ShowQualityTaskDetailResponse.

        调度cron表达式

        :param schedule_cron: The schedule_cron of this ShowQualityTaskDetailResponse.
        :type schedule_cron: str
        """
        self._schedule_cron = schedule_cron

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
        if not isinstance(other, ShowQualityTaskDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
