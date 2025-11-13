# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDbAgentJobsResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'job_name': 'str',
        'is_enabled': 'bool',
        'run_time': 'str',
        'run_status': 'str',
        'last_failure_time': 'str',
        'failure_count': 'int',
        'agent_type': 'str',
        'profile_id': 'str',
        'profile_name': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'job_name': 'job_name',
        'is_enabled': 'is_enabled',
        'run_time': 'run_time',
        'run_status': 'run_status',
        'last_failure_time': 'last_failure_time',
        'failure_count': 'failure_count',
        'agent_type': 'agent_type',
        'profile_id': 'profile_id',
        'profile_name': 'profile_name'
    }

    def __init__(self, job_id=None, job_name=None, is_enabled=None, run_time=None, run_status=None, last_failure_time=None, failure_count=None, agent_type=None, profile_id=None, profile_name=None):
        r"""ListDbAgentJobsResult

        The model defined in huaweicloud sdk

        :param job_id: 作业id。
        :type job_id: str
        :param job_name: 作业名。
        :type job_name: str
        :param is_enabled: 是否可用。  true：可用。 false：不可用。
        :type is_enabled: bool
        :param run_time: 最新执行时间。格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type run_time: str
        :param run_status: 作业执行状态。取值如下:  failed:失败。 succeeded:成功。 retrying:重试中。 canceled:已取消。 in_progress:正在运行。
        :type run_status: str
        :param last_failure_time: 最近失败时间。格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type last_failure_time: str
        :param failure_count: 历史失败次数。
        :type failure_count: int
        :param agent_type: 作业代理的类型。  snapshot：快照代理 log_reader：日志读取器代理 distribution：分发代理 merge:合并代理 queue_reader：队列读取器代理。
        :type agent_type: str
        :param profile_id: 配置文件id。作业类型为replication时特有。
        :type profile_id: str
        :param profile_name: 配置文件名。作业类型为replication时特有。
        :type profile_name: str
        """
        
        

        self._job_id = None
        self._job_name = None
        self._is_enabled = None
        self._run_time = None
        self._run_status = None
        self._last_failure_time = None
        self._failure_count = None
        self._agent_type = None
        self._profile_id = None
        self._profile_name = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if job_name is not None:
            self.job_name = job_name
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if run_time is not None:
            self.run_time = run_time
        if run_status is not None:
            self.run_status = run_status
        if last_failure_time is not None:
            self.last_failure_time = last_failure_time
        if failure_count is not None:
            self.failure_count = failure_count
        if agent_type is not None:
            self.agent_type = agent_type
        if profile_id is not None:
            self.profile_id = profile_id
        if profile_name is not None:
            self.profile_name = profile_name

    @property
    def job_id(self):
        r"""Gets the job_id of this ListDbAgentJobsResult.

        作业id。

        :return: The job_id of this ListDbAgentJobsResult.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ListDbAgentJobsResult.

        作业id。

        :param job_id: The job_id of this ListDbAgentJobsResult.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        r"""Gets the job_name of this ListDbAgentJobsResult.

        作业名。

        :return: The job_name of this ListDbAgentJobsResult.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this ListDbAgentJobsResult.

        作业名。

        :param job_name: The job_name of this ListDbAgentJobsResult.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def is_enabled(self):
        r"""Gets the is_enabled of this ListDbAgentJobsResult.

        是否可用。  true：可用。 false：不可用。

        :return: The is_enabled of this ListDbAgentJobsResult.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        r"""Sets the is_enabled of this ListDbAgentJobsResult.

        是否可用。  true：可用。 false：不可用。

        :param is_enabled: The is_enabled of this ListDbAgentJobsResult.
        :type is_enabled: bool
        """
        self._is_enabled = is_enabled

    @property
    def run_time(self):
        r"""Gets the run_time of this ListDbAgentJobsResult.

        最新执行时间。格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The run_time of this ListDbAgentJobsResult.
        :rtype: str
        """
        return self._run_time

    @run_time.setter
    def run_time(self, run_time):
        r"""Sets the run_time of this ListDbAgentJobsResult.

        最新执行时间。格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param run_time: The run_time of this ListDbAgentJobsResult.
        :type run_time: str
        """
        self._run_time = run_time

    @property
    def run_status(self):
        r"""Gets the run_status of this ListDbAgentJobsResult.

        作业执行状态。取值如下:  failed:失败。 succeeded:成功。 retrying:重试中。 canceled:已取消。 in_progress:正在运行。

        :return: The run_status of this ListDbAgentJobsResult.
        :rtype: str
        """
        return self._run_status

    @run_status.setter
    def run_status(self, run_status):
        r"""Sets the run_status of this ListDbAgentJobsResult.

        作业执行状态。取值如下:  failed:失败。 succeeded:成功。 retrying:重试中。 canceled:已取消。 in_progress:正在运行。

        :param run_status: The run_status of this ListDbAgentJobsResult.
        :type run_status: str
        """
        self._run_status = run_status

    @property
    def last_failure_time(self):
        r"""Gets the last_failure_time of this ListDbAgentJobsResult.

        最近失败时间。格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The last_failure_time of this ListDbAgentJobsResult.
        :rtype: str
        """
        return self._last_failure_time

    @last_failure_time.setter
    def last_failure_time(self, last_failure_time):
        r"""Sets the last_failure_time of this ListDbAgentJobsResult.

        最近失败时间。格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param last_failure_time: The last_failure_time of this ListDbAgentJobsResult.
        :type last_failure_time: str
        """
        self._last_failure_time = last_failure_time

    @property
    def failure_count(self):
        r"""Gets the failure_count of this ListDbAgentJobsResult.

        历史失败次数。

        :return: The failure_count of this ListDbAgentJobsResult.
        :rtype: int
        """
        return self._failure_count

    @failure_count.setter
    def failure_count(self, failure_count):
        r"""Sets the failure_count of this ListDbAgentJobsResult.

        历史失败次数。

        :param failure_count: The failure_count of this ListDbAgentJobsResult.
        :type failure_count: int
        """
        self._failure_count = failure_count

    @property
    def agent_type(self):
        r"""Gets the agent_type of this ListDbAgentJobsResult.

        作业代理的类型。  snapshot：快照代理 log_reader：日志读取器代理 distribution：分发代理 merge:合并代理 queue_reader：队列读取器代理。

        :return: The agent_type of this ListDbAgentJobsResult.
        :rtype: str
        """
        return self._agent_type

    @agent_type.setter
    def agent_type(self, agent_type):
        r"""Sets the agent_type of this ListDbAgentJobsResult.

        作业代理的类型。  snapshot：快照代理 log_reader：日志读取器代理 distribution：分发代理 merge:合并代理 queue_reader：队列读取器代理。

        :param agent_type: The agent_type of this ListDbAgentJobsResult.
        :type agent_type: str
        """
        self._agent_type = agent_type

    @property
    def profile_id(self):
        r"""Gets the profile_id of this ListDbAgentJobsResult.

        配置文件id。作业类型为replication时特有。

        :return: The profile_id of this ListDbAgentJobsResult.
        :rtype: str
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        r"""Sets the profile_id of this ListDbAgentJobsResult.

        配置文件id。作业类型为replication时特有。

        :param profile_id: The profile_id of this ListDbAgentJobsResult.
        :type profile_id: str
        """
        self._profile_id = profile_id

    @property
    def profile_name(self):
        r"""Gets the profile_name of this ListDbAgentJobsResult.

        配置文件名。作业类型为replication时特有。

        :return: The profile_name of this ListDbAgentJobsResult.
        :rtype: str
        """
        return self._profile_name

    @profile_name.setter
    def profile_name(self, profile_name):
        r"""Sets the profile_name of this ListDbAgentJobsResult.

        配置文件名。作业类型为replication时特有。

        :param profile_name: The profile_name of this ListDbAgentJobsResult.
        :type profile_name: str
        """
        self._profile_name = profile_name

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListDbAgentJobsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
