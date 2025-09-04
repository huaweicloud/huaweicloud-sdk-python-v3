# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeviceSimple:

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
        'device_id': 'str',
        'node_id': 'str',
        'gateway_id': 'str',
        'device_name': 'str',
        'product_id': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'device_id': 'device_id',
        'node_id': 'node_id',
        'gateway_id': 'gateway_id',
        'device_name': 'device_name',
        'product_id': 'product_id'
    }

    def __init__(self, app_id=None, device_id=None, node_id=None, gateway_id=None, device_name=None, product_id=None):
        r"""DeviceSimple

        The model defined in huaweicloud sdk

        :param app_id: 资源空间ID。
        :type app_id: str
        :param device_id: 设备ID，用于唯一标识一个设备。在注册设备时直接指定，或者由物联网平台分配获得。由物联网平台分配时，生成规则为\&quot;product_id\&quot; + \&quot;_\&quot; + \&quot;node_id\&quot;拼接而成。
        :type device_id: str
        :param node_id: 设备标识码，通常使用IMEI、MAC地址或Serial No作为node_id。
        :type node_id: str
        :param gateway_id: 网关ID，用于标识设备所属的父设备，即父设备的设备ID。当设备是直连设备时，gateway_id与设备的device_id一致。当设备是非直连设备时，gateway_id为设备所关联的父设备的device_id。
        :type gateway_id: str
        :param device_name: 设备名称。
        :type device_name: str
        :param product_id: 设备关联的产品ID，用于唯一标识一个产品模型。
        :type product_id: str
        """
        
        

        self._app_id = None
        self._device_id = None
        self._node_id = None
        self._gateway_id = None
        self._device_name = None
        self._product_id = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if device_id is not None:
            self.device_id = device_id
        if node_id is not None:
            self.node_id = node_id
        if gateway_id is not None:
            self.gateway_id = gateway_id
        if device_name is not None:
            self.device_name = device_name
        if product_id is not None:
            self.product_id = product_id

    @property
    def app_id(self):
        r"""Gets the app_id of this DeviceSimple.

        资源空间ID。

        :return: The app_id of this DeviceSimple.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this DeviceSimple.

        资源空间ID。

        :param app_id: The app_id of this DeviceSimple.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def device_id(self):
        r"""Gets the device_id of this DeviceSimple.

        设备ID，用于唯一标识一个设备。在注册设备时直接指定，或者由物联网平台分配获得。由物联网平台分配时，生成规则为\"product_id\" + \"_\" + \"node_id\"拼接而成。

        :return: The device_id of this DeviceSimple.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        r"""Sets the device_id of this DeviceSimple.

        设备ID，用于唯一标识一个设备。在注册设备时直接指定，或者由物联网平台分配获得。由物联网平台分配时，生成规则为\"product_id\" + \"_\" + \"node_id\"拼接而成。

        :param device_id: The device_id of this DeviceSimple.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def node_id(self):
        r"""Gets the node_id of this DeviceSimple.

        设备标识码，通常使用IMEI、MAC地址或Serial No作为node_id。

        :return: The node_id of this DeviceSimple.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this DeviceSimple.

        设备标识码，通常使用IMEI、MAC地址或Serial No作为node_id。

        :param node_id: The node_id of this DeviceSimple.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def gateway_id(self):
        r"""Gets the gateway_id of this DeviceSimple.

        网关ID，用于标识设备所属的父设备，即父设备的设备ID。当设备是直连设备时，gateway_id与设备的device_id一致。当设备是非直连设备时，gateway_id为设备所关联的父设备的device_id。

        :return: The gateway_id of this DeviceSimple.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        r"""Sets the gateway_id of this DeviceSimple.

        网关ID，用于标识设备所属的父设备，即父设备的设备ID。当设备是直连设备时，gateway_id与设备的device_id一致。当设备是非直连设备时，gateway_id为设备所关联的父设备的device_id。

        :param gateway_id: The gateway_id of this DeviceSimple.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

    @property
    def device_name(self):
        r"""Gets the device_name of this DeviceSimple.

        设备名称。

        :return: The device_name of this DeviceSimple.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        r"""Sets the device_name of this DeviceSimple.

        设备名称。

        :param device_name: The device_name of this DeviceSimple.
        :type device_name: str
        """
        self._device_name = device_name

    @property
    def product_id(self):
        r"""Gets the product_id of this DeviceSimple.

        设备关联的产品ID，用于唯一标识一个产品模型。

        :return: The product_id of this DeviceSimple.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this DeviceSimple.

        设备关联的产品ID，用于唯一标识一个产品模型。

        :param product_id: The product_id of this DeviceSimple.
        :type product_id: str
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
        if not isinstance(other, DeviceSimple):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
