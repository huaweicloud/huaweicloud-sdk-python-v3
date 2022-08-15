# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateHostResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'hostname': 'str',
        'policyid': 'str',
        'access_code': 'str',
        'protect_status': 'int',
        'access_status': 'int',
        'lb_algorithm': 'str',
        'protocol': 'str',
        'certificateid': 'str',
        'certificatename': 'str',
        'server': 'list[CloudWafServer]',
        'proxy': 'bool',
        'timestamp': 'int',
        'exclusive_ip': 'bool',
        'web_tag': 'str',
        'http2_enable': 'bool',
        'block_page': 'BlockPage',
        'flag': 'Flag',
        'extend': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        'hostname': 'hostname',
        'policyid': 'policyid',
        'access_code': 'access_code',
        'protect_status': 'protect_status',
        'access_status': 'access_status',
        'lb_algorithm': 'lb_algorithm',
        'protocol': 'protocol',
        'certificateid': 'certificateid',
        'certificatename': 'certificatename',
        'server': 'server',
        'proxy': 'proxy',
        'timestamp': 'timestamp',
        'exclusive_ip': 'exclusive_ip',
        'web_tag': 'web_tag',
        'http2_enable': 'http2_enable',
        'block_page': 'block_page',
        'flag': 'flag',
        'extend': 'extend'
    }

    def __init__(self, id=None, hostname=None, policyid=None, access_code=None, protect_status=None, access_status=None, lb_algorithm=None, protocol=None, certificateid=None, certificatename=None, server=None, proxy=None, timestamp=None, exclusive_ip=None, web_tag=None, http2_enable=None, block_page=None, flag=None, extend=None):
        """CreateHostResponse

        The model defined in huaweicloud sdk

        :param id: 域名id
        :type id: str
        :param hostname: 创建的云模式防护域名
        :type hostname: str
        :param policyid: 策略id
        :type policyid: str
        :param access_code: cname前缀
        :type access_code: str
        :param protect_status: 域名防护状态：  - -1：bypass，该域名的请求直接到达其后端服务器，不再经过WAF  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测
        :type protect_status: int
        :param access_status: 域名接入状态，0表示未接入，1表示已接入
        :type access_status: int
        :param lb_algorithm: LB负载均衡，仅专业版（原企业版）和铂金版（原旗舰版）支持配置负载均衡算法   - 源IP Hash：将某个IP的请求定向到同一个服务器   - 加权轮询：所有请求将按权重轮流分配给源站服务器   - Session Hash：将某个Session标识的请求定向到同一个源站服务器，请确保在域名添加完毕后配置攻击惩罚的流量标识，否则Session Hash配置不生效
        :type lb_algorithm: str
        :param protocol: 返回的客户端协议类型
        :type protocol: str
        :param certificateid: 返回的证书id
        :type certificateid: str
        :param certificatename: 证书名称
        :type certificatename: str
        :param server: 防护域名的源站服务器配置信息
        :type server: list[:class:`huaweicloudsdkwaf.v1.CloudWafServer`]
        :param proxy: 防护域名是否使用代理   - false：不使用代理   - true：使用代理
        :type proxy: bool
        :param timestamp: 创建防护域名的时间
        :type timestamp: int
        :param exclusive_ip: 是否使用独享ip   - true：使用独享ip   - false：不实用独享ip
        :type exclusive_ip: bool
        :param web_tag: 网站名称，对应WAF控制台域名详情中的网站名称
        :type web_tag: str
        :param http2_enable: 是否支持http2   - true：表示支持http2   - false：表示不支持http2
        :type http2_enable: bool
        :param block_page: 
        :type block_page: :class:`huaweicloudsdkwaf.v1.BlockPage`
        :param flag: 
        :type flag: :class:`huaweicloudsdkwaf.v1.Flag`
        :param extend: 扩展字段，用于保存防护域名的一些配置信息。
        :type extend: dict(str, str)
        """
        
        super(CreateHostResponse, self).__init__()

        self._id = None
        self._hostname = None
        self._policyid = None
        self._access_code = None
        self._protect_status = None
        self._access_status = None
        self._lb_algorithm = None
        self._protocol = None
        self._certificateid = None
        self._certificatename = None
        self._server = None
        self._proxy = None
        self._timestamp = None
        self._exclusive_ip = None
        self._web_tag = None
        self._http2_enable = None
        self._block_page = None
        self._flag = None
        self._extend = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if hostname is not None:
            self.hostname = hostname
        if policyid is not None:
            self.policyid = policyid
        if access_code is not None:
            self.access_code = access_code
        if protect_status is not None:
            self.protect_status = protect_status
        if access_status is not None:
            self.access_status = access_status
        if lb_algorithm is not None:
            self.lb_algorithm = lb_algorithm
        if protocol is not None:
            self.protocol = protocol
        if certificateid is not None:
            self.certificateid = certificateid
        if certificatename is not None:
            self.certificatename = certificatename
        if server is not None:
            self.server = server
        if proxy is not None:
            self.proxy = proxy
        if timestamp is not None:
            self.timestamp = timestamp
        if exclusive_ip is not None:
            self.exclusive_ip = exclusive_ip
        if web_tag is not None:
            self.web_tag = web_tag
        if http2_enable is not None:
            self.http2_enable = http2_enable
        if block_page is not None:
            self.block_page = block_page
        if flag is not None:
            self.flag = flag
        if extend is not None:
            self.extend = extend

    @property
    def id(self):
        """Gets the id of this CreateHostResponse.

        域名id

        :return: The id of this CreateHostResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateHostResponse.

        域名id

        :param id: The id of this CreateHostResponse.
        :type id: str
        """
        self._id = id

    @property
    def hostname(self):
        """Gets the hostname of this CreateHostResponse.

        创建的云模式防护域名

        :return: The hostname of this CreateHostResponse.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this CreateHostResponse.

        创建的云模式防护域名

        :param hostname: The hostname of this CreateHostResponse.
        :type hostname: str
        """
        self._hostname = hostname

    @property
    def policyid(self):
        """Gets the policyid of this CreateHostResponse.

        策略id

        :return: The policyid of this CreateHostResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this CreateHostResponse.

        策略id

        :param policyid: The policyid of this CreateHostResponse.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def access_code(self):
        """Gets the access_code of this CreateHostResponse.

        cname前缀

        :return: The access_code of this CreateHostResponse.
        :rtype: str
        """
        return self._access_code

    @access_code.setter
    def access_code(self, access_code):
        """Sets the access_code of this CreateHostResponse.

        cname前缀

        :param access_code: The access_code of this CreateHostResponse.
        :type access_code: str
        """
        self._access_code = access_code

    @property
    def protect_status(self):
        """Gets the protect_status of this CreateHostResponse.

        域名防护状态：  - -1：bypass，该域名的请求直接到达其后端服务器，不再经过WAF  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测

        :return: The protect_status of this CreateHostResponse.
        :rtype: int
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this CreateHostResponse.

        域名防护状态：  - -1：bypass，该域名的请求直接到达其后端服务器，不再经过WAF  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测

        :param protect_status: The protect_status of this CreateHostResponse.
        :type protect_status: int
        """
        self._protect_status = protect_status

    @property
    def access_status(self):
        """Gets the access_status of this CreateHostResponse.

        域名接入状态，0表示未接入，1表示已接入

        :return: The access_status of this CreateHostResponse.
        :rtype: int
        """
        return self._access_status

    @access_status.setter
    def access_status(self, access_status):
        """Sets the access_status of this CreateHostResponse.

        域名接入状态，0表示未接入，1表示已接入

        :param access_status: The access_status of this CreateHostResponse.
        :type access_status: int
        """
        self._access_status = access_status

    @property
    def lb_algorithm(self):
        """Gets the lb_algorithm of this CreateHostResponse.

        LB负载均衡，仅专业版（原企业版）和铂金版（原旗舰版）支持配置负载均衡算法   - 源IP Hash：将某个IP的请求定向到同一个服务器   - 加权轮询：所有请求将按权重轮流分配给源站服务器   - Session Hash：将某个Session标识的请求定向到同一个源站服务器，请确保在域名添加完毕后配置攻击惩罚的流量标识，否则Session Hash配置不生效

        :return: The lb_algorithm of this CreateHostResponse.
        :rtype: str
        """
        return self._lb_algorithm

    @lb_algorithm.setter
    def lb_algorithm(self, lb_algorithm):
        """Sets the lb_algorithm of this CreateHostResponse.

        LB负载均衡，仅专业版（原企业版）和铂金版（原旗舰版）支持配置负载均衡算法   - 源IP Hash：将某个IP的请求定向到同一个服务器   - 加权轮询：所有请求将按权重轮流分配给源站服务器   - Session Hash：将某个Session标识的请求定向到同一个源站服务器，请确保在域名添加完毕后配置攻击惩罚的流量标识，否则Session Hash配置不生效

        :param lb_algorithm: The lb_algorithm of this CreateHostResponse.
        :type lb_algorithm: str
        """
        self._lb_algorithm = lb_algorithm

    @property
    def protocol(self):
        """Gets the protocol of this CreateHostResponse.

        返回的客户端协议类型

        :return: The protocol of this CreateHostResponse.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this CreateHostResponse.

        返回的客户端协议类型

        :param protocol: The protocol of this CreateHostResponse.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def certificateid(self):
        """Gets the certificateid of this CreateHostResponse.

        返回的证书id

        :return: The certificateid of this CreateHostResponse.
        :rtype: str
        """
        return self._certificateid

    @certificateid.setter
    def certificateid(self, certificateid):
        """Sets the certificateid of this CreateHostResponse.

        返回的证书id

        :param certificateid: The certificateid of this CreateHostResponse.
        :type certificateid: str
        """
        self._certificateid = certificateid

    @property
    def certificatename(self):
        """Gets the certificatename of this CreateHostResponse.

        证书名称

        :return: The certificatename of this CreateHostResponse.
        :rtype: str
        """
        return self._certificatename

    @certificatename.setter
    def certificatename(self, certificatename):
        """Sets the certificatename of this CreateHostResponse.

        证书名称

        :param certificatename: The certificatename of this CreateHostResponse.
        :type certificatename: str
        """
        self._certificatename = certificatename

    @property
    def server(self):
        """Gets the server of this CreateHostResponse.

        防护域名的源站服务器配置信息

        :return: The server of this CreateHostResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.CloudWafServer`]
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this CreateHostResponse.

        防护域名的源站服务器配置信息

        :param server: The server of this CreateHostResponse.
        :type server: list[:class:`huaweicloudsdkwaf.v1.CloudWafServer`]
        """
        self._server = server

    @property
    def proxy(self):
        """Gets the proxy of this CreateHostResponse.

        防护域名是否使用代理   - false：不使用代理   - true：使用代理

        :return: The proxy of this CreateHostResponse.
        :rtype: bool
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this CreateHostResponse.

        防护域名是否使用代理   - false：不使用代理   - true：使用代理

        :param proxy: The proxy of this CreateHostResponse.
        :type proxy: bool
        """
        self._proxy = proxy

    @property
    def timestamp(self):
        """Gets the timestamp of this CreateHostResponse.

        创建防护域名的时间

        :return: The timestamp of this CreateHostResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this CreateHostResponse.

        创建防护域名的时间

        :param timestamp: The timestamp of this CreateHostResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def exclusive_ip(self):
        """Gets the exclusive_ip of this CreateHostResponse.

        是否使用独享ip   - true：使用独享ip   - false：不实用独享ip

        :return: The exclusive_ip of this CreateHostResponse.
        :rtype: bool
        """
        return self._exclusive_ip

    @exclusive_ip.setter
    def exclusive_ip(self, exclusive_ip):
        """Sets the exclusive_ip of this CreateHostResponse.

        是否使用独享ip   - true：使用独享ip   - false：不实用独享ip

        :param exclusive_ip: The exclusive_ip of this CreateHostResponse.
        :type exclusive_ip: bool
        """
        self._exclusive_ip = exclusive_ip

    @property
    def web_tag(self):
        """Gets the web_tag of this CreateHostResponse.

        网站名称，对应WAF控制台域名详情中的网站名称

        :return: The web_tag of this CreateHostResponse.
        :rtype: str
        """
        return self._web_tag

    @web_tag.setter
    def web_tag(self, web_tag):
        """Sets the web_tag of this CreateHostResponse.

        网站名称，对应WAF控制台域名详情中的网站名称

        :param web_tag: The web_tag of this CreateHostResponse.
        :type web_tag: str
        """
        self._web_tag = web_tag

    @property
    def http2_enable(self):
        """Gets the http2_enable of this CreateHostResponse.

        是否支持http2   - true：表示支持http2   - false：表示不支持http2

        :return: The http2_enable of this CreateHostResponse.
        :rtype: bool
        """
        return self._http2_enable

    @http2_enable.setter
    def http2_enable(self, http2_enable):
        """Sets the http2_enable of this CreateHostResponse.

        是否支持http2   - true：表示支持http2   - false：表示不支持http2

        :param http2_enable: The http2_enable of this CreateHostResponse.
        :type http2_enable: bool
        """
        self._http2_enable = http2_enable

    @property
    def block_page(self):
        """Gets the block_page of this CreateHostResponse.


        :return: The block_page of this CreateHostResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.BlockPage`
        """
        return self._block_page

    @block_page.setter
    def block_page(self, block_page):
        """Sets the block_page of this CreateHostResponse.


        :param block_page: The block_page of this CreateHostResponse.
        :type block_page: :class:`huaweicloudsdkwaf.v1.BlockPage`
        """
        self._block_page = block_page

    @property
    def flag(self):
        """Gets the flag of this CreateHostResponse.


        :return: The flag of this CreateHostResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.Flag`
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        """Sets the flag of this CreateHostResponse.


        :param flag: The flag of this CreateHostResponse.
        :type flag: :class:`huaweicloudsdkwaf.v1.Flag`
        """
        self._flag = flag

    @property
    def extend(self):
        """Gets the extend of this CreateHostResponse.

        扩展字段，用于保存防护域名的一些配置信息。

        :return: The extend of this CreateHostResponse.
        :rtype: dict(str, str)
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        """Sets the extend of this CreateHostResponse.

        扩展字段，用于保存防护域名的一些配置信息。

        :param extend: The extend of this CreateHostResponse.
        :type extend: dict(str, str)
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
        if not isinstance(other, CreateHostResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
