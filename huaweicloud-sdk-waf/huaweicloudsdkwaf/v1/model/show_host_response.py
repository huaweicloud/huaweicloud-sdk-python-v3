# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHostResponse(SdkResponse):

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
        'domainid': 'str',
        'projectid': 'str',
        'enterprise_project_id': 'str',
        'protocol': 'str',
        'server': 'list[CloudWafServer]',
        'proxy': 'bool',
        'protect_status': 'int',
        'access_status': 'int',
        'access_code': 'str',
        'locked': 'int',
        'timestamp': 'int',
        'certificateid': 'str',
        'certificatename': 'str',
        'tls': 'str',
        'cipher': 'str',
        'block_page': 'BlockPage',
        'extend': 'dict(str, str)',
        'traffic_mark': 'TrafficMark',
        'circuit_breaker': 'CircuitBreaker',
        'lb_algorithm': 'str',
        'timeout_config': 'TimeoutConfig',
        'web_tag': 'str',
        'flag': 'Flag',
        'description': 'str',
        'http2_enable': 'bool',
        'exclusive_ip': 'bool',
        'access_progress': 'list[AccessProgress]',
        'forward_header_map': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        'hostname': 'hostname',
        'policyid': 'policyid',
        'domainid': 'domainid',
        'projectid': 'projectid',
        'enterprise_project_id': 'enterprise_project_id',
        'protocol': 'protocol',
        'server': 'server',
        'proxy': 'proxy',
        'protect_status': 'protect_status',
        'access_status': 'access_status',
        'access_code': 'access_code',
        'locked': 'locked',
        'timestamp': 'timestamp',
        'certificateid': 'certificateid',
        'certificatename': 'certificatename',
        'tls': 'tls',
        'cipher': 'cipher',
        'block_page': 'block_page',
        'extend': 'extend',
        'traffic_mark': 'traffic_mark',
        'circuit_breaker': 'circuit_breaker',
        'lb_algorithm': 'lb_algorithm',
        'timeout_config': 'timeout_config',
        'web_tag': 'web_tag',
        'flag': 'flag',
        'description': 'description',
        'http2_enable': 'http2_enable',
        'exclusive_ip': 'exclusive_ip',
        'access_progress': 'access_progress',
        'forward_header_map': 'forward_header_map'
    }

    def __init__(self, id=None, hostname=None, policyid=None, domainid=None, projectid=None, enterprise_project_id=None, protocol=None, server=None, proxy=None, protect_status=None, access_status=None, access_code=None, locked=None, timestamp=None, certificateid=None, certificatename=None, tls=None, cipher=None, block_page=None, extend=None, traffic_mark=None, circuit_breaker=None, lb_algorithm=None, timeout_config=None, web_tag=None, flag=None, description=None, http2_enable=None, exclusive_ip=None, access_progress=None, forward_header_map=None):
        """ShowHostResponse

        The model defined in huaweicloud sdk

        :param id: 域名id
        :type id: str
        :param hostname: 创建的云模式防护域名
        :type hostname: str
        :param policyid: 防护域名的防护策略id
        :type policyid: str
        :param domainid: 帐号ID,对应华为云控制台用户名-&gt;我的凭证-&gt;帐号ID
        :type domainid: str
        :param projectid: 项目ID，对应华为云控制台用户名-&gt;我的凭证-&gt;项目列表-&gt;项目ID
        :type projectid: str
        :param enterprise_project_id: 企业项目ID，对应华为云控制台用户名-&gt;企业-&gt;项目管理-&gt;点击项目名称-&gt;ID
        :type enterprise_project_id: str
        :param protocol: 后端包含的协议类型：HTTPS、HTTP、HTTP&amp;HTTPS
        :type protocol: str
        :param server: 防护域名的源站服务器配置信息
        :type server: list[:class:`huaweicloudsdkwaf.v1.CloudWafServer`]
        :param proxy: 防护域名是否使用代理   - false：不使用代理   - true：使用代理
        :type proxy: bool
        :param protect_status: 域名防护状态：  - -1：bypass，该域名的请求直接到达其后端服务器，不再经过WAF  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测
        :type protect_status: int
        :param access_status: 域名接入状态，0表示未接入，1表示已接入
        :type access_status: int
        :param access_code: cname前缀
        :type access_code: str
        :param locked: 预留参数，用于后期设计冻结域名，解锁域名功能，目前暂不支持
        :type locked: int
        :param timestamp: 创建防护域名的时间戳（毫秒）
        :type timestamp: int
        :param certificateid: https证书id
        :type certificateid: str
        :param certificatename: 证书名称
        :type certificatename: str
        :param tls: 配置的最低TLS版本（TLS v1.0/TLS v1.1/TLS v1.2）,默认为TLS v1.0版本，对于低于最低TLS版本的请求，将无法正常访问网站
        :type tls: str
        :param cipher: 加密套件（cipher_1，cipher_2，cipher_3，cipher_4，cipher_default）：  - cipher_1： 加密算法为ECDHE-ECDSA-AES256-GCM-SHA384:HIGH:!MEDIUM:!LOW:!aNULL:!eNULL:!DES:!MD5:!PSK:!RC4:!kRSA:!SRP:!3DES:!DSS:!EXP:!CAMELLIA:@STRENGTH   - cipher_2：加密算法为EECDH+AESGCM:EDH+AESGCM   - cipher_3：加密算法为ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH   - cipher_4：加密算法为ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!EDH   - cipher_default： 加密算法为ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!AESGCM
        :type cipher: str
        :param block_page: 
        :type block_page: :class:`huaweicloudsdkwaf.v1.BlockPage`
        :param extend: 扩展字段，用于存放Web基础防护中一些开关配置等信息
        :type extend: dict(str, str)
        :param traffic_mark: 
        :type traffic_mark: :class:`huaweicloudsdkwaf.v1.TrafficMark`
        :param circuit_breaker: 
        :type circuit_breaker: :class:`huaweicloudsdkwaf.v1.CircuitBreaker`
        :param lb_algorithm: LB负载均衡，仅专业版（原企业版）和铂金版（原旗舰版）支持配置负载均衡算法   - 源IP Hash：将某个IP的请求定向到同一个服务器   - 加权轮询：所有请求将按权重轮流分配给源站服务器   - Session Hash：将某个Session标识的请求定向到同一个源站服务器，请确保在域名添加完毕后配置攻击惩罚的流量标识，否则Session Hash配置不生效
        :type lb_algorithm: str
        :param timeout_config: 
        :type timeout_config: :class:`huaweicloudsdkwaf.v1.TimeoutConfig`
        :param web_tag: 网站名称，对应WAF控制台域名详情中的网站名称
        :type web_tag: str
        :param flag: 
        :type flag: :class:`huaweicloudsdkwaf.v1.Flag`
        :param description: 网站备注
        :type description: str
        :param http2_enable: 是否支持http2   - true：表示支持http2   - false：表示不支持http2
        :type http2_enable: bool
        :param exclusive_ip: 是否使用独享ip   - true：使用独享ip   - false：不实用独享ip
        :type exclusive_ip: bool
        :param access_progress: 接入进度，仅用于新版console(前端)使用
        :type access_progress: list[:class:`huaweicloudsdkwaf.v1.AccessProgress`]
        :param forward_header_map: 字段转发配置，WAF会将添加的字段插到header中，转给源站；Key不能跟nginx原生字段重复。Value支持的值包括:   - $time_local   - $request_id   - $connection_requests   - $tenant_id   - $project_id   - $remote_addr   - $remote_port   - $scheme   - $request_method   - $http_host   -$origin_uri   - $request_length   - $ssl_server_name   - $ssl_protocol   - $ssl_curves   - $ssl_session_reused
        :type forward_header_map: dict(str, str)
        """
        
        super(ShowHostResponse, self).__init__()

        self._id = None
        self._hostname = None
        self._policyid = None
        self._domainid = None
        self._projectid = None
        self._enterprise_project_id = None
        self._protocol = None
        self._server = None
        self._proxy = None
        self._protect_status = None
        self._access_status = None
        self._access_code = None
        self._locked = None
        self._timestamp = None
        self._certificateid = None
        self._certificatename = None
        self._tls = None
        self._cipher = None
        self._block_page = None
        self._extend = None
        self._traffic_mark = None
        self._circuit_breaker = None
        self._lb_algorithm = None
        self._timeout_config = None
        self._web_tag = None
        self._flag = None
        self._description = None
        self._http2_enable = None
        self._exclusive_ip = None
        self._access_progress = None
        self._forward_header_map = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if hostname is not None:
            self.hostname = hostname
        if policyid is not None:
            self.policyid = policyid
        if domainid is not None:
            self.domainid = domainid
        if projectid is not None:
            self.projectid = projectid
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if protocol is not None:
            self.protocol = protocol
        if server is not None:
            self.server = server
        if proxy is not None:
            self.proxy = proxy
        if protect_status is not None:
            self.protect_status = protect_status
        if access_status is not None:
            self.access_status = access_status
        if access_code is not None:
            self.access_code = access_code
        if locked is not None:
            self.locked = locked
        if timestamp is not None:
            self.timestamp = timestamp
        if certificateid is not None:
            self.certificateid = certificateid
        if certificatename is not None:
            self.certificatename = certificatename
        if tls is not None:
            self.tls = tls
        if cipher is not None:
            self.cipher = cipher
        if block_page is not None:
            self.block_page = block_page
        if extend is not None:
            self.extend = extend
        if traffic_mark is not None:
            self.traffic_mark = traffic_mark
        if circuit_breaker is not None:
            self.circuit_breaker = circuit_breaker
        if lb_algorithm is not None:
            self.lb_algorithm = lb_algorithm
        if timeout_config is not None:
            self.timeout_config = timeout_config
        if web_tag is not None:
            self.web_tag = web_tag
        if flag is not None:
            self.flag = flag
        if description is not None:
            self.description = description
        if http2_enable is not None:
            self.http2_enable = http2_enable
        if exclusive_ip is not None:
            self.exclusive_ip = exclusive_ip
        if access_progress is not None:
            self.access_progress = access_progress
        if forward_header_map is not None:
            self.forward_header_map = forward_header_map

    @property
    def id(self):
        """Gets the id of this ShowHostResponse.

        域名id

        :return: The id of this ShowHostResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowHostResponse.

        域名id

        :param id: The id of this ShowHostResponse.
        :type id: str
        """
        self._id = id

    @property
    def hostname(self):
        """Gets the hostname of this ShowHostResponse.

        创建的云模式防护域名

        :return: The hostname of this ShowHostResponse.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this ShowHostResponse.

        创建的云模式防护域名

        :param hostname: The hostname of this ShowHostResponse.
        :type hostname: str
        """
        self._hostname = hostname

    @property
    def policyid(self):
        """Gets the policyid of this ShowHostResponse.

        防护域名的防护策略id

        :return: The policyid of this ShowHostResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this ShowHostResponse.

        防护域名的防护策略id

        :param policyid: The policyid of this ShowHostResponse.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def domainid(self):
        """Gets the domainid of this ShowHostResponse.

        帐号ID,对应华为云控制台用户名->我的凭证->帐号ID

        :return: The domainid of this ShowHostResponse.
        :rtype: str
        """
        return self._domainid

    @domainid.setter
    def domainid(self, domainid):
        """Sets the domainid of this ShowHostResponse.

        帐号ID,对应华为云控制台用户名->我的凭证->帐号ID

        :param domainid: The domainid of this ShowHostResponse.
        :type domainid: str
        """
        self._domainid = domainid

    @property
    def projectid(self):
        """Gets the projectid of this ShowHostResponse.

        项目ID，对应华为云控制台用户名->我的凭证->项目列表->项目ID

        :return: The projectid of this ShowHostResponse.
        :rtype: str
        """
        return self._projectid

    @projectid.setter
    def projectid(self, projectid):
        """Sets the projectid of this ShowHostResponse.

        项目ID，对应华为云控制台用户名->我的凭证->项目列表->项目ID

        :param projectid: The projectid of this ShowHostResponse.
        :type projectid: str
        """
        self._projectid = projectid

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowHostResponse.

        企业项目ID，对应华为云控制台用户名->企业->项目管理->点击项目名称->ID

        :return: The enterprise_project_id of this ShowHostResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowHostResponse.

        企业项目ID，对应华为云控制台用户名->企业->项目管理->点击项目名称->ID

        :param enterprise_project_id: The enterprise_project_id of this ShowHostResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def protocol(self):
        """Gets the protocol of this ShowHostResponse.

        后端包含的协议类型：HTTPS、HTTP、HTTP&HTTPS

        :return: The protocol of this ShowHostResponse.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ShowHostResponse.

        后端包含的协议类型：HTTPS、HTTP、HTTP&HTTPS

        :param protocol: The protocol of this ShowHostResponse.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def server(self):
        """Gets the server of this ShowHostResponse.

        防护域名的源站服务器配置信息

        :return: The server of this ShowHostResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.CloudWafServer`]
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this ShowHostResponse.

        防护域名的源站服务器配置信息

        :param server: The server of this ShowHostResponse.
        :type server: list[:class:`huaweicloudsdkwaf.v1.CloudWafServer`]
        """
        self._server = server

    @property
    def proxy(self):
        """Gets the proxy of this ShowHostResponse.

        防护域名是否使用代理   - false：不使用代理   - true：使用代理

        :return: The proxy of this ShowHostResponse.
        :rtype: bool
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this ShowHostResponse.

        防护域名是否使用代理   - false：不使用代理   - true：使用代理

        :param proxy: The proxy of this ShowHostResponse.
        :type proxy: bool
        """
        self._proxy = proxy

    @property
    def protect_status(self):
        """Gets the protect_status of this ShowHostResponse.

        域名防护状态：  - -1：bypass，该域名的请求直接到达其后端服务器，不再经过WAF  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测

        :return: The protect_status of this ShowHostResponse.
        :rtype: int
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this ShowHostResponse.

        域名防护状态：  - -1：bypass，该域名的请求直接到达其后端服务器，不再经过WAF  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测

        :param protect_status: The protect_status of this ShowHostResponse.
        :type protect_status: int
        """
        self._protect_status = protect_status

    @property
    def access_status(self):
        """Gets the access_status of this ShowHostResponse.

        域名接入状态，0表示未接入，1表示已接入

        :return: The access_status of this ShowHostResponse.
        :rtype: int
        """
        return self._access_status

    @access_status.setter
    def access_status(self, access_status):
        """Sets the access_status of this ShowHostResponse.

        域名接入状态，0表示未接入，1表示已接入

        :param access_status: The access_status of this ShowHostResponse.
        :type access_status: int
        """
        self._access_status = access_status

    @property
    def access_code(self):
        """Gets the access_code of this ShowHostResponse.

        cname前缀

        :return: The access_code of this ShowHostResponse.
        :rtype: str
        """
        return self._access_code

    @access_code.setter
    def access_code(self, access_code):
        """Sets the access_code of this ShowHostResponse.

        cname前缀

        :param access_code: The access_code of this ShowHostResponse.
        :type access_code: str
        """
        self._access_code = access_code

    @property
    def locked(self):
        """Gets the locked of this ShowHostResponse.

        预留参数，用于后期设计冻结域名，解锁域名功能，目前暂不支持

        :return: The locked of this ShowHostResponse.
        :rtype: int
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this ShowHostResponse.

        预留参数，用于后期设计冻结域名，解锁域名功能，目前暂不支持

        :param locked: The locked of this ShowHostResponse.
        :type locked: int
        """
        self._locked = locked

    @property
    def timestamp(self):
        """Gets the timestamp of this ShowHostResponse.

        创建防护域名的时间戳（毫秒）

        :return: The timestamp of this ShowHostResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ShowHostResponse.

        创建防护域名的时间戳（毫秒）

        :param timestamp: The timestamp of this ShowHostResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def certificateid(self):
        """Gets the certificateid of this ShowHostResponse.

        https证书id

        :return: The certificateid of this ShowHostResponse.
        :rtype: str
        """
        return self._certificateid

    @certificateid.setter
    def certificateid(self, certificateid):
        """Sets the certificateid of this ShowHostResponse.

        https证书id

        :param certificateid: The certificateid of this ShowHostResponse.
        :type certificateid: str
        """
        self._certificateid = certificateid

    @property
    def certificatename(self):
        """Gets the certificatename of this ShowHostResponse.

        证书名称

        :return: The certificatename of this ShowHostResponse.
        :rtype: str
        """
        return self._certificatename

    @certificatename.setter
    def certificatename(self, certificatename):
        """Sets the certificatename of this ShowHostResponse.

        证书名称

        :param certificatename: The certificatename of this ShowHostResponse.
        :type certificatename: str
        """
        self._certificatename = certificatename

    @property
    def tls(self):
        """Gets the tls of this ShowHostResponse.

        配置的最低TLS版本（TLS v1.0/TLS v1.1/TLS v1.2）,默认为TLS v1.0版本，对于低于最低TLS版本的请求，将无法正常访问网站

        :return: The tls of this ShowHostResponse.
        :rtype: str
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """Sets the tls of this ShowHostResponse.

        配置的最低TLS版本（TLS v1.0/TLS v1.1/TLS v1.2）,默认为TLS v1.0版本，对于低于最低TLS版本的请求，将无法正常访问网站

        :param tls: The tls of this ShowHostResponse.
        :type tls: str
        """
        self._tls = tls

    @property
    def cipher(self):
        """Gets the cipher of this ShowHostResponse.

        加密套件（cipher_1，cipher_2，cipher_3，cipher_4，cipher_default）：  - cipher_1： 加密算法为ECDHE-ECDSA-AES256-GCM-SHA384:HIGH:!MEDIUM:!LOW:!aNULL:!eNULL:!DES:!MD5:!PSK:!RC4:!kRSA:!SRP:!3DES:!DSS:!EXP:!CAMELLIA:@STRENGTH   - cipher_2：加密算法为EECDH+AESGCM:EDH+AESGCM   - cipher_3：加密算法为ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH   - cipher_4：加密算法为ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!EDH   - cipher_default： 加密算法为ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!AESGCM

        :return: The cipher of this ShowHostResponse.
        :rtype: str
        """
        return self._cipher

    @cipher.setter
    def cipher(self, cipher):
        """Sets the cipher of this ShowHostResponse.

        加密套件（cipher_1，cipher_2，cipher_3，cipher_4，cipher_default）：  - cipher_1： 加密算法为ECDHE-ECDSA-AES256-GCM-SHA384:HIGH:!MEDIUM:!LOW:!aNULL:!eNULL:!DES:!MD5:!PSK:!RC4:!kRSA:!SRP:!3DES:!DSS:!EXP:!CAMELLIA:@STRENGTH   - cipher_2：加密算法为EECDH+AESGCM:EDH+AESGCM   - cipher_3：加密算法为ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH   - cipher_4：加密算法为ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!EDH   - cipher_default： 加密算法为ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!AESGCM

        :param cipher: The cipher of this ShowHostResponse.
        :type cipher: str
        """
        self._cipher = cipher

    @property
    def block_page(self):
        """Gets the block_page of this ShowHostResponse.

        :return: The block_page of this ShowHostResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.BlockPage`
        """
        return self._block_page

    @block_page.setter
    def block_page(self, block_page):
        """Sets the block_page of this ShowHostResponse.

        :param block_page: The block_page of this ShowHostResponse.
        :type block_page: :class:`huaweicloudsdkwaf.v1.BlockPage`
        """
        self._block_page = block_page

    @property
    def extend(self):
        """Gets the extend of this ShowHostResponse.

        扩展字段，用于存放Web基础防护中一些开关配置等信息

        :return: The extend of this ShowHostResponse.
        :rtype: dict(str, str)
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        """Sets the extend of this ShowHostResponse.

        扩展字段，用于存放Web基础防护中一些开关配置等信息

        :param extend: The extend of this ShowHostResponse.
        :type extend: dict(str, str)
        """
        self._extend = extend

    @property
    def traffic_mark(self):
        """Gets the traffic_mark of this ShowHostResponse.

        :return: The traffic_mark of this ShowHostResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.TrafficMark`
        """
        return self._traffic_mark

    @traffic_mark.setter
    def traffic_mark(self, traffic_mark):
        """Sets the traffic_mark of this ShowHostResponse.

        :param traffic_mark: The traffic_mark of this ShowHostResponse.
        :type traffic_mark: :class:`huaweicloudsdkwaf.v1.TrafficMark`
        """
        self._traffic_mark = traffic_mark

    @property
    def circuit_breaker(self):
        """Gets the circuit_breaker of this ShowHostResponse.

        :return: The circuit_breaker of this ShowHostResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.CircuitBreaker`
        """
        return self._circuit_breaker

    @circuit_breaker.setter
    def circuit_breaker(self, circuit_breaker):
        """Sets the circuit_breaker of this ShowHostResponse.

        :param circuit_breaker: The circuit_breaker of this ShowHostResponse.
        :type circuit_breaker: :class:`huaweicloudsdkwaf.v1.CircuitBreaker`
        """
        self._circuit_breaker = circuit_breaker

    @property
    def lb_algorithm(self):
        """Gets the lb_algorithm of this ShowHostResponse.

        LB负载均衡，仅专业版（原企业版）和铂金版（原旗舰版）支持配置负载均衡算法   - 源IP Hash：将某个IP的请求定向到同一个服务器   - 加权轮询：所有请求将按权重轮流分配给源站服务器   - Session Hash：将某个Session标识的请求定向到同一个源站服务器，请确保在域名添加完毕后配置攻击惩罚的流量标识，否则Session Hash配置不生效

        :return: The lb_algorithm of this ShowHostResponse.
        :rtype: str
        """
        return self._lb_algorithm

    @lb_algorithm.setter
    def lb_algorithm(self, lb_algorithm):
        """Sets the lb_algorithm of this ShowHostResponse.

        LB负载均衡，仅专业版（原企业版）和铂金版（原旗舰版）支持配置负载均衡算法   - 源IP Hash：将某个IP的请求定向到同一个服务器   - 加权轮询：所有请求将按权重轮流分配给源站服务器   - Session Hash：将某个Session标识的请求定向到同一个源站服务器，请确保在域名添加完毕后配置攻击惩罚的流量标识，否则Session Hash配置不生效

        :param lb_algorithm: The lb_algorithm of this ShowHostResponse.
        :type lb_algorithm: str
        """
        self._lb_algorithm = lb_algorithm

    @property
    def timeout_config(self):
        """Gets the timeout_config of this ShowHostResponse.

        :return: The timeout_config of this ShowHostResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.TimeoutConfig`
        """
        return self._timeout_config

    @timeout_config.setter
    def timeout_config(self, timeout_config):
        """Sets the timeout_config of this ShowHostResponse.

        :param timeout_config: The timeout_config of this ShowHostResponse.
        :type timeout_config: :class:`huaweicloudsdkwaf.v1.TimeoutConfig`
        """
        self._timeout_config = timeout_config

    @property
    def web_tag(self):
        """Gets the web_tag of this ShowHostResponse.

        网站名称，对应WAF控制台域名详情中的网站名称

        :return: The web_tag of this ShowHostResponse.
        :rtype: str
        """
        return self._web_tag

    @web_tag.setter
    def web_tag(self, web_tag):
        """Sets the web_tag of this ShowHostResponse.

        网站名称，对应WAF控制台域名详情中的网站名称

        :param web_tag: The web_tag of this ShowHostResponse.
        :type web_tag: str
        """
        self._web_tag = web_tag

    @property
    def flag(self):
        """Gets the flag of this ShowHostResponse.

        :return: The flag of this ShowHostResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.Flag`
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        """Sets the flag of this ShowHostResponse.

        :param flag: The flag of this ShowHostResponse.
        :type flag: :class:`huaweicloudsdkwaf.v1.Flag`
        """
        self._flag = flag

    @property
    def description(self):
        """Gets the description of this ShowHostResponse.

        网站备注

        :return: The description of this ShowHostResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowHostResponse.

        网站备注

        :param description: The description of this ShowHostResponse.
        :type description: str
        """
        self._description = description

    @property
    def http2_enable(self):
        """Gets the http2_enable of this ShowHostResponse.

        是否支持http2   - true：表示支持http2   - false：表示不支持http2

        :return: The http2_enable of this ShowHostResponse.
        :rtype: bool
        """
        return self._http2_enable

    @http2_enable.setter
    def http2_enable(self, http2_enable):
        """Sets the http2_enable of this ShowHostResponse.

        是否支持http2   - true：表示支持http2   - false：表示不支持http2

        :param http2_enable: The http2_enable of this ShowHostResponse.
        :type http2_enable: bool
        """
        self._http2_enable = http2_enable

    @property
    def exclusive_ip(self):
        """Gets the exclusive_ip of this ShowHostResponse.

        是否使用独享ip   - true：使用独享ip   - false：不实用独享ip

        :return: The exclusive_ip of this ShowHostResponse.
        :rtype: bool
        """
        return self._exclusive_ip

    @exclusive_ip.setter
    def exclusive_ip(self, exclusive_ip):
        """Sets the exclusive_ip of this ShowHostResponse.

        是否使用独享ip   - true：使用独享ip   - false：不实用独享ip

        :param exclusive_ip: The exclusive_ip of this ShowHostResponse.
        :type exclusive_ip: bool
        """
        self._exclusive_ip = exclusive_ip

    @property
    def access_progress(self):
        """Gets the access_progress of this ShowHostResponse.

        接入进度，仅用于新版console(前端)使用

        :return: The access_progress of this ShowHostResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.AccessProgress`]
        """
        return self._access_progress

    @access_progress.setter
    def access_progress(self, access_progress):
        """Sets the access_progress of this ShowHostResponse.

        接入进度，仅用于新版console(前端)使用

        :param access_progress: The access_progress of this ShowHostResponse.
        :type access_progress: list[:class:`huaweicloudsdkwaf.v1.AccessProgress`]
        """
        self._access_progress = access_progress

    @property
    def forward_header_map(self):
        """Gets the forward_header_map of this ShowHostResponse.

        字段转发配置，WAF会将添加的字段插到header中，转给源站；Key不能跟nginx原生字段重复。Value支持的值包括:   - $time_local   - $request_id   - $connection_requests   - $tenant_id   - $project_id   - $remote_addr   - $remote_port   - $scheme   - $request_method   - $http_host   -$origin_uri   - $request_length   - $ssl_server_name   - $ssl_protocol   - $ssl_curves   - $ssl_session_reused

        :return: The forward_header_map of this ShowHostResponse.
        :rtype: dict(str, str)
        """
        return self._forward_header_map

    @forward_header_map.setter
    def forward_header_map(self, forward_header_map):
        """Sets the forward_header_map of this ShowHostResponse.

        字段转发配置，WAF会将添加的字段插到header中，转给源站；Key不能跟nginx原生字段重复。Value支持的值包括:   - $time_local   - $request_id   - $connection_requests   - $tenant_id   - $project_id   - $remote_addr   - $remote_port   - $scheme   - $request_method   - $http_host   -$origin_uri   - $request_length   - $ssl_server_name   - $ssl_protocol   - $ssl_curves   - $ssl_session_reused

        :param forward_header_map: The forward_header_map of this ShowHostResponse.
        :type forward_header_map: dict(str, str)
        """
        self._forward_header_map = forward_header_map

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
        if not isinstance(other, ShowHostResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
