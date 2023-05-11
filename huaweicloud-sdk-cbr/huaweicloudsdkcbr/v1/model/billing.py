# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Billing:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'allocated': 'int',
        'charging_mode': 'str',
        'cloud_type': 'str',
        'consistent_level': 'str',
        'object_type': 'str',
        'order_id': 'str',
        'product_id': 'str',
        'protect_type': 'str',
        'size': 'int',
        'spec_code': 'str',
        'status': 'str',
        'storage_unit': 'str',
        'used': 'int',
        'frozen_scene': 'str',
        'is_multi_az': 'bool'
    }

    attribute_map = {
        'allocated': 'allocated',
        'charging_mode': 'charging_mode',
        'cloud_type': 'cloud_type',
        'consistent_level': 'consistent_level',
        'object_type': 'object_type',
        'order_id': 'order_id',
        'product_id': 'product_id',
        'protect_type': 'protect_type',
        'size': 'size',
        'spec_code': 'spec_code',
        'status': 'status',
        'storage_unit': 'storage_unit',
        'used': 'used',
        'frozen_scene': 'frozen_scene',
        'is_multi_az': 'is_multi_az'
    }

    def __init__(self, allocated=None, charging_mode=None, cloud_type=None, consistent_level=None, object_type=None, order_id=None, product_id=None, protect_type=None, size=None, spec_code=None, status=None, storage_unit=None, used=None, frozen_scene=None, is_multi_az=None):
        """Billing

        The model defined in huaweicloud sdk

        :param allocated: 已分配容量，单位GB
        :type allocated: int
        :param charging_mode: 创建模式
        :type charging_mode: str
        :param cloud_type: 云平台
        :type cloud_type: str
        :param consistent_level: 崩溃一致性（crash_consistent）或应用一致性（app_consistent）
        :type consistent_level: str
        :param object_type: 对象类型：云服务器（server），云硬盘（disk），文件系统（turbo），云桌面（workspace），VMware（vmware），关系型数据库（rds），文件（file）。
        :type object_type: str
        :param order_id: 订单ID
        :type order_id: str
        :param product_id: 产品ID
        :type product_id: str
        :param protect_type: 保护类型
        :type protect_type: str
        :param size: 容量，单位GB
        :type size: int
        :param spec_code: 规格编码: 云服务备份存储库:vault.backup.server.normal;云硬盘备份存储库:vault.backup.volume.normal;文件备份存储库:vault.backup.turbo.normal;数据库备份存储库:vault.backup.database.normal;混合云备份存储库:vault.hybrid.server.normal;复制备份存储库:vault.replication.server.normal
        :type spec_code: str
        :param status: 存储库状态
        :type status: str
        :param storage_unit: 存储库桶名
        :type storage_unit: str
        :param used: 已使用容量，单位MB
        :type used: int
        :param frozen_scene: 冻结场景
        :type frozen_scene: str
        :param is_multi_az: 存储库多az属性
        :type is_multi_az: bool
        """
        
        

        self._allocated = None
        self._charging_mode = None
        self._cloud_type = None
        self._consistent_level = None
        self._object_type = None
        self._order_id = None
        self._product_id = None
        self._protect_type = None
        self._size = None
        self._spec_code = None
        self._status = None
        self._storage_unit = None
        self._used = None
        self._frozen_scene = None
        self._is_multi_az = None
        self.discriminator = None

        self.allocated = allocated
        self.charging_mode = charging_mode
        if cloud_type is not None:
            self.cloud_type = cloud_type
        self.consistent_level = consistent_level
        if object_type is not None:
            self.object_type = object_type
        if order_id is not None:
            self.order_id = order_id
        if product_id is not None:
            self.product_id = product_id
        self.protect_type = protect_type
        self.size = size
        self.spec_code = spec_code
        self.status = status
        if storage_unit is not None:
            self.storage_unit = storage_unit
        self.used = used
        if frozen_scene is not None:
            self.frozen_scene = frozen_scene
        if is_multi_az is not None:
            self.is_multi_az = is_multi_az

    @property
    def allocated(self):
        """Gets the allocated of this Billing.

        已分配容量，单位GB

        :return: The allocated of this Billing.
        :rtype: int
        """
        return self._allocated

    @allocated.setter
    def allocated(self, allocated):
        """Sets the allocated of this Billing.

        已分配容量，单位GB

        :param allocated: The allocated of this Billing.
        :type allocated: int
        """
        self._allocated = allocated

    @property
    def charging_mode(self):
        """Gets the charging_mode of this Billing.

        创建模式

        :return: The charging_mode of this Billing.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this Billing.

        创建模式

        :param charging_mode: The charging_mode of this Billing.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def cloud_type(self):
        """Gets the cloud_type of this Billing.

        云平台

        :return: The cloud_type of this Billing.
        :rtype: str
        """
        return self._cloud_type

    @cloud_type.setter
    def cloud_type(self, cloud_type):
        """Sets the cloud_type of this Billing.

        云平台

        :param cloud_type: The cloud_type of this Billing.
        :type cloud_type: str
        """
        self._cloud_type = cloud_type

    @property
    def consistent_level(self):
        """Gets the consistent_level of this Billing.

        崩溃一致性（crash_consistent）或应用一致性（app_consistent）

        :return: The consistent_level of this Billing.
        :rtype: str
        """
        return self._consistent_level

    @consistent_level.setter
    def consistent_level(self, consistent_level):
        """Sets the consistent_level of this Billing.

        崩溃一致性（crash_consistent）或应用一致性（app_consistent）

        :param consistent_level: The consistent_level of this Billing.
        :type consistent_level: str
        """
        self._consistent_level = consistent_level

    @property
    def object_type(self):
        """Gets the object_type of this Billing.

        对象类型：云服务器（server），云硬盘（disk），文件系统（turbo），云桌面（workspace），VMware（vmware），关系型数据库（rds），文件（file）。

        :return: The object_type of this Billing.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this Billing.

        对象类型：云服务器（server），云硬盘（disk），文件系统（turbo），云桌面（workspace），VMware（vmware），关系型数据库（rds），文件（file）。

        :param object_type: The object_type of this Billing.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def order_id(self):
        """Gets the order_id of this Billing.

        订单ID

        :return: The order_id of this Billing.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this Billing.

        订单ID

        :param order_id: The order_id of this Billing.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def product_id(self):
        """Gets the product_id of this Billing.

        产品ID

        :return: The product_id of this Billing.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this Billing.

        产品ID

        :param product_id: The product_id of this Billing.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def protect_type(self):
        """Gets the protect_type of this Billing.

        保护类型

        :return: The protect_type of this Billing.
        :rtype: str
        """
        return self._protect_type

    @protect_type.setter
    def protect_type(self, protect_type):
        """Sets the protect_type of this Billing.

        保护类型

        :param protect_type: The protect_type of this Billing.
        :type protect_type: str
        """
        self._protect_type = protect_type

    @property
    def size(self):
        """Gets the size of this Billing.

        容量，单位GB

        :return: The size of this Billing.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Billing.

        容量，单位GB

        :param size: The size of this Billing.
        :type size: int
        """
        self._size = size

    @property
    def spec_code(self):
        """Gets the spec_code of this Billing.

        规格编码: 云服务备份存储库:vault.backup.server.normal;云硬盘备份存储库:vault.backup.volume.normal;文件备份存储库:vault.backup.turbo.normal;数据库备份存储库:vault.backup.database.normal;混合云备份存储库:vault.hybrid.server.normal;复制备份存储库:vault.replication.server.normal

        :return: The spec_code of this Billing.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this Billing.

        规格编码: 云服务备份存储库:vault.backup.server.normal;云硬盘备份存储库:vault.backup.volume.normal;文件备份存储库:vault.backup.turbo.normal;数据库备份存储库:vault.backup.database.normal;混合云备份存储库:vault.hybrid.server.normal;复制备份存储库:vault.replication.server.normal

        :param spec_code: The spec_code of this Billing.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def status(self):
        """Gets the status of this Billing.

        存储库状态

        :return: The status of this Billing.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Billing.

        存储库状态

        :param status: The status of this Billing.
        :type status: str
        """
        self._status = status

    @property
    def storage_unit(self):
        """Gets the storage_unit of this Billing.

        存储库桶名

        :return: The storage_unit of this Billing.
        :rtype: str
        """
        return self._storage_unit

    @storage_unit.setter
    def storage_unit(self, storage_unit):
        """Sets the storage_unit of this Billing.

        存储库桶名

        :param storage_unit: The storage_unit of this Billing.
        :type storage_unit: str
        """
        self._storage_unit = storage_unit

    @property
    def used(self):
        """Gets the used of this Billing.

        已使用容量，单位MB

        :return: The used of this Billing.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this Billing.

        已使用容量，单位MB

        :param used: The used of this Billing.
        :type used: int
        """
        self._used = used

    @property
    def frozen_scene(self):
        """Gets the frozen_scene of this Billing.

        冻结场景

        :return: The frozen_scene of this Billing.
        :rtype: str
        """
        return self._frozen_scene

    @frozen_scene.setter
    def frozen_scene(self, frozen_scene):
        """Sets the frozen_scene of this Billing.

        冻结场景

        :param frozen_scene: The frozen_scene of this Billing.
        :type frozen_scene: str
        """
        self._frozen_scene = frozen_scene

    @property
    def is_multi_az(self):
        """Gets the is_multi_az of this Billing.

        存储库多az属性

        :return: The is_multi_az of this Billing.
        :rtype: bool
        """
        return self._is_multi_az

    @is_multi_az.setter
    def is_multi_az(self, is_multi_az):
        """Sets the is_multi_az of this Billing.

        存储库多az属性

        :param is_multi_az: The is_multi_az of this Billing.
        :type is_multi_az: bool
        """
        self._is_multi_az = is_multi_az

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
        if not isinstance(other, Billing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
