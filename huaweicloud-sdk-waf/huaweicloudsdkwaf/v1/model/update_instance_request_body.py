# coding: utf-8

import re
import six





class UpdateInstanceRequestBody:


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
        'server': 'list[PremiumWafServer]',
        'tls': 'str',
        'cipher': 'str',
        'block_page': 'BlockPage',
        'traffic_mark': 'TrafficMark',
        'flag': 'dict(str, str)',
        'extend': 'dict(str, str)'
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
        'extend': 'extend'
    }

    def __init__(self, proxy=None, certificateid=None, certificatename=None, server=None, tls=None, cipher=None, block_page=None, traffic_mark=None, flag=None, extend=None):
        """UpdateInstanceRequestBody - a model defined in huaweicloud sdk"""
        
        

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

    @property
    def proxy(self):
        """Gets the proxy of this UpdateInstanceRequestBody.

        是否使用代理

        :return: The proxy of this UpdateInstanceRequestBody.
        :rtype: bool
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this UpdateInstanceRequestBody.

        是否使用代理

        :param proxy: The proxy of this UpdateInstanceRequestBody.
        :type: bool
        """
        self._proxy = proxy

    @property
    def certificateid(self):
        """Gets the certificateid of this UpdateInstanceRequestBody.

        证书ID

        :return: The certificateid of this UpdateInstanceRequestBody.
        :rtype: str
        """
        return self._certificateid

    @certificateid.setter
    def certificateid(self, certificateid):
        """Sets the certificateid of this UpdateInstanceRequestBody.

        证书ID

        :param certificateid: The certificateid of this UpdateInstanceRequestBody.
        :type: str
        """
        self._certificateid = certificateid

    @property
    def certificatename(self):
        """Gets the certificatename of this UpdateInstanceRequestBody.

        证书名称

        :return: The certificatename of this UpdateInstanceRequestBody.
        :rtype: str
        """
        return self._certificatename

    @certificatename.setter
    def certificatename(self, certificatename):
        """Sets the certificatename of this UpdateInstanceRequestBody.

        证书名称

        :param certificatename: The certificatename of this UpdateInstanceRequestBody.
        :type: str
        """
        self._certificatename = certificatename

    @property
    def server(self):
        """Gets the server of this UpdateInstanceRequestBody.

        独享模式回源服务器配置

        :return: The server of this UpdateInstanceRequestBody.
        :rtype: list[PremiumWafServer]
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this UpdateInstanceRequestBody.

        独享模式回源服务器配置

        :param server: The server of this UpdateInstanceRequestBody.
        :type: list[PremiumWafServer]
        """
        self._server = server

    @property
    def tls(self):
        """Gets the tls of this UpdateInstanceRequestBody.

        支持最低的TLS版本（TLS v1.0/TLS v1.1/TLS v1.2）

        :return: The tls of this UpdateInstanceRequestBody.
        :rtype: str
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """Sets the tls of this UpdateInstanceRequestBody.

        支持最低的TLS版本（TLS v1.0/TLS v1.1/TLS v1.2）

        :param tls: The tls of this UpdateInstanceRequestBody.
        :type: str
        """
        self._tls = tls

    @property
    def cipher(self):
        """Gets the cipher of this UpdateInstanceRequestBody.

        加密套件代码（cipher_default/cipher_1/cipher_2）

        :return: The cipher of this UpdateInstanceRequestBody.
        :rtype: str
        """
        return self._cipher

    @cipher.setter
    def cipher(self, cipher):
        """Sets the cipher of this UpdateInstanceRequestBody.

        加密套件代码（cipher_default/cipher_1/cipher_2）

        :param cipher: The cipher of this UpdateInstanceRequestBody.
        :type: str
        """
        self._cipher = cipher

    @property
    def block_page(self):
        """Gets the block_page of this UpdateInstanceRequestBody.


        :return: The block_page of this UpdateInstanceRequestBody.
        :rtype: BlockPage
        """
        return self._block_page

    @block_page.setter
    def block_page(self, block_page):
        """Sets the block_page of this UpdateInstanceRequestBody.


        :param block_page: The block_page of this UpdateInstanceRequestBody.
        :type: BlockPage
        """
        self._block_page = block_page

    @property
    def traffic_mark(self):
        """Gets the traffic_mark of this UpdateInstanceRequestBody.


        :return: The traffic_mark of this UpdateInstanceRequestBody.
        :rtype: TrafficMark
        """
        return self._traffic_mark

    @traffic_mark.setter
    def traffic_mark(self, traffic_mark):
        """Sets the traffic_mark of this UpdateInstanceRequestBody.


        :param traffic_mark: The traffic_mark of this UpdateInstanceRequestBody.
        :type: TrafficMark
        """
        self._traffic_mark = traffic_mark

    @property
    def flag(self):
        """Gets the flag of this UpdateInstanceRequestBody.

        域名特殊标识

        :return: The flag of this UpdateInstanceRequestBody.
        :rtype: dict(str, str)
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        """Sets the flag of this UpdateInstanceRequestBody.

        域名特殊标识

        :param flag: The flag of this UpdateInstanceRequestBody.
        :type: dict(str, str)
        """
        self._flag = flag

    @property
    def extend(self):
        """Gets the extend of this UpdateInstanceRequestBody.

        可扩展字段

        :return: The extend of this UpdateInstanceRequestBody.
        :rtype: dict(str, str)
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        """Sets the extend of this UpdateInstanceRequestBody.

        可扩展字段

        :param extend: The extend of this UpdateInstanceRequestBody.
        :type: dict(str, str)
        """
        self._extend = extend

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
        import simplejson as json
        return json.dumps(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
