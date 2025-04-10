# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerModelExtendSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cpu': 'str',
        'memory': 'str',
        'disk': 'str',
        'network_interface': 'str',
        'gpu': 'str',
        'bms_flavor': 'str',
        'gpu_count': 'int',
        'numa_count': 'int',
        'os_volume': 'ServerModelExtendSpecOsVolume'
    }

    attribute_map = {
        'cpu': 'cpu',
        'memory': 'memory',
        'disk': 'disk',
        'network_interface': 'network_interface',
        'gpu': 'gpu',
        'bms_flavor': 'bms_flavor',
        'gpu_count': 'gpu_count',
        'numa_count': 'numa_count',
        'os_volume': 'os_volume'
    }

    def __init__(self, cpu=None, memory=None, disk=None, network_interface=None, gpu=None, bms_flavor=None, gpu_count=None, numa_count=None, os_volume=None):
        r"""ServerModelExtendSpec

        The model defined in huaweicloud sdk

        :param cpu: 云手机服务器cpu类型。
        :type cpu: str
        :param memory: 云手机服务器内存类型。
        :type memory: str
        :param disk: 云手机服务器磁盘类型。
        :type disk: str
        :param network_interface: 云手机服务器网络类型。
        :type network_interface: str
        :param gpu: 云手机服务器gpu类型。
        :type gpu: str
        :param bms_flavor: 云手机服务器bms规格。
        :type bms_flavor: str
        :param gpu_count: 云手机服务器gpu数量。
        :type gpu_count: int
        :param numa_count: 云手机服务器numa数量。
        :type numa_count: int
        :param os_volume: 
        :type os_volume: :class:`huaweicloudsdkcph.v1.ServerModelExtendSpecOsVolume`
        """
        
        

        self._cpu = None
        self._memory = None
        self._disk = None
        self._network_interface = None
        self._gpu = None
        self._bms_flavor = None
        self._gpu_count = None
        self._numa_count = None
        self._os_volume = None
        self.discriminator = None

        if cpu is not None:
            self.cpu = cpu
        if memory is not None:
            self.memory = memory
        if disk is not None:
            self.disk = disk
        if network_interface is not None:
            self.network_interface = network_interface
        if gpu is not None:
            self.gpu = gpu
        if bms_flavor is not None:
            self.bms_flavor = bms_flavor
        if gpu_count is not None:
            self.gpu_count = gpu_count
        if numa_count is not None:
            self.numa_count = numa_count
        if os_volume is not None:
            self.os_volume = os_volume

    @property
    def cpu(self):
        r"""Gets the cpu of this ServerModelExtendSpec.

        云手机服务器cpu类型。

        :return: The cpu of this ServerModelExtendSpec.
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this ServerModelExtendSpec.

        云手机服务器cpu类型。

        :param cpu: The cpu of this ServerModelExtendSpec.
        :type cpu: str
        """
        self._cpu = cpu

    @property
    def memory(self):
        r"""Gets the memory of this ServerModelExtendSpec.

        云手机服务器内存类型。

        :return: The memory of this ServerModelExtendSpec.
        :rtype: str
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this ServerModelExtendSpec.

        云手机服务器内存类型。

        :param memory: The memory of this ServerModelExtendSpec.
        :type memory: str
        """
        self._memory = memory

    @property
    def disk(self):
        r"""Gets the disk of this ServerModelExtendSpec.

        云手机服务器磁盘类型。

        :return: The disk of this ServerModelExtendSpec.
        :rtype: str
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        r"""Sets the disk of this ServerModelExtendSpec.

        云手机服务器磁盘类型。

        :param disk: The disk of this ServerModelExtendSpec.
        :type disk: str
        """
        self._disk = disk

    @property
    def network_interface(self):
        r"""Gets the network_interface of this ServerModelExtendSpec.

        云手机服务器网络类型。

        :return: The network_interface of this ServerModelExtendSpec.
        :rtype: str
        """
        return self._network_interface

    @network_interface.setter
    def network_interface(self, network_interface):
        r"""Sets the network_interface of this ServerModelExtendSpec.

        云手机服务器网络类型。

        :param network_interface: The network_interface of this ServerModelExtendSpec.
        :type network_interface: str
        """
        self._network_interface = network_interface

    @property
    def gpu(self):
        r"""Gets the gpu of this ServerModelExtendSpec.

        云手机服务器gpu类型。

        :return: The gpu of this ServerModelExtendSpec.
        :rtype: str
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        r"""Sets the gpu of this ServerModelExtendSpec.

        云手机服务器gpu类型。

        :param gpu: The gpu of this ServerModelExtendSpec.
        :type gpu: str
        """
        self._gpu = gpu

    @property
    def bms_flavor(self):
        r"""Gets the bms_flavor of this ServerModelExtendSpec.

        云手机服务器bms规格。

        :return: The bms_flavor of this ServerModelExtendSpec.
        :rtype: str
        """
        return self._bms_flavor

    @bms_flavor.setter
    def bms_flavor(self, bms_flavor):
        r"""Sets the bms_flavor of this ServerModelExtendSpec.

        云手机服务器bms规格。

        :param bms_flavor: The bms_flavor of this ServerModelExtendSpec.
        :type bms_flavor: str
        """
        self._bms_flavor = bms_flavor

    @property
    def gpu_count(self):
        r"""Gets the gpu_count of this ServerModelExtendSpec.

        云手机服务器gpu数量。

        :return: The gpu_count of this ServerModelExtendSpec.
        :rtype: int
        """
        return self._gpu_count

    @gpu_count.setter
    def gpu_count(self, gpu_count):
        r"""Sets the gpu_count of this ServerModelExtendSpec.

        云手机服务器gpu数量。

        :param gpu_count: The gpu_count of this ServerModelExtendSpec.
        :type gpu_count: int
        """
        self._gpu_count = gpu_count

    @property
    def numa_count(self):
        r"""Gets the numa_count of this ServerModelExtendSpec.

        云手机服务器numa数量。

        :return: The numa_count of this ServerModelExtendSpec.
        :rtype: int
        """
        return self._numa_count

    @numa_count.setter
    def numa_count(self, numa_count):
        r"""Sets the numa_count of this ServerModelExtendSpec.

        云手机服务器numa数量。

        :param numa_count: The numa_count of this ServerModelExtendSpec.
        :type numa_count: int
        """
        self._numa_count = numa_count

    @property
    def os_volume(self):
        r"""Gets the os_volume of this ServerModelExtendSpec.

        :return: The os_volume of this ServerModelExtendSpec.
        :rtype: :class:`huaweicloudsdkcph.v1.ServerModelExtendSpecOsVolume`
        """
        return self._os_volume

    @os_volume.setter
    def os_volume(self, os_volume):
        r"""Sets the os_volume of this ServerModelExtendSpec.

        :param os_volume: The os_volume of this ServerModelExtendSpec.
        :type os_volume: :class:`huaweicloudsdkcph.v1.ServerModelExtendSpecOsVolume`
        """
        self._os_volume = os_volume

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
        if not isinstance(other, ServerModelExtendSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
