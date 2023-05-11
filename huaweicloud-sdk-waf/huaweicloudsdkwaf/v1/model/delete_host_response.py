# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteHostResponse(SdkResponse):

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
        'hostid': 'str',
        'description': 'str',
        'type': 'int',
        'proxy': 'bool',
        'flag': 'Flag',
        'hostname': 'str',
        'access_code': 'str',
        'policyid': 'str',
        'timestamp': 'int',
        'protect_status': 'int',
        'access_status': 'int',
        'exclusive_ip': 'bool',
        'paid_type': 'str',
        'web_tag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'hostid': 'hostid',
        'description': 'description',
        'type': 'type',
        'proxy': 'proxy',
        'flag': 'flag',
        'hostname': 'hostname',
        'access_code': 'access_code',
        'policyid': 'policyid',
        'timestamp': 'timestamp',
        'protect_status': 'protect_status',
        'access_status': 'access_status',
        'exclusive_ip': 'exclusive_ip',
        'paid_type': 'paid_type',
        'web_tag': 'web_tag'
    }

    def __init__(self, id=None, hostid=None, description=None, type=None, proxy=None, flag=None, hostname=None, access_code=None, policyid=None, timestamp=None, protect_status=None, access_status=None, exclusive_ip=None, paid_type=None, web_tag=None):
        """DeleteHostResponse

        The model defined in huaweicloud sdk

        :param id: 域名id
        :type id: str
        :param hostid: 域名id
        :type hostid: str
        :param description: 描述信息
        :type description: str
        :param type: WAF部署模式，默认是1，目前仅支持反代模式
        :type type: int
        :param proxy: 防护域名是否使用代理    - false：不使用代理   - true：使用代理
        :type proxy: bool
        :param flag: 
        :type flag: :class:`huaweicloudsdkwaf.v1.Flag`
        :param hostname: 创建的云模式防护域名
        :type hostname: str
        :param access_code: cname后缀
        :type access_code: str
        :param policyid: 策略id
        :type policyid: str
        :param timestamp: 创建防护域名的时间
        :type timestamp: int
        :param protect_status: 域名防护状态：  - -1：bypass，该域名的请求直接到达其后端服务器，不再经过WAF  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测
        :type protect_status: int
        :param access_status: 接入状态，0： 未接入，1：已接入
        :type access_status: int
        :param exclusive_ip: 是否使用独享ip   - true：使用独享ip   - false：不实用独享ip
        :type exclusive_ip: bool
        :param paid_type: 套餐付费模式，默认值为prePaid。prePaid：包周期款模式；postPaid：按需模式。
        :type paid_type: str
        :param web_tag: 网站名称，对应WAF控制台域名详情中的网站名称
        :type web_tag: str
        """
        
        super(DeleteHostResponse, self).__init__()

        self._id = None
        self._hostid = None
        self._description = None
        self._type = None
        self._proxy = None
        self._flag = None
        self._hostname = None
        self._access_code = None
        self._policyid = None
        self._timestamp = None
        self._protect_status = None
        self._access_status = None
        self._exclusive_ip = None
        self._paid_type = None
        self._web_tag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if hostid is not None:
            self.hostid = hostid
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if proxy is not None:
            self.proxy = proxy
        if flag is not None:
            self.flag = flag
        if hostname is not None:
            self.hostname = hostname
        if access_code is not None:
            self.access_code = access_code
        if policyid is not None:
            self.policyid = policyid
        if timestamp is not None:
            self.timestamp = timestamp
        if protect_status is not None:
            self.protect_status = protect_status
        if access_status is not None:
            self.access_status = access_status
        if exclusive_ip is not None:
            self.exclusive_ip = exclusive_ip
        if paid_type is not None:
            self.paid_type = paid_type
        if web_tag is not None:
            self.web_tag = web_tag

    @property
    def id(self):
        """Gets the id of this DeleteHostResponse.

        域名id

        :return: The id of this DeleteHostResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeleteHostResponse.

        域名id

        :param id: The id of this DeleteHostResponse.
        :type id: str
        """
        self._id = id

    @property
    def hostid(self):
        """Gets the hostid of this DeleteHostResponse.

        域名id

        :return: The hostid of this DeleteHostResponse.
        :rtype: str
        """
        return self._hostid

    @hostid.setter
    def hostid(self, hostid):
        """Sets the hostid of this DeleteHostResponse.

        域名id

        :param hostid: The hostid of this DeleteHostResponse.
        :type hostid: str
        """
        self._hostid = hostid

    @property
    def description(self):
        """Gets the description of this DeleteHostResponse.

        描述信息

        :return: The description of this DeleteHostResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeleteHostResponse.

        描述信息

        :param description: The description of this DeleteHostResponse.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        """Gets the type of this DeleteHostResponse.

        WAF部署模式，默认是1，目前仅支持反代模式

        :return: The type of this DeleteHostResponse.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeleteHostResponse.

        WAF部署模式，默认是1，目前仅支持反代模式

        :param type: The type of this DeleteHostResponse.
        :type type: int
        """
        self._type = type

    @property
    def proxy(self):
        """Gets the proxy of this DeleteHostResponse.

        防护域名是否使用代理    - false：不使用代理   - true：使用代理

        :return: The proxy of this DeleteHostResponse.
        :rtype: bool
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this DeleteHostResponse.

        防护域名是否使用代理    - false：不使用代理   - true：使用代理

        :param proxy: The proxy of this DeleteHostResponse.
        :type proxy: bool
        """
        self._proxy = proxy

    @property
    def flag(self):
        """Gets the flag of this DeleteHostResponse.

        :return: The flag of this DeleteHostResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.Flag`
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        """Sets the flag of this DeleteHostResponse.

        :param flag: The flag of this DeleteHostResponse.
        :type flag: :class:`huaweicloudsdkwaf.v1.Flag`
        """
        self._flag = flag

    @property
    def hostname(self):
        """Gets the hostname of this DeleteHostResponse.

        创建的云模式防护域名

        :return: The hostname of this DeleteHostResponse.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this DeleteHostResponse.

        创建的云模式防护域名

        :param hostname: The hostname of this DeleteHostResponse.
        :type hostname: str
        """
        self._hostname = hostname

    @property
    def access_code(self):
        """Gets the access_code of this DeleteHostResponse.

        cname后缀

        :return: The access_code of this DeleteHostResponse.
        :rtype: str
        """
        return self._access_code

    @access_code.setter
    def access_code(self, access_code):
        """Sets the access_code of this DeleteHostResponse.

        cname后缀

        :param access_code: The access_code of this DeleteHostResponse.
        :type access_code: str
        """
        self._access_code = access_code

    @property
    def policyid(self):
        """Gets the policyid of this DeleteHostResponse.

        策略id

        :return: The policyid of this DeleteHostResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this DeleteHostResponse.

        策略id

        :param policyid: The policyid of this DeleteHostResponse.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def timestamp(self):
        """Gets the timestamp of this DeleteHostResponse.

        创建防护域名的时间

        :return: The timestamp of this DeleteHostResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this DeleteHostResponse.

        创建防护域名的时间

        :param timestamp: The timestamp of this DeleteHostResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def protect_status(self):
        """Gets the protect_status of this DeleteHostResponse.

        域名防护状态：  - -1：bypass，该域名的请求直接到达其后端服务器，不再经过WAF  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测

        :return: The protect_status of this DeleteHostResponse.
        :rtype: int
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this DeleteHostResponse.

        域名防护状态：  - -1：bypass，该域名的请求直接到达其后端服务器，不再经过WAF  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测

        :param protect_status: The protect_status of this DeleteHostResponse.
        :type protect_status: int
        """
        self._protect_status = protect_status

    @property
    def access_status(self):
        """Gets the access_status of this DeleteHostResponse.

        接入状态，0： 未接入，1：已接入

        :return: The access_status of this DeleteHostResponse.
        :rtype: int
        """
        return self._access_status

    @access_status.setter
    def access_status(self, access_status):
        """Sets the access_status of this DeleteHostResponse.

        接入状态，0： 未接入，1：已接入

        :param access_status: The access_status of this DeleteHostResponse.
        :type access_status: int
        """
        self._access_status = access_status

    @property
    def exclusive_ip(self):
        """Gets the exclusive_ip of this DeleteHostResponse.

        是否使用独享ip   - true：使用独享ip   - false：不实用独享ip

        :return: The exclusive_ip of this DeleteHostResponse.
        :rtype: bool
        """
        return self._exclusive_ip

    @exclusive_ip.setter
    def exclusive_ip(self, exclusive_ip):
        """Sets the exclusive_ip of this DeleteHostResponse.

        是否使用独享ip   - true：使用独享ip   - false：不实用独享ip

        :param exclusive_ip: The exclusive_ip of this DeleteHostResponse.
        :type exclusive_ip: bool
        """
        self._exclusive_ip = exclusive_ip

    @property
    def paid_type(self):
        """Gets the paid_type of this DeleteHostResponse.

        套餐付费模式，默认值为prePaid。prePaid：包周期款模式；postPaid：按需模式。

        :return: The paid_type of this DeleteHostResponse.
        :rtype: str
        """
        return self._paid_type

    @paid_type.setter
    def paid_type(self, paid_type):
        """Sets the paid_type of this DeleteHostResponse.

        套餐付费模式，默认值为prePaid。prePaid：包周期款模式；postPaid：按需模式。

        :param paid_type: The paid_type of this DeleteHostResponse.
        :type paid_type: str
        """
        self._paid_type = paid_type

    @property
    def web_tag(self):
        """Gets the web_tag of this DeleteHostResponse.

        网站名称，对应WAF控制台域名详情中的网站名称

        :return: The web_tag of this DeleteHostResponse.
        :rtype: str
        """
        return self._web_tag

    @web_tag.setter
    def web_tag(self, web_tag):
        """Sets the web_tag of this DeleteHostResponse.

        网站名称，对应WAF控制台域名详情中的网站名称

        :param web_tag: The web_tag of this DeleteHostResponse.
        :type web_tag: str
        """
        self._web_tag = web_tag

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
        if not isinstance(other, DeleteHostResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
