# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StorageTypeOption:

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
        'zone_code': 'str',
        'expand_capacity_step': 'int',
        'supported_capacities': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'zone_code': 'zone_code',
        'expand_capacity_step': 'expand_capacity_step',
        'supported_capacities': 'supported_capacities'
    }

    def __init__(self, id=None, name=None, zone_code=None, expand_capacity_step=None, supported_capacities=None):
        r"""StorageTypeOption

        The model defined in huaweicloud sdk

        :param id: 存储类型id，uuid
        :type id: str
        :param name: 售卖存储类型
        :type name: str
        :param zone_code: 地区编码，表示允许在这个国家购买部署
        :type zone_code: str
        :param expand_capacity_step: 步长，为0时仅可购买gears中的容量
        :type expand_capacity_step: int
        :param supported_capacities: 固定购买容量，为空时直接按步长购买
        :type supported_capacities: list[int]
        """
        
        

        self._id = None
        self._name = None
        self._zone_code = None
        self._expand_capacity_step = None
        self._supported_capacities = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if zone_code is not None:
            self.zone_code = zone_code
        if expand_capacity_step is not None:
            self.expand_capacity_step = expand_capacity_step
        if supported_capacities is not None:
            self.supported_capacities = supported_capacities

    @property
    def id(self):
        r"""Gets the id of this StorageTypeOption.

        存储类型id，uuid

        :return: The id of this StorageTypeOption.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this StorageTypeOption.

        存储类型id，uuid

        :param id: The id of this StorageTypeOption.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this StorageTypeOption.

        售卖存储类型

        :return: The name of this StorageTypeOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this StorageTypeOption.

        售卖存储类型

        :param name: The name of this StorageTypeOption.
        :type name: str
        """
        self._name = name

    @property
    def zone_code(self):
        r"""Gets the zone_code of this StorageTypeOption.

        地区编码，表示允许在这个国家购买部署

        :return: The zone_code of this StorageTypeOption.
        :rtype: str
        """
        return self._zone_code

    @zone_code.setter
    def zone_code(self, zone_code):
        r"""Sets the zone_code of this StorageTypeOption.

        地区编码，表示允许在这个国家购买部署

        :param zone_code: The zone_code of this StorageTypeOption.
        :type zone_code: str
        """
        self._zone_code = zone_code

    @property
    def expand_capacity_step(self):
        r"""Gets the expand_capacity_step of this StorageTypeOption.

        步长，为0时仅可购买gears中的容量

        :return: The expand_capacity_step of this StorageTypeOption.
        :rtype: int
        """
        return self._expand_capacity_step

    @expand_capacity_step.setter
    def expand_capacity_step(self, expand_capacity_step):
        r"""Sets the expand_capacity_step of this StorageTypeOption.

        步长，为0时仅可购买gears中的容量

        :param expand_capacity_step: The expand_capacity_step of this StorageTypeOption.
        :type expand_capacity_step: int
        """
        self._expand_capacity_step = expand_capacity_step

    @property
    def supported_capacities(self):
        r"""Gets the supported_capacities of this StorageTypeOption.

        固定购买容量，为空时直接按步长购买

        :return: The supported_capacities of this StorageTypeOption.
        :rtype: list[int]
        """
        return self._supported_capacities

    @supported_capacities.setter
    def supported_capacities(self, supported_capacities):
        r"""Sets the supported_capacities of this StorageTypeOption.

        固定购买容量，为空时直接按步长购买

        :param supported_capacities: The supported_capacities of this StorageTypeOption.
        :type supported_capacities: list[int]
        """
        self._supported_capacities = supported_capacities

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
        if not isinstance(other, StorageTypeOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
