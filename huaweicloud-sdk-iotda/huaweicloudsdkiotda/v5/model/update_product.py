# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateProduct:

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
        'name': 'str',
        'device_type': 'str',
        'protocol_type': 'str',
        'data_format': 'str',
        'service_capabilities': 'list[ServiceCapability]',
        'manufacturer_name': 'str',
        'industry': 'str',
        'description': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'name': 'name',
        'device_type': 'device_type',
        'protocol_type': 'protocol_type',
        'data_format': 'data_format',
        'service_capabilities': 'service_capabilities',
        'manufacturer_name': 'manufacturer_name',
        'industry': 'industry',
        'description': 'description'
    }

    def __init__(self, app_id=None, name=None, device_type=None, protocol_type=None, data_format=None, service_capabilities=None, manufacturer_name=None, industry=None, description=None):
        r"""UpdateProduct

        The model defined in huaweicloud sdk

        :param app_id: **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数，指定要修改的产品属于哪个资源空间；若不携带，则优先修改默认资源空间下产品，如默认资源空间下无对应产品，则按照产品创建时间修改最早创建产品。如果用户存在多资源空间，同时又不想携带该参数，可以联系华为技术支持对用户数据做资源空间合并。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type app_id: str
        :param name: **参数说明**：产品名称。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合。
        :type name: str
        :param device_type: **参数说明**：设备类型。 **取值范围**：长度不超过32，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合。
        :type device_type: str
        :param protocol_type: **参数说明**：设备使用的协议类型。注：禁止其他协议类型修改为CoAP。 **取值范围**：MQTT，CoAP，HTTP，HTTPS，Modbus，ONVIF，OPC-UA，OPC-DA，Other，TCP，UDP。
        :type protocol_type: str
        :param data_format: **参数说明**：设备上报数据的格式。 **取值范围**： - json：JSON格式 - binary：二进制码流格式
        :type data_format: str
        :param service_capabilities: **参数说明**：设备的服务能力列表。
        :type service_capabilities: list[:class:`huaweicloudsdkiotda.v5.ServiceCapability`]
        :param manufacturer_name: **参数说明**：厂商名称。 **取值范围**：长度不超过32，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合。
        :type manufacturer_name: str
        :param industry: **参数说明**：设备所属行业。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合。
        :type industry: str
        :param description: **参数说明**：产品的描述信息。 **取值范围**：长度不超过128，只允许中文、字母、数字、空白字符、以及_?&#39;#().,;&amp;%@!- ，、：；。/等字符的组合。
        :type description: str
        """
        
        

        self._app_id = None
        self._name = None
        self._device_type = None
        self._protocol_type = None
        self._data_format = None
        self._service_capabilities = None
        self._manufacturer_name = None
        self._industry = None
        self._description = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if name is not None:
            self.name = name
        if device_type is not None:
            self.device_type = device_type
        if protocol_type is not None:
            self.protocol_type = protocol_type
        if data_format is not None:
            self.data_format = data_format
        if service_capabilities is not None:
            self.service_capabilities = service_capabilities
        if manufacturer_name is not None:
            self.manufacturer_name = manufacturer_name
        if industry is not None:
            self.industry = industry
        if description is not None:
            self.description = description

    @property
    def app_id(self):
        r"""Gets the app_id of this UpdateProduct.

        **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数，指定要修改的产品属于哪个资源空间；若不携带，则优先修改默认资源空间下产品，如默认资源空间下无对应产品，则按照产品创建时间修改最早创建产品。如果用户存在多资源空间，同时又不想携带该参数，可以联系华为技术支持对用户数据做资源空间合并。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The app_id of this UpdateProduct.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this UpdateProduct.

        **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数，指定要修改的产品属于哪个资源空间；若不携带，则优先修改默认资源空间下产品，如默认资源空间下无对应产品，则按照产品创建时间修改最早创建产品。如果用户存在多资源空间，同时又不想携带该参数，可以联系华为技术支持对用户数据做资源空间合并。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param app_id: The app_id of this UpdateProduct.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def name(self):
        r"""Gets the name of this UpdateProduct.

        **参数说明**：产品名称。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :return: The name of this UpdateProduct.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateProduct.

        **参数说明**：产品名称。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :param name: The name of this UpdateProduct.
        :type name: str
        """
        self._name = name

    @property
    def device_type(self):
        r"""Gets the device_type of this UpdateProduct.

        **参数说明**：设备类型。 **取值范围**：长度不超过32，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :return: The device_type of this UpdateProduct.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        r"""Sets the device_type of this UpdateProduct.

        **参数说明**：设备类型。 **取值范围**：长度不超过32，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :param device_type: The device_type of this UpdateProduct.
        :type device_type: str
        """
        self._device_type = device_type

    @property
    def protocol_type(self):
        r"""Gets the protocol_type of this UpdateProduct.

        **参数说明**：设备使用的协议类型。注：禁止其他协议类型修改为CoAP。 **取值范围**：MQTT，CoAP，HTTP，HTTPS，Modbus，ONVIF，OPC-UA，OPC-DA，Other，TCP，UDP。

        :return: The protocol_type of this UpdateProduct.
        :rtype: str
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        r"""Sets the protocol_type of this UpdateProduct.

        **参数说明**：设备使用的协议类型。注：禁止其他协议类型修改为CoAP。 **取值范围**：MQTT，CoAP，HTTP，HTTPS，Modbus，ONVIF，OPC-UA，OPC-DA，Other，TCP，UDP。

        :param protocol_type: The protocol_type of this UpdateProduct.
        :type protocol_type: str
        """
        self._protocol_type = protocol_type

    @property
    def data_format(self):
        r"""Gets the data_format of this UpdateProduct.

        **参数说明**：设备上报数据的格式。 **取值范围**： - json：JSON格式 - binary：二进制码流格式

        :return: The data_format of this UpdateProduct.
        :rtype: str
        """
        return self._data_format

    @data_format.setter
    def data_format(self, data_format):
        r"""Sets the data_format of this UpdateProduct.

        **参数说明**：设备上报数据的格式。 **取值范围**： - json：JSON格式 - binary：二进制码流格式

        :param data_format: The data_format of this UpdateProduct.
        :type data_format: str
        """
        self._data_format = data_format

    @property
    def service_capabilities(self):
        r"""Gets the service_capabilities of this UpdateProduct.

        **参数说明**：设备的服务能力列表。

        :return: The service_capabilities of this UpdateProduct.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.ServiceCapability`]
        """
        return self._service_capabilities

    @service_capabilities.setter
    def service_capabilities(self, service_capabilities):
        r"""Sets the service_capabilities of this UpdateProduct.

        **参数说明**：设备的服务能力列表。

        :param service_capabilities: The service_capabilities of this UpdateProduct.
        :type service_capabilities: list[:class:`huaweicloudsdkiotda.v5.ServiceCapability`]
        """
        self._service_capabilities = service_capabilities

    @property
    def manufacturer_name(self):
        r"""Gets the manufacturer_name of this UpdateProduct.

        **参数说明**：厂商名称。 **取值范围**：长度不超过32，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :return: The manufacturer_name of this UpdateProduct.
        :rtype: str
        """
        return self._manufacturer_name

    @manufacturer_name.setter
    def manufacturer_name(self, manufacturer_name):
        r"""Sets the manufacturer_name of this UpdateProduct.

        **参数说明**：厂商名称。 **取值范围**：长度不超过32，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :param manufacturer_name: The manufacturer_name of this UpdateProduct.
        :type manufacturer_name: str
        """
        self._manufacturer_name = manufacturer_name

    @property
    def industry(self):
        r"""Gets the industry of this UpdateProduct.

        **参数说明**：设备所属行业。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :return: The industry of this UpdateProduct.
        :rtype: str
        """
        return self._industry

    @industry.setter
    def industry(self, industry):
        r"""Sets the industry of this UpdateProduct.

        **参数说明**：设备所属行业。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :param industry: The industry of this UpdateProduct.
        :type industry: str
        """
        self._industry = industry

    @property
    def description(self):
        r"""Gets the description of this UpdateProduct.

        **参数说明**：产品的描述信息。 **取值范围**：长度不超过128，只允许中文、字母、数字、空白字符、以及_?'#().,;&%@!- ，、：；。/等字符的组合。

        :return: The description of this UpdateProduct.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateProduct.

        **参数说明**：产品的描述信息。 **取值范围**：长度不超过128，只允许中文、字母、数字、空白字符、以及_?'#().,;&%@!- ，、：；。/等字符的组合。

        :param description: The description of this UpdateProduct.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, UpdateProduct):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
