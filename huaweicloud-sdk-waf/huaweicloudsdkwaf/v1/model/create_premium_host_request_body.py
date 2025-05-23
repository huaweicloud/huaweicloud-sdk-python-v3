# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePremiumHostRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'certificateid': 'str',
        'certificatename': 'str',
        'hostname': 'str',
        'proxy': 'bool',
        'policyid': 'str',
        'server': 'list[PremiumWafServer]',
        'block_page': 'BlockPage',
        'forward_header_map': 'dict(str, str)',
        'mode': 'str',
        'loadbalancer_id': 'str',
        'listener_id': 'str',
        'protocol_port': 'int',
        'description': 'str',
        'web_tag': 'str'
    }

    attribute_map = {
        'certificateid': 'certificateid',
        'certificatename': 'certificatename',
        'hostname': 'hostname',
        'proxy': 'proxy',
        'policyid': 'policyid',
        'server': 'server',
        'block_page': 'block_page',
        'forward_header_map': 'forward_header_map',
        'mode': 'mode',
        'loadbalancer_id': 'loadbalancer_id',
        'listener_id': 'listener_id',
        'protocol_port': 'protocol_port',
        'description': 'description',
        'web_tag': 'web_tag'
    }

    def __init__(self, certificateid=None, certificatename=None, hostname=None, proxy=None, policyid=None, server=None, block_page=None, forward_header_map=None, mode=None, loadbalancer_id=None, listener_id=None, protocol_port=None, description=None, web_tag=None):
        r"""CreatePremiumHostRequestBody

        The model defined in huaweicloud sdk

        :param certificateid: 证书id，通过查询证书列表接口（ListCertificates）接口获取证书id   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数
        :type certificateid: str
        :param certificatename: 证书名   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数
        :type certificatename: str
        :param hostname: 防护域名或IP（可带端口）
        :type hostname: str
        :param proxy: 防护域名是否使用代理   - false：不使用代理   - true：使用代理
        :type proxy: bool
        :param policyid: 防护域名初始绑定的防护策略ID,可以通过策略名称调用查询防护策略列表（ListPolicy）接口查询到对应的策略id
        :type policyid: str
        :param server: 防护域名的源站服务器配置信息
        :type server: list[:class:`huaweicloudsdkwaf.v1.PremiumWafServer`]
        :param block_page: 
        :type block_page: :class:`huaweicloudsdkwaf.v1.BlockPage`
        :param forward_header_map: 字段转发配置，WAF会将添加的字段插到header中，转给源站；Key不能跟nginx原生字段重复。Value支持的值包括:   - $time_local   - $request_id   - $connection_requests   - $tenant_id   - $project_id   - $remote_addr   - $remote_port   - $scheme   - $request_method   - $http_host   -$origin_uri   - $request_length   - $ssl_server_name   - $ssl_protocol   - $ssl_curves   - $ssl_session_reused
        :type forward_header_map: dict(str, str)
        :param mode: 添加云模式elb接入域名时，请输入elb-shared，否则不输入
        :type mode: str
        :param loadbalancer_id: 负载均衡器（ELB）id,可以在ELB侧查询其id，添加云模式elb接入域名时，此为必须输入的值
        :type loadbalancer_id: str
        :param listener_id: 监听器id，可在ELB侧监听器页签下查询其id；不输入时，负载均衡器（ELB）下的所有监听器都将接入WAF防护，包括该ELB下未来新增的符合条件的监听器，添加云模式elb接入域名时，可考虑输入此项id
        :type listener_id: str
        :param protocol_port: 业务端口，添加云模式elb接入域名时，此为必须输入的值（0 - 65535）
        :type protocol_port: int
        :param description: 防护域名备注
        :type description: str
        :param web_tag: 网站名称，对应WAF控制台域名详情中的网站名称
        :type web_tag: str
        """
        
        

        self._certificateid = None
        self._certificatename = None
        self._hostname = None
        self._proxy = None
        self._policyid = None
        self._server = None
        self._block_page = None
        self._forward_header_map = None
        self._mode = None
        self._loadbalancer_id = None
        self._listener_id = None
        self._protocol_port = None
        self._description = None
        self._web_tag = None
        self.discriminator = None

        if certificateid is not None:
            self.certificateid = certificateid
        if certificatename is not None:
            self.certificatename = certificatename
        self.hostname = hostname
        self.proxy = proxy
        if policyid is not None:
            self.policyid = policyid
        self.server = server
        if block_page is not None:
            self.block_page = block_page
        if forward_header_map is not None:
            self.forward_header_map = forward_header_map
        if mode is not None:
            self.mode = mode
        if loadbalancer_id is not None:
            self.loadbalancer_id = loadbalancer_id
        if listener_id is not None:
            self.listener_id = listener_id
        if protocol_port is not None:
            self.protocol_port = protocol_port
        if description is not None:
            self.description = description
        if web_tag is not None:
            self.web_tag = web_tag

    @property
    def certificateid(self):
        r"""Gets the certificateid of this CreatePremiumHostRequestBody.

        证书id，通过查询证书列表接口（ListCertificates）接口获取证书id   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数

        :return: The certificateid of this CreatePremiumHostRequestBody.
        :rtype: str
        """
        return self._certificateid

    @certificateid.setter
    def certificateid(self, certificateid):
        r"""Sets the certificateid of this CreatePremiumHostRequestBody.

        证书id，通过查询证书列表接口（ListCertificates）接口获取证书id   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数

        :param certificateid: The certificateid of this CreatePremiumHostRequestBody.
        :type certificateid: str
        """
        self._certificateid = certificateid

    @property
    def certificatename(self):
        r"""Gets the certificatename of this CreatePremiumHostRequestBody.

        证书名   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数

        :return: The certificatename of this CreatePremiumHostRequestBody.
        :rtype: str
        """
        return self._certificatename

    @certificatename.setter
    def certificatename(self, certificatename):
        r"""Sets the certificatename of this CreatePremiumHostRequestBody.

        证书名   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数

        :param certificatename: The certificatename of this CreatePremiumHostRequestBody.
        :type certificatename: str
        """
        self._certificatename = certificatename

    @property
    def hostname(self):
        r"""Gets the hostname of this CreatePremiumHostRequestBody.

        防护域名或IP（可带端口）

        :return: The hostname of this CreatePremiumHostRequestBody.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        r"""Sets the hostname of this CreatePremiumHostRequestBody.

        防护域名或IP（可带端口）

        :param hostname: The hostname of this CreatePremiumHostRequestBody.
        :type hostname: str
        """
        self._hostname = hostname

    @property
    def proxy(self):
        r"""Gets the proxy of this CreatePremiumHostRequestBody.

        防护域名是否使用代理   - false：不使用代理   - true：使用代理

        :return: The proxy of this CreatePremiumHostRequestBody.
        :rtype: bool
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        r"""Sets the proxy of this CreatePremiumHostRequestBody.

        防护域名是否使用代理   - false：不使用代理   - true：使用代理

        :param proxy: The proxy of this CreatePremiumHostRequestBody.
        :type proxy: bool
        """
        self._proxy = proxy

    @property
    def policyid(self):
        r"""Gets the policyid of this CreatePremiumHostRequestBody.

        防护域名初始绑定的防护策略ID,可以通过策略名称调用查询防护策略列表（ListPolicy）接口查询到对应的策略id

        :return: The policyid of this CreatePremiumHostRequestBody.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        r"""Sets the policyid of this CreatePremiumHostRequestBody.

        防护域名初始绑定的防护策略ID,可以通过策略名称调用查询防护策略列表（ListPolicy）接口查询到对应的策略id

        :param policyid: The policyid of this CreatePremiumHostRequestBody.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def server(self):
        r"""Gets the server of this CreatePremiumHostRequestBody.

        防护域名的源站服务器配置信息

        :return: The server of this CreatePremiumHostRequestBody.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.PremiumWafServer`]
        """
        return self._server

    @server.setter
    def server(self, server):
        r"""Sets the server of this CreatePremiumHostRequestBody.

        防护域名的源站服务器配置信息

        :param server: The server of this CreatePremiumHostRequestBody.
        :type server: list[:class:`huaweicloudsdkwaf.v1.PremiumWafServer`]
        """
        self._server = server

    @property
    def block_page(self):
        r"""Gets the block_page of this CreatePremiumHostRequestBody.

        :return: The block_page of this CreatePremiumHostRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.BlockPage`
        """
        return self._block_page

    @block_page.setter
    def block_page(self, block_page):
        r"""Sets the block_page of this CreatePremiumHostRequestBody.

        :param block_page: The block_page of this CreatePremiumHostRequestBody.
        :type block_page: :class:`huaweicloudsdkwaf.v1.BlockPage`
        """
        self._block_page = block_page

    @property
    def forward_header_map(self):
        r"""Gets the forward_header_map of this CreatePremiumHostRequestBody.

        字段转发配置，WAF会将添加的字段插到header中，转给源站；Key不能跟nginx原生字段重复。Value支持的值包括:   - $time_local   - $request_id   - $connection_requests   - $tenant_id   - $project_id   - $remote_addr   - $remote_port   - $scheme   - $request_method   - $http_host   -$origin_uri   - $request_length   - $ssl_server_name   - $ssl_protocol   - $ssl_curves   - $ssl_session_reused

        :return: The forward_header_map of this CreatePremiumHostRequestBody.
        :rtype: dict(str, str)
        """
        return self._forward_header_map

    @forward_header_map.setter
    def forward_header_map(self, forward_header_map):
        r"""Sets the forward_header_map of this CreatePremiumHostRequestBody.

        字段转发配置，WAF会将添加的字段插到header中，转给源站；Key不能跟nginx原生字段重复。Value支持的值包括:   - $time_local   - $request_id   - $connection_requests   - $tenant_id   - $project_id   - $remote_addr   - $remote_port   - $scheme   - $request_method   - $http_host   -$origin_uri   - $request_length   - $ssl_server_name   - $ssl_protocol   - $ssl_curves   - $ssl_session_reused

        :param forward_header_map: The forward_header_map of this CreatePremiumHostRequestBody.
        :type forward_header_map: dict(str, str)
        """
        self._forward_header_map = forward_header_map

    @property
    def mode(self):
        r"""Gets the mode of this CreatePremiumHostRequestBody.

        添加云模式elb接入域名时，请输入elb-shared，否则不输入

        :return: The mode of this CreatePremiumHostRequestBody.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this CreatePremiumHostRequestBody.

        添加云模式elb接入域名时，请输入elb-shared，否则不输入

        :param mode: The mode of this CreatePremiumHostRequestBody.
        :type mode: str
        """
        self._mode = mode

    @property
    def loadbalancer_id(self):
        r"""Gets the loadbalancer_id of this CreatePremiumHostRequestBody.

        负载均衡器（ELB）id,可以在ELB侧查询其id，添加云模式elb接入域名时，此为必须输入的值

        :return: The loadbalancer_id of this CreatePremiumHostRequestBody.
        :rtype: str
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        r"""Sets the loadbalancer_id of this CreatePremiumHostRequestBody.

        负载均衡器（ELB）id,可以在ELB侧查询其id，添加云模式elb接入域名时，此为必须输入的值

        :param loadbalancer_id: The loadbalancer_id of this CreatePremiumHostRequestBody.
        :type loadbalancer_id: str
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def listener_id(self):
        r"""Gets the listener_id of this CreatePremiumHostRequestBody.

        监听器id，可在ELB侧监听器页签下查询其id；不输入时，负载均衡器（ELB）下的所有监听器都将接入WAF防护，包括该ELB下未来新增的符合条件的监听器，添加云模式elb接入域名时，可考虑输入此项id

        :return: The listener_id of this CreatePremiumHostRequestBody.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        r"""Sets the listener_id of this CreatePremiumHostRequestBody.

        监听器id，可在ELB侧监听器页签下查询其id；不输入时，负载均衡器（ELB）下的所有监听器都将接入WAF防护，包括该ELB下未来新增的符合条件的监听器，添加云模式elb接入域名时，可考虑输入此项id

        :param listener_id: The listener_id of this CreatePremiumHostRequestBody.
        :type listener_id: str
        """
        self._listener_id = listener_id

    @property
    def protocol_port(self):
        r"""Gets the protocol_port of this CreatePremiumHostRequestBody.

        业务端口，添加云模式elb接入域名时，此为必须输入的值（0 - 65535）

        :return: The protocol_port of this CreatePremiumHostRequestBody.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        r"""Sets the protocol_port of this CreatePremiumHostRequestBody.

        业务端口，添加云模式elb接入域名时，此为必须输入的值（0 - 65535）

        :param protocol_port: The protocol_port of this CreatePremiumHostRequestBody.
        :type protocol_port: int
        """
        self._protocol_port = protocol_port

    @property
    def description(self):
        r"""Gets the description of this CreatePremiumHostRequestBody.

        防护域名备注

        :return: The description of this CreatePremiumHostRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreatePremiumHostRequestBody.

        防护域名备注

        :param description: The description of this CreatePremiumHostRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def web_tag(self):
        r"""Gets the web_tag of this CreatePremiumHostRequestBody.

        网站名称，对应WAF控制台域名详情中的网站名称

        :return: The web_tag of this CreatePremiumHostRequestBody.
        :rtype: str
        """
        return self._web_tag

    @web_tag.setter
    def web_tag(self, web_tag):
        r"""Sets the web_tag of this CreatePremiumHostRequestBody.

        网站名称，对应WAF控制台域名详情中的网站名称

        :param web_tag: The web_tag of this CreatePremiumHostRequestBody.
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
        if not isinstance(other, CreatePremiumHostRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
