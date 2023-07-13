# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConsoleConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eps': 'bool',
        'tls': 'bool',
        'ipv6': 'bool',
        'alert': 'bool',
        'custom': 'bool',
        'elb_mode': 'bool',
        'event_lts': 'bool',
        'multi_dns': 'bool',
        'search_ip': 'bool',
        'cc_enhance': 'bool',
        'cname_switch': 'bool',
        'custom_block': 'bool',
        'advanced_ignore': 'bool',
        'js_crawler_enable': 'bool',
        'deep_decode_enable': 'bool',
        'overview_bandwidth': 'bool',
        'proxy_use_oldcname': 'bool',
        'check_all_headers_enable': 'bool',
        'geoip_enable': 'bool',
        'load_balance_enable': 'bool',
        'ipv6_protection_enable': 'bool',
        'policy_sharing_enable': 'bool',
        'ip_group': 'bool',
        'robot_action_enable': 'bool',
        'http2_enable': 'bool',
        'timeout_config_enable': 'bool'
    }

    attribute_map = {
        'eps': 'eps',
        'tls': 'tls',
        'ipv6': 'ipv6',
        'alert': 'alert',
        'custom': 'custom',
        'elb_mode': 'elb_mode',
        'event_lts': 'event_lts',
        'multi_dns': 'multi_dns',
        'search_ip': 'search_ip',
        'cc_enhance': 'cc_enhance',
        'cname_switch': 'cname_switch',
        'custom_block': 'custom_block',
        'advanced_ignore': 'advanced_ignore',
        'js_crawler_enable': 'js_crawler_enable',
        'deep_decode_enable': 'deep_decode_enable',
        'overview_bandwidth': 'overview_bandwidth',
        'proxy_use_oldcname': 'proxy_use_oldcname',
        'check_all_headers_enable': 'check_all_headers_enable',
        'geoip_enable': 'geoip_enable',
        'load_balance_enable': 'load_balance_enable',
        'ipv6_protection_enable': 'ipv6_protection_enable',
        'policy_sharing_enable': 'policy_sharing_enable',
        'ip_group': 'ip_group',
        'robot_action_enable': 'robot_action_enable',
        'http2_enable': 'http2_enable',
        'timeout_config_enable': 'timeout_config_enable'
    }

    def __init__(self, eps=None, tls=None, ipv6=None, alert=None, custom=None, elb_mode=None, event_lts=None, multi_dns=None, search_ip=None, cc_enhance=None, cname_switch=None, custom_block=None, advanced_ignore=None, js_crawler_enable=None, deep_decode_enable=None, overview_bandwidth=None, proxy_use_oldcname=None, check_all_headers_enable=None, geoip_enable=None, load_balance_enable=None, ipv6_protection_enable=None, policy_sharing_enable=None, ip_group=None, robot_action_enable=None, http2_enable=None, timeout_config_enable=None):
        """ShowConsoleConfigResponse

        The model defined in huaweicloud sdk

        :param eps: 是否支持EPS，false：不支持；true：支持
        :type eps: bool
        :param tls: 是否支持的TLS版本（TLS v1.0/TLS v1.1/TLS v1.2）,默认为TLS v1.0版本，false：不支持；true：支持
        :type tls: bool
        :param ipv6: 是否支持IPV6，false：不支持；true：支持
        :type ipv6: bool
        :param alert: 是否支持告警，false：不支持；true：支持
        :type alert: bool
        :param custom: 是否支持精准防护，false：不支持；true：支持
        :type custom: bool
        :param elb_mode: 是否支持ELB模式，false：不支持；true：支持
        :type elb_mode: bool
        :param event_lts: 是否支持LTS全量日志，false：不支持；true：支持
        :type event_lts: bool
        :param multi_dns: 是否支持多DNS解析，false：不支持；true：支持
        :type multi_dns: bool
        :param search_ip: 是否支持搜索IP，false：不支持；true：支持
        :type search_ip: bool
        :param cc_enhance: 是否支持CC增强，false：不支持；true：支持
        :type cc_enhance: bool
        :param cname_switch: 是否支持cname切换，false：不支持；true：支持
        :type cname_switch: bool
        :param custom_block: 是否支持自定义拦截页面，false：不支持，true：支持
        :type custom_block: bool
        :param advanced_ignore: 是否支持误报屏蔽，false：不支持；true：支持
        :type advanced_ignore: bool
        :param js_crawler_enable: 是否支持js反爬虫，false：不支持；true：支持
        :type js_crawler_enable: bool
        :param deep_decode_enable: 是否支持web基础防护深度检测，false：不支持；true：支持
        :type deep_decode_enable: bool
        :param overview_bandwidth: 是否支持安全总览带宽统计，false：不支持；true：支持
        :type overview_bandwidth: bool
        :param proxy_use_oldcname: 是否支持使用旧cname解析，false：不支持；true：支持
        :type proxy_use_oldcname: bool
        :param check_all_headers_enable: 是否支持检查所有的header，false：不支持；true：支持
        :type check_all_headers_enable: bool
        :param geoip_enable: 是否支持地理位置访问控制，false：不支持；true：支持
        :type geoip_enable: bool
        :param load_balance_enable: 是否支持域名访问负载均衡配置，false：不支持；true：支持
        :type load_balance_enable: bool
        :param ipv6_protection_enable: 是否支持ipv6防护，false：不支持；true：支持
        :type ipv6_protection_enable: bool
        :param policy_sharing_enable: 是否支持策略共享，false：不支持；true：支持
        :type policy_sharing_enable: bool
        :param ip_group: 是否支持ip地址组，false：不支持；true：支持
        :type ip_group: bool
        :param robot_action_enable: 是否支持网站反爬虫，false：不支持；true：支持
        :type robot_action_enable: bool
        :param http2_enable: 是否支持http2，false：不支持；true：支持
        :type http2_enable: bool
        :param timeout_config_enable: 是否支持超时配置，false：不支持；true：支持
        :type timeout_config_enable: bool
        """
        
        super(ShowConsoleConfigResponse, self).__init__()

        self._eps = None
        self._tls = None
        self._ipv6 = None
        self._alert = None
        self._custom = None
        self._elb_mode = None
        self._event_lts = None
        self._multi_dns = None
        self._search_ip = None
        self._cc_enhance = None
        self._cname_switch = None
        self._custom_block = None
        self._advanced_ignore = None
        self._js_crawler_enable = None
        self._deep_decode_enable = None
        self._overview_bandwidth = None
        self._proxy_use_oldcname = None
        self._check_all_headers_enable = None
        self._geoip_enable = None
        self._load_balance_enable = None
        self._ipv6_protection_enable = None
        self._policy_sharing_enable = None
        self._ip_group = None
        self._robot_action_enable = None
        self._http2_enable = None
        self._timeout_config_enable = None
        self.discriminator = None

        if eps is not None:
            self.eps = eps
        if tls is not None:
            self.tls = tls
        if ipv6 is not None:
            self.ipv6 = ipv6
        if alert is not None:
            self.alert = alert
        if custom is not None:
            self.custom = custom
        if elb_mode is not None:
            self.elb_mode = elb_mode
        if event_lts is not None:
            self.event_lts = event_lts
        if multi_dns is not None:
            self.multi_dns = multi_dns
        if search_ip is not None:
            self.search_ip = search_ip
        if cc_enhance is not None:
            self.cc_enhance = cc_enhance
        if cname_switch is not None:
            self.cname_switch = cname_switch
        if custom_block is not None:
            self.custom_block = custom_block
        if advanced_ignore is not None:
            self.advanced_ignore = advanced_ignore
        if js_crawler_enable is not None:
            self.js_crawler_enable = js_crawler_enable
        if deep_decode_enable is not None:
            self.deep_decode_enable = deep_decode_enable
        if overview_bandwidth is not None:
            self.overview_bandwidth = overview_bandwidth
        if proxy_use_oldcname is not None:
            self.proxy_use_oldcname = proxy_use_oldcname
        if check_all_headers_enable is not None:
            self.check_all_headers_enable = check_all_headers_enable
        if geoip_enable is not None:
            self.geoip_enable = geoip_enable
        if load_balance_enable is not None:
            self.load_balance_enable = load_balance_enable
        if ipv6_protection_enable is not None:
            self.ipv6_protection_enable = ipv6_protection_enable
        if policy_sharing_enable is not None:
            self.policy_sharing_enable = policy_sharing_enable
        if ip_group is not None:
            self.ip_group = ip_group
        if robot_action_enable is not None:
            self.robot_action_enable = robot_action_enable
        if http2_enable is not None:
            self.http2_enable = http2_enable
        if timeout_config_enable is not None:
            self.timeout_config_enable = timeout_config_enable

    @property
    def eps(self):
        """Gets the eps of this ShowConsoleConfigResponse.

        是否支持EPS，false：不支持；true：支持

        :return: The eps of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._eps

    @eps.setter
    def eps(self, eps):
        """Sets the eps of this ShowConsoleConfigResponse.

        是否支持EPS，false：不支持；true：支持

        :param eps: The eps of this ShowConsoleConfigResponse.
        :type eps: bool
        """
        self._eps = eps

    @property
    def tls(self):
        """Gets the tls of this ShowConsoleConfigResponse.

        是否支持的TLS版本（TLS v1.0/TLS v1.1/TLS v1.2）,默认为TLS v1.0版本，false：不支持；true：支持

        :return: The tls of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """Sets the tls of this ShowConsoleConfigResponse.

        是否支持的TLS版本（TLS v1.0/TLS v1.1/TLS v1.2）,默认为TLS v1.0版本，false：不支持；true：支持

        :param tls: The tls of this ShowConsoleConfigResponse.
        :type tls: bool
        """
        self._tls = tls

    @property
    def ipv6(self):
        """Gets the ipv6 of this ShowConsoleConfigResponse.

        是否支持IPV6，false：不支持；true：支持

        :return: The ipv6 of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._ipv6

    @ipv6.setter
    def ipv6(self, ipv6):
        """Sets the ipv6 of this ShowConsoleConfigResponse.

        是否支持IPV6，false：不支持；true：支持

        :param ipv6: The ipv6 of this ShowConsoleConfigResponse.
        :type ipv6: bool
        """
        self._ipv6 = ipv6

    @property
    def alert(self):
        """Gets the alert of this ShowConsoleConfigResponse.

        是否支持告警，false：不支持；true：支持

        :return: The alert of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._alert

    @alert.setter
    def alert(self, alert):
        """Sets the alert of this ShowConsoleConfigResponse.

        是否支持告警，false：不支持；true：支持

        :param alert: The alert of this ShowConsoleConfigResponse.
        :type alert: bool
        """
        self._alert = alert

    @property
    def custom(self):
        """Gets the custom of this ShowConsoleConfigResponse.

        是否支持精准防护，false：不支持；true：支持

        :return: The custom of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """Sets the custom of this ShowConsoleConfigResponse.

        是否支持精准防护，false：不支持；true：支持

        :param custom: The custom of this ShowConsoleConfigResponse.
        :type custom: bool
        """
        self._custom = custom

    @property
    def elb_mode(self):
        """Gets the elb_mode of this ShowConsoleConfigResponse.

        是否支持ELB模式，false：不支持；true：支持

        :return: The elb_mode of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._elb_mode

    @elb_mode.setter
    def elb_mode(self, elb_mode):
        """Sets the elb_mode of this ShowConsoleConfigResponse.

        是否支持ELB模式，false：不支持；true：支持

        :param elb_mode: The elb_mode of this ShowConsoleConfigResponse.
        :type elb_mode: bool
        """
        self._elb_mode = elb_mode

    @property
    def event_lts(self):
        """Gets the event_lts of this ShowConsoleConfigResponse.

        是否支持LTS全量日志，false：不支持；true：支持

        :return: The event_lts of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._event_lts

    @event_lts.setter
    def event_lts(self, event_lts):
        """Sets the event_lts of this ShowConsoleConfigResponse.

        是否支持LTS全量日志，false：不支持；true：支持

        :param event_lts: The event_lts of this ShowConsoleConfigResponse.
        :type event_lts: bool
        """
        self._event_lts = event_lts

    @property
    def multi_dns(self):
        """Gets the multi_dns of this ShowConsoleConfigResponse.

        是否支持多DNS解析，false：不支持；true：支持

        :return: The multi_dns of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._multi_dns

    @multi_dns.setter
    def multi_dns(self, multi_dns):
        """Sets the multi_dns of this ShowConsoleConfigResponse.

        是否支持多DNS解析，false：不支持；true：支持

        :param multi_dns: The multi_dns of this ShowConsoleConfigResponse.
        :type multi_dns: bool
        """
        self._multi_dns = multi_dns

    @property
    def search_ip(self):
        """Gets the search_ip of this ShowConsoleConfigResponse.

        是否支持搜索IP，false：不支持；true：支持

        :return: The search_ip of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._search_ip

    @search_ip.setter
    def search_ip(self, search_ip):
        """Sets the search_ip of this ShowConsoleConfigResponse.

        是否支持搜索IP，false：不支持；true：支持

        :param search_ip: The search_ip of this ShowConsoleConfigResponse.
        :type search_ip: bool
        """
        self._search_ip = search_ip

    @property
    def cc_enhance(self):
        """Gets the cc_enhance of this ShowConsoleConfigResponse.

        是否支持CC增强，false：不支持；true：支持

        :return: The cc_enhance of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._cc_enhance

    @cc_enhance.setter
    def cc_enhance(self, cc_enhance):
        """Sets the cc_enhance of this ShowConsoleConfigResponse.

        是否支持CC增强，false：不支持；true：支持

        :param cc_enhance: The cc_enhance of this ShowConsoleConfigResponse.
        :type cc_enhance: bool
        """
        self._cc_enhance = cc_enhance

    @property
    def cname_switch(self):
        """Gets the cname_switch of this ShowConsoleConfigResponse.

        是否支持cname切换，false：不支持；true：支持

        :return: The cname_switch of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._cname_switch

    @cname_switch.setter
    def cname_switch(self, cname_switch):
        """Sets the cname_switch of this ShowConsoleConfigResponse.

        是否支持cname切换，false：不支持；true：支持

        :param cname_switch: The cname_switch of this ShowConsoleConfigResponse.
        :type cname_switch: bool
        """
        self._cname_switch = cname_switch

    @property
    def custom_block(self):
        """Gets the custom_block of this ShowConsoleConfigResponse.

        是否支持自定义拦截页面，false：不支持，true：支持

        :return: The custom_block of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._custom_block

    @custom_block.setter
    def custom_block(self, custom_block):
        """Sets the custom_block of this ShowConsoleConfigResponse.

        是否支持自定义拦截页面，false：不支持，true：支持

        :param custom_block: The custom_block of this ShowConsoleConfigResponse.
        :type custom_block: bool
        """
        self._custom_block = custom_block

    @property
    def advanced_ignore(self):
        """Gets the advanced_ignore of this ShowConsoleConfigResponse.

        是否支持误报屏蔽，false：不支持；true：支持

        :return: The advanced_ignore of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._advanced_ignore

    @advanced_ignore.setter
    def advanced_ignore(self, advanced_ignore):
        """Sets the advanced_ignore of this ShowConsoleConfigResponse.

        是否支持误报屏蔽，false：不支持；true：支持

        :param advanced_ignore: The advanced_ignore of this ShowConsoleConfigResponse.
        :type advanced_ignore: bool
        """
        self._advanced_ignore = advanced_ignore

    @property
    def js_crawler_enable(self):
        """Gets the js_crawler_enable of this ShowConsoleConfigResponse.

        是否支持js反爬虫，false：不支持；true：支持

        :return: The js_crawler_enable of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._js_crawler_enable

    @js_crawler_enable.setter
    def js_crawler_enable(self, js_crawler_enable):
        """Sets the js_crawler_enable of this ShowConsoleConfigResponse.

        是否支持js反爬虫，false：不支持；true：支持

        :param js_crawler_enable: The js_crawler_enable of this ShowConsoleConfigResponse.
        :type js_crawler_enable: bool
        """
        self._js_crawler_enable = js_crawler_enable

    @property
    def deep_decode_enable(self):
        """Gets the deep_decode_enable of this ShowConsoleConfigResponse.

        是否支持web基础防护深度检测，false：不支持；true：支持

        :return: The deep_decode_enable of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._deep_decode_enable

    @deep_decode_enable.setter
    def deep_decode_enable(self, deep_decode_enable):
        """Sets the deep_decode_enable of this ShowConsoleConfigResponse.

        是否支持web基础防护深度检测，false：不支持；true：支持

        :param deep_decode_enable: The deep_decode_enable of this ShowConsoleConfigResponse.
        :type deep_decode_enable: bool
        """
        self._deep_decode_enable = deep_decode_enable

    @property
    def overview_bandwidth(self):
        """Gets the overview_bandwidth of this ShowConsoleConfigResponse.

        是否支持安全总览带宽统计，false：不支持；true：支持

        :return: The overview_bandwidth of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._overview_bandwidth

    @overview_bandwidth.setter
    def overview_bandwidth(self, overview_bandwidth):
        """Sets the overview_bandwidth of this ShowConsoleConfigResponse.

        是否支持安全总览带宽统计，false：不支持；true：支持

        :param overview_bandwidth: The overview_bandwidth of this ShowConsoleConfigResponse.
        :type overview_bandwidth: bool
        """
        self._overview_bandwidth = overview_bandwidth

    @property
    def proxy_use_oldcname(self):
        """Gets the proxy_use_oldcname of this ShowConsoleConfigResponse.

        是否支持使用旧cname解析，false：不支持；true：支持

        :return: The proxy_use_oldcname of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._proxy_use_oldcname

    @proxy_use_oldcname.setter
    def proxy_use_oldcname(self, proxy_use_oldcname):
        """Sets the proxy_use_oldcname of this ShowConsoleConfigResponse.

        是否支持使用旧cname解析，false：不支持；true：支持

        :param proxy_use_oldcname: The proxy_use_oldcname of this ShowConsoleConfigResponse.
        :type proxy_use_oldcname: bool
        """
        self._proxy_use_oldcname = proxy_use_oldcname

    @property
    def check_all_headers_enable(self):
        """Gets the check_all_headers_enable of this ShowConsoleConfigResponse.

        是否支持检查所有的header，false：不支持；true：支持

        :return: The check_all_headers_enable of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._check_all_headers_enable

    @check_all_headers_enable.setter
    def check_all_headers_enable(self, check_all_headers_enable):
        """Sets the check_all_headers_enable of this ShowConsoleConfigResponse.

        是否支持检查所有的header，false：不支持；true：支持

        :param check_all_headers_enable: The check_all_headers_enable of this ShowConsoleConfigResponse.
        :type check_all_headers_enable: bool
        """
        self._check_all_headers_enable = check_all_headers_enable

    @property
    def geoip_enable(self):
        """Gets the geoip_enable of this ShowConsoleConfigResponse.

        是否支持地理位置访问控制，false：不支持；true：支持

        :return: The geoip_enable of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._geoip_enable

    @geoip_enable.setter
    def geoip_enable(self, geoip_enable):
        """Sets the geoip_enable of this ShowConsoleConfigResponse.

        是否支持地理位置访问控制，false：不支持；true：支持

        :param geoip_enable: The geoip_enable of this ShowConsoleConfigResponse.
        :type geoip_enable: bool
        """
        self._geoip_enable = geoip_enable

    @property
    def load_balance_enable(self):
        """Gets the load_balance_enable of this ShowConsoleConfigResponse.

        是否支持域名访问负载均衡配置，false：不支持；true：支持

        :return: The load_balance_enable of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._load_balance_enable

    @load_balance_enable.setter
    def load_balance_enable(self, load_balance_enable):
        """Sets the load_balance_enable of this ShowConsoleConfigResponse.

        是否支持域名访问负载均衡配置，false：不支持；true：支持

        :param load_balance_enable: The load_balance_enable of this ShowConsoleConfigResponse.
        :type load_balance_enable: bool
        """
        self._load_balance_enable = load_balance_enable

    @property
    def ipv6_protection_enable(self):
        """Gets the ipv6_protection_enable of this ShowConsoleConfigResponse.

        是否支持ipv6防护，false：不支持；true：支持

        :return: The ipv6_protection_enable of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._ipv6_protection_enable

    @ipv6_protection_enable.setter
    def ipv6_protection_enable(self, ipv6_protection_enable):
        """Sets the ipv6_protection_enable of this ShowConsoleConfigResponse.

        是否支持ipv6防护，false：不支持；true：支持

        :param ipv6_protection_enable: The ipv6_protection_enable of this ShowConsoleConfigResponse.
        :type ipv6_protection_enable: bool
        """
        self._ipv6_protection_enable = ipv6_protection_enable

    @property
    def policy_sharing_enable(self):
        """Gets the policy_sharing_enable of this ShowConsoleConfigResponse.

        是否支持策略共享，false：不支持；true：支持

        :return: The policy_sharing_enable of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._policy_sharing_enable

    @policy_sharing_enable.setter
    def policy_sharing_enable(self, policy_sharing_enable):
        """Sets the policy_sharing_enable of this ShowConsoleConfigResponse.

        是否支持策略共享，false：不支持；true：支持

        :param policy_sharing_enable: The policy_sharing_enable of this ShowConsoleConfigResponse.
        :type policy_sharing_enable: bool
        """
        self._policy_sharing_enable = policy_sharing_enable

    @property
    def ip_group(self):
        """Gets the ip_group of this ShowConsoleConfigResponse.

        是否支持ip地址组，false：不支持；true：支持

        :return: The ip_group of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._ip_group

    @ip_group.setter
    def ip_group(self, ip_group):
        """Sets the ip_group of this ShowConsoleConfigResponse.

        是否支持ip地址组，false：不支持；true：支持

        :param ip_group: The ip_group of this ShowConsoleConfigResponse.
        :type ip_group: bool
        """
        self._ip_group = ip_group

    @property
    def robot_action_enable(self):
        """Gets the robot_action_enable of this ShowConsoleConfigResponse.

        是否支持网站反爬虫，false：不支持；true：支持

        :return: The robot_action_enable of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._robot_action_enable

    @robot_action_enable.setter
    def robot_action_enable(self, robot_action_enable):
        """Sets the robot_action_enable of this ShowConsoleConfigResponse.

        是否支持网站反爬虫，false：不支持；true：支持

        :param robot_action_enable: The robot_action_enable of this ShowConsoleConfigResponse.
        :type robot_action_enable: bool
        """
        self._robot_action_enable = robot_action_enable

    @property
    def http2_enable(self):
        """Gets the http2_enable of this ShowConsoleConfigResponse.

        是否支持http2，false：不支持；true：支持

        :return: The http2_enable of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._http2_enable

    @http2_enable.setter
    def http2_enable(self, http2_enable):
        """Sets the http2_enable of this ShowConsoleConfigResponse.

        是否支持http2，false：不支持；true：支持

        :param http2_enable: The http2_enable of this ShowConsoleConfigResponse.
        :type http2_enable: bool
        """
        self._http2_enable = http2_enable

    @property
    def timeout_config_enable(self):
        """Gets the timeout_config_enable of this ShowConsoleConfigResponse.

        是否支持超时配置，false：不支持；true：支持

        :return: The timeout_config_enable of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._timeout_config_enable

    @timeout_config_enable.setter
    def timeout_config_enable(self, timeout_config_enable):
        """Sets the timeout_config_enable of this ShowConsoleConfigResponse.

        是否支持超时配置，false：不支持；true：支持

        :param timeout_config_enable: The timeout_config_enable of this ShowConsoleConfigResponse.
        :type timeout_config_enable: bool
        """
        self._timeout_config_enable = timeout_config_enable

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
        if not isinstance(other, ShowConsoleConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
