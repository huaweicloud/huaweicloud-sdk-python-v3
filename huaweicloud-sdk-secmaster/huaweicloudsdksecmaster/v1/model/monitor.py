# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Monitor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cpu_idle': 'str',
        'cpu_usage': 'str',
        'disk_count': 'str',
        'disk_usage': 'str',
        'down_pps': 'str',
        'health_status': 'str',
        'heart_beat': 'str',
        'heart_beat_time': 'int',
        'memory_cache': 'str',
        'memory_count': 'str',
        'memory_free': 'str',
        'memory_shared': 'str',
        'memory_usage': 'str',
        'mini_on_online': 'str',
        'read_rate': 'str',
        'up_pps': 'str',
        'write_rate': 'str'
    }

    attribute_map = {
        'cpu_idle': 'cpu_idle',
        'cpu_usage': 'cpu_usage',
        'disk_count': 'disk_count',
        'disk_usage': 'disk_usage',
        'down_pps': 'down_pps',
        'health_status': 'health_status',
        'heart_beat': 'heart_beat',
        'heart_beat_time': 'heart_beat_time',
        'memory_cache': 'memory_cache',
        'memory_count': 'memory_count',
        'memory_free': 'memory_free',
        'memory_shared': 'memory_shared',
        'memory_usage': 'memory_usage',
        'mini_on_online': 'mini_on_online',
        'read_rate': 'read_rate',
        'up_pps': 'up_pps',
        'write_rate': 'write_rate'
    }

    def __init__(self, cpu_idle=None, cpu_usage=None, disk_count=None, disk_usage=None, down_pps=None, health_status=None, heart_beat=None, heart_beat_time=None, memory_cache=None, memory_count=None, memory_free=None, memory_shared=None, memory_usage=None, mini_on_online=None, read_rate=None, up_pps=None, write_rate=None):
        r"""Monitor

        The model defined in huaweicloud sdk

        :param cpu_idle: CPU 空闲时间的百分比
        :type cpu_idle: str
        :param cpu_usage: CPU 当前的使用率
        :type cpu_usage: str
        :param disk_count: 系统中磁盘设备的数量
        :type disk_count: str
        :param disk_usage: 当前磁盘空间使用量
        :type disk_usage: str
        :param down_pps: 下载数据包每秒数量
        :type down_pps: str
        :param health_status: **参数解释**: 节点的健康状态 - NORMAL 正常 - ANOMALIES 异常 - FAULTS 故障 - LOST_CONTACT 失联  **约束限制** 不涉及 **取值范围**: - NORMAL - ANOMALIES - FAULTS - LOST_CONTACT  **默认值** 不涉及
        :type health_status: str
        :param heart_beat: **参数解释**: 节点是否成功收到心跳信号 - ONLINE 在线 - OFFLINE 离线  **约束限制** 不涉及 **取值范围**: - ONLINE - OFFLINE  **默认值** 不涉及
        :type heart_beat: str
        :param heart_beat_time: 最后一次接收到心跳信号的时间
        :type heart_beat_time: int
        :param memory_cache: 缓存数据的内存大小
        :type memory_cache: str
        :param memory_count: 物理内存条数量
        :type memory_count: str
        :param memory_free: 当前空闲的物理内存量
        :type memory_free: str
        :param memory_shared: 多个进程共享使用的内存总量
        :type memory_shared: str
        :param memory_usage: 已使用的物理内存量
        :type memory_usage: str
        :param mini_on_online: 是否在线
        :type mini_on_online: str
        :param read_rate: 磁盘读取速率
        :type read_rate: str
        :param up_pps: 上传数据包每秒数量
        :type up_pps: str
        :param write_rate: 磁盘写入速率
        :type write_rate: str
        """
        
        

        self._cpu_idle = None
        self._cpu_usage = None
        self._disk_count = None
        self._disk_usage = None
        self._down_pps = None
        self._health_status = None
        self._heart_beat = None
        self._heart_beat_time = None
        self._memory_cache = None
        self._memory_count = None
        self._memory_free = None
        self._memory_shared = None
        self._memory_usage = None
        self._mini_on_online = None
        self._read_rate = None
        self._up_pps = None
        self._write_rate = None
        self.discriminator = None

        if cpu_idle is not None:
            self.cpu_idle = cpu_idle
        if cpu_usage is not None:
            self.cpu_usage = cpu_usage
        if disk_count is not None:
            self.disk_count = disk_count
        if disk_usage is not None:
            self.disk_usage = disk_usage
        if down_pps is not None:
            self.down_pps = down_pps
        if health_status is not None:
            self.health_status = health_status
        if heart_beat is not None:
            self.heart_beat = heart_beat
        if heart_beat_time is not None:
            self.heart_beat_time = heart_beat_time
        if memory_cache is not None:
            self.memory_cache = memory_cache
        if memory_count is not None:
            self.memory_count = memory_count
        if memory_free is not None:
            self.memory_free = memory_free
        if memory_shared is not None:
            self.memory_shared = memory_shared
        if memory_usage is not None:
            self.memory_usage = memory_usage
        if mini_on_online is not None:
            self.mini_on_online = mini_on_online
        if read_rate is not None:
            self.read_rate = read_rate
        if up_pps is not None:
            self.up_pps = up_pps
        if write_rate is not None:
            self.write_rate = write_rate

    @property
    def cpu_idle(self):
        r"""Gets the cpu_idle of this Monitor.

        CPU 空闲时间的百分比

        :return: The cpu_idle of this Monitor.
        :rtype: str
        """
        return self._cpu_idle

    @cpu_idle.setter
    def cpu_idle(self, cpu_idle):
        r"""Sets the cpu_idle of this Monitor.

        CPU 空闲时间的百分比

        :param cpu_idle: The cpu_idle of this Monitor.
        :type cpu_idle: str
        """
        self._cpu_idle = cpu_idle

    @property
    def cpu_usage(self):
        r"""Gets the cpu_usage of this Monitor.

        CPU 当前的使用率

        :return: The cpu_usage of this Monitor.
        :rtype: str
        """
        return self._cpu_usage

    @cpu_usage.setter
    def cpu_usage(self, cpu_usage):
        r"""Sets the cpu_usage of this Monitor.

        CPU 当前的使用率

        :param cpu_usage: The cpu_usage of this Monitor.
        :type cpu_usage: str
        """
        self._cpu_usage = cpu_usage

    @property
    def disk_count(self):
        r"""Gets the disk_count of this Monitor.

        系统中磁盘设备的数量

        :return: The disk_count of this Monitor.
        :rtype: str
        """
        return self._disk_count

    @disk_count.setter
    def disk_count(self, disk_count):
        r"""Sets the disk_count of this Monitor.

        系统中磁盘设备的数量

        :param disk_count: The disk_count of this Monitor.
        :type disk_count: str
        """
        self._disk_count = disk_count

    @property
    def disk_usage(self):
        r"""Gets the disk_usage of this Monitor.

        当前磁盘空间使用量

        :return: The disk_usage of this Monitor.
        :rtype: str
        """
        return self._disk_usage

    @disk_usage.setter
    def disk_usage(self, disk_usage):
        r"""Sets the disk_usage of this Monitor.

        当前磁盘空间使用量

        :param disk_usage: The disk_usage of this Monitor.
        :type disk_usage: str
        """
        self._disk_usage = disk_usage

    @property
    def down_pps(self):
        r"""Gets the down_pps of this Monitor.

        下载数据包每秒数量

        :return: The down_pps of this Monitor.
        :rtype: str
        """
        return self._down_pps

    @down_pps.setter
    def down_pps(self, down_pps):
        r"""Sets the down_pps of this Monitor.

        下载数据包每秒数量

        :param down_pps: The down_pps of this Monitor.
        :type down_pps: str
        """
        self._down_pps = down_pps

    @property
    def health_status(self):
        r"""Gets the health_status of this Monitor.

        **参数解释**: 节点的健康状态 - NORMAL 正常 - ANOMALIES 异常 - FAULTS 故障 - LOST_CONTACT 失联  **约束限制** 不涉及 **取值范围**: - NORMAL - ANOMALIES - FAULTS - LOST_CONTACT  **默认值** 不涉及

        :return: The health_status of this Monitor.
        :rtype: str
        """
        return self._health_status

    @health_status.setter
    def health_status(self, health_status):
        r"""Sets the health_status of this Monitor.

        **参数解释**: 节点的健康状态 - NORMAL 正常 - ANOMALIES 异常 - FAULTS 故障 - LOST_CONTACT 失联  **约束限制** 不涉及 **取值范围**: - NORMAL - ANOMALIES - FAULTS - LOST_CONTACT  **默认值** 不涉及

        :param health_status: The health_status of this Monitor.
        :type health_status: str
        """
        self._health_status = health_status

    @property
    def heart_beat(self):
        r"""Gets the heart_beat of this Monitor.

        **参数解释**: 节点是否成功收到心跳信号 - ONLINE 在线 - OFFLINE 离线  **约束限制** 不涉及 **取值范围**: - ONLINE - OFFLINE  **默认值** 不涉及

        :return: The heart_beat of this Monitor.
        :rtype: str
        """
        return self._heart_beat

    @heart_beat.setter
    def heart_beat(self, heart_beat):
        r"""Sets the heart_beat of this Monitor.

        **参数解释**: 节点是否成功收到心跳信号 - ONLINE 在线 - OFFLINE 离线  **约束限制** 不涉及 **取值范围**: - ONLINE - OFFLINE  **默认值** 不涉及

        :param heart_beat: The heart_beat of this Monitor.
        :type heart_beat: str
        """
        self._heart_beat = heart_beat

    @property
    def heart_beat_time(self):
        r"""Gets the heart_beat_time of this Monitor.

        最后一次接收到心跳信号的时间

        :return: The heart_beat_time of this Monitor.
        :rtype: int
        """
        return self._heart_beat_time

    @heart_beat_time.setter
    def heart_beat_time(self, heart_beat_time):
        r"""Sets the heart_beat_time of this Monitor.

        最后一次接收到心跳信号的时间

        :param heart_beat_time: The heart_beat_time of this Monitor.
        :type heart_beat_time: int
        """
        self._heart_beat_time = heart_beat_time

    @property
    def memory_cache(self):
        r"""Gets the memory_cache of this Monitor.

        缓存数据的内存大小

        :return: The memory_cache of this Monitor.
        :rtype: str
        """
        return self._memory_cache

    @memory_cache.setter
    def memory_cache(self, memory_cache):
        r"""Sets the memory_cache of this Monitor.

        缓存数据的内存大小

        :param memory_cache: The memory_cache of this Monitor.
        :type memory_cache: str
        """
        self._memory_cache = memory_cache

    @property
    def memory_count(self):
        r"""Gets the memory_count of this Monitor.

        物理内存条数量

        :return: The memory_count of this Monitor.
        :rtype: str
        """
        return self._memory_count

    @memory_count.setter
    def memory_count(self, memory_count):
        r"""Sets the memory_count of this Monitor.

        物理内存条数量

        :param memory_count: The memory_count of this Monitor.
        :type memory_count: str
        """
        self._memory_count = memory_count

    @property
    def memory_free(self):
        r"""Gets the memory_free of this Monitor.

        当前空闲的物理内存量

        :return: The memory_free of this Monitor.
        :rtype: str
        """
        return self._memory_free

    @memory_free.setter
    def memory_free(self, memory_free):
        r"""Sets the memory_free of this Monitor.

        当前空闲的物理内存量

        :param memory_free: The memory_free of this Monitor.
        :type memory_free: str
        """
        self._memory_free = memory_free

    @property
    def memory_shared(self):
        r"""Gets the memory_shared of this Monitor.

        多个进程共享使用的内存总量

        :return: The memory_shared of this Monitor.
        :rtype: str
        """
        return self._memory_shared

    @memory_shared.setter
    def memory_shared(self, memory_shared):
        r"""Sets the memory_shared of this Monitor.

        多个进程共享使用的内存总量

        :param memory_shared: The memory_shared of this Monitor.
        :type memory_shared: str
        """
        self._memory_shared = memory_shared

    @property
    def memory_usage(self):
        r"""Gets the memory_usage of this Monitor.

        已使用的物理内存量

        :return: The memory_usage of this Monitor.
        :rtype: str
        """
        return self._memory_usage

    @memory_usage.setter
    def memory_usage(self, memory_usage):
        r"""Sets the memory_usage of this Monitor.

        已使用的物理内存量

        :param memory_usage: The memory_usage of this Monitor.
        :type memory_usage: str
        """
        self._memory_usage = memory_usage

    @property
    def mini_on_online(self):
        r"""Gets the mini_on_online of this Monitor.

        是否在线

        :return: The mini_on_online of this Monitor.
        :rtype: str
        """
        return self._mini_on_online

    @mini_on_online.setter
    def mini_on_online(self, mini_on_online):
        r"""Sets the mini_on_online of this Monitor.

        是否在线

        :param mini_on_online: The mini_on_online of this Monitor.
        :type mini_on_online: str
        """
        self._mini_on_online = mini_on_online

    @property
    def read_rate(self):
        r"""Gets the read_rate of this Monitor.

        磁盘读取速率

        :return: The read_rate of this Monitor.
        :rtype: str
        """
        return self._read_rate

    @read_rate.setter
    def read_rate(self, read_rate):
        r"""Sets the read_rate of this Monitor.

        磁盘读取速率

        :param read_rate: The read_rate of this Monitor.
        :type read_rate: str
        """
        self._read_rate = read_rate

    @property
    def up_pps(self):
        r"""Gets the up_pps of this Monitor.

        上传数据包每秒数量

        :return: The up_pps of this Monitor.
        :rtype: str
        """
        return self._up_pps

    @up_pps.setter
    def up_pps(self, up_pps):
        r"""Sets the up_pps of this Monitor.

        上传数据包每秒数量

        :param up_pps: The up_pps of this Monitor.
        :type up_pps: str
        """
        self._up_pps = up_pps

    @property
    def write_rate(self):
        r"""Gets the write_rate of this Monitor.

        磁盘写入速率

        :return: The write_rate of this Monitor.
        :rtype: str
        """
        return self._write_rate

    @write_rate.setter
    def write_rate(self, write_rate):
        r"""Sets the write_rate of this Monitor.

        磁盘写入速率

        :param write_rate: The write_rate of this Monitor.
        :type write_rate: str
        """
        self._write_rate = write_rate

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Monitor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
