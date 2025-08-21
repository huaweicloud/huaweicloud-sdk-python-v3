# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateConfigs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'http_response_header': 'list[HttpResponseHeader]',
        'cache_rules': 'list[CacheRules]',
        'origin_follow302_status': 'str',
        'compress': 'Compress',
        'origin_range_status': 'str',
        'ip_filter': 'IpFilter',
        'referer': 'RefererConfig',
        'user_agent_filter': 'UserAgentFilter',
        'flow_limit_strategy': 'list[FlowLimitStrategy]'
    }

    attribute_map = {
        'http_response_header': 'http_response_header',
        'cache_rules': 'cache_rules',
        'origin_follow302_status': 'origin_follow302_status',
        'compress': 'compress',
        'origin_range_status': 'origin_range_status',
        'ip_filter': 'ip_filter',
        'referer': 'referer',
        'user_agent_filter': 'user_agent_filter',
        'flow_limit_strategy': 'flow_limit_strategy'
    }

    def __init__(self, http_response_header=None, cache_rules=None, origin_follow302_status=None, compress=None, origin_range_status=None, ip_filter=None, referer=None, user_agent_filter=None, flow_limit_strategy=None):
        r"""TemplateConfigs

        The model defined in huaweicloud sdk

        :param http_response_header: 
        :type http_response_header: list[:class:`huaweicloudsdkcdn.v2.HttpResponseHeader`]
        :param cache_rules: 
        :type cache_rules: list[:class:`huaweicloudsdkcdn.v2.CacheRules`]
        :param origin_follow302_status: **参数解释：** 开启回源跟随，当源站地址因业务需求做了301/302 重定向，CDN节点会先跳转到301/302对应地址获取资源，缓存后再返回给用户 **约束限制：** 不涉及 **取值范围：** - on: 开启 - off: 关闭 **默认取值：** 不涉及
        :type origin_follow302_status: str
        :param compress: 
        :type compress: :class:`huaweicloudsdkcdn.v2.Compress`
        :param origin_range_status: **参数解释：** Range回源，开启后，源站在收到CDN节点回源请求时，根据HTTP请求头中的Range信息返回指定范围的数据给CDN节点 **约束限制：** 开启Range回源的前提是您的源站支持Range请求，即HTTP请求头中包含Range字段，否则可能导致回源失败 **取值范围：** - on: 开启 - off: 关闭 **默认取值：** 不涉及
        :type origin_range_status: str
        :param ip_filter: 
        :type ip_filter: :class:`huaweicloudsdkcdn.v2.IpFilter`
        :param referer: 
        :type referer: :class:`huaweicloudsdkcdn.v2.RefererConfig`
        :param user_agent_filter: 
        :type user_agent_filter: :class:`huaweicloudsdkcdn.v2.UserAgentFilter`
        :param flow_limit_strategy: **参数解释：** 设置用量封顶阈值，当实际用量大于阈值时停用域名，有效预防流量盗刷或恶意攻击带来的高额账单。  &gt; 由于监控数据存在时延，域名将在用量达到阈值后的10分钟左右被停用  **约束限制：** 不涉及
        :type flow_limit_strategy: list[:class:`huaweicloudsdkcdn.v2.FlowLimitStrategy`]
        """
        
        

        self._http_response_header = None
        self._cache_rules = None
        self._origin_follow302_status = None
        self._compress = None
        self._origin_range_status = None
        self._ip_filter = None
        self._referer = None
        self._user_agent_filter = None
        self._flow_limit_strategy = None
        self.discriminator = None

        if http_response_header is not None:
            self.http_response_header = http_response_header
        if cache_rules is not None:
            self.cache_rules = cache_rules
        if origin_follow302_status is not None:
            self.origin_follow302_status = origin_follow302_status
        if compress is not None:
            self.compress = compress
        if origin_range_status is not None:
            self.origin_range_status = origin_range_status
        if ip_filter is not None:
            self.ip_filter = ip_filter
        if referer is not None:
            self.referer = referer
        if user_agent_filter is not None:
            self.user_agent_filter = user_agent_filter
        if flow_limit_strategy is not None:
            self.flow_limit_strategy = flow_limit_strategy

    @property
    def http_response_header(self):
        r"""Gets the http_response_header of this TemplateConfigs.

        :return: The http_response_header of this TemplateConfigs.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.HttpResponseHeader`]
        """
        return self._http_response_header

    @http_response_header.setter
    def http_response_header(self, http_response_header):
        r"""Sets the http_response_header of this TemplateConfigs.

        :param http_response_header: The http_response_header of this TemplateConfigs.
        :type http_response_header: list[:class:`huaweicloudsdkcdn.v2.HttpResponseHeader`]
        """
        self._http_response_header = http_response_header

    @property
    def cache_rules(self):
        r"""Gets the cache_rules of this TemplateConfigs.

        :return: The cache_rules of this TemplateConfigs.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.CacheRules`]
        """
        return self._cache_rules

    @cache_rules.setter
    def cache_rules(self, cache_rules):
        r"""Sets the cache_rules of this TemplateConfigs.

        :param cache_rules: The cache_rules of this TemplateConfigs.
        :type cache_rules: list[:class:`huaweicloudsdkcdn.v2.CacheRules`]
        """
        self._cache_rules = cache_rules

    @property
    def origin_follow302_status(self):
        r"""Gets the origin_follow302_status of this TemplateConfigs.

        **参数解释：** 开启回源跟随，当源站地址因业务需求做了301/302 重定向，CDN节点会先跳转到301/302对应地址获取资源，缓存后再返回给用户 **约束限制：** 不涉及 **取值范围：** - on: 开启 - off: 关闭 **默认取值：** 不涉及

        :return: The origin_follow302_status of this TemplateConfigs.
        :rtype: str
        """
        return self._origin_follow302_status

    @origin_follow302_status.setter
    def origin_follow302_status(self, origin_follow302_status):
        r"""Sets the origin_follow302_status of this TemplateConfigs.

        **参数解释：** 开启回源跟随，当源站地址因业务需求做了301/302 重定向，CDN节点会先跳转到301/302对应地址获取资源，缓存后再返回给用户 **约束限制：** 不涉及 **取值范围：** - on: 开启 - off: 关闭 **默认取值：** 不涉及

        :param origin_follow302_status: The origin_follow302_status of this TemplateConfigs.
        :type origin_follow302_status: str
        """
        self._origin_follow302_status = origin_follow302_status

    @property
    def compress(self):
        r"""Gets the compress of this TemplateConfigs.

        :return: The compress of this TemplateConfigs.
        :rtype: :class:`huaweicloudsdkcdn.v2.Compress`
        """
        return self._compress

    @compress.setter
    def compress(self, compress):
        r"""Sets the compress of this TemplateConfigs.

        :param compress: The compress of this TemplateConfigs.
        :type compress: :class:`huaweicloudsdkcdn.v2.Compress`
        """
        self._compress = compress

    @property
    def origin_range_status(self):
        r"""Gets the origin_range_status of this TemplateConfigs.

        **参数解释：** Range回源，开启后，源站在收到CDN节点回源请求时，根据HTTP请求头中的Range信息返回指定范围的数据给CDN节点 **约束限制：** 开启Range回源的前提是您的源站支持Range请求，即HTTP请求头中包含Range字段，否则可能导致回源失败 **取值范围：** - on: 开启 - off: 关闭 **默认取值：** 不涉及

        :return: The origin_range_status of this TemplateConfigs.
        :rtype: str
        """
        return self._origin_range_status

    @origin_range_status.setter
    def origin_range_status(self, origin_range_status):
        r"""Sets the origin_range_status of this TemplateConfigs.

        **参数解释：** Range回源，开启后，源站在收到CDN节点回源请求时，根据HTTP请求头中的Range信息返回指定范围的数据给CDN节点 **约束限制：** 开启Range回源的前提是您的源站支持Range请求，即HTTP请求头中包含Range字段，否则可能导致回源失败 **取值范围：** - on: 开启 - off: 关闭 **默认取值：** 不涉及

        :param origin_range_status: The origin_range_status of this TemplateConfigs.
        :type origin_range_status: str
        """
        self._origin_range_status = origin_range_status

    @property
    def ip_filter(self):
        r"""Gets the ip_filter of this TemplateConfigs.

        :return: The ip_filter of this TemplateConfigs.
        :rtype: :class:`huaweicloudsdkcdn.v2.IpFilter`
        """
        return self._ip_filter

    @ip_filter.setter
    def ip_filter(self, ip_filter):
        r"""Sets the ip_filter of this TemplateConfigs.

        :param ip_filter: The ip_filter of this TemplateConfigs.
        :type ip_filter: :class:`huaweicloudsdkcdn.v2.IpFilter`
        """
        self._ip_filter = ip_filter

    @property
    def referer(self):
        r"""Gets the referer of this TemplateConfigs.

        :return: The referer of this TemplateConfigs.
        :rtype: :class:`huaweicloudsdkcdn.v2.RefererConfig`
        """
        return self._referer

    @referer.setter
    def referer(self, referer):
        r"""Sets the referer of this TemplateConfigs.

        :param referer: The referer of this TemplateConfigs.
        :type referer: :class:`huaweicloudsdkcdn.v2.RefererConfig`
        """
        self._referer = referer

    @property
    def user_agent_filter(self):
        r"""Gets the user_agent_filter of this TemplateConfigs.

        :return: The user_agent_filter of this TemplateConfigs.
        :rtype: :class:`huaweicloudsdkcdn.v2.UserAgentFilter`
        """
        return self._user_agent_filter

    @user_agent_filter.setter
    def user_agent_filter(self, user_agent_filter):
        r"""Sets the user_agent_filter of this TemplateConfigs.

        :param user_agent_filter: The user_agent_filter of this TemplateConfigs.
        :type user_agent_filter: :class:`huaweicloudsdkcdn.v2.UserAgentFilter`
        """
        self._user_agent_filter = user_agent_filter

    @property
    def flow_limit_strategy(self):
        r"""Gets the flow_limit_strategy of this TemplateConfigs.

        **参数解释：** 设置用量封顶阈值，当实际用量大于阈值时停用域名，有效预防流量盗刷或恶意攻击带来的高额账单。  > 由于监控数据存在时延，域名将在用量达到阈值后的10分钟左右被停用  **约束限制：** 不涉及

        :return: The flow_limit_strategy of this TemplateConfigs.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.FlowLimitStrategy`]
        """
        return self._flow_limit_strategy

    @flow_limit_strategy.setter
    def flow_limit_strategy(self, flow_limit_strategy):
        r"""Sets the flow_limit_strategy of this TemplateConfigs.

        **参数解释：** 设置用量封顶阈值，当实际用量大于阈值时停用域名，有效预防流量盗刷或恶意攻击带来的高额账单。  > 由于监控数据存在时延，域名将在用量达到阈值后的10分钟左右被停用  **约束限制：** 不涉及

        :param flow_limit_strategy: The flow_limit_strategy of this TemplateConfigs.
        :type flow_limit_strategy: list[:class:`huaweicloudsdkcdn.v2.FlowLimitStrategy`]
        """
        self._flow_limit_strategy = flow_limit_strategy

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
        if not isinstance(other, TemplateConfigs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
