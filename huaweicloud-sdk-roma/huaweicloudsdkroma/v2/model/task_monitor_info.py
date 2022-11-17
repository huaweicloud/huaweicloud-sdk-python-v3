# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskMonitorInfo:

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
        'task_name': 'str',
        'task_type': 'str',
        'status': 'int',
        'last_execute_time': 'int',
        'use_quartz_cron': 'bool',
        'cron': 'str',
        'period': 'str',
        'dispatch_interval': 'int',
        'position': 'str',
        'execute_status': 'str',
        'source_app_id': 'str',
        'source_app_name': 'str',
        'source_instance_id': 'str',
        'target_app_id': 'str',
        'target_app_name': 'str',
        'target_instance_id': 'str',
        'ext_type': 'str',
        'enterprise_project_id': 'str',
        'task_tag': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_name': 'task_name',
        'task_type': 'task_type',
        'status': 'status',
        'last_execute_time': 'last_execute_time',
        'use_quartz_cron': 'use_quartz_cron',
        'cron': 'cron',
        'period': 'period',
        'dispatch_interval': 'dispatch_interval',
        'position': 'position',
        'execute_status': 'execute_status',
        'source_app_id': 'source_app_id',
        'source_app_name': 'source_app_name',
        'source_instance_id': 'source_instance_id',
        'target_app_id': 'target_app_id',
        'target_app_name': 'target_app_name',
        'target_instance_id': 'target_instance_id',
        'ext_type': 'ext_type',
        'enterprise_project_id': 'enterprise_project_id',
        'task_tag': 'task_tag'
    }

    def __init__(self, task_id=None, task_name=None, task_type=None, status=None, last_execute_time=None, use_quartz_cron=None, cron=None, period=None, dispatch_interval=None, position=None, execute_status=None, source_app_id=None, source_app_name=None, source_instance_id=None, target_app_id=None, target_app_name=None, target_instance_id=None, ext_type=None, enterprise_project_id=None, task_tag=None):
        """TaskMonitorInfo

        The model defined in huaweicloud sdk

        :param task_id: 任务ID
        :type task_id: str
        :param task_name: 任务名称
        :type task_name: str
        :param task_type: 任务类型, 只允许两种类型:TIMING-定时任务, REALTIME-实时任务
        :type task_type: str
        :param status: 任务状态, 只允许两种类型:0-停止, 1-运行中
        :type status: int
        :param last_execute_time: 任务最近一次执行时间，格式timestamp(ms)，使用UTC时区
        :type last_execute_time: int
        :param use_quartz_cron: 任务是否使用Quartz表达式，只有定时任务才有该属性
        :type use_quartz_cron: bool
        :param cron: CRON表达式，只有定时任务且use_quartz_cron为true时才有该属性
        :type cron: str
        :param period: 调度周期的单位，如天，小时等，只有定时任务且use_quartz_cron为false时才有该属性，当前仅允许如下类型：MIN-分钟, HOUR-小时, DAY-天, WEEK-周, MON-月
        :type period: str
        :param dispatch_interval: 调度周期，和period字段一起可以确定每隔多长时间调度一次，只有定时任务且use_quartz_cron为false时才有该属性
        :type dispatch_interval: int
        :param position: 标识最近一次任务执行到哪一个阶段，允许如下值：ADAPTER-任务处于初始化阶段, READER-任务正在执行Reader读操作, WRITER-任务正在执行Writer写操作
        :type position: str
        :param execute_status: 任务最近一次执行状态，允许如下值：UNSTARTED-未启动, WAITING-等待调度中, RUNNING-执行中, SUCCESS-执行成功, CANCELLED-任务取消, ERROR-执行异常
        :type execute_status: str
        :param source_app_id: 任务源端数据源所属应用ID
        :type source_app_id: str
        :param source_app_name: 任务源端数据源所属应用名称
        :type source_app_name: str
        :param source_instance_id: 任务源端数据源所属实例ID
        :type source_instance_id: str
        :param target_app_id: 任务目标端数据源所属应用ID
        :type target_app_id: str
        :param target_app_name: 任务目标端数据源所属应用名称
        :type target_app_name: str
        :param target_instance_id: 任务目标端数据源所属实例ID
        :type target_instance_id: str
        :param ext_type: 任务扩展类型，当前如果是CDC组合任务，该字段为CDC，否则为null
        :type ext_type: str
        :param enterprise_project_id: 任务所属企业项目ID，默认为0
        :type enterprise_project_id: str
        :param task_tag: 任务标签
        :type task_tag: str
        """
        
        

        self._task_id = None
        self._task_name = None
        self._task_type = None
        self._status = None
        self._last_execute_time = None
        self._use_quartz_cron = None
        self._cron = None
        self._period = None
        self._dispatch_interval = None
        self._position = None
        self._execute_status = None
        self._source_app_id = None
        self._source_app_name = None
        self._source_instance_id = None
        self._target_app_id = None
        self._target_app_name = None
        self._target_instance_id = None
        self._ext_type = None
        self._enterprise_project_id = None
        self._task_tag = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if task_type is not None:
            self.task_type = task_type
        if status is not None:
            self.status = status
        if last_execute_time is not None:
            self.last_execute_time = last_execute_time
        if use_quartz_cron is not None:
            self.use_quartz_cron = use_quartz_cron
        if cron is not None:
            self.cron = cron
        if period is not None:
            self.period = period
        if dispatch_interval is not None:
            self.dispatch_interval = dispatch_interval
        if position is not None:
            self.position = position
        if execute_status is not None:
            self.execute_status = execute_status
        if source_app_id is not None:
            self.source_app_id = source_app_id
        if source_app_name is not None:
            self.source_app_name = source_app_name
        if source_instance_id is not None:
            self.source_instance_id = source_instance_id
        if target_app_id is not None:
            self.target_app_id = target_app_id
        if target_app_name is not None:
            self.target_app_name = target_app_name
        if target_instance_id is not None:
            self.target_instance_id = target_instance_id
        if ext_type is not None:
            self.ext_type = ext_type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if task_tag is not None:
            self.task_tag = task_tag

    @property
    def task_id(self):
        """Gets the task_id of this TaskMonitorInfo.

        任务ID

        :return: The task_id of this TaskMonitorInfo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this TaskMonitorInfo.

        任务ID

        :param task_id: The task_id of this TaskMonitorInfo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        """Gets the task_name of this TaskMonitorInfo.

        任务名称

        :return: The task_name of this TaskMonitorInfo.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this TaskMonitorInfo.

        任务名称

        :param task_name: The task_name of this TaskMonitorInfo.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_type(self):
        """Gets the task_type of this TaskMonitorInfo.

        任务类型, 只允许两种类型:TIMING-定时任务, REALTIME-实时任务

        :return: The task_type of this TaskMonitorInfo.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this TaskMonitorInfo.

        任务类型, 只允许两种类型:TIMING-定时任务, REALTIME-实时任务

        :param task_type: The task_type of this TaskMonitorInfo.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def status(self):
        """Gets the status of this TaskMonitorInfo.

        任务状态, 只允许两种类型:0-停止, 1-运行中

        :return: The status of this TaskMonitorInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskMonitorInfo.

        任务状态, 只允许两种类型:0-停止, 1-运行中

        :param status: The status of this TaskMonitorInfo.
        :type status: int
        """
        self._status = status

    @property
    def last_execute_time(self):
        """Gets the last_execute_time of this TaskMonitorInfo.

        任务最近一次执行时间，格式timestamp(ms)，使用UTC时区

        :return: The last_execute_time of this TaskMonitorInfo.
        :rtype: int
        """
        return self._last_execute_time

    @last_execute_time.setter
    def last_execute_time(self, last_execute_time):
        """Sets the last_execute_time of this TaskMonitorInfo.

        任务最近一次执行时间，格式timestamp(ms)，使用UTC时区

        :param last_execute_time: The last_execute_time of this TaskMonitorInfo.
        :type last_execute_time: int
        """
        self._last_execute_time = last_execute_time

    @property
    def use_quartz_cron(self):
        """Gets the use_quartz_cron of this TaskMonitorInfo.

        任务是否使用Quartz表达式，只有定时任务才有该属性

        :return: The use_quartz_cron of this TaskMonitorInfo.
        :rtype: bool
        """
        return self._use_quartz_cron

    @use_quartz_cron.setter
    def use_quartz_cron(self, use_quartz_cron):
        """Sets the use_quartz_cron of this TaskMonitorInfo.

        任务是否使用Quartz表达式，只有定时任务才有该属性

        :param use_quartz_cron: The use_quartz_cron of this TaskMonitorInfo.
        :type use_quartz_cron: bool
        """
        self._use_quartz_cron = use_quartz_cron

    @property
    def cron(self):
        """Gets the cron of this TaskMonitorInfo.

        CRON表达式，只有定时任务且use_quartz_cron为true时才有该属性

        :return: The cron of this TaskMonitorInfo.
        :rtype: str
        """
        return self._cron

    @cron.setter
    def cron(self, cron):
        """Sets the cron of this TaskMonitorInfo.

        CRON表达式，只有定时任务且use_quartz_cron为true时才有该属性

        :param cron: The cron of this TaskMonitorInfo.
        :type cron: str
        """
        self._cron = cron

    @property
    def period(self):
        """Gets the period of this TaskMonitorInfo.

        调度周期的单位，如天，小时等，只有定时任务且use_quartz_cron为false时才有该属性，当前仅允许如下类型：MIN-分钟, HOUR-小时, DAY-天, WEEK-周, MON-月

        :return: The period of this TaskMonitorInfo.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this TaskMonitorInfo.

        调度周期的单位，如天，小时等，只有定时任务且use_quartz_cron为false时才有该属性，当前仅允许如下类型：MIN-分钟, HOUR-小时, DAY-天, WEEK-周, MON-月

        :param period: The period of this TaskMonitorInfo.
        :type period: str
        """
        self._period = period

    @property
    def dispatch_interval(self):
        """Gets the dispatch_interval of this TaskMonitorInfo.

        调度周期，和period字段一起可以确定每隔多长时间调度一次，只有定时任务且use_quartz_cron为false时才有该属性

        :return: The dispatch_interval of this TaskMonitorInfo.
        :rtype: int
        """
        return self._dispatch_interval

    @dispatch_interval.setter
    def dispatch_interval(self, dispatch_interval):
        """Sets the dispatch_interval of this TaskMonitorInfo.

        调度周期，和period字段一起可以确定每隔多长时间调度一次，只有定时任务且use_quartz_cron为false时才有该属性

        :param dispatch_interval: The dispatch_interval of this TaskMonitorInfo.
        :type dispatch_interval: int
        """
        self._dispatch_interval = dispatch_interval

    @property
    def position(self):
        """Gets the position of this TaskMonitorInfo.

        标识最近一次任务执行到哪一个阶段，允许如下值：ADAPTER-任务处于初始化阶段, READER-任务正在执行Reader读操作, WRITER-任务正在执行Writer写操作

        :return: The position of this TaskMonitorInfo.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this TaskMonitorInfo.

        标识最近一次任务执行到哪一个阶段，允许如下值：ADAPTER-任务处于初始化阶段, READER-任务正在执行Reader读操作, WRITER-任务正在执行Writer写操作

        :param position: The position of this TaskMonitorInfo.
        :type position: str
        """
        self._position = position

    @property
    def execute_status(self):
        """Gets the execute_status of this TaskMonitorInfo.

        任务最近一次执行状态，允许如下值：UNSTARTED-未启动, WAITING-等待调度中, RUNNING-执行中, SUCCESS-执行成功, CANCELLED-任务取消, ERROR-执行异常

        :return: The execute_status of this TaskMonitorInfo.
        :rtype: str
        """
        return self._execute_status

    @execute_status.setter
    def execute_status(self, execute_status):
        """Sets the execute_status of this TaskMonitorInfo.

        任务最近一次执行状态，允许如下值：UNSTARTED-未启动, WAITING-等待调度中, RUNNING-执行中, SUCCESS-执行成功, CANCELLED-任务取消, ERROR-执行异常

        :param execute_status: The execute_status of this TaskMonitorInfo.
        :type execute_status: str
        """
        self._execute_status = execute_status

    @property
    def source_app_id(self):
        """Gets the source_app_id of this TaskMonitorInfo.

        任务源端数据源所属应用ID

        :return: The source_app_id of this TaskMonitorInfo.
        :rtype: str
        """
        return self._source_app_id

    @source_app_id.setter
    def source_app_id(self, source_app_id):
        """Sets the source_app_id of this TaskMonitorInfo.

        任务源端数据源所属应用ID

        :param source_app_id: The source_app_id of this TaskMonitorInfo.
        :type source_app_id: str
        """
        self._source_app_id = source_app_id

    @property
    def source_app_name(self):
        """Gets the source_app_name of this TaskMonitorInfo.

        任务源端数据源所属应用名称

        :return: The source_app_name of this TaskMonitorInfo.
        :rtype: str
        """
        return self._source_app_name

    @source_app_name.setter
    def source_app_name(self, source_app_name):
        """Sets the source_app_name of this TaskMonitorInfo.

        任务源端数据源所属应用名称

        :param source_app_name: The source_app_name of this TaskMonitorInfo.
        :type source_app_name: str
        """
        self._source_app_name = source_app_name

    @property
    def source_instance_id(self):
        """Gets the source_instance_id of this TaskMonitorInfo.

        任务源端数据源所属实例ID

        :return: The source_instance_id of this TaskMonitorInfo.
        :rtype: str
        """
        return self._source_instance_id

    @source_instance_id.setter
    def source_instance_id(self, source_instance_id):
        """Sets the source_instance_id of this TaskMonitorInfo.

        任务源端数据源所属实例ID

        :param source_instance_id: The source_instance_id of this TaskMonitorInfo.
        :type source_instance_id: str
        """
        self._source_instance_id = source_instance_id

    @property
    def target_app_id(self):
        """Gets the target_app_id of this TaskMonitorInfo.

        任务目标端数据源所属应用ID

        :return: The target_app_id of this TaskMonitorInfo.
        :rtype: str
        """
        return self._target_app_id

    @target_app_id.setter
    def target_app_id(self, target_app_id):
        """Sets the target_app_id of this TaskMonitorInfo.

        任务目标端数据源所属应用ID

        :param target_app_id: The target_app_id of this TaskMonitorInfo.
        :type target_app_id: str
        """
        self._target_app_id = target_app_id

    @property
    def target_app_name(self):
        """Gets the target_app_name of this TaskMonitorInfo.

        任务目标端数据源所属应用名称

        :return: The target_app_name of this TaskMonitorInfo.
        :rtype: str
        """
        return self._target_app_name

    @target_app_name.setter
    def target_app_name(self, target_app_name):
        """Sets the target_app_name of this TaskMonitorInfo.

        任务目标端数据源所属应用名称

        :param target_app_name: The target_app_name of this TaskMonitorInfo.
        :type target_app_name: str
        """
        self._target_app_name = target_app_name

    @property
    def target_instance_id(self):
        """Gets the target_instance_id of this TaskMonitorInfo.

        任务目标端数据源所属实例ID

        :return: The target_instance_id of this TaskMonitorInfo.
        :rtype: str
        """
        return self._target_instance_id

    @target_instance_id.setter
    def target_instance_id(self, target_instance_id):
        """Sets the target_instance_id of this TaskMonitorInfo.

        任务目标端数据源所属实例ID

        :param target_instance_id: The target_instance_id of this TaskMonitorInfo.
        :type target_instance_id: str
        """
        self._target_instance_id = target_instance_id

    @property
    def ext_type(self):
        """Gets the ext_type of this TaskMonitorInfo.

        任务扩展类型，当前如果是CDC组合任务，该字段为CDC，否则为null

        :return: The ext_type of this TaskMonitorInfo.
        :rtype: str
        """
        return self._ext_type

    @ext_type.setter
    def ext_type(self, ext_type):
        """Sets the ext_type of this TaskMonitorInfo.

        任务扩展类型，当前如果是CDC组合任务，该字段为CDC，否则为null

        :param ext_type: The ext_type of this TaskMonitorInfo.
        :type ext_type: str
        """
        self._ext_type = ext_type

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this TaskMonitorInfo.

        任务所属企业项目ID，默认为0

        :return: The enterprise_project_id of this TaskMonitorInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this TaskMonitorInfo.

        任务所属企业项目ID，默认为0

        :param enterprise_project_id: The enterprise_project_id of this TaskMonitorInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def task_tag(self):
        """Gets the task_tag of this TaskMonitorInfo.

        任务标签

        :return: The task_tag of this TaskMonitorInfo.
        :rtype: str
        """
        return self._task_tag

    @task_tag.setter
    def task_tag(self, task_tag):
        """Sets the task_tag of this TaskMonitorInfo.

        任务标签

        :param task_tag: The task_tag of this TaskMonitorInfo.
        :type task_tag: str
        """
        self._task_tag = task_tag

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
        if not isinstance(other, TaskMonitorInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
