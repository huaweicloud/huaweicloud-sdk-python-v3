# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NextflowTaskResourceRequested:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'container': 'str',
        'queue': 'str',
        'cpus': 'int',
        'memory': 'str',
        'disk': 'str',
        'time': 'str'
    }

    attribute_map = {
        'container': 'container',
        'queue': 'queue',
        'cpus': 'cpus',
        'memory': 'memory',
        'disk': 'disk',
        'time': 'time'
    }

    def __init__(self, container=None, queue=None, cpus=None, memory=None, disk=None, time=None):
        r"""NextflowTaskResourceRequested

        The model defined in huaweicloud sdk

        :param container: 容器名称
        :type container: str
        :param queue: 执行队列，使用&#39;,&#39;分隔多个值
        :type queue: str
        :param cpus: 指定task执行需要的cpu数量
        :type cpus: int
        :param memory: 指定task执行需要的内存大小
        :type memory: str
        :param disk: 指定task执行需要的磁盘大小
        :type disk: str
        :param time: 指定task执行需要的时间
        :type time: str
        """
        
        

        self._container = None
        self._queue = None
        self._cpus = None
        self._memory = None
        self._disk = None
        self._time = None
        self.discriminator = None

        if container is not None:
            self.container = container
        if queue is not None:
            self.queue = queue
        if cpus is not None:
            self.cpus = cpus
        if memory is not None:
            self.memory = memory
        if disk is not None:
            self.disk = disk
        if time is not None:
            self.time = time

    @property
    def container(self):
        r"""Gets the container of this NextflowTaskResourceRequested.

        容器名称

        :return: The container of this NextflowTaskResourceRequested.
        :rtype: str
        """
        return self._container

    @container.setter
    def container(self, container):
        r"""Sets the container of this NextflowTaskResourceRequested.

        容器名称

        :param container: The container of this NextflowTaskResourceRequested.
        :type container: str
        """
        self._container = container

    @property
    def queue(self):
        r"""Gets the queue of this NextflowTaskResourceRequested.

        执行队列，使用','分隔多个值

        :return: The queue of this NextflowTaskResourceRequested.
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        r"""Sets the queue of this NextflowTaskResourceRequested.

        执行队列，使用','分隔多个值

        :param queue: The queue of this NextflowTaskResourceRequested.
        :type queue: str
        """
        self._queue = queue

    @property
    def cpus(self):
        r"""Gets the cpus of this NextflowTaskResourceRequested.

        指定task执行需要的cpu数量

        :return: The cpus of this NextflowTaskResourceRequested.
        :rtype: int
        """
        return self._cpus

    @cpus.setter
    def cpus(self, cpus):
        r"""Sets the cpus of this NextflowTaskResourceRequested.

        指定task执行需要的cpu数量

        :param cpus: The cpus of this NextflowTaskResourceRequested.
        :type cpus: int
        """
        self._cpus = cpus

    @property
    def memory(self):
        r"""Gets the memory of this NextflowTaskResourceRequested.

        指定task执行需要的内存大小

        :return: The memory of this NextflowTaskResourceRequested.
        :rtype: str
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this NextflowTaskResourceRequested.

        指定task执行需要的内存大小

        :param memory: The memory of this NextflowTaskResourceRequested.
        :type memory: str
        """
        self._memory = memory

    @property
    def disk(self):
        r"""Gets the disk of this NextflowTaskResourceRequested.

        指定task执行需要的磁盘大小

        :return: The disk of this NextflowTaskResourceRequested.
        :rtype: str
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        r"""Sets the disk of this NextflowTaskResourceRequested.

        指定task执行需要的磁盘大小

        :param disk: The disk of this NextflowTaskResourceRequested.
        :type disk: str
        """
        self._disk = disk

    @property
    def time(self):
        r"""Gets the time of this NextflowTaskResourceRequested.

        指定task执行需要的时间

        :return: The time of this NextflowTaskResourceRequested.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this NextflowTaskResourceRequested.

        指定task执行需要的时间

        :param time: The time of this NextflowTaskResourceRequested.
        :type time: str
        """
        self._time = time

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
        if not isinstance(other, NextflowTaskResourceRequested):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
