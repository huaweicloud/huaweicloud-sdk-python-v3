# coding: utf-8

import pprint
import re

import six





class SimplifyDevice:


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
        'node_id': 'str',
        'device_name': 'str',
        'product_id': 'str'
    }

    attribute_map = {
        'device_id': 'device_id',
        'node_id': 'node_id',
        'device_name': 'device_name',
        'product_id': 'product_id'
    }

    def __init__(self, device_id=None, node_id=None, device_name=None, product_id=None):
        """SimplifyDevice - a model defined in huaweicloud sdk"""
        
        

        self._device_id = None
        self._node_id = None
        self._device_name = None
        self._product_id = None
        self.discriminator = None

        if device_id is not None:
            self.device_id = device_id
        if node_id is not None:
            self.node_id = node_id
        if device_name is not None:
            self.device_name = device_name
        if product_id is not None:
            self.product_id = product_id

    @property
    def device_id(self):
        """Gets the device_id of this SimplifyDevice.

        设备ID，用于唯一标识一个设备。在注册设备时直接指定，或者由物联网平台分配获得。由物联网平台分配时，生成规则为\"product_id\" + \"_\" + \"node_id\"拼接而成。

        :return: The device_id of this SimplifyDevice.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this SimplifyDevice.

        设备ID，用于唯一标识一个设备。在注册设备时直接指定，或者由物联网平台分配获得。由物联网平台分配时，生成规则为\"product_id\" + \"_\" + \"node_id\"拼接而成。

        :param device_id: The device_id of this SimplifyDevice.
        :type: str
        """
        self._device_id = device_id

    @property
    def node_id(self):
        """Gets the node_id of this SimplifyDevice.

        设备标识码，通常使用IMEI、MAC地址或Serial No作为nodeId。

        :return: The node_id of this SimplifyDevice.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this SimplifyDevice.

        设备标识码，通常使用IMEI、MAC地址或Serial No作为nodeId。

        :param node_id: The node_id of this SimplifyDevice.
        :type: str
        """
        self._node_id = node_id

    @property
    def device_name(self):
        """Gets the device_name of this SimplifyDevice.

        设备名称。

        :return: The device_name of this SimplifyDevice.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this SimplifyDevice.

        设备名称。

        :param device_name: The device_name of this SimplifyDevice.
        :type: str
        """
        self._device_name = device_name

    @property
    def product_id(self):
        """Gets the product_id of this SimplifyDevice.

        设备关联的产品ID，用于唯一标识一个产品模型。

        :return: The product_id of this SimplifyDevice.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this SimplifyDevice.

        设备关联的产品ID，用于唯一标识一个产品模型。

        :param product_id: The product_id of this SimplifyDevice.
        :type: str
        """
        self._product_id = product_id

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
        if not isinstance(other, SimplifyDevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
