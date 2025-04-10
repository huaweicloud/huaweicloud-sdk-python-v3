# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Configs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'origin_request_header': 'list[OriginRequestHeader]',
        'http_response_header': 'list[HttpResponseHeader]',
        'url_auth': 'UrlAuth',
        'https': 'HttpPutBody',
        'sources': 'list[SourcesConfig]',
        'origin_protocol': 'str',
        'origin_follow302_status': 'str',
        'cache_rules': 'list[CacheRules]',
        'ip_filter': 'IpFilter',
        'referer': 'RefererConfig',
        'force_redirect': 'ForceRedirectConfig',
        'compress': 'Compress',
        'cache_url_parameter_filter': 'CacheUrlParameterFilter',
        'ipv6_accelerate': 'int',
        'error_code_cache': 'list[ErrorCodeCache]',
        'origin_range_status': 'str',
        'user_agent_filter': 'UserAgentFilter',
        'origin_request_url_rewrite': 'list[OriginRequestUrlRewrite]',
        'error_code_redirect_rules': 'list[ErrorCodeRedirectRules]'
    }

    attribute_map = {
        'origin_request_header': 'origin_request_header',
        'http_response_header': 'http_response_header',
        'url_auth': 'url_auth',
        'https': 'https',
        'sources': 'sources',
        'origin_protocol': 'origin_protocol',
        'origin_follow302_status': 'origin_follow302_status',
        'cache_rules': 'cache_rules',
        'ip_filter': 'ip_filter',
        'referer': 'referer',
        'force_redirect': 'force_redirect',
        'compress': 'compress',
        'cache_url_parameter_filter': 'cache_url_parameter_filter',
        'ipv6_accelerate': 'ipv6_accelerate',
        'error_code_cache': 'error_code_cache',
        'origin_range_status': 'origin_range_status',
        'user_agent_filter': 'user_agent_filter',
        'origin_request_url_rewrite': 'origin_request_url_rewrite',
        'error_code_redirect_rules': 'error_code_redirect_rules'
    }

    def __init__(self, origin_request_header=None, http_response_header=None, url_auth=None, https=None, sources=None, origin_protocol=None, origin_follow302_status=None, cache_rules=None, ip_filter=None, referer=None, force_redirect=None, compress=None, cache_url_parameter_filter=None, ipv6_accelerate=None, error_code_cache=None, origin_range_status=None, user_agent_filter=None, origin_request_url_rewrite=None, error_code_redirect_rules=None):
        r"""Configs

        The model defined in huaweicloud sdk

        :param origin_request_header: 回源请求头改写 该功能将覆盖原有配置（清空之前的配置），在使用此接口时，请上传全量头部信息。
        :type origin_request_header: list[:class:`huaweicloudsdkcdn.v1.OriginRequestHeader`]
        :param http_response_header: http header配置 该功能将覆盖原有配置（清空之前的配置），在使用此接口时，请上传全量头部信息。
        :type http_response_header: list[:class:`huaweicloudsdkcdn.v1.HttpResponseHeader`]
        :param url_auth: 
        :type url_auth: :class:`huaweicloudsdkcdn.v1.UrlAuth`
        :param https: 
        :type https: :class:`huaweicloudsdkcdn.v1.HttpPutBody`
        :param sources: 源站配置。
        :type sources: list[:class:`huaweicloudsdkcdn.v1.SourcesConfig`]
        :param origin_protocol: 回源协议，follow：协议跟随回源，http：HTTP回源(默认)，https：https回源。
        :type origin_protocol: str
        :param origin_follow302_status: 回源跟随，on：开启，off：关闭。
        :type origin_follow302_status: str
        :param cache_rules: 缓存规则。
        :type cache_rules: list[:class:`huaweicloudsdkcdn.v1.CacheRules`]
        :param ip_filter: 
        :type ip_filter: :class:`huaweicloudsdkcdn.v1.IpFilter`
        :param referer: 
        :type referer: :class:`huaweicloudsdkcdn.v1.RefererConfig`
        :param force_redirect: 
        :type force_redirect: :class:`huaweicloudsdkcdn.v1.ForceRedirectConfig`
        :param compress: 
        :type compress: :class:`huaweicloudsdkcdn.v1.Compress`
        :param cache_url_parameter_filter: 
        :type cache_url_parameter_filter: :class:`huaweicloudsdkcdn.v1.CacheUrlParameterFilter`
        :param ipv6_accelerate: ipv6设置，1：打开；0：关闭。
        :type ipv6_accelerate: int
        :param error_code_cache: 状态码缓存时间。
        :type error_code_cache: list[:class:`huaweicloudsdkcdn.v1.ErrorCodeCache`]
        :param origin_range_status: Range回源，即分片回源，开启: on，关闭: off。  &gt; 开启Range回源的前提是您的源站支持Range请求，即HTTP请求头中包含Range字段，否则可能导致回源失败。
        :type origin_range_status: str
        :param user_agent_filter: 
        :type user_agent_filter: :class:`huaweicloudsdkcdn.v1.UserAgentFilter`
        :param origin_request_url_rewrite: 改写回源URL，最多配置20条。
        :type origin_request_url_rewrite: list[:class:`huaweicloudsdkcdn.v1.OriginRequestUrlRewrite`]
        :param error_code_redirect_rules: 自定义错误页面。
        :type error_code_redirect_rules: list[:class:`huaweicloudsdkcdn.v1.ErrorCodeRedirectRules`]
        """
        
        

        self._origin_request_header = None
        self._http_response_header = None
        self._url_auth = None
        self._https = None
        self._sources = None
        self._origin_protocol = None
        self._origin_follow302_status = None
        self._cache_rules = None
        self._ip_filter = None
        self._referer = None
        self._force_redirect = None
        self._compress = None
        self._cache_url_parameter_filter = None
        self._ipv6_accelerate = None
        self._error_code_cache = None
        self._origin_range_status = None
        self._user_agent_filter = None
        self._origin_request_url_rewrite = None
        self._error_code_redirect_rules = None
        self.discriminator = None

        if origin_request_header is not None:
            self.origin_request_header = origin_request_header
        if http_response_header is not None:
            self.http_response_header = http_response_header
        if url_auth is not None:
            self.url_auth = url_auth
        if https is not None:
            self.https = https
        if sources is not None:
            self.sources = sources
        if origin_protocol is not None:
            self.origin_protocol = origin_protocol
        if origin_follow302_status is not None:
            self.origin_follow302_status = origin_follow302_status
        if cache_rules is not None:
            self.cache_rules = cache_rules
        if ip_filter is not None:
            self.ip_filter = ip_filter
        if referer is not None:
            self.referer = referer
        if force_redirect is not None:
            self.force_redirect = force_redirect
        if compress is not None:
            self.compress = compress
        if cache_url_parameter_filter is not None:
            self.cache_url_parameter_filter = cache_url_parameter_filter
        if ipv6_accelerate is not None:
            self.ipv6_accelerate = ipv6_accelerate
        if error_code_cache is not None:
            self.error_code_cache = error_code_cache
        if origin_range_status is not None:
            self.origin_range_status = origin_range_status
        if user_agent_filter is not None:
            self.user_agent_filter = user_agent_filter
        if origin_request_url_rewrite is not None:
            self.origin_request_url_rewrite = origin_request_url_rewrite
        if error_code_redirect_rules is not None:
            self.error_code_redirect_rules = error_code_redirect_rules

    @property
    def origin_request_header(self):
        r"""Gets the origin_request_header of this Configs.

        回源请求头改写 该功能将覆盖原有配置（清空之前的配置），在使用此接口时，请上传全量头部信息。

        :return: The origin_request_header of this Configs.
        :rtype: list[:class:`huaweicloudsdkcdn.v1.OriginRequestHeader`]
        """
        return self._origin_request_header

    @origin_request_header.setter
    def origin_request_header(self, origin_request_header):
        r"""Sets the origin_request_header of this Configs.

        回源请求头改写 该功能将覆盖原有配置（清空之前的配置），在使用此接口时，请上传全量头部信息。

        :param origin_request_header: The origin_request_header of this Configs.
        :type origin_request_header: list[:class:`huaweicloudsdkcdn.v1.OriginRequestHeader`]
        """
        self._origin_request_header = origin_request_header

    @property
    def http_response_header(self):
        r"""Gets the http_response_header of this Configs.

        http header配置 该功能将覆盖原有配置（清空之前的配置），在使用此接口时，请上传全量头部信息。

        :return: The http_response_header of this Configs.
        :rtype: list[:class:`huaweicloudsdkcdn.v1.HttpResponseHeader`]
        """
        return self._http_response_header

    @http_response_header.setter
    def http_response_header(self, http_response_header):
        r"""Sets the http_response_header of this Configs.

        http header配置 该功能将覆盖原有配置（清空之前的配置），在使用此接口时，请上传全量头部信息。

        :param http_response_header: The http_response_header of this Configs.
        :type http_response_header: list[:class:`huaweicloudsdkcdn.v1.HttpResponseHeader`]
        """
        self._http_response_header = http_response_header

    @property
    def url_auth(self):
        r"""Gets the url_auth of this Configs.

        :return: The url_auth of this Configs.
        :rtype: :class:`huaweicloudsdkcdn.v1.UrlAuth`
        """
        return self._url_auth

    @url_auth.setter
    def url_auth(self, url_auth):
        r"""Sets the url_auth of this Configs.

        :param url_auth: The url_auth of this Configs.
        :type url_auth: :class:`huaweicloudsdkcdn.v1.UrlAuth`
        """
        self._url_auth = url_auth

    @property
    def https(self):
        r"""Gets the https of this Configs.

        :return: The https of this Configs.
        :rtype: :class:`huaweicloudsdkcdn.v1.HttpPutBody`
        """
        return self._https

    @https.setter
    def https(self, https):
        r"""Sets the https of this Configs.

        :param https: The https of this Configs.
        :type https: :class:`huaweicloudsdkcdn.v1.HttpPutBody`
        """
        self._https = https

    @property
    def sources(self):
        r"""Gets the sources of this Configs.

        源站配置。

        :return: The sources of this Configs.
        :rtype: list[:class:`huaweicloudsdkcdn.v1.SourcesConfig`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        r"""Sets the sources of this Configs.

        源站配置。

        :param sources: The sources of this Configs.
        :type sources: list[:class:`huaweicloudsdkcdn.v1.SourcesConfig`]
        """
        self._sources = sources

    @property
    def origin_protocol(self):
        r"""Gets the origin_protocol of this Configs.

        回源协议，follow：协议跟随回源，http：HTTP回源(默认)，https：https回源。

        :return: The origin_protocol of this Configs.
        :rtype: str
        """
        return self._origin_protocol

    @origin_protocol.setter
    def origin_protocol(self, origin_protocol):
        r"""Sets the origin_protocol of this Configs.

        回源协议，follow：协议跟随回源，http：HTTP回源(默认)，https：https回源。

        :param origin_protocol: The origin_protocol of this Configs.
        :type origin_protocol: str
        """
        self._origin_protocol = origin_protocol

    @property
    def origin_follow302_status(self):
        r"""Gets the origin_follow302_status of this Configs.

        回源跟随，on：开启，off：关闭。

        :return: The origin_follow302_status of this Configs.
        :rtype: str
        """
        return self._origin_follow302_status

    @origin_follow302_status.setter
    def origin_follow302_status(self, origin_follow302_status):
        r"""Sets the origin_follow302_status of this Configs.

        回源跟随，on：开启，off：关闭。

        :param origin_follow302_status: The origin_follow302_status of this Configs.
        :type origin_follow302_status: str
        """
        self._origin_follow302_status = origin_follow302_status

    @property
    def cache_rules(self):
        r"""Gets the cache_rules of this Configs.

        缓存规则。

        :return: The cache_rules of this Configs.
        :rtype: list[:class:`huaweicloudsdkcdn.v1.CacheRules`]
        """
        return self._cache_rules

    @cache_rules.setter
    def cache_rules(self, cache_rules):
        r"""Sets the cache_rules of this Configs.

        缓存规则。

        :param cache_rules: The cache_rules of this Configs.
        :type cache_rules: list[:class:`huaweicloudsdkcdn.v1.CacheRules`]
        """
        self._cache_rules = cache_rules

    @property
    def ip_filter(self):
        r"""Gets the ip_filter of this Configs.

        :return: The ip_filter of this Configs.
        :rtype: :class:`huaweicloudsdkcdn.v1.IpFilter`
        """
        return self._ip_filter

    @ip_filter.setter
    def ip_filter(self, ip_filter):
        r"""Sets the ip_filter of this Configs.

        :param ip_filter: The ip_filter of this Configs.
        :type ip_filter: :class:`huaweicloudsdkcdn.v1.IpFilter`
        """
        self._ip_filter = ip_filter

    @property
    def referer(self):
        r"""Gets the referer of this Configs.

        :return: The referer of this Configs.
        :rtype: :class:`huaweicloudsdkcdn.v1.RefererConfig`
        """
        return self._referer

    @referer.setter
    def referer(self, referer):
        r"""Sets the referer of this Configs.

        :param referer: The referer of this Configs.
        :type referer: :class:`huaweicloudsdkcdn.v1.RefererConfig`
        """
        self._referer = referer

    @property
    def force_redirect(self):
        r"""Gets the force_redirect of this Configs.

        :return: The force_redirect of this Configs.
        :rtype: :class:`huaweicloudsdkcdn.v1.ForceRedirectConfig`
        """
        return self._force_redirect

    @force_redirect.setter
    def force_redirect(self, force_redirect):
        r"""Sets the force_redirect of this Configs.

        :param force_redirect: The force_redirect of this Configs.
        :type force_redirect: :class:`huaweicloudsdkcdn.v1.ForceRedirectConfig`
        """
        self._force_redirect = force_redirect

    @property
    def compress(self):
        r"""Gets the compress of this Configs.

        :return: The compress of this Configs.
        :rtype: :class:`huaweicloudsdkcdn.v1.Compress`
        """
        return self._compress

    @compress.setter
    def compress(self, compress):
        r"""Sets the compress of this Configs.

        :param compress: The compress of this Configs.
        :type compress: :class:`huaweicloudsdkcdn.v1.Compress`
        """
        self._compress = compress

    @property
    def cache_url_parameter_filter(self):
        r"""Gets the cache_url_parameter_filter of this Configs.

        :return: The cache_url_parameter_filter of this Configs.
        :rtype: :class:`huaweicloudsdkcdn.v1.CacheUrlParameterFilter`
        """
        return self._cache_url_parameter_filter

    @cache_url_parameter_filter.setter
    def cache_url_parameter_filter(self, cache_url_parameter_filter):
        r"""Sets the cache_url_parameter_filter of this Configs.

        :param cache_url_parameter_filter: The cache_url_parameter_filter of this Configs.
        :type cache_url_parameter_filter: :class:`huaweicloudsdkcdn.v1.CacheUrlParameterFilter`
        """
        self._cache_url_parameter_filter = cache_url_parameter_filter

    @property
    def ipv6_accelerate(self):
        r"""Gets the ipv6_accelerate of this Configs.

        ipv6设置，1：打开；0：关闭。

        :return: The ipv6_accelerate of this Configs.
        :rtype: int
        """
        return self._ipv6_accelerate

    @ipv6_accelerate.setter
    def ipv6_accelerate(self, ipv6_accelerate):
        r"""Sets the ipv6_accelerate of this Configs.

        ipv6设置，1：打开；0：关闭。

        :param ipv6_accelerate: The ipv6_accelerate of this Configs.
        :type ipv6_accelerate: int
        """
        self._ipv6_accelerate = ipv6_accelerate

    @property
    def error_code_cache(self):
        r"""Gets the error_code_cache of this Configs.

        状态码缓存时间。

        :return: The error_code_cache of this Configs.
        :rtype: list[:class:`huaweicloudsdkcdn.v1.ErrorCodeCache`]
        """
        return self._error_code_cache

    @error_code_cache.setter
    def error_code_cache(self, error_code_cache):
        r"""Sets the error_code_cache of this Configs.

        状态码缓存时间。

        :param error_code_cache: The error_code_cache of this Configs.
        :type error_code_cache: list[:class:`huaweicloudsdkcdn.v1.ErrorCodeCache`]
        """
        self._error_code_cache = error_code_cache

    @property
    def origin_range_status(self):
        r"""Gets the origin_range_status of this Configs.

        Range回源，即分片回源，开启: on，关闭: off。  > 开启Range回源的前提是您的源站支持Range请求，即HTTP请求头中包含Range字段，否则可能导致回源失败。

        :return: The origin_range_status of this Configs.
        :rtype: str
        """
        return self._origin_range_status

    @origin_range_status.setter
    def origin_range_status(self, origin_range_status):
        r"""Sets the origin_range_status of this Configs.

        Range回源，即分片回源，开启: on，关闭: off。  > 开启Range回源的前提是您的源站支持Range请求，即HTTP请求头中包含Range字段，否则可能导致回源失败。

        :param origin_range_status: The origin_range_status of this Configs.
        :type origin_range_status: str
        """
        self._origin_range_status = origin_range_status

    @property
    def user_agent_filter(self):
        r"""Gets the user_agent_filter of this Configs.

        :return: The user_agent_filter of this Configs.
        :rtype: :class:`huaweicloudsdkcdn.v1.UserAgentFilter`
        """
        return self._user_agent_filter

    @user_agent_filter.setter
    def user_agent_filter(self, user_agent_filter):
        r"""Sets the user_agent_filter of this Configs.

        :param user_agent_filter: The user_agent_filter of this Configs.
        :type user_agent_filter: :class:`huaweicloudsdkcdn.v1.UserAgentFilter`
        """
        self._user_agent_filter = user_agent_filter

    @property
    def origin_request_url_rewrite(self):
        r"""Gets the origin_request_url_rewrite of this Configs.

        改写回源URL，最多配置20条。

        :return: The origin_request_url_rewrite of this Configs.
        :rtype: list[:class:`huaweicloudsdkcdn.v1.OriginRequestUrlRewrite`]
        """
        return self._origin_request_url_rewrite

    @origin_request_url_rewrite.setter
    def origin_request_url_rewrite(self, origin_request_url_rewrite):
        r"""Sets the origin_request_url_rewrite of this Configs.

        改写回源URL，最多配置20条。

        :param origin_request_url_rewrite: The origin_request_url_rewrite of this Configs.
        :type origin_request_url_rewrite: list[:class:`huaweicloudsdkcdn.v1.OriginRequestUrlRewrite`]
        """
        self._origin_request_url_rewrite = origin_request_url_rewrite

    @property
    def error_code_redirect_rules(self):
        r"""Gets the error_code_redirect_rules of this Configs.

        自定义错误页面。

        :return: The error_code_redirect_rules of this Configs.
        :rtype: list[:class:`huaweicloudsdkcdn.v1.ErrorCodeRedirectRules`]
        """
        return self._error_code_redirect_rules

    @error_code_redirect_rules.setter
    def error_code_redirect_rules(self, error_code_redirect_rules):
        r"""Sets the error_code_redirect_rules of this Configs.

        自定义错误页面。

        :param error_code_redirect_rules: The error_code_redirect_rules of this Configs.
        :type error_code_redirect_rules: list[:class:`huaweicloudsdkcdn.v1.ErrorCodeRedirectRules`]
        """
        self._error_code_redirect_rules = error_code_redirect_rules

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
        if not isinstance(other, Configs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
