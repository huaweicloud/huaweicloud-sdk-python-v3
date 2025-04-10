# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'running_status': 'str',
        'cpu_usage': 'str',
        'memory_usage': 'str',
        'disk_usage': 'str',
        'total_memory': 'str',
        'available_memory': 'str',
        'total_hard_disk_space': 'str',
        'available_hard_disk_space': 'str',
        'network_read': 'str',
        'network_write': 'str'
    }

    attribute_map = {
        'running_status': 'running_status',
        'cpu_usage': 'cpu_usage',
        'memory_usage': 'memory_usage',
        'disk_usage': 'disk_usage',
        'total_memory': 'total_memory',
        'available_memory': 'available_memory',
        'total_hard_disk_space': 'total_hard_disk_space',
        'available_hard_disk_space': 'available_hard_disk_space',
        'network_read': 'network_read',
        'network_write': 'network_write'
    }

    def __init__(self, running_status=None, cpu_usage=None, memory_usage=None, disk_usage=None, total_memory=None, available_memory=None, total_hard_disk_space=None, available_hard_disk_space=None, network_read=None, network_write=None):
        r"""NodeDetail

        The model defined in huaweicloud sdk

        :param running_status: 运行状态。
        :type running_status: str
        :param cpu_usage: CPU使用率。
        :type cpu_usage: str
        :param memory_usage: 内存使用率。
        :type memory_usage: str
        :param disk_usage: 硬盘使用率。
        :type disk_usage: str
        :param total_memory: 总内存。单位MB。
        :type total_memory: str
        :param available_memory: 可用内存。单位MB。
        :type available_memory: str
        :param total_hard_disk_space: 总硬盘空间。单位GB。
        :type total_hard_disk_space: str
        :param available_hard_disk_space: 可用硬盘空间。单位GB。
        :type available_hard_disk_space: str
        :param network_read: 网络读取速度。单位Byte/s。
        :type network_read: str
        :param network_write: 网络写入速度。单位Byte/s。
        :type network_write: str
        """
        
        

        self._running_status = None
        self._cpu_usage = None
        self._memory_usage = None
        self._disk_usage = None
        self._total_memory = None
        self._available_memory = None
        self._total_hard_disk_space = None
        self._available_hard_disk_space = None
        self._network_read = None
        self._network_write = None
        self.discriminator = None

        if running_status is not None:
            self.running_status = running_status
        if cpu_usage is not None:
            self.cpu_usage = cpu_usage
        if memory_usage is not None:
            self.memory_usage = memory_usage
        if disk_usage is not None:
            self.disk_usage = disk_usage
        if total_memory is not None:
            self.total_memory = total_memory
        if available_memory is not None:
            self.available_memory = available_memory
        if total_hard_disk_space is not None:
            self.total_hard_disk_space = total_hard_disk_space
        if available_hard_disk_space is not None:
            self.available_hard_disk_space = available_hard_disk_space
        if network_read is not None:
            self.network_read = network_read
        if network_write is not None:
            self.network_write = network_write

    @property
    def running_status(self):
        r"""Gets the running_status of this NodeDetail.

        运行状态。

        :return: The running_status of this NodeDetail.
        :rtype: str
        """
        return self._running_status

    @running_status.setter
    def running_status(self, running_status):
        r"""Sets the running_status of this NodeDetail.

        运行状态。

        :param running_status: The running_status of this NodeDetail.
        :type running_status: str
        """
        self._running_status = running_status

    @property
    def cpu_usage(self):
        r"""Gets the cpu_usage of this NodeDetail.

        CPU使用率。

        :return: The cpu_usage of this NodeDetail.
        :rtype: str
        """
        return self._cpu_usage

    @cpu_usage.setter
    def cpu_usage(self, cpu_usage):
        r"""Sets the cpu_usage of this NodeDetail.

        CPU使用率。

        :param cpu_usage: The cpu_usage of this NodeDetail.
        :type cpu_usage: str
        """
        self._cpu_usage = cpu_usage

    @property
    def memory_usage(self):
        r"""Gets the memory_usage of this NodeDetail.

        内存使用率。

        :return: The memory_usage of this NodeDetail.
        :rtype: str
        """
        return self._memory_usage

    @memory_usage.setter
    def memory_usage(self, memory_usage):
        r"""Sets the memory_usage of this NodeDetail.

        内存使用率。

        :param memory_usage: The memory_usage of this NodeDetail.
        :type memory_usage: str
        """
        self._memory_usage = memory_usage

    @property
    def disk_usage(self):
        r"""Gets the disk_usage of this NodeDetail.

        硬盘使用率。

        :return: The disk_usage of this NodeDetail.
        :rtype: str
        """
        return self._disk_usage

    @disk_usage.setter
    def disk_usage(self, disk_usage):
        r"""Sets the disk_usage of this NodeDetail.

        硬盘使用率。

        :param disk_usage: The disk_usage of this NodeDetail.
        :type disk_usage: str
        """
        self._disk_usage = disk_usage

    @property
    def total_memory(self):
        r"""Gets the total_memory of this NodeDetail.

        总内存。单位MB。

        :return: The total_memory of this NodeDetail.
        :rtype: str
        """
        return self._total_memory

    @total_memory.setter
    def total_memory(self, total_memory):
        r"""Sets the total_memory of this NodeDetail.

        总内存。单位MB。

        :param total_memory: The total_memory of this NodeDetail.
        :type total_memory: str
        """
        self._total_memory = total_memory

    @property
    def available_memory(self):
        r"""Gets the available_memory of this NodeDetail.

        可用内存。单位MB。

        :return: The available_memory of this NodeDetail.
        :rtype: str
        """
        return self._available_memory

    @available_memory.setter
    def available_memory(self, available_memory):
        r"""Sets the available_memory of this NodeDetail.

        可用内存。单位MB。

        :param available_memory: The available_memory of this NodeDetail.
        :type available_memory: str
        """
        self._available_memory = available_memory

    @property
    def total_hard_disk_space(self):
        r"""Gets the total_hard_disk_space of this NodeDetail.

        总硬盘空间。单位GB。

        :return: The total_hard_disk_space of this NodeDetail.
        :rtype: str
        """
        return self._total_hard_disk_space

    @total_hard_disk_space.setter
    def total_hard_disk_space(self, total_hard_disk_space):
        r"""Sets the total_hard_disk_space of this NodeDetail.

        总硬盘空间。单位GB。

        :param total_hard_disk_space: The total_hard_disk_space of this NodeDetail.
        :type total_hard_disk_space: str
        """
        self._total_hard_disk_space = total_hard_disk_space

    @property
    def available_hard_disk_space(self):
        r"""Gets the available_hard_disk_space of this NodeDetail.

        可用硬盘空间。单位GB。

        :return: The available_hard_disk_space of this NodeDetail.
        :rtype: str
        """
        return self._available_hard_disk_space

    @available_hard_disk_space.setter
    def available_hard_disk_space(self, available_hard_disk_space):
        r"""Sets the available_hard_disk_space of this NodeDetail.

        可用硬盘空间。单位GB。

        :param available_hard_disk_space: The available_hard_disk_space of this NodeDetail.
        :type available_hard_disk_space: str
        """
        self._available_hard_disk_space = available_hard_disk_space

    @property
    def network_read(self):
        r"""Gets the network_read of this NodeDetail.

        网络读取速度。单位Byte/s。

        :return: The network_read of this NodeDetail.
        :rtype: str
        """
        return self._network_read

    @network_read.setter
    def network_read(self, network_read):
        r"""Sets the network_read of this NodeDetail.

        网络读取速度。单位Byte/s。

        :param network_read: The network_read of this NodeDetail.
        :type network_read: str
        """
        self._network_read = network_read

    @property
    def network_write(self):
        r"""Gets the network_write of this NodeDetail.

        网络写入速度。单位Byte/s。

        :return: The network_write of this NodeDetail.
        :rtype: str
        """
        return self._network_write

    @network_write.setter
    def network_write(self, network_write):
        r"""Sets the network_write of this NodeDetail.

        网络写入速度。单位Byte/s。

        :param network_write: The network_write of this NodeDetail.
        :type network_write: str
        """
        self._network_write = network_write

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
        if not isinstance(other, NodeDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
