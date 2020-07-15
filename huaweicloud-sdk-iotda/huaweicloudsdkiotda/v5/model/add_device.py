# coding: utf-8

import pprint
import re

import six





class AddDevice:


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
        'product_id': 'str',
        'auth_info': 'AuthInfo',
        'description': 'str',
        'gateway_id': 'str',
        'app_id': 'str',
        'extension_info': 'object',
        'shadow': 'list[InitialDesired]'
    }

    attribute_map = {
        'device_id': 'device_id',
        'node_id': 'node_id',
        'device_name': 'device_name',
        'product_id': 'product_id',
        'auth_info': 'auth_info',
        'description': 'description',
        'gateway_id': 'gateway_id',
        'app_id': 'app_id',
        'extension_info': 'extension_info',
        'shadow': 'shadow'
    }

    def __init__(self, device_id=None, node_id=None, device_name=None, product_id=None, auth_info=None, description=None, gateway_id=None, app_id=None, extension_info=None, shadow=None):
        """AddDevice - a model defined in huaweicloud sdk"""
        
        

        self._device_id = None
        self._node_id = None
        self._device_name = None
        self._product_id = None
        self._auth_info = None
        self._description = None
        self._gateway_id = None
        self._app_id = None
        self._extension_info = None
        self._shadow = None
        self.discriminator = None

        if device_id is not None:
            self.device_id = device_id
        self.node_id = node_id
        if device_name is not None:
            self.device_name = device_name
        self.product_id = product_id
        if auth_info is not None:
            self.auth_info = auth_info
        if description is not None:
            self.description = description
        if gateway_id is not None:
            self.gateway_id = gateway_id
        if app_id is not None:
            self.app_id = app_id
        if extension_info is not None:
            self.extension_info = extension_info
        if shadow is not None:
            self.shadow = shadow

    @property
    def device_id(self):
        """Gets the device_id of this AddDevice.

        设备ID，用于唯一标识一个设备。如果携带该参数，平台将设备ID设置为该参数值；如果不携带该参数，设备ID由物联网平台分配获得，生成规则为\"product_id\" + \"_\" + \"node_id\"拼接而成。

        :return: The device_id of this AddDevice.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this AddDevice.

        设备ID，用于唯一标识一个设备。如果携带该参数，平台将设备ID设置为该参数值；如果不携带该参数，设备ID由物联网平台分配获得，生成规则为\"product_id\" + \"_\" + \"node_id\"拼接而成。

        :param device_id: The device_id of this AddDevice.
        :type: str
        """
        self._device_id = device_id

    @property
    def node_id(self):
        """Gets the node_id of this AddDevice.

        设备标识码，通常使用IMEI、MAC地址或Serial No作为node_id。（注意:NB设备由于模组烧录信息后无法配置，所以NB设备会校验node_id全局唯一。）

        :return: The node_id of this AddDevice.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this AddDevice.

        设备标识码，通常使用IMEI、MAC地址或Serial No作为node_id。（注意:NB设备由于模组烧录信息后无法配置，所以NB设备会校验node_id全局唯一。）

        :param node_id: The node_id of this AddDevice.
        :type: str
        """
        self._node_id = node_id

    @property
    def device_name(self):
        """Gets the device_name of this AddDevice.

        设备名称。

        :return: The device_name of this AddDevice.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this AddDevice.

        设备名称。

        :param device_name: The device_name of this AddDevice.
        :type: str
        """
        self._device_name = device_name

    @property
    def product_id(self):
        """Gets the product_id of this AddDevice.

        设备关联的产品ID，用于唯一标识一个产品模型，在管理门户导入产品模型后由平台分配获得。

        :return: The product_id of this AddDevice.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this AddDevice.

        设备关联的产品ID，用于唯一标识一个产品模型，在管理门户导入产品模型后由平台分配获得。

        :param product_id: The product_id of this AddDevice.
        :type: str
        """
        self._product_id = product_id

    @property
    def auth_info(self):
        """Gets the auth_info of this AddDevice.


        :return: The auth_info of this AddDevice.
        :rtype: AuthInfo
        """
        return self._auth_info

    @auth_info.setter
    def auth_info(self, auth_info):
        """Sets the auth_info of this AddDevice.


        :param auth_info: The auth_info of this AddDevice.
        :type: AuthInfo
        """
        self._auth_info = auth_info

    @property
    def description(self):
        """Gets the description of this AddDevice.

        设备的描述信息。

        :return: The description of this AddDevice.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddDevice.

        设备的描述信息。

        :param description: The description of this AddDevice.
        :type: str
        """
        self._description = description

    @property
    def gateway_id(self):
        """Gets the gateway_id of this AddDevice.

        网关ID，用于标识设备所属的父设备，即父设备的设备ID。携带该参数时，表示在该父设备下创建一个子设备，这个子设备不与平台直连，此时必须保证这个父设备在平台已存在，创建成功后子设备的gateway_id等于该参数值；不携带该参数时，表示创建一个和平台直连的设备，创建成功后设备的device_id和gateway_id一致。注意：当前平台最多支持二级子设备。

        :return: The gateway_id of this AddDevice.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """Sets the gateway_id of this AddDevice.

        网关ID，用于标识设备所属的父设备，即父设备的设备ID。携带该参数时，表示在该父设备下创建一个子设备，这个子设备不与平台直连，此时必须保证这个父设备在平台已存在，创建成功后子设备的gateway_id等于该参数值；不携带该参数时，表示创建一个和平台直连的设备，创建成功后设备的device_id和gateway_id一致。注意：当前平台最多支持二级子设备。

        :param gateway_id: The gateway_id of this AddDevice.
        :type: str
        """
        self._gateway_id = gateway_id

    @property
    def app_id(self):
        """Gets the app_id of this AddDevice.

        资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的设备归属到哪个资源空间下，否则创建的设备将会归属到[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)下。

        :return: The app_id of this AddDevice.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this AddDevice.

        资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的设备归属到哪个资源空间下，否则创建的设备将会归属到[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)下。

        :param app_id: The app_id of this AddDevice.
        :type: str
        """
        self._app_id = app_id

    @property
    def extension_info(self):
        """Gets the extension_info of this AddDevice.

        设备扩展信息。用户可以自定义任何想要的扩展信息，如果在创建设备时为子设备指定该字段，将会通过MQTT接口“平台通知网关子设备新增“将该信息通知给网关。字段值大小上限为1K。

        :return: The extension_info of this AddDevice.
        :rtype: object
        """
        return self._extension_info

    @extension_info.setter
    def extension_info(self, extension_info):
        """Sets the extension_info of this AddDevice.

        设备扩展信息。用户可以自定义任何想要的扩展信息，如果在创建设备时为子设备指定该字段，将会通过MQTT接口“平台通知网关子设备新增“将该信息通知给网关。字段值大小上限为1K。

        :param extension_info: The extension_info of this AddDevice.
        :type: object
        """
        self._extension_info = extension_info

    @property
    def shadow(self):
        """Gets the shadow of this AddDevice.

        设备初始配置。用户使用该字段可以为设备指定初始配置，指定后将会根据service_id和desired设置的属性值与产品中对应属性的默认值比对，如果不同，则将以shadow字段中设置的属性值为准写入到设备影子中。service_id的值和desired内的属性必须是profile中定义的。

        :return: The shadow of this AddDevice.
        :rtype: list[InitialDesired]
        """
        return self._shadow

    @shadow.setter
    def shadow(self, shadow):
        """Sets the shadow of this AddDevice.

        设备初始配置。用户使用该字段可以为设备指定初始配置，指定后将会根据service_id和desired设置的属性值与产品中对应属性的默认值比对，如果不同，则将以shadow字段中设置的属性值为准写入到设备影子中。service_id的值和desired内的属性必须是profile中定义的。

        :param shadow: The shadow of this AddDevice.
        :type: list[InitialDesired]
        """
        self._shadow = shadow

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
        if not isinstance(other, AddDevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
