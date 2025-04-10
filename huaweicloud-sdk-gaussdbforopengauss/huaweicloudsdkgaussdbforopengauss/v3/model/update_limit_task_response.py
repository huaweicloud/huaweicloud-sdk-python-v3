# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLimitTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'databases': 'str',
        'task_name': 'str',
        'key_words': 'str',
        'parallel_size': 'int',
        'start_time': 'str',
        'end_time': 'str',
        'cpu_utilization': 'int',
        'memory_utilization': 'int',
        'rule_name': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'databases': 'databases',
        'task_name': 'task_name',
        'key_words': 'key_words',
        'parallel_size': 'parallel_size',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'cpu_utilization': 'cpu_utilization',
        'memory_utilization': 'memory_utilization',
        'rule_name': 'rule_name',
        'job_id': 'job_id'
    }

    def __init__(self, task_id=None, databases=None, task_name=None, key_words=None, parallel_size=None, start_time=None, end_time=None, cpu_utilization=None, memory_utilization=None, rule_name=None, job_id=None):
        r"""UpdateLimitTaskResponse

        The model defined in huaweicloud sdk

        :param task_id: 限流任务ID。
        :type task_id: str
        :param databases: CN节点数据库组,每个数据库字符串以逗号形式隔开，仅当任务类型为SQL_TYPE时，返回该值且与请求参数相同。
        :type databases: str
        :param task_name: 限流任务名，与请求参数相同。
        :type task_name: str
        :param key_words: 关键词，仅当任务类型为SQL_TYPE时，返回该值且与请求参数相同。
        :type key_words: str
        :param parallel_size: 并发数，与请求参数相同。
        :type parallel_size: int
        :param start_time: 限流任务开始时间，格式为yyyy-mm-ddThh:mm:ssZ，当前时间指UTC时间，SQL范围返回该值。
        :type start_time: str
        :param end_time: 限流任务结束时间，格式为yyyy-mm-ddThh:mm:ssZ，当前时间指UTC时间，SQL范围返回该值。
        :type end_time: str
        :param cpu_utilization: cpu利用率，仅当任务类型为SESSION_ACTIVE_MAX_COUNT时，返回该值且只保留正整数。
        :type cpu_utilization: int
        :param memory_utilization: 内存利用率，仅当任务类型为SESSION_ACTIVE_MAX_COUNT时，返回该值且只保留正整数。
        :type memory_utilization: int
        :param rule_name: 规则名。
        :type rule_name: str
        :param job_id: 工作流ID。
        :type job_id: str
        """
        
        super(UpdateLimitTaskResponse, self).__init__()

        self._task_id = None
        self._databases = None
        self._task_name = None
        self._key_words = None
        self._parallel_size = None
        self._start_time = None
        self._end_time = None
        self._cpu_utilization = None
        self._memory_utilization = None
        self._rule_name = None
        self._job_id = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if databases is not None:
            self.databases = databases
        if task_name is not None:
            self.task_name = task_name
        if key_words is not None:
            self.key_words = key_words
        if parallel_size is not None:
            self.parallel_size = parallel_size
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if cpu_utilization is not None:
            self.cpu_utilization = cpu_utilization
        if memory_utilization is not None:
            self.memory_utilization = memory_utilization
        if rule_name is not None:
            self.rule_name = rule_name
        if job_id is not None:
            self.job_id = job_id

    @property
    def task_id(self):
        r"""Gets the task_id of this UpdateLimitTaskResponse.

        限流任务ID。

        :return: The task_id of this UpdateLimitTaskResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this UpdateLimitTaskResponse.

        限流任务ID。

        :param task_id: The task_id of this UpdateLimitTaskResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def databases(self):
        r"""Gets the databases of this UpdateLimitTaskResponse.

        CN节点数据库组,每个数据库字符串以逗号形式隔开，仅当任务类型为SQL_TYPE时，返回该值且与请求参数相同。

        :return: The databases of this UpdateLimitTaskResponse.
        :rtype: str
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        r"""Sets the databases of this UpdateLimitTaskResponse.

        CN节点数据库组,每个数据库字符串以逗号形式隔开，仅当任务类型为SQL_TYPE时，返回该值且与请求参数相同。

        :param databases: The databases of this UpdateLimitTaskResponse.
        :type databases: str
        """
        self._databases = databases

    @property
    def task_name(self):
        r"""Gets the task_name of this UpdateLimitTaskResponse.

        限流任务名，与请求参数相同。

        :return: The task_name of this UpdateLimitTaskResponse.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this UpdateLimitTaskResponse.

        限流任务名，与请求参数相同。

        :param task_name: The task_name of this UpdateLimitTaskResponse.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def key_words(self):
        r"""Gets the key_words of this UpdateLimitTaskResponse.

        关键词，仅当任务类型为SQL_TYPE时，返回该值且与请求参数相同。

        :return: The key_words of this UpdateLimitTaskResponse.
        :rtype: str
        """
        return self._key_words

    @key_words.setter
    def key_words(self, key_words):
        r"""Sets the key_words of this UpdateLimitTaskResponse.

        关键词，仅当任务类型为SQL_TYPE时，返回该值且与请求参数相同。

        :param key_words: The key_words of this UpdateLimitTaskResponse.
        :type key_words: str
        """
        self._key_words = key_words

    @property
    def parallel_size(self):
        r"""Gets the parallel_size of this UpdateLimitTaskResponse.

        并发数，与请求参数相同。

        :return: The parallel_size of this UpdateLimitTaskResponse.
        :rtype: int
        """
        return self._parallel_size

    @parallel_size.setter
    def parallel_size(self, parallel_size):
        r"""Sets the parallel_size of this UpdateLimitTaskResponse.

        并发数，与请求参数相同。

        :param parallel_size: The parallel_size of this UpdateLimitTaskResponse.
        :type parallel_size: int
        """
        self._parallel_size = parallel_size

    @property
    def start_time(self):
        r"""Gets the start_time of this UpdateLimitTaskResponse.

        限流任务开始时间，格式为yyyy-mm-ddThh:mm:ssZ，当前时间指UTC时间，SQL范围返回该值。

        :return: The start_time of this UpdateLimitTaskResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this UpdateLimitTaskResponse.

        限流任务开始时间，格式为yyyy-mm-ddThh:mm:ssZ，当前时间指UTC时间，SQL范围返回该值。

        :param start_time: The start_time of this UpdateLimitTaskResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this UpdateLimitTaskResponse.

        限流任务结束时间，格式为yyyy-mm-ddThh:mm:ssZ，当前时间指UTC时间，SQL范围返回该值。

        :return: The end_time of this UpdateLimitTaskResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this UpdateLimitTaskResponse.

        限流任务结束时间，格式为yyyy-mm-ddThh:mm:ssZ，当前时间指UTC时间，SQL范围返回该值。

        :param end_time: The end_time of this UpdateLimitTaskResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def cpu_utilization(self):
        r"""Gets the cpu_utilization of this UpdateLimitTaskResponse.

        cpu利用率，仅当任务类型为SESSION_ACTIVE_MAX_COUNT时，返回该值且只保留正整数。

        :return: The cpu_utilization of this UpdateLimitTaskResponse.
        :rtype: int
        """
        return self._cpu_utilization

    @cpu_utilization.setter
    def cpu_utilization(self, cpu_utilization):
        r"""Sets the cpu_utilization of this UpdateLimitTaskResponse.

        cpu利用率，仅当任务类型为SESSION_ACTIVE_MAX_COUNT时，返回该值且只保留正整数。

        :param cpu_utilization: The cpu_utilization of this UpdateLimitTaskResponse.
        :type cpu_utilization: int
        """
        self._cpu_utilization = cpu_utilization

    @property
    def memory_utilization(self):
        r"""Gets the memory_utilization of this UpdateLimitTaskResponse.

        内存利用率，仅当任务类型为SESSION_ACTIVE_MAX_COUNT时，返回该值且只保留正整数。

        :return: The memory_utilization of this UpdateLimitTaskResponse.
        :rtype: int
        """
        return self._memory_utilization

    @memory_utilization.setter
    def memory_utilization(self, memory_utilization):
        r"""Sets the memory_utilization of this UpdateLimitTaskResponse.

        内存利用率，仅当任务类型为SESSION_ACTIVE_MAX_COUNT时，返回该值且只保留正整数。

        :param memory_utilization: The memory_utilization of this UpdateLimitTaskResponse.
        :type memory_utilization: int
        """
        self._memory_utilization = memory_utilization

    @property
    def rule_name(self):
        r"""Gets the rule_name of this UpdateLimitTaskResponse.

        规则名。

        :return: The rule_name of this UpdateLimitTaskResponse.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this UpdateLimitTaskResponse.

        规则名。

        :param rule_name: The rule_name of this UpdateLimitTaskResponse.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def job_id(self):
        r"""Gets the job_id of this UpdateLimitTaskResponse.

        工作流ID。

        :return: The job_id of this UpdateLimitTaskResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this UpdateLimitTaskResponse.

        工作流ID。

        :param job_id: The job_id of this UpdateLimitTaskResponse.
        :type job_id: str
        """
        self._job_id = job_id

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
        if not isinstance(other, UpdateLimitTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
