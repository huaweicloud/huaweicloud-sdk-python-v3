# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestcaseResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'execute_result_id': 'str',
        'execute_status': 'str',
        'failure_cause': 'str',
        'task_id': 'str',
        'plan_id': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'executor_id': 'str',
        'executor_name': 'str'
    }

    attribute_map = {
        'execute_result_id': 'execute_result_id',
        'execute_status': 'execute_status',
        'failure_cause': 'failure_cause',
        'task_id': 'task_id',
        'plan_id': 'plan_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'executor_id': 'executor_id',
        'executor_name': 'executor_name'
    }

    def __init__(self, execute_result_id=None, execute_status=None, failure_cause=None, task_id=None, plan_id=None, start_time=None, end_time=None, executor_id=None, executor_name=None):
        """TestcaseResult

        The model defined in huaweicloud sdk

        :param execute_result_id: 结果
        :type execute_result_id: str
        :param execute_status: 测试用例状态
        :type execute_status: str
        :param failure_cause: 失败原因
        :type failure_cause: str
        :param task_id: 任务id
        :type task_id: str
        :param plan_id: 测试计划id
        :type plan_id: str
        :param start_time: 开始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        :param executor_id: 执行测试用例用户id
        :type executor_id: str
        :param executor_name: 执行测试用例用户name
        :type executor_name: str
        """
        
        

        self._execute_result_id = None
        self._execute_status = None
        self._failure_cause = None
        self._task_id = None
        self._plan_id = None
        self._start_time = None
        self._end_time = None
        self._executor_id = None
        self._executor_name = None
        self.discriminator = None

        if execute_result_id is not None:
            self.execute_result_id = execute_result_id
        if execute_status is not None:
            self.execute_status = execute_status
        if failure_cause is not None:
            self.failure_cause = failure_cause
        if task_id is not None:
            self.task_id = task_id
        if plan_id is not None:
            self.plan_id = plan_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if executor_id is not None:
            self.executor_id = executor_id
        if executor_name is not None:
            self.executor_name = executor_name

    @property
    def execute_result_id(self):
        """Gets the execute_result_id of this TestcaseResult.

        结果

        :return: The execute_result_id of this TestcaseResult.
        :rtype: str
        """
        return self._execute_result_id

    @execute_result_id.setter
    def execute_result_id(self, execute_result_id):
        """Sets the execute_result_id of this TestcaseResult.

        结果

        :param execute_result_id: The execute_result_id of this TestcaseResult.
        :type execute_result_id: str
        """
        self._execute_result_id = execute_result_id

    @property
    def execute_status(self):
        """Gets the execute_status of this TestcaseResult.

        测试用例状态

        :return: The execute_status of this TestcaseResult.
        :rtype: str
        """
        return self._execute_status

    @execute_status.setter
    def execute_status(self, execute_status):
        """Sets the execute_status of this TestcaseResult.

        测试用例状态

        :param execute_status: The execute_status of this TestcaseResult.
        :type execute_status: str
        """
        self._execute_status = execute_status

    @property
    def failure_cause(self):
        """Gets the failure_cause of this TestcaseResult.

        失败原因

        :return: The failure_cause of this TestcaseResult.
        :rtype: str
        """
        return self._failure_cause

    @failure_cause.setter
    def failure_cause(self, failure_cause):
        """Sets the failure_cause of this TestcaseResult.

        失败原因

        :param failure_cause: The failure_cause of this TestcaseResult.
        :type failure_cause: str
        """
        self._failure_cause = failure_cause

    @property
    def task_id(self):
        """Gets the task_id of this TestcaseResult.

        任务id

        :return: The task_id of this TestcaseResult.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this TestcaseResult.

        任务id

        :param task_id: The task_id of this TestcaseResult.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def plan_id(self):
        """Gets the plan_id of this TestcaseResult.

        测试计划id

        :return: The plan_id of this TestcaseResult.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this TestcaseResult.

        测试计划id

        :param plan_id: The plan_id of this TestcaseResult.
        :type plan_id: str
        """
        self._plan_id = plan_id

    @property
    def start_time(self):
        """Gets the start_time of this TestcaseResult.

        开始时间

        :return: The start_time of this TestcaseResult.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TestcaseResult.

        开始时间

        :param start_time: The start_time of this TestcaseResult.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this TestcaseResult.

        结束时间

        :return: The end_time of this TestcaseResult.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TestcaseResult.

        结束时间

        :param end_time: The end_time of this TestcaseResult.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def executor_id(self):
        """Gets the executor_id of this TestcaseResult.

        执行测试用例用户id

        :return: The executor_id of this TestcaseResult.
        :rtype: str
        """
        return self._executor_id

    @executor_id.setter
    def executor_id(self, executor_id):
        """Sets the executor_id of this TestcaseResult.

        执行测试用例用户id

        :param executor_id: The executor_id of this TestcaseResult.
        :type executor_id: str
        """
        self._executor_id = executor_id

    @property
    def executor_name(self):
        """Gets the executor_name of this TestcaseResult.

        执行测试用例用户name

        :return: The executor_name of this TestcaseResult.
        :rtype: str
        """
        return self._executor_name

    @executor_name.setter
    def executor_name(self, executor_name):
        """Sets the executor_name of this TestcaseResult.

        执行测试用例用户name

        :param executor_name: The executor_name of this TestcaseResult.
        :type executor_name: str
        """
        self._executor_name = executor_name

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
        if not isinstance(other, TestcaseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
