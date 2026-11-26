# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCopyConfigs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_domain': 'str',
        'source_domain': 'str',
        'config_list': 'list[str]'
    }

    attribute_map = {
        'target_domain': 'target_domain',
        'source_domain': 'source_domain',
        'config_list': 'config_list'
    }

    def __init__(self, target_domain=None, source_domain=None, config_list=None):
        r"""BatchCopyConfigs

        The model defined in huaweicloud sdk

        :param target_domain: **参数解释：** 目标域名，即需要复制配置的域名，支持配置多个域名 **约束限制：** - 多个域名以“,”分隔 - 最多配置10个域名 - 域名状态为已开启、已停用、审核未通过且未被封禁和未被锁定时，才可以使用复制配置功能  **取值范围：** 不涉及 **默认取值：** 不涉及
        :type target_domain: str
        :param source_domain: **参数解释：** 原域名，将该域名的配置复制给目标域名 **约束限制：** 域名状态为已开启、已停用、审核未通过且未被封禁时，才可以使用复制配置功能 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type source_domain: str
        :param config_list: **参数解释：** 需要复制的域名配置项 **约束限制：** 多个配置项以“,”分隔 **取值范围：** - origin_request_header: 回源请求头 - http_response_header: HTTP header配置 - url_auth: URL鉴权配置 - user_agent_black_and_white_list: User-Agent黑白名单 - ipv6_accelerate: IPv6开关 - range_status: Range回源 - cache_rules: 缓存规则 - follow_302_status: 回源跟随 - sources: 源站配置 - compress: 智能压缩 - referer: 防盗链 - ip_black_and_white_list: IP黑白名单 - browser_cacheRules: 浏览器缓存过期时间 - cache_valid_error_code: 状态码缓存时间 - access_area_filter: 区域访问控制 - http2_status: HTTP/2 - ocsp_stapling_status: OCSP Stapling - force_redirect: 强制跳转 - https_tls_version: TLS版本与加密套件配置 - rules: 规则引擎 - error_code_redirect_rules: 自定义错误页面配置  **默认取值：** 不涉及
        :type config_list: list[str]
        """
        
        

        self._target_domain = None
        self._source_domain = None
        self._config_list = None
        self.discriminator = None

        self.target_domain = target_domain
        self.source_domain = source_domain
        self.config_list = config_list

    @property
    def target_domain(self):
        r"""Gets the target_domain of this BatchCopyConfigs.

        **参数解释：** 目标域名，即需要复制配置的域名，支持配置多个域名 **约束限制：** - 多个域名以“,”分隔 - 最多配置10个域名 - 域名状态为已开启、已停用、审核未通过且未被封禁和未被锁定时，才可以使用复制配置功能  **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The target_domain of this BatchCopyConfigs.
        :rtype: str
        """
        return self._target_domain

    @target_domain.setter
    def target_domain(self, target_domain):
        r"""Sets the target_domain of this BatchCopyConfigs.

        **参数解释：** 目标域名，即需要复制配置的域名，支持配置多个域名 **约束限制：** - 多个域名以“,”分隔 - 最多配置10个域名 - 域名状态为已开启、已停用、审核未通过且未被封禁和未被锁定时，才可以使用复制配置功能  **取值范围：** 不涉及 **默认取值：** 不涉及

        :param target_domain: The target_domain of this BatchCopyConfigs.
        :type target_domain: str
        """
        self._target_domain = target_domain

    @property
    def source_domain(self):
        r"""Gets the source_domain of this BatchCopyConfigs.

        **参数解释：** 原域名，将该域名的配置复制给目标域名 **约束限制：** 域名状态为已开启、已停用、审核未通过且未被封禁时，才可以使用复制配置功能 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The source_domain of this BatchCopyConfigs.
        :rtype: str
        """
        return self._source_domain

    @source_domain.setter
    def source_domain(self, source_domain):
        r"""Sets the source_domain of this BatchCopyConfigs.

        **参数解释：** 原域名，将该域名的配置复制给目标域名 **约束限制：** 域名状态为已开启、已停用、审核未通过且未被封禁时，才可以使用复制配置功能 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param source_domain: The source_domain of this BatchCopyConfigs.
        :type source_domain: str
        """
        self._source_domain = source_domain

    @property
    def config_list(self):
        r"""Gets the config_list of this BatchCopyConfigs.

        **参数解释：** 需要复制的域名配置项 **约束限制：** 多个配置项以“,”分隔 **取值范围：** - origin_request_header: 回源请求头 - http_response_header: HTTP header配置 - url_auth: URL鉴权配置 - user_agent_black_and_white_list: User-Agent黑白名单 - ipv6_accelerate: IPv6开关 - range_status: Range回源 - cache_rules: 缓存规则 - follow_302_status: 回源跟随 - sources: 源站配置 - compress: 智能压缩 - referer: 防盗链 - ip_black_and_white_list: IP黑白名单 - browser_cacheRules: 浏览器缓存过期时间 - cache_valid_error_code: 状态码缓存时间 - access_area_filter: 区域访问控制 - http2_status: HTTP/2 - ocsp_stapling_status: OCSP Stapling - force_redirect: 强制跳转 - https_tls_version: TLS版本与加密套件配置 - rules: 规则引擎 - error_code_redirect_rules: 自定义错误页面配置  **默认取值：** 不涉及

        :return: The config_list of this BatchCopyConfigs.
        :rtype: list[str]
        """
        return self._config_list

    @config_list.setter
    def config_list(self, config_list):
        r"""Sets the config_list of this BatchCopyConfigs.

        **参数解释：** 需要复制的域名配置项 **约束限制：** 多个配置项以“,”分隔 **取值范围：** - origin_request_header: 回源请求头 - http_response_header: HTTP header配置 - url_auth: URL鉴权配置 - user_agent_black_and_white_list: User-Agent黑白名单 - ipv6_accelerate: IPv6开关 - range_status: Range回源 - cache_rules: 缓存规则 - follow_302_status: 回源跟随 - sources: 源站配置 - compress: 智能压缩 - referer: 防盗链 - ip_black_and_white_list: IP黑白名单 - browser_cacheRules: 浏览器缓存过期时间 - cache_valid_error_code: 状态码缓存时间 - access_area_filter: 区域访问控制 - http2_status: HTTP/2 - ocsp_stapling_status: OCSP Stapling - force_redirect: 强制跳转 - https_tls_version: TLS版本与加密套件配置 - rules: 规则引擎 - error_code_redirect_rules: 自定义错误页面配置  **默认取值：** 不涉及

        :param config_list: The config_list of this BatchCopyConfigs.
        :type config_list: list[str]
        """
        self._config_list = config_list

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchCopyConfigs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
