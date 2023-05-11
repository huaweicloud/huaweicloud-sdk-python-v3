# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompositeHostResponse:

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
        'hostname': 'str',
        'policyid': 'str',
        'access_code': 'str',
        'protect_status': 'int',
        'access_status': 'int',
        'proxy': 'bool',
        'timestamp': 'int',
        'paid_type': 'str',
        'flag': 'Flag',
        'waf_type': 'str',
        'web_tag': 'str',
        'access_progress': 'list[AccessProgress]',
        'premium_waf_instances': 'list[PremiumWafInstances]',
        'description': 'str',
        'exclusive_ip': 'bool',
        'region': 'str'
    }

    attribute_map = {
        'id': 'id',
        'hostid': 'hostid',
        'hostname': 'hostname',
        'policyid': 'policyid',
        'access_code': 'access_code',
        'protect_status': 'protect_status',
        'access_status': 'access_status',
        'proxy': 'proxy',
        'timestamp': 'timestamp',
        'paid_type': 'paid_type',
        'flag': 'flag',
        'waf_type': 'waf_type',
        'web_tag': 'web_tag',
        'access_progress': 'access_progress',
        'premium_waf_instances': 'premium_waf_instances',
        'description': 'description',
        'exclusive_ip': 'exclusive_ip',
        'region': 'region'
    }

    def __init__(self, id=None, hostid=None, hostname=None, policyid=None, access_code=None, protect_status=None, access_status=None, proxy=None, timestamp=None, paid_type=None, flag=None, waf_type=None, web_tag=None, access_progress=None, premium_waf_instances=None, description=None, exclusive_ip=None, region=None):
        """CompositeHostResponse

        The model defined in huaweicloud sdk

        :param id: 域名id
        :type id: str
        :param hostid: 域名id
        :type hostid: str
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
        :param proxy: 防护域名是否使用代理   - false：不使用代理   - true：使用代理
        :type proxy: bool
        :param timestamp: 创建防护域名的时间
        :type timestamp: int
        :param paid_type: 套餐付费模式，默认值为prePaid。prePaid：包周期款模式；postPaid：按需模式。
        :type paid_type: str
        :param flag: 
        :type flag: :class:`huaweicloudsdkwaf.v1.Flag`
        :param waf_type: 域名所属WAF模式,cloud为云模式，premium为独享模式
        :type waf_type: str
        :param web_tag: 网站名称，对应WAF控制台域名详情中的网站名称
        :type web_tag: str
        :param access_progress: 接入进度，仅用于新版console(前端)使用
        :type access_progress: list[:class:`huaweicloudsdkwaf.v1.AccessProgress`]
        :param premium_waf_instances: 租户引擎实例信息列表
        :type premium_waf_instances: list[:class:`huaweicloudsdkwaf.v1.PremiumWafInstances`]
        :param description: 域名描述
        :type description: str
        :param exclusive_ip: 是否使用独享ip   - true：使用独享ip   - false：不实用独享ip
        :type exclusive_ip: bool
        :param region: 华为云区域ID，控制台创建的域名会携带此参数，api调用创建的域名此参数为空，可以通过华为云上地区和终端节点文档查询区域ID对应的中文名称
        :type region: str
        """
        
        

        self._id = None
        self._hostid = None
        self._hostname = None
        self._policyid = None
        self._access_code = None
        self._protect_status = None
        self._access_status = None
        self._proxy = None
        self._timestamp = None
        self._paid_type = None
        self._flag = None
        self._waf_type = None
        self._web_tag = None
        self._access_progress = None
        self._premium_waf_instances = None
        self._description = None
        self._exclusive_ip = None
        self._region = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if hostid is not None:
            self.hostid = hostid
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
        if proxy is not None:
            self.proxy = proxy
        if timestamp is not None:
            self.timestamp = timestamp
        if paid_type is not None:
            self.paid_type = paid_type
        if flag is not None:
            self.flag = flag
        if waf_type is not None:
            self.waf_type = waf_type
        if web_tag is not None:
            self.web_tag = web_tag
        if access_progress is not None:
            self.access_progress = access_progress
        if premium_waf_instances is not None:
            self.premium_waf_instances = premium_waf_instances
        if description is not None:
            self.description = description
        if exclusive_ip is not None:
            self.exclusive_ip = exclusive_ip
        if region is not None:
            self.region = region

    @property
    def id(self):
        """Gets the id of this CompositeHostResponse.

        域名id

        :return: The id of this CompositeHostResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CompositeHostResponse.

        域名id

        :param id: The id of this CompositeHostResponse.
        :type id: str
        """
        self._id = id

    @property
    def hostid(self):
        """Gets the hostid of this CompositeHostResponse.

        域名id

        :return: The hostid of this CompositeHostResponse.
        :rtype: str
        """
        return self._hostid

    @hostid.setter
    def hostid(self, hostid):
        """Sets the hostid of this CompositeHostResponse.

        域名id

        :param hostid: The hostid of this CompositeHostResponse.
        :type hostid: str
        """
        self._hostid = hostid

    @property
    def hostname(self):
        """Gets the hostname of this CompositeHostResponse.

        创建的云模式防护域名

        :return: The hostname of this CompositeHostResponse.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this CompositeHostResponse.

        创建的云模式防护域名

        :param hostname: The hostname of this CompositeHostResponse.
        :type hostname: str
        """
        self._hostname = hostname

    @property
    def policyid(self):
        """Gets the policyid of this CompositeHostResponse.

        策略id

        :return: The policyid of this CompositeHostResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this CompositeHostResponse.

        策略id

        :param policyid: The policyid of this CompositeHostResponse.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def access_code(self):
        """Gets the access_code of this CompositeHostResponse.

        cname前缀

        :return: The access_code of this CompositeHostResponse.
        :rtype: str
        """
        return self._access_code

    @access_code.setter
    def access_code(self, access_code):
        """Sets the access_code of this CompositeHostResponse.

        cname前缀

        :param access_code: The access_code of this CompositeHostResponse.
        :type access_code: str
        """
        self._access_code = access_code

    @property
    def protect_status(self):
        """Gets the protect_status of this CompositeHostResponse.

        域名防护状态：  - -1：bypass，该域名的请求直接到达其后端服务器，不再经过WAF  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测

        :return: The protect_status of this CompositeHostResponse.
        :rtype: int
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this CompositeHostResponse.

        域名防护状态：  - -1：bypass，该域名的请求直接到达其后端服务器，不再经过WAF  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测

        :param protect_status: The protect_status of this CompositeHostResponse.
        :type protect_status: int
        """
        self._protect_status = protect_status

    @property
    def access_status(self):
        """Gets the access_status of this CompositeHostResponse.

        域名接入状态，0表示未接入，1表示已接入

        :return: The access_status of this CompositeHostResponse.
        :rtype: int
        """
        return self._access_status

    @access_status.setter
    def access_status(self, access_status):
        """Sets the access_status of this CompositeHostResponse.

        域名接入状态，0表示未接入，1表示已接入

        :param access_status: The access_status of this CompositeHostResponse.
        :type access_status: int
        """
        self._access_status = access_status

    @property
    def proxy(self):
        """Gets the proxy of this CompositeHostResponse.

        防护域名是否使用代理   - false：不使用代理   - true：使用代理

        :return: The proxy of this CompositeHostResponse.
        :rtype: bool
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this CompositeHostResponse.

        防护域名是否使用代理   - false：不使用代理   - true：使用代理

        :param proxy: The proxy of this CompositeHostResponse.
        :type proxy: bool
        """
        self._proxy = proxy

    @property
    def timestamp(self):
        """Gets the timestamp of this CompositeHostResponse.

        创建防护域名的时间

        :return: The timestamp of this CompositeHostResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this CompositeHostResponse.

        创建防护域名的时间

        :param timestamp: The timestamp of this CompositeHostResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def paid_type(self):
        """Gets the paid_type of this CompositeHostResponse.

        套餐付费模式，默认值为prePaid。prePaid：包周期款模式；postPaid：按需模式。

        :return: The paid_type of this CompositeHostResponse.
        :rtype: str
        """
        return self._paid_type

    @paid_type.setter
    def paid_type(self, paid_type):
        """Sets the paid_type of this CompositeHostResponse.

        套餐付费模式，默认值为prePaid。prePaid：包周期款模式；postPaid：按需模式。

        :param paid_type: The paid_type of this CompositeHostResponse.
        :type paid_type: str
        """
        self._paid_type = paid_type

    @property
    def flag(self):
        """Gets the flag of this CompositeHostResponse.

        :return: The flag of this CompositeHostResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.Flag`
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        """Sets the flag of this CompositeHostResponse.

        :param flag: The flag of this CompositeHostResponse.
        :type flag: :class:`huaweicloudsdkwaf.v1.Flag`
        """
        self._flag = flag

    @property
    def waf_type(self):
        """Gets the waf_type of this CompositeHostResponse.

        域名所属WAF模式,cloud为云模式，premium为独享模式

        :return: The waf_type of this CompositeHostResponse.
        :rtype: str
        """
        return self._waf_type

    @waf_type.setter
    def waf_type(self, waf_type):
        """Sets the waf_type of this CompositeHostResponse.

        域名所属WAF模式,cloud为云模式，premium为独享模式

        :param waf_type: The waf_type of this CompositeHostResponse.
        :type waf_type: str
        """
        self._waf_type = waf_type

    @property
    def web_tag(self):
        """Gets the web_tag of this CompositeHostResponse.

        网站名称，对应WAF控制台域名详情中的网站名称

        :return: The web_tag of this CompositeHostResponse.
        :rtype: str
        """
        return self._web_tag

    @web_tag.setter
    def web_tag(self, web_tag):
        """Sets the web_tag of this CompositeHostResponse.

        网站名称，对应WAF控制台域名详情中的网站名称

        :param web_tag: The web_tag of this CompositeHostResponse.
        :type web_tag: str
        """
        self._web_tag = web_tag

    @property
    def access_progress(self):
        """Gets the access_progress of this CompositeHostResponse.

        接入进度，仅用于新版console(前端)使用

        :return: The access_progress of this CompositeHostResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.AccessProgress`]
        """
        return self._access_progress

    @access_progress.setter
    def access_progress(self, access_progress):
        """Sets the access_progress of this CompositeHostResponse.

        接入进度，仅用于新版console(前端)使用

        :param access_progress: The access_progress of this CompositeHostResponse.
        :type access_progress: list[:class:`huaweicloudsdkwaf.v1.AccessProgress`]
        """
        self._access_progress = access_progress

    @property
    def premium_waf_instances(self):
        """Gets the premium_waf_instances of this CompositeHostResponse.

        租户引擎实例信息列表

        :return: The premium_waf_instances of this CompositeHostResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.PremiumWafInstances`]
        """
        return self._premium_waf_instances

    @premium_waf_instances.setter
    def premium_waf_instances(self, premium_waf_instances):
        """Sets the premium_waf_instances of this CompositeHostResponse.

        租户引擎实例信息列表

        :param premium_waf_instances: The premium_waf_instances of this CompositeHostResponse.
        :type premium_waf_instances: list[:class:`huaweicloudsdkwaf.v1.PremiumWafInstances`]
        """
        self._premium_waf_instances = premium_waf_instances

    @property
    def description(self):
        """Gets the description of this CompositeHostResponse.

        域名描述

        :return: The description of this CompositeHostResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CompositeHostResponse.

        域名描述

        :param description: The description of this CompositeHostResponse.
        :type description: str
        """
        self._description = description

    @property
    def exclusive_ip(self):
        """Gets the exclusive_ip of this CompositeHostResponse.

        是否使用独享ip   - true：使用独享ip   - false：不实用独享ip

        :return: The exclusive_ip of this CompositeHostResponse.
        :rtype: bool
        """
        return self._exclusive_ip

    @exclusive_ip.setter
    def exclusive_ip(self, exclusive_ip):
        """Sets the exclusive_ip of this CompositeHostResponse.

        是否使用独享ip   - true：使用独享ip   - false：不实用独享ip

        :param exclusive_ip: The exclusive_ip of this CompositeHostResponse.
        :type exclusive_ip: bool
        """
        self._exclusive_ip = exclusive_ip

    @property
    def region(self):
        """Gets the region of this CompositeHostResponse.

        华为云区域ID，控制台创建的域名会携带此参数，api调用创建的域名此参数为空，可以通过华为云上地区和终端节点文档查询区域ID对应的中文名称

        :return: The region of this CompositeHostResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CompositeHostResponse.

        华为云区域ID，控制台创建的域名会携带此参数，api调用创建的域名此参数为空，可以通过华为云上地区和终端节点文档查询区域ID对应的中文名称

        :param region: The region of this CompositeHostResponse.
        :type region: str
        """
        self._region = region

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
        if not isinstance(other, CompositeHostResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
