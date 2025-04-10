# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFirmwaresResponseData:

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
        'description': 'str',
        'version': 'str',
        'version_type': 'str',
        'expire_time': 'str',
        'firmware_whitelist': 'list[str]',
        'type': 'str',
        'series': 'str',
        'device_type': 'str',
        'arch': 'str',
        'os_name': 'str',
        'os_type': 'str',
        'os_version': 'str',
        'size': 'int',
        'create_time': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'version': 'version',
        'version_type': 'version_type',
        'expire_time': 'expire_time',
        'firmware_whitelist': 'firmware_whitelist',
        'type': 'type',
        'series': 'series',
        'device_type': 'device_type',
        'arch': 'arch',
        'os_name': 'os_name',
        'os_type': 'os_type',
        'os_version': 'os_version',
        'size': 'size',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, description=None, version=None, version_type=None, expire_time=None, firmware_whitelist=None, type=None, series=None, device_type=None, arch=None, os_name=None, os_type=None, os_version=None, size=None, create_time=None, update_time=None):
        r"""ListFirmwaresResponseData

        The model defined in huaweicloud sdk

        :param id: 固件id
        :type id: str
        :param name: 固件名称
        :type name: str
        :param description: 固件描述
        :type description: str
        :param version: 固件版本
        :type version: str
        :param version_type: 固件版本类型
        :type version_type: str
        :param expire_time: 固件到期时间
        :type expire_time: str
        :param firmware_whitelist: 固件白名单
        :type firmware_whitelist: list[str]
        :param type: 固件类型
        :type type: str
        :param series: 产品系列
        :type series: str
        :param device_type: 固件适用设备类型
        :type device_type: str
        :param arch: 边缘节点架构
        :type arch: str
        :param os_name: 边缘设备操作系统名称
        :type os_name: str
        :param os_type: 边缘节点操作系统类型
        :type os_type: str
        :param os_version: 边缘设备操作系统版本
        :type os_version: str
        :param size: 当前固件大小(单位:byte)
        :type size: int
        :param create_time: 创建时间毫秒数
        :type create_time: int
        :param update_time: 更新时间毫秒数
        :type update_time: int
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._version = None
        self._version_type = None
        self._expire_time = None
        self._firmware_whitelist = None
        self._type = None
        self._series = None
        self._device_type = None
        self._arch = None
        self._os_name = None
        self._os_type = None
        self._os_version = None
        self._size = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.version = version
        self.version_type = version_type
        self.expire_time = expire_time
        self.firmware_whitelist = firmware_whitelist
        self.type = type
        self.series = series
        self.device_type = device_type
        self.arch = arch
        self.os_name = os_name
        self.os_type = os_type
        self.os_version = os_version
        self.size = size
        self.create_time = create_time
        self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this ListFirmwaresResponseData.

        固件id

        :return: The id of this ListFirmwaresResponseData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListFirmwaresResponseData.

        固件id

        :param id: The id of this ListFirmwaresResponseData.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListFirmwaresResponseData.

        固件名称

        :return: The name of this ListFirmwaresResponseData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListFirmwaresResponseData.

        固件名称

        :param name: The name of this ListFirmwaresResponseData.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ListFirmwaresResponseData.

        固件描述

        :return: The description of this ListFirmwaresResponseData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListFirmwaresResponseData.

        固件描述

        :param description: The description of this ListFirmwaresResponseData.
        :type description: str
        """
        self._description = description

    @property
    def version(self):
        r"""Gets the version of this ListFirmwaresResponseData.

        固件版本

        :return: The version of this ListFirmwaresResponseData.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ListFirmwaresResponseData.

        固件版本

        :param version: The version of this ListFirmwaresResponseData.
        :type version: str
        """
        self._version = version

    @property
    def version_type(self):
        r"""Gets the version_type of this ListFirmwaresResponseData.

        固件版本类型

        :return: The version_type of this ListFirmwaresResponseData.
        :rtype: str
        """
        return self._version_type

    @version_type.setter
    def version_type(self, version_type):
        r"""Sets the version_type of this ListFirmwaresResponseData.

        固件版本类型

        :param version_type: The version_type of this ListFirmwaresResponseData.
        :type version_type: str
        """
        self._version_type = version_type

    @property
    def expire_time(self):
        r"""Gets the expire_time of this ListFirmwaresResponseData.

        固件到期时间

        :return: The expire_time of this ListFirmwaresResponseData.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this ListFirmwaresResponseData.

        固件到期时间

        :param expire_time: The expire_time of this ListFirmwaresResponseData.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def firmware_whitelist(self):
        r"""Gets the firmware_whitelist of this ListFirmwaresResponseData.

        固件白名单

        :return: The firmware_whitelist of this ListFirmwaresResponseData.
        :rtype: list[str]
        """
        return self._firmware_whitelist

    @firmware_whitelist.setter
    def firmware_whitelist(self, firmware_whitelist):
        r"""Sets the firmware_whitelist of this ListFirmwaresResponseData.

        固件白名单

        :param firmware_whitelist: The firmware_whitelist of this ListFirmwaresResponseData.
        :type firmware_whitelist: list[str]
        """
        self._firmware_whitelist = firmware_whitelist

    @property
    def type(self):
        r"""Gets the type of this ListFirmwaresResponseData.

        固件类型

        :return: The type of this ListFirmwaresResponseData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListFirmwaresResponseData.

        固件类型

        :param type: The type of this ListFirmwaresResponseData.
        :type type: str
        """
        self._type = type

    @property
    def series(self):
        r"""Gets the series of this ListFirmwaresResponseData.

        产品系列

        :return: The series of this ListFirmwaresResponseData.
        :rtype: str
        """
        return self._series

    @series.setter
    def series(self, series):
        r"""Sets the series of this ListFirmwaresResponseData.

        产品系列

        :param series: The series of this ListFirmwaresResponseData.
        :type series: str
        """
        self._series = series

    @property
    def device_type(self):
        r"""Gets the device_type of this ListFirmwaresResponseData.

        固件适用设备类型

        :return: The device_type of this ListFirmwaresResponseData.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        r"""Sets the device_type of this ListFirmwaresResponseData.

        固件适用设备类型

        :param device_type: The device_type of this ListFirmwaresResponseData.
        :type device_type: str
        """
        self._device_type = device_type

    @property
    def arch(self):
        r"""Gets the arch of this ListFirmwaresResponseData.

        边缘节点架构

        :return: The arch of this ListFirmwaresResponseData.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this ListFirmwaresResponseData.

        边缘节点架构

        :param arch: The arch of this ListFirmwaresResponseData.
        :type arch: str
        """
        self._arch = arch

    @property
    def os_name(self):
        r"""Gets the os_name of this ListFirmwaresResponseData.

        边缘设备操作系统名称

        :return: The os_name of this ListFirmwaresResponseData.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        r"""Sets the os_name of this ListFirmwaresResponseData.

        边缘设备操作系统名称

        :param os_name: The os_name of this ListFirmwaresResponseData.
        :type os_name: str
        """
        self._os_name = os_name

    @property
    def os_type(self):
        r"""Gets the os_type of this ListFirmwaresResponseData.

        边缘节点操作系统类型

        :return: The os_type of this ListFirmwaresResponseData.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ListFirmwaresResponseData.

        边缘节点操作系统类型

        :param os_type: The os_type of this ListFirmwaresResponseData.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def os_version(self):
        r"""Gets the os_version of this ListFirmwaresResponseData.

        边缘设备操作系统版本

        :return: The os_version of this ListFirmwaresResponseData.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        r"""Sets the os_version of this ListFirmwaresResponseData.

        边缘设备操作系统版本

        :param os_version: The os_version of this ListFirmwaresResponseData.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def size(self):
        r"""Gets the size of this ListFirmwaresResponseData.

        当前固件大小(单位:byte)

        :return: The size of this ListFirmwaresResponseData.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListFirmwaresResponseData.

        当前固件大小(单位:byte)

        :param size: The size of this ListFirmwaresResponseData.
        :type size: int
        """
        self._size = size

    @property
    def create_time(self):
        r"""Gets the create_time of this ListFirmwaresResponseData.

        创建时间毫秒数

        :return: The create_time of this ListFirmwaresResponseData.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListFirmwaresResponseData.

        创建时间毫秒数

        :param create_time: The create_time of this ListFirmwaresResponseData.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ListFirmwaresResponseData.

        更新时间毫秒数

        :return: The update_time of this ListFirmwaresResponseData.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ListFirmwaresResponseData.

        更新时间毫秒数

        :param update_time: The update_time of this ListFirmwaresResponseData.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, ListFirmwaresResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
