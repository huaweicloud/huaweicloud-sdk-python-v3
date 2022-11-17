# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskMonitorLog:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'start_time': 'int',
        'dispatch_time': 'int',
        'end_time': 'int',
        'execute_status': 'str',
        'position': 'str',
        'position_status': 'str',
        'status': 'int',
        'dirty_data_count': 'int',
        'data_count': 'int',
        'data_size': 'float',
        'data_size_unit': 'str',
        'spend_time': 'int',
        'read_spend_time': 'int',
        'write_spend_time': 'int',
        'remarks': 'str',
        'detail_logs': 'list[TaskMonitorDetailLog]'
    }

    attribute_map = {
        'id': 'id',
        'start_time': 'start_time',
        'dispatch_time': 'dispatch_time',
        'end_time': 'end_time',
        'execute_status': 'execute_status',
        'position': 'position',
        'position_status': 'position_status',
        'status': 'status',
        'dirty_data_count': 'dirty_data_count',
        'data_count': 'data_count',
        'data_size': 'data_size',
        'data_size_unit': 'data_size_unit',
        'spend_time': 'spend_time',
        'read_spend_time': 'read_spend_time',
        'write_spend_time': 'write_spend_time',
        'remarks': 'remarks',
        'detail_logs': 'detail_logs'
    }

    def __init__(self, id=None, start_time=None, dispatch_time=None, end_time=None, execute_status=None, position=None, position_status=None, status=None, dirty_data_count=None, data_count=None, data_size=None, data_size_unit=None, spend_time=None, read_spend_time=None, write_spend_time=None, remarks=None, detail_logs=None):
        """TaskMonitorLog

        The model defined in huaweicloud sdk

        :param id: 单次任务执行的跟踪ID
        :type id: str
        :param start_time: 本次执行启动时间，格式timestamp(ms)，使用UTC时区
        :type start_time: int
        :param dispatch_time: 计划执行时间，格式timestamp(ms)，使用UTC时区
        :type dispatch_time: int
        :param end_time: 写入结束时间，格式timestamp(ms)，使用UTC时区
        :type end_time: int
        :param execute_status: 任务本次执行状态，允许如下值：UNSTARTED-未启动, WAITING-等待调度中, RUNNING-执行中, SUCCESS-执行成功, CANCELLED-任务取消, ERROR-执行异常
        :type execute_status: str
        :param position: 标识本次任务执行到哪一个阶段，允许如下值：ADAPTER-任务处于初始化阶段, READER-任务正在执行Reader读操作, WRITER-任务正在执行Writer写操作
        :type position: str
        :param position_status: 任务本次执行当前阶段的状态，允许如下值：NORMAL-正在运行, NODE_END-本节点正常结束, RUNTIME_CANCEL-任务被取消, TASK_END-本任务正常结束, RUNTIME_ERR-运行时异常, INTERNAL_ERR-内部程序异常
        :type position_status: str
        :param status: 本次任务执行详细状态，使用状态码的形式&lt;/br&gt; 状态码划分规则：reader端 100 ~ 499，writer端 500 ~ 899，其他900 ~ &lt;/br&gt; 当前状态码如下：&lt;/br&gt; 16-被强制取消&lt;/br&gt; 99-任务开始&lt;/br&gt; 100-Reader 任务开始&lt;/br&gt; 101-Reader 任务结束&lt;/br&gt; 102-正在读取数据&lt;/br&gt; 103-读端数据源端异常&lt;/br&gt; 104-读取数据结束&lt;/br&gt; 105-读取数据为0&lt;/br&gt; 106-读任务强制取消&lt;/br&gt; 107-在reader plugin中，任务发生了中断&lt;/br&gt; 108-读任务恢复运行&lt;/br&gt; 500-Writer 任务开始&lt;/br&gt; 501-Writer 任务结束&lt;/br&gt; 502-正在数据写入&lt;/br&gt; 503-目标端异常&lt;/br&gt; 504-数据写入结束&lt;/br&gt; 505-写任务强制取消&lt;/br&gt; 506-在writer plugin中，任务发生了中断&lt;/br&gt; 507-写任务恢复运行&lt;/br&gt; 900-接收到调度请求&lt;/br&gt; 901-任务运行结束&lt;/br&gt; 902-任务已运行结束，正在进行数据完整性校验&lt;/br&gt; 903-输出数据完整性校验结果&lt;/br&gt; 904-经过数据完整性校验，发现有数据缺失，正在进行数据补偿&lt;/br&gt; 905-输出数据补偿结果&lt;/br&gt; 906-读取任务正在在排队中（平台资源）&lt;/br&gt; 907-读取任务被拒绝执行，因为上一次调度还没有结束&lt;/br&gt; 908-写入任务正在在排队中（平台资源）&lt;/br&gt; 909-写入任务被拒绝执行，因为上一次调度还没有结束&lt;/br&gt; 911-读取任务没有被正常开启，请检查网络是否通畅，参数是否正确&lt;/br&gt; 912-写入任务没有被正常开启，请检查网络是否通畅，参数是否正确&lt;/br&gt; 913-任务调度请求失败&lt;/br&gt; 914-任务被拒绝执行，因为上一次调度还没有结束&lt;/br&gt; 915-任务不正常运行&lt;/br&gt; 916-任务日志上报异常&lt;/br&gt;
        :type status: int
        :param dirty_data_count: 异常数据条数
        :type dirty_data_count: int
        :param data_count: 成功数据条数
        :type data_count: int
        :param data_size: 成功数据大小，浮点数类型
        :type data_size: float
        :param data_size_unit: 成功数据大小的计量单位
        :type data_size_unit: str
        :param spend_time: 执行时长，单位：ms
        :type spend_time: int
        :param read_spend_time: 读取执行时长，单位：ms，只有在定时任务时存在该属性
        :type read_spend_time: int
        :param write_spend_time: 写入执行时长，单位：ms
        :type write_spend_time: int
        :param remarks: 本次执行结果简要信息
        :type remarks: str
        :param detail_logs: 本次执行详细轨迹信息
        :type detail_logs: list[:class:`huaweicloudsdkroma.v2.TaskMonitorDetailLog`]
        """
        
        

        self._id = None
        self._start_time = None
        self._dispatch_time = None
        self._end_time = None
        self._execute_status = None
        self._position = None
        self._position_status = None
        self._status = None
        self._dirty_data_count = None
        self._data_count = None
        self._data_size = None
        self._data_size_unit = None
        self._spend_time = None
        self._read_spend_time = None
        self._write_spend_time = None
        self._remarks = None
        self._detail_logs = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if start_time is not None:
            self.start_time = start_time
        if dispatch_time is not None:
            self.dispatch_time = dispatch_time
        if end_time is not None:
            self.end_time = end_time
        if execute_status is not None:
            self.execute_status = execute_status
        if position is not None:
            self.position = position
        if position_status is not None:
            self.position_status = position_status
        if status is not None:
            self.status = status
        if dirty_data_count is not None:
            self.dirty_data_count = dirty_data_count
        if data_count is not None:
            self.data_count = data_count
        if data_size is not None:
            self.data_size = data_size
        if data_size_unit is not None:
            self.data_size_unit = data_size_unit
        if spend_time is not None:
            self.spend_time = spend_time
        if read_spend_time is not None:
            self.read_spend_time = read_spend_time
        if write_spend_time is not None:
            self.write_spend_time = write_spend_time
        if remarks is not None:
            self.remarks = remarks
        if detail_logs is not None:
            self.detail_logs = detail_logs

    @property
    def id(self):
        """Gets the id of this TaskMonitorLog.

        单次任务执行的跟踪ID

        :return: The id of this TaskMonitorLog.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskMonitorLog.

        单次任务执行的跟踪ID

        :param id: The id of this TaskMonitorLog.
        :type id: str
        """
        self._id = id

    @property
    def start_time(self):
        """Gets the start_time of this TaskMonitorLog.

        本次执行启动时间，格式timestamp(ms)，使用UTC时区

        :return: The start_time of this TaskMonitorLog.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TaskMonitorLog.

        本次执行启动时间，格式timestamp(ms)，使用UTC时区

        :param start_time: The start_time of this TaskMonitorLog.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def dispatch_time(self):
        """Gets the dispatch_time of this TaskMonitorLog.

        计划执行时间，格式timestamp(ms)，使用UTC时区

        :return: The dispatch_time of this TaskMonitorLog.
        :rtype: int
        """
        return self._dispatch_time

    @dispatch_time.setter
    def dispatch_time(self, dispatch_time):
        """Sets the dispatch_time of this TaskMonitorLog.

        计划执行时间，格式timestamp(ms)，使用UTC时区

        :param dispatch_time: The dispatch_time of this TaskMonitorLog.
        :type dispatch_time: int
        """
        self._dispatch_time = dispatch_time

    @property
    def end_time(self):
        """Gets the end_time of this TaskMonitorLog.

        写入结束时间，格式timestamp(ms)，使用UTC时区

        :return: The end_time of this TaskMonitorLog.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TaskMonitorLog.

        写入结束时间，格式timestamp(ms)，使用UTC时区

        :param end_time: The end_time of this TaskMonitorLog.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def execute_status(self):
        """Gets the execute_status of this TaskMonitorLog.

        任务本次执行状态，允许如下值：UNSTARTED-未启动, WAITING-等待调度中, RUNNING-执行中, SUCCESS-执行成功, CANCELLED-任务取消, ERROR-执行异常

        :return: The execute_status of this TaskMonitorLog.
        :rtype: str
        """
        return self._execute_status

    @execute_status.setter
    def execute_status(self, execute_status):
        """Sets the execute_status of this TaskMonitorLog.

        任务本次执行状态，允许如下值：UNSTARTED-未启动, WAITING-等待调度中, RUNNING-执行中, SUCCESS-执行成功, CANCELLED-任务取消, ERROR-执行异常

        :param execute_status: The execute_status of this TaskMonitorLog.
        :type execute_status: str
        """
        self._execute_status = execute_status

    @property
    def position(self):
        """Gets the position of this TaskMonitorLog.

        标识本次任务执行到哪一个阶段，允许如下值：ADAPTER-任务处于初始化阶段, READER-任务正在执行Reader读操作, WRITER-任务正在执行Writer写操作

        :return: The position of this TaskMonitorLog.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this TaskMonitorLog.

        标识本次任务执行到哪一个阶段，允许如下值：ADAPTER-任务处于初始化阶段, READER-任务正在执行Reader读操作, WRITER-任务正在执行Writer写操作

        :param position: The position of this TaskMonitorLog.
        :type position: str
        """
        self._position = position

    @property
    def position_status(self):
        """Gets the position_status of this TaskMonitorLog.

        任务本次执行当前阶段的状态，允许如下值：NORMAL-正在运行, NODE_END-本节点正常结束, RUNTIME_CANCEL-任务被取消, TASK_END-本任务正常结束, RUNTIME_ERR-运行时异常, INTERNAL_ERR-内部程序异常

        :return: The position_status of this TaskMonitorLog.
        :rtype: str
        """
        return self._position_status

    @position_status.setter
    def position_status(self, position_status):
        """Sets the position_status of this TaskMonitorLog.

        任务本次执行当前阶段的状态，允许如下值：NORMAL-正在运行, NODE_END-本节点正常结束, RUNTIME_CANCEL-任务被取消, TASK_END-本任务正常结束, RUNTIME_ERR-运行时异常, INTERNAL_ERR-内部程序异常

        :param position_status: The position_status of this TaskMonitorLog.
        :type position_status: str
        """
        self._position_status = position_status

    @property
    def status(self):
        """Gets the status of this TaskMonitorLog.

        本次任务执行详细状态，使用状态码的形式</br> 状态码划分规则：reader端 100 ~ 499，writer端 500 ~ 899，其他900 ~ </br> 当前状态码如下：</br> 16-被强制取消</br> 99-任务开始</br> 100-Reader 任务开始</br> 101-Reader 任务结束</br> 102-正在读取数据</br> 103-读端数据源端异常</br> 104-读取数据结束</br> 105-读取数据为0</br> 106-读任务强制取消</br> 107-在reader plugin中，任务发生了中断</br> 108-读任务恢复运行</br> 500-Writer 任务开始</br> 501-Writer 任务结束</br> 502-正在数据写入</br> 503-目标端异常</br> 504-数据写入结束</br> 505-写任务强制取消</br> 506-在writer plugin中，任务发生了中断</br> 507-写任务恢复运行</br> 900-接收到调度请求</br> 901-任务运行结束</br> 902-任务已运行结束，正在进行数据完整性校验</br> 903-输出数据完整性校验结果</br> 904-经过数据完整性校验，发现有数据缺失，正在进行数据补偿</br> 905-输出数据补偿结果</br> 906-读取任务正在在排队中（平台资源）</br> 907-读取任务被拒绝执行，因为上一次调度还没有结束</br> 908-写入任务正在在排队中（平台资源）</br> 909-写入任务被拒绝执行，因为上一次调度还没有结束</br> 911-读取任务没有被正常开启，请检查网络是否通畅，参数是否正确</br> 912-写入任务没有被正常开启，请检查网络是否通畅，参数是否正确</br> 913-任务调度请求失败</br> 914-任务被拒绝执行，因为上一次调度还没有结束</br> 915-任务不正常运行</br> 916-任务日志上报异常</br>

        :return: The status of this TaskMonitorLog.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskMonitorLog.

        本次任务执行详细状态，使用状态码的形式</br> 状态码划分规则：reader端 100 ~ 499，writer端 500 ~ 899，其他900 ~ </br> 当前状态码如下：</br> 16-被强制取消</br> 99-任务开始</br> 100-Reader 任务开始</br> 101-Reader 任务结束</br> 102-正在读取数据</br> 103-读端数据源端异常</br> 104-读取数据结束</br> 105-读取数据为0</br> 106-读任务强制取消</br> 107-在reader plugin中，任务发生了中断</br> 108-读任务恢复运行</br> 500-Writer 任务开始</br> 501-Writer 任务结束</br> 502-正在数据写入</br> 503-目标端异常</br> 504-数据写入结束</br> 505-写任务强制取消</br> 506-在writer plugin中，任务发生了中断</br> 507-写任务恢复运行</br> 900-接收到调度请求</br> 901-任务运行结束</br> 902-任务已运行结束，正在进行数据完整性校验</br> 903-输出数据完整性校验结果</br> 904-经过数据完整性校验，发现有数据缺失，正在进行数据补偿</br> 905-输出数据补偿结果</br> 906-读取任务正在在排队中（平台资源）</br> 907-读取任务被拒绝执行，因为上一次调度还没有结束</br> 908-写入任务正在在排队中（平台资源）</br> 909-写入任务被拒绝执行，因为上一次调度还没有结束</br> 911-读取任务没有被正常开启，请检查网络是否通畅，参数是否正确</br> 912-写入任务没有被正常开启，请检查网络是否通畅，参数是否正确</br> 913-任务调度请求失败</br> 914-任务被拒绝执行，因为上一次调度还没有结束</br> 915-任务不正常运行</br> 916-任务日志上报异常</br>

        :param status: The status of this TaskMonitorLog.
        :type status: int
        """
        self._status = status

    @property
    def dirty_data_count(self):
        """Gets the dirty_data_count of this TaskMonitorLog.

        异常数据条数

        :return: The dirty_data_count of this TaskMonitorLog.
        :rtype: int
        """
        return self._dirty_data_count

    @dirty_data_count.setter
    def dirty_data_count(self, dirty_data_count):
        """Sets the dirty_data_count of this TaskMonitorLog.

        异常数据条数

        :param dirty_data_count: The dirty_data_count of this TaskMonitorLog.
        :type dirty_data_count: int
        """
        self._dirty_data_count = dirty_data_count

    @property
    def data_count(self):
        """Gets the data_count of this TaskMonitorLog.

        成功数据条数

        :return: The data_count of this TaskMonitorLog.
        :rtype: int
        """
        return self._data_count

    @data_count.setter
    def data_count(self, data_count):
        """Sets the data_count of this TaskMonitorLog.

        成功数据条数

        :param data_count: The data_count of this TaskMonitorLog.
        :type data_count: int
        """
        self._data_count = data_count

    @property
    def data_size(self):
        """Gets the data_size of this TaskMonitorLog.

        成功数据大小，浮点数类型

        :return: The data_size of this TaskMonitorLog.
        :rtype: float
        """
        return self._data_size

    @data_size.setter
    def data_size(self, data_size):
        """Sets the data_size of this TaskMonitorLog.

        成功数据大小，浮点数类型

        :param data_size: The data_size of this TaskMonitorLog.
        :type data_size: float
        """
        self._data_size = data_size

    @property
    def data_size_unit(self):
        """Gets the data_size_unit of this TaskMonitorLog.

        成功数据大小的计量单位

        :return: The data_size_unit of this TaskMonitorLog.
        :rtype: str
        """
        return self._data_size_unit

    @data_size_unit.setter
    def data_size_unit(self, data_size_unit):
        """Sets the data_size_unit of this TaskMonitorLog.

        成功数据大小的计量单位

        :param data_size_unit: The data_size_unit of this TaskMonitorLog.
        :type data_size_unit: str
        """
        self._data_size_unit = data_size_unit

    @property
    def spend_time(self):
        """Gets the spend_time of this TaskMonitorLog.

        执行时长，单位：ms

        :return: The spend_time of this TaskMonitorLog.
        :rtype: int
        """
        return self._spend_time

    @spend_time.setter
    def spend_time(self, spend_time):
        """Sets the spend_time of this TaskMonitorLog.

        执行时长，单位：ms

        :param spend_time: The spend_time of this TaskMonitorLog.
        :type spend_time: int
        """
        self._spend_time = spend_time

    @property
    def read_spend_time(self):
        """Gets the read_spend_time of this TaskMonitorLog.

        读取执行时长，单位：ms，只有在定时任务时存在该属性

        :return: The read_spend_time of this TaskMonitorLog.
        :rtype: int
        """
        return self._read_spend_time

    @read_spend_time.setter
    def read_spend_time(self, read_spend_time):
        """Sets the read_spend_time of this TaskMonitorLog.

        读取执行时长，单位：ms，只有在定时任务时存在该属性

        :param read_spend_time: The read_spend_time of this TaskMonitorLog.
        :type read_spend_time: int
        """
        self._read_spend_time = read_spend_time

    @property
    def write_spend_time(self):
        """Gets the write_spend_time of this TaskMonitorLog.

        写入执行时长，单位：ms

        :return: The write_spend_time of this TaskMonitorLog.
        :rtype: int
        """
        return self._write_spend_time

    @write_spend_time.setter
    def write_spend_time(self, write_spend_time):
        """Sets the write_spend_time of this TaskMonitorLog.

        写入执行时长，单位：ms

        :param write_spend_time: The write_spend_time of this TaskMonitorLog.
        :type write_spend_time: int
        """
        self._write_spend_time = write_spend_time

    @property
    def remarks(self):
        """Gets the remarks of this TaskMonitorLog.

        本次执行结果简要信息

        :return: The remarks of this TaskMonitorLog.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        """Sets the remarks of this TaskMonitorLog.

        本次执行结果简要信息

        :param remarks: The remarks of this TaskMonitorLog.
        :type remarks: str
        """
        self._remarks = remarks

    @property
    def detail_logs(self):
        """Gets the detail_logs of this TaskMonitorLog.

        本次执行详细轨迹信息

        :return: The detail_logs of this TaskMonitorLog.
        :rtype: list[:class:`huaweicloudsdkroma.v2.TaskMonitorDetailLog`]
        """
        return self._detail_logs

    @detail_logs.setter
    def detail_logs(self, detail_logs):
        """Sets the detail_logs of this TaskMonitorLog.

        本次执行详细轨迹信息

        :param detail_logs: The detail_logs of this TaskMonitorLog.
        :type detail_logs: list[:class:`huaweicloudsdkroma.v2.TaskMonitorDetailLog`]
        """
        self._detail_logs = detail_logs

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
        if not isinstance(other, TaskMonitorLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
