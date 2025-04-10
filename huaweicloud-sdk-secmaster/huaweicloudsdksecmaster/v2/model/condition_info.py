# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConditionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'expression_type': 'str',
        'conditions': 'list[ConditionItem]',
        'logics': 'list[str]',
        'cron': 'str',
        'schedule_type': 'str',
        'start_type': 'str',
        'end_type': 'str',
        'end_time': 'str',
        'repeat_range': 'str',
        'only_once': 'bool',
        'execution_type': 'str'
    }

    attribute_map = {
        'expression_type': 'expression_type',
        'conditions': 'conditions',
        'logics': 'logics',
        'cron': 'cron',
        'schedule_type': 'schedule_type',
        'start_type': 'start_type',
        'end_type': 'end_type',
        'end_time': 'end_time',
        'repeat_range': 'repeat_range',
        'only_once': 'only_once',
        'execution_type': 'execution_type'
    }

    def __init__(self, expression_type=None, conditions=None, logics=None, cron=None, schedule_type=None, start_type=None, end_type=None, end_time=None, repeat_range=None, only_once=None, execution_type=None):
        r"""ConditionInfo

        The model defined in huaweicloud sdk

        :param expression_type: 表达式类型。默认为common,事件触发剧本必填
        :type expression_type: str
        :param conditions: 触发条件。事件触发剧本必填
        :type conditions: list[:class:`huaweicloudsdksecmaster.v2.ConditionItem`]
        :param logics: 条件逻辑组合。事件触发剧本必填
        :type logics: list[str]
        :param cron: Cron 表达式（定时任务）。定时触发剧本必填
        :type cron: str
        :param schedule_type: 定时重复类型(second--秒, hour--小时,day--天，week-周)。定时触发剧本必填
        :type schedule_type: str
        :param start_type: 剧本开始执行类型，IMMEDIATELY--创建完成立即执行, CUSTOM--自定义执行时间。定时触发剧本必填
        :type start_type: str
        :param end_type: 剧本结束执行类型，FOREVER--一直执行, CUSTOM--自定义结束时间。定时触发剧本必填
        :type end_type: str
        :param end_time: 定时结束时间。定时触发剧本必填
        :type end_time: str
        :param repeat_range: 执行时间段 2021-01-30T23:00:00Z+0800。定时触发剧本必填
        :type repeat_range: str
        :param only_once: 是否只执行一次。定时触发剧本必填
        :type only_once: bool
        :param execution_type: 执行队列类型（PARALLEL-新任务与之前任务并行）。定时触发剧本必填
        :type execution_type: str
        """
        
        

        self._expression_type = None
        self._conditions = None
        self._logics = None
        self._cron = None
        self._schedule_type = None
        self._start_type = None
        self._end_type = None
        self._end_time = None
        self._repeat_range = None
        self._only_once = None
        self._execution_type = None
        self.discriminator = None

        if expression_type is not None:
            self.expression_type = expression_type
        if conditions is not None:
            self.conditions = conditions
        if logics is not None:
            self.logics = logics
        if cron is not None:
            self.cron = cron
        if schedule_type is not None:
            self.schedule_type = schedule_type
        if start_type is not None:
            self.start_type = start_type
        if end_type is not None:
            self.end_type = end_type
        if end_time is not None:
            self.end_time = end_time
        if repeat_range is not None:
            self.repeat_range = repeat_range
        if only_once is not None:
            self.only_once = only_once
        if execution_type is not None:
            self.execution_type = execution_type

    @property
    def expression_type(self):
        r"""Gets the expression_type of this ConditionInfo.

        表达式类型。默认为common,事件触发剧本必填

        :return: The expression_type of this ConditionInfo.
        :rtype: str
        """
        return self._expression_type

    @expression_type.setter
    def expression_type(self, expression_type):
        r"""Sets the expression_type of this ConditionInfo.

        表达式类型。默认为common,事件触发剧本必填

        :param expression_type: The expression_type of this ConditionInfo.
        :type expression_type: str
        """
        self._expression_type = expression_type

    @property
    def conditions(self):
        r"""Gets the conditions of this ConditionInfo.

        触发条件。事件触发剧本必填

        :return: The conditions of this ConditionInfo.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.ConditionItem`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this ConditionInfo.

        触发条件。事件触发剧本必填

        :param conditions: The conditions of this ConditionInfo.
        :type conditions: list[:class:`huaweicloudsdksecmaster.v2.ConditionItem`]
        """
        self._conditions = conditions

    @property
    def logics(self):
        r"""Gets the logics of this ConditionInfo.

        条件逻辑组合。事件触发剧本必填

        :return: The logics of this ConditionInfo.
        :rtype: list[str]
        """
        return self._logics

    @logics.setter
    def logics(self, logics):
        r"""Sets the logics of this ConditionInfo.

        条件逻辑组合。事件触发剧本必填

        :param logics: The logics of this ConditionInfo.
        :type logics: list[str]
        """
        self._logics = logics

    @property
    def cron(self):
        r"""Gets the cron of this ConditionInfo.

        Cron 表达式（定时任务）。定时触发剧本必填

        :return: The cron of this ConditionInfo.
        :rtype: str
        """
        return self._cron

    @cron.setter
    def cron(self, cron):
        r"""Sets the cron of this ConditionInfo.

        Cron 表达式（定时任务）。定时触发剧本必填

        :param cron: The cron of this ConditionInfo.
        :type cron: str
        """
        self._cron = cron

    @property
    def schedule_type(self):
        r"""Gets the schedule_type of this ConditionInfo.

        定时重复类型(second--秒, hour--小时,day--天，week-周)。定时触发剧本必填

        :return: The schedule_type of this ConditionInfo.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        r"""Sets the schedule_type of this ConditionInfo.

        定时重复类型(second--秒, hour--小时,day--天，week-周)。定时触发剧本必填

        :param schedule_type: The schedule_type of this ConditionInfo.
        :type schedule_type: str
        """
        self._schedule_type = schedule_type

    @property
    def start_type(self):
        r"""Gets the start_type of this ConditionInfo.

        剧本开始执行类型，IMMEDIATELY--创建完成立即执行, CUSTOM--自定义执行时间。定时触发剧本必填

        :return: The start_type of this ConditionInfo.
        :rtype: str
        """
        return self._start_type

    @start_type.setter
    def start_type(self, start_type):
        r"""Sets the start_type of this ConditionInfo.

        剧本开始执行类型，IMMEDIATELY--创建完成立即执行, CUSTOM--自定义执行时间。定时触发剧本必填

        :param start_type: The start_type of this ConditionInfo.
        :type start_type: str
        """
        self._start_type = start_type

    @property
    def end_type(self):
        r"""Gets the end_type of this ConditionInfo.

        剧本结束执行类型，FOREVER--一直执行, CUSTOM--自定义结束时间。定时触发剧本必填

        :return: The end_type of this ConditionInfo.
        :rtype: str
        """
        return self._end_type

    @end_type.setter
    def end_type(self, end_type):
        r"""Sets the end_type of this ConditionInfo.

        剧本结束执行类型，FOREVER--一直执行, CUSTOM--自定义结束时间。定时触发剧本必填

        :param end_type: The end_type of this ConditionInfo.
        :type end_type: str
        """
        self._end_type = end_type

    @property
    def end_time(self):
        r"""Gets the end_time of this ConditionInfo.

        定时结束时间。定时触发剧本必填

        :return: The end_time of this ConditionInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ConditionInfo.

        定时结束时间。定时触发剧本必填

        :param end_time: The end_time of this ConditionInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def repeat_range(self):
        r"""Gets the repeat_range of this ConditionInfo.

        执行时间段 2021-01-30T23:00:00Z+0800。定时触发剧本必填

        :return: The repeat_range of this ConditionInfo.
        :rtype: str
        """
        return self._repeat_range

    @repeat_range.setter
    def repeat_range(self, repeat_range):
        r"""Sets the repeat_range of this ConditionInfo.

        执行时间段 2021-01-30T23:00:00Z+0800。定时触发剧本必填

        :param repeat_range: The repeat_range of this ConditionInfo.
        :type repeat_range: str
        """
        self._repeat_range = repeat_range

    @property
    def only_once(self):
        r"""Gets the only_once of this ConditionInfo.

        是否只执行一次。定时触发剧本必填

        :return: The only_once of this ConditionInfo.
        :rtype: bool
        """
        return self._only_once

    @only_once.setter
    def only_once(self, only_once):
        r"""Sets the only_once of this ConditionInfo.

        是否只执行一次。定时触发剧本必填

        :param only_once: The only_once of this ConditionInfo.
        :type only_once: bool
        """
        self._only_once = only_once

    @property
    def execution_type(self):
        r"""Gets the execution_type of this ConditionInfo.

        执行队列类型（PARALLEL-新任务与之前任务并行）。定时触发剧本必填

        :return: The execution_type of this ConditionInfo.
        :rtype: str
        """
        return self._execution_type

    @execution_type.setter
    def execution_type(self, execution_type):
        r"""Sets the execution_type of this ConditionInfo.

        执行队列类型（PARALLEL-新任务与之前任务并行）。定时触发剧本必填

        :param execution_type: The execution_type of this ConditionInfo.
        :type execution_type: str
        """
        self._execution_type = execution_type

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
        if not isinstance(other, ConditionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
