# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddProduct:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'product_id': 'str',
        'name': 'str',
        'device_type': 'str',
        'protocol_type': 'str',
        'data_format': 'str',
        'service_capabilities': 'list[ServiceCapability]',
        'manufacturer_name': 'str',
        'industry': 'str',
        'description': 'str',
        'app_id': 'str'
    }

    attribute_map = {
        'product_id': 'product_id',
        'name': 'name',
        'device_type': 'device_type',
        'protocol_type': 'protocol_type',
        'data_format': 'data_format',
        'service_capabilities': 'service_capabilities',
        'manufacturer_name': 'manufacturer_name',
        'industry': 'industry',
        'description': 'description',
        'app_id': 'app_id'
    }

    def __init__(self, product_id=None, name=None, device_type=None, protocol_type=None, data_format=None, service_capabilities=None, manufacturer_name=None, industry=None, description=None, app_id=None):
        """AddProduct

        The model defined in huaweicloud sdk

        :param product_id: **参数说明**：产品ID，资源空间下唯一。常app_id一起使用，用于唯一标识一个产品。如果携带此参数，平台将产品ID设置为该参数值；如果不携带此参数，产品ID在物联网平台创建产品后由平台分配获得。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type product_id: str
        :param name: **参数说明**：产品名称。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合。
        :type name: str
        :param device_type: **参数说明**：设备类型。 **取值范围**：长度不超过32，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合。
        :type device_type: str
        :param protocol_type: **参数说明**：设备使用的协议类型。 **取值范围**：MQTT，CoAP，HTTP，HTTPS，Modbus，ONVIF，OPC-UA，OPC-DA，Other。
        :type protocol_type: str
        :param data_format: **参数说明**：设备上报数据的格式。 **取值范围**： - json：JSON格式 - binary：二进制码流格式 默认值json。
        :type data_format: str
        :param service_capabilities: **参数说明**：设备的服务能力列表。 **取值范围**：数组长度大小不超过500，内容大小不超过500k。
        :type service_capabilities: list[:class:`huaweicloudsdkiotda.v5.ServiceCapability`]
        :param manufacturer_name: **参数说明**：厂商名称。 **取值范围**：长度不超过32，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合。
        :type manufacturer_name: str
        :param industry: **参数说明**：设备所属行业。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合。
        :type industry: str
        :param description: **参数说明**：产品的描述信息。 **取值范围**：长度不超过128，只允许中文、字母、数字、空白字符、以及_?&#39;#().,;&amp;%@!- ，、：；。/等字符的组合。
        :type description: str
        :param app_id: **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的产品归属到哪个资源空间下，否则创建的产品将会归属到[[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)](tag:hws)[[默认资源空间](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0006.html#section0)](tag:hws_hk)下。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type app_id: str
        """
        
        

        self._product_id = None
        self._name = None
        self._device_type = None
        self._protocol_type = None
        self._data_format = None
        self._service_capabilities = None
        self._manufacturer_name = None
        self._industry = None
        self._description = None
        self._app_id = None
        self.discriminator = None

        if product_id is not None:
            self.product_id = product_id
        self.name = name
        self.device_type = device_type
        self.protocol_type = protocol_type
        self.data_format = data_format
        self.service_capabilities = service_capabilities
        if manufacturer_name is not None:
            self.manufacturer_name = manufacturer_name
        if industry is not None:
            self.industry = industry
        if description is not None:
            self.description = description
        if app_id is not None:
            self.app_id = app_id

    @property
    def product_id(self):
        """Gets the product_id of this AddProduct.

        **参数说明**：产品ID，资源空间下唯一。常app_id一起使用，用于唯一标识一个产品。如果携带此参数，平台将产品ID设置为该参数值；如果不携带此参数，产品ID在物联网平台创建产品后由平台分配获得。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The product_id of this AddProduct.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this AddProduct.

        **参数说明**：产品ID，资源空间下唯一。常app_id一起使用，用于唯一标识一个产品。如果携带此参数，平台将产品ID设置为该参数值；如果不携带此参数，产品ID在物联网平台创建产品后由平台分配获得。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param product_id: The product_id of this AddProduct.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def name(self):
        """Gets the name of this AddProduct.

        **参数说明**：产品名称。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :return: The name of this AddProduct.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddProduct.

        **参数说明**：产品名称。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :param name: The name of this AddProduct.
        :type name: str
        """
        self._name = name

    @property
    def device_type(self):
        """Gets the device_type of this AddProduct.

        **参数说明**：设备类型。 **取值范围**：长度不超过32，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :return: The device_type of this AddProduct.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this AddProduct.

        **参数说明**：设备类型。 **取值范围**：长度不超过32，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :param device_type: The device_type of this AddProduct.
        :type device_type: str
        """
        self._device_type = device_type

    @property
    def protocol_type(self):
        """Gets the protocol_type of this AddProduct.

        **参数说明**：设备使用的协议类型。 **取值范围**：MQTT，CoAP，HTTP，HTTPS，Modbus，ONVIF，OPC-UA，OPC-DA，Other。

        :return: The protocol_type of this AddProduct.
        :rtype: str
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        """Sets the protocol_type of this AddProduct.

        **参数说明**：设备使用的协议类型。 **取值范围**：MQTT，CoAP，HTTP，HTTPS，Modbus，ONVIF，OPC-UA，OPC-DA，Other。

        :param protocol_type: The protocol_type of this AddProduct.
        :type protocol_type: str
        """
        self._protocol_type = protocol_type

    @property
    def data_format(self):
        """Gets the data_format of this AddProduct.

        **参数说明**：设备上报数据的格式。 **取值范围**： - json：JSON格式 - binary：二进制码流格式 默认值json。

        :return: The data_format of this AddProduct.
        :rtype: str
        """
        return self._data_format

    @data_format.setter
    def data_format(self, data_format):
        """Sets the data_format of this AddProduct.

        **参数说明**：设备上报数据的格式。 **取值范围**： - json：JSON格式 - binary：二进制码流格式 默认值json。

        :param data_format: The data_format of this AddProduct.
        :type data_format: str
        """
        self._data_format = data_format

    @property
    def service_capabilities(self):
        """Gets the service_capabilities of this AddProduct.

        **参数说明**：设备的服务能力列表。 **取值范围**：数组长度大小不超过500，内容大小不超过500k。

        :return: The service_capabilities of this AddProduct.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.ServiceCapability`]
        """
        return self._service_capabilities

    @service_capabilities.setter
    def service_capabilities(self, service_capabilities):
        """Sets the service_capabilities of this AddProduct.

        **参数说明**：设备的服务能力列表。 **取值范围**：数组长度大小不超过500，内容大小不超过500k。

        :param service_capabilities: The service_capabilities of this AddProduct.
        :type service_capabilities: list[:class:`huaweicloudsdkiotda.v5.ServiceCapability`]
        """
        self._service_capabilities = service_capabilities

    @property
    def manufacturer_name(self):
        """Gets the manufacturer_name of this AddProduct.

        **参数说明**：厂商名称。 **取值范围**：长度不超过32，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :return: The manufacturer_name of this AddProduct.
        :rtype: str
        """
        return self._manufacturer_name

    @manufacturer_name.setter
    def manufacturer_name(self, manufacturer_name):
        """Sets the manufacturer_name of this AddProduct.

        **参数说明**：厂商名称。 **取值范围**：长度不超过32，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :param manufacturer_name: The manufacturer_name of this AddProduct.
        :type manufacturer_name: str
        """
        self._manufacturer_name = manufacturer_name

    @property
    def industry(self):
        """Gets the industry of this AddProduct.

        **参数说明**：设备所属行业。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :return: The industry of this AddProduct.
        :rtype: str
        """
        return self._industry

    @industry.setter
    def industry(self, industry):
        """Sets the industry of this AddProduct.

        **参数说明**：设备所属行业。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :param industry: The industry of this AddProduct.
        :type industry: str
        """
        self._industry = industry

    @property
    def description(self):
        """Gets the description of this AddProduct.

        **参数说明**：产品的描述信息。 **取值范围**：长度不超过128，只允许中文、字母、数字、空白字符、以及_?'#().,;&%@!- ，、：；。/等字符的组合。

        :return: The description of this AddProduct.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddProduct.

        **参数说明**：产品的描述信息。 **取值范围**：长度不超过128，只允许中文、字母、数字、空白字符、以及_?'#().,;&%@!- ，、：；。/等字符的组合。

        :param description: The description of this AddProduct.
        :type description: str
        """
        self._description = description

    @property
    def app_id(self):
        """Gets the app_id of this AddProduct.

        **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的产品归属到哪个资源空间下，否则创建的产品将会归属到[[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)](tag:hws)[[默认资源空间](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0006.html#section0)](tag:hws_hk)下。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The app_id of this AddProduct.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this AddProduct.

        **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的产品归属到哪个资源空间下，否则创建的产品将会归属到[[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)](tag:hws)[[默认资源空间](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0006.html#section0)](tag:hws_hk)下。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param app_id: The app_id of this AddProduct.
        :type app_id: str
        """
        self._app_id = app_id

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
        if not isinstance(other, AddProduct):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
