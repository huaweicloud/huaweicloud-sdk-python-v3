# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConsistencyTaskDetailResponse(SdkResponse):

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
        'schedule_period': 'str',
        'schedule_interval': 'str',
        'schedule_start_time': 'str',
        'schedule_end_time': 'str',
        'create_time': 'int',
        'last_run_time': 'int',
        'sub_rules': 'list[list[ConsistencyRuleDetailForOpenApi]]'
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
        'schedule_period': 'schedule_period',
        'schedule_interval': 'schedule_interval',
        'schedule_start_time': 'schedule_start_time',
        'schedule_end_time': 'schedule_end_time',
        'create_time': 'create_time',
        'last_run_time': 'last_run_time',
        'sub_rules': 'sub_rules'
    }

    def __init__(self, id=None, name=None, description=None, category_id=None, level=None, alarm_condition=None, alarm_notify=None, alarm_notify_type=None, alarm_notify_topic=None, schedule_type=None, schedule_period=None, schedule_interval=None, schedule_start_time=None, schedule_end_time=None, create_time=None, last_run_time=None, sub_rules=None):
        r"""ShowConsistencyTaskDetailResponse

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
        :param schedule_period: 调度周期，MINUTE:按分钟调度，HOUR:按小时调度，DAY:按天调度，WEEK:按周调度
        :type schedule_period: str
        :param schedule_interval: 调度间隔，注意：当调度周期为分钟、小时、天时，间隔时间为数字；而当调度周期为周时，调度间隔为星期的英文，如：每周一、周二调度时，schedule_interval为MONDAY,TUESDAY
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
        :type sub_rules: list[list[ConsistencyRuleDetailForOpenApi]]
        """
        
        super(ShowConsistencyTaskDetailResponse, self).__init__()

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
        self._schedule_period = None
        self._schedule_interval = None
        self._schedule_start_time = None
        self._schedule_end_time = None
        self._create_time = None
        self._last_run_time = None
        self._sub_rules = None
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

    @property
    def id(self):
        r"""Gets the id of this ShowConsistencyTaskDetailResponse.

        ID

        :return: The id of this ShowConsistencyTaskDetailResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowConsistencyTaskDetailResponse.

        ID

        :param id: The id of this ShowConsistencyTaskDetailResponse.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowConsistencyTaskDetailResponse.

        作业名称

        :return: The name of this ShowConsistencyTaskDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowConsistencyTaskDetailResponse.

        作业名称

        :param name: The name of this ShowConsistencyTaskDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowConsistencyTaskDetailResponse.

        作业描述

        :return: The description of this ShowConsistencyTaskDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowConsistencyTaskDetailResponse.

        作业描述

        :param description: The description of this ShowConsistencyTaskDetailResponse.
        :type description: str
        """
        self._description = description

    @property
    def category_id(self):
        r"""Gets the category_id of this ShowConsistencyTaskDetailResponse.

        所属目录ID

        :return: The category_id of this ShowConsistencyTaskDetailResponse.
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        r"""Sets the category_id of this ShowConsistencyTaskDetailResponse.

        所属目录ID

        :param category_id: The category_id of this ShowConsistencyTaskDetailResponse.
        :type category_id: int
        """
        self._category_id = category_id

    @property
    def level(self):
        r"""Gets the level of this ShowConsistencyTaskDetailResponse.

        SUGGEST:提示, MINOR:一般, MAJOR:严重, FATAL:致命

        :return: The level of this ShowConsistencyTaskDetailResponse.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this ShowConsistencyTaskDetailResponse.

        SUGGEST:提示, MINOR:一般, MAJOR:严重, FATAL:致命

        :param level: The level of this ShowConsistencyTaskDetailResponse.
        :type level: str
        """
        self._level = level

    @property
    def alarm_condition(self):
        r"""Gets the alarm_condition of this ShowConsistencyTaskDetailResponse.

        统一告警条件

        :return: The alarm_condition of this ShowConsistencyTaskDetailResponse.
        :rtype: str
        """
        return self._alarm_condition

    @alarm_condition.setter
    def alarm_condition(self, alarm_condition):
        r"""Sets the alarm_condition of this ShowConsistencyTaskDetailResponse.

        统一告警条件

        :param alarm_condition: The alarm_condition of this ShowConsistencyTaskDetailResponse.
        :type alarm_condition: str
        """
        self._alarm_condition = alarm_condition

    @property
    def alarm_notify(self):
        r"""Gets the alarm_notify of this ShowConsistencyTaskDetailResponse.

        是否开启通知告警

        :return: The alarm_notify of this ShowConsistencyTaskDetailResponse.
        :rtype: bool
        """
        return self._alarm_notify

    @alarm_notify.setter
    def alarm_notify(self, alarm_notify):
        r"""Sets the alarm_notify of this ShowConsistencyTaskDetailResponse.

        是否开启通知告警

        :param alarm_notify: The alarm_notify of this ShowConsistencyTaskDetailResponse.
        :type alarm_notify: bool
        """
        self._alarm_notify = alarm_notify

    @property
    def alarm_notify_type(self):
        r"""Gets the alarm_notify_type of this ShowConsistencyTaskDetailResponse.

        TRIGGER_ALARM:触发告警, RUN_SUCCESS:运行成功, TRIGGER_ALARM_AND_RUNNING_SUCCESS:触发告警和运行成功

        :return: The alarm_notify_type of this ShowConsistencyTaskDetailResponse.
        :rtype: str
        """
        return self._alarm_notify_type

    @alarm_notify_type.setter
    def alarm_notify_type(self, alarm_notify_type):
        r"""Sets the alarm_notify_type of this ShowConsistencyTaskDetailResponse.

        TRIGGER_ALARM:触发告警, RUN_SUCCESS:运行成功, TRIGGER_ALARM_AND_RUNNING_SUCCESS:触发告警和运行成功

        :param alarm_notify_type: The alarm_notify_type of this ShowConsistencyTaskDetailResponse.
        :type alarm_notify_type: str
        """
        self._alarm_notify_type = alarm_notify_type

    @property
    def alarm_notify_topic(self):
        r"""Gets the alarm_notify_topic of this ShowConsistencyTaskDetailResponse.

        通知主题名

        :return: The alarm_notify_topic of this ShowConsistencyTaskDetailResponse.
        :rtype: str
        """
        return self._alarm_notify_topic

    @alarm_notify_topic.setter
    def alarm_notify_topic(self, alarm_notify_topic):
        r"""Sets the alarm_notify_topic of this ShowConsistencyTaskDetailResponse.

        通知主题名

        :param alarm_notify_topic: The alarm_notify_topic of this ShowConsistencyTaskDetailResponse.
        :type alarm_notify_topic: str
        """
        self._alarm_notify_topic = alarm_notify_topic

    @property
    def schedule_type(self):
        r"""Gets the schedule_type of this ShowConsistencyTaskDetailResponse.

        调度类型，ONCE：单次调度，PERIODIC：周期性调度

        :return: The schedule_type of this ShowConsistencyTaskDetailResponse.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        r"""Sets the schedule_type of this ShowConsistencyTaskDetailResponse.

        调度类型，ONCE：单次调度，PERIODIC：周期性调度

        :param schedule_type: The schedule_type of this ShowConsistencyTaskDetailResponse.
        :type schedule_type: str
        """
        self._schedule_type = schedule_type

    @property
    def schedule_period(self):
        r"""Gets the schedule_period of this ShowConsistencyTaskDetailResponse.

        调度周期，MINUTE:按分钟调度，HOUR:按小时调度，DAY:按天调度，WEEK:按周调度

        :return: The schedule_period of this ShowConsistencyTaskDetailResponse.
        :rtype: str
        """
        return self._schedule_period

    @schedule_period.setter
    def schedule_period(self, schedule_period):
        r"""Sets the schedule_period of this ShowConsistencyTaskDetailResponse.

        调度周期，MINUTE:按分钟调度，HOUR:按小时调度，DAY:按天调度，WEEK:按周调度

        :param schedule_period: The schedule_period of this ShowConsistencyTaskDetailResponse.
        :type schedule_period: str
        """
        self._schedule_period = schedule_period

    @property
    def schedule_interval(self):
        r"""Gets the schedule_interval of this ShowConsistencyTaskDetailResponse.

        调度间隔，注意：当调度周期为分钟、小时、天时，间隔时间为数字；而当调度周期为周时，调度间隔为星期的英文，如：每周一、周二调度时，schedule_interval为MONDAY,TUESDAY

        :return: The schedule_interval of this ShowConsistencyTaskDetailResponse.
        :rtype: str
        """
        return self._schedule_interval

    @schedule_interval.setter
    def schedule_interval(self, schedule_interval):
        r"""Sets the schedule_interval of this ShowConsistencyTaskDetailResponse.

        调度间隔，注意：当调度周期为分钟、小时、天时，间隔时间为数字；而当调度周期为周时，调度间隔为星期的英文，如：每周一、周二调度时，schedule_interval为MONDAY,TUESDAY

        :param schedule_interval: The schedule_interval of this ShowConsistencyTaskDetailResponse.
        :type schedule_interval: str
        """
        self._schedule_interval = schedule_interval

    @property
    def schedule_start_time(self):
        r"""Gets the schedule_start_time of this ShowConsistencyTaskDetailResponse.

        调度开始时间

        :return: The schedule_start_time of this ShowConsistencyTaskDetailResponse.
        :rtype: str
        """
        return self._schedule_start_time

    @schedule_start_time.setter
    def schedule_start_time(self, schedule_start_time):
        r"""Sets the schedule_start_time of this ShowConsistencyTaskDetailResponse.

        调度开始时间

        :param schedule_start_time: The schedule_start_time of this ShowConsistencyTaskDetailResponse.
        :type schedule_start_time: str
        """
        self._schedule_start_time = schedule_start_time

    @property
    def schedule_end_time(self):
        r"""Gets the schedule_end_time of this ShowConsistencyTaskDetailResponse.

        调度结束时间

        :return: The schedule_end_time of this ShowConsistencyTaskDetailResponse.
        :rtype: str
        """
        return self._schedule_end_time

    @schedule_end_time.setter
    def schedule_end_time(self, schedule_end_time):
        r"""Sets the schedule_end_time of this ShowConsistencyTaskDetailResponse.

        调度结束时间

        :param schedule_end_time: The schedule_end_time of this ShowConsistencyTaskDetailResponse.
        :type schedule_end_time: str
        """
        self._schedule_end_time = schedule_end_time

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowConsistencyTaskDetailResponse.

        最近运行时间,13位时间戳(精确到毫秒)

        :return: The create_time of this ShowConsistencyTaskDetailResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowConsistencyTaskDetailResponse.

        最近运行时间,13位时间戳(精确到毫秒)

        :param create_time: The create_time of this ShowConsistencyTaskDetailResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def last_run_time(self):
        r"""Gets the last_run_time of this ShowConsistencyTaskDetailResponse.

        最近运行时间,13位时间戳(精确到毫秒)

        :return: The last_run_time of this ShowConsistencyTaskDetailResponse.
        :rtype: int
        """
        return self._last_run_time

    @last_run_time.setter
    def last_run_time(self, last_run_time):
        r"""Sets the last_run_time of this ShowConsistencyTaskDetailResponse.

        最近运行时间,13位时间戳(精确到毫秒)

        :param last_run_time: The last_run_time of this ShowConsistencyTaskDetailResponse.
        :type last_run_time: int
        """
        self._last_run_time = last_run_time

    @property
    def sub_rules(self):
        r"""Gets the sub_rules of this ShowConsistencyTaskDetailResponse.

        子规则

        :return: The sub_rules of this ShowConsistencyTaskDetailResponse.
        :rtype: list[list[ConsistencyRuleDetailForOpenApi]]
        """
        return self._sub_rules

    @sub_rules.setter
    def sub_rules(self, sub_rules):
        r"""Sets the sub_rules of this ShowConsistencyTaskDetailResponse.

        子规则

        :param sub_rules: The sub_rules of this ShowConsistencyTaskDetailResponse.
        :type sub_rules: list[list[ConsistencyRuleDetailForOpenApi]]
        """
        self._sub_rules = sub_rules

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
        if not isinstance(other, ShowConsistencyTaskDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
