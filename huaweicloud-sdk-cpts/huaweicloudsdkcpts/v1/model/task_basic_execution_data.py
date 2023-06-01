# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskBasicExecutionData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'complete_num': 'int',
        'duration': 'int',
        'end_time': 'str',
        'executed_num': 'int',
        'kpi_case_count': 'int',
        'kpi_case_execute_count': 'int',
        'kpi_case_pass_count': 'int',
        'parallel': 'bool',
        'pass_num': 'int',
        'start_time': 'str',
        'task_status': 'int',
        'total_num': 'int',
        'vum': 'int'
    }

    attribute_map = {
        'complete_num': 'complete_num',
        'duration': 'duration',
        'end_time': 'end_time',
        'executed_num': 'executed_num',
        'kpi_case_count': 'kpi_case_count',
        'kpi_case_execute_count': 'kpi_case_execute_count',
        'kpi_case_pass_count': 'kpi_case_pass_count',
        'parallel': 'parallel',
        'pass_num': 'pass_num',
        'start_time': 'start_time',
        'task_status': 'task_status',
        'total_num': 'total_num',
        'vum': 'vum'
    }

    def __init__(self, complete_num=None, duration=None, end_time=None, executed_num=None, kpi_case_count=None, kpi_case_execute_count=None, kpi_case_pass_count=None, parallel=None, pass_num=None, start_time=None, task_status=None, total_num=None, vum=None):
        """TaskBasicExecutionData

        The model defined in huaweicloud sdk

        :param complete_num: 已执行完成的用例数
        :type complete_num: int
        :param duration: 持续时间
        :type duration: int
        :param end_time: 结束时间
        :type end_time: str
        :param executed_num: 已执行用例数
        :type executed_num: int
        :param kpi_case_count: 【指标数据:最后一个轮次】 用例数
        :type kpi_case_count: int
        :param kpi_case_execute_count: 【指标数据:最后一个轮次】 已执行的用例数
        :type kpi_case_execute_count: int
        :param kpi_case_pass_count: 【指标数据:最后一个轮次】 最后一轮结果为Pass的用例数
        :type kpi_case_pass_count: int
        :param parallel: 任务间用例是否并行执行
        :type parallel: bool
        :param pass_num: 用例通过数
        :type pass_num: int
        :param start_time: 开始时间
        :type start_time: str
        :param task_status: 任务状态
        :type task_status: int
        :param total_num: 总用例数
        :type total_num: int
        :param vum: 分钟*并发数
        :type vum: int
        """
        
        

        self._complete_num = None
        self._duration = None
        self._end_time = None
        self._executed_num = None
        self._kpi_case_count = None
        self._kpi_case_execute_count = None
        self._kpi_case_pass_count = None
        self._parallel = None
        self._pass_num = None
        self._start_time = None
        self._task_status = None
        self._total_num = None
        self._vum = None
        self.discriminator = None

        if complete_num is not None:
            self.complete_num = complete_num
        if duration is not None:
            self.duration = duration
        if end_time is not None:
            self.end_time = end_time
        if executed_num is not None:
            self.executed_num = executed_num
        if kpi_case_count is not None:
            self.kpi_case_count = kpi_case_count
        if kpi_case_execute_count is not None:
            self.kpi_case_execute_count = kpi_case_execute_count
        if kpi_case_pass_count is not None:
            self.kpi_case_pass_count = kpi_case_pass_count
        if parallel is not None:
            self.parallel = parallel
        if pass_num is not None:
            self.pass_num = pass_num
        if start_time is not None:
            self.start_time = start_time
        if task_status is not None:
            self.task_status = task_status
        if total_num is not None:
            self.total_num = total_num
        if vum is not None:
            self.vum = vum

    @property
    def complete_num(self):
        """Gets the complete_num of this TaskBasicExecutionData.

        已执行完成的用例数

        :return: The complete_num of this TaskBasicExecutionData.
        :rtype: int
        """
        return self._complete_num

    @complete_num.setter
    def complete_num(self, complete_num):
        """Sets the complete_num of this TaskBasicExecutionData.

        已执行完成的用例数

        :param complete_num: The complete_num of this TaskBasicExecutionData.
        :type complete_num: int
        """
        self._complete_num = complete_num

    @property
    def duration(self):
        """Gets the duration of this TaskBasicExecutionData.

        持续时间

        :return: The duration of this TaskBasicExecutionData.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this TaskBasicExecutionData.

        持续时间

        :param duration: The duration of this TaskBasicExecutionData.
        :type duration: int
        """
        self._duration = duration

    @property
    def end_time(self):
        """Gets the end_time of this TaskBasicExecutionData.

        结束时间

        :return: The end_time of this TaskBasicExecutionData.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TaskBasicExecutionData.

        结束时间

        :param end_time: The end_time of this TaskBasicExecutionData.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def executed_num(self):
        """Gets the executed_num of this TaskBasicExecutionData.

        已执行用例数

        :return: The executed_num of this TaskBasicExecutionData.
        :rtype: int
        """
        return self._executed_num

    @executed_num.setter
    def executed_num(self, executed_num):
        """Sets the executed_num of this TaskBasicExecutionData.

        已执行用例数

        :param executed_num: The executed_num of this TaskBasicExecutionData.
        :type executed_num: int
        """
        self._executed_num = executed_num

    @property
    def kpi_case_count(self):
        """Gets the kpi_case_count of this TaskBasicExecutionData.

        【指标数据:最后一个轮次】 用例数

        :return: The kpi_case_count of this TaskBasicExecutionData.
        :rtype: int
        """
        return self._kpi_case_count

    @kpi_case_count.setter
    def kpi_case_count(self, kpi_case_count):
        """Sets the kpi_case_count of this TaskBasicExecutionData.

        【指标数据:最后一个轮次】 用例数

        :param kpi_case_count: The kpi_case_count of this TaskBasicExecutionData.
        :type kpi_case_count: int
        """
        self._kpi_case_count = kpi_case_count

    @property
    def kpi_case_execute_count(self):
        """Gets the kpi_case_execute_count of this TaskBasicExecutionData.

        【指标数据:最后一个轮次】 已执行的用例数

        :return: The kpi_case_execute_count of this TaskBasicExecutionData.
        :rtype: int
        """
        return self._kpi_case_execute_count

    @kpi_case_execute_count.setter
    def kpi_case_execute_count(self, kpi_case_execute_count):
        """Sets the kpi_case_execute_count of this TaskBasicExecutionData.

        【指标数据:最后一个轮次】 已执行的用例数

        :param kpi_case_execute_count: The kpi_case_execute_count of this TaskBasicExecutionData.
        :type kpi_case_execute_count: int
        """
        self._kpi_case_execute_count = kpi_case_execute_count

    @property
    def kpi_case_pass_count(self):
        """Gets the kpi_case_pass_count of this TaskBasicExecutionData.

        【指标数据:最后一个轮次】 最后一轮结果为Pass的用例数

        :return: The kpi_case_pass_count of this TaskBasicExecutionData.
        :rtype: int
        """
        return self._kpi_case_pass_count

    @kpi_case_pass_count.setter
    def kpi_case_pass_count(self, kpi_case_pass_count):
        """Sets the kpi_case_pass_count of this TaskBasicExecutionData.

        【指标数据:最后一个轮次】 最后一轮结果为Pass的用例数

        :param kpi_case_pass_count: The kpi_case_pass_count of this TaskBasicExecutionData.
        :type kpi_case_pass_count: int
        """
        self._kpi_case_pass_count = kpi_case_pass_count

    @property
    def parallel(self):
        """Gets the parallel of this TaskBasicExecutionData.

        任务间用例是否并行执行

        :return: The parallel of this TaskBasicExecutionData.
        :rtype: bool
        """
        return self._parallel

    @parallel.setter
    def parallel(self, parallel):
        """Sets the parallel of this TaskBasicExecutionData.

        任务间用例是否并行执行

        :param parallel: The parallel of this TaskBasicExecutionData.
        :type parallel: bool
        """
        self._parallel = parallel

    @property
    def pass_num(self):
        """Gets the pass_num of this TaskBasicExecutionData.

        用例通过数

        :return: The pass_num of this TaskBasicExecutionData.
        :rtype: int
        """
        return self._pass_num

    @pass_num.setter
    def pass_num(self, pass_num):
        """Sets the pass_num of this TaskBasicExecutionData.

        用例通过数

        :param pass_num: The pass_num of this TaskBasicExecutionData.
        :type pass_num: int
        """
        self._pass_num = pass_num

    @property
    def start_time(self):
        """Gets the start_time of this TaskBasicExecutionData.

        开始时间

        :return: The start_time of this TaskBasicExecutionData.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TaskBasicExecutionData.

        开始时间

        :param start_time: The start_time of this TaskBasicExecutionData.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def task_status(self):
        """Gets the task_status of this TaskBasicExecutionData.

        任务状态

        :return: The task_status of this TaskBasicExecutionData.
        :rtype: int
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this TaskBasicExecutionData.

        任务状态

        :param task_status: The task_status of this TaskBasicExecutionData.
        :type task_status: int
        """
        self._task_status = task_status

    @property
    def total_num(self):
        """Gets the total_num of this TaskBasicExecutionData.

        总用例数

        :return: The total_num of this TaskBasicExecutionData.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        """Sets the total_num of this TaskBasicExecutionData.

        总用例数

        :param total_num: The total_num of this TaskBasicExecutionData.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def vum(self):
        """Gets the vum of this TaskBasicExecutionData.

        分钟*并发数

        :return: The vum of this TaskBasicExecutionData.
        :rtype: int
        """
        return self._vum

    @vum.setter
    def vum(self, vum):
        """Sets the vum of this TaskBasicExecutionData.

        分钟*并发数

        :param vum: The vum of this TaskBasicExecutionData.
        :type vum: int
        """
        self._vum = vum

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
        if not isinstance(other, TaskBasicExecutionData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
