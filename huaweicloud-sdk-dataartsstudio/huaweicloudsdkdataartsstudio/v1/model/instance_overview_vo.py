# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceOverviewVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'task_id': 'int',
        'task_type': 'str',
        'run_status': 'str',
        'notify_status': 'str',
        'start_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'task_id': 'task_id',
        'task_type': 'task_type',
        'run_status': 'run_status',
        'notify_status': 'notify_status',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, id=None, name=None, task_id=None, task_type=None, run_status=None, notify_status=None, start_time=None, end_time=None):
        """InstanceOverviewVo

        The model defined in huaweicloud sdk

        :param id: id
        :type id: int
        :param name: 名称
        :type name: str
        :param task_id: task id
        :type task_id: int
        :param task_type: QUALITY_TASK:质量作业,CONSISTENCY_TASK:对账作业
        :type task_type: str
        :param run_status: RUNNING:运行中,FAILED:失败,ALARMING:报警,SUCCESS:正常
        :type run_status: str
        :param notify_status: NOT_TRIGGERED:未触发,SUCCESS:成功,FAILED:失败
        :type notify_status: str
        :param start_time: 开始时间
        :type start_time: int
        :param end_time: 结束时间
        :type end_time: int
        """
        
        

        self._id = None
        self._name = None
        self._task_id = None
        self._task_type = None
        self._run_status = None
        self._notify_status = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if task_id is not None:
            self.task_id = task_id
        if task_type is not None:
            self.task_type = task_type
        if run_status is not None:
            self.run_status = run_status
        if notify_status is not None:
            self.notify_status = notify_status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def id(self):
        """Gets the id of this InstanceOverviewVo.

        id

        :return: The id of this InstanceOverviewVo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InstanceOverviewVo.

        id

        :param id: The id of this InstanceOverviewVo.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this InstanceOverviewVo.

        名称

        :return: The name of this InstanceOverviewVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InstanceOverviewVo.

        名称

        :param name: The name of this InstanceOverviewVo.
        :type name: str
        """
        self._name = name

    @property
    def task_id(self):
        """Gets the task_id of this InstanceOverviewVo.

        task id

        :return: The task_id of this InstanceOverviewVo.
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this InstanceOverviewVo.

        task id

        :param task_id: The task_id of this InstanceOverviewVo.
        :type task_id: int
        """
        self._task_id = task_id

    @property
    def task_type(self):
        """Gets the task_type of this InstanceOverviewVo.

        QUALITY_TASK:质量作业,CONSISTENCY_TASK:对账作业

        :return: The task_type of this InstanceOverviewVo.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this InstanceOverviewVo.

        QUALITY_TASK:质量作业,CONSISTENCY_TASK:对账作业

        :param task_type: The task_type of this InstanceOverviewVo.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def run_status(self):
        """Gets the run_status of this InstanceOverviewVo.

        RUNNING:运行中,FAILED:失败,ALARMING:报警,SUCCESS:正常

        :return: The run_status of this InstanceOverviewVo.
        :rtype: str
        """
        return self._run_status

    @run_status.setter
    def run_status(self, run_status):
        """Sets the run_status of this InstanceOverviewVo.

        RUNNING:运行中,FAILED:失败,ALARMING:报警,SUCCESS:正常

        :param run_status: The run_status of this InstanceOverviewVo.
        :type run_status: str
        """
        self._run_status = run_status

    @property
    def notify_status(self):
        """Gets the notify_status of this InstanceOverviewVo.

        NOT_TRIGGERED:未触发,SUCCESS:成功,FAILED:失败

        :return: The notify_status of this InstanceOverviewVo.
        :rtype: str
        """
        return self._notify_status

    @notify_status.setter
    def notify_status(self, notify_status):
        """Sets the notify_status of this InstanceOverviewVo.

        NOT_TRIGGERED:未触发,SUCCESS:成功,FAILED:失败

        :param notify_status: The notify_status of this InstanceOverviewVo.
        :type notify_status: str
        """
        self._notify_status = notify_status

    @property
    def start_time(self):
        """Gets the start_time of this InstanceOverviewVo.

        开始时间

        :return: The start_time of this InstanceOverviewVo.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this InstanceOverviewVo.

        开始时间

        :param start_time: The start_time of this InstanceOverviewVo.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this InstanceOverviewVo.

        结束时间

        :return: The end_time of this InstanceOverviewVo.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this InstanceOverviewVo.

        结束时间

        :param end_time: The end_time of this InstanceOverviewVo.
        :type end_time: int
        """
        self._end_time = end_time

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
        if not isinstance(other, InstanceOverviewVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
