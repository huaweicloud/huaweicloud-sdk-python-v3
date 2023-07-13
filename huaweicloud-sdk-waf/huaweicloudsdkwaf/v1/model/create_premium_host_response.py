# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePremiumHostResponse(SdkResponse):

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
        'protect_status': 'int',
        'access_status': 'int',
        'block_page': 'BlockPage',
        'forward_header_map': 'dict(str, str)'
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
        'protect_status': 'protect_status',
        'access_status': 'access_status',
        'block_page': 'block_page',
        'forward_header_map': 'forward_header_map'
    }

    def __init__(self, id=None, hostname=None, protocol=None, server=None, proxy=None, locked=None, timestamp=None, tls=None, cipher=None, extend=None, flag=None, description=None, policyid=None, domainid=None, projectid=None, enterprise_project_id=None, protect_status=None, access_status=None, block_page=None, forward_header_map=None):
        """CreatePremiumHostResponse

        The model defined in huaweicloud sdk

        :param id: 域名id
        :type id: str
        :param hostname: 防护域名
        :type hostname: str
        :param protocol: 对外协议，客户端（例如浏览器）请求访问网站的协议类型
        :type protocol: str
        :param server: 防护域名的源站服务器配置信息
        :type server: list[:class:`huaweicloudsdkwaf.v1.PremiumWafServer`]
        :param proxy: 是否使用代理   - true：代表使用代理   - false：代表未使用代理
        :type proxy: bool
        :param locked: 域名冻结状态，0表示未冻结，1表示为冻结，冗余参数
        :type locked: int
        :param timestamp: 创建域名的时间，13位毫秒时间戳
        :type timestamp: int
        :param tls: 配置的最低TLS版本（TLS v1.0/TLS v1.1/TLS v1.2）,默认为TLS v1.0版本，对于低于最低TLS版本的请求，将无法正常访问网站
        :type tls: str
        :param cipher: 对外协议为https时才有cipher参数，加密套件（cipher_1，cipher_2，cipher_3，cipher_4，cipher_default）：  - cipher_1： 加密算法为ECDHE-ECDSA-AES256-GCM-SHA384:HIGH:!MEDIUM:!LOW:!aNULL:!eNULL:!DES:!MD5:!PSK:!RC4:!kRSA:!SRP:!3DES:!DSS:!EXP:!CAMELLIA:@STRENGTH   - cipher_2：加密算法为EECDH+AESGCM:EDH+AESGCM   - cipher_3：加密算法为ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH   - cipher_4：加密算法为ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!EDH   - cipher_default： 加密算法为ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!AESGCM
        :type cipher: str
        :param extend: 扩展字段，用于保存防护域名的一些配置信息。
        :type extend: dict(str, str)
        :param flag: 
        :type flag: :class:`huaweicloudsdkwaf.v1.Flag`
        :param description: 域名描述
        :type description: str
        :param policyid: 防护域名初始绑定的防护策略ID,可以通过策略名称调用查询防护策略列表（ListPolicy）接口查询到对应的策略id
        :type policyid: str
        :param domainid: 帐号ID,对应华为云控制台用户名-&gt;我的凭证-&gt;帐号ID
        :type domainid: str
        :param projectid: 项目ID，对应华为云控制台用户名-&gt;我的凭证-&gt;项目列表-&gt;项目ID
        :type projectid: str
        :param enterprise_project_id: 企业项目ID，对应华为云控制台用户名-&gt;企业-&gt;项目管理-&gt;点击项目名称-&gt;ID
        :type enterprise_project_id: str
        :param protect_status: 域名防护状态：  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测
        :type protect_status: int
        :param access_status: 域名接入状态，0表示未接入，1表示已接入
        :type access_status: int
        :param block_page: 
        :type block_page: :class:`huaweicloudsdkwaf.v1.BlockPage`
        :param forward_header_map: 字段转发配置，WAF会将添加的字段插到header中，转给源站；Key不能跟nginx原生字段重复。Value支持的值包括:   - $time_local   - $request_id   - $connection_requests   - $tenant_id   - $project_id   - $remote_addr   - $remote_port   - $scheme   - $request_method   - $http_host   -$origin_uri   - $request_length   - $ssl_server_name   - $ssl_protocol   - $ssl_curves   - $ssl_session_reused
        :type forward_header_map: dict(str, str)
        """
        
        super(CreatePremiumHostResponse, self).__init__()

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
        self._protect_status = None
        self._access_status = None
        self._block_page = None
        self._forward_header_map = None
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
        if protect_status is not None:
            self.protect_status = protect_status
        if access_status is not None:
            self.access_status = access_status
        if block_page is not None:
            self.block_page = block_page
        if forward_header_map is not None:
            self.forward_header_map = forward_header_map

    @property
    def id(self):
        """Gets the id of this CreatePremiumHostResponse.

        域名id

        :return: The id of this CreatePremiumHostResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreatePremiumHostResponse.

        域名id

        :param id: The id of this CreatePremiumHostResponse.
        :type id: str
        """
        self._id = id

    @property
    def hostname(self):
        """Gets the hostname of this CreatePremiumHostResponse.

        防护域名

        :return: The hostname of this CreatePremiumHostResponse.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this CreatePremiumHostResponse.

        防护域名

        :param hostname: The hostname of this CreatePremiumHostResponse.
        :type hostname: str
        """
        self._hostname = hostname

    @property
    def protocol(self):
        """Gets the protocol of this CreatePremiumHostResponse.

        对外协议，客户端（例如浏览器）请求访问网站的协议类型

        :return: The protocol of this CreatePremiumHostResponse.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this CreatePremiumHostResponse.

        对外协议，客户端（例如浏览器）请求访问网站的协议类型

        :param protocol: The protocol of this CreatePremiumHostResponse.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def server(self):
        """Gets the server of this CreatePremiumHostResponse.

        防护域名的源站服务器配置信息

        :return: The server of this CreatePremiumHostResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.PremiumWafServer`]
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this CreatePremiumHostResponse.

        防护域名的源站服务器配置信息

        :param server: The server of this CreatePremiumHostResponse.
        :type server: list[:class:`huaweicloudsdkwaf.v1.PremiumWafServer`]
        """
        self._server = server

    @property
    def proxy(self):
        """Gets the proxy of this CreatePremiumHostResponse.

        是否使用代理   - true：代表使用代理   - false：代表未使用代理

        :return: The proxy of this CreatePremiumHostResponse.
        :rtype: bool
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this CreatePremiumHostResponse.

        是否使用代理   - true：代表使用代理   - false：代表未使用代理

        :param proxy: The proxy of this CreatePremiumHostResponse.
        :type proxy: bool
        """
        self._proxy = proxy

    @property
    def locked(self):
        """Gets the locked of this CreatePremiumHostResponse.

        域名冻结状态，0表示未冻结，1表示为冻结，冗余参数

        :return: The locked of this CreatePremiumHostResponse.
        :rtype: int
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this CreatePremiumHostResponse.

        域名冻结状态，0表示未冻结，1表示为冻结，冗余参数

        :param locked: The locked of this CreatePremiumHostResponse.
        :type locked: int
        """
        self._locked = locked

    @property
    def timestamp(self):
        """Gets the timestamp of this CreatePremiumHostResponse.

        创建域名的时间，13位毫秒时间戳

        :return: The timestamp of this CreatePremiumHostResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this CreatePremiumHostResponse.

        创建域名的时间，13位毫秒时间戳

        :param timestamp: The timestamp of this CreatePremiumHostResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def tls(self):
        """Gets the tls of this CreatePremiumHostResponse.

        配置的最低TLS版本（TLS v1.0/TLS v1.1/TLS v1.2）,默认为TLS v1.0版本，对于低于最低TLS版本的请求，将无法正常访问网站

        :return: The tls of this CreatePremiumHostResponse.
        :rtype: str
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """Sets the tls of this CreatePremiumHostResponse.

        配置的最低TLS版本（TLS v1.0/TLS v1.1/TLS v1.2）,默认为TLS v1.0版本，对于低于最低TLS版本的请求，将无法正常访问网站

        :param tls: The tls of this CreatePremiumHostResponse.
        :type tls: str
        """
        self._tls = tls

    @property
    def cipher(self):
        """Gets the cipher of this CreatePremiumHostResponse.

        对外协议为https时才有cipher参数，加密套件（cipher_1，cipher_2，cipher_3，cipher_4，cipher_default）：  - cipher_1： 加密算法为ECDHE-ECDSA-AES256-GCM-SHA384:HIGH:!MEDIUM:!LOW:!aNULL:!eNULL:!DES:!MD5:!PSK:!RC4:!kRSA:!SRP:!3DES:!DSS:!EXP:!CAMELLIA:@STRENGTH   - cipher_2：加密算法为EECDH+AESGCM:EDH+AESGCM   - cipher_3：加密算法为ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH   - cipher_4：加密算法为ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!EDH   - cipher_default： 加密算法为ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!AESGCM

        :return: The cipher of this CreatePremiumHostResponse.
        :rtype: str
        """
        return self._cipher

    @cipher.setter
    def cipher(self, cipher):
        """Sets the cipher of this CreatePremiumHostResponse.

        对外协议为https时才有cipher参数，加密套件（cipher_1，cipher_2，cipher_3，cipher_4，cipher_default）：  - cipher_1： 加密算法为ECDHE-ECDSA-AES256-GCM-SHA384:HIGH:!MEDIUM:!LOW:!aNULL:!eNULL:!DES:!MD5:!PSK:!RC4:!kRSA:!SRP:!3DES:!DSS:!EXP:!CAMELLIA:@STRENGTH   - cipher_2：加密算法为EECDH+AESGCM:EDH+AESGCM   - cipher_3：加密算法为ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH   - cipher_4：加密算法为ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!EDH   - cipher_default： 加密算法为ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!AESGCM

        :param cipher: The cipher of this CreatePremiumHostResponse.
        :type cipher: str
        """
        self._cipher = cipher

    @property
    def extend(self):
        """Gets the extend of this CreatePremiumHostResponse.

        扩展字段，用于保存防护域名的一些配置信息。

        :return: The extend of this CreatePremiumHostResponse.
        :rtype: dict(str, str)
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        """Sets the extend of this CreatePremiumHostResponse.

        扩展字段，用于保存防护域名的一些配置信息。

        :param extend: The extend of this CreatePremiumHostResponse.
        :type extend: dict(str, str)
        """
        self._extend = extend

    @property
    def flag(self):
        """Gets the flag of this CreatePremiumHostResponse.

        :return: The flag of this CreatePremiumHostResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.Flag`
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        """Sets the flag of this CreatePremiumHostResponse.

        :param flag: The flag of this CreatePremiumHostResponse.
        :type flag: :class:`huaweicloudsdkwaf.v1.Flag`
        """
        self._flag = flag

    @property
    def description(self):
        """Gets the description of this CreatePremiumHostResponse.

        域名描述

        :return: The description of this CreatePremiumHostResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreatePremiumHostResponse.

        域名描述

        :param description: The description of this CreatePremiumHostResponse.
        :type description: str
        """
        self._description = description

    @property
    def policyid(self):
        """Gets the policyid of this CreatePremiumHostResponse.

        防护域名初始绑定的防护策略ID,可以通过策略名称调用查询防护策略列表（ListPolicy）接口查询到对应的策略id

        :return: The policyid of this CreatePremiumHostResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this CreatePremiumHostResponse.

        防护域名初始绑定的防护策略ID,可以通过策略名称调用查询防护策略列表（ListPolicy）接口查询到对应的策略id

        :param policyid: The policyid of this CreatePremiumHostResponse.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def domainid(self):
        """Gets the domainid of this CreatePremiumHostResponse.

        帐号ID,对应华为云控制台用户名->我的凭证->帐号ID

        :return: The domainid of this CreatePremiumHostResponse.
        :rtype: str
        """
        return self._domainid

    @domainid.setter
    def domainid(self, domainid):
        """Sets the domainid of this CreatePremiumHostResponse.

        帐号ID,对应华为云控制台用户名->我的凭证->帐号ID

        :param domainid: The domainid of this CreatePremiumHostResponse.
        :type domainid: str
        """
        self._domainid = domainid

    @property
    def projectid(self):
        """Gets the projectid of this CreatePremiumHostResponse.

        项目ID，对应华为云控制台用户名->我的凭证->项目列表->项目ID

        :return: The projectid of this CreatePremiumHostResponse.
        :rtype: str
        """
        return self._projectid

    @projectid.setter
    def projectid(self, projectid):
        """Sets the projectid of this CreatePremiumHostResponse.

        项目ID，对应华为云控制台用户名->我的凭证->项目列表->项目ID

        :param projectid: The projectid of this CreatePremiumHostResponse.
        :type projectid: str
        """
        self._projectid = projectid

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreatePremiumHostResponse.

        企业项目ID，对应华为云控制台用户名->企业->项目管理->点击项目名称->ID

        :return: The enterprise_project_id of this CreatePremiumHostResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreatePremiumHostResponse.

        企业项目ID，对应华为云控制台用户名->企业->项目管理->点击项目名称->ID

        :param enterprise_project_id: The enterprise_project_id of this CreatePremiumHostResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def protect_status(self):
        """Gets the protect_status of this CreatePremiumHostResponse.

        域名防护状态：  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测

        :return: The protect_status of this CreatePremiumHostResponse.
        :rtype: int
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this CreatePremiumHostResponse.

        域名防护状态：  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测

        :param protect_status: The protect_status of this CreatePremiumHostResponse.
        :type protect_status: int
        """
        self._protect_status = protect_status

    @property
    def access_status(self):
        """Gets the access_status of this CreatePremiumHostResponse.

        域名接入状态，0表示未接入，1表示已接入

        :return: The access_status of this CreatePremiumHostResponse.
        :rtype: int
        """
        return self._access_status

    @access_status.setter
    def access_status(self, access_status):
        """Sets the access_status of this CreatePremiumHostResponse.

        域名接入状态，0表示未接入，1表示已接入

        :param access_status: The access_status of this CreatePremiumHostResponse.
        :type access_status: int
        """
        self._access_status = access_status

    @property
    def block_page(self):
        """Gets the block_page of this CreatePremiumHostResponse.

        :return: The block_page of this CreatePremiumHostResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.BlockPage`
        """
        return self._block_page

    @block_page.setter
    def block_page(self, block_page):
        """Sets the block_page of this CreatePremiumHostResponse.

        :param block_page: The block_page of this CreatePremiumHostResponse.
        :type block_page: :class:`huaweicloudsdkwaf.v1.BlockPage`
        """
        self._block_page = block_page

    @property
    def forward_header_map(self):
        """Gets the forward_header_map of this CreatePremiumHostResponse.

        字段转发配置，WAF会将添加的字段插到header中，转给源站；Key不能跟nginx原生字段重复。Value支持的值包括:   - $time_local   - $request_id   - $connection_requests   - $tenant_id   - $project_id   - $remote_addr   - $remote_port   - $scheme   - $request_method   - $http_host   -$origin_uri   - $request_length   - $ssl_server_name   - $ssl_protocol   - $ssl_curves   - $ssl_session_reused

        :return: The forward_header_map of this CreatePremiumHostResponse.
        :rtype: dict(str, str)
        """
        return self._forward_header_map

    @forward_header_map.setter
    def forward_header_map(self, forward_header_map):
        """Sets the forward_header_map of this CreatePremiumHostResponse.

        字段转发配置，WAF会将添加的字段插到header中，转给源站；Key不能跟nginx原生字段重复。Value支持的值包括:   - $time_local   - $request_id   - $connection_requests   - $tenant_id   - $project_id   - $remote_addr   - $remote_port   - $scheme   - $request_method   - $http_host   -$origin_uri   - $request_length   - $ssl_server_name   - $ssl_protocol   - $ssl_curves   - $ssl_session_reused

        :param forward_header_map: The forward_header_map of this CreatePremiumHostResponse.
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
        if not isinstance(other, CreatePremiumHostResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
