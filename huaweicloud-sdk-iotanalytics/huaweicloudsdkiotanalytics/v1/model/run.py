# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Run:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'run_id': 'str',
        'job_id': 'str',
        'job_name': 'str',
        'job_type': 'str',
        'start_time': 'str',
        'duration': 'int',
        'status': 'str',
        'is_schedule_job': 'bool',
        'computing_resource_name': 'str',
        'sql_job': 'SqlJobRun'
    }

    attribute_map = {
        'run_id': 'run_id',
        'job_id': 'job_id',
        'job_name': 'job_name',
        'job_type': 'job_type',
        'start_time': 'start_time',
        'duration': 'duration',
        'status': 'status',
        'is_schedule_job': 'is_schedule_job',
        'computing_resource_name': 'computing_resource_name',
        'sql_job': 'sql_job'
    }

    def __init__(self, run_id=None, job_id=None, job_name=None, job_type=None, start_time=None, duration=None, status=None, is_schedule_job=None, computing_resource_name=None, sql_job=None):
        """Run

        The model defined in huaweicloud sdk

        :param run_id: 作业运行ID。
        :type run_id: str
        :param job_id: 作业ID。
        :type job_id: str
        :param job_name: 作业名称。
        :type job_name: str
        :param job_type: 作业类型。
        :type job_type: str
        :param start_time: 作业开始的时间。时间格式为ISO日期时间格式yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;
        :type start_time: str
        :param duration: 作业运行时长，单位毫秒。
        :type duration: int
        :param status: 此作业的当前状态，包含提交（LAUNCHING）、运行中（RUNNING）、完成（FINISHED）、失败（FAILED）、取消（CANCELLED）。
        :type status: str
        :param is_schedule_job: 是否定时作业。
        :type is_schedule_job: bool
        :param computing_resource_name: 计算资源名称。
        :type computing_resource_name: str
        :param sql_job: 
        :type sql_job: :class:`huaweicloudsdkiotanalytics.v1.SqlJobRun`
        """
        
        

        self._run_id = None
        self._job_id = None
        self._job_name = None
        self._job_type = None
        self._start_time = None
        self._duration = None
        self._status = None
        self._is_schedule_job = None
        self._computing_resource_name = None
        self._sql_job = None
        self.discriminator = None

        self.run_id = run_id
        if job_id is not None:
            self.job_id = job_id
        self.job_name = job_name
        self.job_type = job_type
        self.start_time = start_time
        self.duration = duration
        self.status = status
        if is_schedule_job is not None:
            self.is_schedule_job = is_schedule_job
        if computing_resource_name is not None:
            self.computing_resource_name = computing_resource_name
        if sql_job is not None:
            self.sql_job = sql_job

    @property
    def run_id(self):
        """Gets the run_id of this Run.

        作业运行ID。

        :return: The run_id of this Run.
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this Run.

        作业运行ID。

        :param run_id: The run_id of this Run.
        :type run_id: str
        """
        self._run_id = run_id

    @property
    def job_id(self):
        """Gets the job_id of this Run.

        作业ID。

        :return: The job_id of this Run.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this Run.

        作业ID。

        :param job_id: The job_id of this Run.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        """Gets the job_name of this Run.

        作业名称。

        :return: The job_name of this Run.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this Run.

        作业名称。

        :param job_name: The job_name of this Run.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_type(self):
        """Gets the job_type of this Run.

        作业类型。

        :return: The job_type of this Run.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this Run.

        作业类型。

        :param job_type: The job_type of this Run.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def start_time(self):
        """Gets the start_time of this Run.

        作业开始的时间。时间格式为ISO日期时间格式yyyy-MM-dd'T'HH:mm:ss'Z'

        :return: The start_time of this Run.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Run.

        作业开始的时间。时间格式为ISO日期时间格式yyyy-MM-dd'T'HH:mm:ss'Z'

        :param start_time: The start_time of this Run.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def duration(self):
        """Gets the duration of this Run.

        作业运行时长，单位毫秒。

        :return: The duration of this Run.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Run.

        作业运行时长，单位毫秒。

        :param duration: The duration of this Run.
        :type duration: int
        """
        self._duration = duration

    @property
    def status(self):
        """Gets the status of this Run.

        此作业的当前状态，包含提交（LAUNCHING）、运行中（RUNNING）、完成（FINISHED）、失败（FAILED）、取消（CANCELLED）。

        :return: The status of this Run.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Run.

        此作业的当前状态，包含提交（LAUNCHING）、运行中（RUNNING）、完成（FINISHED）、失败（FAILED）、取消（CANCELLED）。

        :param status: The status of this Run.
        :type status: str
        """
        self._status = status

    @property
    def is_schedule_job(self):
        """Gets the is_schedule_job of this Run.

        是否定时作业。

        :return: The is_schedule_job of this Run.
        :rtype: bool
        """
        return self._is_schedule_job

    @is_schedule_job.setter
    def is_schedule_job(self, is_schedule_job):
        """Sets the is_schedule_job of this Run.

        是否定时作业。

        :param is_schedule_job: The is_schedule_job of this Run.
        :type is_schedule_job: bool
        """
        self._is_schedule_job = is_schedule_job

    @property
    def computing_resource_name(self):
        """Gets the computing_resource_name of this Run.

        计算资源名称。

        :return: The computing_resource_name of this Run.
        :rtype: str
        """
        return self._computing_resource_name

    @computing_resource_name.setter
    def computing_resource_name(self, computing_resource_name):
        """Sets the computing_resource_name of this Run.

        计算资源名称。

        :param computing_resource_name: The computing_resource_name of this Run.
        :type computing_resource_name: str
        """
        self._computing_resource_name = computing_resource_name

    @property
    def sql_job(self):
        """Gets the sql_job of this Run.


        :return: The sql_job of this Run.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.SqlJobRun`
        """
        return self._sql_job

    @sql_job.setter
    def sql_job(self, sql_job):
        """Sets the sql_job of this Run.


        :param sql_job: The sql_job of this Run.
        :type sql_job: :class:`huaweicloudsdkiotanalytics.v1.SqlJobRun`
        """
        self._sql_job = sql_job

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
        if not isinstance(other, Run):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
