# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobResult:

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
        'owner': 'str',
        'priority': 'int',
        'status': 'str',
        'create_user': 'str',
        'create_time': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'last_instance_status': 'str',
        'last_instance_end_time': 'int',
        'last_update_time': 'int',
        'last_update_user': 'str',
        'path': 'str',
        'single_node_job_flag': 'bool',
        'flink_job_info': 'str',
        'alarms': 'list[JobAlarm]'
    }

    attribute_map = {
        'name': 'name',
        'job_type': 'jobType',
        'owner': 'owner',
        'priority': 'priority',
        'status': 'status',
        'create_user': 'createUser',
        'create_time': 'createTime',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'last_instance_status': 'lastInstanceStatus',
        'last_instance_end_time': 'lastInstanceEndTime',
        'last_update_time': 'lastUpdateTime',
        'last_update_user': 'lastUpdateUser',
        'path': 'path',
        'single_node_job_flag': 'singleNodeJobFlag',
        'flink_job_info': 'flinkJobInfo',
        'alarms': 'alarms'
    }

    def __init__(self, name=None, job_type=None, owner=None, priority=None, status=None, create_user=None, create_time=None, start_time=None, end_time=None, last_instance_status=None, last_instance_end_time=None, last_update_time=None, last_update_user=None, path=None, single_node_job_flag=None, flink_job_info=None, alarms=None):
        r"""JobResult

        The model defined in huaweicloud sdk

        :param name: 作业名称
        :type name: str
        :param job_type: 作业类型
        :type job_type: str
        :param owner: 作业责任人，长度不能超过128个字符
        :type owner: str
        :param priority: 作业优先级，取值范围[0, 2]，默认值是0。0代表高优先级，1代表中优先级，2代表低优先级
        :type priority: int
        :param status: 
        :type status: str
        :param create_user: 作业的创建者
        :type create_user: str
        :param create_time: 作业的创建时间
        :type create_time: int
        :param start_time: 作业的启动时间
        :type start_time: int
        :param end_time: 作业配置的结束时间
        :type end_time: int
        :param last_instance_status: 作业最近一次运行实例状态，当jobType为BATCH时才有本字段
        :type last_instance_status: str
        :param last_instance_end_time: 作业最近一次运行实例运行结束时间，当jobType为BATCH时才有本字段
        :type last_instance_end_time: int
        :param last_update_time: 作业最后一次更新时间
        :type last_update_time: int
        :param last_update_user: 作业最后一次更新用户
        :type last_update_user: str
        :param path: 作业的路径
        :type path: str
        :param single_node_job_flag: 作业是否为单任务作业
        :type single_node_job_flag: bool
        :param flink_job_info: flink作业信息
        :type flink_job_info: str
        :param alarms: 作业监控告警信息
        :type alarms: list[:class:`huaweicloudsdkdgc.v1.JobAlarm`]
        """
        
        

        self._name = None
        self._job_type = None
        self._owner = None
        self._priority = None
        self._status = None
        self._create_user = None
        self._create_time = None
        self._start_time = None
        self._end_time = None
        self._last_instance_status = None
        self._last_instance_end_time = None
        self._last_update_time = None
        self._last_update_user = None
        self._path = None
        self._single_node_job_flag = None
        self._flink_job_info = None
        self._alarms = None
        self.discriminator = None

        self.name = name
        self.job_type = job_type
        if owner is not None:
            self.owner = owner
        if priority is not None:
            self.priority = priority
        self.status = status
        self.create_user = create_user
        self.create_time = create_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if last_instance_status is not None:
            self.last_instance_status = last_instance_status
        if last_instance_end_time is not None:
            self.last_instance_end_time = last_instance_end_time
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if last_update_user is not None:
            self.last_update_user = last_update_user
        if path is not None:
            self.path = path
        if single_node_job_flag is not None:
            self.single_node_job_flag = single_node_job_flag
        if flink_job_info is not None:
            self.flink_job_info = flink_job_info
        if alarms is not None:
            self.alarms = alarms

    @property
    def name(self):
        r"""Gets the name of this JobResult.

        作业名称

        :return: The name of this JobResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this JobResult.

        作业名称

        :param name: The name of this JobResult.
        :type name: str
        """
        self._name = name

    @property
    def job_type(self):
        r"""Gets the job_type of this JobResult.

        作业类型

        :return: The job_type of this JobResult.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this JobResult.

        作业类型

        :param job_type: The job_type of this JobResult.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def owner(self):
        r"""Gets the owner of this JobResult.

        作业责任人，长度不能超过128个字符

        :return: The owner of this JobResult.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this JobResult.

        作业责任人，长度不能超过128个字符

        :param owner: The owner of this JobResult.
        :type owner: str
        """
        self._owner = owner

    @property
    def priority(self):
        r"""Gets the priority of this JobResult.

        作业优先级，取值范围[0, 2]，默认值是0。0代表高优先级，1代表中优先级，2代表低优先级

        :return: The priority of this JobResult.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this JobResult.

        作业优先级，取值范围[0, 2]，默认值是0。0代表高优先级，1代表中优先级，2代表低优先级

        :param priority: The priority of this JobResult.
        :type priority: int
        """
        self._priority = priority

    @property
    def status(self):
        r"""Gets the status of this JobResult.

        :return: The status of this JobResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this JobResult.

        :param status: The status of this JobResult.
        :type status: str
        """
        self._status = status

    @property
    def create_user(self):
        r"""Gets the create_user of this JobResult.

        作业的创建者

        :return: The create_user of this JobResult.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this JobResult.

        作业的创建者

        :param create_user: The create_user of this JobResult.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def create_time(self):
        r"""Gets the create_time of this JobResult.

        作业的创建时间

        :return: The create_time of this JobResult.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this JobResult.

        作业的创建时间

        :param create_time: The create_time of this JobResult.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def start_time(self):
        r"""Gets the start_time of this JobResult.

        作业的启动时间

        :return: The start_time of this JobResult.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this JobResult.

        作业的启动时间

        :param start_time: The start_time of this JobResult.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this JobResult.

        作业配置的结束时间

        :return: The end_time of this JobResult.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this JobResult.

        作业配置的结束时间

        :param end_time: The end_time of this JobResult.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def last_instance_status(self):
        r"""Gets the last_instance_status of this JobResult.

        作业最近一次运行实例状态，当jobType为BATCH时才有本字段

        :return: The last_instance_status of this JobResult.
        :rtype: str
        """
        return self._last_instance_status

    @last_instance_status.setter
    def last_instance_status(self, last_instance_status):
        r"""Sets the last_instance_status of this JobResult.

        作业最近一次运行实例状态，当jobType为BATCH时才有本字段

        :param last_instance_status: The last_instance_status of this JobResult.
        :type last_instance_status: str
        """
        self._last_instance_status = last_instance_status

    @property
    def last_instance_end_time(self):
        r"""Gets the last_instance_end_time of this JobResult.

        作业最近一次运行实例运行结束时间，当jobType为BATCH时才有本字段

        :return: The last_instance_end_time of this JobResult.
        :rtype: int
        """
        return self._last_instance_end_time

    @last_instance_end_time.setter
    def last_instance_end_time(self, last_instance_end_time):
        r"""Sets the last_instance_end_time of this JobResult.

        作业最近一次运行实例运行结束时间，当jobType为BATCH时才有本字段

        :param last_instance_end_time: The last_instance_end_time of this JobResult.
        :type last_instance_end_time: int
        """
        self._last_instance_end_time = last_instance_end_time

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this JobResult.

        作业最后一次更新时间

        :return: The last_update_time of this JobResult.
        :rtype: int
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this JobResult.

        作业最后一次更新时间

        :param last_update_time: The last_update_time of this JobResult.
        :type last_update_time: int
        """
        self._last_update_time = last_update_time

    @property
    def last_update_user(self):
        r"""Gets the last_update_user of this JobResult.

        作业最后一次更新用户

        :return: The last_update_user of this JobResult.
        :rtype: str
        """
        return self._last_update_user

    @last_update_user.setter
    def last_update_user(self, last_update_user):
        r"""Sets the last_update_user of this JobResult.

        作业最后一次更新用户

        :param last_update_user: The last_update_user of this JobResult.
        :type last_update_user: str
        """
        self._last_update_user = last_update_user

    @property
    def path(self):
        r"""Gets the path of this JobResult.

        作业的路径

        :return: The path of this JobResult.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this JobResult.

        作业的路径

        :param path: The path of this JobResult.
        :type path: str
        """
        self._path = path

    @property
    def single_node_job_flag(self):
        r"""Gets the single_node_job_flag of this JobResult.

        作业是否为单任务作业

        :return: The single_node_job_flag of this JobResult.
        :rtype: bool
        """
        return self._single_node_job_flag

    @single_node_job_flag.setter
    def single_node_job_flag(self, single_node_job_flag):
        r"""Sets the single_node_job_flag of this JobResult.

        作业是否为单任务作业

        :param single_node_job_flag: The single_node_job_flag of this JobResult.
        :type single_node_job_flag: bool
        """
        self._single_node_job_flag = single_node_job_flag

    @property
    def flink_job_info(self):
        r"""Gets the flink_job_info of this JobResult.

        flink作业信息

        :return: The flink_job_info of this JobResult.
        :rtype: str
        """
        return self._flink_job_info

    @flink_job_info.setter
    def flink_job_info(self, flink_job_info):
        r"""Sets the flink_job_info of this JobResult.

        flink作业信息

        :param flink_job_info: The flink_job_info of this JobResult.
        :type flink_job_info: str
        """
        self._flink_job_info = flink_job_info

    @property
    def alarms(self):
        r"""Gets the alarms of this JobResult.

        作业监控告警信息

        :return: The alarms of this JobResult.
        :rtype: list[:class:`huaweicloudsdkdgc.v1.JobAlarm`]
        """
        return self._alarms

    @alarms.setter
    def alarms(self, alarms):
        r"""Sets the alarms of this JobResult.

        作业监控告警信息

        :param alarms: The alarms of this JobResult.
        :type alarms: list[:class:`huaweicloudsdkdgc.v1.JobAlarm`]
        """
        self._alarms = alarms

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
        if not isinstance(other, JobResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
