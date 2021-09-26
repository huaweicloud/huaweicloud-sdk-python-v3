# coding: utf-8

import re
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
        'check_all_headers_enable': 'bool'
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
        'check_all_headers_enable': 'check_all_headers_enable'
    }

    def __init__(self, eps=None, tls=None, ipv6=None, alert=None, custom=None, elb_mode=None, event_lts=None, multi_dns=None, search_ip=None, cc_enhance=None, cname_switch=None, custom_block=None, advanced_ignore=None, js_crawler_enable=None, deep_decode_enable=None, overview_bandwidth=None, proxy_use_oldcname=None, check_all_headers_enable=None):
        """ShowConsoleConfigResponse - a model defined in huaweicloud sdk"""
        
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

    @property
    def eps(self):
        """Gets the eps of this ShowConsoleConfigResponse.

        支持EPS

        :return: The eps of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._eps

    @eps.setter
    def eps(self, eps):
        """Sets the eps of this ShowConsoleConfigResponse.

        支持EPS

        :param eps: The eps of this ShowConsoleConfigResponse.
        :type: bool
        """
        self._eps = eps

    @property
    def tls(self):
        """Gets the tls of this ShowConsoleConfigResponse.

        支持TLS

        :return: The tls of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """Sets the tls of this ShowConsoleConfigResponse.

        支持TLS

        :param tls: The tls of this ShowConsoleConfigResponse.
        :type: bool
        """
        self._tls = tls

    @property
    def ipv6(self):
        """Gets the ipv6 of this ShowConsoleConfigResponse.

        支持IPV6

        :return: The ipv6 of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._ipv6

    @ipv6.setter
    def ipv6(self, ipv6):
        """Sets the ipv6 of this ShowConsoleConfigResponse.

        支持IPV6

        :param ipv6: The ipv6 of this ShowConsoleConfigResponse.
        :type: bool
        """
        self._ipv6 = ipv6

    @property
    def alert(self):
        """Gets the alert of this ShowConsoleConfigResponse.

        支持告警

        :return: The alert of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._alert

    @alert.setter
    def alert(self, alert):
        """Sets the alert of this ShowConsoleConfigResponse.

        支持告警

        :param alert: The alert of this ShowConsoleConfigResponse.
        :type: bool
        """
        self._alert = alert

    @property
    def custom(self):
        """Gets the custom of this ShowConsoleConfigResponse.

        支持精准防护

        :return: The custom of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """Sets the custom of this ShowConsoleConfigResponse.

        支持精准防护

        :param custom: The custom of this ShowConsoleConfigResponse.
        :type: bool
        """
        self._custom = custom

    @property
    def elb_mode(self):
        """Gets the elb_mode of this ShowConsoleConfigResponse.

        支持ELB模式

        :return: The elb_mode of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._elb_mode

    @elb_mode.setter
    def elb_mode(self, elb_mode):
        """Sets the elb_mode of this ShowConsoleConfigResponse.

        支持ELB模式

        :param elb_mode: The elb_mode of this ShowConsoleConfigResponse.
        :type: bool
        """
        self._elb_mode = elb_mode

    @property
    def event_lts(self):
        """Gets the event_lts of this ShowConsoleConfigResponse.

        支持LTS全量日志

        :return: The event_lts of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._event_lts

    @event_lts.setter
    def event_lts(self, event_lts):
        """Sets the event_lts of this ShowConsoleConfigResponse.

        支持LTS全量日志

        :param event_lts: The event_lts of this ShowConsoleConfigResponse.
        :type: bool
        """
        self._event_lts = event_lts

    @property
    def multi_dns(self):
        """Gets the multi_dns of this ShowConsoleConfigResponse.

        支持多DNS解析

        :return: The multi_dns of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._multi_dns

    @multi_dns.setter
    def multi_dns(self, multi_dns):
        """Sets the multi_dns of this ShowConsoleConfigResponse.

        支持多DNS解析

        :param multi_dns: The multi_dns of this ShowConsoleConfigResponse.
        :type: bool
        """
        self._multi_dns = multi_dns

    @property
    def search_ip(self):
        """Gets the search_ip of this ShowConsoleConfigResponse.

        支持搜索IP

        :return: The search_ip of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._search_ip

    @search_ip.setter
    def search_ip(self, search_ip):
        """Sets the search_ip of this ShowConsoleConfigResponse.

        支持搜索IP

        :param search_ip: The search_ip of this ShowConsoleConfigResponse.
        :type: bool
        """
        self._search_ip = search_ip

    @property
    def cc_enhance(self):
        """Gets the cc_enhance of this ShowConsoleConfigResponse.

        支持CC增强

        :return: The cc_enhance of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._cc_enhance

    @cc_enhance.setter
    def cc_enhance(self, cc_enhance):
        """Sets the cc_enhance of this ShowConsoleConfigResponse.

        支持CC增强

        :param cc_enhance: The cc_enhance of this ShowConsoleConfigResponse.
        :type: bool
        """
        self._cc_enhance = cc_enhance

    @property
    def cname_switch(self):
        """Gets the cname_switch of this ShowConsoleConfigResponse.

        支持cname切换

        :return: The cname_switch of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._cname_switch

    @cname_switch.setter
    def cname_switch(self, cname_switch):
        """Sets the cname_switch of this ShowConsoleConfigResponse.

        支持cname切换

        :param cname_switch: The cname_switch of this ShowConsoleConfigResponse.
        :type: bool
        """
        self._cname_switch = cname_switch

    @property
    def custom_block(self):
        """Gets the custom_block of this ShowConsoleConfigResponse.

        支持精准拦截

        :return: The custom_block of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._custom_block

    @custom_block.setter
    def custom_block(self, custom_block):
        """Sets the custom_block of this ShowConsoleConfigResponse.

        支持精准拦截

        :param custom_block: The custom_block of this ShowConsoleConfigResponse.
        :type: bool
        """
        self._custom_block = custom_block

    @property
    def advanced_ignore(self):
        """Gets the advanced_ignore of this ShowConsoleConfigResponse.

        支持误报屏蔽

        :return: The advanced_ignore of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._advanced_ignore

    @advanced_ignore.setter
    def advanced_ignore(self, advanced_ignore):
        """Sets the advanced_ignore of this ShowConsoleConfigResponse.

        支持误报屏蔽

        :param advanced_ignore: The advanced_ignore of this ShowConsoleConfigResponse.
        :type: bool
        """
        self._advanced_ignore = advanced_ignore

    @property
    def js_crawler_enable(self):
        """Gets the js_crawler_enable of this ShowConsoleConfigResponse.

        支持js反爬虫

        :return: The js_crawler_enable of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._js_crawler_enable

    @js_crawler_enable.setter
    def js_crawler_enable(self, js_crawler_enable):
        """Sets the js_crawler_enable of this ShowConsoleConfigResponse.

        支持js反爬虫

        :param js_crawler_enable: The js_crawler_enable of this ShowConsoleConfigResponse.
        :type: bool
        """
        self._js_crawler_enable = js_crawler_enable

    @property
    def deep_decode_enable(self):
        """Gets the deep_decode_enable of this ShowConsoleConfigResponse.

        支持深度解析

        :return: The deep_decode_enable of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._deep_decode_enable

    @deep_decode_enable.setter
    def deep_decode_enable(self, deep_decode_enable):
        """Sets the deep_decode_enable of this ShowConsoleConfigResponse.

        支持深度解析

        :param deep_decode_enable: The deep_decode_enable of this ShowConsoleConfigResponse.
        :type: bool
        """
        self._deep_decode_enable = deep_decode_enable

    @property
    def overview_bandwidth(self):
        """Gets the overview_bandwidth of this ShowConsoleConfigResponse.

        支持安全总览带宽统计

        :return: The overview_bandwidth of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._overview_bandwidth

    @overview_bandwidth.setter
    def overview_bandwidth(self, overview_bandwidth):
        """Sets the overview_bandwidth of this ShowConsoleConfigResponse.

        支持安全总览带宽统计

        :param overview_bandwidth: The overview_bandwidth of this ShowConsoleConfigResponse.
        :type: bool
        """
        self._overview_bandwidth = overview_bandwidth

    @property
    def proxy_use_oldcname(self):
        """Gets the proxy_use_oldcname of this ShowConsoleConfigResponse.

        支持使用旧cname解析

        :return: The proxy_use_oldcname of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._proxy_use_oldcname

    @proxy_use_oldcname.setter
    def proxy_use_oldcname(self, proxy_use_oldcname):
        """Sets the proxy_use_oldcname of this ShowConsoleConfigResponse.

        支持使用旧cname解析

        :param proxy_use_oldcname: The proxy_use_oldcname of this ShowConsoleConfigResponse.
        :type: bool
        """
        self._proxy_use_oldcname = proxy_use_oldcname

    @property
    def check_all_headers_enable(self):
        """Gets the check_all_headers_enable of this ShowConsoleConfigResponse.

        支持检查所有的header

        :return: The check_all_headers_enable of this ShowConsoleConfigResponse.
        :rtype: bool
        """
        return self._check_all_headers_enable

    @check_all_headers_enable.setter
    def check_all_headers_enable(self, check_all_headers_enable):
        """Sets the check_all_headers_enable of this ShowConsoleConfigResponse.

        支持检查所有的header

        :param check_all_headers_enable: The check_all_headers_enable of this ShowConsoleConfigResponse.
        :type: bool
        """
        self._check_all_headers_enable = check_all_headers_enable

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
