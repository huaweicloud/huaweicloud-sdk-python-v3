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
        'business_type': 'str',
        'service_area': 'str',
        'remark': 'str',
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
        'flexible_origin': 'list[FlexibleOrigins]',
        'slice_etag_status': 'str',
        'origin_receive_timeout': 'int',
        'remote_auth': 'CommonRemoteAuth',
        'websocket': 'WebSocketSeek',
        'video_seek': 'VideoSeek',
        'request_limit_rules': 'list[RequestLimitRules]',
        'ip_frequency_limit': 'IpFrequencyLimit',
        'hsts': 'Hsts',
        'quic': 'Quic',
        'error_code_redirect_rules': 'list[ErrorCodeRedirectRules]',
        'sni': 'Sni',
        'request_url_rewrite': 'list[RequestUrlRewrite]',
        'browser_cache_rules': 'list[BrowserCacheRules]',
        'access_area_filter': 'list[AccessAreaFilter]'
    }

    attribute_map = {
        'business_type': 'business_type',
        'service_area': 'service_area',
        'remark': 'remark',
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
        'flexible_origin': 'flexible_origin',
        'slice_etag_status': 'slice_etag_status',
        'origin_receive_timeout': 'origin_receive_timeout',
        'remote_auth': 'remote_auth',
        'websocket': 'websocket',
        'video_seek': 'video_seek',
        'request_limit_rules': 'request_limit_rules',
        'ip_frequency_limit': 'ip_frequency_limit',
        'hsts': 'hsts',
        'quic': 'quic',
        'error_code_redirect_rules': 'error_code_redirect_rules',
        'sni': 'sni',
        'request_url_rewrite': 'request_url_rewrite',
        'browser_cache_rules': 'browser_cache_rules',
        'access_area_filter': 'access_area_filter'
    }

    def __init__(self, business_type=None, service_area=None, remark=None, origin_request_header=None, http_response_header=None, url_auth=None, https=None, sources=None, origin_protocol=None, origin_follow302_status=None, cache_rules=None, ip_filter=None, referer=None, force_redirect=None, compress=None, cache_url_parameter_filter=None, ipv6_accelerate=None, error_code_cache=None, origin_range_status=None, user_agent_filter=None, origin_request_url_rewrite=None, flexible_origin=None, slice_etag_status=None, origin_receive_timeout=None, remote_auth=None, websocket=None, video_seek=None, request_limit_rules=None, ip_frequency_limit=None, hsts=None, quic=None, error_code_redirect_rules=None, sni=None, request_url_rewrite=None, browser_cache_rules=None, access_area_filter=None):
        """Configs

        The model defined in huaweicloud sdk

        :param business_type: 业务类型： - web：网站加速； - download：文件下载加速； - video：点播加速。  &gt; 暂不支持“全站加速”变更为其它业务类型。
        :type business_type: str
        :param service_area: 服务区域： - mainland_china：中国大陆； - global：全球； - outside_mainland_china：中国大陆境外。  &gt; 暂不支持“中国大陆”与“中国大陆境外”互相直接切换。
        :type service_area: str
        :param remark: 给域名添加备注，字符长度范围0-200。
        :type remark: str
        :param origin_request_header: 回源请求头改写 该功能将覆盖原有配置（清空之前的配置），在使用此接口时，请上传全量头部信息。
        :type origin_request_header: list[:class:`huaweicloudsdkcdn.v2.OriginRequestHeader`]
        :param http_response_header: http header配置 该功能将覆盖原有配置（清空之前的配置），在使用此接口时，请上传全量头部信息。
        :type http_response_header: list[:class:`huaweicloudsdkcdn.v2.HttpResponseHeader`]
        :param url_auth: 
        :type url_auth: :class:`huaweicloudsdkcdn.v2.UrlAuth`
        :param https: 
        :type https: :class:`huaweicloudsdkcdn.v2.HttpPutBody`
        :param sources: 源站配置。
        :type sources: list[:class:`huaweicloudsdkcdn.v2.SourcesConfig`]
        :param origin_protocol: 回源协议，follow：协议跟随回源，http：HTTP回源(默认)，https：https回源。
        :type origin_protocol: str
        :param origin_follow302_status: 回源跟随，on：开启，off：关闭。
        :type origin_follow302_status: str
        :param cache_rules: 缓存规则。
        :type cache_rules: list[:class:`huaweicloudsdkcdn.v2.CacheRules`]
        :param ip_filter: 
        :type ip_filter: :class:`huaweicloudsdkcdn.v2.IpFilter`
        :param referer: 
        :type referer: :class:`huaweicloudsdkcdn.v2.RefererConfig`
        :param force_redirect: 
        :type force_redirect: :class:`huaweicloudsdkcdn.v2.ForceRedirectConfig`
        :param compress: 
        :type compress: :class:`huaweicloudsdkcdn.v2.Compress`
        :param cache_url_parameter_filter: 
        :type cache_url_parameter_filter: :class:`huaweicloudsdkcdn.v2.CacheUrlParameterFilter`
        :param ipv6_accelerate: ipv6设置，1：打开；0：关闭。
        :type ipv6_accelerate: int
        :param error_code_cache: 状态码缓存时间。
        :type error_code_cache: list[:class:`huaweicloudsdkcdn.v2.ErrorCodeCache`]
        :param origin_range_status: Range回源，即分片回源，开启: on，关闭: off。  &gt; 开启Range回源的前提是您的源站支持Range请求，即HTTP请求头中包含Range字段，否则可能导致回源失败。
        :type origin_range_status: str
        :param user_agent_filter: 
        :type user_agent_filter: :class:`huaweicloudsdkcdn.v2.UserAgentFilter`
        :param origin_request_url_rewrite: 改写回源URL，最多配置20条。
        :type origin_request_url_rewrite: list[:class:`huaweicloudsdkcdn.v2.OriginRequestUrlRewrite`]
        :param flexible_origin: 高级回源，最多配置20条。
        :type flexible_origin: list[:class:`huaweicloudsdkcdn.v2.FlexibleOrigins`]
        :param slice_etag_status: 回源是否校验ETag，on：开启，off：关闭。
        :type slice_etag_status: str
        :param origin_receive_timeout: 回源超时时间，范围:5-60，单位：秒。
        :type origin_receive_timeout: int
        :param remote_auth: 
        :type remote_auth: :class:`huaweicloudsdkcdn.v2.CommonRemoteAuth`
        :param websocket: 
        :type websocket: :class:`huaweicloudsdkcdn.v2.WebSocketSeek`
        :param video_seek: 
        :type video_seek: :class:`huaweicloudsdkcdn.v2.VideoSeek`
        :param request_limit_rules: 请求限速配置。
        :type request_limit_rules: list[:class:`huaweicloudsdkcdn.v2.RequestLimitRules`]
        :param ip_frequency_limit: 
        :type ip_frequency_limit: :class:`huaweicloudsdkcdn.v2.IpFrequencyLimit`
        :param hsts: 
        :type hsts: :class:`huaweicloudsdkcdn.v2.Hsts`
        :param quic: 
        :type quic: :class:`huaweicloudsdkcdn.v2.Quic`
        :param error_code_redirect_rules: 自定义错误页面。
        :type error_code_redirect_rules: list[:class:`huaweicloudsdkcdn.v2.ErrorCodeRedirectRules`]
        :param sni: 
        :type sni: :class:`huaweicloudsdkcdn.v2.Sni`
        :param request_url_rewrite: 访问URL重写。
        :type request_url_rewrite: list[:class:`huaweicloudsdkcdn.v2.RequestUrlRewrite`]
        :param browser_cache_rules: 浏览器缓存过期时间。
        :type browser_cache_rules: list[:class:`huaweicloudsdkcdn.v2.BrowserCacheRules`]
        :param access_area_filter: 
        :type access_area_filter: list[:class:`huaweicloudsdkcdn.v2.AccessAreaFilter`]
        """
        
        

        self._business_type = None
        self._service_area = None
        self._remark = None
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
        self._flexible_origin = None
        self._slice_etag_status = None
        self._origin_receive_timeout = None
        self._remote_auth = None
        self._websocket = None
        self._video_seek = None
        self._request_limit_rules = None
        self._ip_frequency_limit = None
        self._hsts = None
        self._quic = None
        self._error_code_redirect_rules = None
        self._sni = None
        self._request_url_rewrite = None
        self._browser_cache_rules = None
        self._access_area_filter = None
        self.discriminator = None

        if business_type is not None:
            self.business_type = business_type
        if service_area is not None:
            self.service_area = service_area
        if remark is not None:
            self.remark = remark
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
        if flexible_origin is not None:
            self.flexible_origin = flexible_origin
        if slice_etag_status is not None:
            self.slice_etag_status = slice_etag_status
        if origin_receive_timeout is not None:
            self.origin_receive_timeout = origin_receive_timeout
        if remote_auth is not None:
            self.remote_auth = remote_auth
        if websocket is not None:
            self.websocket = websocket
        if video_seek is not None:
            self.video_seek = video_seek
        if request_limit_rules is not None:
            self.request_limit_rules = request_limit_rules
        if ip_frequency_limit is not None:
            self.ip_frequency_limit = ip_frequency_limit
        if hsts is not None:
            self.hsts = hsts
        if quic is not None:
            self.quic = quic
        if error_code_redirect_rules is not None:
            self.error_code_redirect_rules = error_code_redirect_rules
        if sni is not None:
            self.sni = sni
        if request_url_rewrite is not None:
            self.request_url_rewrite = request_url_rewrite
        if browser_cache_rules is not None:
            self.browser_cache_rules = browser_cache_rules
        if access_area_filter is not None:
            self.access_area_filter = access_area_filter

    @property
    def business_type(self):
        """Gets the business_type of this Configs.

        业务类型： - web：网站加速； - download：文件下载加速； - video：点播加速。  > 暂不支持“全站加速”变更为其它业务类型。

        :return: The business_type of this Configs.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        """Sets the business_type of this Configs.

        业务类型： - web：网站加速； - download：文件下载加速； - video：点播加速。  > 暂不支持“全站加速”变更为其它业务类型。

        :param business_type: The business_type of this Configs.
        :type business_type: str
        """
        self._business_type = business_type

    @property
    def service_area(self):
        """Gets the service_area of this Configs.

        服务区域： - mainland_china：中国大陆； - global：全球； - outside_mainland_china：中国大陆境外。  > 暂不支持“中国大陆”与“中国大陆境外”互相直接切换。

        :return: The service_area of this Configs.
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        """Sets the service_area of this Configs.

        服务区域： - mainland_china：中国大陆； - global：全球； - outside_mainland_china：中国大陆境外。  > 暂不支持“中国大陆”与“中国大陆境外”互相直接切换。

        :param service_area: The service_area of this Configs.
        :type service_area: str
        """
        self._service_area = service_area

    @property
    def remark(self):
        """Gets the remark of this Configs.

        给域名添加备注，字符长度范围0-200。

        :return: The remark of this Configs.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this Configs.

        给域名添加备注，字符长度范围0-200。

        :param remark: The remark of this Configs.
        :type remark: str
        """
        self._remark = remark

    @property
    def origin_request_header(self):
        """Gets the origin_request_header of this Configs.

        回源请求头改写 该功能将覆盖原有配置（清空之前的配置），在使用此接口时，请上传全量头部信息。

        :return: The origin_request_header of this Configs.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.OriginRequestHeader`]
        """
        return self._origin_request_header

    @origin_request_header.setter
    def origin_request_header(self, origin_request_header):
        """Sets the origin_request_header of this Configs.

        回源请求头改写 该功能将覆盖原有配置（清空之前的配置），在使用此接口时，请上传全量头部信息。

        :param origin_request_header: The origin_request_header of this Configs.
        :type origin_request_header: list[:class:`huaweicloudsdkcdn.v2.OriginRequestHeader`]
        """
        self._origin_request_header = origin_request_header

    @property
    def http_response_header(self):
        """Gets the http_response_header of this Configs.

        http header配置 该功能将覆盖原有配置（清空之前的配置），在使用此接口时，请上传全量头部信息。

        :return: The http_response_header of this Configs.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.HttpResponseHeader`]
        """
        return self._http_response_header

    @http_response_header.setter
    def http_response_header(self, http_response_header):
        """Sets the http_response_header of this Configs.

        http header配置 该功能将覆盖原有配置（清空之前的配置），在使用此接口时，请上传全量头部信息。

        :param http_response_header: The http_response_header of this Configs.
        :type http_response_header: list[:class:`huaweicloudsdkcdn.v2.HttpResponseHeader`]
        """
        self._http_response_header = http_response_header

    @property
    def url_auth(self):
        """Gets the url_auth of this Configs.

        :return: The url_auth of this Configs.
        :rtype: :class:`huaweicloudsdkcdn.v2.UrlAuth`
        """
        return self._url_auth

    @url_auth.setter
    def url_auth(self, url_auth):
        """Sets the url_auth of this Configs.

        :param url_auth: The url_auth of this Configs.
        :type url_auth: :class:`huaweicloudsdkcdn.v2.UrlAuth`
        """
        self._url_auth = url_auth

    @property
    def https(self):
        """Gets the https of this Configs.

        :return: The https of this Configs.
        :rtype: :class:`huaweicloudsdkcdn.v2.HttpPutBody`
        """
        return self._https

    @https.setter
    def https(self, https):
        """Sets the https of this Configs.

        :param https: The https of this Configs.
        :type https: :class:`huaweicloudsdkcdn.v2.HttpPutBody`
        """
        self._https = https

    @property
    def sources(self):
        """Gets the sources of this Configs.

        源站配置。

        :return: The sources of this Configs.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.SourcesConfig`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this Configs.

        源站配置。

        :param sources: The sources of this Configs.
        :type sources: list[:class:`huaweicloudsdkcdn.v2.SourcesConfig`]
        """
        self._sources = sources

    @property
    def origin_protocol(self):
        """Gets the origin_protocol of this Configs.

        回源协议，follow：协议跟随回源，http：HTTP回源(默认)，https：https回源。

        :return: The origin_protocol of this Configs.
        :rtype: str
        """
        return self._origin_protocol

    @origin_protocol.setter
    def origin_protocol(self, origin_protocol):
        """Sets the origin_protocol of this Configs.

        回源协议，follow：协议跟随回源，http：HTTP回源(默认)，https：https回源。

        :param origin_protocol: The origin_protocol of this Configs.
        :type origin_protocol: str
        """
        self._origin_protocol = origin_protocol

    @property
    def origin_follow302_status(self):
        """Gets the origin_follow302_status of this Configs.

        回源跟随，on：开启，off：关闭。

        :return: The origin_follow302_status of this Configs.
        :rtype: str
        """
        return self._origin_follow302_status

    @origin_follow302_status.setter
    def origin_follow302_status(self, origin_follow302_status):
        """Sets the origin_follow302_status of this Configs.

        回源跟随，on：开启，off：关闭。

        :param origin_follow302_status: The origin_follow302_status of this Configs.
        :type origin_follow302_status: str
        """
        self._origin_follow302_status = origin_follow302_status

    @property
    def cache_rules(self):
        """Gets the cache_rules of this Configs.

        缓存规则。

        :return: The cache_rules of this Configs.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.CacheRules`]
        """
        return self._cache_rules

    @cache_rules.setter
    def cache_rules(self, cache_rules):
        """Sets the cache_rules of this Configs.

        缓存规则。

        :param cache_rules: The cache_rules of this Configs.
        :type cache_rules: list[:class:`huaweicloudsdkcdn.v2.CacheRules`]
        """
        self._cache_rules = cache_rules

    @property
    def ip_filter(self):
        """Gets the ip_filter of this Configs.

        :return: The ip_filter of this Configs.
        :rtype: :class:`huaweicloudsdkcdn.v2.IpFilter`
        """
        return self._ip_filter

    @ip_filter.setter
    def ip_filter(self, ip_filter):
        """Sets the ip_filter of this Configs.

        :param ip_filter: The ip_filter of this Configs.
        :type ip_filter: :class:`huaweicloudsdkcdn.v2.IpFilter`
        """
        self._ip_filter = ip_filter

    @property
    def referer(self):
        """Gets the referer of this Configs.

        :return: The referer of this Configs.
        :rtype: :class:`huaweicloudsdkcdn.v2.RefererConfig`
        """
        return self._referer

    @referer.setter
    def referer(self, referer):
        """Sets the referer of this Configs.

        :param referer: The referer of this Configs.
        :type referer: :class:`huaweicloudsdkcdn.v2.RefererConfig`
        """
        self._referer = referer

    @property
    def force_redirect(self):
        """Gets the force_redirect of this Configs.

        :return: The force_redirect of this Configs.
        :rtype: :class:`huaweicloudsdkcdn.v2.ForceRedirectConfig`
        """
        return self._force_redirect

    @force_redirect.setter
    def force_redirect(self, force_redirect):
        """Sets the force_redirect of this Configs.

        :param force_redirect: The force_redirect of this Configs.
        :type force_redirect: :class:`huaweicloudsdkcdn.v2.ForceRedirectConfig`
        """
        self._force_redirect = force_redirect

    @property
    def compress(self):
        """Gets the compress of this Configs.

        :return: The compress of this Configs.
        :rtype: :class:`huaweicloudsdkcdn.v2.Compress`
        """
        return self._compress

    @compress.setter
    def compress(self, compress):
        """Sets the compress of this Configs.

        :param compress: The compress of this Configs.
        :type compress: :class:`huaweicloudsdkcdn.v2.Compress`
        """
        self._compress = compress

    @property
    def cache_url_parameter_filter(self):
        """Gets the cache_url_parameter_filter of this Configs.

        :return: The cache_url_parameter_filter of this Configs.
        :rtype: :class:`huaweicloudsdkcdn.v2.CacheUrlParameterFilter`
        """
        return self._cache_url_parameter_filter

    @cache_url_parameter_filter.setter
    def cache_url_parameter_filter(self, cache_url_parameter_filter):
        """Sets the cache_url_parameter_filter of this Configs.

        :param cache_url_parameter_filter: The cache_url_parameter_filter of this Configs.
        :type cache_url_parameter_filter: :class:`huaweicloudsdkcdn.v2.CacheUrlParameterFilter`
        """
        self._cache_url_parameter_filter = cache_url_parameter_filter

    @property
    def ipv6_accelerate(self):
        """Gets the ipv6_accelerate of this Configs.

        ipv6设置，1：打开；0：关闭。

        :return: The ipv6_accelerate of this Configs.
        :rtype: int
        """
        return self._ipv6_accelerate

    @ipv6_accelerate.setter
    def ipv6_accelerate(self, ipv6_accelerate):
        """Sets the ipv6_accelerate of this Configs.

        ipv6设置，1：打开；0：关闭。

        :param ipv6_accelerate: The ipv6_accelerate of this Configs.
        :type ipv6_accelerate: int
        """
        self._ipv6_accelerate = ipv6_accelerate

    @property
    def error_code_cache(self):
        """Gets the error_code_cache of this Configs.

        状态码缓存时间。

        :return: The error_code_cache of this Configs.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.ErrorCodeCache`]
        """
        return self._error_code_cache

    @error_code_cache.setter
    def error_code_cache(self, error_code_cache):
        """Sets the error_code_cache of this Configs.

        状态码缓存时间。

        :param error_code_cache: The error_code_cache of this Configs.
        :type error_code_cache: list[:class:`huaweicloudsdkcdn.v2.ErrorCodeCache`]
        """
        self._error_code_cache = error_code_cache

    @property
    def origin_range_status(self):
        """Gets the origin_range_status of this Configs.

        Range回源，即分片回源，开启: on，关闭: off。  > 开启Range回源的前提是您的源站支持Range请求，即HTTP请求头中包含Range字段，否则可能导致回源失败。

        :return: The origin_range_status of this Configs.
        :rtype: str
        """
        return self._origin_range_status

    @origin_range_status.setter
    def origin_range_status(self, origin_range_status):
        """Sets the origin_range_status of this Configs.

        Range回源，即分片回源，开启: on，关闭: off。  > 开启Range回源的前提是您的源站支持Range请求，即HTTP请求头中包含Range字段，否则可能导致回源失败。

        :param origin_range_status: The origin_range_status of this Configs.
        :type origin_range_status: str
        """
        self._origin_range_status = origin_range_status

    @property
    def user_agent_filter(self):
        """Gets the user_agent_filter of this Configs.

        :return: The user_agent_filter of this Configs.
        :rtype: :class:`huaweicloudsdkcdn.v2.UserAgentFilter`
        """
        return self._user_agent_filter

    @user_agent_filter.setter
    def user_agent_filter(self, user_agent_filter):
        """Sets the user_agent_filter of this Configs.

        :param user_agent_filter: The user_agent_filter of this Configs.
        :type user_agent_filter: :class:`huaweicloudsdkcdn.v2.UserAgentFilter`
        """
        self._user_agent_filter = user_agent_filter

    @property
    def origin_request_url_rewrite(self):
        """Gets the origin_request_url_rewrite of this Configs.

        改写回源URL，最多配置20条。

        :return: The origin_request_url_rewrite of this Configs.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.OriginRequestUrlRewrite`]
        """
        return self._origin_request_url_rewrite

    @origin_request_url_rewrite.setter
    def origin_request_url_rewrite(self, origin_request_url_rewrite):
        """Sets the origin_request_url_rewrite of this Configs.

        改写回源URL，最多配置20条。

        :param origin_request_url_rewrite: The origin_request_url_rewrite of this Configs.
        :type origin_request_url_rewrite: list[:class:`huaweicloudsdkcdn.v2.OriginRequestUrlRewrite`]
        """
        self._origin_request_url_rewrite = origin_request_url_rewrite

    @property
    def flexible_origin(self):
        """Gets the flexible_origin of this Configs.

        高级回源，最多配置20条。

        :return: The flexible_origin of this Configs.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.FlexibleOrigins`]
        """
        return self._flexible_origin

    @flexible_origin.setter
    def flexible_origin(self, flexible_origin):
        """Sets the flexible_origin of this Configs.

        高级回源，最多配置20条。

        :param flexible_origin: The flexible_origin of this Configs.
        :type flexible_origin: list[:class:`huaweicloudsdkcdn.v2.FlexibleOrigins`]
        """
        self._flexible_origin = flexible_origin

    @property
    def slice_etag_status(self):
        """Gets the slice_etag_status of this Configs.

        回源是否校验ETag，on：开启，off：关闭。

        :return: The slice_etag_status of this Configs.
        :rtype: str
        """
        return self._slice_etag_status

    @slice_etag_status.setter
    def slice_etag_status(self, slice_etag_status):
        """Sets the slice_etag_status of this Configs.

        回源是否校验ETag，on：开启，off：关闭。

        :param slice_etag_status: The slice_etag_status of this Configs.
        :type slice_etag_status: str
        """
        self._slice_etag_status = slice_etag_status

    @property
    def origin_receive_timeout(self):
        """Gets the origin_receive_timeout of this Configs.

        回源超时时间，范围:5-60，单位：秒。

        :return: The origin_receive_timeout of this Configs.
        :rtype: int
        """
        return self._origin_receive_timeout

    @origin_receive_timeout.setter
    def origin_receive_timeout(self, origin_receive_timeout):
        """Sets the origin_receive_timeout of this Configs.

        回源超时时间，范围:5-60，单位：秒。

        :param origin_receive_timeout: The origin_receive_timeout of this Configs.
        :type origin_receive_timeout: int
        """
        self._origin_receive_timeout = origin_receive_timeout

    @property
    def remote_auth(self):
        """Gets the remote_auth of this Configs.

        :return: The remote_auth of this Configs.
        :rtype: :class:`huaweicloudsdkcdn.v2.CommonRemoteAuth`
        """
        return self._remote_auth

    @remote_auth.setter
    def remote_auth(self, remote_auth):
        """Sets the remote_auth of this Configs.

        :param remote_auth: The remote_auth of this Configs.
        :type remote_auth: :class:`huaweicloudsdkcdn.v2.CommonRemoteAuth`
        """
        self._remote_auth = remote_auth

    @property
    def websocket(self):
        """Gets the websocket of this Configs.

        :return: The websocket of this Configs.
        :rtype: :class:`huaweicloudsdkcdn.v2.WebSocketSeek`
        """
        return self._websocket

    @websocket.setter
    def websocket(self, websocket):
        """Sets the websocket of this Configs.

        :param websocket: The websocket of this Configs.
        :type websocket: :class:`huaweicloudsdkcdn.v2.WebSocketSeek`
        """
        self._websocket = websocket

    @property
    def video_seek(self):
        """Gets the video_seek of this Configs.

        :return: The video_seek of this Configs.
        :rtype: :class:`huaweicloudsdkcdn.v2.VideoSeek`
        """
        return self._video_seek

    @video_seek.setter
    def video_seek(self, video_seek):
        """Sets the video_seek of this Configs.

        :param video_seek: The video_seek of this Configs.
        :type video_seek: :class:`huaweicloudsdkcdn.v2.VideoSeek`
        """
        self._video_seek = video_seek

    @property
    def request_limit_rules(self):
        """Gets the request_limit_rules of this Configs.

        请求限速配置。

        :return: The request_limit_rules of this Configs.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.RequestLimitRules`]
        """
        return self._request_limit_rules

    @request_limit_rules.setter
    def request_limit_rules(self, request_limit_rules):
        """Sets the request_limit_rules of this Configs.

        请求限速配置。

        :param request_limit_rules: The request_limit_rules of this Configs.
        :type request_limit_rules: list[:class:`huaweicloudsdkcdn.v2.RequestLimitRules`]
        """
        self._request_limit_rules = request_limit_rules

    @property
    def ip_frequency_limit(self):
        """Gets the ip_frequency_limit of this Configs.

        :return: The ip_frequency_limit of this Configs.
        :rtype: :class:`huaweicloudsdkcdn.v2.IpFrequencyLimit`
        """
        return self._ip_frequency_limit

    @ip_frequency_limit.setter
    def ip_frequency_limit(self, ip_frequency_limit):
        """Sets the ip_frequency_limit of this Configs.

        :param ip_frequency_limit: The ip_frequency_limit of this Configs.
        :type ip_frequency_limit: :class:`huaweicloudsdkcdn.v2.IpFrequencyLimit`
        """
        self._ip_frequency_limit = ip_frequency_limit

    @property
    def hsts(self):
        """Gets the hsts of this Configs.

        :return: The hsts of this Configs.
        :rtype: :class:`huaweicloudsdkcdn.v2.Hsts`
        """
        return self._hsts

    @hsts.setter
    def hsts(self, hsts):
        """Sets the hsts of this Configs.

        :param hsts: The hsts of this Configs.
        :type hsts: :class:`huaweicloudsdkcdn.v2.Hsts`
        """
        self._hsts = hsts

    @property
    def quic(self):
        """Gets the quic of this Configs.

        :return: The quic of this Configs.
        :rtype: :class:`huaweicloudsdkcdn.v2.Quic`
        """
        return self._quic

    @quic.setter
    def quic(self, quic):
        """Sets the quic of this Configs.

        :param quic: The quic of this Configs.
        :type quic: :class:`huaweicloudsdkcdn.v2.Quic`
        """
        self._quic = quic

    @property
    def error_code_redirect_rules(self):
        """Gets the error_code_redirect_rules of this Configs.

        自定义错误页面。

        :return: The error_code_redirect_rules of this Configs.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.ErrorCodeRedirectRules`]
        """
        return self._error_code_redirect_rules

    @error_code_redirect_rules.setter
    def error_code_redirect_rules(self, error_code_redirect_rules):
        """Sets the error_code_redirect_rules of this Configs.

        自定义错误页面。

        :param error_code_redirect_rules: The error_code_redirect_rules of this Configs.
        :type error_code_redirect_rules: list[:class:`huaweicloudsdkcdn.v2.ErrorCodeRedirectRules`]
        """
        self._error_code_redirect_rules = error_code_redirect_rules

    @property
    def sni(self):
        """Gets the sni of this Configs.

        :return: The sni of this Configs.
        :rtype: :class:`huaweicloudsdkcdn.v2.Sni`
        """
        return self._sni

    @sni.setter
    def sni(self, sni):
        """Sets the sni of this Configs.

        :param sni: The sni of this Configs.
        :type sni: :class:`huaweicloudsdkcdn.v2.Sni`
        """
        self._sni = sni

    @property
    def request_url_rewrite(self):
        """Gets the request_url_rewrite of this Configs.

        访问URL重写。

        :return: The request_url_rewrite of this Configs.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.RequestUrlRewrite`]
        """
        return self._request_url_rewrite

    @request_url_rewrite.setter
    def request_url_rewrite(self, request_url_rewrite):
        """Sets the request_url_rewrite of this Configs.

        访问URL重写。

        :param request_url_rewrite: The request_url_rewrite of this Configs.
        :type request_url_rewrite: list[:class:`huaweicloudsdkcdn.v2.RequestUrlRewrite`]
        """
        self._request_url_rewrite = request_url_rewrite

    @property
    def browser_cache_rules(self):
        """Gets the browser_cache_rules of this Configs.

        浏览器缓存过期时间。

        :return: The browser_cache_rules of this Configs.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.BrowserCacheRules`]
        """
        return self._browser_cache_rules

    @browser_cache_rules.setter
    def browser_cache_rules(self, browser_cache_rules):
        """Sets the browser_cache_rules of this Configs.

        浏览器缓存过期时间。

        :param browser_cache_rules: The browser_cache_rules of this Configs.
        :type browser_cache_rules: list[:class:`huaweicloudsdkcdn.v2.BrowserCacheRules`]
        """
        self._browser_cache_rules = browser_cache_rules

    @property
    def access_area_filter(self):
        """Gets the access_area_filter of this Configs.

        :return: The access_area_filter of this Configs.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.AccessAreaFilter`]
        """
        return self._access_area_filter

    @access_area_filter.setter
    def access_area_filter(self, access_area_filter):
        """Sets the access_area_filter of this Configs.

        :param access_area_filter: The access_area_filter of this Configs.
        :type access_area_filter: list[:class:`huaweicloudsdkcdn.v2.AccessAreaFilter`]
        """
        self._access_area_filter = access_area_filter

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
