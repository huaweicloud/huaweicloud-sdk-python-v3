# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Processors:

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
        'manufacturer': 'str',
        'model': 'str',
        'total_cores': 'int',
        'total_enabled_cores': 'str',
        'total_threads': 'int',
        'total_enabled_threads': 'str',
        'socket': 'int',
        'max_speed_mhz': 'int',
        'temperature': 'int',
        'l1_cache_kib': 'int',
        'l2_cache_kib': 'int',
        'l3_cache_kib': 'int',
        'frequency_mhz': 'int',
        'other_parameters': 'str',
        'serial_number': 'str',
        'health': 'str',
        'state': 'str'
    }

    attribute_map = {
        'name': 'name',
        'manufacturer': 'manufacturer',
        'model': 'model',
        'total_cores': 'total_cores',
        'total_enabled_cores': 'total_enabled_cores',
        'total_threads': 'total_threads',
        'total_enabled_threads': 'total_enabled_threads',
        'socket': 'socket',
        'max_speed_mhz': 'max_speed_mhz',
        'temperature': 'temperature',
        'l1_cache_kib': 'l1_cache_kib',
        'l2_cache_kib': 'l2_cache_kib',
        'l3_cache_kib': 'l3_cache_kib',
        'frequency_mhz': 'frequency_mhz',
        'other_parameters': 'other_parameters',
        'serial_number': 'serial_number',
        'health': 'health',
        'state': 'state'
    }

    def __init__(self, name=None, manufacturer=None, model=None, total_cores=None, total_enabled_cores=None, total_threads=None, total_enabled_threads=None, socket=None, max_speed_mhz=None, temperature=None, l1_cache_kib=None, l2_cache_kib=None, l3_cache_kib=None, frequency_mhz=None, other_parameters=None, serial_number=None, health=None, state=None):
        r"""Processors

        The model defined in huaweicloud sdk

        :param name: 处理器名称
        :type name: str
        :param manufacturer: 制造商
        :type manufacturer: str
        :param model: 处理器型号
        :type model: str
        :param total_cores: 处理器的总核数
        :type total_cores: int
        :param total_enabled_cores: 启用的核心数
        :type total_enabled_cores: str
        :param total_threads: 处理器的总线程数
        :type total_threads: int
        :param total_enabled_threads: 启用的总线程
        :type total_enabled_threads: str
        :param socket: 处理器的插槽号
        :type socket: int
        :param max_speed_mhz: 处理器的最大主频（单位：MHz）
        :type max_speed_mhz: int
        :param temperature: 处理器的温度
        :type temperature: int
        :param l1_cache_kib: 一级缓存（单位：KiB）
        :type l1_cache_kib: int
        :param l2_cache_kib: 二级缓存（单位：KiB）
        :type l2_cache_kib: int
        :param l3_cache_kib: 三级缓存（单位：KiB）
        :type l3_cache_kib: int
        :param frequency_mhz: 处理器的主频
        :type frequency_mhz: int
        :param other_parameters: 其他参数
        :type other_parameters: str
        :param serial_number: 序列号
        :type serial_number: str
        :param health: 健康状态
        :type health: str
        :param state: 状态
        :type state: str
        """
        
        

        self._name = None
        self._manufacturer = None
        self._model = None
        self._total_cores = None
        self._total_enabled_cores = None
        self._total_threads = None
        self._total_enabled_threads = None
        self._socket = None
        self._max_speed_mhz = None
        self._temperature = None
        self._l1_cache_kib = None
        self._l2_cache_kib = None
        self._l3_cache_kib = None
        self._frequency_mhz = None
        self._other_parameters = None
        self._serial_number = None
        self._health = None
        self._state = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if model is not None:
            self.model = model
        if total_cores is not None:
            self.total_cores = total_cores
        if total_enabled_cores is not None:
            self.total_enabled_cores = total_enabled_cores
        if total_threads is not None:
            self.total_threads = total_threads
        if total_enabled_threads is not None:
            self.total_enabled_threads = total_enabled_threads
        if socket is not None:
            self.socket = socket
        if max_speed_mhz is not None:
            self.max_speed_mhz = max_speed_mhz
        if temperature is not None:
            self.temperature = temperature
        if l1_cache_kib is not None:
            self.l1_cache_kib = l1_cache_kib
        if l2_cache_kib is not None:
            self.l2_cache_kib = l2_cache_kib
        if l3_cache_kib is not None:
            self.l3_cache_kib = l3_cache_kib
        if frequency_mhz is not None:
            self.frequency_mhz = frequency_mhz
        if other_parameters is not None:
            self.other_parameters = other_parameters
        if serial_number is not None:
            self.serial_number = serial_number
        if health is not None:
            self.health = health
        if state is not None:
            self.state = state

    @property
    def name(self):
        r"""Gets the name of this Processors.

        处理器名称

        :return: The name of this Processors.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Processors.

        处理器名称

        :param name: The name of this Processors.
        :type name: str
        """
        self._name = name

    @property
    def manufacturer(self):
        r"""Gets the manufacturer of this Processors.

        制造商

        :return: The manufacturer of this Processors.
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        r"""Sets the manufacturer of this Processors.

        制造商

        :param manufacturer: The manufacturer of this Processors.
        :type manufacturer: str
        """
        self._manufacturer = manufacturer

    @property
    def model(self):
        r"""Gets the model of this Processors.

        处理器型号

        :return: The model of this Processors.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        r"""Sets the model of this Processors.

        处理器型号

        :param model: The model of this Processors.
        :type model: str
        """
        self._model = model

    @property
    def total_cores(self):
        r"""Gets the total_cores of this Processors.

        处理器的总核数

        :return: The total_cores of this Processors.
        :rtype: int
        """
        return self._total_cores

    @total_cores.setter
    def total_cores(self, total_cores):
        r"""Sets the total_cores of this Processors.

        处理器的总核数

        :param total_cores: The total_cores of this Processors.
        :type total_cores: int
        """
        self._total_cores = total_cores

    @property
    def total_enabled_cores(self):
        r"""Gets the total_enabled_cores of this Processors.

        启用的核心数

        :return: The total_enabled_cores of this Processors.
        :rtype: str
        """
        return self._total_enabled_cores

    @total_enabled_cores.setter
    def total_enabled_cores(self, total_enabled_cores):
        r"""Sets the total_enabled_cores of this Processors.

        启用的核心数

        :param total_enabled_cores: The total_enabled_cores of this Processors.
        :type total_enabled_cores: str
        """
        self._total_enabled_cores = total_enabled_cores

    @property
    def total_threads(self):
        r"""Gets the total_threads of this Processors.

        处理器的总线程数

        :return: The total_threads of this Processors.
        :rtype: int
        """
        return self._total_threads

    @total_threads.setter
    def total_threads(self, total_threads):
        r"""Sets the total_threads of this Processors.

        处理器的总线程数

        :param total_threads: The total_threads of this Processors.
        :type total_threads: int
        """
        self._total_threads = total_threads

    @property
    def total_enabled_threads(self):
        r"""Gets the total_enabled_threads of this Processors.

        启用的总线程

        :return: The total_enabled_threads of this Processors.
        :rtype: str
        """
        return self._total_enabled_threads

    @total_enabled_threads.setter
    def total_enabled_threads(self, total_enabled_threads):
        r"""Sets the total_enabled_threads of this Processors.

        启用的总线程

        :param total_enabled_threads: The total_enabled_threads of this Processors.
        :type total_enabled_threads: str
        """
        self._total_enabled_threads = total_enabled_threads

    @property
    def socket(self):
        r"""Gets the socket of this Processors.

        处理器的插槽号

        :return: The socket of this Processors.
        :rtype: int
        """
        return self._socket

    @socket.setter
    def socket(self, socket):
        r"""Sets the socket of this Processors.

        处理器的插槽号

        :param socket: The socket of this Processors.
        :type socket: int
        """
        self._socket = socket

    @property
    def max_speed_mhz(self):
        r"""Gets the max_speed_mhz of this Processors.

        处理器的最大主频（单位：MHz）

        :return: The max_speed_mhz of this Processors.
        :rtype: int
        """
        return self._max_speed_mhz

    @max_speed_mhz.setter
    def max_speed_mhz(self, max_speed_mhz):
        r"""Sets the max_speed_mhz of this Processors.

        处理器的最大主频（单位：MHz）

        :param max_speed_mhz: The max_speed_mhz of this Processors.
        :type max_speed_mhz: int
        """
        self._max_speed_mhz = max_speed_mhz

    @property
    def temperature(self):
        r"""Gets the temperature of this Processors.

        处理器的温度

        :return: The temperature of this Processors.
        :rtype: int
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        r"""Sets the temperature of this Processors.

        处理器的温度

        :param temperature: The temperature of this Processors.
        :type temperature: int
        """
        self._temperature = temperature

    @property
    def l1_cache_kib(self):
        r"""Gets the l1_cache_kib of this Processors.

        一级缓存（单位：KiB）

        :return: The l1_cache_kib of this Processors.
        :rtype: int
        """
        return self._l1_cache_kib

    @l1_cache_kib.setter
    def l1_cache_kib(self, l1_cache_kib):
        r"""Sets the l1_cache_kib of this Processors.

        一级缓存（单位：KiB）

        :param l1_cache_kib: The l1_cache_kib of this Processors.
        :type l1_cache_kib: int
        """
        self._l1_cache_kib = l1_cache_kib

    @property
    def l2_cache_kib(self):
        r"""Gets the l2_cache_kib of this Processors.

        二级缓存（单位：KiB）

        :return: The l2_cache_kib of this Processors.
        :rtype: int
        """
        return self._l2_cache_kib

    @l2_cache_kib.setter
    def l2_cache_kib(self, l2_cache_kib):
        r"""Sets the l2_cache_kib of this Processors.

        二级缓存（单位：KiB）

        :param l2_cache_kib: The l2_cache_kib of this Processors.
        :type l2_cache_kib: int
        """
        self._l2_cache_kib = l2_cache_kib

    @property
    def l3_cache_kib(self):
        r"""Gets the l3_cache_kib of this Processors.

        三级缓存（单位：KiB）

        :return: The l3_cache_kib of this Processors.
        :rtype: int
        """
        return self._l3_cache_kib

    @l3_cache_kib.setter
    def l3_cache_kib(self, l3_cache_kib):
        r"""Sets the l3_cache_kib of this Processors.

        三级缓存（单位：KiB）

        :param l3_cache_kib: The l3_cache_kib of this Processors.
        :type l3_cache_kib: int
        """
        self._l3_cache_kib = l3_cache_kib

    @property
    def frequency_mhz(self):
        r"""Gets the frequency_mhz of this Processors.

        处理器的主频

        :return: The frequency_mhz of this Processors.
        :rtype: int
        """
        return self._frequency_mhz

    @frequency_mhz.setter
    def frequency_mhz(self, frequency_mhz):
        r"""Sets the frequency_mhz of this Processors.

        处理器的主频

        :param frequency_mhz: The frequency_mhz of this Processors.
        :type frequency_mhz: int
        """
        self._frequency_mhz = frequency_mhz

    @property
    def other_parameters(self):
        r"""Gets the other_parameters of this Processors.

        其他参数

        :return: The other_parameters of this Processors.
        :rtype: str
        """
        return self._other_parameters

    @other_parameters.setter
    def other_parameters(self, other_parameters):
        r"""Sets the other_parameters of this Processors.

        其他参数

        :param other_parameters: The other_parameters of this Processors.
        :type other_parameters: str
        """
        self._other_parameters = other_parameters

    @property
    def serial_number(self):
        r"""Gets the serial_number of this Processors.

        序列号

        :return: The serial_number of this Processors.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        r"""Sets the serial_number of this Processors.

        序列号

        :param serial_number: The serial_number of this Processors.
        :type serial_number: str
        """
        self._serial_number = serial_number

    @property
    def health(self):
        r"""Gets the health of this Processors.

        健康状态

        :return: The health of this Processors.
        :rtype: str
        """
        return self._health

    @health.setter
    def health(self, health):
        r"""Sets the health of this Processors.

        健康状态

        :param health: The health of this Processors.
        :type health: str
        """
        self._health = health

    @property
    def state(self):
        r"""Gets the state of this Processors.

        状态

        :return: The state of this Processors.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this Processors.

        状态

        :param state: The state of this Processors.
        :type state: str
        """
        self._state = state

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
        if not isinstance(other, Processors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
