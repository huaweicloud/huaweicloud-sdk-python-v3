# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_name': 'str',
        'status': 'str',
        'job_instance_name': 'str',
        'plan_time': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'execute_time': 'int',
        'instance_id': 'int',
        'instance_type': 'int',
        'submit_time': 'int',
        'job_id': 'int',
        'version': 'int',
        'force_success': 'bool',
        'ignore_success': 'bool'
    }

    attribute_map = {
        'job_name': 'job_name',
        'status': 'status',
        'job_instance_name': 'job_instance_name',
        'plan_time': 'plan_time',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'execute_time': 'execute_time',
        'instance_id': 'instance_id',
        'instance_type': 'instance_type',
        'submit_time': 'submit_time',
        'job_id': 'job_id',
        'version': 'version',
        'force_success': 'force_success',
        'ignore_success': 'ignore_success'
    }

    def __init__(self, job_name=None, status=None, job_instance_name=None, plan_time=None, start_time=None, end_time=None, execute_time=None, instance_id=None, instance_type=None, submit_time=None, job_id=None, version=None, force_success=None, ignore_success=None):
        """JobInstance

        The model defined in huaweicloud sdk

        :param job_name: 作业名称。如果要查询指定批处理作业的实例列表，jobName就是批处理作业名。如果要查询实时作业下某个节点关联的子作业，jobName格式为[实时作业名称]_[节点名称]。
        :type job_name: str
        :param status: 实例运行状态： - waiting：等待运行 - running：运行中 - success：运行成功 - fail： 运行失败 - running-exception：运行异常 - pause： 暂停 - manual-stop：取消 - skip-by-depend：跳过 - freeze：冻结
        :type status: str
        :param job_instance_name: 作业实例运行时日志记录的实例名称, 非作业定义的名称
        :type job_instance_name: str
        :param plan_time: 作业实例计划执行时间
        :type plan_time: int
        :param start_time: 作业实例实际执行开始时间
        :type start_time: int
        :param end_time: 作业实例实际执行结束时间
        :type end_time: int
        :param execute_time: 执行耗时，单位：毫秒
        :type execute_time: int
        :param instance_id: 作业实例id
        :type instance_id: int
        :param instance_type: 作业实例类型
        :type instance_type: int
        :param submit_time: 作业提交运行时间
        :type submit_time: int
        :param job_id: 作业id
        :type job_id: int
        :param version: 作业实例版本
        :type version: int
        :param force_success: 作业实例状态筛选为强制成功
        :type force_success: bool
        :param ignore_success: 作业实例状态筛选为忽略失败
        :type ignore_success: bool
        """
        
        

        self._job_name = None
        self._status = None
        self._job_instance_name = None
        self._plan_time = None
        self._start_time = None
        self._end_time = None
        self._execute_time = None
        self._instance_id = None
        self._instance_type = None
        self._submit_time = None
        self._job_id = None
        self._version = None
        self._force_success = None
        self._ignore_success = None
        self.discriminator = None

        if job_name is not None:
            self.job_name = job_name
        if status is not None:
            self.status = status
        if job_instance_name is not None:
            self.job_instance_name = job_instance_name
        if plan_time is not None:
            self.plan_time = plan_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if execute_time is not None:
            self.execute_time = execute_time
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_type is not None:
            self.instance_type = instance_type
        if submit_time is not None:
            self.submit_time = submit_time
        if job_id is not None:
            self.job_id = job_id
        if version is not None:
            self.version = version
        if force_success is not None:
            self.force_success = force_success
        if ignore_success is not None:
            self.ignore_success = ignore_success

    @property
    def job_name(self):
        """Gets the job_name of this JobInstance.

        作业名称。如果要查询指定批处理作业的实例列表，jobName就是批处理作业名。如果要查询实时作业下某个节点关联的子作业，jobName格式为[实时作业名称]_[节点名称]。

        :return: The job_name of this JobInstance.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this JobInstance.

        作业名称。如果要查询指定批处理作业的实例列表，jobName就是批处理作业名。如果要查询实时作业下某个节点关联的子作业，jobName格式为[实时作业名称]_[节点名称]。

        :param job_name: The job_name of this JobInstance.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def status(self):
        """Gets the status of this JobInstance.

        实例运行状态： - waiting：等待运行 - running：运行中 - success：运行成功 - fail： 运行失败 - running-exception：运行异常 - pause： 暂停 - manual-stop：取消 - skip-by-depend：跳过 - freeze：冻结

        :return: The status of this JobInstance.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JobInstance.

        实例运行状态： - waiting：等待运行 - running：运行中 - success：运行成功 - fail： 运行失败 - running-exception：运行异常 - pause： 暂停 - manual-stop：取消 - skip-by-depend：跳过 - freeze：冻结

        :param status: The status of this JobInstance.
        :type status: str
        """
        self._status = status

    @property
    def job_instance_name(self):
        """Gets the job_instance_name of this JobInstance.

        作业实例运行时日志记录的实例名称, 非作业定义的名称

        :return: The job_instance_name of this JobInstance.
        :rtype: str
        """
        return self._job_instance_name

    @job_instance_name.setter
    def job_instance_name(self, job_instance_name):
        """Sets the job_instance_name of this JobInstance.

        作业实例运行时日志记录的实例名称, 非作业定义的名称

        :param job_instance_name: The job_instance_name of this JobInstance.
        :type job_instance_name: str
        """
        self._job_instance_name = job_instance_name

    @property
    def plan_time(self):
        """Gets the plan_time of this JobInstance.

        作业实例计划执行时间

        :return: The plan_time of this JobInstance.
        :rtype: int
        """
        return self._plan_time

    @plan_time.setter
    def plan_time(self, plan_time):
        """Sets the plan_time of this JobInstance.

        作业实例计划执行时间

        :param plan_time: The plan_time of this JobInstance.
        :type plan_time: int
        """
        self._plan_time = plan_time

    @property
    def start_time(self):
        """Gets the start_time of this JobInstance.

        作业实例实际执行开始时间

        :return: The start_time of this JobInstance.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this JobInstance.

        作业实例实际执行开始时间

        :param start_time: The start_time of this JobInstance.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this JobInstance.

        作业实例实际执行结束时间

        :return: The end_time of this JobInstance.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this JobInstance.

        作业实例实际执行结束时间

        :param end_time: The end_time of this JobInstance.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def execute_time(self):
        """Gets the execute_time of this JobInstance.

        执行耗时，单位：毫秒

        :return: The execute_time of this JobInstance.
        :rtype: int
        """
        return self._execute_time

    @execute_time.setter
    def execute_time(self, execute_time):
        """Sets the execute_time of this JobInstance.

        执行耗时，单位：毫秒

        :param execute_time: The execute_time of this JobInstance.
        :type execute_time: int
        """
        self._execute_time = execute_time

    @property
    def instance_id(self):
        """Gets the instance_id of this JobInstance.

        作业实例id

        :return: The instance_id of this JobInstance.
        :rtype: int
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this JobInstance.

        作业实例id

        :param instance_id: The instance_id of this JobInstance.
        :type instance_id: int
        """
        self._instance_id = instance_id

    @property
    def instance_type(self):
        """Gets the instance_type of this JobInstance.

        作业实例类型

        :return: The instance_type of this JobInstance.
        :rtype: int
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this JobInstance.

        作业实例类型

        :param instance_type: The instance_type of this JobInstance.
        :type instance_type: int
        """
        self._instance_type = instance_type

    @property
    def submit_time(self):
        """Gets the submit_time of this JobInstance.

        作业提交运行时间

        :return: The submit_time of this JobInstance.
        :rtype: int
        """
        return self._submit_time

    @submit_time.setter
    def submit_time(self, submit_time):
        """Sets the submit_time of this JobInstance.

        作业提交运行时间

        :param submit_time: The submit_time of this JobInstance.
        :type submit_time: int
        """
        self._submit_time = submit_time

    @property
    def job_id(self):
        """Gets the job_id of this JobInstance.

        作业id

        :return: The job_id of this JobInstance.
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this JobInstance.

        作业id

        :param job_id: The job_id of this JobInstance.
        :type job_id: int
        """
        self._job_id = job_id

    @property
    def version(self):
        """Gets the version of this JobInstance.

        作业实例版本

        :return: The version of this JobInstance.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this JobInstance.

        作业实例版本

        :param version: The version of this JobInstance.
        :type version: int
        """
        self._version = version

    @property
    def force_success(self):
        """Gets the force_success of this JobInstance.

        作业实例状态筛选为强制成功

        :return: The force_success of this JobInstance.
        :rtype: bool
        """
        return self._force_success

    @force_success.setter
    def force_success(self, force_success):
        """Sets the force_success of this JobInstance.

        作业实例状态筛选为强制成功

        :param force_success: The force_success of this JobInstance.
        :type force_success: bool
        """
        self._force_success = force_success

    @property
    def ignore_success(self):
        """Gets the ignore_success of this JobInstance.

        作业实例状态筛选为忽略失败

        :return: The ignore_success of this JobInstance.
        :rtype: bool
        """
        return self._ignore_success

    @ignore_success.setter
    def ignore_success(self, ignore_success):
        """Sets the ignore_success of this JobInstance.

        作业实例状态筛选为忽略失败

        :param ignore_success: The ignore_success of this JobInstance.
        :type ignore_success: bool
        """
        self._ignore_success = ignore_success

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
        if not isinstance(other, JobInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
