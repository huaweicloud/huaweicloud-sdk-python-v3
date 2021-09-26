# coding: utf-8

import re
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
        'migrate_speed': 'float'
    }

    attribute_map = {
        'subtask_name': 'subtask_name',
        'progress': 'progress',
        'replicatesize': 'replicatesize',
        'totalsize': 'totalsize',
        'migrate_speed': 'migrate_speed'
    }

    def __init__(self, subtask_name=None, progress=None, replicatesize=None, totalsize=None, migrate_speed=None):
        """UpdateTaskSpeedReq - a model defined in huaweicloud sdk"""
        
        

        self._subtask_name = None
        self._progress = None
        self._replicatesize = None
        self._totalsize = None
        self._migrate_speed = None
        self.discriminator = None

        self.subtask_name = subtask_name
        self.progress = progress
        self.replicatesize = replicatesize
        self.totalsize = totalsize
        self.migrate_speed = migrate_speed

    @property
    def subtask_name(self):
        """Gets the subtask_name of this UpdateTaskSpeedReq.

        当前上报进度的子任务名称，子任务名称包括： 创建虚拟机 CREATE_CLOUD_SERVER 配置安全通道 SSL_CONFIG 挂载代理镜像 ATTACH_AGENT_IMAGE 卸载载代理镜像 DETTACH_AGENT_IMAGE Linux分区格式化 FORMAT_DISK_LINUX Linux分区格式化(文件级级） FORMAT_DISK_LINUX_FILE Linux分区格式化(块级） FORMAT_DISK_LINUX_BLOCK Windows分区格式化 FORMAT_DISK_WINDOWS Linux文件级数据迁移 MIGRATE_LINUX_FILE, Linux块级数据迁移 MIGRATE_LINUX_BLOCK Windows块级数据迁移 MIGRATE_WINDOWS_BLOCK 克隆一个虚拟机 CLONE_VM Linux文件级数据同步 SYNC_LINUX_FILE Linux块级数据同步 SYNC_LINUX_BLOCK Windows块级数据同步 SYNC_WINDOWS_BLOCK Linux配置修改 CONFIGURE_LINUX Linux配置修改(块级）CONFIGURE_LINUX_BLOCK Linux配置修改（文件级） CONFIGURE_LINUX_FILE Windows配置修改 CONFIGURE_WINDOWS

        :return: The subtask_name of this UpdateTaskSpeedReq.
        :rtype: str
        """
        return self._subtask_name

    @subtask_name.setter
    def subtask_name(self, subtask_name):
        """Sets the subtask_name of this UpdateTaskSpeedReq.

        当前上报进度的子任务名称，子任务名称包括： 创建虚拟机 CREATE_CLOUD_SERVER 配置安全通道 SSL_CONFIG 挂载代理镜像 ATTACH_AGENT_IMAGE 卸载载代理镜像 DETTACH_AGENT_IMAGE Linux分区格式化 FORMAT_DISK_LINUX Linux分区格式化(文件级级） FORMAT_DISK_LINUX_FILE Linux分区格式化(块级） FORMAT_DISK_LINUX_BLOCK Windows分区格式化 FORMAT_DISK_WINDOWS Linux文件级数据迁移 MIGRATE_LINUX_FILE, Linux块级数据迁移 MIGRATE_LINUX_BLOCK Windows块级数据迁移 MIGRATE_WINDOWS_BLOCK 克隆一个虚拟机 CLONE_VM Linux文件级数据同步 SYNC_LINUX_FILE Linux块级数据同步 SYNC_LINUX_BLOCK Windows块级数据同步 SYNC_WINDOWS_BLOCK Linux配置修改 CONFIGURE_LINUX Linux配置修改(块级）CONFIGURE_LINUX_BLOCK Linux配置修改（文件级） CONFIGURE_LINUX_FILE Windows配置修改 CONFIGURE_WINDOWS

        :param subtask_name: The subtask_name of this UpdateTaskSpeedReq.
        :type: str
        """
        self._subtask_name = subtask_name

    @property
    def progress(self):
        """Gets the progress of this UpdateTaskSpeedReq.

        当前上报的子任务的最新百分比进度

        :return: The progress of this UpdateTaskSpeedReq.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this UpdateTaskSpeedReq.

        当前上报的子任务的最新百分比进度

        :param progress: The progress of this UpdateTaskSpeedReq.
        :type: int
        """
        self._progress = progress

    @property
    def replicatesize(self):
        """Gets the replicatesize of this UpdateTaskSpeedReq.

        当前任务已经复制的数据量大小（B）

        :return: The replicatesize of this UpdateTaskSpeedReq.
        :rtype: int
        """
        return self._replicatesize

    @replicatesize.setter
    def replicatesize(self, replicatesize):
        """Sets the replicatesize of this UpdateTaskSpeedReq.

        当前任务已经复制的数据量大小（B）

        :param replicatesize: The replicatesize of this UpdateTaskSpeedReq.
        :type: int
        """
        self._replicatesize = replicatesize

    @property
    def totalsize(self):
        """Gets the totalsize of this UpdateTaskSpeedReq.

        当前任务的总迁移数据大小

        :return: The totalsize of this UpdateTaskSpeedReq.
        :rtype: int
        """
        return self._totalsize

    @totalsize.setter
    def totalsize(self, totalsize):
        """Sets the totalsize of this UpdateTaskSpeedReq.

        当前任务的总迁移数据大小

        :param totalsize: The totalsize of this UpdateTaskSpeedReq.
        :type: int
        """
        self._totalsize = totalsize

    @property
    def migrate_speed(self):
        """Gets the migrate_speed of this UpdateTaskSpeedReq.

        实施迁移速率，单位Mb/s

        :return: The migrate_speed of this UpdateTaskSpeedReq.
        :rtype: float
        """
        return self._migrate_speed

    @migrate_speed.setter
    def migrate_speed(self, migrate_speed):
        """Sets the migrate_speed of this UpdateTaskSpeedReq.

        实施迁移速率，单位Mb/s

        :param migrate_speed: The migrate_speed of this UpdateTaskSpeedReq.
        :type: float
        """
        self._migrate_speed = migrate_speed

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
