# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateHostRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hostname': 'str',
        'policyid': 'str',
        'server': 'list[CloudWafServer]',
        'certificateid': 'str',
        'certificatename': 'str',
        'web_tag': 'str',
        'exclusive_ip': 'bool',
        'paid_type': 'str',
        'proxy': 'bool',
        'lb_algorithm': 'str',
        'description': 'str'
    }

    attribute_map = {
        'hostname': 'hostname',
        'policyid': 'policyid',
        'server': 'server',
        'certificateid': 'certificateid',
        'certificatename': 'certificatename',
        'web_tag': 'web_tag',
        'exclusive_ip': 'exclusive_ip',
        'paid_type': 'paid_type',
        'proxy': 'proxy',
        'lb_algorithm': 'lb_algorithm',
        'description': 'description'
    }

    def __init__(self, hostname=None, policyid=None, server=None, certificateid=None, certificatename=None, web_tag=None, exclusive_ip=None, paid_type=None, proxy=None, lb_algorithm=None, description=None):
        """CreateHostRequestBody

        The model defined in huaweicloud sdk

        :param hostname: 域名（域名只能由字母、数字、-、_和.组成，长度不能超过64个字符，如www.domain.com）
        :type hostname: str
        :param policyid: 防护域名初始绑定的策略ID,可以通过策略名称调用查询防护策略列表（ListPolicy）接口查询到对应的策略id
        :type policyid: str
        :param server: 防护域名的源站服务器配置信息
        :type server: list[:class:`huaweicloudsdkwaf.v1.CloudWafServer`]
        :param certificateid: 证书id，通过查询证书列表接口（ListCertificates）接口获取证书id   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数
        :type certificateid: str
        :param certificatename: 证书名   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数
        :type certificatename: str
        :param web_tag: 网站名称，对应WAF控制台域名详情中的网站名称
        :type web_tag: str
        :param exclusive_ip: 是否使用独享ip   - true：使用独享ip   - false：不实用独享ip
        :type exclusive_ip: bool
        :param paid_type: 套餐付费模式，目前只支持prePaid预付款模式
        :type paid_type: str
        :param proxy: 防护域名是否使用代理   - false：不使用代理   - true：使用代理
        :type proxy: bool
        :param lb_algorithm: LB负载均衡，仅专业版（原企业版）和铂金版（原旗舰版）支持配置负载均衡算法   - 源IP Hash：将某个IP的请求定向到同一个服务器   - 加权轮询：所有请求将按权重轮流分配给源站服务器   - Session Hash：将某个Session标识的请求定向到同一个源站服务器，请确保在域名添加完毕后配置攻击惩罚的流量标识，否则Session Hash配置不生效
        :type lb_algorithm: str
        :param description: 域名描述
        :type description: str
        """
        
        

        self._hostname = None
        self._policyid = None
        self._server = None
        self._certificateid = None
        self._certificatename = None
        self._web_tag = None
        self._exclusive_ip = None
        self._paid_type = None
        self._proxy = None
        self._lb_algorithm = None
        self._description = None
        self.discriminator = None

        self.hostname = hostname
        if policyid is not None:
            self.policyid = policyid
        self.server = server
        if certificateid is not None:
            self.certificateid = certificateid
        if certificatename is not None:
            self.certificatename = certificatename
        if web_tag is not None:
            self.web_tag = web_tag
        if exclusive_ip is not None:
            self.exclusive_ip = exclusive_ip
        if paid_type is not None:
            self.paid_type = paid_type
        self.proxy = proxy
        if lb_algorithm is not None:
            self.lb_algorithm = lb_algorithm
        if description is not None:
            self.description = description

    @property
    def hostname(self):
        """Gets the hostname of this CreateHostRequestBody.

        域名（域名只能由字母、数字、-、_和.组成，长度不能超过64个字符，如www.domain.com）

        :return: The hostname of this CreateHostRequestBody.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this CreateHostRequestBody.

        域名（域名只能由字母、数字、-、_和.组成，长度不能超过64个字符，如www.domain.com）

        :param hostname: The hostname of this CreateHostRequestBody.
        :type hostname: str
        """
        self._hostname = hostname

    @property
    def policyid(self):
        """Gets the policyid of this CreateHostRequestBody.

        防护域名初始绑定的策略ID,可以通过策略名称调用查询防护策略列表（ListPolicy）接口查询到对应的策略id

        :return: The policyid of this CreateHostRequestBody.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this CreateHostRequestBody.

        防护域名初始绑定的策略ID,可以通过策略名称调用查询防护策略列表（ListPolicy）接口查询到对应的策略id

        :param policyid: The policyid of this CreateHostRequestBody.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def server(self):
        """Gets the server of this CreateHostRequestBody.

        防护域名的源站服务器配置信息

        :return: The server of this CreateHostRequestBody.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.CloudWafServer`]
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this CreateHostRequestBody.

        防护域名的源站服务器配置信息

        :param server: The server of this CreateHostRequestBody.
        :type server: list[:class:`huaweicloudsdkwaf.v1.CloudWafServer`]
        """
        self._server = server

    @property
    def certificateid(self):
        """Gets the certificateid of this CreateHostRequestBody.

        证书id，通过查询证书列表接口（ListCertificates）接口获取证书id   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数

        :return: The certificateid of this CreateHostRequestBody.
        :rtype: str
        """
        return self._certificateid

    @certificateid.setter
    def certificateid(self, certificateid):
        """Sets the certificateid of this CreateHostRequestBody.

        证书id，通过查询证书列表接口（ListCertificates）接口获取证书id   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数

        :param certificateid: The certificateid of this CreateHostRequestBody.
        :type certificateid: str
        """
        self._certificateid = certificateid

    @property
    def certificatename(self):
        """Gets the certificatename of this CreateHostRequestBody.

        证书名   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数

        :return: The certificatename of this CreateHostRequestBody.
        :rtype: str
        """
        return self._certificatename

    @certificatename.setter
    def certificatename(self, certificatename):
        """Sets the certificatename of this CreateHostRequestBody.

        证书名   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数

        :param certificatename: The certificatename of this CreateHostRequestBody.
        :type certificatename: str
        """
        self._certificatename = certificatename

    @property
    def web_tag(self):
        """Gets the web_tag of this CreateHostRequestBody.

        网站名称，对应WAF控制台域名详情中的网站名称

        :return: The web_tag of this CreateHostRequestBody.
        :rtype: str
        """
        return self._web_tag

    @web_tag.setter
    def web_tag(self, web_tag):
        """Sets the web_tag of this CreateHostRequestBody.

        网站名称，对应WAF控制台域名详情中的网站名称

        :param web_tag: The web_tag of this CreateHostRequestBody.
        :type web_tag: str
        """
        self._web_tag = web_tag

    @property
    def exclusive_ip(self):
        """Gets the exclusive_ip of this CreateHostRequestBody.

        是否使用独享ip   - true：使用独享ip   - false：不实用独享ip

        :return: The exclusive_ip of this CreateHostRequestBody.
        :rtype: bool
        """
        return self._exclusive_ip

    @exclusive_ip.setter
    def exclusive_ip(self, exclusive_ip):
        """Sets the exclusive_ip of this CreateHostRequestBody.

        是否使用独享ip   - true：使用独享ip   - false：不实用独享ip

        :param exclusive_ip: The exclusive_ip of this CreateHostRequestBody.
        :type exclusive_ip: bool
        """
        self._exclusive_ip = exclusive_ip

    @property
    def paid_type(self):
        """Gets the paid_type of this CreateHostRequestBody.

        套餐付费模式，目前只支持prePaid预付款模式

        :return: The paid_type of this CreateHostRequestBody.
        :rtype: str
        """
        return self._paid_type

    @paid_type.setter
    def paid_type(self, paid_type):
        """Sets the paid_type of this CreateHostRequestBody.

        套餐付费模式，目前只支持prePaid预付款模式

        :param paid_type: The paid_type of this CreateHostRequestBody.
        :type paid_type: str
        """
        self._paid_type = paid_type

    @property
    def proxy(self):
        """Gets the proxy of this CreateHostRequestBody.

        防护域名是否使用代理   - false：不使用代理   - true：使用代理

        :return: The proxy of this CreateHostRequestBody.
        :rtype: bool
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this CreateHostRequestBody.

        防护域名是否使用代理   - false：不使用代理   - true：使用代理

        :param proxy: The proxy of this CreateHostRequestBody.
        :type proxy: bool
        """
        self._proxy = proxy

    @property
    def lb_algorithm(self):
        """Gets the lb_algorithm of this CreateHostRequestBody.

        LB负载均衡，仅专业版（原企业版）和铂金版（原旗舰版）支持配置负载均衡算法   - 源IP Hash：将某个IP的请求定向到同一个服务器   - 加权轮询：所有请求将按权重轮流分配给源站服务器   - Session Hash：将某个Session标识的请求定向到同一个源站服务器，请确保在域名添加完毕后配置攻击惩罚的流量标识，否则Session Hash配置不生效

        :return: The lb_algorithm of this CreateHostRequestBody.
        :rtype: str
        """
        return self._lb_algorithm

    @lb_algorithm.setter
    def lb_algorithm(self, lb_algorithm):
        """Sets the lb_algorithm of this CreateHostRequestBody.

        LB负载均衡，仅专业版（原企业版）和铂金版（原旗舰版）支持配置负载均衡算法   - 源IP Hash：将某个IP的请求定向到同一个服务器   - 加权轮询：所有请求将按权重轮流分配给源站服务器   - Session Hash：将某个Session标识的请求定向到同一个源站服务器，请确保在域名添加完毕后配置攻击惩罚的流量标识，否则Session Hash配置不生效

        :param lb_algorithm: The lb_algorithm of this CreateHostRequestBody.
        :type lb_algorithm: str
        """
        self._lb_algorithm = lb_algorithm

    @property
    def description(self):
        """Gets the description of this CreateHostRequestBody.

        域名描述

        :return: The description of this CreateHostRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateHostRequestBody.

        域名描述

        :param description: The description of this CreateHostRequestBody.
        :type description: str
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
        if not isinstance(other, CreateHostRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
