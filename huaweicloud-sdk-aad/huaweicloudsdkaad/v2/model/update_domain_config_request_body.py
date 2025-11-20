# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDomainConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'real_server_type': 'int',
        'real_server': 'str',
        'port_http': 'list[int]',
        'port_https': 'list[int]',
        'overseas_type': 'str',
        'cert_name': 'str'
    }

    attribute_map = {
        'real_server_type': 'real_server_type',
        'real_server': 'real_server',
        'port_http': 'port_http',
        'port_https': 'port_https',
        'overseas_type': 'overseas_type',
        'cert_name': 'cert_name'
    }

    def __init__(self, real_server_type=None, real_server=None, port_http=None, port_https=None, overseas_type=None, cert_name=None):
        r"""UpdateDomainConfigRequestBody

        The model defined in huaweicloud sdk

        :param real_server_type: 源站类型。 0 - 源站IP， 1 - 源站域名。
        :type real_server_type: int
        :param real_server: 源站ip/源站域名
        :type real_server: str
        :param port_http: HTTP端口，与port_https不能同时为空。DDoS高防支持的HTTP端口可用ListDomainPort接口查询。
        :type port_http: list[int]
        :param port_https: HTTPS端口，与port_http不能同时为空。DDoS高防支持的HTTPS端口可用ListDomainPort接口查询。
        :type port_https: list[int]
        :param overseas_type: 防护区域：0-中国大陆、1-中国大陆外
        :type overseas_type: str
        :param cert_name: 证书名称
        :type cert_name: str
        """
        
        

        self._real_server_type = None
        self._real_server = None
        self._port_http = None
        self._port_https = None
        self._overseas_type = None
        self._cert_name = None
        self.discriminator = None

        self.real_server_type = real_server_type
        self.real_server = real_server
        if port_http is not None:
            self.port_http = port_http
        if port_https is not None:
            self.port_https = port_https
        if overseas_type is not None:
            self.overseas_type = overseas_type
        if cert_name is not None:
            self.cert_name = cert_name

    @property
    def real_server_type(self):
        r"""Gets the real_server_type of this UpdateDomainConfigRequestBody.

        源站类型。 0 - 源站IP， 1 - 源站域名。

        :return: The real_server_type of this UpdateDomainConfigRequestBody.
        :rtype: int
        """
        return self._real_server_type

    @real_server_type.setter
    def real_server_type(self, real_server_type):
        r"""Sets the real_server_type of this UpdateDomainConfigRequestBody.

        源站类型。 0 - 源站IP， 1 - 源站域名。

        :param real_server_type: The real_server_type of this UpdateDomainConfigRequestBody.
        :type real_server_type: int
        """
        self._real_server_type = real_server_type

    @property
    def real_server(self):
        r"""Gets the real_server of this UpdateDomainConfigRequestBody.

        源站ip/源站域名

        :return: The real_server of this UpdateDomainConfigRequestBody.
        :rtype: str
        """
        return self._real_server

    @real_server.setter
    def real_server(self, real_server):
        r"""Sets the real_server of this UpdateDomainConfigRequestBody.

        源站ip/源站域名

        :param real_server: The real_server of this UpdateDomainConfigRequestBody.
        :type real_server: str
        """
        self._real_server = real_server

    @property
    def port_http(self):
        r"""Gets the port_http of this UpdateDomainConfigRequestBody.

        HTTP端口，与port_https不能同时为空。DDoS高防支持的HTTP端口可用ListDomainPort接口查询。

        :return: The port_http of this UpdateDomainConfigRequestBody.
        :rtype: list[int]
        """
        return self._port_http

    @port_http.setter
    def port_http(self, port_http):
        r"""Sets the port_http of this UpdateDomainConfigRequestBody.

        HTTP端口，与port_https不能同时为空。DDoS高防支持的HTTP端口可用ListDomainPort接口查询。

        :param port_http: The port_http of this UpdateDomainConfigRequestBody.
        :type port_http: list[int]
        """
        self._port_http = port_http

    @property
    def port_https(self):
        r"""Gets the port_https of this UpdateDomainConfigRequestBody.

        HTTPS端口，与port_http不能同时为空。DDoS高防支持的HTTPS端口可用ListDomainPort接口查询。

        :return: The port_https of this UpdateDomainConfigRequestBody.
        :rtype: list[int]
        """
        return self._port_https

    @port_https.setter
    def port_https(self, port_https):
        r"""Sets the port_https of this UpdateDomainConfigRequestBody.

        HTTPS端口，与port_http不能同时为空。DDoS高防支持的HTTPS端口可用ListDomainPort接口查询。

        :param port_https: The port_https of this UpdateDomainConfigRequestBody.
        :type port_https: list[int]
        """
        self._port_https = port_https

    @property
    def overseas_type(self):
        r"""Gets the overseas_type of this UpdateDomainConfigRequestBody.

        防护区域：0-中国大陆、1-中国大陆外

        :return: The overseas_type of this UpdateDomainConfigRequestBody.
        :rtype: str
        """
        return self._overseas_type

    @overseas_type.setter
    def overseas_type(self, overseas_type):
        r"""Sets the overseas_type of this UpdateDomainConfigRequestBody.

        防护区域：0-中国大陆、1-中国大陆外

        :param overseas_type: The overseas_type of this UpdateDomainConfigRequestBody.
        :type overseas_type: str
        """
        self._overseas_type = overseas_type

    @property
    def cert_name(self):
        r"""Gets the cert_name of this UpdateDomainConfigRequestBody.

        证书名称

        :return: The cert_name of this UpdateDomainConfigRequestBody.
        :rtype: str
        """
        return self._cert_name

    @cert_name.setter
    def cert_name(self, cert_name):
        r"""Sets the cert_name of this UpdateDomainConfigRequestBody.

        证书名称

        :param cert_name: The cert_name of this UpdateDomainConfigRequestBody.
        :type cert_name: str
        """
        self._cert_name = cert_name

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateDomainConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
