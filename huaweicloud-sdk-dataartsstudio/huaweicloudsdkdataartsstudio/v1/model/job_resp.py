# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'int',
        'create_user': 'str',
        'job_type': 'str',
        'last_instance_end_time': 'int',
        'last_instance_status': 'str',
        'last_update_time': 'int',
        'last_update_user': 'str',
        'name': 'str',
        'owner': 'str',
        'path': 'str',
        'priority': 'int',
        'single_node_job_flag': 'bool',
        'start_time': 'int',
        'status': 'str'
    }

    attribute_map = {
        'create_time': 'create_time',
        'create_user': 'create_user',
        'job_type': 'job_type',
        'last_instance_end_time': 'last_instance_end_time',
        'last_instance_status': 'last_instance_status',
        'last_update_time': 'last_update_time',
        'last_update_user': 'last_update_user',
        'name': 'name',
        'owner': 'owner',
        'path': 'path',
        'priority': 'priority',
        'single_node_job_flag': 'single_node_job_flag',
        'start_time': 'start_time',
        'status': 'status'
    }

    def __init__(self, create_time=None, create_user=None, job_type=None, last_instance_end_time=None, last_instance_status=None, last_update_time=None, last_update_user=None, name=None, owner=None, path=None, priority=None, single_node_job_flag=None, start_time=None, status=None):
        """JobResp

        The model defined in huaweicloud sdk

        :param create_time: 创建时间
        :type create_time: int
        :param create_user: 创建用户
        :type create_user: str
        :param job_type: 作业类型:  - REAL_TIME: 实时处理  - BATCH: 批处理
        :type job_type: str
        :param last_instance_end_time: 最近实例的运行结束时间
        :type last_instance_end_time: int
        :param last_instance_status: 最近实例的运行状态
        :type last_instance_status: str
        :param last_update_time: 最后更新时间
        :type last_update_time: int
        :param last_update_user: 最后修改人
        :type last_update_user: str
        :param name: 作业名称
        :type name: str
        :param owner: 责任人
        :type owner: str
        :param path: 作业目录路径
        :type path: str
        :param priority: 作业优先级
        :type priority: int
        :param single_node_job_flag: 单算子作业标识
        :type single_node_job_flag: bool
        :param start_time: 作业启动时间
        :type start_time: int
        :param status: 作业状态
        :type status: str
        """
        
        

        self._create_time = None
        self._create_user = None
        self._job_type = None
        self._last_instance_end_time = None
        self._last_instance_status = None
        self._last_update_time = None
        self._last_update_user = None
        self._name = None
        self._owner = None
        self._path = None
        self._priority = None
        self._single_node_job_flag = None
        self._start_time = None
        self._status = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if job_type is not None:
            self.job_type = job_type
        if last_instance_end_time is not None:
            self.last_instance_end_time = last_instance_end_time
        if last_instance_status is not None:
            self.last_instance_status = last_instance_status
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if last_update_user is not None:
            self.last_update_user = last_update_user
        if name is not None:
            self.name = name
        if owner is not None:
            self.owner = owner
        if path is not None:
            self.path = path
        if priority is not None:
            self.priority = priority
        if single_node_job_flag is not None:
            self.single_node_job_flag = single_node_job_flag
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status

    @property
    def create_time(self):
        """Gets the create_time of this JobResp.

        创建时间

        :return: The create_time of this JobResp.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this JobResp.

        创建时间

        :param create_time: The create_time of this JobResp.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def create_user(self):
        """Gets the create_user of this JobResp.

        创建用户

        :return: The create_user of this JobResp.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this JobResp.

        创建用户

        :param create_user: The create_user of this JobResp.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def job_type(self):
        """Gets the job_type of this JobResp.

        作业类型:  - REAL_TIME: 实时处理  - BATCH: 批处理

        :return: The job_type of this JobResp.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this JobResp.

        作业类型:  - REAL_TIME: 实时处理  - BATCH: 批处理

        :param job_type: The job_type of this JobResp.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def last_instance_end_time(self):
        """Gets the last_instance_end_time of this JobResp.

        最近实例的运行结束时间

        :return: The last_instance_end_time of this JobResp.
        :rtype: int
        """
        return self._last_instance_end_time

    @last_instance_end_time.setter
    def last_instance_end_time(self, last_instance_end_time):
        """Sets the last_instance_end_time of this JobResp.

        最近实例的运行结束时间

        :param last_instance_end_time: The last_instance_end_time of this JobResp.
        :type last_instance_end_time: int
        """
        self._last_instance_end_time = last_instance_end_time

    @property
    def last_instance_status(self):
        """Gets the last_instance_status of this JobResp.

        最近实例的运行状态

        :return: The last_instance_status of this JobResp.
        :rtype: str
        """
        return self._last_instance_status

    @last_instance_status.setter
    def last_instance_status(self, last_instance_status):
        """Sets the last_instance_status of this JobResp.

        最近实例的运行状态

        :param last_instance_status: The last_instance_status of this JobResp.
        :type last_instance_status: str
        """
        self._last_instance_status = last_instance_status

    @property
    def last_update_time(self):
        """Gets the last_update_time of this JobResp.

        最后更新时间

        :return: The last_update_time of this JobResp.
        :rtype: int
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this JobResp.

        最后更新时间

        :param last_update_time: The last_update_time of this JobResp.
        :type last_update_time: int
        """
        self._last_update_time = last_update_time

    @property
    def last_update_user(self):
        """Gets the last_update_user of this JobResp.

        最后修改人

        :return: The last_update_user of this JobResp.
        :rtype: str
        """
        return self._last_update_user

    @last_update_user.setter
    def last_update_user(self, last_update_user):
        """Sets the last_update_user of this JobResp.

        最后修改人

        :param last_update_user: The last_update_user of this JobResp.
        :type last_update_user: str
        """
        self._last_update_user = last_update_user

    @property
    def name(self):
        """Gets the name of this JobResp.

        作业名称

        :return: The name of this JobResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobResp.

        作业名称

        :param name: The name of this JobResp.
        :type name: str
        """
        self._name = name

    @property
    def owner(self):
        """Gets the owner of this JobResp.

        责任人

        :return: The owner of this JobResp.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this JobResp.

        责任人

        :param owner: The owner of this JobResp.
        :type owner: str
        """
        self._owner = owner

    @property
    def path(self):
        """Gets the path of this JobResp.

        作业目录路径

        :return: The path of this JobResp.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this JobResp.

        作业目录路径

        :param path: The path of this JobResp.
        :type path: str
        """
        self._path = path

    @property
    def priority(self):
        """Gets the priority of this JobResp.

        作业优先级

        :return: The priority of this JobResp.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this JobResp.

        作业优先级

        :param priority: The priority of this JobResp.
        :type priority: int
        """
        self._priority = priority

    @property
    def single_node_job_flag(self):
        """Gets the single_node_job_flag of this JobResp.

        单算子作业标识

        :return: The single_node_job_flag of this JobResp.
        :rtype: bool
        """
        return self._single_node_job_flag

    @single_node_job_flag.setter
    def single_node_job_flag(self, single_node_job_flag):
        """Sets the single_node_job_flag of this JobResp.

        单算子作业标识

        :param single_node_job_flag: The single_node_job_flag of this JobResp.
        :type single_node_job_flag: bool
        """
        self._single_node_job_flag = single_node_job_flag

    @property
    def start_time(self):
        """Gets the start_time of this JobResp.

        作业启动时间

        :return: The start_time of this JobResp.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this JobResp.

        作业启动时间

        :param start_time: The start_time of this JobResp.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this JobResp.

        作业状态

        :return: The status of this JobResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JobResp.

        作业状态

        :param status: The status of this JobResp.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, JobResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
