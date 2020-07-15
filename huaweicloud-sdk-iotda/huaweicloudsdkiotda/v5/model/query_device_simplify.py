# coding: utf-8

import pprint
import re

import six





class QueryDeviceSimplify:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'app_name': 'str',
        'device_id': 'str',
        'node_id': 'str',
        'gateway_id': 'str',
        'device_name': 'str',
        'node_type': 'str',
        'description': 'str',
        'fw_version': 'str',
        'sw_version': 'str',
        'product_id': 'str',
        'product_name': 'str',
        'status': 'str',
        'tags': 'list[TagV5DTO]'
    }

    attribute_map = {
        'app_id': 'app_id',
        'app_name': 'app_name',
        'device_id': 'device_id',
        'node_id': 'node_id',
        'gateway_id': 'gateway_id',
        'device_name': 'device_name',
        'node_type': 'node_type',
        'description': 'description',
        'fw_version': 'fw_version',
        'sw_version': 'sw_version',
        'product_id': 'product_id',
        'product_name': 'product_name',
        'status': 'status',
        'tags': 'tags'
    }

    def __init__(self, app_id=None, app_name=None, device_id=None, node_id=None, gateway_id=None, device_name=None, node_type=None, description=None, fw_version=None, sw_version=None, product_id=None, product_name=None, status=None, tags=None):
        """QueryDeviceSimplify - a model defined in huaweicloud sdk"""
        
        

        self._app_id = None
        self._app_name = None
        self._device_id = None
        self._node_id = None
        self._gateway_id = None
        self._device_name = None
        self._node_type = None
        self._description = None
        self._fw_version = None
        self._sw_version = None
        self._product_id = None
        self._product_name = None
        self._status = None
        self._tags = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if app_name is not None:
            self.app_name = app_name
        if device_id is not None:
            self.device_id = device_id
        if node_id is not None:
            self.node_id = node_id
        if gateway_id is not None:
            self.gateway_id = gateway_id
        if device_name is not None:
            self.device_name = device_name
        if node_type is not None:
            self.node_type = node_type
        if description is not None:
            self.description = description
        if fw_version is not None:
            self.fw_version = fw_version
        if sw_version is not None:
            self.sw_version = sw_version
        if product_id is not None:
            self.product_id = product_id
        if product_name is not None:
            self.product_name = product_name
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags

    @property
    def app_id(self):
        """Gets the app_id of this QueryDeviceSimplify.

        资源空间ID。

        :return: The app_id of this QueryDeviceSimplify.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this QueryDeviceSimplify.

        资源空间ID。

        :param app_id: The app_id of this QueryDeviceSimplify.
        :type: str
        """
        self._app_id = app_id

    @property
    def app_name(self):
        """Gets the app_name of this QueryDeviceSimplify.

        资源空间名称。

        :return: The app_name of this QueryDeviceSimplify.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this QueryDeviceSimplify.

        资源空间名称。

        :param app_name: The app_name of this QueryDeviceSimplify.
        :type: str
        """
        self._app_name = app_name

    @property
    def device_id(self):
        """Gets the device_id of this QueryDeviceSimplify.

        设备ID，用于唯一标识一个设备。在注册设备时直接指定，或者由物联网平台分配获得。由物联网平台分配时，生成规则为\"product_id\" + \"_\" + \"node_id\"拼接而成。

        :return: The device_id of this QueryDeviceSimplify.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this QueryDeviceSimplify.

        设备ID，用于唯一标识一个设备。在注册设备时直接指定，或者由物联网平台分配获得。由物联网平台分配时，生成规则为\"product_id\" + \"_\" + \"node_id\"拼接而成。

        :param device_id: The device_id of this QueryDeviceSimplify.
        :type: str
        """
        self._device_id = device_id

    @property
    def node_id(self):
        """Gets the node_id of this QueryDeviceSimplify.

        设备标识码，通常使用IMEI、MAC地址或Serial No作为nodeId。

        :return: The node_id of this QueryDeviceSimplify.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this QueryDeviceSimplify.

        设备标识码，通常使用IMEI、MAC地址或Serial No作为nodeId。

        :param node_id: The node_id of this QueryDeviceSimplify.
        :type: str
        """
        self._node_id = node_id

    @property
    def gateway_id(self):
        """Gets the gateway_id of this QueryDeviceSimplify.

        网关ID，用于标识设备所属的父设备，即父设备的设备ID。当设备是直连设备时，gateway_id与设备的device_id一致。当设备是非直连设备时，gateway_id为设备所关联的父设备的device_id。

        :return: The gateway_id of this QueryDeviceSimplify.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """Sets the gateway_id of this QueryDeviceSimplify.

        网关ID，用于标识设备所属的父设备，即父设备的设备ID。当设备是直连设备时，gateway_id与设备的device_id一致。当设备是非直连设备时，gateway_id为设备所关联的父设备的device_id。

        :param gateway_id: The gateway_id of this QueryDeviceSimplify.
        :type: str
        """
        self._gateway_id = gateway_id

    @property
    def device_name(self):
        """Gets the device_name of this QueryDeviceSimplify.

        设备名称。

        :return: The device_name of this QueryDeviceSimplify.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this QueryDeviceSimplify.

        设备名称。

        :param device_name: The device_name of this QueryDeviceSimplify.
        :type: str
        """
        self._device_name = device_name

    @property
    def node_type(self):
        """Gets the node_type of this QueryDeviceSimplify.

        设备节点类型。 - ENDPOINT：非直连设备。 - GATEWAY：直连设备或网关。 - UNKNOWN：未知。 

        :return: The node_type of this QueryDeviceSimplify.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this QueryDeviceSimplify.

        设备节点类型。 - ENDPOINT：非直连设备。 - GATEWAY：直连设备或网关。 - UNKNOWN：未知。 

        :param node_type: The node_type of this QueryDeviceSimplify.
        :type: str
        """
        self._node_type = node_type

    @property
    def description(self):
        """Gets the description of this QueryDeviceSimplify.

        设备的描述信息。

        :return: The description of this QueryDeviceSimplify.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this QueryDeviceSimplify.

        设备的描述信息。

        :param description: The description of this QueryDeviceSimplify.
        :type: str
        """
        self._description = description

    @property
    def fw_version(self):
        """Gets the fw_version of this QueryDeviceSimplify.

        设备的固件版本。

        :return: The fw_version of this QueryDeviceSimplify.
        :rtype: str
        """
        return self._fw_version

    @fw_version.setter
    def fw_version(self, fw_version):
        """Sets the fw_version of this QueryDeviceSimplify.

        设备的固件版本。

        :param fw_version: The fw_version of this QueryDeviceSimplify.
        :type: str
        """
        self._fw_version = fw_version

    @property
    def sw_version(self):
        """Gets the sw_version of this QueryDeviceSimplify.

        设备的软件版本。

        :return: The sw_version of this QueryDeviceSimplify.
        :rtype: str
        """
        return self._sw_version

    @sw_version.setter
    def sw_version(self, sw_version):
        """Sets the sw_version of this QueryDeviceSimplify.

        设备的软件版本。

        :param sw_version: The sw_version of this QueryDeviceSimplify.
        :type: str
        """
        self._sw_version = sw_version

    @property
    def product_id(self):
        """Gets the product_id of this QueryDeviceSimplify.

        设备关联的产品ID，用于唯一标识一个产品模型。

        :return: The product_id of this QueryDeviceSimplify.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this QueryDeviceSimplify.

        设备关联的产品ID，用于唯一标识一个产品模型。

        :param product_id: The product_id of this QueryDeviceSimplify.
        :type: str
        """
        self._product_id = product_id

    @property
    def product_name(self):
        """Gets the product_name of this QueryDeviceSimplify.

        设备关联的产品名称。

        :return: The product_name of this QueryDeviceSimplify.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this QueryDeviceSimplify.

        设备关联的产品名称。

        :param product_name: The product_name of this QueryDeviceSimplify.
        :type: str
        """
        self._product_name = product_name

    @property
    def status(self):
        """Gets the status of this QueryDeviceSimplify.

        设备的状态。 - ONLINE：设备在线。 - OFFLINE：设备离线。 - ABNORMAL：设备异常。 - INACTIVE：设备未激活。 - FREEZED：设备冻结。 

        :return: The status of this QueryDeviceSimplify.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this QueryDeviceSimplify.

        设备的状态。 - ONLINE：设备在线。 - OFFLINE：设备离线。 - ABNORMAL：设备异常。 - INACTIVE：设备未激活。 - FREEZED：设备冻结。 

        :param status: The status of this QueryDeviceSimplify.
        :type: str
        """
        self._status = status

    @property
    def tags(self):
        """Gets the tags of this QueryDeviceSimplify.

        设备的标签列表。

        :return: The tags of this QueryDeviceSimplify.
        :rtype: list[TagV5DTO]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this QueryDeviceSimplify.

        设备的标签列表。

        :param tags: The tags of this QueryDeviceSimplify.
        :type: list[TagV5DTO]
        """
        self._tags = tags

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
        if not isinstance(other, QueryDeviceSimplify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
