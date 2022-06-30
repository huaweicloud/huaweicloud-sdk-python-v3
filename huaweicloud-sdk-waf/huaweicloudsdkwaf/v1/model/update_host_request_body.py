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
        'server': 'list[UpdateCloudWafServer]',
        'tls': 'str',
        'cipher': 'str',
        'block_page': 'BlockPage',
        'traffic_mark': 'TrafficMark',
        'flag': 'dict(str, str)',
        'extend': 'dict(str, str)',
        'http2_enable': 'bool',
        'ipv6_enable': 'bool',
        'lb_algorithm': 'str',
        'timeout_config': 'TimeoutConfig'
    }

    attribute_map = {
        'proxy': 'proxy',
        'certificateid': 'certificateid',
        'certificatename': 'certificatename',
        'server': 'server',
        'tls': 'tls',
        'cipher': 'cipher',
        'block_page': 'block_page',
        'traffic_mark': 'traffic_mark',
        'flag': 'flag',
        'extend': 'extend',
        'http2_enable': 'http2_enable',
        'ipv6_enable': 'ipv6_enable',
        'lb_algorithm': 'lb_algorithm',
        'timeout_config': 'timeout_config'
    }

    def __init__(self, proxy=None, certificateid=None, certificatename=None, server=None, tls=None, cipher=None, block_page=None, traffic_mark=None, flag=None, extend=None, http2_enable=None, ipv6_enable=None, lb_algorithm=None, timeout_config=None):
        """UpdateHostRequestBody

        The model defined in huaweicloud sdk

        :param proxy: 是否使用代理
        :type proxy: bool
        :param certificateid: 证书id,在对外协议为https的场景下可以使用，可以通过查询证书列表（ListCertificates）接口查询证书id
        :type certificateid: str
        :param certificatename: 证书名称,在对外协议为https的场景下可以使用，可以在页面上获取的证书名称，或通过查询证书列表（ListCertificates）接口获取证书名称
        :type certificatename: str
        :param server: 服务器配置
        :type server: list[:class:`huaweicloudsdkwaf.v1.UpdateCloudWafServer`]
        :param tls: 支持最低的TLS版本（TLS v1.0/TLS v1.1/TLS v1.2）,默认为TLS v1.0版本
        :type tls: str
        :param cipher: 加密套件（cipher_1，cipher_2，cipher_3，cipher_4，cipher_default）：  cipher_1： 加密算法为ECDHE-ECDSA-AES256-GCM-SHA384:HIGH:!MEDIUM:!LOW:!aNULL:!eNULL:!DES:!MD5:!PSK:!RC4:!kRSA:!SRP:!3DES:!DSS:!EXP:!CAMELLIA:@STRENGTH   cipher_2：加密算法为EECDH+AESGCM:EDH+AESGCM    cipher_3：加密算法为ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH    cipher_4：加密算法为ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!EDH    cipher_default： 加密算法为ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!AESGCM
        :type cipher: str
        :param block_page: 
        :type block_page: :class:`huaweicloudsdkwaf.v1.BlockPage`
        :param traffic_mark: 
        :type traffic_mark: :class:`huaweicloudsdkwaf.v1.TrafficMark`
        :param flag: 域名特殊标识
        :type flag: dict(str, str)
        :param extend: 可扩展字段
        :type extend: dict(str, str)
        :param http2_enable: 是否使用HTTP2
        :type http2_enable: bool
        :param ipv6_enable: 是否开启IPv6防护
        :type ipv6_enable: bool
        :param lb_algorithm: 负载均衡算法
        :type lb_algorithm: str
        :param timeout_config: 
        :type timeout_config: :class:`huaweicloudsdkwaf.v1.TimeoutConfig`
        """
        
        

        self._proxy = None
        self._certificateid = None
        self._certificatename = None
        self._server = None
        self._tls = None
        self._cipher = None
        self._block_page = None
        self._traffic_mark = None
        self._flag = None
        self._extend = None
        self._http2_enable = None
        self._ipv6_enable = None
        self._lb_algorithm = None
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
        if block_page is not None:
            self.block_page = block_page
        if traffic_mark is not None:
            self.traffic_mark = traffic_mark
        if flag is not None:
            self.flag = flag
        if extend is not None:
            self.extend = extend
        if http2_enable is not None:
            self.http2_enable = http2_enable
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if lb_algorithm is not None:
            self.lb_algorithm = lb_algorithm
        if timeout_config is not None:
            self.timeout_config = timeout_config

    @property
    def proxy(self):
        """Gets the proxy of this UpdateHostRequestBody.

        是否使用代理

        :return: The proxy of this UpdateHostRequestBody.
        :rtype: bool
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this UpdateHostRequestBody.

        是否使用代理

        :param proxy: The proxy of this UpdateHostRequestBody.
        :type proxy: bool
        """
        self._proxy = proxy

    @property
    def certificateid(self):
        """Gets the certificateid of this UpdateHostRequestBody.

        证书id,在对外协议为https的场景下可以使用，可以通过查询证书列表（ListCertificates）接口查询证书id

        :return: The certificateid of this UpdateHostRequestBody.
        :rtype: str
        """
        return self._certificateid

    @certificateid.setter
    def certificateid(self, certificateid):
        """Sets the certificateid of this UpdateHostRequestBody.

        证书id,在对外协议为https的场景下可以使用，可以通过查询证书列表（ListCertificates）接口查询证书id

        :param certificateid: The certificateid of this UpdateHostRequestBody.
        :type certificateid: str
        """
        self._certificateid = certificateid

    @property
    def certificatename(self):
        """Gets the certificatename of this UpdateHostRequestBody.

        证书名称,在对外协议为https的场景下可以使用，可以在页面上获取的证书名称，或通过查询证书列表（ListCertificates）接口获取证书名称

        :return: The certificatename of this UpdateHostRequestBody.
        :rtype: str
        """
        return self._certificatename

    @certificatename.setter
    def certificatename(self, certificatename):
        """Sets the certificatename of this UpdateHostRequestBody.

        证书名称,在对外协议为https的场景下可以使用，可以在页面上获取的证书名称，或通过查询证书列表（ListCertificates）接口获取证书名称

        :param certificatename: The certificatename of this UpdateHostRequestBody.
        :type certificatename: str
        """
        self._certificatename = certificatename

    @property
    def server(self):
        """Gets the server of this UpdateHostRequestBody.

        服务器配置

        :return: The server of this UpdateHostRequestBody.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.UpdateCloudWafServer`]
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this UpdateHostRequestBody.

        服务器配置

        :param server: The server of this UpdateHostRequestBody.
        :type server: list[:class:`huaweicloudsdkwaf.v1.UpdateCloudWafServer`]
        """
        self._server = server

    @property
    def tls(self):
        """Gets the tls of this UpdateHostRequestBody.

        支持最低的TLS版本（TLS v1.0/TLS v1.1/TLS v1.2）,默认为TLS v1.0版本

        :return: The tls of this UpdateHostRequestBody.
        :rtype: str
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """Sets the tls of this UpdateHostRequestBody.

        支持最低的TLS版本（TLS v1.0/TLS v1.1/TLS v1.2）,默认为TLS v1.0版本

        :param tls: The tls of this UpdateHostRequestBody.
        :type tls: str
        """
        self._tls = tls

    @property
    def cipher(self):
        """Gets the cipher of this UpdateHostRequestBody.

        加密套件（cipher_1，cipher_2，cipher_3，cipher_4，cipher_default）：  cipher_1： 加密算法为ECDHE-ECDSA-AES256-GCM-SHA384:HIGH:!MEDIUM:!LOW:!aNULL:!eNULL:!DES:!MD5:!PSK:!RC4:!kRSA:!SRP:!3DES:!DSS:!EXP:!CAMELLIA:@STRENGTH   cipher_2：加密算法为EECDH+AESGCM:EDH+AESGCM    cipher_3：加密算法为ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH    cipher_4：加密算法为ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!EDH    cipher_default： 加密算法为ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!AESGCM

        :return: The cipher of this UpdateHostRequestBody.
        :rtype: str
        """
        return self._cipher

    @cipher.setter
    def cipher(self, cipher):
        """Sets the cipher of this UpdateHostRequestBody.

        加密套件（cipher_1，cipher_2，cipher_3，cipher_4，cipher_default）：  cipher_1： 加密算法为ECDHE-ECDSA-AES256-GCM-SHA384:HIGH:!MEDIUM:!LOW:!aNULL:!eNULL:!DES:!MD5:!PSK:!RC4:!kRSA:!SRP:!3DES:!DSS:!EXP:!CAMELLIA:@STRENGTH   cipher_2：加密算法为EECDH+AESGCM:EDH+AESGCM    cipher_3：加密算法为ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH    cipher_4：加密算法为ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!EDH    cipher_default： 加密算法为ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!AESGCM

        :param cipher: The cipher of this UpdateHostRequestBody.
        :type cipher: str
        """
        self._cipher = cipher

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

        域名特殊标识

        :return: The flag of this UpdateHostRequestBody.
        :rtype: dict(str, str)
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        """Sets the flag of this UpdateHostRequestBody.

        域名特殊标识

        :param flag: The flag of this UpdateHostRequestBody.
        :type flag: dict(str, str)
        """
        self._flag = flag

    @property
    def extend(self):
        """Gets the extend of this UpdateHostRequestBody.

        可扩展字段

        :return: The extend of this UpdateHostRequestBody.
        :rtype: dict(str, str)
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        """Sets the extend of this UpdateHostRequestBody.

        可扩展字段

        :param extend: The extend of this UpdateHostRequestBody.
        :type extend: dict(str, str)
        """
        self._extend = extend

    @property
    def http2_enable(self):
        """Gets the http2_enable of this UpdateHostRequestBody.

        是否使用HTTP2

        :return: The http2_enable of this UpdateHostRequestBody.
        :rtype: bool
        """
        return self._http2_enable

    @http2_enable.setter
    def http2_enable(self, http2_enable):
        """Sets the http2_enable of this UpdateHostRequestBody.

        是否使用HTTP2

        :param http2_enable: The http2_enable of this UpdateHostRequestBody.
        :type http2_enable: bool
        """
        self._http2_enable = http2_enable

    @property
    def ipv6_enable(self):
        """Gets the ipv6_enable of this UpdateHostRequestBody.

        是否开启IPv6防护

        :return: The ipv6_enable of this UpdateHostRequestBody.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        """Sets the ipv6_enable of this UpdateHostRequestBody.

        是否开启IPv6防护

        :param ipv6_enable: The ipv6_enable of this UpdateHostRequestBody.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def lb_algorithm(self):
        """Gets the lb_algorithm of this UpdateHostRequestBody.

        负载均衡算法

        :return: The lb_algorithm of this UpdateHostRequestBody.
        :rtype: str
        """
        return self._lb_algorithm

    @lb_algorithm.setter
    def lb_algorithm(self, lb_algorithm):
        """Sets the lb_algorithm of this UpdateHostRequestBody.

        负载均衡算法

        :param lb_algorithm: The lb_algorithm of this UpdateHostRequestBody.
        :type lb_algorithm: str
        """
        self._lb_algorithm = lb_algorithm

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
