# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryMetricResult:

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
        'node_id': 'str',
        'time_stamp': 'date',
        'cpu_util': 'str',
        'mem_util': 'str',
        'network_incoming_bytes_rate': 'str',
        'network_outgoing_bytes_rate': 'str',
        'disk_read_bytes_rate': 'str',
        'disk_write_bytes_rate': 'str',
        'apply_rows_rate': 'str',
        'apply_transactions_rate': 'str',
        'apply_ddl_rate': 'str',
        'apply_average_execute_time': 'str',
        'apply_average_commit_time': 'str',
        'apply_current_state': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'node_id': 'node_id',
        'time_stamp': 'time_stamp',
        'cpu_util': 'cpu_util',
        'mem_util': 'mem_util',
        'network_incoming_bytes_rate': 'network_incoming_bytes_rate',
        'network_outgoing_bytes_rate': 'network_outgoing_bytes_rate',
        'disk_read_bytes_rate': 'disk_read_bytes_rate',
        'disk_write_bytes_rate': 'disk_write_bytes_rate',
        'apply_rows_rate': 'apply_rows_rate',
        'apply_transactions_rate': 'apply_transactions_rate',
        'apply_ddl_rate': 'apply_ddl_rate',
        'apply_average_execute_time': 'apply_average_execute_time',
        'apply_average_commit_time': 'apply_average_commit_time',
        'apply_current_state': 'apply_current_state'
    }

    def __init__(self, job_id=None, node_id=None, time_stamp=None, cpu_util=None, mem_util=None, network_incoming_bytes_rate=None, network_outgoing_bytes_rate=None, disk_read_bytes_rate=None, disk_write_bytes_rate=None, apply_rows_rate=None, apply_transactions_rate=None, apply_ddl_rate=None, apply_average_execute_time=None, apply_average_commit_time=None, apply_current_state=None):
        """QueryMetricResult

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param node_id: 实例ID。
        :type node_id: str
        :param time_stamp: 上报时间。
        :type time_stamp: date
        :param cpu_util: CPU使用率。
        :type cpu_util: str
        :param mem_util: 内存使用率。
        :type mem_util: str
        :param network_incoming_bytes_rate: 网络输入吞吐量。
        :type network_incoming_bytes_rate: str
        :param network_outgoing_bytes_rate: 网络输出吞吐量。
        :type network_outgoing_bytes_rate: str
        :param disk_read_bytes_rate: 磁盘读吞吐量。
        :type disk_read_bytes_rate: str
        :param disk_write_bytes_rate: 磁盘写吞吐量。
        :type disk_write_bytes_rate: str
        :param apply_rows_rate: 写目标库频率。
        :type apply_rows_rate: str
        :param apply_transactions_rate: DML TPS。
        :type apply_transactions_rate: str
        :param apply_ddl_rate: DDL TPS。
        :type apply_ddl_rate: str
        :param apply_average_execute_time: 事务平均执行时间。
        :type apply_average_execute_time: str
        :param apply_average_commit_time: 事务平均提交时间。
        :type apply_average_commit_time: str
        :param apply_current_state: 同步状态。
        :type apply_current_state: str
        """
        
        

        self._job_id = None
        self._node_id = None
        self._time_stamp = None
        self._cpu_util = None
        self._mem_util = None
        self._network_incoming_bytes_rate = None
        self._network_outgoing_bytes_rate = None
        self._disk_read_bytes_rate = None
        self._disk_write_bytes_rate = None
        self._apply_rows_rate = None
        self._apply_transactions_rate = None
        self._apply_ddl_rate = None
        self._apply_average_execute_time = None
        self._apply_average_commit_time = None
        self._apply_current_state = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if node_id is not None:
            self.node_id = node_id
        if time_stamp is not None:
            self.time_stamp = time_stamp
        if cpu_util is not None:
            self.cpu_util = cpu_util
        if mem_util is not None:
            self.mem_util = mem_util
        if network_incoming_bytes_rate is not None:
            self.network_incoming_bytes_rate = network_incoming_bytes_rate
        if network_outgoing_bytes_rate is not None:
            self.network_outgoing_bytes_rate = network_outgoing_bytes_rate
        if disk_read_bytes_rate is not None:
            self.disk_read_bytes_rate = disk_read_bytes_rate
        if disk_write_bytes_rate is not None:
            self.disk_write_bytes_rate = disk_write_bytes_rate
        if apply_rows_rate is not None:
            self.apply_rows_rate = apply_rows_rate
        if apply_transactions_rate is not None:
            self.apply_transactions_rate = apply_transactions_rate
        if apply_ddl_rate is not None:
            self.apply_ddl_rate = apply_ddl_rate
        if apply_average_execute_time is not None:
            self.apply_average_execute_time = apply_average_execute_time
        if apply_average_commit_time is not None:
            self.apply_average_commit_time = apply_average_commit_time
        if apply_current_state is not None:
            self.apply_current_state = apply_current_state

    @property
    def job_id(self):
        """Gets the job_id of this QueryMetricResult.

        任务ID。

        :return: The job_id of this QueryMetricResult.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this QueryMetricResult.

        任务ID。

        :param job_id: The job_id of this QueryMetricResult.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def node_id(self):
        """Gets the node_id of this QueryMetricResult.

        实例ID。

        :return: The node_id of this QueryMetricResult.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this QueryMetricResult.

        实例ID。

        :param node_id: The node_id of this QueryMetricResult.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def time_stamp(self):
        """Gets the time_stamp of this QueryMetricResult.

        上报时间。

        :return: The time_stamp of this QueryMetricResult.
        :rtype: date
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this QueryMetricResult.

        上报时间。

        :param time_stamp: The time_stamp of this QueryMetricResult.
        :type time_stamp: date
        """
        self._time_stamp = time_stamp

    @property
    def cpu_util(self):
        """Gets the cpu_util of this QueryMetricResult.

        CPU使用率。

        :return: The cpu_util of this QueryMetricResult.
        :rtype: str
        """
        return self._cpu_util

    @cpu_util.setter
    def cpu_util(self, cpu_util):
        """Sets the cpu_util of this QueryMetricResult.

        CPU使用率。

        :param cpu_util: The cpu_util of this QueryMetricResult.
        :type cpu_util: str
        """
        self._cpu_util = cpu_util

    @property
    def mem_util(self):
        """Gets the mem_util of this QueryMetricResult.

        内存使用率。

        :return: The mem_util of this QueryMetricResult.
        :rtype: str
        """
        return self._mem_util

    @mem_util.setter
    def mem_util(self, mem_util):
        """Sets the mem_util of this QueryMetricResult.

        内存使用率。

        :param mem_util: The mem_util of this QueryMetricResult.
        :type mem_util: str
        """
        self._mem_util = mem_util

    @property
    def network_incoming_bytes_rate(self):
        """Gets the network_incoming_bytes_rate of this QueryMetricResult.

        网络输入吞吐量。

        :return: The network_incoming_bytes_rate of this QueryMetricResult.
        :rtype: str
        """
        return self._network_incoming_bytes_rate

    @network_incoming_bytes_rate.setter
    def network_incoming_bytes_rate(self, network_incoming_bytes_rate):
        """Sets the network_incoming_bytes_rate of this QueryMetricResult.

        网络输入吞吐量。

        :param network_incoming_bytes_rate: The network_incoming_bytes_rate of this QueryMetricResult.
        :type network_incoming_bytes_rate: str
        """
        self._network_incoming_bytes_rate = network_incoming_bytes_rate

    @property
    def network_outgoing_bytes_rate(self):
        """Gets the network_outgoing_bytes_rate of this QueryMetricResult.

        网络输出吞吐量。

        :return: The network_outgoing_bytes_rate of this QueryMetricResult.
        :rtype: str
        """
        return self._network_outgoing_bytes_rate

    @network_outgoing_bytes_rate.setter
    def network_outgoing_bytes_rate(self, network_outgoing_bytes_rate):
        """Sets the network_outgoing_bytes_rate of this QueryMetricResult.

        网络输出吞吐量。

        :param network_outgoing_bytes_rate: The network_outgoing_bytes_rate of this QueryMetricResult.
        :type network_outgoing_bytes_rate: str
        """
        self._network_outgoing_bytes_rate = network_outgoing_bytes_rate

    @property
    def disk_read_bytes_rate(self):
        """Gets the disk_read_bytes_rate of this QueryMetricResult.

        磁盘读吞吐量。

        :return: The disk_read_bytes_rate of this QueryMetricResult.
        :rtype: str
        """
        return self._disk_read_bytes_rate

    @disk_read_bytes_rate.setter
    def disk_read_bytes_rate(self, disk_read_bytes_rate):
        """Sets the disk_read_bytes_rate of this QueryMetricResult.

        磁盘读吞吐量。

        :param disk_read_bytes_rate: The disk_read_bytes_rate of this QueryMetricResult.
        :type disk_read_bytes_rate: str
        """
        self._disk_read_bytes_rate = disk_read_bytes_rate

    @property
    def disk_write_bytes_rate(self):
        """Gets the disk_write_bytes_rate of this QueryMetricResult.

        磁盘写吞吐量。

        :return: The disk_write_bytes_rate of this QueryMetricResult.
        :rtype: str
        """
        return self._disk_write_bytes_rate

    @disk_write_bytes_rate.setter
    def disk_write_bytes_rate(self, disk_write_bytes_rate):
        """Sets the disk_write_bytes_rate of this QueryMetricResult.

        磁盘写吞吐量。

        :param disk_write_bytes_rate: The disk_write_bytes_rate of this QueryMetricResult.
        :type disk_write_bytes_rate: str
        """
        self._disk_write_bytes_rate = disk_write_bytes_rate

    @property
    def apply_rows_rate(self):
        """Gets the apply_rows_rate of this QueryMetricResult.

        写目标库频率。

        :return: The apply_rows_rate of this QueryMetricResult.
        :rtype: str
        """
        return self._apply_rows_rate

    @apply_rows_rate.setter
    def apply_rows_rate(self, apply_rows_rate):
        """Sets the apply_rows_rate of this QueryMetricResult.

        写目标库频率。

        :param apply_rows_rate: The apply_rows_rate of this QueryMetricResult.
        :type apply_rows_rate: str
        """
        self._apply_rows_rate = apply_rows_rate

    @property
    def apply_transactions_rate(self):
        """Gets the apply_transactions_rate of this QueryMetricResult.

        DML TPS。

        :return: The apply_transactions_rate of this QueryMetricResult.
        :rtype: str
        """
        return self._apply_transactions_rate

    @apply_transactions_rate.setter
    def apply_transactions_rate(self, apply_transactions_rate):
        """Sets the apply_transactions_rate of this QueryMetricResult.

        DML TPS。

        :param apply_transactions_rate: The apply_transactions_rate of this QueryMetricResult.
        :type apply_transactions_rate: str
        """
        self._apply_transactions_rate = apply_transactions_rate

    @property
    def apply_ddl_rate(self):
        """Gets the apply_ddl_rate of this QueryMetricResult.

        DDL TPS。

        :return: The apply_ddl_rate of this QueryMetricResult.
        :rtype: str
        """
        return self._apply_ddl_rate

    @apply_ddl_rate.setter
    def apply_ddl_rate(self, apply_ddl_rate):
        """Sets the apply_ddl_rate of this QueryMetricResult.

        DDL TPS。

        :param apply_ddl_rate: The apply_ddl_rate of this QueryMetricResult.
        :type apply_ddl_rate: str
        """
        self._apply_ddl_rate = apply_ddl_rate

    @property
    def apply_average_execute_time(self):
        """Gets the apply_average_execute_time of this QueryMetricResult.

        事务平均执行时间。

        :return: The apply_average_execute_time of this QueryMetricResult.
        :rtype: str
        """
        return self._apply_average_execute_time

    @apply_average_execute_time.setter
    def apply_average_execute_time(self, apply_average_execute_time):
        """Sets the apply_average_execute_time of this QueryMetricResult.

        事务平均执行时间。

        :param apply_average_execute_time: The apply_average_execute_time of this QueryMetricResult.
        :type apply_average_execute_time: str
        """
        self._apply_average_execute_time = apply_average_execute_time

    @property
    def apply_average_commit_time(self):
        """Gets the apply_average_commit_time of this QueryMetricResult.

        事务平均提交时间。

        :return: The apply_average_commit_time of this QueryMetricResult.
        :rtype: str
        """
        return self._apply_average_commit_time

    @apply_average_commit_time.setter
    def apply_average_commit_time(self, apply_average_commit_time):
        """Sets the apply_average_commit_time of this QueryMetricResult.

        事务平均提交时间。

        :param apply_average_commit_time: The apply_average_commit_time of this QueryMetricResult.
        :type apply_average_commit_time: str
        """
        self._apply_average_commit_time = apply_average_commit_time

    @property
    def apply_current_state(self):
        """Gets the apply_current_state of this QueryMetricResult.

        同步状态。

        :return: The apply_current_state of this QueryMetricResult.
        :rtype: str
        """
        return self._apply_current_state

    @apply_current_state.setter
    def apply_current_state(self, apply_current_state):
        """Sets the apply_current_state of this QueryMetricResult.

        同步状态。

        :param apply_current_state: The apply_current_state of this QueryMetricResult.
        :type apply_current_state: str
        """
        self._apply_current_state = apply_current_state

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
        if not isinstance(other, QueryMetricResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
