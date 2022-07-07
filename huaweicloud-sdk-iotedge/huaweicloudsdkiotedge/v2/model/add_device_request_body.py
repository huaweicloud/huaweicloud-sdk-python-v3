# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddDeviceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'device_name': 'str',
        'product_id': 'str',
        'auth_info': 'EdgeDeviceAuthInfo',
        'description': 'str',
        'gateway_id': 'str',
        'space_id': 'str',
        'extension_info': 'object',
        'config': 'object'
    }

    attribute_map = {
        'node_id': 'node_id',
        'device_name': 'device_name',
        'product_id': 'product_id',
        'auth_info': 'auth_info',
        'description': 'description',
        'gateway_id': 'gateway_id',
        'space_id': 'space_id',
        'extension_info': 'extension_info',
        'config': 'config'
    }

    def __init__(self, node_id=None, device_name=None, product_id=None, auth_info=None, description=None, gateway_id=None, space_id=None, extension_info=None, config=None):
        """AddDeviceRequestBody

        The model defined in huaweicloud sdk

        :param node_id: 设备标识码，通常使用IMEI、MAC地址或Serial No作为node_id。（注意:NB设备由于模组烧录信息后无法配置，所以NB设备会校验node_id全局唯一。）
        :type node_id: str
        :param device_name: 设备名称。
        :type device_name: str
        :param product_id: 设备关联的产品ID，用于唯一标识一个产品模型，在管理门户导入产品模型后由平台分配获得。
        :type product_id: str
        :param auth_info: 
        :type auth_info: :class:`huaweicloudsdkiotedge.v2.EdgeDeviceAuthInfo`
        :param description: 设备的描述信息。
        :type description: str
        :param gateway_id: 父设备ID，用于标识设备所属的父设备。创建网关直连设备时，不携带该参数；在网关直连设备下创建子设备时，携带该参数，参数值为父设备ID。
        :type gateway_id: str
        :param space_id: 资源空间Id。此参数为非必选参数，用于兼容平台老用户存在多应用的场景。存在多应用的用户需要使用该接口时，必须携带该参数指定注册的设备归属到哪个应用下，否则接口会提示错误。如果用户存在多应用，同时又不想携带该参数，可以联系华为技术支持对用户数据做应用合并。
        :type space_id: str
        :param extension_info: 设备扩展信息。用户可以自定义任何想要的扩展信息，如果在创建设备时为子设备指定该字段，将会通过MQTT接口“平台通知网关子设备新增“将该信息通知给网关。字段值大小上限为1K。 追加：如果通过EdgeHub, EdgeAccess进行设备接入，不需要携带extension_info；如果通过用户自定义的应用进行边缘设备接入，则携带模块id参数作为extension_info, 例如：{\\\&quot;module_id\&quot;:\\\&quot;user_xxx\&quot;}
        :type extension_info: object
        :param config: 设备初始配置。用户使用该字段可以为设备指定初始配置，指定后将会根据service_id和desired设置的属性值与产品中对应属性的默认值比对，如果不同，则将以设置的属性值为准写入到设备配置中。例如连接MQTT设备，配置接入平台密码，携带该参数{\\\&quot;password\&quot;:\\\&quot;xxxxxxxx\&quot;}
        :type config: object
        """
        
        

        self._node_id = None
        self._device_name = None
        self._product_id = None
        self._auth_info = None
        self._description = None
        self._gateway_id = None
        self._space_id = None
        self._extension_info = None
        self._config = None
        self.discriminator = None

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
        if space_id is not None:
            self.space_id = space_id
        if extension_info is not None:
            self.extension_info = extension_info
        if config is not None:
            self.config = config

    @property
    def node_id(self):
        """Gets the node_id of this AddDeviceRequestBody.

        设备标识码，通常使用IMEI、MAC地址或Serial No作为node_id。（注意:NB设备由于模组烧录信息后无法配置，所以NB设备会校验node_id全局唯一。）

        :return: The node_id of this AddDeviceRequestBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this AddDeviceRequestBody.

        设备标识码，通常使用IMEI、MAC地址或Serial No作为node_id。（注意:NB设备由于模组烧录信息后无法配置，所以NB设备会校验node_id全局唯一。）

        :param node_id: The node_id of this AddDeviceRequestBody.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def device_name(self):
        """Gets the device_name of this AddDeviceRequestBody.

        设备名称。

        :return: The device_name of this AddDeviceRequestBody.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this AddDeviceRequestBody.

        设备名称。

        :param device_name: The device_name of this AddDeviceRequestBody.
        :type device_name: str
        """
        self._device_name = device_name

    @property
    def product_id(self):
        """Gets the product_id of this AddDeviceRequestBody.

        设备关联的产品ID，用于唯一标识一个产品模型，在管理门户导入产品模型后由平台分配获得。

        :return: The product_id of this AddDeviceRequestBody.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this AddDeviceRequestBody.

        设备关联的产品ID，用于唯一标识一个产品模型，在管理门户导入产品模型后由平台分配获得。

        :param product_id: The product_id of this AddDeviceRequestBody.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def auth_info(self):
        """Gets the auth_info of this AddDeviceRequestBody.


        :return: The auth_info of this AddDeviceRequestBody.
        :rtype: :class:`huaweicloudsdkiotedge.v2.EdgeDeviceAuthInfo`
        """
        return self._auth_info

    @auth_info.setter
    def auth_info(self, auth_info):
        """Sets the auth_info of this AddDeviceRequestBody.


        :param auth_info: The auth_info of this AddDeviceRequestBody.
        :type auth_info: :class:`huaweicloudsdkiotedge.v2.EdgeDeviceAuthInfo`
        """
        self._auth_info = auth_info

    @property
    def description(self):
        """Gets the description of this AddDeviceRequestBody.

        设备的描述信息。

        :return: The description of this AddDeviceRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddDeviceRequestBody.

        设备的描述信息。

        :param description: The description of this AddDeviceRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def gateway_id(self):
        """Gets the gateway_id of this AddDeviceRequestBody.

        父设备ID，用于标识设备所属的父设备。创建网关直连设备时，不携带该参数；在网关直连设备下创建子设备时，携带该参数，参数值为父设备ID。

        :return: The gateway_id of this AddDeviceRequestBody.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """Sets the gateway_id of this AddDeviceRequestBody.

        父设备ID，用于标识设备所属的父设备。创建网关直连设备时，不携带该参数；在网关直连设备下创建子设备时，携带该参数，参数值为父设备ID。

        :param gateway_id: The gateway_id of this AddDeviceRequestBody.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

    @property
    def space_id(self):
        """Gets the space_id of this AddDeviceRequestBody.

        资源空间Id。此参数为非必选参数，用于兼容平台老用户存在多应用的场景。存在多应用的用户需要使用该接口时，必须携带该参数指定注册的设备归属到哪个应用下，否则接口会提示错误。如果用户存在多应用，同时又不想携带该参数，可以联系华为技术支持对用户数据做应用合并。

        :return: The space_id of this AddDeviceRequestBody.
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this AddDeviceRequestBody.

        资源空间Id。此参数为非必选参数，用于兼容平台老用户存在多应用的场景。存在多应用的用户需要使用该接口时，必须携带该参数指定注册的设备归属到哪个应用下，否则接口会提示错误。如果用户存在多应用，同时又不想携带该参数，可以联系华为技术支持对用户数据做应用合并。

        :param space_id: The space_id of this AddDeviceRequestBody.
        :type space_id: str
        """
        self._space_id = space_id

    @property
    def extension_info(self):
        """Gets the extension_info of this AddDeviceRequestBody.

        设备扩展信息。用户可以自定义任何想要的扩展信息，如果在创建设备时为子设备指定该字段，将会通过MQTT接口“平台通知网关子设备新增“将该信息通知给网关。字段值大小上限为1K。 追加：如果通过EdgeHub, EdgeAccess进行设备接入，不需要携带extension_info；如果通过用户自定义的应用进行边缘设备接入，则携带模块id参数作为extension_info, 例如：{\\\"module_id\":\\\"user_xxx\"}

        :return: The extension_info of this AddDeviceRequestBody.
        :rtype: object
        """
        return self._extension_info

    @extension_info.setter
    def extension_info(self, extension_info):
        """Sets the extension_info of this AddDeviceRequestBody.

        设备扩展信息。用户可以自定义任何想要的扩展信息，如果在创建设备时为子设备指定该字段，将会通过MQTT接口“平台通知网关子设备新增“将该信息通知给网关。字段值大小上限为1K。 追加：如果通过EdgeHub, EdgeAccess进行设备接入，不需要携带extension_info；如果通过用户自定义的应用进行边缘设备接入，则携带模块id参数作为extension_info, 例如：{\\\"module_id\":\\\"user_xxx\"}

        :param extension_info: The extension_info of this AddDeviceRequestBody.
        :type extension_info: object
        """
        self._extension_info = extension_info

    @property
    def config(self):
        """Gets the config of this AddDeviceRequestBody.

        设备初始配置。用户使用该字段可以为设备指定初始配置，指定后将会根据service_id和desired设置的属性值与产品中对应属性的默认值比对，如果不同，则将以设置的属性值为准写入到设备配置中。例如连接MQTT设备，配置接入平台密码，携带该参数{\\\"password\":\\\"xxxxxxxx\"}

        :return: The config of this AddDeviceRequestBody.
        :rtype: object
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this AddDeviceRequestBody.

        设备初始配置。用户使用该字段可以为设备指定初始配置，指定后将会根据service_id和desired设置的属性值与产品中对应属性的默认值比对，如果不同，则将以设置的属性值为准写入到设备配置中。例如连接MQTT设备，配置接入平台密码，携带该参数{\\\"password\":\\\"xxxxxxxx\"}

        :param config: The config of this AddDeviceRequestBody.
        :type config: object
        """
        self._config = config

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
        if not isinstance(other, AddDeviceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
