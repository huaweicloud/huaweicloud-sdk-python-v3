# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'port': 'int',
        'non_tls_port': 'int',
        'websocket_port': 'int',
        'domain_name': 'str',
        'private_addresses': 'list[str]',
        'public_address': 'list[str]',
        'ipv6_address': 'list[str]',
        'ip_whitelist': 'IPWhiteList'
    }

    attribute_map = {
        'type': 'type',
        'port': 'port',
        'non_tls_port': 'non_tls_port',
        'websocket_port': 'websocket_port',
        'domain_name': 'domain_name',
        'private_addresses': 'private_addresses',
        'public_address': 'public_address',
        'ipv6_address': 'ipv6_address',
        'ip_whitelist': 'ip_whitelist'
    }

    def __init__(self, type=None, port=None, non_tls_port=None, websocket_port=None, domain_name=None, private_addresses=None, public_address=None, ipv6_address=None, ip_whitelist=None):
        r"""AccessInfo

        The model defined in huaweicloud sdk

        :param type: **参数说明**：接入地址的类型，如应用接入的HTTPS协议的取值为：APP_HTTPS，设备接入的MQTT协议的取值为：DEVICE_MQTT **取值范围**： - APP_HTTPS：应用接入HTTPS协议 - APP_AMQP：应用接入AMQP协议 - APP_MQTT：应用接入MQTT协议 - DEVICE_COAP：设备接入COAP协议 - DEVICE_MQTT：设备接入MQTT协议 - DEVICE_HTTPS：设备接入HTTPS协议 
        :type type: str
        :param port: **参数说明**：实例的应用/设备的安全接入端口 
        :type port: int
        :param non_tls_port: **参数说明**：实例的应用/设备的非安全接入端口。返回null时表示该类型的接入地址不支持非安全端口接入。 
        :type non_tls_port: int
        :param websocket_port: **参数说明**：基于WebSocket的MQTT接入端口。返回null时表示该类型的接入地址不支持WebSocket端口接入。 
        :type websocket_port: int
        :param domain_name: **参数说明**：实例的接入域名 
        :type domain_name: str
        :param private_addresses: **参数说明**：实例的私网接入地址列表 
        :type private_addresses: list[str]
        :param public_address: **参数说明**：实例的公网接入地址 
        :type public_address: list[str]
        :param ipv6_address: **参数说明**：实例的ipv6接入地址列表 
        :type ipv6_address: list[str]
        :param ip_whitelist: 
        :type ip_whitelist: :class:`huaweicloudsdkiotdm.v5.IPWhiteList`
        """
        
        

        self._type = None
        self._port = None
        self._non_tls_port = None
        self._websocket_port = None
        self._domain_name = None
        self._private_addresses = None
        self._public_address = None
        self._ipv6_address = None
        self._ip_whitelist = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if port is not None:
            self.port = port
        if non_tls_port is not None:
            self.non_tls_port = non_tls_port
        if websocket_port is not None:
            self.websocket_port = websocket_port
        if domain_name is not None:
            self.domain_name = domain_name
        if private_addresses is not None:
            self.private_addresses = private_addresses
        if public_address is not None:
            self.public_address = public_address
        if ipv6_address is not None:
            self.ipv6_address = ipv6_address
        if ip_whitelist is not None:
            self.ip_whitelist = ip_whitelist

    @property
    def type(self):
        r"""Gets the type of this AccessInfo.

        **参数说明**：接入地址的类型，如应用接入的HTTPS协议的取值为：APP_HTTPS，设备接入的MQTT协议的取值为：DEVICE_MQTT **取值范围**： - APP_HTTPS：应用接入HTTPS协议 - APP_AMQP：应用接入AMQP协议 - APP_MQTT：应用接入MQTT协议 - DEVICE_COAP：设备接入COAP协议 - DEVICE_MQTT：设备接入MQTT协议 - DEVICE_HTTPS：设备接入HTTPS协议 

        :return: The type of this AccessInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AccessInfo.

        **参数说明**：接入地址的类型，如应用接入的HTTPS协议的取值为：APP_HTTPS，设备接入的MQTT协议的取值为：DEVICE_MQTT **取值范围**： - APP_HTTPS：应用接入HTTPS协议 - APP_AMQP：应用接入AMQP协议 - APP_MQTT：应用接入MQTT协议 - DEVICE_COAP：设备接入COAP协议 - DEVICE_MQTT：设备接入MQTT协议 - DEVICE_HTTPS：设备接入HTTPS协议 

        :param type: The type of this AccessInfo.
        :type type: str
        """
        self._type = type

    @property
    def port(self):
        r"""Gets the port of this AccessInfo.

        **参数说明**：实例的应用/设备的安全接入端口 

        :return: The port of this AccessInfo.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this AccessInfo.

        **参数说明**：实例的应用/设备的安全接入端口 

        :param port: The port of this AccessInfo.
        :type port: int
        """
        self._port = port

    @property
    def non_tls_port(self):
        r"""Gets the non_tls_port of this AccessInfo.

        **参数说明**：实例的应用/设备的非安全接入端口。返回null时表示该类型的接入地址不支持非安全端口接入。 

        :return: The non_tls_port of this AccessInfo.
        :rtype: int
        """
        return self._non_tls_port

    @non_tls_port.setter
    def non_tls_port(self, non_tls_port):
        r"""Sets the non_tls_port of this AccessInfo.

        **参数说明**：实例的应用/设备的非安全接入端口。返回null时表示该类型的接入地址不支持非安全端口接入。 

        :param non_tls_port: The non_tls_port of this AccessInfo.
        :type non_tls_port: int
        """
        self._non_tls_port = non_tls_port

    @property
    def websocket_port(self):
        r"""Gets the websocket_port of this AccessInfo.

        **参数说明**：基于WebSocket的MQTT接入端口。返回null时表示该类型的接入地址不支持WebSocket端口接入。 

        :return: The websocket_port of this AccessInfo.
        :rtype: int
        """
        return self._websocket_port

    @websocket_port.setter
    def websocket_port(self, websocket_port):
        r"""Sets the websocket_port of this AccessInfo.

        **参数说明**：基于WebSocket的MQTT接入端口。返回null时表示该类型的接入地址不支持WebSocket端口接入。 

        :param websocket_port: The websocket_port of this AccessInfo.
        :type websocket_port: int
        """
        self._websocket_port = websocket_port

    @property
    def domain_name(self):
        r"""Gets the domain_name of this AccessInfo.

        **参数说明**：实例的接入域名 

        :return: The domain_name of this AccessInfo.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this AccessInfo.

        **参数说明**：实例的接入域名 

        :param domain_name: The domain_name of this AccessInfo.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def private_addresses(self):
        r"""Gets the private_addresses of this AccessInfo.

        **参数说明**：实例的私网接入地址列表 

        :return: The private_addresses of this AccessInfo.
        :rtype: list[str]
        """
        return self._private_addresses

    @private_addresses.setter
    def private_addresses(self, private_addresses):
        r"""Sets the private_addresses of this AccessInfo.

        **参数说明**：实例的私网接入地址列表 

        :param private_addresses: The private_addresses of this AccessInfo.
        :type private_addresses: list[str]
        """
        self._private_addresses = private_addresses

    @property
    def public_address(self):
        r"""Gets the public_address of this AccessInfo.

        **参数说明**：实例的公网接入地址 

        :return: The public_address of this AccessInfo.
        :rtype: list[str]
        """
        return self._public_address

    @public_address.setter
    def public_address(self, public_address):
        r"""Sets the public_address of this AccessInfo.

        **参数说明**：实例的公网接入地址 

        :param public_address: The public_address of this AccessInfo.
        :type public_address: list[str]
        """
        self._public_address = public_address

    @property
    def ipv6_address(self):
        r"""Gets the ipv6_address of this AccessInfo.

        **参数说明**：实例的ipv6接入地址列表 

        :return: The ipv6_address of this AccessInfo.
        :rtype: list[str]
        """
        return self._ipv6_address

    @ipv6_address.setter
    def ipv6_address(self, ipv6_address):
        r"""Sets the ipv6_address of this AccessInfo.

        **参数说明**：实例的ipv6接入地址列表 

        :param ipv6_address: The ipv6_address of this AccessInfo.
        :type ipv6_address: list[str]
        """
        self._ipv6_address = ipv6_address

    @property
    def ip_whitelist(self):
        r"""Gets the ip_whitelist of this AccessInfo.

        :return: The ip_whitelist of this AccessInfo.
        :rtype: :class:`huaweicloudsdkiotdm.v5.IPWhiteList`
        """
        return self._ip_whitelist

    @ip_whitelist.setter
    def ip_whitelist(self, ip_whitelist):
        r"""Sets the ip_whitelist of this AccessInfo.

        :param ip_whitelist: The ip_whitelist of this AccessInfo.
        :type ip_whitelist: :class:`huaweicloudsdkiotdm.v5.IPWhiteList`
        """
        self._ip_whitelist = ip_whitelist

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
        if not isinstance(other, AccessInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
