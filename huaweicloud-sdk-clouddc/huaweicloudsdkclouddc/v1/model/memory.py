# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Memory:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'capacity_mib': 'int',
        'manufacturer': 'str',
        'memory_device_type': 'str',
        'allowed_speed_mhz': 'int',
        'operating_speed_mhz': 'int',
        'serial_number': 'str',
        'health': 'str',
        'state': 'str',
        'rank_count': 'str',
        'data_width_bits': 'str',
        'part_number': 'str',
        'min_voltage_millivolt': 'str',
        'bom_number': 'str',
        'type_detail': 'str',
        'technology': 'str',
        'position': 'str'
    }

    attribute_map = {
        'name': 'name',
        'capacity_mib': 'capacity_mib',
        'manufacturer': 'manufacturer',
        'memory_device_type': 'memory_device_type',
        'allowed_speed_mhz': 'allowed_speed_mhz',
        'operating_speed_mhz': 'operating_speed_mhz',
        'serial_number': 'serial_number',
        'health': 'health',
        'state': 'state',
        'rank_count': 'rank_count',
        'data_width_bits': 'data_width_bits',
        'part_number': 'part_number',
        'min_voltage_millivolt': 'min_voltage_millivolt',
        'bom_number': 'bom_number',
        'type_detail': 'type_detail',
        'technology': 'technology',
        'position': 'position'
    }

    def __init__(self, name=None, capacity_mib=None, manufacturer=None, memory_device_type=None, allowed_speed_mhz=None, operating_speed_mhz=None, serial_number=None, health=None, state=None, rank_count=None, data_width_bits=None, part_number=None, min_voltage_millivolt=None, bom_number=None, type_detail=None, technology=None, position=None):
        r"""Memory

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param capacity_mib: 表示系统的总内存容量（单位：MiB）
        :type capacity_mib: int
        :param manufacturer: 制造商
        :type manufacturer: str
        :param memory_device_type: 内存类型：DDR4/DDR6
        :type memory_device_type: str
        :param allowed_speed_mhz: 主频（单位：MHz）
        :type allowed_speed_mhz: int
        :param operating_speed_mhz: 当前频率（单位：MHz）
        :type operating_speed_mhz: int
        :param serial_number: 序列号
        :type serial_number: str
        :param health: 健康状态
        :type health: str
        :param state: 启用状态
        :type state: str
        :param rank_count: Rank数量
        :type rank_count: str
        :param data_width_bits: 数据带宽
        :type data_width_bits: str
        :param part_number: 部件编号
        :type part_number: str
        :param min_voltage_millivolt: 最小电压
        :type min_voltage_millivolt: str
        :param bom_number: Bom编码
        :type bom_number: str
        :param type_detail: 类型详细信息
        :type type_detail: str
        :param technology: 技术
        :type technology: str
        :param position: 位置
        :type position: str
        """
        
        

        self._name = None
        self._capacity_mib = None
        self._manufacturer = None
        self._memory_device_type = None
        self._allowed_speed_mhz = None
        self._operating_speed_mhz = None
        self._serial_number = None
        self._health = None
        self._state = None
        self._rank_count = None
        self._data_width_bits = None
        self._part_number = None
        self._min_voltage_millivolt = None
        self._bom_number = None
        self._type_detail = None
        self._technology = None
        self._position = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if capacity_mib is not None:
            self.capacity_mib = capacity_mib
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if memory_device_type is not None:
            self.memory_device_type = memory_device_type
        if allowed_speed_mhz is not None:
            self.allowed_speed_mhz = allowed_speed_mhz
        if operating_speed_mhz is not None:
            self.operating_speed_mhz = operating_speed_mhz
        if serial_number is not None:
            self.serial_number = serial_number
        if health is not None:
            self.health = health
        if state is not None:
            self.state = state
        if rank_count is not None:
            self.rank_count = rank_count
        if data_width_bits is not None:
            self.data_width_bits = data_width_bits
        if part_number is not None:
            self.part_number = part_number
        if min_voltage_millivolt is not None:
            self.min_voltage_millivolt = min_voltage_millivolt
        if bom_number is not None:
            self.bom_number = bom_number
        if type_detail is not None:
            self.type_detail = type_detail
        if technology is not None:
            self.technology = technology
        if position is not None:
            self.position = position

    @property
    def name(self):
        r"""Gets the name of this Memory.

        名称

        :return: The name of this Memory.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Memory.

        名称

        :param name: The name of this Memory.
        :type name: str
        """
        self._name = name

    @property
    def capacity_mib(self):
        r"""Gets the capacity_mib of this Memory.

        表示系统的总内存容量（单位：MiB）

        :return: The capacity_mib of this Memory.
        :rtype: int
        """
        return self._capacity_mib

    @capacity_mib.setter
    def capacity_mib(self, capacity_mib):
        r"""Sets the capacity_mib of this Memory.

        表示系统的总内存容量（单位：MiB）

        :param capacity_mib: The capacity_mib of this Memory.
        :type capacity_mib: int
        """
        self._capacity_mib = capacity_mib

    @property
    def manufacturer(self):
        r"""Gets the manufacturer of this Memory.

        制造商

        :return: The manufacturer of this Memory.
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        r"""Sets the manufacturer of this Memory.

        制造商

        :param manufacturer: The manufacturer of this Memory.
        :type manufacturer: str
        """
        self._manufacturer = manufacturer

    @property
    def memory_device_type(self):
        r"""Gets the memory_device_type of this Memory.

        内存类型：DDR4/DDR6

        :return: The memory_device_type of this Memory.
        :rtype: str
        """
        return self._memory_device_type

    @memory_device_type.setter
    def memory_device_type(self, memory_device_type):
        r"""Sets the memory_device_type of this Memory.

        内存类型：DDR4/DDR6

        :param memory_device_type: The memory_device_type of this Memory.
        :type memory_device_type: str
        """
        self._memory_device_type = memory_device_type

    @property
    def allowed_speed_mhz(self):
        r"""Gets the allowed_speed_mhz of this Memory.

        主频（单位：MHz）

        :return: The allowed_speed_mhz of this Memory.
        :rtype: int
        """
        return self._allowed_speed_mhz

    @allowed_speed_mhz.setter
    def allowed_speed_mhz(self, allowed_speed_mhz):
        r"""Sets the allowed_speed_mhz of this Memory.

        主频（单位：MHz）

        :param allowed_speed_mhz: The allowed_speed_mhz of this Memory.
        :type allowed_speed_mhz: int
        """
        self._allowed_speed_mhz = allowed_speed_mhz

    @property
    def operating_speed_mhz(self):
        r"""Gets the operating_speed_mhz of this Memory.

        当前频率（单位：MHz）

        :return: The operating_speed_mhz of this Memory.
        :rtype: int
        """
        return self._operating_speed_mhz

    @operating_speed_mhz.setter
    def operating_speed_mhz(self, operating_speed_mhz):
        r"""Sets the operating_speed_mhz of this Memory.

        当前频率（单位：MHz）

        :param operating_speed_mhz: The operating_speed_mhz of this Memory.
        :type operating_speed_mhz: int
        """
        self._operating_speed_mhz = operating_speed_mhz

    @property
    def serial_number(self):
        r"""Gets the serial_number of this Memory.

        序列号

        :return: The serial_number of this Memory.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        r"""Sets the serial_number of this Memory.

        序列号

        :param serial_number: The serial_number of this Memory.
        :type serial_number: str
        """
        self._serial_number = serial_number

    @property
    def health(self):
        r"""Gets the health of this Memory.

        健康状态

        :return: The health of this Memory.
        :rtype: str
        """
        return self._health

    @health.setter
    def health(self, health):
        r"""Sets the health of this Memory.

        健康状态

        :param health: The health of this Memory.
        :type health: str
        """
        self._health = health

    @property
    def state(self):
        r"""Gets the state of this Memory.

        启用状态

        :return: The state of this Memory.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this Memory.

        启用状态

        :param state: The state of this Memory.
        :type state: str
        """
        self._state = state

    @property
    def rank_count(self):
        r"""Gets the rank_count of this Memory.

        Rank数量

        :return: The rank_count of this Memory.
        :rtype: str
        """
        return self._rank_count

    @rank_count.setter
    def rank_count(self, rank_count):
        r"""Sets the rank_count of this Memory.

        Rank数量

        :param rank_count: The rank_count of this Memory.
        :type rank_count: str
        """
        self._rank_count = rank_count

    @property
    def data_width_bits(self):
        r"""Gets the data_width_bits of this Memory.

        数据带宽

        :return: The data_width_bits of this Memory.
        :rtype: str
        """
        return self._data_width_bits

    @data_width_bits.setter
    def data_width_bits(self, data_width_bits):
        r"""Sets the data_width_bits of this Memory.

        数据带宽

        :param data_width_bits: The data_width_bits of this Memory.
        :type data_width_bits: str
        """
        self._data_width_bits = data_width_bits

    @property
    def part_number(self):
        r"""Gets the part_number of this Memory.

        部件编号

        :return: The part_number of this Memory.
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        r"""Sets the part_number of this Memory.

        部件编号

        :param part_number: The part_number of this Memory.
        :type part_number: str
        """
        self._part_number = part_number

    @property
    def min_voltage_millivolt(self):
        r"""Gets the min_voltage_millivolt of this Memory.

        最小电压

        :return: The min_voltage_millivolt of this Memory.
        :rtype: str
        """
        return self._min_voltage_millivolt

    @min_voltage_millivolt.setter
    def min_voltage_millivolt(self, min_voltage_millivolt):
        r"""Sets the min_voltage_millivolt of this Memory.

        最小电压

        :param min_voltage_millivolt: The min_voltage_millivolt of this Memory.
        :type min_voltage_millivolt: str
        """
        self._min_voltage_millivolt = min_voltage_millivolt

    @property
    def bom_number(self):
        r"""Gets the bom_number of this Memory.

        Bom编码

        :return: The bom_number of this Memory.
        :rtype: str
        """
        return self._bom_number

    @bom_number.setter
    def bom_number(self, bom_number):
        r"""Sets the bom_number of this Memory.

        Bom编码

        :param bom_number: The bom_number of this Memory.
        :type bom_number: str
        """
        self._bom_number = bom_number

    @property
    def type_detail(self):
        r"""Gets the type_detail of this Memory.

        类型详细信息

        :return: The type_detail of this Memory.
        :rtype: str
        """
        return self._type_detail

    @type_detail.setter
    def type_detail(self, type_detail):
        r"""Sets the type_detail of this Memory.

        类型详细信息

        :param type_detail: The type_detail of this Memory.
        :type type_detail: str
        """
        self._type_detail = type_detail

    @property
    def technology(self):
        r"""Gets the technology of this Memory.

        技术

        :return: The technology of this Memory.
        :rtype: str
        """
        return self._technology

    @technology.setter
    def technology(self, technology):
        r"""Sets the technology of this Memory.

        技术

        :param technology: The technology of this Memory.
        :type technology: str
        """
        self._technology = technology

    @property
    def position(self):
        r"""Gets the position of this Memory.

        位置

        :return: The position of this Memory.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        r"""Sets the position of this Memory.

        位置

        :param position: The position of this Memory.
        :type position: str
        """
        self._position = position

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
        if not isinstance(other, Memory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
