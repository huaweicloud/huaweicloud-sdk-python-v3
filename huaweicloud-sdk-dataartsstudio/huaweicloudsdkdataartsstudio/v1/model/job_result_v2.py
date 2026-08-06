# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobResultV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'job_type': 'str',
        'status': 'str',
        'create_user': 'str',
        'create_time': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'last_instance_status': 'str',
        'last_instance_end_time': 'int',
        'owner': 'str',
        'last_update_user': 'str',
        'priority': 'int',
        'flink_job_info': 'str',
        'path': 'str',
        'single_node_job_flag': 'bool',
        'alarms': 'list[JobAlarm]',
        'last_update_time': 'int',
        'single_node_job_type': 'str',
        'empty_running_job': 'str',
        'next_plan_time': 'str'
    }

    attribute_map = {
        'name': 'name',
        'job_type': 'job_type',
        'status': 'status',
        'create_user': 'create_user',
        'create_time': 'create_time',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'last_instance_status': 'last_instance_status',
        'last_instance_end_time': 'last_instance_end_time',
        'owner': 'owner',
        'last_update_user': 'last_update_user',
        'priority': 'priority',
        'flink_job_info': 'flink_job_info',
        'path': 'path',
        'single_node_job_flag': 'single_node_job_flag',
        'alarms': 'alarms',
        'last_update_time': 'last_update_time',
        'single_node_job_type': 'single_node_job_type',
        'empty_running_job': 'empty_running_job',
        'next_plan_time': 'next_plan_time'
    }

    def __init__(self, name=None, job_type=None, status=None, create_user=None, create_time=None, start_time=None, end_time=None, last_instance_status=None, last_instance_end_time=None, owner=None, last_update_user=None, priority=None, flink_job_info=None, path=None, single_node_job_flag=None, alarms=None, last_update_time=None, single_node_job_type=None, empty_running_job=None, next_plan_time=None):
        r"""JobResultV2

        The model defined in huaweicloud sdk

        :param name: 作业名称。
        :type name: str
        :param job_type: 作业类型： - BATCH: 批处理作业 - REAL_TIME: 实时作业
        :type job_type: str
        :param status: 作业状态。
        :type status: str
        :param create_user: 作业创建者。
        :type create_user: str
        :param create_time: 作业创建时间，13位时间戳。
        :type create_time: int
        :param start_time: 作业开始时间，13位时间戳。
        :type start_time: int
        :param end_time: 作业结束时间，13位时间戳。
        :type end_time: int
        :param last_instance_status: 上次实例运行状态。
        :type last_instance_status: str
        :param last_instance_end_time: 上次实例结束时间，13位时间戳。
        :type last_instance_end_time: int
        :param owner: 作业负责人。
        :type owner: str
        :param last_update_user: 最后更新人。
        :type last_update_user: str
        :param priority: 作业优先级。
        :type priority: int
        :param flink_job_info: Flink作业信息。
        :type flink_job_info: str
        :param path: 作业路径。
        :type path: str
        :param single_node_job_flag: 是否为单节点作业。
        :type single_node_job_flag: bool
        :param alarms: 告警信息列表。
        :type alarms: list[:class:`huaweicloudsdkdataartsstudio.v1.JobAlarm`]
        :param last_update_time: 最后更新时间，13位时间戳。
        :type last_update_time: int
        :param single_node_job_type: 单节点作业类型。
        :type single_node_job_type: str
        :param empty_running_job: 空跑作业标识。
        :type empty_running_job: str
        :param next_plan_time: 下次计划执行时间。
        :type next_plan_time: str
        """
        
        

        self._name = None
        self._job_type = None
        self._status = None
        self._create_user = None
        self._create_time = None
        self._start_time = None
        self._end_time = None
        self._last_instance_status = None
        self._last_instance_end_time = None
        self._owner = None
        self._last_update_user = None
        self._priority = None
        self._flink_job_info = None
        self._path = None
        self._single_node_job_flag = None
        self._alarms = None
        self._last_update_time = None
        self._single_node_job_type = None
        self._empty_running_job = None
        self._next_plan_time = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if job_type is not None:
            self.job_type = job_type
        if status is not None:
            self.status = status
        if create_user is not None:
            self.create_user = create_user
        if create_time is not None:
            self.create_time = create_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if last_instance_status is not None:
            self.last_instance_status = last_instance_status
        if last_instance_end_time is not None:
            self.last_instance_end_time = last_instance_end_time
        if owner is not None:
            self.owner = owner
        if last_update_user is not None:
            self.last_update_user = last_update_user
        if priority is not None:
            self.priority = priority
        if flink_job_info is not None:
            self.flink_job_info = flink_job_info
        if path is not None:
            self.path = path
        if single_node_job_flag is not None:
            self.single_node_job_flag = single_node_job_flag
        if alarms is not None:
            self.alarms = alarms
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if single_node_job_type is not None:
            self.single_node_job_type = single_node_job_type
        if empty_running_job is not None:
            self.empty_running_job = empty_running_job
        if next_plan_time is not None:
            self.next_plan_time = next_plan_time

    @property
    def name(self):
        r"""Gets the name of this JobResultV2.

        作业名称。

        :return: The name of this JobResultV2.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this JobResultV2.

        作业名称。

        :param name: The name of this JobResultV2.
        :type name: str
        """
        self._name = name

    @property
    def job_type(self):
        r"""Gets the job_type of this JobResultV2.

        作业类型： - BATCH: 批处理作业 - REAL_TIME: 实时作业

        :return: The job_type of this JobResultV2.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this JobResultV2.

        作业类型： - BATCH: 批处理作业 - REAL_TIME: 实时作业

        :param job_type: The job_type of this JobResultV2.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def status(self):
        r"""Gets the status of this JobResultV2.

        作业状态。

        :return: The status of this JobResultV2.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this JobResultV2.

        作业状态。

        :param status: The status of this JobResultV2.
        :type status: str
        """
        self._status = status

    @property
    def create_user(self):
        r"""Gets the create_user of this JobResultV2.

        作业创建者。

        :return: The create_user of this JobResultV2.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this JobResultV2.

        作业创建者。

        :param create_user: The create_user of this JobResultV2.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def create_time(self):
        r"""Gets the create_time of this JobResultV2.

        作业创建时间，13位时间戳。

        :return: The create_time of this JobResultV2.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this JobResultV2.

        作业创建时间，13位时间戳。

        :param create_time: The create_time of this JobResultV2.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def start_time(self):
        r"""Gets the start_time of this JobResultV2.

        作业开始时间，13位时间戳。

        :return: The start_time of this JobResultV2.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this JobResultV2.

        作业开始时间，13位时间戳。

        :param start_time: The start_time of this JobResultV2.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this JobResultV2.

        作业结束时间，13位时间戳。

        :return: The end_time of this JobResultV2.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this JobResultV2.

        作业结束时间，13位时间戳。

        :param end_time: The end_time of this JobResultV2.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def last_instance_status(self):
        r"""Gets the last_instance_status of this JobResultV2.

        上次实例运行状态。

        :return: The last_instance_status of this JobResultV2.
        :rtype: str
        """
        return self._last_instance_status

    @last_instance_status.setter
    def last_instance_status(self, last_instance_status):
        r"""Sets the last_instance_status of this JobResultV2.

        上次实例运行状态。

        :param last_instance_status: The last_instance_status of this JobResultV2.
        :type last_instance_status: str
        """
        self._last_instance_status = last_instance_status

    @property
    def last_instance_end_time(self):
        r"""Gets the last_instance_end_time of this JobResultV2.

        上次实例结束时间，13位时间戳。

        :return: The last_instance_end_time of this JobResultV2.
        :rtype: int
        """
        return self._last_instance_end_time

    @last_instance_end_time.setter
    def last_instance_end_time(self, last_instance_end_time):
        r"""Sets the last_instance_end_time of this JobResultV2.

        上次实例结束时间，13位时间戳。

        :param last_instance_end_time: The last_instance_end_time of this JobResultV2.
        :type last_instance_end_time: int
        """
        self._last_instance_end_time = last_instance_end_time

    @property
    def owner(self):
        r"""Gets the owner of this JobResultV2.

        作业负责人。

        :return: The owner of this JobResultV2.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this JobResultV2.

        作业负责人。

        :param owner: The owner of this JobResultV2.
        :type owner: str
        """
        self._owner = owner

    @property
    def last_update_user(self):
        r"""Gets the last_update_user of this JobResultV2.

        最后更新人。

        :return: The last_update_user of this JobResultV2.
        :rtype: str
        """
        return self._last_update_user

    @last_update_user.setter
    def last_update_user(self, last_update_user):
        r"""Sets the last_update_user of this JobResultV2.

        最后更新人。

        :param last_update_user: The last_update_user of this JobResultV2.
        :type last_update_user: str
        """
        self._last_update_user = last_update_user

    @property
    def priority(self):
        r"""Gets the priority of this JobResultV2.

        作业优先级。

        :return: The priority of this JobResultV2.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this JobResultV2.

        作业优先级。

        :param priority: The priority of this JobResultV2.
        :type priority: int
        """
        self._priority = priority

    @property
    def flink_job_info(self):
        r"""Gets the flink_job_info of this JobResultV2.

        Flink作业信息。

        :return: The flink_job_info of this JobResultV2.
        :rtype: str
        """
        return self._flink_job_info

    @flink_job_info.setter
    def flink_job_info(self, flink_job_info):
        r"""Sets the flink_job_info of this JobResultV2.

        Flink作业信息。

        :param flink_job_info: The flink_job_info of this JobResultV2.
        :type flink_job_info: str
        """
        self._flink_job_info = flink_job_info

    @property
    def path(self):
        r"""Gets the path of this JobResultV2.

        作业路径。

        :return: The path of this JobResultV2.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this JobResultV2.

        作业路径。

        :param path: The path of this JobResultV2.
        :type path: str
        """
        self._path = path

    @property
    def single_node_job_flag(self):
        r"""Gets the single_node_job_flag of this JobResultV2.

        是否为单节点作业。

        :return: The single_node_job_flag of this JobResultV2.
        :rtype: bool
        """
        return self._single_node_job_flag

    @single_node_job_flag.setter
    def single_node_job_flag(self, single_node_job_flag):
        r"""Sets the single_node_job_flag of this JobResultV2.

        是否为单节点作业。

        :param single_node_job_flag: The single_node_job_flag of this JobResultV2.
        :type single_node_job_flag: bool
        """
        self._single_node_job_flag = single_node_job_flag

    @property
    def alarms(self):
        r"""Gets the alarms of this JobResultV2.

        告警信息列表。

        :return: The alarms of this JobResultV2.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.JobAlarm`]
        """
        return self._alarms

    @alarms.setter
    def alarms(self, alarms):
        r"""Sets the alarms of this JobResultV2.

        告警信息列表。

        :param alarms: The alarms of this JobResultV2.
        :type alarms: list[:class:`huaweicloudsdkdataartsstudio.v1.JobAlarm`]
        """
        self._alarms = alarms

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this JobResultV2.

        最后更新时间，13位时间戳。

        :return: The last_update_time of this JobResultV2.
        :rtype: int
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this JobResultV2.

        最后更新时间，13位时间戳。

        :param last_update_time: The last_update_time of this JobResultV2.
        :type last_update_time: int
        """
        self._last_update_time = last_update_time

    @property
    def single_node_job_type(self):
        r"""Gets the single_node_job_type of this JobResultV2.

        单节点作业类型。

        :return: The single_node_job_type of this JobResultV2.
        :rtype: str
        """
        return self._single_node_job_type

    @single_node_job_type.setter
    def single_node_job_type(self, single_node_job_type):
        r"""Sets the single_node_job_type of this JobResultV2.

        单节点作业类型。

        :param single_node_job_type: The single_node_job_type of this JobResultV2.
        :type single_node_job_type: str
        """
        self._single_node_job_type = single_node_job_type

    @property
    def empty_running_job(self):
        r"""Gets the empty_running_job of this JobResultV2.

        空跑作业标识。

        :return: The empty_running_job of this JobResultV2.
        :rtype: str
        """
        return self._empty_running_job

    @empty_running_job.setter
    def empty_running_job(self, empty_running_job):
        r"""Sets the empty_running_job of this JobResultV2.

        空跑作业标识。

        :param empty_running_job: The empty_running_job of this JobResultV2.
        :type empty_running_job: str
        """
        self._empty_running_job = empty_running_job

    @property
    def next_plan_time(self):
        r"""Gets the next_plan_time of this JobResultV2.

        下次计划执行时间。

        :return: The next_plan_time of this JobResultV2.
        :rtype: str
        """
        return self._next_plan_time

    @next_plan_time.setter
    def next_plan_time(self, next_plan_time):
        r"""Sets the next_plan_time of this JobResultV2.

        下次计划执行时间。

        :param next_plan_time: The next_plan_time of this JobResultV2.
        :type next_plan_time: str
        """
        self._next_plan_time = next_plan_time

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
        if not isinstance(other, JobResultV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
