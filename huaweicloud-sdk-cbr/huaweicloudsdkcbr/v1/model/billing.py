# coding: utf-8

import pprint
import re

import six





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
        'frozen_scene': 'str'
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
        'frozen_scene': 'frozen_scene'
    }

    def __init__(self, allocated=None, charging_mode=None, cloud_type=None, consistent_level=None, object_type=None, order_id=None, product_id=None, protect_type=None, size=None, spec_code=None, status=None, storage_unit=None, used=None, frozen_scene=None):
        """Billing - a model defined in huaweicloud sdk"""
        
        

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

    @property
    def allocated(self):
        """Gets the allocated of this Billing.

        已分配容量，单位MB

        :return: The allocated of this Billing.
        :rtype: int
        """
        return self._allocated

    @allocated.setter
    def allocated(self, allocated):
        """Sets the allocated of this Billing.

        已分配容量，单位MB

        :param allocated: The allocated of this Billing.
        :type: int
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
        :type: str
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
        :type: str
        """
        self._cloud_type = cloud_type

    @property
    def consistent_level(self):
        """Gets the consistent_level of this Billing.

        [规格，崩溃一致性（crash_consistent）或应用一致性（app_consistent）](tag:hws,hws_hk,fcs_vm,ctc) [规格，默认为崩溃一致性（crash_consistent）](tag:dt,ocb,tlf,sbc)

        :return: The consistent_level of this Billing.
        :rtype: str
        """
        return self._consistent_level

    @consistent_level.setter
    def consistent_level(self, consistent_level):
        """Sets the consistent_level of this Billing.

        [规格，崩溃一致性（crash_consistent）或应用一致性（app_consistent）](tag:hws,hws_hk,fcs_vm,ctc) [规格，默认为崩溃一致性（crash_consistent）](tag:dt,ocb,tlf,sbc)

        :param consistent_level: The consistent_level of this Billing.
        :type: str
        """
        self._consistent_level = consistent_level

    @property
    def object_type(self):
        """Gets the object_type of this Billing.

        对象类型

        :return: The object_type of this Billing.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this Billing.

        对象类型

        :param object_type: The object_type of this Billing.
        :type: str
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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: int
        """
        self._size = size

    @property
    def spec_code(self):
        """Gets the spec_code of this Billing.

        规格编码

        :return: The spec_code of this Billing.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this Billing.

        规格编码

        :param spec_code: The spec_code of this Billing.
        :type: str
        """
        self._spec_code = spec_code

    @property
    def status(self):
        """Gets the status of this Billing.

        保管库状态

        :return: The status of this Billing.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Billing.

        保管库状态

        :param status: The status of this Billing.
        :type: str
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
        :type: str
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
        :type: int
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
        :type: str
        """
        self._frozen_scene = frozen_scene

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Billing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
