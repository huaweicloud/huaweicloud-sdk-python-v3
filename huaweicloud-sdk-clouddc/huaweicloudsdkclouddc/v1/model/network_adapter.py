# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetworkAdapter:

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
        'card_model': 'str',
        'model': 'str',
        'manufacturer': 'str',
        'card_manufacturer': 'str',
        'position': 'str',
        'slot_number': 'int',
        'pcb_version': 'str',
        'driver_name': 'str',
        'driver_version': 'str',
        'associated_resource': 'str',
        'firmware_version': 'str',
        'health': 'str',
        'network_ports': 'list[NetworkPort]'
    }

    attribute_map = {
        'name': 'name',
        'card_model': 'card_model',
        'model': 'model',
        'manufacturer': 'manufacturer',
        'card_manufacturer': 'card_manufacturer',
        'position': 'position',
        'slot_number': 'slot_number',
        'pcb_version': 'pcb_version',
        'driver_name': 'driver_name',
        'driver_version': 'driver_version',
        'associated_resource': 'associated_resource',
        'firmware_version': 'firmware_version',
        'health': 'health',
        'network_ports': 'network_ports'
    }

    def __init__(self, name=None, card_model=None, model=None, manufacturer=None, card_manufacturer=None, position=None, slot_number=None, pcb_version=None, driver_name=None, driver_version=None, associated_resource=None, firmware_version=None, health=None, network_ports=None):
        r"""NetworkAdapter

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param card_model: 网络适配器的芯片型号
        :type card_model: str
        :param model: 网络适配器的型号
        :type model: str
        :param manufacturer: 网络适配器的制造商
        :type manufacturer: str
        :param card_manufacturer: 网络适配器的芯片制造商
        :type card_manufacturer: str
        :param position: 网络适配器的位置
        :type position: str
        :param slot_number: 网络适配器的卡槽号
        :type slot_number: int
        :param pcb_version: 网络适配器的PCB版本
        :type pcb_version: str
        :param driver_name: 网络适配器的驱动名称
        :type driver_name: str
        :param driver_version: 网络适配器的驱动版本
        :type driver_version: str
        :param associated_resource: 网络适配器的资源归属
        :type associated_resource: str
        :param firmware_version: 网络适配器的固件版本
        :type firmware_version: str
        :param health: 健康状态
        :type health: str
        :param network_ports: 网络端口列表
        :type network_ports: list[:class:`huaweicloudsdkclouddc.v1.NetworkPort`]
        """
        
        

        self._name = None
        self._card_model = None
        self._model = None
        self._manufacturer = None
        self._card_manufacturer = None
        self._position = None
        self._slot_number = None
        self._pcb_version = None
        self._driver_name = None
        self._driver_version = None
        self._associated_resource = None
        self._firmware_version = None
        self._health = None
        self._network_ports = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if card_model is not None:
            self.card_model = card_model
        if model is not None:
            self.model = model
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if card_manufacturer is not None:
            self.card_manufacturer = card_manufacturer
        if position is not None:
            self.position = position
        if slot_number is not None:
            self.slot_number = slot_number
        if pcb_version is not None:
            self.pcb_version = pcb_version
        if driver_name is not None:
            self.driver_name = driver_name
        if driver_version is not None:
            self.driver_version = driver_version
        if associated_resource is not None:
            self.associated_resource = associated_resource
        if firmware_version is not None:
            self.firmware_version = firmware_version
        if health is not None:
            self.health = health
        if network_ports is not None:
            self.network_ports = network_ports

    @property
    def name(self):
        r"""Gets the name of this NetworkAdapter.

        名称

        :return: The name of this NetworkAdapter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this NetworkAdapter.

        名称

        :param name: The name of this NetworkAdapter.
        :type name: str
        """
        self._name = name

    @property
    def card_model(self):
        r"""Gets the card_model of this NetworkAdapter.

        网络适配器的芯片型号

        :return: The card_model of this NetworkAdapter.
        :rtype: str
        """
        return self._card_model

    @card_model.setter
    def card_model(self, card_model):
        r"""Sets the card_model of this NetworkAdapter.

        网络适配器的芯片型号

        :param card_model: The card_model of this NetworkAdapter.
        :type card_model: str
        """
        self._card_model = card_model

    @property
    def model(self):
        r"""Gets the model of this NetworkAdapter.

        网络适配器的型号

        :return: The model of this NetworkAdapter.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        r"""Sets the model of this NetworkAdapter.

        网络适配器的型号

        :param model: The model of this NetworkAdapter.
        :type model: str
        """
        self._model = model

    @property
    def manufacturer(self):
        r"""Gets the manufacturer of this NetworkAdapter.

        网络适配器的制造商

        :return: The manufacturer of this NetworkAdapter.
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        r"""Sets the manufacturer of this NetworkAdapter.

        网络适配器的制造商

        :param manufacturer: The manufacturer of this NetworkAdapter.
        :type manufacturer: str
        """
        self._manufacturer = manufacturer

    @property
    def card_manufacturer(self):
        r"""Gets the card_manufacturer of this NetworkAdapter.

        网络适配器的芯片制造商

        :return: The card_manufacturer of this NetworkAdapter.
        :rtype: str
        """
        return self._card_manufacturer

    @card_manufacturer.setter
    def card_manufacturer(self, card_manufacturer):
        r"""Sets the card_manufacturer of this NetworkAdapter.

        网络适配器的芯片制造商

        :param card_manufacturer: The card_manufacturer of this NetworkAdapter.
        :type card_manufacturer: str
        """
        self._card_manufacturer = card_manufacturer

    @property
    def position(self):
        r"""Gets the position of this NetworkAdapter.

        网络适配器的位置

        :return: The position of this NetworkAdapter.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        r"""Sets the position of this NetworkAdapter.

        网络适配器的位置

        :param position: The position of this NetworkAdapter.
        :type position: str
        """
        self._position = position

    @property
    def slot_number(self):
        r"""Gets the slot_number of this NetworkAdapter.

        网络适配器的卡槽号

        :return: The slot_number of this NetworkAdapter.
        :rtype: int
        """
        return self._slot_number

    @slot_number.setter
    def slot_number(self, slot_number):
        r"""Sets the slot_number of this NetworkAdapter.

        网络适配器的卡槽号

        :param slot_number: The slot_number of this NetworkAdapter.
        :type slot_number: int
        """
        self._slot_number = slot_number

    @property
    def pcb_version(self):
        r"""Gets the pcb_version of this NetworkAdapter.

        网络适配器的PCB版本

        :return: The pcb_version of this NetworkAdapter.
        :rtype: str
        """
        return self._pcb_version

    @pcb_version.setter
    def pcb_version(self, pcb_version):
        r"""Sets the pcb_version of this NetworkAdapter.

        网络适配器的PCB版本

        :param pcb_version: The pcb_version of this NetworkAdapter.
        :type pcb_version: str
        """
        self._pcb_version = pcb_version

    @property
    def driver_name(self):
        r"""Gets the driver_name of this NetworkAdapter.

        网络适配器的驱动名称

        :return: The driver_name of this NetworkAdapter.
        :rtype: str
        """
        return self._driver_name

    @driver_name.setter
    def driver_name(self, driver_name):
        r"""Sets the driver_name of this NetworkAdapter.

        网络适配器的驱动名称

        :param driver_name: The driver_name of this NetworkAdapter.
        :type driver_name: str
        """
        self._driver_name = driver_name

    @property
    def driver_version(self):
        r"""Gets the driver_version of this NetworkAdapter.

        网络适配器的驱动版本

        :return: The driver_version of this NetworkAdapter.
        :rtype: str
        """
        return self._driver_version

    @driver_version.setter
    def driver_version(self, driver_version):
        r"""Sets the driver_version of this NetworkAdapter.

        网络适配器的驱动版本

        :param driver_version: The driver_version of this NetworkAdapter.
        :type driver_version: str
        """
        self._driver_version = driver_version

    @property
    def associated_resource(self):
        r"""Gets the associated_resource of this NetworkAdapter.

        网络适配器的资源归属

        :return: The associated_resource of this NetworkAdapter.
        :rtype: str
        """
        return self._associated_resource

    @associated_resource.setter
    def associated_resource(self, associated_resource):
        r"""Sets the associated_resource of this NetworkAdapter.

        网络适配器的资源归属

        :param associated_resource: The associated_resource of this NetworkAdapter.
        :type associated_resource: str
        """
        self._associated_resource = associated_resource

    @property
    def firmware_version(self):
        r"""Gets the firmware_version of this NetworkAdapter.

        网络适配器的固件版本

        :return: The firmware_version of this NetworkAdapter.
        :rtype: str
        """
        return self._firmware_version

    @firmware_version.setter
    def firmware_version(self, firmware_version):
        r"""Sets the firmware_version of this NetworkAdapter.

        网络适配器的固件版本

        :param firmware_version: The firmware_version of this NetworkAdapter.
        :type firmware_version: str
        """
        self._firmware_version = firmware_version

    @property
    def health(self):
        r"""Gets the health of this NetworkAdapter.

        健康状态

        :return: The health of this NetworkAdapter.
        :rtype: str
        """
        return self._health

    @health.setter
    def health(self, health):
        r"""Sets the health of this NetworkAdapter.

        健康状态

        :param health: The health of this NetworkAdapter.
        :type health: str
        """
        self._health = health

    @property
    def network_ports(self):
        r"""Gets the network_ports of this NetworkAdapter.

        网络端口列表

        :return: The network_ports of this NetworkAdapter.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.NetworkPort`]
        """
        return self._network_ports

    @network_ports.setter
    def network_ports(self, network_ports):
        r"""Sets the network_ports of this NetworkAdapter.

        网络端口列表

        :param network_ports: The network_ports of this NetworkAdapter.
        :type network_ports: list[:class:`huaweicloudsdkclouddc.v1.NetworkPort`]
        """
        self._network_ports = network_ports

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
        if not isinstance(other, NetworkAdapter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
