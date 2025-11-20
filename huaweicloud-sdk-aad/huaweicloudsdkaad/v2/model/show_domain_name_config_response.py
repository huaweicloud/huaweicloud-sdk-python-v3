# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainNameConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'domain_name': 'str',
        'real_server_type': 'int',
        'port_http': 'list[int]',
        'port_https': 'list[int]',
        'real_server': 'str',
        'pp_enable': 'int',
        'overseas_type': 'int',
        'tls': 'str',
        'cipher': 'str',
        'http2_enable': 'bool',
        'header_map': 'object'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'real_server_type': 'real_server_type',
        'port_http': 'port_http',
        'port_https': 'port_https',
        'real_server': 'real_server',
        'pp_enable': 'pp_enable',
        'overseas_type': 'overseas_type',
        'tls': 'tls',
        'cipher': 'cipher',
        'http2_enable': 'http2_enable',
        'header_map': 'header_map'
    }

    def __init__(self, domain_id=None, domain_name=None, real_server_type=None, port_http=None, port_https=None, real_server=None, pp_enable=None, overseas_type=None, tls=None, cipher=None, http2_enable=None, header_map=None):
        r"""ShowDomainNameConfigResponse

        The model defined in huaweicloud sdk

        :param domain_id: 域名id
        :type domain_id: str
        :param domain_name: 域名
        :type domain_name: str
        :param real_server_type: 源站类型，0 - 源站IP， 1 - 源站域名
        :type real_server_type: int
        :param port_http: HTTP端口，与port_https不能同时为空。DDoS高防支持的HTTP端口可在控制台查看。
        :type port_http: list[int]
        :param port_https: HTTPS端口，与port_http不能同时为空。DDoS高防支持的HTTPS端口可在控制台查看。
        :type port_https: list[int]
        :param real_server: 源站ip/源站域名
        :type real_server: str
        :param pp_enable: pp是否开启, 1-开启，0-关闭
        :type pp_enable: int
        :param overseas_type: 防护区域,0-大陆,1-海外
        :type overseas_type: int
        :param tls: tls(请求参数type&#x3D;waf时)
        :type tls: str
        :param cipher: 加密套件(请求参数type&#x3D;waf时)
        :type cipher: str
        :param http2_enable: 是否允许http2(请求参数type&#x3D;waf时)
        :type http2_enable: bool
        :param header_map: 字段转发(请求参数type&#x3D;waf时)
        :type header_map: object
        """
        
        super().__init__()

        self._domain_id = None
        self._domain_name = None
        self._real_server_type = None
        self._port_http = None
        self._port_https = None
        self._real_server = None
        self._pp_enable = None
        self._overseas_type = None
        self._tls = None
        self._cipher = None
        self._http2_enable = None
        self._header_map = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name
        if real_server_type is not None:
            self.real_server_type = real_server_type
        if port_http is not None:
            self.port_http = port_http
        if port_https is not None:
            self.port_https = port_https
        if real_server is not None:
            self.real_server = real_server
        if pp_enable is not None:
            self.pp_enable = pp_enable
        if overseas_type is not None:
            self.overseas_type = overseas_type
        if tls is not None:
            self.tls = tls
        if cipher is not None:
            self.cipher = cipher
        if http2_enable is not None:
            self.http2_enable = http2_enable
        if header_map is not None:
            self.header_map = header_map

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowDomainNameConfigResponse.

        域名id

        :return: The domain_id of this ShowDomainNameConfigResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowDomainNameConfigResponse.

        域名id

        :param domain_id: The domain_id of this ShowDomainNameConfigResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ShowDomainNameConfigResponse.

        域名

        :return: The domain_name of this ShowDomainNameConfigResponse.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ShowDomainNameConfigResponse.

        域名

        :param domain_name: The domain_name of this ShowDomainNameConfigResponse.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def real_server_type(self):
        r"""Gets the real_server_type of this ShowDomainNameConfigResponse.

        源站类型，0 - 源站IP， 1 - 源站域名

        :return: The real_server_type of this ShowDomainNameConfigResponse.
        :rtype: int
        """
        return self._real_server_type

    @real_server_type.setter
    def real_server_type(self, real_server_type):
        r"""Sets the real_server_type of this ShowDomainNameConfigResponse.

        源站类型，0 - 源站IP， 1 - 源站域名

        :param real_server_type: The real_server_type of this ShowDomainNameConfigResponse.
        :type real_server_type: int
        """
        self._real_server_type = real_server_type

    @property
    def port_http(self):
        r"""Gets the port_http of this ShowDomainNameConfigResponse.

        HTTP端口，与port_https不能同时为空。DDoS高防支持的HTTP端口可在控制台查看。

        :return: The port_http of this ShowDomainNameConfigResponse.
        :rtype: list[int]
        """
        return self._port_http

    @port_http.setter
    def port_http(self, port_http):
        r"""Sets the port_http of this ShowDomainNameConfigResponse.

        HTTP端口，与port_https不能同时为空。DDoS高防支持的HTTP端口可在控制台查看。

        :param port_http: The port_http of this ShowDomainNameConfigResponse.
        :type port_http: list[int]
        """
        self._port_http = port_http

    @property
    def port_https(self):
        r"""Gets the port_https of this ShowDomainNameConfigResponse.

        HTTPS端口，与port_http不能同时为空。DDoS高防支持的HTTPS端口可在控制台查看。

        :return: The port_https of this ShowDomainNameConfigResponse.
        :rtype: list[int]
        """
        return self._port_https

    @port_https.setter
    def port_https(self, port_https):
        r"""Sets the port_https of this ShowDomainNameConfigResponse.

        HTTPS端口，与port_http不能同时为空。DDoS高防支持的HTTPS端口可在控制台查看。

        :param port_https: The port_https of this ShowDomainNameConfigResponse.
        :type port_https: list[int]
        """
        self._port_https = port_https

    @property
    def real_server(self):
        r"""Gets the real_server of this ShowDomainNameConfigResponse.

        源站ip/源站域名

        :return: The real_server of this ShowDomainNameConfigResponse.
        :rtype: str
        """
        return self._real_server

    @real_server.setter
    def real_server(self, real_server):
        r"""Sets the real_server of this ShowDomainNameConfigResponse.

        源站ip/源站域名

        :param real_server: The real_server of this ShowDomainNameConfigResponse.
        :type real_server: str
        """
        self._real_server = real_server

    @property
    def pp_enable(self):
        r"""Gets the pp_enable of this ShowDomainNameConfigResponse.

        pp是否开启, 1-开启，0-关闭

        :return: The pp_enable of this ShowDomainNameConfigResponse.
        :rtype: int
        """
        return self._pp_enable

    @pp_enable.setter
    def pp_enable(self, pp_enable):
        r"""Sets the pp_enable of this ShowDomainNameConfigResponse.

        pp是否开启, 1-开启，0-关闭

        :param pp_enable: The pp_enable of this ShowDomainNameConfigResponse.
        :type pp_enable: int
        """
        self._pp_enable = pp_enable

    @property
    def overseas_type(self):
        r"""Gets the overseas_type of this ShowDomainNameConfigResponse.

        防护区域,0-大陆,1-海外

        :return: The overseas_type of this ShowDomainNameConfigResponse.
        :rtype: int
        """
        return self._overseas_type

    @overseas_type.setter
    def overseas_type(self, overseas_type):
        r"""Sets the overseas_type of this ShowDomainNameConfigResponse.

        防护区域,0-大陆,1-海外

        :param overseas_type: The overseas_type of this ShowDomainNameConfigResponse.
        :type overseas_type: int
        """
        self._overseas_type = overseas_type

    @property
    def tls(self):
        r"""Gets the tls of this ShowDomainNameConfigResponse.

        tls(请求参数type=waf时)

        :return: The tls of this ShowDomainNameConfigResponse.
        :rtype: str
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        r"""Sets the tls of this ShowDomainNameConfigResponse.

        tls(请求参数type=waf时)

        :param tls: The tls of this ShowDomainNameConfigResponse.
        :type tls: str
        """
        self._tls = tls

    @property
    def cipher(self):
        r"""Gets the cipher of this ShowDomainNameConfigResponse.

        加密套件(请求参数type=waf时)

        :return: The cipher of this ShowDomainNameConfigResponse.
        :rtype: str
        """
        return self._cipher

    @cipher.setter
    def cipher(self, cipher):
        r"""Sets the cipher of this ShowDomainNameConfigResponse.

        加密套件(请求参数type=waf时)

        :param cipher: The cipher of this ShowDomainNameConfigResponse.
        :type cipher: str
        """
        self._cipher = cipher

    @property
    def http2_enable(self):
        r"""Gets the http2_enable of this ShowDomainNameConfigResponse.

        是否允许http2(请求参数type=waf时)

        :return: The http2_enable of this ShowDomainNameConfigResponse.
        :rtype: bool
        """
        return self._http2_enable

    @http2_enable.setter
    def http2_enable(self, http2_enable):
        r"""Sets the http2_enable of this ShowDomainNameConfigResponse.

        是否允许http2(请求参数type=waf时)

        :param http2_enable: The http2_enable of this ShowDomainNameConfigResponse.
        :type http2_enable: bool
        """
        self._http2_enable = http2_enable

    @property
    def header_map(self):
        r"""Gets the header_map of this ShowDomainNameConfigResponse.

        字段转发(请求参数type=waf时)

        :return: The header_map of this ShowDomainNameConfigResponse.
        :rtype: object
        """
        return self._header_map

    @header_map.setter
    def header_map(self, header_map):
        r"""Sets the header_map of this ShowDomainNameConfigResponse.

        字段转发(请求参数type=waf时)

        :param header_map: The header_map of this ShowDomainNameConfigResponse.
        :type header_map: object
        """
        self._header_map = header_map

    def to_dict(self):
        import warnings
        warnings.warn("ShowDomainNameConfigResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowDomainNameConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
