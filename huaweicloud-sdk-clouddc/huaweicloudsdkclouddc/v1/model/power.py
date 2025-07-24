# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Power:

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
        'slot_number': 'int',
        'model': 'str',
        'manufacturer': 'str',
        'power_supply_type': 'str',
        'power_capacity_watts': 'str',
        'line_input_voltage': 'int',
        'output_voltage': 'int',
        'protocol': 'str',
        'active_standby': 'str',
        'part_number': 'str',
        'serial_number': 'str',
        'firmware_version': 'str',
        'status': 'Status'
    }

    attribute_map = {
        'name': 'name',
        'slot_number': 'slot_number',
        'model': 'model',
        'manufacturer': 'manufacturer',
        'power_supply_type': 'power_supply_type',
        'power_capacity_watts': 'power_capacity_watts',
        'line_input_voltage': 'line_input_voltage',
        'output_voltage': 'output_voltage',
        'protocol': 'protocol',
        'active_standby': 'active_standby',
        'part_number': 'part_number',
        'serial_number': 'serial_number',
        'firmware_version': 'firmware_version',
        'status': 'status'
    }

    def __init__(self, name=None, slot_number=None, model=None, manufacturer=None, power_supply_type=None, power_capacity_watts=None, line_input_voltage=None, output_voltage=None, protocol=None, active_standby=None, part_number=None, serial_number=None, firmware_version=None, status=None):
        r"""Power

        The model defined in huaweicloud sdk

        :param name: 电源名称
        :type name: str
        :param slot_number: 槽位
        :type slot_number: int
        :param model: 型号
        :type model: str
        :param manufacturer: 厂商
        :type manufacturer: str
        :param power_supply_type: 输入模式
        :type power_supply_type: str
        :param power_capacity_watts: 额定功率
        :type power_capacity_watts: str
        :param line_input_voltage: 输入电压
        :type line_input_voltage: int
        :param output_voltage: 输出电压
        :type output_voltage: int
        :param protocol: 协议
        :type protocol: str
        :param active_standby: 主备模式
        :type active_standby: str
        :param part_number: 部件编号
        :type part_number: str
        :param serial_number: 序列号
        :type serial_number: str
        :param firmware_version: 固件版本
        :type firmware_version: str
        :param status: 
        :type status: :class:`huaweicloudsdkclouddc.v1.Status`
        """
        
        

        self._name = None
        self._slot_number = None
        self._model = None
        self._manufacturer = None
        self._power_supply_type = None
        self._power_capacity_watts = None
        self._line_input_voltage = None
        self._output_voltage = None
        self._protocol = None
        self._active_standby = None
        self._part_number = None
        self._serial_number = None
        self._firmware_version = None
        self._status = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if slot_number is not None:
            self.slot_number = slot_number
        if model is not None:
            self.model = model
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if power_supply_type is not None:
            self.power_supply_type = power_supply_type
        if power_capacity_watts is not None:
            self.power_capacity_watts = power_capacity_watts
        if line_input_voltage is not None:
            self.line_input_voltage = line_input_voltage
        if output_voltage is not None:
            self.output_voltage = output_voltage
        if protocol is not None:
            self.protocol = protocol
        if active_standby is not None:
            self.active_standby = active_standby
        if part_number is not None:
            self.part_number = part_number
        if serial_number is not None:
            self.serial_number = serial_number
        if firmware_version is not None:
            self.firmware_version = firmware_version
        if status is not None:
            self.status = status

    @property
    def name(self):
        r"""Gets the name of this Power.

        电源名称

        :return: The name of this Power.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Power.

        电源名称

        :param name: The name of this Power.
        :type name: str
        """
        self._name = name

    @property
    def slot_number(self):
        r"""Gets the slot_number of this Power.

        槽位

        :return: The slot_number of this Power.
        :rtype: int
        """
        return self._slot_number

    @slot_number.setter
    def slot_number(self, slot_number):
        r"""Sets the slot_number of this Power.

        槽位

        :param slot_number: The slot_number of this Power.
        :type slot_number: int
        """
        self._slot_number = slot_number

    @property
    def model(self):
        r"""Gets the model of this Power.

        型号

        :return: The model of this Power.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        r"""Sets the model of this Power.

        型号

        :param model: The model of this Power.
        :type model: str
        """
        self._model = model

    @property
    def manufacturer(self):
        r"""Gets the manufacturer of this Power.

        厂商

        :return: The manufacturer of this Power.
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        r"""Sets the manufacturer of this Power.

        厂商

        :param manufacturer: The manufacturer of this Power.
        :type manufacturer: str
        """
        self._manufacturer = manufacturer

    @property
    def power_supply_type(self):
        r"""Gets the power_supply_type of this Power.

        输入模式

        :return: The power_supply_type of this Power.
        :rtype: str
        """
        return self._power_supply_type

    @power_supply_type.setter
    def power_supply_type(self, power_supply_type):
        r"""Sets the power_supply_type of this Power.

        输入模式

        :param power_supply_type: The power_supply_type of this Power.
        :type power_supply_type: str
        """
        self._power_supply_type = power_supply_type

    @property
    def power_capacity_watts(self):
        r"""Gets the power_capacity_watts of this Power.

        额定功率

        :return: The power_capacity_watts of this Power.
        :rtype: str
        """
        return self._power_capacity_watts

    @power_capacity_watts.setter
    def power_capacity_watts(self, power_capacity_watts):
        r"""Sets the power_capacity_watts of this Power.

        额定功率

        :param power_capacity_watts: The power_capacity_watts of this Power.
        :type power_capacity_watts: str
        """
        self._power_capacity_watts = power_capacity_watts

    @property
    def line_input_voltage(self):
        r"""Gets the line_input_voltage of this Power.

        输入电压

        :return: The line_input_voltage of this Power.
        :rtype: int
        """
        return self._line_input_voltage

    @line_input_voltage.setter
    def line_input_voltage(self, line_input_voltage):
        r"""Sets the line_input_voltage of this Power.

        输入电压

        :param line_input_voltage: The line_input_voltage of this Power.
        :type line_input_voltage: int
        """
        self._line_input_voltage = line_input_voltage

    @property
    def output_voltage(self):
        r"""Gets the output_voltage of this Power.

        输出电压

        :return: The output_voltage of this Power.
        :rtype: int
        """
        return self._output_voltage

    @output_voltage.setter
    def output_voltage(self, output_voltage):
        r"""Sets the output_voltage of this Power.

        输出电压

        :param output_voltage: The output_voltage of this Power.
        :type output_voltage: int
        """
        self._output_voltage = output_voltage

    @property
    def protocol(self):
        r"""Gets the protocol of this Power.

        协议

        :return: The protocol of this Power.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this Power.

        协议

        :param protocol: The protocol of this Power.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def active_standby(self):
        r"""Gets the active_standby of this Power.

        主备模式

        :return: The active_standby of this Power.
        :rtype: str
        """
        return self._active_standby

    @active_standby.setter
    def active_standby(self, active_standby):
        r"""Sets the active_standby of this Power.

        主备模式

        :param active_standby: The active_standby of this Power.
        :type active_standby: str
        """
        self._active_standby = active_standby

    @property
    def part_number(self):
        r"""Gets the part_number of this Power.

        部件编号

        :return: The part_number of this Power.
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        r"""Sets the part_number of this Power.

        部件编号

        :param part_number: The part_number of this Power.
        :type part_number: str
        """
        self._part_number = part_number

    @property
    def serial_number(self):
        r"""Gets the serial_number of this Power.

        序列号

        :return: The serial_number of this Power.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        r"""Sets the serial_number of this Power.

        序列号

        :param serial_number: The serial_number of this Power.
        :type serial_number: str
        """
        self._serial_number = serial_number

    @property
    def firmware_version(self):
        r"""Gets the firmware_version of this Power.

        固件版本

        :return: The firmware_version of this Power.
        :rtype: str
        """
        return self._firmware_version

    @firmware_version.setter
    def firmware_version(self, firmware_version):
        r"""Sets the firmware_version of this Power.

        固件版本

        :param firmware_version: The firmware_version of this Power.
        :type firmware_version: str
        """
        self._firmware_version = firmware_version

    @property
    def status(self):
        r"""Gets the status of this Power.

        :return: The status of this Power.
        :rtype: :class:`huaweicloudsdkclouddc.v1.Status`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Power.

        :param status: The status of this Power.
        :type status: :class:`huaweicloudsdkclouddc.v1.Status`
        """
        self._status = status

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
        if not isinstance(other, Power):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
