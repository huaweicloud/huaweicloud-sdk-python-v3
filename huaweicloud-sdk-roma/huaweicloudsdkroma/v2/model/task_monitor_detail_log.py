# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskMonitorDetailLog:

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
        'status': 'int',
        'position': 'str',
        'position_status': 'str',
        'stage': 'str',
        'dirty_data_count': 'int',
        'data_count': 'int',
        'data_size': 'float',
        'data_size_unit': 'str',
        'spend_time': 'int',
        'remarks': 'str',
        'step_begin_time': 'int',
        'step_end_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'position': 'position',
        'position_status': 'position_status',
        'stage': 'stage',
        'dirty_data_count': 'dirty_data_count',
        'data_count': 'data_count',
        'data_size': 'data_size',
        'data_size_unit': 'data_size_unit',
        'spend_time': 'spend_time',
        'remarks': 'remarks',
        'step_begin_time': 'step_begin_time',
        'step_end_time': 'step_end_time'
    }

    def __init__(self, id=None, status=None, position=None, position_status=None, stage=None, dirty_data_count=None, data_count=None, data_size=None, data_size_unit=None, spend_time=None, remarks=None, step_begin_time=None, step_end_time=None):
        """TaskMonitorDetailLog

        The model defined in huaweicloud sdk

        :param id: 任务每次执行步骤产生的唯一ID
        :type id: str
        :param status: 当前步骤执行详细状态，使用状态码的形式&lt;/br&gt; 状态码划分规则：reader端 100 ~ 499，writer端 500 ~ 899，其他900 ~ &lt;/br&gt; 当前状态码如下：&lt;/br&gt; 16-被强制取消&lt;/br&gt; 99-任务开始&lt;/br&gt; 100-Reader 任务开始&lt;/br&gt; 101-Reader 任务结束&lt;/br&gt; 102-正在读取数据&lt;/br&gt; 103-读端数据源端异常&lt;/br&gt; 104-读取数据结束&lt;/br&gt; 105-读取数据为0&lt;/br&gt; 106-读任务强制取消&lt;/br&gt; 107-在reader plugin中，任务发生了中断&lt;/br&gt; 108-读任务恢复运行&lt;/br&gt; 500-Writer 任务开始&lt;/br&gt; 501-Writer 任务结束&lt;/br&gt; 502-正在数据写入&lt;/br&gt; 503-目标端异常&lt;/br&gt; 504-数据写入结束&lt;/br&gt; 505-写任务强制取消&lt;/br&gt; 506-在writer plugin中，任务发生了中断&lt;/br&gt; 507-写任务恢复运行&lt;/br&gt; 900-接收到调度请求&lt;/br&gt; 901-任务运行结束&lt;/br&gt; 902-任务已运行结束，正在进行数据完整性校验&lt;/br&gt; 903-输出数据完整性校验结果&lt;/br&gt; 904-经过数据完整性校验，发现有数据缺失，正在进行数据补偿&lt;/br&gt; 905-输出数据补偿结果&lt;/br&gt; 906-读取任务正在在排队中（平台资源）&lt;/br&gt; 907-读取任务被拒绝执行，因为上一次调度还没有结束&lt;/br&gt; 908-写入任务正在在排队中（平台资源）&lt;/br&gt; 909-写入任务被拒绝执行，因为上一次调度还没有结束&lt;/br&gt; 911-读取任务没有被正常开启，请检查网络是否通畅，参数是否正确&lt;/br&gt; 912-写入任务没有被正常开启，请检查网络是否通畅，参数是否正确&lt;/br&gt; 913-任务调度请求失败&lt;/br&gt; 914-任务被拒绝执行，因为上一次调度还没有结束&lt;/br&gt; 915-任务不正常运行&lt;/br&gt; 916-任务日志上报异常&lt;/br&gt;
        :type status: int
        :param position: 标识当前步骤属于哪一个阶段，允许如下值：ADAPTER-任务处于初始化阶段, READER-任务正在执行Reader读操作, WRITER-任务正在执行Writer写操作
        :type position: str
        :param position_status: 任务当前步骤的状态，允许如下值：NORMAL-正在运行, NODE_END-本节点正常结束, RUNTIME_CANCEL-任务被取消, TASK_END-本任务正常结束, RUNTIME_ERR-运行时异常, INTERNAL_ERR-内部程序异常
        :type position_status: str
        :param stage: 标识当前步骤属于哪一个FDI插件，如adapter, apireader, rdbwriter等
        :type stage: str
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
        :param remarks: 执行详细信息
        :type remarks: str
        :param step_begin_time: 本次步骤启动时间，格式timestamp(ms)，使用UTC时区
        :type step_begin_time: int
        :param step_end_time: 本次步骤结束时间，格式timestamp(ms)，使用UTC时区
        :type step_end_time: int
        """
        
        

        self._id = None
        self._status = None
        self._position = None
        self._position_status = None
        self._stage = None
        self._dirty_data_count = None
        self._data_count = None
        self._data_size = None
        self._data_size_unit = None
        self._spend_time = None
        self._remarks = None
        self._step_begin_time = None
        self._step_end_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if position is not None:
            self.position = position
        if position_status is not None:
            self.position_status = position_status
        if stage is not None:
            self.stage = stage
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
        if remarks is not None:
            self.remarks = remarks
        if step_begin_time is not None:
            self.step_begin_time = step_begin_time
        if step_end_time is not None:
            self.step_end_time = step_end_time

    @property
    def id(self):
        """Gets the id of this TaskMonitorDetailLog.

        任务每次执行步骤产生的唯一ID

        :return: The id of this TaskMonitorDetailLog.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskMonitorDetailLog.

        任务每次执行步骤产生的唯一ID

        :param id: The id of this TaskMonitorDetailLog.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this TaskMonitorDetailLog.

        当前步骤执行详细状态，使用状态码的形式</br> 状态码划分规则：reader端 100 ~ 499，writer端 500 ~ 899，其他900 ~ </br> 当前状态码如下：</br> 16-被强制取消</br> 99-任务开始</br> 100-Reader 任务开始</br> 101-Reader 任务结束</br> 102-正在读取数据</br> 103-读端数据源端异常</br> 104-读取数据结束</br> 105-读取数据为0</br> 106-读任务强制取消</br> 107-在reader plugin中，任务发生了中断</br> 108-读任务恢复运行</br> 500-Writer 任务开始</br> 501-Writer 任务结束</br> 502-正在数据写入</br> 503-目标端异常</br> 504-数据写入结束</br> 505-写任务强制取消</br> 506-在writer plugin中，任务发生了中断</br> 507-写任务恢复运行</br> 900-接收到调度请求</br> 901-任务运行结束</br> 902-任务已运行结束，正在进行数据完整性校验</br> 903-输出数据完整性校验结果</br> 904-经过数据完整性校验，发现有数据缺失，正在进行数据补偿</br> 905-输出数据补偿结果</br> 906-读取任务正在在排队中（平台资源）</br> 907-读取任务被拒绝执行，因为上一次调度还没有结束</br> 908-写入任务正在在排队中（平台资源）</br> 909-写入任务被拒绝执行，因为上一次调度还没有结束</br> 911-读取任务没有被正常开启，请检查网络是否通畅，参数是否正确</br> 912-写入任务没有被正常开启，请检查网络是否通畅，参数是否正确</br> 913-任务调度请求失败</br> 914-任务被拒绝执行，因为上一次调度还没有结束</br> 915-任务不正常运行</br> 916-任务日志上报异常</br>

        :return: The status of this TaskMonitorDetailLog.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskMonitorDetailLog.

        当前步骤执行详细状态，使用状态码的形式</br> 状态码划分规则：reader端 100 ~ 499，writer端 500 ~ 899，其他900 ~ </br> 当前状态码如下：</br> 16-被强制取消</br> 99-任务开始</br> 100-Reader 任务开始</br> 101-Reader 任务结束</br> 102-正在读取数据</br> 103-读端数据源端异常</br> 104-读取数据结束</br> 105-读取数据为0</br> 106-读任务强制取消</br> 107-在reader plugin中，任务发生了中断</br> 108-读任务恢复运行</br> 500-Writer 任务开始</br> 501-Writer 任务结束</br> 502-正在数据写入</br> 503-目标端异常</br> 504-数据写入结束</br> 505-写任务强制取消</br> 506-在writer plugin中，任务发生了中断</br> 507-写任务恢复运行</br> 900-接收到调度请求</br> 901-任务运行结束</br> 902-任务已运行结束，正在进行数据完整性校验</br> 903-输出数据完整性校验结果</br> 904-经过数据完整性校验，发现有数据缺失，正在进行数据补偿</br> 905-输出数据补偿结果</br> 906-读取任务正在在排队中（平台资源）</br> 907-读取任务被拒绝执行，因为上一次调度还没有结束</br> 908-写入任务正在在排队中（平台资源）</br> 909-写入任务被拒绝执行，因为上一次调度还没有结束</br> 911-读取任务没有被正常开启，请检查网络是否通畅，参数是否正确</br> 912-写入任务没有被正常开启，请检查网络是否通畅，参数是否正确</br> 913-任务调度请求失败</br> 914-任务被拒绝执行，因为上一次调度还没有结束</br> 915-任务不正常运行</br> 916-任务日志上报异常</br>

        :param status: The status of this TaskMonitorDetailLog.
        :type status: int
        """
        self._status = status

    @property
    def position(self):
        """Gets the position of this TaskMonitorDetailLog.

        标识当前步骤属于哪一个阶段，允许如下值：ADAPTER-任务处于初始化阶段, READER-任务正在执行Reader读操作, WRITER-任务正在执行Writer写操作

        :return: The position of this TaskMonitorDetailLog.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this TaskMonitorDetailLog.

        标识当前步骤属于哪一个阶段，允许如下值：ADAPTER-任务处于初始化阶段, READER-任务正在执行Reader读操作, WRITER-任务正在执行Writer写操作

        :param position: The position of this TaskMonitorDetailLog.
        :type position: str
        """
        self._position = position

    @property
    def position_status(self):
        """Gets the position_status of this TaskMonitorDetailLog.

        任务当前步骤的状态，允许如下值：NORMAL-正在运行, NODE_END-本节点正常结束, RUNTIME_CANCEL-任务被取消, TASK_END-本任务正常结束, RUNTIME_ERR-运行时异常, INTERNAL_ERR-内部程序异常

        :return: The position_status of this TaskMonitorDetailLog.
        :rtype: str
        """
        return self._position_status

    @position_status.setter
    def position_status(self, position_status):
        """Sets the position_status of this TaskMonitorDetailLog.

        任务当前步骤的状态，允许如下值：NORMAL-正在运行, NODE_END-本节点正常结束, RUNTIME_CANCEL-任务被取消, TASK_END-本任务正常结束, RUNTIME_ERR-运行时异常, INTERNAL_ERR-内部程序异常

        :param position_status: The position_status of this TaskMonitorDetailLog.
        :type position_status: str
        """
        self._position_status = position_status

    @property
    def stage(self):
        """Gets the stage of this TaskMonitorDetailLog.

        标识当前步骤属于哪一个FDI插件，如adapter, apireader, rdbwriter等

        :return: The stage of this TaskMonitorDetailLog.
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """Sets the stage of this TaskMonitorDetailLog.

        标识当前步骤属于哪一个FDI插件，如adapter, apireader, rdbwriter等

        :param stage: The stage of this TaskMonitorDetailLog.
        :type stage: str
        """
        self._stage = stage

    @property
    def dirty_data_count(self):
        """Gets the dirty_data_count of this TaskMonitorDetailLog.

        异常数据条数

        :return: The dirty_data_count of this TaskMonitorDetailLog.
        :rtype: int
        """
        return self._dirty_data_count

    @dirty_data_count.setter
    def dirty_data_count(self, dirty_data_count):
        """Sets the dirty_data_count of this TaskMonitorDetailLog.

        异常数据条数

        :param dirty_data_count: The dirty_data_count of this TaskMonitorDetailLog.
        :type dirty_data_count: int
        """
        self._dirty_data_count = dirty_data_count

    @property
    def data_count(self):
        """Gets the data_count of this TaskMonitorDetailLog.

        成功数据条数

        :return: The data_count of this TaskMonitorDetailLog.
        :rtype: int
        """
        return self._data_count

    @data_count.setter
    def data_count(self, data_count):
        """Sets the data_count of this TaskMonitorDetailLog.

        成功数据条数

        :param data_count: The data_count of this TaskMonitorDetailLog.
        :type data_count: int
        """
        self._data_count = data_count

    @property
    def data_size(self):
        """Gets the data_size of this TaskMonitorDetailLog.

        成功数据大小，浮点数类型

        :return: The data_size of this TaskMonitorDetailLog.
        :rtype: float
        """
        return self._data_size

    @data_size.setter
    def data_size(self, data_size):
        """Sets the data_size of this TaskMonitorDetailLog.

        成功数据大小，浮点数类型

        :param data_size: The data_size of this TaskMonitorDetailLog.
        :type data_size: float
        """
        self._data_size = data_size

    @property
    def data_size_unit(self):
        """Gets the data_size_unit of this TaskMonitorDetailLog.

        成功数据大小的计量单位

        :return: The data_size_unit of this TaskMonitorDetailLog.
        :rtype: str
        """
        return self._data_size_unit

    @data_size_unit.setter
    def data_size_unit(self, data_size_unit):
        """Sets the data_size_unit of this TaskMonitorDetailLog.

        成功数据大小的计量单位

        :param data_size_unit: The data_size_unit of this TaskMonitorDetailLog.
        :type data_size_unit: str
        """
        self._data_size_unit = data_size_unit

    @property
    def spend_time(self):
        """Gets the spend_time of this TaskMonitorDetailLog.

        执行时长，单位：ms

        :return: The spend_time of this TaskMonitorDetailLog.
        :rtype: int
        """
        return self._spend_time

    @spend_time.setter
    def spend_time(self, spend_time):
        """Sets the spend_time of this TaskMonitorDetailLog.

        执行时长，单位：ms

        :param spend_time: The spend_time of this TaskMonitorDetailLog.
        :type spend_time: int
        """
        self._spend_time = spend_time

    @property
    def remarks(self):
        """Gets the remarks of this TaskMonitorDetailLog.

        执行详细信息

        :return: The remarks of this TaskMonitorDetailLog.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        """Sets the remarks of this TaskMonitorDetailLog.

        执行详细信息

        :param remarks: The remarks of this TaskMonitorDetailLog.
        :type remarks: str
        """
        self._remarks = remarks

    @property
    def step_begin_time(self):
        """Gets the step_begin_time of this TaskMonitorDetailLog.

        本次步骤启动时间，格式timestamp(ms)，使用UTC时区

        :return: The step_begin_time of this TaskMonitorDetailLog.
        :rtype: int
        """
        return self._step_begin_time

    @step_begin_time.setter
    def step_begin_time(self, step_begin_time):
        """Sets the step_begin_time of this TaskMonitorDetailLog.

        本次步骤启动时间，格式timestamp(ms)，使用UTC时区

        :param step_begin_time: The step_begin_time of this TaskMonitorDetailLog.
        :type step_begin_time: int
        """
        self._step_begin_time = step_begin_time

    @property
    def step_end_time(self):
        """Gets the step_end_time of this TaskMonitorDetailLog.

        本次步骤结束时间，格式timestamp(ms)，使用UTC时区

        :return: The step_end_time of this TaskMonitorDetailLog.
        :rtype: int
        """
        return self._step_end_time

    @step_end_time.setter
    def step_end_time(self, step_end_time):
        """Sets the step_end_time of this TaskMonitorDetailLog.

        本次步骤结束时间，格式timestamp(ms)，使用UTC时区

        :param step_end_time: The step_end_time of this TaskMonitorDetailLog.
        :type step_end_time: int
        """
        self._step_end_time = step_end_time

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
        if not isinstance(other, TaskMonitorDetailLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
