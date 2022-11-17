# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostSourceServerBody:

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
        'os_type': 'str',
        'os_version': 'str',
        'virtualization_type': 'str',
        'linux_block_check': 'str',
        'firmware': 'str',
        'cpu_quantity': 'int',
        'memory': 'int',
        'disks': 'list[ServerDisk]',
        'btrfs_list': 'list[BtrfsFileSystem]',
        'networks': 'list[NetWork]',
        'domain_id': 'str',
        'has_rsync': 'bool',
        'paravirtualization': 'bool',
        'raw_devices': 'str',
        'driver_files': 'bool',
        'system_services': 'bool',
        'account_rights': 'bool',
        'boot_loader': 'str',
        'system_dir': 'str',
        'volume_groups': 'list[VolumeGroups]',
        'agent_version': 'str',
        'kernel_version': 'str',
        'migration_cycle': 'str',
        'state': 'str',
        'oem_system': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'ip': 'ip',
        'name': 'name',
        'hostname': 'hostname',
        'os_type': 'os_type',
        'os_version': 'os_version',
        'virtualization_type': 'virtualization_type',
        'linux_block_check': 'linux_block_check',
        'firmware': 'firmware',
        'cpu_quantity': 'cpu_quantity',
        'memory': 'memory',
        'disks': 'disks',
        'btrfs_list': 'btrfs_list',
        'networks': 'networks',
        'domain_id': 'domain_id',
        'has_rsync': 'has_rsync',
        'paravirtualization': 'paravirtualization',
        'raw_devices': 'raw_devices',
        'driver_files': 'driver_files',
        'system_services': 'system_services',
        'account_rights': 'account_rights',
        'boot_loader': 'boot_loader',
        'system_dir': 'system_dir',
        'volume_groups': 'volume_groups',
        'agent_version': 'agent_version',
        'kernel_version': 'kernel_version',
        'migration_cycle': 'migration_cycle',
        'state': 'state',
        'oem_system': 'oem_system'
    }

    def __init__(self, id=None, ip=None, name=None, hostname=None, os_type=None, os_version=None, virtualization_type=None, linux_block_check=None, firmware=None, cpu_quantity=None, memory=None, disks=None, btrfs_list=None, networks=None, domain_id=None, has_rsync=None, paravirtualization=None, raw_devices=None, driver_files=None, system_services=None, account_rights=None, boot_loader=None, system_dir=None, volume_groups=None, agent_version=None, kernel_version=None, migration_cycle=None, state=None, oem_system=None):
        """PostSourceServerBody

        The model defined in huaweicloud sdk

        :param id: 源端在SMS数据库中的ID
        :type id: str
        :param ip: 源端服务器ip，注册源端时必选，更新非必选
        :type ip: str
        :param name: 用来区分不同源端服务器的名称
        :type name: str
        :param hostname: 源端主机名，注册源端必选，更新非必选
        :type hostname: str
        :param os_type: 源端服务器的OS类型，分为Windows和Linux，注册必选，更新非必选
        :type os_type: str
        :param os_version: 操作系统版本，注册必选，更新非必选
        :type os_version: str
        :param virtualization_type: 操作系统虚拟化方式
        :type virtualization_type: str
        :param linux_block_check: Linux操作系统块检查
        :type linux_block_check: str
        :param firmware: 源端服务器启动类型，如BIOS或者UEFI
        :type firmware: str
        :param cpu_quantity: CPU个数，单位vCPU
        :type cpu_quantity: int
        :param memory: 内存大小，单位MB
        :type memory: int
        :param disks: 源端服务器的磁盘信息
        :type disks: list[:class:`huaweicloudsdksms.v3.ServerDisk`]
        :param btrfs_list: Linux 必选，源端的Btrfs信息。如果源端不存在Btrfs，则为[]
        :type btrfs_list: list[:class:`huaweicloudsdksms.v3.BtrfsFileSystem`]
        :param networks: 源端服务器的网卡信息
        :type networks: list[:class:`huaweicloudsdksms.v3.NetWork`]
        :param domain_id: 租户的domainId
        :type domain_id: str
        :param has_rsync: 是否安装rsync组件，Linux系统此参数为必选
        :type has_rsync: bool
        :param paravirtualization: Linux场景必选，源端是否是半虚拟化
        :type paravirtualization: bool
        :param raw_devices: Linux必选，裸设备列表
        :type raw_devices: str
        :param driver_files: Windows 必选，是否缺少驱动文件
        :type driver_files: bool
        :param system_services: Windows必选，是否存在不正常服务
        :type system_services: bool
        :param account_rights: Windows必选，权限是否满足要求
        :type account_rights: bool
        :param boot_loader: Linux必选，系统引导类型，BOOT_LOADER(GRUB/LILO)
        :type boot_loader: str
        :param system_dir: Windows必选，系统目录
        :type system_dir: str
        :param volume_groups: Linux必选，如果没有卷组，输入[]
        :type volume_groups: list[:class:`huaweicloudsdksms.v3.VolumeGroups`]
        :param agent_version: Agent版本
        :type agent_version: str
        :param kernel_version: 内核版本信息
        :type kernel_version: str
        :param migration_cycle: 迁移周期 cutovering:启动目的端中 cutovered:启动目的端完成 checking:检查中 setting:设置中 replicating:复制中 syncing:同步中 
        :type migration_cycle: str
        :param state: 源端服务器状态 unavailable：环境校验不通过 waiting：等待 initialize：初始化 replicate：复制 syncing：持续同步 stopping：暂停中 stopped：已暂停 deleting：删除中 error：错误 cloning：等待克隆完成 cutovering：启动目的端中 finished：启动目的端完成
        :type state: str
        :param oem_system: 是否是OEM操作系统(Windows)
        :type oem_system: bool
        """
        
        

        self._id = None
        self._ip = None
        self._name = None
        self._hostname = None
        self._os_type = None
        self._os_version = None
        self._virtualization_type = None
        self._linux_block_check = None
        self._firmware = None
        self._cpu_quantity = None
        self._memory = None
        self._disks = None
        self._btrfs_list = None
        self._networks = None
        self._domain_id = None
        self._has_rsync = None
        self._paravirtualization = None
        self._raw_devices = None
        self._driver_files = None
        self._system_services = None
        self._account_rights = None
        self._boot_loader = None
        self._system_dir = None
        self._volume_groups = None
        self._agent_version = None
        self._kernel_version = None
        self._migration_cycle = None
        self._state = None
        self._oem_system = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.ip = ip
        self.name = name
        if hostname is not None:
            self.hostname = hostname
        self.os_type = os_type
        if os_version is not None:
            self.os_version = os_version
        if virtualization_type is not None:
            self.virtualization_type = virtualization_type
        if linux_block_check is not None:
            self.linux_block_check = linux_block_check
        if firmware is not None:
            self.firmware = firmware
        if cpu_quantity is not None:
            self.cpu_quantity = cpu_quantity
        if memory is not None:
            self.memory = memory
        if disks is not None:
            self.disks = disks
        if btrfs_list is not None:
            self.btrfs_list = btrfs_list
        if networks is not None:
            self.networks = networks
        if domain_id is not None:
            self.domain_id = domain_id
        if has_rsync is not None:
            self.has_rsync = has_rsync
        if paravirtualization is not None:
            self.paravirtualization = paravirtualization
        if raw_devices is not None:
            self.raw_devices = raw_devices
        if driver_files is not None:
            self.driver_files = driver_files
        if system_services is not None:
            self.system_services = system_services
        if account_rights is not None:
            self.account_rights = account_rights
        if boot_loader is not None:
            self.boot_loader = boot_loader
        if system_dir is not None:
            self.system_dir = system_dir
        if volume_groups is not None:
            self.volume_groups = volume_groups
        self.agent_version = agent_version
        if kernel_version is not None:
            self.kernel_version = kernel_version
        if migration_cycle is not None:
            self.migration_cycle = migration_cycle
        if state is not None:
            self.state = state
        if oem_system is not None:
            self.oem_system = oem_system

    @property
    def id(self):
        """Gets the id of this PostSourceServerBody.

        源端在SMS数据库中的ID

        :return: The id of this PostSourceServerBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PostSourceServerBody.

        源端在SMS数据库中的ID

        :param id: The id of this PostSourceServerBody.
        :type id: str
        """
        self._id = id

    @property
    def ip(self):
        """Gets the ip of this PostSourceServerBody.

        源端服务器ip，注册源端时必选，更新非必选

        :return: The ip of this PostSourceServerBody.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this PostSourceServerBody.

        源端服务器ip，注册源端时必选，更新非必选

        :param ip: The ip of this PostSourceServerBody.
        :type ip: str
        """
        self._ip = ip

    @property
    def name(self):
        """Gets the name of this PostSourceServerBody.

        用来区分不同源端服务器的名称

        :return: The name of this PostSourceServerBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostSourceServerBody.

        用来区分不同源端服务器的名称

        :param name: The name of this PostSourceServerBody.
        :type name: str
        """
        self._name = name

    @property
    def hostname(self):
        """Gets the hostname of this PostSourceServerBody.

        源端主机名，注册源端必选，更新非必选

        :return: The hostname of this PostSourceServerBody.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this PostSourceServerBody.

        源端主机名，注册源端必选，更新非必选

        :param hostname: The hostname of this PostSourceServerBody.
        :type hostname: str
        """
        self._hostname = hostname

    @property
    def os_type(self):
        """Gets the os_type of this PostSourceServerBody.

        源端服务器的OS类型，分为Windows和Linux，注册必选，更新非必选

        :return: The os_type of this PostSourceServerBody.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this PostSourceServerBody.

        源端服务器的OS类型，分为Windows和Linux，注册必选，更新非必选

        :param os_type: The os_type of this PostSourceServerBody.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def os_version(self):
        """Gets the os_version of this PostSourceServerBody.

        操作系统版本，注册必选，更新非必选

        :return: The os_version of this PostSourceServerBody.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this PostSourceServerBody.

        操作系统版本，注册必选，更新非必选

        :param os_version: The os_version of this PostSourceServerBody.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def virtualization_type(self):
        """Gets the virtualization_type of this PostSourceServerBody.

        操作系统虚拟化方式

        :return: The virtualization_type of this PostSourceServerBody.
        :rtype: str
        """
        return self._virtualization_type

    @virtualization_type.setter
    def virtualization_type(self, virtualization_type):
        """Sets the virtualization_type of this PostSourceServerBody.

        操作系统虚拟化方式

        :param virtualization_type: The virtualization_type of this PostSourceServerBody.
        :type virtualization_type: str
        """
        self._virtualization_type = virtualization_type

    @property
    def linux_block_check(self):
        """Gets the linux_block_check of this PostSourceServerBody.

        Linux操作系统块检查

        :return: The linux_block_check of this PostSourceServerBody.
        :rtype: str
        """
        return self._linux_block_check

    @linux_block_check.setter
    def linux_block_check(self, linux_block_check):
        """Sets the linux_block_check of this PostSourceServerBody.

        Linux操作系统块检查

        :param linux_block_check: The linux_block_check of this PostSourceServerBody.
        :type linux_block_check: str
        """
        self._linux_block_check = linux_block_check

    @property
    def firmware(self):
        """Gets the firmware of this PostSourceServerBody.

        源端服务器启动类型，如BIOS或者UEFI

        :return: The firmware of this PostSourceServerBody.
        :rtype: str
        """
        return self._firmware

    @firmware.setter
    def firmware(self, firmware):
        """Sets the firmware of this PostSourceServerBody.

        源端服务器启动类型，如BIOS或者UEFI

        :param firmware: The firmware of this PostSourceServerBody.
        :type firmware: str
        """
        self._firmware = firmware

    @property
    def cpu_quantity(self):
        """Gets the cpu_quantity of this PostSourceServerBody.

        CPU个数，单位vCPU

        :return: The cpu_quantity of this PostSourceServerBody.
        :rtype: int
        """
        return self._cpu_quantity

    @cpu_quantity.setter
    def cpu_quantity(self, cpu_quantity):
        """Sets the cpu_quantity of this PostSourceServerBody.

        CPU个数，单位vCPU

        :param cpu_quantity: The cpu_quantity of this PostSourceServerBody.
        :type cpu_quantity: int
        """
        self._cpu_quantity = cpu_quantity

    @property
    def memory(self):
        """Gets the memory of this PostSourceServerBody.

        内存大小，单位MB

        :return: The memory of this PostSourceServerBody.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this PostSourceServerBody.

        内存大小，单位MB

        :param memory: The memory of this PostSourceServerBody.
        :type memory: int
        """
        self._memory = memory

    @property
    def disks(self):
        """Gets the disks of this PostSourceServerBody.

        源端服务器的磁盘信息

        :return: The disks of this PostSourceServerBody.
        :rtype: list[:class:`huaweicloudsdksms.v3.ServerDisk`]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this PostSourceServerBody.

        源端服务器的磁盘信息

        :param disks: The disks of this PostSourceServerBody.
        :type disks: list[:class:`huaweicloudsdksms.v3.ServerDisk`]
        """
        self._disks = disks

    @property
    def btrfs_list(self):
        """Gets the btrfs_list of this PostSourceServerBody.

        Linux 必选，源端的Btrfs信息。如果源端不存在Btrfs，则为[]

        :return: The btrfs_list of this PostSourceServerBody.
        :rtype: list[:class:`huaweicloudsdksms.v3.BtrfsFileSystem`]
        """
        return self._btrfs_list

    @btrfs_list.setter
    def btrfs_list(self, btrfs_list):
        """Sets the btrfs_list of this PostSourceServerBody.

        Linux 必选，源端的Btrfs信息。如果源端不存在Btrfs，则为[]

        :param btrfs_list: The btrfs_list of this PostSourceServerBody.
        :type btrfs_list: list[:class:`huaweicloudsdksms.v3.BtrfsFileSystem`]
        """
        self._btrfs_list = btrfs_list

    @property
    def networks(self):
        """Gets the networks of this PostSourceServerBody.

        源端服务器的网卡信息

        :return: The networks of this PostSourceServerBody.
        :rtype: list[:class:`huaweicloudsdksms.v3.NetWork`]
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        """Sets the networks of this PostSourceServerBody.

        源端服务器的网卡信息

        :param networks: The networks of this PostSourceServerBody.
        :type networks: list[:class:`huaweicloudsdksms.v3.NetWork`]
        """
        self._networks = networks

    @property
    def domain_id(self):
        """Gets the domain_id of this PostSourceServerBody.

        租户的domainId

        :return: The domain_id of this PostSourceServerBody.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this PostSourceServerBody.

        租户的domainId

        :param domain_id: The domain_id of this PostSourceServerBody.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def has_rsync(self):
        """Gets the has_rsync of this PostSourceServerBody.

        是否安装rsync组件，Linux系统此参数为必选

        :return: The has_rsync of this PostSourceServerBody.
        :rtype: bool
        """
        return self._has_rsync

    @has_rsync.setter
    def has_rsync(self, has_rsync):
        """Sets the has_rsync of this PostSourceServerBody.

        是否安装rsync组件，Linux系统此参数为必选

        :param has_rsync: The has_rsync of this PostSourceServerBody.
        :type has_rsync: bool
        """
        self._has_rsync = has_rsync

    @property
    def paravirtualization(self):
        """Gets the paravirtualization of this PostSourceServerBody.

        Linux场景必选，源端是否是半虚拟化

        :return: The paravirtualization of this PostSourceServerBody.
        :rtype: bool
        """
        return self._paravirtualization

    @paravirtualization.setter
    def paravirtualization(self, paravirtualization):
        """Sets the paravirtualization of this PostSourceServerBody.

        Linux场景必选，源端是否是半虚拟化

        :param paravirtualization: The paravirtualization of this PostSourceServerBody.
        :type paravirtualization: bool
        """
        self._paravirtualization = paravirtualization

    @property
    def raw_devices(self):
        """Gets the raw_devices of this PostSourceServerBody.

        Linux必选，裸设备列表

        :return: The raw_devices of this PostSourceServerBody.
        :rtype: str
        """
        return self._raw_devices

    @raw_devices.setter
    def raw_devices(self, raw_devices):
        """Sets the raw_devices of this PostSourceServerBody.

        Linux必选，裸设备列表

        :param raw_devices: The raw_devices of this PostSourceServerBody.
        :type raw_devices: str
        """
        self._raw_devices = raw_devices

    @property
    def driver_files(self):
        """Gets the driver_files of this PostSourceServerBody.

        Windows 必选，是否缺少驱动文件

        :return: The driver_files of this PostSourceServerBody.
        :rtype: bool
        """
        return self._driver_files

    @driver_files.setter
    def driver_files(self, driver_files):
        """Sets the driver_files of this PostSourceServerBody.

        Windows 必选，是否缺少驱动文件

        :param driver_files: The driver_files of this PostSourceServerBody.
        :type driver_files: bool
        """
        self._driver_files = driver_files

    @property
    def system_services(self):
        """Gets the system_services of this PostSourceServerBody.

        Windows必选，是否存在不正常服务

        :return: The system_services of this PostSourceServerBody.
        :rtype: bool
        """
        return self._system_services

    @system_services.setter
    def system_services(self, system_services):
        """Sets the system_services of this PostSourceServerBody.

        Windows必选，是否存在不正常服务

        :param system_services: The system_services of this PostSourceServerBody.
        :type system_services: bool
        """
        self._system_services = system_services

    @property
    def account_rights(self):
        """Gets the account_rights of this PostSourceServerBody.

        Windows必选，权限是否满足要求

        :return: The account_rights of this PostSourceServerBody.
        :rtype: bool
        """
        return self._account_rights

    @account_rights.setter
    def account_rights(self, account_rights):
        """Sets the account_rights of this PostSourceServerBody.

        Windows必选，权限是否满足要求

        :param account_rights: The account_rights of this PostSourceServerBody.
        :type account_rights: bool
        """
        self._account_rights = account_rights

    @property
    def boot_loader(self):
        """Gets the boot_loader of this PostSourceServerBody.

        Linux必选，系统引导类型，BOOT_LOADER(GRUB/LILO)

        :return: The boot_loader of this PostSourceServerBody.
        :rtype: str
        """
        return self._boot_loader

    @boot_loader.setter
    def boot_loader(self, boot_loader):
        """Sets the boot_loader of this PostSourceServerBody.

        Linux必选，系统引导类型，BOOT_LOADER(GRUB/LILO)

        :param boot_loader: The boot_loader of this PostSourceServerBody.
        :type boot_loader: str
        """
        self._boot_loader = boot_loader

    @property
    def system_dir(self):
        """Gets the system_dir of this PostSourceServerBody.

        Windows必选，系统目录

        :return: The system_dir of this PostSourceServerBody.
        :rtype: str
        """
        return self._system_dir

    @system_dir.setter
    def system_dir(self, system_dir):
        """Sets the system_dir of this PostSourceServerBody.

        Windows必选，系统目录

        :param system_dir: The system_dir of this PostSourceServerBody.
        :type system_dir: str
        """
        self._system_dir = system_dir

    @property
    def volume_groups(self):
        """Gets the volume_groups of this PostSourceServerBody.

        Linux必选，如果没有卷组，输入[]

        :return: The volume_groups of this PostSourceServerBody.
        :rtype: list[:class:`huaweicloudsdksms.v3.VolumeGroups`]
        """
        return self._volume_groups

    @volume_groups.setter
    def volume_groups(self, volume_groups):
        """Sets the volume_groups of this PostSourceServerBody.

        Linux必选，如果没有卷组，输入[]

        :param volume_groups: The volume_groups of this PostSourceServerBody.
        :type volume_groups: list[:class:`huaweicloudsdksms.v3.VolumeGroups`]
        """
        self._volume_groups = volume_groups

    @property
    def agent_version(self):
        """Gets the agent_version of this PostSourceServerBody.

        Agent版本

        :return: The agent_version of this PostSourceServerBody.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        """Sets the agent_version of this PostSourceServerBody.

        Agent版本

        :param agent_version: The agent_version of this PostSourceServerBody.
        :type agent_version: str
        """
        self._agent_version = agent_version

    @property
    def kernel_version(self):
        """Gets the kernel_version of this PostSourceServerBody.

        内核版本信息

        :return: The kernel_version of this PostSourceServerBody.
        :rtype: str
        """
        return self._kernel_version

    @kernel_version.setter
    def kernel_version(self, kernel_version):
        """Sets the kernel_version of this PostSourceServerBody.

        内核版本信息

        :param kernel_version: The kernel_version of this PostSourceServerBody.
        :type kernel_version: str
        """
        self._kernel_version = kernel_version

    @property
    def migration_cycle(self):
        """Gets the migration_cycle of this PostSourceServerBody.

        迁移周期 cutovering:启动目的端中 cutovered:启动目的端完成 checking:检查中 setting:设置中 replicating:复制中 syncing:同步中 

        :return: The migration_cycle of this PostSourceServerBody.
        :rtype: str
        """
        return self._migration_cycle

    @migration_cycle.setter
    def migration_cycle(self, migration_cycle):
        """Sets the migration_cycle of this PostSourceServerBody.

        迁移周期 cutovering:启动目的端中 cutovered:启动目的端完成 checking:检查中 setting:设置中 replicating:复制中 syncing:同步中 

        :param migration_cycle: The migration_cycle of this PostSourceServerBody.
        :type migration_cycle: str
        """
        self._migration_cycle = migration_cycle

    @property
    def state(self):
        """Gets the state of this PostSourceServerBody.

        源端服务器状态 unavailable：环境校验不通过 waiting：等待 initialize：初始化 replicate：复制 syncing：持续同步 stopping：暂停中 stopped：已暂停 deleting：删除中 error：错误 cloning：等待克隆完成 cutovering：启动目的端中 finished：启动目的端完成

        :return: The state of this PostSourceServerBody.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PostSourceServerBody.

        源端服务器状态 unavailable：环境校验不通过 waiting：等待 initialize：初始化 replicate：复制 syncing：持续同步 stopping：暂停中 stopped：已暂停 deleting：删除中 error：错误 cloning：等待克隆完成 cutovering：启动目的端中 finished：启动目的端完成

        :param state: The state of this PostSourceServerBody.
        :type state: str
        """
        self._state = state

    @property
    def oem_system(self):
        """Gets the oem_system of this PostSourceServerBody.

        是否是OEM操作系统(Windows)

        :return: The oem_system of this PostSourceServerBody.
        :rtype: bool
        """
        return self._oem_system

    @oem_system.setter
    def oem_system(self, oem_system):
        """Sets the oem_system of this PostSourceServerBody.

        是否是OEM操作系统(Windows)

        :param oem_system: The oem_system of this PostSourceServerBody.
        :type oem_system: bool
        """
        self._oem_system = oem_system

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
        if not isinstance(other, PostSourceServerBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
