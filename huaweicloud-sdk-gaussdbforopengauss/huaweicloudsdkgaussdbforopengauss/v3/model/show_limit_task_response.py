# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLimitTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_name': 'str',
        'limit_type': 'str',
        'parallel_size': 'int',
        'start_time': 'str',
        'end_time': 'str',
        'task_running_time': 'int',
        'limit_count': 'int',
        'rule_name': 'str',
        'memory_utilization': 'int',
        'cpu_utilization': 'int',
        'limit_task_rule_info_list': 'list[LimitTaskRuleInfoOption]'
    }

    attribute_map = {
        'task_name': 'task_name',
        'limit_type': 'limit_type',
        'parallel_size': 'parallel_size',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'task_running_time': 'task_running_time',
        'limit_count': 'limit_count',
        'rule_name': 'rule_name',
        'memory_utilization': 'memory_utilization',
        'cpu_utilization': 'cpu_utilization',
        'limit_task_rule_info_list': 'limit_task_rule_info_list'
    }

    def __init__(self, task_name=None, limit_type=None, parallel_size=None, start_time=None, end_time=None, task_running_time=None, limit_count=None, rule_name=None, memory_utilization=None, cpu_utilization=None, limit_task_rule_info_list=None):
        r"""ShowLimitTaskResponse

        The model defined in huaweicloud sdk

        :param task_name: 限流任务名传。
        :type task_name: str
        :param limit_type: 任务限流类型。
        :type limit_type: str
        :param parallel_size: 并发数。
        :type parallel_size: int
        :param start_time: 限流任务开始时间,格式为yyyy-mm-ddThh:mm:ssZ，当前时间指UTC时间。
        :type start_time: str
        :param end_time: 限流任务结束时间,格式为yyyy-mm-ddThh:mm:ssZ，当前时间指UTC时间。
        :type end_time: str
        :param task_running_time: 限流任务已执行时间，单位秒。
        :type task_running_time: int
        :param limit_count: 限流任务拦截次数。
        :type limit_count: int
        :param rule_name: 规则名。
        :type rule_name: str
        :param memory_utilization: 内存利用率，仅当任务类型为SESSION_ACTIVE_MAX_COUNT时，返回该值且与请求参数相同。
        :type memory_utilization: int
        :param cpu_utilization: cpu利用率，仅当任务类型为SESSION_ACTIVE_MAX_COUNT时，返回该值且与请求参数相同。
        :type cpu_utilization: int
        :param limit_task_rule_info_list: 限流任务列表
        :type limit_task_rule_info_list: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.LimitTaskRuleInfoOption`]
        """
        
        super(ShowLimitTaskResponse, self).__init__()

        self._task_name = None
        self._limit_type = None
        self._parallel_size = None
        self._start_time = None
        self._end_time = None
        self._task_running_time = None
        self._limit_count = None
        self._rule_name = None
        self._memory_utilization = None
        self._cpu_utilization = None
        self._limit_task_rule_info_list = None
        self.discriminator = None

        if task_name is not None:
            self.task_name = task_name
        if limit_type is not None:
            self.limit_type = limit_type
        if parallel_size is not None:
            self.parallel_size = parallel_size
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if task_running_time is not None:
            self.task_running_time = task_running_time
        if limit_count is not None:
            self.limit_count = limit_count
        if rule_name is not None:
            self.rule_name = rule_name
        if memory_utilization is not None:
            self.memory_utilization = memory_utilization
        if cpu_utilization is not None:
            self.cpu_utilization = cpu_utilization
        if limit_task_rule_info_list is not None:
            self.limit_task_rule_info_list = limit_task_rule_info_list

    @property
    def task_name(self):
        r"""Gets the task_name of this ShowLimitTaskResponse.

        限流任务名传。

        :return: The task_name of this ShowLimitTaskResponse.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this ShowLimitTaskResponse.

        限流任务名传。

        :param task_name: The task_name of this ShowLimitTaskResponse.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def limit_type(self):
        r"""Gets the limit_type of this ShowLimitTaskResponse.

        任务限流类型。

        :return: The limit_type of this ShowLimitTaskResponse.
        :rtype: str
        """
        return self._limit_type

    @limit_type.setter
    def limit_type(self, limit_type):
        r"""Sets the limit_type of this ShowLimitTaskResponse.

        任务限流类型。

        :param limit_type: The limit_type of this ShowLimitTaskResponse.
        :type limit_type: str
        """
        self._limit_type = limit_type

    @property
    def parallel_size(self):
        r"""Gets the parallel_size of this ShowLimitTaskResponse.

        并发数。

        :return: The parallel_size of this ShowLimitTaskResponse.
        :rtype: int
        """
        return self._parallel_size

    @parallel_size.setter
    def parallel_size(self, parallel_size):
        r"""Sets the parallel_size of this ShowLimitTaskResponse.

        并发数。

        :param parallel_size: The parallel_size of this ShowLimitTaskResponse.
        :type parallel_size: int
        """
        self._parallel_size = parallel_size

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowLimitTaskResponse.

        限流任务开始时间,格式为yyyy-mm-ddThh:mm:ssZ，当前时间指UTC时间。

        :return: The start_time of this ShowLimitTaskResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowLimitTaskResponse.

        限流任务开始时间,格式为yyyy-mm-ddThh:mm:ssZ，当前时间指UTC时间。

        :param start_time: The start_time of this ShowLimitTaskResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowLimitTaskResponse.

        限流任务结束时间,格式为yyyy-mm-ddThh:mm:ssZ，当前时间指UTC时间。

        :return: The end_time of this ShowLimitTaskResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowLimitTaskResponse.

        限流任务结束时间,格式为yyyy-mm-ddThh:mm:ssZ，当前时间指UTC时间。

        :param end_time: The end_time of this ShowLimitTaskResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def task_running_time(self):
        r"""Gets the task_running_time of this ShowLimitTaskResponse.

        限流任务已执行时间，单位秒。

        :return: The task_running_time of this ShowLimitTaskResponse.
        :rtype: int
        """
        return self._task_running_time

    @task_running_time.setter
    def task_running_time(self, task_running_time):
        r"""Sets the task_running_time of this ShowLimitTaskResponse.

        限流任务已执行时间，单位秒。

        :param task_running_time: The task_running_time of this ShowLimitTaskResponse.
        :type task_running_time: int
        """
        self._task_running_time = task_running_time

    @property
    def limit_count(self):
        r"""Gets the limit_count of this ShowLimitTaskResponse.

        限流任务拦截次数。

        :return: The limit_count of this ShowLimitTaskResponse.
        :rtype: int
        """
        return self._limit_count

    @limit_count.setter
    def limit_count(self, limit_count):
        r"""Sets the limit_count of this ShowLimitTaskResponse.

        限流任务拦截次数。

        :param limit_count: The limit_count of this ShowLimitTaskResponse.
        :type limit_count: int
        """
        self._limit_count = limit_count

    @property
    def rule_name(self):
        r"""Gets the rule_name of this ShowLimitTaskResponse.

        规则名。

        :return: The rule_name of this ShowLimitTaskResponse.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this ShowLimitTaskResponse.

        规则名。

        :param rule_name: The rule_name of this ShowLimitTaskResponse.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def memory_utilization(self):
        r"""Gets the memory_utilization of this ShowLimitTaskResponse.

        内存利用率，仅当任务类型为SESSION_ACTIVE_MAX_COUNT时，返回该值且与请求参数相同。

        :return: The memory_utilization of this ShowLimitTaskResponse.
        :rtype: int
        """
        return self._memory_utilization

    @memory_utilization.setter
    def memory_utilization(self, memory_utilization):
        r"""Sets the memory_utilization of this ShowLimitTaskResponse.

        内存利用率，仅当任务类型为SESSION_ACTIVE_MAX_COUNT时，返回该值且与请求参数相同。

        :param memory_utilization: The memory_utilization of this ShowLimitTaskResponse.
        :type memory_utilization: int
        """
        self._memory_utilization = memory_utilization

    @property
    def cpu_utilization(self):
        r"""Gets the cpu_utilization of this ShowLimitTaskResponse.

        cpu利用率，仅当任务类型为SESSION_ACTIVE_MAX_COUNT时，返回该值且与请求参数相同。

        :return: The cpu_utilization of this ShowLimitTaskResponse.
        :rtype: int
        """
        return self._cpu_utilization

    @cpu_utilization.setter
    def cpu_utilization(self, cpu_utilization):
        r"""Sets the cpu_utilization of this ShowLimitTaskResponse.

        cpu利用率，仅当任务类型为SESSION_ACTIVE_MAX_COUNT时，返回该值且与请求参数相同。

        :param cpu_utilization: The cpu_utilization of this ShowLimitTaskResponse.
        :type cpu_utilization: int
        """
        self._cpu_utilization = cpu_utilization

    @property
    def limit_task_rule_info_list(self):
        r"""Gets the limit_task_rule_info_list of this ShowLimitTaskResponse.

        限流任务列表

        :return: The limit_task_rule_info_list of this ShowLimitTaskResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.LimitTaskRuleInfoOption`]
        """
        return self._limit_task_rule_info_list

    @limit_task_rule_info_list.setter
    def limit_task_rule_info_list(self, limit_task_rule_info_list):
        r"""Sets the limit_task_rule_info_list of this ShowLimitTaskResponse.

        限流任务列表

        :param limit_task_rule_info_list: The limit_task_rule_info_list of this ShowLimitTaskResponse.
        :type limit_task_rule_info_list: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.LimitTaskRuleInfoOption`]
        """
        self._limit_task_rule_info_list = limit_task_rule_info_list

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
        if not isinstance(other, ShowLimitTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
