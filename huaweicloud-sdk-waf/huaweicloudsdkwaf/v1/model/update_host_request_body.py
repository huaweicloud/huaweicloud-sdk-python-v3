# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHostRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'proxy': 'bool',
        'certificateid': 'str',
        'certificatename': 'str',
        'server': 'list[CloudWafServer]',
        'tls': 'str',
        'cipher': 'str',
        'http2_enable': 'bool',
        'ipv6_enable': 'bool',
        'web_tag': 'str',
        'exclusive_ip': 'bool',
        'paid_type': 'str',
        'block_page': 'BlockPage',
        'traffic_mark': 'TrafficMark',
        'flag': 'Flag',
        'extend': 'dict(str, str)',
        'circuit_breaker': 'CircuitBreaker',
        'timeout_config': 'TimeoutConfig'
    }

    attribute_map = {
        'proxy': 'proxy',
        'certificateid': 'certificateid',
        'certificatename': 'certificatename',
        'server': 'server',
        'tls': 'tls',
        'cipher': 'cipher',
        'http2_enable': 'http2_enable',
        'ipv6_enable': 'ipv6_enable',
        'web_tag': 'web_tag',
        'exclusive_ip': 'exclusive_ip',
        'paid_type': 'paid_type',
        'block_page': 'block_page',
        'traffic_mark': 'traffic_mark',
        'flag': 'flag',
        'extend': 'extend',
        'circuit_breaker': 'circuit_breaker',
        'timeout_config': 'timeout_config'
    }

    def __init__(self, proxy=None, certificateid=None, certificatename=None, server=None, tls=None, cipher=None, http2_enable=None, ipv6_enable=None, web_tag=None, exclusive_ip=None, paid_type=None, block_page=None, traffic_mark=None, flag=None, extend=None, circuit_breaker=None, timeout_config=None):
        """UpdateHostRequestBody

        The model defined in huaweicloud sdk

        :param proxy: 防护域名是否使用代理   - false：不使用代理   - true：使用代理
        :type proxy: bool
        :param certificateid: 证书id，通过查询证书列表接口（ListCertificates）接口获取证书id   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数
        :type certificateid: str
        :param certificatename: 证书名   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数
        :type certificatename: str
        :param server: 防护域名的源站服务器配置信息
        :type server: list[:class:`huaweicloudsdkwaf.v1.CloudWafServer`]
        :param tls: 配置的最低TLS版本（TLS v1.0/TLS v1.1/TLS v1.2）,默认为TLS v1.0版本，对于低于最低TLS版本的请求，将无法正常访问网站
        :type tls: str
        :param cipher: 加密套件（cipher_1，cipher_2，cipher_3，cipher_4，cipher_default）：  - cipher_1： 加密算法为ECDHE-ECDSA-AES256-GCM-SHA384:HIGH:!MEDIUM:!LOW:!aNULL:!eNULL:!DES:!MD5:!PSK:!RC4:!kRSA:!SRP:!3DES:!DSS:!EXP:!CAMELLIA:@STRENGTH   - cipher_2：加密算法为EECDH+AESGCM:EDH+AESGCM   - cipher_3：加密算法为ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH   - cipher_4：加密算法为ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!EDH   - cipher_default： 加密算法为ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!AESGCM
        :type cipher: str
        :param http2_enable: 是否支持http2   - true：表示支持http2   - false：表示不支持http2
        :type http2_enable: bool
        :param ipv6_enable: 是否开启IPv6防护，仅专业版（原企业版）和铂金版（原旗舰版）支持IPv6防护。   - true：开启IPv6防护   - false：关闭IPV6防护
        :type ipv6_enable: bool
        :param web_tag: 网站名称，对应WAF控制台域名详情中的网站名称
        :type web_tag: str
        :param exclusive_ip: 是否使用独享ip   - true：使用独享ip   - false：不实用独享ip
        :type exclusive_ip: bool
        :param paid_type: 套餐付费模式，目前只支持prePaid预付款模式
        :type paid_type: str
        :param block_page: 
        :type block_page: :class:`huaweicloudsdkwaf.v1.BlockPage`
        :param traffic_mark: 
        :type traffic_mark: :class:`huaweicloudsdkwaf.v1.TrafficMark`
        :param flag: 
        :type flag: :class:`huaweicloudsdkwaf.v1.Flag`
        :param extend: 扩展字段，用于保存防护域名的一些配置信息。
        :type extend: dict(str, str)
        :param circuit_breaker: 
        :type circuit_breaker: :class:`huaweicloudsdkwaf.v1.CircuitBreaker`
        :param timeout_config: 
        :type timeout_config: :class:`huaweicloudsdkwaf.v1.TimeoutConfig`
        """
        
        

        self._proxy = None
        self._certificateid = None
        self._certificatename = None
        self._server = None
        self._tls = None
        self._cipher = None
        self._http2_enable = None
        self._ipv6_enable = None
        self._web_tag = None
        self._exclusive_ip = None
        self._paid_type = None
        self._block_page = None
        self._traffic_mark = None
        self._flag = None
        self._extend = None
        self._circuit_breaker = None
        self._timeout_config = None
        self.discriminator = None

        if proxy is not None:
            self.proxy = proxy
        if certificateid is not None:
            self.certificateid = certificateid
        if certificatename is not None:
            self.certificatename = certificatename
        if server is not None:
            self.server = server
        if tls is not None:
            self.tls = tls
        if cipher is not None:
            self.cipher = cipher
        if http2_enable is not None:
            self.http2_enable = http2_enable
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if web_tag is not None:
            self.web_tag = web_tag
        if exclusive_ip is not None:
            self.exclusive_ip = exclusive_ip
        if paid_type is not None:
            self.paid_type = paid_type
        if block_page is not None:
            self.block_page = block_page
        if traffic_mark is not None:
            self.traffic_mark = traffic_mark
        if flag is not None:
            self.flag = flag
        if extend is not None:
            self.extend = extend
        if circuit_breaker is not None:
            self.circuit_breaker = circuit_breaker
        if timeout_config is not None:
            self.timeout_config = timeout_config

    @property
    def proxy(self):
        """Gets the proxy of this UpdateHostRequestBody.

        防护域名是否使用代理   - false：不使用代理   - true：使用代理

        :return: The proxy of this UpdateHostRequestBody.
        :rtype: bool
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this UpdateHostRequestBody.

        防护域名是否使用代理   - false：不使用代理   - true：使用代理

        :param proxy: The proxy of this UpdateHostRequestBody.
        :type proxy: bool
        """
        self._proxy = proxy

    @property
    def certificateid(self):
        """Gets the certificateid of this UpdateHostRequestBody.

        证书id，通过查询证书列表接口（ListCertificates）接口获取证书id   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数

        :return: The certificateid of this UpdateHostRequestBody.
        :rtype: str
        """
        return self._certificateid

    @certificateid.setter
    def certificateid(self, certificateid):
        """Sets the certificateid of this UpdateHostRequestBody.

        证书id，通过查询证书列表接口（ListCertificates）接口获取证书id   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数

        :param certificateid: The certificateid of this UpdateHostRequestBody.
        :type certificateid: str
        """
        self._certificateid = certificateid

    @property
    def certificatename(self):
        """Gets the certificatename of this UpdateHostRequestBody.

        证书名   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数

        :return: The certificatename of this UpdateHostRequestBody.
        :rtype: str
        """
        return self._certificatename

    @certificatename.setter
    def certificatename(self, certificatename):
        """Sets the certificatename of this UpdateHostRequestBody.

        证书名   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数

        :param certificatename: The certificatename of this UpdateHostRequestBody.
        :type certificatename: str
        """
        self._certificatename = certificatename

    @property
    def server(self):
        """Gets the server of this UpdateHostRequestBody.

        防护域名的源站服务器配置信息

        :return: The server of this UpdateHostRequestBody.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.CloudWafServer`]
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this UpdateHostRequestBody.

        防护域名的源站服务器配置信息

        :param server: The server of this UpdateHostRequestBody.
        :type server: list[:class:`huaweicloudsdkwaf.v1.CloudWafServer`]
        """
        self._server = server

    @property
    def tls(self):
        """Gets the tls of this UpdateHostRequestBody.

        配置的最低TLS版本（TLS v1.0/TLS v1.1/TLS v1.2）,默认为TLS v1.0版本，对于低于最低TLS版本的请求，将无法正常访问网站

        :return: The tls of this UpdateHostRequestBody.
        :rtype: str
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """Sets the tls of this UpdateHostRequestBody.

        配置的最低TLS版本（TLS v1.0/TLS v1.1/TLS v1.2）,默认为TLS v1.0版本，对于低于最低TLS版本的请求，将无法正常访问网站

        :param tls: The tls of this UpdateHostRequestBody.
        :type tls: str
        """
        self._tls = tls

    @property
    def cipher(self):
        """Gets the cipher of this UpdateHostRequestBody.

        加密套件（cipher_1，cipher_2，cipher_3，cipher_4，cipher_default）：  - cipher_1： 加密算法为ECDHE-ECDSA-AES256-GCM-SHA384:HIGH:!MEDIUM:!LOW:!aNULL:!eNULL:!DES:!MD5:!PSK:!RC4:!kRSA:!SRP:!3DES:!DSS:!EXP:!CAMELLIA:@STRENGTH   - cipher_2：加密算法为EECDH+AESGCM:EDH+AESGCM   - cipher_3：加密算法为ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH   - cipher_4：加密算法为ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!EDH   - cipher_default： 加密算法为ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!AESGCM

        :return: The cipher of this UpdateHostRequestBody.
        :rtype: str
        """
        return self._cipher

    @cipher.setter
    def cipher(self, cipher):
        """Sets the cipher of this UpdateHostRequestBody.

        加密套件（cipher_1，cipher_2，cipher_3，cipher_4，cipher_default）：  - cipher_1： 加密算法为ECDHE-ECDSA-AES256-GCM-SHA384:HIGH:!MEDIUM:!LOW:!aNULL:!eNULL:!DES:!MD5:!PSK:!RC4:!kRSA:!SRP:!3DES:!DSS:!EXP:!CAMELLIA:@STRENGTH   - cipher_2：加密算法为EECDH+AESGCM:EDH+AESGCM   - cipher_3：加密算法为ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH   - cipher_4：加密算法为ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!EDH   - cipher_default： 加密算法为ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!AESGCM

        :param cipher: The cipher of this UpdateHostRequestBody.
        :type cipher: str
        """
        self._cipher = cipher

    @property
    def http2_enable(self):
        """Gets the http2_enable of this UpdateHostRequestBody.

        是否支持http2   - true：表示支持http2   - false：表示不支持http2

        :return: The http2_enable of this UpdateHostRequestBody.
        :rtype: bool
        """
        return self._http2_enable

    @http2_enable.setter
    def http2_enable(self, http2_enable):
        """Sets the http2_enable of this UpdateHostRequestBody.

        是否支持http2   - true：表示支持http2   - false：表示不支持http2

        :param http2_enable: The http2_enable of this UpdateHostRequestBody.
        :type http2_enable: bool
        """
        self._http2_enable = http2_enable

    @property
    def ipv6_enable(self):
        """Gets the ipv6_enable of this UpdateHostRequestBody.

        是否开启IPv6防护，仅专业版（原企业版）和铂金版（原旗舰版）支持IPv6防护。   - true：开启IPv6防护   - false：关闭IPV6防护

        :return: The ipv6_enable of this UpdateHostRequestBody.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        """Sets the ipv6_enable of this UpdateHostRequestBody.

        是否开启IPv6防护，仅专业版（原企业版）和铂金版（原旗舰版）支持IPv6防护。   - true：开启IPv6防护   - false：关闭IPV6防护

        :param ipv6_enable: The ipv6_enable of this UpdateHostRequestBody.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def web_tag(self):
        """Gets the web_tag of this UpdateHostRequestBody.

        网站名称，对应WAF控制台域名详情中的网站名称

        :return: The web_tag of this UpdateHostRequestBody.
        :rtype: str
        """
        return self._web_tag

    @web_tag.setter
    def web_tag(self, web_tag):
        """Sets the web_tag of this UpdateHostRequestBody.

        网站名称，对应WAF控制台域名详情中的网站名称

        :param web_tag: The web_tag of this UpdateHostRequestBody.
        :type web_tag: str
        """
        self._web_tag = web_tag

    @property
    def exclusive_ip(self):
        """Gets the exclusive_ip of this UpdateHostRequestBody.

        是否使用独享ip   - true：使用独享ip   - false：不实用独享ip

        :return: The exclusive_ip of this UpdateHostRequestBody.
        :rtype: bool
        """
        return self._exclusive_ip

    @exclusive_ip.setter
    def exclusive_ip(self, exclusive_ip):
        """Sets the exclusive_ip of this UpdateHostRequestBody.

        是否使用独享ip   - true：使用独享ip   - false：不实用独享ip

        :param exclusive_ip: The exclusive_ip of this UpdateHostRequestBody.
        :type exclusive_ip: bool
        """
        self._exclusive_ip = exclusive_ip

    @property
    def paid_type(self):
        """Gets the paid_type of this UpdateHostRequestBody.

        套餐付费模式，目前只支持prePaid预付款模式

        :return: The paid_type of this UpdateHostRequestBody.
        :rtype: str
        """
        return self._paid_type

    @paid_type.setter
    def paid_type(self, paid_type):
        """Sets the paid_type of this UpdateHostRequestBody.

        套餐付费模式，目前只支持prePaid预付款模式

        :param paid_type: The paid_type of this UpdateHostRequestBody.
        :type paid_type: str
        """
        self._paid_type = paid_type

    @property
    def block_page(self):
        """Gets the block_page of this UpdateHostRequestBody.

        :return: The block_page of this UpdateHostRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.BlockPage`
        """
        return self._block_page

    @block_page.setter
    def block_page(self, block_page):
        """Sets the block_page of this UpdateHostRequestBody.

        :param block_page: The block_page of this UpdateHostRequestBody.
        :type block_page: :class:`huaweicloudsdkwaf.v1.BlockPage`
        """
        self._block_page = block_page

    @property
    def traffic_mark(self):
        """Gets the traffic_mark of this UpdateHostRequestBody.

        :return: The traffic_mark of this UpdateHostRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.TrafficMark`
        """
        return self._traffic_mark

    @traffic_mark.setter
    def traffic_mark(self, traffic_mark):
        """Sets the traffic_mark of this UpdateHostRequestBody.

        :param traffic_mark: The traffic_mark of this UpdateHostRequestBody.
        :type traffic_mark: :class:`huaweicloudsdkwaf.v1.TrafficMark`
        """
        self._traffic_mark = traffic_mark

    @property
    def flag(self):
        """Gets the flag of this UpdateHostRequestBody.

        :return: The flag of this UpdateHostRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.Flag`
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        """Sets the flag of this UpdateHostRequestBody.

        :param flag: The flag of this UpdateHostRequestBody.
        :type flag: :class:`huaweicloudsdkwaf.v1.Flag`
        """
        self._flag = flag

    @property
    def extend(self):
        """Gets the extend of this UpdateHostRequestBody.

        扩展字段，用于保存防护域名的一些配置信息。

        :return: The extend of this UpdateHostRequestBody.
        :rtype: dict(str, str)
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        """Sets the extend of this UpdateHostRequestBody.

        扩展字段，用于保存防护域名的一些配置信息。

        :param extend: The extend of this UpdateHostRequestBody.
        :type extend: dict(str, str)
        """
        self._extend = extend

    @property
    def circuit_breaker(self):
        """Gets the circuit_breaker of this UpdateHostRequestBody.

        :return: The circuit_breaker of this UpdateHostRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.CircuitBreaker`
        """
        return self._circuit_breaker

    @circuit_breaker.setter
    def circuit_breaker(self, circuit_breaker):
        """Sets the circuit_breaker of this UpdateHostRequestBody.

        :param circuit_breaker: The circuit_breaker of this UpdateHostRequestBody.
        :type circuit_breaker: :class:`huaweicloudsdkwaf.v1.CircuitBreaker`
        """
        self._circuit_breaker = circuit_breaker

    @property
    def timeout_config(self):
        """Gets the timeout_config of this UpdateHostRequestBody.

        :return: The timeout_config of this UpdateHostRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.TimeoutConfig`
        """
        return self._timeout_config

    @timeout_config.setter
    def timeout_config(self, timeout_config):
        """Sets the timeout_config of this UpdateHostRequestBody.

        :param timeout_config: The timeout_config of this UpdateHostRequestBody.
        :type timeout_config: :class:`huaweicloudsdkwaf.v1.TimeoutConfig`
        """
        self._timeout_config = timeout_config

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
        if not isinstance(other, UpdateHostRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
