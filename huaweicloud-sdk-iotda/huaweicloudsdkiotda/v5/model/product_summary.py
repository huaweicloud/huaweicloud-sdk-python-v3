# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductSummary:

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
        'product_id': 'str',
        'name': 'str',
        'device_type': 'str',
        'protocol_type': 'str',
        'data_format': 'str',
        'manufacturer_name': 'str',
        'industry': 'str',
        'description': 'str',
        'create_time': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'app_name': 'app_name',
        'product_id': 'product_id',
        'name': 'name',
        'device_type': 'device_type',
        'protocol_type': 'protocol_type',
        'data_format': 'data_format',
        'manufacturer_name': 'manufacturer_name',
        'industry': 'industry',
        'description': 'description',
        'create_time': 'create_time'
    }

    def __init__(self, app_id=None, app_name=None, product_id=None, name=None, device_type=None, protocol_type=None, data_format=None, manufacturer_name=None, industry=None, description=None, create_time=None):
        """ProductSummary

        The model defined in huaweicloud sdk

        :param app_id: 资源空间ID。
        :type app_id: str
        :param app_name: 资源空间名称。
        :type app_name: str
        :param product_id: 产品ID，用于唯一标识一个产品，在物联网平台创建产品后由平台分配获得。
        :type product_id: str
        :param name: 产品名称。
        :type name: str
        :param device_type: 设备类型。
        :type device_type: str
        :param protocol_type: 设备使用的协议类型。取值范围：MQTT，CoAP，HTTP，HTTPS，Modbus，ONVIF， OPC-UA，OPC-DA，Other。
        :type protocol_type: str
        :param data_format: 设备上报数据的格式，取值范围：json，binary。
        :type data_format: str
        :param manufacturer_name: 厂商名称。
        :type manufacturer_name: str
        :param industry: 设备所属行业。
        :type industry: str
        :param description: 产品的描述信息。
        :type description: str
        :param create_time: 在物联网平台创建产品的时间，格式：yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;，如20151212T121212Z。
        :type create_time: str
        """
        
        

        self._app_id = None
        self._app_name = None
        self._product_id = None
        self._name = None
        self._device_type = None
        self._protocol_type = None
        self._data_format = None
        self._manufacturer_name = None
        self._industry = None
        self._description = None
        self._create_time = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if app_name is not None:
            self.app_name = app_name
        if product_id is not None:
            self.product_id = product_id
        if name is not None:
            self.name = name
        if device_type is not None:
            self.device_type = device_type
        if protocol_type is not None:
            self.protocol_type = protocol_type
        if data_format is not None:
            self.data_format = data_format
        if manufacturer_name is not None:
            self.manufacturer_name = manufacturer_name
        if industry is not None:
            self.industry = industry
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time

    @property
    def app_id(self):
        """Gets the app_id of this ProductSummary.

        资源空间ID。

        :return: The app_id of this ProductSummary.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ProductSummary.

        资源空间ID。

        :param app_id: The app_id of this ProductSummary.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_name(self):
        """Gets the app_name of this ProductSummary.

        资源空间名称。

        :return: The app_name of this ProductSummary.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ProductSummary.

        资源空间名称。

        :param app_name: The app_name of this ProductSummary.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def product_id(self):
        """Gets the product_id of this ProductSummary.

        产品ID，用于唯一标识一个产品，在物联网平台创建产品后由平台分配获得。

        :return: The product_id of this ProductSummary.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ProductSummary.

        产品ID，用于唯一标识一个产品，在物联网平台创建产品后由平台分配获得。

        :param product_id: The product_id of this ProductSummary.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def name(self):
        """Gets the name of this ProductSummary.

        产品名称。

        :return: The name of this ProductSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductSummary.

        产品名称。

        :param name: The name of this ProductSummary.
        :type name: str
        """
        self._name = name

    @property
    def device_type(self):
        """Gets the device_type of this ProductSummary.

        设备类型。

        :return: The device_type of this ProductSummary.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this ProductSummary.

        设备类型。

        :param device_type: The device_type of this ProductSummary.
        :type device_type: str
        """
        self._device_type = device_type

    @property
    def protocol_type(self):
        """Gets the protocol_type of this ProductSummary.

        设备使用的协议类型。取值范围：MQTT，CoAP，HTTP，HTTPS，Modbus，ONVIF， OPC-UA，OPC-DA，Other。

        :return: The protocol_type of this ProductSummary.
        :rtype: str
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        """Sets the protocol_type of this ProductSummary.

        设备使用的协议类型。取值范围：MQTT，CoAP，HTTP，HTTPS，Modbus，ONVIF， OPC-UA，OPC-DA，Other。

        :param protocol_type: The protocol_type of this ProductSummary.
        :type protocol_type: str
        """
        self._protocol_type = protocol_type

    @property
    def data_format(self):
        """Gets the data_format of this ProductSummary.

        设备上报数据的格式，取值范围：json，binary。

        :return: The data_format of this ProductSummary.
        :rtype: str
        """
        return self._data_format

    @data_format.setter
    def data_format(self, data_format):
        """Sets the data_format of this ProductSummary.

        设备上报数据的格式，取值范围：json，binary。

        :param data_format: The data_format of this ProductSummary.
        :type data_format: str
        """
        self._data_format = data_format

    @property
    def manufacturer_name(self):
        """Gets the manufacturer_name of this ProductSummary.

        厂商名称。

        :return: The manufacturer_name of this ProductSummary.
        :rtype: str
        """
        return self._manufacturer_name

    @manufacturer_name.setter
    def manufacturer_name(self, manufacturer_name):
        """Sets the manufacturer_name of this ProductSummary.

        厂商名称。

        :param manufacturer_name: The manufacturer_name of this ProductSummary.
        :type manufacturer_name: str
        """
        self._manufacturer_name = manufacturer_name

    @property
    def industry(self):
        """Gets the industry of this ProductSummary.

        设备所属行业。

        :return: The industry of this ProductSummary.
        :rtype: str
        """
        return self._industry

    @industry.setter
    def industry(self, industry):
        """Sets the industry of this ProductSummary.

        设备所属行业。

        :param industry: The industry of this ProductSummary.
        :type industry: str
        """
        self._industry = industry

    @property
    def description(self):
        """Gets the description of this ProductSummary.

        产品的描述信息。

        :return: The description of this ProductSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProductSummary.

        产品的描述信息。

        :param description: The description of this ProductSummary.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        """Gets the create_time of this ProductSummary.

        在物联网平台创建产品的时间，格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :return: The create_time of this ProductSummary.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ProductSummary.

        在物联网平台创建产品的时间，格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :param create_time: The create_time of this ProductSummary.
        :type create_time: str
        """
        self._create_time = create_time

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
        if not isinstance(other, ProductSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
