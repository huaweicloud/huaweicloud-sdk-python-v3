# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowServerResponse(SdkResponse):

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
        'hostname': 'str',
        'enterprise_project_id': 'str',
        'add_date': 'int',
        'os_type': 'str',
        'os_version': 'str',
        'oem_system': 'bool',
        'state': 'str',
        'connected': 'bool',
        'firmware': 'str',
        'init_target_server': 'InitTargetServer',
        'cpu_quantity': 'int',
        'memory': 'int',
        'current_task': 'TaskByServerSource',
        'disks': 'list[ServerDisk]',
        'volume_groups': 'list[VolumeGroups]',
        'btrfs_list': 'list[BtrfsFileSystem]',
        'networks': 'list[NetWork]',
        'checks': 'list[EnvironmentCheck]',
        'migration_cycle': 'str',
        'state_action_time': 'int',
        'replicatesize': 'int',
        'totalsize': 'int',
        'last_visit_time': 'int',
        'stage_action_time': 'int',
        'agent_version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'ip': 'ip',
        'name': 'name',
        'hostname': 'hostname',
        'enterprise_project_id': 'enterprise_project_id',
        'add_date': 'add_date',
        'os_type': 'os_type',
        'os_version': 'os_version',
        'oem_system': 'oem_system',
        'state': 'state',
        'connected': 'connected',
        'firmware': 'firmware',
        'init_target_server': 'init_target_server',
        'cpu_quantity': 'cpu_quantity',
        'memory': 'memory',
        'current_task': 'current_task',
        'disks': 'disks',
        'volume_groups': 'volume_groups',
        'btrfs_list': 'btrfs_list',
        'networks': 'networks',
        'checks': 'checks',
        'migration_cycle': 'migration_cycle',
        'state_action_time': 'state_action_time',
        'replicatesize': 'replicatesize',
        'totalsize': 'totalsize',
        'last_visit_time': 'last_visit_time',
        'stage_action_time': 'stage_action_time',
        'agent_version': 'agent_version'
    }

    def __init__(self, id=None, ip=None, name=None, hostname=None, enterprise_project_id=None, add_date=None, os_type=None, os_version=None, oem_system=None, state=None, connected=None, firmware=None, init_target_server=None, cpu_quantity=None, memory=None, current_task=None, disks=None, volume_groups=None, btrfs_list=None, networks=None, checks=None, migration_cycle=None, state_action_time=None, replicatesize=None, totalsize=None, last_visit_time=None, stage_action_time=None, agent_version=None):
        """ShowServerResponse

        The model defined in huaweicloud sdk

        :param id: 源端服务器ID
        :type id: str
        :param ip: 源端服务器的IP
        :type ip: str
        :param name: 用来区分不同源端服务器的名称
        :type name: str
        :param hostname: 源端主机名，注册源端必选，更新非必选
        :type hostname: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param add_date: 源端服务器注册的时间
        :type add_date: int
        :param os_type: 源端服务器的OS类型，分为Windows和Linux，注册必选，更新非必选
        :type os_type: str
        :param os_version: 操作系统版本，注册必选，更新非必选
        :type os_version: str
        :param oem_system: 是否是OEM操作系统(Windows)
        :type oem_system: bool
        :param state: 当前源端服务器状态 unavailable：环境校验不通过 waiting：等待 initialize：初始化 replicate：复制 syncing：持续同步 stopping：暂停中 stopped：已暂停 deleting：删除中 error：错误 cloning：等待克隆完成 testing：测试中 finished：启动目的端完成
        :type state: str
        :param connected: 与Agent连接状态
        :type connected: bool
        :param firmware: 源端服务器启动类型，如BIOS或者UEFI
        :type firmware: str
        :param init_target_server: 
        :type init_target_server: :class:`huaweicloudsdksms.v3.InitTargetServer`
        :param cpu_quantity: 源端CPU核心数
        :type cpu_quantity: int
        :param memory: 源端服务器物理内存大小，单位MB
        :type memory: int
        :param current_task: 
        :type current_task: :class:`huaweicloudsdksms.v3.TaskByServerSource`
        :param disks: 源端服务器磁盘信息
        :type disks: list[:class:`huaweicloudsdksms.v3.ServerDisk`]
        :param volume_groups: 源端服务器的卷组信息，Linux必选，如果没有卷组，输入[]
        :type volume_groups: list[:class:`huaweicloudsdksms.v3.VolumeGroups`]
        :param btrfs_list: Linux 必选，源端的Btrfs信息。如果源端不存在Btrfs，则为[]
        :type btrfs_list: list[:class:`huaweicloudsdksms.v3.BtrfsFileSystem`]
        :param networks: 源端服务器的网卡信息
        :type networks: list[:class:`huaweicloudsdksms.v3.NetWork`]
        :param checks: 源端环境校验信息
        :type checks: list[:class:`huaweicloudsdksms.v3.EnvironmentCheck`]
        :param migration_cycle: 迁移周期 cutovering:启动目的端中 cutovered:启动目的端完成 checking:检查中 setting:设置中 replicating:复制中 syncing:同步中 
        :type migration_cycle: str
        :param state_action_time: 源端状态（state）上次发生变化的时间戳
        :type state_action_time: int
        :param replicatesize: 已经完成迁移的大小（B）
        :type replicatesize: int
        :param totalsize: 需要迁移的数据量总大小（B）
        :type totalsize: int
        :param last_visit_time: agent上一次连接状态发生变化的时间戳
        :type last_visit_time: int
        :param stage_action_time: 迁移周期（migration_cycle）上一次变化的时间戳
        :type stage_action_time: int
        :param agent_version: Agent版本信息
        :type agent_version: str
        """
        
        super(ShowServerResponse, self).__init__()

        self._id = None
        self._ip = None
        self._name = None
        self._hostname = None
        self._enterprise_project_id = None
        self._add_date = None
        self._os_type = None
        self._os_version = None
        self._oem_system = None
        self._state = None
        self._connected = None
        self._firmware = None
        self._init_target_server = None
        self._cpu_quantity = None
        self._memory = None
        self._current_task = None
        self._disks = None
        self._volume_groups = None
        self._btrfs_list = None
        self._networks = None
        self._checks = None
        self._migration_cycle = None
        self._state_action_time = None
        self._replicatesize = None
        self._totalsize = None
        self._last_visit_time = None
        self._stage_action_time = None
        self._agent_version = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if ip is not None:
            self.ip = ip
        if name is not None:
            self.name = name
        if hostname is not None:
            self.hostname = hostname
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
        if firmware is not None:
            self.firmware = firmware
        if init_target_server is not None:
            self.init_target_server = init_target_server
        if cpu_quantity is not None:
            self.cpu_quantity = cpu_quantity
        if memory is not None:
            self.memory = memory
        if current_task is not None:
            self.current_task = current_task
        if disks is not None:
            self.disks = disks
        if volume_groups is not None:
            self.volume_groups = volume_groups
        if btrfs_list is not None:
            self.btrfs_list = btrfs_list
        if networks is not None:
            self.networks = networks
        if checks is not None:
            self.checks = checks
        if migration_cycle is not None:
            self.migration_cycle = migration_cycle
        if state_action_time is not None:
            self.state_action_time = state_action_time
        if replicatesize is not None:
            self.replicatesize = replicatesize
        if totalsize is not None:
            self.totalsize = totalsize
        if last_visit_time is not None:
            self.last_visit_time = last_visit_time
        if stage_action_time is not None:
            self.stage_action_time = stage_action_time
        if agent_version is not None:
            self.agent_version = agent_version

    @property
    def id(self):
        """Gets the id of this ShowServerResponse.

        源端服务器ID

        :return: The id of this ShowServerResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowServerResponse.

        源端服务器ID

        :param id: The id of this ShowServerResponse.
        :type id: str
        """
        self._id = id

    @property
    def ip(self):
        """Gets the ip of this ShowServerResponse.

        源端服务器的IP

        :return: The ip of this ShowServerResponse.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ShowServerResponse.

        源端服务器的IP

        :param ip: The ip of this ShowServerResponse.
        :type ip: str
        """
        self._ip = ip

    @property
    def name(self):
        """Gets the name of this ShowServerResponse.

        用来区分不同源端服务器的名称

        :return: The name of this ShowServerResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowServerResponse.

        用来区分不同源端服务器的名称

        :param name: The name of this ShowServerResponse.
        :type name: str
        """
        self._name = name

    @property
    def hostname(self):
        """Gets the hostname of this ShowServerResponse.

        源端主机名，注册源端必选，更新非必选

        :return: The hostname of this ShowServerResponse.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this ShowServerResponse.

        源端主机名，注册源端必选，更新非必选

        :param hostname: The hostname of this ShowServerResponse.
        :type hostname: str
        """
        self._hostname = hostname

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowServerResponse.

        企业项目ID

        :return: The enterprise_project_id of this ShowServerResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowServerResponse.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ShowServerResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def add_date(self):
        """Gets the add_date of this ShowServerResponse.

        源端服务器注册的时间

        :return: The add_date of this ShowServerResponse.
        :rtype: int
        """
        return self._add_date

    @add_date.setter
    def add_date(self, add_date):
        """Sets the add_date of this ShowServerResponse.

        源端服务器注册的时间

        :param add_date: The add_date of this ShowServerResponse.
        :type add_date: int
        """
        self._add_date = add_date

    @property
    def os_type(self):
        """Gets the os_type of this ShowServerResponse.

        源端服务器的OS类型，分为Windows和Linux，注册必选，更新非必选

        :return: The os_type of this ShowServerResponse.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this ShowServerResponse.

        源端服务器的OS类型，分为Windows和Linux，注册必选，更新非必选

        :param os_type: The os_type of this ShowServerResponse.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def os_version(self):
        """Gets the os_version of this ShowServerResponse.

        操作系统版本，注册必选，更新非必选

        :return: The os_version of this ShowServerResponse.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this ShowServerResponse.

        操作系统版本，注册必选，更新非必选

        :param os_version: The os_version of this ShowServerResponse.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def oem_system(self):
        """Gets the oem_system of this ShowServerResponse.

        是否是OEM操作系统(Windows)

        :return: The oem_system of this ShowServerResponse.
        :rtype: bool
        """
        return self._oem_system

    @oem_system.setter
    def oem_system(self, oem_system):
        """Sets the oem_system of this ShowServerResponse.

        是否是OEM操作系统(Windows)

        :param oem_system: The oem_system of this ShowServerResponse.
        :type oem_system: bool
        """
        self._oem_system = oem_system

    @property
    def state(self):
        """Gets the state of this ShowServerResponse.

        当前源端服务器状态 unavailable：环境校验不通过 waiting：等待 initialize：初始化 replicate：复制 syncing：持续同步 stopping：暂停中 stopped：已暂停 deleting：删除中 error：错误 cloning：等待克隆完成 testing：测试中 finished：启动目的端完成

        :return: The state of this ShowServerResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShowServerResponse.

        当前源端服务器状态 unavailable：环境校验不通过 waiting：等待 initialize：初始化 replicate：复制 syncing：持续同步 stopping：暂停中 stopped：已暂停 deleting：删除中 error：错误 cloning：等待克隆完成 testing：测试中 finished：启动目的端完成

        :param state: The state of this ShowServerResponse.
        :type state: str
        """
        self._state = state

    @property
    def connected(self):
        """Gets the connected of this ShowServerResponse.

        与Agent连接状态

        :return: The connected of this ShowServerResponse.
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """Sets the connected of this ShowServerResponse.

        与Agent连接状态

        :param connected: The connected of this ShowServerResponse.
        :type connected: bool
        """
        self._connected = connected

    @property
    def firmware(self):
        """Gets the firmware of this ShowServerResponse.

        源端服务器启动类型，如BIOS或者UEFI

        :return: The firmware of this ShowServerResponse.
        :rtype: str
        """
        return self._firmware

    @firmware.setter
    def firmware(self, firmware):
        """Sets the firmware of this ShowServerResponse.

        源端服务器启动类型，如BIOS或者UEFI

        :param firmware: The firmware of this ShowServerResponse.
        :type firmware: str
        """
        self._firmware = firmware

    @property
    def init_target_server(self):
        """Gets the init_target_server of this ShowServerResponse.

        :return: The init_target_server of this ShowServerResponse.
        :rtype: :class:`huaweicloudsdksms.v3.InitTargetServer`
        """
        return self._init_target_server

    @init_target_server.setter
    def init_target_server(self, init_target_server):
        """Sets the init_target_server of this ShowServerResponse.

        :param init_target_server: The init_target_server of this ShowServerResponse.
        :type init_target_server: :class:`huaweicloudsdksms.v3.InitTargetServer`
        """
        self._init_target_server = init_target_server

    @property
    def cpu_quantity(self):
        """Gets the cpu_quantity of this ShowServerResponse.

        源端CPU核心数

        :return: The cpu_quantity of this ShowServerResponse.
        :rtype: int
        """
        return self._cpu_quantity

    @cpu_quantity.setter
    def cpu_quantity(self, cpu_quantity):
        """Sets the cpu_quantity of this ShowServerResponse.

        源端CPU核心数

        :param cpu_quantity: The cpu_quantity of this ShowServerResponse.
        :type cpu_quantity: int
        """
        self._cpu_quantity = cpu_quantity

    @property
    def memory(self):
        """Gets the memory of this ShowServerResponse.

        源端服务器物理内存大小，单位MB

        :return: The memory of this ShowServerResponse.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this ShowServerResponse.

        源端服务器物理内存大小，单位MB

        :param memory: The memory of this ShowServerResponse.
        :type memory: int
        """
        self._memory = memory

    @property
    def current_task(self):
        """Gets the current_task of this ShowServerResponse.

        :return: The current_task of this ShowServerResponse.
        :rtype: :class:`huaweicloudsdksms.v3.TaskByServerSource`
        """
        return self._current_task

    @current_task.setter
    def current_task(self, current_task):
        """Sets the current_task of this ShowServerResponse.

        :param current_task: The current_task of this ShowServerResponse.
        :type current_task: :class:`huaweicloudsdksms.v3.TaskByServerSource`
        """
        self._current_task = current_task

    @property
    def disks(self):
        """Gets the disks of this ShowServerResponse.

        源端服务器磁盘信息

        :return: The disks of this ShowServerResponse.
        :rtype: list[:class:`huaweicloudsdksms.v3.ServerDisk`]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this ShowServerResponse.

        源端服务器磁盘信息

        :param disks: The disks of this ShowServerResponse.
        :type disks: list[:class:`huaweicloudsdksms.v3.ServerDisk`]
        """
        self._disks = disks

    @property
    def volume_groups(self):
        """Gets the volume_groups of this ShowServerResponse.

        源端服务器的卷组信息，Linux必选，如果没有卷组，输入[]

        :return: The volume_groups of this ShowServerResponse.
        :rtype: list[:class:`huaweicloudsdksms.v3.VolumeGroups`]
        """
        return self._volume_groups

    @volume_groups.setter
    def volume_groups(self, volume_groups):
        """Sets the volume_groups of this ShowServerResponse.

        源端服务器的卷组信息，Linux必选，如果没有卷组，输入[]

        :param volume_groups: The volume_groups of this ShowServerResponse.
        :type volume_groups: list[:class:`huaweicloudsdksms.v3.VolumeGroups`]
        """
        self._volume_groups = volume_groups

    @property
    def btrfs_list(self):
        """Gets the btrfs_list of this ShowServerResponse.

        Linux 必选，源端的Btrfs信息。如果源端不存在Btrfs，则为[]

        :return: The btrfs_list of this ShowServerResponse.
        :rtype: list[:class:`huaweicloudsdksms.v3.BtrfsFileSystem`]
        """
        return self._btrfs_list

    @btrfs_list.setter
    def btrfs_list(self, btrfs_list):
        """Sets the btrfs_list of this ShowServerResponse.

        Linux 必选，源端的Btrfs信息。如果源端不存在Btrfs，则为[]

        :param btrfs_list: The btrfs_list of this ShowServerResponse.
        :type btrfs_list: list[:class:`huaweicloudsdksms.v3.BtrfsFileSystem`]
        """
        self._btrfs_list = btrfs_list

    @property
    def networks(self):
        """Gets the networks of this ShowServerResponse.

        源端服务器的网卡信息

        :return: The networks of this ShowServerResponse.
        :rtype: list[:class:`huaweicloudsdksms.v3.NetWork`]
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        """Sets the networks of this ShowServerResponse.

        源端服务器的网卡信息

        :param networks: The networks of this ShowServerResponse.
        :type networks: list[:class:`huaweicloudsdksms.v3.NetWork`]
        """
        self._networks = networks

    @property
    def checks(self):
        """Gets the checks of this ShowServerResponse.

        源端环境校验信息

        :return: The checks of this ShowServerResponse.
        :rtype: list[:class:`huaweicloudsdksms.v3.EnvironmentCheck`]
        """
        return self._checks

    @checks.setter
    def checks(self, checks):
        """Sets the checks of this ShowServerResponse.

        源端环境校验信息

        :param checks: The checks of this ShowServerResponse.
        :type checks: list[:class:`huaweicloudsdksms.v3.EnvironmentCheck`]
        """
        self._checks = checks

    @property
    def migration_cycle(self):
        """Gets the migration_cycle of this ShowServerResponse.

        迁移周期 cutovering:启动目的端中 cutovered:启动目的端完成 checking:检查中 setting:设置中 replicating:复制中 syncing:同步中 

        :return: The migration_cycle of this ShowServerResponse.
        :rtype: str
        """
        return self._migration_cycle

    @migration_cycle.setter
    def migration_cycle(self, migration_cycle):
        """Sets the migration_cycle of this ShowServerResponse.

        迁移周期 cutovering:启动目的端中 cutovered:启动目的端完成 checking:检查中 setting:设置中 replicating:复制中 syncing:同步中 

        :param migration_cycle: The migration_cycle of this ShowServerResponse.
        :type migration_cycle: str
        """
        self._migration_cycle = migration_cycle

    @property
    def state_action_time(self):
        """Gets the state_action_time of this ShowServerResponse.

        源端状态（state）上次发生变化的时间戳

        :return: The state_action_time of this ShowServerResponse.
        :rtype: int
        """
        return self._state_action_time

    @state_action_time.setter
    def state_action_time(self, state_action_time):
        """Sets the state_action_time of this ShowServerResponse.

        源端状态（state）上次发生变化的时间戳

        :param state_action_time: The state_action_time of this ShowServerResponse.
        :type state_action_time: int
        """
        self._state_action_time = state_action_time

    @property
    def replicatesize(self):
        """Gets the replicatesize of this ShowServerResponse.

        已经完成迁移的大小（B）

        :return: The replicatesize of this ShowServerResponse.
        :rtype: int
        """
        return self._replicatesize

    @replicatesize.setter
    def replicatesize(self, replicatesize):
        """Sets the replicatesize of this ShowServerResponse.

        已经完成迁移的大小（B）

        :param replicatesize: The replicatesize of this ShowServerResponse.
        :type replicatesize: int
        """
        self._replicatesize = replicatesize

    @property
    def totalsize(self):
        """Gets the totalsize of this ShowServerResponse.

        需要迁移的数据量总大小（B）

        :return: The totalsize of this ShowServerResponse.
        :rtype: int
        """
        return self._totalsize

    @totalsize.setter
    def totalsize(self, totalsize):
        """Sets the totalsize of this ShowServerResponse.

        需要迁移的数据量总大小（B）

        :param totalsize: The totalsize of this ShowServerResponse.
        :type totalsize: int
        """
        self._totalsize = totalsize

    @property
    def last_visit_time(self):
        """Gets the last_visit_time of this ShowServerResponse.

        agent上一次连接状态发生变化的时间戳

        :return: The last_visit_time of this ShowServerResponse.
        :rtype: int
        """
        return self._last_visit_time

    @last_visit_time.setter
    def last_visit_time(self, last_visit_time):
        """Sets the last_visit_time of this ShowServerResponse.

        agent上一次连接状态发生变化的时间戳

        :param last_visit_time: The last_visit_time of this ShowServerResponse.
        :type last_visit_time: int
        """
        self._last_visit_time = last_visit_time

    @property
    def stage_action_time(self):
        """Gets the stage_action_time of this ShowServerResponse.

        迁移周期（migration_cycle）上一次变化的时间戳

        :return: The stage_action_time of this ShowServerResponse.
        :rtype: int
        """
        return self._stage_action_time

    @stage_action_time.setter
    def stage_action_time(self, stage_action_time):
        """Sets the stage_action_time of this ShowServerResponse.

        迁移周期（migration_cycle）上一次变化的时间戳

        :param stage_action_time: The stage_action_time of this ShowServerResponse.
        :type stage_action_time: int
        """
        self._stage_action_time = stage_action_time

    @property
    def agent_version(self):
        """Gets the agent_version of this ShowServerResponse.

        Agent版本信息

        :return: The agent_version of this ShowServerResponse.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        """Sets the agent_version of this ShowServerResponse.

        Agent版本信息

        :param agent_version: The agent_version of this ShowServerResponse.
        :type agent_version: str
        """
        self._agent_version = agent_version

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
        if not isinstance(other, ShowServerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
