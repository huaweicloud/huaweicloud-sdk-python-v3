# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Setting:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workers': 'int',
        'batch_size': 'int',
        'batch_delay_ms': 'int',
        'queue_type': 'str',
        'queue_check_point_writes': 'int',
        'queue_max_bytes_mb': 'int'
    }

    attribute_map = {
        'workers': 'workers',
        'batch_size': 'batchSize',
        'batch_delay_ms': 'batchDelayMs',
        'queue_type': 'queueType',
        'queue_check_point_writes': 'queueCheckPointWrites',
        'queue_max_bytes_mb': 'queueMaxBytesMb'
    }

    def __init__(self, workers=None, batch_size=None, batch_delay_ms=None, queue_type=None, queue_check_point_writes=None, queue_max_bytes_mb=None):
        """Setting

        The model defined in huaweicloud sdk

        :param workers: 并行执行管道的Filters+Outputs阶段的工作线程数，默认值为CPU核数。
        :type workers: int
        :param batch_size: 单个工作线程在尝试执行其Filters和Outputs之前将从inputs收集的最大事件数，该值较大通常更有效，但会增加内存开销，默认为125。
        :type batch_size: int
        :param batch_delay_ms: 每个event被pipeline调度等待的最小时间。 单位毫秒。
        :type batch_delay_ms: int
        :param queue_type: 用于事件缓冲的内部队列模型。memory 为基于内存的传统队列，persisted为基于磁盘的ACKed持久化队列，默认值为memory。
        :type queue_type: str
        :param queue_check_point_writes: 如果使用持久化队列，则表示强制执行检查点之前写入的最大事件数，默认值为1024。
        :type queue_check_point_writes: int
        :param queue_max_bytes_mb: 如果使用持久化队列，则表示持久化队列的总容量（以兆字节MB为单位），确保磁盘的容量大于该值，默认值为1024。
        :type queue_max_bytes_mb: int
        """
        
        

        self._workers = None
        self._batch_size = None
        self._batch_delay_ms = None
        self._queue_type = None
        self._queue_check_point_writes = None
        self._queue_max_bytes_mb = None
        self.discriminator = None

        if workers is not None:
            self.workers = workers
        if batch_size is not None:
            self.batch_size = batch_size
        if batch_delay_ms is not None:
            self.batch_delay_ms = batch_delay_ms
        self.queue_type = queue_type
        if queue_check_point_writes is not None:
            self.queue_check_point_writes = queue_check_point_writes
        if queue_max_bytes_mb is not None:
            self.queue_max_bytes_mb = queue_max_bytes_mb

    @property
    def workers(self):
        """Gets the workers of this Setting.

        并行执行管道的Filters+Outputs阶段的工作线程数，默认值为CPU核数。

        :return: The workers of this Setting.
        :rtype: int
        """
        return self._workers

    @workers.setter
    def workers(self, workers):
        """Sets the workers of this Setting.

        并行执行管道的Filters+Outputs阶段的工作线程数，默认值为CPU核数。

        :param workers: The workers of this Setting.
        :type workers: int
        """
        self._workers = workers

    @property
    def batch_size(self):
        """Gets the batch_size of this Setting.

        单个工作线程在尝试执行其Filters和Outputs之前将从inputs收集的最大事件数，该值较大通常更有效，但会增加内存开销，默认为125。

        :return: The batch_size of this Setting.
        :rtype: int
        """
        return self._batch_size

    @batch_size.setter
    def batch_size(self, batch_size):
        """Sets the batch_size of this Setting.

        单个工作线程在尝试执行其Filters和Outputs之前将从inputs收集的最大事件数，该值较大通常更有效，但会增加内存开销，默认为125。

        :param batch_size: The batch_size of this Setting.
        :type batch_size: int
        """
        self._batch_size = batch_size

    @property
    def batch_delay_ms(self):
        """Gets the batch_delay_ms of this Setting.

        每个event被pipeline调度等待的最小时间。 单位毫秒。

        :return: The batch_delay_ms of this Setting.
        :rtype: int
        """
        return self._batch_delay_ms

    @batch_delay_ms.setter
    def batch_delay_ms(self, batch_delay_ms):
        """Sets the batch_delay_ms of this Setting.

        每个event被pipeline调度等待的最小时间。 单位毫秒。

        :param batch_delay_ms: The batch_delay_ms of this Setting.
        :type batch_delay_ms: int
        """
        self._batch_delay_ms = batch_delay_ms

    @property
    def queue_type(self):
        """Gets the queue_type of this Setting.

        用于事件缓冲的内部队列模型。memory 为基于内存的传统队列，persisted为基于磁盘的ACKed持久化队列，默认值为memory。

        :return: The queue_type of this Setting.
        :rtype: str
        """
        return self._queue_type

    @queue_type.setter
    def queue_type(self, queue_type):
        """Sets the queue_type of this Setting.

        用于事件缓冲的内部队列模型。memory 为基于内存的传统队列，persisted为基于磁盘的ACKed持久化队列，默认值为memory。

        :param queue_type: The queue_type of this Setting.
        :type queue_type: str
        """
        self._queue_type = queue_type

    @property
    def queue_check_point_writes(self):
        """Gets the queue_check_point_writes of this Setting.

        如果使用持久化队列，则表示强制执行检查点之前写入的最大事件数，默认值为1024。

        :return: The queue_check_point_writes of this Setting.
        :rtype: int
        """
        return self._queue_check_point_writes

    @queue_check_point_writes.setter
    def queue_check_point_writes(self, queue_check_point_writes):
        """Sets the queue_check_point_writes of this Setting.

        如果使用持久化队列，则表示强制执行检查点之前写入的最大事件数，默认值为1024。

        :param queue_check_point_writes: The queue_check_point_writes of this Setting.
        :type queue_check_point_writes: int
        """
        self._queue_check_point_writes = queue_check_point_writes

    @property
    def queue_max_bytes_mb(self):
        """Gets the queue_max_bytes_mb of this Setting.

        如果使用持久化队列，则表示持久化队列的总容量（以兆字节MB为单位），确保磁盘的容量大于该值，默认值为1024。

        :return: The queue_max_bytes_mb of this Setting.
        :rtype: int
        """
        return self._queue_max_bytes_mb

    @queue_max_bytes_mb.setter
    def queue_max_bytes_mb(self, queue_max_bytes_mb):
        """Sets the queue_max_bytes_mb of this Setting.

        如果使用持久化队列，则表示持久化队列的总容量（以兆字节MB为单位），确保磁盘的容量大于该值，默认值为1024。

        :param queue_max_bytes_mb: The queue_max_bytes_mb of this Setting.
        :type queue_max_bytes_mb: int
        """
        self._queue_max_bytes_mb = queue_max_bytes_mb

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
        if not isinstance(other, Setting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
