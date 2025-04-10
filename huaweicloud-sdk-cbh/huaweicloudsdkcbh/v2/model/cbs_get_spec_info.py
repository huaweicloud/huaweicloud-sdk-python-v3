# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CbsGetSpecInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_spec_code': 'str',
        'ecs_system_data_size': 'int',
        'cpu': 'int',
        'ram': 'int',
        'asset': 'int',
        'connection': 'int',
        'type': 'str',
        'data_disk_size': 'float'
    }

    attribute_map = {
        'resource_spec_code': 'resource_spec_code',
        'ecs_system_data_size': 'ecs_system_data_size',
        'cpu': 'cpu',
        'ram': 'ram',
        'asset': 'asset',
        'connection': 'connection',
        'type': 'type',
        'data_disk_size': 'data_disk_size'
    }

    def __init__(self, resource_spec_code=None, ecs_system_data_size=None, cpu=None, ram=None, asset=None, connection=None, type=None, data_disk_size=None):
        r"""CbsGetSpecInfo

        The model defined in huaweicloud sdk

        :param resource_spec_code: 云堡垒机规格名称。
        :type resource_spec_code: str
        :param ecs_system_data_size: 云堡垒机系统盘磁盘大小，单位GB。
        :type ecs_system_data_size: int
        :param cpu: 云堡垒机CPU核心数。
        :type cpu: int
        :param ram: 云堡垒机内存大小，单位GB。
        :type ram: int
        :param asset: 云堡垒机资产数量。
        :type asset: int
        :param connection: 云堡垒机最大连接数。
        :type connection: int
        :param type: 云堡垒机规格类型。 - basic：标准版 - enhance：专业版
        :type type: str
        :param data_disk_size: 云堡垒机数据盘大小，单位TB。
        :type data_disk_size: float
        """
        
        

        self._resource_spec_code = None
        self._ecs_system_data_size = None
        self._cpu = None
        self._ram = None
        self._asset = None
        self._connection = None
        self._type = None
        self._data_disk_size = None
        self.discriminator = None

        self.resource_spec_code = resource_spec_code
        self.ecs_system_data_size = ecs_system_data_size
        self.cpu = cpu
        self.ram = ram
        self.asset = asset
        self.connection = connection
        self.type = type
        self.data_disk_size = data_disk_size

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this CbsGetSpecInfo.

        云堡垒机规格名称。

        :return: The resource_spec_code of this CbsGetSpecInfo.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this CbsGetSpecInfo.

        云堡垒机规格名称。

        :param resource_spec_code: The resource_spec_code of this CbsGetSpecInfo.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def ecs_system_data_size(self):
        r"""Gets the ecs_system_data_size of this CbsGetSpecInfo.

        云堡垒机系统盘磁盘大小，单位GB。

        :return: The ecs_system_data_size of this CbsGetSpecInfo.
        :rtype: int
        """
        return self._ecs_system_data_size

    @ecs_system_data_size.setter
    def ecs_system_data_size(self, ecs_system_data_size):
        r"""Sets the ecs_system_data_size of this CbsGetSpecInfo.

        云堡垒机系统盘磁盘大小，单位GB。

        :param ecs_system_data_size: The ecs_system_data_size of this CbsGetSpecInfo.
        :type ecs_system_data_size: int
        """
        self._ecs_system_data_size = ecs_system_data_size

    @property
    def cpu(self):
        r"""Gets the cpu of this CbsGetSpecInfo.

        云堡垒机CPU核心数。

        :return: The cpu of this CbsGetSpecInfo.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this CbsGetSpecInfo.

        云堡垒机CPU核心数。

        :param cpu: The cpu of this CbsGetSpecInfo.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def ram(self):
        r"""Gets the ram of this CbsGetSpecInfo.

        云堡垒机内存大小，单位GB。

        :return: The ram of this CbsGetSpecInfo.
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        r"""Sets the ram of this CbsGetSpecInfo.

        云堡垒机内存大小，单位GB。

        :param ram: The ram of this CbsGetSpecInfo.
        :type ram: int
        """
        self._ram = ram

    @property
    def asset(self):
        r"""Gets the asset of this CbsGetSpecInfo.

        云堡垒机资产数量。

        :return: The asset of this CbsGetSpecInfo.
        :rtype: int
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        r"""Sets the asset of this CbsGetSpecInfo.

        云堡垒机资产数量。

        :param asset: The asset of this CbsGetSpecInfo.
        :type asset: int
        """
        self._asset = asset

    @property
    def connection(self):
        r"""Gets the connection of this CbsGetSpecInfo.

        云堡垒机最大连接数。

        :return: The connection of this CbsGetSpecInfo.
        :rtype: int
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        r"""Sets the connection of this CbsGetSpecInfo.

        云堡垒机最大连接数。

        :param connection: The connection of this CbsGetSpecInfo.
        :type connection: int
        """
        self._connection = connection

    @property
    def type(self):
        r"""Gets the type of this CbsGetSpecInfo.

        云堡垒机规格类型。 - basic：标准版 - enhance：专业版

        :return: The type of this CbsGetSpecInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CbsGetSpecInfo.

        云堡垒机规格类型。 - basic：标准版 - enhance：专业版

        :param type: The type of this CbsGetSpecInfo.
        :type type: str
        """
        self._type = type

    @property
    def data_disk_size(self):
        r"""Gets the data_disk_size of this CbsGetSpecInfo.

        云堡垒机数据盘大小，单位TB。

        :return: The data_disk_size of this CbsGetSpecInfo.
        :rtype: float
        """
        return self._data_disk_size

    @data_disk_size.setter
    def data_disk_size(self, data_disk_size):
        r"""Sets the data_disk_size of this CbsGetSpecInfo.

        云堡垒机数据盘大小，单位TB。

        :param data_disk_size: The data_disk_size of this CbsGetSpecInfo.
        :type data_disk_size: float
        """
        self._data_disk_size = data_disk_size

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
        if not isinstance(other, CbsGetSpecInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
