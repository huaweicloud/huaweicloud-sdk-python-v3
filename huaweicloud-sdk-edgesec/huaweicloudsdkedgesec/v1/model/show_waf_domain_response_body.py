# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWafDomainResponseBody:

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
        'domain_name': 'str',
        'enterprise_project_id': 'str',
        'tenant_id': 'str',
        'open_time': 'int',
        'close_time': 'int',
        'dispatch_status': 'int',
        'service_area': 'str',
        'web_tag': 'str',
        'description': 'str',
        'policy_id': 'str',
        'protocol': 'str',
        'certificate_id': 'str',
        'certificate_name': 'str',
        'tls': 'str',
        'cipher': 'str',
        'protect_status': 'int',
        'access_status': 'int',
        'create_time': 'int',
        'block_page': 'WafBlockPage',
        'traffic_mark': 'WafTrafficMark',
        'flag': 'Flag',
        'extend': 'dict(str, str)',
        'is_added': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'domain_name': 'domain_name',
        'enterprise_project_id': 'enterprise_project_id',
        'tenant_id': 'tenant_id',
        'open_time': 'open_time',
        'close_time': 'close_time',
        'dispatch_status': 'dispatch_status',
        'service_area': 'service_area',
        'web_tag': 'web_tag',
        'description': 'description',
        'policy_id': 'policy_id',
        'protocol': 'protocol',
        'certificate_id': 'certificate_id',
        'certificate_name': 'certificate_name',
        'tls': 'tls',
        'cipher': 'cipher',
        'protect_status': 'protect_status',
        'access_status': 'access_status',
        'create_time': 'create_time',
        'block_page': 'block_page',
        'traffic_mark': 'traffic_mark',
        'flag': 'flag',
        'extend': 'extend',
        'is_added': 'is_added'
    }

    def __init__(self, id=None, domain_name=None, enterprise_project_id=None, tenant_id=None, open_time=None, close_time=None, dispatch_status=None, service_area=None, web_tag=None, description=None, policy_id=None, protocol=None, certificate_id=None, certificate_name=None, tls=None, cipher=None, protect_status=None, access_status=None, create_time=None, block_page=None, traffic_mark=None, flag=None, extend=None, is_added=None):
        """ShowWafDomainResponseBody

        The model defined in huaweicloud sdk

        :param id: 域名id
        :type id: str
        :param domain_name: 域名
        :type domain_name: str
        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id
        :type enterprise_project_id: str
        :param tenant_id: 租户ID
        :type tenant_id: str
        :param open_time: 上一次开启防护的时间
        :type open_time: int
        :param close_time: 上一次关闭防护的时间
        :type close_time: int
        :param dispatch_status: cdn域名调度情况（0：未防护，1：配置中，2：已防护，3：删除中）
        :type dispatch_status: int
        :param service_area: 域名在CDN所属区域
        :type service_area: str
        :param web_tag: 域名名称
        :type web_tag: str
        :param description: 域名描述
        :type description: str
        :param policy_id: 策略id
        :type policy_id: str
        :param protocol: 协议
        :type protocol: str
        :param certificate_id: 证书id
        :type certificate_id: str
        :param certificate_name: 证书名称
        :type certificate_name: str
        :param tls: 配置的最低TLS版本（TLS v1.0/TLS v1.1/TLS v1.2），默认为TLS v1.0版本，对外协议为https时才有tls参数
        :type tls: str
        :param cipher: 对外协议为https时才有cipher参数，加密套件（cipher_1，cipher_2，cipher_3，cipher_4，cipher_default）：  - cipher_1： 加密算法为ECDHE-ECDSA-AES256-GCM-SHA384:HIGH:!MEDIUM:!LOW:!aNULL:!eNULL:!DES:!MD5:!PSK:!RC4:!kRSA:!SRP:!3DES:!DSS:!EXP:!CAMELLIA:@STRENGTH   - cipher_2：加密算法为EECDH+AESGCM:EDH+AESGCM   - cipher_3：加密算法为ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH   - cipher_4：加密算法为ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!EDH   - cipher_default： 加密算法为ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!AESGCM
        :type cipher: str
        :param protect_status: 防护状态：  - 0-关闭   - 1-开启
        :type protect_status: int
        :param access_status: 接入状态：  - 0-未接入   - 1-已接入
        :type access_status: int
        :param create_time: 创建域名的时间，13位时间戳
        :type create_time: int
        :param block_page: 
        :type block_page: :class:`huaweicloudsdkedgesec.v1.WafBlockPage`
        :param traffic_mark: 
        :type traffic_mark: :class:`huaweicloudsdkedgesec.v1.WafTrafficMark`
        :param flag: 
        :type flag: :class:`huaweicloudsdkedgesec.v1.Flag`
        :param extend: 域名可扩展属性
        :type extend: dict(str, str)
        :param is_added: 是否为ddos防护域名
        :type is_added: bool
        """
        
        

        self._id = None
        self._domain_name = None
        self._enterprise_project_id = None
        self._tenant_id = None
        self._open_time = None
        self._close_time = None
        self._dispatch_status = None
        self._service_area = None
        self._web_tag = None
        self._description = None
        self._policy_id = None
        self._protocol = None
        self._certificate_id = None
        self._certificate_name = None
        self._tls = None
        self._cipher = None
        self._protect_status = None
        self._access_status = None
        self._create_time = None
        self._block_page = None
        self._traffic_mark = None
        self._flag = None
        self._extend = None
        self._is_added = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if domain_name is not None:
            self.domain_name = domain_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if open_time is not None:
            self.open_time = open_time
        if close_time is not None:
            self.close_time = close_time
        if dispatch_status is not None:
            self.dispatch_status = dispatch_status
        if service_area is not None:
            self.service_area = service_area
        if web_tag is not None:
            self.web_tag = web_tag
        if description is not None:
            self.description = description
        if policy_id is not None:
            self.policy_id = policy_id
        if protocol is not None:
            self.protocol = protocol
        if certificate_id is not None:
            self.certificate_id = certificate_id
        if certificate_name is not None:
            self.certificate_name = certificate_name
        if tls is not None:
            self.tls = tls
        if cipher is not None:
            self.cipher = cipher
        if protect_status is not None:
            self.protect_status = protect_status
        if access_status is not None:
            self.access_status = access_status
        if create_time is not None:
            self.create_time = create_time
        if block_page is not None:
            self.block_page = block_page
        if traffic_mark is not None:
            self.traffic_mark = traffic_mark
        if flag is not None:
            self.flag = flag
        if extend is not None:
            self.extend = extend
        if is_added is not None:
            self.is_added = is_added

    @property
    def id(self):
        """Gets the id of this ShowWafDomainResponseBody.

        域名id

        :return: The id of this ShowWafDomainResponseBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowWafDomainResponseBody.

        域名id

        :param id: The id of this ShowWafDomainResponseBody.
        :type id: str
        """
        self._id = id

    @property
    def domain_name(self):
        """Gets the domain_name of this ShowWafDomainResponseBody.

        域名

        :return: The domain_name of this ShowWafDomainResponseBody.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ShowWafDomainResponseBody.

        域名

        :param domain_name: The domain_name of this ShowWafDomainResponseBody.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowWafDomainResponseBody.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :return: The enterprise_project_id of this ShowWafDomainResponseBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowWafDomainResponseBody.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ShowWafDomainResponseBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ShowWafDomainResponseBody.

        租户ID

        :return: The tenant_id of this ShowWafDomainResponseBody.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ShowWafDomainResponseBody.

        租户ID

        :param tenant_id: The tenant_id of this ShowWafDomainResponseBody.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def open_time(self):
        """Gets the open_time of this ShowWafDomainResponseBody.

        上一次开启防护的时间

        :return: The open_time of this ShowWafDomainResponseBody.
        :rtype: int
        """
        return self._open_time

    @open_time.setter
    def open_time(self, open_time):
        """Sets the open_time of this ShowWafDomainResponseBody.

        上一次开启防护的时间

        :param open_time: The open_time of this ShowWafDomainResponseBody.
        :type open_time: int
        """
        self._open_time = open_time

    @property
    def close_time(self):
        """Gets the close_time of this ShowWafDomainResponseBody.

        上一次关闭防护的时间

        :return: The close_time of this ShowWafDomainResponseBody.
        :rtype: int
        """
        return self._close_time

    @close_time.setter
    def close_time(self, close_time):
        """Sets the close_time of this ShowWafDomainResponseBody.

        上一次关闭防护的时间

        :param close_time: The close_time of this ShowWafDomainResponseBody.
        :type close_time: int
        """
        self._close_time = close_time

    @property
    def dispatch_status(self):
        """Gets the dispatch_status of this ShowWafDomainResponseBody.

        cdn域名调度情况（0：未防护，1：配置中，2：已防护，3：删除中）

        :return: The dispatch_status of this ShowWafDomainResponseBody.
        :rtype: int
        """
        return self._dispatch_status

    @dispatch_status.setter
    def dispatch_status(self, dispatch_status):
        """Sets the dispatch_status of this ShowWafDomainResponseBody.

        cdn域名调度情况（0：未防护，1：配置中，2：已防护，3：删除中）

        :param dispatch_status: The dispatch_status of this ShowWafDomainResponseBody.
        :type dispatch_status: int
        """
        self._dispatch_status = dispatch_status

    @property
    def service_area(self):
        """Gets the service_area of this ShowWafDomainResponseBody.

        域名在CDN所属区域

        :return: The service_area of this ShowWafDomainResponseBody.
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        """Sets the service_area of this ShowWafDomainResponseBody.

        域名在CDN所属区域

        :param service_area: The service_area of this ShowWafDomainResponseBody.
        :type service_area: str
        """
        self._service_area = service_area

    @property
    def web_tag(self):
        """Gets the web_tag of this ShowWafDomainResponseBody.

        域名名称

        :return: The web_tag of this ShowWafDomainResponseBody.
        :rtype: str
        """
        return self._web_tag

    @web_tag.setter
    def web_tag(self, web_tag):
        """Sets the web_tag of this ShowWafDomainResponseBody.

        域名名称

        :param web_tag: The web_tag of this ShowWafDomainResponseBody.
        :type web_tag: str
        """
        self._web_tag = web_tag

    @property
    def description(self):
        """Gets the description of this ShowWafDomainResponseBody.

        域名描述

        :return: The description of this ShowWafDomainResponseBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowWafDomainResponseBody.

        域名描述

        :param description: The description of this ShowWafDomainResponseBody.
        :type description: str
        """
        self._description = description

    @property
    def policy_id(self):
        """Gets the policy_id of this ShowWafDomainResponseBody.

        策略id

        :return: The policy_id of this ShowWafDomainResponseBody.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this ShowWafDomainResponseBody.

        策略id

        :param policy_id: The policy_id of this ShowWafDomainResponseBody.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def protocol(self):
        """Gets the protocol of this ShowWafDomainResponseBody.

        协议

        :return: The protocol of this ShowWafDomainResponseBody.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ShowWafDomainResponseBody.

        协议

        :param protocol: The protocol of this ShowWafDomainResponseBody.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def certificate_id(self):
        """Gets the certificate_id of this ShowWafDomainResponseBody.

        证书id

        :return: The certificate_id of this ShowWafDomainResponseBody.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """Sets the certificate_id of this ShowWafDomainResponseBody.

        证书id

        :param certificate_id: The certificate_id of this ShowWafDomainResponseBody.
        :type certificate_id: str
        """
        self._certificate_id = certificate_id

    @property
    def certificate_name(self):
        """Gets the certificate_name of this ShowWafDomainResponseBody.

        证书名称

        :return: The certificate_name of this ShowWafDomainResponseBody.
        :rtype: str
        """
        return self._certificate_name

    @certificate_name.setter
    def certificate_name(self, certificate_name):
        """Sets the certificate_name of this ShowWafDomainResponseBody.

        证书名称

        :param certificate_name: The certificate_name of this ShowWafDomainResponseBody.
        :type certificate_name: str
        """
        self._certificate_name = certificate_name

    @property
    def tls(self):
        """Gets the tls of this ShowWafDomainResponseBody.

        配置的最低TLS版本（TLS v1.0/TLS v1.1/TLS v1.2），默认为TLS v1.0版本，对外协议为https时才有tls参数

        :return: The tls of this ShowWafDomainResponseBody.
        :rtype: str
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """Sets the tls of this ShowWafDomainResponseBody.

        配置的最低TLS版本（TLS v1.0/TLS v1.1/TLS v1.2），默认为TLS v1.0版本，对外协议为https时才有tls参数

        :param tls: The tls of this ShowWafDomainResponseBody.
        :type tls: str
        """
        self._tls = tls

    @property
    def cipher(self):
        """Gets the cipher of this ShowWafDomainResponseBody.

        对外协议为https时才有cipher参数，加密套件（cipher_1，cipher_2，cipher_3，cipher_4，cipher_default）：  - cipher_1： 加密算法为ECDHE-ECDSA-AES256-GCM-SHA384:HIGH:!MEDIUM:!LOW:!aNULL:!eNULL:!DES:!MD5:!PSK:!RC4:!kRSA:!SRP:!3DES:!DSS:!EXP:!CAMELLIA:@STRENGTH   - cipher_2：加密算法为EECDH+AESGCM:EDH+AESGCM   - cipher_3：加密算法为ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH   - cipher_4：加密算法为ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!EDH   - cipher_default： 加密算法为ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!AESGCM

        :return: The cipher of this ShowWafDomainResponseBody.
        :rtype: str
        """
        return self._cipher

    @cipher.setter
    def cipher(self, cipher):
        """Sets the cipher of this ShowWafDomainResponseBody.

        对外协议为https时才有cipher参数，加密套件（cipher_1，cipher_2，cipher_3，cipher_4，cipher_default）：  - cipher_1： 加密算法为ECDHE-ECDSA-AES256-GCM-SHA384:HIGH:!MEDIUM:!LOW:!aNULL:!eNULL:!DES:!MD5:!PSK:!RC4:!kRSA:!SRP:!3DES:!DSS:!EXP:!CAMELLIA:@STRENGTH   - cipher_2：加密算法为EECDH+AESGCM:EDH+AESGCM   - cipher_3：加密算法为ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH   - cipher_4：加密算法为ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!EDH   - cipher_default： 加密算法为ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!AESGCM

        :param cipher: The cipher of this ShowWafDomainResponseBody.
        :type cipher: str
        """
        self._cipher = cipher

    @property
    def protect_status(self):
        """Gets the protect_status of this ShowWafDomainResponseBody.

        防护状态：  - 0-关闭   - 1-开启

        :return: The protect_status of this ShowWafDomainResponseBody.
        :rtype: int
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this ShowWafDomainResponseBody.

        防护状态：  - 0-关闭   - 1-开启

        :param protect_status: The protect_status of this ShowWafDomainResponseBody.
        :type protect_status: int
        """
        self._protect_status = protect_status

    @property
    def access_status(self):
        """Gets the access_status of this ShowWafDomainResponseBody.

        接入状态：  - 0-未接入   - 1-已接入

        :return: The access_status of this ShowWafDomainResponseBody.
        :rtype: int
        """
        return self._access_status

    @access_status.setter
    def access_status(self, access_status):
        """Sets the access_status of this ShowWafDomainResponseBody.

        接入状态：  - 0-未接入   - 1-已接入

        :param access_status: The access_status of this ShowWafDomainResponseBody.
        :type access_status: int
        """
        self._access_status = access_status

    @property
    def create_time(self):
        """Gets the create_time of this ShowWafDomainResponseBody.

        创建域名的时间，13位时间戳

        :return: The create_time of this ShowWafDomainResponseBody.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowWafDomainResponseBody.

        创建域名的时间，13位时间戳

        :param create_time: The create_time of this ShowWafDomainResponseBody.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def block_page(self):
        """Gets the block_page of this ShowWafDomainResponseBody.

        :return: The block_page of this ShowWafDomainResponseBody.
        :rtype: :class:`huaweicloudsdkedgesec.v1.WafBlockPage`
        """
        return self._block_page

    @block_page.setter
    def block_page(self, block_page):
        """Sets the block_page of this ShowWafDomainResponseBody.

        :param block_page: The block_page of this ShowWafDomainResponseBody.
        :type block_page: :class:`huaweicloudsdkedgesec.v1.WafBlockPage`
        """
        self._block_page = block_page

    @property
    def traffic_mark(self):
        """Gets the traffic_mark of this ShowWafDomainResponseBody.

        :return: The traffic_mark of this ShowWafDomainResponseBody.
        :rtype: :class:`huaweicloudsdkedgesec.v1.WafTrafficMark`
        """
        return self._traffic_mark

    @traffic_mark.setter
    def traffic_mark(self, traffic_mark):
        """Sets the traffic_mark of this ShowWafDomainResponseBody.

        :param traffic_mark: The traffic_mark of this ShowWafDomainResponseBody.
        :type traffic_mark: :class:`huaweicloudsdkedgesec.v1.WafTrafficMark`
        """
        self._traffic_mark = traffic_mark

    @property
    def flag(self):
        """Gets the flag of this ShowWafDomainResponseBody.

        :return: The flag of this ShowWafDomainResponseBody.
        :rtype: :class:`huaweicloudsdkedgesec.v1.Flag`
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        """Sets the flag of this ShowWafDomainResponseBody.

        :param flag: The flag of this ShowWafDomainResponseBody.
        :type flag: :class:`huaweicloudsdkedgesec.v1.Flag`
        """
        self._flag = flag

    @property
    def extend(self):
        """Gets the extend of this ShowWafDomainResponseBody.

        域名可扩展属性

        :return: The extend of this ShowWafDomainResponseBody.
        :rtype: dict(str, str)
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        """Sets the extend of this ShowWafDomainResponseBody.

        域名可扩展属性

        :param extend: The extend of this ShowWafDomainResponseBody.
        :type extend: dict(str, str)
        """
        self._extend = extend

    @property
    def is_added(self):
        """Gets the is_added of this ShowWafDomainResponseBody.

        是否为ddos防护域名

        :return: The is_added of this ShowWafDomainResponseBody.
        :rtype: bool
        """
        return self._is_added

    @is_added.setter
    def is_added(self, is_added):
        """Sets the is_added of this ShowWafDomainResponseBody.

        是否为ddos防护域名

        :param is_added: The is_added of this ShowWafDomainResponseBody.
        :type is_added: bool
        """
        self._is_added = is_added

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
        if not isinstance(other, ShowWafDomainResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
