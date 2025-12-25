# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerSpec:

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
        'name': 'str',
        'server_type': 'str',
        'flavor_type': 'str',
        'performance_type': 'str',
        'power': 'int',
        'unit': 'int',
        'vcpus': 'int',
        'memory': 'int',
        'storage_capacity': 'int',
        'cpu_name': 'str',
        'cpu_architecture': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'server_type': 'server_type',
        'flavor_type': 'flavor_type',
        'performance_type': 'performance_type',
        'power': 'power',
        'unit': 'unit',
        'vcpus': 'vcpus',
        'memory': 'memory',
        'storage_capacity': 'storage_capacity',
        'cpu_name': 'cpu_name',
        'cpu_architecture': 'cpu_architecture'
    }

    def __init__(self, id=None, name=None, server_type=None, flavor_type=None, performance_type=None, power=None, unit=None, vcpus=None, memory=None, storage_capacity=None, cpu_name=None, cpu_architecture=None):
        r"""ServerSpec

        The model defined in huaweicloud sdk

        :param id: 服务器规格ID
        :type id: str
        :param name: 服务器规格名称。
        :type name: str
        :param server_type: 服务器类型。 COMPUTE: 计算服务器 NETWORK: 网络服务器 BLOCK_STORAGE: 硬盘存储服务器
        :type server_type: str
        :param flavor_type: 服务器发放的资源规格类型
        :type flavor_type: str
        :param performance_type: 服务器规格分类。如通用计算型/云桌面型/网关型等。
        :type performance_type: str
        :param power: 服务器功率（单位：w）
        :type power: int
        :param unit: 设备高度。U位数
        :type unit: int
        :param vcpus: 可用虚拟CPU核数
        :type vcpus: int
        :param memory: 可用内存大小。单位：GB
        :type memory: int
        :param storage_capacity: 可用存储容量。单位：TiB
        :type storage_capacity: int
        :param cpu_name: 名称
        :type cpu_name: str
        :param cpu_architecture: CPU架构
        :type cpu_architecture: str
        """
        
        

        self._id = None
        self._name = None
        self._server_type = None
        self._flavor_type = None
        self._performance_type = None
        self._power = None
        self._unit = None
        self._vcpus = None
        self._memory = None
        self._storage_capacity = None
        self._cpu_name = None
        self._cpu_architecture = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if server_type is not None:
            self.server_type = server_type
        if flavor_type is not None:
            self.flavor_type = flavor_type
        if performance_type is not None:
            self.performance_type = performance_type
        if power is not None:
            self.power = power
        if unit is not None:
            self.unit = unit
        if vcpus is not None:
            self.vcpus = vcpus
        if memory is not None:
            self.memory = memory
        if storage_capacity is not None:
            self.storage_capacity = storage_capacity
        if cpu_name is not None:
            self.cpu_name = cpu_name
        if cpu_architecture is not None:
            self.cpu_architecture = cpu_architecture

    @property
    def id(self):
        r"""Gets the id of this ServerSpec.

        服务器规格ID

        :return: The id of this ServerSpec.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ServerSpec.

        服务器规格ID

        :param id: The id of this ServerSpec.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ServerSpec.

        服务器规格名称。

        :return: The name of this ServerSpec.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ServerSpec.

        服务器规格名称。

        :param name: The name of this ServerSpec.
        :type name: str
        """
        self._name = name

    @property
    def server_type(self):
        r"""Gets the server_type of this ServerSpec.

        服务器类型。 COMPUTE: 计算服务器 NETWORK: 网络服务器 BLOCK_STORAGE: 硬盘存储服务器

        :return: The server_type of this ServerSpec.
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        r"""Sets the server_type of this ServerSpec.

        服务器类型。 COMPUTE: 计算服务器 NETWORK: 网络服务器 BLOCK_STORAGE: 硬盘存储服务器

        :param server_type: The server_type of this ServerSpec.
        :type server_type: str
        """
        self._server_type = server_type

    @property
    def flavor_type(self):
        r"""Gets the flavor_type of this ServerSpec.

        服务器发放的资源规格类型

        :return: The flavor_type of this ServerSpec.
        :rtype: str
        """
        return self._flavor_type

    @flavor_type.setter
    def flavor_type(self, flavor_type):
        r"""Sets the flavor_type of this ServerSpec.

        服务器发放的资源规格类型

        :param flavor_type: The flavor_type of this ServerSpec.
        :type flavor_type: str
        """
        self._flavor_type = flavor_type

    @property
    def performance_type(self):
        r"""Gets the performance_type of this ServerSpec.

        服务器规格分类。如通用计算型/云桌面型/网关型等。

        :return: The performance_type of this ServerSpec.
        :rtype: str
        """
        return self._performance_type

    @performance_type.setter
    def performance_type(self, performance_type):
        r"""Sets the performance_type of this ServerSpec.

        服务器规格分类。如通用计算型/云桌面型/网关型等。

        :param performance_type: The performance_type of this ServerSpec.
        :type performance_type: str
        """
        self._performance_type = performance_type

    @property
    def power(self):
        r"""Gets the power of this ServerSpec.

        服务器功率（单位：w）

        :return: The power of this ServerSpec.
        :rtype: int
        """
        return self._power

    @power.setter
    def power(self, power):
        r"""Sets the power of this ServerSpec.

        服务器功率（单位：w）

        :param power: The power of this ServerSpec.
        :type power: int
        """
        self._power = power

    @property
    def unit(self):
        r"""Gets the unit of this ServerSpec.

        设备高度。U位数

        :return: The unit of this ServerSpec.
        :rtype: int
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this ServerSpec.

        设备高度。U位数

        :param unit: The unit of this ServerSpec.
        :type unit: int
        """
        self._unit = unit

    @property
    def vcpus(self):
        r"""Gets the vcpus of this ServerSpec.

        可用虚拟CPU核数

        :return: The vcpus of this ServerSpec.
        :rtype: int
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        r"""Sets the vcpus of this ServerSpec.

        可用虚拟CPU核数

        :param vcpus: The vcpus of this ServerSpec.
        :type vcpus: int
        """
        self._vcpus = vcpus

    @property
    def memory(self):
        r"""Gets the memory of this ServerSpec.

        可用内存大小。单位：GB

        :return: The memory of this ServerSpec.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this ServerSpec.

        可用内存大小。单位：GB

        :param memory: The memory of this ServerSpec.
        :type memory: int
        """
        self._memory = memory

    @property
    def storage_capacity(self):
        r"""Gets the storage_capacity of this ServerSpec.

        可用存储容量。单位：TiB

        :return: The storage_capacity of this ServerSpec.
        :rtype: int
        """
        return self._storage_capacity

    @storage_capacity.setter
    def storage_capacity(self, storage_capacity):
        r"""Sets the storage_capacity of this ServerSpec.

        可用存储容量。单位：TiB

        :param storage_capacity: The storage_capacity of this ServerSpec.
        :type storage_capacity: int
        """
        self._storage_capacity = storage_capacity

    @property
    def cpu_name(self):
        r"""Gets the cpu_name of this ServerSpec.

        名称

        :return: The cpu_name of this ServerSpec.
        :rtype: str
        """
        return self._cpu_name

    @cpu_name.setter
    def cpu_name(self, cpu_name):
        r"""Sets the cpu_name of this ServerSpec.

        名称

        :param cpu_name: The cpu_name of this ServerSpec.
        :type cpu_name: str
        """
        self._cpu_name = cpu_name

    @property
    def cpu_architecture(self):
        r"""Gets the cpu_architecture of this ServerSpec.

        CPU架构

        :return: The cpu_architecture of this ServerSpec.
        :rtype: str
        """
        return self._cpu_architecture

    @cpu_architecture.setter
    def cpu_architecture(self, cpu_architecture):
        r"""Sets the cpu_architecture of this ServerSpec.

        CPU架构

        :param cpu_architecture: The cpu_architecture of this ServerSpec.
        :type cpu_architecture: str
        """
        self._cpu_architecture = cpu_architecture

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
        if not isinstance(other, ServerSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
