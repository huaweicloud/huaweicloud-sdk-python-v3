# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubTaskRuntimeDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sub_task_name': 'str',
        'create_time': 'str',
        'finish_time': 'str',
        'actual_running_time': 'int',
        'status': 'str',
        'log_storage_link': 'str',
        'pod_create_time': 'str',
        'pod_start_time': 'str',
        'job_failed_times': 'int'
    }

    attribute_map = {
        'sub_task_name': 'sub_task_name',
        'create_time': 'create_time',
        'finish_time': 'finish_time',
        'actual_running_time': 'actual_running_time',
        'status': 'status',
        'log_storage_link': 'log_storage_link',
        'pod_create_time': 'pod_create_time',
        'pod_start_time': 'pod_start_time',
        'job_failed_times': 'job_failed_times'
    }

    def __init__(self, sub_task_name=None, create_time=None, finish_time=None, actual_running_time=None, status=None, log_storage_link=None, pod_create_time=None, pod_start_time=None, job_failed_times=None):
        """SubTaskRuntimeDto

        The model defined in huaweicloud sdk

        :param sub_task_name: 作业子任务的并发实例名称
        :type sub_task_name: str
        :param create_time: 作业子任务的并发实例运行创建时间
        :type create_time: str
        :param finish_time: 作业子任务的并发实例运行结束时间
        :type finish_time: str
        :param actual_running_time: 作业子任务的并发实例实际运行时间
        :type actual_running_time: int
        :param status: 作业子任务的并发实例运行状态
        :type status: str
        :param log_storage_link: 作业日志存储链接
        :type log_storage_link: str
        :param pod_create_time: task的pod创建时间
        :type pod_create_time: str
        :param pod_start_time: task的pod启动时间
        :type pod_start_time: str
        :param job_failed_times: task的cce job失败次数
        :type job_failed_times: int
        """
        
        

        self._sub_task_name = None
        self._create_time = None
        self._finish_time = None
        self._actual_running_time = None
        self._status = None
        self._log_storage_link = None
        self._pod_create_time = None
        self._pod_start_time = None
        self._job_failed_times = None
        self.discriminator = None

        if sub_task_name is not None:
            self.sub_task_name = sub_task_name
        if create_time is not None:
            self.create_time = create_time
        if finish_time is not None:
            self.finish_time = finish_time
        if actual_running_time is not None:
            self.actual_running_time = actual_running_time
        if status is not None:
            self.status = status
        if log_storage_link is not None:
            self.log_storage_link = log_storage_link
        if pod_create_time is not None:
            self.pod_create_time = pod_create_time
        if pod_start_time is not None:
            self.pod_start_time = pod_start_time
        if job_failed_times is not None:
            self.job_failed_times = job_failed_times

    @property
    def sub_task_name(self):
        """Gets the sub_task_name of this SubTaskRuntimeDto.

        作业子任务的并发实例名称

        :return: The sub_task_name of this SubTaskRuntimeDto.
        :rtype: str
        """
        return self._sub_task_name

    @sub_task_name.setter
    def sub_task_name(self, sub_task_name):
        """Sets the sub_task_name of this SubTaskRuntimeDto.

        作业子任务的并发实例名称

        :param sub_task_name: The sub_task_name of this SubTaskRuntimeDto.
        :type sub_task_name: str
        """
        self._sub_task_name = sub_task_name

    @property
    def create_time(self):
        """Gets the create_time of this SubTaskRuntimeDto.

        作业子任务的并发实例运行创建时间

        :return: The create_time of this SubTaskRuntimeDto.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this SubTaskRuntimeDto.

        作业子任务的并发实例运行创建时间

        :param create_time: The create_time of this SubTaskRuntimeDto.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def finish_time(self):
        """Gets the finish_time of this SubTaskRuntimeDto.

        作业子任务的并发实例运行结束时间

        :return: The finish_time of this SubTaskRuntimeDto.
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        """Sets the finish_time of this SubTaskRuntimeDto.

        作业子任务的并发实例运行结束时间

        :param finish_time: The finish_time of this SubTaskRuntimeDto.
        :type finish_time: str
        """
        self._finish_time = finish_time

    @property
    def actual_running_time(self):
        """Gets the actual_running_time of this SubTaskRuntimeDto.

        作业子任务的并发实例实际运行时间

        :return: The actual_running_time of this SubTaskRuntimeDto.
        :rtype: int
        """
        return self._actual_running_time

    @actual_running_time.setter
    def actual_running_time(self, actual_running_time):
        """Sets the actual_running_time of this SubTaskRuntimeDto.

        作业子任务的并发实例实际运行时间

        :param actual_running_time: The actual_running_time of this SubTaskRuntimeDto.
        :type actual_running_time: int
        """
        self._actual_running_time = actual_running_time

    @property
    def status(self):
        """Gets the status of this SubTaskRuntimeDto.

        作业子任务的并发实例运行状态

        :return: The status of this SubTaskRuntimeDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SubTaskRuntimeDto.

        作业子任务的并发实例运行状态

        :param status: The status of this SubTaskRuntimeDto.
        :type status: str
        """
        self._status = status

    @property
    def log_storage_link(self):
        """Gets the log_storage_link of this SubTaskRuntimeDto.

        作业日志存储链接

        :return: The log_storage_link of this SubTaskRuntimeDto.
        :rtype: str
        """
        return self._log_storage_link

    @log_storage_link.setter
    def log_storage_link(self, log_storage_link):
        """Sets the log_storage_link of this SubTaskRuntimeDto.

        作业日志存储链接

        :param log_storage_link: The log_storage_link of this SubTaskRuntimeDto.
        :type log_storage_link: str
        """
        self._log_storage_link = log_storage_link

    @property
    def pod_create_time(self):
        """Gets the pod_create_time of this SubTaskRuntimeDto.

        task的pod创建时间

        :return: The pod_create_time of this SubTaskRuntimeDto.
        :rtype: str
        """
        return self._pod_create_time

    @pod_create_time.setter
    def pod_create_time(self, pod_create_time):
        """Sets the pod_create_time of this SubTaskRuntimeDto.

        task的pod创建时间

        :param pod_create_time: The pod_create_time of this SubTaskRuntimeDto.
        :type pod_create_time: str
        """
        self._pod_create_time = pod_create_time

    @property
    def pod_start_time(self):
        """Gets the pod_start_time of this SubTaskRuntimeDto.

        task的pod启动时间

        :return: The pod_start_time of this SubTaskRuntimeDto.
        :rtype: str
        """
        return self._pod_start_time

    @pod_start_time.setter
    def pod_start_time(self, pod_start_time):
        """Sets the pod_start_time of this SubTaskRuntimeDto.

        task的pod启动时间

        :param pod_start_time: The pod_start_time of this SubTaskRuntimeDto.
        :type pod_start_time: str
        """
        self._pod_start_time = pod_start_time

    @property
    def job_failed_times(self):
        """Gets the job_failed_times of this SubTaskRuntimeDto.

        task的cce job失败次数

        :return: The job_failed_times of this SubTaskRuntimeDto.
        :rtype: int
        """
        return self._job_failed_times

    @job_failed_times.setter
    def job_failed_times(self, job_failed_times):
        """Sets the job_failed_times of this SubTaskRuntimeDto.

        task的cce job失败次数

        :param job_failed_times: The job_failed_times of this SubTaskRuntimeDto.
        :type job_failed_times: int
        """
        self._job_failed_times = job_failed_times

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
        if not isinstance(other, SubTaskRuntimeDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
