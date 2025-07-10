# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Actions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flexible_origin': 'list[FlexibleOriginsEngine]',
        'origin_request_header': 'list[OriginRequestHeader]',
        'http_response_header': 'list[HttpResponseHeader]',
        'access_control': 'AccessControl',
        'request_limit_rules': 'RequestLimitRulesEngine',
        'origin_request_url_rewrite': 'OriginRequestUrlRewriteEngine',
        'cache_rule': 'CacheRulesEngine',
        'request_url_rewrite': 'RequestUrlRewriteEngine',
        'browser_cache_rule': 'BrowserCacheRulesEngine',
        'error_code_cache': 'ErrorCodeCacheEngine'
    }

    attribute_map = {
        'flexible_origin': 'flexible_origin',
        'origin_request_header': 'origin_request_header',
        'http_response_header': 'http_response_header',
        'access_control': 'access_control',
        'request_limit_rules': 'request_limit_rules',
        'origin_request_url_rewrite': 'origin_request_url_rewrite',
        'cache_rule': 'cache_rule',
        'request_url_rewrite': 'request_url_rewrite',
        'browser_cache_rule': 'browser_cache_rule',
        'error_code_cache': 'error_code_cache'
    }

    def __init__(self, flexible_origin=None, origin_request_header=None, http_response_header=None, access_control=None, request_limit_rules=None, origin_request_url_rewrite=None, cache_rule=None, request_url_rewrite=None, browser_cache_rule=None, error_code_cache=None):
        r"""Actions

        The model defined in huaweicloud sdk

        :param flexible_origin: **参数解释：** 高级回源，实现根据不同的资源类型或路径回源到不同源站 **约束限制：** 最多配置20条
        :type flexible_origin: list[:class:`huaweicloudsdkcdn.v2.FlexibleOriginsEngine`]
        :param origin_request_header: **参数解释：** CDN节点回源时，改写用户回源请求URL的HTTP头部信息 **约束限制：** - 该功能将覆盖原有配置（清空之前的配置），在使用此接口时，请上传全量头部信息 - 如果域名在后台配置了特殊请求头，需要将对应的请求头一并传入
        :type origin_request_header: list[:class:`huaweicloudsdkcdn.v2.OriginRequestHeader`]
        :param http_response_header: **参数解释：** 配置节点响应给客户端的头部信息，配置响应消息后，用户请求加速域名下的资源时，CDN返回给用户的消息中将包含该域名配置的响应头信息 **约束限制：** - 该功能将覆盖原有配置（清空之前的配置），在使用此接口时，请上传全量头部信息 - 如果域名在后台配置了特殊请求头，需要将对应的请求头一并传入
        :type http_response_header: list[:class:`huaweicloudsdkcdn.v2.HttpResponseHeader`]
        :param access_control: 
        :type access_control: :class:`huaweicloudsdkcdn.v2.AccessControl`
        :param request_limit_rules: 
        :type request_limit_rules: :class:`huaweicloudsdkcdn.v2.RequestLimitRulesEngine`
        :param origin_request_url_rewrite: 
        :type origin_request_url_rewrite: :class:`huaweicloudsdkcdn.v2.OriginRequestUrlRewriteEngine`
        :param cache_rule: 
        :type cache_rule: :class:`huaweicloudsdkcdn.v2.CacheRulesEngine`
        :param request_url_rewrite: 
        :type request_url_rewrite: :class:`huaweicloudsdkcdn.v2.RequestUrlRewriteEngine`
        :param browser_cache_rule: 
        :type browser_cache_rule: :class:`huaweicloudsdkcdn.v2.BrowserCacheRulesEngine`
        :param error_code_cache: 
        :type error_code_cache: :class:`huaweicloudsdkcdn.v2.ErrorCodeCacheEngine`
        """
        
        

        self._flexible_origin = None
        self._origin_request_header = None
        self._http_response_header = None
        self._access_control = None
        self._request_limit_rules = None
        self._origin_request_url_rewrite = None
        self._cache_rule = None
        self._request_url_rewrite = None
        self._browser_cache_rule = None
        self._error_code_cache = None
        self.discriminator = None

        if flexible_origin is not None:
            self.flexible_origin = flexible_origin
        if origin_request_header is not None:
            self.origin_request_header = origin_request_header
        if http_response_header is not None:
            self.http_response_header = http_response_header
        if access_control is not None:
            self.access_control = access_control
        if request_limit_rules is not None:
            self.request_limit_rules = request_limit_rules
        if origin_request_url_rewrite is not None:
            self.origin_request_url_rewrite = origin_request_url_rewrite
        if cache_rule is not None:
            self.cache_rule = cache_rule
        if request_url_rewrite is not None:
            self.request_url_rewrite = request_url_rewrite
        if browser_cache_rule is not None:
            self.browser_cache_rule = browser_cache_rule
        if error_code_cache is not None:
            self.error_code_cache = error_code_cache

    @property
    def flexible_origin(self):
        r"""Gets the flexible_origin of this Actions.

        **参数解释：** 高级回源，实现根据不同的资源类型或路径回源到不同源站 **约束限制：** 最多配置20条

        :return: The flexible_origin of this Actions.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.FlexibleOriginsEngine`]
        """
        return self._flexible_origin

    @flexible_origin.setter
    def flexible_origin(self, flexible_origin):
        r"""Sets the flexible_origin of this Actions.

        **参数解释：** 高级回源，实现根据不同的资源类型或路径回源到不同源站 **约束限制：** 最多配置20条

        :param flexible_origin: The flexible_origin of this Actions.
        :type flexible_origin: list[:class:`huaweicloudsdkcdn.v2.FlexibleOriginsEngine`]
        """
        self._flexible_origin = flexible_origin

    @property
    def origin_request_header(self):
        r"""Gets the origin_request_header of this Actions.

        **参数解释：** CDN节点回源时，改写用户回源请求URL的HTTP头部信息 **约束限制：** - 该功能将覆盖原有配置（清空之前的配置），在使用此接口时，请上传全量头部信息 - 如果域名在后台配置了特殊请求头，需要将对应的请求头一并传入

        :return: The origin_request_header of this Actions.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.OriginRequestHeader`]
        """
        return self._origin_request_header

    @origin_request_header.setter
    def origin_request_header(self, origin_request_header):
        r"""Sets the origin_request_header of this Actions.

        **参数解释：** CDN节点回源时，改写用户回源请求URL的HTTP头部信息 **约束限制：** - 该功能将覆盖原有配置（清空之前的配置），在使用此接口时，请上传全量头部信息 - 如果域名在后台配置了特殊请求头，需要将对应的请求头一并传入

        :param origin_request_header: The origin_request_header of this Actions.
        :type origin_request_header: list[:class:`huaweicloudsdkcdn.v2.OriginRequestHeader`]
        """
        self._origin_request_header = origin_request_header

    @property
    def http_response_header(self):
        r"""Gets the http_response_header of this Actions.

        **参数解释：** 配置节点响应给客户端的头部信息，配置响应消息后，用户请求加速域名下的资源时，CDN返回给用户的消息中将包含该域名配置的响应头信息 **约束限制：** - 该功能将覆盖原有配置（清空之前的配置），在使用此接口时，请上传全量头部信息 - 如果域名在后台配置了特殊请求头，需要将对应的请求头一并传入

        :return: The http_response_header of this Actions.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.HttpResponseHeader`]
        """
        return self._http_response_header

    @http_response_header.setter
    def http_response_header(self, http_response_header):
        r"""Sets the http_response_header of this Actions.

        **参数解释：** 配置节点响应给客户端的头部信息，配置响应消息后，用户请求加速域名下的资源时，CDN返回给用户的消息中将包含该域名配置的响应头信息 **约束限制：** - 该功能将覆盖原有配置（清空之前的配置），在使用此接口时，请上传全量头部信息 - 如果域名在后台配置了特殊请求头，需要将对应的请求头一并传入

        :param http_response_header: The http_response_header of this Actions.
        :type http_response_header: list[:class:`huaweicloudsdkcdn.v2.HttpResponseHeader`]
        """
        self._http_response_header = http_response_header

    @property
    def access_control(self):
        r"""Gets the access_control of this Actions.

        :return: The access_control of this Actions.
        :rtype: :class:`huaweicloudsdkcdn.v2.AccessControl`
        """
        return self._access_control

    @access_control.setter
    def access_control(self, access_control):
        r"""Sets the access_control of this Actions.

        :param access_control: The access_control of this Actions.
        :type access_control: :class:`huaweicloudsdkcdn.v2.AccessControl`
        """
        self._access_control = access_control

    @property
    def request_limit_rules(self):
        r"""Gets the request_limit_rules of this Actions.

        :return: The request_limit_rules of this Actions.
        :rtype: :class:`huaweicloudsdkcdn.v2.RequestLimitRulesEngine`
        """
        return self._request_limit_rules

    @request_limit_rules.setter
    def request_limit_rules(self, request_limit_rules):
        r"""Sets the request_limit_rules of this Actions.

        :param request_limit_rules: The request_limit_rules of this Actions.
        :type request_limit_rules: :class:`huaweicloudsdkcdn.v2.RequestLimitRulesEngine`
        """
        self._request_limit_rules = request_limit_rules

    @property
    def origin_request_url_rewrite(self):
        r"""Gets the origin_request_url_rewrite of this Actions.

        :return: The origin_request_url_rewrite of this Actions.
        :rtype: :class:`huaweicloudsdkcdn.v2.OriginRequestUrlRewriteEngine`
        """
        return self._origin_request_url_rewrite

    @origin_request_url_rewrite.setter
    def origin_request_url_rewrite(self, origin_request_url_rewrite):
        r"""Sets the origin_request_url_rewrite of this Actions.

        :param origin_request_url_rewrite: The origin_request_url_rewrite of this Actions.
        :type origin_request_url_rewrite: :class:`huaweicloudsdkcdn.v2.OriginRequestUrlRewriteEngine`
        """
        self._origin_request_url_rewrite = origin_request_url_rewrite

    @property
    def cache_rule(self):
        r"""Gets the cache_rule of this Actions.

        :return: The cache_rule of this Actions.
        :rtype: :class:`huaweicloudsdkcdn.v2.CacheRulesEngine`
        """
        return self._cache_rule

    @cache_rule.setter
    def cache_rule(self, cache_rule):
        r"""Sets the cache_rule of this Actions.

        :param cache_rule: The cache_rule of this Actions.
        :type cache_rule: :class:`huaweicloudsdkcdn.v2.CacheRulesEngine`
        """
        self._cache_rule = cache_rule

    @property
    def request_url_rewrite(self):
        r"""Gets the request_url_rewrite of this Actions.

        :return: The request_url_rewrite of this Actions.
        :rtype: :class:`huaweicloudsdkcdn.v2.RequestUrlRewriteEngine`
        """
        return self._request_url_rewrite

    @request_url_rewrite.setter
    def request_url_rewrite(self, request_url_rewrite):
        r"""Sets the request_url_rewrite of this Actions.

        :param request_url_rewrite: The request_url_rewrite of this Actions.
        :type request_url_rewrite: :class:`huaweicloudsdkcdn.v2.RequestUrlRewriteEngine`
        """
        self._request_url_rewrite = request_url_rewrite

    @property
    def browser_cache_rule(self):
        r"""Gets the browser_cache_rule of this Actions.

        :return: The browser_cache_rule of this Actions.
        :rtype: :class:`huaweicloudsdkcdn.v2.BrowserCacheRulesEngine`
        """
        return self._browser_cache_rule

    @browser_cache_rule.setter
    def browser_cache_rule(self, browser_cache_rule):
        r"""Sets the browser_cache_rule of this Actions.

        :param browser_cache_rule: The browser_cache_rule of this Actions.
        :type browser_cache_rule: :class:`huaweicloudsdkcdn.v2.BrowserCacheRulesEngine`
        """
        self._browser_cache_rule = browser_cache_rule

    @property
    def error_code_cache(self):
        r"""Gets the error_code_cache of this Actions.

        :return: The error_code_cache of this Actions.
        :rtype: :class:`huaweicloudsdkcdn.v2.ErrorCodeCacheEngine`
        """
        return self._error_code_cache

    @error_code_cache.setter
    def error_code_cache(self, error_code_cache):
        r"""Sets the error_code_cache of this Actions.

        :param error_code_cache: The error_code_cache of this Actions.
        :type error_code_cache: :class:`huaweicloudsdkcdn.v2.ErrorCodeCacheEngine`
        """
        self._error_code_cache = error_code_cache

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
        if not isinstance(other, Actions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
