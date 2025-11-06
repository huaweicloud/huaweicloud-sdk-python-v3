# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetworkDeviceSpec:

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
        'power': 'int',
        'unit': 'int',
        'performance_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'power': 'power',
        'unit': 'unit',
        'performance_type': 'performance_type'
    }

    def __init__(self, id=None, name=None, power=None, unit=None, performance_type=None):
        r"""NetworkDeviceSpec

        The model defined in huaweicloud sdk

        :param id: 网络设备规格ID
        :type id: str
        :param name: 网络设备规格名称。
        :type name: str
        :param power: 设备功率。单位：w
        :type power: int
        :param unit: 设备高度。U位数。
        :type unit: int
        :param performance_type: 用途
        :type performance_type: str
        """
        
        

        self._id = None
        self._name = None
        self._power = None
        self._unit = None
        self._performance_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if power is not None:
            self.power = power
        if unit is not None:
            self.unit = unit
        if performance_type is not None:
            self.performance_type = performance_type

    @property
    def id(self):
        r"""Gets the id of this NetworkDeviceSpec.

        网络设备规格ID

        :return: The id of this NetworkDeviceSpec.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this NetworkDeviceSpec.

        网络设备规格ID

        :param id: The id of this NetworkDeviceSpec.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this NetworkDeviceSpec.

        网络设备规格名称。

        :return: The name of this NetworkDeviceSpec.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this NetworkDeviceSpec.

        网络设备规格名称。

        :param name: The name of this NetworkDeviceSpec.
        :type name: str
        """
        self._name = name

    @property
    def power(self):
        r"""Gets the power of this NetworkDeviceSpec.

        设备功率。单位：w

        :return: The power of this NetworkDeviceSpec.
        :rtype: int
        """
        return self._power

    @power.setter
    def power(self, power):
        r"""Sets the power of this NetworkDeviceSpec.

        设备功率。单位：w

        :param power: The power of this NetworkDeviceSpec.
        :type power: int
        """
        self._power = power

    @property
    def unit(self):
        r"""Gets the unit of this NetworkDeviceSpec.

        设备高度。U位数。

        :return: The unit of this NetworkDeviceSpec.
        :rtype: int
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this NetworkDeviceSpec.

        设备高度。U位数。

        :param unit: The unit of this NetworkDeviceSpec.
        :type unit: int
        """
        self._unit = unit

    @property
    def performance_type(self):
        r"""Gets the performance_type of this NetworkDeviceSpec.

        用途

        :return: The performance_type of this NetworkDeviceSpec.
        :rtype: str
        """
        return self._performance_type

    @performance_type.setter
    def performance_type(self, performance_type):
        r"""Sets the performance_type of this NetworkDeviceSpec.

        用途

        :param performance_type: The performance_type of this NetworkDeviceSpec.
        :type performance_type: str
        """
        self._performance_type = performance_type

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
        if not isinstance(other, NetworkDeviceSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
