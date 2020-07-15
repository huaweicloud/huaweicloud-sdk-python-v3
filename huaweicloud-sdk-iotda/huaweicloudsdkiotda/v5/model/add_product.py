# coding: utf-8

import pprint
import re

import six





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
        'manufacturer_name': 'str',
        'industry': 'str',
        'description': 'str',
        'service_capabilities': 'list[ServiceCapability]',
        'app_id': 'str'
    }

    attribute_map = {
        'product_id': 'product_id',
        'name': 'name',
        'device_type': 'device_type',
        'protocol_type': 'protocol_type',
        'data_format': 'data_format',
        'manufacturer_name': 'manufacturer_name',
        'industry': 'industry',
        'description': 'description',
        'service_capabilities': 'service_capabilities',
        'app_id': 'app_id'
    }

    def __init__(self, product_id=None, name=None, device_type=None, protocol_type=None, data_format=None, manufacturer_name=None, industry=None, description=None, service_capabilities=None, app_id=None):
        """AddProduct - a model defined in huaweicloud sdk"""
        
        

        self._product_id = None
        self._name = None
        self._device_type = None
        self._protocol_type = None
        self._data_format = None
        self._manufacturer_name = None
        self._industry = None
        self._description = None
        self._service_capabilities = None
        self._app_id = None
        self.discriminator = None

        if product_id is not None:
            self.product_id = product_id
        self.name = name
        self.device_type = device_type
        self.protocol_type = protocol_type
        self.data_format = data_format
        if manufacturer_name is not None:
            self.manufacturer_name = manufacturer_name
        if industry is not None:
            self.industry = industry
        if description is not None:
            self.description = description
        self.service_capabilities = service_capabilities
        if app_id is not None:
            self.app_id = app_id

    @property
    def product_id(self):
        """Gets the product_id of this AddProduct.

        产品ID，用于唯一标识一个产品。如果携带此参数，平台将产品ID设置为该参数值；如果不携带此参数，产品ID在物联网平台创建产品后由平台分配获得。

        :return: The product_id of this AddProduct.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this AddProduct.

        产品ID，用于唯一标识一个产品。如果携带此参数，平台将产品ID设置为该参数值；如果不携带此参数，产品ID在物联网平台创建产品后由平台分配获得。

        :param product_id: The product_id of this AddProduct.
        :type: str
        """
        self._product_id = product_id

    @property
    def name(self):
        """Gets the name of this AddProduct.

        产品名称。

        :return: The name of this AddProduct.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddProduct.

        产品名称。

        :param name: The name of this AddProduct.
        :type: str
        """
        self._name = name

    @property
    def device_type(self):
        """Gets the device_type of this AddProduct.

        设备类型。

        :return: The device_type of this AddProduct.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this AddProduct.

        设备类型。

        :param device_type: The device_type of this AddProduct.
        :type: str
        """
        self._device_type = device_type

    @property
    def protocol_type(self):
        """Gets the protocol_type of this AddProduct.

        设备使用的协议类型。取值范围：MQTT，CoAP，HTTP，HTTPS，Modbus，ONVIF。

        :return: The protocol_type of this AddProduct.
        :rtype: str
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        """Sets the protocol_type of this AddProduct.

        设备使用的协议类型。取值范围：MQTT，CoAP，HTTP，HTTPS，Modbus，ONVIF。

        :param protocol_type: The protocol_type of this AddProduct.
        :type: str
        """
        self._protocol_type = protocol_type

    @property
    def data_format(self):
        """Gets the data_format of this AddProduct.

        设备上报数据的格式，取值范围：json，binary。

        :return: The data_format of this AddProduct.
        :rtype: str
        """
        return self._data_format

    @data_format.setter
    def data_format(self, data_format):
        """Sets the data_format of this AddProduct.

        设备上报数据的格式，取值范围：json，binary。

        :param data_format: The data_format of this AddProduct.
        :type: str
        """
        self._data_format = data_format

    @property
    def manufacturer_name(self):
        """Gets the manufacturer_name of this AddProduct.

        厂商名称。

        :return: The manufacturer_name of this AddProduct.
        :rtype: str
        """
        return self._manufacturer_name

    @manufacturer_name.setter
    def manufacturer_name(self, manufacturer_name):
        """Sets the manufacturer_name of this AddProduct.

        厂商名称。

        :param manufacturer_name: The manufacturer_name of this AddProduct.
        :type: str
        """
        self._manufacturer_name = manufacturer_name

    @property
    def industry(self):
        """Gets the industry of this AddProduct.

        设备所属行业。

        :return: The industry of this AddProduct.
        :rtype: str
        """
        return self._industry

    @industry.setter
    def industry(self, industry):
        """Sets the industry of this AddProduct.

        设备所属行业。

        :param industry: The industry of this AddProduct.
        :type: str
        """
        self._industry = industry

    @property
    def description(self):
        """Gets the description of this AddProduct.

        产品的描述信息。

        :return: The description of this AddProduct.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddProduct.

        产品的描述信息。

        :param description: The description of this AddProduct.
        :type: str
        """
        self._description = description

    @property
    def service_capabilities(self):
        """Gets the service_capabilities of this AddProduct.

        设备的服务能力列表。

        :return: The service_capabilities of this AddProduct.
        :rtype: list[ServiceCapability]
        """
        return self._service_capabilities

    @service_capabilities.setter
    def service_capabilities(self, service_capabilities):
        """Sets the service_capabilities of this AddProduct.

        设备的服务能力列表。

        :param service_capabilities: The service_capabilities of this AddProduct.
        :type: list[ServiceCapability]
        """
        self._service_capabilities = service_capabilities

    @property
    def app_id(self):
        """Gets the app_id of this AddProduct.

        资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的产品归属到哪个资源空间下，否则创建的产品将会归属到[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)下。

        :return: The app_id of this AddProduct.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this AddProduct.

        资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的产品归属到哪个资源空间下，否则创建的产品将会归属到[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)下。

        :param app_id: The app_id of this AddProduct.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AddProduct):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
