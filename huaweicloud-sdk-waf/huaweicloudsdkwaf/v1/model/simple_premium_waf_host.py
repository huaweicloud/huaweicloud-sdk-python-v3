# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimplePremiumWafHost:

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
        'extend': 'dict(str, str)',
        'region': 'str',
        'flag': 'Flag',
        'description': 'str',
        'policyid': 'str',
        'protect_status': 'int',
        'access_status': 'int',
        'web_tag': 'str',
        'hostid': 'str',
        'enterprise_project_id': 'str',
        'pool_ids': 'list[str]',
        'loadbalancer_id': 'str',
        'protocol_port': 'int'
    }

    attribute_map = {
        'id': 'id',
        'hostname': 'hostname',
        'extend': 'extend',
        'region': 'region',
        'flag': 'flag',
        'description': 'description',
        'policyid': 'policyid',
        'protect_status': 'protect_status',
        'access_status': 'access_status',
        'web_tag': 'web_tag',
        'hostid': 'hostid',
        'enterprise_project_id': 'enterprise_project_id',
        'pool_ids': 'pool_ids',
        'loadbalancer_id': 'loadbalancer_id',
        'protocol_port': 'protocol_port'
    }

    def __init__(self, id=None, hostname=None, extend=None, region=None, flag=None, description=None, policyid=None, protect_status=None, access_status=None, web_tag=None, hostid=None, enterprise_project_id=None, pool_ids=None, loadbalancer_id=None, protocol_port=None):
        r"""SimplePremiumWafHost

        The model defined in huaweicloud sdk

        :param id: 域名id
        :type id: str
        :param hostname: 域名
        :type hostname: str
        :param extend: 扩展字段，用于保存防护域名的一些配置信息。
        :type extend: dict(str, str)
        :param region: 华为云区域ID，控制台创建的域名会携带此参数，api调用创建的域名此参数为空，可以通过华为云上地区和终端节点文档查询区域ID对应的中文名称
        :type region: str
        :param flag: 
        :type flag: :class:`huaweicloudsdkwaf.v1.Flag`
        :param description: 域名描述
        :type description: str
        :param policyid: 防护域名初始绑定的防护策略ID,可以通过策略名称调用查询防护策略列表（ListPolicy）接口查询到对应的策略id
        :type policyid: str
        :param protect_status: 域名防护状态：  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测
        :type protect_status: int
        :param access_status: 域名接入状态，0表示未接入，1表示已接入
        :type access_status: int
        :param web_tag: 网站名称，对应WAF控制台域名详情中的网站名称
        :type web_tag: str
        :param hostid: 域名id，和id的值是一样的，属于冗余字段
        :type hostid: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param pool_ids: 云模式elb接入域名返回此字段，表示域名所属独享引擎组
        :type pool_ids: list[str]
        :param loadbalancer_id: 云模式elb接入域名返回此字段，表示负载均衡器（ELB）id
        :type loadbalancer_id: str
        :param protocol_port: 云模式elb接入域名返回此字段，表示业务端口
        :type protocol_port: int
        """
        
        

        self._id = None
        self._hostname = None
        self._extend = None
        self._region = None
        self._flag = None
        self._description = None
        self._policyid = None
        self._protect_status = None
        self._access_status = None
        self._web_tag = None
        self._hostid = None
        self._enterprise_project_id = None
        self._pool_ids = None
        self._loadbalancer_id = None
        self._protocol_port = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if hostname is not None:
            self.hostname = hostname
        if extend is not None:
            self.extend = extend
        if region is not None:
            self.region = region
        if flag is not None:
            self.flag = flag
        if description is not None:
            self.description = description
        if policyid is not None:
            self.policyid = policyid
        if protect_status is not None:
            self.protect_status = protect_status
        if access_status is not None:
            self.access_status = access_status
        if web_tag is not None:
            self.web_tag = web_tag
        if hostid is not None:
            self.hostid = hostid
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if pool_ids is not None:
            self.pool_ids = pool_ids
        if loadbalancer_id is not None:
            self.loadbalancer_id = loadbalancer_id
        if protocol_port is not None:
            self.protocol_port = protocol_port

    @property
    def id(self):
        r"""Gets the id of this SimplePremiumWafHost.

        域名id

        :return: The id of this SimplePremiumWafHost.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SimplePremiumWafHost.

        域名id

        :param id: The id of this SimplePremiumWafHost.
        :type id: str
        """
        self._id = id

    @property
    def hostname(self):
        r"""Gets the hostname of this SimplePremiumWafHost.

        域名

        :return: The hostname of this SimplePremiumWafHost.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        r"""Sets the hostname of this SimplePremiumWafHost.

        域名

        :param hostname: The hostname of this SimplePremiumWafHost.
        :type hostname: str
        """
        self._hostname = hostname

    @property
    def extend(self):
        r"""Gets the extend of this SimplePremiumWafHost.

        扩展字段，用于保存防护域名的一些配置信息。

        :return: The extend of this SimplePremiumWafHost.
        :rtype: dict(str, str)
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        r"""Sets the extend of this SimplePremiumWafHost.

        扩展字段，用于保存防护域名的一些配置信息。

        :param extend: The extend of this SimplePremiumWafHost.
        :type extend: dict(str, str)
        """
        self._extend = extend

    @property
    def region(self):
        r"""Gets the region of this SimplePremiumWafHost.

        华为云区域ID，控制台创建的域名会携带此参数，api调用创建的域名此参数为空，可以通过华为云上地区和终端节点文档查询区域ID对应的中文名称

        :return: The region of this SimplePremiumWafHost.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this SimplePremiumWafHost.

        华为云区域ID，控制台创建的域名会携带此参数，api调用创建的域名此参数为空，可以通过华为云上地区和终端节点文档查询区域ID对应的中文名称

        :param region: The region of this SimplePremiumWafHost.
        :type region: str
        """
        self._region = region

    @property
    def flag(self):
        r"""Gets the flag of this SimplePremiumWafHost.

        :return: The flag of this SimplePremiumWafHost.
        :rtype: :class:`huaweicloudsdkwaf.v1.Flag`
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        r"""Sets the flag of this SimplePremiumWafHost.

        :param flag: The flag of this SimplePremiumWafHost.
        :type flag: :class:`huaweicloudsdkwaf.v1.Flag`
        """
        self._flag = flag

    @property
    def description(self):
        r"""Gets the description of this SimplePremiumWafHost.

        域名描述

        :return: The description of this SimplePremiumWafHost.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SimplePremiumWafHost.

        域名描述

        :param description: The description of this SimplePremiumWafHost.
        :type description: str
        """
        self._description = description

    @property
    def policyid(self):
        r"""Gets the policyid of this SimplePremiumWafHost.

        防护域名初始绑定的防护策略ID,可以通过策略名称调用查询防护策略列表（ListPolicy）接口查询到对应的策略id

        :return: The policyid of this SimplePremiumWafHost.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        r"""Sets the policyid of this SimplePremiumWafHost.

        防护域名初始绑定的防护策略ID,可以通过策略名称调用查询防护策略列表（ListPolicy）接口查询到对应的策略id

        :param policyid: The policyid of this SimplePremiumWafHost.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def protect_status(self):
        r"""Gets the protect_status of this SimplePremiumWafHost.

        域名防护状态：  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测

        :return: The protect_status of this SimplePremiumWafHost.
        :rtype: int
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this SimplePremiumWafHost.

        域名防护状态：  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测

        :param protect_status: The protect_status of this SimplePremiumWafHost.
        :type protect_status: int
        """
        self._protect_status = protect_status

    @property
    def access_status(self):
        r"""Gets the access_status of this SimplePremiumWafHost.

        域名接入状态，0表示未接入，1表示已接入

        :return: The access_status of this SimplePremiumWafHost.
        :rtype: int
        """
        return self._access_status

    @access_status.setter
    def access_status(self, access_status):
        r"""Sets the access_status of this SimplePremiumWafHost.

        域名接入状态，0表示未接入，1表示已接入

        :param access_status: The access_status of this SimplePremiumWafHost.
        :type access_status: int
        """
        self._access_status = access_status

    @property
    def web_tag(self):
        r"""Gets the web_tag of this SimplePremiumWafHost.

        网站名称，对应WAF控制台域名详情中的网站名称

        :return: The web_tag of this SimplePremiumWafHost.
        :rtype: str
        """
        return self._web_tag

    @web_tag.setter
    def web_tag(self, web_tag):
        r"""Sets the web_tag of this SimplePremiumWafHost.

        网站名称，对应WAF控制台域名详情中的网站名称

        :param web_tag: The web_tag of this SimplePremiumWafHost.
        :type web_tag: str
        """
        self._web_tag = web_tag

    @property
    def hostid(self):
        r"""Gets the hostid of this SimplePremiumWafHost.

        域名id，和id的值是一样的，属于冗余字段

        :return: The hostid of this SimplePremiumWafHost.
        :rtype: str
        """
        return self._hostid

    @hostid.setter
    def hostid(self, hostid):
        r"""Sets the hostid of this SimplePremiumWafHost.

        域名id，和id的值是一样的，属于冗余字段

        :param hostid: The hostid of this SimplePremiumWafHost.
        :type hostid: str
        """
        self._hostid = hostid

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this SimplePremiumWafHost.

        企业项目id

        :return: The enterprise_project_id of this SimplePremiumWafHost.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this SimplePremiumWafHost.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this SimplePremiumWafHost.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def pool_ids(self):
        r"""Gets the pool_ids of this SimplePremiumWafHost.

        云模式elb接入域名返回此字段，表示域名所属独享引擎组

        :return: The pool_ids of this SimplePremiumWafHost.
        :rtype: list[str]
        """
        return self._pool_ids

    @pool_ids.setter
    def pool_ids(self, pool_ids):
        r"""Sets the pool_ids of this SimplePremiumWafHost.

        云模式elb接入域名返回此字段，表示域名所属独享引擎组

        :param pool_ids: The pool_ids of this SimplePremiumWafHost.
        :type pool_ids: list[str]
        """
        self._pool_ids = pool_ids

    @property
    def loadbalancer_id(self):
        r"""Gets the loadbalancer_id of this SimplePremiumWafHost.

        云模式elb接入域名返回此字段，表示负载均衡器（ELB）id

        :return: The loadbalancer_id of this SimplePremiumWafHost.
        :rtype: str
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        r"""Sets the loadbalancer_id of this SimplePremiumWafHost.

        云模式elb接入域名返回此字段，表示负载均衡器（ELB）id

        :param loadbalancer_id: The loadbalancer_id of this SimplePremiumWafHost.
        :type loadbalancer_id: str
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def protocol_port(self):
        r"""Gets the protocol_port of this SimplePremiumWafHost.

        云模式elb接入域名返回此字段，表示业务端口

        :return: The protocol_port of this SimplePremiumWafHost.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        r"""Sets the protocol_port of this SimplePremiumWafHost.

        云模式elb接入域名返回此字段，表示业务端口

        :param protocol_port: The protocol_port of this SimplePremiumWafHost.
        :type protocol_port: int
        """
        self._protocol_port = protocol_port

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
        if not isinstance(other, SimplePremiumWafHost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
