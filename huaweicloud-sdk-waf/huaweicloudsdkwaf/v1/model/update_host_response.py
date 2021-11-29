# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHostResponse(SdkResponse):


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
        'policyid': 'str',
        'hostname': 'str',
        'domainid': 'str',
        'access_code': 'str',
        'protocol': 'str',
        'server': 'list[CloudWafServer]',
        'certificateid': 'str',
        'certificatename': 'str',
        'proxy': 'bool',
        'locked': 'int',
        'protect_status': 'int',
        'access_status': 'int',
        'timestamp': 'int',
        'tls': 'str',
        'cipher': 'str',
        'enterprise_project_id': 'str',
        'block_page': 'BlockPage',
        'web_tag': 'bool',
        'flag': 'Flag',
        'exclusive_ip': 'bool',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'policyid': 'policyid',
        'hostname': 'hostname',
        'domainid': 'domainid',
        'access_code': 'access_code',
        'protocol': 'protocol',
        'server': 'server',
        'certificateid': 'certificateid',
        'certificatename': 'certificatename',
        'proxy': 'proxy',
        'locked': 'locked',
        'protect_status': 'protect_status',
        'access_status': 'access_status',
        'timestamp': 'timestamp',
        'tls': 'tls',
        'cipher': 'cipher',
        'enterprise_project_id': 'enterprise_project_id',
        'block_page': 'block_page',
        'web_tag': 'web_tag',
        'flag': 'flag',
        'exclusive_ip': 'exclusive_ip',
        'description': 'description'
    }

    def __init__(self, id=None, policyid=None, hostname=None, domainid=None, access_code=None, protocol=None, server=None, certificateid=None, certificatename=None, proxy=None, locked=None, protect_status=None, access_status=None, timestamp=None, tls=None, cipher=None, enterprise_project_id=None, block_page=None, web_tag=None, flag=None, exclusive_ip=None, description=None):
        """UpdateHostResponse - a model defined in huaweicloud sdk"""
        
        super(UpdateHostResponse, self).__init__()

        self._id = None
        self._policyid = None
        self._hostname = None
        self._domainid = None
        self._access_code = None
        self._protocol = None
        self._server = None
        self._certificateid = None
        self._certificatename = None
        self._proxy = None
        self._locked = None
        self._protect_status = None
        self._access_status = None
        self._timestamp = None
        self._tls = None
        self._cipher = None
        self._enterprise_project_id = None
        self._block_page = None
        self._web_tag = None
        self._flag = None
        self._exclusive_ip = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if policyid is not None:
            self.policyid = policyid
        if hostname is not None:
            self.hostname = hostname
        if domainid is not None:
            self.domainid = domainid
        if access_code is not None:
            self.access_code = access_code
        if protocol is not None:
            self.protocol = protocol
        if server is not None:
            self.server = server
        if certificateid is not None:
            self.certificateid = certificateid
        if certificatename is not None:
            self.certificatename = certificatename
        if proxy is not None:
            self.proxy = proxy
        if locked is not None:
            self.locked = locked
        if protect_status is not None:
            self.protect_status = protect_status
        if access_status is not None:
            self.access_status = access_status
        if timestamp is not None:
            self.timestamp = timestamp
        if tls is not None:
            self.tls = tls
        if cipher is not None:
            self.cipher = cipher
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if block_page is not None:
            self.block_page = block_page
        if web_tag is not None:
            self.web_tag = web_tag
        if flag is not None:
            self.flag = flag
        if exclusive_ip is not None:
            self.exclusive_ip = exclusive_ip
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this UpdateHostResponse.

        域名id

        :return: The id of this UpdateHostResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateHostResponse.

        域名id

        :param id: The id of this UpdateHostResponse.
        :type: str
        """
        self._id = id

    @property
    def policyid(self):
        """Gets the policyid of this UpdateHostResponse.

        策略id

        :return: The policyid of this UpdateHostResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this UpdateHostResponse.

        策略id

        :param policyid: The policyid of this UpdateHostResponse.
        :type: str
        """
        self._policyid = policyid

    @property
    def hostname(self):
        """Gets the hostname of this UpdateHostResponse.

        创建的云模式防护域名

        :return: The hostname of this UpdateHostResponse.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this UpdateHostResponse.

        创建的云模式防护域名

        :param hostname: The hostname of this UpdateHostResponse.
        :type: str
        """
        self._hostname = hostname

    @property
    def domainid(self):
        """Gets the domainid of this UpdateHostResponse.

        账户id

        :return: The domainid of this UpdateHostResponse.
        :rtype: str
        """
        return self._domainid

    @domainid.setter
    def domainid(self, domainid):
        """Sets the domainid of this UpdateHostResponse.

        账户id

        :param domainid: The domainid of this UpdateHostResponse.
        :type: str
        """
        self._domainid = domainid

    @property
    def access_code(self):
        """Gets the access_code of this UpdateHostResponse.

        cname前缀

        :return: The access_code of this UpdateHostResponse.
        :rtype: str
        """
        return self._access_code

    @access_code.setter
    def access_code(self, access_code):
        """Sets the access_code of this UpdateHostResponse.

        cname前缀

        :param access_code: The access_code of this UpdateHostResponse.
        :type: str
        """
        self._access_code = access_code

    @property
    def protocol(self):
        """Gets the protocol of this UpdateHostResponse.

        后端协议类型

        :return: The protocol of this UpdateHostResponse.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this UpdateHostResponse.

        后端协议类型

        :param protocol: The protocol of this UpdateHostResponse.
        :type: str
        """
        self._protocol = protocol

    @property
    def server(self):
        """Gets the server of this UpdateHostResponse.

        源站信息

        :return: The server of this UpdateHostResponse.
        :rtype: list[CloudWafServer]
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this UpdateHostResponse.

        源站信息

        :param server: The server of this UpdateHostResponse.
        :type: list[CloudWafServer]
        """
        self._server = server

    @property
    def certificateid(self):
        """Gets the certificateid of this UpdateHostResponse.

        证书id，通过查询证书列表接口（ListCertificates）接口获取证书id

        :return: The certificateid of this UpdateHostResponse.
        :rtype: str
        """
        return self._certificateid

    @certificateid.setter
    def certificateid(self, certificateid):
        """Sets the certificateid of this UpdateHostResponse.

        证书id，通过查询证书列表接口（ListCertificates）接口获取证书id

        :param certificateid: The certificateid of this UpdateHostResponse.
        :type: str
        """
        self._certificateid = certificateid

    @property
    def certificatename(self):
        """Gets the certificatename of this UpdateHostResponse.

        证书名，通过查询证书列表接口（ListCertificates）接口获取证书id

        :return: The certificatename of this UpdateHostResponse.
        :rtype: str
        """
        return self._certificatename

    @certificatename.setter
    def certificatename(self, certificatename):
        """Sets the certificatename of this UpdateHostResponse.

        证书名，通过查询证书列表接口（ListCertificates）接口获取证书id

        :param certificatename: The certificatename of this UpdateHostResponse.
        :type: str
        """
        self._certificatename = certificatename

    @property
    def proxy(self):
        """Gets the proxy of this UpdateHostResponse.

        是否开启了代理

        :return: The proxy of this UpdateHostResponse.
        :rtype: bool
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this UpdateHostResponse.

        是否开启了代理

        :param proxy: The proxy of this UpdateHostResponse.
        :type: bool
        """
        self._proxy = proxy

    @property
    def locked(self):
        """Gets the locked of this UpdateHostResponse.

        锁定状态,默认为0

        :return: The locked of this UpdateHostResponse.
        :rtype: int
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this UpdateHostResponse.

        锁定状态,默认为0

        :param locked: The locked of this UpdateHostResponse.
        :type: int
        """
        self._locked = locked

    @property
    def protect_status(self):
        """Gets the protect_status of this UpdateHostResponse.

        域名防护状态：  - -1：bypass，该域名的请求直接到达其后端服务器，不再经过WAF  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测

        :return: The protect_status of this UpdateHostResponse.
        :rtype: int
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this UpdateHostResponse.

        域名防护状态：  - -1：bypass，该域名的请求直接到达其后端服务器，不再经过WAF  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测

        :param protect_status: The protect_status of this UpdateHostResponse.
        :type: int
        """
        self._protect_status = protect_status

    @property
    def access_status(self):
        """Gets the access_status of this UpdateHostResponse.

        接入状态

        :return: The access_status of this UpdateHostResponse.
        :rtype: int
        """
        return self._access_status

    @access_status.setter
    def access_status(self, access_status):
        """Sets the access_status of this UpdateHostResponse.

        接入状态

        :param access_status: The access_status of this UpdateHostResponse.
        :type: int
        """
        self._access_status = access_status

    @property
    def timestamp(self):
        """Gets the timestamp of this UpdateHostResponse.

        创建防护域名的时间

        :return: The timestamp of this UpdateHostResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this UpdateHostResponse.

        创建防护域名的时间

        :param timestamp: The timestamp of this UpdateHostResponse.
        :type: int
        """
        self._timestamp = timestamp

    @property
    def tls(self):
        """Gets the tls of this UpdateHostResponse.

        ssl协议版本

        :return: The tls of this UpdateHostResponse.
        :rtype: str
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """Sets the tls of this UpdateHostResponse.

        ssl协议版本

        :param tls: The tls of this UpdateHostResponse.
        :type: str
        """
        self._tls = tls

    @property
    def cipher(self):
        """Gets the cipher of this UpdateHostResponse.

        加密套件（cipher_1，cipher_2，cipher_3，cipher_4，cipher_default）：  cipher_1： 加密算法为ECDHE-ECDSA-AES256-GCM-SHA384:HIGH:!MEDIUM:!LOW:!aNULL:!eNULL:!DES:!MD5:!PSK:!RC4:!kRSA:!SRP:!3DES:!DSS:!EXP:!CAMELLIA:@STRENGTH   cipher_2：加密算法为EECDH+AESGCM:EDH+AESGCM    cipher_3：加密算法为ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH    cipher_4：加密算法为ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!EDH    cipher_default： 加密算法为ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!AESGCM

        :return: The cipher of this UpdateHostResponse.
        :rtype: str
        """
        return self._cipher

    @cipher.setter
    def cipher(self, cipher):
        """Sets the cipher of this UpdateHostResponse.

        加密套件（cipher_1，cipher_2，cipher_3，cipher_4，cipher_default）：  cipher_1： 加密算法为ECDHE-ECDSA-AES256-GCM-SHA384:HIGH:!MEDIUM:!LOW:!aNULL:!eNULL:!DES:!MD5:!PSK:!RC4:!kRSA:!SRP:!3DES:!DSS:!EXP:!CAMELLIA:@STRENGTH   cipher_2：加密算法为EECDH+AESGCM:EDH+AESGCM    cipher_3：加密算法为ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH    cipher_4：加密算法为ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!EDH    cipher_default： 加密算法为ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!AESGCM

        :param cipher: The cipher of this UpdateHostResponse.
        :type: str
        """
        self._cipher = cipher

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this UpdateHostResponse.

        企业项目ID

        :return: The enterprise_project_id of this UpdateHostResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this UpdateHostResponse.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this UpdateHostResponse.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def block_page(self):
        """Gets the block_page of this UpdateHostResponse.


        :return: The block_page of this UpdateHostResponse.
        :rtype: BlockPage
        """
        return self._block_page

    @block_page.setter
    def block_page(self, block_page):
        """Sets the block_page of this UpdateHostResponse.


        :param block_page: The block_page of this UpdateHostResponse.
        :type: BlockPage
        """
        self._block_page = block_page

    @property
    def web_tag(self):
        """Gets the web_tag of this UpdateHostResponse.

        域名名称

        :return: The web_tag of this UpdateHostResponse.
        :rtype: bool
        """
        return self._web_tag

    @web_tag.setter
    def web_tag(self, web_tag):
        """Sets the web_tag of this UpdateHostResponse.

        域名名称

        :param web_tag: The web_tag of this UpdateHostResponse.
        :type: bool
        """
        self._web_tag = web_tag

    @property
    def flag(self):
        """Gets the flag of this UpdateHostResponse.


        :return: The flag of this UpdateHostResponse.
        :rtype: Flag
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        """Sets the flag of this UpdateHostResponse.


        :param flag: The flag of this UpdateHostResponse.
        :type: Flag
        """
        self._flag = flag

    @property
    def exclusive_ip(self):
        """Gets the exclusive_ip of this UpdateHostResponse.

        是否使用独享ip

        :return: The exclusive_ip of this UpdateHostResponse.
        :rtype: bool
        """
        return self._exclusive_ip

    @exclusive_ip.setter
    def exclusive_ip(self, exclusive_ip):
        """Sets the exclusive_ip of this UpdateHostResponse.

        是否使用独享ip

        :param exclusive_ip: The exclusive_ip of this UpdateHostResponse.
        :type: bool
        """
        self._exclusive_ip = exclusive_ip

    @property
    def description(self):
        """Gets the description of this UpdateHostResponse.

        域名描述

        :return: The description of this UpdateHostResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateHostResponse.

        域名描述

        :param description: The description of this UpdateHostResponse.
        :type: str
        """
        self._description = description

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
        if not isinstance(other, UpdateHostResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
