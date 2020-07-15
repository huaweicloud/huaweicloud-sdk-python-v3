# coding: utf-8

import pprint
import re

import six





class DeviceDataCondition:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'device_id': 'str',
        'product_id': 'str',
        'filters': 'list[PropertyFilter]'
    }

    attribute_map = {
        'device_id': 'device_id',
        'product_id': 'product_id',
        'filters': 'filters'
    }

    def __init__(self, device_id=None, product_id=None, filters=None):
        """DeviceDataCondition - a model defined in huaweicloud sdk"""
        
        

        self._device_id = None
        self._product_id = None
        self._filters = None
        self.discriminator = None

        if device_id is not None:
            self.device_id = device_id
        if product_id is not None:
            self.product_id = product_id
        if filters is not None:
            self.filters = filters

    @property
    def device_id(self):
        """Gets the device_id of this DeviceDataCondition.

        设备ID，用于唯一标识一个设备，在注册设备时由物联网平台分配获得。当rule_type为DEVICE_LINKAGE时，该参数值和product_id不能同时为空。如果该参数和product_id同时存在时，以该参数值对应的设备进行条件过滤。

        :return: The device_id of this DeviceDataCondition.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this DeviceDataCondition.

        设备ID，用于唯一标识一个设备，在注册设备时由物联网平台分配获得。当rule_type为DEVICE_LINKAGE时，该参数值和product_id不能同时为空。如果该参数和product_id同时存在时，以该参数值对应的设备进行条件过滤。

        :param device_id: The device_id of this DeviceDataCondition.
        :type: str
        """
        self._device_id = device_id

    @property
    def product_id(self):
        """Gets the product_id of this DeviceDataCondition.

        设备关联的产品ID，用于唯一标识一个产品模型，在管理门户导入产品模型后由平台分配获得。当rule_type为DEVICE_LINKAGE时，该参数值和device_id不能同时为空。如果该参数和device_id同时存在时，以device_id参数值对应的设备进行条件过滤。

        :return: The product_id of this DeviceDataCondition.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this DeviceDataCondition.

        设备关联的产品ID，用于唯一标识一个产品模型，在管理门户导入产品模型后由平台分配获得。当rule_type为DEVICE_LINKAGE时，该参数值和device_id不能同时为空。如果该参数和device_id同时存在时，以device_id参数值对应的设备进行条件过滤。

        :param product_id: The product_id of this DeviceDataCondition.
        :type: str
        """
        self._product_id = product_id

    @property
    def filters(self):
        """Gets the filters of this DeviceDataCondition.

        数据过滤条件

        :return: The filters of this DeviceDataCondition.
        :rtype: list[PropertyFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this DeviceDataCondition.

        数据过滤条件

        :param filters: The filters of this DeviceDataCondition.
        :type: list[PropertyFilter]
        """
        self._filters = filters

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
        if not isinstance(other, DeviceDataCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
