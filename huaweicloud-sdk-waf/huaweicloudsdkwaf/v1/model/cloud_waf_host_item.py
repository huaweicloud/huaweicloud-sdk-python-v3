# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloudWafHostItem:

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
        'region': 'str',
        'description': 'str',
        'server': 'list[CloudWafServer]',
        'type': 'int',
        'proxy': 'bool',
        'hostname': 'str',
        'access_code': 'str',
        'policyid': 'str',
        'timestamp': 'int',
        'protect_status': 'int',
        'access_status': 'int',
        'exclusive_ip': 'bool',
        'paid_type': 'str',
        'web_tag': 'str',
        'flag': 'Flag',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'hostid': 'hostid',
        'region': 'region',
        'description': 'description',
        'server': 'server',
        'type': 'type',
        'proxy': 'proxy',
        'hostname': 'hostname',
        'access_code': 'access_code',
        'policyid': 'policyid',
        'timestamp': 'timestamp',
        'protect_status': 'protect_status',
        'access_status': 'access_status',
        'exclusive_ip': 'exclusive_ip',
        'paid_type': 'paid_type',
        'web_tag': 'web_tag',
        'flag': 'flag',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, id=None, hostid=None, region=None, description=None, server=None, type=None, proxy=None, hostname=None, access_code=None, policyid=None, timestamp=None, protect_status=None, access_status=None, exclusive_ip=None, paid_type=None, web_tag=None, flag=None, enterprise_project_id=None):
        r"""CloudWafHostItem

        The model defined in huaweicloud sdk

        :param id: 域名id
        :type id: str
        :param hostid: 域名id
        :type hostid: str
        :param region: 华为云区域ID，控制台创建的域名会携带此参数，api调用创建的域名此参数为空，可以通过华为云上地区和终端节点文档查询区域ID对应的中文名称
        :type region: str
        :param description: 域名描述信息，可选参数。
        :type description: str
        :param server: 防护域名的源站服务器配置信息
        :type server: list[:class:`huaweicloudsdkwaf.v1.CloudWafServer`]
        :param type: WAF部署模式，默认是1，目前仅支持反代模式，冗余参数
        :type type: int
        :param proxy: 防护域名是否使用代理   - false：不使用代理   - true：使用代理
        :type proxy: bool
        :param hostname: 创建的云模式防护域名
        :type hostname: str
        :param access_code: cname前缀
        :type access_code: str
        :param policyid: 防护策略id
        :type policyid: str
        :param timestamp: 创建防护域名的时间
        :type timestamp: int
        :param protect_status: 域名防护状态：  - -1：bypass，该域名的请求直接到达其后端服务器，不再经过WAF  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测
        :type protect_status: int
        :param access_status: 域名接入状态，0表示未接入，1表示已接入
        :type access_status: int
        :param exclusive_ip: 是否使用独享ip   - true：使用独享ip   - false：不实用独享ip
        :type exclusive_ip: bool
        :param paid_type: 套餐付费模式，默认值为prePaid。prePaid：包周期款模式；postPaid：按需模式。
        :type paid_type: str
        :param web_tag: 网站名称，对应WAF控制台域名详情中的网站名称
        :type web_tag: str
        :param flag: 
        :type flag: :class:`huaweicloudsdkwaf.v1.Flag`
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        """
        
        

        self._id = None
        self._hostid = None
        self._region = None
        self._description = None
        self._server = None
        self._type = None
        self._proxy = None
        self._hostname = None
        self._access_code = None
        self._policyid = None
        self._timestamp = None
        self._protect_status = None
        self._access_status = None
        self._exclusive_ip = None
        self._paid_type = None
        self._web_tag = None
        self._flag = None
        self._enterprise_project_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if hostid is not None:
            self.hostid = hostid
        if region is not None:
            self.region = region
        if description is not None:
            self.description = description
        if server is not None:
            self.server = server
        if type is not None:
            self.type = type
        if proxy is not None:
            self.proxy = proxy
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
        if flag is not None:
            self.flag = flag
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        r"""Gets the id of this CloudWafHostItem.

        域名id

        :return: The id of this CloudWafHostItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CloudWafHostItem.

        域名id

        :param id: The id of this CloudWafHostItem.
        :type id: str
        """
        self._id = id

    @property
    def hostid(self):
        r"""Gets the hostid of this CloudWafHostItem.

        域名id

        :return: The hostid of this CloudWafHostItem.
        :rtype: str
        """
        return self._hostid

    @hostid.setter
    def hostid(self, hostid):
        r"""Sets the hostid of this CloudWafHostItem.

        域名id

        :param hostid: The hostid of this CloudWafHostItem.
        :type hostid: str
        """
        self._hostid = hostid

    @property
    def region(self):
        r"""Gets the region of this CloudWafHostItem.

        华为云区域ID，控制台创建的域名会携带此参数，api调用创建的域名此参数为空，可以通过华为云上地区和终端节点文档查询区域ID对应的中文名称

        :return: The region of this CloudWafHostItem.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this CloudWafHostItem.

        华为云区域ID，控制台创建的域名会携带此参数，api调用创建的域名此参数为空，可以通过华为云上地区和终端节点文档查询区域ID对应的中文名称

        :param region: The region of this CloudWafHostItem.
        :type region: str
        """
        self._region = region

    @property
    def description(self):
        r"""Gets the description of this CloudWafHostItem.

        域名描述信息，可选参数。

        :return: The description of this CloudWafHostItem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CloudWafHostItem.

        域名描述信息，可选参数。

        :param description: The description of this CloudWafHostItem.
        :type description: str
        """
        self._description = description

    @property
    def server(self):
        r"""Gets the server of this CloudWafHostItem.

        防护域名的源站服务器配置信息

        :return: The server of this CloudWafHostItem.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.CloudWafServer`]
        """
        return self._server

    @server.setter
    def server(self, server):
        r"""Sets the server of this CloudWafHostItem.

        防护域名的源站服务器配置信息

        :param server: The server of this CloudWafHostItem.
        :type server: list[:class:`huaweicloudsdkwaf.v1.CloudWafServer`]
        """
        self._server = server

    @property
    def type(self):
        r"""Gets the type of this CloudWafHostItem.

        WAF部署模式，默认是1，目前仅支持反代模式，冗余参数

        :return: The type of this CloudWafHostItem.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CloudWafHostItem.

        WAF部署模式，默认是1，目前仅支持反代模式，冗余参数

        :param type: The type of this CloudWafHostItem.
        :type type: int
        """
        self._type = type

    @property
    def proxy(self):
        r"""Gets the proxy of this CloudWafHostItem.

        防护域名是否使用代理   - false：不使用代理   - true：使用代理

        :return: The proxy of this CloudWafHostItem.
        :rtype: bool
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        r"""Sets the proxy of this CloudWafHostItem.

        防护域名是否使用代理   - false：不使用代理   - true：使用代理

        :param proxy: The proxy of this CloudWafHostItem.
        :type proxy: bool
        """
        self._proxy = proxy

    @property
    def hostname(self):
        r"""Gets the hostname of this CloudWafHostItem.

        创建的云模式防护域名

        :return: The hostname of this CloudWafHostItem.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        r"""Sets the hostname of this CloudWafHostItem.

        创建的云模式防护域名

        :param hostname: The hostname of this CloudWafHostItem.
        :type hostname: str
        """
        self._hostname = hostname

    @property
    def access_code(self):
        r"""Gets the access_code of this CloudWafHostItem.

        cname前缀

        :return: The access_code of this CloudWafHostItem.
        :rtype: str
        """
        return self._access_code

    @access_code.setter
    def access_code(self, access_code):
        r"""Sets the access_code of this CloudWafHostItem.

        cname前缀

        :param access_code: The access_code of this CloudWafHostItem.
        :type access_code: str
        """
        self._access_code = access_code

    @property
    def policyid(self):
        r"""Gets the policyid of this CloudWafHostItem.

        防护策略id

        :return: The policyid of this CloudWafHostItem.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        r"""Sets the policyid of this CloudWafHostItem.

        防护策略id

        :param policyid: The policyid of this CloudWafHostItem.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def timestamp(self):
        r"""Gets the timestamp of this CloudWafHostItem.

        创建防护域名的时间

        :return: The timestamp of this CloudWafHostItem.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this CloudWafHostItem.

        创建防护域名的时间

        :param timestamp: The timestamp of this CloudWafHostItem.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def protect_status(self):
        r"""Gets the protect_status of this CloudWafHostItem.

        域名防护状态：  - -1：bypass，该域名的请求直接到达其后端服务器，不再经过WAF  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测

        :return: The protect_status of this CloudWafHostItem.
        :rtype: int
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this CloudWafHostItem.

        域名防护状态：  - -1：bypass，该域名的请求直接到达其后端服务器，不再经过WAF  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测

        :param protect_status: The protect_status of this CloudWafHostItem.
        :type protect_status: int
        """
        self._protect_status = protect_status

    @property
    def access_status(self):
        r"""Gets the access_status of this CloudWafHostItem.

        域名接入状态，0表示未接入，1表示已接入

        :return: The access_status of this CloudWafHostItem.
        :rtype: int
        """
        return self._access_status

    @access_status.setter
    def access_status(self, access_status):
        r"""Sets the access_status of this CloudWafHostItem.

        域名接入状态，0表示未接入，1表示已接入

        :param access_status: The access_status of this CloudWafHostItem.
        :type access_status: int
        """
        self._access_status = access_status

    @property
    def exclusive_ip(self):
        r"""Gets the exclusive_ip of this CloudWafHostItem.

        是否使用独享ip   - true：使用独享ip   - false：不实用独享ip

        :return: The exclusive_ip of this CloudWafHostItem.
        :rtype: bool
        """
        return self._exclusive_ip

    @exclusive_ip.setter
    def exclusive_ip(self, exclusive_ip):
        r"""Sets the exclusive_ip of this CloudWafHostItem.

        是否使用独享ip   - true：使用独享ip   - false：不实用独享ip

        :param exclusive_ip: The exclusive_ip of this CloudWafHostItem.
        :type exclusive_ip: bool
        """
        self._exclusive_ip = exclusive_ip

    @property
    def paid_type(self):
        r"""Gets the paid_type of this CloudWafHostItem.

        套餐付费模式，默认值为prePaid。prePaid：包周期款模式；postPaid：按需模式。

        :return: The paid_type of this CloudWafHostItem.
        :rtype: str
        """
        return self._paid_type

    @paid_type.setter
    def paid_type(self, paid_type):
        r"""Sets the paid_type of this CloudWafHostItem.

        套餐付费模式，默认值为prePaid。prePaid：包周期款模式；postPaid：按需模式。

        :param paid_type: The paid_type of this CloudWafHostItem.
        :type paid_type: str
        """
        self._paid_type = paid_type

    @property
    def web_tag(self):
        r"""Gets the web_tag of this CloudWafHostItem.

        网站名称，对应WAF控制台域名详情中的网站名称

        :return: The web_tag of this CloudWafHostItem.
        :rtype: str
        """
        return self._web_tag

    @web_tag.setter
    def web_tag(self, web_tag):
        r"""Sets the web_tag of this CloudWafHostItem.

        网站名称，对应WAF控制台域名详情中的网站名称

        :param web_tag: The web_tag of this CloudWafHostItem.
        :type web_tag: str
        """
        self._web_tag = web_tag

    @property
    def flag(self):
        r"""Gets the flag of this CloudWafHostItem.

        :return: The flag of this CloudWafHostItem.
        :rtype: :class:`huaweicloudsdkwaf.v1.Flag`
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        r"""Sets the flag of this CloudWafHostItem.

        :param flag: The flag of this CloudWafHostItem.
        :type flag: :class:`huaweicloudsdkwaf.v1.Flag`
        """
        self._flag = flag

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CloudWafHostItem.

        企业项目id

        :return: The enterprise_project_id of this CloudWafHostItem.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CloudWafHostItem.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this CloudWafHostItem.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, CloudWafHostItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
