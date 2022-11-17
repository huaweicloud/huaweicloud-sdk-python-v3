# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SourceServersResponseBody:

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
        'ip': 'str',
        'name': 'str',
        'enterprise_project_id': 'str',
        'add_date': 'int',
        'os_type': 'str',
        'os_version': 'str',
        'oem_system': 'bool',
        'state': 'str',
        'connected': 'bool',
        'cpu_quantity': 'int',
        'memory': 'int',
        'current_task': 'TaskByServerSources',
        'checks': 'list[EnvironmentCheck]',
        'init_target_server': 'InitTargetServer',
        'replicatesize': 'int',
        'stage_action_time': 'int',
        'totalsize': 'int',
        'last_visit_time': 'int',
        'migration_cycle': 'str',
        'state_action_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'ip': 'ip',
        'name': 'name',
        'enterprise_project_id': 'enterprise_project_id',
        'add_date': 'add_date',
        'os_type': 'os_type',
        'os_version': 'os_version',
        'oem_system': 'oem_system',
        'state': 'state',
        'connected': 'connected',
        'cpu_quantity': 'cpu_quantity',
        'memory': 'memory',
        'current_task': 'current_task',
        'checks': 'checks',
        'init_target_server': 'init_target_server',
        'replicatesize': 'replicatesize',
        'stage_action_time': 'stage_action_time',
        'totalsize': 'totalsize',
        'last_visit_time': 'last_visit_time',
        'migration_cycle': 'migration_cycle',
        'state_action_time': 'state_action_time'
    }

    def __init__(self, id=None, ip=None, name=None, enterprise_project_id=None, add_date=None, os_type=None, os_version=None, oem_system=None, state=None, connected=None, cpu_quantity=None, memory=None, current_task=None, checks=None, init_target_server=None, replicatesize=None, stage_action_time=None, totalsize=None, last_visit_time=None, migration_cycle=None, state_action_time=None):
        """SourceServersResponseBody

        The model defined in huaweicloud sdk

        :param id: 源端服务器ID
        :type id: str
        :param ip: 源端服务器的IP地址
        :type ip: str
        :param name: 源端服务器名称
        :type name: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param add_date: 源端服务器的注册时间
        :type add_date: int
        :param os_type: 操作系统类型，OS_TYPE (WINDOWS/LINUX)
        :type os_type: str
        :param os_version: 系统详细版本号，如CENTOS7.6等
        :type os_version: str
        :param oem_system: 是否是OEM操作系统(Windows)
        :type oem_system: bool
        :param state: 源端服务器状态 unavailable：环境校验不通过 waiting：等待 initialize：初始化 replicate：复制 syncing：持续同步 stopping：暂停中 stopped：已暂停 deleting：删除中 error：错误 cloning：等待克隆完成 cutovering：启动目的端中 finished：启动目的端完成
        :type state: str
        :param connected: 源端服务器与主机迁移服务端是否连接
        :type connected: bool
        :param cpu_quantity: 源端CPU核心数
        :type cpu_quantity: int
        :param memory: 源端物理内存大小（单位：字节）
        :type memory: int
        :param current_task: 
        :type current_task: :class:`huaweicloudsdksms.v3.TaskByServerSources`
        :param checks: 源端校验检查项列表
        :type checks: list[:class:`huaweicloudsdksms.v3.EnvironmentCheck`]
        :param init_target_server: 
        :type init_target_server: :class:`huaweicloudsdksms.v3.InitTargetServer`
        :param replicatesize: 已复制的大小（单位：字节）
        :type replicatesize: int
        :param stage_action_time: 迁移周期（migration_cycle）上一次变化的时间
        :type stage_action_time: int
        :param totalsize: 需要迁移的数据量总大小（单位：字节）
        :type totalsize: int
        :param last_visit_time: Agent上一次连接状态发生变化的时间
        :type last_visit_time: int
        :param migration_cycle: 迁移周期 cutovering:启动目的端中 cutovered:启动目的端完成 checking:检查中 setting:设置中 replicating:复制中 syncing:同步中 
        :type migration_cycle: str
        :param state_action_time: 源端状态（state）上次发生变化的时间
        :type state_action_time: int
        """
        
        

        self._id = None
        self._ip = None
        self._name = None
        self._enterprise_project_id = None
        self._add_date = None
        self._os_type = None
        self._os_version = None
        self._oem_system = None
        self._state = None
        self._connected = None
        self._cpu_quantity = None
        self._memory = None
        self._current_task = None
        self._checks = None
        self._init_target_server = None
        self._replicatesize = None
        self._stage_action_time = None
        self._totalsize = None
        self._last_visit_time = None
        self._migration_cycle = None
        self._state_action_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if ip is not None:
            self.ip = ip
        if name is not None:
            self.name = name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if add_date is not None:
            self.add_date = add_date
        if os_type is not None:
            self.os_type = os_type
        if os_version is not None:
            self.os_version = os_version
        if oem_system is not None:
            self.oem_system = oem_system
        if state is not None:
            self.state = state
        if connected is not None:
            self.connected = connected
        if cpu_quantity is not None:
            self.cpu_quantity = cpu_quantity
        if memory is not None:
            self.memory = memory
        if current_task is not None:
            self.current_task = current_task
        if checks is not None:
            self.checks = checks
        if init_target_server is not None:
            self.init_target_server = init_target_server
        if replicatesize is not None:
            self.replicatesize = replicatesize
        if stage_action_time is not None:
            self.stage_action_time = stage_action_time
        if totalsize is not None:
            self.totalsize = totalsize
        if last_visit_time is not None:
            self.last_visit_time = last_visit_time
        if migration_cycle is not None:
            self.migration_cycle = migration_cycle
        if state_action_time is not None:
            self.state_action_time = state_action_time

    @property
    def id(self):
        """Gets the id of this SourceServersResponseBody.

        源端服务器ID

        :return: The id of this SourceServersResponseBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SourceServersResponseBody.

        源端服务器ID

        :param id: The id of this SourceServersResponseBody.
        :type id: str
        """
        self._id = id

    @property
    def ip(self):
        """Gets the ip of this SourceServersResponseBody.

        源端服务器的IP地址

        :return: The ip of this SourceServersResponseBody.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this SourceServersResponseBody.

        源端服务器的IP地址

        :param ip: The ip of this SourceServersResponseBody.
        :type ip: str
        """
        self._ip = ip

    @property
    def name(self):
        """Gets the name of this SourceServersResponseBody.

        源端服务器名称

        :return: The name of this SourceServersResponseBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SourceServersResponseBody.

        源端服务器名称

        :param name: The name of this SourceServersResponseBody.
        :type name: str
        """
        self._name = name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this SourceServersResponseBody.

        企业项目ID

        :return: The enterprise_project_id of this SourceServersResponseBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this SourceServersResponseBody.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this SourceServersResponseBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def add_date(self):
        """Gets the add_date of this SourceServersResponseBody.

        源端服务器的注册时间

        :return: The add_date of this SourceServersResponseBody.
        :rtype: int
        """
        return self._add_date

    @add_date.setter
    def add_date(self, add_date):
        """Sets the add_date of this SourceServersResponseBody.

        源端服务器的注册时间

        :param add_date: The add_date of this SourceServersResponseBody.
        :type add_date: int
        """
        self._add_date = add_date

    @property
    def os_type(self):
        """Gets the os_type of this SourceServersResponseBody.

        操作系统类型，OS_TYPE (WINDOWS/LINUX)

        :return: The os_type of this SourceServersResponseBody.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this SourceServersResponseBody.

        操作系统类型，OS_TYPE (WINDOWS/LINUX)

        :param os_type: The os_type of this SourceServersResponseBody.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def os_version(self):
        """Gets the os_version of this SourceServersResponseBody.

        系统详细版本号，如CENTOS7.6等

        :return: The os_version of this SourceServersResponseBody.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this SourceServersResponseBody.

        系统详细版本号，如CENTOS7.6等

        :param os_version: The os_version of this SourceServersResponseBody.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def oem_system(self):
        """Gets the oem_system of this SourceServersResponseBody.

        是否是OEM操作系统(Windows)

        :return: The oem_system of this SourceServersResponseBody.
        :rtype: bool
        """
        return self._oem_system

    @oem_system.setter
    def oem_system(self, oem_system):
        """Sets the oem_system of this SourceServersResponseBody.

        是否是OEM操作系统(Windows)

        :param oem_system: The oem_system of this SourceServersResponseBody.
        :type oem_system: bool
        """
        self._oem_system = oem_system

    @property
    def state(self):
        """Gets the state of this SourceServersResponseBody.

        源端服务器状态 unavailable：环境校验不通过 waiting：等待 initialize：初始化 replicate：复制 syncing：持续同步 stopping：暂停中 stopped：已暂停 deleting：删除中 error：错误 cloning：等待克隆完成 cutovering：启动目的端中 finished：启动目的端完成

        :return: The state of this SourceServersResponseBody.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SourceServersResponseBody.

        源端服务器状态 unavailable：环境校验不通过 waiting：等待 initialize：初始化 replicate：复制 syncing：持续同步 stopping：暂停中 stopped：已暂停 deleting：删除中 error：错误 cloning：等待克隆完成 cutovering：启动目的端中 finished：启动目的端完成

        :param state: The state of this SourceServersResponseBody.
        :type state: str
        """
        self._state = state

    @property
    def connected(self):
        """Gets the connected of this SourceServersResponseBody.

        源端服务器与主机迁移服务端是否连接

        :return: The connected of this SourceServersResponseBody.
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """Sets the connected of this SourceServersResponseBody.

        源端服务器与主机迁移服务端是否连接

        :param connected: The connected of this SourceServersResponseBody.
        :type connected: bool
        """
        self._connected = connected

    @property
    def cpu_quantity(self):
        """Gets the cpu_quantity of this SourceServersResponseBody.

        源端CPU核心数

        :return: The cpu_quantity of this SourceServersResponseBody.
        :rtype: int
        """
        return self._cpu_quantity

    @cpu_quantity.setter
    def cpu_quantity(self, cpu_quantity):
        """Sets the cpu_quantity of this SourceServersResponseBody.

        源端CPU核心数

        :param cpu_quantity: The cpu_quantity of this SourceServersResponseBody.
        :type cpu_quantity: int
        """
        self._cpu_quantity = cpu_quantity

    @property
    def memory(self):
        """Gets the memory of this SourceServersResponseBody.

        源端物理内存大小（单位：字节）

        :return: The memory of this SourceServersResponseBody.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this SourceServersResponseBody.

        源端物理内存大小（单位：字节）

        :param memory: The memory of this SourceServersResponseBody.
        :type memory: int
        """
        self._memory = memory

    @property
    def current_task(self):
        """Gets the current_task of this SourceServersResponseBody.

        :return: The current_task of this SourceServersResponseBody.
        :rtype: :class:`huaweicloudsdksms.v3.TaskByServerSources`
        """
        return self._current_task

    @current_task.setter
    def current_task(self, current_task):
        """Sets the current_task of this SourceServersResponseBody.

        :param current_task: The current_task of this SourceServersResponseBody.
        :type current_task: :class:`huaweicloudsdksms.v3.TaskByServerSources`
        """
        self._current_task = current_task

    @property
    def checks(self):
        """Gets the checks of this SourceServersResponseBody.

        源端校验检查项列表

        :return: The checks of this SourceServersResponseBody.
        :rtype: list[:class:`huaweicloudsdksms.v3.EnvironmentCheck`]
        """
        return self._checks

    @checks.setter
    def checks(self, checks):
        """Sets the checks of this SourceServersResponseBody.

        源端校验检查项列表

        :param checks: The checks of this SourceServersResponseBody.
        :type checks: list[:class:`huaweicloudsdksms.v3.EnvironmentCheck`]
        """
        self._checks = checks

    @property
    def init_target_server(self):
        """Gets the init_target_server of this SourceServersResponseBody.

        :return: The init_target_server of this SourceServersResponseBody.
        :rtype: :class:`huaweicloudsdksms.v3.InitTargetServer`
        """
        return self._init_target_server

    @init_target_server.setter
    def init_target_server(self, init_target_server):
        """Sets the init_target_server of this SourceServersResponseBody.

        :param init_target_server: The init_target_server of this SourceServersResponseBody.
        :type init_target_server: :class:`huaweicloudsdksms.v3.InitTargetServer`
        """
        self._init_target_server = init_target_server

    @property
    def replicatesize(self):
        """Gets the replicatesize of this SourceServersResponseBody.

        已复制的大小（单位：字节）

        :return: The replicatesize of this SourceServersResponseBody.
        :rtype: int
        """
        return self._replicatesize

    @replicatesize.setter
    def replicatesize(self, replicatesize):
        """Sets the replicatesize of this SourceServersResponseBody.

        已复制的大小（单位：字节）

        :param replicatesize: The replicatesize of this SourceServersResponseBody.
        :type replicatesize: int
        """
        self._replicatesize = replicatesize

    @property
    def stage_action_time(self):
        """Gets the stage_action_time of this SourceServersResponseBody.

        迁移周期（migration_cycle）上一次变化的时间

        :return: The stage_action_time of this SourceServersResponseBody.
        :rtype: int
        """
        return self._stage_action_time

    @stage_action_time.setter
    def stage_action_time(self, stage_action_time):
        """Sets the stage_action_time of this SourceServersResponseBody.

        迁移周期（migration_cycle）上一次变化的时间

        :param stage_action_time: The stage_action_time of this SourceServersResponseBody.
        :type stage_action_time: int
        """
        self._stage_action_time = stage_action_time

    @property
    def totalsize(self):
        """Gets the totalsize of this SourceServersResponseBody.

        需要迁移的数据量总大小（单位：字节）

        :return: The totalsize of this SourceServersResponseBody.
        :rtype: int
        """
        return self._totalsize

    @totalsize.setter
    def totalsize(self, totalsize):
        """Sets the totalsize of this SourceServersResponseBody.

        需要迁移的数据量总大小（单位：字节）

        :param totalsize: The totalsize of this SourceServersResponseBody.
        :type totalsize: int
        """
        self._totalsize = totalsize

    @property
    def last_visit_time(self):
        """Gets the last_visit_time of this SourceServersResponseBody.

        Agent上一次连接状态发生变化的时间

        :return: The last_visit_time of this SourceServersResponseBody.
        :rtype: int
        """
        return self._last_visit_time

    @last_visit_time.setter
    def last_visit_time(self, last_visit_time):
        """Sets the last_visit_time of this SourceServersResponseBody.

        Agent上一次连接状态发生变化的时间

        :param last_visit_time: The last_visit_time of this SourceServersResponseBody.
        :type last_visit_time: int
        """
        self._last_visit_time = last_visit_time

    @property
    def migration_cycle(self):
        """Gets the migration_cycle of this SourceServersResponseBody.

        迁移周期 cutovering:启动目的端中 cutovered:启动目的端完成 checking:检查中 setting:设置中 replicating:复制中 syncing:同步中 

        :return: The migration_cycle of this SourceServersResponseBody.
        :rtype: str
        """
        return self._migration_cycle

    @migration_cycle.setter
    def migration_cycle(self, migration_cycle):
        """Sets the migration_cycle of this SourceServersResponseBody.

        迁移周期 cutovering:启动目的端中 cutovered:启动目的端完成 checking:检查中 setting:设置中 replicating:复制中 syncing:同步中 

        :param migration_cycle: The migration_cycle of this SourceServersResponseBody.
        :type migration_cycle: str
        """
        self._migration_cycle = migration_cycle

    @property
    def state_action_time(self):
        """Gets the state_action_time of this SourceServersResponseBody.

        源端状态（state）上次发生变化的时间

        :return: The state_action_time of this SourceServersResponseBody.
        :rtype: int
        """
        return self._state_action_time

    @state_action_time.setter
    def state_action_time(self, state_action_time):
        """Sets the state_action_time of this SourceServersResponseBody.

        源端状态（state）上次发生变化的时间

        :param state_action_time: The state_action_time of this SourceServersResponseBody.
        :type state_action_time: int
        """
        self._state_action_time = state_action_time

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
        if not isinstance(other, SourceServersResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
