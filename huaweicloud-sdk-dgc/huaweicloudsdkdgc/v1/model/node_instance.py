# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_name': 'str',
        'status': 'str',
        'queue': 'str',
        'plan_time': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'type': 'str',
        'retry_times': 'int',
        'instance_id': 'int',
        'input_row_count': 'int',
        'speed': 'float',
        'log_path': 'str'
    }

    attribute_map = {
        'node_name': 'nodeName',
        'status': 'status',
        'queue': 'queue',
        'plan_time': 'planTime',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'type': 'type',
        'retry_times': 'retryTimes',
        'instance_id': 'instanceId',
        'input_row_count': 'inputRowCount',
        'speed': 'speed',
        'log_path': 'logPath'
    }

    def __init__(self, node_name=None, status=None, queue=None, plan_time=None, start_time=None, end_time=None, type=None, retry_times=None, instance_id=None, input_row_count=None, speed=None, log_path=None):
        r"""NodeInstance

        The model defined in huaweicloud sdk

        :param node_name: 节点名称
        :type node_name: str
        :param status: 节点状态： - waiting：等待运行 - running：运行中 - success：运行成功 - fail： 运行失败 - skip：跳过 - pause： 暂停 - manual-stop：取消
        :type status: str
        :param queue: DLI资源队列名称。在返回响应中，仅DLI SQL或者DLI SPARK算子会返回DLI队列名称。
        :type queue: str
        :param plan_time: 作业实例计划执行时间
        :type plan_time: int
        :param start_time: 节点实际执行开始时间
        :type start_time: int
        :param end_time: 节点实际执行结束时间
        :type end_time: int
        :param type: 节点类型： - HiveSQL：执行Hive SQL脚本 - SparkSQL：执行Spark SQL脚本 - DWSSQL：执行DWS SQL脚本 - DLISQL：执行DLI SQL脚本 - Shell：执行Shell SQL脚本 - CDMJob：执行CDM作业 - DISTransferTask：创建DIS转储任务 - CloudTableManager：CloudTable表管理，创建和删除表。 - OBSManager：OBS路径管理，包括创建和删除路径。 - RestClient：REST API请求 - SMN：发送短信或邮件 - MRSSpark：执行MRS服务的Spark作业 - MapReduce：执行MRS服务的MapReduce作业 - MRSFlinkJob：执行MRS服务的FlinkJob作业。 - MRSHetuEngine：执行MRS服务的HetuEngine作业。 - DLISpark：执行DLF服务的Spark作业 - RDSSQL：传递SQL语句到RDS中执行。 - ModelArts Train：执行ModelArts服务的workflow作业。
        :type type: str
        :param retry_times: 失败重试次数
        :type retry_times: int
        :param instance_id: 作业实例id
        :type instance_id: int
        :param input_row_count: 写入数据行数
        :type input_row_count: int
        :param speed: 写入速度(行/秒)
        :type speed: float
        :param log_path: 节点执行的日志路径
        :type log_path: str
        """
        
        

        self._node_name = None
        self._status = None
        self._queue = None
        self._plan_time = None
        self._start_time = None
        self._end_time = None
        self._type = None
        self._retry_times = None
        self._instance_id = None
        self._input_row_count = None
        self._speed = None
        self._log_path = None
        self.discriminator = None

        self.node_name = node_name
        self.status = status
        self.queue = queue
        self.plan_time = plan_time
        self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        self.type = type
        if retry_times is not None:
            self.retry_times = retry_times
        self.instance_id = instance_id
        if input_row_count is not None:
            self.input_row_count = input_row_count
        if speed is not None:
            self.speed = speed
        if log_path is not None:
            self.log_path = log_path

    @property
    def node_name(self):
        r"""Gets the node_name of this NodeInstance.

        节点名称

        :return: The node_name of this NodeInstance.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this NodeInstance.

        节点名称

        :param node_name: The node_name of this NodeInstance.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def status(self):
        r"""Gets the status of this NodeInstance.

        节点状态： - waiting：等待运行 - running：运行中 - success：运行成功 - fail： 运行失败 - skip：跳过 - pause： 暂停 - manual-stop：取消

        :return: The status of this NodeInstance.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this NodeInstance.

        节点状态： - waiting：等待运行 - running：运行中 - success：运行成功 - fail： 运行失败 - skip：跳过 - pause： 暂停 - manual-stop：取消

        :param status: The status of this NodeInstance.
        :type status: str
        """
        self._status = status

    @property
    def queue(self):
        r"""Gets the queue of this NodeInstance.

        DLI资源队列名称。在返回响应中，仅DLI SQL或者DLI SPARK算子会返回DLI队列名称。

        :return: The queue of this NodeInstance.
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        r"""Sets the queue of this NodeInstance.

        DLI资源队列名称。在返回响应中，仅DLI SQL或者DLI SPARK算子会返回DLI队列名称。

        :param queue: The queue of this NodeInstance.
        :type queue: str
        """
        self._queue = queue

    @property
    def plan_time(self):
        r"""Gets the plan_time of this NodeInstance.

        作业实例计划执行时间

        :return: The plan_time of this NodeInstance.
        :rtype: int
        """
        return self._plan_time

    @plan_time.setter
    def plan_time(self, plan_time):
        r"""Sets the plan_time of this NodeInstance.

        作业实例计划执行时间

        :param plan_time: The plan_time of this NodeInstance.
        :type plan_time: int
        """
        self._plan_time = plan_time

    @property
    def start_time(self):
        r"""Gets the start_time of this NodeInstance.

        节点实际执行开始时间

        :return: The start_time of this NodeInstance.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this NodeInstance.

        节点实际执行开始时间

        :param start_time: The start_time of this NodeInstance.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this NodeInstance.

        节点实际执行结束时间

        :return: The end_time of this NodeInstance.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this NodeInstance.

        节点实际执行结束时间

        :param end_time: The end_time of this NodeInstance.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def type(self):
        r"""Gets the type of this NodeInstance.

        节点类型： - HiveSQL：执行Hive SQL脚本 - SparkSQL：执行Spark SQL脚本 - DWSSQL：执行DWS SQL脚本 - DLISQL：执行DLI SQL脚本 - Shell：执行Shell SQL脚本 - CDMJob：执行CDM作业 - DISTransferTask：创建DIS转储任务 - CloudTableManager：CloudTable表管理，创建和删除表。 - OBSManager：OBS路径管理，包括创建和删除路径。 - RestClient：REST API请求 - SMN：发送短信或邮件 - MRSSpark：执行MRS服务的Spark作业 - MapReduce：执行MRS服务的MapReduce作业 - MRSFlinkJob：执行MRS服务的FlinkJob作业。 - MRSHetuEngine：执行MRS服务的HetuEngine作业。 - DLISpark：执行DLF服务的Spark作业 - RDSSQL：传递SQL语句到RDS中执行。 - ModelArts Train：执行ModelArts服务的workflow作业。

        :return: The type of this NodeInstance.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this NodeInstance.

        节点类型： - HiveSQL：执行Hive SQL脚本 - SparkSQL：执行Spark SQL脚本 - DWSSQL：执行DWS SQL脚本 - DLISQL：执行DLI SQL脚本 - Shell：执行Shell SQL脚本 - CDMJob：执行CDM作业 - DISTransferTask：创建DIS转储任务 - CloudTableManager：CloudTable表管理，创建和删除表。 - OBSManager：OBS路径管理，包括创建和删除路径。 - RestClient：REST API请求 - SMN：发送短信或邮件 - MRSSpark：执行MRS服务的Spark作业 - MapReduce：执行MRS服务的MapReduce作业 - MRSFlinkJob：执行MRS服务的FlinkJob作业。 - MRSHetuEngine：执行MRS服务的HetuEngine作业。 - DLISpark：执行DLF服务的Spark作业 - RDSSQL：传递SQL语句到RDS中执行。 - ModelArts Train：执行ModelArts服务的workflow作业。

        :param type: The type of this NodeInstance.
        :type type: str
        """
        self._type = type

    @property
    def retry_times(self):
        r"""Gets the retry_times of this NodeInstance.

        失败重试次数

        :return: The retry_times of this NodeInstance.
        :rtype: int
        """
        return self._retry_times

    @retry_times.setter
    def retry_times(self, retry_times):
        r"""Sets the retry_times of this NodeInstance.

        失败重试次数

        :param retry_times: The retry_times of this NodeInstance.
        :type retry_times: int
        """
        self._retry_times = retry_times

    @property
    def instance_id(self):
        r"""Gets the instance_id of this NodeInstance.

        作业实例id

        :return: The instance_id of this NodeInstance.
        :rtype: int
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this NodeInstance.

        作业实例id

        :param instance_id: The instance_id of this NodeInstance.
        :type instance_id: int
        """
        self._instance_id = instance_id

    @property
    def input_row_count(self):
        r"""Gets the input_row_count of this NodeInstance.

        写入数据行数

        :return: The input_row_count of this NodeInstance.
        :rtype: int
        """
        return self._input_row_count

    @input_row_count.setter
    def input_row_count(self, input_row_count):
        r"""Sets the input_row_count of this NodeInstance.

        写入数据行数

        :param input_row_count: The input_row_count of this NodeInstance.
        :type input_row_count: int
        """
        self._input_row_count = input_row_count

    @property
    def speed(self):
        r"""Gets the speed of this NodeInstance.

        写入速度(行/秒)

        :return: The speed of this NodeInstance.
        :rtype: float
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        r"""Sets the speed of this NodeInstance.

        写入速度(行/秒)

        :param speed: The speed of this NodeInstance.
        :type speed: float
        """
        self._speed = speed

    @property
    def log_path(self):
        r"""Gets the log_path of this NodeInstance.

        节点执行的日志路径

        :return: The log_path of this NodeInstance.
        :rtype: str
        """
        return self._log_path

    @log_path.setter
    def log_path(self, log_path):
        r"""Sets the log_path of this NodeInstance.

        节点执行的日志路径

        :param log_path: The log_path of this NodeInstance.
        :type log_path: str
        """
        self._log_path = log_path

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
        if not isinstance(other, NodeInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
