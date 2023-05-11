# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostOverviewResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_name': 'str',
        'host_name': 'str',
        'host_stat': 'str',
        'work_ip': 'str',
        'mem_free': 'float',
        'mem_total': 'float',
        'mem_usage': 'float',
        'mem_cached': 'float',
        'mem_buffer': 'float',
        'swap_free': 'float',
        'swap_total': 'float',
        'cpu_usage': 'float',
        'cpu_usage_sys': 'float',
        'cpu_usage_usr': 'float',
        'cpu_idle': 'float',
        'cpu_iowait': 'float',
        'disk_usage_avg': 'float',
        'disk_total': 'float',
        'disk_used': 'float',
        'disk_available': 'float',
        'disk_io': 'float',
        'disk_io_read': 'float',
        'disk_io_write': 'float',
        'tcp_resend_rate': 'float',
        'net_io': 'float'
    }

    attribute_map = {
        'instance_name': 'instance_name',
        'host_name': 'host_name',
        'host_stat': 'host_stat',
        'work_ip': 'work_ip',
        'mem_free': 'mem_free',
        'mem_total': 'mem_total',
        'mem_usage': 'mem_usage',
        'mem_cached': 'mem_cached',
        'mem_buffer': 'mem_buffer',
        'swap_free': 'swap_free',
        'swap_total': 'swap_total',
        'cpu_usage': 'cpu_usage',
        'cpu_usage_sys': 'cpu_usage_sys',
        'cpu_usage_usr': 'cpu_usage_usr',
        'cpu_idle': 'cpu_idle',
        'cpu_iowait': 'cpu_iowait',
        'disk_usage_avg': 'disk_usage_avg',
        'disk_total': 'disk_total',
        'disk_used': 'disk_used',
        'disk_available': 'disk_available',
        'disk_io': 'disk_io',
        'disk_io_read': 'disk_io_read',
        'disk_io_write': 'disk_io_write',
        'tcp_resend_rate': 'tcp_resend_rate',
        'net_io': 'net_io'
    }

    def __init__(self, instance_name=None, host_name=None, host_stat=None, work_ip=None, mem_free=None, mem_total=None, mem_usage=None, mem_cached=None, mem_buffer=None, swap_free=None, swap_total=None, cpu_usage=None, cpu_usage_sys=None, cpu_usage_usr=None, cpu_idle=None, cpu_iowait=None, disk_usage_avg=None, disk_total=None, disk_used=None, disk_available=None, disk_io=None, disk_io_read=None, disk_io_write=None, tcp_resend_rate=None, net_io=None):
        """HostOverviewResponse

        The model defined in huaweicloud sdk

        :param instance_name: 实例名称
        :type instance_name: str
        :param host_name: 主机名称
        :type host_name: str
        :param host_stat: 主机状态
        :type host_stat: str
        :param work_ip: IP地址
        :type work_ip: str
        :param mem_free: 系统中未使用的内存(GB)。
        :type mem_free: float
        :param mem_total: 总内存(GB)。
        :type mem_total: float
        :param mem_usage: 内存使用率(GB)。
        :type mem_usage: float
        :param mem_cached: 缓存内存(GB)。
        :type mem_cached: float
        :param mem_buffer: 缓冲内存(MB)。
        :type mem_buffer: float
        :param swap_free: ram暂存在swap中的大小(GB)。
        :type swap_free: float
        :param swap_total: 交换空间总和(GB)。
        :type swap_total: float
        :param cpu_usage: CPU使用率(%)。
        :type cpu_usage: float
        :param cpu_usage_sys: 系统CPU占用率(%)。
        :type cpu_usage_sys: float
        :param cpu_usage_usr: 用户CPU占用率(%)。
        :type cpu_usage_usr: float
        :param cpu_idle: 空闲CPU占用率(%)。
        :type cpu_idle: float
        :param cpu_iowait: IO等待(%)。
        :type cpu_iowait: float
        :param disk_usage_avg: 磁盘平均使用率(%)。
        :type disk_usage_avg: float
        :param disk_total: 磁盘总容量(GB)。
        :type disk_total: float
        :param disk_used: 磁盘使用容量(GB)。
        :type disk_used: float
        :param disk_available: 磁盘可用容量(GB)。
        :type disk_available: float
        :param disk_io: 磁盘IO(KB/s)。
        :type disk_io: float
        :param disk_io_read: 磁盘读速率(KB/s)。
        :type disk_io_read: float
        :param disk_io_write: 磁盘写速率(KB/s)。
        :type disk_io_write: float
        :param tcp_resend_rate: TCP协议栈重传率(%)。
        :type tcp_resend_rate: float
        :param net_io: 网络IO(KB/s)。
        :type net_io: float
        """
        
        

        self._instance_name = None
        self._host_name = None
        self._host_stat = None
        self._work_ip = None
        self._mem_free = None
        self._mem_total = None
        self._mem_usage = None
        self._mem_cached = None
        self._mem_buffer = None
        self._swap_free = None
        self._swap_total = None
        self._cpu_usage = None
        self._cpu_usage_sys = None
        self._cpu_usage_usr = None
        self._cpu_idle = None
        self._cpu_iowait = None
        self._disk_usage_avg = None
        self._disk_total = None
        self._disk_used = None
        self._disk_available = None
        self._disk_io = None
        self._disk_io_read = None
        self._disk_io_write = None
        self._tcp_resend_rate = None
        self._net_io = None
        self.discriminator = None

        if instance_name is not None:
            self.instance_name = instance_name
        if host_name is not None:
            self.host_name = host_name
        if host_stat is not None:
            self.host_stat = host_stat
        if work_ip is not None:
            self.work_ip = work_ip
        if mem_free is not None:
            self.mem_free = mem_free
        if mem_total is not None:
            self.mem_total = mem_total
        if mem_usage is not None:
            self.mem_usage = mem_usage
        if mem_cached is not None:
            self.mem_cached = mem_cached
        if mem_buffer is not None:
            self.mem_buffer = mem_buffer
        if swap_free is not None:
            self.swap_free = swap_free
        if swap_total is not None:
            self.swap_total = swap_total
        if cpu_usage is not None:
            self.cpu_usage = cpu_usage
        if cpu_usage_sys is not None:
            self.cpu_usage_sys = cpu_usage_sys
        if cpu_usage_usr is not None:
            self.cpu_usage_usr = cpu_usage_usr
        if cpu_idle is not None:
            self.cpu_idle = cpu_idle
        if cpu_iowait is not None:
            self.cpu_iowait = cpu_iowait
        if disk_usage_avg is not None:
            self.disk_usage_avg = disk_usage_avg
        if disk_total is not None:
            self.disk_total = disk_total
        if disk_used is not None:
            self.disk_used = disk_used
        if disk_available is not None:
            self.disk_available = disk_available
        if disk_io is not None:
            self.disk_io = disk_io
        if disk_io_read is not None:
            self.disk_io_read = disk_io_read
        if disk_io_write is not None:
            self.disk_io_write = disk_io_write
        if tcp_resend_rate is not None:
            self.tcp_resend_rate = tcp_resend_rate
        if net_io is not None:
            self.net_io = net_io

    @property
    def instance_name(self):
        """Gets the instance_name of this HostOverviewResponse.

        实例名称

        :return: The instance_name of this HostOverviewResponse.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this HostOverviewResponse.

        实例名称

        :param instance_name: The instance_name of this HostOverviewResponse.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def host_name(self):
        """Gets the host_name of this HostOverviewResponse.

        主机名称

        :return: The host_name of this HostOverviewResponse.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this HostOverviewResponse.

        主机名称

        :param host_name: The host_name of this HostOverviewResponse.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_stat(self):
        """Gets the host_stat of this HostOverviewResponse.

        主机状态

        :return: The host_stat of this HostOverviewResponse.
        :rtype: str
        """
        return self._host_stat

    @host_stat.setter
    def host_stat(self, host_stat):
        """Sets the host_stat of this HostOverviewResponse.

        主机状态

        :param host_stat: The host_stat of this HostOverviewResponse.
        :type host_stat: str
        """
        self._host_stat = host_stat

    @property
    def work_ip(self):
        """Gets the work_ip of this HostOverviewResponse.

        IP地址

        :return: The work_ip of this HostOverviewResponse.
        :rtype: str
        """
        return self._work_ip

    @work_ip.setter
    def work_ip(self, work_ip):
        """Sets the work_ip of this HostOverviewResponse.

        IP地址

        :param work_ip: The work_ip of this HostOverviewResponse.
        :type work_ip: str
        """
        self._work_ip = work_ip

    @property
    def mem_free(self):
        """Gets the mem_free of this HostOverviewResponse.

        系统中未使用的内存(GB)。

        :return: The mem_free of this HostOverviewResponse.
        :rtype: float
        """
        return self._mem_free

    @mem_free.setter
    def mem_free(self, mem_free):
        """Sets the mem_free of this HostOverviewResponse.

        系统中未使用的内存(GB)。

        :param mem_free: The mem_free of this HostOverviewResponse.
        :type mem_free: float
        """
        self._mem_free = mem_free

    @property
    def mem_total(self):
        """Gets the mem_total of this HostOverviewResponse.

        总内存(GB)。

        :return: The mem_total of this HostOverviewResponse.
        :rtype: float
        """
        return self._mem_total

    @mem_total.setter
    def mem_total(self, mem_total):
        """Sets the mem_total of this HostOverviewResponse.

        总内存(GB)。

        :param mem_total: The mem_total of this HostOverviewResponse.
        :type mem_total: float
        """
        self._mem_total = mem_total

    @property
    def mem_usage(self):
        """Gets the mem_usage of this HostOverviewResponse.

        内存使用率(GB)。

        :return: The mem_usage of this HostOverviewResponse.
        :rtype: float
        """
        return self._mem_usage

    @mem_usage.setter
    def mem_usage(self, mem_usage):
        """Sets the mem_usage of this HostOverviewResponse.

        内存使用率(GB)。

        :param mem_usage: The mem_usage of this HostOverviewResponse.
        :type mem_usage: float
        """
        self._mem_usage = mem_usage

    @property
    def mem_cached(self):
        """Gets the mem_cached of this HostOverviewResponse.

        缓存内存(GB)。

        :return: The mem_cached of this HostOverviewResponse.
        :rtype: float
        """
        return self._mem_cached

    @mem_cached.setter
    def mem_cached(self, mem_cached):
        """Sets the mem_cached of this HostOverviewResponse.

        缓存内存(GB)。

        :param mem_cached: The mem_cached of this HostOverviewResponse.
        :type mem_cached: float
        """
        self._mem_cached = mem_cached

    @property
    def mem_buffer(self):
        """Gets the mem_buffer of this HostOverviewResponse.

        缓冲内存(MB)。

        :return: The mem_buffer of this HostOverviewResponse.
        :rtype: float
        """
        return self._mem_buffer

    @mem_buffer.setter
    def mem_buffer(self, mem_buffer):
        """Sets the mem_buffer of this HostOverviewResponse.

        缓冲内存(MB)。

        :param mem_buffer: The mem_buffer of this HostOverviewResponse.
        :type mem_buffer: float
        """
        self._mem_buffer = mem_buffer

    @property
    def swap_free(self):
        """Gets the swap_free of this HostOverviewResponse.

        ram暂存在swap中的大小(GB)。

        :return: The swap_free of this HostOverviewResponse.
        :rtype: float
        """
        return self._swap_free

    @swap_free.setter
    def swap_free(self, swap_free):
        """Sets the swap_free of this HostOverviewResponse.

        ram暂存在swap中的大小(GB)。

        :param swap_free: The swap_free of this HostOverviewResponse.
        :type swap_free: float
        """
        self._swap_free = swap_free

    @property
    def swap_total(self):
        """Gets the swap_total of this HostOverviewResponse.

        交换空间总和(GB)。

        :return: The swap_total of this HostOverviewResponse.
        :rtype: float
        """
        return self._swap_total

    @swap_total.setter
    def swap_total(self, swap_total):
        """Sets the swap_total of this HostOverviewResponse.

        交换空间总和(GB)。

        :param swap_total: The swap_total of this HostOverviewResponse.
        :type swap_total: float
        """
        self._swap_total = swap_total

    @property
    def cpu_usage(self):
        """Gets the cpu_usage of this HostOverviewResponse.

        CPU使用率(%)。

        :return: The cpu_usage of this HostOverviewResponse.
        :rtype: float
        """
        return self._cpu_usage

    @cpu_usage.setter
    def cpu_usage(self, cpu_usage):
        """Sets the cpu_usage of this HostOverviewResponse.

        CPU使用率(%)。

        :param cpu_usage: The cpu_usage of this HostOverviewResponse.
        :type cpu_usage: float
        """
        self._cpu_usage = cpu_usage

    @property
    def cpu_usage_sys(self):
        """Gets the cpu_usage_sys of this HostOverviewResponse.

        系统CPU占用率(%)。

        :return: The cpu_usage_sys of this HostOverviewResponse.
        :rtype: float
        """
        return self._cpu_usage_sys

    @cpu_usage_sys.setter
    def cpu_usage_sys(self, cpu_usage_sys):
        """Sets the cpu_usage_sys of this HostOverviewResponse.

        系统CPU占用率(%)。

        :param cpu_usage_sys: The cpu_usage_sys of this HostOverviewResponse.
        :type cpu_usage_sys: float
        """
        self._cpu_usage_sys = cpu_usage_sys

    @property
    def cpu_usage_usr(self):
        """Gets the cpu_usage_usr of this HostOverviewResponse.

        用户CPU占用率(%)。

        :return: The cpu_usage_usr of this HostOverviewResponse.
        :rtype: float
        """
        return self._cpu_usage_usr

    @cpu_usage_usr.setter
    def cpu_usage_usr(self, cpu_usage_usr):
        """Sets the cpu_usage_usr of this HostOverviewResponse.

        用户CPU占用率(%)。

        :param cpu_usage_usr: The cpu_usage_usr of this HostOverviewResponse.
        :type cpu_usage_usr: float
        """
        self._cpu_usage_usr = cpu_usage_usr

    @property
    def cpu_idle(self):
        """Gets the cpu_idle of this HostOverviewResponse.

        空闲CPU占用率(%)。

        :return: The cpu_idle of this HostOverviewResponse.
        :rtype: float
        """
        return self._cpu_idle

    @cpu_idle.setter
    def cpu_idle(self, cpu_idle):
        """Sets the cpu_idle of this HostOverviewResponse.

        空闲CPU占用率(%)。

        :param cpu_idle: The cpu_idle of this HostOverviewResponse.
        :type cpu_idle: float
        """
        self._cpu_idle = cpu_idle

    @property
    def cpu_iowait(self):
        """Gets the cpu_iowait of this HostOverviewResponse.

        IO等待(%)。

        :return: The cpu_iowait of this HostOverviewResponse.
        :rtype: float
        """
        return self._cpu_iowait

    @cpu_iowait.setter
    def cpu_iowait(self, cpu_iowait):
        """Sets the cpu_iowait of this HostOverviewResponse.

        IO等待(%)。

        :param cpu_iowait: The cpu_iowait of this HostOverviewResponse.
        :type cpu_iowait: float
        """
        self._cpu_iowait = cpu_iowait

    @property
    def disk_usage_avg(self):
        """Gets the disk_usage_avg of this HostOverviewResponse.

        磁盘平均使用率(%)。

        :return: The disk_usage_avg of this HostOverviewResponse.
        :rtype: float
        """
        return self._disk_usage_avg

    @disk_usage_avg.setter
    def disk_usage_avg(self, disk_usage_avg):
        """Sets the disk_usage_avg of this HostOverviewResponse.

        磁盘平均使用率(%)。

        :param disk_usage_avg: The disk_usage_avg of this HostOverviewResponse.
        :type disk_usage_avg: float
        """
        self._disk_usage_avg = disk_usage_avg

    @property
    def disk_total(self):
        """Gets the disk_total of this HostOverviewResponse.

        磁盘总容量(GB)。

        :return: The disk_total of this HostOverviewResponse.
        :rtype: float
        """
        return self._disk_total

    @disk_total.setter
    def disk_total(self, disk_total):
        """Sets the disk_total of this HostOverviewResponse.

        磁盘总容量(GB)。

        :param disk_total: The disk_total of this HostOverviewResponse.
        :type disk_total: float
        """
        self._disk_total = disk_total

    @property
    def disk_used(self):
        """Gets the disk_used of this HostOverviewResponse.

        磁盘使用容量(GB)。

        :return: The disk_used of this HostOverviewResponse.
        :rtype: float
        """
        return self._disk_used

    @disk_used.setter
    def disk_used(self, disk_used):
        """Sets the disk_used of this HostOverviewResponse.

        磁盘使用容量(GB)。

        :param disk_used: The disk_used of this HostOverviewResponse.
        :type disk_used: float
        """
        self._disk_used = disk_used

    @property
    def disk_available(self):
        """Gets the disk_available of this HostOverviewResponse.

        磁盘可用容量(GB)。

        :return: The disk_available of this HostOverviewResponse.
        :rtype: float
        """
        return self._disk_available

    @disk_available.setter
    def disk_available(self, disk_available):
        """Sets the disk_available of this HostOverviewResponse.

        磁盘可用容量(GB)。

        :param disk_available: The disk_available of this HostOverviewResponse.
        :type disk_available: float
        """
        self._disk_available = disk_available

    @property
    def disk_io(self):
        """Gets the disk_io of this HostOverviewResponse.

        磁盘IO(KB/s)。

        :return: The disk_io of this HostOverviewResponse.
        :rtype: float
        """
        return self._disk_io

    @disk_io.setter
    def disk_io(self, disk_io):
        """Sets the disk_io of this HostOverviewResponse.

        磁盘IO(KB/s)。

        :param disk_io: The disk_io of this HostOverviewResponse.
        :type disk_io: float
        """
        self._disk_io = disk_io

    @property
    def disk_io_read(self):
        """Gets the disk_io_read of this HostOverviewResponse.

        磁盘读速率(KB/s)。

        :return: The disk_io_read of this HostOverviewResponse.
        :rtype: float
        """
        return self._disk_io_read

    @disk_io_read.setter
    def disk_io_read(self, disk_io_read):
        """Sets the disk_io_read of this HostOverviewResponse.

        磁盘读速率(KB/s)。

        :param disk_io_read: The disk_io_read of this HostOverviewResponse.
        :type disk_io_read: float
        """
        self._disk_io_read = disk_io_read

    @property
    def disk_io_write(self):
        """Gets the disk_io_write of this HostOverviewResponse.

        磁盘写速率(KB/s)。

        :return: The disk_io_write of this HostOverviewResponse.
        :rtype: float
        """
        return self._disk_io_write

    @disk_io_write.setter
    def disk_io_write(self, disk_io_write):
        """Sets the disk_io_write of this HostOverviewResponse.

        磁盘写速率(KB/s)。

        :param disk_io_write: The disk_io_write of this HostOverviewResponse.
        :type disk_io_write: float
        """
        self._disk_io_write = disk_io_write

    @property
    def tcp_resend_rate(self):
        """Gets the tcp_resend_rate of this HostOverviewResponse.

        TCP协议栈重传率(%)。

        :return: The tcp_resend_rate of this HostOverviewResponse.
        :rtype: float
        """
        return self._tcp_resend_rate

    @tcp_resend_rate.setter
    def tcp_resend_rate(self, tcp_resend_rate):
        """Sets the tcp_resend_rate of this HostOverviewResponse.

        TCP协议栈重传率(%)。

        :param tcp_resend_rate: The tcp_resend_rate of this HostOverviewResponse.
        :type tcp_resend_rate: float
        """
        self._tcp_resend_rate = tcp_resend_rate

    @property
    def net_io(self):
        """Gets the net_io of this HostOverviewResponse.

        网络IO(KB/s)。

        :return: The net_io of this HostOverviewResponse.
        :rtype: float
        """
        return self._net_io

    @net_io.setter
    def net_io(self, net_io):
        """Sets the net_io of this HostOverviewResponse.

        网络IO(KB/s)。

        :param net_io: The net_io of this HostOverviewResponse.
        :type net_io: float
        """
        self._net_io = net_io

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
        if not isinstance(other, HostOverviewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
