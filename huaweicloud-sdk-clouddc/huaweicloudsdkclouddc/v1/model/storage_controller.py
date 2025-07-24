# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StorageController:

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
        'model': 'str',
        'manufacturer': 'str',
        'state': 'str',
        'health': 'str',
        'type': 'str',
        'firmware_version': 'str',
        'supported_raid_levels': 'list[str]',
        'mode': 'str',
        'configuration_version': 'str',
        'sas_address': 'str',
        'capacitance_name': 'str',
        'capacitance_state': 'str',
        'capacitance_health': 'str',
        'min_stripe_size_bytes': 'int',
        'max_stripe_size_bytes': 'int',
        'volumes': 'list[Volume]',
        'drives': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'model': 'model',
        'manufacturer': 'manufacturer',
        'state': 'state',
        'health': 'health',
        'type': 'type',
        'firmware_version': 'firmware_version',
        'supported_raid_levels': 'supported_raid_levels',
        'mode': 'mode',
        'configuration_version': 'configuration_version',
        'sas_address': 'sas_address',
        'capacitance_name': 'capacitance_name',
        'capacitance_state': 'capacitance_state',
        'capacitance_health': 'capacitance_health',
        'min_stripe_size_bytes': 'min_stripe_size_bytes',
        'max_stripe_size_bytes': 'max_stripe_size_bytes',
        'volumes': 'volumes',
        'drives': 'drives'
    }

    def __init__(self, name=None, model=None, manufacturer=None, state=None, health=None, type=None, firmware_version=None, supported_raid_levels=None, mode=None, configuration_version=None, sas_address=None, capacitance_name=None, capacitance_state=None, capacitance_health=None, min_stripe_size_bytes=None, max_stripe_size_bytes=None, volumes=None, drives=None):
        r"""StorageController

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param model: 型号
        :type model: str
        :param manufacturer: 制造商
        :type manufacturer: str
        :param state: 状态
        :type state: str
        :param health: 健康情况
        :type health: str
        :param type: 存储控制器的类型
        :type type: str
        :param firmware_version: 固件版本
        :type firmware_version: str
        :param supported_raid_levels: 支持的raid级别列表
        :type supported_raid_levels: list[str]
        :param mode: 存储控制器的模式
        :type mode: str
        :param configuration_version: 储控制器配置版本
        :type configuration_version: str
        :param sas_address: SAS地址
        :type sas_address: str
        :param capacitance_name: 存储控制器BBU名称
        :type capacitance_name: str
        :param capacitance_state: 存储控制器电容(BBU)使能状态
        :type capacitance_state: str
        :param capacitance_health: 存储控制器电容(BBU)健康状态
        :type capacitance_health: str
        :param min_stripe_size_bytes: 控制器支持最小条带值
        :type min_stripe_size_bytes: int
        :param max_stripe_size_bytes: 控制器支持最大条带值
        :type max_stripe_size_bytes: int
        :param volumes: 逻辑盘列表
        :type volumes: list[:class:`huaweicloudsdkclouddc.v1.Volume`]
        :param drives: 管理的驱动器列表信息
        :type drives: list[str]
        """
        
        

        self._name = None
        self._model = None
        self._manufacturer = None
        self._state = None
        self._health = None
        self._type = None
        self._firmware_version = None
        self._supported_raid_levels = None
        self._mode = None
        self._configuration_version = None
        self._sas_address = None
        self._capacitance_name = None
        self._capacitance_state = None
        self._capacitance_health = None
        self._min_stripe_size_bytes = None
        self._max_stripe_size_bytes = None
        self._volumes = None
        self._drives = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if model is not None:
            self.model = model
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if state is not None:
            self.state = state
        if health is not None:
            self.health = health
        if type is not None:
            self.type = type
        if firmware_version is not None:
            self.firmware_version = firmware_version
        if supported_raid_levels is not None:
            self.supported_raid_levels = supported_raid_levels
        if mode is not None:
            self.mode = mode
        if configuration_version is not None:
            self.configuration_version = configuration_version
        if sas_address is not None:
            self.sas_address = sas_address
        if capacitance_name is not None:
            self.capacitance_name = capacitance_name
        if capacitance_state is not None:
            self.capacitance_state = capacitance_state
        if capacitance_health is not None:
            self.capacitance_health = capacitance_health
        if min_stripe_size_bytes is not None:
            self.min_stripe_size_bytes = min_stripe_size_bytes
        if max_stripe_size_bytes is not None:
            self.max_stripe_size_bytes = max_stripe_size_bytes
        if volumes is not None:
            self.volumes = volumes
        if drives is not None:
            self.drives = drives

    @property
    def name(self):
        r"""Gets the name of this StorageController.

        名称

        :return: The name of this StorageController.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this StorageController.

        名称

        :param name: The name of this StorageController.
        :type name: str
        """
        self._name = name

    @property
    def model(self):
        r"""Gets the model of this StorageController.

        型号

        :return: The model of this StorageController.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        r"""Sets the model of this StorageController.

        型号

        :param model: The model of this StorageController.
        :type model: str
        """
        self._model = model

    @property
    def manufacturer(self):
        r"""Gets the manufacturer of this StorageController.

        制造商

        :return: The manufacturer of this StorageController.
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        r"""Sets the manufacturer of this StorageController.

        制造商

        :param manufacturer: The manufacturer of this StorageController.
        :type manufacturer: str
        """
        self._manufacturer = manufacturer

    @property
    def state(self):
        r"""Gets the state of this StorageController.

        状态

        :return: The state of this StorageController.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this StorageController.

        状态

        :param state: The state of this StorageController.
        :type state: str
        """
        self._state = state

    @property
    def health(self):
        r"""Gets the health of this StorageController.

        健康情况

        :return: The health of this StorageController.
        :rtype: str
        """
        return self._health

    @health.setter
    def health(self, health):
        r"""Sets the health of this StorageController.

        健康情况

        :param health: The health of this StorageController.
        :type health: str
        """
        self._health = health

    @property
    def type(self):
        r"""Gets the type of this StorageController.

        存储控制器的类型

        :return: The type of this StorageController.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this StorageController.

        存储控制器的类型

        :param type: The type of this StorageController.
        :type type: str
        """
        self._type = type

    @property
    def firmware_version(self):
        r"""Gets the firmware_version of this StorageController.

        固件版本

        :return: The firmware_version of this StorageController.
        :rtype: str
        """
        return self._firmware_version

    @firmware_version.setter
    def firmware_version(self, firmware_version):
        r"""Sets the firmware_version of this StorageController.

        固件版本

        :param firmware_version: The firmware_version of this StorageController.
        :type firmware_version: str
        """
        self._firmware_version = firmware_version

    @property
    def supported_raid_levels(self):
        r"""Gets the supported_raid_levels of this StorageController.

        支持的raid级别列表

        :return: The supported_raid_levels of this StorageController.
        :rtype: list[str]
        """
        return self._supported_raid_levels

    @supported_raid_levels.setter
    def supported_raid_levels(self, supported_raid_levels):
        r"""Sets the supported_raid_levels of this StorageController.

        支持的raid级别列表

        :param supported_raid_levels: The supported_raid_levels of this StorageController.
        :type supported_raid_levels: list[str]
        """
        self._supported_raid_levels = supported_raid_levels

    @property
    def mode(self):
        r"""Gets the mode of this StorageController.

        存储控制器的模式

        :return: The mode of this StorageController.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this StorageController.

        存储控制器的模式

        :param mode: The mode of this StorageController.
        :type mode: str
        """
        self._mode = mode

    @property
    def configuration_version(self):
        r"""Gets the configuration_version of this StorageController.

        储控制器配置版本

        :return: The configuration_version of this StorageController.
        :rtype: str
        """
        return self._configuration_version

    @configuration_version.setter
    def configuration_version(self, configuration_version):
        r"""Sets the configuration_version of this StorageController.

        储控制器配置版本

        :param configuration_version: The configuration_version of this StorageController.
        :type configuration_version: str
        """
        self._configuration_version = configuration_version

    @property
    def sas_address(self):
        r"""Gets the sas_address of this StorageController.

        SAS地址

        :return: The sas_address of this StorageController.
        :rtype: str
        """
        return self._sas_address

    @sas_address.setter
    def sas_address(self, sas_address):
        r"""Sets the sas_address of this StorageController.

        SAS地址

        :param sas_address: The sas_address of this StorageController.
        :type sas_address: str
        """
        self._sas_address = sas_address

    @property
    def capacitance_name(self):
        r"""Gets the capacitance_name of this StorageController.

        存储控制器BBU名称

        :return: The capacitance_name of this StorageController.
        :rtype: str
        """
        return self._capacitance_name

    @capacitance_name.setter
    def capacitance_name(self, capacitance_name):
        r"""Sets the capacitance_name of this StorageController.

        存储控制器BBU名称

        :param capacitance_name: The capacitance_name of this StorageController.
        :type capacitance_name: str
        """
        self._capacitance_name = capacitance_name

    @property
    def capacitance_state(self):
        r"""Gets the capacitance_state of this StorageController.

        存储控制器电容(BBU)使能状态

        :return: The capacitance_state of this StorageController.
        :rtype: str
        """
        return self._capacitance_state

    @capacitance_state.setter
    def capacitance_state(self, capacitance_state):
        r"""Sets the capacitance_state of this StorageController.

        存储控制器电容(BBU)使能状态

        :param capacitance_state: The capacitance_state of this StorageController.
        :type capacitance_state: str
        """
        self._capacitance_state = capacitance_state

    @property
    def capacitance_health(self):
        r"""Gets the capacitance_health of this StorageController.

        存储控制器电容(BBU)健康状态

        :return: The capacitance_health of this StorageController.
        :rtype: str
        """
        return self._capacitance_health

    @capacitance_health.setter
    def capacitance_health(self, capacitance_health):
        r"""Sets the capacitance_health of this StorageController.

        存储控制器电容(BBU)健康状态

        :param capacitance_health: The capacitance_health of this StorageController.
        :type capacitance_health: str
        """
        self._capacitance_health = capacitance_health

    @property
    def min_stripe_size_bytes(self):
        r"""Gets the min_stripe_size_bytes of this StorageController.

        控制器支持最小条带值

        :return: The min_stripe_size_bytes of this StorageController.
        :rtype: int
        """
        return self._min_stripe_size_bytes

    @min_stripe_size_bytes.setter
    def min_stripe_size_bytes(self, min_stripe_size_bytes):
        r"""Sets the min_stripe_size_bytes of this StorageController.

        控制器支持最小条带值

        :param min_stripe_size_bytes: The min_stripe_size_bytes of this StorageController.
        :type min_stripe_size_bytes: int
        """
        self._min_stripe_size_bytes = min_stripe_size_bytes

    @property
    def max_stripe_size_bytes(self):
        r"""Gets the max_stripe_size_bytes of this StorageController.

        控制器支持最大条带值

        :return: The max_stripe_size_bytes of this StorageController.
        :rtype: int
        """
        return self._max_stripe_size_bytes

    @max_stripe_size_bytes.setter
    def max_stripe_size_bytes(self, max_stripe_size_bytes):
        r"""Sets the max_stripe_size_bytes of this StorageController.

        控制器支持最大条带值

        :param max_stripe_size_bytes: The max_stripe_size_bytes of this StorageController.
        :type max_stripe_size_bytes: int
        """
        self._max_stripe_size_bytes = max_stripe_size_bytes

    @property
    def volumes(self):
        r"""Gets the volumes of this StorageController.

        逻辑盘列表

        :return: The volumes of this StorageController.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.Volume`]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        r"""Sets the volumes of this StorageController.

        逻辑盘列表

        :param volumes: The volumes of this StorageController.
        :type volumes: list[:class:`huaweicloudsdkclouddc.v1.Volume`]
        """
        self._volumes = volumes

    @property
    def drives(self):
        r"""Gets the drives of this StorageController.

        管理的驱动器列表信息

        :return: The drives of this StorageController.
        :rtype: list[str]
        """
        return self._drives

    @drives.setter
    def drives(self, drives):
        r"""Sets the drives of this StorageController.

        管理的驱动器列表信息

        :param drives: The drives of this StorageController.
        :type drives: list[str]
        """
        self._drives = drives

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
        if not isinstance(other, StorageController):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
