# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTaskSpeedReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subtask_name': 'str',
        'progress': 'int',
        'replicatesize': 'int',
        'totalsize': 'int',
        'process_trace': 'str',
        'migrate_speed': 'float',
        'compress_rate': 'float',
        'remain_time': 'int',
        'total_cpu_usage': 'float',
        'agent_cpu_usage': 'float',
        'total_mem_usage': 'float',
        'agent_mem_usage': 'float',
        'total_disk_io': 'float',
        'agent_disk_io': 'float',
        'need_migration_test': 'bool',
        'agent_time': 'str'
    }

    attribute_map = {
        'subtask_name': 'subtask_name',
        'progress': 'progress',
        'replicatesize': 'replicatesize',
        'totalsize': 'totalsize',
        'process_trace': 'process_trace',
        'migrate_speed': 'migrate_speed',
        'compress_rate': 'compress_rate',
        'remain_time': 'remain_time',
        'total_cpu_usage': 'total_cpu_usage',
        'agent_cpu_usage': 'agent_cpu_usage',
        'total_mem_usage': 'total_mem_usage',
        'agent_mem_usage': 'agent_mem_usage',
        'total_disk_io': 'total_disk_io',
        'agent_disk_io': 'agent_disk_io',
        'need_migration_test': 'need_migration_test',
        'agent_time': 'agent_time'
    }

    def __init__(self, subtask_name=None, progress=None, replicatesize=None, totalsize=None, process_trace=None, migrate_speed=None, compress_rate=None, remain_time=None, total_cpu_usage=None, agent_cpu_usage=None, total_mem_usage=None, agent_mem_usage=None, total_disk_io=None, agent_disk_io=None, need_migration_test=None, agent_time=None):
        r"""UpdateTaskSpeedReq

        The model defined in huaweicloud sdk

        :param subtask_name: 当前上报进度的子任务名称，子任务名称包括： 创建虚拟机 CREATE_CLOUD_SERVER 配置安全通道 SSL_CONFIG 挂载代理镜像 ATTACH_AGENT_IMAGE 卸载载代理镜像 DETTACH_AGENT_IMAGE Linux分区格式化 FORMAT_DISK_LINUX Linux分区格式化(文件级级） FORMAT_DISK_LINUX_FILE Linux分区格式化(块级） FORMAT_DISK_LINUX_BLOCK Windows分区格式化 FORMAT_DISK_WINDOWS Linux文件级数据迁移 MIGRATE_LINUX_FILE, Linux块级数据迁移 MIGRATE_LINUX_BLOCK Windows块级数据迁移 MIGRATE_WINDOWS_BLOCK 克隆一个虚拟机 CLONE_VM Linux文件级数据同步 SYNC_LINUX_FILE Linux块级数据同步 SYNC_LINUX_BLOCK Windows块级数据同步 SYNC_WINDOWS_BLOCK Linux配置修改 CONFIGURE_LINUX Linux配置修改(块级）CONFIGURE_LINUX_BLOCK Linux配置修改（文件级） CONFIGURE_LINUX_FILE Windows配置修改 CONFIGURE_WINDOWS
        :type subtask_name: str
        :param progress: 当前上报的子任务的最新百分比进度
        :type progress: int
        :param replicatesize: 当前任务已经复制的数据量大小（B）
        :type replicatesize: int
        :param totalsize: 当前任务的总迁移数据大小
        :type totalsize: int
        :param process_trace: 迁移或同步时，具体的迁移详情
        :type process_trace: str
        :param migrate_speed: 实施迁移速率，单位Mb/s
        :type migrate_speed: float
        :param compress_rate: 实施文件压缩率
        :type compress_rate: float
        :param remain_time: 剩余时间
        :type remain_time: int
        :param total_cpu_usage: 主机的CPU使用率，0到100，单位是百分比
        :type total_cpu_usage: float
        :param agent_cpu_usage: Agent的CPU使用率，0到100，单位是百分比
        :type agent_cpu_usage: float
        :param total_mem_usage: 主机的内存使用值，单位是MB
        :type total_mem_usage: float
        :param agent_mem_usage: Agent的内存使用值，单位是MB
        :type agent_mem_usage: float
        :param total_disk_io: 主机的磁盘I/O值，单位是MB/s
        :type total_disk_io: float
        :param agent_disk_io: Agent的磁盘I/O值，单位是MB/s
        :type agent_disk_io: float
        :param need_migration_test: 是否开启迁移演练
        :type need_migration_test: bool
        :param agent_time: Agent的当前时间，用于超速检测，因为限速值是可以分时间段设置的
        :type agent_time: str
        """
        
        

        self._subtask_name = None
        self._progress = None
        self._replicatesize = None
        self._totalsize = None
        self._process_trace = None
        self._migrate_speed = None
        self._compress_rate = None
        self._remain_time = None
        self._total_cpu_usage = None
        self._agent_cpu_usage = None
        self._total_mem_usage = None
        self._agent_mem_usage = None
        self._total_disk_io = None
        self._agent_disk_io = None
        self._need_migration_test = None
        self._agent_time = None
        self.discriminator = None

        self.subtask_name = subtask_name
        self.progress = progress
        self.replicatesize = replicatesize
        self.totalsize = totalsize
        self.process_trace = process_trace
        if migrate_speed is not None:
            self.migrate_speed = migrate_speed
        if compress_rate is not None:
            self.compress_rate = compress_rate
        if remain_time is not None:
            self.remain_time = remain_time
        if total_cpu_usage is not None:
            self.total_cpu_usage = total_cpu_usage
        if agent_cpu_usage is not None:
            self.agent_cpu_usage = agent_cpu_usage
        if total_mem_usage is not None:
            self.total_mem_usage = total_mem_usage
        if agent_mem_usage is not None:
            self.agent_mem_usage = agent_mem_usage
        if total_disk_io is not None:
            self.total_disk_io = total_disk_io
        if agent_disk_io is not None:
            self.agent_disk_io = agent_disk_io
        if need_migration_test is not None:
            self.need_migration_test = need_migration_test
        if agent_time is not None:
            self.agent_time = agent_time

    @property
    def subtask_name(self):
        r"""Gets the subtask_name of this UpdateTaskSpeedReq.

        当前上报进度的子任务名称，子任务名称包括： 创建虚拟机 CREATE_CLOUD_SERVER 配置安全通道 SSL_CONFIG 挂载代理镜像 ATTACH_AGENT_IMAGE 卸载载代理镜像 DETTACH_AGENT_IMAGE Linux分区格式化 FORMAT_DISK_LINUX Linux分区格式化(文件级级） FORMAT_DISK_LINUX_FILE Linux分区格式化(块级） FORMAT_DISK_LINUX_BLOCK Windows分区格式化 FORMAT_DISK_WINDOWS Linux文件级数据迁移 MIGRATE_LINUX_FILE, Linux块级数据迁移 MIGRATE_LINUX_BLOCK Windows块级数据迁移 MIGRATE_WINDOWS_BLOCK 克隆一个虚拟机 CLONE_VM Linux文件级数据同步 SYNC_LINUX_FILE Linux块级数据同步 SYNC_LINUX_BLOCK Windows块级数据同步 SYNC_WINDOWS_BLOCK Linux配置修改 CONFIGURE_LINUX Linux配置修改(块级）CONFIGURE_LINUX_BLOCK Linux配置修改（文件级） CONFIGURE_LINUX_FILE Windows配置修改 CONFIGURE_WINDOWS

        :return: The subtask_name of this UpdateTaskSpeedReq.
        :rtype: str
        """
        return self._subtask_name

    @subtask_name.setter
    def subtask_name(self, subtask_name):
        r"""Sets the subtask_name of this UpdateTaskSpeedReq.

        当前上报进度的子任务名称，子任务名称包括： 创建虚拟机 CREATE_CLOUD_SERVER 配置安全通道 SSL_CONFIG 挂载代理镜像 ATTACH_AGENT_IMAGE 卸载载代理镜像 DETTACH_AGENT_IMAGE Linux分区格式化 FORMAT_DISK_LINUX Linux分区格式化(文件级级） FORMAT_DISK_LINUX_FILE Linux分区格式化(块级） FORMAT_DISK_LINUX_BLOCK Windows分区格式化 FORMAT_DISK_WINDOWS Linux文件级数据迁移 MIGRATE_LINUX_FILE, Linux块级数据迁移 MIGRATE_LINUX_BLOCK Windows块级数据迁移 MIGRATE_WINDOWS_BLOCK 克隆一个虚拟机 CLONE_VM Linux文件级数据同步 SYNC_LINUX_FILE Linux块级数据同步 SYNC_LINUX_BLOCK Windows块级数据同步 SYNC_WINDOWS_BLOCK Linux配置修改 CONFIGURE_LINUX Linux配置修改(块级）CONFIGURE_LINUX_BLOCK Linux配置修改（文件级） CONFIGURE_LINUX_FILE Windows配置修改 CONFIGURE_WINDOWS

        :param subtask_name: The subtask_name of this UpdateTaskSpeedReq.
        :type subtask_name: str
        """
        self._subtask_name = subtask_name

    @property
    def progress(self):
        r"""Gets the progress of this UpdateTaskSpeedReq.

        当前上报的子任务的最新百分比进度

        :return: The progress of this UpdateTaskSpeedReq.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this UpdateTaskSpeedReq.

        当前上报的子任务的最新百分比进度

        :param progress: The progress of this UpdateTaskSpeedReq.
        :type progress: int
        """
        self._progress = progress

    @property
    def replicatesize(self):
        r"""Gets the replicatesize of this UpdateTaskSpeedReq.

        当前任务已经复制的数据量大小（B）

        :return: The replicatesize of this UpdateTaskSpeedReq.
        :rtype: int
        """
        return self._replicatesize

    @replicatesize.setter
    def replicatesize(self, replicatesize):
        r"""Sets the replicatesize of this UpdateTaskSpeedReq.

        当前任务已经复制的数据量大小（B）

        :param replicatesize: The replicatesize of this UpdateTaskSpeedReq.
        :type replicatesize: int
        """
        self._replicatesize = replicatesize

    @property
    def totalsize(self):
        r"""Gets the totalsize of this UpdateTaskSpeedReq.

        当前任务的总迁移数据大小

        :return: The totalsize of this UpdateTaskSpeedReq.
        :rtype: int
        """
        return self._totalsize

    @totalsize.setter
    def totalsize(self, totalsize):
        r"""Sets the totalsize of this UpdateTaskSpeedReq.

        当前任务的总迁移数据大小

        :param totalsize: The totalsize of this UpdateTaskSpeedReq.
        :type totalsize: int
        """
        self._totalsize = totalsize

    @property
    def process_trace(self):
        r"""Gets the process_trace of this UpdateTaskSpeedReq.

        迁移或同步时，具体的迁移详情

        :return: The process_trace of this UpdateTaskSpeedReq.
        :rtype: str
        """
        return self._process_trace

    @process_trace.setter
    def process_trace(self, process_trace):
        r"""Sets the process_trace of this UpdateTaskSpeedReq.

        迁移或同步时，具体的迁移详情

        :param process_trace: The process_trace of this UpdateTaskSpeedReq.
        :type process_trace: str
        """
        self._process_trace = process_trace

    @property
    def migrate_speed(self):
        r"""Gets the migrate_speed of this UpdateTaskSpeedReq.

        实施迁移速率，单位Mb/s

        :return: The migrate_speed of this UpdateTaskSpeedReq.
        :rtype: float
        """
        return self._migrate_speed

    @migrate_speed.setter
    def migrate_speed(self, migrate_speed):
        r"""Sets the migrate_speed of this UpdateTaskSpeedReq.

        实施迁移速率，单位Mb/s

        :param migrate_speed: The migrate_speed of this UpdateTaskSpeedReq.
        :type migrate_speed: float
        """
        self._migrate_speed = migrate_speed

    @property
    def compress_rate(self):
        r"""Gets the compress_rate of this UpdateTaskSpeedReq.

        实施文件压缩率

        :return: The compress_rate of this UpdateTaskSpeedReq.
        :rtype: float
        """
        return self._compress_rate

    @compress_rate.setter
    def compress_rate(self, compress_rate):
        r"""Sets the compress_rate of this UpdateTaskSpeedReq.

        实施文件压缩率

        :param compress_rate: The compress_rate of this UpdateTaskSpeedReq.
        :type compress_rate: float
        """
        self._compress_rate = compress_rate

    @property
    def remain_time(self):
        r"""Gets the remain_time of this UpdateTaskSpeedReq.

        剩余时间

        :return: The remain_time of this UpdateTaskSpeedReq.
        :rtype: int
        """
        return self._remain_time

    @remain_time.setter
    def remain_time(self, remain_time):
        r"""Sets the remain_time of this UpdateTaskSpeedReq.

        剩余时间

        :param remain_time: The remain_time of this UpdateTaskSpeedReq.
        :type remain_time: int
        """
        self._remain_time = remain_time

    @property
    def total_cpu_usage(self):
        r"""Gets the total_cpu_usage of this UpdateTaskSpeedReq.

        主机的CPU使用率，0到100，单位是百分比

        :return: The total_cpu_usage of this UpdateTaskSpeedReq.
        :rtype: float
        """
        return self._total_cpu_usage

    @total_cpu_usage.setter
    def total_cpu_usage(self, total_cpu_usage):
        r"""Sets the total_cpu_usage of this UpdateTaskSpeedReq.

        主机的CPU使用率，0到100，单位是百分比

        :param total_cpu_usage: The total_cpu_usage of this UpdateTaskSpeedReq.
        :type total_cpu_usage: float
        """
        self._total_cpu_usage = total_cpu_usage

    @property
    def agent_cpu_usage(self):
        r"""Gets the agent_cpu_usage of this UpdateTaskSpeedReq.

        Agent的CPU使用率，0到100，单位是百分比

        :return: The agent_cpu_usage of this UpdateTaskSpeedReq.
        :rtype: float
        """
        return self._agent_cpu_usage

    @agent_cpu_usage.setter
    def agent_cpu_usage(self, agent_cpu_usage):
        r"""Sets the agent_cpu_usage of this UpdateTaskSpeedReq.

        Agent的CPU使用率，0到100，单位是百分比

        :param agent_cpu_usage: The agent_cpu_usage of this UpdateTaskSpeedReq.
        :type agent_cpu_usage: float
        """
        self._agent_cpu_usage = agent_cpu_usage

    @property
    def total_mem_usage(self):
        r"""Gets the total_mem_usage of this UpdateTaskSpeedReq.

        主机的内存使用值，单位是MB

        :return: The total_mem_usage of this UpdateTaskSpeedReq.
        :rtype: float
        """
        return self._total_mem_usage

    @total_mem_usage.setter
    def total_mem_usage(self, total_mem_usage):
        r"""Sets the total_mem_usage of this UpdateTaskSpeedReq.

        主机的内存使用值，单位是MB

        :param total_mem_usage: The total_mem_usage of this UpdateTaskSpeedReq.
        :type total_mem_usage: float
        """
        self._total_mem_usage = total_mem_usage

    @property
    def agent_mem_usage(self):
        r"""Gets the agent_mem_usage of this UpdateTaskSpeedReq.

        Agent的内存使用值，单位是MB

        :return: The agent_mem_usage of this UpdateTaskSpeedReq.
        :rtype: float
        """
        return self._agent_mem_usage

    @agent_mem_usage.setter
    def agent_mem_usage(self, agent_mem_usage):
        r"""Sets the agent_mem_usage of this UpdateTaskSpeedReq.

        Agent的内存使用值，单位是MB

        :param agent_mem_usage: The agent_mem_usage of this UpdateTaskSpeedReq.
        :type agent_mem_usage: float
        """
        self._agent_mem_usage = agent_mem_usage

    @property
    def total_disk_io(self):
        r"""Gets the total_disk_io of this UpdateTaskSpeedReq.

        主机的磁盘I/O值，单位是MB/s

        :return: The total_disk_io of this UpdateTaskSpeedReq.
        :rtype: float
        """
        return self._total_disk_io

    @total_disk_io.setter
    def total_disk_io(self, total_disk_io):
        r"""Sets the total_disk_io of this UpdateTaskSpeedReq.

        主机的磁盘I/O值，单位是MB/s

        :param total_disk_io: The total_disk_io of this UpdateTaskSpeedReq.
        :type total_disk_io: float
        """
        self._total_disk_io = total_disk_io

    @property
    def agent_disk_io(self):
        r"""Gets the agent_disk_io of this UpdateTaskSpeedReq.

        Agent的磁盘I/O值，单位是MB/s

        :return: The agent_disk_io of this UpdateTaskSpeedReq.
        :rtype: float
        """
        return self._agent_disk_io

    @agent_disk_io.setter
    def agent_disk_io(self, agent_disk_io):
        r"""Sets the agent_disk_io of this UpdateTaskSpeedReq.

        Agent的磁盘I/O值，单位是MB/s

        :param agent_disk_io: The agent_disk_io of this UpdateTaskSpeedReq.
        :type agent_disk_io: float
        """
        self._agent_disk_io = agent_disk_io

    @property
    def need_migration_test(self):
        r"""Gets the need_migration_test of this UpdateTaskSpeedReq.

        是否开启迁移演练

        :return: The need_migration_test of this UpdateTaskSpeedReq.
        :rtype: bool
        """
        return self._need_migration_test

    @need_migration_test.setter
    def need_migration_test(self, need_migration_test):
        r"""Sets the need_migration_test of this UpdateTaskSpeedReq.

        是否开启迁移演练

        :param need_migration_test: The need_migration_test of this UpdateTaskSpeedReq.
        :type need_migration_test: bool
        """
        self._need_migration_test = need_migration_test

    @property
    def agent_time(self):
        r"""Gets the agent_time of this UpdateTaskSpeedReq.

        Agent的当前时间，用于超速检测，因为限速值是可以分时间段设置的

        :return: The agent_time of this UpdateTaskSpeedReq.
        :rtype: str
        """
        return self._agent_time

    @agent_time.setter
    def agent_time(self, agent_time):
        r"""Sets the agent_time of this UpdateTaskSpeedReq.

        Agent的当前时间，用于超速检测，因为限速值是可以分时间段设置的

        :param agent_time: The agent_time of this UpdateTaskSpeedReq.
        :type agent_time: str
        """
        self._agent_time = agent_time

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
        if not isinstance(other, UpdateTaskSpeedReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
