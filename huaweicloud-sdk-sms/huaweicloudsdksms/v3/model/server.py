# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Server:

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
        'firmware': 'str',
        'cpu_quantity': 'int',
        'memory': 'int',
        'disks': 'list[Disk]',
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
        'volume_groups': 'list[VolumeGroups]'
    }

    attribute_map = {
        'id': 'id',
        'ip': 'ip',
        'name': 'name',
        'hostname': 'hostname',
        'os_type': 'os_type',
        'os_version': 'os_version',
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
        'volume_groups': 'volume_groups'
    }

    def __init__(self, id=None, ip=None, name=None, hostname=None, os_type=None, os_version=None, firmware=None, cpu_quantity=None, memory=None, disks=None, btrfs_list=None, networks=None, domain_id=None, has_rsync=None, paravirtualization=None, raw_devices=None, driver_files=None, system_services=None, account_rights=None, boot_loader=None, system_dir=None, volume_groups=None):
        """Server

        The model defined in huaweicloud sdk

        :param id: 源端在SMS数据库中的ID
        :type id: str
        :param ip: 源端服务器IP，注册源端时必选，更新非必选
        :type ip: str
        :param name: 用来区分不同源端服务器的名称
        :type name: str
        :param hostname: 源端主机名，注册源端必选，更新非必选
        :type hostname: str
        :param os_type: 源端服务器的OS类型，分为Windows和Linux，注册必选，更新非必选
        :type os_type: str
        :param os_version: 操作系统版本，注册必选，更新非必选
        :type os_version: str
        :param firmware: 源端服务器启动类型，如BIOS或者UEFI
        :type firmware: str
        :param cpu_quantity: CPU个数，单位vCPU
        :type cpu_quantity: int
        :param memory: 内存大小，单位MB
        :type memory: int
        :param disks: 源端服务器的磁盘信息
        :type disks: list[:class:`huaweicloudsdksms.v3.Disk`]
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
        """
        
        

        self._id = None
        self._ip = None
        self._name = None
        self._hostname = None
        self._os_type = None
        self._os_version = None
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

    @property
    def id(self):
        """Gets the id of this Server.

        源端在SMS数据库中的ID

        :return: The id of this Server.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Server.

        源端在SMS数据库中的ID

        :param id: The id of this Server.
        :type id: str
        """
        self._id = id

    @property
    def ip(self):
        """Gets the ip of this Server.

        源端服务器IP，注册源端时必选，更新非必选

        :return: The ip of this Server.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this Server.

        源端服务器IP，注册源端时必选，更新非必选

        :param ip: The ip of this Server.
        :type ip: str
        """
        self._ip = ip

    @property
    def name(self):
        """Gets the name of this Server.

        用来区分不同源端服务器的名称

        :return: The name of this Server.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Server.

        用来区分不同源端服务器的名称

        :param name: The name of this Server.
        :type name: str
        """
        self._name = name

    @property
    def hostname(self):
        """Gets the hostname of this Server.

        源端主机名，注册源端必选，更新非必选

        :return: The hostname of this Server.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this Server.

        源端主机名，注册源端必选，更新非必选

        :param hostname: The hostname of this Server.
        :type hostname: str
        """
        self._hostname = hostname

    @property
    def os_type(self):
        """Gets the os_type of this Server.

        源端服务器的OS类型，分为Windows和Linux，注册必选，更新非必选

        :return: The os_type of this Server.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this Server.

        源端服务器的OS类型，分为Windows和Linux，注册必选，更新非必选

        :param os_type: The os_type of this Server.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def os_version(self):
        """Gets the os_version of this Server.

        操作系统版本，注册必选，更新非必选

        :return: The os_version of this Server.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this Server.

        操作系统版本，注册必选，更新非必选

        :param os_version: The os_version of this Server.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def firmware(self):
        """Gets the firmware of this Server.

        源端服务器启动类型，如BIOS或者UEFI

        :return: The firmware of this Server.
        :rtype: str
        """
        return self._firmware

    @firmware.setter
    def firmware(self, firmware):
        """Sets the firmware of this Server.

        源端服务器启动类型，如BIOS或者UEFI

        :param firmware: The firmware of this Server.
        :type firmware: str
        """
        self._firmware = firmware

    @property
    def cpu_quantity(self):
        """Gets the cpu_quantity of this Server.

        CPU个数，单位vCPU

        :return: The cpu_quantity of this Server.
        :rtype: int
        """
        return self._cpu_quantity

    @cpu_quantity.setter
    def cpu_quantity(self, cpu_quantity):
        """Sets the cpu_quantity of this Server.

        CPU个数，单位vCPU

        :param cpu_quantity: The cpu_quantity of this Server.
        :type cpu_quantity: int
        """
        self._cpu_quantity = cpu_quantity

    @property
    def memory(self):
        """Gets the memory of this Server.

        内存大小，单位MB

        :return: The memory of this Server.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this Server.

        内存大小，单位MB

        :param memory: The memory of this Server.
        :type memory: int
        """
        self._memory = memory

    @property
    def disks(self):
        """Gets the disks of this Server.

        源端服务器的磁盘信息

        :return: The disks of this Server.
        :rtype: list[:class:`huaweicloudsdksms.v3.Disk`]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this Server.

        源端服务器的磁盘信息

        :param disks: The disks of this Server.
        :type disks: list[:class:`huaweicloudsdksms.v3.Disk`]
        """
        self._disks = disks

    @property
    def btrfs_list(self):
        """Gets the btrfs_list of this Server.

        Linux 必选，源端的Btrfs信息。如果源端不存在Btrfs，则为[]

        :return: The btrfs_list of this Server.
        :rtype: list[:class:`huaweicloudsdksms.v3.BtrfsFileSystem`]
        """
        return self._btrfs_list

    @btrfs_list.setter
    def btrfs_list(self, btrfs_list):
        """Sets the btrfs_list of this Server.

        Linux 必选，源端的Btrfs信息。如果源端不存在Btrfs，则为[]

        :param btrfs_list: The btrfs_list of this Server.
        :type btrfs_list: list[:class:`huaweicloudsdksms.v3.BtrfsFileSystem`]
        """
        self._btrfs_list = btrfs_list

    @property
    def networks(self):
        """Gets the networks of this Server.

        源端服务器的网卡信息

        :return: The networks of this Server.
        :rtype: list[:class:`huaweicloudsdksms.v3.NetWork`]
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        """Sets the networks of this Server.

        源端服务器的网卡信息

        :param networks: The networks of this Server.
        :type networks: list[:class:`huaweicloudsdksms.v3.NetWork`]
        """
        self._networks = networks

    @property
    def domain_id(self):
        """Gets the domain_id of this Server.

        租户的domainId

        :return: The domain_id of this Server.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this Server.

        租户的domainId

        :param domain_id: The domain_id of this Server.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def has_rsync(self):
        """Gets the has_rsync of this Server.

        是否安装rsync组件，Linux系统此参数为必选

        :return: The has_rsync of this Server.
        :rtype: bool
        """
        return self._has_rsync

    @has_rsync.setter
    def has_rsync(self, has_rsync):
        """Sets the has_rsync of this Server.

        是否安装rsync组件，Linux系统此参数为必选

        :param has_rsync: The has_rsync of this Server.
        :type has_rsync: bool
        """
        self._has_rsync = has_rsync

    @property
    def paravirtualization(self):
        """Gets the paravirtualization of this Server.

        Linux场景必选，源端是否是半虚拟化

        :return: The paravirtualization of this Server.
        :rtype: bool
        """
        return self._paravirtualization

    @paravirtualization.setter
    def paravirtualization(self, paravirtualization):
        """Sets the paravirtualization of this Server.

        Linux场景必选，源端是否是半虚拟化

        :param paravirtualization: The paravirtualization of this Server.
        :type paravirtualization: bool
        """
        self._paravirtualization = paravirtualization

    @property
    def raw_devices(self):
        """Gets the raw_devices of this Server.

        Linux必选，裸设备列表

        :return: The raw_devices of this Server.
        :rtype: str
        """
        return self._raw_devices

    @raw_devices.setter
    def raw_devices(self, raw_devices):
        """Sets the raw_devices of this Server.

        Linux必选，裸设备列表

        :param raw_devices: The raw_devices of this Server.
        :type raw_devices: str
        """
        self._raw_devices = raw_devices

    @property
    def driver_files(self):
        """Gets the driver_files of this Server.

        Windows 必选，是否缺少驱动文件

        :return: The driver_files of this Server.
        :rtype: bool
        """
        return self._driver_files

    @driver_files.setter
    def driver_files(self, driver_files):
        """Sets the driver_files of this Server.

        Windows 必选，是否缺少驱动文件

        :param driver_files: The driver_files of this Server.
        :type driver_files: bool
        """
        self._driver_files = driver_files

    @property
    def system_services(self):
        """Gets the system_services of this Server.

        Windows必选，是否存在不正常服务

        :return: The system_services of this Server.
        :rtype: bool
        """
        return self._system_services

    @system_services.setter
    def system_services(self, system_services):
        """Sets the system_services of this Server.

        Windows必选，是否存在不正常服务

        :param system_services: The system_services of this Server.
        :type system_services: bool
        """
        self._system_services = system_services

    @property
    def account_rights(self):
        """Gets the account_rights of this Server.

        Windows必选，权限是否满足要求

        :return: The account_rights of this Server.
        :rtype: bool
        """
        return self._account_rights

    @account_rights.setter
    def account_rights(self, account_rights):
        """Sets the account_rights of this Server.

        Windows必选，权限是否满足要求

        :param account_rights: The account_rights of this Server.
        :type account_rights: bool
        """
        self._account_rights = account_rights

    @property
    def boot_loader(self):
        """Gets the boot_loader of this Server.

        Linux必选，系统引导类型，BOOT_LOADER(GRUB/LILO)

        :return: The boot_loader of this Server.
        :rtype: str
        """
        return self._boot_loader

    @boot_loader.setter
    def boot_loader(self, boot_loader):
        """Sets the boot_loader of this Server.

        Linux必选，系统引导类型，BOOT_LOADER(GRUB/LILO)

        :param boot_loader: The boot_loader of this Server.
        :type boot_loader: str
        """
        self._boot_loader = boot_loader

    @property
    def system_dir(self):
        """Gets the system_dir of this Server.

        Windows必选，系统目录

        :return: The system_dir of this Server.
        :rtype: str
        """
        return self._system_dir

    @system_dir.setter
    def system_dir(self, system_dir):
        """Sets the system_dir of this Server.

        Windows必选，系统目录

        :param system_dir: The system_dir of this Server.
        :type system_dir: str
        """
        self._system_dir = system_dir

    @property
    def volume_groups(self):
        """Gets the volume_groups of this Server.

        Linux必选，如果没有卷组，输入[]

        :return: The volume_groups of this Server.
        :rtype: list[:class:`huaweicloudsdksms.v3.VolumeGroups`]
        """
        return self._volume_groups

    @volume_groups.setter
    def volume_groups(self, volume_groups):
        """Sets the volume_groups of this Server.

        Linux必选，如果没有卷组，输入[]

        :param volume_groups: The volume_groups of this Server.
        :type volume_groups: list[:class:`huaweicloudsdksms.v3.VolumeGroups`]
        """
        self._volume_groups = volume_groups

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
        if not isinstance(other, Server):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
