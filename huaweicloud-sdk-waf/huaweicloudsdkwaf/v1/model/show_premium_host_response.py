# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPremiumHostResponse(SdkResponse):

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
        'protocol': 'str',
        'server': 'list[PremiumWafServer]',
        'proxy': 'bool',
        'locked': 'int',
        'timestamp': 'int',
        'tls': 'str',
        'cipher': 'str',
        'extend': 'dict(str, str)',
        'flag': 'Flag',
        'description': 'str',
        'policyid': 'str',
        'domainid': 'str',
        'projectid': 'str',
        'enterprise_project_id': 'str',
        'certificateid': 'str',
        'certificatename': 'str',
        'protect_status': 'int',
        'access_status': 'int',
        'web_tag': 'str',
        'block_page': 'BlockPage',
        'traffic_mark': 'TrafficMark',
        'timeout_config': 'TimeoutConfig',
        'forward_header_map': 'dict(str, str)',
        'access_progress': 'list[AccessProgress]'
    }

    attribute_map = {
        'id': 'id',
        'hostname': 'hostname',
        'protocol': 'protocol',
        'server': 'server',
        'proxy': 'proxy',
        'locked': 'locked',
        'timestamp': 'timestamp',
        'tls': 'tls',
        'cipher': 'cipher',
        'extend': 'extend',
        'flag': 'flag',
        'description': 'description',
        'policyid': 'policyid',
        'domainid': 'domainid',
        'projectid': 'projectid',
        'enterprise_project_id': 'enterprise_project_id',
        'certificateid': 'certificateid',
        'certificatename': 'certificatename',
        'protect_status': 'protect_status',
        'access_status': 'access_status',
        'web_tag': 'web_tag',
        'block_page': 'block_page',
        'traffic_mark': 'traffic_mark',
        'timeout_config': 'timeout_config',
        'forward_header_map': 'forward_header_map',
        'access_progress': 'access_progress'
    }

    def __init__(self, id=None, hostname=None, protocol=None, server=None, proxy=None, locked=None, timestamp=None, tls=None, cipher=None, extend=None, flag=None, description=None, policyid=None, domainid=None, projectid=None, enterprise_project_id=None, certificateid=None, certificatename=None, protect_status=None, access_status=None, web_tag=None, block_page=None, traffic_mark=None, timeout_config=None, forward_header_map=None, access_progress=None):
        """ShowPremiumHostResponse

        The model defined in huaweicloud sdk

        :param id: 域名id
        :type id: str
        :param hostname: 创建的独享模式防护域名
        :type hostname: str
        :param protocol: 对外协议，客户端（例如浏览器）请求访问网站的协议类型
        :type protocol: str
        :param server: 防护域名的源站服务器配置信息
        :type server: list[:class:`huaweicloudsdkwaf.v1.PremiumWafServer`]
        :param proxy: 防护域名是否使用代理   - false：不使用代理   - true：使用代理
        :type proxy: bool
        :param locked: 预留参数，用于后期设计冻结域名，解锁域名功能，目前暂不支持
        :type locked: int
        :param timestamp: 创建防护域名的时间
        :type timestamp: int
        :param tls: 配置的最低TLS版本（TLS v1.0/TLS v1.1/TLS v1.2）,默认为TLS v1.0版本，对外协议为https时才有tls参数
        :type tls: str
        :param cipher: 对外协议为https时才有cipher参数，加密套件（cipher_1，cipher_2，cipher_3，cipher_4，cipher_default）：  - cipher_1： 加密算法为ECDHE-ECDSA-AES256-GCM-SHA384:HIGH:!MEDIUM:!LOW:!aNULL:!eNULL:!DES:!MD5:!PSK:!RC4:!kRSA:!SRP:!3DES:!DSS:!EXP:!CAMELLIA:@STRENGTH   - cipher_2：加密算法为EECDH+AESGCM:EDH+AESGCM   - cipher_3：加密算法为ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH   - cipher_4：加密算法为ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!EDH   - cipher_default： 加密算法为ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!AESGCM
        :type cipher: str
        :param extend: 扩展字段，用于保存防护域名的一些配置信息。
        :type extend: dict(str, str)
        :param flag: 
        :type flag: :class:`huaweicloudsdkwaf.v1.Flag`
        :param description: 域名描述
        :type description: str
        :param policyid: 防护域名初始绑定的策略ID,可以通过策略名称调用查询防护策略列表（ListPolicy）接口查询到对应的策略id
        :type policyid: str
        :param domainid: 帐号ID,对应华为云控制台用户名-&gt;我的凭证-&gt;帐号ID
        :type domainid: str
        :param projectid: 项目ID，对应华为云控制台用户名-&gt;我的凭证-&gt;项目列表-&gt;项目ID
        :type projectid: str
        :param enterprise_project_id: 企业项目ID，对应华为云控制台用户名-&gt;企业-&gt;项目管理-&gt;点击项目名称-&gt;ID
        :type enterprise_project_id: str
        :param certificateid: https证书id
        :type certificateid: str
        :param certificatename: 证书名称
        :type certificatename: str
        :param protect_status: 域名防护状态：  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测
        :type protect_status: int
        :param access_status: 域名接入状态，0表示未接入，1表示已接入
        :type access_status: int
        :param web_tag: 网站名称，对应WAF控制台域名详情中的网站名称
        :type web_tag: str
        :param block_page: 
        :type block_page: :class:`huaweicloudsdkwaf.v1.BlockPage`
        :param traffic_mark: 
        :type traffic_mark: :class:`huaweicloudsdkwaf.v1.TrafficMark`
        :param timeout_config: 
        :type timeout_config: :class:`huaweicloudsdkwaf.v1.TimeoutConfig`
        :param forward_header_map: 字段转发配置，WAF会将添加的字段插到header中，转给源站；Key不能跟nginx原生字段重复。Value支持的值包括:   - $time_local   - $request_id   - $connection_requests   - $tenant_id   - $project_id   - $remote_addr   - $remote_port   - $scheme   - $request_method   - $http_host   -$origin_uri   - $request_length   - $ssl_server_name   - $ssl_protocol   - $ssl_curves   - $ssl_session_reused
        :type forward_header_map: dict(str, str)
        :param access_progress: 接入进度，仅用于新版console(前端)使用
        :type access_progress: list[:class:`huaweicloudsdkwaf.v1.AccessProgress`]
        """
        
        super(ShowPremiumHostResponse, self).__init__()

        self._id = None
        self._hostname = None
        self._protocol = None
        self._server = None
        self._proxy = None
        self._locked = None
        self._timestamp = None
        self._tls = None
        self._cipher = None
        self._extend = None
        self._flag = None
        self._description = None
        self._policyid = None
        self._domainid = None
        self._projectid = None
        self._enterprise_project_id = None
        self._certificateid = None
        self._certificatename = None
        self._protect_status = None
        self._access_status = None
        self._web_tag = None
        self._block_page = None
        self._traffic_mark = None
        self._timeout_config = None
        self._forward_header_map = None
        self._access_progress = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if hostname is not None:
            self.hostname = hostname
        if protocol is not None:
            self.protocol = protocol
        if server is not None:
            self.server = server
        if proxy is not None:
            self.proxy = proxy
        if locked is not None:
            self.locked = locked
        if timestamp is not None:
            self.timestamp = timestamp
        if tls is not None:
            self.tls = tls
        if cipher is not None:
            self.cipher = cipher
        if extend is not None:
            self.extend = extend
        if flag is not None:
            self.flag = flag
        if description is not None:
            self.description = description
        if policyid is not None:
            self.policyid = policyid
        if domainid is not None:
            self.domainid = domainid
        if projectid is not None:
            self.projectid = projectid
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if certificateid is not None:
            self.certificateid = certificateid
        if certificatename is not None:
            self.certificatename = certificatename
        if protect_status is not None:
            self.protect_status = protect_status
        if access_status is not None:
            self.access_status = access_status
        if web_tag is not None:
            self.web_tag = web_tag
        if block_page is not None:
            self.block_page = block_page
        if traffic_mark is not None:
            self.traffic_mark = traffic_mark
        if timeout_config is not None:
            self.timeout_config = timeout_config
        if forward_header_map is not None:
            self.forward_header_map = forward_header_map
        if access_progress is not None:
            self.access_progress = access_progress

    @property
    def id(self):
        """Gets the id of this ShowPremiumHostResponse.

        域名id

        :return: The id of this ShowPremiumHostResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowPremiumHostResponse.

        域名id

        :param id: The id of this ShowPremiumHostResponse.
        :type id: str
        """
        self._id = id

    @property
    def hostname(self):
        """Gets the hostname of this ShowPremiumHostResponse.

        创建的独享模式防护域名

        :return: The hostname of this ShowPremiumHostResponse.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this ShowPremiumHostResponse.

        创建的独享模式防护域名

        :param hostname: The hostname of this ShowPremiumHostResponse.
        :type hostname: str
        """
        self._hostname = hostname

    @property
    def protocol(self):
        """Gets the protocol of this ShowPremiumHostResponse.

        对外协议，客户端（例如浏览器）请求访问网站的协议类型

        :return: The protocol of this ShowPremiumHostResponse.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ShowPremiumHostResponse.

        对外协议，客户端（例如浏览器）请求访问网站的协议类型

        :param protocol: The protocol of this ShowPremiumHostResponse.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def server(self):
        """Gets the server of this ShowPremiumHostResponse.

        防护域名的源站服务器配置信息

        :return: The server of this ShowPremiumHostResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.PremiumWafServer`]
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this ShowPremiumHostResponse.

        防护域名的源站服务器配置信息

        :param server: The server of this ShowPremiumHostResponse.
        :type server: list[:class:`huaweicloudsdkwaf.v1.PremiumWafServer`]
        """
        self._server = server

    @property
    def proxy(self):
        """Gets the proxy of this ShowPremiumHostResponse.

        防护域名是否使用代理   - false：不使用代理   - true：使用代理

        :return: The proxy of this ShowPremiumHostResponse.
        :rtype: bool
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this ShowPremiumHostResponse.

        防护域名是否使用代理   - false：不使用代理   - true：使用代理

        :param proxy: The proxy of this ShowPremiumHostResponse.
        :type proxy: bool
        """
        self._proxy = proxy

    @property
    def locked(self):
        """Gets the locked of this ShowPremiumHostResponse.

        预留参数，用于后期设计冻结域名，解锁域名功能，目前暂不支持

        :return: The locked of this ShowPremiumHostResponse.
        :rtype: int
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this ShowPremiumHostResponse.

        预留参数，用于后期设计冻结域名，解锁域名功能，目前暂不支持

        :param locked: The locked of this ShowPremiumHostResponse.
        :type locked: int
        """
        self._locked = locked

    @property
    def timestamp(self):
        """Gets the timestamp of this ShowPremiumHostResponse.

        创建防护域名的时间

        :return: The timestamp of this ShowPremiumHostResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ShowPremiumHostResponse.

        创建防护域名的时间

        :param timestamp: The timestamp of this ShowPremiumHostResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def tls(self):
        """Gets the tls of this ShowPremiumHostResponse.

        配置的最低TLS版本（TLS v1.0/TLS v1.1/TLS v1.2）,默认为TLS v1.0版本，对外协议为https时才有tls参数

        :return: The tls of this ShowPremiumHostResponse.
        :rtype: str
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """Sets the tls of this ShowPremiumHostResponse.

        配置的最低TLS版本（TLS v1.0/TLS v1.1/TLS v1.2）,默认为TLS v1.0版本，对外协议为https时才有tls参数

        :param tls: The tls of this ShowPremiumHostResponse.
        :type tls: str
        """
        self._tls = tls

    @property
    def cipher(self):
        """Gets the cipher of this ShowPremiumHostResponse.

        对外协议为https时才有cipher参数，加密套件（cipher_1，cipher_2，cipher_3，cipher_4，cipher_default）：  - cipher_1： 加密算法为ECDHE-ECDSA-AES256-GCM-SHA384:HIGH:!MEDIUM:!LOW:!aNULL:!eNULL:!DES:!MD5:!PSK:!RC4:!kRSA:!SRP:!3DES:!DSS:!EXP:!CAMELLIA:@STRENGTH   - cipher_2：加密算法为EECDH+AESGCM:EDH+AESGCM   - cipher_3：加密算法为ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH   - cipher_4：加密算法为ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!EDH   - cipher_default： 加密算法为ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!AESGCM

        :return: The cipher of this ShowPremiumHostResponse.
        :rtype: str
        """
        return self._cipher

    @cipher.setter
    def cipher(self, cipher):
        """Sets the cipher of this ShowPremiumHostResponse.

        对外协议为https时才有cipher参数，加密套件（cipher_1，cipher_2，cipher_3，cipher_4，cipher_default）：  - cipher_1： 加密算法为ECDHE-ECDSA-AES256-GCM-SHA384:HIGH:!MEDIUM:!LOW:!aNULL:!eNULL:!DES:!MD5:!PSK:!RC4:!kRSA:!SRP:!3DES:!DSS:!EXP:!CAMELLIA:@STRENGTH   - cipher_2：加密算法为EECDH+AESGCM:EDH+AESGCM   - cipher_3：加密算法为ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH   - cipher_4：加密算法为ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!EDH   - cipher_default： 加密算法为ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!AESGCM

        :param cipher: The cipher of this ShowPremiumHostResponse.
        :type cipher: str
        """
        self._cipher = cipher

    @property
    def extend(self):
        """Gets the extend of this ShowPremiumHostResponse.

        扩展字段，用于保存防护域名的一些配置信息。

        :return: The extend of this ShowPremiumHostResponse.
        :rtype: dict(str, str)
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        """Sets the extend of this ShowPremiumHostResponse.

        扩展字段，用于保存防护域名的一些配置信息。

        :param extend: The extend of this ShowPremiumHostResponse.
        :type extend: dict(str, str)
        """
        self._extend = extend

    @property
    def flag(self):
        """Gets the flag of this ShowPremiumHostResponse.

        :return: The flag of this ShowPremiumHostResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.Flag`
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        """Sets the flag of this ShowPremiumHostResponse.

        :param flag: The flag of this ShowPremiumHostResponse.
        :type flag: :class:`huaweicloudsdkwaf.v1.Flag`
        """
        self._flag = flag

    @property
    def description(self):
        """Gets the description of this ShowPremiumHostResponse.

        域名描述

        :return: The description of this ShowPremiumHostResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowPremiumHostResponse.

        域名描述

        :param description: The description of this ShowPremiumHostResponse.
        :type description: str
        """
        self._description = description

    @property
    def policyid(self):
        """Gets the policyid of this ShowPremiumHostResponse.

        防护域名初始绑定的策略ID,可以通过策略名称调用查询防护策略列表（ListPolicy）接口查询到对应的策略id

        :return: The policyid of this ShowPremiumHostResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this ShowPremiumHostResponse.

        防护域名初始绑定的策略ID,可以通过策略名称调用查询防护策略列表（ListPolicy）接口查询到对应的策略id

        :param policyid: The policyid of this ShowPremiumHostResponse.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def domainid(self):
        """Gets the domainid of this ShowPremiumHostResponse.

        帐号ID,对应华为云控制台用户名->我的凭证->帐号ID

        :return: The domainid of this ShowPremiumHostResponse.
        :rtype: str
        """
        return self._domainid

    @domainid.setter
    def domainid(self, domainid):
        """Sets the domainid of this ShowPremiumHostResponse.

        帐号ID,对应华为云控制台用户名->我的凭证->帐号ID

        :param domainid: The domainid of this ShowPremiumHostResponse.
        :type domainid: str
        """
        self._domainid = domainid

    @property
    def projectid(self):
        """Gets the projectid of this ShowPremiumHostResponse.

        项目ID，对应华为云控制台用户名->我的凭证->项目列表->项目ID

        :return: The projectid of this ShowPremiumHostResponse.
        :rtype: str
        """
        return self._projectid

    @projectid.setter
    def projectid(self, projectid):
        """Sets the projectid of this ShowPremiumHostResponse.

        项目ID，对应华为云控制台用户名->我的凭证->项目列表->项目ID

        :param projectid: The projectid of this ShowPremiumHostResponse.
        :type projectid: str
        """
        self._projectid = projectid

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowPremiumHostResponse.

        企业项目ID，对应华为云控制台用户名->企业->项目管理->点击项目名称->ID

        :return: The enterprise_project_id of this ShowPremiumHostResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowPremiumHostResponse.

        企业项目ID，对应华为云控制台用户名->企业->项目管理->点击项目名称->ID

        :param enterprise_project_id: The enterprise_project_id of this ShowPremiumHostResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def certificateid(self):
        """Gets the certificateid of this ShowPremiumHostResponse.

        https证书id

        :return: The certificateid of this ShowPremiumHostResponse.
        :rtype: str
        """
        return self._certificateid

    @certificateid.setter
    def certificateid(self, certificateid):
        """Sets the certificateid of this ShowPremiumHostResponse.

        https证书id

        :param certificateid: The certificateid of this ShowPremiumHostResponse.
        :type certificateid: str
        """
        self._certificateid = certificateid

    @property
    def certificatename(self):
        """Gets the certificatename of this ShowPremiumHostResponse.

        证书名称

        :return: The certificatename of this ShowPremiumHostResponse.
        :rtype: str
        """
        return self._certificatename

    @certificatename.setter
    def certificatename(self, certificatename):
        """Sets the certificatename of this ShowPremiumHostResponse.

        证书名称

        :param certificatename: The certificatename of this ShowPremiumHostResponse.
        :type certificatename: str
        """
        self._certificatename = certificatename

    @property
    def protect_status(self):
        """Gets the protect_status of this ShowPremiumHostResponse.

        域名防护状态：  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测

        :return: The protect_status of this ShowPremiumHostResponse.
        :rtype: int
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this ShowPremiumHostResponse.

        域名防护状态：  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测

        :param protect_status: The protect_status of this ShowPremiumHostResponse.
        :type protect_status: int
        """
        self._protect_status = protect_status

    @property
    def access_status(self):
        """Gets the access_status of this ShowPremiumHostResponse.

        域名接入状态，0表示未接入，1表示已接入

        :return: The access_status of this ShowPremiumHostResponse.
        :rtype: int
        """
        return self._access_status

    @access_status.setter
    def access_status(self, access_status):
        """Sets the access_status of this ShowPremiumHostResponse.

        域名接入状态，0表示未接入，1表示已接入

        :param access_status: The access_status of this ShowPremiumHostResponse.
        :type access_status: int
        """
        self._access_status = access_status

    @property
    def web_tag(self):
        """Gets the web_tag of this ShowPremiumHostResponse.

        网站名称，对应WAF控制台域名详情中的网站名称

        :return: The web_tag of this ShowPremiumHostResponse.
        :rtype: str
        """
        return self._web_tag

    @web_tag.setter
    def web_tag(self, web_tag):
        """Sets the web_tag of this ShowPremiumHostResponse.

        网站名称，对应WAF控制台域名详情中的网站名称

        :param web_tag: The web_tag of this ShowPremiumHostResponse.
        :type web_tag: str
        """
        self._web_tag = web_tag

    @property
    def block_page(self):
        """Gets the block_page of this ShowPremiumHostResponse.

        :return: The block_page of this ShowPremiumHostResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.BlockPage`
        """
        return self._block_page

    @block_page.setter
    def block_page(self, block_page):
        """Sets the block_page of this ShowPremiumHostResponse.

        :param block_page: The block_page of this ShowPremiumHostResponse.
        :type block_page: :class:`huaweicloudsdkwaf.v1.BlockPage`
        """
        self._block_page = block_page

    @property
    def traffic_mark(self):
        """Gets the traffic_mark of this ShowPremiumHostResponse.

        :return: The traffic_mark of this ShowPremiumHostResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.TrafficMark`
        """
        return self._traffic_mark

    @traffic_mark.setter
    def traffic_mark(self, traffic_mark):
        """Sets the traffic_mark of this ShowPremiumHostResponse.

        :param traffic_mark: The traffic_mark of this ShowPremiumHostResponse.
        :type traffic_mark: :class:`huaweicloudsdkwaf.v1.TrafficMark`
        """
        self._traffic_mark = traffic_mark

    @property
    def timeout_config(self):
        """Gets the timeout_config of this ShowPremiumHostResponse.

        :return: The timeout_config of this ShowPremiumHostResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.TimeoutConfig`
        """
        return self._timeout_config

    @timeout_config.setter
    def timeout_config(self, timeout_config):
        """Sets the timeout_config of this ShowPremiumHostResponse.

        :param timeout_config: The timeout_config of this ShowPremiumHostResponse.
        :type timeout_config: :class:`huaweicloudsdkwaf.v1.TimeoutConfig`
        """
        self._timeout_config = timeout_config

    @property
    def forward_header_map(self):
        """Gets the forward_header_map of this ShowPremiumHostResponse.

        字段转发配置，WAF会将添加的字段插到header中，转给源站；Key不能跟nginx原生字段重复。Value支持的值包括:   - $time_local   - $request_id   - $connection_requests   - $tenant_id   - $project_id   - $remote_addr   - $remote_port   - $scheme   - $request_method   - $http_host   -$origin_uri   - $request_length   - $ssl_server_name   - $ssl_protocol   - $ssl_curves   - $ssl_session_reused

        :return: The forward_header_map of this ShowPremiumHostResponse.
        :rtype: dict(str, str)
        """
        return self._forward_header_map

    @forward_header_map.setter
    def forward_header_map(self, forward_header_map):
        """Sets the forward_header_map of this ShowPremiumHostResponse.

        字段转发配置，WAF会将添加的字段插到header中，转给源站；Key不能跟nginx原生字段重复。Value支持的值包括:   - $time_local   - $request_id   - $connection_requests   - $tenant_id   - $project_id   - $remote_addr   - $remote_port   - $scheme   - $request_method   - $http_host   -$origin_uri   - $request_length   - $ssl_server_name   - $ssl_protocol   - $ssl_curves   - $ssl_session_reused

        :param forward_header_map: The forward_header_map of this ShowPremiumHostResponse.
        :type forward_header_map: dict(str, str)
        """
        self._forward_header_map = forward_header_map

    @property
    def access_progress(self):
        """Gets the access_progress of this ShowPremiumHostResponse.

        接入进度，仅用于新版console(前端)使用

        :return: The access_progress of this ShowPremiumHostResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.AccessProgress`]
        """
        return self._access_progress

    @access_progress.setter
    def access_progress(self, access_progress):
        """Sets the access_progress of this ShowPremiumHostResponse.

        接入进度，仅用于新版console(前端)使用

        :param access_progress: The access_progress of this ShowPremiumHostResponse.
        :type access_progress: list[:class:`huaweicloudsdkwaf.v1.AccessProgress`]
        """
        self._access_progress = access_progress

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
        if not isinstance(other, ShowPremiumHostResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
