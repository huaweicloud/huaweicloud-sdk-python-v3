# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PremiumWafHost:


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
        'project_id': 'str',
        'access_code': 'str',
        'protocol': 'str',
        'server': 'list[PremiumWafServer]',
        'certificateid': 'str',
        'certificatename': 'str',
        'tls': 'str',
        'cipher': 'str',
        'proxy': 'bool',
        'locked': 'int',
        'protect_status': 'int',
        'access_status': 'int',
        'timestamp': 'int',
        'block_page': 'BlockPage',
        'extend': 'dict(str, str)',
        'traffic_mark': 'TrafficMark'
    }

    attribute_map = {
        'id': 'id',
        'policyid': 'policyid',
        'hostname': 'hostname',
        'domainid': 'domainid',
        'project_id': 'project_id',
        'access_code': 'access_code',
        'protocol': 'protocol',
        'server': 'server',
        'certificateid': 'certificateid',
        'certificatename': 'certificatename',
        'tls': 'tls',
        'cipher': 'cipher',
        'proxy': 'proxy',
        'locked': 'locked',
        'protect_status': 'protect_status',
        'access_status': 'access_status',
        'timestamp': 'timestamp',
        'block_page': 'block_page',
        'extend': 'extend',
        'traffic_mark': 'traffic_mark'
    }

    def __init__(self, id=None, policyid=None, hostname=None, domainid=None, project_id=None, access_code=None, protocol=None, server=None, certificateid=None, certificatename=None, tls=None, cipher=None, proxy=None, locked=None, protect_status=None, access_status=None, timestamp=None, block_page=None, extend=None, traffic_mark=None):
        """PremiumWafHost - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._policyid = None
        self._hostname = None
        self._domainid = None
        self._project_id = None
        self._access_code = None
        self._protocol = None
        self._server = None
        self._certificateid = None
        self._certificatename = None
        self._tls = None
        self._cipher = None
        self._proxy = None
        self._locked = None
        self._protect_status = None
        self._access_status = None
        self._timestamp = None
        self._block_page = None
        self._extend = None
        self._traffic_mark = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if policyid is not None:
            self.policyid = policyid
        if hostname is not None:
            self.hostname = hostname
        if domainid is not None:
            self.domainid = domainid
        if project_id is not None:
            self.project_id = project_id
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
        if tls is not None:
            self.tls = tls
        if cipher is not None:
            self.cipher = cipher
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
        if block_page is not None:
            self.block_page = block_page
        if extend is not None:
            self.extend = extend
        if traffic_mark is not None:
            self.traffic_mark = traffic_mark

    @property
    def id(self):
        """Gets the id of this PremiumWafHost.

        域名id

        :return: The id of this PremiumWafHost.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PremiumWafHost.

        域名id

        :param id: The id of this PremiumWafHost.
        :type: str
        """
        self._id = id

    @property
    def policyid(self):
        """Gets the policyid of this PremiumWafHost.

        策略id

        :return: The policyid of this PremiumWafHost.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this PremiumWafHost.

        策略id

        :param policyid: The policyid of this PremiumWafHost.
        :type: str
        """
        self._policyid = policyid

    @property
    def hostname(self):
        """Gets the hostname of this PremiumWafHost.

        创建的云模式防护域名

        :return: The hostname of this PremiumWafHost.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this PremiumWafHost.

        创建的云模式防护域名

        :param hostname: The hostname of this PremiumWafHost.
        :type: str
        """
        self._hostname = hostname

    @property
    def domainid(self):
        """Gets the domainid of this PremiumWafHost.

        用户Domain ID

        :return: The domainid of this PremiumWafHost.
        :rtype: str
        """
        return self._domainid

    @domainid.setter
    def domainid(self, domainid):
        """Sets the domainid of this PremiumWafHost.

        用户Domain ID

        :param domainid: The domainid of this PremiumWafHost.
        :type: str
        """
        self._domainid = domainid

    @property
    def project_id(self):
        """Gets the project_id of this PremiumWafHost.

        用户的project_id

        :return: The project_id of this PremiumWafHost.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this PremiumWafHost.

        用户的project_id

        :param project_id: The project_id of this PremiumWafHost.
        :type: str
        """
        self._project_id = project_id

    @property
    def access_code(self):
        """Gets the access_code of this PremiumWafHost.

        cname前缀

        :return: The access_code of this PremiumWafHost.
        :rtype: str
        """
        return self._access_code

    @access_code.setter
    def access_code(self, access_code):
        """Sets the access_code of this PremiumWafHost.

        cname前缀

        :param access_code: The access_code of this PremiumWafHost.
        :type: str
        """
        self._access_code = access_code

    @property
    def protocol(self):
        """Gets the protocol of this PremiumWafHost.

        http协议类型

        :return: The protocol of this PremiumWafHost.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this PremiumWafHost.

        http协议类型

        :param protocol: The protocol of this PremiumWafHost.
        :type: str
        """
        self._protocol = protocol

    @property
    def server(self):
        """Gets the server of this PremiumWafHost.

        源站信息

        :return: The server of this PremiumWafHost.
        :rtype: list[PremiumWafServer]
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this PremiumWafHost.

        源站信息

        :param server: The server of this PremiumWafHost.
        :type: list[PremiumWafServer]
        """
        self._server = server

    @property
    def certificateid(self):
        """Gets the certificateid of this PremiumWafHost.

        返回的证书id

        :return: The certificateid of this PremiumWafHost.
        :rtype: str
        """
        return self._certificateid

    @certificateid.setter
    def certificateid(self, certificateid):
        """Sets the certificateid of this PremiumWafHost.

        返回的证书id

        :param certificateid: The certificateid of this PremiumWafHost.
        :type: str
        """
        self._certificateid = certificateid

    @property
    def certificatename(self):
        """Gets the certificatename of this PremiumWafHost.

        证书名称

        :return: The certificatename of this PremiumWafHost.
        :rtype: str
        """
        return self._certificatename

    @certificatename.setter
    def certificatename(self, certificatename):
        """Sets the certificatename of this PremiumWafHost.

        证书名称

        :param certificatename: The certificatename of this PremiumWafHost.
        :type: str
        """
        self._certificatename = certificatename

    @property
    def tls(self):
        """Gets the tls of this PremiumWafHost.

        支持最低的TLS版本

        :return: The tls of this PremiumWafHost.
        :rtype: str
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """Sets the tls of this PremiumWafHost.

        支持最低的TLS版本

        :param tls: The tls of this PremiumWafHost.
        :type: str
        """
        self._tls = tls

    @property
    def cipher(self):
        """Gets the cipher of this PremiumWafHost.

        加密套件代码

        :return: The cipher of this PremiumWafHost.
        :rtype: str
        """
        return self._cipher

    @cipher.setter
    def cipher(self, cipher):
        """Sets the cipher of this PremiumWafHost.

        加密套件代码

        :param cipher: The cipher of this PremiumWafHost.
        :type: str
        """
        self._cipher = cipher

    @property
    def proxy(self):
        """Gets the proxy of this PremiumWafHost.

        是否开启了代理

        :return: The proxy of this PremiumWafHost.
        :rtype: bool
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this PremiumWafHost.

        是否开启了代理

        :param proxy: The proxy of this PremiumWafHost.
        :type: bool
        """
        self._proxy = proxy

    @property
    def locked(self):
        """Gets the locked of this PremiumWafHost.

        锁定状态

        :return: The locked of this PremiumWafHost.
        :rtype: int
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this PremiumWafHost.

        锁定状态

        :param locked: The locked of this PremiumWafHost.
        :type: int
        """
        self._locked = locked

    @property
    def protect_status(self):
        """Gets the protect_status of this PremiumWafHost.

        防护状态

        :return: The protect_status of this PremiumWafHost.
        :rtype: int
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this PremiumWafHost.

        防护状态

        :param protect_status: The protect_status of this PremiumWafHost.
        :type: int
        """
        self._protect_status = protect_status

    @property
    def access_status(self):
        """Gets the access_status of this PremiumWafHost.

        接入状态

        :return: The access_status of this PremiumWafHost.
        :rtype: int
        """
        return self._access_status

    @access_status.setter
    def access_status(self, access_status):
        """Sets the access_status of this PremiumWafHost.

        接入状态

        :param access_status: The access_status of this PremiumWafHost.
        :type: int
        """
        self._access_status = access_status

    @property
    def timestamp(self):
        """Gets the timestamp of this PremiumWafHost.

        创建防护域名的时间

        :return: The timestamp of this PremiumWafHost.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this PremiumWafHost.

        创建防护域名的时间

        :param timestamp: The timestamp of this PremiumWafHost.
        :type: int
        """
        self._timestamp = timestamp

    @property
    def block_page(self):
        """Gets the block_page of this PremiumWafHost.


        :return: The block_page of this PremiumWafHost.
        :rtype: BlockPage
        """
        return self._block_page

    @block_page.setter
    def block_page(self, block_page):
        """Sets the block_page of this PremiumWafHost.


        :param block_page: The block_page of this PremiumWafHost.
        :type: BlockPage
        """
        self._block_page = block_page

    @property
    def extend(self):
        """Gets the extend of this PremiumWafHost.

        可扩展属性

        :return: The extend of this PremiumWafHost.
        :rtype: dict(str, str)
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        """Sets the extend of this PremiumWafHost.

        可扩展属性

        :param extend: The extend of this PremiumWafHost.
        :type: dict(str, str)
        """
        self._extend = extend

    @property
    def traffic_mark(self):
        """Gets the traffic_mark of this PremiumWafHost.


        :return: The traffic_mark of this PremiumWafHost.
        :rtype: TrafficMark
        """
        return self._traffic_mark

    @traffic_mark.setter
    def traffic_mark(self, traffic_mark):
        """Sets the traffic_mark of this PremiumWafHost.


        :param traffic_mark: The traffic_mark of this PremiumWafHost.
        :type: TrafficMark
        """
        self._traffic_mark = traffic_mark

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
        if not isinstance(other, PremiumWafHost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
