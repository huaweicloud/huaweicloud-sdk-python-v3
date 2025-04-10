# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NextflowTaskListDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'process': 'str',
        'tag': 'str',
        'hash': 'str',
        'status': 'str',
        'container': 'str',
        'pod_name': 'str',
        'submit': 'str',
        'complete': 'str',
        'duration': 'int',
        'realtime': 'int',
        'cpu_percent': 'float',
        'mem_percent': 'float'
    }

    attribute_map = {
        'task_id': 'task_id',
        'process': 'process',
        'tag': 'tag',
        'hash': 'hash',
        'status': 'status',
        'container': 'container',
        'pod_name': 'pod_name',
        'submit': 'submit',
        'complete': 'complete',
        'duration': 'duration',
        'realtime': 'realtime',
        'cpu_percent': 'cpu_percent',
        'mem_percent': 'mem_percent'
    }

    def __init__(self, task_id=None, process=None, tag=None, hash=None, status=None, container=None, pod_name=None, submit=None, complete=None, duration=None, realtime=None, cpu_percent=None, mem_percent=None):
        r"""NextflowTaskListDto

        The model defined in huaweicloud sdk

        :param task_id: 子任务id
        :type task_id: str
        :param process: 流程名称
        :type process: str
        :param tag: 子任务标识符
        :type tag: str
        :param hash: 哈希值
        :type hash: str
        :param status: 子任务状态
        :type status: str
        :param container: 容器名称
        :type container: str
        :param pod_name: pod名称
        :type pod_name: str
        :param submit: 提交时间
        :type submit: str
        :param complete: 完成时间
        :type complete: str
        :param duration: 总时间
        :type duration: int
        :param realtime: 实际运行时间
        :type realtime: int
        :param cpu_percent: cpu使用率
        :type cpu_percent: float
        :param mem_percent: 内存使用率
        :type mem_percent: float
        """
        
        

        self._task_id = None
        self._process = None
        self._tag = None
        self._hash = None
        self._status = None
        self._container = None
        self._pod_name = None
        self._submit = None
        self._complete = None
        self._duration = None
        self._realtime = None
        self._cpu_percent = None
        self._mem_percent = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if process is not None:
            self.process = process
        if tag is not None:
            self.tag = tag
        if hash is not None:
            self.hash = hash
        if status is not None:
            self.status = status
        if container is not None:
            self.container = container
        if pod_name is not None:
            self.pod_name = pod_name
        if submit is not None:
            self.submit = submit
        if complete is not None:
            self.complete = complete
        if duration is not None:
            self.duration = duration
        if realtime is not None:
            self.realtime = realtime
        if cpu_percent is not None:
            self.cpu_percent = cpu_percent
        if mem_percent is not None:
            self.mem_percent = mem_percent

    @property
    def task_id(self):
        r"""Gets the task_id of this NextflowTaskListDto.

        子任务id

        :return: The task_id of this NextflowTaskListDto.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this NextflowTaskListDto.

        子任务id

        :param task_id: The task_id of this NextflowTaskListDto.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def process(self):
        r"""Gets the process of this NextflowTaskListDto.

        流程名称

        :return: The process of this NextflowTaskListDto.
        :rtype: str
        """
        return self._process

    @process.setter
    def process(self, process):
        r"""Sets the process of this NextflowTaskListDto.

        流程名称

        :param process: The process of this NextflowTaskListDto.
        :type process: str
        """
        self._process = process

    @property
    def tag(self):
        r"""Gets the tag of this NextflowTaskListDto.

        子任务标识符

        :return: The tag of this NextflowTaskListDto.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this NextflowTaskListDto.

        子任务标识符

        :param tag: The tag of this NextflowTaskListDto.
        :type tag: str
        """
        self._tag = tag

    @property
    def hash(self):
        r"""Gets the hash of this NextflowTaskListDto.

        哈希值

        :return: The hash of this NextflowTaskListDto.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        r"""Sets the hash of this NextflowTaskListDto.

        哈希值

        :param hash: The hash of this NextflowTaskListDto.
        :type hash: str
        """
        self._hash = hash

    @property
    def status(self):
        r"""Gets the status of this NextflowTaskListDto.

        子任务状态

        :return: The status of this NextflowTaskListDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this NextflowTaskListDto.

        子任务状态

        :param status: The status of this NextflowTaskListDto.
        :type status: str
        """
        self._status = status

    @property
    def container(self):
        r"""Gets the container of this NextflowTaskListDto.

        容器名称

        :return: The container of this NextflowTaskListDto.
        :rtype: str
        """
        return self._container

    @container.setter
    def container(self, container):
        r"""Sets the container of this NextflowTaskListDto.

        容器名称

        :param container: The container of this NextflowTaskListDto.
        :type container: str
        """
        self._container = container

    @property
    def pod_name(self):
        r"""Gets the pod_name of this NextflowTaskListDto.

        pod名称

        :return: The pod_name of this NextflowTaskListDto.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        r"""Sets the pod_name of this NextflowTaskListDto.

        pod名称

        :param pod_name: The pod_name of this NextflowTaskListDto.
        :type pod_name: str
        """
        self._pod_name = pod_name

    @property
    def submit(self):
        r"""Gets the submit of this NextflowTaskListDto.

        提交时间

        :return: The submit of this NextflowTaskListDto.
        :rtype: str
        """
        return self._submit

    @submit.setter
    def submit(self, submit):
        r"""Sets the submit of this NextflowTaskListDto.

        提交时间

        :param submit: The submit of this NextflowTaskListDto.
        :type submit: str
        """
        self._submit = submit

    @property
    def complete(self):
        r"""Gets the complete of this NextflowTaskListDto.

        完成时间

        :return: The complete of this NextflowTaskListDto.
        :rtype: str
        """
        return self._complete

    @complete.setter
    def complete(self, complete):
        r"""Sets the complete of this NextflowTaskListDto.

        完成时间

        :param complete: The complete of this NextflowTaskListDto.
        :type complete: str
        """
        self._complete = complete

    @property
    def duration(self):
        r"""Gets the duration of this NextflowTaskListDto.

        总时间

        :return: The duration of this NextflowTaskListDto.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this NextflowTaskListDto.

        总时间

        :param duration: The duration of this NextflowTaskListDto.
        :type duration: int
        """
        self._duration = duration

    @property
    def realtime(self):
        r"""Gets the realtime of this NextflowTaskListDto.

        实际运行时间

        :return: The realtime of this NextflowTaskListDto.
        :rtype: int
        """
        return self._realtime

    @realtime.setter
    def realtime(self, realtime):
        r"""Sets the realtime of this NextflowTaskListDto.

        实际运行时间

        :param realtime: The realtime of this NextflowTaskListDto.
        :type realtime: int
        """
        self._realtime = realtime

    @property
    def cpu_percent(self):
        r"""Gets the cpu_percent of this NextflowTaskListDto.

        cpu使用率

        :return: The cpu_percent of this NextflowTaskListDto.
        :rtype: float
        """
        return self._cpu_percent

    @cpu_percent.setter
    def cpu_percent(self, cpu_percent):
        r"""Sets the cpu_percent of this NextflowTaskListDto.

        cpu使用率

        :param cpu_percent: The cpu_percent of this NextflowTaskListDto.
        :type cpu_percent: float
        """
        self._cpu_percent = cpu_percent

    @property
    def mem_percent(self):
        r"""Gets the mem_percent of this NextflowTaskListDto.

        内存使用率

        :return: The mem_percent of this NextflowTaskListDto.
        :rtype: float
        """
        return self._mem_percent

    @mem_percent.setter
    def mem_percent(self, mem_percent):
        r"""Sets the mem_percent of this NextflowTaskListDto.

        内存使用率

        :param mem_percent: The mem_percent of this NextflowTaskListDto.
        :type mem_percent: float
        """
        self._mem_percent = mem_percent

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
        if not isinstance(other, NextflowTaskListDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
